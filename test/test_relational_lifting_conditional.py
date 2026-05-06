import unittest
import ir
import asg
from optimizer import RelationalLiftingOptimizer
from metadata_registry import MetadataRegistry
from emitter import PostgresEmitter

class TestRelationalLiftingConditional(unittest.TestCase):
    def test_lift_conditional_sum(self):
        # 1. Setup metadata
        registry = MetadataRegistry()
        car_master = asg.MasterFile(name="CAR", segments=[
            asg.Segment(name="ORIGIN", fields=[
                asg.Field(name="COUNTRY"),
                asg.Field(name="SALES", format="D12.2")
            ])
        ])
        registry.register_master_file(car_master)

        # 2. Construct CFG for procedural conditional loop:
        # -REPEAT LBL 10 TIMES
        # -READ CAR &COUNTRY &SALES
        # -IF &COUNTRY EQ 'ENGLAND' THEN GOTO ACC;
        # -GOTO LBL;
        # -ACC
        # -SET &TOT_SALES = &TOT_SALES + &SALES
        # LBL

        cfg = ir.ControlFlowGraph()

        # Entry
        entry = ir.BasicBlock(name="ENTRY")
        entry.add_instruction(ir.Assign(target="TOT_SALES_0", source=asg.Literal(0)))
        entry.add_instruction(ir.Assign(target="I_0", source=asg.Literal(1)))
        entry.add_instruction(ir.Jump(target="LOOP_HEADER_LBL"))
        cfg.add_block(entry)

        # Header
        header = ir.BasicBlock(name="LOOP_HEADER_LBL")
        header.add_instruction(ir.Phi(target="TOT_SALES_1", sources=["TOT_SALES_0", "TOT_SALES_2"]))
        header.add_instruction(ir.Phi(target="I_1", sources=["I_0", "I_2"]))
        header.add_instruction(ir.Branch(
            condition=asg.BinaryOperation(left=asg.AmperVar(name="I_1"), operator="LE", right=asg.Literal(10)),
            true_target="BODY",
            false_target="EXIT"
        ))
        cfg.add_block(header)

        # Body (Decision point)
        body = ir.BasicBlock(name="BODY")
        body.add_instruction(ir.Read(filename="CAR", variables=["COUNTRY_1", "SALES_1"]))
        body.add_instruction(ir.Branch(
            condition=asg.BinaryOperation(left=asg.AmperVar(name="COUNTRY_1"), operator="EQ", right=asg.Literal("ENGLAND")),
            true_target="ACC",
            false_target="LBL"
        ))
        cfg.add_block(body)

        # Accumulator block
        acc_block = ir.BasicBlock(name="ACC")
        acc_block.add_instruction(ir.Assign(
            target="TOT_SALES_3",
            source=asg.BinaryOperation(
                left=asg.AmperVar(name="TOT_SALES_1"),
                operator="+",
                right=asg.AmperVar(name="SALES_1")
            )
        ))
        acc_block.add_instruction(ir.Jump(target="LBL"))
        cfg.add_block(acc_block)

        # Closing
        closing = ir.BasicBlock(name="LBL")
        closing.add_instruction(ir.Phi(target="TOT_SALES_2", sources=["TOT_SALES_1", "TOT_SALES_3"]))
        closing.add_instruction(ir.Assign(
            target="I_2",
            source=asg.BinaryOperation(left=asg.AmperVar(name="I_1"), operator="+", right=asg.Literal(1))
        ))
        closing.add_instruction(ir.Jump(target="LOOP_HEADER_LBL"))
        cfg.add_block(closing)

        # Exit
        exit_block = ir.BasicBlock(name="EXIT")
        cfg.add_block(exit_block)

        cfg.add_edge("ENTRY", "LOOP_HEADER_LBL")
        cfg.add_edge("LOOP_HEADER_LBL", "BODY")
        cfg.add_edge("LOOP_HEADER_LBL", "EXIT")
        cfg.add_edge("BODY", "ACC")
        cfg.add_edge("BODY", "LBL")
        cfg.add_edge("ACC", "LBL")
        cfg.add_edge("LBL", "LOOP_HEADER_LBL")

        cfg.entry_block = entry

        # 3. Run Relational Lifting
        optimizer = RelationalLiftingOptimizer()
        optimizer.lift_data_loops(cfg, registry)

        # 4. Verifications
        self.assertIn("LIFTED_LOOP_HEADER_LBL", cfg.blocks)
        lifted_block = cfg.blocks["LIFTED_LOOP_HEADER_LBL"]

        report_instr = next(i for i in lifted_block.instructions if isinstance(i, ir.Report))

        # Check for SUM verb
        sum_verb = next(c for c in report_instr.components if isinstance(c, asg.VerbCommand) and c.verb == "SUM")

        # TOT_SALES should be a conditional SUM
        tot_sales_field = next(f for f in sum_verb.fields if f.alias == "TOT_SALES")
        self.assertIsInstance(tot_sales_field.name, asg.IfExpression)

        if_expr = tot_sales_field.name
        self.assertIsInstance(if_expr.condition, asg.BinaryOperation)
        self.assertEqual(if_expr.condition.operator, "EQ")
        self.assertEqual(if_expr.condition.left.name, "COUNTRY")
        self.assertEqual(if_expr.condition.right.value, "ENGLAND")
        self.assertEqual(if_expr.then_expr.name, "SALES")
        self.assertEqual(if_expr.else_expr.value, 0)

        # 5. Emit SQL and check for CASE
        emitter = PostgresEmitter(metadata_registry=registry)
        sql = emitter._emit_report(report_instr)
        self.assertIn("SUM((CASE WHEN (COUNTRY = 'ENGLAND') THEN SALES ELSE 0 END)) AS \"TOT_SALES\"", sql)

if __name__ == '__main__':
    unittest.main()

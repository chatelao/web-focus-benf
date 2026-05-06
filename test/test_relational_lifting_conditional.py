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

        # 2. Construct CFG for procedural conditional loop with TWO conditional sums.
        # This prevents the optimizer from lifting the conditions to a global WHERE.
        #
        # -REPEAT LBL 10 TIMES
        # -READ CAR &COUNTRY &SALES
        # -IF &COUNTRY EQ 'ENGLAND' THEN SET &ENG_SALES = &ENG_SALES + &SALES;
        # -IF &COUNTRY EQ 'FRANCE' THEN SET &FRA_SALES = &FRA_SALES + &SALES;
        # -LBL

        cfg = ir.ControlFlowGraph()

        # Entry
        entry = ir.BasicBlock(name="ENTRY")
        entry.add_instruction(ir.Assign(target="ENG_SALES_0", source=asg.Literal(0)))
        entry.add_instruction(ir.Assign(target="FRA_SALES_0", source=asg.Literal(0)))
        entry.add_instruction(ir.Assign(target="I_0", source=asg.Literal(1)))
        entry.add_instruction(ir.Jump(target="LOOP_HEADER_LBL"))
        cfg.add_block(entry)

        # Header
        header = ir.BasicBlock(name="LOOP_HEADER_LBL")
        header.add_instruction(ir.Phi(target="ENG_SALES_1", sources=["ENG_SALES_0", "ENG_SALES_2"]))
        header.add_instruction(ir.Phi(target="FRA_SALES_1", sources=["FRA_SALES_0", "FRA_SALES_2"]))
        header.add_instruction(ir.Phi(target="I_1", sources=["I_0", "I_2"]))
        header.add_instruction(ir.Branch(
            condition=asg.BinaryOperation(left=asg.AmperVar(name="I_1"), operator="LE", right=asg.Literal(10)),
            true_target="BODY",
            false_target="EXIT"
        ))
        cfg.add_block(header)

        # Body (Read)
        body = ir.BasicBlock(name="BODY")
        body.add_instruction(ir.Read(filename="CAR", variables=["COUNTRY_1", "SALES_1"]))
        body.add_instruction(ir.Branch(
            condition=asg.BinaryOperation(left=asg.AmperVar(name="COUNTRY_1"), operator="EQ", right=asg.Literal("ENGLAND")),
            true_target="ACC_ENG",
            false_target="BODY_2"
        ))
        cfg.add_block(body)

        # First Accumulator
        acc_eng = ir.BasicBlock(name="ACC_ENG")
        acc_eng.add_instruction(ir.Assign(
            target="ENG_SALES_3",
            source=asg.BinaryOperation(
                left=asg.AmperVar(name="ENG_SALES_1"),
                operator="+",
                right=asg.AmperVar(name="SALES_1")
            )
        ))
        acc_eng.add_instruction(ir.Jump(target="BODY_2"))
        cfg.add_block(acc_eng)

        # Second decision point
        body2 = ir.BasicBlock(name="BODY_2")
        body2.add_instruction(ir.Phi(target="ENG_SALES_2", sources=["ENG_SALES_1", "ENG_SALES_3"]))
        body2.add_instruction(ir.Branch(
            condition=asg.BinaryOperation(left=asg.AmperVar(name="COUNTRY_1"), operator="EQ", right=asg.Literal("FRANCE")),
            true_target="ACC_FRA",
            false_target="POST_ACC"
        ))
        cfg.add_block(body2)

        # Second Accumulator
        acc_fra = ir.BasicBlock(name="ACC_FRA")
        acc_fra.add_instruction(ir.Assign(
            target="FRA_SALES_3",
            source=asg.BinaryOperation(
                left=asg.AmperVar(name="FRA_SALES_1"),
                operator="+",
                right=asg.AmperVar(name="SALES_1")
            )
        ))
        acc_fra.add_instruction(ir.Jump(target="POST_ACC"))
        cfg.add_block(acc_fra)

        # Post accumulator block to prevent it being seen as a global filter
        post_acc = ir.BasicBlock(name="POST_ACC")
        post_acc.add_instruction(ir.Type(messages=[asg.Literal("Continuing")]))
        post_acc.add_instruction(ir.Jump(target="LBL"))
        cfg.add_block(post_acc)

        # Closing
        closing = ir.BasicBlock(name="LBL")
        closing.add_instruction(ir.Phi(target="FRA_SALES_2", sources=["FRA_SALES_1", "FRA_SALES_3"]))
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
        cfg.add_edge("BODY", "ACC_ENG")
        cfg.add_edge("BODY", "BODY_2")
        cfg.add_edge("ACC_ENG", "BODY_2")
        cfg.add_edge("BODY_2", "ACC_FRA")
        cfg.add_edge("BODY_2", "POST_ACC")
        cfg.add_edge("ACC_FRA", "POST_ACC")
        cfg.add_edge("POST_ACC", "LBL")
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

        # ENG_SALES should be a conditional SUM
        eng_sales_field = next(f for f in sum_verb.fields if f.alias == "ENG_SALES")
        self.assertIsInstance(eng_sales_field.name, asg.IfExpression)

        if_expr = eng_sales_field.name
        self.assertEqual(str(if_expr.condition), "(COUNTRY EQ 'ENGLAND')")
        self.assertEqual(if_expr.then_expr.name, "SALES")

        # FRA_SALES should also be a conditional SUM
        fra_sales_field = next(f for f in sum_verb.fields if f.alias == "FRA_SALES")
        self.assertIsInstance(fra_sales_field.name, asg.IfExpression)
        self.assertEqual(str(fra_sales_field.name.condition), "(COUNTRY EQ 'FRANCE')")

        # 5. Emit SQL and check for CASE
        emitter = PostgresEmitter(metadata_registry=registry)
        sql = emitter._emit_report(report_instr)
        self.assertIn("SUM((CASE WHEN (COUNTRY = 'ENGLAND') THEN SALES ELSE 0 END)) AS \"ENG_SALES\"", sql)
        self.assertIn("SUM((CASE WHEN (COUNTRY = 'FRANCE') THEN SALES ELSE 0 END)) AS \"FRA_SALES\"", sql)

if __name__ == '__main__':
    unittest.main()

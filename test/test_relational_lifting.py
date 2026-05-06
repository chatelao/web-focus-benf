import unittest
import ir
import asg
from optimizer import RelationalLiftingOptimizer
from metadata_registry import MetadataRegistry

class TestRelationalLifting(unittest.TestCase):
    def test_lift_simple_sum_loop(self):
        # 1. Setup metadata for CAR file
        registry = MetadataRegistry()
        car_master = asg.MasterFile(name="CAR", segments=[
            asg.Segment(name="ORIGIN", fields=[
                asg.Field(name="COUNTRY"),
                asg.Field(name="CAR"),
                asg.Field(name="MODEL"),
                asg.Field(name="PRICE")
            ])
        ])
        registry.register_master_file(car_master)

        # 2. Construct CFG for procedural loop:
        # -REPEAT LBL 10 TIMES
        # -READ CAR &COUNTRY &CAR &MODEL &PRICE
        # -SET &TOTAL_PRICE = &TOTAL_PRICE + &PRICE
        # LBL

        cfg = ir.ControlFlowGraph()

        # Entry Block
        entry = ir.BasicBlock(name="ENTRY")
        entry.add_instruction(ir.Assign(target="TOTAL_PRICE_0", source=asg.Literal(0)))
        entry.add_instruction(ir.Assign(target="I_0", source=asg.Literal(1)))
        entry.add_instruction(ir.Jump(target="LOOP_HEADER_LBL"))
        cfg.add_block(entry)

        # Header Block
        header = ir.BasicBlock(name="LOOP_HEADER_LBL")
        header.add_instruction(ir.Phi(target="TOTAL_PRICE_1", sources=["TOTAL_PRICE_0", "TOTAL_PRICE_2"]))
        header.add_instruction(ir.Phi(target="I_1", sources=["I_0", "I_2"]))
        header.add_instruction(ir.Branch(
            condition=asg.BinaryOperation(left=asg.AmperVar(name="I_1"), operator="LE", right=asg.Literal(10)),
            true_target="BODY",
            false_target="EXIT"
        ))
        cfg.add_block(header)

        # Body Block
        body = ir.BasicBlock(name="BODY")
        body.add_instruction(ir.Read(filename="CAR", variables=["COUNTRY_1", "CAR_1", "MODEL_1", "PRICE_1"]))
        body.add_instruction(ir.Assign(
            target="TOTAL_PRICE_2",
            source=asg.BinaryOperation(
                left=asg.AmperVar(name="TOTAL_PRICE_1"),
                operator="+",
                right=asg.AmperVar(name="PRICE_1")
            )
        ))
        body.add_instruction(ir.Jump(target="LBL"))
        cfg.add_block(body)

        # Closing Block
        closing = ir.BasicBlock(name="LBL")
        closing.add_instruction(ir.Assign(
            target="I_2",
            source=asg.BinaryOperation(left=asg.AmperVar(name="I_1"), operator="+", right=asg.Literal(1))
        ))
        closing.add_instruction(ir.Jump(target="LOOP_HEADER_LBL"))
        cfg.add_block(closing)

        # Exit Block
        exit_block = ir.BasicBlock(name="EXIT")
        cfg.add_block(exit_block)

        # Add Edges
        cfg.add_edge("ENTRY", "LOOP_HEADER_LBL")
        cfg.add_edge("LOOP_HEADER_LBL", "BODY")
        cfg.add_edge("LOOP_HEADER_LBL", "EXIT")
        cfg.add_edge("BODY", "LBL")
        cfg.add_edge("LBL", "LOOP_HEADER_LBL")

        cfg.entry_block = entry

        # 3. Run Relational Lifting
        optimizer = RelationalLiftingOptimizer()
        optimizer.lift_data_loops(cfg, registry)

        # 4. Verifications
        # Entry should now jump to LIFTED_LOOP_HEADER_LBL
        self.assertEqual(entry.instructions[-1].target, "LIFTED_LOOP_HEADER_LBL")

        # LIFTED_LOOP_HEADER_LBL should exist and contain an ir.Report
        self.assertIn("LIFTED_LOOP_HEADER_LBL", cfg.blocks)
        lifted_block = cfg.blocks["LIFTED_LOOP_HEADER_LBL"]

        report_instr = None
        for instr in lifted_block.instructions:
            if isinstance(instr, ir.Report):
                report_instr = instr
                break

        self.assertIsNotNone(report_instr)
        self.assertEqual(report_instr.filename, "CAR")

        # Check SUM component
        sum_verb = report_instr.components[0]
        self.assertIsInstance(sum_verb, asg.VerbCommand)
        self.assertEqual(sum_verb.verb, "SUM")
        self.assertEqual(sum_verb.fields[0].name, "PRICE")
        self.assertEqual(sum_verb.fields[0].alias, "TOTAL_PRICE")

    def test_lift_loop_with_filter(self):
        # 1. Setup metadata
        registry = MetadataRegistry()
        car_master = asg.MasterFile(name="CAR", segments=[
            asg.Segment(name="ORIGIN", fields=[
                asg.Field(name="COUNTRY"),
                asg.Field(name="CAR"),
                asg.Field(name="MODEL"),
                asg.Field(name="PRICE")
            ])
        ])
        registry.register_master_file(car_master)

        # 2. Construct CFG with procedural filter:
        # -REPEAT LBL 10 TIMES
        # -READ CAR &COUNTRY &CAR &MODEL &PRICE
        # -IF &COUNTRY NE 'JAPAN' GOTO LBL
        # -SET &TOTAL_PRICE = &TOTAL_PRICE + &PRICE
        # LBL

        cfg = ir.ControlFlowGraph()

        # Entry
        entry = ir.BasicBlock(name="ENTRY")
        entry.add_instruction(ir.Assign(target="TOTAL_PRICE_0", source=asg.Literal(0)))
        entry.add_instruction(ir.Assign(target="I_0", source=asg.Literal(1)))
        entry.add_instruction(ir.Jump(target="LOOP_HEADER_LBL"))
        cfg.add_block(entry)

        # Header
        header = ir.BasicBlock(name="LOOP_HEADER_LBL")
        header.add_instruction(ir.Phi(target="TOTAL_PRICE_1", sources=["TOTAL_PRICE_0", "TOTAL_PRICE_2"]))
        header.add_instruction(ir.Phi(target="I_1", sources=["I_0", "I_2"]))
        header.add_instruction(ir.Branch(
            condition=asg.BinaryOperation(left=asg.AmperVar(name="I_1"), operator="LE", right=asg.Literal(10)),
            true_target="BODY1",
            false_target="EXIT"
        ))
        cfg.add_block(header)

        # Body1: Read and Filter
        body1 = ir.BasicBlock(name="BODY1")
        body1.add_instruction(ir.Read(filename="CAR", variables=["COUNTRY_1", "CAR_1", "MODEL_1", "PRICE_1"]))
        body1.add_instruction(ir.Branch(
            condition=asg.BinaryOperation(left=asg.AmperVar(name="COUNTRY_1"), operator="NE", right=asg.Literal("JAPAN")),
            true_target="LBL",
            false_target="BODY2"
        ))
        cfg.add_block(body1)

        # Body2: Accumulate
        body2 = ir.BasicBlock(name="BODY2")
        body2.add_instruction(ir.Assign(
            target="TOTAL_PRICE_2",
            source=asg.BinaryOperation(
                left=asg.AmperVar(name="TOTAL_PRICE_1"),
                operator="+",
                right=asg.AmperVar(name="PRICE_1")
            )
        ))
        body2.add_instruction(ir.Jump(target="LBL"))
        cfg.add_block(body2)

        # Closing
        closing = ir.BasicBlock(name="LBL")
        closing.add_instruction(ir.Phi(target="TOTAL_PRICE_3", sources=["TOTAL_PRICE_1", "TOTAL_PRICE_2"]))
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
        cfg.add_edge("LOOP_HEADER_LBL", "BODY1")
        cfg.add_edge("LOOP_HEADER_LBL", "EXIT")
        cfg.add_edge("BODY1", "LBL")
        cfg.add_edge("BODY1", "BODY2")
        cfg.add_edge("BODY2", "LBL")
        cfg.add_edge("LBL", "LOOP_HEADER_LBL")

        cfg.entry_block = entry

        # 3. Run Relational Lifting
        optimizer = RelationalLiftingOptimizer()
        optimizer.lift_data_loops(cfg, registry)

        # 4. Verifications
        lifted_block = cfg.blocks["LIFTED_LOOP_HEADER_LBL"]
        report_instr = lifted_block.instructions[0]

        self.assertIsInstance(report_instr, ir.Report)

        # Verify WHERE clause
        where = None
        for comp in report_instr.components:
            if isinstance(comp, asg.WhereClause):
                where = comp
                break

        self.assertIsNotNone(where)
        # Condition should be NOT (COUNTRY NE 'JAPAN') which is (COUNTRY EQ 'JAPAN')
        # but identify_filters negates the skip condition.
        # Skip condition: COUNTRY NE 'JAPAN'
        # Filter: NOT (COUNTRY NE 'JAPAN')
        self.assertIsInstance(where.condition, asg.UnaryOperation)
        self.assertEqual(where.condition.operator, "NOT")
        self.assertEqual(where.condition.operand.left.name, "COUNTRY")
        self.assertEqual(where.condition.operand.operator, "NE")

if __name__ == '__main__':
    unittest.main()

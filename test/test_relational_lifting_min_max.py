import unittest
import ir
import asg
from optimizer import RelationalLiftingOptimizer
from metadata_registry import MetadataRegistry

class TestRelationalLiftingMinMax(unittest.TestCase):
    def setUp(self):
        self.registry = MetadataRegistry()
        car_master = asg.MasterFile(name="CAR", segments=[
            asg.Segment(name="ORIGIN", fields=[
                asg.Field(name="COUNTRY"),
                asg.Field(name="CAR"),
                asg.Field(name="MODEL"),
                asg.Field(name="PRICE")
            ])
        ])
        self.registry.register_master_file(car_master)
        self.optimizer = RelationalLiftingOptimizer()

    def test_lift_min_loop(self):
        # Procedural MIN loop:
        # -SET &MIN_PRICE = 999999;
        # -REPEAT LBL 10 TIMES
        # -READ CAR &COUNTRY &CAR &MODEL &PRICE
        # -IF &PRICE LT &MIN_PRICE THEN -SET &MIN_PRICE = &PRICE
        # LBL

        cfg = ir.ControlFlowGraph()

        # Entry
        entry = ir.BasicBlock(name="ENTRY")
        entry.add_instruction(ir.Assign(target="MIN_PRICE_0", source=asg.Literal(999999)))
        entry.add_instruction(ir.Assign(target="I_0", source=asg.Literal(1)))
        entry.add_instruction(ir.Jump(target="LOOP_HEADER_LBL"))
        cfg.add_block(entry)

        # Header
        header = ir.BasicBlock(name="LOOP_HEADER_LBL")
        header.add_instruction(ir.Phi(target="MIN_PRICE_1", sources=["MIN_PRICE_0", "MIN_PRICE_3"]))
        header.add_instruction(ir.Phi(target="I_1", sources=["I_0", "I_2"]))
        header.add_instruction(ir.Branch(
            condition=asg.BinaryOperation(left=asg.AmperVar(name="I_1"), operator="LE", right=asg.Literal(10)),
            true_target="BODY1",
            false_target="EXIT"
        ))
        cfg.add_block(header)

        # Body1: Read and Guard
        body1 = ir.BasicBlock(name="BODY1")
        body1.add_instruction(ir.Read(filename="CAR", variables=["COUNTRY_1", "CAR_1", "MODEL_1", "PRICE_1"]))
        body1.add_instruction(ir.Branch(
            condition=asg.BinaryOperation(left=asg.AmperVar(name="PRICE_1"), operator="LT", right=asg.AmperVar(name="MIN_PRICE_1")),
            true_target="BODY2",
            false_target="LBL"
        ))
        cfg.add_block(body1)

        # Body2: Update MIN
        body2 = ir.BasicBlock(name="BODY2")
        body2.add_instruction(ir.Assign(target="MIN_PRICE_2", source=asg.AmperVar(name="PRICE_1")))
        body2.add_instruction(ir.Jump(target="LBL"))
        cfg.add_block(body2)

        # Closing
        closing = ir.BasicBlock(name="LBL")
        closing.add_instruction(ir.Phi(target="MIN_PRICE_3", sources=["MIN_PRICE_2", "MIN_PRICE_1"]))
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
        cfg.add_edge("BODY1", "BODY2")
        cfg.add_edge("BODY1", "LBL")
        cfg.add_edge("BODY2", "LBL")
        cfg.add_edge("LBL", "LOOP_HEADER_LBL")

        cfg.entry_block = entry

        # Run Lifting
        self.optimizer.lift_data_loops(cfg, self.registry)

        # Verify
        lifted_block = cfg.blocks["LIFTED_LOOP_HEADER_LBL"]
        report_instr = lifted_block.instructions[0]
        self.assertIsInstance(report_instr, ir.Report)

        # Components might be [COUNT, SUM_MIN] or just [SUM_MIN]
        min_field = None
        for comp in report_instr.components:
            if isinstance(comp, asg.VerbCommand):
                for f in comp.fields:
                    if f.prefix_operators == ["MIN"]:
                        min_field = f
                        break

        self.assertIsNotNone(min_field, "MIN field not found in lifted report")
        self.assertEqual(min_field.name, "PRICE")
        self.assertEqual(min_field.prefix_operators, ["MIN"])
        self.assertEqual(min_field.alias, "MIN_PRICE")

    def test_lift_max_loop(self):
        # Procedural MAX loop:
        # -SET &MAX_PRICE = 0;
        # -REPEAT LBL 10 TIMES
        # -READ CAR &COUNTRY &CAR &MODEL &PRICE
        # -IF &PRICE GT &MAX_PRICE THEN -SET &MAX_PRICE = &PRICE
        # LBL

        cfg = ir.ControlFlowGraph()

        # Entry
        entry = ir.BasicBlock(name="ENTRY")
        entry.add_instruction(ir.Assign(target="MAX_PRICE_0", source=asg.Literal(0)))
        entry.add_instruction(ir.Assign(target="I_0", source=asg.Literal(1)))
        entry.add_instruction(ir.Jump(target="LOOP_HEADER_LBL"))
        cfg.add_block(entry)

        # Header
        header = ir.BasicBlock(name="LOOP_HEADER_LBL")
        header.add_instruction(ir.Phi(target="MAX_PRICE_1", sources=["MAX_PRICE_0", "MAX_PRICE_3"]))
        header.add_instruction(ir.Phi(target="I_1", sources=["I_0", "I_2"]))
        header.add_instruction(ir.Branch(
            condition=asg.BinaryOperation(left=asg.AmperVar(name="I_1"), operator="LE", right=asg.Literal(10)),
            true_target="BODY1",
            false_target="EXIT"
        ))
        cfg.add_block(header)

        # Body1: Read and Guard
        body1 = ir.BasicBlock(name="BODY1")
        body1.add_instruction(ir.Read(filename="CAR", variables=["COUNTRY_1", "CAR_1", "MODEL_1", "PRICE_1"]))
        body1.add_instruction(ir.Branch(
            condition=asg.BinaryOperation(left=asg.AmperVar(name="PRICE_1"), operator="GT", right=asg.AmperVar(name="MAX_PRICE_1")),
            true_target="BODY2",
            false_target="LBL"
        ))
        cfg.add_block(body1)

        # Body2: Update MAX
        body2 = ir.BasicBlock(name="BODY2")
        body2.add_instruction(ir.Assign(target="MAX_PRICE_2", source=asg.AmperVar(name="PRICE_1")))
        body2.add_instruction(ir.Jump(target="LBL"))
        cfg.add_block(body2)

        # Closing
        closing = ir.BasicBlock(name="LBL")
        closing.add_instruction(ir.Phi(target="MAX_PRICE_3", sources=["MAX_PRICE_2", "MAX_PRICE_1"]))
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
        cfg.add_edge("BODY1", "BODY2")
        cfg.add_edge("BODY1", "LBL")
        cfg.add_edge("BODY2", "LBL")
        cfg.add_edge("LBL", "LOOP_HEADER_LBL")

        cfg.entry_block = entry

        # Run Lifting
        self.optimizer.lift_data_loops(cfg, self.registry)

        # Verify
        lifted_block = cfg.blocks["LIFTED_LOOP_HEADER_LBL"]
        report_instr = lifted_block.instructions[0]
        self.assertIsInstance(report_instr, ir.Report)

        # Components might be [COUNT, SUM_MAX] or just [SUM_MAX]
        max_field = None
        for comp in report_instr.components:
            if isinstance(comp, asg.VerbCommand):
                for f in comp.fields:
                    if f.prefix_operators == ["MAX"]:
                        max_field = f
                        break

        self.assertIsNotNone(max_field, "MAX field not found in lifted report")
        self.assertEqual(max_field.name, "PRICE")
        self.assertEqual(max_field.prefix_operators, ["MAX"])
        self.assertEqual(max_field.alias, "MAX_PRICE")

if __name__ == '__main__':
    unittest.main()

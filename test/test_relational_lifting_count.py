import unittest
import ir
import asg
from optimizer import RelationalLiftingOptimizer
from metadata_registry import MetadataRegistry

class TestRelationalLiftingCount(unittest.TestCase):
    def test_lift_count_loop(self):
        # 1. Setup metadata
        registry = MetadataRegistry()
        car_master = asg.MasterFile(name="CAR", segments=[
            asg.Segment(name="ORIGIN", fields=[
                asg.Field(name="COUNTRY"),
                asg.Field(name="CAR")
            ])
        ])
        registry.register_master_file(car_master)

        # 2. Construct CFG for procedural count loop:
        # -REPEAT LBL 10 TIMES
        # -READ CAR &COUNTRY &CAR
        # -SET &CNT = &CNT + 1
        # LBL

        cfg = ir.ControlFlowGraph()

        # Entry
        entry = ir.BasicBlock(name="ENTRY")
        entry.add_instruction(ir.Assign(target="CNT_0", source=asg.Literal(0)))
        entry.add_instruction(ir.Assign(target="I_0", source=asg.Literal(1)))
        entry.add_instruction(ir.Jump(target="LOOP_HEADER_LBL"))
        cfg.add_block(entry)

        # Header
        header = ir.BasicBlock(name="LOOP_HEADER_LBL")
        header.add_instruction(ir.Phi(target="CNT_1", sources=["CNT_0", "CNT_2"]))
        header.add_instruction(ir.Phi(target="I_1", sources=["I_0", "I_2"]))
        header.add_instruction(ir.Branch(
            condition=asg.BinaryOperation(left=asg.AmperVar(name="I_1"), operator="LE", right=asg.Literal(10)),
            true_target="BODY",
            false_target="EXIT"
        ))
        cfg.add_block(header)

        # Body
        body = ir.BasicBlock(name="BODY")
        body.add_instruction(ir.Read(filename="CAR", variables=["COUNTRY_1", "CAR_1"]))
        body.add_instruction(ir.Assign(
            target="CNT_2",
            source=asg.BinaryOperation(
                left=asg.AmperVar(name="CNT_1"),
                operator="+",
                right=asg.Literal(1)
            )
        ))
        body.add_instruction(ir.Jump(target="LBL"))
        cfg.add_block(body)

        # Closing
        closing = ir.BasicBlock(name="LBL")
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
        cfg.add_edge("BODY", "LBL")
        cfg.add_edge("LBL", "LOOP_HEADER_LBL")

        cfg.entry_block = entry

        # 3. Run Relational Lifting
        optimizer = RelationalLiftingOptimizer()
        optimizer.lift_data_loops(cfg, registry)

        # 4. Verifications
        self.assertIn("LIFTED_LOOP_HEADER_LBL", cfg.blocks)
        lifted_block = cfg.blocks["LIFTED_LOOP_HEADER_LBL"]

        report_instr = None
        for instr in lifted_block.instructions:
            if isinstance(instr, ir.Report):
                report_instr = instr
                break

        self.assertIsNotNone(report_instr, "Loop should have been lifted to ir.Report")

        # Check for COUNT verb
        count_verb = None
        for comp in report_instr.components:
            if isinstance(comp, asg.VerbCommand) and comp.verb == "COUNT":
                count_verb = comp
                break

        self.assertIsNotNone(count_verb, "Should have a COUNT verb command")

        # Find CNT alias in the fields
        cnt_field = next((f for f in count_verb.fields if f.alias == "CNT"), None)
        self.assertIsNotNone(cnt_field, "Should have a field with alias 'CNT'")
        # It should be COUNTing one of the fields from CAR
        self.assertIn(cnt_field.name, ["COUNTRY", "CAR"])

if __name__ == '__main__':
    unittest.main()

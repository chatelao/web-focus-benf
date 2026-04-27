import unittest
import sys
import os

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from ir_builder import IRBuilder
from asg import *
from ir import *

class TestIRBuilder(unittest.TestCase):
    def test_linear_flow(self):
        # -SET &X = 1
        # -TYPE Hello
        # TABLE FILE CAR ... END
        asg = [
            SetDM(variable="&X", expression=Literal(1)),
            TypeDM(messages=[Literal("Hello")]),
            ReportRequest(filename="CAR")
        ]

        builder = IRBuilder()
        cfg = builder.build(asg)

        # Should have ENTRY block containing 3 instructions
        self.assertIn("ENTRY", cfg.blocks)
        entry = cfg.blocks["ENTRY"]
        self.assertEqual(len(entry.instructions), 3)
        self.assertIsInstance(entry.instructions[0], Assign)
        self.assertIsInstance(entry.instructions[1], Type)
        self.assertIsInstance(entry.instructions[2], Report)

    def test_basic_jump(self):
        # -GOTO MYLABEL
        # -SET &X = 1 (dead code)
        # -MYLABEL
        # -TYPE Done
        asg = [
            Goto(target="MYLABEL"),
            SetDM(variable="&X", expression=Literal(1)),
            Label(name="MYLABEL"),
            TypeDM(messages=[Literal("Done")])
        ]

        builder = IRBuilder()
        cfg = builder.build(asg)

        self.assertIn("ENTRY", cfg.blocks)
        self.assertIn("MYLABEL", cfg.blocks)

        entry = cfg.blocks["ENTRY"]
        self.assertEqual(len(entry.instructions), 1)
        self.assertIsInstance(entry.instructions[0], Jump)
        self.assertEqual(entry.instructions[0].target, "MYLABEL")

        # Edge from ENTRY to MYLABEL
        self.assertIn(cfg.blocks["MYLABEL"], entry.successors)

        # DEAD code block should exist but ENTRY doesn't fall through to it
        # because ENTRY ends with a Jump.
        # Wait, the current implementation doesn't explicitly mark dead code,
        # but -SET &X=1 will be in an anonymous block.

        mylabel = cfg.blocks["MYLABEL"]
        self.assertEqual(len(mylabel.instructions), 1)
        self.assertIsInstance(mylabel.instructions[0], Type)

    def test_fallthrough(self):
        # -TYPE Start
        # -MYLABEL
        # -TYPE End
        asg = [
            TypeDM(messages=[Literal("Start")]),
            Label(name="MYLABEL"),
            TypeDM(messages=[Literal("End")])
        ]

        builder = IRBuilder()
        cfg = builder.build(asg)

        entry = cfg.blocks["ENTRY"]
        mylabel = cfg.blocks["MYLABEL"]

        # Edge from ENTRY to MYLABEL (fallthrough)
        self.assertIn(mylabel, entry.successors)
        self.assertEqual(len(entry.instructions), 1)
        self.assertEqual(len(mylabel.instructions), 1)

    def test_conditional_branch(self):
        # -IF &X EQ 1 GOTO TRUE_LAB
        # -TYPE False
        # -TRUE_LAB
        # -TYPE True
        asg = [
            IfDM(condition=BinaryOperation(AmperVar("&X"), "EQ", Literal(1)), then_target="TRUE_LAB"),
            TypeDM(messages=[Literal("False")]),
            Label(name="TRUE_LAB"),
            TypeDM(messages=[Literal("True")])
        ]

        builder = IRBuilder()
        cfg = builder.build(asg)

        self.assertIn("ENTRY", cfg.blocks)
        self.assertIn("TRUE_LAB", cfg.blocks)

        entry = cfg.blocks["ENTRY"]
        self.assertEqual(len(entry.instructions), 1)
        self.assertIsInstance(entry.instructions[0], Branch)
        self.assertEqual(entry.instructions[0].true_target, "TRUE_LAB")

        # Fallthrough block (where -TYPE False is)
        false_block_name = entry.instructions[0].false_target
        self.assertIn(false_block_name, cfg.blocks)
        false_block = cfg.blocks[false_block_name]
        self.assertIsInstance(false_block.instructions[0], Type)

        # Edges
        self.assertIn(cfg.blocks["TRUE_LAB"], entry.successors)
        self.assertIn(false_block, entry.successors)
        self.assertIn(cfg.blocks["TRUE_LAB"], false_block.successors) # Fallthrough from FALSE to TRUE_LAB

    def test_conditional_branch_with_else(self):
        # -IF &X EQ 1 GOTO TRUE_LAB ELSE GOTO FALSE_LAB
        # -TRUE_LAB
        # -TYPE True
        # -FALSE_LAB
        # -TYPE False
        asg = [
            IfDM(condition=BinaryOperation(AmperVar("&X"), "EQ", Literal(1)),
                 then_target="TRUE_LAB", else_target="FALSE_LAB"),
            Label(name="TRUE_LAB"),
            TypeDM(messages=[Literal("True")]),
            Label(name="FALSE_LAB"),
            TypeDM(messages=[Literal("False")])
        ]

        builder = IRBuilder()
        cfg = builder.build(asg)

        entry = cfg.blocks["ENTRY"]
        self.assertEqual(len(entry.instructions), 1)
        self.assertIsInstance(entry.instructions[0], Branch)
        self.assertEqual(entry.instructions[0].true_target, "TRUE_LAB")
        self.assertEqual(entry.instructions[0].false_target, "FALSE_LAB")

        self.assertIn(cfg.blocks["TRUE_LAB"], entry.successors)
        self.assertIn(cfg.blocks["FALSE_LAB"], entry.successors)

if __name__ == '__main__':
    unittest.main()

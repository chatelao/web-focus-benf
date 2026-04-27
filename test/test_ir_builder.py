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

if __name__ == '__main__':
    unittest.main()

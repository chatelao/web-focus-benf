import unittest
import sys
import os

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from ir_builder import IRBuilder
from asg import MatchRequest, SubMatch, Literal
import ir

class TestIRMatch(unittest.TestCase):
    def test_match_ir_conversion(self):
        # MATCH FILE file1
        # SUM sales
        # RUN
        # FILE file2
        # AFTER MATCH OLD-OR-NEW
        # END
        asg = [
            MatchRequest(
                filename="file1",
                components=[Literal("SUM sales")], # Simplification for test
                sub_matches=[
                    SubMatch(filename="file2", components=[], after_match=None)
                ]
            )
        ]

        builder = IRBuilder()
        cfg = builder.build(asg)

        self.assertIn("ENTRY", cfg.blocks)
        entry = cfg.blocks["ENTRY"]
        self.assertEqual(len(entry.instructions), 1)
        self.assertIsInstance(entry.instructions[0], ir.Match)
        match_instr = entry.instructions[0]
        self.assertEqual(match_instr.filename, "file1")
        self.assertEqual(len(match_instr.sub_matches), 1)
        self.assertEqual(match_instr.sub_matches[0].filename, "file2")

if __name__ == '__main__':
    unittest.main()

import unittest
import sys
import os

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from ir import *

class TestIR(unittest.TestCase):
    def test_basic_block(self):
        bb = BasicBlock(name="B1")
        bb.add_instruction(Assign(target="x", source=1))
        bb.add_instruction(Assign(target="y", source=2))

        self.assertEqual(len(bb.instructions), 2)
        self.assertIsInstance(bb.instructions[0], Assign)
        self.assertEqual(bb.instructions[0].target, "x")

    def test_cfg_construction(self):
        cfg = ControlFlowGraph()

        b1 = BasicBlock(name="B1")
        b2 = BasicBlock(name="B2")
        b3 = BasicBlock(name="B3")

        cfg.add_block(b1)
        cfg.add_block(b2)
        cfg.add_block(b3)

        cfg.add_edge("B1", "B2")
        cfg.add_edge("B1", "B3")

        self.assertEqual(cfg.entry_block.name, "B1")
        self.assertEqual(len(b1.successors), 2)
        self.assertIn(b2, b1.successors)
        self.assertIn(b3, b1.successors)
        self.assertIn(b1, b2.predecessors)
        self.assertIn(b1, b3.predecessors)

    def test_instruction_types(self):
        label = Label(name="L1")
        jump = Jump(target="L1")
        branch = Branch(condition="x > 0", true_target="L1", false_target="L2")
        phi = Phi(target="x2", sources=["x0", "x1"])

        self.assertEqual(label.name, "L1")
        self.assertEqual(jump.target, "L1")
        self.assertEqual(branch.true_target, "L1")
        self.assertEqual(phi.sources, ["x0", "x1"])

if __name__ == '__main__':
    unittest.main()

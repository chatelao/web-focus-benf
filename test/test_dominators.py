import unittest
import sys
import os

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from ir import BasicBlock, ControlFlowGraph
from dominators import DominatorAnalysis

class TestDominatorAnalysis(unittest.TestCase):
    def test_linear_flow(self):
        # A -> B -> C
        cfg = ControlFlowGraph()
        a = BasicBlock("A")
        b = BasicBlock("B")
        c = BasicBlock("C")
        cfg.add_block(a)
        cfg.add_block(b)
        cfg.add_block(c)
        cfg.add_edge("A", "B")
        cfg.add_edge("B", "C")
        cfg.entry_block = a

        analysis = DominatorAnalysis(cfg)
        analysis.run()

        self.assertEqual(analysis.idoms["A"], "A")
        self.assertEqual(analysis.idoms["B"], "A")
        self.assertEqual(analysis.idoms["C"], "B")

        self.assertEqual(analysis.frontiers["A"], set())
        self.assertEqual(analysis.frontiers["B"], set())
        self.assertEqual(analysis.frontiers["C"], set())

    def test_diamond_flow(self):
        #      A
        #     / \
        #    B   C
        #     \ /
        #      D
        cfg = ControlFlowGraph()
        a = BasicBlock("A")
        b = BasicBlock("B")
        c = BasicBlock("C")
        d = BasicBlock("D")
        cfg.add_block(a)
        cfg.add_block(b)
        cfg.add_block(c)
        cfg.add_block(d)
        cfg.add_edge("A", "B")
        cfg.add_edge("A", "C")
        cfg.add_edge("B", "D")
        cfg.add_edge("C", "D")
        cfg.entry_block = a

        analysis = DominatorAnalysis(cfg)
        analysis.run()

        self.assertEqual(analysis.idoms["A"], "A")
        self.assertEqual(analysis.idoms["B"], "A")
        self.assertEqual(analysis.idoms["C"], "A")
        self.assertEqual(analysis.idoms["D"], "A")

        self.assertEqual(analysis.frontiers["A"], set())
        self.assertEqual(analysis.frontiers["B"], {"D"})
        self.assertEqual(analysis.frontiers["C"], {"D"})
        self.assertEqual(analysis.frontiers["D"], set())

    def test_loop_flow(self):
        #      A
        #      |
        #      B <---
        #     / \    |
        #    C   D --|
        #    |
        #    E
        cfg = ControlFlowGraph()
        a = BasicBlock("A")
        b = BasicBlock("B")
        c = BasicBlock("C")
        d = BasicBlock("D")
        e = BasicBlock("E")
        cfg.add_block(a)
        cfg.add_block(b)
        cfg.add_block(c)
        cfg.add_block(d)
        cfg.add_block(e)
        cfg.add_edge("A", "B")
        cfg.add_edge("B", "C")
        cfg.add_edge("B", "D")
        cfg.add_edge("D", "B")
        cfg.add_edge("C", "E")
        cfg.entry_block = a

        analysis = DominatorAnalysis(cfg)
        analysis.run()

        self.assertEqual(analysis.idoms["A"], "A")
        self.assertEqual(analysis.idoms["B"], "A")
        self.assertEqual(analysis.idoms["C"], "B")
        self.assertEqual(analysis.idoms["D"], "B")
        self.assertEqual(analysis.idoms["E"], "C")

        self.assertEqual(analysis.frontiers["A"], set())
        self.assertEqual(analysis.frontiers["B"], {"B"})
        self.assertEqual(analysis.frontiers["D"], {"B"})
        self.assertEqual(analysis.frontiers["C"], set())
        self.assertEqual(analysis.frontiers["E"], set())

    def test_nested_loop(self):
        # A -> B -> C <---
        #      |    |    |
        #      |    D ---|
        #      |    |
        #      |--->E
        cfg = ControlFlowGraph()
        a = BasicBlock("A")
        b = BasicBlock("B")
        c = BasicBlock("C")
        d = BasicBlock("D")
        e = BasicBlock("E")
        cfg.add_block(a)
        cfg.add_block(b)
        cfg.add_block(c)
        cfg.add_block(d)
        cfg.add_block(e)
        cfg.add_edge("A", "B")
        cfg.add_edge("B", "C")
        cfg.add_edge("B", "E")
        cfg.add_edge("C", "D")
        cfg.add_edge("D", "C")
        cfg.add_edge("D", "E")
        cfg.entry_block = a

        analysis = DominatorAnalysis(cfg)
        analysis.run()

        self.assertEqual(analysis.idoms["A"], "A")
        self.assertEqual(analysis.idoms["B"], "A")
        self.assertEqual(analysis.idoms["C"], "B")
        self.assertEqual(analysis.idoms["D"], "C")
        self.assertEqual(analysis.idoms["E"], "B")

        self.assertEqual(analysis.frontiers["C"], {"C", "E"})
        self.assertEqual(analysis.frontiers["D"], {"C", "E"})

if __name__ == '__main__':
    unittest.main()

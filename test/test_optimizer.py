import unittest
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import ir
import asg
from optimizer import ConstantPropagator

class TestOptimizer(unittest.TestCase):
    def test_constant_propagation_linear(self):
        # X_0 = 1
        # Y_0 = X_0 + 2
        # Z_0 = Y_0 * 3
        cfg = ir.ControlFlowGraph()
        entry = ir.BasicBlock("ENTRY")
        cfg.add_block(entry)
        cfg.entry_block = entry

        entry.add_instruction(ir.Assign(target="X_0", source=asg.Literal(1)))
        entry.add_instruction(ir.Assign(target="Y_0", source=asg.BinaryOperation(asg.AmperVar("X_0"), "+", asg.Literal(2))))
        entry.add_instruction(ir.Assign(target="Z_0", source=asg.BinaryOperation(asg.AmperVar("Y_0"), "*", asg.Literal(3))))

        propagator = ConstantPropagator()
        propagator.run(cfg)

        # Verify substitutions
        instrs = entry.instructions
        self.assertIsInstance(instrs[1].source, asg.Literal)
        self.assertEqual(instrs[1].source.value, 3) # folded 1 + 2

        self.assertIsInstance(instrs[2].source, asg.Literal)
        self.assertEqual(instrs[2].source.value, 9) # folded 3 * 3

    def test_constant_propagation_branch(self):
        # ENTRY: X_0 = 10
        # B1: IF X_0 > 5 GOTO T ELSE GOTO F
        cfg = ir.ControlFlowGraph()
        entry = ir.BasicBlock("ENTRY")
        b1 = ir.BasicBlock("B1")
        cfg.add_block(entry)
        cfg.add_block(b1)
        cfg.entry_block = entry
        cfg.add_edge("ENTRY", "B1")

        entry.add_instruction(ir.Assign(target="X_0", source=asg.Literal(10)))
        b1.add_instruction(ir.Branch(
            condition=asg.BinaryOperation(asg.AmperVar("X_0"), ">", asg.Literal(5)),
            true_target="T",
            false_target="F"
        ))

        propagator = ConstantPropagator()
        propagator.run(cfg)

        branch = b1.instructions[0]
        self.assertIsInstance(branch.condition, asg.Literal)
        self.assertTrue(branch.condition.value)

    def test_constant_propagation_phi(self):
        # ENTRY: X_0 = 5
        # B1: X_1 = 5
        # B2: X_2 = Phi(X_0, X_1)
        # B2: Y_0 = X_2 + 1
        cfg = ir.ControlFlowGraph()
        entry = ir.BasicBlock("ENTRY")
        b1 = ir.BasicBlock("B1")
        b2 = ir.BasicBlock("B2")
        cfg.add_block(entry)
        cfg.add_block(b1)
        cfg.add_block(b2)
        cfg.entry_block = entry
        cfg.add_edge("ENTRY", "B2")
        cfg.add_edge("B1", "B2")

        entry.add_instruction(ir.Assign(target="X_0", source=asg.Literal(5)))
        b1.add_instruction(ir.Assign(target="X_1", source=asg.Literal(5)))

        phi = ir.Phi(target="X_2", sources=["X_0", "X_1"])
        b2.add_instruction(phi)
        b2.add_instruction(ir.Assign(target="Y_0", source=asg.BinaryOperation(asg.AmperVar("X_2"), "+", asg.Literal(1))))

        propagator = ConstantPropagator()
        propagator.run(cfg)

        assign = b2.instructions[1]
        self.assertIsInstance(assign.source, asg.Literal)
        self.assertEqual(assign.source.value, 6)

    def test_constant_propagation_report(self):
        # ENTRY: &VAL_0 = 100
        # ENTRY: TABLE FILE CAR: WHERE PRICE GT &VAL_0; END
        cfg = ir.ControlFlowGraph()
        entry = ir.BasicBlock("ENTRY")
        cfg.add_block(entry)
        cfg.entry_block = entry

        entry.add_instruction(ir.Assign(target="&VAL_0", source=asg.Literal(100)))

        where = asg.WhereClause(condition=asg.BinaryOperation(asg.Identifier("PRICE"), "GT", asg.AmperVar("&VAL_0")))
        report = ir.Report(filename="CAR", components=[where])
        entry.add_instruction(report)

        propagator = ConstantPropagator()
        propagator.run(cfg)

        report_instr = entry.instructions[1]
        where_clause = report_instr.components[0]
        self.assertIsInstance(where_clause.condition.right, asg.Literal)
        self.assertEqual(where_clause.condition.right.value, 100)

if __name__ == '__main__':
    unittest.main()

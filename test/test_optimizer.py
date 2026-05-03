import unittest
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import ir
import asg
from optimizer import ConstantPropagator, DeadCodeEliminator

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

    def test_dead_code_elimination_unreachable(self):
        # ENTRY: GOTO EXIT
        # UNREACHABLE: X = 1
        # EXIT: -TYPE END
        cfg = ir.ControlFlowGraph()
        entry = ir.BasicBlock("ENTRY")
        unreachable = ir.BasicBlock("UNREACHABLE")
        exit_block = ir.BasicBlock("EXIT")

        cfg.add_block(entry)
        cfg.add_block(unreachable)
        cfg.add_block(exit_block)
        cfg.entry_block = entry

        entry.add_instruction(ir.Jump(target="EXIT"))
        cfg.add_edge("ENTRY", "EXIT")

        unreachable.add_instruction(ir.Assign(target="X_0", source=asg.Literal(1)))
        cfg.add_edge("UNREACHABLE", "EXIT") # This edge is from an unreachable block

        exit_block.add_instruction(ir.Type(messages=[asg.Literal("END")]))

        dce = DeadCodeEliminator()
        dce.run(cfg)

        self.assertIn("ENTRY", cfg.blocks)
        self.assertIn("EXIT", cfg.blocks)
        self.assertNotIn("UNREACHABLE", cfg.blocks)
        self.assertEqual(len(cfg.blocks["EXIT"].predecessors), 1)
        self.assertEqual(cfg.blocks["EXIT"].predecessors[0].name, "ENTRY")

    def test_dead_code_elimination_unused_assign(self):
        # ENTRY: X_0 = 1
        # ENTRY: Y_0 = 2
        # ENTRY: -TYPE Y_0
        cfg = ir.ControlFlowGraph()
        entry = ir.BasicBlock("ENTRY")
        cfg.add_block(entry)
        cfg.entry_block = entry

        entry.add_instruction(ir.Assign(target="X_0", source=asg.Literal(1))) # Unused
        entry.add_instruction(ir.Assign(target="Y_0", source=asg.Literal(2))) # Used
        entry.add_instruction(ir.Type(messages=[asg.AmperVar("Y_0")]))

        dce = DeadCodeEliminator()
        dce.run(cfg)

        instrs = entry.instructions
        self.assertEqual(len(instrs), 2)
        self.assertEqual(instrs[0].target, "Y_0")
        self.assertIsInstance(instrs[1], ir.Type)

    def test_dead_code_elimination_side_effects(self):
        # ENTRY: X_0 = 1
        # ENTRY: -TYPE "Hello"
        # ENTRY: TABLE FILE CAR ... END
        cfg = ir.ControlFlowGraph()
        entry = ir.BasicBlock("ENTRY")
        cfg.add_block(entry)
        cfg.entry_block = entry

        entry.add_instruction(ir.Assign(target="X_0", source=asg.Literal(1))) # Unused
        entry.add_instruction(ir.Type(messages=[asg.Literal("Hello")])) # Side effect
        entry.add_instruction(ir.Report(filename="CAR", components=[])) # Side effect

        dce = DeadCodeEliminator()
        dce.run(cfg)

        instrs = entry.instructions
        self.assertEqual(len(instrs), 2)
        self.assertIsInstance(instrs[0], ir.Type)
        self.assertIsInstance(instrs[1], ir.Report)

    def test_dead_code_elimination_cascading(self):
        # X_0 = 1
        # Y_0 = X_0 + 1
        # Z_0 = Y_0 + 1
        # All unused
        cfg = ir.ControlFlowGraph()
        entry = ir.BasicBlock("ENTRY")
        cfg.add_block(entry)
        cfg.entry_block = entry

        entry.add_instruction(ir.Assign(target="X_0", source=asg.Literal(1)))
        entry.add_instruction(ir.Assign(target="Y_0", source=asg.BinaryOperation(asg.AmperVar("X_0"), "+", asg.Literal(1))))
        entry.add_instruction(ir.Assign(target="Z_0", source=asg.BinaryOperation(asg.AmperVar("Y_0"), "+", asg.Literal(1))))

        dce = DeadCodeEliminator()
        dce.run(cfg)

        self.assertEqual(len(entry.instructions), 0)

    def test_constant_folding_concatenation(self):
        cfg = ir.ControlFlowGraph()
        entry = ir.BasicBlock("ENTRY")
        cfg.add_block(entry)
        cfg.entry_block = entry

        entry.add_instruction(ir.Assign(target="S1", source=asg.Literal("Hello")))
        entry.add_instruction(ir.Assign(target="S2", source=asg.Literal("World")))
        entry.add_instruction(ir.Assign(target="S3", source=asg.BinaryOperation(asg.AmperVar("S1"), "||", asg.AmperVar("S2"))))
        entry.add_instruction(ir.Assign(target="S4", source=asg.BinaryOperation(asg.AmperVar("S1"), "|", asg.Literal(" "))))
        entry.add_instruction(ir.Assign(target="S5", source=asg.BinaryOperation(asg.AmperVar("S4"), "CONCAT", asg.AmperVar("S2"))))

        propagator = ConstantPropagator()
        propagator.run(cfg)

        self.assertEqual(propagator.constants["S3"].value, "HelloWorld")
        self.assertEqual(propagator.constants["S4"].value, "Hello ")
        self.assertEqual(propagator.constants["S5"].value, "Hello World")

    def test_constant_folding_boolean_short_circuit(self):
        cfg = ir.ControlFlowGraph()
        entry = ir.BasicBlock("ENTRY")
        cfg.add_block(entry)
        cfg.entry_block = entry

        # False AND X -> False
        entry.add_instruction(ir.Assign(target="B1", source=asg.BinaryOperation(asg.Literal(False), "AND", asg.AmperVar("X"))))
        # True OR X -> True
        entry.add_instruction(ir.Assign(target="B2", source=asg.BinaryOperation(asg.Literal(True), "OR", asg.AmperVar("X"))))
        # X AND False -> False
        entry.add_instruction(ir.Assign(target="B3", source=asg.BinaryOperation(asg.AmperVar("X"), "AND", asg.Literal(False))))
        # X OR True -> True
        entry.add_instruction(ir.Assign(target="B4", source=asg.BinaryOperation(asg.AmperVar("X"), "OR", asg.Literal(True))))

        propagator = ConstantPropagator()
        propagator.run(cfg)

        self.assertEqual(propagator.constants["B1"].value, False)
        self.assertEqual(propagator.constants["B2"].value, True)
        self.assertEqual(propagator.constants["B3"].value, False)
        self.assertEqual(propagator.constants["B4"].value, True)

    def test_constant_folding_boolean_full(self):
        cfg = ir.ControlFlowGraph()
        entry = ir.BasicBlock("ENTRY")
        cfg.add_block(entry)
        cfg.entry_block = entry

        entry.add_instruction(ir.Assign(target="B1", source=asg.BinaryOperation(asg.Literal(True), "AND", asg.Literal(True))))
        entry.add_instruction(ir.Assign(target="B2", source=asg.BinaryOperation(asg.Literal(True), "AND", asg.Literal(False))))
        entry.add_instruction(ir.Assign(target="B3", source=asg.BinaryOperation(asg.Literal(False), "OR", asg.Literal(True))))
        entry.add_instruction(ir.Assign(target="B4", source=asg.BinaryOperation(asg.Literal(False), "OR", asg.Literal(False))))

        propagator = ConstantPropagator()
        propagator.run(cfg)

        self.assertEqual(propagator.constants["B1"].value, True)
        self.assertEqual(propagator.constants["B2"].value, False)
        self.assertEqual(propagator.constants["B3"].value, True)
        self.assertEqual(propagator.constants["B4"].value, False)

if __name__ == '__main__':
    unittest.main()

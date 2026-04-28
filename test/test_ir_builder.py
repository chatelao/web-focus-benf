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

    def test_repeat_while(self):
        # -REPEAT MYLOOP WHILE &X LE 10
        # -TYPE Loop
        # -MYLOOP
        asg_nodes = [
            Repeat(label="MYLOOP", condition=BinaryOperation(AmperVar("&X"), "LE", Literal(10)), condition_type="WHILE"),
            TypeDM(messages=[Literal("Loop")]),
            Label(name="MYLOOP")
        ]

        builder = IRBuilder()
        cfg = builder.build(asg_nodes)

        self.assertIn("ENTRY", cfg.blocks)
        self.assertIn("LOOP_HEADER_MYLOOP", cfg.blocks)
        self.assertIn("LOOP_BODY_MYLOOP", cfg.blocks)
        self.assertIn("LOOP_AFTER_MYLOOP", cfg.blocks)

        entry = cfg.blocks["ENTRY"]
        header = cfg.blocks["LOOP_HEADER_MYLOOP"]
        body = cfg.blocks["LOOP_BODY_MYLOOP"]
        after = cfg.blocks["LOOP_AFTER_MYLOOP"]

        # ENTRY -> HEADER
        self.assertIn(header, entry.successors)

        # HEADER -> BODY (if True) and AFTER (if False)
        self.assertIsInstance(header.instructions[0], Branch)
        self.assertIn(body, header.successors)
        self.assertIn(after, header.successors)

        # BODY contains -TYPE
        self.assertIsInstance(body.instructions[0], Type)

        # BODY -> LABEL -> HEADER
        label_block = cfg.blocks["MYLOOP"]
        self.assertIn(label_block, body.successors)
        self.assertIn(header, label_block.successors)
        self.assertIsInstance(label_block.instructions[0], Jump)
        self.assertEqual(label_block.instructions[0].target, header.name)

    def test_repeat_times(self):
        # -REPEAT MYLOOP 5 TIMES
        # -TYPE Hello
        # -MYLOOP
        asg_nodes = [
            Repeat(label="MYLOOP", times=Literal(5)),
            TypeDM(messages=[Literal("Hello")]),
            Label(name="MYLOOP")
        ]

        builder = IRBuilder()
        cfg = builder.build(asg_nodes)

        entry = cfg.blocks["ENTRY"]
        header = cfg.blocks["LOOP_HEADER_MYLOOP"]
        body = cfg.blocks["LOOP_BODY_MYLOOP"]

        # Initialization in ENTRY
        self.assertIsInstance(entry.instructions[0], Assign)
        self.assertEqual(entry.instructions[0].target, "&REPEAT_COUNTER_MYLOOP")

        # Increment in LABEL block
        label_block = cfg.blocks["MYLOOP"]
        self.assertIsInstance(label_block.instructions[0], Assign)
        self.assertEqual(label_block.instructions[0].target, "&REPEAT_COUNTER_MYLOOP")
        self.assertIsInstance(label_block.instructions[1], Jump)

    def test_repeat_for(self):
        # -REPEAT MYLOOP FOR &I FROM 1 TO 10 STEP 2
        # -TYPE &I
        # -MYLOOP
        asg_nodes = [
            Repeat(label="MYLOOP", loop_var="&I", start_val=Literal(1), end_val=Literal(10), step_val=Literal(2)),
            TypeDM(messages=[AmperVar("&I")]),
            Label(name="MYLOOP")
        ]

        builder = IRBuilder()
        cfg = builder.build(asg_nodes)

        entry = cfg.blocks["ENTRY"]
        body = cfg.blocks["LOOP_BODY_MYLOOP"]

        # Initialization
        self.assertIsInstance(entry.instructions[0], Assign)
        self.assertEqual(entry.instructions[0].target, "&I")

        # Increment in LABEL block
        label_block = cfg.blocks["MYLOOP"]
        self.assertIsInstance(label_block.instructions[0], Assign)
        self.assertEqual(label_block.instructions[0].target, "&I")
        # source should be &I + 2
        source = label_block.instructions[0].source
        self.assertIsInstance(source, BinaryOperation)
        self.assertEqual(source.operator, "+")
        self.assertEqual(source.right.value, 2)

    def test_goto_loop_label(self):
        # -REPEAT MYLOOP WHILE &X LE 10
        # -IF &X EQ 5 GOTO MYLOOP
        # -TYPE Loop
        # -MYLOOP
        asg_nodes = [
            Repeat(label="MYLOOP", condition=BinaryOperation(AmperVar("&X"), "LE", Literal(10)), condition_type="WHILE"),
            IfDM(condition=BinaryOperation(AmperVar("&X"), "EQ", Literal(5)), then_target="MYLOOP"),
            TypeDM(messages=[Literal("Loop")]),
            Label(name="MYLOOP")
        ]

        builder = IRBuilder()
        cfg = builder.build(asg_nodes)

        self.assertIn("LOOP_HEADER_MYLOOP", cfg.blocks)
        self.assertIn("MYLOOP", cfg.blocks)

        body = cfg.blocks["LOOP_BODY_MYLOOP"]
        # body instructions: Branch (IfDM)
        self.assertIsInstance(body.instructions[0], Branch)
        self.assertEqual(body.instructions[0].true_target, "MYLOOP")

        myloop_label_block = cfg.blocks["MYLOOP"]
        # In the fixed implementation, MYLOOP block should contain the Jump back to header
        self.assertIsInstance(myloop_label_block.instructions[0], Jump)
        self.assertEqual(myloop_label_block.instructions[0].target, "LOOP_HEADER_MYLOOP")

    def test_join_instructions(self):
        # JOIN F1.FL1 TO F2.FL2 AS J1
        # JOIN CLEAR *
        asg_nodes = [
            Join(left_file="F1", left_field="FL1", right_file="F2", right_field="FL2", join_as="J1", outer=True),
            JoinClear()
        ]

        builder = IRBuilder()
        cfg = builder.build(asg_nodes)

        entry = cfg.blocks["ENTRY"]
        self.assertEqual(len(entry.instructions), 2)
        self.assertIsInstance(entry.instructions[0], Join)
        self.assertEqual(entry.instructions[0].left_file, "F1")
        self.assertEqual(entry.instructions[0].join_as, "J1")
        self.assertTrue(entry.instructions[0].outer)
        self.assertIsInstance(entry.instructions[1], JoinClear)

if __name__ == '__main__':
    unittest.main()

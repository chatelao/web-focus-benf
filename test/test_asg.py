import unittest
from src.asg import (
    Expression, Statement, Command, MasterFile, Segment, Field,
    Goto, Label, IfDM, Repeat, SetDM, TypeDM, IncludeDM, RunDM, ExitDM
)

class TestASGNodes(unittest.TestCase):
    def test_expression_instantiation(self):
        expr = Expression()
        self.assertIsInstance(expr, Expression)

    def test_statement_instantiation(self):
        stmt = Statement()
        self.assertIsInstance(stmt, Statement)

    def test_command_instantiation(self):
        cmd = Command()
        self.assertIsInstance(cmd, Command)

    def test_master_file_node(self):
        mf = MasterFile(name="EMPLOYEE", suffix="FOC")
        self.assertEqual(mf.name, "EMPLOYEE")
        self.assertEqual(mf.suffix, "FOC")
        self.assertEqual(mf.segments, [])

    def test_segment_node(self):
        seg = Segment(name="EMPDATA", segtype="S1")
        self.assertEqual(seg.name, "EMPDATA")
        self.assertEqual(seg.segtype, "S1")
        self.assertEqual(seg.fields, [])

    def test_field_node(self):
        fld = Field(name="LASTNAME", alias="LN", format="A15")
        self.assertEqual(fld.name, "LASTNAME")
        self.assertEqual(fld.alias, "LN")
        self.assertEqual(fld.format, "A15")

    def test_node_nesting(self):
        mf = MasterFile(name="EMPLOYEE")
        seg = Segment(name="EMPDATA", parent="EMPLOYEE")
        fld = Field(name="LASTNAME", alias="LN", format="A15")

        seg.fields.append(fld)
        mf.segments.append(seg)

        self.assertEqual(len(mf.segments), 1)
        self.assertEqual(mf.segments[0].name, "EMPDATA")
        self.assertEqual(len(mf.segments[0].fields), 1)
        self.assertEqual(mf.segments[0].fields[0].name, "LASTNAME")

    def test_dm_control_flow_nodes(self):
        goto_node = Goto(target="EXIT_REPORT")
        self.assertEqual(goto_node.target, "EXIT_REPORT")

        label_node = Label(name="EXIT_REPORT")
        self.assertEqual(label_node.name, "EXIT_REPORT")

        if_node = IfDM(condition="&VAR EQ 1", then_target="LABEL1", else_target="LABEL2")
        self.assertEqual(if_node.condition, "&VAR EQ 1")
        self.assertEqual(if_node.then_target, "LABEL1")
        self.assertEqual(if_node.else_target, "LABEL2")

        repeat_node = Repeat(label="LOOP_START")
        self.assertEqual(repeat_node.label, "LOOP_START")

    def test_dm_action_nodes(self):
        set_node = SetDM(variable="&VAR", expression="100")
        self.assertEqual(set_node.variable, "&VAR")
        self.assertEqual(set_node.expression, "100")

        type_node = TypeDM(messages=["Hello", "World"])
        self.assertEqual(type_node.messages, ["Hello", "World"])

        include_node = IncludeDM(filename="MYFEX.FEX")
        self.assertEqual(include_node.filename, "MYFEX.FEX")

        run_node = RunDM()
        self.assertIsInstance(run_node, RunDM)

        exit_node = ExitDM()
        self.assertIsInstance(exit_node, ExitDM)

if __name__ == '__main__':
    unittest.main()

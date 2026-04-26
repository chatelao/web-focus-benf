import unittest
from src.asg import (
    Expression, Statement, Command, MasterFile, Segment, Field,
    Goto, Label, IfDM, Repeat, SetDM, TypeDM, IncludeDM, RunDM, ExitDM,
    ReportRequest, VerbCommand, FieldSelection, SortCommand, WhereClause,
    Heading, Footing, OnCommand, ComputeCommand, Join, SetCommand, DefineFile
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

    def test_report_request_nodes(self):
        report = ReportRequest(filename="EMPLOYEE")
        self.assertEqual(report.filename, "EMPLOYEE")
        self.assertEqual(report.components, [])

        verb = VerbCommand(verb="PRINT", fields=[FieldSelection(name="LASTNAME")])
        self.assertEqual(verb.verb, "PRINT")
        self.assertEqual(verb.fields[0].name, "LASTNAME")

        sort = SortCommand(sort_type="BY", field=FieldSelection(name="DEPARTMENT"))
        self.assertEqual(sort.sort_type, "BY")
        self.assertEqual(sort.field.name, "DEPARTMENT")

        where = WhereClause(condition="SALARY GT 50000", is_total=False)
        self.assertEqual(where.condition, "SALARY GT 50000")
        self.assertFalse(where.is_total)

        heading = Heading(text="Employee Report", centered=True)
        self.assertEqual(heading.text, "Employee Report")
        self.assertTrue(heading.centered)

        footing = Footing(text="End of Report")
        self.assertEqual(footing.text, "End of Report")
        self.assertFalse(footing.centered)

        on_table = OnCommand(target="TABLE", actions=["COLUMN-TOTAL"])
        self.assertEqual(on_table.target, "TABLE")
        self.assertEqual(on_table.actions, ["COLUMN-TOTAL"])

        compute = ComputeCommand(name="BONUS", expression="SALARY * 0.1", format="D12.2")
        self.assertEqual(compute.name, "BONUS")
        self.assertEqual(compute.expression, "SALARY * 0.1")
        self.assertEqual(compute.format, "D12.2")

    def test_environment_and_virtual_field_nodes(self):
        join = Join(left_file="EMP", left_field="ID", right_file="SAL", right_field="ID", join_as="EMPSAL", outer=True)
        self.assertEqual(join.left_file, "EMP")
        self.assertEqual(join.join_as, "EMPSAL")
        self.assertTrue(join.outer)

        set_cmd = SetCommand(parameter="NODATA", value="MISSING")
        self.assertEqual(set_cmd.parameter, "NODATA")
        self.assertEqual(set_cmd.value, "MISSING")

        define = DefineFile(filename="EMPLOYEE", assignments=[{"name": "FULLNAME", "expression": "FIRSTNAME || LASTNAME"}])
        self.assertEqual(define.filename, "EMPLOYEE")
        self.assertEqual(len(define.assignments), 1)

if __name__ == '__main__':
    unittest.main()

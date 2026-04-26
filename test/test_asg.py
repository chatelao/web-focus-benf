import unittest
from src.asg import Expression, Statement, Command, MasterFile, Segment, Field

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

if __name__ == '__main__':
    unittest.main()

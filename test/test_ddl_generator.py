import unittest
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from asg import MasterFile, Segment, Field
from ddl_generator import DDLGenerator

class TestDDLGenerator(unittest.TestCase):
    def test_single_segment_ddl(self):
        # Setup
        field1 = Field(name="ID", format="A9")
        field2 = Field(name="NAME", format="A30")
        field3 = Field(name="SALARY", format="D12.2")
        segment = Segment(name="EMPLOYEE", fields=[field1, field2, field3])
        master = MasterFile(name="EMPLOYEE_MAS", segments=[segment])

        # Generate
        generator = DDLGenerator()
        ddl = generator.generate(master)

        # Verify
        expected = """CREATE TABLE EMPLOYEE (
    ID CHAR(9),
    NAME CHAR(30),
    SALARY NUMERIC(12, 2)
);"""
        self.assertEqual(ddl.strip(), expected.strip())

    def test_multi_segment_ddl(self):
        # Setup
        seg1_field1 = Field(name="DEPT_ID", format="I4")
        seg1_field2 = Field(name="DEPT_NAME", format="A20")
        seg1 = Segment(name="DEPT", fields=[seg1_field1, seg1_field2])

        seg2_field1 = Field(name="EMP_ID", format="I8")
        seg2_field2 = Field(name="EMP_NAME", format="A50")
        seg2 = Segment(name="EMP", fields=[seg2_field1, seg2_field2], parent="DEPT")

        master = MasterFile(name="CORP", segments=[seg1, seg2])

        # Generate
        generator = DDLGenerator()
        ddl = generator.generate(master)

        # Verify
        self.assertIn("CREATE TABLE DEPT", ddl)
        self.assertIn("DEPT_ID INTEGER", ddl)
        self.assertIn("CREATE TABLE EMP", ddl)
        self.assertIn("EMP_ID BIGINT", ddl)

    def test_date_types_ddl(self):
        # Setup
        f1 = Field(name="HIRE_DATE", format="YYMD")
        f2 = Field(name="LAST_UPDATE", format="HYYMDS")
        seg = Segment(name="DATES", fields=[f1, f2])
        master = MasterFile(name="DATES_MAS", segments=[seg])

        # Generate
        generator = DDLGenerator()
        ddl = generator.generate(master)

        # Verify
        self.assertIn("HIRE_DATE DATE", ddl)
        self.assertIn("LAST_UPDATE TIMESTAMP", ddl)

if __name__ == '__main__':
    unittest.main()

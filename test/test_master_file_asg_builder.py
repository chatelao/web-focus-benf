import unittest
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from master_file_parser import MasterFileParser
from master_file_asg_builder import MasterFileASGBuilder
from asg import MasterFile, Segment, Field, DefineAssignment

class TestMasterFileASGBuilder(unittest.TestCase):
    def setUp(self):
        self.parser = MasterFileParser()
        self.builder = MasterFileASGBuilder()

    def test_build_basic_asg(self):
        code = """
        FILENAME=CAR, SUFFIX=FOC,$
        SEGNAME=ORIGIN, SEGTYPE=S1,$
        FIELDNAME=COUNTRY, ALIAS=COUNTRY, USAGE=A10, FIELDTYPE=I,$
        """
        tree = self.parser.parse(code)
        master_file = self.builder.visit(tree)

        self.assertIsInstance(master_file, MasterFile)
        self.assertEqual(master_file.name, "CAR")
        self.assertEqual(master_file.suffix, "FOC")
        self.assertEqual(len(master_file.segments), 1)

        segment = master_file.segments[0]
        self.assertIsInstance(segment, Segment)
        self.assertEqual(segment.name, "ORIGIN")
        self.assertEqual(segment.segtype, "S1")
        self.assertEqual(len(segment.fields), 1)

        field = segment.fields[0]
        self.assertIsInstance(field, Field)
        self.assertEqual(field.name, "COUNTRY")
        self.assertEqual(field.alias, "COUNTRY")
        self.assertEqual(field.format, "A10")

    def test_build_complex_asg(self):
        code = """
        FILENAME=EMPLOYEE, SUFFIX=FOC, MFD_PROFILE=baseapp/DDBAEMP,$
        SEGMENT=EMPDATA, SEGTYPE=S0, $
        FIELDNAME=PIN, ALIAS=ID, USAGE=A9, INDEX=I, $
        FIELDNAME=LASTNAME, LN, A15, $
        """
        tree = self.parser.parse(code)
        master_file = self.builder.visit(tree)

        self.assertEqual(master_file.name, "EMPLOYEE")
        self.assertEqual(len(master_file.segments), 1)
        segment = master_file.segments[0]
        self.assertEqual(len(segment.fields), 2)

        pin_field = segment.fields[0]
        self.assertEqual(pin_field.name, "PIN")
        self.assertEqual(pin_field.alias, "ID")
        self.assertEqual(pin_field.format, "A9")

        ln_field = segment.fields[1]
        self.assertEqual(ln_field.name, "LASTNAME")
        self.assertEqual(ln_field.alias, "LN")
        self.assertEqual(ln_field.format, "A15")

    def test_positional_attributes(self):
        code = """
        FILENAME=CAR, FOC, $
        SEGMENT=ORIGIN, S1, $
        FIELDNAME=COUNTRY, COUNTRY, A10, $
        """
        tree = self.parser.parse(code)
        master_file = self.builder.visit(tree)

        self.assertEqual(master_file.name, "CAR")
        self.assertEqual(master_file.suffix, "FOC")

        segment = master_file.segments[0]
        self.assertEqual(segment.name, "ORIGIN")
        self.assertEqual(segment.segtype, "S1")

        field = segment.fields[0]
        self.assertEqual(field.name, "COUNTRY")
        self.assertEqual(field.alias, "COUNTRY")
        self.assertEqual(field.format, "A10")

    def test_virtual_fields(self):
        code = """
        FILENAME=EMPLOYEE, SUFFIX=FOC,$
        SEGMENT=EMPDATA, SEGTYPE=S0,$
        FIELDNAME=SALARY, USAGE=D12.2,$
        DEFINE BONUS/D12.2 = SALARY * 0.1;$
        """
        tree = self.parser.parse(code)
        master_file = self.builder.visit(tree)

        segment = master_file.segments[0]
        self.assertEqual(len(segment.virtual_fields), 1)
        vf = segment.virtual_fields[0]
        self.assertIsInstance(vf, DefineAssignment)
        self.assertEqual(vf.name, "BONUS")
        self.assertEqual(vf.format, "D12.2")
        self.assertEqual(vf.expression, "SALARY*0.1")

if __name__ == '__main__':
    unittest.main()

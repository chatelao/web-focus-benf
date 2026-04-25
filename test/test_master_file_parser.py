import unittest
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from master_file_parser import MasterFileParser
from MasterFileParser import MasterFileParser as ANTLRMasterFileParser

class TestMasterFileParser(unittest.TestCase):
    def setUp(self):
        self.parser = MasterFileParser()

    def count_nodes(self, tree, node_type):
        count = 0
        if isinstance(tree, node_type):
            count += 1
        if hasattr(tree, 'children') and tree.children:
            for child in tree.children:
                count += self.count_nodes(child, node_type)
        return count

    def test_basic_master_file(self):
        code = """
        FILENAME=CAR, SUFFIX=FOC,$
        SEGNAME=ORIGIN, SEGTYPE=S1,$
        FIELDNAME=COUNTRY, ALIAS=COUNTRY, USAGE=A10, FIELDTYPE=I,$
        """
        tree = self.parser.parse(code)
        self.assertEqual(self.count_nodes(tree, ANTLRMasterFileParser.File_declContext), 1)
        self.assertEqual(self.count_nodes(tree, ANTLRMasterFileParser.Segment_declContext), 1)
        self.assertEqual(self.count_nodes(tree, ANTLRMasterFileParser.Field_declContext), 1)

    def test_complex_master_file(self):
        code = """
        FILENAME=EMPLOYEE, SUFFIX=FOC, MFD_PROFILE=baseapp/DDBAEMP,$
        VARIABLE NAME = Emptitle, USAGE=A30, DEFAULT=EMPID,$
        SEGMENT=EMPDATA,SEGTYPE=S0, $
        FIELDNAME=PIN   , ALIAS=ID, USAGE=A9, INDEX=I,   TITLE='&&Emptitle',$
        FIELDNAME=LASTNAME,     LN,       A15,             $
        DEFINE AREA/A13=DECODE DIV (NE 'NORTH EASTERN' SE 'SOUTH EASTERN' CE 'CENTRAL' WE 'WESTERN' CORP 'CORPORATE' ELSE 'INVALID AREA');$
        """
        tree = self.parser.parse(code)
        self.assertEqual(self.count_nodes(tree, ANTLRMasterFileParser.File_declContext), 1)
        self.assertEqual(self.count_nodes(tree, ANTLRMasterFileParser.Variable_declContext), 1)
        self.assertEqual(self.count_nodes(tree, ANTLRMasterFileParser.Segment_declContext), 1)
        self.assertEqual(self.count_nodes(tree, ANTLRMasterFileParser.Field_declContext), 2)
        self.assertEqual(self.count_nodes(tree, ANTLRMasterFileParser.Define_declContext), 1)

    def test_comments(self):
        code = """
        $ This is a comment
        FILENAME=CAR, SUFFIX=FOC,$ $ Another comment
        """
        tree = self.parser.parse(code)
        self.assertEqual(self.count_nodes(tree, ANTLRMasterFileParser.File_declContext), 1)

    def test_positional_attributes(self):
        code = """
        FIELDNAME=COUNTRY, COUNTRY, A10, $
        """
        tree = self.parser.parse(code)
        self.assertEqual(self.count_nodes(tree, ANTLRMasterFileParser.Field_declContext), 1)

if __name__ == '__main__':
    unittest.main()

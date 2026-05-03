import unittest
import os
import tempfile
import shutil
import sys
from antlr4 import *

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
from symbol_resolver import SymbolResolver
from metadata_registry import MetadataRegistry
import asg

class TestJoinedSymbolResolution(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.registry = MetadataRegistry([self.test_dir])

        # Create CAR Master File
        car_mas = """
FILENAME=CAR, SUFFIX=FOC,$
  SEGNAME=ORIGIN, SEGTYPE=S1,$
    FIELDNAME=COUNTRY, ALIAS=COUNTRY, FORMAT=A10,$
"""
        with open(os.path.join(self.test_dir, "CAR.mas"), 'w') as f:
            f.write(car_mas)

        # Create SALES Master File
        sales_mas = """
FILENAME=SALES, SUFFIX=FOC,$
  SEGNAME=SALES, SEGTYPE=S1,$
    FIELDNAME=CAR, ALIAS=CAR, FORMAT=A16,$
    FIELDNAME=RETAIL_PRICE, ALIAS=RP, FORMAT=D12.2,$
"""
        with open(os.path.join(self.test_dir, "SALES.mas"), 'w') as f:
            f.write(sales_mas)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def build_asg(self, text):
        input_stream = InputStream(text)
        lexer = WebFocusReportLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(stream)
        tree = parser.start()
        builder = ReportASGBuilder()
        return builder.visit(tree)

    def test_joined_field_resolution(self):
        code = """
        JOIN CAR IN CAR TO CAR IN SALES AS J1
        TABLE FILE CAR
        PRINT COUNTRY AND J1.RETAIL_PRICE
        END
        """
        asg_nodes = self.build_asg(code)
        resolver = SymbolResolver(metadata_registry=self.registry)
        resolver.resolve(asg_nodes)

        # asg_nodes[0] is Join
        # asg_nodes[1] is ReportRequest
        report = asg_nodes[1]
        verb = report.components[0]

        country_field = verb.fields[0]
        self.assertEqual(country_field.name, "COUNTRY")
        self.assertIsNotNone(country_field.symbol, "COUNTRY field should be resolved")

        rp_field = verb.fields[1]
        self.assertEqual(rp_field.name, "J1.RETAIL_PRICE")
        self.assertIsNotNone(rp_field.symbol, "J1.RETAIL_PRICE field should be resolved")
        self.assertEqual(rp_field.symbol.symbol_type, "FIELD")

if __name__ == '__main__':
    unittest.main()

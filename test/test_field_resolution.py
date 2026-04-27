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
from symbol_table import SymbolTable
import asg

class TestFieldResolution(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.registry = MetadataRegistry([self.test_dir])

        # Create a sample Master File
        mas_content = """
FILENAME=CAR, SUFFIX=FOC,$
  SEGNAME=ORIGIN, SEGTYPE=S1,$
    FIELDNAME=COUNTRY, ALIAS=COUNTRY, FORMAT=A10,$
  SEGNAME=COMP, PARENT=ORIGIN, SEGTYPE=S1,$
    FIELDNAME=CAR, ALIAS=C, FORMAT=A16,$
    FIELDNAME=MODEL, ALIAS=M, FORMAT=A24,$
"""
        with open(os.path.join(self.test_dir, "CAR.mas"), 'w') as f:
            f.write(mas_content)

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

    def test_basic_field_resolution(self):
        code = """
        TABLE FILE CAR
        PRINT CAR AND MODEL
        END
        """
        asg_nodes = self.build_asg(code)
        resolver = SymbolResolver(metadata_registry=self.registry)
        resolver.resolve(asg_nodes)

        report = asg_nodes[0]
        self.assertIsInstance(report, asg.ReportRequest)
        self.assertIsNotNone(report.master_file)
        self.assertEqual(report.master_file.name, "CAR")

        verb = report.components[0]
        self.assertIsInstance(verb, asg.VerbCommand)

        car_field = verb.fields[0]
        self.assertEqual(car_field.name, "CAR")
        self.assertIsNotNone(car_field.symbol)
        self.assertEqual(car_field.symbol.symbol_type, "FIELD")

        model_field = verb.fields[1]
        self.assertEqual(model_field.name, "MODEL")
        self.assertIsNotNone(model_field.symbol)

    def test_qualified_field_resolution(self):
        code = """
        TABLE FILE CAR
        PRINT ORIGIN.COUNTRY AND COMP.CAR
        END
        """
        asg_nodes = self.build_asg(code)
        resolver = SymbolResolver(metadata_registry=self.registry)
        resolver.resolve(asg_nodes)

        report = asg_nodes[0]
        verb = report.components[0]

        country_field = verb.fields[0]
        self.assertEqual(country_field.name, "ORIGIN.COUNTRY")
        self.assertIsNotNone(country_field.symbol)

        car_field = verb.fields[1]
        self.assertEqual(car_field.name, "COMP.CAR")
        self.assertIsNotNone(car_field.symbol)

    def test_define_file_resolution(self):
        code = """
        DEFINE FILE CAR
        MY_VIRTUAL = CAR;
        END
        TABLE FILE CAR
        PRINT MY_VIRTUAL
        END
        """
        asg_nodes = self.build_asg(code)
        resolver = SymbolResolver(metadata_registry=self.registry)
        resolver.resolve(asg_nodes)

        # First node is DefineFile
        define_file = asg_nodes[0]
        self.assertIsInstance(define_file, asg.DefineFile)

        # Second node is ReportRequest
        report = asg_nodes[1]
        verb = report.components[0]
        virtual_field_usage = verb.fields[0]

        self.assertEqual(virtual_field_usage.name, "MY_VIRTUAL")
        self.assertIsNotNone(virtual_field_usage.symbol)
        self.assertEqual(virtual_field_usage.symbol.symbol_type, "VIRTUAL_FIELD")

    def test_compute_resolution(self):
        code = """
        TABLE FILE CAR
        SUM SALES
        COMPUTE MY_CALC = SALES * 2;
        PRINT MY_CALC
        END
        """
        # Note: 'SALES' is not in my CAR.mas above, but COMPUTE will define 'MY_CALC'
        # Let's add SALES to CAR.mas for completeness
        with open(os.path.join(self.test_dir, "CAR.mas"), 'a') as f:
            f.write("    FIELDNAME=SALES, ALIAS=S, FORMAT=I8,$\n")

        # Need to clear cache or use a fresh registry because I modified the file
        self.registry.clear_cache()

        asg_nodes = self.build_asg(code)
        resolver = SymbolResolver(metadata_registry=self.registry)
        resolver.resolve(asg_nodes)

        report = asg_nodes[0]

        # Components: 0: Verb(SUM), 1: ComputeCommand, 2: Verb(PRINT)
        compute_cmd = report.components[1]
        self.assertIsInstance(compute_cmd, asg.ComputeCommand)

        print_cmd = report.components[2]
        calc_usage = print_cmd.fields[0]

        self.assertEqual(calc_usage.name, "MY_CALC")
        self.assertIsNotNone(calc_usage.symbol)
        self.assertEqual(calc_usage.symbol.symbol_type, "VIRTUAL_FIELD")

    def test_compute_scoping(self):
        code = """
        TABLE FILE CAR
        COMPUTE LOCAL_VAR = 1;
        END
        TABLE FILE CAR
        PRINT LOCAL_VAR
        END
        """
        asg_nodes = self.build_asg(code)
        resolver = SymbolResolver(metadata_registry=self.registry)
        resolver.resolve(asg_nodes)

        report2 = asg_nodes[1]
        print_cmd = report2.components[0]
        local_var_usage = print_cmd.fields[0]

        self.assertEqual(local_var_usage.name, "LOCAL_VAR")
        self.assertIsNone(local_var_usage.symbol) # Should be None because it was defined in another request's scope

if __name__ == '__main__':
    unittest.main()

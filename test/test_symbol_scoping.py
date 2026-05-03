import unittest
import sys
import os
import tempfile
import shutil
from antlr4 import *

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
from symbol_resolver import SymbolResolver
from symbol_table import SymbolTable
from metadata_registry import MetadataRegistry
import asg

class TestSymbolScoping(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.registry = MetadataRegistry([self.test_dir])

        # Create a sample Master File
        mas_content = """
FILENAME=CAR, SUFFIX=FOC,$
  SEGNAME=ORIGIN, SEGTYPE=S1,$
    FIELDNAME=COUNTRY, ALIAS=COUNTRY, FORMAT=A10,$
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

    def test_ampervar_global_scope(self):
        code = """
        -SET &OUTER = 1;
        TABLE FILE CAR
        -SET &INNER = 2;
        PRINT CAR
        END
        -TYPE &OUTER &INNER
        """
        asg_nodes = self.build_asg(code)
        resolver = SymbolResolver()
        st = resolver.resolve(asg_nodes)

        # Both should be in the global scope (or at least resolvable at the end)
        self.assertIsNotNone(st.lookup("&OUTER"))
        self.assertIsNotNone(st.lookup("&INNER"))

        # The last node is TypeDM
        type_node = asg_nodes[-1]
        self.assertIsInstance(type_node, asg.TypeDM)

        outer_usage = type_node.messages[0]
        self.assertIsNotNone(outer_usage.symbol, "OUTER should be resolved")

        inner_usage = type_node.messages[1]
        self.assertIsNotNone(inner_usage.symbol, "INNER should be resolved")

    def test_ampervar_scoping_with_metadata(self):
        code = """
        TABLE FILE CAR
        -SET &REPORT_VAR = 10;
        PRINT COUNTRY
        END
        -TYPE &REPORT_VAR
        """
        asg_nodes = self.build_asg(code)
        resolver = SymbolResolver(metadata_registry=self.registry)
        st = resolver.resolve(asg_nodes)

        # Currently, &REPORT_VAR is defined while visit_ReportRequest has entered a new scope.
        # When visit_ReportRequest finishes, it exits the scope.
        # If &REPORT_VAR was defined in that nested scope, it won't be available globally.

        self.assertIsNotNone(st.lookup("&REPORT_VAR"), "&REPORT_VAR should be in global scope")

        type_node = asg_nodes[-1]
        self.assertIsInstance(type_node, asg.TypeDM)

        var_usage = type_node.messages[0]
        self.assertIsNotNone(var_usage.symbol, "REPORT_VAR should be resolved in TYPE command after report")

if __name__ == '__main__':
    unittest.main()

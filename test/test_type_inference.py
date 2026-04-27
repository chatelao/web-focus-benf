import unittest
import os
import sys
from antlr4 import *

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
from symbol_resolver import SymbolResolver
from type_inferrer import TypeInferrer
import asg

class TestTypeInference(unittest.TestCase):
    def build_asg(self, text):
        input_stream = InputStream(text)
        lexer = WebFocusReportLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(stream)
        tree = parser.start()
        builder = ReportASGBuilder()
        return builder.visit(tree)

    def test_literal_inference(self):
        nodes = self.build_asg("-SET &X = 1; -SET &Y = 1.5; -SET &Z = 'HELLO';")
        inferrer = TypeInferrer()
        inferrer.infer(nodes)

        self.assertEqual(nodes[0].expression.data_type, 'I')
        self.assertEqual(nodes[1].expression.data_type, 'F')
        self.assertEqual(nodes[2].expression.data_type, 'A')

    def test_arithmetic_inference(self):
        nodes = self.build_asg("-SET &X = 1 + 2; -SET &Y = 1 + 1.5; -SET &Z = 1.5 / 2.0;")
        inferrer = TypeInferrer()
        inferrer.infer(nodes)

        self.assertEqual(nodes[0].expression.data_type, 'I')
        self.assertEqual(nodes[1].expression.data_type, 'F')
        self.assertEqual(nodes[2].expression.data_type, 'F')

    def test_logical_inference(self):
        nodes = self.build_asg("-SET &X = (1 EQ 1) AND (2 GT 1);")
        inferrer = TypeInferrer()
        inferrer.infer(nodes)

        self.assertEqual(nodes[0].expression.data_type, 'LOGICAL')

    def test_concat_inference(self):
        nodes = self.build_asg("-SET &X = 'A' | 'B';")
        inferrer = TypeInferrer()
        inferrer.infer(nodes)

        self.assertEqual(nodes[0].expression.data_type, 'A')

    def test_if_expression_inference(self):
        nodes = self.build_asg("-SET &X = IF 1 EQ 1 THEN 10 ELSE 20.5;")
        inferrer = TypeInferrer()
        inferrer.infer(nodes)

        self.assertEqual(nodes[0].expression.data_type, 'F')

    def test_function_inference(self):
        nodes = self.build_asg("-SET &X = ABS(-10); -SET &Y = SQRT(16); -SET &Z = UPCASE('hello');")
        inferrer = TypeInferrer()
        inferrer.infer(nodes)

        self.assertEqual(nodes[0].expression.data_type, 'I')
        self.assertEqual(nodes[1].expression.data_type, 'F')
        self.assertEqual(nodes[2].expression.data_type, 'A')

    def test_relational_expressions(self):
        code = """
        TABLE FILE CAR
        WHERE SALES FROM 10 TO 20
        WHERE COUNTRY IN ('ENGLAND', 'FRANCE')
        WHERE MODEL IS MISSING
        END
        """
        nodes = self.build_asg(code)
        inferrer = TypeInferrer()
        inferrer.infer(nodes)

        report = nodes[0]
        # WHERE clauses are components
        self.assertEqual(report.components[0].condition.data_type, 'LOGICAL') # Between
        self.assertEqual(report.components[1].condition.data_type, 'LOGICAL') # In
        self.assertEqual(report.components[2].condition.data_type, 'LOGICAL') # IsMissing

if __name__ == '__main__':
    unittest.main()

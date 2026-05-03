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

    def test_precision_inference_from_metadata(self):
        from symbol_table import Symbol

        # Manually create nodes with symbol and metadata
        field_node = asg.Identifier(name="LARGE_INT")
        field_node.symbol = Symbol(name="LARGE_INT", scope=None)
        field_node.symbol.metadata = {'field': asg.Field(name="LARGE_INT", format="I8")}

        field_node2 = asg.Identifier(name="PREC_NUM")
        field_node2.symbol = Symbol(name="PREC_NUM", scope=None)
        field_node2.symbol.metadata = {'field': asg.Field(name="PREC_NUM", format="P9.2")}

        inferrer = TypeInferrer()
        self.assertEqual(inferrer.visit(field_node), 'I8')
        self.assertEqual(inferrer.visit(field_node2), 'P9.2')

        # Arithmetic with I8
        expr = asg.BinaryOperation(field_node, '+', asg.Literal(1))
        self.assertEqual(inferrer.visit(expr), 'I8')

        # Arithmetic with P9.2
        expr2 = asg.BinaryOperation(field_node2, '*', asg.Literal(2.0))
        self.assertEqual(inferrer.visit(expr2), 'P9.2')

if __name__ == '__main__':
    unittest.main()

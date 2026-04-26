import unittest
from antlr4 import *
from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
import asg

class TestASGBuilder(unittest.TestCase):
    def build_asg(self, text):
        input_stream = InputStream(text)
        lexer = WebFocusReportLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(stream)
        tree = parser.start()
        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)
        return asg_nodes

    def test_dm_set_literal(self):
        code = "-SET &VAR = 10;"
        asg_nodes = self.build_asg(code)
        self.assertEqual(len(asg_nodes), 1)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.SetDM))
        self.assertEqual(node.variable, "&VAR")
        self.assertTrue(isinstance(node.expression, asg.Literal))
        self.assertEqual(node.expression.value, 10)

    def test_dm_set_expression(self):
        code = "-SET &VAR = 1 + 2 * 3;"
        asg_nodes = self.build_asg(code)
        self.assertEqual(len(asg_nodes), 1)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.SetDM))
        expr = node.expression
        self.assertTrue(isinstance(expr, asg.BinaryOperation))
        self.assertEqual(expr.operator, "+")
        self.assertTrue(isinstance(expr.left, asg.Literal))
        self.assertEqual(expr.left.value, 1)
        self.assertTrue(isinstance(expr.right, asg.BinaryOperation))
        self.assertEqual(expr.right.operator, "*")

    def test_dm_type(self):
        code = "-TYPE Hello World &VAR"
        asg_nodes = self.build_asg(code)
        self.assertEqual(len(asg_nodes), 1)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.TypeDM))
        self.assertEqual(len(node.messages), 3)
        self.assertEqual(node.messages[0], "Hello")
        self.assertEqual(node.messages[1], "World")
        self.assertEqual(node.messages[2], "&VAR")

    def test_dm_set_string(self):
        code = "-SET &VAR = 'TEXT';"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertEqual(node.expression.value, "TEXT")

    def test_dm_logical_expression(self):
        code = "-SET &VAR = &X EQ 1 AND &Y GT 2;"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        expr = node.expression
        self.assertTrue(isinstance(expr, asg.BinaryOperation))
        self.assertEqual(expr.operator, "AND")

if __name__ == '__main__':
    unittest.main()

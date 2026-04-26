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

    def test_dm_goto(self):
        code = "-GOTO MYLABEL;"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.Goto))
        self.assertEqual(node.target, "MYLABEL")

    def test_dm_label(self):
        code = "-MYLABEL"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.Label))
        self.assertEqual(node.name, "MYLABEL")

    def test_dm_if(self):
        code = "-IF &X EQ 1 GOTO LABEL1 ELSE GOTO LABEL2;"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.IfDM))
        self.assertEqual(node.then_target, "LABEL1")
        self.assertEqual(node.else_target, "LABEL2")

    def test_dm_include(self):
        code = "-INCLUDE GGHDR.FEX"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.IncludeDM))
        self.assertEqual(node.filename, "GGHDR.FEX")

    def test_dm_run_exit(self):
        code = "-RUN\n-EXIT"
        asg_nodes = self.build_asg(code)
        self.assertEqual(len(asg_nodes), 2)
        self.assertTrue(isinstance(asg_nodes[0], asg.RunDM))
        self.assertTrue(isinstance(asg_nodes[1], asg.ExitDM))

    def test_dm_repeat_while(self):
        code = "-REPEAT LOOP1 WHILE &X LT 10;"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.Repeat))
        self.assertEqual(node.label, "LOOP1")
        self.assertEqual(node.condition_type, "WHILE")

    def test_dm_repeat_for(self):
        code = "-REPEAT LOOP2 FOR &I FROM 1 TO 10 STEP 1;"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.Repeat))
        self.assertEqual(node.loop_var, "&I")
        self.assertEqual(node.start_val.value, 1)
        self.assertEqual(node.end_val.value, 10)
        self.assertEqual(node.step_val.value, 1)

    def test_dm_if_expression(self):
        code = "-SET &VAR = IF &X EQ 1 THEN 'YES' ELSE 'NO';"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        expr = node.expression
        self.assertTrue(isinstance(expr, asg.IfExpression))
        self.assertEqual(expr.then_expr.value, "YES")
        self.assertEqual(expr.else_expr.value, "NO")

    def test_dm_concat_expression(self):
        code = "-SET &VAR = 'A' | 'B' || 'C';"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        expr = node.expression
        self.assertTrue(isinstance(expr, asg.BinaryOperation))
        self.assertEqual(expr.operator, "||")
        self.assertTrue(isinstance(expr.left, asg.BinaryOperation))
        self.assertEqual(expr.left.operator, "|")

if __name__ == '__main__':
    unittest.main()

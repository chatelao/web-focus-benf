import unittest
from antlr4 import *
from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
from symbol_resolver import SymbolResolver
import asg

class TestSymbolResolution(unittest.TestCase):
    def build_asg(self, text):
        input_stream = InputStream(text)
        lexer = WebFocusReportLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(stream)
        tree = parser.start()
        builder = ReportASGBuilder()
        return builder.visit(tree)

    def test_dm_variable_resolution(self):
        code = """
        -SET &VAR1 = 10;
        -SET &VAR2 = &VAR1 + 5;
        """
        asg_nodes = self.build_asg(code)
        resolver = SymbolResolver()
        st = resolver.resolve(asg_nodes)

        # Verify definitions in symbol table
        self.assertIsNotNone(st.lookup("&VAR1"))
        self.assertIsNotNone(st.lookup("&VAR2"))

        # Verify resolution in ASG node
        set2_node = asg_nodes[1]
        self.assertTrue(isinstance(set2_node, asg.SetDM))
        expr = set2_node.expression
        self.assertTrue(isinstance(expr, asg.BinaryOperation))
        var1_usage = expr.left
        self.assertTrue(isinstance(var1_usage, asg.AmperVar))
        self.assertIsNotNone(var1_usage.symbol)
        self.assertEqual(var1_usage.symbol.name, "&VAR1")

    def test_dm_repeat_loop_var_resolution(self):
        code = """
        -REPEAT LOOP1 FOR &I FROM 1 TO 10;
        -TYPE &I
        """
        asg_nodes = self.build_asg(code)
        resolver = SymbolResolver()
        st = resolver.resolve(asg_nodes)

        self.assertIsNotNone(st.lookup("&I"))

        type_node = asg_nodes[1]
        self.assertTrue(isinstance(type_node, asg.TypeDM))
        i_usage = type_node.messages[0]
        self.assertTrue(isinstance(i_usage, asg.AmperVar))
        self.assertIsNotNone(i_usage.symbol)
        self.assertEqual(i_usage.symbol.name, "&I")

    def test_external_parameter_unresolved(self):
        code = "-SET &VAR = &PARAM + 1;"
        asg_nodes = self.build_asg(code)
        resolver = SymbolResolver()
        resolver.resolve(asg_nodes)

        set_node = asg_nodes[0]
        param_usage = set_node.expression.left
        self.assertTrue(isinstance(param_usage, asg.AmperVar))
        self.assertIsNone(param_usage.symbol) # Not defined yet

if __name__ == '__main__':
    unittest.main()

import unittest
from antlr4 import *
from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
import asg

class TestSummarizationASG(unittest.TestCase):
    def build_asg(self, text):
        input_stream = InputStream(text)
        lexer = WebFocusReportLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(stream)
        tree = parser.start()
        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)
        return asg_nodes

    def test_by_with_subtotal(self):
        code = "TABLE FILE CAR\nPRINT MODEL\nBY COUNTRY SUBTOTAL\nEND"
        asg_nodes = self.build_asg(code)
        request = asg_nodes[0]
        by_command = request.components[1]
        self.assertTrue(isinstance(by_command, asg.SortCommand))
        self.assertEqual(by_command.sort_type, "BY")
        self.assertIsNotNone(by_command.summarize)
        self.assertEqual(by_command.summarize.verb, "SUBTOTAL")

    def test_by_with_noprint(self):
        code = "TABLE FILE CAR\nPRINT MODEL\nBY COUNTRY NOPRINT\nEND"
        asg_nodes = self.build_asg(code)
        request = asg_nodes[0]
        by_command = request.components[1]
        self.assertTrue(by_command.noprint)

    def test_by_with_subtotal_options(self):
        code = "TABLE FILE CAR\nPRINT MODEL\nBY COUNTRY SUBTOTAL ROLL. AVE. SALES AS 'Avg Sales'\nEND"
        asg_nodes = self.build_asg(code)
        request = asg_nodes[0]
        by_command = request.components[1]
        summarize = by_command.summarize
        self.assertEqual(summarize.verb, "SUBTOTAL")
        self.assertTrue(summarize.options["roll"])
        self.assertEqual(summarize.options["prefixes"], ["AVE"])
        self.assertEqual(summarize.field, "SALES")
        self.assertEqual(summarize.alias, "Avg Sales")

    def test_on_table_column_total(self):
        code = "TABLE FILE CAR\nPRINT MODEL\nON TABLE COLUMN-TOTAL\nEND"
        asg_nodes = self.build_asg(code)
        request = asg_nodes[0]
        on_command = request.components[1]
        self.assertTrue(isinstance(on_command, asg.OnCommand))
        self.assertEqual(on_command.target, "TABLE")
        action = on_command.actions[0]
        self.assertTrue(isinstance(action, asg.SetCommand))
        self.assertEqual(action.parameter, "COLUMN-TOTAL")
        self.assertEqual(action.value, "ON")

    def test_on_field_subtotal(self):
        code = "TABLE FILE CAR\nPRINT MODEL\nBY COUNTRY\nON COUNTRY SUBTOTAL\nEND"
        asg_nodes = self.build_asg(code)
        request = asg_nodes[0]
        on_command = request.components[2]
        self.assertEqual(on_command.target, "COUNTRY")
        action = on_command.actions[0]
        self.assertTrue(isinstance(action, asg.SummarizeCommand))
        self.assertEqual(action.verb, "SUBTOTAL")

    def test_on_field_subhead(self):
        code = "TABLE FILE CAR\nPRINT MODEL\nBY COUNTRY\nON COUNTRY SUBHEAD 'Header for <COUNTRY'\nEND"
        asg_nodes = self.build_asg(code)
        request = asg_nodes[0]
        on_command = request.components[2]
        action = on_command.actions[0]
        self.assertTrue(isinstance(action, asg.Subhead))
        self.assertEqual(action.text, "Header for <COUNTRY")

    def test_on_table_hold(self):
        code = "TABLE FILE CAR\nPRINT MODEL\nON TABLE HOLD AS MYFILE FORMAT FOCUS\nEND"
        asg_nodes = self.build_asg(code)
        request = asg_nodes[0]
        on_command = request.components[1]
        action = on_command.actions[0]
        self.assertTrue(isinstance(action, asg.OutputCommand))
        self.assertEqual(action.output_type, "HOLD")
        self.assertEqual(action.filename, "MYFILE")
        self.assertEqual(action.format, "FOCUS")

if __name__ == '__main__':
    unittest.main()

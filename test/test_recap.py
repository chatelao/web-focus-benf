import unittest
from antlr4 import CommonTokenStream, InputStream
from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
import asg

class TestRecapParsing(unittest.TestCase):
    def parse_fex(self, fex_content):
        input_stream = InputStream(fex_content)
        lexer = WebFocusReportLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(token_stream)
        tree = parser.start()
        builder = ReportASGBuilder()
        return builder.visit(tree)

    def test_recap_in_on_phrase(self):
        fex = """
        TABLE FILE GGSALES
        SUM DOLLARS
        BY REGION
        ON REGION RECAP DEPT_NET/D8.2M = DOLLARS - 100; AS 'Net Earnings'
        END
        """
        nodes = self.parse_fex(fex)
        self.assertEqual(len(nodes), 1)
        report = nodes[0]
        self.assertIsInstance(report, asg.ReportRequest)

        on_command = next(c for c in report.components if isinstance(c, asg.OnCommand))
        self.assertEqual(on_command.target, "REGION")

        recap = on_command.actions[0]
        self.assertIsInstance(recap, asg.RecapCommand)
        self.assertEqual(len(recap.assignments), 1)

        assign = recap.assignments[0]
        self.assertEqual(assign.name, "DEPT_NET")
        self.assertEqual(assign.format, "D8.2M")
        self.assertEqual(assign.alias, "Net Earnings")
        self.assertIsInstance(assign.expression, asg.BinaryOperation)

    def test_multiple_recap_assignments(self):
        fex = """
        TABLE FILE GGSALES
        SUM DOLLARS
        BY REGION
        ON REGION RECAP
          NET = DOLLARS - 100;
          TAX = NET * 0.1;
        END
        """
        nodes = self.parse_fex(fex)
        report = nodes[0]
        on_command = next(c for c in report.components if isinstance(c, asg.OnCommand))
        recap = on_command.actions[0]
        self.assertEqual(len(recap.assignments), 2)
        self.assertEqual(recap.assignments[0].name, "NET")
        self.assertEqual(recap.assignments[1].name, "TAX")

    def test_recap_with_column_ref(self):
        # FML style RECAP
        fex = """
        TABLE FILE GGSALES
        SUM DOLLARS
        BY REGION
        ON REGION RECAP PROFIT(2) = TOTAL(1) - TOTAL(2); INDENT 5 AS 'Profit'
        END
        """
        nodes = self.parse_fex(fex)
        report = nodes[0]
        on_command = next(c for c in report.components if isinstance(c, asg.OnCommand))
        recap = on_command.actions[0]
        assign = recap.assignments[0]

        self.assertEqual(assign.name, "PROFIT")
        self.assertIsInstance(assign.column_ref, asg.Literal)
        self.assertEqual(assign.column_ref.value, 2)
        self.assertEqual(assign.indent, 5)
        self.assertEqual(assign.alias, "Profit")

        expr = assign.expression
        self.assertIsInstance(expr, asg.BinaryOperation)
        self.assertIsInstance(expr.left, asg.FunctionCall) # TOTAL(1) is parsed as FunctionCall in current dm_primary
        self.assertEqual(expr.left.function_name, "TOTAL")

    def test_standalone_recap(self):
        fex = """
        TABLE FILE GGSALES
        SUM DOLLARS
        RECAP TOTAL_SALES = DOLLARS;
        END
        """
        nodes = self.parse_fex(fex)
        report = nodes[0]
        recap = next(c for c in report.components if isinstance(c, asg.RecapCommand))
        self.assertEqual(recap.assignments[0].name, "TOTAL_SALES")

if __name__ == "__main__":
    unittest.main()

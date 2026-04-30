import unittest
from antlr4 import InputStream, CommonTokenStream
from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
import asg

class TestHierarchicalProcedural(unittest.TestCase):
    def parse_to_asg(self, text):
        input_stream = InputStream(text)
        lexer = WebFocusReportLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(stream)
        tree = parser.start()
        builder = ReportASGBuilder()
        return builder.visit(tree)

    def test_hierarchical_report_parsing(self):
        fex = """
        TABLE FILE NEWGL
        SUM GL_ACCOUNT_AMOUNT
        BY GL_ACCOUNT_CAPTION HIERARCHY
        WHEN GL_ACCOUNT GT '2000' AND GL_ACCOUNT LT '3000';
         SHOW UP 1 TO DOWN 1
        ON TABLE SET PAGE NOPAGE
        ON TABLE SET STYLE *
        TYPE=REPORT,GRID=OFF,$
        ENDSTYLE
        END
        """
        nodes = self.parse_to_asg(fex)
        self.assertEqual(len(nodes), 1)
        request = nodes[0]
        self.assertIsInstance(request, asg.ReportRequest)
        self.assertEqual(request.filename, "NEWGL")

        # BY ... HIERARCHY
        by_cmd = next(c for c in request.components if isinstance(c, asg.SortCommand))
        self.assertEqual(by_cmd.field.name, "GL_ACCOUNT_CAPTION")
        self.assertTrue(by_cmd.is_hierarchy)

        # WHEN clause
        when_cmd = next(c for c in request.components if isinstance(c, asg.WhenCommand))
        self.assertIsInstance(when_cmd.condition, asg.BinaryOperation)
        self.assertEqual(when_cmd.condition.operator, "AND")

        # SHOW UP 1 TO DOWN 1
        show_cmd = next(c for c in request.components if isinstance(c, asg.ShowCommand))
        self.assertEqual(show_cmd.from_direction, "UP")
        self.assertEqual(show_cmd.from_value.value, 1)
        self.assertEqual(show_cmd.to_direction, "DOWN")
        self.assertEqual(show_cmd.to_value.value, 1)

if __name__ == "__main__":
    unittest.main()

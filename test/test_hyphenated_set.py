import unittest
from antlr4 import *
from src.WebFocusReportLexer import WebFocusReportLexer
from src.WebFocusReportParser import WebFocusReportParser
from src.asg_builder import ReportASGBuilder

class TestHyphenatedSet(unittest.TestCase):
    def parse_asg(self, text):
        input_stream = InputStream(text)
        lexer = WebFocusReportLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(stream)
        tree = parser.start()
        builder = ReportASGBuilder()
        return builder.visit(tree)

    def test_hyphenated_set_with_eq(self):
        # Currently expected to fail because ONLINE-FMT is not a valid NAME
        code = "SET ONLINE-FMT = PDF;"
        asg = self.parse_asg(code)
        self.assertEqual(len(asg), 1)
        self.assertEqual(asg[0].parameter, "ONLINE-FMT")
        self.assertEqual(asg[0].value, "PDF")

    def test_hyphenated_set_without_eq(self):
        # Currently expected to fail because EQ is mandatory in grammar
        code = "SET ONLINE-FMT PDF;"
        asg = self.parse_asg(code)
        self.assertEqual(len(asg), 1)
        self.assertEqual(asg[0].parameter, "ONLINE-FMT")
        self.assertEqual(asg[0].value, "PDF")

if __name__ == "__main__":
    unittest.main()

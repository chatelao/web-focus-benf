import unittest
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from src.WebFocusReportLexer import WebFocusReportLexer
from src.WebFocusReportParser import WebFocusReportParser

class TestAntlrWebFocusParser(unittest.TestCase):
    def parse(self, text):
        input_stream = InputStream(text)
        lexer = WebFocusReportLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(stream)
        # Add error listener to raise exception on failure
        parser.removeErrorListeners()
        class FailErrorListener(ErrorListener):
            def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
                raise Exception(f"Syntax error at {line}:{column}: {msg}")
        parser.addErrorListener(FailErrorListener())
        return parser.start()

    def test_summarization_commands(self):
        variations = [
            "TABLE FILE EMPDATA SUM SALARY BY DEPARTMENT SUBTOTAL END",
            "TABLE FILE EMPDATA SUM SALARY BY DEPARTMENT SUB-TOTAL END",
            "TABLE FILE EMPDATA SUM SALARY BY DEPARTMENT SUMMARIZE END",
            "TABLE FILE EMPDATA SUM SALARY BY DEPARTMENT RECOMPUTE END",
            "TABLE FILE EMPDATA SUM SALARY ON DEPARTMENT SUBTOTAL END",
            "TABLE FILE EMPDATA SUM SALARY ON DEPARTMENT SUBTOTAL AVE. SALARY END",
            "TABLE FILE EMPDATA SUM SALARY ON DEPARTMENT SUBTOTAL AVE. SALARY AS 'Average' END",
            "TABLE FILE EMPDATA SUM SALARY ON DEPARTMENT SUBTOTAL ROLL.AVE. SALARY END",
            "TABLE FILE EMPDATA SUM SALARY ON TABLE SUBTOTAL END",
            "TABLE FILE EMPDATA SUM SALARY ON TABLE COLUMN-TOTAL END",
            "TABLE FILE EMPDATA SUM SALARY ON TABLE ROW-TOTAL END"
        ]
        for code in variations:
            try:
                self.parse(code)
            except Exception as e:
                self.fail(f"Failed to parse summarization command '{code}': {e}")

    def test_output_commands(self):
        variations = [
            "TABLE FILE EMPDATA SUM SALARY ON TABLE HOLD END",
            "TABLE FILE EMPDATA SUM SALARY ON TABLE PCHOLD END",
            "TABLE FILE EMPDATA SUM SALARY ON TABLE SAVE END",
            "TABLE FILE EMPDATA SUM SALARY ON TABLE SAVB END",
            "TABLE FILE EMPDATA SUM SALARY ON TABLE HOLD AS MYFILE END",
            "TABLE FILE EMPDATA SUM SALARY ON TABLE HOLD FORMAT ALPHA END",
            "TABLE FILE EMPDATA SUM SALARY ON TABLE HOLD AS MYFILE FORMAT FOCUS END"
        ]
        for code in variations:
            try:
                self.parse(code)
            except Exception as e:
                self.fail(f"Failed to parse output command '{code}': {e}")

if __name__ == '__main__':
    unittest.main()

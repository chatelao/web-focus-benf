import unittest
import os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from src.WebFocusReportLexer import WebFocusReportLexer
from src.WebFocusReportParser import WebFocusReportParser

class TestEducationalSamples(unittest.TestCase):
    def parse(self, text):
        input_stream = InputStream(text)
        lexer = WebFocusReportLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(stream)
        parser.removeErrorListeners()
        class FailErrorListener(ErrorListener):
            def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
                raise Exception(f"Syntax error at {line}:{column}: {msg}")
        parser.addErrorListener(FailErrorListener())
        return parser.start()

    def test_educational_samples(self):
        samples_dir = 'test/educational_samples'
        if not os.path.exists(samples_dir):
            self.skipTest("Educational samples directory not found")

        for filename in sorted(os.listdir(samples_dir)):
            if filename.endswith('.fex'):
                filepath = os.path.join(samples_dir, filename)
                with open(filepath, 'r') as f:
                    code = f.read()
                with self.subTest(filename=filename):
                    try:
                        self.parse(code)
                    except Exception as e:
                        self.fail(f"Failed to parse {filename}: {e}")

if __name__ == '__main__':
    unittest.main()

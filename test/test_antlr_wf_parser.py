import unittest
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from src.WebFocusReportLexer import WebFocusReportLexer
from src.WebFocusReportParser import WebFocusReportParser
import os

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
            with self.subTest(code=code):
                self.parse(code)

    def test_define_file(self):
        variations = [
            "DEFINE FILE EMPDATA MYFIELD = SALARY * 1.1; END",
            "DEFINE FILE GGSALES BONUS/D12.2 = DOLLARS * 0.1; END",
            "DEFINE FILE CAR NEW_C/A20 = COUNTRY | CAR; FLAG/A1 = 'Y'; END",
            "DEFINE FILE EMPDATA PREC = 1 + 2 * 3; END",
            "DEFINE FILE EMPDATA PREC2 = (1 + 2) * 3; END",
            "DEFINE FILE EMPDATA ABS_VAL = ABS(SALARY); END",
            "DEFINE FILE EMPDATA MULTI_ARG = MAX(SALARY, 50000); END",
            "DEFINE FILE EMPDATA NO_ARG = GET_DATE(); END"
        ]
        for code in variations:
            with self.subTest(code=code):
                self.parse(code)

    def test_compute_commands(self):
        variations = [
            "TABLE FILE EMPDATA SUM SALARY COMPUTE RATIO = SALARY / 1000; END",
            "TABLE FILE EMPDATA SUM SALARY COMPUTE BONUS/D12.2 = SALARY * 0.1; END",
            "TABLE FILE EMPDATA SUM SALARY BY DEPT COMPUTE DEPT_AVG = AVE.SALARY; END",
            "TABLE FILE EMPDATA SUM SALARY COMPUTE FLAG/A1 = IF SALARY GT 50000 THEN 'H' ELSE 'L'; END",
            "TABLE FILE EMPDATA SUM SALARY COMPUTE ROUNDED = ROUND(SALARY); END"
        ]
        for code in variations:
            with self.subTest(code=code):
                self.parse(code)

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
            with self.subTest(code=code):
                self.parse(code)

    def test_where_clauses(self):
        variations = [
            "TABLE FILE EMPDATA PRINT SALARY WHERE DEPARTMENT EQ 'SALES' END",
            "TABLE FILE EMPDATA SUM SALARY WHERE YEAR EQ 1991 END",
            "TABLE FILE EMPDATA LIST SALARY WHERE SALARY EQ CURR_SAL END",
            "TABLE FILE EMPDATA PRINT * WHERE DIV EQ 'NORTH' END"
        ]
        for code in variations:
            with self.subTest(code=code):
                self.parse(code)

    def test_basic_requests(self):
        variations = [
            "TABLE FILE EMPDATA SUM SALARY END",
            "TABLE FILE EMPDATA PRINT LAST_NAME FIRST_NAME END",
            "TABLE FILE EMPDATA LIST * END"
        ]
        for code in variations:
            with self.subTest(code=code):
                self.parse(code)

    def test_sort_phrases(self):
        variations = [
            "TABLE FILE EMPDATA SUM SALARY BY DEPT END",
            "TABLE FILE EMPDATA SUM SALARY ACROSS DIV END",
            "TABLE FILE EMPDATA SUM SALARY BY HIGHEST 5 SALARY END",
            "TABLE FILE EMPDATA SUM SALARY BY LOWEST CURR_SAL END"
        ]
        for code in variations:
            with self.subTest(code=code):
                self.parse(code)

    def test_formatting_commands(self):
        variations = [
            "TABLE FILE EMPDATA HEADING 'My Report' SUM SALARY END",
            "TABLE FILE EMPDATA PRINT SALARY FOOTING 'End of Page' END",
            "TABLE FILE EMPDATA SUM SALARY ON DEPT SUBHEAD 'Dept: <DEPT' END"
        ]
        for code in variations:
            with self.subTest(code=code):
                self.parse(code)

    def test_samples(self):
        samples_dir = 'test/samples'
        if not os.path.exists(samples_dir):
            return
        for filename in sorted(os.listdir(samples_dir)):
            if filename.endswith('.fex'):
                filepath = os.path.join(samples_dir, filename)
                with open(filepath, 'r') as f:
                    code = f.read()
                with self.subTest(filename=filename):
                    self.parse(code)

if __name__ == '__main__':
    unittest.main()

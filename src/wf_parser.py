from antlr4 import InputStream, CommonTokenStream
try:
    from WebFocusReportLexer import WebFocusReportLexer
    from WebFocusReportParser import WebFocusReportParser as GeneratedWebFocusReportParser
except ImportError:
    from .WebFocusReportLexer import WebFocusReportLexer
    from .WebFocusReportParser import WebFocusReportParser as GeneratedWebFocusReportParser
from antlr4.error.ErrorListener import ErrorListener
import sys
from master_file_parser import MasterFileParser

class BailErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error at line {line}:{column}: {msg}")

class ReportParser:
    def parse(self, text):
        input_stream = InputStream(text)
        lexer = WebFocusReportLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(BailErrorListener())

        stream = CommonTokenStream(lexer)
        parser = GeneratedWebFocusReportParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(BailErrorListener())

        return parser.start()

class WebFocusParser:
    def __init__(self):
        self.report_parser = ReportParser()
        self.master_parser = MasterFileParser()

    def parse(self, text):
        # A simple dispatcher: if it contains 'FILENAME', assume it's a Master File
        # Otherwise, assume it's a report request.
        if 'FILENAME' in text.upper() or 'SEGNAME' in text.upper():
            return self.master_parser.parse(text)
        else:
            return self.report_parser.parse(text)

if __name__ == "__main__":
    sample_report = """
    TABLE FILE EMPDATA
    HEADING CENTER "Education Cost vs. Salary"
    FOOTING "End of Report"
    SUM AVE.EXPENSES AS 'Average Education Cost' MAX.SALARY AS 'Max Salary'
    BY DIV
    BY DEPT
    WHERE YEAR EQ 1991
    END
    """

    parser = WebFocusParser()

    print("--- Parsing Report Request ---")
    try:
        tree = parser.parse(sample_report)
        print(tree.toStringTree(recog=None))
    except Exception as e:
        print(f"Error parsing report:\n{e}")

    sample_master = """
    FILENAME=EMPLOYEE, SUFFIX=FOC, $
    SEGNAME=EMPINFO, SEGTYPE=S1, $
    FIELDNAME=EMP_ID, ALIAS=EID, FORMAT=A9, $
    """
    print("\n--- Parsing Master File ---")
    try:
        tree = parser.parse(sample_master)
        print(tree.toStringTree(recog=None))
    except Exception as e:
        print(f"Error parsing Master File:\n{e}")

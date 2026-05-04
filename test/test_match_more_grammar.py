import unittest
from antlr4 import InputStream, CommonTokenStream
from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser

class TestMatchMoreGrammar(unittest.TestCase):
    def parse(self, text):
        input_stream = InputStream(text)
        lexer = WebFocusReportLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(token_stream)
        tree = parser.start()
        return parser.getNumberOfSyntaxErrors()

    def test_match_file_basic(self):
        # Scenario from p. 1160
        text = """
        MATCH FILE EDUCFILE
        SUM COURSE_CODE
        BY EMP_ID
        RUN
        FILE EMPLOYEE
        SUM LAST_NAME AND FIRST_NAME
        BY EMP_ID BY CURR_SAL
        AFTER MATCH HOLD OLD-OR-NEW
        END
        """
        self.assertEqual(self.parse(text), 0)

    def test_table_more_phrase(self):
        # Scenario from p. 1175
        text = """
        TABLE FILE EMPLOYEE
        PRINT CURR_SAL
        BY EMP_ID
        MORE
        FILE EXPERSON
        END
        """
        self.assertEqual(self.parse(text), 0)

    def test_match_multi_file(self):
        # Scenario from p. 1156
        text = """
        MATCH FILE file1
        RUN
        FILE file2
        AFTER MATCH OLD-OR-NEW
        RUN
        FILE file3
        AFTER MATCH OLD-OR-NEW
        END
        """
        self.assertEqual(self.parse(text), 0)

    def test_all_merge_phrases(self):
        phrases = [
            "OLD-OR-NEW",
            "OLD-AND-NEW",
            "OLD-NOT-NEW",
            "NEW-NOT-OLD",
            "OLD-NOR-NEW",
            "OLD",
            "NEW"
        ]
        for phrase in phrases:
            text = f"""
            MATCH FILE F1
            RUN
            FILE F2
            AFTER MATCH HOLD {phrase}
            END
            """
            with self.subTest(phrase=phrase):
                self.assertEqual(self.parse(text), 0)

if __name__ == "__main__":
    unittest.main()

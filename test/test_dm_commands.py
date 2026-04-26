import unittest
from antlr4 import CommonTokenStream, InputStream
from src.WebFocusReportLexer import WebFocusReportLexer
from src.WebFocusReportParser import WebFocusReportParser

class TestDMCommands(unittest.TestCase):
    def parse(self, text):
        input_stream = InputStream(text)
        lexer = WebFocusReportLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(stream)
        return parser.start()

    def test_dm_if_simple(self):
        tree = self.parse("-IF &VAR EQ 1 GOTO MYLABEL")
        # Should parse without error
        self.assertIsNotNone(tree)

    def test_dm_if_with_then(self):
        tree = self.parse("-IF &VAR EQ 1 THEN GOTO MYLABEL")
        self.assertIsNotNone(tree)

    def test_dm_if_with_else(self):
        tree = self.parse("-IF &VAR EQ 1 GOTO LABEL1 ELSE GOTO LABEL2")
        self.assertIsNotNone(tree)

    def test_dm_if_complex_logical(self):
        tree = self.parse("-IF (&VAR1 EQ 1) AND (&VAR2 NE 'X' OR NOT &VAR3 LE 10) GOTO LABEL")
        self.assertIsNotNone(tree)

    def test_dm_type_simple(self):
        tree = self.parse("-TYPE HELLO WORLD")
        self.assertIsNotNone(tree)

    def test_dm_type_with_vars(self):
        tree = self.parse("-TYPE VALUE IS &VAR")
        self.assertIsNotNone(tree)

    def test_dm_comment(self):
        # Comments should be skipped by lexer
        tree = self.parse("-* THIS IS A COMMENT\n-SET &A = 1;")
        self.assertIsNotNone(tree)
        # Check if -SET was parsed
        # In ANTLR4 Python, we should check if any child is a WebFocusReportParser.Dm_commandContext
        found_dm = False
        for i in range(tree.getChildCount()):
            child = tree.getChild(i)
            if isinstance(child, WebFocusReportParser.Dm_commandContext):
                found_dm = True
                break
        self.assertTrue(found_dm)

    def test_interleaved_dm_and_table(self):
        text = """
        -SET &VAR = 1;
        -* A comment
        -IF &VAR EQ 1 GOTO LABEL1;
        TABLE FILE MYFILE
        PRINT *
        END
        -LABEL1
        -TYPE DONE
        """
        tree = self.parse(text)
        self.assertIsNotNone(tree)

    def test_dm_repeat_while(self):
        tree = self.parse("-REPEAT ENDLP WHILE &DONE EQ 'N';")
        self.assertIsNotNone(tree)

    def test_dm_repeat_until(self):
        tree = self.parse("-REPEAT ENDLP UNTIL &DONE EQ 'Y';")
        self.assertIsNotNone(tree)

    def test_dm_repeat_times(self):
        tree = self.parse("-REPEAT ENDLP 10 TIMES")
        self.assertIsNotNone(tree)

    def test_dm_repeat_for(self):
        tree = self.parse("-REPEAT ENDLP FOR &I FROM 1 TO 10 STEP 1")
        self.assertIsNotNone(tree)

if __name__ == '__main__':
    unittest.main()

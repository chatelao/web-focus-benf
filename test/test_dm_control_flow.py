import unittest
import sys
import os

# Add src to sys.path to allow importing wf_parser
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from wf_parser import ReportParser

class TestDMControlFlow(unittest.TestCase):
    def setUp(self):
        self.parser = ReportParser()

    def test_dm_goto_label(self):
        fex = """
        -GOTO EXIT_REPORT
        TABLE FILE CAR
        PRINT COUNTRY
        END
        -EXIT_REPORT
        """
        try:
            tree = self.parser.parse(fex)
            self.assertIsNotNone(tree)
        except Exception as e:
            self.fail(f"Parsing failed for -GOTO and Label: {e}")

    def test_dm_goto_with_semi(self):
        fex = "-GOTO MYLABEL;"
        try:
            tree = self.parser.parse(fex)
            self.assertIsNotNone(tree)
        except Exception as e:
            self.fail(f"Parsing failed for -GOTO with semicolon: {e}")

    def test_dm_label_at_start(self):
        fex = "-START_HERE"
        try:
            tree = self.parser.parse(fex)
            self.assertIsNotNone(tree)
        except Exception as e:
            self.fail(f"Parsing failed for Label at start: {e}")

    def test_dm_interleaved_goto(self):
        fex = """
        TABLE FILE CAR
        PRINT COUNTRY
        -GOTO SKIP_BY
        BY MODEL
        -SKIP_BY
        END
        """
        try:
            tree = self.parser.parse(fex)
            self.assertIsNotNone(tree)
        except Exception as e:
            self.fail(f"Parsing failed for interleaved -GOTO: {e}")

if __name__ == '__main__':
    unittest.main()

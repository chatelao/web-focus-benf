import unittest
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from wf_parser import WebFocusParser

class TestWebFocusParser(unittest.TestCase):
    def setUp(self):
        self.parser = WebFocusParser()

    def test_simple_table_request(self):
        code = """
        TABLE FILE EMPDATA
        SUM SALARY
        END
        """
        tree = self.parser.parse(code)
        self.assertEqual(tree.data, 'request')

        # Check table_file
        table_file = next(tree.find_data('table_file'))
        self.assertIn('EMPDATA', [str(t) for t in table_file.children])

    def test_complex_request(self):
        code = """
        TABLE FILE EMPDATA
        HEADING CENTER "Education Cost vs. Salary"
        SUM EXPENSES AS 'Education,Cost' SALARY AS 'Current,Salary'
        BY DIV
        BY DEPT
        WHERE YEAR EQ 1991
        END
        """
        tree = self.parser.parse(code)
        self.assertEqual(tree.data, 'request')

        # Check sum_command
        sum_commands = list(tree.find_data('sum_command'))
        self.assertEqual(len(sum_commands), 1)

        # Check by_commands
        by_commands = list(tree.find_data('by_command'))
        self.assertEqual(len(by_commands), 2)

    def test_invalid_syntax(self):
        code = "INVALID REQUEST"
        with self.assertRaises(Exception):
            self.parser.parse(code)

if __name__ == '__main__':
    unittest.main()

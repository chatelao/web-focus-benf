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

        # Check display_command
        display_commands = list(tree.find_data('display_command'))
        self.assertEqual(len(display_commands), 1)

        # Check by_commands
        by_commands = list(tree.find_data('by_command'))
        self.assertEqual(len(by_commands), 2)

    def test_invalid_syntax(self):
        code = "INVALID REQUEST"
        with self.assertRaises(Exception):
            self.parser.parse(code)

    def test_verbs_and_wildcard(self):
        verbs = ['PRINT', 'LIST', 'COUNT', 'SUM', 'WRITE', 'ADD']
        for verb in verbs:
            code = f"TABLE FILE EMPDATA\n{verb} *\nEND"
            tree = self.parser.parse(code)
            display_cmd = next(tree.find_data('display_command'))
            self.assertEqual(str(next(display_cmd.find_data('verb')).children[0]), verb)
            self.assertTrue(list(display_cmd.find_data('asterisk')))

    def test_optional_keywords(self):
        code = """
        TABLE FILE EMPLOYEE
        PRINT THE LAST_NAME AND THE FIRST_NAME
        END
        """
        tree = self.parser.parse(code)
        display_cmd = next(tree.find_data('display_command'))
        field_list = next(display_cmd.find_data('field_list'))
        fields = list(field_list.find_data('field'))
        self.assertEqual(len(fields), 2)

    def test_samples(self):
        samples_dir = os.path.join(os.path.dirname(__file__), 'samples')
        for filename in os.listdir(samples_dir):
            if filename.endswith('.fex'):
                filepath = os.path.join(samples_dir, filename)
                with open(filepath, 'r') as f:
                    code = f.read()
                try:
                    self.parser.parse(code)
                except Exception as e:
                    self.fail(f"Failed to parse {filename}: {e}")

if __name__ == '__main__':
    unittest.main()

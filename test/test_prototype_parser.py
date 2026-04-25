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
        qn = next(table_file.find_data('qualified_name'))
        self.assertIn('EMPDATA', [str(t) for t in qn.children])

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

    def test_across_command(self):
        code = """
        TABLE FILE EMPDATA
        SUM SALARY
        ACROSS DEPARTMENT
        END
        """
        tree = self.parser.parse(code)
        across_cmds = list(tree.find_data('across_command'))
        self.assertEqual(len(across_cmds), 1)

    def test_sort_options(self):
        variations = [
            "BY HIGHEST 5 SALARY",
            "BY LOWEST SALARY",
            "BY TOP 10 SALARY",
            "BY BOTTOM SALARY",
            "BY 12 SALARY",
            "ACROSS HIGHEST 3 DEPT",
            "ACROSS TOP DEPT"
        ]
        for var in variations:
            code = f"TABLE FILE EMPDATA\nSUM SALARY\n{var}\nEND"
            try:
                self.parser.parse(code)
            except Exception as e:
                self.fail(f"Failed to parse sort option '{var}': {e}")

    def test_ranked_by(self):
        code = """
        TABLE FILE EMPLOYEE
        PRINT LAST_NAME
        RANKED BY HIGHEST 5 CURR_SAL
        END
        """
        tree = self.parser.parse(code)
        by_cmd = next(tree.find_data('by_command'))
        self.assertTrue(any(t.type == 'RANKED' for t in by_cmd.children if hasattr(t, 'type')))

    def test_sort_as_phrase(self):
        code = """
        TABLE FILE EMPLOYEE
        SUM SALARY
        BY DEPARTMENT AS 'Dept. Title'
        ACROSS BANK_NAME AS 'Bank Name'
        END
        """
        tree = self.parser.parse(code)
        by_cmd = next(tree.find_data('by_command'))
        field = next(by_cmd.find_data('field'))
        self.assertTrue(list(field.find_data('as_phrase')))
        across_cmd = next(tree.find_data('across_command'))
        field_across = next(across_cmd.find_data('field'))
        self.assertTrue(list(field_across.find_data('as_phrase')))

    def test_prefix_operators(self):
        code = """
        TABLE FILE EMPDATA
        SUM AVE.EXPENSES AS 'Avg Exp' MAX.SALARY MIN.SALARY CNT.PIN
        END
        """
        tree = self.parser.parse(code)
        field_list = next(tree.find_data('field_list'))
        prefixed_fields = list(field_list.find_data('field_or_prefixed'))
        self.assertEqual(len(prefixed_fields), 4)

        # Verify AVE.EXPENSES
        f1 = prefixed_fields[0]
        self.assertEqual(str(next(f1.find_data('prefix_operator')).children[0]), 'AVE')

        # Verify multiple prefixes (WebFOCUS supports recursive prefixes)
        code_multi = "TABLE FILE EMPDATA\nSUM TOT.AVE.SALARY\nEND"
        tree_multi = self.parser.parse(code_multi)
        f_multi = next(tree_multi.find_data('field_or_prefixed'))
        prefixes = [str(p.children[0]) for p in f_multi.find_data('prefix_operator')]
        self.assertEqual(prefixes, ['TOT', 'AVE'])

    def test_footing_command(self):
        code = """
        TABLE FILE EMPDATA
        PRINT SALARY
        FOOTING CENTER "END OF REPORT"
        END
        """
        tree = self.parser.parse(code)
        footing_cmd = next(tree.find_data('footing_command'))
        self.assertIn('FOOTING', [str(t) for t in footing_cmd.children if hasattr(t, 'type')])
        self.assertIn('"END OF REPORT"', [str(t) for t in footing_cmd.children if hasattr(t, 'type')])

    def test_qualified_names(self):
        code = """
        TABLE FILE SEG1.MASTER
        PRINT SEG1.FIELD1 SEG2.FIELD2
        WHERE SEG1.FIELD1 EQ 'VAL'
        END
        """
        tree = self.parser.parse(code)
        # Table name
        table_file = next(tree.find_data('table_file'))
        qn = next(table_file.find_data('qualified_name'))
        self.assertEqual([str(t) for t in qn.children], ['SEG1', 'MASTER'])

        # Fields
        field_list = next(tree.find_data('field_list'))
        qns = [next(f.find_data('qualified_name')) for f in field_list.find_data('field')]
        self.assertEqual([str(t) for t in qns[0].children], ['SEG1', 'FIELD1'])
        self.assertEqual([str(t) for t in qns[1].children], ['SEG2', 'FIELD2'])

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

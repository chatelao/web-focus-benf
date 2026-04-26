import unittest
import sys
import os
from antlr4 import ParserRuleContext

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from wf_parser import WebFocusParser

def find_context(ctx, context_type_name):
    """Helper to find all contexts of a certain type in the ANTLR tree."""
    results = []
    if ctx.__class__.__name__ == context_type_name:
        results.append(ctx)
    if hasattr(ctx, 'children') and ctx.children:
        for child in ctx.children:
            if isinstance(child, ParserRuleContext):
                results.extend(find_context(child, context_type_name))
    return results

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
        # tree is 'start' rule context
        self.assertEqual(tree.__class__.__name__, 'StartContext')

        requests = find_context(tree, 'RequestContext')
        self.assertEqual(len(requests), 1)

        # Check table_file
        table_files = find_context(tree, 'Table_fileContext')
        self.assertEqual(len(table_files), 1)
        qn = find_context(table_files[0], 'Qualified_nameContext')[0]
        self.assertIn('EMPDATA', qn.getText().upper())

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

        # Check display_command
        display_commands = find_context(tree, 'Verb_commandContext')
        self.assertEqual(len(display_commands), 1)

        # Check by_commands
        by_commands = find_context(tree, 'By_commandContext')
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
            verb_cmds = find_context(tree, 'Verb_commandContext')
            self.assertEqual(len(verb_cmds), 1)
            # verb context is child of verb_command
            v_ctx = find_context(verb_cmds[0], 'VerbContext')[0]
            self.assertEqual(v_ctx.getText().upper(), verb)
            self.assertTrue(find_context(verb_cmds[0], 'AsteriskContext'))

    def test_across_command(self):
        code = """
        TABLE FILE EMPDATA
        SUM SALARY
        ACROSS DEPARTMENT
        END
        """
        tree = self.parser.parse(code)
        across_cmds = find_context(tree, 'Across_commandContext')
        self.assertEqual(len(across_cmds), 1)

    def test_prefix_operators(self):
        code = """
        TABLE FILE EMPDATA
        SUM AVE.EXPENSES AS 'Avg Exp' MAX.SALARY MIN.SALARY CNT.PIN
        END
        """
        tree = self.parser.parse(code)
        field_list = find_context(tree, 'Field_listContext')[0]
        prefixed_fields = find_context(field_list, 'Field_or_prefixedContext')
        self.assertEqual(len(prefixed_fields), 4)

        # Verify AVE.EXPENSES
        f1 = prefixed_fields[0]
        prefixes = find_context(f1, 'Prefix_operatorContext')
        self.assertEqual(prefixes[0].getText().upper(), 'AVE')

    def test_footing_command(self):
        code = """
        TABLE FILE EMPDATA
        PRINT SALARY
        FOOTING CENTER "END OF REPORT" "Line 2"
        END
        """
        tree = self.parser.parse(code)
        footing_cmds = find_context(tree, 'Footing_commandContext')
        self.assertEqual(len(footing_cmds), 1)

    def test_on_commands(self):
        code = """
        TABLE FILE EMPLOYEE
        PRINT CURR_SAL
        BY LAST_NAME
        ON TABLE SUBHEAD
        "CONFIDENTIAL"
        ON LAST_NAME SUBHEAD
        "ID: <EMP_ID"
        ON LAST_NAME SUBFOOT
        "End of Last Name"
        ON TABLE SUBFOOT
        "Grand Total"
        END
        """
        tree = self.parser.parse(code)
        on_cmds = find_context(tree, 'On_commandContext')
        self.assertEqual(len(on_cmds), 4)

    def test_qualified_names(self):
        code = """
        TABLE FILE SEG1.MASTER
        PRINT SEG1.FIELD1 SEG2.FIELD2
        WHERE SEG1.FIELD1 EQ 'VAL'
        END
        """
        tree = self.parser.parse(code)
        # Table name
        table_file = find_context(tree, 'Table_fileContext')[0]
        qn = find_context(table_file, 'Qualified_nameContext')[0]
        self.assertEqual(qn.getText().upper(), 'SEG1.MASTER')

        # Fields
        field_list = find_context(tree, 'Field_listContext')[0]
        qns = [find_context(f, 'Qualified_nameContext')[0] for f in find_context(field_list, 'FieldContext')]
        self.assertEqual(qns[0].getText().upper(), 'SEG1.FIELD1')
        self.assertEqual(qns[1].getText().upper(), 'SEG2.FIELD2')

    def test_dm_set(self):
        code = """
        -SET &VAR1 = 10;
        -SET &&VAR2 = 'HELLO' | ' WORLD';
        -SET &VAR3 = IF &VAR1 EQ 10 THEN 'YES' ELSE 'NO';
        TABLE FILE EMPDATA
        -SET &IN_TABLE = 1;
        PRINT *
        WHERE YEAR EQ &YEAR
        END
        -SET &AFTER = 'DONE';
        """
        tree = self.parser.parse(code)
        dm_sets = find_context(tree, 'Dm_setContext')
        self.assertEqual(len(dm_sets), 5)

        # Check if variables are recognized
        amper_vars = find_context(tree, 'Amper_varContext')
        # &VAR1, &&VAR2, &VAR3, &VAR1, &IN_TABLE, &YEAR, &AFTER
        self.assertEqual(len(amper_vars), 7)

    def test_dm_misc_commands(self):
        code = """
        -INCLUDE GGHDR.FEX
        TABLE FILE EMPDATA
        PRINT *
        -RUN
        END
        -EXIT
        """
        tree = self.parser.parse(code)

        includes = find_context(tree, 'Dm_includeContext')
        self.assertEqual(len(includes), 1)
        self.assertEqual(includes[0].getText().upper(), '-INCLUDEGGHDR.FEX')

        runs = find_context(tree, 'Dm_runContext')
        self.assertEqual(len(runs), 1)

        exits = find_context(tree, 'Dm_exitContext')
        self.assertEqual(len(exits), 1)

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

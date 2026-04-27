import unittest
import os
import sys

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from wf_parser import WebFocusParser

class TestDocumentationExamples(unittest.TestCase):
    def setUp(self):
        self.parser = WebFocusParser()

    def test_documentation_examples(self):
        """
        Test that documentation examples can be parsed.
        Note: Some examples currently fail due to known grammar gaps.
        These are tracked in the ROADMAP and technical debt documentation.
        """
        examples_dir = os.path.join(os.path.dirname(__file__), 'documentation_examples')
        if not os.path.exists(examples_dir):
            self.fail(f"Documentation examples directory not found: {examples_dir}")

        # List of files known to fail due to missing grammar features
        known_failures = {
            'project1_joined_report/joined_report.fex': 'JOIN ... TO ALL not supported',
            'project2_compound_layout/compound_layout.fex': 'COMPOUND LAYOUT and hyphenated SET keywords not supported',
            'project3_hierarchical_cube/hierarchical_report.fex': 'BY ... HIERARCHY and SHOW UP/DOWN not supported',
            'project3_hierarchical_cube/newgl.mas': 'DIMENSION and HIERARCHY in Master Files not supported',
            'project4_data_merge/data_merge.fex': 'ON TABLE MERGE not supported',
            'project5_drill_through/main_controller.fex': '-HTMLFORM not supported',
            'project5_drill_through/detail_report.fex': 'External reference from main_controller',
            'project5_drill_through/summary_report.fex': 'External reference from main_controller'
        }

        for root, dirs, files in os.walk(examples_dir):
            for filename in files:
                if filename.endswith(('.fex', '.mas')):
                    filepath = os.path.join(root, filename)
                    rel_path = os.path.relpath(filepath, examples_dir).replace(os.sep, '/')

                    with self.subTest(filename=rel_path):
                        if rel_path in known_failures:
                            self.skipTest(f"Skipping known failure: {known_failures[rel_path]}")

                        with open(filepath, 'r') as f:
                            code = f.read()

                        try:
                            self.parser.parse(code)
                        except Exception as e:
                            self.fail(f"Failed to parse {filepath}: {e}")

if __name__ == '__main__':
    unittest.main()

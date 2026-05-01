import unittest
import os
import shutil
import subprocess

class TestRailroadIntegration(unittest.TestCase):
    def setUp(self):
        self.test_output_dir = "test_run_docs"
        self.test_ebnf_dir = "test_run_ebnf"
        if os.path.exists(self.test_output_dir):
            shutil.rmtree(self.test_output_dir)
        if os.path.exists(self.test_ebnf_dir):
            shutil.rmtree(self.test_ebnf_dir)

    def tearDown(self):
        if os.path.exists(self.test_output_dir):
            shutil.rmtree(self.test_output_dir)
        if os.path.exists(self.test_ebnf_dir):
            shutil.rmtree(self.test_ebnf_dir)

    def test_full_pipeline(self):
        """Verifies that the generation script runs and produces all expected artifacts."""
        cmd = [
            "python3", "scripts/generate_railroad.py",
            "--output-dir", self.test_output_dir,
            "--ebnf-dir", self.test_ebnf_dir,
            "--grammars", "WebFocusReport.g4"
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, f"Script failed: {result.stderr}")

        # Check for expected files
        expected_files = [
            os.path.join(self.test_ebnf_dir, "WebFocusReport.ebnf"),
            os.path.join(self.test_output_dir, "WebFocusReport.xhtml"),
            os.path.join(self.test_output_dir, "index.html")
        ]

        for filepath in expected_files:
            self.assertTrue(os.path.exists(filepath), f"Missing expected file: {filepath}")
            self.assertGreater(os.path.getsize(filepath), 0, f"File is empty: {filepath}")

        # Basic content validation
        with open(os.path.join(self.test_output_dir, "WebFocusReport.xhtml"), "r") as f:
            content = f.read()
            self.assertIn("<svg", content, "XHTML does not contain SVG")

        with open(os.path.join(self.test_output_dir, "index.html"), "r") as f:
            content = f.read()
            self.assertIn("WebFocusReport.xhtml", content, "Index does not link to report")

if __name__ == "__main__":
    unittest.main()

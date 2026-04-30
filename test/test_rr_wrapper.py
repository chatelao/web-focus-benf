import unittest
import os
import tempfile
from src.rr_wrapper import RRTool

class TestRRWrapper(unittest.TestCase):
    def setUp(self):
        self.rr = RRTool()
        self.test_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.test_dir.cleanup()

    def test_basic_generation(self):
        ebnf_path = os.path.join(self.test_dir.name, "test.ebnf")
        out_path = os.path.join(self.test_dir.name, "test.xhtml")

        with open(ebnf_path, "w") as f:
            f.write("STMT ::= 'SELECT' NAME 'FROM' NAME\n")
            f.write("NAME ::= [a-zA-Z]+\n")

        self.rr.generate(ebnf_path, out_path=out_path)

        self.assertTrue(os.path.exists(out_path))
        with open(out_path, "r") as f:
            content = f.read()
            self.assertIn("<svg", content)
            self.assertIn("SELECT", content)

    def test_color_option(self):
        ebnf_path = os.path.join(self.test_dir.name, "test_color.ebnf")
        out_path = os.path.join(self.test_dir.name, "test_color.xhtml")

        with open(ebnf_path, "w") as f:
            f.write("STMT ::= 'TEST'\n")

        self.rr.generate(ebnf_path, out_path=out_path, color="#FF0000")

        self.assertTrue(os.path.exists(out_path))
        with open(out_path, "r") as f:
            content = f.read()
            # RR tool uses the color in the generated CSS/SVG
            self.assertIn("#FF0000", content.upper())

    def test_invalid_ebnf(self):
        ebnf_path = os.path.join(self.test_dir.name, "invalid.ebnf")

        with open(ebnf_path, "w") as f:
            f.write("STMT ::= 'MISSING_QUOTE\n")

        with self.assertRaises(RuntimeError):
            self.rr.generate(ebnf_path)

if __name__ == "__main__":
    unittest.main()

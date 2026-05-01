import unittest
import os
import subprocess
import shutil

class TestRailroadGolden(unittest.TestCase):
    def setUp(self):
        self.temp_ebnf_dir = "test_run_ebnf_golden"
        if os.path.exists(self.temp_ebnf_dir):
            shutil.rmtree(self.temp_ebnf_dir)
        os.makedirs(self.temp_ebnf_dir)
        self.golden_dir = "test/golden/railroad"

    def tearDown(self):
        if os.path.exists(self.temp_ebnf_dir):
            shutil.rmtree(self.temp_ebnf_dir)

    def test_ebnf_golden_master(self):
        """Compares generated EBNF against golden master files."""
        grammars = ["WebFocusReport.g4", "MasterFile.g4"]

        for grammar in grammars:
            grammar_path = os.path.join("src", grammar)
            grammar_name = os.path.basename(grammar_path)
            ebnf_name = grammar_name.replace(".g4", ".ebnf")
            generated_ebnf_path = os.path.join(self.temp_ebnf_dir, ebnf_name)
            golden_ebnf_path = os.path.join(self.golden_dir, ebnf_name)

            # Generate EBNF
            with open(generated_ebnf_path, "w") as f:
                subprocess.run(["python3", "scripts/antlr4_to_ebnf.py", grammar_path, "--check"], stdout=f, check=True)

            self.assertTrue(os.path.exists(golden_ebnf_path), f"Golden master missing for {grammar_name}")

            with open(generated_ebnf_path, "r") as f:
                generated_content = f.read()
            with open(golden_ebnf_path, "r") as f:
                golden_content = f.read()

            if os.environ.get("UPDATE_GOLDEN"):
                if generated_content != golden_content:
                    print(f"Updating golden master for {ebnf_name}")
                    with open(golden_ebnf_path, "w") as f:
                        f.write(generated_content)
            else:
                self.assertEqual(generated_content, golden_content,
                                 f"EBNF mismatch for {grammar_name}. "
                                 "If this is intentional, run with UPDATE_GOLDEN=1 to update golden masters.")

if __name__ == "__main__":
    unittest.main()

import unittest
import os
import sys

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from wf_parser import WebFocusParser
from asg_builder import ReportASGBuilder
from ir_builder import IRBuilder

class TestCoreSamples(unittest.TestCase):
    def setUp(self):
        self.parser = WebFocusParser()
        self.asg_builder = ReportASGBuilder()
        self.ir_builder = IRBuilder()

    def test_core_samples(self):
        """
        Test that core samples in test/samples/ can be parsed and transformed to IR.
        """
        samples_dir = os.path.join(os.path.dirname(__file__), 'samples')
        if not os.path.exists(samples_dir):
            self.fail(f"Samples directory not found: {samples_dir}")

        for filename in os.listdir(samples_dir):
            if filename.endswith('.fex'):
                filepath = os.path.join(samples_dir, filename)
                with self.subTest(filename=filename):
                    with open(filepath, 'r') as f:
                        code = f.read()

                    try:
                        # 1. Parse
                        tree = self.parser.parse(code)

                        # 2. Build ASG
                        asg = self.asg_builder.visit(tree)

                        # 3. Build IR
                        cfg = self.ir_builder.build(asg)

                        self.assertIsNotNone(cfg)
                        self.assertGreater(len(cfg.blocks), 0)

                    except Exception as e:
                        self.fail(f"Failed to process {filename}: {e}")

if __name__ == '__main__':
    unittest.main()

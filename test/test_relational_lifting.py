import unittest
import sys
import os
from antlr4 import CommonTokenStream, InputStream

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
from symbol_resolver import SymbolResolver
from ir_builder import IRBuilder
from ssa_transformer import SSATransformer
from optimizer import RelationalLiftingOptimizer

class TestRelationalLifting(unittest.TestCase):
    def _get_cfg(self, fex_code):
        input_stream = InputStream(fex_code)
        lexer = WebFocusReportLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(token_stream)
        tree = parser.start()

        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)

        SymbolResolver().resolve(asg_nodes)

        cfg = IRBuilder().build(asg_nodes)
        SSATransformer().transform(cfg)
        return cfg

    def test_identify_read_loop(self):
        fex = """
        -SET &I = 1;
        -REPEAT LBL WHILE &I LE 10;
        -READ MYFILE &VAR
        -SET &I = &I + 1;
        -LBL
        """
        cfg = self._get_cfg(fex)
        optimizer = RelationalLiftingOptimizer()
        data_loops = optimizer.find_data_loops(cfg)

        self.assertEqual(len(data_loops), 1)
        self.assertEqual(data_loops[0]['type'], 'WHILE')
        self.assertTrue(any(b.startswith('LOOP_BODY_') for b in data_loops[0]['body_blocks']))

    def test_identify_read_loop_for(self):
        fex = """
        -REPEAT LBL 10 TIMES;
        -READ MYFILE &VAR
        -LBL
        """
        cfg = self._get_cfg(fex)
        optimizer = RelationalLiftingOptimizer()
        data_loops = optimizer.find_data_loops(cfg)

        self.assertEqual(len(data_loops), 1)
        self.assertEqual(data_loops[0]['type'], 'FOR')

    def test_no_read_no_data_loop(self):
        fex = """
        -REPEAT LBL 10 TIMES;
        -SET &X = 1;
        -LBL
        """
        cfg = self._get_cfg(fex)
        optimizer = RelationalLiftingOptimizer()
        data_loops = optimizer.find_data_loops(cfg)

        self.assertEqual(len(data_loops), 0)

if __name__ == '__main__':
    unittest.main()

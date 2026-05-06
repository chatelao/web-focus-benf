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
from metadata_registry import MetadataRegistry
from asg import MasterFile, Segment, Field
import asg

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

        ir_builder = IRBuilder()
        cfg = ir_builder.build(asg_nodes)
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

    def test_loop_carried_dependencies(self):
        fex = """
        -SET &TOTAL = 0;
        -REPEAT LBL 10 TIMES;
        -SET &TOTAL = &TOTAL + 1;
        -LBL
        """
        cfg = self._get_cfg(fex)
        optimizer = RelationalLiftingOptimizer()
        data_loops = []
        from ir_utils import find_simple_for_loop
        for b in cfg.blocks:
            loop = find_simple_for_loop(cfg, b)
            if loop:
                data_loops.append(loop)

        self.assertEqual(len(data_loops), 1)

        carried = optimizer.analyze_loop_carried_dependencies(cfg, data_loops[0])
        self.assertIn("&TOTAL", carried)
        self.assertIn("&REPEAT_COUNTER_LBL", carried)

    def test_identify_accumulators(self):
        fex = """
        -SET &TOTAL = 0;
        -REPEAT LBL 10 TIMES;
        -SET &TOTAL = &TOTAL + 5;
        -LBL
        """
        cfg = self._get_cfg(fex)
        optimizer = RelationalLiftingOptimizer()
        from ir_utils import find_simple_for_loop
        loop = None
        for b in cfg.blocks:
            loop = find_simple_for_loop(cfg, b)
            if loop: break

        carried = optimizer.analyze_loop_carried_dependencies(cfg, loop)
        accs = optimizer.identify_accumulators(cfg, loop, carried)

        self.assertIn("&TOTAL", accs)
        self.assertEqual(accs["&TOTAL"]["operator"], "+")
        self.assertEqual(accs["&TOTAL"]["increment"].value, 5)

    def test_map_read_variables(self):
        fex = """
        -REPEAT LBL WHILE &I LE 10;
        -READ MYFILE &VAR1 &VAR2
        -LBL
        """
        # Setup metadata
        registry = MetadataRegistry()
        mf = MasterFile(name="MYFILE")
        seg = Segment(name="S1")
        seg.fields = [Field(name="FIELD1"), Field(name="FIELD2")]
        mf.segments = [seg]
        registry.register_master_file(mf)

        cfg = self._get_cfg(fex)
        optimizer = RelationalLiftingOptimizer()
        data_loops = optimizer.find_data_loops(cfg)

        self.assertEqual(len(data_loops), 1)
        read_map = optimizer.map_read_variables(cfg, data_loops[0], registry)

        self.assertEqual(read_map["&VAR1"], ("MYFILE", "FIELD1"))
        self.assertEqual(read_map["&VAR2"], ("MYFILE", "FIELD2"))

    def test_identify_filters(self):
        fex = """
        -REPEAT LBL WHILE &I LE 10;
        -READ MYFILE &VAR1 &VAR2
        -IF &VAR1 EQ 'SKIP' GOTO LBL;
        -SET &TOTAL = &TOTAL + &VAR2;
        -LBL
        """
        # Setup metadata
        registry = MetadataRegistry()
        mf = MasterFile(name="MYFILE")
        seg = Segment(name="S1")
        seg.fields = [Field(name="FIELD1"), Field(name="FIELD2")]
        mf.segments = [seg]
        registry.register_master_file(mf)

        cfg = self._get_cfg(fex)
        optimizer = RelationalLiftingOptimizer()
        data_loops = optimizer.find_data_loops(cfg)
        self.assertEqual(len(data_loops), 1)

        read_map = optimizer.map_read_variables(cfg, data_loops[0], registry)
        filters = optimizer.identify_filters(cfg, data_loops[0], read_map)

        self.assertEqual(len(filters), 1)
        # Condition should be NOT (&VAR1 EQ 'SKIP')
        cond = filters[0]
        self.assertTrue(isinstance(cond, asg.UnaryOperation))
        self.assertEqual(cond.operator, "NOT")
        bin_op = cond.operand
        self.assertTrue(isinstance(bin_op, asg.BinaryOperation))
        self.assertEqual(bin_op.operator, "EQ")
        self.assertEqual(bin_op.left.name, "&VAR1")
        self.assertEqual(bin_op.right.value, "SKIP")

if __name__ == '__main__':
    unittest.main()

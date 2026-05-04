import unittest
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from asg_builder import ReportASGBuilder
from wf_parser import ReportParser
from ir_builder import IRBuilder
from emitter import PostgresEmitter

class TestLoopOptimization(unittest.TestCase):
    def setUp(self):
        self.parser = ReportParser()
        self.asg_builder = ReportASGBuilder()
        self.ir_builder = IRBuilder()
        self.emitter = PostgresEmitter()

    def test_simple_times_loop_optimization(self):
        fex = """
        -REPEAT MYLABEL 5 TIMES
        -TYPE 'Hello' &REPEAT_COUNTER_MYLABEL
        -MYLABEL
        """
        tree = self.parser.parse(fex)
        asg_nodes = self.asg_builder.visit(tree)
        cfg = self.ir_builder.build(asg_nodes)

        # We need to make sure the counter variable is declared
        # Actually emitter handles it via get_variables_from_cfg

        sql = self.emitter.emit(cfg)

        # Verify that native FOR loop is present
        self.assertIn("FOR v_REPEAT_COUNTER_MYLABEL IN 1..5 LOOP", sql)
        # Verify that it doesn't just use the state machine for the loop body
        # (Though the state machine is still the outer wrapper)
        self.assertIn("RAISE NOTICE '%', 'Hello' || v_REPEAT_COUNTER_MYLABEL;", sql)

    def test_complex_loop_remains_state_machine(self):
        # A loop with a -GOTO out of it might be too complex for the simple optimizer
        fex = """
        -REPEAT MYLABEL 5 TIMES
        -IF &X EQ 1 THEN GOTO EXIT_LOOP;
        -TYPE Hello
        -MYLABEL
        -EXIT_LOOP
        """
        tree = self.parser.parse(fex)
        asg_nodes = self.asg_builder.visit(tree)
        cfg = self.ir_builder.build(asg_nodes)

        sql = self.emitter.emit(cfg)

        # Should NOT contain native FOR loop because of the conditional branch to outside
        self.assertNotIn("FOR v_REPEAT_COUNTER_MYLABEL IN 1..5 LOOP", sql)

if __name__ == '__main__':
    unittest.main()

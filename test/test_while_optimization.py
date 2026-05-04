import unittest
import sys
import os
from antlr4 import CommonTokenStream, InputStream

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
from ir_builder import IRBuilder
from ssa_transformer import SSATransformer
from optimizer import ConstantPropagator, DeadCodeEliminator
from emitter import PostgresEmitter
from metadata_registry import MetadataRegistry

class TestWhileOptimization(unittest.TestCase):
    def _run_e2e(self, fex_code):
        # 2. Parse
        input_stream = InputStream(fex_code)
        lexer = WebFocusReportLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(token_stream)
        tree = parser.start()

        # 3. ASG Construction
        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)

        # 4. IR/CFG Construction
        ir_builder = IRBuilder()
        cfg = ir_builder.build(asg_nodes)

        # 5. SSA Transformation
        ssa_transformer = SSATransformer()
        ssa_transformer.transform(cfg)

        # 6. Optimization
        ConstantPropagator().run(cfg)
        DeadCodeEliminator().run(cfg)

        # 7. Backend Emission
        metadata = MetadataRegistry()
        emitter = PostgresEmitter(metadata_registry=metadata)
        sql_output = emitter.emit(cfg)

        return sql_output

    def test_repeat_while_optimization(self):
        fex_code = """
        -SET &I = 1;
        -REPEAT LOOP_END WHILE &I LE 5;
        -TYPE &I
        -SET &I = &I + 1;
        -LOOP_END
        """
        sql = self._run_e2e(fex_code)

        # Verify it uses native WHILE loop
        self.assertIn("WHILE (v_I_0 <= 5) LOOP", sql)
        self.assertIn("RAISE NOTICE '%', v_I_0;", sql)
        self.assertIn("v_I_0 := (v_I_0 + 1);", sql)
        self.assertIn("END LOOP;", sql)

        # Verify it doesn't have the body as separate CASE WHEN blocks
        # (It's consumed by the optimization)
        # Note: LOOP_HEADER remains as the container for the optimized loop
        self.assertNotIn("WHEN 'LOOP_BODY_LOOP_END' THEN", sql)

    def test_repeat_until_optimization(self):
        fex_code = """
        -SET &I = 1;
        -REPEAT LOOP_END UNTIL &I GT 5;
        -TYPE &I
        -SET &I = &I + 1;
        -LOOP_END
        """
        sql = self._run_e2e(fex_code)

        # UNTIL &I GT 5 is translated to WHILE NOT (&I GT 5)
        # Emitter might add space after NOT
        self.assertIn("WHILE NOT ((v_I_0 > 5)) LOOP", sql)
        self.assertIn("END LOOP;", sql)

if __name__ == '__main__':
    unittest.main()

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

class TestE2EControlFlow(unittest.TestCase):
    def _run_e2e(self, fex_code, optimize=True):
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
        if optimize:
            ConstantPropagator().run(cfg)
            DeadCodeEliminator().run(cfg)

        # 7. Backend Emission
        metadata = MetadataRegistry()
        emitter = PostgresEmitter(metadata_registry=metadata)
        sql_output = emitter.emit(cfg)

        return sql_output

    def test_basic_set_and_type_no_opt(self):
        fex_code = """
        -SET &MSG = 'Hello World';
        -TYPE &MSG
        """
        sql = self._run_e2e(fex_code, optimize=False)
        # Check assignment (using versioned or unversioned depends on ssa)
        self.assertIn("v_MSG", sql)
        self.assertIn(":= 'Hello World';", sql)
        # Check type/message
        self.assertIn("RAISE NOTICE '%', v_MSG", sql)

    def test_if_goto_branching_no_opt(self):
        fex_code = """
        -SET &VAL = 10;
        -IF &VAL GT 5 GOTO LABEL_TRUE ELSE GOTO LABEL_FALSE;
        -LABEL_TRUE
        -TYPE TRUE
        -GOTO END_LABEL
        -LABEL_FALSE
        -TYPE FALSE
        -END_LABEL
        -TYPE DONE
        """
        sql = self._run_e2e(fex_code, optimize=False)
        # Check branching logic
        self.assertIn("v_next_block := CASE WHEN (v_VAL > 5) THEN 'LABEL_TRUE' ELSE 'LABEL_FALSE' END;", sql)
        self.assertIn("WHEN 'LABEL_TRUE' THEN", sql)
        self.assertIn("RAISE NOTICE '%', v_TRUE;", sql)

    def test_repeat_while_loop_no_opt(self):
        fex_code = """
        -SET &I = 1;
        -REPEAT LOOP_END WHILE &I LE 3;
        -TYPE &I
        -SET &I = &I + 1;
        -LOOP_END
        """
        sql = self._run_e2e(fex_code, optimize=False)
        # Check loop structure
        self.assertIn("WHEN 'LOOP_HEADER_LOOP_END' THEN", sql)
        # Condition check
        self.assertIn("(v_I_0 <= 3)", sql)
        # Increment
        self.assertIn("v_I_0 := (v_I_0 + 1);", sql)

    def test_repeat_times_loop_no_opt(self):
        fex_code = """
        -REPEAT END_REPEAT 5 TIMES
        -TYPE HELLO
        -END_REPEAT
        """
        sql = self._run_e2e(fex_code, optimize=False)
        # With the new emitter, simple loops are optimized even without global optimize=True
        # because the optimization happens during emission based on CFG structure.
        self.assertIn("FOR v_REPEAT_COUNTER_END_REPEAT_0 IN 1..5 LOOP", sql)

if __name__ == '__main__':
    unittest.main()

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
        # After fixing entry block, SSA now correctly versions &VAL to v_VAL_0
        self.assertIn("v_next_block := CASE WHEN (v_VAL_0 > 5) THEN 'LABEL_TRUE' ELSE 'LABEL_FALSE' END;", sql)
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
        # Condition check - v_I_1 is the Phi node result in the loop header
        self.assertIn("(v_I_1 <= 3)", sql)
        # Increment
        self.assertIn("v_I_2 := (v_I_1 + 1);", sql)

    def test_repeat_times_loop_no_opt(self):
        fex_code = """
        -REPEAT END_REPEAT 5 TIMES
        -TYPE HELLO
        -END_REPEAT
        """
        sql = self._run_e2e(fex_code, optimize=False)
        # With the new emitter, simple loops are optimized even without global optimize=True
        # because the optimization happens during emission based on CFG structure.
        # v_REPEAT_COUNTER_END_REPEAT_1 is the counter in the loop header
        self.assertIn("FOR v_REPEAT_COUNTER_END_REPEAT_1 IN 1..5 LOOP", sql)

    def test_repeat_for_loop_optimization(self):
        fex_code = """
        -REPEAT END_REPEAT FOR &I FROM 1 TO 10 STEP 2
        -TYPE &I
        -END_REPEAT
        """
        sql = self._run_e2e(fex_code, optimize=False)
        # v_I_1 is the counter in the loop header
        self.assertIn("FOR v_I_1 IN 1..10 BY 2 LOOP", sql)
        self.assertIn("RAISE NOTICE '%', v_I_1;", sql)

if __name__ == '__main__':
    unittest.main()

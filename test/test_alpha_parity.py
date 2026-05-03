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
from emitter import PostgresEmitter

class TestAlphaParity(unittest.TestCase):
    def test_define_alpha_truncation(self):
        fex_code = """
        DEFINE FILE CAR
        SHORT_NAME/A5 = 'VERYLONGNAME';
        END
        TABLE FILE CAR
        PRINT SHORT_NAME
        END
        """

        input_stream = InputStream(fex_code)
        lexer = WebFocusReportLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(token_stream)
        tree = parser.start()

        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)

        ir_builder = IRBuilder()
        cfg = ir_builder.build(asg_nodes)

        emitter = PostgresEmitter()
        sql_output = emitter.emit(cfg)

        # Verify CAST to CHAR(5) for the virtual field
        self.assertIn("CAST('VERYLONGNAME' AS CHAR(5)) AS \"SHORT_NAME\"", sql_output)

    def test_compute_alpha_truncation(self):
        fex_code = """
        TABLE FILE CAR
        SUM SALES
        COMPUTE C_NAME/A3 = 'ABCDEFG';
        END
        """

        input_stream = InputStream(fex_code)
        lexer = WebFocusReportLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(token_stream)
        tree = parser.start()

        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)

        ir_builder = IRBuilder()
        cfg = ir_builder.build(asg_nodes)

        emitter = PostgresEmitter()
        sql_output = emitter.emit(cfg)

        # Verify CAST to CHAR(3) for the compute field
        self.assertIn("CAST('ABCDEFG' AS CHAR(3)) AS \"C_NAME\"", sql_output)

    def test_nested_define_alpha_truncation(self):
        fex_code = """
        DEFINE FILE CAR
        VAL1/A10 = 'LONGVALUEHERE';
        VAL2/A5 = VAL1;
        END
        TABLE FILE CAR
        PRINT VAL2
        END
        """

        input_stream = InputStream(fex_code)
        lexer = WebFocusReportLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(token_stream)
        tree = parser.start()

        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)

        ir_builder = IRBuilder()
        cfg = ir_builder.build(asg_nodes)

        emitter = PostgresEmitter()
        sql_output = emitter.emit(cfg)

        # Verify nested casting
        # VAL1 is CAST('LONGVALUEHERE' AS CHAR(10))
        # VAL2 is CAST(VAL1 AS CHAR(5))
        self.assertIn("CAST(CAST('LONGVALUEHERE' AS CHAR(10)) AS CHAR(5)) AS \"VAL2\"", sql_output)

if __name__ == '__main__':
    unittest.main()

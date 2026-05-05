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
from emitter import PostgresEmitter
from metadata_registry import MetadataRegistry

class TestTypeDeclarations(unittest.TestCase):
    def _get_sql(self, fex_code):
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

        metadata = MetadataRegistry()
        emitter = PostgresEmitter(metadata_registry=metadata)
        return emitter.emit(cfg)

    def test_integer_declaration(self):
        fex = """
        -SET &I = 1;
        -SET &J = &I + 5;
        """
        sql = self._get_sql(fex)
        # &I is 1 (Integer), &J is Integer + Integer -> Integer
        # In PL/pgSQL, this should be INTEGER or BIGINT
        self.assertIn("v_I_0 INTEGER", sql)
        self.assertIn("v_J_0 INTEGER", sql)

    def test_float_declaration(self):
        fex = """
        -SET &X = 1.5;
        -SET &Y = &X * 2;
        """
        sql = self._get_sql(fex)
        # &X is float, &Y should be float
        self.assertIn("v_X_0 DOUBLE PRECISION", sql)
        self.assertIn("v_Y_0 DOUBLE PRECISION", sql)

    def test_mixed_type_promotion(self):
        fex = """
        -SET &A = 10;
        -SET &B = &A / 3.0;
        """
        sql = self._get_sql(fex)
        self.assertIn("v_A_0 INTEGER", sql)
        self.assertIn("v_B_0 DOUBLE PRECISION", sql)

if __name__ == '__main__':
    unittest.main()

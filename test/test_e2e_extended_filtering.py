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

class TestE2EExtendedFiltering(unittest.TestCase):
    def _transpile(self, fex_code):
        input_stream = InputStream(fex_code)
        lexer = WebFocusReportLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(token_stream)
        tree = parser.start()

        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)

        ir_builder = IRBuilder()
        cfg = ir_builder.build(asg_nodes)

        ssa_transformer = SSATransformer()
        ssa_transformer.transform(cfg)

        ConstantPropagator().run(cfg)
        DeadCodeEliminator().run(cfg)

        metadata = MetadataRegistry()
        emitter = PostgresEmitter(metadata_registry=metadata)
        return emitter.emit(cfg)

    def test_contains_filtering(self):
        fex_code = """
        TABLE FILE CAR
        PRINT MODEL
        WHERE MODEL CONTAINS 'V8'
        END
        """
        sql_output = self._transpile(fex_code)
        self.assertIn("(MODEL LIKE '%' || 'V8' || '%')", sql_output)

    def test_omits_filtering(self):
        fex_code = """
        TABLE FILE CAR
        PRINT MODEL
        WHERE MODEL OMITS 'TURBO'
        END
        """
        sql_output = self._transpile(fex_code)
        self.assertIn("(MODEL NOT LIKE '%' || 'TURBO' || '%')", sql_output)

    def test_exceeds_filtering(self):
        fex_code = """
        TABLE FILE CAR
        PRINT MODEL
        WHERE SALES EXCEEDS 5000
        END
        """
        sql_output = self._transpile(fex_code)
        self.assertIn("(SALES > 5000)", sql_output)

    def test_is_less_than_filtering(self):
        fex_code = """
        TABLE FILE CAR
        PRINT MODEL
        WHERE SALES IS LESS THAN 1000
        END
        """
        sql_output = self._transpile(fex_code)
        self.assertIn("(SALES < 1000)", sql_output)

    def test_includes_filtering(self):
        fex_code = """
        TABLE FILE CAR
        PRINT MODEL
        WHERE MODEL INCLUDES 'V8' AND 'TURBO'
        END
        """
        sql_output = self._transpile(fex_code)
        # Expansion should be: (MODEL LIKE '%' || 'V8' || '%') AND (MODEL LIKE '%' || 'TURBO' || '%')
        self.assertIn("(MODEL LIKE '%' || 'V8' || '%')", sql_output)
        self.assertIn("(MODEL LIKE '%' || 'TURBO' || '%')", sql_output)
        self.assertIn(" AND ", sql_output)

    def test_excludes_filtering(self):
        fex_code = """
        TABLE FILE CAR
        PRINT MODEL
        WHERE MODEL EXCLUDES 'DIESEL' AND 'OLD'
        END
        """
        sql_output = self._transpile(fex_code)
        # Expansion should be: (MODEL NOT LIKE '%' || 'DIESEL' || '%') AND (MODEL NOT LIKE '%' || 'OLD' || '%')
        self.assertIn("(MODEL NOT LIKE '%' || 'DIESEL' || '%')", sql_output)
        self.assertIn("(MODEL NOT LIKE '%' || 'OLD' || '%')", sql_output)
        self.assertIn(" AND ", sql_output)

if __name__ == '__main__':
    unittest.main()

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

class TestE2EAdvancedFiltering(unittest.TestCase):
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

    def test_between_filtering(self):
        fex_code = """
        TABLE FILE CAR
        SUM SALES
        BY COUNTRY
        WHERE SALES FROM 1000 TO 5000
        END
        """
        sql_output = self._transpile(fex_code)
        self.assertIn("BETWEEN 1000 AND 5000", sql_output)

    def test_in_list_filtering(self):
        fex_code = """
        TABLE FILE CAR
        PRINT MODEL
        BY COUNTRY
        WHERE COUNTRY IN ('ENGLAND', 'FRANCE', 'ITALY')
        END
        """
        sql_output = self._transpile(fex_code)
        self.assertIn("COUNTRY IN ('ENGLAND', 'FRANCE', 'ITALY')", sql_output)

    def test_in_file_filtering(self):
        fex_code = """
        TABLE FILE CAR
        PRINT MODEL
        BY COUNTRY
        WHERE COUNTRY IN FILE TOP_COUNTRIES
        END
        """
        sql_output = self._transpile(fex_code)
        # Based on emitter.py, it should produce something like:
        # (COUNTRY IN (SELECT * FROM TOP_COUNTRIES))
        self.assertIn("COUNTRY IN (SELECT * FROM TOP_COUNTRIES)", sql_output)

    def test_missing_filtering(self):
        fex_code = """
        TABLE FILE CAR
        PRINT MODEL
        BY COUNTRY
        WHERE SALES IS MISSING
        END
        """
        sql_output = self._transpile(fex_code)
        self.assertIn("SALES IS NULL", sql_output)

        fex_code_not = """
        TABLE FILE CAR
        PRINT MODEL
        BY COUNTRY
        WHERE SALES IS NOT MISSING
        END
        """
        sql_output_not = self._transpile(fex_code_not)
        self.assertIn("SALES IS NOT NULL", sql_output_not)

if __name__ == '__main__':
    unittest.main()

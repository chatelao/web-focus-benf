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

class TestE2EBasicReporting(unittest.TestCase):
    def test_basic_print_report(self):
        # 1. Setup
        fex_code = """
        -SET &MIN_PRICE = 10000;
        TABLE FILE CAR
        PRINT CAR MODEL PRICE
        BY COUNTRY
        WHERE PRICE GT &MIN_PRICE
        END
        """

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
        # Mocking some metadata if necessary, but PostgresEmitter should handle defaults
        emitter = PostgresEmitter(metadata_registry=metadata)
        sql_output = emitter.emit(cfg)

        # 8. Verifications
        self.assertIn("CREATE OR REPLACE PROCEDURE", sql_output)
        self.assertIn("SELECT", sql_output)
        self.assertIn("FROM CAR", sql_output) # It seems it's not quoted in current emitter implementation
        self.assertIn("WHERE (PRICE > 10000)", sql_output)
        self.assertIn("ORDER BY COUNTRY ASC", sql_output)
        # Checking for the specific SQL generated for basic reporting
        self.assertIn("CAR", sql_output)
        self.assertIn("MODEL", sql_output)
        self.assertIn("PRICE", sql_output)
        self.assertIn("COUNTRY", sql_output)

    def test_basic_sum_report(self):
        # 1. Setup
        fex_code = """
        TABLE FILE SALES
        SUM UNITS DOLLARS
        BY REGION
        BY MONTH
        WHERE MONTH EQ 'JAN'
        END
        """

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

        # 6. Optimization (No constants here but good to run)
        ConstantPropagator().run(cfg)
        DeadCodeEliminator().run(cfg)

        # 7. Backend Emission
        emitter = PostgresEmitter()
        sql_output = emitter.emit(cfg)

        # 8. Verifications
        self.assertIn("SUM(UNITS)", sql_output)
        self.assertIn("SUM(DOLLARS)", sql_output)
        self.assertIn("FROM SALES", sql_output)
        self.assertIn("WHERE (MONTH = 'JAN')", sql_output)
        self.assertIn("GROUP BY REGION, MONTH", sql_output)

if __name__ == '__main__':
    unittest.main()

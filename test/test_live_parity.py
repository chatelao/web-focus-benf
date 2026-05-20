import unittest
import sys
import os
import json

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from db_utils import is_db_available
from runtime_runner import RuntimeRunner
from asg import MasterFile, Segment, Field
from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from antlr4 import CommonTokenStream, InputStream
from asg_builder import ReportASGBuilder
from ir_builder import IRBuilder
from ssa_transformer import SSATransformer
from emitter import PostgresEmitter
from metadata_registry import MetadataRegistry

class TestLiveParity(unittest.TestCase):
    """
    Integration tests against a live PostgreSQL database.
    These tests are skipped if no database is available.
    """

    @unittest.skipUnless(is_db_available(), "PostgreSQL not available")
    def test_live_db_connection(self):
        """
        Verify that we can actually connect and execute a simple query on the live DB.
        """
        with RuntimeRunner() as runner:
            with runner.conn.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
                self.assertEqual(result[0], 1)

    @unittest.skipUnless(is_db_available(), "PostgreSQL not available")
    def test_basic_report_parity(self):
        """
        End-to-end verification (DDL, fixtures, transpilation, execution) against a live database.
        """
        # 1. Define Metadata
        registry = MetadataRegistry()
        f1 = MasterFile(name="LIVE_SALES_DATA")
        s1 = Segment(name="LIVE_SALES_DATA")
        s1.fields = [
            Field(name="PRODUCT", alias="PROD", usage="A20"),
            Field(name="AMOUNT", alias="AMT", usage="I8")
        ]
        f1.segments = [s1]
        registry.register_master_file(f1)

        # 2. Prepare Fixtures
        sample_data = [
            {"PRODUCT": "Widgets", "AMOUNT": 100},
            {"PRODUCT": "Widgets", "AMOUNT": 200},
            {"PRODUCT": "Gadgets", "AMOUNT": 50},
        ]
        fixture_path = "live_sales_fixtures.json"
        with open(fixture_path, "w") as f:
            json.dump(sample_data, f)

        try:
            # 3. Transpile Report
            fex_code = """
            TABLE FILE LIVE_SALES_DATA
            SUM AMOUNT
            BY PRODUCT
            ON TABLE HOLD AS LIVE_AGG_RESULTS
            END
            """

            input_stream = InputStream(fex_code)
            lexer = WebFocusReportLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = WebFocusReportParser(token_stream)
            tree = parser.start()

            asg_nodes = ReportASGBuilder().visit(tree)
            cfg = IRBuilder().build(asg_nodes)
            SSATransformer().transform(cfg)

            emitter = PostgresEmitter(metadata_registry=registry)
            sql_procedure = emitter.emit(cfg, "live_parity_proc")

            # 4. Execute via RuntimeRunner
            with RuntimeRunner() as runner:
                # Setup schema and data
                runner.setup_schema([f1])
                runner.load_fixtures([("LIVE_SALES_DATA", fixture_path)])

                # Run the transpiled procedure
                runner.run_procedure(sql_procedure, "live_parity_proc")

                # Fetch results from the HOLD table
                results = runner.fetch_table("LIVE_AGG_RESULTS")

            # 5. Verification
            self.assertEqual(len(results), 2)

            # Sort results by PRODUCT for deterministic check
            results = sorted(results, key=lambda x: x['PRODUCT'])

            self.assertEqual(results[0]['PRODUCT'], 'Gadgets')
            self.assertEqual(results[0]['AMOUNT'], 50)

            self.assertEqual(results[1]['PRODUCT'], 'Widgets')
            self.assertEqual(results[1]['AMOUNT'], 300)

        finally:
            if os.path.exists(fixture_path):
                os.remove(fixture_path)

if __name__ == '__main__':
    unittest.main()

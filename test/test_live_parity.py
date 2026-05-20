import unittest
import os
import sys
import json
import psycopg2

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

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
from db_utils import get_db_connection

def is_db_available():
    """Checks if the PostgreSQL database is available."""
    try:
        conn = get_db_connection()
        conn.close()
        return True
    except Exception:
        return False

@unittest.skipUnless(is_db_available(), "PostgreSQL database not available")
class TestLiveParity(unittest.TestCase):
    """
    End-to-End integration test for result-set parity using a LIVE database.
    This test runs in CI environments where a real PostgreSQL instance is provided.
    """

    def setUp(self):
        self.registry = MetadataRegistry()
        self.runner = RuntimeRunner()

    def tearDown(self):
        self.runner.__exit__(None, None, None)

    def test_e2e_sum_aggregation_live(self):
        # 1. Define Metadata
        f1 = MasterFile(name="LIVE_SALES")
        s1 = Segment(name="LIVE_SALES")
        s1.fields = [
            Field(name="PRODUCT", alias="PROD", usage="A20"),
            Field(name="AMOUNT", alias="AMT", usage="I8")
        ]
        f1.segments = [s1]
        self.registry.register_master_file(f1)

        # 2. Prepare Fixtures
        sample_data = [
            {"PRODUCT": "Widgets", "AMOUNT": 100},
            {"PRODUCT": "Widgets", "AMOUNT": 200},
            {"PRODUCT": "Gadgets", "AMOUNT": 50},
        ]
        fixture_path = "test_live_sales_fixtures.json"
        with open(fixture_path, "w") as f:
            json.dump(sample_data, f)

        try:
            # 3. Transpile Report
            fex_code = """
            TABLE FILE LIVE_SALES
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

            emitter = PostgresEmitter(metadata_registry=self.registry)
            sql_procedure = emitter.emit(cfg, "test_live_parity_proc")

            # 4. Execute via RuntimeRunner on LIVE DB
            with self.runner as runner:
                # Cleanup if previous run failed
                with runner.conn.cursor() as cursor:
                    cursor.execute("DROP TABLE IF EXISTS LIVE_SALES CASCADE;")
                    cursor.execute("DROP TABLE IF EXISTS LIVE_AGG_RESULTS CASCADE;")
                    cursor.execute("DROP PROCEDURE IF EXISTS test_live_parity_proc();")

                runner.setup_schema([f1])
                runner.load_fixtures([("LIVE_SALES", fixture_path)])
                runner.run_procedure(sql_procedure, "test_live_parity_proc")
                results = runner.fetch_table("LIVE_AGG_RESULTS")

            # 5. Verification
            self.assertEqual(len(results), 2)

            # Results should be aggregated: Widgets: 300, Gadgets: 50
            gadgets = next(r for r in results if r['PRODUCT'] == 'Gadgets')
            self.assertEqual(gadgets['AMOUNT'], 50)

            # Some numeric types might come back as int or decimal depending on PG driver/mapping
            widgets = next(r for r in results if r['PRODUCT'] == 'Widgets')
            self.assertEqual(int(widgets['AMOUNT']), 300)

        finally:
            if os.path.exists(fixture_path):
                os.remove(fixture_path)
            # Cleanup DB
            try:
                if self.runner.conn:
                    with self.runner.conn.cursor() as cursor:
                        cursor.execute("DROP TABLE IF EXISTS LIVE_SALES CASCADE;")
                        cursor.execute("DROP TABLE IF EXISTS LIVE_AGG_RESULTS CASCADE;")
                        cursor.execute("DROP PROCEDURE IF EXISTS test_live_parity_proc();")
            except:
                pass

if __name__ == '__main__':
    unittest.main()

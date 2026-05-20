import unittest
import sys
import os
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

def is_db_reachable():
    try:
        conn = get_db_connection()
        conn.close()
        return True
    except Exception:
        return False

class TestLiveParity(unittest.TestCase):
    """
    Live integration test for result-set parity.
    Verifies the full pipeline against a real PostgreSQL database if available.
    """

    @unittest.skipUnless(is_db_reachable(), "PostgreSQL database not reachable")
    def test_live_aggregation_parity(self):
        # 1. Define Metadata
        registry = MetadataRegistry()
        f1 = MasterFile(name="LIVE_SALES")
        s1 = Segment(name="LIVE_SALES")
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

            emitter = PostgresEmitter(metadata_registry=registry)
            sql_procedure = emitter.emit(cfg, "test_live_parity_proc")

            # 4. Execute via RuntimeRunner
            with RuntimeRunner() as runner:
                # Cleanup if previous run failed
                with runner.conn.cursor() as cur:
                    cur.execute("DROP TABLE IF EXISTS \"LIVE_SALES\" CASCADE;")
                    cur.execute("DROP PROCEDURE IF EXISTS test_live_parity_proc();")

                runner.setup_schema([f1])
                runner.load_fixtures([("LIVE_SALES", fixture_path)])
                runner.run_procedure(sql_procedure, "test_live_parity_proc")
                results = runner.fetch_table("LIVE_AGG_RESULTS")

            # 5. Verification
            self.assertEqual(len(results), 2)

            # Sort results by PRODUCT for stable comparison
            results = sorted(results, key=lambda x: x['PRODUCT'])

            self.assertEqual(results[0]['PRODUCT'].strip(), 'Gadgets')
            self.assertEqual(int(results[0]['AMOUNT']), 50)

            self.assertEqual(results[1]['PRODUCT'].strip(), 'Widgets')
            self.assertEqual(int(results[1]['AMOUNT']), 300)

        finally:
            if os.path.exists(fixture_path):
                os.remove(fixture_path)

            # Final cleanup
            if is_db_reachable():
                try:
                    conn = get_db_connection()
                    with conn.cursor() as cur:
                        cur.execute("DROP TABLE IF EXISTS \"LIVE_SALES\" CASCADE;")
                        cur.execute("DROP PROCEDURE IF EXISTS test_live_parity_proc();")
                    conn.commit()
                    conn.close()
                except:
                    pass

if __name__ == '__main__':
    unittest.main()

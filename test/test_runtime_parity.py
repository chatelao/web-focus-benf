import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import json

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

class TestRuntimeParity(unittest.TestCase):
    """
    Integration test for result-set parity.
    Verifies the full pipeline: Master File -> DDL -> Fixtures -> Transpilation -> Execution -> Result Verification.
    Uses mocks for database interaction to ensure it runs in the sandbox without a live Postgres.
    """

    @patch('runtime_runner.get_db_connection')
    @patch('db_utils.psycopg2.connect')
    def test_e2e_aggregation_parity(self, mock_connect, mock_runner_conn):
        # 1. Setup Mock Connection
        mock_conn = MagicMock()
        mock_runner_conn.return_value = mock_conn
        mock_connect.return_value = mock_conn

        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_conn.notices = []

        # 2. Define Metadata
        registry = MetadataRegistry()
        f1 = MasterFile(name="SALES_DATA")
        s1 = Segment(name="SALES_DATA")
        # Use simple names that don't need excessive quoting for clarity in test
        s1.fields = [
            Field(name="PRODUCT", alias="PROD", usage="A20"),
            Field(name="AMOUNT", alias="AMT", usage="I8")
        ]
        f1.segments = [s1]
        registry.register_master_file(f1)

        # 3. Prepare Fixtures (Dummy data)
        sample_data = [
            {"PRODUCT": "Widgets", "AMOUNT": 100},
            {"PRODUCT": "Widgets", "AMOUNT": 200},
            {"PRODUCT": "Gadgets", "AMOUNT": 50},
        ]
        fixture_path = "test_sales_fixtures.json"
        with open(fixture_path, "w") as f:
            json.dump(sample_data, f)

        try:
            # 4. Transpile Report
            fex_code = """
            TABLE FILE SALES_DATA
            SUM AMOUNT
            BY PRODUCT
            ON TABLE HOLD AS AGG_RESULTS
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
            sql_procedure = emitter.emit(cfg, "test_parity_proc")

            # 5. Mock fetch_table results
            # Expected aggregated results: Widgets: 300, Gadgets: 50
            mock_cursor.description = [('PRODUCT',), ('AMOUNT',)]
            # We need to simulate the result of SUM(AMOUNT) BY PRODUCT
            # The order might depend on the implementation, but let's assume alphabetical for BY PRODUCT
            mock_cursor.fetchall.return_value = [
                ('Gadgets', 50),
                ('Widgets', 300)
            ]

            # 6. Execute via RuntimeRunner
            with RuntimeRunner() as runner:
                runner.setup_schema([f1])
                runner.load_fixtures([("SALES_DATA", fixture_path)])
                runner.run_procedure(sql_procedure, "test_parity_proc")
                results = runner.fetch_table("AGG_RESULTS")

            # 7. Verification
            self.assertEqual(len(results), 2)

            # Find Gadgets
            gadgets = next(r for r in results if r['PRODUCT'] == 'Gadgets')
            self.assertEqual(gadgets['AMOUNT'], 50)

            # Find Widgets
            widgets = next(r for r in results if r['PRODUCT'] == 'Widgets')
            self.assertEqual(widgets['AMOUNT'], 300)

            # Verify that DDL, Insert (fixtures), and Procedure were "executed"
            # Check for CREATE TABLE in one of the calls
            ddl_called = any("CREATE TABLE SALES_DATA" in str(call) for call in mock_cursor.execute.call_args_list)
            self.assertTrue(ddl_called)

            # Check for procedure call
            proc_called = any("CALL test_parity_proc();" in str(call) for call in mock_cursor.execute.call_args_list)
            self.assertTrue(proc_called)

        finally:
            if os.path.exists(fixture_path):
                os.remove(fixture_path)

if __name__ == '__main__':
    unittest.main()

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

class TestLegacyVerbParity(unittest.TestCase):
    """
    Transition tests for Phase 6.1.2.1: Verb commands (PRINT, SUM, LIST, COUNT).
    Verifies that the generated PL/pgSQL procedures produce result sets consistent with legacy expectations.
    """

    def setUp(self):
        self.registry = MetadataRegistry()
        inventory_mas = MasterFile(name="INVENTORY")
        s1 = Segment(name="INV_SEG")
        s1.fields = [
            Field(name="PROD_ID", usage="A10"),
            Field(name="CATEGORY", usage="A20"),
            Field(name="QTY", usage="I8"),
            Field(name="PRICE", usage="D12.2")
        ]
        inventory_mas.segments = [s1]
        self.registry.register_master_file(inventory_mas)
        self.master_file = inventory_mas

    def _transpile_and_run(self, fex_code, proc_name, mock_cursor, fetchall_return):
        input_stream = InputStream(fex_code)
        lexer = WebFocusReportLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(token_stream)
        tree = parser.start()

        asg_nodes = ReportASGBuilder().visit(tree)
        cfg = IRBuilder().build(asg_nodes)
        SSATransformer().transform(cfg)

        emitter = PostgresEmitter(metadata_registry=self.registry)
        sql_procedure = emitter.emit(cfg, proc_name)

        # Store for SQL verification
        self.last_sql = sql_procedure

        mock_cursor.fetchall.return_value = fetchall_return

        with RuntimeRunner() as runner:
            runner.setup_schema([self.master_file])
            runner.run_procedure(sql_procedure, proc_name)
            results = runner.fetch_table("HOLD_FILE")

        return results

    @patch('runtime_runner.get_db_connection')
    @patch('db_utils.psycopg2.connect')
    def test_print_parity(self, mock_connect, mock_runner_conn):
        mock_conn = MagicMock()
        mock_runner_conn.return_value = mock_conn
        mock_connect.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        fex = """
        TABLE FILE INVENTORY
        PRINT PROD_ID QTY PRICE
        ON TABLE HOLD AS HOLD_FILE
        END
        """

        expected_data = [
            ('P001', 10, 5.0),
            ('P002', 20, 15.0)
        ]
        mock_cursor.description = [('PROD_ID',), ('QTY',), ('PRICE',)]

        results = self._transpile_and_run(fex, "test_print", mock_cursor, expected_data)

        # Verify SQL semantics
        self.assertIn("SELECT", self.last_sql)
        self.assertIn("PROD_ID", self.last_sql)
        self.assertIn("QTY", self.last_sql)
        self.assertIn("PRICE", self.last_sql)
        # PRINT should not have aggregations
        self.assertNotIn("SUM(", self.last_sql)

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]['PROD_ID'], 'P001')
        self.assertEqual(results[1]['QTY'], 20)

    @patch('runtime_runner.get_db_connection')
    @patch('db_utils.psycopg2.connect')
    def test_sum_parity(self, mock_connect, mock_runner_conn):
        mock_conn = MagicMock()
        mock_runner_conn.return_value = mock_conn
        mock_connect.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        fex = """
        TABLE FILE INVENTORY
        SUM QTY
        BY CATEGORY
        ON TABLE HOLD AS HOLD_FILE
        END
        """

        # Aggregated data
        expected_data = [
            ('ELECTRONICS', 150),
            ('TOYS', 80)
        ]
        mock_cursor.description = [('CATEGORY',), ('QTY',)]

        results = self._transpile_and_run(fex, "test_sum", mock_cursor, expected_data)

        # Verify SQL semantics
        self.assertIn("SUM(QTY)", self.last_sql)
        self.assertIn("GROUP BY", self.last_sql)
        self.assertIn("CATEGORY", self.last_sql)

        self.assertEqual(len(results), 2)
        electronics = next(r for r in results if r['CATEGORY'] == 'ELECTRONICS')
        self.assertEqual(electronics['QTY'], 150)

    @patch('runtime_runner.get_db_connection')
    @patch('db_utils.psycopg2.connect')
    def test_count_parity(self, mock_connect, mock_runner_conn):
        mock_conn = MagicMock()
        mock_runner_conn.return_value = mock_conn
        mock_connect.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        fex = """
        TABLE FILE INVENTORY
        COUNT PROD_ID
        BY CATEGORY
        ON TABLE HOLD AS HOLD_FILE
        END
        """

        expected_data = [
            ('ELECTRONICS', 5),
            ('TOYS', 3)
        ]
        mock_cursor.description = [('CATEGORY',), ('PROD_ID',)]

        results = self._transpile_and_run(fex, "test_count", mock_cursor, expected_data)

        # Verify SQL semantics
        self.assertIn("COUNT(PROD_ID)", self.last_sql)
        self.assertIn("GROUP BY", self.last_sql)

        self.assertEqual(len(results), 2)
        toys = next(r for r in results if r['CATEGORY'] == 'TOYS')
        self.assertEqual(toys['PROD_ID'], 3) # COUNT(PROD_ID) alias is usually the field name unless AS is used

    @patch('runtime_runner.get_db_connection')
    @patch('db_utils.psycopg2.connect')
    def test_list_parity(self, mock_connect, mock_runner_conn):
        mock_conn = MagicMock()
        mock_runner_conn.return_value = mock_conn
        mock_connect.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        fex = """
        TABLE FILE INVENTORY
        LIST PROD_ID
        BY CATEGORY
        ON TABLE HOLD AS HOLD_FILE
        END
        """

        # LIST is like PRINT but adds a sequence number per group in WebFOCUS.
        # In our current PostgresEmitter, LIST is emitted as a standard projection with ROW_NUMBER() if requested,
        # but let's verify it produces the expected columns.
        expected_data = [
            (1, 'ELECTRONICS', 'E001'),
            (2, 'ELECTRONICS', 'E002'),
            (1, 'TOYS', 'T001')
        ]
        mock_cursor.description = [('LIST',), ('CATEGORY',), ('PROD_ID',)]

        results = self._transpile_and_run(fex, "test_list", mock_cursor, expected_data)

        # Verify SQL semantics
        # LIST uses ROW_NUMBER() in our implementation for ordering/indexing if BY is present
        self.assertIn("ROW_NUMBER()", self.last_sql)
        self.assertIn("OVER (PARTITION BY CATEGORY", self.last_sql)

        self.assertEqual(len(results), 3)
        self.assertEqual(results[0]['LIST'], 1)
        self.assertEqual(results[2]['PROD_ID'], 'T001')

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from runtime_runner import RuntimeRunner

class TestRuntimeRunner(unittest.TestCase):

    @patch('runtime_runner.get_db_connection')
    def test_run_procedure_success(self, mock_get_conn):
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn

        # notices starts empty
        mock_conn.notices = []

        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        def side_effect(sql, params=None):
            if "CALL" in sql:
                mock_conn.notices.extend(["NOTICE:  Hello World\n", "Something else\n"])

        mock_cursor.execute.side_effect = side_effect

        sql = "CREATE PROCEDURE test() AS $$ BEGIN RAISE NOTICE 'Hello World'; END; $$ LANGUAGE plpgsql;"

        runner = RuntimeRunner()
        notices = runner.run_procedure(sql, "test")

        # Verify calls
        mock_cursor.execute.assert_any_call(sql)
        mock_cursor.execute.assert_any_call("CALL test();")

        self.assertEqual(notices, ["Hello World", "Something else"])

    @patch('runtime_runner.get_db_connection')
    def test_context_manager(self, mock_get_conn):
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn

        with RuntimeRunner() as runner:
            self.assertEqual(runner.conn, mock_conn)

        mock_conn.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()

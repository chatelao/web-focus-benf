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

    @patch('runtime_runner.DDLGenerator')
    @patch('runtime_runner.get_db_connection')
    def test_setup_schema(self, mock_get_conn, mock_ddl_gen_class):
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        mock_ddl_gen = mock_ddl_gen_class.return_value
        mock_ddl_gen.generate.return_value = "CREATE TABLE TEST;"

        master = MagicMock()
        runner = RuntimeRunner()
        runner.setup_schema([master])

        mock_ddl_gen.generate.assert_called_once_with(master)
        mock_cursor.execute.assert_called_once_with("CREATE TABLE TEST;")

    @patch('runtime_runner.FixtureLoader')
    def test_load_fixtures(self, mock_loader_class):
        mock_loader = mock_loader_class.return_value

        runner = RuntimeRunner()
        fixtures_config = [
            ('TABLE1', 'data1.json'),
            ('TABLE2', 'data2.csv')
        ]
        runner.load_fixtures(fixtures_config)

        mock_loader.load_json.assert_called_once_with('TABLE1', 'data1.json')
        mock_loader.load_csv.assert_called_once_with('TABLE2', 'data2.csv')

if __name__ == '__main__':
    unittest.main()

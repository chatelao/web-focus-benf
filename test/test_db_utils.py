import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from db_utils import get_db_connection, db_cursor

class TestDBUtils(unittest.TestCase):

    @patch('psycopg2.connect')
    def test_get_db_connection_defaults(self, mock_connect):
        # Ensure env vars are NOT set
        with patch.dict(os.environ, {}, clear=True):
            get_db_connection()
            mock_connect.assert_called_once_with(
                host='localhost',
                port='5432',
                dbname='webfocus_test',
                user='webfocus',
                password='password'
            )

    @patch('psycopg2.connect')
    def test_get_db_connection_env_vars(self, mock_connect):
        env_vars = {
            'PGHOST': 'myhost',
            'PGPORT': '1234',
            'PGDATABASE': 'mydb',
            'PGUSER': 'myuser',
            'PGPASSWORD': 'mypassword'
        }
        with patch.dict(os.environ, env_vars):
            get_db_connection()
            mock_connect.assert_called_once_with(
                host='myhost',
                port='1234',
                dbname='mydb',
                user='myuser',
                password='mypassword'
            )

    @patch('db_utils.get_db_connection')
    def test_db_cursor_context_manager_success(self, mock_get_conn):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor

        with db_cursor() as cursor:
            self.assertEqual(cursor, mock_cursor)

        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()
        mock_conn.rollback.assert_not_called()

    @patch('db_utils.get_db_connection')
    def test_db_cursor_context_manager_failure(self, mock_get_conn):
        mock_conn = MagicMock()
        mock_get_conn.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.side_effect = Exception("Test Error")

        with self.assertRaises(Exception):
            with db_cursor():
                pass

        mock_conn.rollback.assert_called_once()
        mock_conn.close.assert_called_once()
        mock_conn.commit.assert_not_called()

if __name__ == '__main__':
    unittest.main()

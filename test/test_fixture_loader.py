import unittest
from unittest.mock import patch, MagicMock, mock_open, ANY
import json
import csv
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from fixture_loader import FixtureLoader

class TestFixtureLoader(unittest.TestCase):

    @patch('fixture_loader.db_cursor')
    @patch('builtins.open', new_callable=mock_open, read_data='[{"ID": 1, "NAME": "Alice"}]')
    @patch('json.load')
    def test_load_json_success(self, mock_json_load, mock_file, mock_db_cursor):
        mock_json_load.return_value = [{"ID": 1, "NAME": "Alice"}]
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor

        loader = FixtureLoader()
        loader.load_json("EMPLOYEE", "dummy.json")

        # Verify SQL (using ANY for the psycopg2.sql.Composed object)
        mock_cursor.execute.assert_called_once_with(ANY, [1, "Alice"])

    @patch('fixture_loader.db_cursor')
    def test_load_csv_success(self, mock_db_cursor):
        csv_content = "ID,NAME\n1,Alice\n2,Bob\n"
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor

        with patch('builtins.open', mock_open(read_data=csv_content)):
            loader = FixtureLoader()
            loader.load_csv("EMPLOYEE", "dummy.csv")

        # Verify SQL calls
        self.assertEqual(mock_cursor.execute.call_count, 2)
        mock_cursor.execute.assert_any_call(ANY, ["1", "Alice"])
        mock_cursor.execute.assert_any_call(ANY, ["2", "Bob"])

    @patch('fixture_loader.db_cursor')
    @patch('builtins.open', new_callable=mock_open, read_data='{}')
    @patch('json.load')
    def test_load_json_invalid_format(self, mock_json_load, mock_file, mock_db_cursor):
        mock_json_load.return_value = {"not": "a list"}
        loader = FixtureLoader()
        with self.assertRaises(ValueError):
            loader.load_json("TABLE", "dummy.json")

    @patch('fixture_loader.db_cursor')
    def test_load_empty_data(self, mock_db_cursor):
        mock_cursor = MagicMock()
        mock_db_cursor.return_value.__enter__.return_value = mock_cursor

        loader = FixtureLoader()

        # Test empty list doesn't call cursor.execute
        loader._insert_data("TABLE", [])
        mock_cursor.execute.assert_not_called()

if __name__ == '__main__':
    unittest.main()

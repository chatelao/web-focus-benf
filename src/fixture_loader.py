import json
import csv
from db_utils import db_cursor

class FixtureLoader:
    """
    Loads test data from JSON or CSV files into PostgreSQL tables.
    """

    def load_json(self, table_name, filepath, cursor=None):
        """
        Loads data from a JSON file into the specified table.
        The JSON file should contain a list of dictionaries.
        """
        with open(filepath, 'r') as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError(f"JSON fixture {filepath} must be a list of objects.")

        if not data:
            return

        self._insert_data(table_name, data, cursor=cursor)

    def load_csv(self, table_name, filepath, cursor=None):
        """
        Loads data from a CSV file into the specified table.
        The CSV file must have a header row.
        """
        data = []
        with open(filepath, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)

        if not data:
            return

        self._insert_data(table_name, data, cursor=cursor)

    def _insert_data(self, table_name, data, cursor=None):
        """
        Internal helper to insert a list of dictionaries into a table.
        """
        if not data:
            return

        # Use the keys from the first dictionary as column names
        columns = [c.upper() for c in data[0].keys()]

        # Prepare the INSERT statement
        col_str = ", ".join([f'"{c}"' for c in columns])
        placeholders = ", ".join(["%s"] * len(columns))
        sql = f'INSERT INTO "{table_name.upper()}" ({col_str}) VALUES ({placeholders})'

        if cursor:
            self._execute_insert(cursor, sql, data, columns)
        else:
            with db_cursor() as cursor:
                self._execute_insert(cursor, sql, data, columns)

    def _execute_insert(self, cursor, sql, data, columns):
        # We need to map the original keys to the upper-case column names
        original_keys = list(data[0].keys())
        key_map = {c.upper(): c for c in original_keys}

        for row in data:
            values = [row.get(key_map[c]) for c in columns]
            cursor.execute(sql, values)

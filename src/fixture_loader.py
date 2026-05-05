import json
import csv
from db_utils import db_cursor

class FixtureLoader:
    """
    Loads test data from JSON or CSV files into PostgreSQL tables.
    """

    def load_json(self, table_name, filepath):
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

        self._insert_data(table_name, data)

    def load_csv(self, table_name, filepath):
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

        self._insert_data(table_name, data)

    def _insert_data(self, table_name, data):
        """
        Internal helper to insert a list of dictionaries into a table.
        """
        if not data:
            return

        # Use the keys from the first dictionary as column names
        columns = list(data[0].keys())

        # Prepare the INSERT statement
        col_str = ", ".join([f'"{c}"' for c in columns])
        placeholders = ", ".join(["%s"] * len(columns))
        sql = f'INSERT INTO "{table_name.upper()}" ({col_str}) VALUES ({placeholders})'

        with db_cursor() as cursor:
            for row in data:
                values = [row.get(c) for c in columns]
                cursor.execute(sql, values)

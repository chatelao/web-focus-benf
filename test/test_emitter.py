import unittest
import os
import sys

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from emitter import PostgresEmitter

class TestEmitter(unittest.TestCase):
    def test_basic_procedure_emission(self):
        emitter = PostgresEmitter()

        procedure_name = "test_procedure"
        parameters = [
            {"name": "p_input", "type": "TEXT"},
            {"name": "p_id", "type": "INTEGER"}
        ]
        variables = [
            {"name": "v_counter", "type": "INTEGER"},
            {"name": "v_name", "type": "TEXT"}
        ]
        body = "v_counter := 1;\nRAISE NOTICE 'Input: %', p_input;"

        sql = emitter.emit_procedure(procedure_name, parameters, variables, body)

        self.assertIn("CREATE OR REPLACE PROCEDURE test_procedure", sql)
        self.assertIn("IN p_input TEXT,", sql)
        self.assertIn("IN p_id INTEGER", sql)
        self.assertIn("v_counter INTEGER;", sql)
        self.assertIn("v_name TEXT;", sql)
        self.assertIn("    v_counter := 1;", sql)
        self.assertIn("    RAISE NOTICE 'Input: %', p_input;", sql)
        self.assertIn("LANGUAGE plpgsql", sql)

if __name__ == '__main__':
    unittest.main()

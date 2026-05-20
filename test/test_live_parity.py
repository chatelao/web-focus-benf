import unittest
import sys
import os

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from db_utils import is_db_available
from runtime_runner import RuntimeRunner

class TestLiveParity(unittest.TestCase):
    """
    Integration tests against a live PostgreSQL database.
    These tests are skipped if no database is available.
    """

    @unittest.skipUnless(is_db_available(), "PostgreSQL not available")
    def test_live_db_connection(self):
        """
        Verify that we can actually connect and execute a simple query on the live DB.
        """
        with RuntimeRunner() as runner:
            with runner.conn.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
                self.assertEqual(result[0], 1)

if __name__ == '__main__':
    unittest.main()

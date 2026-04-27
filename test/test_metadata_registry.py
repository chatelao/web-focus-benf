import unittest
import os
import tempfile
import shutil
import sys

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from metadata_registry import MetadataRegistry
from asg import MasterFile

class TestMetadataRegistry(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.registry = MetadataRegistry([self.test_dir])

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def create_mas_file(self, name, content):
        path = os.path.join(self.test_dir, f"{name}.mas")
        with open(path, 'w') as f:
            f.write(content)
        return path

    def test_load_from_path(self):
        content = "FILENAME=CAR, SUFFIX=FOC,$"
        self.create_mas_file("CAR", content)

        mf = self.registry.get_master_file("CAR")
        self.assertIsNotNone(mf)
        self.assertIsInstance(mf, MasterFile)
        self.assertEqual(mf.name, "CAR")

    def test_caching(self):
        content = "FILENAME=CAR, SUFFIX=FOC,$"
        self.create_mas_file("CAR", content)

        mf1 = self.registry.get_master_file("CAR")
        mf2 = self.registry.get_master_file("CAR")

        self.assertIs(mf1, mf2) # Should be the same object from cache

    def test_case_insensitivity(self):
        content = "FILENAME=CAR, SUFFIX=FOC,$"
        self.create_mas_file("CAR", content)

        mf = self.registry.get_master_file("car")
        self.assertIsNotNone(mf)
        self.assertEqual(mf.name, "CAR")

    def test_multiple_paths(self):
        dir2 = tempfile.mkdtemp()
        try:
            self.registry.add_search_path(dir2)
            content = "FILENAME=EMPLOYEE, SUFFIX=FOC,$"
            path = os.path.join(dir2, "EMPLOYEE.mas")
            with open(path, 'w') as f:
                f.write(content)

            mf = self.registry.get_master_file("EMPLOYEE")
            self.assertIsNotNone(mf)
            self.assertEqual(mf.name, "EMPLOYEE")
        finally:
            shutil.rmtree(dir2)

    def test_missing_file(self):
        mf = self.registry.get_master_file("NONEXISTENT")
        self.assertIsNone(mf)

    def test_invalid_file(self):
        # Create a file that will fail parsing
        self.create_mas_file("INVALID", "THIS IS NOT A VALID MASTER FILE")

        mf = self.registry.get_master_file("INVALID")
        self.assertIsNone(mf) # get_master_file catches the exception and returns None

if __name__ == '__main__':
    unittest.main()

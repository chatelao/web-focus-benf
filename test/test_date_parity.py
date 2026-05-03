import unittest
from type_inferrer import TypeInferrer
from emitter import PostgresEmitter

class TestDateParity(unittest.TestCase):
    def setUp(self):
        self.inferrer = TypeInferrer()
        self.emitter = PostgresEmitter()

    def test_type_inferrer_preserves_format(self):
        self.assertEqual(self.inferrer._get_base_type('A10'), 'A10')
        self.assertEqual(self.inferrer._get_base_type('YYMD'), 'YYMD')
        self.assertEqual(self.inferrer._get_base_type('HYYMDI'), 'HYYMDI')
        self.assertEqual(self.inferrer._get_base_type('I8'), 'I8')

    def test_postgres_emitter_maps_dates(self):
        self.assertEqual(self.emitter._map_type('YYMD'), 'DATE')
        self.assertEqual(self.emitter._map_type('MDYY'), 'DATE')
        self.assertEqual(self.emitter._map_type('DMYY'), 'DATE')
        self.assertEqual(self.emitter._map_type('YMD'), 'DATE')
        self.assertEqual(self.emitter._map_type('MDY'), 'DATE')
        self.assertEqual(self.emitter._map_type('DMY'), 'DATE')

    def test_postgres_emitter_maps_timestamps(self):
        self.assertEqual(self.emitter._map_type('HYYMDI'), 'TIMESTAMP')
        self.assertEqual(self.emitter._map_type('HYYMDm'), 'TIMESTAMP')
        self.assertEqual(self.emitter._map_type('H'), 'TIMESTAMP')

    def test_postgres_emitter_maps_alpha(self):
        self.assertEqual(self.emitter._map_type('A10'), 'CHAR(10)')
        self.assertEqual(self.emitter._map_type('A'), 'TEXT')

if __name__ == '__main__':
    unittest.main()

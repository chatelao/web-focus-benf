import unittest
import os
import sys

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from emitter import PostgresEmitter

class TestEmitter(unittest.TestCase):
    def test_emitter_basic_render(self):
        emitter = PostgresEmitter()
        output = emitter.render('base.sql.j2', procedure_name='test_proc', procedure_body='RAISE NOTICE \'Hello\';')

        self.assertIn('CREATE OR REPLACE PROCEDURE test_proc()', output)
        self.assertIn('RAISE NOTICE \'Hello\';', output)
        self.assertIn('END;', output)

    def test_emit_procedure(self):
        emitter = PostgresEmitter()
        output = emitter.emit_procedure('my_procedure', 'SELECT 1;')

        self.assertIn('CREATE OR REPLACE PROCEDURE my_procedure()', output)
        self.assertIn('    SELECT 1;', output)  # Testing indentation

if __name__ == '__main__':
    unittest.main()

import unittest
import os
import sys

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from emitter import PostgresEmitter
import ir

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

    def test_emit_procedure_with_variables(self):
        emitter = PostgresEmitter()
        vars = {'v_X': 'INTEGER', 'v_Y': 'TEXT'}
        output = emitter.emit_procedure('var_proc', 'v_X := 10;', variables=vars)

        self.assertIn('DECLARE', output)
        self.assertIn('v_X INTEGER;', output)
        self.assertIn('v_Y TEXT;', output)
        self.assertIn('BEGIN', output)
        self.assertIn('v_X := 10;', output)

    def test_get_variables_from_cfg(self):
        emitter = PostgresEmitter()
        cfg = ir.ControlFlowGraph()
        block = ir.BasicBlock('B1')

        # Mocking instruction with data_type
        instr1 = ir.Assign(target='&VAR1', source=None)
        instr1.data_type = 'I'

        instr2 = ir.Assign(target='&VAR2', source=None)
        instr2.data_type = 'F'

        instr3 = ir.Assign(target='&VAR3', source=None)
        instr3.data_type = 'LOGICAL'

        block.add_instruction(instr1)
        block.add_instruction(instr2)
        block.add_instruction(instr3)
        cfg.add_block(block)

        variables = emitter.get_variables_from_cfg(cfg)

        self.assertEqual(variables['v_VAR1'], 'INTEGER')
        self.assertEqual(variables['v_VAR2'], 'NUMERIC')
        self.assertEqual(variables['v_VAR3'], 'BOOLEAN')

if __name__ == '__main__':
    unittest.main()

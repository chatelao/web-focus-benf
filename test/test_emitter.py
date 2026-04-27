import unittest
import os
import sys

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from emitter import PostgresEmitter
import ir
import asg

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

    def test_emit_expression_literals(self):
        emitter = PostgresEmitter()

        self.assertEqual(emitter.emit_expression(asg.Literal(10)), "10")
        self.assertEqual(emitter.emit_expression(asg.Literal("hello")), "'hello'")
        self.assertEqual(emitter.emit_expression(asg.Literal(123.45)), "123.45")

    def test_emit_expression_variables(self):
        emitter = PostgresEmitter()

        self.assertEqual(emitter.emit_expression(asg.AmperVar("&X")), "v_X")
        self.assertEqual(emitter.emit_expression(asg.Identifier("FIELD")), "v_FIELD")

    def test_emit_expression_binary(self):
        emitter = PostgresEmitter()
        expr = asg.BinaryOperation(asg.AmperVar("&X"), "EQ", asg.Literal(10))
        self.assertEqual(emitter.emit_expression(expr), "(v_X = 10)")

        expr = asg.BinaryOperation(asg.AmperVar("&A"), "CONCAT", asg.Literal("suffix"))
        self.assertEqual(emitter.emit_expression(expr), "(v_A || 'suffix')")

    def test_emit_expression_unary(self):
        emitter = PostgresEmitter()
        expr = asg.UnaryOperation("NOT", asg.AmperVar("&B"))
        self.assertEqual(emitter.emit_expression(expr), "NOT (v_B)")

    def test_emit_expression_function(self):
        emitter = PostgresEmitter()
        expr = asg.FunctionCall("ABS", [asg.Literal(-5)])
        self.assertEqual(emitter.emit_expression(expr), "ABS(-5)")

    def test_emit_expression_if(self):
        emitter = PostgresEmitter()
        expr = asg.IfExpression(
            condition=asg.BinaryOperation(asg.AmperVar("&X"), "GT", asg.Literal(0)),
            then_expr=asg.Literal("pos"),
            else_expr=asg.Literal("neg")
        )
        self.assertEqual(emitter.emit_expression(expr), "(CASE WHEN (v_X > 0) THEN 'pos' ELSE 'neg' END)")

    def test_emit_instruction_assign(self):
        emitter = PostgresEmitter()
        instr = ir.Assign(target="&X", source=asg.Literal(10))
        self.assertEqual(emitter.emit_instruction(instr), "v_X := 10;")

    def test_emit_instruction_type(self):
        emitter = PostgresEmitter()
        instr = ir.Type(messages=[asg.Literal("Value is: "), asg.AmperVar("&X")])
        self.assertEqual(emitter.emit_instruction(instr), "RAISE NOTICE '%', 'Value is: ' || v_X;")

if __name__ == '__main__':
    unittest.main()

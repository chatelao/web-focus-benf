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
        self.assertEqual(variables['v_VAR2'], 'DOUBLE PRECISION')
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

    def test_emit_cfg_complex(self):
        emitter = PostgresEmitter()
        cfg = ir.ControlFlowGraph()

        b1 = ir.BasicBlock('B1')
        b1.add_instruction(ir.Assign(target='&X', source=asg.Literal(1)))

        b2 = ir.BasicBlock('B2')
        # Phi(X_1, X_2)
        phi = ir.Phi(target='&X_SSA', sources=['&X_B1', '&X_B3'])
        b2.add_instruction(phi)
        b2.add_instruction(ir.Type(messages=[asg.Literal("X is "), asg.AmperVar("&X_SSA")]))

        b3 = ir.BasicBlock('B3')
        b3.add_instruction(ir.Assign(target='&X', source=asg.Literal(2)))

        cfg.add_block(b1)
        cfg.add_block(b2)
        cfg.add_block(b3)
        cfg.entry_block = b1

        # B1 -> B2
        cfg.add_edge('B1', 'B2')
        # B2 -> B3
        cfg.add_edge('B2', 'B3')
        # B3 -> B2
        cfg.add_edge('B3', 'B2')

        # B1 needs a jump or fallthrough. Emitter handles fallthrough.
        # But let's be explicit.
        b1.add_instruction(ir.Jump(target='B2'))

        # B2: if X_SSA < 10 branch to B3 else EXIT
        b2.add_instruction(ir.Branch(
            condition=asg.BinaryOperation(asg.AmperVar("&X_SSA"), "LT", asg.Literal(10)),
            true_target='B3',
            false_target='EXIT'
        ))

        # B3 jumps back to B2
        b3.add_instruction(ir.Jump(target='B2'))

        output = emitter.emit_cfg(cfg)

        # Check for block dispatcher structure
        self.assertIn("WHILE v_next_block NOT IN ('EXIT', 'DONE') LOOP", output)
        self.assertIn("CASE v_next_block", output)
        self.assertIn("WHEN 'B1' THEN", output)
        self.assertIn("WHEN 'B2' THEN", output)
        self.assertIn("WHEN 'B3' THEN", output)

        # Check Phi resolution in B1 -> B2
        # In B1, it should set X_SSA from X_B1 (if X_B1 was the name, but here we just used &X)
        # Wait, the test uses &X_B1 as source for Phi in B2.
        self.assertIn("v_X_SSA := v_X_B1;", output) # Resolution for B1 -> B2
        self.assertIn("v_X_SSA := v_X_B3;", output) # Resolution for B3 -> B2

        # Check Branch
        self.assertIn("v_next_block := CASE WHEN (v_X_SSA < 10) THEN 'B3' ELSE 'EXIT' END;", output)

    def test_emit_full_procedure(self):
        emitter = PostgresEmitter()
        cfg = ir.ControlFlowGraph()
        b1 = ir.BasicBlock('START')
        assign = ir.Assign(target='&VAR', source=asg.Literal(100))
        assign.data_type = 'I'
        b1.add_instruction(assign)
        cfg.add_block(b1)
        cfg.entry_block = b1

        variables = emitter.get_variables_from_cfg(cfg)
        body = emitter.emit_cfg(cfg)
        proc = emitter.emit_procedure('test_full', body, variables=variables)

        self.assertIn("DECLARE", proc)
        self.assertIn("v_VAR INTEGER;", proc)
        self.assertIn("v_next_block TEXT;", proc)
        self.assertIn("BEGIN", proc)
        self.assertIn("v_VAR := 100;", proc)

    def test_map_type_precision(self):
        emitter = PostgresEmitter()
        self.assertEqual(emitter._map_type('I'), 'INTEGER')
        self.assertEqual(emitter._map_type('I4'), 'INTEGER')
        self.assertEqual(emitter._map_type('I8'), 'BIGINT')
        self.assertEqual(emitter._map_type('F8'), 'DOUBLE PRECISION')
        self.assertEqual(emitter._map_type('D12'), 'DOUBLE PRECISION')
        self.assertEqual(emitter._map_type('F8.2'), 'NUMERIC(8, 2)')
        self.assertEqual(emitter._map_type('P9.2'), 'NUMERIC(9, 2)')
        self.assertEqual(emitter._map_type('P9'), 'NUMERIC(9, 0)')
        self.assertEqual(emitter._map_type('A10'), 'CHAR(10)')

    def test_emit_instruction_report(self):
        emitter = PostgresEmitter()

        # Mocking a VerbCommand with FieldSelections
        f1 = asg.FieldSelection(name="FIELD1")
        f2 = asg.FieldSelection(name="FIELD2")
        verb = asg.VerbCommand(verb="PRINT", fields=[f1, f2])

        instr = ir.Report(filename="MYTABLE", components=[verb])

        sql = emitter.emit_instruction(instr)

        self.assertIn("SELECT FIELD1, FIELD2", sql)
        self.assertIn("FROM MYTABLE", sql)
        self.assertIn("/* MYTABLE */", sql)

    def test_emit_instruction_report_with_where(self):
        emitter = PostgresEmitter()
        verb = asg.VerbCommand(verb="PRINT", fields=[asg.FieldSelection(name="FIELD1")])

        # Simple WHERE
        where1 = asg.WhereClause(condition=asg.BinaryOperation(asg.Identifier("FIELD1"), "GT", asg.Literal(10)))

        # BETWEEN
        where2 = asg.WhereClause(condition=asg.BetweenExpression(asg.Identifier("FIELD2"), asg.Literal(1), asg.Literal(100)))

        # IN
        where3 = asg.WhereClause(condition=asg.InExpression(asg.Identifier("FIELD3"), [asg.Literal("A"), asg.Literal("B")]))

        # IS MISSING
        where4 = asg.WhereClause(condition=asg.IsMissingExpression(asg.Identifier("FIELD4")))

        instr = ir.Report(filename="MYTABLE", components=[verb, where1, where2, where3, where4])

        sql = emitter.emit_instruction(instr)

        self.assertIn("WHERE (FIELD1 > 10)", sql)
        self.assertIn("AND (FIELD2 BETWEEN 1 AND 100)", sql)
        self.assertIn("AND (FIELD3 IN ('A', 'B'))", sql)
        self.assertIn("AND (FIELD4 IS NULL)", sql)

    def test_emit_instruction_report_advanced(self):
        emitter = PostgresEmitter()

        # BY REGION
        s1 = asg.SortCommand(sort_type="BY", field=asg.FieldSelection(name="REGION"))
        # BY HIGHEST DATE
        s2 = asg.SortCommand(sort_type="BY", field=asg.FieldSelection(name="DATE"), options={"order": "HIGHEST"})
        # BY DEPT NOPRINT
        s3 = asg.SortCommand(sort_type="BY", field=asg.FieldSelection(name="DEPT"), noprint=True)

        # SUM SALES AS 'Total Sales'
        f1 = asg.FieldSelection(name="SALES", alias="Total Sales")
        # AVE.COST
        f2 = asg.FieldSelection(name="COST", prefix_operators=["AVE"])
        verb = asg.VerbCommand(verb="SUM", fields=[f1, f2])

        instr = ir.Report(filename="SALES_DATA", components=[s1, s2, s3, verb])

        sql = emitter.emit_instruction(instr)

        # SELECT should include non-noprint sort fields and verb fields
        # Note: sort fields come first in my implementation
        self.assertIn("SELECT REGION, DATE, SUM(SALES) AS \"Total Sales\", AVG(COST)", sql)
        self.assertIn("FROM SALES_DATA", sql)
        # GROUP BY should include all sort fields
        self.assertIn("GROUP BY REGION, DATE, DEPT", sql)
        # ORDER BY
        self.assertIn("ORDER BY REGION ASC, DATE DESC, DEPT ASC", sql)

    def test_emit_instruction_report_with_where_total(self):
        emitter = PostgresEmitter()
        verb = asg.VerbCommand(verb="SUM", fields=[asg.FieldSelection(name="SALES")])
        sort = asg.SortCommand(sort_type="BY", field=asg.FieldSelection(name="REGION"))

        # WHERE TOTAL SALES GT 1000
        where_total = asg.WhereClause(
            condition=asg.BinaryOperation(asg.Identifier("SALES"), "GT", asg.Literal(1000)),
            is_total=True
        )

        instr = ir.Report(filename="SALES_DATA", components=[verb, sort, where_total])

        sql = emitter.emit_instruction(instr)

        self.assertIn("SELECT REGION, SUM(SALES)", sql)
        self.assertIn("GROUP BY REGION", sql)
        self.assertIn("HAVING (SUM(SALES) > 1000)", sql)

    def test_emit_instruction_report_with_compute(self):
        emitter = PostgresEmitter()
        verb = asg.VerbCommand(verb="SUM", fields=[asg.FieldSelection(name="SALES")])
        compute = asg.ComputeCommand(
            name="RATIO",
            expression=asg.BinaryOperation(asg.Identifier("SALES"), "/", asg.Literal(1000))
        )

        instr = ir.Report(filename="SALES_DATA", components=[verb, compute])

        sql = emitter.emit_instruction(instr)

        self.assertIn("SELECT SUM(SALES), (SUM(SALES) / 1000) AS \"RATIO\"", sql)

    def test_emit_instruction_define_and_lift(self):
        emitter = PostgresEmitter()

        # DEFINE FILE SALES_DATA
        #   BONUS = SALES * 0.1;
        # END
        define = ir.Define(filename="SALES_DATA", assignments=[
            asg.DefineAssignment(name="BONUS", expression=asg.BinaryOperation(asg.Identifier("SALES"), "*", asg.Literal(0.1)))
        ])
        emitter.emit_instruction(define)

        # TABLE FILE SALES_DATA
        #   SUM SALES BONUS
        # END
        verb = asg.VerbCommand(verb="SUM", fields=[
            asg.FieldSelection(name="SALES"),
            asg.FieldSelection(name="BONUS")
        ])
        report = ir.Report(filename="SALES_DATA", components=[verb])

        sql = emitter.emit_instruction(report)

        self.assertIn("SELECT SUM(SALES), SUM((SALES * 0.1)) AS \"BONUS\"", sql)

    def test_emit_instruction_define_recursive_lifting(self):
        emitter = PostgresEmitter()

        # DEFINE FILE SALES_DATA
        #   BONUS = SALES * 0.1;
        #   TOTAL_COMP = SALARY + BONUS;
        # END
        define = ir.Define(filename="SALES_DATA", assignments=[
            asg.DefineAssignment(name="BONUS", expression=asg.BinaryOperation(asg.Identifier("SALES"), "*", asg.Literal(0.1))),
            asg.DefineAssignment(name="TOTAL_COMP", expression=asg.BinaryOperation(asg.Identifier("SALARY"), "+", asg.Identifier("BONUS")))
        ])
        emitter.emit_instruction(define)

        # TABLE FILE SALES_DATA
        #   PRINT TOTAL_COMP
        # END
        verb = asg.VerbCommand(verb="PRINT", fields=[asg.FieldSelection(name="TOTAL_COMP")])
        report = ir.Report(filename="SALES_DATA", components=[verb])

        sql = emitter.emit_instruction(report)

        self.assertIn("SELECT (SALARY + (SALES * 0.1)) AS \"TOTAL_COMP\"", sql)

    def test_emit_instruction_join_context(self):
        emitter = PostgresEmitter()

        join1 = ir.Join(left_file="F1", left_field="FL1", right_file="F2", right_field="FL2", join_as="J1", outer=False)
        emitter.emit_instruction(join1)
        self.assertEqual(len(emitter.active_joins), 1)
        self.assertEqual(emitter.active_joins[0].join_as, "J1")

        join2 = ir.Join(left_file="F1", left_field="FL1", right_file="F3", right_field="FL3", join_as="J2", outer=True)
        emitter.emit_instruction(join2)
        self.assertEqual(len(emitter.active_joins), 2)

        emitter.emit_instruction(ir.JoinClear())
        self.assertEqual(len(emitter.active_joins), 0)

    def test_emit_instruction_report_with_join(self):
        emitter = PostgresEmitter()

        # JOIN LEFT_FILE.FLD1 TO RIGHT_FILE.FLD2 AS J1
        join = ir.Join(left_file="LEFT_FILE", left_field="FLD1", right_file="RIGHT_FILE", right_field="FLD2", join_as="J1")

        # TABLE FILE LEFT_FILE
        #   PRINT FLD1 RIGHT_FILE.FLD2
        # END
        verb = asg.VerbCommand(verb="PRINT", fields=[
            asg.FieldSelection(name="FLD1"),
            asg.FieldSelection(name="RIGHT_FILE.FLD2")
        ])

        report = ir.Report(filename="LEFT_FILE", components=[verb], joins=[join])

        sql = emitter.emit_instruction(report)

        self.assertIn("SELECT LEFT_FILE.FLD1, J1.FLD2", sql)
        self.assertIn("FROM LEFT_FILE", sql)
        self.assertIn("JOIN RIGHT_FILE J1 ON LEFT_FILE.FLD1 = J1.FLD2", sql)

    def test_emit_instruction_report_with_outer_join(self):
        emitter = PostgresEmitter()

        # JOIN LEFT OUTER LEFT_FILE.FLD1 TO RIGHT_FILE.FLD2
        join = ir.Join(left_file="LEFT_FILE", left_field="FLD1", right_file="RIGHT_FILE", right_field="FLD2", outer=True)

        verb = asg.VerbCommand(verb="PRINT", fields=[asg.FieldSelection(name="FLD1")])
        report = ir.Report(filename="LEFT_FILE", components=[verb], joins=[join])

        sql = emitter.emit_instruction(report)

        self.assertIn("LEFT OUTER JOIN RIGHT_FILE ON LEFT_FILE.FLD1 = RIGHT_FILE.FLD2", sql)

    def test_emit_instruction_report_with_chained_joins(self):
        emitter = PostgresEmitter()

        # JOIN F1.A TO F2.B
        # JOIN F2.C TO F3.D
        j1 = ir.Join(left_file="F1", left_field="A", right_file="F2", right_field="B")
        j2 = ir.Join(left_file="F2", left_field="C", right_file="F3", right_field="D")

        verb = asg.VerbCommand(verb="PRINT", fields=[asg.FieldSelection(name="A")])
        report = ir.Report(filename="F1", components=[verb], joins=[j1, j2])

        sql = emitter.emit_instruction(report)

        self.assertIn("JOIN F2 ON F1.A = F2.B", sql)
        self.assertIn("JOIN F3 ON F2.C = F3.D", sql)

    def test_emit_instruction_report_with_join_and_virtual_lifting(self):
        emitter = PostgresEmitter()

        # DEFINE FILE RIGHT_FILE
        #   CALC = FLD2 * 2;
        # END
        define = ir.Define(filename="RIGHT_FILE", assignments=[
            asg.DefineAssignment(name="CALC", expression=asg.BinaryOperation(asg.Identifier("FLD2"), "*", asg.Literal(2)))
        ])
        emitter.emit_instruction(define)

        # JOIN LEFT_FILE.FLD1 TO RIGHT_FILE.FLD2
        join = ir.Join(left_file="LEFT_FILE", left_field="FLD1", right_file="RIGHT_FILE", right_field="FLD2")

        # TABLE FILE LEFT_FILE
        #   PRINT CALC
        # END
        verb = asg.VerbCommand(verb="PRINT", fields=[asg.FieldSelection(name="CALC")])
        report = ir.Report(filename="LEFT_FILE", components=[verb], joins=[join])

        sql = emitter.emit_instruction(report)

        # Should lift CALC from RIGHT_FILE and qualify FLD2
        self.assertIn("(RIGHT_FILE.FLD2 * 2) AS \"CALC\"", sql)
        self.assertIn("JOIN RIGHT_FILE ON LEFT_FILE.FLD1 = RIGHT_FILE.FLD2", sql)

if __name__ == '__main__':
    unittest.main()

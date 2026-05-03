import unittest
from antlr4 import InputStream, CommonTokenStream
from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
from ir_builder import IRBuilder
from ssa_transformer import SSATransformer
from emitter import PostgresEmitter
import asg

class TestDecode(unittest.TestCase):
    def test_decode_parsing(self):
        code = "DEFINE FILE EMPDATA GENDER = DECODE FIRST_NAME('ALFRED' 'M' 'RICHARD' 'M' ELSE 'F'); END"
        input_stream = InputStream(code)
        lexer = WebFocusReportLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(stream)
        tree = parser.start()

        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)

        define_file = asg_nodes[0]
        self.assertIsInstance(define_file, asg.DefineFile)
        assignment = define_file.assignments[0]
        self.assertIsInstance(assignment.expression, asg.DecodeExpression)

        decode = assignment.expression
        self.assertEqual(decode.expression.name, 'FIRST_NAME')
        self.assertEqual(len(decode.pairs), 2)
        self.assertEqual(decode.pairs[0][0].value, 'ALFRED')
        self.assertEqual(decode.pairs[0][1].value, 'M')
        self.assertEqual(decode.default_value.value, 'F')

    def test_decode_emission(self):
        code = "DEFINE FILE EMPDATA GENDER = DECODE FIRST_NAME('ALFRED' 'M' ELSE 'F'); END"
        input_stream = InputStream(code)
        lexer = WebFocusReportLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(stream)
        tree = parser.start()

        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)

        ir_builder = IRBuilder()
        cfg = ir_builder.build(asg_nodes)

        emitter = PostgresEmitter()
        # We can test emit_expression directly
        define_instr = cfg.blocks['ENTRY'].instructions[0]
        decode_expr = define_instr.assignments[0].expression

        sql = emitter.emit_expression(decode_expr)
        # Note: PostgresEmitter._sanitize_name prepends 'v_' for identifiers in procedural code
        self.assertEqual(sql, "(CASE v_FIRST_NAME WHEN 'ALFRED' THEN 'M' ELSE 'F' END)")

    def test_decode_in_report(self):
        code = """
        TABLE FILE EMPDATA
        SUM SALARY
        COMPUTE DEPT_NAME = DECODE DEPARTMENT ('MIS' 'Mgmt' 'PROD' 'Prod' ELSE 'Other');
        END
        """
        input_stream = InputStream(code)
        lexer = WebFocusReportLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(stream)
        tree = parser.start()

        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)

        ir_builder = IRBuilder()
        cfg = ir_builder.build(asg_nodes)

        emitter = PostgresEmitter()
        sql = emitter.emit(cfg)

        # In reports, fields are often qualified or aggregated.
        # Here DEPARTMENT is not in BY, so it's wrapped in SUM() because the report is aggregating (SUM SALARY).
        self.assertIn("(CASE SUM(DEPARTMENT) WHEN 'MIS' THEN 'Mgmt' WHEN 'PROD' THEN 'Prod' ELSE 'Other' END)", sql)

if __name__ == '__main__':
    unittest.main()

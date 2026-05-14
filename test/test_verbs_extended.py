import unittest
import sys
import os
from antlr4 import CommonTokenStream, InputStream

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
from ir_builder import IRBuilder
from ssa_transformer import SSATransformer
from emitter import PostgresEmitter

class TestVerbsExtended(unittest.TestCase):
    def test_count_star(self):
        fex_code = """
        TABLE FILE EMPLOYEE
        COUNT *
        END
        """
        input_stream = InputStream(fex_code)
        lexer = WebFocusReportLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(token_stream)
        tree = parser.start()

        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)

        ir_builder = IRBuilder()
        cfg = ir_builder.build(asg_nodes)

        emitter = PostgresEmitter()
        sql_output = emitter.emit(cfg)

        self.assertIn('COUNT(*) AS "COUNT"', sql_output)

    def test_list_verb(self):
        fex_code = """
        TABLE FILE EMPLOYEE
        LIST LAST_NAME FIRST_NAME
        END
        """
        input_stream = InputStream(fex_code)
        lexer = WebFocusReportLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(token_stream)
        tree = parser.start()

        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)

        ir_builder = IRBuilder()
        cfg = ir_builder.build(asg_nodes)

        emitter = PostgresEmitter()
        sql_output = emitter.emit(cfg)

        self.assertIn('ROW_NUMBER() OVER () AS "LIST"', sql_output)
        self.assertIn('LAST_NAME', sql_output)
        self.assertIn('FIRST_NAME', sql_output)

if __name__ == '__main__':
    unittest.main()

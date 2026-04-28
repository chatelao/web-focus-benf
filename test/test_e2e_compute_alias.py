import unittest
from antlr4 import CommonTokenStream, InputStream
from src.WebFocusReportLexer import WebFocusReportLexer
from src.WebFocusReportParser import WebFocusReportParser
from src.asg_builder import ReportASGBuilder
from src.ir_builder import IRBuilder
from src.emitter import PostgresEmitter

class TestE2EComputeAlias(unittest.TestCase):
    def test_compute_with_alias_and_and(self):
        fex_code = """
        TABLE FILE CAR
        SUM SALES
        BY COUNTRY
        AND COMPUTE RATIO/D8.2 = SALES / 1000 AS 'Sales Ratio';
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

        # Verification
        self.assertIn("(SUM(SALES) / 1000) AS \"Sales Ratio\"", sql_output)
        self.assertIn("SUM(SALES)", sql_output)
        self.assertIn("GROUP BY COUNTRY", sql_output)

if __name__ == '__main__':
    unittest.main()

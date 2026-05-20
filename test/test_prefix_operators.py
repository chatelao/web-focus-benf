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

class TestPrefixOperators(unittest.TestCase):
    def _compile_to_sql(self, fex_code):
        input_stream = InputStream(fex_code)
        lexer = WebFocusReportLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(token_stream)
        tree = parser.start()

        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)

        ir_builder = IRBuilder()
        cfg = ir_builder.build(asg_nodes)

        ssa_transformer = SSATransformer()
        ssa_transformer.transform(cfg)

        emitter = PostgresEmitter()
        return emitter.emit(cfg)

    def test_basic_prefixes(self):
        fex = """
        TABLE FILE CAR
        SUM AVE.PRICE MIN.PRICE MAX.PRICE CNT.PRICE TOT.PRICE CT.PRICE
        BY COUNTRY
        END
        """
        sql = self._compile_to_sql(fex)
        self.assertIn("AVG(\"CAR\".\"PRICE\")", sql)
        self.assertIn("MIN(\"CAR\".\"PRICE\")", sql)
        self.assertIn("MAX(\"CAR\".\"PRICE\")", sql)
        self.assertIn("COUNT(\"CAR\".\"PRICE\")", sql)
        self.assertIn("SUM(\"CAR\".\"PRICE\")", sql) # TOT.PRICE

    def test_distinct_prefixes(self):
        fex = """
        TABLE FILE CAR
        SUM DST.COUNTRY CNT.DST.COUNTRY SUM.DST.PRICE AVE.DST.PRICE
        BY COUNTRY
        END
        """
        sql = self._compile_to_sql(fex)
        self.assertIn("COUNT(DISTINCT \"CAR\".\"COUNTRY\")", sql)
        self.assertIn("SUM(DISTINCT \"CAR\".\"PRICE\")", sql)
        self.assertIn("AVG(DISTINCT \"CAR\".\"PRICE\")", sql)

    def test_statistical_prefixes(self):
        fex = """
        TABLE FILE CAR
        SUM ASQ.PRICE MDN.PRICE MDE.PRICE
        BY COUNTRY
        END
        """
        sql = self._compile_to_sql(fex)
        self.assertIn("AVG((\"CAR\".\"PRICE\") * (\"CAR\".\"PRICE\"))", sql)
        self.assertIn("PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY \"CAR\".\"PRICE\")", sql)
        self.assertIn("MODE() WITHIN GROUP (ORDER BY \"CAR\".\"PRICE\")", sql)

    def test_print_with_prefixes(self):
        fex = """
        TABLE FILE CAR
        PRINT SUM.PRICE AVE.PRICE
        BY COUNTRY
        END
        """
        sql = self._compile_to_sql(fex)
        self.assertIn("SUM(\"CAR\".\"PRICE\")", sql)
        self.assertIn("AVG(\"CAR\".\"PRICE\")", sql)
        self.assertIn("GROUP BY \"CAR\".\"COUNTRY\"", sql)

    def test_more_with_prefixes(self):
        fex = """
        TABLE FILE CAR
        SUM AVE.PRICE
        BY COUNTRY
        MORE
        FILE CAR_EXTRA
        END
        """
        sql = self._compile_to_sql(fex)
        self.assertIn("AVG(SRC.\"PRICE\")", sql)
        self.assertIn("GROUP BY SRC.\"COUNTRY\"", sql)

    def test_advanced_window_prefixes(self):
        fex = """
        TABLE FILE CAR
        SUM FST.MODEL LST.MODEL RNK.PRICE PCT.PRICE
        BY COUNTRY
        END
        """
        sql = self._compile_to_sql(fex)
        # FST/LST via ARRAY_AGG
        self.assertIn("(ARRAY_AGG(\"CAR\".\"MODEL\" ORDER BY \"CAR\".\"COUNTRY\"))[1]", sql)
        self.assertIn("(ARRAY_AGG(\"CAR\".\"MODEL\" ORDER BY \"CAR\".\"COUNTRY\"))[ARRAY_UPPER(ARRAY_AGG(\"CAR\".\"MODEL\" ORDER BY \"CAR\".\"COUNTRY\"), 1)]", sql)
        # RNK
        self.assertIn("RANK() OVER (PARTITION BY \"CAR\".\"COUNTRY\" ORDER BY SUM(\"CAR\".\"PRICE\") DESC)", sql)
        # PCT
        self.assertIn("(SUM(\"CAR\".\"PRICE\") * 100.0 / SUM(SUM(\"CAR\".\"PRICE\")) OVER ())", sql)

    def test_print_advanced_prefixes(self):
        fex = """
        TABLE FILE CAR
        PRINT FST.MODEL RNK.PRICE
        BY COUNTRY
        END
        """
        sql = self._compile_to_sql(fex)
        self.assertIn("(ARRAY_AGG(\"CAR\".\"MODEL\" ORDER BY \"CAR\".\"COUNTRY\"))[1]", sql)
        self.assertIn("RANK() OVER (PARTITION BY \"CAR\".\"COUNTRY\" ORDER BY \"CAR\".\"PRICE\" DESC)", sql)

if __name__ == '__main__':
    unittest.main()

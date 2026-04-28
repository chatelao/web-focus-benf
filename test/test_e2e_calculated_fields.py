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
from optimizer import ConstantPropagator, DeadCodeEliminator
from emitter import PostgresEmitter
from metadata_registry import MetadataRegistry

class TestE2ECalculatedFields(unittest.TestCase):
    def _run_e2e(self, fex_code):
        # 2. Parse
        input_stream = InputStream(fex_code)
        lexer = WebFocusReportLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(token_stream)
        tree = parser.start()

        # 3. ASG Construction
        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)

        # 4. IR/CFG Construction
        ir_builder = IRBuilder()
        cfg = ir_builder.build(asg_nodes)

        # 5. SSA Transformation
        ssa_transformer = SSATransformer()
        ssa_transformer.transform(cfg)

        # 6. Optimization
        ConstantPropagator().run(cfg)
        DeadCodeEliminator().run(cfg)

        # 7. Backend Emission
        metadata = MetadataRegistry()
        emitter = PostgresEmitter(metadata_registry=metadata)
        sql_output = emitter.emit(cfg)

        return sql_output

    def test_define_in_print(self):
        fex_code = """
        DEFINE FILE CAR
        PRICE_EUR = PRICE * 0.85;
        END
        TABLE FILE CAR
        PRINT CAR MODEL PRICE PRICE_EUR
        END
        """
        sql = self._run_e2e(fex_code)
        self.assertIn("(PRICE * 0.85) AS \"PRICE_EUR\"", sql)
        self.assertIn("SELECT CAR, MODEL, PRICE, (PRICE * 0.85) AS \"PRICE_EUR\"", sql)

    def test_define_in_sum(self):
        fex_code = """
        DEFINE FILE CAR
        REVENUE = SALES * PRICE;
        END
        TABLE FILE CAR
        SUM REVENUE BY COUNTRY
        END
        """
        sql = self._run_e2e(fex_code)
        # REVENUE is (SALES * PRICE). SUM(REVENUE) -> SUM(SALES * PRICE)
        self.assertIn("SUM((SALES * PRICE)) AS \"REVENUE\"", sql)
        self.assertIn("GROUP BY COUNTRY", sql)

    def test_compute_in_print(self):
        fex_code = """
        TABLE FILE CAR
        PRINT CAR MODEL PRICE
        COMPUTE PRICE_EUR/D12.2 = PRICE * 0.85;
        END
        """
        sql = self._run_e2e(fex_code)
        # In PRINT, COMPUTE should behave like a regular expression
        self.assertIn("(PRICE * 0.85) AS \"PRICE_EUR\"", sql)

    def test_compute_in_sum(self):
        fex_code = """
        TABLE FILE CAR
        SUM SALES
        COMPUTE AVG_PRICE = SALES / 10;
        BY COUNTRY
        END
        """
        sql = self._run_e2e(fex_code)
        # In SUM, fields in COMPUTE should be aggregated.
        # WebFOCUS: SUM SALES COMPUTE AVG_PRICE = SALES / 10;
        # means AVG_PRICE = SUM(SALES) / 10
        self.assertIn("(SUM(SALES) / 10) AS \"AVG_PRICE\"", sql)

    def test_recursive_define_and_compute(self):
        fex_code = """
        DEFINE FILE CAR
        BASE_TAX = PRICE * 0.1;
        TOTAL_PRICE = PRICE + BASE_TAX;
        END
        TABLE FILE CAR
        SUM TOTAL_PRICE
        COMPUTE NET_PROFIT = TOTAL_PRICE * 0.5;
        END
        """
        sql = self._run_e2e(fex_code)
        # TOTAL_PRICE = PRICE + (PRICE * 0.1)
        # SUM(TOTAL_PRICE) = SUM(PRICE + (PRICE * 0.1))
        # COMPUTE NET_PROFIT = SUM(TOTAL_PRICE) * 0.5 = SUM(PRICE + (PRICE * 0.1)) * 0.5
        self.assertIn("SUM((PRICE + (PRICE * 0.1))) AS \"TOTAL_PRICE\"", sql)
        self.assertIn("(SUM((PRICE + (PRICE * 0.1))) * 0.5) AS \"NET_PROFIT\"", sql)

if __name__ == '__main__':
    unittest.main()

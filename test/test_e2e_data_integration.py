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

class TestE2EDataIntegration(unittest.TestCase):
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

    def test_simple_join(self):
        fex_code = """
        JOIN COUNTRY IN CAR TO COUNTRY IN COUNTRY AS J1
        TABLE FILE CAR
        PRINT CAR MODEL COUNTRY.COUNTRY
        END
        """
        sql = self._run_e2e(fex_code)
        self.assertIn("JOIN COUNTRY J1 ON CAR.COUNTRY = J1.COUNTRY", sql)
        self.assertIn("SELECT CAR.CAR, CAR.MODEL, J1.COUNTRY", sql)

    def test_left_outer_join(self):
        fex_code = """
        JOIN LEFT OUTER COUNTRY IN CAR TO COUNTRY IN COUNTRY AS J1
        TABLE FILE CAR
        PRINT CAR MODEL COUNTRY.COUNTRY
        END
        """
        sql = self._run_e2e(fex_code)
        self.assertIn("LEFT OUTER JOIN COUNTRY J1 ON CAR.COUNTRY = J1.COUNTRY", sql)

    def test_virtual_field_lifting_from_joined_table(self):
        fex_code = """
        DEFINE FILE COUNTRY
        IS_EUROPE = IF COUNTRY EQ 'ENGLAND' OR 'FRANCE' OR 'ITALY' OR 'W GERMANY' THEN 'YES' ELSE 'NO';
        END
        JOIN COUNTRY IN CAR TO COUNTRY IN COUNTRY AS J1
        TABLE FILE CAR
        PRINT CAR MODEL IS_EUROPE
        END
        """
        sql = self._run_e2e(fex_code)
        # IS_EUROPE expression should be lifted from COUNTRY file context.
        # Inside the expression, 'COUNTRY' should be qualified as 'J1.COUNTRY'.
        self.assertIn("(CASE WHEN ((((J1.COUNTRY = 'ENGLAND') OR (J1.COUNTRY = 'FRANCE')) OR (J1.COUNTRY = 'ITALY')) OR (J1.COUNTRY = 'W GERMANY')) THEN 'YES' ELSE 'NO' END) AS \"IS_EUROPE\"", sql)
        self.assertIn("JOIN COUNTRY J1 ON CAR.COUNTRY = J1.COUNTRY", sql)

    def test_chained_joins(self):
        fex_code = """
        JOIN COUNTRY IN CAR TO COUNTRY IN COUNTRY AS J1
        JOIN COUNTRY IN COUNTRY TO COUNTRY IN REGION AS J2
        TABLE FILE CAR
        PRINT CAR REGION.REGION
        END
        """
        sql = self._run_e2e(fex_code)
        self.assertIn("JOIN COUNTRY J1 ON CAR.COUNTRY = J1.COUNTRY", sql)
        self.assertIn("JOIN REGION J2 ON J1.COUNTRY = J2.COUNTRY", sql)
        self.assertIn("SELECT CAR.CAR, J2.REGION", sql)

if __name__ == '__main__':
    unittest.main()

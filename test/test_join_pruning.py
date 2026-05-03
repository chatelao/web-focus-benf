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
from metadata_registry import MetadataRegistry

class TestJoinPruning(unittest.TestCase):
    def _run_e2e(self, fex_code):
        # Parse
        input_stream = InputStream(fex_code)
        lexer = WebFocusReportLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(token_stream)
        tree = parser.start()

        # ASG Construction
        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)

        # IR/CFG Construction
        ir_builder = IRBuilder()
        cfg = ir_builder.build(asg_nodes)

        # SSA Transformation
        ssa_transformer = SSATransformer()
        ssa_transformer.transform(cfg)

        # Backend Emission
        metadata = MetadataRegistry()
        emitter = PostgresEmitter(metadata_registry=metadata)
        sql_output = emitter.emit(cfg)

        return sql_output

    def test_unused_join_is_pruned(self):
        fex_code = """
        JOIN COUNTRY IN CAR TO COUNTRY IN COUNTRY AS J1
        TABLE FILE CAR
        PRINT CAR MODEL
        END
        """
        sql = self._run_e2e(fex_code)
        # Should NOT contain the join to COUNTRY
        self.assertNotIn("JOIN COUNTRY J1", sql)
        self.assertIn("SELECT CAR.CAR, CAR.MODEL", sql)

    def test_used_join_is_kept(self):
        fex_code = """
        JOIN COUNTRY IN CAR TO COUNTRY IN COUNTRY AS J1
        TABLE FILE CAR
        PRINT CAR MODEL J1.COUNTRY
        END
        """
        sql = self._run_e2e(fex_code)
        # Should contain the join to COUNTRY
        self.assertIn("JOIN COUNTRY J1 ON CAR.COUNTRY = J1.COUNTRY", sql)
        self.assertIn("SELECT CAR.CAR, CAR.MODEL, J1.COUNTRY", sql)

    def test_join_pruning_with_where_clause(self):
        fex_code = """
        JOIN COUNTRY IN CAR TO COUNTRY IN COUNTRY AS J1
        TABLE FILE CAR
        PRINT CAR MODEL
        WHERE J1.COUNTRY EQ 'ENGLAND'
        END
        """
        sql = self._run_e2e(fex_code)
        # Should keep the join because it's used in WHERE
        self.assertIn("JOIN COUNTRY J1 ON CAR.COUNTRY = J1.COUNTRY", sql)
        self.assertIn("WHERE (J1.COUNTRY = 'ENGLAND')", sql)

    def test_join_pruning_with_virtual_field(self):
        # First test where virtual field from joined file IS used
        fex_code = """
        DEFINE FILE COUNTRY
        IS_EUROPE = IF COUNTRY EQ 'ENGLAND' OR 'FRANCE' THEN 'YES' ELSE 'NO';
        END
        JOIN COUNTRY IN CAR TO COUNTRY IN COUNTRY AS J1
        TABLE FILE CAR
        PRINT CAR MODEL IS_EUROPE
        END
        """
        sql = self._run_e2e(fex_code)
        self.assertIn("JOIN COUNTRY J1", sql)
        self.assertIn("IS_EUROPE", sql)

        # Now test where it is NOT used
        fex_code_unused = """
        DEFINE FILE COUNTRY
        IS_EUROPE = IF COUNTRY EQ 'ENGLAND' OR 'FRANCE' THEN 'YES' ELSE 'NO';
        END
        JOIN COUNTRY IN CAR TO COUNTRY IN COUNTRY AS J1
        TABLE FILE CAR
        PRINT CAR MODEL
        END
        """
        sql_unused = self._run_e2e(fex_code_unused)
        self.assertNotIn("JOIN COUNTRY J1", sql_unused)
        self.assertNotIn("IS_EUROPE", sql_unused)

    def test_chained_join_pruning(self):
        # Chain: CAR -> COUNTRY (J1) -> REGION (J2)
        # Use only fields from CAR and COUNTRY. REGION should be pruned.
        fex_code = """
        JOIN COUNTRY IN CAR TO COUNTRY IN COUNTRY AS J1
        JOIN COUNTRY IN COUNTRY TO COUNTRY IN REGION AS J2
        TABLE FILE CAR
        PRINT CAR J1.COUNTRY
        END
        """
        sql = self._run_e2e(fex_code)
        self.assertIn("JOIN COUNTRY J1", sql)
        self.assertNotIn("JOIN REGION J2", sql)

        # Now use only CAR. Both should be pruned.
        fex_code_all_unused = """
        JOIN COUNTRY IN CAR TO COUNTRY IN COUNTRY AS J1
        JOIN COUNTRY IN COUNTRY TO COUNTRY IN REGION AS J2
        TABLE FILE CAR
        PRINT CAR MODEL
        END
        """
        sql_all_unused = self._run_e2e(fex_code_all_unused)
        self.assertNotIn("JOIN COUNTRY J1", sql_all_unused)
        self.assertNotIn("JOIN REGION J2", sql_all_unused)

    def test_chained_join_keeping(self):
        # Chain: CAR -> COUNTRY (J1) -> REGION (J2)
        # Use field from REGION. Both joins must be kept.
        fex_code = """
        JOIN COUNTRY IN CAR TO COUNTRY IN COUNTRY AS J1
        JOIN COUNTRY IN COUNTRY TO COUNTRY IN REGION AS J2
        TABLE FILE CAR
        PRINT CAR J2.REGION
        END
        """
        sql = self._run_e2e(fex_code)
        self.assertIn("JOIN COUNTRY J1", sql)
        self.assertIn("JOIN REGION J2", sql)

if __name__ == '__main__':
    unittest.main()

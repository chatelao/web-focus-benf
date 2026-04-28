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

class TestCompoundLayout(unittest.TestCase):
    def test_compound_layout_compilation(self):
        fex_code = """
        SET PAGE-NUM=OFF
        COMPOUND LAYOUT PCHOLD FORMAT PDF
        SECTION=S1, LAYOUT=ON, MERGE=ON, ORIENTATION=LANDSCAPE, $
        PAGELAYOUT=1, $
        COMPONENT=Sales, TYPE=REPORT, POSITION=(1 1), DIMENSION=(4 4), $
        COMPONENT=Units, TYPE=REPORT, POSITION=(6.25 1), DIMENSION=(4 4), $
        END
        SET COMPONENT=Sales
        TABLE FILE GGSALES
        SUM DOLLARS
        BY REGION
        ON TABLE HOLD FORMAT PDF
        END
        SET COMPONENT=Units
        TABLE FILE GGSALES
        SUM UNITS
        BY PRODUCT
        ON TABLE HOLD FORMAT PDF
        END
        COMPOUND END
        """

        # 1. Parse
        input_stream = InputStream(fex_code)
        lexer = WebFocusReportLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(token_stream)
        tree = parser.start()

        # 2. ASG Construction
        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)

        # Verify ASG has CompoundLayout
        self.assertTrue(any(node.__class__.__name__ == 'CompoundLayout' for node in asg_nodes))

        # 3. IR/CFG Construction
        ir_builder = IRBuilder()
        cfg = ir_builder.build(asg_nodes)

        # 4. SSA Transformation
        ssa_transformer = SSATransformer()
        ssa_transformer.transform(cfg)

        # 5. Backend Emission
        emitter = PostgresEmitter()
        sql_output = emitter.emit(cfg)

        # 6. Verifications
        self.assertIn("COMPOUND LAYOUT", sql_output)
        self.assertIn("GGSALES", sql_output)
        self.assertIn("SUM(DOLLARS)", sql_output)
        self.assertIn("SUM(UNITS)", sql_output)

if __name__ == '__main__':
    unittest.main()

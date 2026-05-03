import unittest
import sys
import os

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from wf_parser import WebFocusParser
from asg_builder import ReportASGBuilder
from ir_builder import IRBuilder
from emitter import PostgresEmitter
from metadata_registry import MetadataRegistry

class TestE2EMerge(unittest.TestCase):
    def setUp(self):
        self.parser = WebFocusParser()
        self.asg_builder = ReportASGBuilder()
        self.ir_builder = IRBuilder()
        self.registry = MetadataRegistry()
        self.emitter = PostgresEmitter(metadata_registry=self.registry)

    def test_basic_merge(self):
        fex = """
        TABLE FILE dminv
        PRINT
           PROD_NUM
         COMPUTE QUANTITY =  SUM.QTY_IN_STOCK;

        ON TABLE MERGE INTO FILE dmrpts
        MATCHING TRG.PROD_NUM EQ SRC.PROD_NUM;

        WHEN MATCHED UPDATE
          QUANTITY=SRC.QUANTITY;

        WHEN NOT MATCHED INSERT
          PROD_NUM=SRC.PROD_NUM;
          QUANTITY=SRC.QUANTITY;
        END
        """

        # 1. Parse
        tree = self.parser.parse(fex)

        # 2. Build ASG
        asg_nodes = self.asg_builder.visit(tree)

        # 3. Build IR
        cfg = self.ir_builder.build(asg_nodes)

        # 4. Emit
        sql = self.emitter.emit(cfg)

        print(sql)

        # 5. Assertions
        self.assertIn("MERGE INTO DMRPTS", sql.upper())
        self.assertIn("USING (", sql.upper())
        self.assertIn("ON (TRG.PROD_NUM = SRC.PROD_NUM)", sql.upper())
        self.assertIn("WHEN MATCHED THEN", sql.upper())
        self.assertIn("UPDATE SET", sql.upper())
        self.assertIn("WHEN NOT MATCHED THEN", sql.upper())
        self.assertIn('INSERT ("PROD_NUM", "QUANTITY")', sql.upper())

if __name__ == "__main__":
    unittest.main()

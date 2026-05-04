import unittest
from antlr4 import InputStream, CommonTokenStream
from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
from ir_builder import IRBuilder
from emitter import PostgresEmitter
from metadata_registry import MetadataRegistry
from asg import MasterFile, Segment, Field

class TestE2EMorePhrase(unittest.TestCase):
    def test_more_phrase_union_all(self):
        fex = """
        TABLE FILE EMP1
        SUM SALARY BY EMP_ID
        WHERE DEPT EQ 'A'
        MORE
        FILE EMP2
        WHERE DEPT EQ 'B'
        END
        """

        # Setup metadata
        registry = MetadataRegistry()
        emp1 = MasterFile(name="EMP1")
        seg1 = Segment(name="S1")
        seg1.fields = [Field(name="SALARY", format="I8"), Field(name="EMP_ID", format="A10"), Field(name="DEPT", format="A10")]
        emp1.segments = [seg1]
        registry.register_master_file(emp1)

        emp2 = MasterFile(name="EMP2")
        seg2 = Segment(name="S2")
        seg2.fields = [Field(name="SALARY", format="I8"), Field(name="EMP_ID", format="A10"), Field(name="DEPT", format="A10")]
        emp2.segments = [seg2]
        registry.register_master_file(emp2)

        # Parse
        input_stream = InputStream(fex)
        lexer = WebFocusReportLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(token_stream)
        tree = parser.start()

        asg_builder = ReportASGBuilder()
        asg_nodes = asg_builder.visit(tree)

        # Build IR
        ir_builder = IRBuilder()
        cfg = ir_builder.build(asg_nodes)

        # Emit
        emitter = PostgresEmitter(metadata_registry=registry)
        sql = emitter.emit(cfg)

        print(sql)

        # Verify
        self.assertIn("UNION ALL", sql)
        # Wrapping subquery
        self.assertIn('SELECT SRC."EMP_ID", SUM(SRC."SALARY") FROM (', sql)
        # Main source query
        self.assertIn('SELECT EMP_ID AS "EMP_ID", SALARY AS "SALARY" FROM EMP1', sql)
        self.assertIn("WHERE (DEPT = 'A')", sql)
        # Sub source query
        self.assertIn('SELECT EMP2.EMP_ID AS "EMP_ID", EMP2.SALARY AS "SALARY" FROM EMP2', sql)
        self.assertIn("WHERE (EMP2.DEPT = 'B')", sql)
        # Final aggregation
        self.assertIn('GROUP BY SRC."EMP_ID"', sql)
        self.assertIn('ORDER BY SRC."EMP_ID" ASC', sql)

if __name__ == "__main__":
    unittest.main()

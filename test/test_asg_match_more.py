import unittest
from antlr4 import InputStream, CommonTokenStream
from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
from asg import *

class TestAsgMatchMore(unittest.TestCase):
    def get_asg(self, text):
        input_stream = InputStream(text)
        lexer = WebFocusReportLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(token_stream)
        tree = parser.start()
        builder = ReportASGBuilder()
        return builder.visit(tree)

    def test_match_file_asg(self):
        text = """
        MATCH FILE EDUCFILE
        SUM COURSE_CODE
        BY EMP_ID
        RUN
        FILE EMPLOYEE
        SUM LAST_NAME AND FIRST_NAME
        BY EMP_ID BY CURR_SAL
        AFTER MATCH HOLD AS MYRESULT OLD-OR-NEW
        END
        """
        asg = self.get_asg(text)
        self.assertEqual(len(asg), 1)
        match_req = asg[0]
        self.assertIsInstance(match_req, MatchRequest)
        self.assertEqual(match_req.filename, "EDUCFILE")
        self.assertEqual(len(match_req.components), 2) # SUM and BY
        self.assertEqual(len(match_req.sub_matches), 1)

        sub = match_req.sub_matches[0]
        self.assertIsInstance(sub, SubMatch)
        self.assertEqual(sub.filename, "EMPLOYEE")
        self.assertEqual(len(sub.components), 3) # SUM, BY, BY
        self.assertIsInstance(sub.after_match, AfterMatchPhrase)
        self.assertEqual(sub.after_match.merge_type, "OLD-OR-NEW")
        self.assertIsInstance(sub.after_match.output_command, OutputCommand)
        self.assertEqual(sub.after_match.output_command.filename, "MYRESULT")

    def test_table_more_phrase_asg(self):
        text = """
        TABLE FILE EMPLOYEE
        PRINT CURR_SAL
        BY EMP_ID
        MORE
        FILE EXPERSON
        WHERE SALARY GT 50000;
        FILE OTHERS
        END
        """
        asg = self.get_asg(text)
        self.assertEqual(len(asg), 1)
        req = asg[0]
        self.assertIsInstance(req, ReportRequest)
        self.assertIsInstance(req.more_clause, MoreClause)
        self.assertEqual(len(req.more_clause.sub_requests), 2)

        sub1 = req.more_clause.sub_requests[0]
        self.assertEqual(sub1.filename, "EXPERSON")
        self.assertEqual(len(sub1.where_clauses), 1)

        sub2 = req.more_clause.sub_requests[1]
        self.assertEqual(sub2.filename, "OTHERS")
        self.assertEqual(len(sub2.where_clauses), 0)

    def test_match_multi_file_asg(self):
        text = """
        MATCH FILE file1
        RUN
        FILE file2
        AFTER MATCH OLD-OR-NEW
        RUN
        FILE file3
        AFTER MATCH OLD-AND-NEW
        END
        """
        asg = self.get_asg(text)
        self.assertEqual(len(asg), 1)
        match_req = asg[0]
        self.assertEqual(len(match_req.sub_matches), 2)
        self.assertEqual(match_req.sub_matches[0].after_match.merge_type, "OLD-OR-NEW")
        self.assertEqual(match_req.sub_matches[1].after_match.merge_type, "OLD-AND-NEW")

if __name__ == "__main__":
    unittest.main()

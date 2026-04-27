import unittest
import sys
import os
from antlr4 import *

# Add src to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
import asg

class TestASGBuilder(unittest.TestCase):
    def build_asg(self, text):
        input_stream = InputStream(text)
        lexer = WebFocusReportLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = WebFocusReportParser(stream)
        tree = parser.start()
        builder = ReportASGBuilder()
        asg_nodes = builder.visit(tree)
        return asg_nodes

    def test_dm_set_literal(self):
        code = "-SET &VAR = 10;"
        asg_nodes = self.build_asg(code)
        self.assertEqual(len(asg_nodes), 1)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.SetDM))
        self.assertEqual(node.variable, "&VAR")
        self.assertTrue(isinstance(node.expression, asg.Literal))
        self.assertEqual(node.expression.value, 10)

    def test_dm_set_expression(self):
        code = "-SET &VAR = 1 + 2 * 3;"
        asg_nodes = self.build_asg(code)
        self.assertEqual(len(asg_nodes), 1)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.SetDM))
        expr = node.expression
        self.assertTrue(isinstance(expr, asg.BinaryOperation))
        self.assertEqual(expr.operator, "+")
        self.assertTrue(isinstance(expr.left, asg.Literal))
        self.assertEqual(expr.left.value, 1)
        self.assertTrue(isinstance(expr.right, asg.BinaryOperation))
        self.assertEqual(expr.right.operator, "*")

    def test_dm_type(self):
        code = "-TYPE Hello World &VAR"
        asg_nodes = self.build_asg(code)
        self.assertEqual(len(asg_nodes), 1)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.TypeDM))
        self.assertEqual(len(node.messages), 3)
        self.assertEqual(node.messages[0].name, "Hello")
        self.assertEqual(node.messages[1].name, "World")
        self.assertEqual(node.messages[2].name, "&VAR")

    def test_dm_set_string(self):
        code = "-SET &VAR = 'TEXT';"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertEqual(node.expression.value, "TEXT")

    def test_dm_logical_expression(self):
        code = "-SET &VAR = &X EQ 1 AND &Y GT 2;"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        expr = node.expression
        self.assertTrue(isinstance(expr, asg.BinaryOperation))
        self.assertEqual(expr.operator, "AND")

    def test_dm_goto(self):
        code = "-GOTO MYLABEL;"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.Goto))
        self.assertEqual(node.target, "MYLABEL")

    def test_dm_label(self):
        code = "-MYLABEL"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.Label))
        self.assertEqual(node.name, "MYLABEL")

    def test_dm_if(self):
        code = "-IF &X EQ 1 GOTO LABEL1 ELSE GOTO LABEL2;"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.IfDM))
        self.assertEqual(node.then_target, "LABEL1")
        self.assertEqual(node.else_target, "LABEL2")

    def test_dm_include(self):
        code = "-INCLUDE GGHDR.FEX"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.IncludeDM))
        self.assertEqual(node.filename, "GGHDR.FEX")

    def test_dm_run_exit(self):
        code = "-RUN\n-EXIT"
        asg_nodes = self.build_asg(code)
        self.assertEqual(len(asg_nodes), 2)
        self.assertTrue(isinstance(asg_nodes[0], asg.RunDM))
        self.assertTrue(isinstance(asg_nodes[1], asg.ExitDM))

    def test_dm_repeat_while(self):
        code = "-REPEAT LOOP1 WHILE &X LT 10;"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.Repeat))
        self.assertEqual(node.label, "LOOP1")
        self.assertEqual(node.condition_type, "WHILE")

    def test_dm_repeat_for(self):
        code = "-REPEAT LOOP2 FOR &I FROM 1 TO 10 STEP 1;"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.Repeat))
        self.assertEqual(node.loop_var, "&I")
        self.assertEqual(node.start_val.value, 1)
        self.assertEqual(node.end_val.value, 10)
        self.assertEqual(node.step_val.value, 1)

    def test_dm_if_expression(self):
        code = "-SET &VAR = IF &X EQ 1 THEN 'YES' ELSE 'NO';"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        expr = node.expression
        self.assertTrue(isinstance(expr, asg.IfExpression))
        self.assertEqual(expr.then_expr.value, "YES")
        self.assertEqual(expr.else_expr.value, "NO")

    def test_dm_concat_expression(self):
        code = "-SET &VAR = 'A' | 'B' || 'C';"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        expr = node.expression
        self.assertTrue(isinstance(expr, asg.BinaryOperation))
        self.assertEqual(expr.operator, "||")
        self.assertTrue(isinstance(expr.left, asg.BinaryOperation))
        self.assertEqual(expr.left.operator, "|")

    def test_table_request_basic(self):
        code = "TABLE FILE CAR\nPRINT MODEL\nEND"
        asg_nodes = self.build_asg(code)
        self.assertEqual(len(asg_nodes), 1)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.ReportRequest))
        self.assertEqual(node.filename, "CAR")
        self.assertEqual(len(node.components), 1)
        verb = node.components[0]
        self.assertTrue(isinstance(verb, asg.VerbCommand))
        self.assertEqual(verb.verb, "PRINT")
        self.assertEqual(len(verb.fields), 1)
        self.assertEqual(verb.fields[0].name, "MODEL")

    def test_table_request_with_as_and_prefix(self):
        code = "TABLE FILE CAR\nSUM AVE.PRICE AS 'Average Price'\nEND"
        asg_nodes = self.build_asg(code)
        verb = asg_nodes[0].components[0]
        self.assertEqual(verb.verb, "SUM")
        field = verb.fields[0]
        self.assertEqual(field.name, "PRICE")
        self.assertEqual(field.prefix_operators, ["AVE"])
        self.assertEqual(field.alias, "Average Price")

    def test_table_request_with_sort(self):
        code = "TABLE FILE CAR\nPRINT MODEL\nBY COUNTRY\nACROSS HIGHEST 3 BODYTYPE\nEND"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertEqual(len(node.components), 3)
        by_node = node.components[1]
        across_node = node.components[2]
        self.assertTrue(isinstance(by_node, asg.SortCommand))
        self.assertEqual(by_node.sort_type, "BY")
        self.assertEqual(by_node.field.name, "COUNTRY")
        self.assertTrue(isinstance(across_node, asg.SortCommand))
        self.assertEqual(across_node.sort_type, "ACROSS")
        self.assertEqual(across_node.field.name, "BODYTYPE")
        self.assertEqual(across_node.options["order"], "HIGHEST")
        self.assertEqual(across_node.options["limit"], 3)

    def test_table_request_with_asterisk(self):
        code = "TABLE FILE CAR\nPRINT *\nEND"
        asg_nodes = self.build_asg(code)
        verb = asg_nodes[0].components[0]
        self.assertEqual(verb.fields[0].name, "*")

    def test_table_request_with_where(self):
        code = "TABLE FILE CAR\nPRINT MODEL\nWHERE COUNTRY EQ 'ENGLAND';\nWHERE TOTAL SALES GT 1000\nEND"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertEqual(len(node.components), 3)
        where1 = node.components[1]
        where2 = node.components[2]
        self.assertTrue(isinstance(where1, asg.WhereClause))
        self.assertFalse(where1.is_total)
        self.assertTrue(isinstance(where2, asg.WhereClause))
        self.assertTrue(where2.is_total)

    def test_table_request_with_heading_footing(self):
        code = "TABLE FILE CAR\nHEADING CENTER 'My Report'\nFOOTING 'Page 1'\nPRINT MODEL\nEND"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        heading = node.components[0]
        footing = node.components[1]
        self.assertTrue(isinstance(heading, asg.Heading))
        self.assertEqual(heading.text, "My Report")
        self.assertTrue(heading.centered)
        self.assertTrue(isinstance(footing, asg.Footing))
        self.assertEqual(footing.text, "Page 1")
        self.assertFalse(footing.centered)

    def test_table_request_with_compute(self):
        code = "TABLE FILE CAR\nSUM SALES\nCOMPUTE RATIO/D12.2 = SALES / 1000;\nEND"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        compute = node.components[1]
        self.assertTrue(isinstance(compute, asg.ComputeCommand))
        self.assertEqual(compute.name, "RATIO")
        self.assertEqual(compute.format, "D12.2")
        self.assertTrue(isinstance(compute.expression, asg.BinaryOperation))

    def test_relational_missing(self):
        code = "-SET &VAR = &X IS MISSING;"
        asg_nodes = self.build_asg(code)
        expr = asg_nodes[0].expression
        self.assertTrue(isinstance(expr, asg.IsMissingExpression))
        self.assertFalse(expr.inverted)

    def test_relational_not_missing(self):
        code = "-SET &VAR = &X IS-NOT MISSING;"
        asg_nodes = self.build_asg(code)
        expr = asg_nodes[0].expression
        self.assertTrue(isinstance(expr, asg.IsMissingExpression))
        self.assertTrue(expr.inverted)

    def test_relational_between(self):
        code = "-SET &VAR = &X FROM 1 TO 10;"
        asg_nodes = self.build_asg(code)
        expr = asg_nodes[0].expression
        self.assertTrue(isinstance(expr, asg.BetweenExpression))
        self.assertEqual(expr.lower.value, 1)
        self.assertEqual(expr.upper.value, 10)

    def test_relational_in(self):
        code = "-SET &VAR = &X IN ('A', 'B', 'C');"
        asg_nodes = self.build_asg(code)
        expr = asg_nodes[0].expression
        self.assertTrue(isinstance(expr, asg.InExpression))
        self.assertEqual(len(expr.values), 3)

    def test_relational_or_list(self):
        code = "-SET &VAR = &X EQ 'A' OR 'B' OR 'C';"
        asg_nodes = self.build_asg(code)
        expr = asg_nodes[0].expression
        # Should be (&X EQ 'A' OR &X EQ 'B') OR &X EQ 'C'
        self.assertTrue(isinstance(expr, asg.BinaryOperation))
        self.assertEqual(expr.operator, "OR")

    def test_join_basic(self):
        code = "JOIN EMP_ID IN EMPDATA TO EMP_ID IN TRAINING AS J1"
        asg_nodes = self.build_asg(code)
        self.assertEqual(len(asg_nodes), 1)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.Join))
        self.assertEqual(node.source.fields, ["EMP_ID"])
        self.assertEqual(node.source.filename, "EMPDATA")
        self.assertEqual(node.target.fields, ["EMP_ID"])
        self.assertEqual(node.target.filename, "TRAINING")
        self.assertEqual(node.join_as, "J1")
        self.assertIsNone(node.join_type)

    def test_join_left_outer(self):
        code = "JOIN LEFT OUTER EMP_ID IN EMPDATA TO EMP_ID IN TRAINING"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.Join))
        self.assertEqual(node.join_type, "LEFT_OUTER")

    def test_join_clear(self):
        code = "JOIN CLEAR *"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.JoinClear))

    def test_set_command(self):
        code = "SET PAGE = NOPAGE;"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.SetCommand))
        self.assertEqual(node.parameter, "PAGE")
        self.assertEqual(node.value, "NOPAGE")

    def test_set_command_numeric(self):
        code = "SET LINES = 66"
        asg_nodes = self.build_asg(code)
        node = asg_nodes[0]
        self.assertEqual(node.value, "66")

    def test_define_file(self):
        code = """
        DEFINE FILE CAR
        SALES_K/D12.2 = SALES / 1000;
        TAX/D12.2 = SALES * 0.08;
        END
        """
        asg_nodes = self.build_asg(code)
        self.assertEqual(len(asg_nodes), 1)
        node = asg_nodes[0]
        self.assertTrue(isinstance(node, asg.DefineFile))
        self.assertEqual(node.filename, "CAR")
        self.assertEqual(len(node.assignments), 2)

        a1 = node.assignments[0]
        self.assertEqual(a1.name, "SALES_K")
        self.assertEqual(a1.format, "D12.2")
        self.assertTrue(isinstance(a1.expression, asg.BinaryOperation))

        a2 = node.assignments[1]
        self.assertEqual(a2.name, "TAX")
        self.assertEqual(a2.format, "D12.2")
        self.assertTrue(isinstance(a2.expression, asg.BinaryOperation))

if __name__ == '__main__':
    unittest.main()

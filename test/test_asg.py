import unittest
from src.asg import Expression, Statement, Command

class TestASGNodes(unittest.TestCase):
    def test_expression_instantiation(self):
        expr = Expression()
        self.assertIsInstance(expr, Expression)

    def test_statement_instantiation(self):
        stmt = Statement()
        self.assertIsInstance(stmt, Statement)

    def test_command_instantiation(self):
        cmd = Command()
        self.assertIsInstance(cmd, Command)

if __name__ == '__main__':
    unittest.main()

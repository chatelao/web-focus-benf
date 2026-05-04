import unittest
from wf_parser import WebFocusParser
from asg_builder import ReportASGBuilder
from ir_builder import IRBuilder
from emitter import PostgresEmitter

class TestDmIO(unittest.TestCase):
    def setUp(self):
        self.parser = WebFocusParser()
        self.asg_builder = ReportASGBuilder()
        self.ir_builder = IRBuilder()
        self.emitter = PostgresEmitter()

    def test_dm_read(self):
        fex = "-READ MYFILE &VAR1 &VAR2.A10"
        tree = self.parser.parse(fex)
        asg_nodes = self.asg_builder.visit(tree)
        cfg = self.ir_builder.build(asg_nodes)
        sql = self.emitter.emit(cfg)

        self.assertIn("/* -READ MYFILE &VAR1 &VAR2.A10 */", sql)

    def test_dm_write(self):
        fex = "-WRITE LOGFILE \"Processing started for\" &USER"
        tree = self.parser.parse(fex)
        asg_nodes = self.asg_builder.visit(tree)
        cfg = self.ir_builder.build(asg_nodes)
        sql = self.emitter.emit(cfg)

        self.assertIn("/* -WRITE LOGFILE 'Processing started for' || v_USER */", sql)

    def test_dm_default(self):
        fex = "-DEFAULT &COUNTRY='USA'"
        tree = self.parser.parse(fex)
        asg_nodes = self.asg_builder.visit(tree)
        cfg = self.ir_builder.build(asg_nodes)
        sql = self.emitter.emit(cfg)

        self.assertIn("/* -DEFAULT &COUNTRY = 'USA' */", sql)

    def test_dm_defaults(self):
        fex = "-DEFAULTS &FORMAT='PDF'"
        tree = self.parser.parse(fex)
        asg_nodes = self.asg_builder.visit(tree)
        cfg = self.ir_builder.build(asg_nodes)
        sql = self.emitter.emit(cfg)

        self.assertIn("/* -DEFAULT &FORMAT = 'PDF' */", sql)

    def test_dm_defaulth(self):
        fex = "-DEFAULTH &HEIGHT=400"
        tree = self.parser.parse(fex)
        asg_nodes = self.asg_builder.visit(tree)
        cfg = self.ir_builder.build(asg_nodes)
        sql = self.emitter.emit(cfg)

        self.assertIn("/* -DEFAULT &HEIGHT = 400 */", sql)

if __name__ == '__main__':
    unittest.main()

import unittest
import os
import sys

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from emitter import PostgresEmitter
import ir
import asg

class TestHoldEmitter(unittest.TestCase):
    def test_emit_instruction_report_with_hold(self):
        emitter = PostgresEmitter()
        verb = asg.VerbCommand(verb="PRINT", fields=[asg.FieldSelection(name="FIELD1")])
        hold = asg.OutputCommand(output_type="HOLD", filename="MYHOLD")

        instr = ir.Report(filename="MYTABLE", components=[verb, hold])

        sql = emitter.emit_instruction(instr)

        self.assertIn("DROP TABLE IF EXISTS MYHOLD;", sql)
        self.assertIn("CREATE TEMP TABLE MYHOLD AS", sql)
        self.assertIn("SELECT FIELD1 FROM MYTABLE", sql)

    def test_emit_instruction_report_with_on_table_hold(self):
        emitter = PostgresEmitter()
        verb = asg.VerbCommand(verb="PRINT", fields=[asg.FieldSelection(name="FIELD1")])
        hold = asg.OutputCommand(output_type="HOLD", filename="ON_TABLE_HOLD")
        on_table = asg.OnCommand(target="TABLE", actions=[hold])

        instr = ir.Report(filename="MYTABLE", components=[verb, on_table])

        sql = emitter.emit_instruction(instr)

        self.assertIn("DROP TABLE IF EXISTS ON_TABLE_HOLD;", sql)
        self.assertIn("CREATE TEMP TABLE ON_TABLE_HOLD AS", sql)
        self.assertIn("SELECT FIELD1 FROM MYTABLE", sql)

    def test_emit_instruction_report_with_hold_sanitization(self):
        emitter = PostgresEmitter()
        verb = asg.VerbCommand(verb="PRINT", fields=[asg.FieldSelection(name="FIELD1")])
        # WebFOCUS filenames can have dots or hyphens
        hold = asg.OutputCommand(output_type="HOLD", filename="MY-DATA.TMP")

        instr = ir.Report(filename="MYTABLE", components=[verb, hold])

        sql = emitter.emit_instruction(instr)

        # Should be sanitized to MY_DATA_TMP
        self.assertIn("DROP TABLE IF EXISTS MY_DATA_TMP;", sql)
        self.assertIn("CREATE TEMP TABLE MY_DATA_TMP AS", sql)

if __name__ == '__main__':
    unittest.main()

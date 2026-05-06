import unittest
import ir
import asg
from emitter import PostgresEmitter
from metadata_registry import MetadataRegistry

class TestMatchHold(unittest.TestCase):
    def test_match_hold_emission(self):
        # 1. Setup metadata
        registry = MetadataRegistry()
        f1 = asg.MasterFile(name="FILE1")
        f1.segments = [asg.Segment(name="S1", fields=[asg.Field(name="ID"), asg.Field(name="VAL1")])]
        registry.register_master_file(f1)

        f2 = asg.MasterFile(name="FILE2")
        f2.segments = [asg.Segment(name="S1", fields=[asg.Field(name="ID"), asg.Field(name="VAL2")])]
        registry.register_master_file(f2)

        # 2. Create Match instruction with HOLD
        match_instr = ir.Match(
            filename="FILE1",
            components=[
                asg.SortCommand(sort_type="BY", field=asg.FieldSelection(name="ID")),
                asg.VerbCommand(verb="SUM", fields=[asg.FieldSelection(name="VAL1")]),
                asg.OutputCommand(output_type="HOLD", filename="MATCH_RESULTS")
            ],
            sub_matches=[
                ir.Instruction( # This is actually an ASG node in the current Match implementation but we use IR wrapper for tests
                    filename="FILE2",
                    components=[
                        asg.SortCommand(sort_type="BY", field=asg.FieldSelection(name="ID")),
                        asg.VerbCommand(verb="SUM", fields=[asg.FieldSelection(name="VAL2")])
                    ],
                    after_match=asg.AfterMatchPhrase(merge_type="OLD_OR_NEW")
                )
            ]
        )

        # In ir.py Match takes sub_matches as list of objects with certain attributes.
        # Looking at _emit_match, it expects them to have filename and components.
        # Let's fix the test setup to match what _emit_match expects.

        class MockSubMatch:
            def __init__(self, filename, components, after_match):
                self.filename = filename
                self.components = components
                self.after_match = after_match

        match_instr.sub_matches = [
            MockSubMatch("FILE2", [
                asg.SortCommand(sort_type="BY", field=asg.FieldSelection(name="ID")),
                asg.VerbCommand(verb="SUM", fields=[asg.FieldSelection(name="VAL2")])
            ], asg.AfterMatchPhrase(merge_type="OLD_OR_NEW"))
        ]

        emitter = PostgresEmitter(metadata_registry=registry)
        sql = emitter._emit_match(match_instr)

        # 3. Verifications
        self.assertIn("DROP TABLE IF EXISTS MATCH_RESULTS;", sql)
        self.assertIn("CREATE TEMP TABLE MATCH_RESULTS AS", sql)
        self.assertIn("WITH", sql)
        self.assertIn("FULL OUTER JOIN T2", sql)
        self.assertTrue(sql.strip().endswith(";"))

if __name__ == '__main__':
    unittest.main()

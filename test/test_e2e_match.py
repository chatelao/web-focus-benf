import unittest
import sys
import os

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from asg import (
    MatchRequest, SubMatch, VerbCommand, FieldSelection,
    SortCommand, AfterMatchPhrase, MasterFile, Segment, Field
)
from ir_builder import IRBuilder
from emitter import PostgresEmitter
from metadata_registry import MetadataRegistry

class TestE2EMatch(unittest.TestCase):
    def test_basic_match_old_or_new(self):
        # Setup metadata
        registry = MetadataRegistry()

        f1 = MasterFile(name="FILE1")
        s1 = Segment(name="S1")
        s1.fields = [Field(name="PRODUCT"), Field(name="SALES")]
        f1.segments = [s1]
        registry.register_master_file(f1)

        f2 = MasterFile(name="FILE2")
        s2 = Segment(name="S2")
        s2.fields = [Field(name="PRODUCT"), Field(name="RETURNS")]
        f2.segments = [s2]
        registry.register_master_file(f2)

        # Construct ASG
        match_request = MatchRequest(
            filename="FILE1",
            components=[
                VerbCommand(verb="SUM", fields=[FieldSelection(name="SALES")]),
                SortCommand(sort_type="BY", field=FieldSelection(name="PRODUCT"))
            ],
            sub_matches=[
                SubMatch(
                    filename="FILE2",
                    components=[
                        VerbCommand(verb="SUM", fields=[FieldSelection(name="RETURNS")]),
                        SortCommand(sort_type="BY", field=FieldSelection(name="PRODUCT"))
                    ],
                    after_match=AfterMatchPhrase(merge_type="OLD-OR-NEW")
                )
            ]
        )

        # Build IR
        builder = IRBuilder()
        cfg = builder.build([match_request])

        # Emit SQL
        emitter = PostgresEmitter(metadata_registry=registry)
        sql = emitter.emit(cfg)

        print(sql)

        # Basic assertions
        self.assertIn("FULL OUTER JOIN", sql)
        self.assertIn("COALESCE", sql)
        self.assertIn("FILE1", sql)
        self.assertIn("FILE2", sql)
        self.assertIn("PRODUCT", sql)
        self.assertIn("SALES", sql)
        self.assertIn("RETURNS", sql)

    def test_match_old_nor_new(self):
        # Setup metadata
        registry = MetadataRegistry()
        f1 = MasterFile(name="FILE1")
        s1 = Segment(name="S1")
        s1.fields = [Field(name="PRODUCT"), Field(name="SALES")]
        f1.segments = [s1]
        registry.register_master_file(f1)

        f2 = MasterFile(name="FILE2")
        s2 = Segment(name="S2")
        s2.fields = [Field(name="PRODUCT"), Field(name="RETURNS")]
        f2.segments = [s2]
        registry.register_master_file(f2)

        # Construct ASG
        match_request = MatchRequest(
            filename="FILE1",
            components=[
                VerbCommand(verb="SUM", fields=[FieldSelection(name="SALES")]),
                SortCommand(sort_type="BY", field=FieldSelection(name="PRODUCT"))
            ],
            sub_matches=[
                SubMatch(
                    filename="FILE2",
                    components=[
                        VerbCommand(verb="SUM", fields=[FieldSelection(name="RETURNS")]),
                        SortCommand(sort_type="BY", field=FieldSelection(name="PRODUCT"))
                    ],
                    after_match=AfterMatchPhrase(merge_type="OLD-NOR-NEW")
                )
            ]
        )

        # Build IR
        builder = IRBuilder()
        cfg = builder.build([match_request])

        # Emit SQL
        emitter = PostgresEmitter(metadata_registry=registry)
        sql = emitter.emit(cfg)

        print(sql)

        # Assertions for OLD-NOR-NEW (symmetric difference)
        self.assertIn("FULL OUTER JOIN", sql)
        # Check for WHERE clause that implements symmetric difference
        self.assertIn("WHERE T1.\"PRODUCT\" IS NULL OR T2.\"PRODUCT\" IS NULL", sql)

    def test_three_file_match(self):
        # Setup metadata
        registry = MetadataRegistry()
        for i in range(1, 4):
            f = MasterFile(name=f"FILE{i}")
            s = Segment(name=f"S{i}")
            s.fields = [Field(name="PRODUCT"), Field(name=f"VAL{i}")]
            f.segments = [s]
            registry.register_master_file(f)

        # Construct ASG: FILE1 + FILE2 + FILE3
        match_request = MatchRequest(
            filename="FILE1",
            components=[
                VerbCommand(verb="SUM", fields=[FieldSelection(name="VAL1")]),
                SortCommand(sort_type="BY", field=FieldSelection(name="PRODUCT"))
            ],
            sub_matches=[
                SubMatch(
                    filename="FILE2",
                    components=[
                        VerbCommand(verb="SUM", fields=[FieldSelection(name="VAL2")]),
                        SortCommand(sort_type="BY", field=FieldSelection(name="PRODUCT"))
                    ],
                    after_match=AfterMatchPhrase(merge_type="OLD-OR-NEW")
                ),
                SubMatch(
                    filename="FILE3",
                    components=[
                        VerbCommand(verb="SUM", fields=[FieldSelection(name="VAL3")]),
                        SortCommand(sort_type="BY", field=FieldSelection(name="PRODUCT"))
                    ],
                    after_match=AfterMatchPhrase(merge_type="OLD-AND-NEW")
                )
            ]
        )

        # Build IR
        builder = IRBuilder()
        cfg = builder.build([match_request])

        # Emit SQL
        emitter = PostgresEmitter(metadata_registry=registry)
        sql = emitter.emit(cfg)

        print(sql)

        # Assertions for 3-way match
        self.assertIn("T1 AS (", sql)
        self.assertIn("T2 AS (", sql)
        self.assertIn("T3 AS (", sql)
        self.assertIn("M1 AS (", sql)
        self.assertIn("M2 AS (", sql)
        self.assertIn("FROM M1 INNER JOIN T3", sql)
        self.assertIn("SELECT * FROM M2", sql)

    def test_match_old(self):
        # Setup metadata
        registry = MetadataRegistry()
        f1 = MasterFile(name="FILE1")
        s1 = Segment(name="S1")
        s1.fields = [Field(name="PRODUCT"), Field(name="SALES")]
        f1.segments = [s1]
        registry.register_master_file(f1)

        f2 = MasterFile(name="FILE2")
        s2 = Segment(name="S2")
        s2.fields = [Field(name="PRODUCT"), Field(name="RETURNS")]
        f2.segments = [s2]
        registry.register_master_file(f2)

        # Construct ASG
        match_request = MatchRequest(
            filename="FILE1",
            components=[
                VerbCommand(verb="SUM", fields=[FieldSelection(name="SALES")]),
                SortCommand(sort_type="BY", field=FieldSelection(name="PRODUCT"))
            ],
            sub_matches=[
                SubMatch(
                    filename="FILE2",
                    components=[
                        VerbCommand(verb="SUM", fields=[FieldSelection(name="RETURNS")]),
                        SortCommand(sort_type="BY", field=FieldSelection(name="PRODUCT"))
                    ],
                    after_match=AfterMatchPhrase(merge_type="OLD")
                )
            ]
        )

        # Build IR
        builder = IRBuilder()
        cfg = builder.build([match_request])

        # Emit SQL
        emitter = PostgresEmitter(metadata_registry=registry)
        sql = emitter.emit(cfg)

        print(sql)

        self.assertIn("LEFT JOIN", sql)
        self.assertNotIn("WHERE", sql)

    def test_match_new(self):
        # Setup metadata
        registry = MetadataRegistry()
        f1 = MasterFile(name="FILE1")
        s1 = Segment(name="S1")
        s1.fields = [Field(name="PRODUCT"), Field(name="SALES")]
        f1.segments = [s1]
        registry.register_master_file(f1)

        f2 = MasterFile(name="FILE2")
        s2 = Segment(name="S2")
        s2.fields = [Field(name="PRODUCT"), Field(name="RETURNS")]
        f2.segments = [s2]
        registry.register_master_file(f2)

        # Construct ASG
        match_request = MatchRequest(
            filename="FILE1",
            components=[
                VerbCommand(verb="SUM", fields=[FieldSelection(name="SALES")]),
                SortCommand(sort_type="BY", field=FieldSelection(name="PRODUCT"))
            ],
            sub_matches=[
                SubMatch(
                    filename="FILE2",
                    components=[
                        VerbCommand(verb="SUM", fields=[FieldSelection(name="RETURNS")]),
                        SortCommand(sort_type="BY", field=FieldSelection(name="PRODUCT"))
                    ],
                    after_match=AfterMatchPhrase(merge_type="NEW")
                )
            ]
        )

        # Build IR
        builder = IRBuilder()
        cfg = builder.build([match_request])

        # Emit SQL
        emitter = PostgresEmitter(metadata_registry=registry)
        sql = emitter.emit(cfg)

        print(sql)

        self.assertIn("RIGHT JOIN", sql)
        self.assertNotIn("WHERE", sql)

if __name__ == '__main__':
    unittest.main()

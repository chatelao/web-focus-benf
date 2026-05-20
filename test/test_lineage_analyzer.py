import unittest
import ir
import asg
from lineage_analyzer import LineageAnalyzer

class TestLineageAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = LineageAnalyzer()

    def test_basic_report_lineage(self):
        # TABLE FILE CAR
        # PRINT MODEL
        # BY COUNTRY
        # WHERE SEATS GT 2
        # END
        report = ir.Report(
            filename="CAR",
            components=[
                asg.VerbCommand(verb="PRINT", fields=[asg.FieldSelection(name="MODEL")]),
                asg.SortCommand(sort_type="BY", field=asg.FieldSelection(name="COUNTRY")),
                asg.WhereClause(condition=asg.BinaryOperation(
                    left=asg.Identifier(name="SEATS"),
                    operator="GT",
                    right=asg.Literal(value=2)
                ))
            ]
        )
        cfg = ir.ControlFlowGraph()
        block = ir.BasicBlock(name="B1")
        block.add_instruction(report)
        cfg.add_block(block)

        lineage = self.analyzer.analyze(cfg)

        self.assertIn("CAR", lineage['sources'])
        self.assertIn("MODEL", lineage['fields']['select'])
        self.assertIn("COUNTRY", lineage['fields']['sort'])
        self.assertIn("SEATS", lineage['fields']['filter'])

    def test_match_lineage(self):
        # MATCH FILE CAR
        # PRINT MODEL BY BODYTYPE
        # RUN
        # FILE SALES
        # PRINT RETAIL_COST BY BODYTYPE
        # AFTER MATCH HOLD AS MATCHED_DATA
        # END
        match = ir.Match(
            filename="CAR",
            components=[
                asg.VerbCommand(verb="PRINT", fields=[asg.FieldSelection(name="MODEL")]),
                asg.SortCommand(sort_type="BY", field=asg.FieldSelection(name="BODYTYPE"))
            ],
            sub_matches=[
                asg.SubMatch(
                    filename="SALES",
                    components=[
                        asg.VerbCommand(verb="PRINT", fields=[asg.FieldSelection(name="RETAIL_COST")]),
                        asg.SortCommand(sort_type="BY", field=asg.FieldSelection(name="BODYTYPE"))
                    ],
                    after_match=asg.AfterMatchPhrase(merge_type="OLD_OR_NEW", output_command=asg.OutputCommand(output_type="HOLD", filename="MATCHED_DATA"))
                )
            ]
        )
        cfg = ir.ControlFlowGraph()
        block = ir.BasicBlock(name="B1")
        block.add_instruction(match)
        cfg.add_block(block)

        lineage = self.analyzer.analyze(cfg)

        self.assertIn("CAR", lineage['sources'])
        self.assertIn("SALES", lineage['sources'])
        self.assertIn("MATCHED_DATA", lineage['targets'])
        self.assertIn("MODEL", lineage['fields']['select'])
        self.assertIn("RETAIL_COST", lineage['fields']['select'])
        self.assertIn("BODYTYPE", lineage['fields']['sort'])

    def test_compute_and_on_lineage(self):
        # TABLE FILE CAR
        # SUM SALES
        # COMPUTE MARGIN = SALES - COST;
        # ON COUNTRY SUM SALES
        # END
        report = ir.Report(
            filename="CAR",
            components=[
                asg.VerbCommand(verb="SUM", fields=[asg.FieldSelection(name="SALES")]),
                asg.ComputeCommand(name="MARGIN", expression=asg.BinaryOperation(
                    left=asg.Identifier(name="SALES"),
                    operator="-",
                    right=asg.Identifier(name="COST")
                )),
                asg.OnCommand(target="COUNTRY", actions=[
                    asg.VerbCommand(verb="SUM", fields=[asg.FieldSelection(name="SALES")])
                ])
            ]
        )
        cfg = ir.ControlFlowGraph()
        block = ir.BasicBlock(name="B1")
        block.add_instruction(report)
        cfg.add_block(block)

        lineage = self.analyzer.analyze(cfg)

        self.assertIn("SALES", lineage['fields']['select'])
        self.assertIn("COST", lineage['fields']['select'])

if __name__ == '__main__':
    unittest.main()

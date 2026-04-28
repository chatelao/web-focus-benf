import pytest
from antlr4 import CommonTokenStream, InputStream
from WebFocusReportLexer import WebFocusReportLexer
from WebFocusReportParser import WebFocusReportParser
from asg_builder import ReportASGBuilder
from asg import *

def test_compound_layout_asg():
    fex = """
COMPOUND LAYOUT PCHOLD FORMAT PDF
SECTION=section1, LAYOUT=ON, METADATA='metadata', $
PAGELAYOUT=1, NAME='Page Layout 1', SCREEN=ON, $
COMPONENT=Table_1, TYPE=REPORT, POSITION=(1.0 1.0), DIMENSION=(5.0 5.0), $
END
TABLE FILE CAR
PRINT COUNTRY CAR MODEL
END
COMPOUND END
"""
    input_stream = InputStream(fex)
    lexer = WebFocusReportLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = WebFocusReportParser(token_stream)
    tree = parser.start()

    builder = ReportASGBuilder()
    asg_nodes = builder.visit(tree)

    assert len(asg_nodes) == 1
    compound = asg_nodes[0]
    assert isinstance(compound, CompoundLayout)
    assert compound.output_command.output_type == "PCHOLD"
    assert compound.output_command.format == "PDF"

    assert len(compound.statements) == 3
    assert compound.statements[0].name == "SECTION"
    assert compound.statements[0].value == "section1"
    assert len(compound.statements[0].properties) == 2
    assert compound.statements[0].properties[0].name == "LAYOUT"
    assert compound.statements[0].properties[0].value == "ON"

    assert compound.statements[1].name == "PAGELAYOUT"
    assert compound.statements[1].value == "1"
    assert len(compound.statements[1].properties) == 2
    assert compound.statements[1].properties[0].name == "NAME"
    assert compound.statements[1].properties[0].value == "Page Layout 1"

    assert compound.statements[2].name == "COMPONENT"
    assert compound.statements[2].value == "Table_1"
    assert len(compound.statements[2].properties) == 3
    assert compound.statements[2].properties[1].name == "POSITION"
    assert compound.statements[2].properties[1].value == ["1.0", "1.0"]

    assert len(compound.components) == 1
    assert isinstance(compound.components[0], ReportRequest)
    assert compound.components[0].filename == "CAR"

def test_on_table_set_style_asg():
    fex = """
TABLE FILE CAR
PRINT COUNTRY
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END
"""
    input_stream = InputStream(fex)
    lexer = WebFocusReportLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = WebFocusReportParser(token_stream)
    tree = parser.start()

    builder = ReportASGBuilder()
    asg_nodes = builder.visit(tree)

    assert len(asg_nodes) == 1
    report = asg_nodes[0]
    assert isinstance(report, ReportRequest)

    on_table = next(c for c in report.components if isinstance(c, OnCommand) and c.target == "TABLE")
    style_block = next(a for a in on_table.actions if isinstance(a, StyleBlock))

    assert len(style_block.statements) == 1
    assert style_block.statements[0].name == "TYPE"
    assert style_block.statements[0].value == "REPORT"
    assert style_block.statements[0].properties[0].name == "GRID"
    assert style_block.statements[0].properties[0].value == "OFF"

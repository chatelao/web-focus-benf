import pytest
from scripts.antlr4_to_ebnf import convert_antlr_to_ebnf

def test_basic_conversion():
    antlr = """
    grammar Test;
    rule1: 'TERM' rule2;
    rule2: 'ANOTHER' | rule3;
    rule3: 'FINAL';

    TOKEN1: 'literal';
    """
    expected = [
        "rule1 ::= 'TERM' rule2",
        "rule2 ::= 'ANOTHER' | rule3",
        "rule3 ::= 'FINAL'",
        "TOKEN1 ::= 'literal'"
    ]
    result = convert_antlr_to_ebnf(antlr)
    for rule in expected:
        assert rule in result

def test_multiline_rule():
    antlr = """
    rule:
        PART1
        | PART2
        ;
    """
    result = convert_antlr_to_ebnf(antlr)
    assert "rule ::= PART1 | PART2" in result

def test_comment_removal():
    antlr = """
    // This is a comment
    rule: 'TERM'; /* Multiline
    comment */
    """
    result = convert_antlr_to_ebnf(antlr)
    assert "//" not in result
    assert "/*" not in result
    assert "rule ::= 'TERM'" in result

def test_string_with_comment_markers():
    antlr = """
    rule: 'http://' | "/* not a comment */";
    """
    result = convert_antlr_to_ebnf(antlr)
    assert "rule ::= 'http://' | \"/* not a comment */\"" in result

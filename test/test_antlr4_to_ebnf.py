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

def test_cardinality_and_grouping():
    antlr = """
    rule: (part1 | part2)* part3+ part4?;
    """
    result = convert_antlr_to_ebnf(antlr)
    assert "rule ::= (part1 | part2)* part3+ part4?" in result

def test_non_greedy_markers():
    antlr = """
    rule: part1*? part2+? part3??;
    """
    result = convert_antlr_to_ebnf(antlr)
    assert "rule ::= part1* part2+ part3?" in result

def test_lexer_commands():
    antlr = r"""
    WS: [ \t\r\n]+ -> skip;
    COMMENT: '/*' .*? '*/' -> channel(HIDDEN);
    """
    result = convert_antlr_to_ebnf(antlr)
    assert r"WS ::= [ \t\r\n]+" in result
    assert "COMMENT ::= '/*' .* '*/'" in result

def test_char_class_conversion():
    antlr = """
    TABLE: [tT][aA][bB][lL][eE];
    FILE: [fF][iI][lL][eE];
    MIXED: 'PREFIX' [sS][uU][fF][fF][iI][xX];
    """
    result = convert_antlr_to_ebnf(antlr)
    assert "TABLE ::= 'TABLE'" in result
    assert "FILE ::= 'FILE'" in result
    assert "MIXED ::= 'PREFIX' 'SUFFIX'" in result

def test_fragment_rules():
    antlr = """
    fragment DIGIT: [0-9];
    NUMBER: DIGIT+;
    """
    result = convert_antlr_to_ebnf(antlr)
    assert "DIGIT ::= [0-9]" in result
    assert "NUMBER ::= DIGIT+" in result

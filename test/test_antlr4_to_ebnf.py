import pytest
from scripts.antlr4_to_ebnf import convert_antlr_to_ebnf, check_coverage

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

def test_pruning_and_inlining():
    antlr = """
    // @internal
    rule1: 'internal_body';

    // @inline
    rule2: 'inline_body';

    // @inline
    rule3: 'with' 'spaces';

    /* @inline */
    rule4: rule2 | 'other';

    start: rule1 rule2 rule3 rule4;
    """
    result = convert_antlr_to_ebnf(antlr)

    # rule1, rule2, rule3, rule4 should not be in the output as top-level rules
    assert "rule1 ::=" not in result
    assert "rule2 ::=" not in result
    assert "rule3 ::=" not in result
    assert "rule4 ::=" not in result

    # Check inlining in start
    # rule1 was internal, so it is inlined (currently we inline both)
    assert "start ::= 'internal_body' 'inline_body' ( 'with' 'spaces' ) ( 'inline_body' | 'other' )" in result

def test_recursion_protection():
    antlr = """
    // @inline
    a: a 'x' | 'y';

    start: a;
    """
    result = convert_antlr_to_ebnf(antlr)
    # a should NOT be inlined into itself or start if it causes recursion
    # our current logic says: if name_to_inline in inline_body, don't inline.
    assert "a ::= a 'x' | 'y'" in result
    assert "start ::= a" in result

def test_semicolon_in_string():
    antlr = """
    SEMI: ';';
    OTHER: 'abc;def';
    """
    result = convert_antlr_to_ebnf(antlr)
    assert "SEMI ::= ';'" in result
    assert "OTHER ::= 'abc;def'" in result

def test_coverage_check_all_present():
    antlr = """
    rule1: 'A';
    rule2: 'B';
    """
    ebnf = convert_antlr_to_ebnf(antlr)
    missing = check_coverage(antlr, ebnf)
    assert missing == []

def test_coverage_check_missing_rule():
    antlr = """
    rule1: 'A';
    rule2: 'B';
    """
    # Simulate ebnf missing rule2
    ebnf = "rule1 ::= 'A'"
    missing = check_coverage(antlr, ebnf)
    assert missing == ["rule2"]

def test_coverage_check_ignores_internal_and_inline():
    antlr = """
    // @internal
    rule1: 'A';
    // @inline
    rule2: 'B';
    rule3: 'C';
    """
    # ebnf will only contain rule3
    ebnf = "rule3 ::= 'C'"
    missing = check_coverage(antlr, ebnf)
    assert missing == []

def test_coverage_check_recursive_inline_preserved():
    antlr = """
    // @inline
    a: a 'x' | 'y';
    """
    ebnf = convert_antlr_to_ebnf(antlr)
    # Since 'a' is recursive, it is NOT inlined and should remain in EBNF.
    assert "a ::= a 'x' | 'y'" in ebnf
    missing = check_coverage(antlr, ebnf)
    assert missing == []

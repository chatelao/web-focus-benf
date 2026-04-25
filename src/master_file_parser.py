from lark import Lark
import sys

# Master File grammar
# It needs to be flexible enough to handle the variety of WebFOCUS Master File syntaxes.
# Declarations usually end with a '$'.
# Attributes can be named (ATTR=VAL) or positional.

mf_grammar = r"""
    ?start: (item)*

    ?item: declaration
         | comment
         | _WS

    ?declaration: file_decl
                | segment_decl
                | field_decl
                | define_decl
                | compute_decl
                | variable_decl
                | other_decl

    file_decl: FILENAME_KW ["="] VALUE ("," attr_val)* [","] DOLLAR
    segment_decl: SEGNAME_KW ["="] VALUE ("," attr_val)* [","] DOLLAR
    field_decl: FIELDNAME_KW ["="] VALUE ("," attr_val)* [","] DOLLAR
    variable_decl: VARIABLE_KW (attr_val | ",")* DOLLAR

    define_decl: DEFINE_KW name_format "=" expression ";" ("," attr_val)* [","] DOLLAR
    compute_decl: COMPUTE_KW name_format "=" expression ";" ("," attr_val)* [","] DOLLAR

    other_decl: ATTR "=" VALUE ("," attr_val)* [","] DOLLAR

    ?attr_val: assignment | VALUE
    assignment: ATTR "=" VALUE

    name_format: UNQUOTED_VALUE ["/" UNQUOTED_VALUE]
    expression: /[^;]+/

    FILENAME_KW.2: /FILENAME|FILE/i
    SEGNAME_KW.2: /SEGNAME|SEGMENT/i
    FIELDNAME_KW.2: /FIELDNAME|FIELD/i
    VARIABLE_KW.2: /VARIABLE/i
    DEFINE_KW.2: /DEFINE/i
    COMPUTE_KW.2: /COMPUTE/i

    ATTR: /[a-zA-Z_][a-zA-Z0-9_.]*/
    VALUE: STRING | UNQUOTED_VALUE

    UNQUOTED_VALUE: /[a-zA-Z0-9_.\/&%#@<>:*-]+/
    STRING: /'[^']*'/ | /"[^"]*"/

    DOLLAR: "$"
    comment: DOLLAR /[^\n]+/

    %import common.WS
    %ignore WS
    _WS: WS
"""

class MasterFileParser:
    def __init__(self):
        self.parser = Lark(mf_grammar, start='start', parser='earley')

    def parse(self, text):
        return self.parser.parse(text)

if __name__ == "__main__":
    sample_mf = """
    FILENAME=EMPLOYEE, SUFFIX=FOC, MFD_PROFILE=baseapp/DDBAEMP,$
    VARIABLE NAME = Emptitle, USAGE=A30, DEFAULT=EMPID,$
    SEGMENT=EMPDATA,SEGTYPE=S0, $
    FIELDNAME=PIN   , ALIAS=ID, USAGE=A9, INDEX=I,   TITLE='&&Emptitle',$
    FIELDNAME=LASTNAME,     LN,       A15,             $
    DEFINE AREA/A13=DECODE DIV (NE 'NORTH EASTERN' SE 'SOUTH EASTERN' CE 'CENTRAL' WE 'WESTERN' CORP 'CORPORATE' ELSE 'INVALID AREA');$
    """
    parser = MasterFileParser()
    try:
        tree = parser.parse(sample_mf)
        print(tree.pretty())
    except Exception as e:
        print(f"Error parsing Master File:\n{e}")
        sys.exit(1)

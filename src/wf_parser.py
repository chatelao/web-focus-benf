from lark import Lark
import sys
from master_file_parser import MasterFileParser

# A basic grammar for a subset of WebFOCUS TABLE requests
wf_grammar = r"""
    ?start: request

    request: table_file verb_command* end_command

    table_file: TABLE FILE qualified_name

    ?verb_command: display_command
                 | by_command
                 | across_command
                 | where_command
                 | heading_command
                 | footing_command

    display_command: verb (field_list | asterisk)

    asterisk: "*"

    verb: SUM_K | PRINT_K | LIST_K | COUNT_K | WRITE_K | ADD_K

    field_list: [THE] field_or_prefixed (([AND] [THE]) field_or_prefixed)*

    field_or_prefixed: (prefix_operator ".")* field

    field: qualified_name (as_phrase)?

    as_phrase: AS STRING

    by_command: [RANKED] BY sort_options? field [NOPRINT]
    across_command: ACROSS sort_options? field [NOPRINT]

    sort_options: (HIGHEST | LOWEST | TOP | BOTTOM) NUMBER?
                | NUMBER

    where_command: WHERE qualified_name EQ (qualified_name | NUMBER | STRING)
    heading_command: HEADING CENTER? STRING
    footing_command: FOOTING CENTER? STRING

    end_command: END

    qualified_name: NAME ("." NAME)*

    prefix_operator: AVE | MIN | MAX | CNT | FST | LST | ASQ | MDN | MDE | PCT | RPCT | RNK | DST | TOT | SUM_K | CT

    TABLE: /TABLE/i
    FILE: /FILE/i
    SUM_K: /SUM/i
    PRINT_K: /PRINT/i
    LIST_K: /LIST/i
    COUNT_K: /COUNT/i
    WRITE_K: /WRITE/i
    ADD_K: /ADD/i
    BY: /BY/i
    ACROSS: /ACROSS/i
    RANKED: /RANKED/i
    HIGHEST: /HIGHEST/i
    LOWEST: /LOWEST/i
    TOP: /TOP/i
    BOTTOM: /BOTTOM/i
    NOPRINT: /NOPRINT/i
    WHERE: /WHERE/i
    EQ: /EQ/i
    AS: /AS/i
    HEADING: /HEADING/i
    FOOTING: /FOOTING/i
    CENTER: /CENTER/i
    AND: /AND/i
    THE: /THE/i
    END: /END/i

    AVE: /AVE/i
    MIN: /MIN/i
    MAX: /MAX/i
    CNT: /CNT/i
    FST: /FST/i
    LST: /LST/i
    ASQ: /ASQ/i
    MDN: /MDN/i
    MDE: /MDE/i
    PCT: /PCT/i
    RPCT: /RPCT/i
    RNK: /RNK/i
    DST: /DST/i
    TOT: /TOT/i
    CT: /CT/i

    NAME: /(?!(TABLE|FILE|SUM|PRINT|LIST|COUNT|WRITE|ADD|BY|ACROSS|RANKED|HIGHEST|LOWEST|TOP|BOTTOM|NOPRINT|WHERE|EQ|AS|HEADING|FOOTING|CENTER|AND|THE|END|AVE|MIN|MAX|CNT|FST|LST|ASQ|MDN|MDE|PCT|RPCT|RNK|DST|TOT|CT)\b)[a-zA-Z_][a-zA-Z0-9_]*/i

    %import common.NUMBER
    %import common.WS
    %ignore WS

    STRING: "'" /[^']*/ "'"
          | "\"" /[^"]*/ "\""
"""

class WebFocusParser:
    def __init__(self):
        self.report_parser = Lark(wf_grammar, start='start', parser='earley')
        self.master_parser = MasterFileParser()

    def parse(self, text):
        # A simple dispatcher: if it contains 'FILENAME', assume it's a Master File
        # Otherwise, assume it's a report request.
        if 'FILENAME' in text.upper() or 'SEGNAME' in text.upper():
            return self.master_parser.parse(text)
        else:
            return self.report_parser.parse(text)

if __name__ == "__main__":
    sample_report = """
    TABLE FILE EMPDATA
    HEADING CENTER "Education Cost vs. Salary"
    FOOTING "End of Report"
    SUM AVE.EXPENSES AS 'Average Education Cost' MAX.SALARY AS 'Max Salary'
    BY DIV
    BY DEPT
    WHERE YEAR EQ 1991
    END
    """

    parser = WebFocusParser()

    print("--- Parsing Report Request ---")
    try:
        tree = parser.parse(sample_report)
        print(tree.pretty())
    except Exception as e:
        print(f"Error parsing report:\n{e}")

    sample_master = """
    FILENAME=EMPLOYEE, SUFFIX=FOC, $
    SEGNAME=EMPINFO, SEGTYPE=S1, $
    FIELDNAME=EMP_ID, ALIAS=EID, FORMAT=A9, $
    """
    print("\n--- Parsing Master File ---")
    try:
        tree = parser.parse(sample_master)
        print(tree.pretty())
    except Exception as e:
        print(f"Error parsing Master File:\n{e}")

from lark import Lark
import sys
from master_file_parser import MasterFileParser

# A basic grammar for a subset of WebFOCUS TABLE requests
wf_grammar = r"""
    ?start: request

    request: table_file command* end_command

    table_file: TABLE FILE NAME

    ?command: sum_command
            | by_command
            | where_command
            | heading_command

    sum_command: SUM field_list
    by_command: BY NAME
    where_command: WHERE NAME EQ (NAME | NUMBER | STRING)
    heading_command: HEADING CENTER? STRING

    field_list: field (field)*
    field: NAME (as_phrase)?
    as_phrase: AS STRING

    end_command: END

    TABLE: /TABLE/i
    FILE: /FILE/i
    SUM: /SUM/i
    BY: /BY/i
    WHERE: /WHERE/i
    EQ: /EQ/i
    AS: /AS/i
    HEADING: /HEADING/i
    CENTER: /CENTER/i
    END: /END/i

    NAME: /(?!(TABLE|FILE|SUM|BY|WHERE|EQ|AS|HEADING|CENTER|END)\b)[a-zA-Z_][a-zA-Z0-9_]*/i

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
    SUM EXPENSES AS 'Education,Cost' SALARY AS 'Current,Salary'
    BY DIV
    BY DEPT
    WHERE YEAR EQ 1991
    END
    """

    sample_master = """
    FILENAME=EMPLOYEE, SUFFIX=FOC, $
    SEGNAME=EMPINFO, SEGTYPE=S1, $
    FIELDNAME=EMP_ID, ALIAS=EID, FORMAT=A9, $
    """

    parser = WebFocusParser()

    print("--- Parsing Report Request ---")
    try:
        tree = parser.parse(sample_report)
        print(tree.pretty())
    except Exception as e:
        print(f"Error parsing report:\n{e}")

    print("\n--- Parsing Master File ---")
    try:
        tree = parser.parse(sample_master)
        print(tree.pretty())
    except Exception as e:
        print(f"Error parsing Master File:\n{e}")

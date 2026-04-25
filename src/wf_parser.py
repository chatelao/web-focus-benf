from lark import Lark

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
        self.parser = Lark(wf_grammar, start='start', parser='earley')

    def parse(self, text):
        return self.parser.parse(text)

if __name__ == "__main__":
    import sys
    sample_code = """
    TABLE FILE EMPDATA
    HEADING CENTER "Education Cost vs. Salary"
    SUM EXPENSES AS 'Education,Cost' SALARY AS 'Current,Salary'
    BY DIV
    BY DEPT
    WHERE YEAR EQ 1991
    END
    """
    parser = WebFocusParser()
    try:
        tree = parser.parse(sample_code)
        print(tree.pretty())
    except Exception as e:
        print(f"Error parsing:\n{e}")
        sys.exit(1)

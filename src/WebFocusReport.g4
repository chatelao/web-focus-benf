grammar WebFocusReport;

start: (request | dm_command | join_command | set_command | define_file | compound_layout_block)* EOF;

request: table_file (verb_command | by_command | across_command | where_command | heading_command | footing_command | on_command | compute_command | recap_command | dm_command | STRING)* end_command;

compound_layout_block: COMPOUND LAYOUT output_command (layout_statement)* end_command (request | dm_command | join_command | set_command | define_file)* COMPOUND END;

layout_statement: (identifier | TYPE) EQ layout_value (COMMA layout_property)* (COMMA? DOLLAR)?;

layout_property: (identifier | TYPE) EQ layout_value;

layout_value: qualified_name
            | NUMBER
            | dm_float
            | '(' layout_value (layout_value | COMMA)* ')'
            | STRING
            | ON | OFF | LANDSCAPE | PORTRAIT | REPORT
            ;

define_file: DEFINE FILE qualified_name (define_assignment)* end_command;

define_assignment: qualified_name (SLASH format_name)? EQ dm_expression SEMI?;

compute_command: AND? COMPUTE qualified_name (SLASH format_name)? EQ dm_expression as_phrase? SEMI?;

recap_command: RECAP recap_assignment+;

recap_assignment: qualified_name ('(' dm_expression ')')? (SLASH format_name)? EQ dm_expression (SEMI? recap_option)* SEMI?;

recap_option: as_phrase
            | INDENT NUMBER
            | NOPRINT
            ;

format_name: NAME (DOT NUMBER)? (NAME | NUMBER)*;

join_command: JOIN (CLEAR asterisk | (LEFT? OUTER)? qualified_name IN qualified_name TO ALL? qualified_name IN qualified_name (AS NAME)?) SEMI?;

set_command: SET hyphenated_name (EQ? set_value)? SEMI?;

set_value: hyphenated_name | STRING;

hyphenated_name: (identifier | NUMBER | AMPER_VAR) (dm_token | SUB_OP (identifier | NUMBER | AMPER_VAR))*;

dm_token: LABEL_DM | SET_DM | GOTO_DM | REPEAT_DM | IF_DM | TYPE_DM | INCLUDE_DM | RUN_DM | EXIT_DM;

dm_command: dm_set
          | dm_goto
          | dm_label
          | dm_if
          | dm_type
          | dm_include
          | dm_run
          | dm_exit
          | dm_repeat
          ;

dm_set: SET_DM amper_var EQ dm_expression SEMI?;

dm_goto: GOTO_DM NAME SEMI?;

dm_repeat: REPEAT_DM NAME (WHILE dm_logical_expression
                          | UNTIL dm_logical_expression
                          | dm_primary TIMES
                          | FOR amper_var FROM dm_primary TO dm_primary (STEP dm_primary)?) SEMI?;

dm_label: LABEL_DM;

dm_if: IF_DM dm_logical_expression (THEN GOTO? | GOTO) NAME (ELSE GOTO NAME)? SEMI?;

dm_type: TYPE_DM (dm_primary)* SEMI?;

dm_include: INCLUDE_DM qualified_name SEMI?;

dm_run: RUN_DM SEMI?;

dm_exit: EXIT_DM SEMI?;

dm_expression: dm_if_expression;

dm_if_expression: IF dm_logical_expression THEN dm_expression ELSE dm_expression
                | dm_logical_expression;

dm_logical_expression: '(' dm_logical_expression ')'
                     | dm_relational_expression
                     | NOT dm_logical_expression
                     | dm_logical_expression AND dm_logical_expression
                     | dm_logical_expression OR dm_logical_expression
                     ;

dm_relational_expression: dm_concat_expression (IS | EQ | NE | is_not_op)? MISSING
                        | dm_concat_expression (FROM | is_from_op | not_from_op) dm_concat_expression TO dm_concat_expression
                        | dm_concat_expression IN (FILE qualified_name | '(' dm_concat_expression (COMMA dm_concat_expression)* ')')
                        | dm_concat_expression (INCLUDES | EXCLUDES) dm_concat_expression (AND dm_concat_expression)*
                        | dm_concat_expression dm_relational_op (dm_concat_expression (OR dm_concat_expression)*)
                        | dm_concat_expression
                        ;

dm_relational_op: EQ | NE | LE | GE | LT | GT | CONTAINS | OMITS | LIKE | EXCEEDS
                | IS
                | is_not_op
                | is_less_op
                | is_more_op
                | is_greater_op
                | NOT LIKE | NOT SUB_OP LIKE
                ;

is_not_op: IS_NOT | IS NOT | IS SUB_OP NOT;
is_from_op: IS_FROM | IS FROM | IS SUB_OP FROM;
not_from_op: NOT_FROM | NOT FROM | NOT SUB_OP FROM;
is_less_op: IS_LESS_THAN | IS LESS THAN | IS SUB_OP LESS THAN;
is_more_op: IS_MORE_THAN | IS MORE_KW THAN | IS SUB_OP MORE_KW THAN;
is_greater_op: IS_GREATER_THAN | IS GREATER THAN | IS SUB_OP GREATER THAN;

dm_concat_expression: dm_additive_expression (CONCAT dm_additive_expression)*;

dm_additive_expression: dm_multiplicative_expression ((ADD_OP | SUB_OP) dm_multiplicative_expression)*;

dm_multiplicative_expression: dm_unary_expression ((MUL | SLASH) dm_unary_expression)*;

dm_unary_expression: (ADD_OP | SUB_OP) dm_unary_expression
                   | dm_primary;

dm_primary: NUMBER
          | dm_float
          | qualified_name '(' (dm_expression (COMMA dm_expression)*)? ')'
          | qualified_name
          | amper_var
          | STRING
          | '(' dm_expression ')';

dm_float: NUMBER DOT NUMBER;

amper_var: AMPER_VAR;

table_file: TABLE FILE qualified_name;

verb_command: verb (field_list | asterisk);

verb: PRINT | SUM | LIST | COUNT | WRITE | ADD;

field_list: THE? field_or_prefixed (field_separator? field_or_prefixed)*;

field_separator: COMMA | AND THE | AND | THE;

field_or_prefixed: (prefix_operator DOT)* field;

field: qualified_name (SLASH format_name)? as_phrase?;

as_phrase: AS STRING;

asterisk: '*';

by_command: RANKED? BY sort_options? field summarize_command? NOPRINT?;

across_command: ACROSS sort_options? field (ACROSS_TOTAL as_phrase?)? NOPRINT?;

sort_options: (HIGHEST | LOWEST | TOP | BOTTOM) NUMBER?
            | NUMBER;

where_command: WHERE TOTAL? dm_logical_expression SEMI?;

heading_command: HEADING CENTER? STRING+;

footing_command: FOOTING CENTER? STRING+;

on_command: ON TABLE on_table_options
          | ON qualified_name on_field_options;

on_table_options: (SUBHEAD | SUBFOOT) CENTER? STRING+
                | COLUMN_TOTAL_KW
                | ROW_TOTAL_KW
                | ACROSS_TOTAL (SLASH format_name)? as_phrase? qualified_name?
                | output_command
                | summarize_command
                | recap_command
                | set_command
                | SET STYLE asterisk (layout_statement)* ENDSTYLE?;

on_field_options: (SUBHEAD | SUBFOOT) CENTER? STRING+
                | summarize_command
                | recap_command;

summarize_command: (SUBTOTAL | SUB_TOTAL | SUMMARIZE | RECOMPUTE) (summarize_options? (field as_phrase? | as_phrase) | summarize_options)?;

summarize_options: ROLL_DOT (prefix_operator DOT)* | (prefix_operator DOT)+;

output_command: (HOLD | PCHOLD | SAVE | SAVB) (AS qualified_name)? (FORMAT (NAME | verb))?;

end_command: END;

qualified_name: identifier (DOT identifier)*;

identifier: NAME
          | prefix_operator
          | IS | CONTAINS | OMITS | LIKE | TOTAL | MISSING | INCLUDES | EXCLUDES | EXCEEDS | ALL
          | LESS | THAN | MORE_KW | GREATER
          | OFF | ON
          | RECAP | INDENT | ACROSS_TOTAL
          | COMPOUND | LAYOUT | SECTION | PAGELAYOUT | COMPONENT | MERGE | ORIENTATION
          | LANDSCAPE | PORTRAIT | TYPE | POSITION | DIMENSION | STYLE | ENDSTYLE
          ;

prefix_operator: AVE | MIN | MAX | CNT | FST | LST | ASQ | MDN | MDE | PCT | RPCT | RNK | DST | TOT | SUM | CT;

// Keywords
SET_DM: '-' [sS][eE][tT];
GOTO_DM: '-' [gG][oO][tT][oO];
REPEAT_DM: '-' [rR][eE][pP][eE][aA][tT];
IF_DM: '-' [iI][fF];
TYPE_DM: '-' [tT][yY][pP][eE];
INCLUDE_DM: '-' [iI][nN][cC][lL][uU][dD][eE];
RUN_DM: '-' [rR][uU][nN];
EXIT_DM: '-' [eE][xX][iI][tT];

SUB_TOTAL: [sS][uU][bB] '-' [tT][oO][tT][aA][lL];
COLUMN_TOTAL_KW: [cC][oO][lL][uU][mM][nN] '-' [tT][oO][tT][aA][lL];
ROW_TOTAL_KW: [rR][oO][wW] '-' [tT][oO][tT][aA][lL];
ACROSS_TOTAL: [aA][cC][rR][oO][sS][sS] '-' [tT][oO][tT][aA][lL];

IS_NOT: [iI][sS] '-' [nN][oO][tT];
IS_FROM: [iI][sS] '-' [fF][rR][oO][mM];
NOT_FROM: [nN][oO][tT] '-' [fF][rR][oO][mM];
IS_LESS_THAN: [iI][sS] '-' [lL][eE][sS][sS] '-' [tT][hH][aA][nN];
IS_MORE_THAN: [iI][sS] '-' [mM][oO][rR][eE] '-' [tT][hH][aA][nN];
IS_GREATER_THAN: [iI][sS] '-' [gG][rR][eE][aA][tT][eE][rR] '-' [tT][hH][aA][nN];

LABEL_DM: '-' [a-zA-Z_] [a-zA-Z0-9_]*;
COMMENT_DM: '-*' ~[\r\n]* -> skip;

TABLE: [tT][aA][bB][lL][eE];
FILE: [fF][iI][lL][eE];
DEFINE: [dD][eE][fF][iI][nN][eE];
COMPUTE: [cC][oO][mM][pP][uU][tT][eE];
END: [eE][nN][dD];

PRINT: [pP][rR][iI][nN][tT];
SUM: [sS][uU][mM];
LIST: [lL][iI][sS][tT];
COUNT: [cC][oO][uU][nN][tT];
WRITE: [wW][rR][iI][tT][eE];
ADD: [aA][dD][dD];

BY: [bB][yY];
ACROSS: [aA][cC][rR][oO][sS][sS];
WHERE: [wW][hH][eE][rR][eE];
GOTO: [gG][oO][tT][oO];
EQ: [eE][qQ] | '=';
NE: [nN][eE] | '!=';
LT: [lL][tT] | '<';
GT: [gG][tT] | '>';
LE: [lL][eE] | '<=';
GE: [gG][eE] | '>=';
RANKED: [rR][aA][nN][kK][eE][dD];
JOIN: [jJ][oO][iI][nN];
CLEAR: [cC][lL][eE][aA][rR];
LEFT: [lL][eE][fF][tT];
OUTER: [oO][uU][tT][eE][rR];
SET: [sS][eE][tT];
OFF: [oO][fF][fF];
WHILE: [wW][hH][iI][lL][eE];
UNTIL: [uU][nN][tT][iI][lL];
TIMES: [tT][iI][mM][eE][sS];
FOR: [fF][oO][rR];
FROM: [fF][rR][oO][mM];
TO: [tT][oO];
STEP: [sS][tT][eE][pP];
HIGHEST: [hH][iI][gG][hH][eE][sS][tT];
LOWEST: [lL][oO][wW][eE][sS][tT];
TOP: [tT][oO][pP];
BOTTOM: [bB][oO][tT][tT][oO][mM];
NOPRINT: [nN][oO][pP][rR][iI][nN][tT];

AS: [aA][sS];
IN: [iI][nN];
ALL: [aA][lL][lL];
CONTAINS: [cC][oO][nN][tT][aA][iI][nN][sS];
OMITS: [oO][mM][iI][tT][sS];
LIKE: [lL][iI][kK][eE];
IS: [iI][sS];
TOTAL: [tT][oO][tT][aA][lL];
MISSING: [mM][iI][sS][sS][iI][nN][gG];
INCLUDES: [iI][nN][cC][lL][uU][dD][eE][sS];
EXCLUDES: [eE][xX][cC][lL][uU][dD][eE][sS];
EXCEEDS: [eE][xX][cC][eE][eE][dD][sS];

LESS: [lL][eE][sS][sS];
THAN: [tT][hH][aA][nN];
MORE_KW: [mM][oO][rR][eE];
GREATER: [gG][rR][eE][aA][tT][eE][rR];

THE: [tT][hH][eE];
AND: [aA][nN][dD];
OR: [oO][rR];
NOT: [nN][oO][tT];
THEN: [tT][hH][eE][nN];
ELSE: [eE][lL][sS][eE];
IF: [iI][fF];

HEADING: [hH][eE][aA][dD][iI][nN][gG];
FOOTING: [fF][oO][oO][tT][iI][nN][gG];
ON: [oO][nN];
SUBHEAD: [sS][uU][bB][hH][eE][aA][dD];
SUBFOOT: [sS][uU][bB][fF][oO][oO][tT];
CENTER: [cC][eE][nN][tT][eE][rR];

RECAP: [rR][eE][cC][aA][pP];
INDENT: [iI][nN][dD][eE][nN][tT];

COMPOUND: [cC][oO][mM][pP][oO][uU][nN][dD];
LAYOUT: [lL][aA][yY][oO][uU][tT];
SECTION: [sS][eE][cC][tT][iI][oO][nN];
PAGELAYOUT: [pP][aA][gG][eE][lL][aA][yY][oO][uU][tT];
COMPONENT: [cC][oO][mM][pP][oO][nN][eE][nN][tT];
MERGE: [mM][eE][rR][gG][eE];
ORIENTATION: [oO][rR][iI][eE][nN][tT][aA][tT][iI][oO][nN];
LANDSCAPE: [lL][aA][nN][dD][sS][cC][aA][pP][eE];
PORTRAIT: [pP][oO][rR][tT][rR][aA][iI][tT];
TYPE: [tT][yY][pP][eE];
POSITION: [pP][oO][sS][iI][tT][iI][oO][nN];
DIMENSION: [dD][iI][mM][eE][nN][sS][iI][oO][nN];
STYLE: [sS][tT][yY][lL][eE];
ENDSTYLE: [eE][nN][dD][sS][tT][yY][lL][eE];
REPORT: [rR][eE][pP][oO][rR][tT];

SUBTOTAL: [sS][uU][bB][tT][oO][tT][aA][lL];
SUMMARIZE: [sS][uU][mM][mM][aA][rR][iI][zZ][eE];
RECOMPUTE: [rR][eE][cC][oO][mM][pP][uU][tT][eE];
HOLD: [hH][oO][lL][dD];
PCHOLD: [pP][cC][hH][oO][lL][dD];
SAVE: [sS][aA][vV][eE];
SAVB: [sS][aA][vV][bB];
FORMAT: [fF][oO][rR][mM][aA][tT];
ROLL_DOT: [rR][oO][lL][lL] '.';

AVE: [aA][vV][eE];
MIN: [mM][iI][nN];
MAX: [mM][aA][xX];
CNT: [cC][nN][tT];
FST: [fF][sS][tT];
LST: [lL][sS][tT];
ASQ: [aA][sS][qQ];
MDN: [mM][dD][nN];
MDE: [mM][dD][eE];
PCT: [pP][cC][tT];
RPCT: [rR][pP][cC][tT];
RNK: [rR][nN][kK];
DST: [dD][sS][tT];
TOT: [tT][oO][tT];
CT: [cC][tT];

DOT: '.';
COMMA: ',';
SEMI: ';';
SLASH: '/';
MUL: '*';
ADD_OP: '+';
SUB_OP: '-';
CONCAT: '||' | '|';
DOLLAR: '$';

NUMBER: [0-9]+;

STRING: '\'' ~[']* '\''
      | '"' ~["]* '"';

AMPER_VAR: ('&&' | '&') [a-zA-Z_] [a-zA-Z0-9_]*;

NAME: [a-zA-Z_] [a-zA-Z0-9_]*;

WS: [ \t\r\n]+ -> skip;

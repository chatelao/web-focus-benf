grammar WebFocusReport;

start: (request | dm_command)* EOF;

request: table_file (verb_command | by_command | across_command | where_command | heading_command | footing_command | on_command | dm_command)* end_command;

dm_command: dm_set
          | dm_goto
          | dm_label
          | dm_if
          | dm_type
          | dm_include
          | dm_run
          | dm_exit
          ;

dm_set: SET_DM amper_var EQ dm_expression SEMI?;

dm_goto: GOTO_DM NAME SEMI?;

dm_label: LABEL_DM;

dm_if: IF_DM dm_logical_expression (THEN GOTO? | GOTO) NAME (ELSE GOTO NAME)? SEMI?;

dm_type: TYPE_DM (dm_term)* SEMI?;

dm_include: INCLUDE_DM qualified_name SEMI?;

dm_run: RUN_DM SEMI?;

dm_exit: EXIT_DM SEMI?;

dm_expression: dm_term (CONCAT dm_term)*
             | IF dm_logical_expression THEN dm_expression ELSE dm_expression;

dm_term: qualified_name
       | amper_var
       | NUMBER
       | STRING;

amper_var: AMPER_VAR;

dm_logical_expression: dm_logical_expression (AND | OR) dm_logical_expression
                     | NOT dm_logical_expression
                     | '(' dm_logical_expression ')'
                     | dm_term dm_relational_op dm_term;

dm_relational_op: EQ | NE | LE | GE | LT | GT;

table_file: TABLE FILE qualified_name;

verb_command: verb (field_list | asterisk);

verb: PRINT | SUM | LIST | COUNT | WRITE | ADD;

field_list: THE? field_or_prefixed (field_separator? field_or_prefixed)*;

field_separator: COMMA | AND THE | AND | THE;

field_or_prefixed: (prefix_operator DOT)* field;

field: qualified_name as_phrase?;

as_phrase: AS STRING;

asterisk: '*';

by_command: RANKED? BY sort_options? field summarize_command? NOPRINT?;

across_command: ACROSS sort_options? field NOPRINT?;

sort_options: (HIGHEST | LOWEST | TOP | BOTTOM) NUMBER?
            | NUMBER;

where_command: WHERE qualified_name EQ (qualified_name | NUMBER | STRING | amper_var);

heading_command: HEADING CENTER? STRING+;

footing_command: FOOTING CENTER? STRING+;

on_command: ON TABLE on_table_options
          | ON qualified_name on_field_options;

on_table_options: (SUBHEAD | SUBFOOT) CENTER? STRING+
                | COLUMN_TOTAL
                | ROW_TOTAL
                | output_command
                | summarize_command;

on_field_options: (SUBHEAD | SUBFOOT) CENTER? STRING+
                | summarize_command;

summarize_command: (SUBTOTAL | SUB_TOTAL | SUMMARIZE | RECOMPUTE) (summarize_options? (field as_phrase? | as_phrase) | summarize_options)?;

summarize_options: ROLL_DOT (prefix_operator DOT)* | (prefix_operator DOT)+;

output_command: (HOLD | PCHOLD | SAVE | SAVB) (AS qualified_name)? (FORMAT (NAME | verb))?;

end_command: END;

qualified_name: NAME (DOT NAME)*;

prefix_operator: AVE | MIN | MAX | CNT | FST | LST | ASQ | MDN | MDE | PCT | RPCT | RNK | DST | TOT | SUM | CT;

// Keywords
SET_DM: '-' [sS][eE][tT];
GOTO_DM: '-' [gG][oO][tT][oO];
IF_DM: '-' [iI][fF];
TYPE_DM: '-' [tT][yY][pP][eE];
INCLUDE_DM: '-' [iI][nN][cC][lL][uU][dD][eE];
RUN_DM: '-' [rR][uU][nN];
EXIT_DM: '-' [eE][xX][iI][tT];
LABEL_DM: '-' [a-zA-Z_] [a-zA-Z0-9_]*;
COMMENT_DM: '-*' ~[\r\n]* -> skip;

TABLE: [tT][aA][bB][lL][eE];
FILE: [fF][iI][lL][eE];
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
HIGHEST: [hH][iI][gG][hH][eE][sS][tT];
LOWEST: [lL][oO][wW][eE][sS][tT];
TOP: [tT][oO][pP];
BOTTOM: [bB][oO][tT][tT][oO][mM];
NOPRINT: [nN][oO][pP][rR][iI][nN][tT];

AS: [aA][sS];
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

SUBTOTAL: [sS][uU][bB][tT][oO][tT][aA][lL];
SUB_TOTAL: [sS][uU][bB] '-' [tT][oO][tT][aA][lL];
SUMMARIZE: [sS][uU][mM][mM][aA][rR][iI][zZ][eE];
RECOMPUTE: [rR][eE][cC][oO][mM][pP][uU][tT][eE];
COLUMN_TOTAL: [cC][oO][lL][uU][mM][nN] '-' [tT][oO][tT][aA][lL];
ROW_TOTAL: [rR][oO][wW] '-' [tT][oO][tT][aA][lL];
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
CONCAT: '||' | '|';

NUMBER: [0-9]+;

STRING: '\'' ~[']* '\''
      | '"' ~["]* '"';

AMPER_VAR: ('&&' | '&') [a-zA-Z_] [a-zA-Z0-9_]*;

NAME: [a-zA-Z_] [a-zA-Z0-9_]*;

WS: [ \t\r\n]+ -> skip;

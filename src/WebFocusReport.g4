grammar WebFocusReport;

start: request EOF;

request: table_file (verb_command | by_command | across_command)* end_command;

table_file: TABLE FILE qualified_name;

verb_command: verb (field_list | asterisk);

verb: PRINT | SUM | LIST | COUNT | WRITE | ADD;

field_list: THE? field_or_prefixed (field_separator? field_or_prefixed)*;

field_separator: COMMA | AND THE | AND | THE;

field_or_prefixed: (prefix_operator DOT)* field;

field: qualified_name as_phrase?;

as_phrase: AS STRING;

asterisk: '*';

by_command: RANKED? BY sort_options? field NOPRINT?;

across_command: ACROSS sort_options? field NOPRINT?;

sort_options: (HIGHEST | LOWEST | TOP | BOTTOM) NUMBER?
            | NUMBER;

end_command: END;

qualified_name: NAME (DOT NAME)*;

prefix_operator: AVE | MIN | MAX | CNT | FST | LST | ASQ | MDN | MDE | PCT | RPCT | RNK | DST | TOT | SUM | CT;

// Keywords
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
RANKED: [rR][aA][nN][kK][eE][dD];
HIGHEST: [hH][iI][gG][hH][eE][sS][tT];
LOWEST: [lL][oO][wW][eE][sS][tT];
TOP: [tT][oO][pP];
BOTTOM: [bB][oO][tT][tT][oO][mM];
NOPRINT: [nN][oO][pP][rR][iI][nN][tT];

AS: [aA][sS];
THE: [tT][hH][eE];
AND: [aA][nN][dD];

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

NUMBER: [0-9]+;

STRING: '\'' ~[']* '\''
      | '"' ~["]* '"';

NAME: [a-zA-Z_] [a-zA-Z0-9_]*;

// Ensure keywords are not matched as NAME
// Note: In ANTLR4, lexer rules are matched in order.
// Since keywords are defined before NAME, they will be matched as keywords.
// However, to be extra safe and follow the requirement to "exclude",
// we rely on the order or use a gated semantic predicate if needed.
// For now, order is sufficient.

WS: [ \t\r\n]+ -> skip;

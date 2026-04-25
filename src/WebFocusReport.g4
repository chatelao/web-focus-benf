grammar WebFocusReport;

start: request EOF;

request: table_file verb_command* end_command;

table_file: TABLE FILE qualified_name;

verb_command: verb field_list;

verb: PRINT | SUM;

field_list: field (COMMA? field)*;

field: qualified_name;

end_command: END;

qualified_name: NAME (DOT NAME)*;

TABLE: [tT][aA][bB][lL][eE];
FILE: [fF][iI][lL][eE];
END: [eE][nN][dD];
PRINT: [pP][rR][iI][nN][tT];
SUM: [sS][uU][mM];

DOT: '.';
COMMA: ',';

NAME: [a-zA-Z_] [a-zA-Z0-9_]*;

WS: [ \t\r\n]+ -> skip;

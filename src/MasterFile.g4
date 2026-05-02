grammar MasterFile;

start: item* EOF;

item: declaration
    | TERMINATOR
    ;

declaration: file_decl
           | segment_decl
           | field_decl
           | dimension_decl
           | hierarchy_decl
           | define_decl
           | compute_decl
           | variable_decl
           | other_decl
           | TERMINATOR
           ;

// @category Metadata
file_decl: FILENAME_KW (EQUALS | COMMA)? value (COMMA attr_val)* COMMA? TERMINATOR?;
// @category Metadata
segment_decl: SEGNAME_KW (EQUALS | COMMA)? value (COMMA attr_val)* COMMA? TERMINATOR?;
// @category Metadata
field_decl: FIELDNAME_KW (EQUALS | COMMA)? value (COMMA attr_val)* COMMA? TERMINATOR?;
// @category Metadata
dimension_decl: DIMENSION_KW (EQUALS | COMMA)? value (COMMA attr_val)* COMMA? TERMINATOR?;
// @category Metadata
hierarchy_decl: HIERARCHY_KW (EQUALS | COMMA)? value (COMMA attr_val)* COMMA? TERMINATOR?;
variable_decl: VARIABLE_KW (attr_val | COMMA)* TERMINATOR?;

define_decl: DEFINE_KW name_format EQUALS expression SEMICOLON (COMMA attr_val)* COMMA? TERMINATOR?;
compute_decl: COMPUTE_KW name_format EQUALS expression SEMICOLON (COMMA attr_val)* COMMA? TERMINATOR?;

other_decl: ATTR EQUALS value (COMMA attr_val)* COMMA? TERMINATOR?;

// @inline
attr_val: assignment | value;
// @inline
assignment: ATTR EQUALS value;

// @inline
name_format: value (SLASH value)?;

// @inline
value: STRING | ATTR | UNQUOTED_VALUE;

// @internal
expression: expression_part+;
// @internal
expression_part: ATTR | UNQUOTED_VALUE | STRING | COMMA | EQUALS | SLASH | FILENAME_KW | SEGNAME_KW | FIELDNAME_KW | VARIABLE_KW | DEFINE_KW | COMPUTE_KW ;

FILENAME_KW: [fF][iI][lL][eE][nN][aA][mM][eE] | [fF][iI][lL][eE];
SEGNAME_KW: [sS][eE][gG][nN][aA][mM][eE] | [sS][eE][gG][mM][eE][nN][tT];
FIELDNAME_KW: [fF][iI][eE][lL][dD][nN][aA][mM][eE] | [fF][iI][eE][lL][dD];
DIMENSION_KW: [dD][iI][mM][eE][nN][sS][iI][oO][nN];
HIERARCHY_KW: [hH][iI][eE][rR][aA][rR][cC][hH][yY];
VARIABLE_KW: [vV][aA][rR][iI][aA][bB][lL][eE];
DEFINE_KW: [dD][eE][fF][iI][nN][eE];
COMPUTE_KW: [cC][oO][mM][pP][uU][tT][eE];

// @internal
TERMINATOR: '$' ~[\r\n]* (WS* '$' ~[\r\n]*)*;

COMMA: ',';
EQUALS: '=';
SLASH: '/';
SEMICOLON: ';';

ATTR: [a-zA-Z_] [a-zA-Z0-9_.]*;
UNQUOTED_VALUE: [a-zA-Z0-9_./&%#@<>:*\-()+]+;
STRING: '\'' ~'\''* '\'' | '"' ~'"'* '"';

WS: [ \t\r\n]+ -> skip;

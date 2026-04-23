Appendix C

Table Syntax Summary and Limits

This appendix summarizes WebFOCUS reporting commands and options.

In this appendix:

TABLE Syntax Summary

TABLEF Syntax Summary

MATCH Syntax Summary

FOR Syntax Summary

TABLE Limits

Creating Reports With TIBCO® WebFOCUS Language

 1985

TABLE Syntax Summary

TABLE Syntax Summary

The syntax of a TABLE request is:

DEFINE FILE filename    CLEAR|ADD
tempfield  [/format] [{DEFCENT|DFC} {cc|19} {YRTHRESH|YRT} {[-]yy|0}]
    [MISSING {ON|OFF} [NEEDS] {SOME|ALL} [DATA]]
    [(GEOGRAPHIC_ROLE = georole)] [WITH realfield]
    [TITLE 'line1[,line2 ...']]
  [DESCRIPTION 'description'] = expression;
tempfield  [/format]    REDEFINES qualifier.fieldname = expression;
.
.
.
END
TABLE  FILE  filename
HEADING  [CENTER]
"text"
{display_command}   [SEG.] field   [/R|/L|/C]   [/format]
{display_command}   [prefixop.] [field]  [/R|/L|/C]  [/format]
  [NOPRINT|AS 'title1,...,title5']   [AND|OVER]   [obj2...obj1024]
      [WITHIN field]   [IN [+]n]
COMPUTE field  [/format] [(GEOGRAPHIC_ROLE = georole)] =
        expression; [AS 'title,...,title5']  [IN [+]n]
[AND]  ROW-TOTAL      [/R|/L|/C]    [/format][AS 'name']
[AND]  COLUMN-TOTAL   [/R|/L|/C]    [AS 'name']
ACROSS  [HIGHEST]  sortfieldn       [IN-GROUPS-OF qty]
    [NOPRINT|  AS 'title1,...,title5']
BY  [HIGHEST]  sortfieldn           [IN-GROUPS-OF qty]
    [NOPRINT|  AS 'title1,...,title5']
BY  [HIGHEST|LOWEST{n}]  TOTAL  [prefix_operator]  {field|code_value}
RANKED [AS 'name'] BY {TOP|HIGHEST|LOWEST} [n] field
       [PLUS OTHERS AS 'othertext']
      [IN-GROUPS-OF qty [TILES [TOP m]] [AS 'heading']]
      [NOPRINT|AS 'title1,...,title5']

{BY|ACROSS} sortfield IN-RANGES-OF value [TOP limit]
ON   sfld  option1  [AND]  option2   [WHEN expression;...]
ON   sfld  RECAP   fld1  [/fmt] = FORECAST (fld2, intvl, npredct,
  '{MOVAVE|EXPAVE}',npnt);

ON sfld RECAP fld1[/fmt] = FORECAST(fld2, interval, npredict, 'DOUBLEXP',
   npoint1, npoint2);

ON sfld RECAP fld1[/fmt] = FORECAST(fld2, interval, npredict, 'SEASONAL',
   nperiod, npoint1, npoint2, npoint3);

ON   sfld  RECAP   fld1  [/fmt] = FORECAST (fld2, intvl, npredct,
'REGRESS');

1986

C. Table Syntax Summary and Limits

ON {sortfield|TABLE} RECAP y[/fmt] = REGRESS(n, x1, [x2, [x3,]] z);
ON   sfld  RECAP   fld1  [/fmt] = FORECAST (infield, interval, npredict,
  'DOUBLEXP',npoint, npoint2);
ON  sfld   RECAP   fld1  [/fmt] = FORECAST (infield, interval, npredict,
  'SEASONAL', nperiod, npoint, npoint2, npoint3);{BY|ON} fieldname
SUBHEAD
  [NEWPAGE]
"text"

{BY|ON} fieldname SUBFOOT [WITHIN] [MULTILINES][NEWPAGE]
"text" [<prefop.fieldname ... ]"        [WHEN expression;]

WHERE   [TOTAL]  expression
WHERE   {RECORDLIMIT|READLIMIT}  EQ  n
IF      [TOTAL]  field relation  value  [OR value...]
WHERE_GROUPED expression
ON TABLE  SET parameter value
ON TABLE  HOLD [VIA program][AS name] [FORMAT format] [DATASET dataset]
               [MISSING {ON|OFF}] [PERSISTENCE {STAGE|PERMANENT}]
ON TABLE  {PCHOLD|SAVE|SAVB} [AS name] [FORMAT format]  [MISSING {ON|OFF}]
ON TABLE  NOTOTAL
ON TABLE  COLUMN-TOTAL [/R|/L|/C]  [AS 'name']  fieldname
ON TABLE  {ROW-TOTAL|ACROSS-TOTAL}[/R|/L|/C][format] [AS 'name'] fldname
{BY|ON}  sfld [AS 'text1']   {SUBTOTAL|SUB-TOTAL|SUMMARIZE|RECOMPUTE}
  [MULTILINES] [pref. ] [field1 [pref. ] field2 ...] [AS 'text2']
  [WHEN expression;]
{ACROSS|ON}  sfld [AS 'text1'] {SUBTOTAL|SUB-TOTAL|SUMMARIZE|RECOMPUTE}
   [AS 'text2']  [COLUMNS c1 [AND c2 ...]]
ON  TABLE {SUBTOTAL|SUB-TOTAL|SUMMARIZE|RECOMPUTE}
  [pref. ] [field1 [pref. ] field2 ...] [AS 'text2']
FOOTING  [CENTER]  [BOTTOM]
"text"
MORE
FILE  file2
   [IF field relation value [OR value...]|WHERE expression]
{END|RUN|QUIT}

Hierarchical Reporting Syntax Summary

SUM [FROLL.]measure_field ...
BY hierarchy_field [HIERARCHY [WHEN expression_using_hierarchy_fields;]
  [SHOW [TOP|UP n] [TO {BOTTOM|DOWN m}] [byoption [WHEN condition] ...] ]
[WHERE expression_using_dimension_data]
[ON hierarchy_field HIERARCHY [WHEN expression_using_hierarchy_fields;]
  [SHOW [TOP|UP n] [TO BOTTOM|DOWN m] [byoption [WHEN condition] ...]]

Creating Reports With TIBCO® WebFOCUS Language

 1987

TABLEF Syntax Summary

TABLEF Syntax Summary

The syntax of a TABLEF request is:

TABLEF FILE filename
HEADING [CENTER]
"text"

{display_command}  [SEG.]field  [/R|/L|/C]  [/format]
{display_command}  [prefixop.][field] [/R|/L|/C] [/format]
    [NOPRINT|AS 'title1,...,title5']    [AND|OVER]    [obj2...obj495]
    [IN n]

COMPUTE field [/format]=expression; [AS 'title1,...title5']
[AND] ROW-TOTAL [AND] COLUMN-TOTAL

BY [HIGHEST] keyfieldn [NOPRINT]

ON keyfield option1 [AND] option2...

WHERE [TOTAL] expression

IF [TOTAL] field relation value [OR value...]

ON TABLE SET parameter value

ON TABLE HOLD [VIA program] [AS name] [FORMAT format]  [MISSING {ON|OFF}]
ON TABLE PCHOLD             [AS name] [FORMAT format]  [MISSING {ON|OFF}]
ON TABLE SAVE               [AS name] [FORMAT format]  [MISSING {ON|OFF}]
ON TABLE SAVB               [AS name] [FORMAT format]  [MISSING {ON|OFF}]

ON TABLE  NOTOTAL
ON TABLE  COLUMN-TOTAL fieldname
ON TABLE  ROW-TOTAL fieldname

 FOOTING [CENTER] [BOTTOM]
 "text"

{END|RUN|QUIT}

Note:

Prefix operators for TABLEF can be: AVE., ASQ., MAX., MIN., FST., LST., CNT., or SUM.

TABLEF requests cannot use:

Prefix operators DST., PCT., PCT.CNT., RPCT., and TOT.

Variables TABPAGENO, TABLASTPAGE, and BYLASTPAGE.

1988



C. Table Syntax Summary and Limits

SET SQUEEZE

Border styling.

ACROSS phrases.

WITHIN phrases.

RANKED BY phrases.

NOSPLIT.

Requests with multiple display commands (multi-verb requests).

MATCH Syntax Summary

The syntax of a MATCH request is:

MATCH FILE filename    (the OLD file) report request
BY field1 [AS sortfield]
MORE
FILE file3
subrequest
RUN
.
.
.
FILE filename2         (the NEW file) report request
BY field1 [AS sortfield1]
.
.
.
[AFTER MATCH HOLD [AS filename]  matchtype]
MORE
FILE file4
subrequest
END

where:

matchtype

Can be any of the following:

OLD

NEW

OLD-NOT-NEW

NEW-NOT-OLD

Creating Reports With TIBCO® WebFOCUS Language

 1989

FOR Syntax Summary

OLD-AND-NEW

OLD-OR-NEW

OLD-NOR-NEW

FOR Syntax Summary

The formal syntax of the FOR statement is:

FOR fieldname [NOPRINT]row [OVER row]
.
.
.
.
END

where:

row

Can be any of the following:

tag [OR tag...][options]
[fieldname]
DATA n,[n,....] $
DATA PICKUP [FROM filename] tag [LABEL label] [AS 'text']
RECAP name[/format]=expression;
BAR [AS 'character'] [OVER]
"text"
parentvalue {GET|WITH} CHILD[REN] [{n|ALL}] [ADD [m|ALL]]
   [AS {CAPTION|'text'}] [LABEL label]parentvalue ADD [{m|ALL}] [AS
{CAPTION|'text'}] [LABEL label]
PAGE-BREAK [OVER]

tag

Can be any of the following:

value [OR value...] value TO value

options

Can be any of the following:

1990




C. Table Syntax Summary and Limits

AS 'text'
[INDENT m]
NOPRINT
[LABEL label]
WHEN EXISTS
[POST [TO filename]]

TABLE Limits

The following limits apply to TABLE requests:

There is no limit to the number of verb objects in a TABLE request. However, an error can
occur if the report output format has a limit to the number of columns supported, the
operating system has a maximum record length that cannot fit all of the columns, or the
amount of memory needed to store the output is not available.

Number of verb objects referenced in a MATCH request: 495

Number of columns of report output: 1024

Total length of all fields in the request or in a single Master File: 256K

Total number of sort fields (combined BY and ACROSS): 128

An internal sort will be generated automatically under some circumstances, and these have
to be counted in the total. HOLD FORMAT FOCUS/XFOCUS will add FOCLIST as a BY field in
order to ensure uniqueness.

Maximum size of the output record: 256K (FORMAT/USAGE)

Maximum size of the output file: FOCUS partition 2GB, XFOCUS 32GB

Maximum size of internal expression representation of a single DEFINE, COMPUTE, -SET, or
WHERE phrase: 64K

The internal representation is generated in polish postfix notation, which is significantly
smaller than the entered expression. In addition, the constants in expressions (as in
DECODE or IF…THEN..ELSE conditions) are stored outside of the expression
representations, reducing the space requirement for the expression representation itself.

Maximum number of segments in a structure or file: 512.

This means that a total of 511 JOINs can be in effect at any one given time.

Note: FOCUS data sources are limited to 64 segments.

The maximum number of field pairs in a join is 128.

Creating Reports With TIBCO® WebFOCUS Language

 1991

TABLE Limits

Maximum size of Alphanumeric fields: 4K characters ( in UTF, this means 12K bytes)

Maximum number of display commands in a TABLE request: 64.

1992

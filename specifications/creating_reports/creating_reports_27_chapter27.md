Chapter27

Using SQL to Create Reports

SQL users can issue report requests that combine SQL statements with TABLE
formatting phrases to take advantage of a wide range of report preparation options.

These combined requests are supported through the SQL Translator, which converts
ANSI Level 2 SQL statements into executable FOCUS requests.

You can use the SQL Translator to retrieve and analyze FOCUS and DBMS data.

In this chapter:

Supported and Unsupported SQL Statements

Using SQL Translator Commands

SQL Translator Support for Date, Time, and Timestamp Fields

Index Optimized Retrieval

TABLEF Optimization

SQL INSERT, UPDATE, and DELETE Commands

Supported and Unsupported SQL Statements

SQL Translation Services is compliant with ANSI Level 2. This facility supports many, but not
all, SQL statements. The Reporting Server and specific RDBMS engines may also support the
alpha1 CONCAT alpha2 syntax. See Supported SQL Statements on page 1908 and
Unsupported SQL Statements on page 1909.

Many of the supported SQL statements are candidates for Dialect Translation. This feature
enables a server to route inbound SQL requests to SQL-capable subservers and data adapters
where possible. Dialect Translation avoids translation to the Reporting Server Data
Manipulation Language (DML), while maintaining data location transparency. It transforms a
standard SQL statement into one that can be processed by the destination SQL engine, while
preserving the semantic meaning of the statement.

Note: Because the SQL Translator is ANSI Level 2 compliant, some requests that worked in
prior releases may no longer work.

Creating Reports With TIBCO® WebFOCUS Language

 1907

Supported and Unsupported SQL Statements

Reference: Supported SQL Statements

SQL Translation Services supports the following:

SELECT, including SELECT ALL and SELECT DISTINCT.

CREATE TABLE. The following data types are supported for CREATE TABLE: REAL, DOUBLE
PRECISION, FLOAT, INTEGER, DECIMAL, CHARACTER, SMALLINT, DATE, TIME, and
TIMESTAMP.

INSERT, UPDATE, and DELETE for relational, IMS, and FOCUS data sources.

Equijoins and non-equijoins.

Outer joins, subject to certain restrictions. See SQL Joins on page 1913.

CREATE VIEW and DROP VIEW.

PREPARE and EXECUTE.

Delimited identifiers of table names and column names. Table and column names
containing embedded blanks or other special characters in the SELECT list should be
enclosed in double quotation marks.

Column names qualified by table names or by table tags.

The UNION [ALL], INTERSECT [ALL], and EXCEPT [ALL] operators.

Non-correlated subqueries for all requests in the WHERE predicate and in the FROM list.

Correlated subqueries for requests that are candidates for Dialect Translation to an RDBMS
that supports this feature. Note that correlated subqueries are not supported for FOCUS
and other non-relational data sources.

Numeric constants, literals, and expressions in the SELECT list.

Scalar functions for queries that are candidates for Dialect Translation if the RDBMS engine
supports the scalar function type. These include: ABS, CHAR, CHAR_LENGTH, CONCAT,
COUNTBY, DATE, DAY, DAYS, DECIMAL, EDIT, EXTRACT, FLOAT, HOUR, IF, INT, INTEGER,
LCASE, LENGTH, LOG, LTRIM, MICROSECOND, MILLISECOND, MINUTE, MONTH, POSITION,
RTRIM, SECOND, SQRT, SUBSTR (or SUBSTRING), TIME, TIMESTAMP, TRIM, VALUE,
UCASE, and YEAR.

The concatenation operator, '||', used with literals or alphanumeric columns.

The following aggregate functions: COUNT, MIN, MAX, SUM, and AVG.

1908

27. Using SQL to Create Reports

The following expressions can appear in conditions: CASE, NULLIF, and COALESCE.

Date, time, and timestamp literals of several different formats. See SQL Translator Support
for Date, Time, and Timestamp Fields on page 1921.

All requests that contain ANY, SOME, and ALL that do not contain =ALL, <>ANY, and
<>SOME.

=ALL, <>ANY, and <>SOME for requests that are candidates for Dialect Translation if the
RDBMS engine supports quantified subqueries.

The special registers USER, CURRENT_DATE, CURRENT_TIME, CURRENT_TIMESTAMP,
CURRENT_EDASQLVERSION, and CURRENT_TIMEZONE.

NULL and NOT NULL predicates.

LIKE and NOT LIKE predicates.

IN and NOT IN predicates.

Date and time arithmetic.

EXISTS and NOT EXISTS predicates.

GROUP BY clauses expressed using explicit column names, AS names, or column
positions.

ORDER BY clauses expressed using explicit column names or column numbers.

FOR FETCH ONLY feature to circumvent record locking.

Continental Decimal Notation (CDN) when the CDN variable is set.

National Language Support (NLS).

Reference: Unsupported SQL Statements

SQL Translation Services does not support the following:

More than 15 joins per SELECT. This limit is set by SQL. FOCUS supports up to 16 joins.

ALIAS names in Master Files and the use of formatting options to format output.

Unique truncations of column names.

Temporary defined columns. Permanent defined columns, defined in the Reporting Server
Dynamic Catalog or in the Master File, are supported.

Creating Reports With TIBCO® WebFOCUS Language

 1909

Using SQL Translator Commands

Correlated subqueries for DML Generation.

Reference: SQL Translator Reserved Words

The following words may not be used as field names in a Master File that is used with the SQL
Translator:

ALL

COUNT

SUM

MAX

MIN

AVG

CURRENT

DISTINCT

USER

Using SQL Translator Commands

The SQL command may be used to report from any supported data source or set of data
sources. Standard TABLE phrases for formatting reports can be appended to the SQL
statements to take advantage of a wide range of report preparation options.

Note: If you need to join data sources for your request, you have two options: use the JOIN
command before you issue any SQL statements, or use the WHERE predicate in the SQL
SELECT statement to join the required files dynamically. See SQL Joins on page 1913.

Syntax:

How to Use SQL Translator Commands

SQL
sql statement;
[ECHO|FILE]
[TABLE phrases]
END

where:

SQL

Is the SQL command identifier, which invokes the SQL Translator.

1910

27. Using SQL to Create Reports

Note: The SQL command components must appear in the order represented above.

sql statement

Is a supported SQL statement. The statement must be terminated by a semicolon (;). It
can continue for more than one line. See Supported SQL Statements on page 1908.

Within the SQL statement, field names are limited to 48 characters (an ANSI standard
Level 2 limitation). View names generated through the SQL CREATE VIEW statement are
limited to 18 characters and subqueries can be nested up to 15 levels deep. Correlated
subqueries are not supported by FOCUS and other non-relational data sources.

ECHO

Are optional debugging phrases that capture the generated TABLE request. These options
are placed after the SQL statement.

FILE [name]

Writes the translated TABLE phrases to the named procedure. If you do not supply a file
name, a default name is assigned when the request runs. The file is then deleted.

TABLE phrases

Are optional TABLE formatting phrases. See TABLE Formatting Phrases in SQL Requests on
page 1911.

END or QUIT

Is required to terminate the procedure.

Example:

Using SQL Translator Commands

The following request contains an SQL statement and TABLE formatting commands:

SQL
SELECT BODYTYPE, AVG(MPG), SUM(SALES)
FROM CAR
WHERE RETAIL_COST > 5000
GROUP BY BODYTYPE;
TABLE HEADING CENTER
"AVERAGE MPG AND TOTAL SALES PER BODYTYPE"
END

Reference: TABLE Formatting Phrases in SQL Requests

You can include TABLE formatting phrases in an SQL request, subject to the following rules:

Use TABLE formatting phrases with SELECT and UNION only.

Introduce the formatting phrases with the word TABLE.

Creating Reports With TIBCO® WebFOCUS Language

 1911

Using SQL Translator Commands

You may specify headings and footings, describe actions with an ON phrase, or use the ON
TABLE SET command. Additionally, you can use ON TABLE HOLD or ON TABLE PCHOLD to
create an extract file. You can also specify READLIMIT and RECORDLIMIT tests.

For details on headings and footings, see Using Headings, Footings, Titles, and Labels on
page 1517.

For details on ON TABLE HOLD or ON TABLE PCHOLD, see Saving and Reusing Your Report
Output on page 471.

You cannot specify additional display fields, ACROSS fields, WHERE or IF criteria (other
than READLIMIT or RECORDLIMIT tests), or calculated values. BY phrases are ignored.

The SQL SELECT Statement

The SQL SELECT statement translates into one or more TABLE PRINT or TABLE SUM
commands, depending on whether individual field display or aggregation is applied in the
request. See Displaying Report Data on page 39.

The SQL statement SELECT * translates to a PRINT of every field in the Master File, and uses
all of the fields of the Cartesian product. This is a quick way to display a file, provided it fits in
a reasonable number of screens for display, or provided you use ON TABLE HOLD or ON TABLE
PCHOLD to retain retrieved data in a file for reuse. See Saving and Reusing Your Report Output
on page 471.

SQL functions (such as COUNT, SUM, MAX, MIN, AVG) are supported in SELECT lists and
HAVING conditions. Expressions may be used as function arguments.

The function COUNT (*) translates to a count of the number of records produced by printing all
fields in the Master File. This is the same as counting all rows in the Cartesian product that
results from a SELECT on all fields.

Whenever possible, expressions in the SQL WHERE predicate are translated into corresponding
WHERE criteria in the TABLE request. Expressions in SELECT lists generate virtual fields. The
SQL HAVING clauses also translate into corresponding WHERE TOTAL criteria in the TABLE
request. The SQL LIKE operator is translated directly into the corresponding LIKE operator in
the WHERE criteria of the TABLE request. For details on record selection in TABLE requests,
see Selecting Records for Your Report on page 217.

Only subqueries based on equality, when the WHERE expression is compared to a subquery by
using an equal (=) sign, are supported. For example: WHERE field = (SELECT ...).

1912

27. Using SQL to Create Reports

The SQL UNION operator translates to a TABLE request that creates a HOLD file for each data
source specified, followed by a MATCH command with option HOLD OLD-OR-NEW, which
combines records from both the first (old) data source and the second (new) data source. See
Merging Data Sources on page 1155.

For related information, see Supported SQL Statements on page 1908 and How to Use SQL
Translator Commands on page 1910.

Using the SQL SELECT Statement Without a FROM Clause

SELECT without a FROM clause is supported for returning a one-row answer set consisting of
one or more constant values. No Master File is needed for issuing this type of SELECT. One
use for this syntax is to test functions. For example, the following SQL SELECT returns a literal
value and the results of two function calls:

SQL
SELECT 'MOD' AS FUNCTION, MOD(6,3) AS MOD1, MOD(5,3) AS MOD2;
TABLE
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

The output is shown in the following image.

SQL Joins

When performing SQL joins, the formats of the joined fields must be the same. Join fields
need not be indexed, and non-equijoins are supported.

Recursive, outer, and inner joins are supported. Inner join is the default.

Syntax:

How to Create an Inner Join

Two syntax variations are supported for inner joins.

Variation 1

SQL
SELECT fieldlist FROM file1 [alias1], file2 [alias2]
[WHERE where_condition];
END

Creating Reports With TIBCO® WebFOCUS Language

 1913

Using SQL Translator Commands

Variation 2

SQL
SELECT fieldlist FROM file1 [alias1] INNER JOIN file2 [alias2]
ON join_condition [INNER JOIN ...]
[WHERE where_condition];
END

where:

fieldlist

Identifies which fields are retrieved from which data sources.

Joined fields in the SQL WHERE predicate must be qualified if the names are not unique.
Specify them with their corresponding file names or file aliases. For example:

{file1|alias1}.field1, {file2|
alias2}.field2

FROM

Introduces the data sources to be joined.

file1, file2

Are the data sources to be joined.

alias1, alias2

Are optional alternate names for the data sources to be joined.

where_condition

Is an optional selection condition for the joined answer set. Joined rows that do not satisfy
this condition are eliminated from the returned answer set. If omitted in Variation 1, the
answer set is the Cartesian product of the two data sources.

join_condition

Is the join condition.

1914

27. Using SQL to Create Reports

Syntax:

How to Create an Outer Join

SQL
SELECT fieldlist FROM file1 {LEFT|RIGHT|FULL} JOIN file2
ON join_condition [{LEFT|RIGHT|FULL} JOIN ...]
WHERE where_condition
END

where:

fieldlist

Identifies which fields are to be retrieved from which data sources.

Joined fields in the SQL WHERE predicate must be qualified if the names are not unique.
Specify them with their corresponding file names or file aliases. For example:

{file1|alias1}.field1, {file2|
alias2}.field2

FROM

Introduces the data sources to be joined.

file1, file2

Are the data sources to be joined.

alias1, alias2

Are optional alternate names for the data sources to be joined.

join_condition

Is the join condition. The condition must specify equality. For example, T1.A=T2.B.

where_condition

Is an optional selection condition for the joined answer set. Joined rows that do not satisfy
this condition are eliminated from the returned answer set.

Reference: Join Name Assignments From the SQL Translator

Joins issued by the SQL Translator are assigned names in the format:

SQLJNMnn

where:

SQLJNM

Is the SQL Translator join prefix.

Creating Reports With TIBCO® WebFOCUS Language

 1915

Using SQL Translator Commands

nn

Is a number between 01 and 16 assigned in the order in which the joins are created
(FOCUS supports a maximum of 16 joins). The first join has the AS name SQLJNM01, the
second join is named SQLJNM02, and so on, up to SQLJNM16.

All joins are automatically created and cleared by the SQL Translator. No user-specified joins
are affected.

Example:

Using Qualified Field Names in SQL Joins

In the following statement, T.A and U.B are qualified field names:

SQL
 SELECT T.A, T.B
 FROM T, U
 WHERE T.A = U.B;
END

Example:

Using Recursive SQL Joins

In the following statement, A and B are aliases for the same data source, CAR. The output
from CAR is pairs of B values that have the same A values:

SQL
   SELECT A.SEATS, B.SEATS
   FROM CAR A, CAR B
   WHERE A.MODEL = B.MODEL;
END

Note that all field names in the SELECT clause must be unique or qualified.

Example:

Using SQL Full Outer Joins

In the following statement, B, C, and D are aliases for different data sources:

SQL
SELECT
       B.FIELD1 AS B_FIELD1, B.FIELD2 AS B_FIELD2,
       D.FIELD1 AS D_FIELD1, D.FIELD2 AS D_FIELD2
FROM
((FILE1 B FULL OUTER JOIN FILE2 C ON B.FIELD2 = C.FIELD2 )
           FULL OUTER JOIN FILE3 D ON C.FIELD2 = D.FIELD2 )
WHERE B.FIELD1 < 2
END

Multiple FULL OUTER JOINS are supported. However, they generate from a few to many
temporary HOLD files.

1916

Reference: SQL Join Considerations

27. Using SQL to Create Reports

In standard SQL, WHERE field='a' selects records where the field has the value 'a' or 'A'.
The SQL Translator is case-sensitive and returns the exact value requested (in this case,
'a' only).

The SQL comparison operators ANY, SOME, and ALL are supported, with the exception of
=ALL, <>ANY, and <>SOME.

Sub-selects are not supported in HAVING conditions.

In a multi-segment structure, parent segments are omitted from reports if no instances of
their descendant segments exist. This is an inner join.

The SQL Translator applies optimization techniques when constructing joins. See Index
Optimized Retrieval on page 1926.

For related information about index optimization and optimized join statements, see your
Server documentation.

SQL CREATE TABLE and INSERT INTO Commands

SQL Translator supports the commands CREATE TABLE and INSERT INTO table:

CREATE TABLE creates a new data source table. It only generates single-segment Master
Files.

INSERT INTO inserts a row or block of rows into a table or view. Single-record insert with
actual data values is supported.

These commands enable you to create tables to enhance reporting efficiency.

Note: When applications are enabled, the Master File and data source are written to the
APPHOLD directory. When applications are disabled, the Master File and data source are
written to the TEMP directory.

Reference: Usage Notes for CREATE TABLE and INSERT INTO Commands

According to normal SQL data definition syntax, each CREATE TABLE or INSERT INTO
statement must terminate with a semicolon.

The CREATE TABLE command supports the INTEGER, SMALLINT, FLOAT, CHARACTER,
DATE, TIME, TIMESTAMP, DECIMAL, DOUBLE PRECISION and REAL data types. Decimals
are rounded in the DOUBLE PRECISION and REAL data types.

Creating Reports With TIBCO® WebFOCUS Language

 1917

Using SQL Translator Commands

When using the CREATE TABLE and INSERT INTO commands, the data type FLOAT should
be declared with a precision and used in an INSERT INTO command without the 'E'
designation. This requires the entire value to be specified without an exponent.

The CHECK and DEFAULT options are not supported with the CREATE TABLE command.

Example:

Creating a Table With Single-Record Insert

The following shows a single-record insert, creating the table U with one record:

-* Single-record insert example.
-*
SQL
CREATE TABLE U (A INT, B CHAR(6), C CHAR(6), X INT, Y INT);
END
SQL
INSERT INTO U (A,B,C,X,Y) VALUES (10, '123456','654321', 10, 15);
END

SQL CREATE VIEW and DROP VIEW Commands

A view is a transient object that inherits most of the characteristics of a table. Like a table, it
is composed of rows and columns:

CREATE VIEW creates views. Note that it does not put the view in the system catalog.

DROP VIEW explicitly removes transient tables and views from the environment.

Tip: To use a view, issue a SELECT from it. You cannot issue a TABLE request against the view
because the view is not extracted as a physical FOCUS data source. To create a HOLD file for
extracted data, specify ON TABLE HOLD after the SQL statements. For details on creating
HOLD files, see Saving and Reusing Your Report Output on page 471.

1918

27. Using SQL to Create Reports

Syntax:

How to Create a View

The SQL Translator supports the following SQL statement:

CREATE VIEW viewname AS subquery ;

where:

viewname

Is the name of the view.

subquery

Is a SELECT statement that nests inside:

A WHERE, HAVING, or SELECT clause of another SELECT.

An UPDATE, DELETE, or INSERT statement.

Another subquery.

Example:

Creating and Reporting From an SQL View

The following example creates a view named XYZ:

SQL
CREATE VIEW XYZ
 AS SELECT CAR, MODEL
 FROM CAR;
END

To report from the view, issue:

SQL
 SELECT CAR, MODEL
 FROM XYZ;
END

According to normal SQL data definition syntax, each CREATE VIEW statement must terminate
with a semicolon.

Example:

Dropping an SQL View

The following request removes the XYZ view:

SQL
 DROP VIEW XYZ;
END

Creating Reports With TIBCO® WebFOCUS Language

 1919

Using SQL Translator Commands

Cartesian Product Style Answer Sets

The SQL Translator automatically generates Cartesian product style answer sets unless you
explicitly turn this feature off. However, it is advisable to leave the CARTESIAN setting on,
since turning it off does not comply with ANSI standards. For details on the SET CARTESIAN
command, see Merging Data Sources on page 1155.

Continental Decimal Notation (CDN)

Continental Decimal Notation displays numbers using a comma to mark the decimal position
and periods for separating significant digits into groups of three. This notation is available for
SQL Translator requests.

Example:

Using CDN to Separate Digits

The following example creates a column defined as 1.2 + SEATS:

SET CDN=ON
SQL
   SELECT SEATS + 1,2
   FROM CAR;
END

Specifying Field Names in SQL Requests

Specify fields in an SQL request using:

Delimited identifiers. A field name may contain (but not begin with) the symbols ., #, @, _,
and $. You must enclose such field names in double quotation marks when referring to
them.

Qualified field names. Qualify a field name with file and file alias names. File alias names
are described in the discussion of joins in SQL Joins on page 1913. See the Describing
Data With WebFOCUS Language manual for more information.

Field names with embedded blanks and special characters. A SELECT list can specify field
names with embedded blanks or other special characters. You must enclose such field
names in double quotation marks. Special characters are any characters not listed as
delimited identifiers, and not contained in the national character set of the installed FOCUS
environment.

Example:

Specifying a Field Name With a Delimited Identifier

The following field identifier can be included in a request:

"COUNTRY.NAME"

1920

27. Using SQL to Create Reports

Example:

Qualifying a Delimited Field Name

To qualify the delimited field name COUNTRY.NAME with its file name, use:

CAR."COUNTRY.NAME"

SQL UNION, INTERSECT, and EXCEPT Operators

The SQL UNION, INTERSECT, and EXCEPT operators generate MATCH logic. The number of files
that can participate is determined by the MATCH limit. UNION with parentheses is supported.

SELECT A UNION SELECT B retrieves rows in A or B or both. (This is equivalent to the
MATCH phrase OLD-OR-NEW.)

INTERSECT retrieves rows in both A and B. (This is equivalent to the MATCH phrase OLD-
AND-NEW.)

EXCEPT retrieves rows in A, but not B. (This is equivalent to the MATCH phrase OLD-NOT-
NEW.)

Match logic merges the contents of your data sources. See Merging Data Sources on page
1155.

Numeric Constants, Literals, Expressions, and Functions

The SQL SELECT list, WHERE predicate, and HAVING clause can include numeric constants,
literals enclosed in single quotation marks, expressions, and any scalar functions. Internally, a
virtual field is created for each of these in the SELECT list. The value of the virtual field is
provided in the answer set.

SQL Translator Support for Date, Time, and Timestamp Fields

Several new data types have been defined for the SQL Translator to support date-time fields in
the WHERE predicate or field list of a SELECT statement.

In addition, time or timestamp columns can be defined in relational or FOCUS data sources,
and are accessible to the translator. Values can be entered using INSERT and UPDATE
statements, and displayed in SELECT statements.

Time or timestamp data items (columns or literals) can be compared in conditions. Time
values or timestamp values can be added to or subtracted from each other, with the result
being the difference in number of seconds. Expressions of the form T + 2 HOURS or TS + 5
YEARS are allowed. These expressions are translated to calls to the date-time functions
described in the Using Functions manual.

Creating Reports With TIBCO® WebFOCUS Language

 1921

SQL Translator Support for Date, Time, and Timestamp Fields

All date formats for actual and virtual fields in the Master File are converted to the form
YYYYMMDD. If you specify a format that lacks any component, the SQL Translator supplies a
default value for the missing component. To specify a portion of a date, such as the month,
use a virtual field with an alphanumeric format.

Reference: SQL Translator Support for Date, Time, and Timestamp Fields

In the following chart, fff represents the second to three decimal places (milliseconds) and
ffffff represents the second to six decimal places (microseconds).

The following formats are allowed as input to the Translator:

Format

Date

Hour

Hour through minute

Hour through second

USAGE Attribute in
Master File

Date Components

YYMD

HH

HHI

HHIS

YYYY-MM-DD

HH

HH.MM

HH.MM.SS

Hour through millisecond

HHISs

HH.MM.SS.fff

Hour through microsecond

HHISsm

HH.MM.SS.ffffff

Year through hour

Year through minute

Year through second

HYYMDH

HYYMDI

HYYMDS

YYYY-MM-DD HH

YYYY-MM-DD HH.MM

YYYY-MM-DD HH.MM.SS

Year through millisecond

HYYMDs

YYYY-MM-DD HH.MM.SS.fff

Year through microsecond

HYYMDm

YYYY-MM-DD
HH.MM.SS.ffffff

Note:

Time information may be given to the hour, minute, second, or fraction of a second.

1922

27. Using SQL to Create Reports

The separator within date information may be either a hyphen or a slash.

The separator within time information must be a colon.

The separator between date and time information must be a space.

Extracting Date-Time Components Using the SQL Translator

The SQL Translator supports several functions that return components from date-time values.
Use the EXTRACT statement to extract components.

Use the TRIM function to remove leading and/or trailing patterns from date, time, and
timestamp values. See the Using Functions manual.

Syntax:

How to Use Date, Time, and Timestamp Functions Accepted by the SQL Translator

The following functions return date-time components as integer values. Assume x is a date-
time value:

Function

YEAR(x)

MONTH(x)

DAY(x)

HOUR(x)

MINUTE(x)

SECOND(x)

MILLISECOND(x)

MICROSECOND(x)

Return Value

year

month number

day number

hour

minute

second

millisecond

microsecond

Creating Reports With TIBCO® WebFOCUS Language

 1923

SQL Translator Support for Date, Time, and Timestamp Fields

Example:

Using SQL Translator Date, Time, and Timestamp Functions

Using the timestamp column TS whose value is '1999-11-23 07:32:16.123456':

YEAR(TS) = 1999
MONTH(TS) = 11
DAY(TS) = 23
HOUR(TS) = 7
MINUTE(TS) = 32
SECOND(TS) = 16
MILLISECOND(TS) = 123
MICROSECOND(TS) = 123456

Example:

Using SQL Translator Date, Time, and Timestamp Functions in a SELECT Statement

Assume that a FOCUS data source called VIDEOTR2 includes a date-time field named
TRANSDATE.

SQL
SELECT TRANSDATE,
YEAR(TRANSDATE), MONTH(TRANSDATE),
MINUTE(TRANSDATE)
FROM VIDEOTR2;
FILE VIDSQL
END

The SQL Translator produces the following virtual fields for functions, followed by a TABLE
request to display the output:

SET COUNTWIDTH=ON
-SET SQLERRNUM = 0;
DEFINE FILE
VIDEOTR2 TEMP
SQLDEF01/I4 MISSING ON NEEDS ALL = HPART(TRANSDATE,'YEAR','I4');
SQLDEF02/I2 MISSING ON NEEDS ALL = HPART(TRANSDATE,'MONTH','I2');
SQLDEF03/I2 MISSING ON NEEDS ALL = HPART(TRANSDATE,'MINUTE','I2');
END
TABLEF FILE VIDEOTR2
PRINT TRANSDATE SQLDEF01 AS 'SQLDEF01' SQLDEF02 AS 'SQLDEF02' SQLDEF03 AS
  'SQLDEF03'
ON TABLE SET CARTESIAN ON
ON TABLE SET ASNAMES ON
ON TABLE SET HOLDLIST PRINTONLY
END

1924

27. Using SQL to Create Reports

The output is:

TRANSDATE         SQLDEF02  SQLDEF04  SQLDEF05
1999/06/20 04:14      1999         6        14
1991/06/27 02:45      1991         6        45
1996/06/21 01:16      1996         6        16
1991/06/21 07:11      1991         6        11
1991/06/20 05:15      1991         6        15
1999/06/26 12:34      1999         6        34
1919/06/26 05:45      1919         6        45
1991/06/21 01:10      1991         6        10
1991/06/19 07:18      1991         6        18
1991/06/19 04:11      1991         6        11
1998/10/03 02:41      1998        10        41
1991/06/25 01:19      1991         6        19
1986/02/05 03:30      1986         2        30
1991/06/24 04:43      1991         6        43
1991/06/24 02:08      1991         6         8
1999/10/06 02:51      1999        10        51
1991/06/25 01:17      1991         6        17

Syntax:

How to Use the SQL Translator EXTRACT Function to Extract Date-Time Components

Use the following ANSI standard function to extract date-time components as integer values:

EXTRACT(component FROM value)

where:

component

Is one of the following: YEAR, MONTH, QUARTER, DAY, WEEKDAY, HOUR, MINUTE,
SECOND, MILLISECOND, or MICROSECOND.

value

Is a date-time, DATE, TIME, or TIMESTAMP field, constant or expression.

For example, the following are equivalent:

EXTRACT(YEAR FROM TS)
YEAR(TS)

Example:

Using the EXTRACT Function

SELECT D. EXTRACT(YEAR FROM D), EXTRACT(MONTH FROM D),
EXTRACT(DAY FROM D) FROM T

This request produces rows similar to the following:

1999-01-01     1999      1       1
2000-03-03     2000      3       3

Creating Reports With TIBCO® WebFOCUS Language

 1925

Index Optimized Retrieval

Index Optimized Retrieval

The SQL Translator improves query performance by generating optimized code that enables the
underlying retrieval engine to access the selected records directly, without scanning all
segment instances.

For more information about index optimization and optimized join statements, see your Server
documentation for your platform.

Optimized Joins

The SQL Translator accepts joins in SQL syntax. SQL language joins have no implied direction.
The concepts of host and cross-referenced files do not exist in SQL.

The SQL Translator analyzes each join to identify efficient implementation. First, it assigns
costs to the candidate joins in the query:

Cost = 1 for an equijoin to a field that can participate as a cross-referenced field according
to FOCUS join rules. This is common in queries against relational tables with equijoin
predicates in the WHERE clause.

Cost = 16 for an equijoin to a field that cannot participate as a cross-referenced field
according to FOCUS join rules.

Cost = 256 for a non-equijoin or an unrestricted Cartesian product.

The Translator then uses these costs to build a join structure for the query. The order of the
tables in the FROM clause of the query influences the first two phases of the join analysis:

1. If there are cost=1 joins from the first table referenced in the FROM clause to the second,
from the second table to the third, and so on, the Translator joins the tables in the order
specified in the query. If not, it goes on to Phase 2.

2. If Phase 1 fails to generate an acceptable join structure, the Translator attempts to

generate a join structure without joining any table to a table that precedes it in the FROM
clause. Therefore, this phase always makes the first table referenced in the query the host
table. If there is no cost=1 join between two tables, or if using one requires changing the
table order, the Translator abandons Phase 2 and implements Phase 3.

3. The Translator generates the join structure from the lowest-cost joins first, and then from

the more expensive joins as necessary. This sorting process may change the order in which
tables are joined. The efficiency of the join that this procedure generates depends on the
relative sizes of the tables being joined.

1926

27. Using SQL to Create Reports

If the analysis results in joining to a table that cannot participate as a cross-referenced file
according to FOCUS rules (because it lacks an index, for example), the Translator generates
code to build an indexed HOLD file, and implements the join with this file. However, the HOLD
file does not participate in the analysis of join order.

TABLEF Optimization

To improve performance, the SQL Translator can be set to generate FOCUS TABLEF commands
instead of TABLE commands. Take advantage of this optimization using the SET SQLTOPTTF
command (SQL Translator OPTimization TableF). See Improving Report Processing on page
1929.

Syntax:

How to Improve Performance Using SQLTOPTTF

SET SQLTOPTTF = {ON|OFF}

where:

ON

Causes TABLEF commands to be generated when possible (for example, if there is no join
or GROUP BY phrase). ON is the default value.

OFF

Causes TABLE commands to be generated.

SQL INSERT, UPDATE, and DELETE Commands

The SQL INSERT, UPDATE, and DELETE commands enable SQL users to manipulate and modify
data:

The INSERT statement introduces new rows into an existing table.

The DELETE statement removes a row or combination of rows from a table.

The UPDATE statement enables users to update a row or group of rows in a table.

You can issue an SQL INSERT, UPDATE, or DELETE command against one segment instance
(row) at a time. When you issue one of these commands against a multi-segment Master File:

All fields referenced in the command must be on a single path through the file structure.

The command must explicitly specify (in the WHERE predicate) every key value from the root
to the target segment instance, and this combination of key values must uniquely identify
one segment instance (row) to be affected by the command.

Creating Reports With TIBCO® WebFOCUS Language

 1927

SQL INSERT, UPDATE, and DELETE Commands

If you are modifying every field in the row, you can omit the list of field names from the
command.

The SQL Translator supports subqueries, such as:

INSERT...INTO...SELECT...FROM...

Although each INSERT, UPDATE, or DELETE command can specify only one row, referential
integrity constraints may produce the following modifications to the data source:

If you delete a segment instance that has descendant segment instances (children), the
children are automatically deleted.

If you insert a segment for which parent segments are missing, the parent segments are
automatically created.

1928

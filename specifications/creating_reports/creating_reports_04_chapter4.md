Chapter4

Selecting Records for Your Report

When generating a report and selecting fields, you may not want to include every
instance of a field. By including selection criteria, you can display only those field values
that meet your needs. In effect, you can select a subset of data that you can easily
redefine each time you issue the report request.

In this chapter:

Selecting Records Overview

Types of Record Selection Tests

Choosing a Filtering Method

Selections Based on Group Key Values

Selections Based on Individual Values

Selection Based on Aggregate Values

Applying Selection Criteria to the Internal
Matrix Prior to COMPUTE Processing

Using Compound Expressions for Record
Selection

Using Operators in Record Selection
Tests

Setting Limits on the Number of Records
Read

Selecting Records Using IF Phrases

Reading Selection Values From a File

Assigning Screening Conditions to a File

VSAM Record Selection Efficiencies

Selecting Records Overview

When developing a report request, you can define criteria that select records based on a
variety of factors:

The values of an individual field. See Selections Based on Individual Values on page 218.

The aggregate value of a field (for example, the sum or average of field values). See
Selection Based on Aggregate Values on page 226.

The existence of missing values for a field, whether field values fall within a range, or
whether a field does not contain a certain value. See Types of Record Selection Tests on
page 243.

The number of records that exist for a field (for example, the first 50 records), rather than
on the field values. See Setting Limits on the Number of Records Read on page 258.

Creating Reports With TIBCO® WebFOCUS Language

 217

Choosing a Filtering Method

For non-FOCUS data sources that have group keys, you can select records based on group
key values. See Selections Based on Group Key Values on page 257.

In addition, you can take advantage of a variety of record selection efficiencies, including
assigning filtering criteria to a data source and reading selection values from a file.

Choosing a Filtering Method

There are two phrases for selecting records: WHERE and IF. It is recommended that you use
WHERE to select records. IF offers a subset of the functionality of WHERE. Everything that you
can accomplish with IF, you can also accomplish with WHERE. WHERE can accomplish things
that IF cannot.

If you used IF to select records in the past, remember that WHERE and IF are two different
phrases, and may require different syntax to achieve the same result.

WHERE syntax is described and illustrated throughout this topic. For details on IF syntax, see
Selecting Records Using IF Phrases on page 259.

Selections Based on Individual Values

The WHERE phrase selects records from the data source to be included in a report. The data is
evaluated according to the selection criteria before it is retrieved from the data source.

You can use as many WHERE phrases as necessary to define your selection criteria. For an
illustration, see Using Multiple WHERE Phrases on page 220. For additional information, see
Using Compound Expressions for Record Selection on page 235.

Note: Multiple selection tests on fields that reside on separate paths of a multi-path data
source are processed as though connected by either AND or OR operators, based on the
setting of a parameter called MULTIPATH. For details, see Controlling Record Selection in Multi-
path Data Sources on page 221.

Syntax:

How to Select Records With WHERE

WHERE criteria [;]

where:

criteria

Are the criteria for selecting records to include in the report. The criteria must be
defined in a valid expression that evaluates as true or false (that is, a Boolean
expression). Expressions are described in detail in Using Expressions on page 429.
Operators that can be used in WHERE expressions (such as, CONTAINS, IS, and GT),
are described in Operators Supported for WHERE and IF Tests on page 236.

218

4. Selecting Records for Your Report

;

Is an optional semicolon that can be used to enhance the readability of the request. It
does not affect the report.

Reference: Usage Notes for WHERE Phrases

The WHERE phrase can include:

Most expressions that would be valid on the right-hand side of a DEFINE expression.
However, the logical expression IF ... THEN ... ELSE cannot be used.

Real fields, temporary fields, and fields in joined files. If a field name is enclosed in single
or double quotation marks, it is treated as a literal string, not a field reference.

The operators EQ, NE, GE, GT, LT, LE, CONTAINS, OMITS, FROM ... TO, NOT-FROM ... TO,
INCLUDES, EXCLUDES, LIKE, and NOT LIKE.

All arithmetic operators (+, -, *, /, **), as well as, functions (MIN, MAX, ABS, and SQRT).

An alphanumeric expression, which can be a literal, or a function yielding an alphanumeric
or numeric result using EDIT or DECODE.

Note that files used with DECODE expressions can contain two columns, one for field
values and one for numeric decode values.

Alphanumeric and date literals enclosed in single quotation marks and date-time literals in
the form DT (date-time literal).

A date literal used in a selection test against a date field cannot contain the day of the
week value.

Text fields. However, the only operators supported for use with text fields are CONTAINS
and OMITS.

All functions.

You can build complex selection criteria by joining simple expressions with AND and OR logical
operators and, optionally, adding parentheses to specify explicitly the order of evaluation. This
is easier than trying to achieve the same effect with the IF phrase, which may require the use
of a separate DEFINE command. For details, see Using Compound Expressions for Record
Selection on page 235.

Creating Reports With TIBCO® WebFOCUS Language

 219

Selections Based on Individual Values

Example:

Using a Simple WHERE Test

To show only the names and salaries of employees earning more than $20,000 a year, issue
the following request:

TABLE FILE EMPLOYEE
PRINT LAST_NAME AND FIRST_NAME AND CURR_SAL
BY LAST_NAME NOPRINT
WHERE CURR_SAL GT 20000
END

In this example, CURR_SAL is a selected field, and CURR_SAL GT 20000 is the selection
criterion. Only those records with a current salary greater than $20,000 are retrieved. All other
records are ignored.

The output is:

Example:

Using Multiple WHERE Phrases

You can use as many WHERE phrases as necessary to define your selection criteria. This
request uses multiple WHERE phrases so that only those employees in the MIS or Production
departments with the last name of Cross or Banning are included in the report.

TABLE FILE EMPLOYEE
PRINT EMP_ID LAST_NAME
WHERE SALARY GT 20000
WHERE DEPARTMENT IS 'MIS' OR 'PRODUCTION'
WHERE LAST_NAME IS 'CROSS' OR 'BANNING'
END

The output is:

220

For related information, see Using Compound Expressions for Record Selection on page 235.

Controlling Record Selection in Multi-path Data Sources

4. Selecting Records for Your Report

When you report from a multi-path data source, a parent segment may have children down
some paths, but not others. The MULTIPATH parameter allows you to control whether such a
parent segment is omitted from the report output.

The MULTIPATH setting also affects the processing of selection tests on independent paths. If
MULTIPATH is set to:

COMPOUND, WHERE or IF tests on separate paths are treated as if they are connected by
an AND operator. That is, all paths must pass the screening tests in order for the parent to
be included in the report output.

SIMPLE, WHERE or IF tests on separate paths are considered independently, as if an OR
operator connected them. Therefore, a parent instance is included in the report if at least
one of the paths passes its screening test. A warning message is produced, indicating that
if the request contains a test on one path, data is also retrieved from another, independent
path. Records on the independent path are retrieved regardless of whether the condition is
satisfied on the tested path.

The MULTIPATH settings apply in all types of data sources and in all reporting environments
(TABLE, TABLEF, MATCH, GRAPH, and requests with multiple display commands). MULTIPATH
also works with alternate views, indexed views, filters, DBA, and joined structures.

Syntax:

How to Control Record Selection in Multi-path Data Sources

To set MULTIPATH from the command level or in a stored procedure, use

SET MULTIPATH = {SIMPLE|COMPOUND}

To set MULTIPATH in a report request, use

ON TABLE SET MULTIPATH {SIMPLE|COMPOUND}

where:

SIMPLE

Includes a parent segment in the report output if:

It has at least one child that passes its screening conditions.

Note: A unique segment is considered a part of its parent segment, and therefore does
not invoke independent path processing.

Creating Reports With TIBCO® WebFOCUS Language

 221

Selections Based on Individual Values

It lacks any referenced child on a path, but the child is optional.

The (FOC144) warning message is generated when a request screens data in a multi-
path report:

(FOC144) WARNING. TESTING IN INDEPENDENT SETS OF DATA

COMPOUND

Includes a parent in the report output if it has all of its required children. WHERE or IF
tests on separate paths are treated as if they are connected by an AND operator. That
is, all paths must pass the screening tests in order for the parent to be included in
the report output. COMPOUND is the default value.

For related information, see MULTIPATH and SET ALL Combinations on page 224 and Rules for
Determining If a Segment Is Required on page 226.

Reference: Requirements and Usage Notes for MULTIPATH = COMPOUND

The minimum memory requirement for the MULTIPATH = COMPOUND setting is 4K per
active segment. If there is insufficient memory, the SIMPLE setting is implemented and a
message is returned.

There is no limit to the number of segment instances (rows). However, no single segment
instance can have more than 4K of active fields (referenced fields or fields needed for
retrieving referenced fields). If this limit is exceeded, the SIMPLE setting is implemented
and a message is returned.

WHERE criteria that screen on more than one path with the OR operator are not supported.

222

Example:

Retrieving Data From Multiple Paths

This example uses the following segments from the EMPLOYEE data source:

4. Selecting Records for Your Report

The request that follows retrieves data from both paths with MULTIPATH = SIMPLE, and
displays data if either criterion is met:

SET ALL = OFF
SET MULTIPATH = SIMPLE
TABLE FILE EMPLOYEE
PRINT GROSS DATE_ATTEND COURSE_NAME
BY LAST_NAME BY FIRST_NAME
WHERE PAY_DATE EQ 820730
WHERE COURSE_CODE EQ '103'
END

The following warning message is generated:

(FOC144) WARNING. TESTING IN INDEPENDENT SETS OF DATA

Although several employees have not taken any courses, they are included in the report output
since they have instances on one of the two paths.

Creating Reports With TIBCO® WebFOCUS Language

 223

Selections Based on Individual Values

The output is:

If you run the same request with MULTIPATH = COMPOUND, the employees without instances
for COURSE_NAME are omitted from the report output, and the warning message is not
generated.

The output is:

LAST_NAME       FIRST_NAME            GROSS  DATE_ATTEND  COURSE_NAME
---------       ----------            -----  -----------  -----------
JONES           DIANE             $1,540.00     82/05/26  BASIC REPORT PREP FOR PROG
SMITH           MARY              $1,100.00     81/11/16  BASIC REPORT PREP FOR PROG

Reference: MULTIPATH and SET ALL Combinations

The ALL parameter affects independent path processing. The following table uses examples
from the EMPLOYEE data source to explain the interaction of ALL and MULTIPATH.

Request

MULTIPATH=SIMPLE

MULTIPATH=COMPOUND

SET ALL = OFF
PRINT EMP_ID
PAY_DATE
DATE_ATTEND

SET ALL = ON
PRINT EMP_ID
PAY_DATE
DATE_ATTEND

Shows employees who
have either SALINFO data
or ATTNDSEG data.

Shows employees who
have SALINFO data or
ATTNDSEG data or no child
data at all.

Shows employees who have both
SALINFO and ATTNDSEG data.

Same as SIMPLE.

224

4. Selecting Records for Your Report

Request

MULTIPATH=SIMPLE

MULTIPATH=COMPOUND

SET ALL = OFF
PRINT EMP_ID
PAY_DATE
DATE_ATTEND
WHERE PAY_DATE EQ
980115

Shows employees who
have either SALINFO data
for 980115 or any
ATTNDSEG data.

Produces (FOC144)
message.

Shows employees who have both
SALINFO data for 980115 and
ATTNDSEG data.

SET ALL = ON
PRINT EMP_ID
PAY_DATE
DATE_ATTEND
WHERE PAY_DATE EQ
980115

Shows employees who
have either SALINFO data
for 980115 or any
ATTNDSEG data.

Shows employees who have
SALINFO data for 980115. Any
DATE_ATTEND data is also
shown.

Produces (FOC144)
message.

SET ALL = OFF
PRINT ALL.EMP_ID
DATE_ATTEND
WHERE PAY_DATE EQ
980115

Shows employees who
have either SALINFO data
for 980115 or any
ATTNDSEG data.

Shows employees who have
SALINFO data for 980115. Any
DATE_ATTEND data is also
shown.

SET ALL = ON or OFF
PRINT EMP_ID
PAY_DATE
DATE_ATTEND
WHERE PAY_DATE EQ
980115 AND
COURSE_CODE EQ
'103'

Produces (FOC144)
message.

Shows employees who
have either SALINFO data
for 980115 or COURSE
103.

Note: SIMPLE treats AND
in the WHERE clause as
OR.

Produces (FOC144)
message.

Shows employees who have both
SALINFO data for 980115 and
COURSE 103.

Note: SET ALL = PASS is not supported with MULTIPATH = COMPOUND.

For related information about the ALL parameter, see Handling Records With Missing Field
Values on page 1035.

Creating Reports With TIBCO® WebFOCUS Language

 225

Selection Based on Aggregate Values

Reference: Rules for Determining If a Segment Is Required

The segment rule is applied level by level, descending through the data source/view hierarchy.
That is, a parent segment existence depends on the child segment existence, and the child
segment depends on the grandchild existence, and so on, for the full data source tree.

The following rules are used to determine if a segment is required or optional:

When SET ALL is ON or OFF, a segment with WHERE or IF criteria is required for its parent,
and all segments up to the root segment are required for their parents.

When SET ALL = PASS, a segment with WHERE or IF criteria is optional.

IF SET ALL = ON or PASS, all referenced segments with no WHERE or IF criteria are optional
for their parents (outer join).

IF SET ALL = OFF, all referenced segments are required (inner join).

A referenced segment can become optional if its parent segment uses the ALL. field prefix
operator.

Note: ALL = PASS is not supported for all data adapters and, if it is supported, it may behave
slightly differently. Check your specific data adapter documentation for detailed information.

For related information about the ALL parameter, see Handling Records With Missing Field
Values on page 1035, and the Describing Data With WebFOCUS Language manual.

Selection Based on Aggregate Values

You can select records based on the aggregate value of a field. For example, on the sum of
field values, or on the average of field values, by using the WHERE TOTAL phrase. WHERE
TOTAL is very helpful when you employ the aggregate display commands SUM and COUNT, and
is required for fields with a prefix operator, such as AVE. and PCT.

In WHERE tests, data is evaluated before it is retrieved. In WHERE TOTAL tests, however, data
is selected after all the data has been retrieved and processed. For an example, see Using
WHERE TOTAL for Record Selection on page 227.

Syntax:

How to Select Records With WHERE TOTAL

WHERE TOTAL criteria[;]

where:

criteria

Are the criteria for selecting records to include in the report. The criteria must be
defined in a valid expression that evaluates as true or false (that is, a Boolean

226

4. Selecting Records for Your Report

expression). Expressions are described in detail in Using Expressions on page 429.
Operators that can be used in WHERE expressions (such as, IS and GT) are described
in Operators Supported for WHERE and IF Tests on page 236.

;

Is an optional semicolon that can be used to enhance the readability of the request. It
does not affect the report.

Reference: Usage Notes for WHERE TOTAL

Any reference to a calculated value, or use of a feature that aggregates values, such as
TOT.field, AVE.field, requires the use of WHERE TOTAL.

Fields with prefix operators require the use of WHERE TOTAL.

WHERE TOTAL tests are performed at the lowest sort level.

Alphanumeric and date literals must be enclosed in single quotation marks. Date-time
literals must be in the form DT (date-time literal).

When you use ACROSS with WHERE TOTAL, data that does not satisfy the selection criteria
is represented in the report with the NODATA character.

If you save the output from your report request in a HOLD file, the WHERE TOTAL test
creates a field called WH$$$T1, which contains its internal computations. If there is more
than one WHERE TOTAL test, each TOTAL test creates a corresponding WH$$$T field and
the fields are numbered consecutively.

Example:

Using WHERE TOTAL for Record Selection

The following example sums current salaries by department.

TABLE FILE EMPLOYEE
SUM CURR_SAL
BY DEPARTMENT
END

The output is:

DEPARTMENT         CURR_SAL
----------         --------
MIS             $108,002.00
PRODUCTION      $114,282.00

Creating Reports With TIBCO® WebFOCUS Language

 227

Applying Selection Criteria to the Internal Matrix Prior to COMPUTE Processing

Now, add a WHERE TOTAL phrase to the request in order to generate a report that lists only
the departments where the total of the salaries is more than $110,000.

TABLE FILE EMPLOYEE
SUM CURR_SAL
BY DEPARTMENT
WHERE TOTAL CURR_SAL EXCEEDS 110000
END

The values for each department are calculated and then each final value is compared to
$110,000. The output is:

DEPARTMENT         CURR_SAL
----------         --------
PRODUCTION      $114,282.00

Example:

Combining WHERE TOTAL and WHERE for Record Selection

The following request extracts records for the MIS department. Then, CURR_SAL is summed
for each employee. If the total salary for an employee is greater than $20,000, the values of
CURR_SAL are processed for the report. In other words, WHERE TOTAL screens data after
records are selected.

TABLE FILE EMPLOYEE
SUM CURR_SAL
BY LAST_NAME AND BY FIRST_NAME
WHERE TOTAL CURR_SAL EXCEEDS 20000
WHERE DEPARTMENT IS 'MIS'
END

The output is:

LAST_NAME        FIRST_NAME         CURR_SAL
---------        ----------         --------
BLACKWOOD        ROSEMARIE        $21,780.00
CROSS            BARBARA          $27,062.00

Applying Selection Criteria to the Internal Matrix Prior to COMPUTE Processing

WHERE TOTAL tests are applied to the rows of the internal matrix after COMPUTE calculations
are processed in the output phase of the report. WHERE_GROUPED tests are applied to the
internal matrix values prior to COMPUTE calculations. The processing then continues with
COMPUTE calculations, and then WHERE TOTAL tests. This allows the developer to control the
evaluation, and is particularly useful in recursive calculations.

Syntax:

How to Apply WHERE_GROUPED Selection Criteria

WHERE_GROUPED expression

228

4. Selecting Records for Your Report

where:

expression

Is an expression that does not refer to more than one row in the internal matrix. For
example, it cannot use the LAST operator to refer to or retrieve a value from a prior record.

Example:

Using a WHERE_GROUPED Test

The following request has two COMPUTE commands. The first COMPUTE checks to see if the
business region value has changed, incrementing a counter if it has. This allows us to
sequence the records in the matrix. The second COMPUTE creates a rolling total of the days
delayed within the business region.

TABLE FILE WF_RETAIL_LITE
SUM  DAYSDELAYED AS DAYS
COMPUTE CTR/I3 = IF BUSINESS_REGION EQ LAST BUSINESS_REGION THEN CTR+1 ELSE
1;
COMPUTE NEWDAYS = IF BUSINESS_REGION EQ LAST BUSINESS_REGION THEN NEWDAYS
+DAYSDELAYED ELSE DAYSDELAYED;
BY BUSINESS_REGION AS Region
BY TIME_MTH
WHERE BUSINESS_REGION NE 'Oceania'
ON TABLE SET PAGE NOPAGE
END

Creating Reports With TIBCO® WebFOCUS Language

 229

Applying Selection Criteria to the Internal Matrix Prior to COMPUTE Processing

The output is shown in the following image.

230

4. Selecting Records for Your Report

The following version of the request adds a WHERE TOTAL test to select only those months
where DAYSDELAYED exceeded 200 days.

TABLE FILE WF_RETAIL_LITE
SUM  DAYSDELAYED AS DAYS
COMPUTE CTR/I3 = IF BUSINESS_REGION EQ LAST BUSINESS_REGION THEN CTR+1 ELSE
1;
COMPUTE NEWDAYS= IF BUSINESS_REGION EQ LAST BUSINESS_REGION THEN NEWDAYS
+DAYSDELAYED ELSE DAYSDELAYED;
BY BUSINESS_REGION AS Region
BY TIME_MTH
WHERE BUSINESS_REGION NE 'Oceania'
WHERE TOTAL DAYSDELAYED GT 200
ON TABLE SET PAGE NOPAGE
END

Creating Reports With TIBCO® WebFOCUS Language

 231

Applying Selection Criteria to the Internal Matrix Prior to COMPUTE Processing

The output is shown in the following image. The COMPUTE calculations for CTR and NEWDAYS
were processed prior to eliminating the rows in which TOTAL DAYSDELAYED were 200 or less,
so their values are the same as in the original output. This does not correctly reflect the
sequence of records and the rolling total of the values that are actually displayed on the
output. To do this, we need to select the appropriate months (DAYSDELAYED GT 200) before
the COMPUTE expressions are evaluated. This requires WHERE_GROUPED.

232

4. Selecting Records for Your Report

The following version of the request replaces the WHERE TOTAL test with a WHERE_GROUPED
test.

TABLE FILE WF_RETAIL_LITE
SUM  DAYSDELAYED AS DAYS
COMPUTE CTR/I3 = IF BUSINESS_REGION EQ LAST BUSINESS_REGION THEN CTR+1 ELSE
1;
COMPUTE NEWDAYS= IF BUSINESS_REGION EQ LAST BUSINESS_REGION THEN NEWDAYS
+DAYSDELAYED ELSE DAYSDELAYED;
BY BUSINESS_REGION AS Region
BY TIME_MTH
WHERE BUSINESS_REGION NE 'Oceania'
WHERE_GROUPED DAYSDELAYED GT 200
ON TABLE SET PAGE NOPAGE
END

Creating Reports With TIBCO® WebFOCUS Language

 233

Applying Selection Criteria to the Internal Matrix Prior to COMPUTE Processing

The output is shown in the following image. The COMPUTE calculation for NEWDAYS was
processed after eliminating the rows in which TOTAL DAYSDELAYED were 200 or less, so its
values are based on fewer rows than the calculations in the original request. This is verified by
the CTR values, which are now in a continuous sequence. The rolling total now reflects the
values that are actually displayed on the report output.

Reference: Usage Notes for WHERE_GROUPED

If the expression refers to multiple rows in the internal matrix, the following message is
generated and processing stops.

(FOC32692) WHERE_GROUPED CANNOT REFER TO OTHER LINES OF REPORT

A COMPUTE that does not reference multiple lines will be evaluated prior to
WHERE_GROUPED tests, and may, therefore, be used in an expression and evaluated as
part of a WHERE_GROUPED test.

234

4. Selecting Records for Your Report

WHERE_GROUPED can be optimized for SQL data sources by creating a GROUP BY
fieldname HAVING expression clause, where the expression is the WHERE_GROUPED
selection criteria.

Using Compound Expressions for Record Selection

You can combine two or more simple WHERE expressions, connected by AND and/or OR
operators, to create a compound expression.

By default, when multiple WHERE phrases are evaluated, logical ANDs are processed before
logical ORs. In compound expressions, you can use parentheses to change the order of
evaluation. All AND and OR operators enclosed in parentheses are evaluated first, followed by
AND and OR operators outside of parentheses.

You should always use parentheses in complex expressions to ensure that the expression is
evaluated correctly. For example:

WHERE (SEATS EQ 2) AND (SEATS NOT-FROM 3 TO 4)

This is especially useful when mixing literal OR tests with logical AND and OR tests:

In a logical AND or OR test, all field names, test relations, and test values are explicitly
referenced and connected by the words OR or AND. For example:

WHERE (LAST_NAME EQ 'CROSS') OR (LAST_NAME EQ 'JONES')

or

WHERE (CURR_SAL GT 20000) AND (DEPARTMENT IS 'MIS')
       AND (CURR_JOBCODE CONTAINS 'A')

In a literal OR test, the word OR is repeated between test values of a field name, but the
field name itself and the connecting relational operator are not repeated. For example:

WHERE (LAST_NAME EQ 'CROSS' OR 'JONES')

Example: Mixing AND and OR Record Selection Tests

This example illustrates the impact of parentheses on the evaluation of literal ORs and logical
ANDs.

In this request, each expression enclosed in parentheses is evaluated first in the order in
which it appears. Notice that the first expression contains a literal OR. The result of each
expression is then evaluated using the logical AND.

Creating Reports With TIBCO® WebFOCUS Language

 235

Using Operators in Record Selection Tests

If parentheses are excluded, the logical AND is evaluated before the literal OR.

TABLE FILE EMPLOYEE
PRINT CURR_SAL BY LAST_NAME
WHERE (LAST_NAME EQ 'CROSS' OR 'JONES')
AND (CURR_SAL GT 22000)
END

The output is:

LAST_NAME               CURR_SAL
---------               --------
CROSS                 $27,062.00

Using Operators in Record Selection Tests

You can include a variety of operators in your WHERE and IF selection tests. Many of the
operators are common for WHERE and IF. However, several are supported only for WHERE
tests.

Reference: Operators Supported for WHERE and IF Tests

You can define WHERE and IF selection criteria using the following operators.

WHERE Operator

IF Operator

Meaning

EQ
IS

NE
IS-NOT

GE

EQ
IS

NE
IS-NOT

GE
FROM
IS-FROM

GT
EXCEEDS
IS-MORE-THAN

GT
EXCEEDS
IS-MORE-THAN

LT
IS-LESS-THAN

LT
IS-LESS-THAN

236

Tests for and selects values equal to
the test expression.

Tests for and selects values not
equal to the test expression.

Tests for and selects values greater
than or equal to the test value
(based on the characters 0 to 9 for
numeric values, A to Z and a to z for
alphanumeric values).

The test value can be a field value or
the result of an expression.

Tests for and selects values greater
than the test value.

Tests for and selects values less
than the test value.

4. Selecting Records for Your Report

WHERE Operator

IF Operator

Meaning

LE

LE
TO

GE lower AND
...
LE upper

LT lower OR
... GT upper

FROM lower
TO upper

IS-FROM lower
TO upper

IS-FROM lower
TO upper

NOT-FROM lower
TO upper

NOT-FROM lower
TO upper

IS MISSING
IS-NOT MISSING
NE MISSING

IS MISSING
IS-NOT MISSING
NE MISSING

CONTAINS
LIKE

CONTAINS
LIKE

Tests for and selects values less
than or equal to the test value.

Tests for and selects values within a
range of values.

Tests for and selects values outside
of a range of values.

Tests for and selects values within a
range of values.

Tests for and selects values within a
range of values. For WHERE, this is
alternate syntax for FROM lower to
UPPER. Both operators produce
identical results.

Tests for and selects values that are
outside a range of values.

Tests whether a field contains
missing values. If some instances of
the field contain no data, they have
missing data. For information on
missing data, see Handling Records
With Missing Field Values on page
1035.

Tests for and selects values that
include a character string matching
test value. The string can occur in
any position in the value being
tested. When used with WHERE,
CONTAINS can test alphanumeric
fields. When used with IF, it can test
both alphanumeric and text fields.

Creating Reports With TIBCO® WebFOCUS Language

 237




Using Operators in Record Selection Tests

WHERE Operator

IF Operator

Meaning

OMITS
NOT LIKE

OMITS
UNLIKE

INCLUDES

INCLUDES

EXCLUDES

EXCLUDES

IN (z,x,y)

NOT ... IN
(z,x,y)

IN FILE

NOT ... IN FILE

IF-THEN-ELSE

Tests for and selects values that do
not include a character string
matching test value. The string
cannot occur in any position in the
value being tested. When used with
WHERE, OMITS can test
alphanumeric fields. When used with
IF, it can test both alphanumeric and
text fields.

Tests whether a chain of values of a
given field in a child segment
includes all of a list of literals.

Tests whether a chain of values of a
given field in a child segment
excludes all of a list of literals.

Selects records based on values
found in an unordered list.

Selects records based on values not
found in an unordered list.

Selects records based on values
stored in a sequential file.

Selects records with field values not
found in a sequential file.

Selects records based on the logical
conditions listed in the IF-THEN-ELSE
phrase.

238





Example:

Using Operators to Compare a Field to One or More Values

The following examples illustrate field selection criteria that use one or more values. You may
use the operators: EQ, IS, IS-NOT, EXCEEDS, IS-LESS-THAN, and IN.

4. Selecting Records for Your Report

Example 1: The field LAST_NAME must equal the value JONES:

WHERE LAST_NAME EQ 'JONES'

Example 2: The field LAST_NAME begins with 'CR' or 'MC:'

WHERE EDIT (LAST_NAME, '99') EQ 'CR' OR 'MC'

Example 3: The field AREA must not equal the value EAST or WEST:

WHERE AREA IS-NOT 'EAST' OR 'WEST'

Example 4: The value of the field AREA must equal the value of the field REGION:

WHERE AREA EQ REGION

Note that you cannot compare one field to another in an IF test.

Example 5: The ratio between retail cost and dealer cost must be greater than 1.25:

WHERE RETAIL_COST/DEALER_COST GT 1.25

Example 6: The field UNITS must be equal to or less than the value 50, and AREA must not be
equal to either NORTH EAST or WEST. Note the use of single quotation marks around NORTH
EAST. All alphanumeric strings must be enclosed within single quotation marks.

WHERE UNITS LE 50 WHERE AREA IS-NOT 'NORTH EAST' OR 'WEST'

Example 7: The value of AMOUNT must be greater than 40:

WHERE AMOUNT EXCEEDS 40

Example 8: The value of AMOUNT must be less than 50:

WHERE AMOUNT IS-LESS-THAN 50

Example 9: The value of SALES must be equal to one of the numeric values in the unordered
list. Use commas or blanks to separate the list values.

WHERE SALES IN (43000,12000,13000)

Creating Reports With TIBCO® WebFOCUS Language

 239

Using Operators in Record Selection Tests

Example 10: The value of CAR must be equal to one of the alphanumeric values in the
unordered list. Single quotation marks must enclose alphanumeric list values.

WHERE CAR IN ('JENSEN','JAGUAR')

Example:

Using IF-THEN-ELSE Logic in a WHERE Clause

The following request uses IF-THEN-ELSE logic in a WHERE clause to select records based on
values of WHOLESALEPR where the values used for selection vary depending on the value of
LISTPR in that record.

TABLE FILE MOVIES
PRINT COPIES
LISTPR
WHOLESALEPR
BY CATEGORY
WHERE WHOLESALEPR GT (IF LISTPR GT 20.00 THEN 15.00 ELSE 11.00)
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

240

4. Selecting Records for Your Report

The output is shown in the following image. In the selected records, WHOLESALEPR is greater
than $15.00 if LISTPR is greater than $20.00. WHOLESALEPR is greater than $11.00 if
LISTPR is less than or equal to $20.00.

Creating Reports With TIBCO® WebFOCUS Language

 241

Using Operators in Record Selection Tests

Example:

Using Variables in Record Selection Tests

In this example, the field REGION is used in the WHERE test as a variable so that when the
report is executed, the user is prompted to select one of the listed values (CE, CORP, NE, SE
or WE) of the REGION field. The text that appears after the values is what appears before the
drop-down list in the output.

TABLE FILE EMPDATA
SUM SALARY
BY DIV
BY DEPT
HEADING
"Current Salary Report"
"for the &REGION Division"
" "
WHERE ( DIV EQ
'&REGION.(CE,CORP,NE,SE,WE).Please select a Region.');
END

The output is:

Select a region from the drop-down list and click Submit. The output for the NE region is:

242

Types of Record Selection Tests

4. Selecting Records for Your Report

You can select records for your reports using a variety of tests that are implemented using the
operators described in Operators Supported for WHERE and IF Tests on page 236. You can test
for:

Values that lie within or outside of a range. See Range Tests With FROM and TO on page
243 and Range Tests With GE and LE or GT and LT on page 245.

Missing or existing data. See Missing Data Tests on page 246.

The existence or absence of a character string. See Character String Screening With
CONTAINS and OMITS on page 247.

Partially defined character strings in a data field. See Screening on Masked Fields on page
248.

Literals in a parent segment. See Qualifying Parent Segments Using INCLUDES and
EXCLUDES on page 256.

Range Tests With FROM and TO

Use the operators FROM ... TO and NOT-FROM ... TO in order to determine whether field values
fall within or outside of a given range. You can use either values or expressions to specify the
lower and upper boundaries. Range tests can also be applied on the sort control fields. The
range test is specified immediately after the sort phrase.

You can also test whether an expression falls within or outside the boundaries.

Syntax:

How to Specify a Range Test (FROM and TO)

WHERE [TOTAL] {fieldname|expression} {FROM|IS-FROM} lower TO upper
WHERE [TOTAL] fieldname  NOT-FROM      lower TO upper

where:

fieldname

Is any valid field name or alias.

expression

Is any valid expression.

lower

Are numeric or alphanumeric values or expressions that indicate lower boundaries.
You may add parentheses around expressions for readability.

Creating Reports With TIBCO® WebFOCUS Language

 243

Types of Record Selection Tests

upper

Are numeric or alphanumeric values or expressions that indicate upper boundaries.
You may add parentheses around expressions for readability.

Example:

Range Test With FROM ... TO

An example of a range test using expressions as boundaries follows:

WHERE SALES FROM (DEALER_COST * 1.4) TO (DEALER_COST * 2.0)

The following is an example of a range test using expressions as the comparison value and the
boundaries:

WHERE SALES * 1.5 FROM (DEALER_COST * 1.4) TO (DEALER_COST * 2.0)

Example:

Range Test With NOT-FROM ... TO

The following illustrates how you can use the range test NOT-FROM ... TO to display only those
records that fall outside of the specified range. In this example, it is all employees whose
salaries do not fall in the range between $12,000 and $22,000.

TABLE FILE EMPLOYEE
PRINT CURR_SAL
BY LAST_NAME
WHERE CURR_SAL NOT-FROM 12000 TO 22000
END

The output is:

LAST_NAME               CURR_SAL
---------               --------
BANNING               $29,700.00
CROSS                 $27,062.00
GREENSPAN              $9,000.00
IRVING                $26,862.00
SMITH                  $9,500.00
STEVENS               $11,000.00

Example:

Range Tests on Sort Fields With FROM ... TO

The following examples demonstrate how to perform range tests when sorting a field using the
BY or ACROSS sort phrases:

BY MONTH FROM 4 TO 8

or

ACROSS MONTH FROM 6 TO 10

244

4. Selecting Records for Your Report

Range Tests With GE and LE or GT and LT

The operators GE (greater than or equal to), LE (less than or equal to), GT (greater than), and
LT (less than) can be used to specify a range.

GE ... LE enable you to specify values within the range test boundaries.

LT ...GT enable you to specify values outside the range test boundaries.

Syntax:

How to Specify Range Tests (GE and LE)

To select values that fall within a range, use

WHERE fieldname GE lower AND fieldname LE upper

To find records whose values do not fall in a specified range, use

WHERE fieldname LT lower OR fieldname GT upper

where:

fieldname

Is any valid field name or alias.

lower

Are numeric or alphanumeric values or expressions that indicate lower boundaries.
You may add parentheses around expressions for readability.

upper

Are numeric or alphanumeric values or expressions that indicate upper boundaries.
You may add parentheses around expressions for readability.

Example:

Selecting Values Inside a Range

This WHERE phrase selects records in which the UNIT value is between 10,000 and 14,000.

WHERE UNITS GE 10000 AND UNITS LE 14000

This example is equivalent to:

WHERE UNITS GE 10000
WHERE UNITS LE 14000

Creating Reports With TIBCO® WebFOCUS Language

 245

Types of Record Selection Tests

Example:

Selecting Values Outside a Range

The following illustrates how you can select values that are outside a range of values using the
LT and GT operators. In this example, only those employees whose salaries are less than
$12,000 and greater than $22,000 are included in the output.

TABLE FILE EMPLOYEE
PRINT CURR_SAL
BY LAST_NAME
WHERE CURR_SAL LT 12000 OR CURR_SAL GT 22000
END

The output is:

LAST_NAME               CURR_SAL
---------               --------
BANNING               $29,700.00
CROSS                 $27,062.00
GREENSPAN              $9,000.00
IRVING                $26,862.00
SMITH                  $9,500.00
STEVENS               $11,000.00

Missing Data Tests

When creating report requests, you may want to test for missing data. This type of test is most
useful when fields that have missing data also have the MISSING attribute set to ON in the
Master File. For information on missing data, see Handling Records With Missing Field Values
on page 1035, and the Describing Data With WebFOCUS Language manual.

Note: If a test value to screen on an alphanumeric field is a variable and you want to look for
missing instances, you must use _FOC_MISSING, instead of MISSING, as an alphanumeric
literal value in a test must be in single quotation marks, and 'MISSING' is the literal value
MISSING, not the MISSING value. The value _FOC_MISSING represents the MISSING value
whether it is in single quotation marks or not.

Syntax:

How to Test for Missing Data

{WHERE|IF} fieldname {EQ|IS} MISSING

where:

fieldname

Is any valid field name or alias.

EQ|IS

Are record selection operators. EQ and IS are synonyms.

246

4. Selecting Records for Your Report

Syntax:

How to Test for Existing Data

{WHERE|IF} fieldname {NE|IS-NOT} MISSING

where:

fieldname

Is any valid field name or alias.

NE|IS-NOT

Are record selection operators. NE and IS-NOT are synonyms.

Character String Screening With CONTAINS and OMITS

The CONTAINS and OMITS operators test alphanumeric fields when used with WHERE, and
both alphanumeric and text fields when used with IF. With CONTAINS, if the characters in the
given literal or literals appear anywhere within the characters of the field value, the test is
passed.

OMITS is the opposite of CONTAINS; if the characters of the given literal or literals appear
anywhere within the characters of the field's value, the test fails.

CONTAINS and OMITS tests are useful when you do not know the exact spelling of a value. As
long as you know that a specific string appears within the value, you can retrieve the desired
data.

Example:

Selecting Records With CONTAINS and OMITS

The following examples illustrate several ways to use the CONTAINS and OMITS operators. The
field name that is being tested must appear on the left side of the CONTAINS or OMITS
operator.

In this example, the characters JOHN are contained in JOHNSON, and are selected by the
following phrase:

WHERE LAST_NAME CONTAINS 'JOHN'

The LAST_NAME field may contain the characters JOHN anywhere in the field.

In this example, any last name without the string JOHN is selected:

WHERE LAST_NAME OMITS 'JOHN'

In this example, all names that contain the letters ING are retrieved.

TABLE FILE EMPLOYEE
LIST LAST_NAME AND FIRST_NAME
WHERE LAST_NAME CONTAINS 'ING'
END

Creating Reports With TIBCO® WebFOCUS Language

 247

Types of Record Selection Tests

The output is:

    LIST  LAST_NAME        FIRST_NAME
    ----  ---------        ----------
       1  BANNING          JOHN
       2  IRVING           JOAN

Screening on Masked Fields

A mask is an alphanumeric pattern that you supply for comparison to characters in a data
field. The data field must have an alphanumeric format (A). You can use the LIKE and NOT LIKE
or the IS and IS-NOT operators to perform screening on masked fields.

The wildcard characters for screening on masked fields with:

LIKE and NOT LIKE operators are % and _. The percent allows any following sequence of
zero or more characters. The underscore indicates that any character in that position is
acceptable. The LIKE operator is supported in expressions that are used to derive
temporary fields with either the DEFINE or COMPUTE command.

IS (or EQ) and IS-NOT (or NE) operators are $ and $*. The dollar sign indicates that any
character in that position is acceptable. The $* is shorthand for writing a sequence of
dollar signs to fill the end of the mask without specifying a length. This combination can
only be used at the end of the mask.

In IF clauses and those WHERE clauses that can be translated into one or more IF clauses,
you can treat the $ and $* characters as normal characters rather than wildcards by
issuing the SET EQTEST=EXACT command.

Note: The IS (or EQ) and IS-NOT (or NE) operators support screening based on a mask for fixed
length formats only. If the format is a variable length format, for example, AnV, use the LIKE or
NOT LIKE operator to screen based on a mask.

Syntax:

How to Screen Fields Based on a Mask (Using LIKE and NOT LIKE)

To search for records with the LIKE operator, use

WHERE field LIKE 'mask'

248

4. Selecting Records for Your Report

To reject records based on the mask value, use either

WHERE field NOT LIKE 'mask'

or

WHERE NOT field LIKE 'mask'

where:

field

Is any valid field name or alias.

mask

Is an alphanumeric or text character string you supply. There are two wildcard
characters that you can use in the mask. The underscore (_) indicates that any
character in that position is acceptable, and the percent sign (%) allows any following
sequence of zero or more characters.

For related information, see Restrictions on Masking Characters on page 250.

Syntax:

How to Screen Using LIKE and UNLIKE in an IF Phrase

To search for records with the LIKE operator, use

IF field LIKE 'mask1' [OR 'mask2'...]

To reject records based on the mask value, use

IF field UNLIKE 'mask1' [OR 'mask2' ...]

where:

field

Is any valid field name or alias.

mask1, mask2

Are the alphanumeric patterns you want to use for comparison. The single quotation
marks are required if the mask contains blanks. There are two wildcard characters
that you can use in a mask. The underscore (_) indicates that any character in that
position is acceptable, and the percent sign (%) allows any following sequence of zero
or more characters. Every other character in the mask accepts only itself in that
position as a match to the pattern.

Syntax:

How to Screen Fields Based on a Mask (Using IS and IS-NOT)

To search for records with the IS operator, use

{WHERE|IF} field {IS|EQ} 'mask'

Creating Reports With TIBCO® WebFOCUS Language

 249

Types of Record Selection Tests

To reject records based on the mask value, use

{WHERE|IF} field {IS-NOT|NE} 'mask'

where:

field

Is any valid field name or alias.

IS|IS-NOT

Are record selection operators. EQ is a synonym for IS. NE is a synonym for IS-NOT.

mask

Is an alphanumeric or text character string you supply. The wildcard characters that
you can use in the mask are the dollar sign ($) and the combination $*. The dollar
sign indicates that any character in that position is acceptable. The $* combination
allows any sequence of zero or more characters. The $* is shorthand for writing a
sequence of dollar signs to fill the end of the mask without specifying a specific
length. This combination can only be used at the end of the mask.

For related information, see Restrictions on Masking Characters on page 250.

Reference: Restrictions on Masking Characters

The wildcard characters dollar sign ($) and dollar sign with an asterisk ($*), which are used
with IS operators, are treated as literals with LIKE operators.

Masking with the characters $ and $* is not supported for compound WHERE phrases that
use the AND or OR logical operators.

Example:

Screening on Initial Characters

To list all employees who have taken basic-level courses, where every basic course begins with
the word BASIC, issue the following request:

TABLE FILE EMPLOYEE
PRINT COURSE_NAME COURSE_CODE
BY LAST_NAME BY FIRST_NAME
WHERE COURSE_NAME LIKE 'BASIC%'
END

250

The output is:

4. Selecting Records for Your Report

Example:

Screening on Characters Anywhere in a Field

If you want to see which employees have taken a FOCUS course, but you do not know where
the word FOCUS appears in the title, bracket the word FOCUS with wildcards (which is
equivalent to using the CONTAINS operator):

TABLE FILE EMPLOYEE
PRINT COURSE_NAME COURSE_CODE
BY LAST_NAME BY FIRST_NAME
WHERE COURSE_NAME LIKE '%FOCUS%'
END

The output is:

LAST_NAME        FIRST_NAME  COURSE_NAME                     COURSE_CODE
---------        ----------  -----------                     -----------
BLACKWOOD        ROSEMARIE   WHAT'S NEW IN FOCUS             202
JONES            DIANE       FOCUS INTERNALS                 203

If you want to list all employees who have taken a 20x-series course, and you know that all of
these courses have the same code except for the final character, issue the following request:

TABLE FILE EMPLOYEE
PRINT COURSE_NAME COURSE_CODE
BY LAST_NAME BY FIRST_NAME
WHERE COURSE_CODE LIKE '20_'
END

The output is:

LAST_NAME        FIRST_NAME  COURSE_NAME                     COURSE_CODE
---------        ----------  -----------                     -----------
BLACKWOOD        ROSEMARIE   WHAT'S NEW IN FOCUS             202
JONES            DIANE       FOCUS INTERNALS                 203
                             ADVANCED TECHNIQUES             201

Creating Reports With TIBCO® WebFOCUS Language

 251

Types of Record Selection Tests

Example:

Screening on Initial Characters and Specific Length

The following example illustrates how to screen on initial characters and specify the length of
the field value you are searching for. In this example, the WHERE phrase states that the last
name must begin with BAN and be seven characters in length (the three initial characters BAN
and the four placeholders, in this case, the dollar sign). The remaining characters in the field
(positions 8 through 15) must be blank.

TABLE FILE EMPLOYEE
PRINT LAST_NAME
WHERE LAST_NAME IS 'BAN$$$$'
END

The output is:

LAST_NAME
---------
BANNING

Example:

Screening on Records of Unspecified Length

To retrieve records with unspecified lengths, use the dollar sign followed by an asterisk ($*):

WHERE LAST_NAME IS 'BAN$*'

This phrase searches for last names that start with the letters BAN, regardless of the name
length. The characters $* reduce typing, and enable you to define a screen mask without
knowing the exact length of the field you wish to retrieve.

Syntax:

How to Deactivate Wildcard Characters

SET EQTEST = {WILDCARD|EXACT}

where:

WILDCARD

Treats the $ and $* characters as wildcard characters. WILDCARD is the default
value.

EXACT

Treats the $ and $* characters as normal characters, not wildcards, in IF tests and in
WHERE tests that can be translated to IF tests.

Example:

Selecting Records With SET EQTEST

The following request against the VIDEOTR2 data source creates two similar email addresses:

handy$man@usa.com, which has a dollar sign.

252

4. Selecting Records for Your Report

handyiman@usa.com, which has the letter i in the same position as the $ character in the
other email address.

DEFINE FILE VIDEOTR2
SMAIL/A18= IF EMAIL EQ 'handyman@usa.com'
           THEN 'handyiman@usa.com'
           ELSE EMAIL;
SMAIL/A18 = STRREP(18,SMAIL,1,'_',1,'$',18,SMAIL);
END
TABLE FILE VIDEOTR2
PRINT SMAIL
BY LASTNAME BY FIRSTNAME
WHERE SMAIL EQ 'handy$man@usa.com'
ON TABLE SET EQTEST WILDCARD
END

With SET EQTEST=WILDCARD (the default), the WHERE test WHERE SMAIL IS 'handy
$man@usa.com' returns both the record with the $ in the address and the record with the
letter i in the address because the $ is treated as a wildcard character, and any character in
that position causes the record to pass the screening test:

LASTNAME         FIRSTNAME   SMAIL
--------         ---------   -----
HANDLER          EVAN        handy$man@usa.com
                             handyiman@usa.com

Changing the ON TABLE SET command to ON TABLE SET EQTEST EXACT returns just the ONE
email address with the $ character because the dollar sign is now treated as a normal
character and only passes the test if there is an exact match:

LASTNAME         FIRSTNAME   SMAIL
--------         ---------   -----
HANDLER          EVAN        handy$man@usa.com

Using an Escape Character for LIKE

You can use an escape character in the LIKE syntax to treat the masking characters (% and _)
as literals within the search pattern, rather than as wildcards. This technique enables you to
search for these characters in the data. For related information, see Screening on Masked
Fields on page 248.

Creating Reports With TIBCO® WebFOCUS Language

 253

Types of Record Selection Tests

Syntax:

How to Use an Escape Character in a WHERE Phrase

Any single character can be used as an escape character, if prefaced with the word ESCAPE

WHERE fieldname LIKE 'mask' ESCAPE 'c'

where:

fieldname

Is any valid field name or alias to be evaluated in the selection test.

mask

Is the search pattern that you supply. The single quotation marks are required.

c

Is any single character that you identify as the escape character. If you embed the
escape character in the mask, before a % or _, the % or _ character is treated as a
literal, rather than as a wildcard. The single quotation marks are required.

Syntax:

How to Specify an Escape Character for a Mask in an IF Phrase

You can assign any single character as an escape character by prefacing it with the word
ESCAPE in the LIKE or UNLIKE syntax

IF field {LIKE|UNLIKE} 'mask1' ESCAPE 'a' [OR 'mask2' ESCAPE 'b' ...

where:

field

Is any valid field name or alias to be evaluated in the selection test.

mask1, mask2

Are search patterns that you supply. The single quotation marks are required.

a, b ...

Are single characters that you identify as escape characters. Each mask can specify
its own escape character or use the same character as other masks. If you embed the
escape character in the mask, before a % or _, the % or _ character is treated as a
literal, rather than as a wildcard. The single quotation marks are required if the mask
contains blanks.

Reference: Usage Notes for Escape Characters

The use of an escape character in front of any character other than %, _, and itself is
ignored.

The escape character itself can be escaped, thus becoming a normal character in a string
(for example, 'abc\%\\').

254

4. Selecting Records for Your Report

Only one escape character can be used per LIKE phrase in a WHERE phrase.

The escape character is only in effect when the ESCAPE syntax is included in the LIKE
phrase.

Every LIKE phrase can provide its own escape character.

If a WHERE criterion is used with literal OR phrases, the ESCAPE must be on the first OR
phrase, and applies to all subsequent phrases in that WHERE expression. For example:

WHERE field LIKE 'ABCg_' ESCAPE 'g' OR 'ABCg%' OR 'g%ABC'

Example:

Using the Escape Character in a WHERE Phrase

The VIDEOTR2 data source contains an email address field. To search for the email address
with the characters 'handy_' you can issue the following request:

TABLE FILE VIDEOTR2
PRINT CUSTID LASTNAME FIRSTNAME EMAIL
WHERE EMAIL LIKE 'handy_%'
END

Because the underscore character functions as a wildcard character, this request returns two
instances, only one of which contains the underscore character.

The output is:

CUSTID  LASTNAME         FIRSTNAME   EMAIL
------  --------         ---------   -----
0944    HANDLER          EVAN        handy_man@usa.com
0944    HANDLER          EVAN        handyman@usa.com

To retrieve only the instance that contains the underscore character, you must indicate that
the underscore should be treated as a normal character, not a wildcard. The following request
retrieves only the instance with the underscore character in the email field:

TABLE FILE VIDEOTR2
PRINT CUSTID LASTNAME FIRSTNAME EMAIL
WHERE EMAIL LIKE 'handy\_%' ESCAPE '\'
END

The output is:

CUSTID  LASTNAME         FIRSTNAME   EMAIL
------  --------         ---------   -----
0944    HANDLER          EVAN        handy_man@usa.com

Creating Reports With TIBCO® WebFOCUS Language

 255

Types of Record Selection Tests

Example:

Using an Escape Character in an IF Phrase

The VIDEOTR2 data source contains an email address field. To search for email addresses
with the characters 'handy_' you can issue the following request:

TABLE FILE VIDEOTR2
PRINT CUSTID LASTNAME FIRSTNAME EMAI
IF EMAIL LIKE 'handy_%'
END

Because the underscore character functions as a wildcard character, this request returns two
instances, only one of which contains the underscore character.

The output is:

CUSTID  LASTNAME         FIRSTNAME   EMAIL
------  --------         ---------   -----
0944    HANDLER          EVAN        handy_man@usa.com
0944    HANDLER          EVAN        handyman@usa.com

To retrieve only the instance that contains the underscore character, you must indicate that
the underscore should be treated as a normal character, not a wildcard. The following request
retrieves only the instance with the underscore character in the email field:

TABLE FILE VIDEOTR2
PRINT CUSTID LASTNAME FIRSTNAME EMAI
IF EMAIL LIKE 'handy\_%' ESCAPE '\'
END

The output is:

CUSTID  LASTNAME         FIRSTNAME   EMAIL
------  --------         ---------   -----
0944    HANDLER          EVAN        handy_man@usa.com

Qualifying Parent Segments Using INCLUDES and EXCLUDES

You can test whether instances of a given field in a child segment include or exclude all literals
in a list using the INCLUDES and EXCLUDES operators. INCLUDES and EXCLUDES retrieve only
parent records. You cannot print or list any field in the same segment as the field specified for
the INCLUDES or EXCLUDES test.

Note: INCLUDES and EXCLUDES work only with multi-segment FOCUS data sources.

Reference: Usage Notes for INCLUDES and EXCLUDES

Literals containing embedded blanks must be enclosed in single quotation marks.

The total number of literals must be 31 or less.

To use more than one INCLUDES or EXCLUDES phrase in a request, begin each phrase on
a separate line.

256

4. Selecting Records for Your Report

You can connect the literals you are testing for with ANDs and ORs; however, the ORs are
changed to ANDs.

Example:

Selecting Records With INCLUDES and EXCLUDES

A request that contains the phrase

WHERE JOBCODE INCLUDES A01 OR B01

returns employee records with JOBCODE instances for both A01 and B01, as if you had used
AND.

In the following example, for a record to be selected, its JOBCODE field must have values of
both A01 and B01:

WHERE JOBCODE INCLUDES A01 AND B01

If either one is missing, the record is not selected for the report.

If the selection criterion is

WHERE JOBCODE EXCLUDES A01 AND B01

every record that does not have both values is selected for the report.

In the CAR data source, only England produces Jaguars and Jensens, and so the request

TABLE FILE CAR
PRINT COUNTRY
WHERE CAR INCLUDES JAGUAR AND JENSEN
END

generates this output:

COUNTRY
-------
ENGLAND

Selections Based on Group Key Values

Some data sources use group keys. A group key is a single key composed of several fields.
You can use a group name to refer to group key fields.

To select records based on a group key value, you need to supply the value of each field. The
values must be separated by the slash character (/).

Note that a WHERE phrase that refers to a group field cannot be used in conjunction with AND
or OR. For related information, see Using Compound Expressions for Record Selection on page
235.

Creating Reports With TIBCO® WebFOCUS Language

 257

Setting Limits on the Number of Records Read

Example:

Selecting Records Using Group Keys

Suppose that a data source has a group key named PRODNO, which contains three separate
fields. The first is stored in alphanumeric format, the second as a packed decimal, and the
third as an integer. A screening phrase on this group might be:

WHERE PRODNO EQ 'RS/62/83'

Setting Limits on the Number of Records Read

For some reports, a limited number of records is satisfactory. When the specified number of
records is retrieved, record retrieval can stop. This is useful when:

You are designing a new report, and you need only a few records from the actual data
source to test your design.

The database administrator needs to limit the size of reports by placing an upper limit on
retrieval from very large data sources. This limit is attached to the user password.

You know the number of records that meet the test criteria. You can specify that number so
that the search does not continue beyond the last record that meets the criteria. For
example, suppose only ten employees use electronic transfer of funds, and you want to
retrieve only those records. The record limit would be ten, and retrieval would stop when
the tenth record is retrieved. The data source would not be searched any further.

Syntax:

How to Limit the Number of Records Read

There are two ways to limit the number of records retrieved. You can use

WHERE RECORDLIMIT EQ n

where:

n

Is a number greater than 0, and indicates the number of records to be retrieved. This
syntax can be used with FOCUS and non-FOCUS data sources.

For all non-FOCUS data sources, you can also use

WHERE READLIMIT EQ n

where:

n

Is a number greater than 0, and indicates the number of read operations (not records)
to be performed. For details, see the appropriate data adapter manual.

258

4. Selecting Records for Your Report

Tip: If an attempt is made to apply the READLIMIT test to a FOCUS data source, the request is
processed correctly, but the READLIMIT phrase is ignored.

Note: Using SET RECORDLIMIT disables AUTOINDEX.

Example:

Limiting the Number of Records Read

The following request retrieves four records, generating a four-line report:

TABLE FILE EMPLOYEE
PRINT LAST_NAME AND FIRST_NAME AND EMP_ID
WHERE RECORDLIMIT EQ 4
END

The output is:

LAST_NAME        FIRST_NAME  EMP_ID
---------        ----------  ------
STEVENS          ALFRED      071382660
SMITH            MARY        112847612
JONES            DIANE       117593129
SMITH            RICHARD     119265415

Selecting Records Using IF Phrases

The IF phrase selects records to be included in a report, and offers a subset of the
functionality of WHERE. For a list of supported IF operators, see Operators Supported for
WHERE and IF Tests on page 236.

Tip: Unless you specifically require IF syntax (for example, to support legacy applications), we
recommend using WHERE.

Syntax:

How to Select Records Using the IF Phrase

IF fieldname operator literal [OR literal]

where:

fieldname

Is the field you want to test (the test value).

operator

Is the type of selection operator you want. Valid operators are described in Operators
Supported for WHERE and IF Tests on page 236.

literal

Can be the MISSING keyword (as described in Missing Data Tests on page 246) or
alphanumeric or numeric values that are in your data source, with the word OR
between values.

Creating Reports With TIBCO® WebFOCUS Language

 259

Reading Selection Values From a File

Note that all literals that contain blanks (for example, New York City) and all date and date-
time literals must be enclosed within single quotation marks.

Note: The IF phrase alone cannot be used to create compound expressions by connecting
simple expressions with AND and OR logical operators. Compound logic requires that the IF
phrase be used with the DEFINE command, as described in Using Expressions on page 429.
You can accomplish this more easily with WHERE. See Using Compound Expressions for Record
Selection on page 235.

Example:

Using Multiple IF Phrases

You can use as many IF phrases as necessary to define all your selection criteria, as
illustrated in the following example:

TABLE FILE EMPLOYEE
PRINT EMP_ID LAST_NAME
IF SALARY GT 20000
IF DEPARTMENT IS MIS
IF LAST_NAME IS CROSS OR BANNING
END

All of these criteria must be satisfied in order for a record to be included in a report. The
output is:

EMP_ID     LAST_NAME
------     ---------
818692173  CROSS

Reading Selection Values From a File

Instead of typing literal test values in a WHERE or IF phrase, you can store them in a file and
refer to the file in the report request. You can then select records based on equality or
inequality tests on values stored in the file.

This method has the following advantages:

You can save time by coding a large set of selection values once, then using these values
as a set in as many report requests as you wish. You also ensure consistency by
maintaining the criteria in just one location.

260

4. Selecting Records for Your Report

If the selection values already exist in a data source, you can quickly create a file of
selection values by generating a report and saving the output in a HOLD or SAVE file. You
can then read selection values from that file.

Values from a HOLD file (with a data description) can be in either BINARY format (the
default) or ALPHA (simple character) format. If you use a SAVE file, it must be in ALPHA
format (the default). Using a SAVB file is only valid for alphanumeric values. For information
on HOLD and SAVE files, see Saving and Reusing Your Report Output on page 471.

Note that in z/OS, a HOLD file in BINARY format that is used for selection values must be
allocated to ddname HOLD (the default). The other extract files used for this purpose can
be allocated to any ddname.

You can include entries with mixed-case and special characters.

Syntax:

How to Read Selection Values From a File: WHERE field IN file

WHERE [NOT] fieldname IN FILE file

where:

fieldname

Is the name of the selection field. It can be any real or temporary field in the data
source.

file

Is the name of the file.

Two-part names (app/file) are not supported. The file name is the ddname assigned by a
DYNAM or TSO ALLOCATE command for z/OS, or a FILEDEF command for other
environments.

For related information, see Usage Notes for Reading Values From a File on page 262.

Syntax:

How to Read Selection Values From a File: WHERE field operator (file)

WHERE field1 operator1 (file1) [{OR|AND} field2 operator2 (file2) ... ]

where:

field1, field2

Are any valid field names or aliases.

operator1, operator2

Can be the EQ, IS, NE, or IS-NOT operator.

Creating Reports With TIBCO® WebFOCUS Language

 261

Reading Selection Values From a File

file1, file1

Are the names of the files.

Two-part names (app/file) are not supported. The file name is the ddname assigned by a
DYNAM or TSO ALLOCATE command for z/OS, or a FILEDEF command for other
environments.

Syntax:

How to Read Selection Values From a File: IF

IF fieldname operator (file) [OR (file) ... ]

where:

fieldname

Is any valid field name or alias.

operator

Is the EQ, IS, NE, or IS-NOT operator (see Operators Supported for WHERE and IF Tests
on page 236).

file

Is the name of the file.

Two-part names (app/file) are not supported. The file name is the ddname assigned by a
DYNAM or TSO ALLOCATE command for z/OS, or a FILEDEF command for other
environments.

Reference: Usage Notes for Reading Values From a File

In order to read selection criteria from a file, the file must comply with the following rules:

Each value in the file must be on a separate line.

For IF, more information can appear on a line, but only the first data value encountered on
the line is used.

The selection value must start in column one.

The values are assumed to be in character format, unless the file name is HOLD, and
numeric digits are converted to internal computational numbers where needed (for
example, binary integer).

The maximum number of values is 32,767.

For WHERE, alphanumeric values with embedded blanks or any mathematical operator (-, +,
*, /) must be enclosed in single quotation marks.

262

4. Selecting Records for Your Report

For WHERE, when a compound WHERE phrase uses IN FILE more than once, the specified
files must have the same record formats.

If your list of literals is too large, an error is displayed.

For IF, sets of file names may be used, separated by the word OR, and with WHERE, AND.
The file names cannot be prefaced with app names. Actual literals may also be mixed with
the file names. For example:

IF fieldname operator (filename) OR literal...etc...

Example:

Reading Selection Values From a File (WHERE field IN file)

Create a file named EXPER, which contains the values B141 and B142.

This request uses selection criteria from the file EXPER. You must allocate or FILEDEF the
EXPER file prior to running the request. For example, if the file is named exper.ftm and it is in
the baseapp application, you can issue the following FILEDEF command:

FILEDEF EXPER DISK baseapp/exper.ftm

All records for which PRODUCT_ID has a value of B141 or B142 are selected:

TABLE FILE GGPRODS
SUM UNIT_PRICE
BY PRODUCT_DESCRIPTION
WHERE PRODUCT_ID IN FILE EXPER
END

If you include the selection criteria directly in the request, the WHERE phrase specifies the
values explicitly:

WHERE PRODUCT_DESCRIPTION EQ 'B141' or 'B142'

The output is:

                     Unit
Product              Price
-------              -----
French Roast         81.00
Hazelnut             58.00

Example:

Reading Selection Values From a File With WHERE field operator (file)

The following request against the GGPRODS data source creates a HOLD file named EXPER1
that contains product IDs B141, B142, B143, and B144.

Creating Reports With TIBCO® WebFOCUS Language

 263

Reading Selection Values From a File

TABLE FILE GGPRODS
BY PRODUCT_ID BY PRODUCT_DESCRIPTION
WHERE PRODUCT_ID EQ 'B141' OR 'B142' OR 'B143' OR 'B144'
ON TABLE HOLD AS EXPER1 FORMAT ALPHA
END

The following request against the GGPRODS data source creates a HOLD file named EXPER2
that contains product IDs B144, F101, and F102.

TABLE FILE GGPRODS
BY PRODUCT_ID BY PRODUCT_DESCRIPTION
WHERE PRODUCT_ID EQ 'B144' OR 'F101' OR 'F102'
ON TABLE HOLD AS EXPER2 FORMAT ALPHA
END

The following request selects the values that exist in both EXPER1 AND EXPER2.

TABLE FILE GGPRODS
SUM PRODUCT_DESCRIPTION
BY PRODUCT_ID
WHERE PRODUCT_ID EQ (EXPER1) AND PRODUCT_ID IS (EXPER2)
ON TABLE SET PAGE NOPAGE
END

The output is:

Product
Code     Product
-------  -------
B144     Kona

Example:

Reading Selection Values From a File (IF)

Create a file named EXPER, which contains the values B141 and B142.

This request uses selection criteria from the file EXPER. All records for which PRODUCT_ID has
a value of B141 or B142 are selected:

TABLE FILE GGPRODS
SUM UNIT_PRICE
BY PRODUCT_DESCRIPTION
IF PRODUCT_ID IS (EXPER)
END

If you include the selection criteria directly in the request, the IF phrase specifies the values
explicitly:

IF PRODUCT_DESCRIPTION EQ 'B141' or 'B142'

264

4. Selecting Records for Your Report

The output is:

                     Unit
Product              Price
-------              -----
French Roast         81.00
Hazelnut             58.00

Assigning Screening Conditions to a File

You can assign screening conditions to a data source, independent of a request, and activate
these screening conditions for use in report requests against the data source.

A filter is a packet of definitions that resides at the file level, containing WHERE and/or IF
criteria. Whenever a report request is issued against a data source, all filters that have been
activated for that data source are in effect. WHERE or IF syntax that is valid in a report request
is also valid in a filter.

A filter can be declared at any time before the report request is run. The filters are available to
subsequent requests during the session in which the filters have been run. For details, see
How to Declare a Filter on page 266.

Filters allow you to:

Declare a common set of screening conditions that apply each time you retrieve data from
a data source. You can declare one or more filters for a data source.

Declare a set of screening conditions and dynamically turn them on and off.

Limit access to data without specifying rules in the Master File.

In an interactive environment, filters also reduce repetitive ad hoc typing.

Note: Simply declaring a filter for a data source does not make it active. A filter must be
activated with a SET command. For details, see How to Activate or Deactivate Filters on page
268.

Creating Reports With TIBCO® WebFOCUS Language

 265

Assigning Screening Conditions to a File

Syntax:

How to Declare a Filter

A filter can be described by the following declaration

 FILTER FILE filename [CLEAR|ADD]
    [filter-defines;]
    NAME=filtername1 [,DESC=text]
    where-if phrases    .
    .
    .
    NAME=filternamen [,DESC=text]
    where-if phrases END

where:

filename

Is the name of the Master File to which the filters apply.

CLEAR

Deletes any existing filter phrases, including any previously defined virtual fields.

ADD

Enables you to add new filter phrases to an existing filter declaration without clearing
previously defined filters.

filter-defines

Are virtual fields declared for use in filters. For more information, see Usage Notes for
Virtual Fields Used in Filters on page 266.

filtername1...filternamen

Is the name by which the filter is referenced in subsequent SET FILTER commands.
This name may be up to 66 characters long and must be unique for a particular file
name.

text

Describes the filter for documentation purposes. Text must fit on one line.

where-if phrases

Are screening conditions that can include all valid syntax. They may refer to data
source fields and virtual fields in the Master File. They may not refer to virtual fields
declared using a DEFINE command, or to other filter names.

Reference: Usage Notes for Virtual Fields Used in Filters

Virtual fields used in filters:

Are exclusively local to (or usable by) filters in a specific filter declaration.

Cannot be referenced in a DEFINE or TABLE command.

266

4. Selecting Records for Your Report

Support any syntax valid for virtual fields in a DEFINE command.

Cannot reference virtual fields in a DEFINE command, but can reference virtual fields in the
Master File.

Do not count toward the display field limit, unlike virtual fields in DEFINE commands.

Must all be declared before the first named filter.

Must each end with a semi-colon.

Cannot be enclosed between the DEFINE FILE and END commands.

Cannot reuse a virtual field name for a the same file.

Example:

Declaring Filters

The first example creates the filter named UK, which consists of one WHERE condition. It also
adds a definition for the virtual field MARK_UP to the set of virtual fields already being used in
filters for the CAR data source.

When a report request is issued for CAR, with UK activated, the condition WHERE MARK_UP is
greater than 1000 is automatically added to the request.

Note: The virtual field MARK_UP cannot be explicitly displayed or referenced in the TABLE
request.

FILTER FILE CAR ADD
MARK_UP/D7=RCOST-DCOST;
NAME=UK
WHERE MARK_UP GT 1000
END

The second example declares three named filters for the CAR data source: ASIA, UK, and
LUXURY. The filter ASIA contains a textual description, for documentation purposes only.
CLEAR, on the first line, erases any previously existing filters for CAR, as well any previously
defined virtual fields used in filters for CAR, before it processes the new definitions.

FILTER FILE CAR CLEAR
NAME=ASIA,DESC=Asian cars only
IF COUNTRY EQ JAPAN
NAME=UK
IF COUNTRY EQ ENGLAND
NAME=LUXURY
IF RETAIL_COST GT 50000
END

Creating Reports With TIBCO® WebFOCUS Language

 267

Assigning Screening Conditions to a File

Syntax:

How to Activate or Deactivate Filters

Filters can be activated and deactivated with the command

SET FILTER= {*|xx[yy zz]} IN {file|*} {ON|OFF}

where:

*

Denotes all declared filters. This is the default value.

xx, yy, zz

Are the names of filters as declared in the NAME = syntax of the FILTER FILE
command.

file

Is the name of the data source to which you are assigning screening conditions. *
denotes all data sources.

ON

OFF

Activates all (*) or specifically named filters for the data source or all data sources
(*). The maximum number of filters you can activate for a data source is limited by the
number of WHERE/IF phrases that the filters contain, not to exceed the limit of
WHERE/IF criteria in any single report request.

Deactivates all (*) or specifically named filters for the data source or all data sources
(*). OFF is the default value.

Note: The SET FILTER command is limited to one line. To activate more filters than fit on one
line, issue additional SET FILTER commands. As long as you specify ON, the effect is
cumulative.

Example:

Activating and Deactivating Filters

The following commands activate A, B, C, D, E, F, and deactivate G (assuming that it was set
ON, previously):

SET FILTER = A B C IN CAR ON
SET FILTER = D E F IN CAR ON
SET FILTER = G IN CAR OFF

268

The following commands activate some filters and deactivate others:

4. Selecting Records for Your Report

SET FILTER = UK LUXURY IN CAR ON
...
TABLE FILE CAR
PRINT COUNTRY MODEL RETAIL_COST
END
...
SET FILTER = LUXURY IN CAR OFF
TABLE FILE CAR
PRINT COUNTRY MODEL RETAIL_COST
END

The first SET FILTER command activates the filters UK and LUXURY, assigned to the CAR data
source, and applies their screening conditions to any subsequent report request against the
CAR data source.

The second SET FILTER command deactivates the filter LUXURY for the CAR data source.
Unless LUXURY is reactivated, any subsequent report request against CAR will not apply the
conditions in LUXURY, but will continue to apply UK.

Syntax:

How to Query the Status of Filters

To determine the status of existing filters, use

? FILTER [{file|*}] [SET] [ALL]]

where:

file

Is the name of a Master File.

*

SET

ALL

Displays filters for all Master Files for which filters have been declared.

Displays only active filters.

Displays all information about the filter, including its description and the exact
WHERE/IF definition.

Creating Reports With TIBCO® WebFOCUS Language

 269

Assigning Screening Conditions to a File

Example:

Querying Filters

To query filters, issue the following command:

FILTER FILE CAR CLEAR
NAME=BOTH, DESC=Asian and British cars only
IF COUNTRY EQ JAPAN AND ENGLAND
END
SET FILTER =BOTH IN CAR ON
TABLE FILE CAR
PRINT CAR RETAIL_COST
BY COUNTRY
END

The output is:

COUNTRY     CAR               RETAIL_COST
-------     ---               -----------
ENGLAND     JAGUAR                  8,878
            JAGUAR                 13,491
            JENSEN                 17,850
            TRIUMPH                 5,100
JAPAN       DATSUN                  3,139
            TOYOTA                  3,339

The following example queries filters for all data sources:

? FILTER

If no filters are defined, the following message displays:

NO FILTERS DEFINED

If filters are defined, the following screen displays:

Set File     Filter name Description
--- -------- ----------- -----------------------------------
    CAR      ROB         Rob's selections
*   CAR      PETER       Peter's selections for CAR
*   EMPLOYEE DAVE        Dave's tests
    EMPLOYEE BRAD        Brad's tests

To query filters for the CAR data source, issue:

? FILTER CAR

If no filters are defined for the CAR data source, the following message displays:

NO FILTERS DEFINED FOR FILE NAMED CAR

270

4. Selecting Records for Your Report

If filters are defined for the CAR data source, the following screen displays:

Set File     Filter name Description
--- -------- ----------- -----------------------------------
    CAR      ROB         Rob's selections
*   CAR      PETER       Peter's selections for CAR

To see all active filters, issue the following command:

? FILTER * SET

The output is:

Set File     Filter name Description
--- -------- ----------- -----------------------------------
*   CAR      PETER       Peter's selections for CAR
*   EMPLOYEE DAVE        Dave's tests

The asterisk in the first column indicates that a filter is activated.

Preserving Filters Across Joins

By default, filters defined on the host data source are cleared by a JOIN command. However,
filters can be maintained when a JOIN command is issued, by issuing the SET
KEEPFILTERS=ON command.

Setting KEEPFILTERS to ON reinstates filter definitions and their individual declared status
after a JOIN command. The set of filters and virtual fields defined prior to each join is called a
context (see your documentation on SET KEEPDEFINES and on DEFINE FILE SAVE for
information about contexts as they relate to virtual fields). Each new JOIN or DEFINE FILE
command creates a new context.

If a new filter is defined after a JOIN command, it cannot have the same name as any
previously defined filter unless you issue the FILTER FILE command with the CLEAR option. The
CLEAR option clears all filter definitions for that data source in all contexts.

When a JOIN is cleared, each filter definition that was in effect prior to the JOIN command and
that was not cleared, is reinstated with its original status. Clearing a join by issuing the JOIN
CLEAR join_name command removes all of the contexts and filter definitions that were created
after the JOIN join_name command was issued.

Note: When an error occurs because of a reference to field that does not exist in the original
FILTER FILE, the filter is disabled even though KEEPFILTERs is set to ON.

Creating Reports With TIBCO® WebFOCUS Language

 271

Assigning Screening Conditions to a File

Syntax:

How to Preserve Filter Definitions With KEEPFILTERS

SET KEEPFILTERS = {OFF|ON}

where:

OFF

ON

Does not preserve filters issued prior to a join. OFF is the default value.

Preserves filters across joins.

Example:

Preserving Filters With KEEPFILTERS

The first filter, UNITPR, is defined prior to issuing any joins, but after setting KEEPFILTERS to
ON:

SET KEEPFILTERS = ON
FILTER FILE VIDEOTRK
PERUNIT/F5 = TRANSTOT/QUANTITY;
NAME=UNITPR
WHERE PERUNIT GT 2
WHERE LASTNAME LE 'CRUZ'
END

The ? FILTER command shows that the filter named UNITPR was created but not activated
(activation is indicated by an asterisk in the SET column of the display:

? FILTER

SET FILE     FILTER NAME DESCRIPTION
--- -------- ----------- ---------------------------------
    VIDEOTRK UNITPR

Next, the filter is activated:

SET FILTER= UNITPR IN VIDEOTRK ON

The ? FILTER query shows that the filter is now activated:

? FILTER

SET FILE     FILTER NAME DESCRIPTION
--- -------- ----------- ---------------------------------
*   VIDEOTRK UNITPR

The following TABLE request is issued against the filtered data source:

TABLE FILE VIDEOTRK
SUM QUANTITY TRANSTOT BY LASTNAME
END

272



4. Selecting Records for Your Report

The output shows that the TABLE request retrieved only the data that satisfies the UNITPR
filter:

NUMBER OF RECORDS IN TABLE=        6  LINES=      3
ACCESS LIMITED BY FILTERS

PAUSE.. PLEASE ISSUE CARRIAGE RETURN WHEN READY

LASTNAME         QUANTITY  TRANSTOT
--------         --------  --------
CHANG                   3     31.00
COLE                    2     18.98
CRUZ                    2     16.00

Now, the VIDEOTRK data source is joined to the MOVIES data source. The ? FILTER query
shows that the join did not clear the UNITPR filter:

JOIN MOVIECODE IN VIDEOTRK TO ALL MOVIECODE IN MOVIES AS J1

The ? FILTER command shows that the UNITPR filter still exists and is still activated:

? FILTER

SET FILE     FILTER NAME DESCRIPTION
--- -------- ----------- ---------------------------------
*   VIDEOTRK UNITPR

Next a new filter, YEARS1, is created and activated for the join between VIDEOTRK and
MOVIES:

FILTER FILE VIDEOTRK
YEARS/I5 = (EXPDATE - TRANSDATE)/365;
NAME=YEARS1
WHERE YEARS GT 1
END
SET FILTER= YEARS1 IN VIDEOTRK ON

The ? FILTER query shows that both the UNITPR and YEARS1 filters exist and are activated:

? FILTER

SET FILE     FILTER NAME DESCRIPTION
--- -------- ----------- ---------------------------------
*   VIDEOTRK UNITPR
*   VIDEOTRK YEARS1

Creating Reports With TIBCO® WebFOCUS Language

 273





VSAM Record Selection Efficiencies

Now, J1 is cleared. The output of the ? FILTER command shows that the YEARS1 filter that
was created after the JOIN command was issued no longer exists. The UNITPR filter created
prior to the JOIN command still exists with its original status:

JOIN CLEAR J1
? FILTER

SET FILE     FILTER NAME DESCRIPTION
--- -------- ----------- ---------------------------------
*   VIDEOTRK UNITPR

VSAM Record Selection Efficiencies

The most efficient way to retrieve selected records from a VSAM KSDS data source is by
applying an IF screening test against the primary key. This results in a direct reading of the
data using the data source's index. Only those records that you request are retrieved from the
file. The alternative method of retrieval, the sequential read, forces the data adapter to retrieve
all the records into storage.

Selection criteria that are based on the entire primary key, or on a subset of the primary key,
cause direct reads using the index. A partial key is any contiguous part of the primary key
beginning with the first byte.

IF selection tests performed against virtual fields can take advantage of these efficiencies as
well, if the full or partial key is embedded in the virtual field.

The EQ and IS relations realize the greatest performance improvement over sequential reads.
When testing on a partial key, equality logic is used to retrieve only the first segment instance
of the screening value. To retrieve subsequent instances, NEXT logic is used.

Screening relations GE, FROM, FROM-TO, GT, EXCEEDS, IS-MORE-THAN, and NOT-FROM-TO all
obtain some benefit from direct reads. The following example uses the index to find the record
containing primary key value 66:

IF keyfield GE 66

It then continues to retrieve records by sequential processing, because VSAM stores records in
ascending key sequence. The direct read is not attempted when the IF screening conditions
NE, IS-NOT, CONTAINS, OMITS, LT, IS-LESS-THAN, LE, and NOT-FROM are used in the report
request.

Reporting From Files With Alternate Indexes

Similar performance improvement is available for ESDS and KSDS files that use alternate
indexes. An alternate index provides access to records in a key sequenced data set based on
a key other than the primary key.

274


4. Selecting Records for Your Report

All benefits and limitations inherent with screening on the primary or partial key are applicable
to screening on the alternate index or partial alternate index.

Note: It is not necessary to take an explicit indexed view to use the index.

Creating Reports With TIBCO® WebFOCUS Language

 275

VSAM Record Selection Efficiencies

276

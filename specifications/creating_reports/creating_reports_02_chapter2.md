Chapter2

Displaying Report Data

Reporting, at the simplest level, retrieves field values from a data source and displays
those values. There are three ways to do this:

List each field value (PRINT and LIST commands).

Add all the values and display the sum (SUM command).

Count all the values and display the quantity (COUNT command).

In this chapter:

Using Display Commands in a Request

Displaying Individual Values

Adding Values

Counting Values

Expanding Byte Precision for COUNT and LIST

Maximum Number of Display Fields Supported in a Request

Manipulating Display Fields With Prefix Operators

Displaying Pop-up Field Descriptions for Column Titles

Using Display Commands in a Request

The four display commands (PRINT, LIST, SUM, and COUNT) are also known as verbs. These
commands are flexible; you can report from several fields using a single command, and
include several different display commands in a single report request.

Creating Reports With TIBCO® WebFOCUS Language

 39

Using Display Commands in a Request

Syntax:

How to Use Display Commands in a Request

display [THE] [SEG.]fieldname1 [AND] [THE] fieldname2 ...

or

display *

where:

display

Is the PRINT, LIST, SUM, or COUNT command. WRITE and ADD are synonyms of SUM
and can be substituted for it.

SEG.

Displays all fields in a segment (a group of related fields in a Master File). The field
name you specify can be any field in the segment.

fieldname

Is the name of the field to be displayed in the report.

The maximum number of display fields your report can contain is determined by a
combination of factors. For details, see Maximum Number of Display Fields Supported in a
Request on page 55.

The fields appear in the report in the same order in which they are specified in the report
request. For example, the report column for fieldname1 appears first, followed by the
report column for fieldname2.

The field to be displayed is also known as the display field.

AND

THE

*

Is optional and is used to enhance readability. It can be used between any two field
names, and does not affect the report.

Is optional and is used to enhance readability. It can be used before any field name,
and does not affect the report.

Applies the display command to every field in the left path of the data source.

Note: The SEG. and * options do not display virtual fields. To print virtual fields, explicitly
reference them in the PRINT statement (PRINT * virtual field name). This is true even if the
virtual field name redefines a real field.

40

Displaying Individual Values

2. Displaying Report Data

The display commands LIST and PRINT list the individual values of the fields you specify in
your report request. LIST numbers the items in the report. PRINT does not number the items.

You can easily display all of the fields in the data source by specifying an asterisk (*) wildcard
instead of a specific field name, as described in Displaying All Fields on page 42.

For all PRINT and LIST requests, the number of records retrieved and the number of lines
displayed are the same. In addition, there is no order to the report rows. The PRINT and LIST
commands display all the values of the selected fields found in the data source in the order in
which they are accessed. The order in which data is displayed may be affected by the
AUTOPATH setting. For more information, see Optimizing Retrieval Speed for FOCUS Data
Sources on page 1932, and the documentation on SET parameters in the Developing Reporting
Applications manual.

In general, when using PRINT or LIST, the order of the values displayed in the report depends
on whether or not the field is a key field, as described in the Describing Data With WebFOCUS
Language manual.

Alternatively, you can sort the values using the BY or ACROSS sort phrases. When LIST is used
in a request that includes a sort phrase, the list counter is reset to 1 every time the value in
the outermost sort field changes. For more information on sorting, see Sorting Tabular Reports
on page 87.

PRINT * or PRINT SEG.* prints only the real fields in the Master File. To print virtual fields,
explicitly reference them in the PRINT statement (PRINT * virtual field name). This is true even
if the virtual field name is a re-defines of a real field.

For PRINT and LIST syntax, see Using Display Commands in a Request on page 39.

Example:

Displaying Individual Field Values

To display the values of individual fields, use the PRINT command. The following request
displays the values of two fields, LAST_NAME and FIRST_NAME, for all employees.

TABLE FILE EMPLOYEE
PRINT LAST_NAME AND FIRST_NAME
END

The following shows the report output.

Creating Reports With TIBCO® WebFOCUS Language

 41

Displaying Individual Values

LAST_NAME
---------

STEVENS
SMITH
JONES
SMITH
BANNING
IRVING
ROMANS
MCCOY
BLACKWOOD
MCKNIGHT
GREENSPAN
CROSS

FIRST_NAME
----------

ALFRED
MARY
DIANE
RICHARD
JOHN
JOAN
ANTHONY
JOHN
ROSEMARIE
ROGER
MARY
BARBARA

Example:

Listing Records

To number the records in a report, use the LIST command.

TABLE FILE EMPLOYEE
LIST LAST_NAME AND FIRST_NAME
END

The following shows the report output.

LIST
----

   1
   2
   3
   4
   5
   6
   7
   8
   9
  10
  11
  12

LAST_NAME
---------

FIRST_NAME
----------

STEVENS
SMITH
JONES
SMITH
BANNING
IRVING
ROMANS
MCCOY
BLACKWOOD
MCKNIGHT
GREENSPAN
CROSS

ALFRED
MARY
DIANE
RICHARD
JOHN
JOAN
ANTHONY
JOHN
ROSEMARIE
ROGER
MARY
BARBARA

Displaying All Fields

You can easily display all of the fields in the left path of the data source by specifying an
asterisk (*) wildcard instead of a specific field name. For additional information about Master
File structures and segment paths, including left paths and short paths, see the Describing
Data With WebFOCUS Language manual.

42




Example:

Displaying All Fields

The following request produces a report displaying all of the fields in the EDUCFILE data
source.

2. Displaying Report Data

TABLE FILE EDUCFILE
LIST *
END

The following shows the report output.

LIST
----

COURSE_CODE
-----------

COURSE_NAME
-----------

DATE_ATTEND
-----------

EMP_ID
------

   1

   2

   3

   4

   5

   6

101

101

101

101

101

102

   7

103

   8

103

   9

103

  10

104

  11

  12

  13

106

202

301

  14

107

  15

  16

  17

  18

302

108

108

201

FILE DESCRPT & MAINT

   83/01/04

212289111

FILE DESCRPT & MAINT

   82/05/25

117593129

FILE DESCRPT & MAINT

   82/05/25

071382660

FILE DESCRPT & MAINT

   81/11/15

451123478

FILE DESCRPT & MAINT

   81/11/15

112847612

BASIC REPORT PREP NON-
PROG

BASIC REPORT PREP NON-
PROG

BASIC REPORT PREP NON-
PROG

BASIC REPORT PREP NON-
PROG

FILE DESC & MAINT NON-
PROG

   82/07/12

326179357

   83/01/05

212289111

   82/05/26

117593129

   81/11/16

112847612

   82/07/14

326179357

TIMESHARING WORKSHOP

   82/07/15

326179357

WHAT'S NEW IN FOCUS

   82/10/28

326179357

DECISION SUPPORT
WORKSHOP

BASIC REPORT PREP DP
MGRS

   82/09/03

326179357

   82/08/02

818692173

HOST LANGUAGE INTERFACE

   82/10/21

818692173

BASIC RPT NON-DP MGRS

   82/10/10

315548712

BASIC RPT NON-DP MGRS

   82/08/24

119265415

ADVANCED TECHNIQUES

   82/07/26

117593129

Creating Reports With TIBCO® WebFOCUS Language

 43






Displaying Individual Values

  19

203

FOCUS INTERNALS

   82/10/28

117593129

Displaying All Fields in a Segment

You can easily display all fields in a segment by adding the prefix "SEG." to any field in the
desired segment.

Syntax:

How to Display All Fields in a Segment

seg.anyfield

where:

anyfield

Is any field that is in the desired segment.

Example:

Displaying All Fields in a Segment

The following request produces a report displaying all of the fields in the segment that
contains the QTY_IN_STOCK field.

TABLE FILE CENTINV
PRINT SEG.QTY_IN_STOCK
BY PRODNAME NOPRINT
END

44

The following shows the report output.

2. Displaying Report Data

Displaying the Structure and Retrieval Order of a Multi-Path Data Source

When using display commands, it is important to understand the structure of the data source
and the relationship between segments, since these factors affect your results. You can use
the CHECK command PICTURE option to display a diagram of the data source structure defined
by the Master File.

You can also display the retrieval order of a data source using the CHECK command PICTURE
RETRIEVE option. It should be noted that retrieval is controlled by the minimum referenced
subtree. For more information, see Understanding the Efficiency of the Minimum Referenced
Subtree in the Describing a Group of Fields chapter in the Describing Data With WebFOCUS
Language manual.

Creating Reports With TIBCO® WebFOCUS Language

 45

Displaying Individual Values

Example:

Displaying the Structure of a Multi-Path Data Source

To display the structure diagram of the CENTORD data source, which is joined to the CENTINV
and CENTCOMP data sources, issue the following command:

CHECK FILE CENTORD PICTURE

46

2. Displaying Report Data

The following shows the structure diagram output.

 NUMBER OF ERRORS=     0
 NUMBER OF SEGMENTS=   4  ( REAL=    2  VIRTUAL=   2 )
 NUMBER OF FIELDS=    23  INDEXES=   4  FILES=     3
 NUMBER OF DEFINES=    8
 TOTAL LENGTH OF ALL FIELDS=  139

SECTION 01
              STRUCTURE OF FOCUS    FILE CENTORD  ON 07/18/03 AT 11.06.34

          OINFO
  01      S1
 **************
 *ORDER_NUM   **I
 *STORE_CODE  **I
 *PLANT       **I
 *ORDER_DATE  **
 *            **
 ***************
  **************
        I
        +-----------------+
        I                 I
        I STOSEG          I PINFO
  02    I KU        03    I S1
 ..............    **************
 :STORE_CODE  :K   *PROD_NUM    **I
 :STORENAME   :    *QUANTITY    **
 :STATE       :    *LINEPRICE   **
 :            :    *            **
 :            :    *            **
 :............:    ***************
  JOINED  CENTCOMPFO**************
                          I
                          I
                          I
                          I INVSEG
                    04    I KU
                   ..............
                   :PROD_NUM    :K
                   :PRODNAME    :
                   :QTY_IN_STOCK:
                   :PRICE       :
                   :            :
                   :............:
                    JOINED  CENTINV FOCUS   A1

Example:

Displaying the Retrieval Order of a Multi-Path Data Source

To display the retrieval order of the EMPLOYEE data source, which is joined to the JOBFILE and
EDUCFILE data sources, issue the following command:

CHECK FILE EMPLOYEE PICTURE RETRIEVE

Creating Reports With TIBCO® WebFOCUS Language

 47



Displaying Individual Values

The following shows the command output that adds the numbers that display at the top left of
each segment, indicating the retrieval order of the segments. A unique segment such as
FUNDTRAN is treated as a logical addition to the parent segment for retrieval. FUNDTRAN and
SECSEG are unique segments, and are therefore treated as part of their parents.

48

The following shows the retrieval order:

2. Displaying Report Data

Creating Reports With TIBCO® WebFOCUS Language

 49

Adding Values

Example:

Displaying Fields From a Multi-Path Data Source

The following request produces a report displaying all of the fields on the left path of the
EMPLOYEE data source.

TABLE FILE EMPLOYEE
PRINT *
END

The following shows a list of the output fields the previous request produces. Due to the size
of the report, only the fields for which all instances will be printed are listed here. In the report,
these fields would be displayed from left to right, starting with EMP_ID.

EMP_ID
LAST_NAME
FIRST_NAME
HIRE_DATE
DEPARTMENT
CURR_SAL
CURR_JOBCODE
ED_HRS
BANK_NAME
BANK_CODE
BANK_ACCT
EFFECT_DATE
DAT_INC
PCT_INC
SALARY
JOBCODE
JOBCODE
JOB_DESC
SEC_CLEAR
SKILLS
SKILL_DESC

Each field in this list appears in segments on the left path of the EMPLOYEE data source. To
view the retrieval order structure of the EMPLOYEE data source, see Displaying the Retrieval
Order of a Multi-Path Data Source on page 47.

Tip: In some environments, the following warning is displayed whenever you use PRINT * with
a multi-path data source, to remind you that PRINT * only displays the left path:

(FOC757) WARNING. YOU REQUESTED PRINT * OR COUNT * FOR A MULTI-PATH FILE

Adding Values

SUM, WRITE, and ADD sum the values of a numeric field. The three commands are synonyms;
they can be used interchangeably, and every reference to SUM in this documentation also
refers to WRITE and ADD.

50

2. Displaying Report Data

When you use SUM, multiple records are read from the data source, but only one summary line
is produced. If you use SUM with a non-numeric field—such as an alphanumeric, text, or date
field—SUM does not add the values. Instead, by default, it displays the last value retrieved
from the data source. You can change this to the first value, minimum value, or maximum
value using the SUMPREFIX parameter.

For SUM, WRITE, and ADD syntax, see Using Display Commands in a Request on page 39.

Example:

Adding Values

This request adds all the values of the field CURR_SAL:

TABLE FILE EMPLOYEE
SUM CURR_SAL
END

The following shows the output of the request.

   CURR_SAL

   --------

$222,284.00

Example:

Adding Non-Numeric Values

This request attempts to add non-numeric fields. Any request for aggregation on non-numeric
data returns the last record retrieved from the data source.

TABLE FILE EMPLOYEE
SUM LAST_NAME AND FIRST_NAME
END

The following shows the output of the request.

LAST_NAME

---------

CROSS

FIRST_NAME

----------

BARBARA

Note that any request for aggregation on all date format fields also returns the last record
retrieved from the data source.

Tip: You can set the SUMPREFIX parameter to FST, MIN, MAX, or LST to control the sort order.
For details, see Sorting Tabular Reports on page 87.

Creating Reports With TIBCO® WebFOCUS Language

 51

Counting Values

Counting Values

The COUNT command counts the number of instances that exist for a specified field. The
COUNT command is particularly useful combined with the BY phrase, which is discussed in
Sorting Tabular Reports on page 87.

COUNT counts the instances of data contained in a report, not the data values.

For COUNT syntax, see Using Display Commands in a Request on page 39.

By default, a COUNT field is a five-digit integer. You can reformat it using the COMPUTE
command, and change its field length using the SET COUNTWIDTH parameter. For details
about the COMPUTE command, see Creating Temporary Fields on page 277. For information
about SET COUNTWIDTH, see the Developing Reporting Applications manual.

When COUNT is used in a request, the word COUNT is appended to the default column title,
unless the column title is changed with an AS phrase.

Example:

Counting Values

To determine how many employees are in the EMPLOYEE data source, you can count the
instances of EMP_ID, the employee identification number.

TABLE FILE EMPLOYEE
COUNT EMP_ID
END

The following shows the output of the request.

EMP_ID

COUNT

------

    12

Example:

Counting Values With a Sort Phrase

To count the instances of EMP_ID for each department, use this request:

TABLE FILE EMPLOYEE
COUNT EMP_ID
BY DEPARTMENT
END

52

The following shows the output of the request indicating that of the 12 EMP_IDs in the data
source, six are from the MIS department and six are from the PRODUCTION department:

2. Displaying Report Data

            EMP_ID
DEPARTMENT  COUNT
----------  ------
MIS              6
PRODUCTION       6

Example:

Counting Instances of Data

The following example counts the instances of data in the LAST_NAME, DEPARTMENT, and
JOBCODE fields in the EMPLOYEE data source.

TABLE FILE EMPLOYEE
COUNT LAST_NAME AND DEPARTMENT AND JOBCODE
END

The following shows the output of the request.

LAST_NAME  DEPARTMENT  JOBCODE
COUNT      COUNT       COUNT
---------  ----------  -------
       12          12       19

The EMPLOYEE data source contains data on 12 employees, with one instance for each
LAST_NAME. While there are only two values for DEPARTMENT, there are 12 instances of the
DEPARTMENT field because each employee works for one of the two departments. Similarly,
there are 19 instances of the JOBCODE field because employees can have more than one job
code during their employment.

Counting Segment Instances

You can easily count the instances of the lowest segment in the left path of a data source by
specifying an asterisk (*) wildcard instead of a specific field name. In a single-segment data
source, this effectively counts all instances in the data source.

COUNT * accomplishes this by counting the values of the first field in the segment. Instances
with a missing value in the first field are not counted (when SET MISSING=ON).

Segment instances in short paths are not counted by COUNT *, regardless of the value of the
ALL parameter of the SET command.

For more information about missing values, short paths, and the SET ALL parameter, see
Handling Records With Missing Field Values on page 1035.

Creating Reports With TIBCO® WebFOCUS Language

 53

Expanding Byte Precision for COUNT and LIST

Example:

Counting Segments From a Multi-Path Data Source

The following request counts the number of instances of the SKILLSEG segment of the
EMPLOYEE data source.

TABLE FILE EMPLOYEE
COUNT *
END

The following shows the output of the request.

COUNT *

COUNT

-------

     19

COUNT * counts the number of instances of the SKILLSEG segment, which is the lowest
segment in the left path of the EMPLOYEE data source structure (that is, the EMPLOYEE data
source joined to the JOBFILE and EDUCFILE data sources). You can see a picture of the path
structure in Displaying the Structure and Retrieval Order of a Multi-Path Data Source on page
45.

Tip: In some environments, the following warning is displayed if you use COUNT * with a multi-
path data source (such as EMPLOYEE in the above example):

(FOC757) WARNING. YOU REQUESTED PRINT * OR COUNT * FOR A MULTI-PATH FILE

Expanding Byte Precision for COUNT and LIST

By default, the number of characters that display for counter values retrieved using the COUNT
and LIST commands is five. You can increase the number of characters to nine.

For example, if the number of records retrieved for a field exceeds 99,999 (5 bytes), asterisks
appear in the report to indicate an overflow condition. You can increase the display to allow as
large a count as 999,999,999 (9 bytes) using SET COUNTWIDTH.

Note: You can change the overflow character by issuing the SET OVERFLOWCHAR command.

54

2. Displaying Report Data

Syntax:

How to Set the Precision for COUNT and LIST

SET COUNTWIDTH = {OFF|ON}

where:

OFF

Displays five characters (bytes) for COUNT and LIST counter values. Asterisks are
displayed if the number of records retrieved for a field exceeds five characters. OFF is
the default.

ON

Displays up to nine characters (bytes) for COUNT and LIST counter values. Asterisks
are displayed if the value exceeds nine characters.

Example:

Setting Precision for COUNT and LIST

The following example shows the COUNT command with SET COUNTWIDTH = OFF:

TABLE FILE filename
COUNT Fldxx
BY Fldyy
END

Fldyy

value

Fldxx

COUNT

*****

The following example shows the COUNT command with SET COUNTWIDTH = ON:

TABLE FILE filename
COUNT Fldxx
BY Fldyy
END

Fldyy

value

    Fldxx

COUNT

999999999

Note: This feature affects the width of a report when COUNTWIDTH is set to ON. Calculating
the width of a report now requires an additional four display positions for each COUNT or LIST
column.

Maximum Number of Display Fields Supported in a Request

There is no limit to the number of verb objects in a TABLE or MATCH request.

Creating Reports With TIBCO® WebFOCUS Language

 55

Manipulating Display Fields With Prefix Operators

However, an error can occur under the following conditions:

The report output format has a limit to the number of columns supported. For example,
Excel, FOCUS, and XFOCUS formats have limits on the number of columns.

The operating system has a maximum record length that cannot fit all of the columns.

The amount of memory needed to store the output is not available.

If the combined length of the display fields in the data area exceeds the maximum capacity, an
error message displays. To correct the problem, adjust the number or lengths of the fields in
the request.

Manipulating Display Fields With Prefix Operators

You can use prefix operators to perform calculations directly on the values of fields.

Note: Unless you change a column or ACROSS title with an AS phrase, the prefix operator is
automatically added to the title. Without an AS phrase, the column title is constructed using
the prefix operator and either the field name or the TITLE attribute in the Master File (if there is
one):

If there is no TITLE attribute, the field name is used.

If there is a TITLE attribute in the Master File, the choice between using the field name or
the TITLE attribute depends on the value of the TITLES parameter:

If SET TITLES = ON, the TITLE attribute is used.

If SET TITLES = OFF or NOPREFIX, the field name is used.

You can use the SET PRFTITLE command to create descriptive and translatable column titles
for prefixed fields. For example, the following request sets PRFTITLE to LONG.

SET PRFTITLE = LONG
TABLE FILE WF_RETAIL_LITE
SUM COGS_US CNT.COGS_US AVE.COGS_US CNT.DST.COGS_US MIN.COGS_US MAX.COGS_US
MDN.COGS_US
BY PRODUCT_CATEGORY
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

56

The output is shown in the following image. The prefix operator names are converted to
descriptive text.

2. Displaying Report Data

If PRFTITLE had been set to SHORT (the default), the prefix operator name would have been
used instead of the descriptive text.

For a list of prefix operators and their functions, see Functions You Can Perform With Prefix
Operators on page 58.

Prefix Operator Basics

This topic describes basic syntax and notes for using prefix operators.

Syntax:

How to Use Prefix Operators

Each prefix operator is applied to a single field, and affects only that field.

{SUM|COUNT} prefix.fieldname AS 'coltitle'

{PRINT|COMPUTE} RNK.byfield

where:

prefix

Is any prefix operator.

fieldname

Is the name of the field to be displayed in the report.

'coltitle'

Is the column title for the report column, enclosed in single quotation marks.

byfield

Is the name of a vertical sort field to be ranked in the report.

Reference: Usage Notes for Prefix Operators

Because PRINT and LIST display individual field values, not an aggregate value, they are
not used with prefix operators, except TOT. and DST.

Creating Reports With TIBCO® WebFOCUS Language

 57

Manipulating Display Fields With Prefix Operators

To sort by the results of a prefix command, use the phrase BY TOTAL to aggregate and sort
numeric columns simultaneously. For details, see Sorting Tabular Reports on page 87.

The WITHIN phrase is very useful when using prefixes. The WITHIN phrase is not supported
with the MDN., MDE., DST., CNT.DST., AVE.DST., or SUM.DST. prefix operators in an
aggregation display command, such as SUM. The WITHIN phrase is supported with the
DST. operator with the PRINT display command.

You can use the results of prefix operators in COMPUTE commands.

With the exception of PCT., RPCT., CNT. and PCT.CNT., resulting values have the same
format as the field against which the prefix operation was performed.

For percent-based prefix operators PCT. and RPCT., if you set the PCTFORMAT parameter to
OLD, resulting values have the same format as the field against which the prefix operation
was performed. By default, PCTFORMAT is set to PERCENT, which displays the prefixed
column with a percent sign and removes other options, such as currency symbols, although
you can reformat it. PCT.CNT.field will always display with two decimal places and a percent
sign, unless reformatted. With PCTFORMAT = PERCENT, the format of the output column
may depend on the format of the original field. For a field with a:

Precision-based format (F, D, M, X), the column will display with length 7 and two
decimal places.

Packed format, the column will display with its original number of decimal places.

Integer format, the column will display with no decimal places.

Text fields can only be used with the FST., LST., and CNT. prefix operators.

PCT., TOT., PCT.CNT., RNK., and RPCT. are not supported with TABLEF and should not be
used with TABLEF.

Reference: Functions You Can Perform With Prefix Operators

The following table lists prefix operators and describes the function of each.

Prefix

ASQ.

AVE.

Function

Computes the average sum of squares for standard deviation in
statistical analysis.

Computes the average value of the field.

58

Prefix

CNT.

AVE.DST.

CNT.DST.

SUM.DST.

CT.

DST.

FST.

LST.

MAX.

MDE.

MDN.

MIN.

PCT.

PCT.CNT.

RNK.

2. Displaying Report Data

Function

Counts the number of occurrences of the field. The data type of the
result is always Integer.

Averages the distinct values within a field.

Counts the number of distinct values within a field.

Sums the distinct values within a field.

Produces a cumulative total of the specified field. This operator only
applies when used in subfootings. For details, see Using Headings,
Footings, Titles, and Labels on page 1517.

Determines the total number of distinct values in a single pass of a
data source.

Generates the first physical instance of the field. Can be used with
numeric or text fields.

Generates the last physical instance of the field. Can be used with
numeric or text fields.

Generates the maximum value of the field.

Computes the mode of the field values.

Computes the median of the field values.

Generates the minimum value of the field.

Computes a field percentage based on the total values for the field.
The PCT operator can be used with detail as well as summary fields.

Computes a field percentage based on the number of instances
found. The format of the result is always F6.2 and cannot be
reformatted.

Ranks the instances of a BY sort field in the request. Can be used in
PRINT commands, COMPUTE commands, and IF or WHERE TOTAL
tests.

Creating Reports With TIBCO® WebFOCUS Language

 59

Manipulating Display Fields With Prefix Operators

Prefix

ROLL.

RPCT.

ST.

STDP.

STDS.

SUM.

TOT.

Function

Recalculates values on summary lines using the aggregated values
from lower level summary lines.

Computes a field percentage based on the total values for the field
across a row.

Produces a subtotal value of the specified field at a sort break in the
report. This operator only applies when used in subfootings. For
details, see Using Headings, Footings, Titles, and Labels on page 1517.

Computes the standard deviation for a population.

Computes the standard deviation for a sample.

Sums the field values.

Totals the field values for use in a heading (includes footings,
subheads, and subfoots).

Averaging Values of a Field

The AVE. prefix computes the average value of a particular field. The computation is performed
at the lowest sort level of the display command. It is computed as the sum of the field values
within a sort group divided by the number of records in that sort group. If the request does not
include a sort phrase, AVE. calculates the average for the entire report.

Example:

Averaging Values of a Field

This request calculates the average number of education hours spent in each department.

TABLE FILE EMPLOYEE
SUM AVE.ED_HRS BY DEPARTMENT
END

The following shows the output of the request.

            AVE
DEPARTMENT  ED_HRS
----------  ------
MIS          38.50
PRODUCTION   20.00

60

Averaging the Sum of Squared Fields

The ASQ. prefix computes the average sum of squares, which is a component of the standard
deviation in statistical analysis (shown as a formula in the following image).

2. Displaying Report Data

Note: If the field format is integer and you get a large set of numbers, the ASQ. result may
exceed the limit of the I4 field, which is 2,147,483,647. The display of any number larger than
this will generate a negative number or an incorrect positive number. For this reason, we
recommend that you do not use Integer fields if this result could occur.

Example:

Averaging the Sum of Squared Fields

This request calculates the sum and the sum of squared fields for the DELIVER_AMT field.

TABLE FILE SALES
SUM DELIVER_AMT AND ASQ.DELIVER_AMT
BY CITY
END

The following shows the output of the request.

                              ASQ
CITY             DELIVER_AMT  DELIVER_AMT
----             -----------  -----------
NEW YORK                 300          980
NEWARK                    60          900
STAMFORD                 430         3637
UNIONDALE                 80         1600

Calculating Maximum and Minimum Field Values

The prefixes MAX. and MIN. produce the maximum and minimum values, respectively, within a
sort group. If the request does not include a sort phrase, MAX. and MIN. produce the
maximum and minimum values for the entire report.

Example:

Calculating Maximum and Minimum Field Values

This report request calculates the maximum and minimum values of SALARY.

TABLE FILE EMPLOYEE
SUM MAX.SALARY AND MIN.SALARY
END

Creating Reports With TIBCO® WebFOCUS Language

 61

Manipulating Display Fields With Prefix Operators

The following shows the output of the request.

    MAX              MIN
    SALARY           SALARY
    ------           ------
$29,700.00        $8,650.00

Calculating Median and Mode Values for a Field

You can use the MDN. (median) and MDE. (mode) prefix operators, in conjunction with an
aggregation display command (SUM, WRITE) and a numeric or smart date field, to calculate the
statistical median and mode of the values in the field.

These calculations are not supported in a DEFINE command, in WHERE or IF expressions, in a
WITHIN phrase, or in a summary command. If used in a multi-verb request, they must be used
at the lowest level of aggregation.

The median is the middle value (50th percentile). If there is an even number of values, the
median is the average of the middle two values. The mode is the value that occurs most
frequently within the set of values. If no value occurs more frequently than the others, MDE.
returns the lowest value.

Example:

Calculating the Median and Mode

The following request against the EMPLOYEE data source displays the current salaries and
calculates the average (mean), median, and mode within each department.

TABLE FILE EMPLOYEE
SUM CURR_SAL AS 'INDIVIDUAL,SALARIES'
AVE.CURR_SAL AS 'DEPARTMENT,AVERAGE'
MDN.CURR_SAL AS 'DEPARTMENT,MEDIAN'
MDE.CURR_SAL AS 'DEPARTMENT,MODE'
BY DEPARTMENT
ON TABLE SET PAGE NOPAGE
END

Both departments have an even number of employees. For the MIS department, the two
middle values are the same, making that value ($18,480.00) both the median and the mode.
For the PRODUCTION department, the median is the average of the two middle values
($16,100.00 and $21,120.00) and, since there are no duplicate values, the mode is the
lowest value ($9,500.00).

62

2. Displaying Report Data

Calculating Column and Row Percentages

For each individual value in a column, PCT. calculates what percentage that field makes up of
the column total value. You can control how values are distributed down the column by sorting
the column using the BY phrase.

You can also determine percentages for row values. For each individual value in a row that has
been sorted using the ACROSS phrase, the RPCT. operator calculates what percentage it
makes up for the total value of the row.

Example:

Calculating Column Percentages

To calculate each employee share of education hours, issue the following request:

TABLE FILE EMPLOYEE
SUM ED_HRS PCT.ED_HRS BY LAST_NAME
ON TABLE COLUMN-TOTAL
ON TABLE SET PAGE NOPAGE
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

The output is shown in the following image:

Creating Reports With TIBCO® WebFOCUS Language

 63

Manipulating Display Fields With Prefix Operators

If you set PCFORMAT to OLD, PCT. and RPCT. WILL take the same format as the field, and the
column may not always total exactly 100 because of the nature of floating-point arithmetic.

Example:

Calculating Row Percentages

The following request calculates the total units sold for each product (UNIT_SOLD column), and
the percentage that total makes up in relation to the sum of all products sold
(RPCT.UNIT_SOLD column) in each city.

TABLE FILE SALES
SUM UNIT_SOLD RPCT.UNIT_SOLD ROW-TOTAL
BY PROD_CODE
ACROSS CITY    WHERE
CITY EQ 'NEW YORK' OR 'STAMFORD'
ON TABLE SET PAGE NOPAGE
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

The output is shown in the following image.

Because UNIT_SOLD has an integer format, the columns created by RPCT. also have integer (I)
formats. Therefore, individual percentages may be truncated and the total percentage may be
less than 100%. If you require precise totals, redefine the field with a format that declares
decimal places (D, F).

64

2. Displaying Report Data

Producing a Direct Percent of a Count

When counting occurrences in a file, a common reporting need is determining the relative
percentages of each row’s count within the total number of instances. You can do this, for
columns only, with the following syntax:

PCT.CNT.fieldname

The format is a decimal value of length seven, with two decimal places and a percent sign.

Example:

Producing a Direct Percent of a Count

This request illustrates the relative percentage of the values in the EMP_ID field for each
department.

TABLE FILE EMPLOYEE
SUM PCT.CNT.EMP_ID
BY DEPARTMENT
ON TABLE SET PAGE NOPAGE
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

The output is shown in the following image:

Aggregating and Listing Unique Values

The distinct prefix operator (DST.) may be used to aggregate and list unique values of any data
source field. Similar in function to the SQL COUNT, SUM, and AVG(DISTINCT col) column
functions, it permits you to determine the total number of distinct values in a single pass of
the data source.

The DST. operator can be used with the SUM, PRINT or COUNT commands, and also in
conjunction with the aggregate prefix operators SUM., CNT., and AVE. Multiple DST. operators
are supported in TABLE and TABLEF requests. They are supported in requests that use the BY,
ACROSS, and FOR phrases.

Creating Reports With TIBCO® WebFOCUS Language

 65

Manipulating Display Fields With Prefix Operators

Note that in a request using the PRINT command and multiple DST operators, you should issue
the command SET PRINTDST=NEW. For more information, see the Developing Reporting
Applications manual.

Syntax:

How to Use the Distinct Operator

command DST.fieldname

or

SUM [operator].DST.fieldname

where:

command

Is SUM, PRINT, or COUNT.

DST.

Indicates the distinct operator.

fieldname

Indicates the display-field object or field name.

operator

Indicates SUM., CNT., or AVE.

Example:

Using the Distinct Operator

The procedure requesting a count of unique ED_HRS values is either:

TABLE FILE EMPLOYEE
SUM CNT.DST.ED_HRS
END

or

TABLE FILE EMPLOYEE
COUNT DST.ED_HRS
END

The output is:

COUNT
DISTINCT
ED_HRS
--------
       9

66

2. Displaying Report Data

Notice that the count includes records for both employees with the last name SMITH, but
excludes the second records for values 50.00, 25.00, and .0, resulting in nine unique ED_HRS
values.

Example:

Counting Distinct Field Values With Multiple Display Commands

The following request against the GGSALES data source counts the total number of records by
region, then the number of records, distinct categories, and distinct products by region and by
state. The DST or CNT.DST operator can be used only with the last display command:

TABLE FILE GGSALES
COUNT CATEGORY AS 'TOTAL,COUNT'
  BY REGION
SUM CNT.CATEGORY AS 'STATE,COUNT'
    CNT.DST.CATEGORY    CNT.DST.PRODUCT
  BY REGION
  BY ST
END

The output is:

                                  COUNT     COUNT
             TOTAL         STATE  DISTINCT  DISTINCT
Region       COUNT  State  COUNT  CATEGORY  PRODUCT
------       -----  -----  -----  --------  --------
Midwest       1085  IL       362         3         9
                    MO       361         3         9
                    TX       362         3         9
Northeast     1084  CT       361         3        10
                    MA       360         3        10
                    NY       363         3        10
Southeast     1082  FL       361         3        10
                    GA       361         3        10
                    TN       360         3        10
West          1080  CA       721         3        10
                    WA       359         3        10

Reference: Distinct Operator Limitations

If you reformat a column created using COUNT DST. or the CNT.DST operator, you must
reformat it to an integer (I) data type. If you specify another data type, the following error
occurs:

(FOC950) INVALID REFORMAT OPTION WITH COUNT OR CNT.

The following error occurs if you use the prefix operators CNT., SUM., and AVE. with any
other display command:

(FOC1853) CNT/SUM/AVE.DST CAN ONLY BE USED WITH AGGREGATION VERBS

Creating Reports With TIBCO® WebFOCUS Language

 67

Manipulating Display Fields With Prefix Operators

The following error occurs if you use DST. in a MATCH command:

(FOC1854) THE DST OPERATOR IS ONLY SUPPORTED IN TABLE REQUESTS

The following error occurs if you reformat a BY field (when used with the PRINT command,
the DST.fieldname becomes a BY field):

(FOC1862) REFORMAT DST.FIELD IS NOT SUPPORTED WITH PRINT

The following error occurs if you use the DST. operator with NOSPLIT:

(FOC1864) THE DST OPERATOR IS NOT SUPPORTED WITH NOSPLIT

The following error occurs if you use a multi-verb request, SUM DST.fieldname BY field
PRINT fld BY fld (a verb object operator used with the SUM command must be at the lowest
level of aggregation):

(FOC1867) DST OPERATOR MUST BE AT THE LOWEST LEVEL OF AGGREGATION

The DST. operator may not be used as part of a HEADING or a FOOTING.

The DST., AVE.DST, CNT.DST., and SUM.DST. operators are not supported with WITHIN in a
request that uses an aggregation display command, such as SUM. The DST. operator is
supported with WITHIN when the request uses the PRINT display command.

Retrieving First and Last Records

FST. is a prefix that displays the first retrieved record selected for a given field. LST. displays
the last retrieved record selected for a given field.

When using the FST. and LST. prefix operators, it is important to understand how your data
source is structured.

If the record is in a segment with values organized from lowest to highest (segment type
S1), the first logical record that the FST. prefix operator retrieves is the lowest value in the
set of values. The LST. prefix operator would, therefore, retrieve the highest value in the set
of values.

If the record is in a segment with values organized from highest to lowest (segment type
SH1), the first logical record that the FST. prefix operator retrieves is the highest value in
the set of values. The LST. prefix operator would, therefore, retrieve the lowest value in the
set of values.

68

2. Displaying Report Data

For more information on segment types and file design, see the Describing Data With
WebFOCUS Language manual. If you wish to reorganize the data in the data source or
restructure the data source while reporting, see Improving Report Processing on page 1929.

Example:

Retrieving the First Record

The following request retrieves the first logical record in the EMP_ID field:

TABLE FILE EMPLOYEE
SUM FST.EMP_ID
END

The output is:

FST
EMP_ID
------
071382660

Example:

Segment Types and Retrieving Records

The EMPLOYEE data source contains the DEDUCT segment, which orders the fields DED_CODE
and DED_AMT from lowest value to highest value (segment type of S1). The DED_CODE field
indicates the type of deduction, such as CITY, STATE, FED, and FICA. The following request
retrieves the first logical record for DED_CODE for each employee:

TABLE FILE EMPLOYEE
SUM FST.DED_CODE
BY EMP_ID
END

The output is:

           FST
EMP_ID     DED_CODE
------     --------
071382660  CITY
112847612  CITY
117593129  CITY
119265415  CITY
119329144  CITY
123764317  CITY
126724188  CITY
219984371  CITY
326179357  CITY
451123478  CITY
543729165  CITY
818692173  CITY

Note, however, the command SUM LST.DED_CODE would have retrieved the last logical record
for DED_CODE for each employee.

Creating Reports With TIBCO® WebFOCUS Language

 69

Manipulating Display Fields With Prefix Operators

If the record is in a segment with values organized from highest to lowest (segment type SH1),
the first logical record that the FST. prefix operator retrieves is the highest value in the set of
values. The LST. prefix operator would therefore retrieve the lowest value in the set of values.

For example, the EMPLOYEE data source contains the PAYINFO segment, which orders the
fields JOBCODE, SALARY, PCT_INC, and DAT_INC from highest value to lowest value (segment
type SH1). The following request retrieves the first logical record for SALARY for each
employee:

TABLEF FILE EMPLOYEE
SUM FST.SALARY
BY EMP_ID
END

The output is:

                    FST
EMP_ID              SALARY
------              ------
071382660       $11,000.00
112847612       $13,200.00
117593129       $18,480.00
119265415        $9,500.00
119329144       $29,700.00
123764317       $26,862.00
126724188       $21,120.00
219984371       $18,480.00
326179357       $21,780.00
451123478       $16,100.00
543729165        $9,000.00
818692173       $27,062.00

However, the command SUM LST.SALARY would have retrieved the last logical record for
SALARY for each employee.

Summing and Counting Values

You can count occurrences and summarize values with one display command using the prefix
operators CNT., SUM., and TOT. Just like the COUNT command, CNT. counts the occurrences
of the field it prefixes. Just like the SUM command, SUM. sums the values of the field it
prefixes. TOT. sums the values of the field it prefixes when used in a heading (including
footings, subheads, and subfoots).

70

Example:

Counting Values With CNT

The following request counts the occurrences of PRODUCT_ID, and sums the value of
UNIT_PRICE.

2. Displaying Report Data

TABLE FILE GGPRODS
SUM CNT.PRODUCT_ID AND UNIT_PRICE
END

The output is:

Product
Code        Unit
COUNT       Price
-------     -----
     10    660.00

Example:

Summing Values With SUM

The following request counts the occurrences of PRODUCT_ID, and sums the value of
UNIT_PRICE.

TABLE FILE GGPRODS
COUNT PRODUCT_ID AND SUM.UNIT_PRICE
END

The output is:

Product
Code        Unit
COUNT       Price
-------     -----
     10    660.00

Example:

Summing Values With TOT

The following request uses the TOT prefix operator to show the total of current salaries for all
employees.

TABLE FILE EMPLOYEE
PRINT LAST_NAME
BY DEPARTMENT
ON TABLE SUBFOOT
"Total salaries equal: <TOT.CURR_SAL"
END

Creating Reports With TIBCO® WebFOCUS Language

 71

Manipulating Display Fields With Prefix Operators

The output is:

DEPARTMENT  LAST_NAME
----------  ---------
MIS         SMITH
            JONES
            MCCOY
            BLACKWOOD
            GREENSPAN
            CROSS
PRODUCTION  STEVENS
            SMITH
            BANNING
            IRVING
            ROMANS
            MCKNIGHT
Total salaries equal:     $222,284.00

Ranking Sort Field Values With RNK.

RANKED BY fieldname, when used in a sort phrase in a TABLE request, not only sorts the data
by the specified field, but assigns a RANK value to the instances. The RNK. prefix operator
also calculates the rank while allowing the RANK value to be printed anywhere on the page.
You use this operator by specifying RNK.fieldname, where fieldname is a BY field in the
request.

The ranking process occurs after selecting and sorting records. Therefore, the RNK. operator
cannot be used in a WHERE or IF selection test or in a virtual (DEFINE) field. However,
RNK.fieldname can be used in a WHERE TOTAL or IF TOTAL test or in a calculated (COMPUTE)
value. You can change the default column title for the rank field using an AS phrase.

You can apply the RNK. operator to multiple sort fields, in which case the rank for each BY
field is calculated within its higher level BY field.

Syntax:

How to Calculate Ranks Using the RNK. Prefix Operator

In a PRINT command, COMPUTE expression, or IF/WHERE TOTAL expression :

RNK.field  ...

where:

field

Is a vertical (BY) sort field in the request.

72

Example:

Ranking Within Sort Groups

The following request ranks years of service within department and ranks salary within years of
service and department. Note that years of service depends on the value of TODAY. The output
for this example was valid when run in September, 2006:

2. Displaying Report Data

DEFINE FILE EMPDATA
  TODAY/YYMD = &YYMD;
  YRS_SERVICE/I9 = DATEDIF(HIREDATE,TODAY,'Y');
END
TABLE FILE EMPDATA
PRINT SALARY
  RNK.YRS_SERVICE AS 'RANKING,BY,SERVICE'
  RNK.SALARY AS 'SALARY,RANK'
     BY DEPT
     BY HIGHEST YRS_SERVICE
     BY HIGHEST SALARY NOPRINT
WHERE DEPT EQ 'MARKETING' OR 'SALES'
ON TABLE SET PAGE NOPAGE
END

The output is:

                                                    RANKING
                                                    BY       SALARY
DEPT                  YRS_SERVICE           SALARY  SERVICE  RANK
----                  -----------           ------  -------  ------
MARKETING                      17       $55,500.00        1       1
                                        $55,500.00        1       1
                               16       $62,500.00        2       1
                                        $62,500.00        2       1
                                        $62,500.00        2       1
                                        $58,800.00        2       2
                                        $52,000.00        2       3
                                        $35,200.00        2       4
                                        $32,300.00        2       5
                               15       $50,500.00        3       1
                                        $43,400.00        3       2
SALES                          17      $115,000.00        1       1
                                        $54,100.00        1       2
                               16       $70,000.00        2       1
                                        $43,000.00        2       2
                               15       $43,600.00        3       1
                                        $39,000.00        3       2
                               15       $30,500.00        3       3

Creating Reports With TIBCO® WebFOCUS Language

 73

Manipulating Display Fields With Prefix Operators

Example:

Using RNK. in a WHERE TOTAL Test

The following request displays only those rows in the highest two salary ranks within the years
of service category. Note that years of service depends on the value of TODAY. The output for
this example was valid when run in September, 2006:

DEFINE FILE EMPDATA
  TODAY/YYMD = &YYMD;
  YRS_SERVICE/I9 = DATEDIF(HIREDATE,TODAY,'Y');
END
TABLE FILE EMPDATA
PRINT LASTNAME FIRSTNAME RNK.SALARY
BY HIGHEST YRS_SERVICE BY HIGHEST SALARY
WHERE TOTAL RNK.SALARY LE 2
END

The output is:

                                                           RANK
YRS_SERVICE           SALARY  LASTNAME         FIRSTNAME   SALARY
-----------           ------  --------         ---------   ------
         17      $115,000.00  LASTRA           KAREN            1
                  $80,500.00  NOZAWA           JIM              2
         16       $83,000.00  SANCHEZ          EVELYN           1
                  $70,000.00  CASSANOVA        LOIS             2
         15       $62,500.00  HIRSCHMAN        ROSE             1
                              WANG             JOHN             1
                  $50,500.00  LEWIS            CASSANDRA        2

Example:

Using RNK. in a COMPUTE Command

The following request sets a flag to Y for records in which the salary rank within department is
less than or equal to 5 and the rank of years of service within salary and department is less
than or equal to 6. Otherwise, the flag has the value N. Note that the years of service depends
on the value of TODAY. The output for this example was valid when run in September, 2006:

DEFINE FILE EMPDATA
  TODAY/YYMD = &YYMD;
  YRS_SERVICE/I9 = DATEDIF(HIREDATE,TODAY,'Y');
END
TABLE FILE EMPDATA
PRINT RNK.SALARY RNK.YRS_SERVICE
COMPUTE FLAG/A1 = IF RNK.SALARY LE 5  AND RNK.YRS_SERVICE LE 6
    THEN 'Y' ELSE 'N';
BY DEPT BY SALARY BY YRS_SERVICE
WHERE DEPT EQ 'MARKETING' OR 'SALES'
ON TABLE SET PAGE NOPAGE
END

74

2. Displaying Report Data

The output is:

                                                 RANK   RANK
DEPT                          SALARY YRS_SERVICE SALARY YRS_SERVICE FLAG
----                          ------ ----------- ------ ----------- ----
MARKETING                 $32,300.00          16      1           1 Y
                          $35,200.00          16      2           1 Y
                          $43,400.00          15      3           1 Y
                          $50,500.00          15      4           1 Y
                          $52,000.00          16      5           1 Y
                          $55,500.00          17      6           1 N
                                                      6           1 N
                          $58,800.00          16      7           1 N
                          $62,500.00          16      8           1 N
                                                      8           1 N
                                                      8           1 N
SALES                     $30,500.00          15      1           1 Y
                          $39,000.00          15      2           1 Y
                          $43,000.00          16      3           1 Y
                          $43,600.00          15      4           1 Y
                          $54,100.00          17      5           1 Y
                          $70,000.00          16      6           1 N
                         $115,000.00          17      7           1 N

Rolling Up Calculations on Summary Rows

Using SUMMARIZE and RECOMPUTE, you can recalculate values at sort field breaks, but these
calculations use the detail data to calculate the value for the summary line.

Using the ROLL. operator in conjunction with another prefix operator on a summary line
recalculates the sort break values using the values from summary lines generated for the
lower level sort break.

The operator combinations supported are:

ROLL.SUM. (same as ROLL.). Alphanumeric fields are supported with SUM. This returns
either the first, minimum, maximum, or last value according to the SUMPREFIX parameter.

ROLL.AVE.

ROLL.MAX. (supported with alphanumeric fields as well as numeric fields)

ROLL.MIN. (supported with alphanumeric fields as well as numeric fields)

ROLL.FST. (supported with alphanumeric fields as well as numeric fields)

ROLL.LST. (supported with alphanumeric fields as well as numeric fields)

ROLL.CNT.

ROLL.ASQ.

Creating Reports With TIBCO® WebFOCUS Language

 75

Manipulating Display Fields With Prefix Operators

ROLL.prefix on a summary line indicates that the prefix operation will be performed on the
summary values from the next lowest level of summary command.

If the ROLL. operator is used without another prefix operator, it is treated as a SUM. Therefore,
if the summary command for the lowest BY field specifies AVE., and the next higher specifies
ROLL., the result will be the sum of the averages. To get the average of the averages, you
would use ROLL.AVE at the higher level.

Note: With SUMMARIZE and SUB-TOTAL, the same calculations are propagated to all higher
level sort breaks.

Syntax:

How to Roll Up Summary Values

BY field {SUMMARIZE|SUBTOTAL|SUB-TOTAL|RECOMPUTE} [ROLL.][prefix1.]
[field1 field2 ...|*] [ROLL.][prefix2.] [fieldn ...]

Or:

BY field

ON field {SUMMARIZE|SUBTOTAL|SUB-TOTAL|RECOMPUTE} ROLL.[prefix.]
[field1 field2 ...|*]

where:

ROLL.

Indicates that the summary values should be calculated using the summary values from
the next lowest level summary command.

field

Is a BY field in the request.

prefix1, prefix2

Are prefix operators to use for the summary values. It can be one of the following
operators: SUM. (the default operator if none is specified), AVE., MAX., MIN., FST., LST.,
CNT., ASQ.

field1 field2 fieldn

Are fields to be summarized.

*

Indicates that all fields, numeric and alphanumeric, should be included on the summary
lines. You can either use the asterisk to display all columns or reference the specific
columns you want to display.

76

Example:

Rolling Up an Average Calculation

The following request against the GGSALES data source contains two sort fields, REGION and
ST. The summary command for REGION applies the AVE. operator to the sum of the units
value for each state.

2. Displaying Report Data

TABLE FILE GGSALES
   SUM UNITS AS 'Inventory '
     BY REGION
   BY ST
   ON REGION SUBTOTAL      AVE.  AS 'Average'
   WHERE DATE GE 19971001
   WHERE REGION EQ 'West' OR 'Northeast'
   ON TABLE SET PAGE NOPAGE
   END

On the output, the UNITS values for each state are averaged to calculate the subtotal for each
region. The UNITS values for each state are also used to calculate the average for the grand
total row.

Region       State  Inventory
------       -----  ----------
Northeast    CT          37234
             MA          35720
             NY          36248

Average Northeast
                         36400

West         CA          75553
             WA          40969

Average West
                         58261

TOTAL                    45144

The following version of the request adds a summary command for the grand total line that
includes the ROLL. operator:

TABLE FILE GGSALES
   SUM UNITS AS 'Inventory '
     BY REGION
   BY ST
   ON REGION SUBTOTAL  AVE.  AS 'Average'
   WHERE DATE GE 19971001
   WHERE REGION EQ 'West' OR 'Northeast'
   ON TABLE SUBTOTAL ROLL.AVE. AS ROLL.AVE
   ON TABLE SET PAGE NOPAGE
   END

Creating Reports With TIBCO® WebFOCUS Language

 77

Manipulating Display Fields With Prefix Operators

On the output, the UNITS values for each state are averaged to calculate the subtotal for each
region, and those region subtotal values are used to calculate the average for the grand total
row:

Region       State  Inventory
  ------       -----  ----------
  Northeast    CT          37234
               MA          35720
               NY          36248

  Average Northeast
                           36400

  West         CA          75553
               WA          40969

  Average West
                           58261

  ROLL.AVE                 47330

Example:

Propagating Rollups to Higher Level Sort Breaks

The following request against the GGSALES data source has three BY fields. The SUBTOTAL
command for the PRODUCT sort field specifies AVE., and the SUMMARIZE command for the
higher level sort field, REGION, specifies ROLL.AVE.

TABLE FILE GGSALES
SUM UNITS
BY REGION
BY PRODUCT
BY HIGHEST DATE
WHERE DATE GE 19971001
  WHERE REGION EQ 'Midwest' OR 'Northeast'
  WHERE PRODUCT LIKE 'C%'
  ON PRODUCT SUBTOTAL AVE.
  ON REGION SUMMARIZE ROLL.AVE. AS ROLL.AVE
ON TABLE SET PAGE NOPAGE
END

78






2. Displaying Report Data

On the output, the detail rows for each date are used to calculate the average for each
product. Because of the ROLL.AVE. at the region level, the averages for each product are used
to calculate the averages for each region, and the region averages are used to calculate the
average for the grand total line:

Region       Product                 Date  Unit Sales
  ------       -------                 ----  ----------
  Midwest      Coffee Grinder    1997/12/01        4648
                                 1997/11/01        3144
                                 1997/10/01        1597

  *TOTAL PRODUCT Coffee Grinder                    3129

               Coffee Pot        1997/12/01        1769
                                 1997/11/01        1462
                                 1997/10/01        2346

  *TOTAL PRODUCT Coffee Pot                        1859

               Croissant         1997/12/01        7436
                                 1997/11/01        5528
                                 1997/10/01        6060

  *TOTAL PRODUCT Croissant                         6341
  ROLL.AVE Midwest                                 3776

  Northeast    Capuccino         1997/12/01        1188
                                 1997/11/01        2282
                                 1997/10/01        3675

  *TOTAL PRODUCT Capuccino                         2381

               Coffee Grinder    1997/12/01        1536
                                 1997/11/01        1399
                                 1997/10/01        1315

  *TOTAL PRODUCT Coffee Grinder                    1416

               Coffee Pot        1997/12/01        1442
                                 1997/11/01        2129
                                 1997/10/01        2082

  *TOTAL PRODUCT Coffee Pot                        1884

               Croissant         1997/12/01        4291
                                 1997/11/01        6978
                                 1997/10/01        4741

  *TOTAL PRODUCT Croissant                         5336
  ROLL.AVE Northeast                               2754

  TOTAL                                            3265

Creating Reports With TIBCO® WebFOCUS Language

 79
















Manipulating Display Fields With Prefix Operators

Reference: Usage Notes for ROLL.

ROLL.prefix on a summary line indicates that the prefix operation will be performed on the
summary values from the next lowest level of summary command.

If no summary command was issued at the level below the ROLL., and no other operator
was used in conjunction with the ROLL., a SUM. will be calculated. If the lower level had no
summary command and ROLL. was used with another prefix operator (for example,
ROLL.AVE.), the specified prefix operator will be used. For example, ROLL.AVE. will become
AVE.

CNT. prefix shows the number of data lines displayed, which is not affected by MULTILINES.

ROLL.CNT. prefix shows the number of summary lines displayed, which is affected by
MULTILINES.

Calculating the Standard Deviation for a Population or a Sample

The standard deviation prefix operators return a numeric value that represents the amount of
dispersion in the data. The set of data can be specified as the entire population (STDP.) or a
sample (STDS.). The standard deviation is the square root of the variance, which is a measure
of how observations deviate from their expected value (mean). If specified as a population, the
divisor in the standard deviation calculation (also called degrees of freedom) will be the total
number of data points, N. If specified as a sample, the divisor will be N-1.

If x¡ is an observation, N is the number of observations, and µ is the mean of all of the
observations, the formula for calculating the standard deviation for a population is:

To calculate the standard deviation for a sample, the mean is calculated using the sample
observations, and the divisor is N-1 instead of N.

To calculate the standard deviation for a population, the syntax is:

STDP.field

To calculate the standard deviation for a sample, the syntax is:

STDS.field

80

2. Displaying Report Data

where:

field

Numeric

Is the set of observations for the standard deviation calculation.

Example:

Calculating the Standard Deviation of a Population

The following request calculates the standard deviation of the population of the DOLLARS field
converted to double precision.

DEFINE FILE ibisamp/ggsales
DOLLARS/D12.2 = DOLLARS;
END
TABLE FILE ibisamp/ggsales
SUM DOLLARS STDP.DOLLARS
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

The output is shown in the following image.

Using Report-Level Prefix Operators

Report level prefix operators are available for headings, footings, subheadings, subfootings,
verb objects, and calculated values (COMPUTEs) that calculate the average, maximum,
minimum, and count for the entire report. They are based on the TOT. operator, which
calculates total values to include in a heading.

These operators cannot be referenced in WHERE or WHERE TOTAL tests. However, they can be
used in a COMPUTE command to generate a calculated value that can be used in a WHERE
TOTAL test.

Syntax:

How to Calculate Report-Level Average, Maximum, Minimum, and Count Values

operator.field

Creating Reports With TIBCO® WebFOCUS Language

 81

Manipulating Display Fields With Prefix Operators

where:

operator

Can be one of the following prefix operators.

TOTAVE. Calculates the average value of the field for the entire table.

TOTMAX. Calculates the maximum value of the field for the entire table.

TOTMIN. Calculates the minimum value of the field for the entire table.

TOTCNT. Calculates the count of the field instances for the entire table.

field

Is a verb object or calculated value in the request.

Example:

Using Prefix Operators in a Heading

The following request uses prefix operators in the heading.

TABLE WF_RETAIL_LITE
HEADING
"Heading Calculations:"
"Total:      <TOT.COGS_US"
"Count:                   <TOTCNT.COGS_US"
"Average:           <TOTAVE.COGS_US"
"Minimum:            <TOTMIN.COGS_US"
"Maximum:      <TOTMAX.COGS_US"
SUM COGS_US CNT.COGS_US AS Count AVE.COGS_US AS Average
MIN.COGS_US AS Minimum MAX.COGS_US AS Maximum
BY BUSINESS_REGION AS Region
BY PRODUCT_CATEGORY AS Category
WHERE BUSINESS_REGION NE 'Oceania'
ON TABLE SUBTOTAL COGS_US CNT.COGS_US  AS Total
ON TABLE SET PAGE NOPAGE
ON TABLE SET SHOWBLANKS ON
ON TABLE SET STYLE *
type=report,grid=off, size=11,$
ENDSTYLE
END

82

The output is shown in the following image.

2. Displaying Report Data

Reference: Usage Notes for Report-Level Prefix Operators

These operators can be used on a field in a heading or footing without being referenced in
a display command in the request.

Creating Reports With TIBCO® WebFOCUS Language

 83

Displaying Pop-up Field Descriptions for Column Titles

They work in a heading or footing for real or virtual (DEFINE) fields. They work in a display
command field list on real fields, virtual (DEFINE) fields, and calculated (COMPUTE) values
that are calculated prior to their use in the request.

They can be used in subheadings and subfootings to reference the total value for the entire
report.

Displaying Pop-up Field Descriptions for Column Titles

You can have pop-up field descriptions display in an HTML report when the mouse pointer is
positioned over column titles. Field description text displays in a pop-up box near the column
title using the default font for the report. Pop-up text appears for report column titles including
titles created with ACROSS phrases and stacked column titles created with OVER phrases.

The pop-up text displayed for a column title is defined by the Description attribute in the
Master File for the corresponding field. If a column title has no Description entry in the Master
File, then no pop-up box is generated when your mouse is positioned over the title.

For more information about the Description attribute, see Null or MISSING Values: MISSING in
the Describing Data With WebFOCUS Language manual.

Syntax:

How to Use the POPUPDESC Command

SET POPUPDESC = {ON|OFF}

where:

ON

Enables pop-up field descriptions when your mouse pointer is positioned over column
titles.

OFF

Disables pop-up field descriptions when your mouse pointer is positioned over column
titles. OFF is the default value.

Example:

Using the POPUPDESC Command

The Master File referenced by the report contains the following:

FIELD=UNITS, ALIAS=E10, FORMAT=I08, TITLE='Unit Sales',
 DESC='Number of units sold',$

84

2. Displaying Report Data

The code used to create the report is:

TABLE FILE GGSALES
SUM UNITS
BY REGION
BY PRODUCT
WHERE REGION EQ 'Midwest'
ON TABLE SET POPUPDESC ON
END

The following image shows the report output and the pop-up field description text that displays
when your mouse pointer is positioned over the Unit Sales column title.

Reference: Distributing Reports With Pop-up Field Descriptions Using ReportCaster

Distributing an HTML report containing pop-up field descriptions with ReportCaster requires the
use of JavaScript components located on the WebFOCUS Client. To access these components
from a report distributed by ReportCaster, the scheduled procedure must contain the SET
FOCHTMLURL command, which must be set to an absolute URL, instead of the default value.
For example,

SET FOCHTMLURL = http://hostname[:port]/ibi_apps/ibi_html

where:

hostname[:port]

Is the host name and optional port number (specified only if you are not using the default
port number) where the WebFOCUS Web application is deployed.

Creating Reports With TIBCO® WebFOCUS Language

 85

Displaying Pop-up Field Descriptions for Column Titles

ibi_apps/ibi_html

ibi_apps is the site-customized web server alias pointing to the WEBFOCUS81/ibi_apps
directory (where ibi_apps is the default value). ibi_html is a directory within the path to the
JavaScript files that are required to be accessible.

For more information about coding reports for use with ReportCaster, see the Tips and
Techniques for Coding a ReportCaster Report appendix in the ReportCaster manual.

86

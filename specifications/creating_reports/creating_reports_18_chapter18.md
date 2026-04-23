Chapter18

Controlling Report Formatting

When you format a report, you can control how the formatting is applied. You can:

Generate an internal cascading style sheet for HTML reports. This improves
performance and provides more formatting options.

Apply formatting conditionally. You can make the appearance of a report conditional
based on the report values. You can also make its links to other reports and Internet
resources conditional. For example, in a monthly order report, you can specify that all
unpaid orders be displayed in red and be linked to a recent payment history report of
a customer.

Select a scale for specifying measurements, such as the size of a report top margin.
You can select an inch, centimeter, or point as the unit of measure.

Control the display of empty reports. If a report request returns no records, you can
choose to display the report without data, or to display a message stating there is no
output.

In this chapter:

Generating an Internal Cascading Style Sheet for HTML Reports

Selecting a Unit of Measurement

Conditionally Formatting, Displaying, and Linking in a StyleSheet

Including Summary Lines, Underlines, Skipped Lines, and Page Breaks

Conditionally Including Summary Lines, Underlines, Skipped Lines, and Page Breaks

Controlling the Display of Empty Reports

Formatting a Report Using Only StyleSheet Defaults

Creating Reports With TIBCO® WebFOCUS Language

 1219

Generating an Internal Cascading Style Sheet for HTML Reports

Generating an Internal Cascading Style Sheet for HTML Reports

When you create a report in HTML format, code is generated that specifies how the report is
formatted. You can set up your report to generate an internal cascading style sheet as part of
this HTML code. This will:

Improve performance by significantly reducing the size of the HTML file, decreasing
transmission bandwidth, and displaying large reports more quickly.

Provide more formatting options for your HTML report. Some WebFOCUS StyleSheet
attributes are supported for HTML display format only in reports that generate an internal
cascading style sheet.

Internal cascading style sheets enable HTML support for the UNITS, BOTTOMMARGIN,
TOPMARGIN, LEFTMARGIN, RIGHTMARGIN, SIZE, POSITION, WRAP, and PAGECOLOR
attributes. It also enables you to add and remove underlines from most report components
and specify the starting position and size of an image. For details on the UNITS attribute,
see Selecting a Unit of Measurement on page 1221. For more information on all other
attributes, see Laying Out the Report Page on page 1331.

You can generate an internal cascading style sheet and apply an external cascading style
sheet in the same report request. If any formatting instructions conflict, the internal cascading
style sheet should override the external cascading style sheet.

Note: In most cases, you should not specify native WebFOCUS StyleSheet attributes and
external CSS classes in the same report or style sheet. For more information, see Using an
External Cascading Style Sheet on page 1293.

Syntax:

How to Generate an Internal Cascading Style Sheet

You can have an internal cascading style sheet created as part of the HTML code that is
generated for a report in HTML format. To do so:

Outside of a report request, use

SET HTMLCSS = {ON|OFF}

Within a report request, use

ON TABLE SET HTMLCSS {ON|OFF}

where:

ON

Generates an internal cascading style sheet in the HTML output to control most aspects of
the report appearance. ON is the default value.

1220

18. Controlling Report Formatting

OFF

Turns off the generation of an internal cascading style sheet. Instead, formatting tags are
placed in each HTML table cell used to create the report.

Reference: Requirements for Internal Cascading Style Sheets

If you wish to display a report formatted via an internal cascading style sheet (CSS), you must
have a web browser that supports cascading style sheets. Microsoft Internet Explorer Version
5.0 or higher, support cascading style sheets.

Note that how an internal cascading style sheet formats your report is determined entirely by
your web browser support and implementation of cascading style sheets, not by WebFOCUS.
Some web browsers may not fully support the latest CSS version, or may implement a CSS
feature in a different way.

Selecting a Unit of Measurement

You can select the unit of measurement for page margins and column width for HTML reports
that generate an internal cascading style sheet, as well as PDF and PostScript reports. In
addition, you can also select the unit of measurement for column position in PDF and PS
reports. You can select inches, centimeters, or points as the unit of measure.

If you change the unit of measure, all existing measurements are automatically converted to
the new scale. For example, if the unit of measure is inches and the top margin for the report
is set to 1, and you later change the unit of measure to centimeters, the size of the top margin
is automatically converted to 1 centimeter.

You can set the unit of measure using a:

StyleSheet by using the UNITS attribute.

SET command by using the UNITS parameter.

Syntax:

How to Set the Unit of Measurement

To set a unit of measurement:

In a StyleSheet, add the following attribute

UNITS = units

Outside of a report request, use

SET UNITS = units

Creating Reports With TIBCO® WebFOCUS Language

 1221

Conditionally Formatting, Displaying, and Linking in a StyleSheet

Within a report request, use

ON TABLE SET UNITS units

where:

units

Is the unit of measure. Values can be:

INCHES, that specifies the unit of measure as inches. This is the default value.

CM, that specifies the unit of measure as centimeters.

PTS, that specifies the unit of measure as points. Points is a common measurement
scale for typefaces.

Conditionally Formatting, Displaying, and Linking in a StyleSheet

You can conditionally format report components, display a graphic, and include links in your
report based on the values in your report. Using conditional styling, you can:

Draw attention to particular items in the report.

Emphasize differences between significant values.

Customize the resources to which an end user navigates from different parts of the report.

To conditionally format reports, add the WHEN attribute to a StyleSheet declaration. The WHEN
attribute specifies a condition that is evaluated for each instance of a report component (that
is, for each cell of a tabular report column, each element in a graph, or each free-form report
page). The StyleSheet declaration is applied to each instance that satisfies the condition, and
is ignored by each instance that fails to satisfy the condition.

You can also apply sequential conditional formatting.

Note: The variables TABPAGENO and TABLASTPAGE cannot be used to define styling with
conditional styling (WHEN).

1222

Applying Sequential Conditional Formatting

18. Controlling Report Formatting

You can apply sequential conditional logic to a report component by creating a series of
declarations, each with a different condition. This is the StyleSheet equivalent of a sequence
of nested IF-THEN-ELSE statements. When several conditional declarations specify the same
report component (for example, the same column) and evaluate the same field in the
condition, they are processed together as a group. For each instance of the report component
(for example, for each cell of a column):

1. The conditional declarations in the "group" are evaluated, in the order in which they are
found in the StyleSheet, until one of the conditions is satisfied. That declaration is then
applied to that instance of the report component. The other conditional declarations in the
"group," and any non-conditional declarations that specify the same report component and
the same attributes, are ignored for that instance.

2. If, however, none of the conditional declarations have been satisfied for that instance, then

the first unconditional declaration for that report component that specifies the same
attribute(s) is applied to that instance.

3. Any unconditional declarations for that report component that specify other attributes (that
is, attributes that have not already been applied to the instance in Steps 1 or 2) are now
applied to the instance.

4. The entire process is repeated for the next instance of the report component (for example,

for the next cell of the column).

Syntax:

How to Conditionally Format, Display, or Link in a StyleSheet

TYPE=type, [subtype,] attributes, WHEN=field1 operator {field2|value},$

or

TYPE=type, [subtype,] attributes, WHEN=FORECAST, $

where:

type

Is the value of the TYPE attribute. You can specify any report component. For details, see
Identifying a Report Component in a WebFOCUS StyleSheet on page 1249.

subtype

Are any additional attributes, such as COLUMN, ACROSS, or ITEM, that are needed to
identify the report component to which you are applying the declaration.

attributes

Are the attributes in the StyleSheet declaration that are made conditional by the WHEN
attribute. They can include most formatting, graphic images, and hyperlink attributes.

Creating Reports With TIBCO® WebFOCUS Language

 1223

Conditionally Formatting, Displaying, and Linking in a StyleSheet

field1, field2

Identifies the report fields that are being compared. Each one can be:

The name of a display field or vertical or horizontal sort field in a graph or tabular
report. ACROSS values can be used as part of the conditional expressions used to
define styling attributes for each cell in the table.

A column reference in a graph or tabular report.

The name of an embedded field in the heading or footing of a free-form report.

If you wish to use a field that you do not want to display in the report, you can specify the
field in the report request, and use the NOPRINT option to prevent the field from being
displayed (for example, PRINT fieldname NOPRINT).

To apply a prefix operator to a field in a report, you can:

Use the same prefix operator in the WHEN attribute. You must refer to the field by
name in the WHEN attribute (for example, WHEN=AVE.PRICE GT 300).

Refer to the field in the WHEN attribute by column position and omit the prefix operator
(for example, WHEN=N3 GT 300). This is not supported for the ST. and CT. prefix
operators.

You cannot use compound boolean expressions with the WHEN attribute.

The field cannot be a packed (P) numeric field.

operator

Defines how the condition is satisfied. You can use these relational operators:

EQ where the condition is satisfied if the values on the left and right are equal. If the
values being compared are alphanumeric, their case (uppercase, lowercase, or mixed
case) must match.

NE where the condition is satisfied if the values on the left and right are not equal.

LT where the condition is satisfied if the value on the left is less than the value on the
right.

LE where the condition is satisfied if the value on the left is less than or equal to the value
on the right.

GT where the condition is satisfied if the value on the left is greater than the value on the
right.

GE where the condition is satisfied if the value on the left is greater than or equal to the
value on the right.

1224

18. Controlling Report Formatting

value

Is a constant, such as a number, character string, or date. You must enclose non-numeric
constants, such as character strings and dates, in single quotation marks.

Although you cannot use functions or operators here to specify the value, you can define a
temporary field (COMPUTE or DEFINE) using functions and operators, use the temporary
field in the report, and specify it here instead of a constant.

FORECAST

Identifies fields that are generated using the FORECAST command.

Example:

Using Sequential Conditional Formatting

This example illustrates how to apply sequential conditional formatting to a report. This report
uses sequential conditional logic to format each row based on its order total (LINEPRICE).

   TABLE FILE CENTORD
   HEADING
   "Order Revenue"
   " "
   SUM ORDER_DATE LINEPRICE AS 'Order,Total:'
   BY HIGHEST 10 ORDER_NUM
   ON TABLE SET PAGE-NUM OFF

   ON TABLE SET STYLESHEET *
   TYPE=REPORT, GRID=OFF, $
1. TYPE=DATA, BACKCOLOR=AQUA, STYLE=BOLD+ITALIC,
   WHEN=LINEPRICE GT 500000, $
2. TYPE=DATA, BACKCOLOR=YELLOW, STYLE=BOLD,
   WHEN=LINEPRICE GT 400000, $
3. TYPE=DATA, BACKCOLOR=ORANGE, STYLE=ITALIC,
   WHEN=LINEPRICE GT 100000, $
4. TYPE=DATA, BACKCOLOR=SILVER, FONT='Arial', $
   TYPE=HEADING, FONT='Arial', STYLE=BOLD, SIZE=11, $
   ENDSTYLE

   END

Notice that:

1. The first conditional declaration formats any rows whose order total is greater than

500,000.

2. The second conditional declaration formats any rows whose order total is greater than
400,000 and less than or equal to 500,000. This is because rows with an order total
greater than 500,000 would have already been formatted by the first conditional
declaration.

Creating Reports With TIBCO® WebFOCUS Language

 1225



Conditionally Formatting, Displaying, and Linking in a StyleSheet

3. The third conditional declaration formats any rows whose order total is greater than

100,000 and less than or equal to 400,000. This is because rows with an order total
greater than 400,000 would have already been formatted by one of the first two conditional
declarations.

4. The unconditional declaration following the conditional declarations specifies:

Background color, which is also specified by the conditional declarations. It applies
background color (silver) to any rows whose order total is less than or equal to
100,000, since those rows have not already been formatted by the conditional
declarations.

Font, which is not specified by the conditional declarations. It applies font (Arial) to all
data rows.

The output is:

Example:

Applying Basic Conditional Formatting

This example illustrates how to apply conditional formatting to a report. The conditional
formatting draws attention to orders that total more than 200,000.

Notice that because a particular column is not specified in the declaration, the formatting is
applied to the entire row.

1226

18. Controlling Report Formatting

TABLE FILE CENTORD
HEADING
"Order Revenue"
" "
SUM ORDER_DATE LINEPRICE AS 'Order,Total:'
BY HIGHEST 10 ORDER_NUM
ON TABLE SET PAGE-NUM OFF

ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
TYPE=DATA, BACKCOLOR=AQUA, STYLE=BOLD, WHEN=LINEPRICE GT 200000, $
TYPE=HEADING, FONT='Arial', STYLE=BOLD, SIZE=11, $
ENDSTYLE

END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1227



Conditionally Formatting, Displaying, and Linking in a StyleSheet

Example:

Applying Conditional Formatting to a Column

This example illustrates how you can use conditional formatting to draw attention to columns
that are not specified in the condition. The WHEN condition states that the order number for
orders exceeding 200,000 should display in boldface with an aqua background.

Notice that the column that is evaluated in the WHEN condition (LINEPRICE) is different from
the column that is formatted (ORDER_NUM); they do not need to be the same.

TABLE FILE CENTORD
HEADING
"Order Revenue"
" "
SUM ORDER_DATE LINEPRICE AS 'Order,Total:'
BY HIGHEST 10 ORDER_NUM
ON TABLE SET PAGE-NUM OFF

ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
TYPE=DATA, COLUMN=ORDER_NUM,
   BACKCOLOR=AQUA, STYLE=BOLD, WHEN=LINEPRICE GT 200000, $
TYPE=HEADING, FONT='Arial', STYLE=BOLD, SIZE=11, $
ENDSTYLE

END

1228



The output is:

18. Controlling Report Formatting

Example:

Conditionally Styling an ACROSS Value

The example below demonstrates how an ACROSS value can be referenced using either the
ACROSS field name or the ACROSS column designator (A1, A2).

Creating Reports With TIBCO® WebFOCUS Language

 1229

Conditionally Formatting, Displaying, and Linking in a StyleSheet

In this example, the ACROSS values are used in conditional styling to set a unique backcolor
for all ACROSS columns in the Category Coffee, and additional font styling for the Espresso
ACROSS column.

SET ACROSSTITLE=SIDE
TABLE FILE GGSALES
SUM DOLLARS/I8M AS ''
BY REGION
BY ST
BY CITY
ACROSS CATEGORY
ACROSS PRODUCT
WHERE CATEGORY EQ 'Coffee' OR 'Food';
ON TABLE SET PAGE-NUM NOPAGE
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
SQUEEZE=ON,UNITS=IN,ORIENTATION=PORTRAIT,$
TYPE=REPORT,FONT='ARIAL',SIZE=10,BORDER=LIGHT,$
TYPE=ACROSSTITLE,COLOR=WHITE, BACKCOLOR=GREY,$
TYPE=ACROSSVALUE,COLOR=WHITE, BACKCOLOR=GREY,$
TYPE=TITLE,COLOR=WHITE, BACKCOLOR=GREY,$
TYPE=DATA, ACROSSCOLUMN=DOLLARS, BACKCOLOR=THISTLE, WHEN=CATEGORY EQ
'Coffee',$
TYPE=DATA, ACROSSCOLUMN=DOLLARS, STYLE=BOLD+ITALIC, WHEN=A2 EQ 'Espresso', $
ENDSTYLE
END

The output is:

1230

18. Controlling Report Formatting

Example:

Conditionally Formatting a Data Visualization Bar Graph

This example illustrates how to apply conditional formatting to a data visualization bar graph.
This report request incorporates a data visualization bar chart to graphically represent the data
in the LINEPRICE column. It uses conditional formatting to draw attention to orders that total
more than 200,000. It conditionally applies that formatting both to the data columns
(TYPE=DATA) and to the bar graph (GRAPHTYPE=DATA).

Note that data visualization is only supported for HTML reports.

TABLE FILE CENTORD
HEADING
"Order Revenue"
" "
SUM ORDER_DATE LINEPRICE AS 'Order,Total:'
BY HIGHEST 10 ORDER_NUM
ON TABLE SET PAGE-NUM OFF

ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
TYPE=DATA, BACKCOLOR=AQUA, STYLE=BOLD, WHEN=LINEPRICE GT 200000, $
GRAPHTYPE=DATA, COLUMN=LINEPRICE, $
GRAPHTYPE=DATA, GRAPHCOLOR=AQUA, WHEN=LINEPRICE GT 200000,$
TYPE=HEADING, FONT='Arial', STYLE=BOLD, SIZE=11, $
ENDSTYLE

END

Creating Reports With TIBCO® WebFOCUS Language

 1231



Conditionally Formatting, Displaying, and Linking in a StyleSheet

The output is:

Example:

Applying Conditional Formatting Based on Hidden (NOPRINT) Field Values

This example illustrates how to apply conditional formatting based on the values of a hidden
(NOPRINT) field. This report uses conditional formatting to draw attention to those employees
who have resigned.

Notice that the WHEN attribute condition evaluates a field (STATUS) that is hidden in the
report. Although the field that is evaluated in the condition must be included in the report
request, you can prevent it from displaying in the report by using the NOPRINT option, as
shown in the following request.

1232

18. Controlling Report Formatting

TABLE FILE CENTHR
HEADING
"Employee List for Boston"
" "
"For Pay Levels 5+"
" "
"Resigned Employees Shown in <0>Red Bold"
" "
PRINT LNAME FNAME PAYSCALE STATUS NOPRINT
BY ID_NUM
WHERE PLANT EQ 'BOS' AND PAYSCALE GE 5
ON TABLE SET PAGE-NUM OFF

ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
TYPE=DATA, COLUMN=LNAME,
   COLOR=RED, FONT='Arial', STYLE=BOLD, WHEN=STATUS EQ 'RESIGNED', $
TYPE=DATA, COLUMN=FNAME,
   COLOR=RED, FONT='Arial', STYLE=BOLD, WHEN=STATUS EQ 'RESIGNED', $
TYPE=HEADING, FONT='Arial', STYLE=BOLD, SIZE=11, $
TYPE=HEADING, LINE=5, STYLE=-BOLD, $
TYPE=HEADING, LINE=5, ITEM=2, STYLE=BOLD, COLOR=RED, $
ENDSTYLE

END

Creating Reports With TIBCO® WebFOCUS Language

 1233



Conditionally Formatting, Displaying, and Linking in a StyleSheet

The output is:

Example:

Applying Conditional Formatting to a Sort Group

This example illustrates how to apply conditional formatting to a sort group. This report uses
conditional formatting to draw attention to those employees who have resigned.

Notice that one conditional declaration can apply formatting to all the sort group rows. You can
accomplish this by evaluating the sort field (STATUS) in the WHEN attribute condition.

1234

18. Controlling Report Formatting

TABLE FILE CENTHR
HEADING
"Employee List for Boston"
" "
"For Pay Levels 5+"
" "
PRINT LNAME FNAME PAYSCALE
BY STATUS SKIP-LINE
WHERE PLANT EQ 'BOS' AND PAYSCALE GE 5
ON TABLE SET PAGE-NUM OFF

ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
TYPE=DATA,
   COLOR=RED, FONT='Arial', STYLE=BOLD, WHEN=STATUS EQ 'RESIGNED',$
TYPE=HEADING, FONT='Arial', STYLE=BOLD, SIZE=11, $
ENDSTYLE

END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1235



Conditionally Formatting, Displaying, and Linking in a StyleSheet

In order to apply the same conditional formatting to only two columns, instead of all the
columns, this version of the report request uses two declarations, each specifying a different
column (LNAME and FNAME):

TABLE FILE CENTHR
HEADING
"Employee List for Boston"
" "
"Pay Levels 5+"
" "
PRINT LNAME FNAME PAYSCALE
BY STATUS SKIP-LINE
WHERE PLANT EQ 'BOS' AND PAYSCALE GE 5
ON TABLE SET PAGE-NUM OFF

ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
TYPE=DATA, COLUMN=LNAME,
   COLOR=RED, FONT='Arial', STYLE=BOLD, WHEN=STATUS EQ 'RESIGNED', $
TYPE=DATA, COLUMN=FNAME,
   COLOR=RED, FONT='Arial', STYLE=BOLD, WHEN=STATUS EQ 'RESIGNED', $
TYPE=HEADING, FONT='Arial', STYLE=BOLD, SIZE=11, $
ENDSTYLE

END

1236



The output is:

18. Controlling Report Formatting

Example:

Applying Conditional Formatting to Forecasted Values

The following illustrates how you can apply conditional formatting to forecasted values in a
report.

Creating Reports With TIBCO® WebFOCUS Language

 1237

Conditionally Formatting, Displaying, and Linking in a StyleSheet

DEFINE FILE GGSALES
SDATE/YYM = DATE;
SYEAR/Y = SDATE;
SMONTH/M = SDATE;
PERIOD/I2 = SMONTH;
END

TABLE FILE GGSALES
SUM UNITS DOLLARS
BY CATEGORY BY PERIOD
WHERE SYEAR EQ 97 AND CATEGORY EQ 'Coffee'
ON PERIOD RECAP MOVAVE/D10.1= FORECAST(DOLLARS,1,3,'MOVAVE',3);
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=REPORT, BACKCOLOR=SILVER, WHEN=FORECAST, $
ENDSTYLE
END

The output is:

1238


Including Summary Lines, Underlines, Skipped Lines, and Page Breaks

18. Controlling Report Formatting

You can include sort-based options such as subtotals and other summary lines, sort headings
and footings, underlines, skipped lines, and page breaks, as well as restart page numbering,
by using the ON phrase in your report request. The ON phrase specifies an option that can be
triggered by the change in a sort field or display field. The sort-based option (summary line,
underline, skipped line, or page break) is applied to each sort group.

To make report requests flexible, options may be included that are not needed in every
situation. User selections then control the options used for each execution of the request.

By default, if the field referenced in the ON phrase is not present in the request, or if the
option is not supported with the type of field specified, the following message is generated and
processing terminates:

(FOC013) The 'ON FIELDNAME' FIELD IS NOT A SORT FIELD: sortfield

You can use the SET ONFIELD =IGNORE command to instruct WebFOCUS to ignore ON phrases
that reference absent fields or fields that are not supported by the specified option.

Note that any field used must be present in the Master File for the data source or the following
message is generated and execution terminates:

(FOC003) THE FIELDNAME IS NOT RECOGNIZED: field

Syntax:

How to Display Summary Lines, Underlines, Skipped lines, and Page Breaks

{BY|ON} sortfield option [[AND] option ...]

where:

BY|ON

These are functionally identical. The only difference is syntactic (BY enables you to specify
the sort-based feature as part of the sort phrase, while ON enables you to specify it
separately from the sort phrase). For more information, see the documentation for the
sortfield option you are using.

sortfield

Is the name of a vertical sort (BY) field.

Creating Reports With TIBCO® WebFOCUS Language

 1239

Including Summary Lines, Underlines, Skipped Lines, and Page Breaks

option

Is one of the following sort-based features: PAGE-BREAK, PAGE-BREAK REPAGE, RECAP,
RECOMPUTE, SKIP-LINE, SUBFOOT, SUBHEAD, SUBTOTAL, SUB-TOTAL, SUMMARIZE,
UNDER-LINE.

AND

Can be included between two sets of sortfield options to enhance readability.

Syntax:

How to Control Processing of ON Phrases

SET ONFIELD = {ALL|IGNORE}

ON TABLE SET ONFIELD {ALL|IGNORE}

where:

ALL

Issues a message and terminates execution when a field referenced in an ON phrase is
not present in the request. ALL is the default value.

IGNORE

Ignores ON phrases that reference fields that are not present in the request, as well as ON
phrases that include options not supported by the type of field specified.

Example:

Ignoring ON Phrases for Absent Fields

The following request against the EMPDATA data source has ON phrases for the fields DEPT,
DIV, and PIN. PIN is a sort field, but the other sort field must be entered at run time as the
amper variable &F1:

SET USER = EUSER
 TABLE FILE EMPDATA
   SUM SALARY
   BY &F1
   BY PIN
      ON DEPT SKIP-LINE NOSPLIT
      ON &F1  SUBTOTAL
      ON DIV   PAGE-BREAK
      ON TABLE SET ONFIELD ALL
 END

Run the request supplying the value DEPT for the variable &F1. The following messages are
generated:

 ERROR AT OR NEAR LINE      8  IN PROCEDURE IGNORE3 FOCEXEC *
(FOC013) THE 'ON FIELDNAME' FIELD IS NOT A SORT FIELD: DIV
 BYPASSING TO END OF COMMAND
(FOC009) INCOMPLETE REQUEST STATEMENT

1240

Now change the value of the ONFIELD parameter to IGNORE and run the request again,
supplying the value DEPT for the variable &F1. The partial output is:

18. Controlling Report Formatting

DEPT                  PIN                 SALARY
----                  ---                 ------

ACCOUNTING            000000070       $83,000.00
                      000000100       $32,400.00
                      000000300       $79,000.00
                      000000370       $62,500.00
                      000000400       $26,400.00

*TOTAL ACCOUNTING                    $283,300.00

ADMIN SERVICES        000000170       $30,800.00
                      000000180       $25,400.00

*TOTAL ADMIN SERVICES                 $56,200.00

Conditionally Including Summary Lines, Underlines, Skipped Lines, and Page Breaks

You can conditionally include sort-based options such as subtotals and other summary lines,
sort headings and footings, underlines, skipped lines, and page breaks, as well as
conditionally restart page numbering, by using the WHEN phrase in your report request. The
WHEN phrase specifies a condition that is evaluated for each value of a vertical sort (BY) field.
The sort-based option (summary line, underline, skipped line, or page break) is applied to each
sort group that satisfies the condition, and is ignored by sort groups that do not satisfy the
condition.

The WHEN phrase is an extension of the ON sortfield and BY sortfield phrases. You can specify
a WHEN phrase for each sortfield phrase. For example:

ON ORDER_NUM UNDER-LINE WHEN QUANTITY GT 5
ON COUNTRY PAGE-BREAK WHEN LINEPRICE GT 200000

If a sortfield phrase includes several sort-related options, you can specify a different WHEN
phrase for each option. For example:

ON ORDER_NUM SKIP-LINE WHEN QUANTITY GT 5; UNDER-LINE WHEN QUANTITY GT 10

Creating Reports With TIBCO® WebFOCUS Language

 1241






Conditionally Including Summary Lines, Underlines, Skipped Lines, and Page Breaks

Syntax:

How to Conditionally Display Summary Lines, Underlines, Skipped lines, and Page
Breaks

{BY|ON} sortfield [option WHEN condition [;] [AND]]...

where:

BY|ON

These are functionally identical. The only difference is syntactic (BY enables you to specify
the sort-based feature as part of the sort phrase, while ON enables you to specify it
separately from the sort phrase). For more information, see the documentation for the
sortfield option you are using.

sortfield

Is the name of a vertical sort (BY) field.

option

Is one of the following sort-based features: PAGE-BREAK, PAGE-BREAK REPAGE, RECAP,
RECOMPUTE, SKIP-LINE, SUBFOOT, SUBHEAD, SUBTOTAL, SUB-TOTAL, SUMMARIZE,
UNDER-LINE.

If you specify SUBHEAD or SUBFOOT, you must place the WHEN phrase on the line
following the text of the heading or footing.

condition

Is a logical expression. For more information, see Using Expressions on page 429.

You must enclose non-numeric constants, such as character strings and dates, in single
quotation marks.

If the condition evaluates a numeric detail field, it evaluates the sum of the detail field
values within each sort group, not the individual detail values. For example, in the request

TABLE FILE CENTHR
PRINT ID_NUM SALARY
BY PLANT
ON PLANT UNDER-LINE
WHEN SALARY GT 2000000
END

the condition evaluates the sum of the SALARY values within each PLANT value.

If the condition evaluates an alphanumeric field that appears multiple times in a sort
group, it evaluates the last value of the field in each sort group.

You can apply a prefix operator to a field in the condition (for example, WHEN AVE.PRICE
GT 300) even if the operator and the field are not used in the report. The aggregation is
performed for each value of the sort field.

1242

18. Controlling Report Formatting

If the BY or ON phrase includes several options, the WHEN condition applies only to the
option that immediately precedes it.

Is required if WHEN phrases are being included for several options in this BY or ON
phrase. In all other situations it is optional and just enhances readability.

;

AND

Can be included between two sets of sortfield options to enhance readability.

Example:

Using a WHEN Condition for a Sort Option

This example illustrates how to conditionally display a sub footing in a report. This report uses
a conditional sort footing to draw attention to orders that total less than 200,000.

TABLE FILE CENTORD
HEADING
"Order Revenue"
" "
SUM ORDER_DATE LINEPRICE AS 'Order,Total:'
BY HIGHEST 5 ORDER_NUM

ON ORDER_NUM
    SUBFOOT
       "--- Order total is less than $200,000 ---"
       " "
       WHEN LINEPRICE LT 200000

ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1243



Conditionally Including Summary Lines, Underlines, Skipped Lines, and Page Breaks

The output is:

Example:

Using WHEN Conditions for Multiple Sort Options

This example illustrates how to apply multiple conditions to a report component. This report
uses conditional sort footings to distinguish between orders that total more than 200,000 and
less than 200,000.

Notice that one sort phrase (ON ORDER_NUM) specifies several sort-related options (two
different SUBFOOT phrases), and that each option has its own WHEN phrase.

TABLE FILE CENTORD
HEADING
"Order Revenue"
" "
SUM ORDER_DATE LINEPRICE AS 'Order,Total:'
BY HIGHEST 5 ORDER_NUM
ON ORDER_NUM
   SUBFOOT
      "--- Order total is less than $200,000 ---"
      " "
      WHEN LINEPRICE LT 200000;
   SUBFOOT
      "+++ Order total is greater than or equal to $200,000 +++"
      " "
      WHEN LINEPRICE GE 200000;

ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

1244


The output is:

18. Controlling Report Formatting

Creating Reports With TIBCO® WebFOCUS Language

 1245

Controlling the Display of Empty Reports

Controlling the Display of Empty Reports

If a report request returns no records (for example, because no records satisfy its selection
criteria, or because the data source has no records), you can choose to display or print:

An empty report, that is, the report without data but including column titles, a report
heading (if one was specified in the report request), and a page heading (if one was
specified).

To do this, set the EMPTYREPORT parameter to ON.

A message stating that there is no report output.

This is the default. You can return to the default by setting the EMPTYREPORT parameter to
OFF.

This applies to tabular reports, not to free-form reports and graphs.

SET EMPTYREPORT = OFF is not supported with DOC format.

If you have created a report that contains a WHERE TOTAL statement and the test yields zero
records, an empty report will display.

Syntax:

How to Control the Display of an Empty Report

You can control what is displayed (or printed) when a report request returns no records, using
the EMPTYREPORT parameter. To issue the SET command:

Outside of a report request, use the syntax

SET EMPTYREPORT = {ANSI|ON|OFF}

Within a report request, use the syntax

ON TABLE SET EMPTYREPORT {ANSI|ON|OFF}

where:

ANSI

Produces a single-line report and displays the missing data character or a zero if a COUNT
is requested. In each case, &RECORDS will be 0, and &LINES will be 1.

If the SQL Translator is invoked, ANSI automatically replaces OFF as the default setting for
EMPTYREPORT.

1246

18. Controlling Report Formatting

ON

OFF

Specifies that the report will be displayed without data but with column titles, a report
heading (if one was specified in the report request), and a page heading (if one was
specified).

Specifies that a message will be displayed indicating that there is no report output. OFF is
the default value.

Example:

Controlling the Display of Empty Reports

The following request does not retrieve any records and sets the EMPTYREPORT parameter to
OFF.

SET EMPTYREPORT=OFF
TABLE FILE WF_RETAIL_LITE
HEADING
"This is the heading"
SUM COGS_US REVENUE_US COLUMN-TOTAL ROW-TOTAL
BY COUNTRY_NAME
WHERE COUNTRY_NAME EQ 'Louisiana'
FOOTING
"This is the footing"
ON TABLE SET STYLE *
GRID=OFF,$
END

The following output is produced.

0 NUMBER OF RECORDS IN TABLE=        0  LINES=      0

Changing the EMPTYREPORT setting to ON produces the output shown in the following image.

Creating Reports With TIBCO® WebFOCUS Language

 1247

Formatting a Report Using Only StyleSheet Defaults

Changing the EMPTYREPORT setting to ANSI produces the output shown in the following
image.

Formatting a Report Using Only StyleSheet Defaults

You can format a report using only default StyleSheet values. This does not permit you to
specify specific formatting, and does not access a StyleSheet.

Each display format, such as HTML or PDF, has its own set of defaults. For example, HTML
defaults to a proportional font, while PDF defaults to a monospace font. For information on the
default value of a specific StyleSheet attribute, see the documentation for that attribute.

Syntax:

How to Format a Report Using Only StyleSheet Defaults

To use only default StyleSheet values to format:

All report requests within a procedure. Issue the following command at the beginning of
the procedure.

SET STYLE[SHEET] = ON

One report request. Issue the following command within the request.

ON TABLE SET STYLE[SHEET] ON

where:

SHEET

Can be omitted to make the command shorter, and has no effect on its behavior.

1248

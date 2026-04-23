Chapter21

Laying Out the Report Page

You can customize page layout using StyleSheet attributes. The page layout attributes
available to you, like all other attributes, depend on the display format. For instance,
some attributes support print-oriented display formats such as PDF, and they do not
apply to HTML reports displayed in a browser. For details on display formats, see
Choosing a Display Format on page 575 and Saving and Reusing Your Report Output on
page 471.

A report page has default layout characteristics. However, you can change any of them to
customize the layout. You control a report's appearance, including column arrangement
on a page, page numbering, page breaks, use of grids and images, and much more.

You can use SET parameters in place of most StyleSheet attributes to define page layout
characteristics. For details on SET, see the Developing Reporting Applications manual.

In this chapter:

Selecting Page Size, Orientation, and
Color

Setting Page Margins

Positioning a Report Component

Arranging Columns on a Page

Suppressing Column Display

Inserting a Page Break

Inserting Page Numbers

Adding Grids and Borders

Defining Borders Around Boxes With
PPTX and PDF Formats

Displaying Superscripts On Data,
Heading, and Footing Lines

Adding Underlines and Skipped Lines

Removing Blank Lines From a Report

Adding an Image to a Report

Associating Bar Graphs With Report Data

Working With Mailing Labels and Multi-
Pane Pages

Selecting Page Size, Orientation, and Color

You can select the page size, page orientation (portrait or landscape), and page color for your
report. The default page size is letter (8.5 x 11 inches), but you can select from many other
sizes, including legal and envelopes.

Creating Reports With TIBCO® WebFOCUS Language

 1331

Selecting Page Size, Orientation, and Color

Reference: Page Size, Orientation, and Color Attributes

Attribute

PAGESIZE

Description

Applies to

Sets page size.

In the Development environment:

PDF

PS

PPT

PPTX

ORIENTATION

Sets page orientation.

In the Development environment:

PDF

PS

EXL2K

PPT

PPTX

HTML report with internal
cascading style sheet

PPTX

Note: The PAGECOLOR
StyleSheet attribute is ignored in
a report containing a template, in
order to preserve the styles in the
template.

PAGECOLOR

Sets page color.

Syntax:

How to Set Page Size

This syntax applies to a PDF, PS, PPT, or PPTX report.

1332

21. Laying Out the Report Page

[TYPE=REPORT,] PAGESIZE={size|LETTER}, $

where:

TYPE=REPORT

Applies the page size to the entire report. Not required, as it is the default value.

size

Is the page size. If printing a report, the value should match the size of the paper.
Otherwise, the report may be cropped or printed with extra blank space.

Valid values are:

Value

SCREEN

LETTER

LEGAL

CUSTOM

Description

Sets the page size so that the report fills the
screen. Each print line is infinitely wide. The
report width determines the page width. The
number of lines per page depends on how many
lines fit on the screen. This number varies,
depending on the font and screen resolution.

8.5 x 11 inches. LETTER is the default value.

8.5 x 14 inches.

Enables you to set a custom page size for a
DHTML, PDF, or PPTX report. If you use the
CUSTOM option, you can specify the length and
width values in the request using CUSTOM-PAGE-
LENGTH=number and CUSTOM-PAGE-
WIDTH=number through a SET command or
StyleSheet attribute. The number value you
specify depends on the UNITS parameter (inches,
centimeters, points). The default is inches.

TABLOID

LEDGER

11 x 17 inches.

17 x 11 inches.

WIDESCREEN

13.333 x 7.5 inches.

Creating Reports With TIBCO® WebFOCUS Language

 1333

Selecting Page Size, Orientation, and Color

Value

C

D

E

STATEMENT

EXECUTIVE

FOLIO

10x14

A3

A4

A5

B4

B5

QUARTO

ENVELOPE-9

ENVELOPE-10

ENVELOPE-11

ENVELOPE-12

ENVELOPE-14

Description

17 x 22 inches.

22 x 34 inches.

34 x 44 inches.

5.5 x 8.5 inches.

7.5 x 10.5 inches.

8.5 x 13 inches.

10 x 14 inches.

297 x 420 millimeters.

210 x 297 millimeters.

148 x 210 millimeters.

250 x 354 millimeters.

182 x 257 millimeters.

215 x 275 millimeters.

3.875 x 8.875 inches.

4.125 x 9.5 inches.

4.5 x 10.375 inches.

4.5 x 11 inches.

5 x 11.5 inches.

ENVELOPE-MONARCH

3.875 x 7.5 inches.

1334

21. Laying Out the Report Page

Value

Description

ENVELOPE-PERSONAL

3.625 x 6.5 inches.

ENVELOPE-DL

ENVELOPE-C3

ENVELOPE-C4

ENVELOPE-C5

ENVELOPE-C6

110 x 220 millimeters.

324 x 458 millimeters.

229 x 324 millimeters.

162 x 229 millimeters.

114 x 162 millimeters.

ENVELOPE-C65

114 x 229 millimeters.

ENVELOPE-B4

ENVELOPE-B5

ENVELOPE-B6

250 x 353 millimeters.

176 x 250 millimeters.

176 x 125 millimeters.

ENVELOPE-ITALY

110 x 230 millimeters.

US-STANDARD-FANFOLD

14.875 x 11 inches.

GERMAN-STANDARD-FANFOLD

8.5 x 12 inches.

GERMAN-LEGAL-FANFOLD

8.5 x 13 inches.

Syntax:

How to Set Page Orientation

This syntax applies to a PDF, PS, or EXL2K report.

[TYPE=REPORT,] ORIENTATION={PORTRAIT|LANDSCAPE}, $

where:

TYPE=REPORT

Applies the page orientation to the entire report. Not required, as it is the default.

Creating Reports With TIBCO® WebFOCUS Language

 1335

Selecting Page Size, Orientation, and Color

PORTRAIT

Displays the report across the narrower dimension of a vertical page, producing a page
that is longer than it is wide. PORTRAIT is the default value.

LANDSCAPE

Displays the report across the wider dimension of a horizontal page, producing a page that
is wider than it is long.

Example:

Setting Page Orientation

This request sets the page orientation of a PDF report to landscape.

SET ONLINE-FMT = PDF
TABLE FILE CENTQA
SUM CNT.PROBNUM AS 'Total Number, of Problems'
SUM CNT.PROBNUM AS 'Problems From, Each Plant' BY PLANT
SUM CNT.PROBNUM AS 'Problem by Product' BY PLANT BY PRODNAME
ON PLANT PAGE-BREAK
HEADING CENTER
"QA Report for Company, Plant, and Product"
" "
ON TABLE COLUMN-TOTAL
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, ORIENTATION=LANDSCAPE, $
ENDSTYLE
END

Syntax:

How to Set Page Color

This syntax applies to an HTML report with internal cascading style sheet.

[TYPE=REPORT,] ... PAGECOLOR=color, ... , $

where:

TYPE=REPORT

The TYPE specification is optional with this feature. If omitted, TYPE defaults to REPORT.

color

Is a supported color. For a list of values, see Formatting Report Data on page 1697.

1336

Example:

Setting Page Color

This request sets the page color of an HTML report with internal cascading style sheet to
silver.

21. Laying Out the Report Page

SET HTMLCSS = ON
TABLE FILE CENTORD
ON TABLE SUBHEAD
"SELECTED PRODUCT INVENTORY"
SUM QTY_IN_STOCK/D12 BY PROD_NUM BY SNAME BY STATE
WHERE PROD_NUM EQ '1004'
WHERE SNAME EQ 'eMart'
WHERE STATE EQ 'CA'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, PAGECOLOR=SILVER, GRID=OFF, $
ENDSTYLE
END

The output is:

Setting Page Margins

You can set the page margins for your report. This includes the top, bottom, left, and right
margins. You can also change the default unit of measurement (inches) to either centimeters
or points. The unit of measurement applies to page margins, column width, and column
position.

Reference: Page Margin Attributes

Creating Reports With TIBCO® WebFOCUS Language

 1337

Setting Page Margins

Attribute

Description

Applies to

UNITS

Sets unit of measurement.

Used when specifying margin size or
other page characteristics. If you
change the current unit of
measurement, the new value is applied
to all instances in which unit of
measurement is used.

PDF

PS

HTML report with internal
cascading style sheet

TOPMARGIN
BOTTOMMARGIN
LEFTMARGIN
RIGHTMARGIN

Sets size of top, bottom, left, and right
margin.

PDF

PS

HTML report with internal
cascading style sheet

Syntax:

How to Set the Unit of Measurement

This syntax applies to a PDF, PS, or HTML report with internal cascading style sheet.

In a StyleSheet, add the following attribute

UNITS = units

Outside of a report request, use

SET UNITS = units

Within a report request, use

ON TABLE SET UNITS units

where:

units

Is the unit of measure. Values can be:

INCHES, which specifies the unit of measure as inches. This is the default value.

CM, which specifies the unit of measure as centimeters.

PTS, which specifies the unit of measure as points. Points is a common measurement
scale for typefaces.

1338

21. Laying Out the Report Page

Syntax:

How to Set Margin Size

This syntax applies to a PDF, PS, or HTML report with internal cascading style sheet.

[TYPE=REPORT,] [TOPMARGIN={value|.25},] [BOTTOMMARGIN={value|.25},]
 [LEFTMARGIN={value|.25},] [RIGHTMARGIN={value|.25},] $

where:

TYPE=REPORT

Applies the margin size to the entire report. Not required, as it is the default.

TOPMARGIN

Sets the top boundary of the report content.

BOTTOMMARGIN

Sets the bottom boundary of the report content.

LEFTMARGIN

Sets the left boundary of the report content.

RIGHTMARGIN

Sets the right boundary of the report content.

value

Is the size of the specified margin. The report content displays inside the margin. If
printing a report, specify a value compatible with the printer's print area. For example, if
the print area has 0.25 inch margins all around, set the margins to 0.25 inches, or larger.

The default value for all margins is 0.25 inches.

Creating Reports With TIBCO® WebFOCUS Language

 1339

Positioning a Report Component

Example:

Setting the Left Margin

This request sets the left margin of an HTML report with internal cascading style sheet to one
inch.

SET HTMLCSS = ON
TABLE FILE GGSALES
SUM CATEGORY PRODUCT DOLLARS BUDDOLLARS
BY REGION BY ST BY CITY
WHERE DOLLARS GT BUDDOLLARS
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
LEFTMARGIN = 1, $
ENDSTYLE
END

The output is:

Positioning a Report Component

A StyleSheet enables you to specify an absolute or relative starting position for a column,
heading, or footing, or element in a heading or footing. You can also add blank space around a
report component.

This topic addresses column positioning using the StyleSheet attribute POSITION. For details
on the column positioning command IN, see Positioning a Column on page 1367.

1340

For details on positioning a heading or footing, or an element in a heading or footing, see Using
Headings, Footings, Titles, and Labels on page 1517.

Reference: Positioning Attributes

21. Laying Out the Report Page

Attribute

Description

Applies to

POSITION

Sets absolute or relative starting position of a column.

PDF

PS

An absolute position is the distance from the left
margin of the printed paper.

A relative position is the distance from the default
position. After the first column, the default position is
the end of the preceding column.

TOPGAP
BOTTOMGAP

Adds blank space to the top or bottom of a report line.

PDF

LEFTGAP
RIGHTGAP

Adds blank space to the left or right of a report
column.

PS

PDF

PS

Syntax:

How to Specify the Starting Position of a Column

This syntax applies to a PDF or PS report.

TYPE=REPORT, COLUMN=identifier, POSITION={+|-}position, $

where:

identifier

Selects a single column and collectively positions the column title, data, and totals if
applicable. For valid values, see Identifying a Report Component in a WebFOCUS StyleSheet
on page 1249.

+

Starts the column at the specified distance to the right of the default starting position.

By default, text items and alphanumeric fields are left-justified in a column, and numeric
fields are right-justified in a column.

Creating Reports With TIBCO® WebFOCUS Language

 1341

Positioning a Report Component

-

Starts the column at the specified distance to the left of the default starting position.

It is possible to create a report in which columns overlap. If this occurs, simply adjust the
values.

position

Is the desired distance, in the unit of measurement specified with the UNITS attribute.

Example:

Specifying an Absolute Starting Position for a Column

The following illustrates how to position a column in a printed report. It is specified in the
request that the PRODUCT_DESCRIPTION field display three inches from the left margin of the
PDF report.

SET ONLINE-FMT = PDF
TABLE FILE GGORDER
"PRODUCTS ORDERED ON 08/01/96"
SUM QUANTITY BY PRODUCT_DESCRIPTION
WHERE ORDER_DATE EQ '080196'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, COLUMN=PRODUCT_DESCRIPTION, POSITION=3, $
ENDSTYLE
END

The output is:

1342

Example:

Specifying a Relative Starting Position for a Column

This request positions the column title and data for the QUANTITY field two inches from the
default position, in this case, two inches from the end of the preceding column.

21. Laying Out the Report Page

SET ONLINE-FMT = PDF
TABLE FILE GGORDER
"PRODUCTS ORDERED ON 08/01/96"
SUM QUANTITY BY PRODUCT_DESCRIPTION
WHERE ORDER_DATE EQ '080196'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, COLUMN=PRODUCT_DESCRIPTION, POSITION=3, $
TYPE=REPORT, COLUMN=QUANTITY, POSITION=+2, $
ENDSTYLE
END

QUANTITY, titled Ordered Units in the report, is relatively positioned to Product:

Syntax:

How to Add Blank Space Around a Report Component

This syntax applies to a PDF or PS report.

TYPE=REPORT, {TOPGAP|BOTTOMGAP}=gap, $
TYPE=type, [COLUMN=identifier,|ACROSSCOLUMN=acrosscolumn,]
 {LEFTGAP|RIGHTGAP}=gap, $

Creating Reports With TIBCO® WebFOCUS Language

 1343

Positioning a Report Component

TYPE=type, [COLUMN=identifier,|ACROSSCOLUMN=acrosscolumn,]
 {LEFTGAP|RIGHTGAP}=gap, $

where:

TOPGAP

Indicates how much space to add above the report line.

BOTTOMGAP

Indicates how much space to add below the report line.

gap

Is the amount of blank space, in the unit of measurement specified with the UNITS
attribute.

In the absence of grids or background color, the default value is 0. For RIGHTGAP, the
default value is proportional to the size of the text font.

In the presence of grids or background color, the default value increases to provide space
between the grid and the text or to extend the color beyond the text.

The gaps must be the same within a single column or row. That is, you cannot specify
different left or right gaps for individual cells in the same column, or different top and
bottom gaps for individual cells in the same row.

type

Identifies the report component. For valid values, see Identifying a Report Component in a
WebFOCUS StyleSheet on page 1249.

identifier

Selects one or more columns using the COLUMN attribute described in Identifying a Report
Component in a WebFOCUS StyleSheet on page 1249.

acrosscolumn

Selects the same column under every occurrence of an ACROSS sort field using the
ACROSSCOLUMN attribute described in Identifying a Report Component in a WebFOCUS
StyleSheet on page 1249.

LEFTGAP

Indicates how much space to add to the left of a report column.

RIGHTGAP

Indicates how much space to add to the right of a report column.

1344

21. Laying Out the Report Page

Note: For TOPGAP, BOTTOMGAP, LEFTGAP, and RIGHT GAP, you must specify a value of at
least 0.013889 (the decimal size of a point in inches). If you specify a value less than this,
WebFOCUS will round down to the nearest point, which is zero.

Example:

Adding Blank Space Above Data Values

This request generates one-tenth of an inch of blank space above every data value in a PDF
report.

SET ONLINE-FMT = PDF
SET PAGE-NUM = OFF
TABLE FILE GGORDER
"PRODUCTS ORDERED ON 08/01/96"
" "
SUM QUANTITY BY PRODUCT_DESCRIPTION
WHERE ORDER_DATE EQ '080196'
ON TABLE SET STYLE *
TYPE=DATA, TOPGAP = 0.1, $
ENDSTYLE
END

The data is spaced for readability:

Creating Reports With TIBCO® WebFOCUS Language

 1345

Arranging Columns on a Page

Example:

Adding Blank Space to the Left of a Column

The following illustrates how to add blank space to the left of a report component. In this
example, 1.5 inches of blank space are inserted to the left of the Product Category column.

SET ONLINE-FMT=PDF
TABLE FILE CENTORD
HEADING CENTER
"Summary Report for Digital Products"
" "
SUM    LINE_COGS/D12       AS 'Cost of Goods Sold'
BY     PRODTYPE            AS 'Product Type'
BY     PRODCAT             AS 'Product Category'
WHERE PRODTYPE EQ 'Digital';
ON TABLE COLUMN-TOTAL/D12
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, COLUMN=PRODCAT, LEFTGAP=1.5, $
ENDSTYLE
END

The output is:

Arranging Columns on a Page

How easily a user locates data depends on the arrangement of columns on a page. You have
many design options. Using StyleSheet attributes or commands you can:

Determine column width.

Control the number of spaces between columns.

Change the order of vertical sort (BY) columns.

Stack columns to reduce report width, or to easily compare values in a report by creating a
matrix.

Specify the absolute or relative starting position for a column.

1346

Reference: Column Arrangement Features

21. Laying Out the Report Page

Feature

SQUEEZE

Description

Applies to

Sets column width.

SET SPACES

Sets number of spaces
between columns.

SEQUENCE

Sets column order.

HTML

PDF

PS

HTML

PDF

PS

HTML

EXL2K (Note: Does not work
with XLSX and EXL2K
FORMULA)

FOLD-LINE

OVER

Reduces report width by
stacking columns.

Stacks columns by placing
them over one another.

IN {n|+n}

Sets absolute or relative
starting position of a column.

PDF

PS

HTML

PDF

PS

HTML

PDF

PS

Determining Column Width

The value of the SQUEEZE attribute in a StyleSheet determines column width in a report. You
can use a SET parameter instead of a StyleSheet to set the value of SQUEEZE. If there are
conflicting StyleSheet and SET values, the StyleSheet overrides the SET. For details on SET,
see the Developing Reporting Applications manual.

Creating Reports With TIBCO® WebFOCUS Language

 1347

Arranging Columns on a Page

When SQUEEZE is set to ON (the default), StyleSheet column width is ignored. Column width is
determined using your browser's default settings.

When using SQUEEZE it may affect the way headings, footings, and column titles display in
your report. For details, see Using Headings, Footings, Titles, and Labels on page 1517.

Syntax:

How to Determine Column Width (HTML)

This syntax applies to an HTML report. For the syntax for a PDF or PS report, see How to
Determine Column Width (PDF or PS) on page 1350.

The sizing of tables and column width within a standard HTML report is done by browser
processing, including the browser default settings and the size of the browser window or
iframe. The columns are sized to fit the largest data value or column title, whichever is greater,
and trailing spaces are automatically removed.

In standard HTML reports, the data is presented in a single table, so the column widths are
fixed for all data rows.

In HFREEZE HTML reports, the data is presented with no wrapping in three tables containing
the heading, data rows, and footing, to ensure the alignment of the column titles with the data
rows.

[TYPE=REPORT,] SQUEEZE={ON|OFF}, $

where:

TYPE=REPORT

Applies the column width to the entire report. Not required, as it is the default.

Determines column width based on the longest data value or column title, whichever is
greater. ON is the default value.

For HTML reports, the web browser shrinks the column width to the shortest column title or
field value.

ON

OFF

Determines column width based on the longest data value or column title, whichever is
greater. Blank spaces pad the column width up to the length of the column title or field
format, whichever is greater.

Note:

In an HTML report that sets SQUEEZE and uses conditional styling for some columns, use
TYPE=DATA, COLUMN=n, not TYPE=REPORT, COLUMN=n.

1348

21. Laying Out the Report Page

SQUEEZE is not supported for columns created with the OVER phrase.

Example:

Using Default Column Width (HTML)

This request uses SQUEEZE=ON (the default) for an HTML report. Column width is based on
the wider of the data value or column title.

SET PAGE-NUM = OFF
TABLE FILE GGSALES
SUM UNITS DOLLARS
BY CATEGORY BY PRODUCT
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, FONT=COURIER, $
ENDSTYLE
END

For Category, Unit Sales, and Dollar Sales, the column title is wider than the corresponding
data values. For Product, the wider data values determine column width. The HTML report is:

Example:

Using Column Width Based on Field Format (HTML)

This request sets SQUEEZE to OFF for an HTML report. Column width is based on the longest
data value or column title, whichever is greater.

SET PAGE-NUM = OFF
TABLE FILE GGSALES
SUM UNITS DOLLARS
BY CATEGORY BY PRODUCT
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, SQUEEZE=OFF, FONT=COURIER, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1349

Arranging Columns on a Page

Blank spaces pad the column width up to the length of the field format for Category (A11) and
Product (A16). The HTML report is:

Syntax:

How to Determine Column Width (PDF or PS)

This syntax applies to a PDF or PS report. For the syntax for an HTML report, see How to
Determine Column Width (HTML) on page 1348.

[TYPE=REPORT,] COLUMN=identifier, SQUEEZE={ON|OFF|width}, $

where:

TYPE=REPORT

Applies the column width to the entire report. Not required, as it is the default.

identifier

Selects a column using the COLUMN attribute described in Identifying a Report Component
in a WebFOCUS StyleSheet on page 1249. If you omit a column identifier, the value for
SQUEEZE applies to all columns in a report. You can also use SET SQUEEZE to set the
width of all columns.

ON

Determines column width based on the widest data value or column title, whichever is
greater.

1350

21. Laying Out the Report Page

OFF

Determines column width based on the longest data value or column title, whichever is
greater. Blank spaces pad the column width up to the length of the column title or field
format, whichever is greater. OFF is the default value.

width

Is a measurement for the column width, specified with the UNITS attribute.

If the widest data value exceeds the specified measurement:

And the field is...

The following displays...

Alphanumeric

As much of the value as will fit in the specified width, followed
by an exclamation mark (!) to indicate truncation.

Numeric

Asterisks (*) in place of the field value.

Note: SQUEEZE is not supported for columns created with the OVER phrase.

Creating Reports With TIBCO® WebFOCUS Language

 1351

Arranging Columns on a Page

Example:

Determining Column Width (PDF)

This request uses SQUEEZE=2.5 to increase the default column width of the PRODUCT field in
a PDF report. Note that this feature is used primarily for printed reports. Depending on your
screen resolution, the column width may look different than how it will print.

SET ONLINE-FMT = PDF
TABLE FILE GGSALES
SUM UNITS
BY PRODUCT
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, COLUMN=PRODUCT, SQUEEZE=2.5, $
ENDSTYLE
END

The PDF report is:

Controlling Column Spacing

By default, report columns are separated by one or two spaces, depending on the output
width. The SET SPACES or ON TABLE SET SPACES parameter controls the number of spaces
between columns in a report.

In a horizontal sort (ACROSS) phrase, the SPACES parameter determines the distance between
horizontal sort sets. Within a set, the distance between columns is always one space and
cannot be changed.

This feature applies to an HTML report. It requires you to set the STYLEMODE parameter to
FIXED.

1352

21. Laying Out the Report Page

Syntax:

How to Control Column Spacing

This syntax applies to an HTML report.

For all report requests in a procedure

SET SPACES = {n|AUTO}

For one report request

ON TABLE SET SPACES {n|AUTO}

where:

n

Is an integer between 1 and 8, indicating the number of spaces between report columns.

AUTO

Automatically separates report columns with one or two spaces. AUTO is the default value.

Example:

Controlling Column Spacing Between Horizontal (ACROSS) Fields

This request uses ACROSS with ON TABLE SET SPACES. The ON TABLE SET STYLEMODE
FIXED parameter is required for HTML.

TABLE FILE CENTORD
SUM QUANTITY LINEPRICE ACROSS ORDER_NUM BY PLANT AS 'Plant'
WHERE ORDER_NUM EQ '28003' OR '28004'
ON TABLE SET SPACES 7
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLEMODE FIXED
END

The ACROSS set consists of the fields titled Quantity and Line Total. The distance between
each set is seven spaces:

Changing Column Order

You can change the order in which vertical sort (BY) columns are displayed in a report. This
feature does not apply to horizontal sort (ACROSS) rows or stacked (OVER) columns.

Creating Reports With TIBCO® WebFOCUS Language

 1353

Arranging Columns on a Page

Syntax:

How to Change Column Order

This syntax applies to PDF, PS, HTML, XLSX, and EXL2K reports. XLSX FORMULA and EXL2K
FORMULA formats are not supported.

[TYPE=REPORT,] COLUMN=identifier, SEQUENCE=sequence, $

where:

TYPE=REPORT

Applies the column order to the entire report. Not required, as it is the default.

identifier

Selects a column using the COLUMN attribute described in Identifying a Report Component
in a WebFOCUS StyleSheet on page 1249.

sequence

Is a number that represents the order of the selected column.

Numbers need not be in sequential order or in increments of one. The order of the
columns is from lowest to highest. NOPRINT columns are not included.

Example:

Changing Column Order

This request rearranges the order in which columns normally appear in the report, that is, with
SNAME first, PRODCAT second, and LINEPRICE third.

SET ONLINE-FMT = PDF
TABLE FILE CENTORD
SUM LINEPRICE AS 'Sales'
BY SNAME BY PRODCAT AS 'Product'
WHERE SNAME EQ 'eMart' OR 'City Video'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, COLUMN=SNAME, SEQUENCE=3, $
TYPE=REPORT, COLUMN=PRODCAT, SEQUENCE=2, $
TYPE=REPORT, COLUMN=LINEPRICE, SEQUENCE=1, $
ENDSTYLE
END

1354

LINEPRICE (Sales) is now the first column, PRODCAT (Product) is the second column (as it was
by default), and SNAME (Store Name) is the third column. The PDF report is:

21. Laying Out the Report Page

Stacking Columns

You can stack columns in a report to reduce report width, or to easily compare values in a
report by creating a matrix. To stack columns, you can use:

FOLD-LINE:

Reduces the use of space for a vertical sort (BY) column that changes infrequently. You
can include up to 16 FOLD-LINE phrases in a request.

Is available for PDF, PS, and DHTML reports, but not cell-based formats, such as HTML,
XLSX, and EXL2K.

Cell based styling features including BACKCOLOR and BORDERS are not supported.

Alternating back colors are not supported for stacked columns.

OVER:

Stacks columns one over another, which increases readability, especially when you are
sorting your report horizontally with ACROSS. OVER is useful when you are creating
financial reports. For complete details, see Creating Financial Reports With Financial
Modeling Language (FML) on page 1817.

Alternating back colors are not supported for stacked columns.

Creating Reports With TIBCO® WebFOCUS Language

 1355

Arranging Columns on a Page

The difference between FOLD-LINE and OVER is that FOLD-LINE begins the second line (not the
second column) just underneath the first line, but slightly indented. OVER literally stacks the
values of one column directly over another. You can use FOLD-LINE and OVER in the same
request.

Syntax:

How to Stack Columns With FOLD-LINE

display_command fieldname ... FOLD-LINE fieldname ...

or

{ON|BY} fieldname FOLD-LINE

where:

display_command

Is a display command. There is no offset when a line is folded after a display field.

fieldname

Is a display field or sort field placed on a separate line when the value of the ON or BY
field changes. When folded on a sort field, a line is offset by two spaces from the
preceding line.

ON|BY

Is a vertical sort phrase. The terms are synonymous.

Example:

Stacking Columns With FOLD-LINE

The following illustrates how to use FOLD-LINE to decrease the width of your report. In this
example, columns are stacked when the value of the sort field CATEGORY changes.

TABLE FILE GGSALES
SUM UNITS BUDUNITS
BY CATEGORY
ON CATEGORY FOLD-LINE
ON TABLE SET ONLINE-FMT PDF
ON TABLE SET PAGE-NUM OFF
END

1356

The report is:

21. Laying Out the Report Page

Without FOLD-LINE, the report looks like this:

Syntax:

How to Stack Columns With OVER

display_command fieldname1 OVER fieldname2 OVER fieldname3 ...

where:

display_command

Is a display command.

fieldname1, fieldname2, fieldname3

Is a display field or calculated value. A text field is not valid.

Example:

Stacking Columns With OVER

This request contains an ACROSS phrase in an HTML report to sort horizontally by department.
It uses two OVER phrases to stack columns.

TABLE FILE EMPLOYEE
SUM GROSS OVER DED_AMT OVER
COMPUTE NET/D8.2M = GROSS - DED_AMT;
ACROSS DEPARTMENT
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1357

Arranging Columns on a Page

With the use of OVER, the columns GROSS, DED_AMT, and NET are stacked for readability:

Without the use of OVER, the HTML report looks like this:

Alignment of Fields in Reports Using OVER in PDF Report Output

When columns are placed on report output, they are separated by gaps. You can control the
size of the gaps between columns with the LEFTGAP and RIGHTGAP StyleSheet attributes.

1358

21. Laying Out the Report Page

By default, the gaps between columns are placed outside of the boundaries reserved for the
fields on the report output. Therefore, the width or squeeze value defined for a field defines
the size of the text area for the data value. It does not count the width of the gaps between
columns. The bounding box used to define borders and background color is determined based
on the data width plus the left gap plus the right gap.

Gaps external to the column boundaries must be accounted for when you try to align fields in
reports that use the OVER phrase.

This feature is designed to support the development of multi-row reports using blank AS names
(column titles). Unless otherwise noted, these features work with non-blank titles, but they
have not been designed to support alignment with non-blank column titles.

By default, column titles are placed to the left of the field values in a report using OVER. The
OVER Title and the OVER Value each are measured by the combination of three parameters,
LEFTGAP, WIDTH, and RIGHTGAP:

Creating Reports With TIBCO® WebFOCUS Language

 1359

Arranging Columns on a Page

With OVER and blank AS names, each data value becomes a data cell that can be used to
construct rows and columns within the data lines of the report. In order to align data values on
a lower line with the columns above them, you must calculate widths for the lower level
columns that take into account the widths of the data above them plus the widths of all of the
left gaps and right gaps in between.

It can be complex to calculate how to size each column when aligning data and headings in
reports using OVER. Each calculation of the column size must additionally account for the
external left and right gap, and these gaps are cumulative as the number of columns on a
given row increases.

Using the GAPINTERNAL=ON StyleSheet attribute, you can have the gaps placed within the
column boundaries for PDF report output. This feature makes it much easier to align fields and
headings in reports that use the OVER phrase to create multiple lines.

Note: OVER is now supported with SQUEEZE.

Syntax:

How to Control GAP Placement on Reports

TYPE=REPORT, GAPINTERNAL={OFF|ON}

where:

OFF

Places the left and right gaps outside the defined field width. OFF is the default value.

ON

Places the left and right gaps internal to the defined field width.

1360

Example:

Comparing External Gaps With Internal Gaps

With GAPINTERNAL=OFF, you must account for the accumulation of left and right gaps as well
as the field widths when defining widths of stacked columns.

21. Laying Out the Report Page

Creating Reports With TIBCO® WebFOCUS Language

 1361

Arranging Columns on a Page

With GAPINTERNAL=ON, the defined WIDTH represents the entire space used by the given data
cell or column. This takes the cumulative effect out as the OVER values proceed across a row.

1362

Example:

Using GAPINTERNAL in a Report

21. Laying Out the Report Page

The following request against the GGSALES data source places the PRODUCT field over the
UNITS and DOLLARS fields and sets GAPINTERNAL to OFF:

SET LAYOUTGRID=ON
TABLE FILE GGSALES
"Product<+0>"
"Units<+0>Dollars"
SUM
PRODUCT AS ''
OVER
UNITS/D8C AS '' DOLLARS/D12.2CM AS ''
BY PRODUCT NOPRINT
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, SQUEEZE=ON, FONT=ARIAL, SIZE=8, LEFTMARGIN=1, TOPMARGIN=1,
 LEFTGAP=.1, RIGHTGAP=.1, GAPINTERNAL=OFF, $
TYPE=REPORT, BORDER=ON, $
TYPE=HEADING, BORDERALL=ON, $
TYPE=HEADING, LINE=1, ITEM=1, POSITION = PRODUCT, $
TYPE=HEADING, LINE=2, ITEM=1, POSITION = UNITS, $
TYPE=HEADING, LINE=2, ITEM=2, POSITION = DOLLARS, $
TYPE=REPORT, COLUMN=PRODUCT(2),   SQUEEZE=2,  $
TYPE=REPORT, COLUMN=UNITS, SQUEEZE=1, $
TYPE=REPORT, COLUMN=DOLLARS, SQUEEZE=1, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1363

Arranging Columns on a Page

The widths specified for UNITS and DOLLARS are one inch each, while the PRODUCT field is
specified to be two inches. With GAPINTERNAL=OFF, the LAYOUTGRID shows that the widths
used to place the columns are greater than the widths specified in the request. The additional
space presented by the external leftgap and rightgap accounts for this effect:

1364

21. Laying Out the Report Page

The heading borders are aligned on the right of the report because of the SQUEEZE=ON
attribute in the StyleSheet. Extra space was added to the report to align the headings. If you
change the StyleSheet declaration for the PRODUCTS field to JUSTIFY=RIGHT, you can see that
the extra space prevents the product value from aligning with the dollar value:

Creating Reports With TIBCO® WebFOCUS Language

 1365

Arranging Columns on a Page

Changing the StyleSheet declaration to GAPINTERNAL=ON causes the specified widths to be
used because the gaps are internal and are included in the specified values:

1366

The following report output demonstrates that the values align properly even if the PRODUCT
values are defined with JUSTIFY=RIGHT:

21. Laying Out the Report Page

Positioning a Column

You can specify the absolute or relative starting position for a column in a report. The relative
starting position is the number of characters to the right of the last column.

When using this feature with an HTML report, set the STYLEMODE parameter to FIXED.

Creating Reports With TIBCO® WebFOCUS Language

 1367

Arranging Columns on a Page

Syntax:

How to Position a Column

field IN {n|+n}

where:

field

Is the column that is positioned.

n

+n

Is a number indicating the absolute position of the column.

When used with ACROSS, n specifies the starting position of the ACROSS set.

When used with FOLD-LINE or OVER, n applies to the line on which the referenced field
occurs.

Is a number indicating the relative position of the column. The value of n is the number of
characters to the right of the last column.

Example:

Positioning Columns

This request specifies absolute positioning for the three columns in the report. The ON TABLE
SET STYLEMODE FIXED parameter is required for HTML.

TABLE FILE CENTQA
SUM CNT.PROBNUM IN 1 AS 'Total #,Problems'
SUM CNT.PROBNUM IN 45 AS '# Problems,by Product'
BY PLANT NOPRINT BY PRODNAME IN 15
WHERE PLANT EQ 'ORL'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLEMODE FIXED
END

1368

The columns are spaced for readability:

21. Laying Out the Report Page

Example:

Positioning Horizontal Sort (ACROSS) Columns

This request uses the IN phrase with the horizontal sort field PLANT to specify the column
starting position. It also uses relative positioning to add extra spaces between the PROBNUM
columns. The ON TABLE SET STYLEMODE FIXED parameter is required for HTML reports.

TABLE FILE CENTQA
SUM PROBNUM IN +8
ACROSS PLANT IN 35
BY PROBLEM_CATEGORY
WHERE PLANT EQ 'BOS' OR 'ORL'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLEMODE FIXED
END

Creating Reports With TIBCO® WebFOCUS Language

 1369

Arranging Columns on a Page

The ACROSS set starts in column 35, and there are eight extra spaces between the data
columns in the ACROSS:

Example:

Positioning Stacked (OVER) Columns

The following request uses OVER to stack columns and IN to position them.

TABLE FILE EMPLOYEE
SUM GROSS IN 40
OVER DED_AMT IN 40
BY DEPARTMENT BY LAST_NAME IN 20
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLEMODE FIXED
END

1370

In the report, GROSS and DED_AMT are stacked, starting in column 40. LAST_NAME starts in
column 20.

21. Laying Out the Report Page

Suppressing Column Display

A report request may include a field to create a certain result. For example, it may name a sort
field by which to arrange data. However, you may not want to display the title or values of that
field if they appear elsewhere in the report. The phrase NOPRINT (synonym SUP-PRINT)
suppresses column display.

Creating Reports With TIBCO® WebFOCUS Language

 1371

Suppressing Column Display

Reference: Column Suppression Commands

Command

NOPRINT or
SUP-PRINT

Description

Applies to

Suppresses column display.  HTML

PDF

PS

Syntax:

How to Suppress Column Display

display_command fieldname {NOPRINT|SUP-PRINT}

or

{ON|BY} fieldname {NOPRINT|SUP-PRINT}

where:

display_command

Is a display command.

fieldname

Is a display field or sort field. The field values are used but not displayed. A HOLD file will
not contain the values of a suppressed BY field.

For a calculated value with NOPRINT, repeat AND COMPUTE before the next calculated
value if applicable.

NOPRINT|SUP-PRINT

Suppresses column display. The terms are synonymous.

ON|BY

Is a vertical sort phrase. The terms are synonymous.

Example:

Suppressing the Display of a Sort Field

This request sorts data by city. Since the page heading contains the name of the city, the sort
field occurrence is suppressed.

1372

21. Laying Out the Report Page

TABLE FILE SALES
HEADING
"Page <TABPAGENO"
"SALES REPORT FOR <CITY"
PRINT UNIT_SOLD AND DELIVER_AMT
BY CITY PAGE-BREAK NOPRINT
BY PROD_CODE
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The page heading identifies the city to which the data applies:

Creating Reports With TIBCO® WebFOCUS Language

 1373

Suppressing Column Display

Without NOPRINT, the report would unnecessarily repeat the city:

1374

Example:

Suppressing Display of a Sort Field With Subtotal

This request generates a subtotal for each value of the sort field CATEGORY but suppresses
the display of the sort field occurrence.

21. Laying Out the Report Page

TABLE FILE GGSALES
SUM UNITS BY CATEGORY
BY PRODUCT
ON CATEGORY SUB-TOTAL SUP-PRINT PAGE-BREAK
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The default subtotal line identifies each category (for example, *TOTAL Coffee):

Creating Reports With TIBCO® WebFOCUS Language

 1375

Suppressing Column Display

Without SUP-PRINT, the report would unnecessarily repeat the category:

1376

Example:

Sorting Alphabetically

This request sorts last names alphabetically but avoids duplication of data by suppressing the
sort field occurrence of LAST_NAME.

21. Laying Out the Report Page

TABLE FILE EMPLOYEE
PRINT LAST_NAME
BY LAST_NAME NOPRINT
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

Last names are arranged alphabetically:

Inserting a Page Break

Use the PAGE-BREAK command to generate a new page each time the value of a specified
vertical sort (BY) field changes. This helps to prevent related information from being presented
over multiple pages. When you use a page break, column titles and any page headings appear
at the top of each new page. When the request has a PAGE-BREAK, the GRANDTOTAL is on a
page by itself.

PAGE-BREAK does not apply when report output is stored in a HOLD, SAVE, or SAVB file.

Creating Reports With TIBCO® WebFOCUS Language

 1377

Inserting a Page Break

In an HTML report, PAGE-BREAK creates a new section of the report, with column titles and an
incremented page number, on the same webpage. It does not, by itself, create a new
webpage. To create multiple webpages in an HTML report:

Burst the report, with each page corresponding to a different sort field value. For details,
see Bursting Reports Into Multiple HTML Files on page 1029.

Use SET STYLEMODE=PAGED in conjunction with PAGE-BREAK. This is useful when you are
distributing a report via ReportCaster.

Use SET WEBVIEWER=ON, which accesses the WebFOCUS Viewer, in conjunction with
PAGE-BREAK. For details, see the Developing Reporting Applications manual.

Reference: Page Break Commands

Command

Description

PAGE-BREAK

Generates new page.

NOSPLIT

Prevents undesirable page break.

SET LINES

Synchronizes report page with browser
page.

Reference: Working With Multi-Table HTML Reports

Applies to

HTML

PDF

PS

PDF

PS

HTML

You can control where a report breaks using SET LINES or PAGE-BREAK in the request.

ON sortfield PAGE-BREAK or BY sortfield PAGE-BREAK overrides a SET LINES command and
breaks a report into multiple HTML tables whenever the sort field value changes.

Column titles are generated for every PAGE-BREAK or according to the SET LINES
parameter.

When a report is broken into multiple HTML tables, the browser displays each table
according to its own algorithm. Set SQUEEZE to OFF and/or WRAP to OFF to ensure that
HTML tables are aligned consistently across pages.

1378

21. Laying Out the Report Page

Syntax:

How to Insert a Page Break

{ON|BY} fieldname PAGE-BREAK [REPAGE] [WHEN expression;]

where:

ON|BY

Is a vertical sort phrase. The terms are synonymous.

fieldname

Is the sort field on which the page break occurs. Specify the lowest level sort field at which
the page break occurs. A page break occurs automatically whenever a higher level sort
field changes.

REPAGE

Resets the page number to 1 at each page break or, if combined with WHEN, whenever the
WHEN criteria are met.

WHEN expression

Specifies a conditional page break in the printing of a report as determined by a logical
expression. See Controlling Report Formatting on page 1219 for details.

Example:

Inserting a Page Break

This request generates a new page whenever the value of the sort field SALARY changes.

TABLE FILE EMPLOYEE
PRINT EMP_ID
BY SALARY IN-GROUPS-OF 5000
BY PCT_INC BY DAT_INC
ON SALARY PAGE-BREAK
ON TABLE SET ONLINE-FMT PDF
ON TABLE SET PAGE-NUM OFF
END

Creating Reports With TIBCO® WebFOCUS Language

 1379

Inserting a Page Break

The first two pages of the report are displayed to illustrate where the page breaks occur:

The second page is:

1380

Example:

Displaying a Multiple-Table HTML Report

In this request, each page is returned to the browser as a separate HTML table. SQUEEZE is
set to OFF for consistent alignment of tables across pages.

21. Laying Out the Report Page

SET STYLEMODE = PAGED
SET LINES = 12
TABLE FILE CENTORD
HEADING
"SALES OVER $200,000"
PRINT LINEPRICE AS 'Sales'
BY SNAME BY ORDER_NUM
WHERE LINEPRICE GT 200000
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, SQUEEZE=OFF, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1381

Inserting a Page Break

Two pages of the report follow, showing consistent alignment:

1382

The same two pages illustrate inconsistent alignment with SQUEEZE set to ON:

21. Laying Out the Report Page

Preventing an Undesirable Split

A page break may occur in the middle of information logically grouped by a sort field, causing
one or more group-related lines to appear by themselves on the next page or in the next
window. Use the NOSPLIT option to avoid this kind of break. When the value of the sort field
changes, the total number of lines related to the new value appear on a new page, including
sort headings, sort footings, and subtotals if applicable.

This feature applies to a PDF or PS report.

Creating Reports With TIBCO® WebFOCUS Language

 1383

Inserting a Page Break

If you use NOSPLIT with PAGE-BREAK, the PAGE-BREAK must apply to a higher-level sort field.
Otherwise, NOSPLIT is ignored. NOSPLIT is also ignored when report output is stored in a
HOLD, SAVE, or SAVB file. NOSPLIT is not compatible with the TABLEF command and
generates an error message.

Syntax:

How to Prevent an Undesirable Split

This syntax applies to a PDF or PS report. Use only one NOSPLIT per report request.

{ON|BY} fieldname NOSPLIT

where:

ON|BY

Is a vertical sort phrase. The terms are synonymous.

fieldname

Is the name of the sort field for which sort groups are kept together on the same page.

Example:

Preventing an Undesirable Split

This request uses NOSPLIT to keep related information on the same page:

SET ONLINE-FMT = PDF
TABLE FILE EMPLOYEE
PRINT DED_CODE AND DED_AMT
BY PAY_DATE BY LAST_NAME
ON LAST_NAME NOSPLIT
END

1384

When the value of LAST_NAME changes from STEVENS to CROSS, the lines related to CROSS
do not fit on the current page. With NOSPLIT, they appear on the next page:

21. Laying Out the Report Page

Creating Reports With TIBCO® WebFOCUS Language

 1385

Inserting a Page Break

1386

Without NOSPLIT, the information for CROSS falls on the first and second pages:

21. Laying Out the Report Page

Creating Reports With TIBCO® WebFOCUS Language

 1387

Inserting Page Numbers

Inserting Page Numbers

By default, the first two lines of a report page are reserved. The first line contains the page
number in the top-left corner, and the second line is blank.

Note: The features in this section are not supported for Compound Reports.

You can:

Change the position of the default page number with the system variable TABPAGENO,
which contains the current page number.

Insert the total page count using the TABLASTPAGE system variable.

Assign any number to the first page using the FOCFIRSTPAGE parameter.

Suppress the display of the default page number.

Note: The variables TABPAGENO and TABLASTPAGE cannot be used to define styling with
conditional styling (WHEN).

1388

21. Laying Out the Report Page

If you enable Section 508 accessibility, a default page number is not included in the HTML
table.

Reference: Page Number Commands

Command

Description

Applies to

<BYLASTPAGE

Used with REPAGE. Inserts the total page count
within the sort group that has the REPAGE
option.

REPAGE

Resets page number to one.

<TABPAGENO

Inserts the current page number. TABPAGENO
suppresses the default page number, and the
top two lines of a page are blank.

<TABLASTPAGE

Inserts the total page count in the report.

SET FOCFIRSTPAGE

Assigns the designated page number to the first
page.

HTML

PDF

PS

PPTX

HTML

PDF

PS

PPTX

HTML

PDF

PS

PPTX

HTML

PDF

PS

PPTX

HTML

PDF

PS

PPTX

Creating Reports With TIBCO® WebFOCUS Language

 1389

Inserting Page Numbers

Command

Description

SET PAGE-NUM

Controls page number display.

Applies to

HTML

PDF

PS

Syntax:

How to Insert the Current Page Number

To add the current page number, add the following to your request.

<TABPAGENO

Example:

Inserting the Current Page Number in a Sort Footing

This request generates a new page whenever the value of the sort field REGION changes. It
uses TABPAGENO to insert a page number in the sort footing.

TABLE FILE GGSALES
SUM BUDDOLLARS
BY REGION BY ST BY CITY
ON REGION PAGE-BREAK SUBFOOT
"Sales Quota for <REGION Cities"
"Page <TABPAGENO"
ON TABLE SET ONLINE-FMT PDF
END

The first page of output is:

Inserting the Total Page Count

You can use the <TABLASTPAGE system variable to insert the total page count into your report.
For example, if you wanted to add a footing in your report that said "Page 1 of 5", you could
use the <TABLASTPAGE system variable in conjunction with the <TABPAGENO system variable
to do so.

1390

21. Laying Out the Report Page

Syntax:

How to Insert the Total Page Count

To insert the total number of pages, add the following to your request:

<TABLASTPAGE

Reference: Usage Notes for TABLASTPAGE

TABLASTPAGE does not adjust for changes in FOCFIRSTPAGE or for the REPAGE command.
For example, if the report has 10 pages and the user uses FOCFIRSTPAGE to set the first
page number to 3 rather than 1, the value of TABLASTPAGE will still be 10.

TABLASTPAGE is supported only for a single report, not compound reports. A separate page
count is generated for each report in a compound report.

TABLASTPAGE is supported only for styled reports such as HTML, PDF, and PS. it is not
supported for EXL2K, WP, DOC, or HTML with STYLE=OFF and STYLEMODE=FIXED.

TABLASTPAGE causes a second pass through the report results, first to calculate the last
page then to print it with TABPAGENO (even when SQUEEZE=OFF).

TABLASTPAGE does not support the system (external) sort.

GRAPH FILE does not support TABLASTPAGE.

TABLEF is not supported with TABLASTPAGE.

Example:

Inserting the Current Page Number and the Total Page Count

The following illustrates how to add the current page number and the total page count to a
report. The relevant syntax is highlighted in the request.

TABLE FILE EMPLOYEE
PRINT EMP_ID AS 'Employee ID'
BY SALARY IN-GROUPS-OF 5000 AS 'Salary'
BY PCT_INC AS 'Percent,Increase'
BY DAT_INC AS 'Date of,Increase'
ON SALARY PAGE-BREAK
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=TITLE, STYLE=BOLD, SIZE=11, $
ENDSTYLE
FOOTING
"Page <TABPAGENO of <TABLASTPAGE"
END

Creating Reports With TIBCO® WebFOCUS Language

 1391

Inserting Page Numbers

The first two pages of output are:

Displaying the Total Page Count Within a Sort Group

The <BYLASTPAGE variable used in a heading or footing displays the number of pages of
output within each sort group when a report uses the REPAGE option to reset the page
numbers for each sort group. This variable can only be used with styled output formats.

If the REPAGE option is not used in the report, the total number of pages in the report
(<TABLASTPAGE variable) is used for <BYLASTPAGE.

Syntax:

How to Display the Total Number of Pages Within Each Sort Group

The request must have the following syntax and hold the output in a styled output format:

BY sortfield REPAGE

The heading or footing can use the following syntax to display “Page x of y”

1392

21. Laying Out the Report Page

{HEADING|FOOTING}
"Page <TABPAGENO of <BYLASTPAGE"

where:

sortfield

Is the sort field that has the REPAGE option. A PAGE-BREAK is required on the same sort
field or a lower level sort field. PAGE-BREAK starts a new page for each sort break.
REPAGE resets the page number to 1 for each sort break.

<TABPAGENO

Is the current page number.

<BYLASTPAGE

Is the last page number before the repage.

Example:

Paginating Within a Sort Group

The following request against the GGSALES data source sorts by product, region, category, and
city. It resets the pagination each time the product changes. The heading prints the current
page number and the total within each product group.

Note that by default, the TABPAGENO and BYLASTPAGE variables have format I5, which leaves
a lot of blank space before the page numbers. Therefore, you can use spot markers or
COMPUTE commands to move the page numbers to the left.

In the following example, a COMPUTE command creates a field named X that has the value of
TABPAGENO but stores it as an I2 field, and the spot marker in the heading moves the
BYLASTPAGE page number four spaces to the left. The heading command must come after the
COMPUTE command or the field named X will not be recognized:

TABLE FILE GGSALES
SUM UNITS
COMPUTE X/I2 = TABPAGENO;
BY PRODUCT NOPRINT REPAGE
BY REGION PAGE-BREAK
BY CATEGORY
BY CITY
HEADING CENTER
"<PRODUCT : Page <X of <-4> <BYLASTPAGE "
ON TABLE PCHOLD FORMAT PDF
END

Creating Reports With TIBCO® WebFOCUS Language

 1393

Inserting Page Numbers

The following partial output shows that the page number resets to 1 when the product changes
and that the BYLASTPAGE variable displays the total number of pages for each product:

1394

21. Laying Out the Report Page

Assigning Any Page Number to the First Page

You can assign a page number to the first page of a report using the FOCFIRSTPAGE
parameter. This feature is useful when a report is printed and assembled as part of another
one.

You can also control the page numbering of multiple reports in the same procedure using the
FOCFIRSTPAGE parameter with the &FOCNEXTPAGE variable.

If TABPAGENO is used, FOCFIRSTPAGE is ignored.

Syntax:

How to Assign a Page Number to the First Page

For all report requests in a procedure

SET FOCFIRSTPAGE = {n|1|&FOCNEXTPAGE}

For one report request

ON TABLE SET FOCFIRSTPAGE {n|1|&FOCNEXTPAGE}

where:

n

1

Is an integer between 1 and 999999, which is the number assigned to the first page of
the report.

Assigns the number 1 to the first page. 1 is the default value.

&FOCNEXTPAGE

Is a variable whose value is one more than the last page number of the previous report in
a multiple request. The value is calculated at run time.

Example:

Assigning a Page Number to the First Page

This request assigns the number 3 to the first page of the report.

SET FOCFIRSTPAGE = 3
TABLE FILE CENTORD
HEADING
"Sales By Store"
SUM LINEPRICE AS 'Sales'
BY SNAME
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1395

Inserting Page Numbers

The report is:

Example:

Controlling Page Numbers in Consecutive Reports

This procedure contains two report requests. The second request sets FOCFIRSTPAGE to the
value of &FOCNEXTPAGE.

SET FOCFIRSTPAGE = 3
TABLE FILE CENTORD
HEADING
"Sales By Store"
SUM LINEPRICE AS 'Sales'
BY SNAME
WHERE SNAME EQ 'eMart'
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END
-RUN

SET FOCFIRSTPAGE = &FOCNEXTPAGE
TABLE FILE CENTORD
HEADING
"Sales By Product"
SUM LINEPRICE AS 'Sales'
BY PRODCAT AS 'Product'
WHERE PRODCAT EQ 'VCRs'
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

1396

The first page of the second report is numbered 4, which is one more than the last page of the
previous report:

21. Laying Out the Report Page

Controlling the Display of Page Numbers

By default, the first two lines of a report page are reserved. The first line displays the page
number in the top-left corner, and the second line is blank. To suppress the default display,
use the PAGE-NUM parameter.

Syntax:

How to Control the Display of Page Numbers

For all report requests in a procedure

SET PAGE[-NUM] = num_display

For one report request

ON TABLE SET PAGE[-NUM] num_display

where:

-NUM

Is optional. PAGE and PAGE-NUM are synonymous.

num_display

Is one of the following:

ON displays page numbers in the top-left corner, followed by a reserved blank line. ON is
the default value.

OFF suppresses default page numbers.

Creating Reports With TIBCO® WebFOCUS Language

 1397

Inserting Page Numbers

You can use the system variable TABPAGENO.

NOPAGE suppresses default page numbers and makes the top two lines of a page
available for your use.

You can use the system variable TABPAGENO.

TOP or NOLEAD removes the line at the top of each page reserved for the page number,
and the blank line after it. The first line of a report contains the report or page heading if
specified, or column titles if there is no heading.

You can use the system variable TABPAGENO to show page numbers elsewhere in the
report.

Example:

Suppressing Default Page Numbers

This request uses SET PAGE-NUM = NOPAGE to suppress default page numbers. It uses the
top line of the first page of the report for the report heading.

SET PAGE-NUM = NOPAGE
TABLE FILE GGPRODS
ON TABLE SUBHEAD
"PACKAGING INFORMATION"
" "
PRINT PACKAGE_TYPE AND SIZE AND UNIT_PRICE
BY PRODUCT_DESCRIPTION
ON PRODUCT_DESCRIPTION PAGE-BREAK SUBFOOT
"PRODUCT ID <PRODUCT_ID"
"Page <TABPAGENO "
ON TABLE SET ONLINE-FMT PDF
END

1398

TABPAGENO inserts the page number in the sort footing. The first page of the report is:

21. Laying Out the Report Page

Setting the Number of Data Rows For Each Page in an AHTML Report Request

You can use the LINES-PER-PAGE StyleSheet attribute in an AHTML report request to set the
number of data rows to display on each page in the report output.

Syntax:

How to Set the Number of Data Rows For Each Page in an AHTML Report Request

To control the number of data rows to display on each page in the report output, use the
following StyleSheet syntax:

TYPE=REPORT, LINES-PER-PAGE={n|UNLIMITED},$

where:

n

Specifies the number of data rows to display on each page. The default value is 57 rows.

UNLIMITED

Specifies that you want to show all the results on one page.

Note:

In an AHTML report request, using the following SET command, you will see the same
number of data rows as the LINES-PER-PAGE StyleSheet option:

ON TABLE SET LINES {n|UNLIMITED}

Creating Reports With TIBCO® WebFOCUS Language

 1399

Inserting Page Numbers

In an HTML report request, using either the LINES-PER-PAGE StyleSheet option or the SET
LINES command, you will see the number of lines, as opposed to the number of data rows.

Example:

Setting the Number of Data Rows For Each Report Page

The following example uses the default WebFOCUS StyleSheet and displays 20 data rows on
each page of the report output.

TABLE FILE GGSALES
HEADING
"Sales Report"
SUM UNITS DOLLARS
BY CATEGORY BY PRODUCT BY DATE NOPRINT
WHERE DATE GE 19960101 AND DATE LE 19960401
ON TABLE PCHOLD FORMAT AHTML
ON TABLE SET STYLE *
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/ibi_themes/Warm.sty,$
TYPE=REPORT, GRID=OFF, LINES-PER-PAGE = 20, $
ENDSTYLE
END

1400

The following image shows the output for the first page.

21. Laying Out the Report Page

Creating Reports With TIBCO® WebFOCUS Language

 1401

Adding Grids and Borders

The following image shows the output for the second page.

Adding Grids and Borders

By default, an HTML report contains horizontal and vertical grid lines. You can remove the grid
lines or adjust their use on a horizontal (BY) sort field. Grid characteristics apply to an entire
HTML report, not to individual components of a report.

You can emphasize headings, footings, and column titles in a report by adding borders and
grid lines around them.

1402

21. Laying Out the Report Page

Borders: In a PDF, HTML, DHTML, XLSX, EXL2K, PPTX, PPT, or PS report, you can use BORDER
attributes in a StyleSheet to specify the weight, style, and color of border lines. If you wish, you
can specify formatting variations for the top, bottom, left, and right borders.

For an example, see Inserting and Formatting a Border on page 1407.

The BORDERALL StyleSheet attribute supports a heading or footing grid with borders around
each individual heading or footing cell in PDF, DHTML, HTML, XLSX, and PPTX report output.
Using this attribute along with BORDER attributes for individual objects in a heading or footing
enables you to create borders around individual items.

Currently, with SQUEEZE=ON, the right margin border for subheadings and subfootings is
defined based on the maximum width of all heading, footing, subheading, and subfooting lines.
The length of subheading and subfooting lines is tied to the lengths of the page heading and
page footing, not to the size of the data columns in the body of the report. You can use the
ALIGN-BORDERS=BODY attribute in a StyleSheet to align the subheadings and subfootings with
the report body on PDF report output instead of the other heading elements.

Grids: In an HTML report, you can use the GRID attribute in a StyleSheet to turn grid lines on
and off for the entire report. When used in conjunction with internal cascading style sheets,
GRID produces a thin grid line rather than a thick double line (the HTML default). In PDF
reports you can use the HGRID and VGRID attributes to add horizontal or vertical grid lines and
adjust their density.

Note: The SET GRID parameter, which applies to graphs, is not the same as the GRID
StyleSheet attribute.

Reference: Grid Display Attributes

Attribute

Description

GRID

Controls grid display.

Applies to

HTML

PDF

PS

DHTML

PPTX

PPT

Creating Reports With TIBCO® WebFOCUS Language

 1403

Adding Grids and Borders

Attribute

Description

Applies to

HGRID

Controls horizontal grid display and grid line density.

VGRID

Control vertical grid display and grid line density.

PDF

PS

DHTML

PPTX

PPT

PDF

PS

DHTML

PPTX

PPT

Note: When viewing PDF reports with the Adobe Reader, GRID lines may appear thinner than
specified if the view is not set to 100%. For example, if you view the document at the 50%
setting, some GRID lines may be thinner than others.

Syntax:

How to Control Grid Display in HTML Reports

[TYPE=REPORT,] GRID= option, $

where:

TYPE=REPORT

Applies the grid to the entire report. Not required, as it is the default.

option

Is one of the following:

ON applies a grid to a report. Does not apply grid lines to cells underneath a BY field value
until the value changes. Column titles are not underlined. ON is the default value.

OFF disables the default grid. Column titles are underlined. You can include blank lines
and underlines. You cannot wrap cell data. With this setting, a report may be harder to
read.

FILL applies grid lines to all cells of a report. Column titles are not underlined.

1404

Syntax:

How to Add and Format Borders

To request a uniform border, use this syntax:

21. Laying Out the Report Page

TYPE=type, BORDER=option, [BORDER-STYLE=line_style,]
    [BORDER-COLOR={color|RGB(r g b)},] $

To specify different characteristics for the top, bottom, left, and/or right borders, use this
syntax:

TYPE=type, BORDER-position=option,
   [BORDER[-position]-STYLE=line_style,]
   [BORDER[-position]-COLOR={color|RGB(r g b)},] $

where:

type

Identifies the report component to which borders are applied. See Identifying a Report
Component in a WebFOCUS StyleSheet on page 1249 for valid values.

option

Can be one of the following values:

ON turns borders on. ON generates the same line as MEDIUM.

Note: The MEDIUM line setting ensures consistency with lines created with GRID
attributes.

OFF turns borders off. OFF is the default value.

LIGHT specifies a thin line.

MEDIUM identifies a medium line. ON sets the line to MEDIUM.

HEAVY identifies a thick line.

width specifies the line width in points, where 72 pts=1 inch. Note that this option is not
supported with Excel 2003, which does not have an option for specifying a number to
precisely set the border width (thickness) in points.

Tip: Line width specified in points is displayed differently in HTML and PDF output. For
uniform appearance, regardless of display format, use LIGHT, MEDIUM, or HEAVY.

position

Specifies which border line to format. Valid values are: TOP, BOTTOM, LEFT, RIGHT.

You can specify a position qualifier for any of the BORDER attributes. This enables you to
format line width, line style, and line color individually, for any side of the border.

Creating Reports With TIBCO® WebFOCUS Language

 1405

Adding Grids and Borders

line_style

Sets the style of the border line. WebFOCUS StyleSheets support all of the standard
cascading style sheet line styles. Several 3-dimensional styles are available only in HTML,
as noted by asterisks. Valid values are:

Style

NONE

SOLID

DOTTED

DASHED

DOUBLE

GROOVE*

RIDGE*

INSET*

OUTSET*

Description

No border is drawn.

Solid line.

Dotted line.

Dashed line.

Double line.

3D groove. (Not supported with Excel 2003, which has no option
for specifying this type of border.)

3D ridge. (Not supported with Excel 2003, which has no option
for specifying this type of border.)

3D inset.

3D outset.

color

Is one of the preset color values. The default value is BLACK.

If the display or output device does not support colors, it substitutes shades of gray. For a
complete list of available color values, see Formatting Report Data on page 1697.

RGB

Specifies the font color using a mixture of red, green, and blue.

(r g b)

Is the desired intensity of red, green, and blue, respectively. The values are on a scale of 0
to 255, where 0 is the least intense and 255 is the most intense. Using the three color
components in equal intensities results in shades of gray.

1406

21. Laying Out the Report Page

Note: Format EXL2K does not support the GRID=ON parameter.

Example:

Inserting and Formatting a Border

This request generates an HTML report with a heavy red dotted line around the entire report
heading.

TABLE FILE GGSALES
SUM BUDUNITS UNITS BUDDOLLARS DOLLARS
BY CATEGORY
ON TABLE SUBHEAD
"</1 Sales Report"
"**CONFIDENTIAL**"
"December 2002 </1"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
TYPE=TABHEADING, STYLE=BOLD, JUSTIFY=CENTER, BORDER=HEAVY,
     BORDER-COLOR=RED, BORDER-STYLE=DOTTED, $
ENDSTYLE
END

The output is:

Tip: You can use the same BORDER syntax to generate this output in a PDF or PS report.

Creating Reports With TIBCO® WebFOCUS Language

 1407

Adding Grids and Borders

Example:

Displaying the Default Grid on an HTML Report

This request uses the default setting GRID=ON.

TABLE FILE GGSALES
SUM UNITS DOLLARS
BY CATEGORY BY PRODUCT
ON TABLE SET PAGE-NUM OFF
END

The cells underneath the sort field CATEGORY do not have grid lines until the value changes
(for example, from Coffee to Food):

Example:

Applying Grid Lines to All Cells of an HTML Report

This request uses GRID=FILL to apply grid lines to all cells, including those underneath the
sort field CATEGORY.

TABLE FILE GGSALES
SUM UNITS DOLLARS
BY CATEGORY BY PRODUCT
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=FILL, $
ENDSTYLE
END

1408

All cells have grid lines:

21. Laying Out the Report Page

Example:

Removing a Grid From an HTML Report

This request uses GRID=OFF to remove the default grid from a report.

TABLE FILE GGSALES
SUM UNITS DOLLARS
BY CATEGORY BY PRODUCT
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1409

Adding Grids and Borders

Column titles are underlined:

Reference: Adding Borders to Excel Report Output

Adding borders to Excel report output also may add blank rows.

The presence of any BORDER syntax (even BORDERS=OFF), whether it is in the inline
procedure or in the referenced StyleSheet, places the procedure in BORDER mode where the
styling and spacing is adjusted and may result in extra blank rows.

Example:

Adding Borders to FORMAT XLSX Report Output

The following request turns borders on and generates FORMAT XLSX report output.

TABLE FILE WF_RETAIL_LITE
SUM COGS_US
BY PRODUCT_CATEGORY
BY BUSINESS_REGION
HEADING
"This is the heading"
ON TABLE PCHOLD FORMAT XLSX
ON TABLE NOTOTAL
ON TABLE SET STYLE *
TYPE=REPORT,BORDER=ON,$
ENDSTYLE
END

1410

The output is shown in the following image. A blank row has been added after the heading.

21. Laying Out the Report Page

Creating Reports With TIBCO® WebFOCUS Language

 1411

Adding Grids and Borders

The following version of the request has no border attributes.

TABLE FILE WF_RETAIL_LITE
SUM COGS_US
BY PRODUCT_CATEGORY
BY BUSINESS_REGION
HEADING
"This is the heading"
ON TABLE PCHOLD FORMAT XLSX
ON TABLE NOTOTAL
END

1412

The output is shown in the following image. There is no blank row between the report heading
and report body.

21. Laying Out the Report Page

Creating Reports With TIBCO® WebFOCUS Language

 1413

Adding Grids and Borders

Syntax:

How to Insert Inner and Outer Borders Within Headings or Footings

BORDERALL is the quickest way to add borders to the entire heading grid. This feature is
supported in PDF, DHTML, HTML, XLSX, and PPTX formats. Individual borders can be removed
by explicitly turning the border off in individual items using BORDER, BORDER-LEFT, BORDER-
RIGHT, BORDER-TOP, and BORDER-BOTTOM. For a given item that is bordered by BORDERALL,
BORDER-LEFT=OFF presents the item with no left border, but the defined border style is
retained for top, bottom, and right borders.

Three levels of borders for headings and footings are supported:

1. Individual cell borders.

BORDER-LEFT, BORDER-RIGHT, BORDER-TOP, and BORDER-BOTTOM can be used to set the
individual components of the external border of the heading or a selected item or cell.

2. All outer borders.

BORDER= is used to set the external borders within a heading or footing.

3. All outer and internal borders.

BORDERALL is used to apply border characteristics to both the internal and external
borders of the selected heading or footing.

Note: BORDERALL applies to the entire heading or footing element. It cannot be used for
individual lines or items within a heading or footing element.

To turn on all external and internal borders (a border grid):

TYPE=headfoot, BORDERALL=option, [BORDER-STYLE=line_style,] [BORDER-
COLOR={color|RGB(r g b)},] $

where:

headfoot

Is the type of heading or footing. Valid values are TABHEADING, TABFOOTING, HEADING,
FOOTING, SUBHEAD, and SUBFOOT.

Note: BORDERALL applies to the entire heading or footing element. It cannot be used for
individual lines or items within a heading or footing element.

option

Can be one of the following values:

ON turns borders on. ON generates the same line as MEDIUM.

Note: The MEDIUM line setting ensures consistency with lines created with GRID
attributes.

1414

21. Laying Out the Report Page

OFF turns borders off. OFF is the default value.

LIGHT specifies a thin line.

MEDIUM identifies a medium line. ON sets the line to MEDIUM.

HEAVY identifies a thick line.

Entering a numeric value specifies the line width in points, where 72 pts=1 inch. Note
that this option is not supported with Excel 2003, which does not have an option for
specifying a number to precisely set the border width (thickness) in points.

Tip: Line width specified in points is displayed differently in HTML and PDF output. For
uniform appearance, regardless of display format, use LIGHT, MEDIUM, or HEAVY.

To request a uniform border, use this syntax:

TYPE=headfoot, BORDER=option

To specify different characteristics for the top, bottom, left, and/or right borders, use this
syntax:

TYPE=headfoot, BORDER-position=option,
   [BORDER[-position]-STYLE=line_style,]
   [BORDER[-position]-COLOR={color|RGB(r g b)},] $

where:

headfoot

Identifies the heading, footing, subheading, or subfooting to which borders are applied.

position

Specifies which border line to format. Valid values are: TOP, BOTTOM, LEFT, RIGHT.

You can specify a position qualifier for any of the BORDER attributes. This enables you to
format line width, line style, and line color individually, for any side of the border.

option

Can be one of the following values:

ON turns borders on. ON generates the same line as MEDIUM.

Note: The MEDIUM line setting ensures consistency with lines created with GRID
attributes.

OFF turns borders off. OFF is the default value.

LIGHT specifies a thin line.

Creating Reports With TIBCO® WebFOCUS Language

 1415

Adding Grids and Borders

MEDIUM identifies a medium line. ON sets the line to MEDIUM.

HEAVY identifies a thick line.

Entering a numeric value specifies the line width in points, where 72 pts=1 inch. Note
that this option is not supported with Excel 2003, which does not have an option for
specifying a number to precisely set the border width (thickness) in points.

Tip: Line width specified in points is displayed differently in HTML and PDF output. For
uniform appearance, regardless of display format, use LIGHT, MEDIUM, or HEAVY.

line_style

Sets the style of the border line. WebFOCUS StyleSheets support all of the standard
cascading style sheet line styles. Several three-dimensional styles are available only in
HTML, as noted by asterisks. Valid values are:

Style

NONE

SOLID

DOTTED

DASHED

DOUBLE

GROOVE*

RIDGE*

Description

No border is drawn.

Solid line.

Dotted line.

Dashed line.

Double line.

3D groove. (Not supported with Excel 2003, which has no option
for specifying this type of border.)

3D ridge. (Not supported with Excel 2003, which has no option for
specifying this type of border.)

INSET*

3D inset.

OUTSET*

3D outset.

Note: All line types supported for PDF, DHTML, and PPTX can be used for individual
internal borders with HEADALIGN=BODY.

1416

21. Laying Out the Report Page

color

Is one of the preset color values. The default value is BLACK.

If the display or output device does not support colors, it substitutes shades of gray. For a
complete list of available color values, see Color Values in a Report on page 1701.

RGB

Specifies the font color using a mixture of red, green, and blue.

(r g b)

Is the desired intensity of red, green, and blue, respectively, separated by spaces. The
values are on a scale of 0 to 255, where 0 is the least intense and 255 is the most
intense. Using the three color components in equal intensities results in shades of gray.

Example:

Controlling Borders Within Heading and Footing Elements in PDF Report Output

The following request against the EMPLOYEE data source has a page heading, a subheading, a
subfooting, and a report footing:

TABLE FILE EMPLOYEE
HEADING
" Department Report Page <TABPAGENO "
PRINT LAST_NAME AS ''
FIRST_NAME AS ''
CURR_SAL AS ''
CURR_JOBCODE AS ''
BY DEPARTMENT AS ''
WHERE CURR_SAL NE 0.0
ON TABLE PCHOLD FORMAT PDF
ON DEPARTMENT SUBFOOT
" "
"Subtotal:<ST.CURR_SAL"
" "
ON DEPARTMENT SUBHEAD
"Department <+0>Last Name <+0>First Name <+0>Salary<+0>Jobcode <+0>"
ON TABLE SUBFOOT
"Grand Total:<ST.CURR_SAL"
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
TYPE=REPORT, FONT=ARIAL, BORDER=ON, SQUEEZE=ON, $
TYPE=REPORT, COLUMN=CURR_JOBCODE,SQUEEZE=.75, $
TYPE = SUBHEAD, HEADALIGN=BODY, BORDERALL=ON,$
TYPE = SUBFOOT, HEADALIGN=BODY,$
TYPE = SUBFOOT, LINE=2, ITEM=1, COLSPAN=3, JUSTIFY=RIGHT,$
TYPE = SUBFOOT, LINE=2, ITEM=2, JUSTIFY=RIGHT,$
TYPE = TABFOOTING, HEADALIGN=BODY,$
TYPE = TABFOOTING, ITEM=1, COLSPAN=3, JUSTIFY=RIGHT,$
TYPE = TABFOOTING, ITEM=2, JUSTIFY=RIGHT,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1417


Adding Grids and Borders

The REPORT component has BORDER=ON, so the page heading has an external border.

The subheading has BORDERALL=ON and HEADALIGN=BODY, so the subheading grid aligns
with the body grid, and each item within the subhead is presented as fully bordered individual
cells.

The StyleSheet aligns the subfooting elements with the body of the report, and has the salary
subtotal on the second line aligned and justified with the CURR_SAL column.

The table footing has a border around the entire footing because the REPORT component
specifies BORDER=ON. The grand total is aligned and justified with the CURR_SAL column on
the report.

The output is:

Syntax:

How to Align Subheading and Subfooting Margins With the Report Body

Currently, with SQUEEZE=ON, the right margin border for subheadings and subfootings is
defined based on the maximum width of all heading, footing, subheading, and subfooting lines.
The length of subheading and subfooting lines is tied to the lengths of the page heading and
page footing, not to the size of the data columns in the body of the report.

1418

21. Laying Out the Report Page

You can use the ALIGN-BORDERS=BODY attribute in a StyleSheet to align the subheadings and
subfootings with the report body on PDF report output instead of the other heading elements.

You can align subheading and subfooting margins with the report body either by adding the
ALIGN-BORDERS=BODY attribute to the StyleSheet declaration for the REPORT component, or
placing it in its own declaration without a TYPE attribute.

[TYPE=REPORT,] ALIGN-BORDERS={OFF|BODY} ,$

where:

OFF

Does not align the right margin of subheadings and subfootings with the report body.

BODY

Specifies that the width of subheading and subfooting lines is independent of heading,
footing, tabheading, and tabfooting lines, and that the right border of the report body will
be aligned by either extending subheading and subfooting lines (if they are narrower than
the data columns) or extending the data columns (if the data columns are narrower than
the maximum width of subheadings and subfootings).

Reference: Considerations for Aligning Subheading and Subfooting Margins With the Report

Body

Without the ALIGN-BORDERS=BODY attribute, the width of the subheading and subfooting lines
is determined by the largest width of all of the headings and footings (report, page,
subheadings, and subfootings).

Creating Reports With TIBCO® WebFOCUS Language

 1419

Adding Grids and Borders

The following image illustrates report output without the ALIGN-BORDERS=BODY attribute.

1420

21. Laying Out the Report Page

When the body lines are wider than the subheading and subfooting lines, the border and
backcolor of the subheading and subfooting lines are expanded to match the width of the data
lines, as shown on the following report output.

Creating Reports With TIBCO® WebFOCUS Language

 1421

Adding Grids and Borders

If the subheading and subfooting lines are longer than the body lines, an additional filler cell is
added to each data line to allow the defined borders and backcolor to fill the width defined by
the subheading and subfooting lines, as shown on the following report output.

1422

21. Laying Out the Report Page

ALIGN-BORDERS=BODY has been designed to work on:

Single panel reports (reports that do not panel horizontally).

Paneled reports where HEADPANEL has been turned on for all of the subheadings and
subfootings defined in the report.

Setting HEADPANEL ON causes the headings and footings from the first page of a Paneled
report to replicate on the subsequent panels. If HEADPANEL is not used, content can be
placed in the Paneled headings by explicitly positioning items within the headings using the
StyleSheet attribute POSITION. In these situations, ALIGN-BORDERS=BODY is ignored.

Therefore, if HEADPANEL is turned on at the REPORT level and not explicitly turned off for
any of the individual subheadings or subfootings, or if it is explicitly turned on for all
subheadings and subfootings, ALIGN-BORDERS=BODY will align the borders of all
subheadings and subfootings to the data. Otherwise, the borders will continue to exhibit
the default behavior of aligning with the page headings and footings.

Creating Reports With TIBCO® WebFOCUS Language

 1423

Adding Grids and Borders

Example:

Aligning Subheading and Subfooting Margins in a Single Panel PDF Report

The following request against the GGSALES data source has a report heading, report footing,
page heading, page footing, and a subheading for each region. The margins of the
subheadings and subfootings are not aligned (ALIGN-BORDERS=OFF ,$):

DEFINE FILE GGSALES
SHOWCATPROD/A30 = CATEGORY || (' / ' | PRODUCT);
END
TABLE FILE GGSALES
SUM
     DOLLARS/I8M AS ''
BY REGION
BY ST
BY CITY
ACROSS SHOWCATPROD AS 'Product Sales'

ON REGION SUBHEAD
" "
"Subheading <+0>Region <REGION<+0> "
" "
ON REGION SUBTOTAL AS '*TOTAL'
ON TABLE SUBHEAD
"Report Heading"
" "
"TYPE=REPORT, ALIGN-BORDERS=OFF, BORDER=ON, $"
HEADING
"Page Heading "
" "
" "
" "
FOOTING
" "
"Page Footing<+0>Page <TABPAGENO "
ON TABLE SUBFOOT
" "
"Report Footing"

1424


21. Laying Out the Report Page

WHERE CATEGORY EQ 'Coffee';
ON TABLE SET PAGE-NUM OFF
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
    TYPE=REPORT,
     FONT='ARIAL',
     SIZE=9,
     LEFTMARGIN=.75,
     RIGHTMARGIN=.5,
     TOPMARGIN=.1,
     BOTTOMMARGIN=.1,
     ALIGN-BORDERS=OFF,
     BORDER=ON,
     SQUEEZE=ON,$
$
TYPE=TITLE,
     STYLE=BOLD,
$
TYPE=TABHEADING,
     SIZE=12,
     STYLE=BOLD,
$
TYPE=TABHEADING,
     LINE=3,
     JUSTIFY=CENTER,
$
TYPE=TABFOOTING,
     SIZE=12,
     STYLE=BOLD,
$
TYPE=HEADING,
     SIZE=12,
     STYLE=BOLD,
$
TYPE=HEADING,
     IMAGE=smplogo1.gif,
     POSITION=(+4.6000000 +0.03000000),
     JUSTIFY=RIGHT,
$
TYPE=FOOTING,
     SIZE=12,
     STYLE=BOLD,
$
TYPE=FOOTING,
   LINE=2,
   ITEM=2,
   OBJECT=TEXT,
   POSITION=6.3,
     SIZE=12,
     STYLE=BOLD,

Creating Reports With TIBCO® WebFOCUS Language

 1425

Adding Grids and Borders

$
TYPE=SUBHEAD,
     SIZE=10,
     STYLE=BOLD,
$
TYPE=SUBHEAD,
  LINE=2,
  ITEM=3,
  OBJECT=TEXT,
  POSITION=2.5,
$
TYPE=SUBFOOT,
     SIZE=10,
     STYLE=BOLD,
$
TYPE=SUBTOTAL,
     BACKCOLOR=RGB(210 210 210),
$
TYPE=ACROSSVALUE,
     SIZE=9,
     WRAP=ON,
$
TYPE=ACROSSTITLE,
     STYLE=BOLD,
$
TYPE=GRANDTOTAL,
     BACKCOLOR=RGB(210 210 210),
     STYLE=BOLD,
$
ENDSTYLE
END

1426

The output shows that the subheading margins align with the heading, not with the report
body.

21. Laying Out the Report Page

Creating Reports With TIBCO® WebFOCUS Language

 1427

Adding Grids and Borders

Now change the ALIGN-BORDERS attribute to ALIGN-BORDERS=BODY and rerun the request.
The subheadings now align with the report body, as shown in the following image.

1428

Example:

Aligning Subheading and Subfooting Margins in a Multi-Panel Report

The following request has HEADPANEL=ON for all headings and footings. It also has the ALIGN-
BORDERS=BODY attribute:

21. Laying Out the Report Page

SET BYPANEL=ON
DEFINE FILE GGSALES
SHOWCATPROD/A30 = CATEGORY || (' / ' | PRODUCT);
END
TABLE FILE GGSALES
SUM
     DOLLARS/I8M AS ''
BY REGION
BY ST
BY CITY
ACROSS SHOWCATPROD AS 'Product Sales'

ON REGION SUBHEAD
" "
"Subheading <+0>Region <REGION<+0> "
" "
ON REGION SUBTOTAL AS '*TOTAL'
ON TABLE SUBHEAD
"Report Heading"
" "
"TYPE=REPORT, ALIGN-BORDERS=BODY, HEADPANEL=ON, BORDER=ON, $"
HEADING
"Page Heading "
" "
" "
" "
FOOTING
" "
"Page Footing<+0>Page <TABPAGENO "
ON TABLE SUBFOOT
" "
"Report Footing"

Creating Reports With TIBCO® WebFOCUS Language

 1429


Adding Grids and Borders

WHERE CATEGORY NE 'Coffee';
ON TABLE SET PAGE-NUM OFF
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
     UNITS=IN,
     SQUEEZE=ON,
     ORIENTATION=PORTRAIT,
$
TYPE=REPORT,
     FONT='ARIAL',
     SIZE=9,
     LEFTMARGIN=.75,
     RIGHTMARGIN=.5,
     TOPMARGIN=.1,
     BOTTOMMARGIN=.1,
     HEADPANEL=ON,
     ALIGN-BORDERS=BODY,
     BORDER=ON,
$
TYPE=TITLE,
     STYLE=BOLD,
$
TYPE=TABHEADING,
     SIZE=12,
     STYLE=BOLD,
$
TYPE=TABHEADING,
     LINE=3,
     JUSTIFY=CENTER,
$
TYPE=TABFOOTING,
     SIZE=12,
     STYLE=BOLD,
$
TYPE=HEADING,
     SIZE=12,
     STYLE=BOLD,
$
TYPE=HEADING,
     IMAGE=smplogo1.gif,
     POSITION=(+4.6000000 +0.03000000),
     JUSTIFY=RIGHT,

1430

21. Laying Out the Report Page

$
TYPE=FOOTING,
     SIZE=12,
     STYLE=BOLD,
$
TYPE=FOOTING,
   LINE=2,
   ITEM=2,
   OBJECT=TEXT,
   POSITION=6.3,
     SIZE=12,
     STYLE=BOLD,
$
TYPE=SUBHEAD,
     SIZE=10,
     STYLE=BOLD,
$
TYPE=SUBHEAD,
   LINE=2,
   ITEM=3,
   OBJECT=TEXT,
   POSITION=2.5,
$
TYPE=SUBFOOT,
     SIZE=10,
     STYLE=BOLD,
$
TYPE=SUBTOTAL,
     BACKCOLOR=RGB(210 210 210),
$
TYPE=ACROSSVALUE,
     SIZE=9,
     WRAP=ON,
$
TYPE=ACROSSTITLE,
     STYLE=BOLD,
$
TYPE=GRANDTOTAL,
     BACKCOLOR=RGB(210 210 210),
     STYLE=BOLD,
$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1431

Adding Grids and Borders

The output shows that the subheadings are aligned with the data on each panel.

Syntax:

How to Add and Adjust Grid Lines (PDF or PS)

This syntax applies to a PDF or PS report.

TYPE=type, {HGRID|VGRID}={ON|OFF|HEAVY}, $

where:

type

Identifies the report component to which grid lines are applied. See Identifying a Report
Component in a WebFOCUS StyleSheet on page 1249 for valid values.

HGRID

Specifies horizontal grid lines.

VGRID

Specifies vertical grid lines.

ON

OFF

Applies light grid lines.

Suppresses grid lines. OFF is the default value.

1432

21. Laying Out the Report Page

HEAVY

Applies heavy grid lines.

Example:

Applying Grid Lines to Report Data (PDF)

This request applies light, horizontal grid lines to report data.

SET ONLINE-FMT = PDF
TABLE FILE GGDEMOG
HEADING
"State Statistics"
" "
SUM HH AS 'Number of,Households' AVGHHSZ98 AS 'Avg.,Size'
MEDHHI98 AS 'Avg.,Income'
BY ST
WHERE ST EQ 'CA' OR 'FL' OR 'NY'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=DATA, HGRID=ON, $
ENDSTYLE
END

In the PDF report, the lines make it easier to distinguish the data by state:

Defining Borders Around Boxes With PPTX and PDF Formats

In PPTX and PDF formats, the backcolor of a box may be defined independently of the border
color.

Borders Without Backcolor

When the border color is defined and there is no backcolor, only the border or outline of the
box is displayed in the border color specified, as shown in the example below.

Creating Reports With TIBCO® WebFOCUS Language

 1433

Defining Borders Around Boxes With PPTX and PDF Formats

TABLE FILE GGSALES
BY REGION NOPRINT
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
TYPE=REPORT, OBJECT=BOX, POSITION=(1 1), DIMENSION=(2 1), BORDER-
COLOR=GREEN,$
ENDSTYLE
END

The output is shown in the following image.

Backcolor Without Borders

In PPTX format, when a backcolor is defined and there is no border (BORDER-STYLE=NONE),
the box retains the color defined for the backcolor.

TABLE FILE GGSALES
BY REGION NOPRINT
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
TYPE=REPORT, OBJECT=BOX, POSITION=(1 1), DIMENSION=(2 1), BACKCOLOR=GREEN,
BORDER-STYLE=NONE, $
ENDSTYLE
END

The output is shown in the following image.

In PDF format, a gray outline appears around the backcolor, as shown in the following image.

Border Styles Supported

Border styles, except 3D border styles such as ridged, groove, inset, and outset, are supported
in PPTX and PDF formats.

1434

21. Laying Out the Report Page

TABLE FILE GGSALES
BY REGION NOPRINT
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
TYPE=REPORT, OBJECT=BOX, POSITION=(1 1), DIMENSION=(2 1), BORDER-
COLOR=GREEN, BORDER-STYLE=DASHED, $
ENDSTYLE
END

The output is shown in the following image.

Note: When OBJECT=BOX and BORDER-STYLE=DOUBLE is used with FORMAT PPTX and
FORMAT PDF in StyleSheet syntax, a solid border, instead of a double border, is generated.

Displaying Superscripts On Data, Heading, and Footing Lines

Superscript characters are supported as a text style in text objects using HTML markup tags.
The superscript markup tag is now supported in data columns, headings, and footings in
HTML, PDF, PPTX, and PS output formats. Superscript values can be defined within the data,
added to virtual fields, or added to text strings displayed in headings and footings.

In order to activate the translation of the HTML markup tags, in the StyleSheet set
MARKUP=ON for any report component that will display superscripts. Without this attribute, the
markup tags will be treated as text, not tags.

Note: For XLSX output format, you can use superscript functionality in headings and footings
using STYLE=SUPERSCRIPT syntax. STYLE=SUPERSCRIPT syntax is ignored for all other output
formats.

Syntax:

How to Display Superscripts on Report Data, Heading, and Footing Lines

If the tags are not within the data itself, create a field that contains the text to be used as a
superscript. Also, turn markup tags on for the components that will display superscripts:

In a DEFINE or COMPUTE command, define a field that contains the text to be displayed as
a superscript.

For a DEFINE FILE command, the syntax is:

Creating Reports With TIBCO® WebFOCUS Language

 1435

Displaying Superscripts On Data, Heading, and Footing Lines

DEFINE FILE ...
field/An = <sup>text</sup>;
END

For a COMPUTE command or a DEFINE in a Master File, the syntax is:

{COMPUTE|DEFINE} field/An = <sup>text</sup>;

where:

n

Is the length of the string defining the superscript, including the text to be used as the
superscript and the opening and closing markup tags (<sup> and </sup>).

text

Is the text to be used as the superscript.

In the StyleSheet, set MARKUP=ON for any report component that will display superscripts:

TYPE=component,MARKUP=ON ... ,$

where:

component

Is one of the following report components: DATA, HEADING, FOOTING, SUBHEAD,
SUBFOOT, TABHEADING, TABFOOTING.

Example:

Displaying Superscripts in Data and Footing Lines in PDF Output

The following request against the GGSALES data source defines two fields that will display as
superscripts. SUP1 and SUP2 consist of the numbers 1 and 2, respectively. SUPCOPY
consists of a copyright symbol. Note that the difference is the syntax as defined for a text
value as opposed to a HEX value.

The COMPUTE command compares sales dollars to budgeted dollars. If the value calculated is
less than a minimum defined, the superscript SUP1 is concatenated after the category name.
If the value is greater, SUP2 is concatenated.

The superscript SUPCOPY is used to display the copyright symbol in the footing of the report.

The footing concatenates the superscript fields in front of their explanations.

In the StyleSheet, every component that will display a superscript has the attribute
MARKUP=ON.

1436

21. Laying Out the Report Page

DEFINE FILE GGSALES
SUP1/A12= '<SUP>1</SUP>';
SUP2/A15= '<SUP>2</SUP>';
SUPCOPY/A20= '<SUP>'||HEXBYT(169,'A2')||'</SUP>';
END
TABLE FILE GGSALES
SUM
COMPUTE PROFIT/D12CM=DOLLARS-BUDDOLLARS; NOPRINT
COMPUTE SHOWCAT/A100=IF PROFIT LE -50000 THEN CATEGORY || SUP1
       ELSE IF PROFIT GT 50000 THEN CATEGORY || SUP2
           ELSE CATEGORY; AS Category
BUDDOLLARS/D12CM
DOLLARS/D12CM
BY REGION
BY CATEGORY NOPRINT
HEADING
"Analysis of Budgeted and Actual Sales"
FOOTING
""
"<SUP1 Dollar sales $50,000 less than budgeted amount."
"<SUP2 Dollar sales $50,000 greater than budgeted amount."
""
"Copyright<SUPCOPY 2012, by Information Builders, Inc "
ON TABLE SET HTMLCSS ON
ON TABLE SET SQUEEZE ON
ON TABLE SET PAGE-NUM OFF
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/javaassist/intl/EN/
ENIADefault_combine.sty,$
TYPE=DATA,MARKUP=ON,$
TYPE=DATA,COLUMN=N5, COLOR=RED, WHEN=PROFIT LT -50000,$
TYPE=DATA,COLUMN=N6, COLOR=GREEN, WHEN=PROFIT GT 50000,$
TYPE=HEADING, JUSTIFY=LEFT,$
TYPE=FOOTING, MARKUP=ON, JUSTIFY=LEFT,$
TYPE=FOOTING, LINE=2,JUSTIFY=LEFT, COLOR=RED,$
TYPE=FOOTING, LINE=3,JUSTIFY=LEFT, COLOR=GREEN,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1437

Displaying Superscripts On Data, Heading, and Footing Lines

The output is:

1438

Example:

Displaying Superscripts in Heading and Footing Lines in XLSX Output

21. Laying Out the Report Page

The following request against the GGSALES data source defines superscripts for trademark
and copyright symbols in the heading and footing. COPYRIGHT consists of a copyright symbol.
Note the STYLE = SUPERSCRIPT syntax in the heading and footing lines.

DEFINE FILE GGSALES
COPYRIGHT/A1= HEXBYT(169, 'A1');
END
TABLE FILE GGSALES
SUM UNITS BY CATEGORY
HEADING
"Company-Trademark<+0>TM"
" "
"Company-Copyright<+0><COPYRIGHT"
" "
FOOTING
"Company-Trademark<+0>TM"
" "
"Company-Copyright<+0><COPYRIGHT"
" "
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET STYLE *
TYPE=HEADING, WRAP=OFF, $
TYPE=HEADING, LINE=1, ITEM=2, OBJECT=TEXT, STYLE='SUPERSCRIPT+BOLD+ITALIC',
COLOR=RED, $
TYPE=HEADING, LINE=3, ITEM=1, OBJECT=FIELD, STYLE='SUPERSCRIPT+BOLD',
COLOR=GREEN, $
TYPE=FOOTING, LINE=1, ITEM=2, OBJECT=TEXT, STYLE='SUPERSCRIPT+BOLD+ITALIC',
COLOR=RED, $
TYPE=FOOTING, LINE=3, ITEM=1, OBJECT=FIELD, STYLE='SUPERSCRIPT+BOLD',
COLOR=GREEN, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1439

Adding Underlines and Skipped Lines

The output is shown in the following image.

Adding Underlines and Skipped Lines

You can make a detailed tabular report easier to read by separating sections with blank lines
or underlines.

You cannot add blank lines or underlines to an HTML report that displays a grid. You can add
blank lines or underlines if you set the GRID attribute to OFF.

When inserting blank lines, the setting of the LINES parameter should be at least one less
than the setting of the PAPER parameter to allow room for blanks after the display of data on a
page.

A Financial Modeling Language (FML) report with columns of numbers includes, by default, an
underline before a RECAP calculation for readability. In these types of reports, you can change
the default underline from light to heavy (or single to double in a PDF report).

1440

21. Laying Out the Report Page

Reference: Section Separation Features

Feature

SKIP-LINE*

Description

Applies to

Adds a blank line.

HTML (requires GRID=OFF)

DHTML

PDF

PS

XLSX

EXL2K

TYPE=SKIPLINE

Formats a blank line.

DHTML

PDF

PS

UNDER-LINE*

Underlines a sort group.

HTML (requires GRID=OFF)

TYPE=UNDERLINE

Formats an underline.

DHTML

DHTML

PDF

PS

STYLE={+|-}UNDERLINE*

Adds an underline to a
report component, or
removes an underline from
a report component other
than a column title.

PDF

PS

HTML

DHTML

PDF

PS

XLSX

EXL2K

Creating Reports With TIBCO® WebFOCUS Language

 1441

Adding Underlines and Skipped Lines

Feature

Description

STYLE={+|-}
EXTUNDERLINE*

Extends the underline to or
removes the underline from
the entire report column in a
styled report.

BAR AS '{-|=}'*

Selects a single or double
underline in an FML report.

For HTML, selects a light or
heavy underline in an FML
report.

Applies to

DHTML

PDF

PS

PPT

PPTX

HTML

DHTML

PDF

PS

XLSX

EXL2K

* Not supported with border.

Syntax:

How to Add a Blank Line

Use only one SKIP-LINE per report request.

display_command fieldname SKIP-LINE

or

{ON|BY} fieldname SKIP-LINE [WHEN expression;]

where:

display_command

Is a display command.

fieldname

Is the display or sort field after which a blank line is inserted.

SKIP-LINE used with a display field adds a blank line after every displayed line, in effect,
double-spacing a report. Double-spacing is helpful when a report is reviewed, making it
easy for the reader to write comments next to individual lines.

1442

21. Laying Out the Report Page

SKIP-LINE used with a sort field adds a blank line before every change in the value of that
field. This is one of the only ON conditions that does not have to refer solely to a sort (BY)
field.

ON|BY

Is a vertical sort phrase. The terms are synonymous.

WHEN expression

Specifies conditional blank lines in the display of a report as determined by a logical
expression. See Using Expressions on page 429 for details on expressions.

Example:

Adding a Blank Line Between Sort Groups

This request inserts a blank line before every change in value of the sort field EMP_ID.

DEFINE FILE EMPLOYEE
INCREASE/D8.2M = .05*CURR_SAL;
CURR_SAL/D8.2M=CURR_SAL;
NEWSAL/D8.2M=CURR_SAL + INCREASE;
END

TABLE FILE EMPLOYEE
PRINT CURR_SAL OVER INCREASE OVER NEWSAL
BY LOWEST 4 EMP_ID BY LAST_NAME BY FIRST_NAME
ON EMP_ID SKIP-LINE
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT PDF
END

Creating Reports With TIBCO® WebFOCUS Language

 1443


Adding Underlines and Skipped Lines

The data for each employee stands out and is easy to read:

Syntax:

How to Format a Blank Line

TYPE=SKIPLINE, attribute=value, $

where:

attribute

Is a valid StyleSheet attribute.

value

Is the value of the attribute.

Note: This option is supported for PDF, PS, and HTML reports (when used in conjunction with
internal cascading style sheets).

1444

Example:

Adding Color to Blank Lines

In this request, blank lines are formatted to display as silver in the output. The relevant
StyleSheet declaration is highlighted in the request.

21. Laying Out the Report Page

SET ONLINE-FMT=PDF
TABLE FILE CENTINV
HEADING
"Low Stock Report"
" "
SUM QTY_IN_STOCK
WHERE QTY_IN_STOCK LT 5000
BY PRODNAME
ON PRODNAME SKIP-LINE
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=SKIPLINE, BACKCOLOR=SILVER, $
ENDSTYLE
END

The report is:

Creating Reports With TIBCO® WebFOCUS Language

 1445

Adding Underlines and Skipped Lines

Syntax:

How to Underline a Sort Group

{ON|BY} fieldname UNDER-LINE [WHEN expression;]

where:

ON|BY

Is a vertical sort phrase. The terms are synonymous.

fieldname

Is the sort field to which the underline applies. UNDER-LINE adds an underline when the
value of the sort field changes. An underline automatically displays after options such as
RECAP or SUB-TOTAL but displays before page breaks.

WHEN expression

Specifies conditional underlines in the display of a report as determined by a logical
expression. See Using Expressions on page 429 for details on expressions.

Example:

Underlining a Sort Group

This request adds an underline when the value of the sort field BANK_NAME changes. It sets
the GRID attribute to OFF, as required by an HTML report.

TABLE FILE EMPLOYEE
PRINT EMP_ID AND BANK_ACCT AND LAST_NAME
BY BANK_NAME
ON BANK_NAME UNDER-LINE
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

1446

The data for each bank stands out and is easy to read:

21. Laying Out the Report Page

Syntax:

How to Format an Underline

TYPE=UNDERLINE ... COLOR={color|RGB} (r g b), $

where:

UNDERLINE

Denotes underlines generated by ON fieldname UNDER-LINE.

COLOR

Specifies the color of the underline. If the display or output device does not support colors,
it substitutes shades of gray. The default value is black.

color

Is one of the supported color values. For a list of supported values, see Color Values in a
Report on page 1701.

Creating Reports With TIBCO® WebFOCUS Language

 1447

Adding Underlines and Skipped Lines

RGB

Specifies the text color using a mixture of red, green, and blue.

(r g b)

Is the desired intensity of red, green, and blue, respectively. The values are on a scale of 0
to 255, where 0 is the least intense and 255 is the most intense.

Note that using the three-color components in equal intensities results in shades of gray.

Note: This option is supported for PDF, PS, and HTML reports (when used in conjunction with
internal cascading style sheets).

Example:

Formatting a Sort Group Underline

This request uses UNDERLINE to change the default color of an underline from black to red.

SET ONLINE-FMT = PDF
TABLE FILE GGSALES
SUM UNITS DOLLARS
BY CATEGORY BY PRODUCT
HEADING
"Sales Report"
" "
ON CATEGORY UNDER-LINE
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=UNDERLINE, COLOR=RED, $
ENDSTYLE
END

The result is an eye-catching separation between sort group values. The online PDF report is:

1448

21. Laying Out the Report Page

Syntax:

How to Add or Remove a Report Component Underline

TYPE=type, [subtype,] STYLE=[+|-]UNDERLINE, $

where:

type

Is the report component. For valid values, see Identifying a Report Component in a
WebFOCUS StyleSheet on page 1249.

subtype

Are additional attributes, such as COLUMN, ACROSS, or ITEM, needed to identify the
report component. For valid values, see Identifying a Report Component in a WebFOCUS
StyleSheet on page 1249.

+

-

Adds an underline to the inherited text style or specifies a combination of text styles (for
example, STYLE=BOLD+UNDERLINE). This is the default value.

Removes an underline from an inherited text style.

Syntax:

How to Remove an Underline From a Column Title

This syntax applies to an HTML report with internal cascading style sheet.

TYPE=TITLE, [COLUMN=column,] STYLE=-UNDERLINE, $

where:

COLUMN=column

Specifies a column. For valid values, see Identifying a Report Component in a WebFOCUS
StyleSheet on page 1249.

Creating Reports With TIBCO® WebFOCUS Language

 1449

Adding Underlines and Skipped Lines

Example:

Adding Column Underlines and Removing Column Title Underlines

This request adds underlines to the values of the column CATEGORY and removes the default
underlines from the column titles in an HTML report with internal cascading style sheet.

SET HTMLCSS = ON
TABLE FILE MOVIES
PRINT TITLE DIRECTOR
BY CATEGORY
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=TITLE, STYLE=-UNDERLINE, $
TYPE=REPORT, COLUMN=CATEGORY, STYLE=UNDERLINE, $
ENDSTYLE
END

The partial report is:

1450

21. Laying Out the Report Page

Syntax:

How to Extend an Underline to the Entire Report Column

By default, underlines for column titles on a report extend only from the beginning to the end of
the column title text. You can extend the underline to the entire report column in styled report
output using the EXTUNDERLINE option in your WebFOCUS StyleSheet. EXTUNDERLINE is an
option of the STYLE attribute for the TITLE report component. It is supported for formats
DHTML, PDF, PS, PPT, and PPTX.

TYPE = TITLE, [COLUMN = colspec,] STYLE = [+|-]EXTUNDERLINE  ,$

where:

colspec

Is any valid column specification.

+EXTUNDERLINE

Adds the EXTUNDERLINE option to the inherited text style or specifies a combination of
text styles (for example, STYLE=BOLD+UNDERLINE).

-EXTUNDERLINE

Removes the EXTUNDERLINE option from the inherited text style.

Reference: Usage Notes for the EXTUNDERLINE Attribute

HTML format is not supported because the browser calculates the column width and
renders the report.

GRID=ON and EXTUNDERLINE are mutually exclusive since the GRID line spans the width of
the column. GRID overrides any styling specified for the column title underline.

Example:

Extending an Underline to the Entire Report Column

The following request against the GGSALES data source sums dollar sales by city and by date:

DEFINE FILE GGSALES
YEAR/YY = DATE;
MONTH/M = DATE;
END
TABLE FILE GGSALES
SUM DOLLARS AS 'Sales'
BY DATE
BY CITY
WHERE YEAR EQ 1997
WHERE MONTH FROM 01 TO 05
WHERE CITY EQ 'Seattle' OR 'San Francisco' OR 'Los Angeles'
ON TABLE SET PAGE NOPAGE
ON TABLE PCHOLD FORMAT DHTML
END

Creating Reports With TIBCO® WebFOCUS Language

 1451

Adding Underlines and Skipped Lines

The output shows that only the column titles are underlined:

To underline entire columns, generate the output in a format that can be styled and use the
EXTUNDERLINE option in the STYLE attribute for the TITLE component. For example, the
following request creates DHTML output in which the column titles are in boldface and left
justified, and the underline is extended to the entire report column:

DEFINE FILE GGSALES
YEAR/YY = DATE;
MONTH/M = DATE;
END
TABLE FILE GGSALES
SUM DOLLARS AS 'Sales'
BY DATE
BY CITY
WHERE YEAR EQ 1997
WHERE MONTH FROM 01 TO 05
WHERE CITY EQ 'Seattle' OR 'San Francisco' OR 'Los Angeles'
ON TABLE SET PAGE NOPAGE
ON TABLE PCHOLD FORMAT DHTML
ON TABLE SET STYLE *
TYPE=TITLE, STYLE= BOLD +EXTUNDERLINE, JUSTIFY=LEFT, $
ENDSTYLE
END

1452

The output is:

21. Laying Out the Report Page

The following version of the request makes the EXTUNDERLINE and JUSTIFY=LEFT options the
default for the TITLE component, then makes the Date column title bold and removes the
extended underline from that column:

DEFINE FILE GGSALES
YEAR/YY = DATE;
MONTH/M = DATE;
END
TABLE FILE GGSALES
SUM DOLLARS AS 'Sales'
BY DATE
BY CITY
WHERE YEAR EQ 1997
WHERE MONTH FROM 01 TO 05
WHERE CITY EQ 'Seattle' OR 'San Francisco' OR 'Los Angeles'
ON TABLE SET PAGE NOPAGE
ON TABLE PCHOLD FORMAT DHTML
ON TABLE SET STYLE *
TYPE=TITLE,STYLE= EXTUNDERLINE, JUSTIFY=LEFT ,$
TYPE=TITLE,COLUMN= DATE, STYLE= -EXTUNDERLINE +BOLD ,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1453

Adding Underlines and Skipped Lines

The output is:

Syntax:

How to Change Density of an Underline in a Financial Modeling Language (FML)
Report

This syntax applies to an HTML report.

BAR [AS '{-|=}'] OVER

where:

-

=

Generates a light underline. Enclose the hyphen in single quotation marks. This is the
default value.

Generates a heavy underline. Enclose the equal sign in single quotation marks.

1454

Example:

Changing the Default Underline in a Financial Modeling Language (FML) Report
(HTML)

This request changes the default light underline to a heavy underline in an FML report.

21. Laying Out the Report Page

TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
1010 AS 'CASH ON HAND'       OVER
1020 AS 'DEMAND DEPOSITS'    OVER
1030 AS 'TIME DEPOSITS'      OVER
BAR AS '='                   OVER
RECAP TOTCASH = R1 + R2 + R3;
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

A heavy underline separates total cash from the detail data, making it stand out:

Example:

Changing the Default Underline in a Financial Modeling Language (FML) Report (PDF)

This request changes the default single underline in a PDF report to a double underline.

TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
1010 AS 'CASH ON HAND'       OVER
1020 AS 'DEMAND DEPOSITS'    OVER
1030 AS 'TIME DEPOSITS'      OVER
BAR AS '='                   OVER
RECAP TOTCASH = R1 + R2 + R3;
ON TABLE SET ONLINE-FMT PDF
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1455

Removing Blank Lines From a Report

The output is:

Removing Blank Lines From a Report

The DROPBLNKLINE parameter controls whether blank lines display in a WebFOCUS report.
With the options provided, you can affect blank lines that are automatically generated in
different locations within a report. You can choose to drop the blank lines around subtotals,
subheadings and subfootings, as well as certain data lines that may be blank and appear as
blank lines on the report output. Additionally, when using borders, you can select to remove
blank lines inserted around the headings and footings. You can eliminate these blank lines
from the report output using the SET DROPBLNKLINE options.

Syntax:

How to Control Automatic Blank Lines on Report Output

SET DROPBLNKLINE={OFF|ON|BODY|HEADING|ALL}

or

ON TABLE SET DROPBLNKLINE {OFF|ON|BODY|HEADING|ALL}

where:

OFF

Inserts system-generated blank lines as well as empty data lines. OFF is the default value.

ON|BODY

Removes system-generated blank lines within the body of the report (for example, before
and after subheads). In addition, certain data lines that may be blank and appear as blank
lines on the report output will be removed from the output. BODY is a synonym for ON.

HEADING

Removes the blank lines between headings and titles and between the report body and the
footing. Works in positioned formats (PDF, PS, DHTML, PPT, and PPTX) when a request has
a border or backcolor StyleSheet attribute anywhere in the report.

1456

21. Laying Out the Report Page

ALL

Provides both the ON and HEADING behaviors.

Reference: Usage Notes for SET DROPBLNKLINE=HEADING

In the positioned report formats (PDF, PS, DHTML, PPT, and PPTX) with borders or
backcolor, the system automatically generates a blank line below the heading and above
the footing. This is done by design to make bordered lines work together. Generally, the
rule is that each line is responsible for the border setting for its top and left border.
Therefore, the bottom border of the heading is set by the top border of the row beneath it.
To ensure that the bottom of the heading border is complete and does not interfere with
the top of the column titles border, a blank filler line is automatically inserted. This filler
line contains the defined bottom border of the heading as its top border. The same is true
between the bottom of the data and the top of the footing.

DROPBLNKLINE=HEADING removes the filler blank line by defining the height of the filler
line to zero. This causes the bottom border of the heading to become the top border of the
column titles. When backcolor is used without borders, this works well to close any blank
gaps in color. However, WebFOCUS processing will not remediate between line styles, so
using different border styles between different report elements may create some contention
between the border styling definitions. To ensure that you have consistent border line
styling between different report elements, use a single line style between the elements that
present together in the report.

DROPBLNKLINE=HEADING is not supported with:

Different border styles between the heading and the column titles or the data and the
footing.

Reports that use the ACROSS sort phrase.

Usage Considerations:

In some reports, FOOTING BOTTOM requires the space added by the system-generated
blank line between the data and the footing in order to present the correct distance
between the sections. In these instances, the top of the FOOTING BOTTOM may slightly
overlap the bottom of the data grid. You can resolve this by adding a blank line to the
top of your footing.

Creating Reports With TIBCO® WebFOCUS Language

 1457

Removing Blank Lines From a Report

Applying borders for the entire report (TYPE=REPORT) is recommended to avoid certain
known issues that arise when bordering report elements individually. In some reports
that define backcolor and borders on only select elements, the backcolor applied to the
heading is presenting with a different width than the backcolor applied to the column
titles. This difference causes a ragged right edge to present between the headings and
the titles. Additionally, if you can define the color of the border (BORDER-COLOR) for
elements with backcolor to match the backcolor, the borders will blend into the
backcolor and not be visible.

Example:

Comparing DROPBLNKLINE Parameter Settings

The following request against the GGSALES data source has a heading, a footing, and a
subtotal. Initially, DROPBLNKLINE is set to OFF.

TABLE FILE GGSALES
HEADING CENTER
"Gotham Grinds Sales By Region"
FOOTING CENTER
"Generated on: &DATETMDYY"
SUM DOLLARS UNITS
BY REGION SUBTOTAL
BY CATEGORY
BY PRODUCT
WHERE REGION EQ 'Northeast' OR 'West'
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET DROPBLNKLINE OFF
ON TABLE SET PAGE NOPAGE
ON TABLE SET STYLE *
SQUEEZE = ON,
FONT = ARIAL,
TYPE=HEADING, BORDER=LIGHT,
$
ENDSTYLE
END

1458

The output has a blank line below the heading, above the footing, and above and below the
subtotal lines and the grand total line.

21. Laying Out the Report Page

Creating Reports With TIBCO® WebFOCUS Language

 1459

Removing Blank Lines From a Report

Changing the DROPBLNKLINE setting to HEADING produces the following output. The blank line
below the heading and the blank line above the footing have been removed. The blank lines
above and below the subtotal and grand total lines are still inserted.

1460

21. Laying Out the Report Page

Changing the DROPBLNKLINE setting to ON (or BODY) produces the following output in which
the blank lines above and below the subtotal and grand total lines have been removed, but the
blank lines below the heading and above the footing are still inserted.

Creating Reports With TIBCO® WebFOCUS Language

 1461

Adding an Image to a Report

Changing the DROPBLNKLINE setting to ALL produces the following output in which the blank
lines around the subtotal and grandtotal lines as well as the blank lines below the heading and
above the footing have been removed.

Adding an Image to a Report

With a StyleSheet you can add and position an image in a report. An image, such as a logo,
gives corporate identity to a report, or provides visual appeal. You can add more than one
image by creating multiple declarations.

You can also add an image as background to a report. A background image is tiled or
repeated, covering the entire area on which the report displays. An image attached to an entire
report, or an image in a heading or footing, can appear with a background image.

Images must exist in a file format your browser supports, such as GIF (Graphic Interchange
Format) or JPEG (Joint Photographic Experts Group, .jpg extension).

1462

21. Laying Out the Report Page

Image support with WebFOCUS standard reporting formats

GIF and JPG images are supported in DHTML, HTML, PDF, PS, PPTX, XLSX, and PPT
standard report formats. JPEG images are only supported with HTML standard report
format. For other report formats, you can change the extension of the image name
from .jpeg to .jpg, and the image will be displayed in the report output.

PNG images are supported with DHTML, HTML, PPTX, and PDF standard report formats,
while WebFOCUS generated SVG charts will display when inserted in HTML, PDF, and PS
report formats.

SVG images are supported only with HTML reports.

Center and right justification of images in PDF reports is only reflected if the
JUSTIFY=CENTER or JUSTIFY=RIGHT StyleSheet attribute is explicitly set on the image
declaration attribute. By default, if JUSTIFY is not specified in the image declaration
attribute, the image is left justified.

Images are not supported in EXL2K standard report format.

Image support in Compound Report syntax

GIF and JPG images are supported in DHTML, PDF, PPTX, and PPT Compound document
syntax. JPEG images are not supported with any reporting format, but the images will work
in these compound formats if the extension is changed from .jpeg to .jpg.

PNG images are supported with DHTML, PPT, PPTX, and PDF Compound documents.

SVG images are not supported with any WebFOCUS reporting format in Compound
documents, while WebFOCUS generated SVG charts are supported only with PDF
Compound documents.

Images are not supported in EXL2K Compound documents.

Note: Images in report components in Compound documents are supported as described
under Image support with WebFOCUS standard reporting formats. This section, Image support in
Compound Report syntax, refers to images inserted in the PAGELAYOUT sections of the
Compound syntax.

For PDF, HTML, and DHTML output against data sources that support the Binary Large Object
(BLOB) data type (Microsoft SQL Server, DB2, Oracle, Informix, and PostgreSQL, using its
BYTEA data type), an image can be stored in a BLOB field in the data source.

The image must reside on the WebFOCUS Reporting Server in a directory named on EDAPATH
or APPPATH. If the file is not on the search path, supply the full path name.

Creating Reports With TIBCO® WebFOCUS Language

 1463

Adding an Image to a Report

Note: For JPEG files, currently only the .jpg extension is supported. The .jpeg extension is not
supported.

Reference: Browser and Device Support for Images in HTML Documents

Support for presenting images and graphs in HTML and DHTML formatted standard reports and
compound documents is provided using an image embedding facility that allows 64-bit images
to be encoded within a generated .htm file.

The SET HTMLEMBEDIMG command is designed to ensure that all WebFOCUS reports
containing images can be accessed from any browser or device. By default, it is set to ON and
embeds images within an .htm file.

SET HTMLEMBEDIMG={ON|OFF|AUTO}

where:

ON

Encodes images within the .htm file. ON is the default value, and overrides the
HTMLARCHIVE settings.

OFF

Does not embed the image. If HTMLARCHIVE is set to ON, .mht files are generated.

AUTO

Determines which encoding algorithm to use, based on the browser of the client machine
that submits the report request. Where the browser is identified as an Internet Explorer
browser, or the browser is unknown (such as reports distributed by ReportCaster),
WebFOCUS will continue to generate Web Archive files (.mht). For all other browsers,
WebFOCUS will encode the image into an HTML file (.htm).

Usage Notes for HTMLEMBEDIMG

When HTMLEMBEDIMG is set to ON (the default setting) and HTMLARCHIVE is set to ON,
the HTMLEMBEDIMG ON setting overrides the HTMLARCHIVE ON setting, and an .htm file,
in which the image is embedded, is generated.

When HTMLEMBEDIMG is set to ON (the default setting) and HTMLARCHIVE is set to OFF,
an .htm file is generated and the image is embedded.

Setting HTMLEMBEDIMG to OFF and enabling HTMLARCHIVE generates an .mht file, which
contain the encoded image.

When HTMLEMBEDIMG and HTMLARCHIVE are set to OFF, an .html file is generated, but
the image is not embedded.

1464

21. Laying Out the Report Page

The encoding algorithm that uses 64-bit encoding supported for images less than 32K in
size is supported by Internet Explorer 8. For Internet Explorer 8, Information Builders
recommends continuing to use the .mht format generated by HTMLARCHIVE. In Internet
Explorer 9 and higher and browsers other than Internet Explorer, the new algorithm is
supported for images of any size. See the browser vendor information to confirm 64-bit
encoding support.

Reference: Image Attributes

Attribute

IMAGE

IMAGEALIGN

POSITION

IMAGEBREAK

SIZE

ALT

PRESERVERATIO

Description

Adds an image.

Positions an image. This applies only to HTML reports.

Positions an image.

Controls generation of a line break after an image. This applies
only to HTML reports without internal cascading style sheets.

Sizes an image.

Supplies a description of an image for compliance with Section
accessibility (Workforce Investment Act of 1998). ALT only
applies to HTML reports.

ON specifies that the aspect ratio (ratio of height to width) of
the image should be preserved when it is scaled to the
specified SIZE. This avoids distorting the appearance of the
image. The image is scaled to the largest size possible within
the bounds specified by SIZE for which the aspect ratio can be
maintained. Supported for images in PDF and PostScript report
output.

BACKIMAGE

Adds a background image.

Creating Reports With TIBCO® WebFOCUS Language

 1465

Adding an Image to a Report

Syntax:

How to Add an Image to an HTML Report

This syntax applies to an HTML report. For details on adding an image to a PDF, PS, or HTML
report with an internal CSS, see How to Add an Image to a PDF, PS, or HTML Report With an
Internal Cascading Style Sheet on page 1476.

TYPE={REPORT|heading}, IMAGE={url|(column)} [,IMAGEALIGN=position]
     [,IMAGEBREAK={ON|OFF}] [,ALT='description'], $

where:

REPORT

Embeds an image in the body of a report. REPORT is the default value.

Note: The IMAGE=(column) option is not supported with TYPE=REPORT.

heading

Embeds an image in a heading or footing. Valid values are TABHEADING, TABFOOTING,
HEADING, FOOTING, SUBHEAD, and SUBFOOT.

url

Is the URL for the image file. The image must exist in a separate file in a format that your
browser supports, such as GIF or JPEG (.jpg). The file can be on your local web server, or
on any server accessible from your network. For details, see Specifying a URL on page
1467.

column

Is an alphanumeric field in a request (for example, a display field or a BY field) whose
value is a URL that points to an image file. Specify a value using the COLUMN attribute
described in Identifying a Report Component in a WebFOCUS StyleSheet on page 1249.
Enclose column in parentheses.

This option enables you to add different images to a heading or footing, depending on the
value of the field.

IMAGEALIGN = position

Is the position of the image.

Note: IMAGEALIGN is not supported with HTMLCSS=ON. With HTMLCSS=ON, you can
position images within a heading or footing by using the POSITION attribute to specify a
position relative to the upper-left corner of the heading or footing. For more information
about the POSITION attribute, see How to Add an Image to a PDF, PS, or HTML Report With
an Internal Cascading Style Sheet on page 1476.

1466

21. Laying Out the Report Page

Valid values are:

TOP where the top right corner of the image aligns with heading or footing text. If the image
is attached to the entire report, it appears on top of the report.

MIDDLE where the image appears in the middle of the heading or footing text. If the image
is attached to the entire report, it appears in the middle of the report.

BOTTOM where the bottom right corner of the image aligns with heading or footing text. If
the image is attached to the entire report, it appears at the bottom of the report.

LEFT where the image appears to the left of heading or footing text. If the image is
attached to the entire report, it appears to the left of the report.

RIGHT where the image appears to the right of heading or footing text. If the image is
attached to the entire report, it appears to the right of the report.

IMAGEBREAK

Controls generation of a line break after the image. Valid values are:

ON which generates a line break after the image so that an element following it (such as,
report heading text) appears on the next line.

OFF which suppresses a line break after the image so that an element following it is on
the same line. OFF is the default value.

description

Is a textual description of an image for compliance with Section 508 accessibility. Enclose
the description in single quotation marks.

Reference: Specifying a URL

The following guidelines are the same for IMAGE=url and IMAGE=(column) syntax. In the latter
case, they apply to a URL stored in a data source field.

Specify a URL by:

Supplying an absolute or relative address that points to an image file, for example:

TYPE=TABHEADING,IMAGE=http://www.ibi.com/images/logo_wf3.gif,$
TYPE=TABHEADING, IMAGE=/ibi_apps/ibi_html/ggdemo/gotham.gif,$

Using the SET BASEURL parameter to establish a URL that is logically prefixed to all
relative URLs in the request. With this feature, you can add an image by specifying just its
file name in the IMAGE attribute. For example:

Creating Reports With TIBCO® WebFOCUS Language

 1467

Adding an Image to a Report

SET BASEURL=http://host:port/
.
.
.
TYPE=REPORT, IMAGE=gotham.gif,$

The following apply:

A base URL must end with a slash (/).

An absolute URL (which begins with http://) overrides a base URL.

A URL is case-sensitive when referring to a UNIX server.

If the name of the image file does not contain an extension, .GIF is used.

Example:

Adding a GIF Image to an HTML Report Heading

This request adds the Gotham Grinds logo to a report heading. The logo is in a separate image
file identified by a relative URL in the IMAGE attribute.

TABLE FILE GGORDER
ON TABLE SUBHEAD
"PRODUCTS ORDERED ON 08/01/96"
SUM QUANTITY AS 'Ordered Units' BY PRODUCT
WHERE PRODUCT EQ 'Coffee Grinder' OR 'Coffee Pot'
WHERE ORDER_DATE EQ '08/01/96'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=TABHEADING, IMAGE=/IBI_APPS/IBI_HTML/GGDEMO/GOTHAM.GIF, IMAGEBREAK=ON,
$
ENDSTYLE
END

1468

IMAGEBREAK, set to ON, generates a line break between the logo and the heading text:

21. Laying Out the Report Page

Example:

Creating a Report Heading With an Embedded JPEG Image

TABLE FILE EMPLOYEE
ON TABLE SUBHEAD
"Employee Salary Information and Courses"
" "
" "
" "
" "
" "
" "
" "
" "
" "
PRINT CURR_SAL BY COURSE_NAME
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=TABHEADING, IMAGE=C:\IBI\APPS\IMAGES\Pencils.jpg,
POSITION=(.5 .5), SIZE=(.5 .5), $
ENDSTYLE
END

Note: The image used in this request is not distributed with WebFOCUS.

Creating Reports With TIBCO® WebFOCUS Language

 1469

Adding an Image to a Report

The output is:

1470

Example:

Using a File Name in a Data Source Field in an HTML Report

The following illustrates how to embed an image in a SUBHEAD, and use a different image for
each value of the BY field on which the SUBHEAD occurs.

21. Laying Out the Report Page

DEFINE FILE CAR
FLAG/A12=
DECODE COUNTRY ( 'ENGLAND' 'uk' 'ITALY' 'italy'
   'FRANCE' 'france' 'JAPAN' 'japan' );
END

TABLE FILE CAR
PRINT FLAG NOPRINT AND MODEL AS '' BY COUNTRY NOPRINT AS '' BY CAR AS ''
WHERE COUNTRY EQ 'ENGLAND' OR 'FRANCE' OR 'ITALY' OR 'JAPAN'
ON COUNTRY SUBHEAD
"                     <+0>Cars produced in <ST.COUNTRY"
HEADING CENTER
"Car Manufacturer Report"
" "
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=SUBHEAD, IMAGE=(FLAG), $
TYPE=REPORT, GRID=OFF, $
TYPE=HEADING, SIZE=12, STYLE=BOLD, $
TYPE=SUBHEAD, STYLE=BOLD, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1471

Adding an Image to a Report

The output is:

1472

Example:

Supplying an Image Description Using the ALT Attribute

21. Laying Out the Report Page

This request adds the Information Builders logo to a report footing. It uses the WebFOCUS
StyleSheet ALT attribute to add descriptive text (Information Builders logo) that identifies the
image.

TABLE FILE GGORDER
SUM QUANTITY AS 'Ordered Units'
BY PRODUCT
ON TABLE SUBHEAD
"PRODUCTS ORDERED"
FOOTING
" "
ON TABLE SET ACCESSHTML 508
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF,$
TYPE=FOOTING, IMAGE=/ibi_html/iblogo.gif, ALT='Information Builders logo',$
ENDSTYLE
END

Note: If the request is located in the WebFOCUS repository and the WebFOCUS Client Upload
Images to be Embedded in Reports Applications setting is selected, you need to either:

Include the -MRNOEDIT command at the beginning of the line that references the IMAGE
not located in the WebFOCUS repository.

Include the fully qualified path in the IMAGE parameter.

The WebFOCUS Client Upload Images to be Embedded in Reports Applications setting specifies
whether to upload Repository images to the Reporting Server for embedding in reports and
HTML pages. The default is to upload Repository images. For more information on the Upload
Images to be Embedded in Reports Applications setting, see the Security and Administration
manual.

The -MRNOEDIT command instructs the WebFOCUS Client to not process the line of code. For
more information on the -MRNOEDIT command, see the Business Intelligence Portal manual.

Creating Reports With TIBCO® WebFOCUS Language

 1473

Adding an Image to a Report

When you run the request, the image displays below the report data, as shown in the following
image.

When you hover the mouse over the image, the descriptive text displays in a box if your
browser image loader is turned off or if the browser does not display images.

WebFOCUS generates the following HTML code for the image:

<IMG SRC="/ibi_html/ibilogo.gif"
ALT="Information Builders logo">

Syntax:

How to Add a Background Image

This syntax applies to an HTML report.

[TYPE=REPORT,] BACKIMAGE=url, $

where:

TYPE=REPORT

Applies the image to the entire report. Not required, as it is the default.

1474

21. Laying Out the Report Page

url

Is the URL of a GIF or JPEG file (.jpg). Specify a file on your local web server, or on a server
accessible from your network.

The URL can be an absolute or relative address. See Image Attributes on page 1465.

When specifying a GIF file, you can omit the file extension.

Example:

Adding a Background Image

This request adds a background image to a report. The image file CALM_BKG.GIF resides in
the relative address shown.

TABLE FILE GGSALES
SUM UNITS DOLLARS
BY CATEGORY BY PRODUCT
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, STYLE=BOLD, GRID=OFF, $
TYPE=REPORT, BACKIMAGE=/IBI_APPS/IBI_HTML/TEMPLATE/CALM_BKG.GIF, $
ENDSTYLE
END

The background is tiled across the report area:

Creating Reports With TIBCO® WebFOCUS Language

 1475

Adding an Image to a Report

Syntax:

How to Add an Image to a PDF, PS, or HTML Report With an Internal Cascading Style
Sheet

This syntax applies to a PDF, PS, or HTML report with an internal cascading style sheet. The
image can be in a separate file.

A report with an Internal cascading style sheet is an HTML page with an HTML cascading style
sheet (CSS) stored between the style tags within the HTML document.

TYPE={REPORT|heading}, IMAGE={url|file|(column)} [,BY=byfield]
[,POSITION=([+|-]x [+|-]y )] [,SIZE=(w h)] ,$

where:

REPORT

Embeds an image in the body of a report. The image appears in the background of the
report. REPORT is the default value.

heading

Embeds an image in a heading or footing. Valid values are TABHEADING, TABFOOTING,
FOOTING, HEADING, SUBHEAD, and SUBFOOT.

Provide sufficient blank space in the heading or footing so that the image does not overlap
the heading or footing text. Also, you may want to place heading or footing text to the right
of the image using spot markers or the POSITION attribute in the StyleSheet.

url

HTML report with internal cascading style sheet:

Is the absolute or relative address for the image file. The image must exist in a separate
file in a format that your browser supports, such as GIF or JPEG (.jpg). The file can be on
your local web server, or on any server accessible from your network. For details, see
Specifying a URL on page 1467.

file

PDF or PS report:

Is the name of the image file. It must reside on the WebFOCUS Reporting Server in a
directory named on EDAPATH or APPPATH. If the file is not on the search path, supply the
full path name.

When specifying a GIF file, you can omit the file extension.

1476

21. Laying Out the Report Page

column

Is an alphanumeric field in the data source that contains the name of an image file. Use
the COLUMN attribute described in Identifying a Report Component in a WebFOCUS
StyleSheet on page 1249. Enclose column in parentheses.

The field containing the file name or image must be a display field or BY field referenced in
the request.

Note that the value of the field is interpreted exactly as if it were typed as the URL of the
image in the StyleSheet. If you omit the suffix, .GIF is supplied by default. SET BASEURL
can be useful for supplying the base URL of the images. If you do that, the value of the
field does not have to include the complete URL.

This syntax is useful, for example, if you want to embed an image in a SUBHEAD, and you
want a different image for each value of the BY field on which the SUBHEAD occurs.

byfield

Is the sort field that generated the subhead or subfoot.

POSITION

Is the starting position of the image.

+|-

x

y

Measures the horizontal or vertical distance from the upper-left corner of the report
component in which the image is embedded.

Is the horizontal starting position of the image from the upper-left corner of the physical
report page, expressed in the unit of measurement specified by the UNITS parameter.

Enclose the x and y values in parentheses. Do not include a comma between them.

Is the vertical starting position of the image from the upper-left corner of the physical
report page, expressed in the unit of measurement specified by the UNITS parameter.

SIZE

Is the size of the image. By default, an image is added at its original size.

Creating Reports With TIBCO® WebFOCUS Language

 1477

Adding an Image to a Report

w

h

Is the width of the image, expressed in the unit of measurement specified by the UNITS
parameter.

Enclose the w and h values in parentheses. Do not include a comma between them.

Is the height of the image, expressed in the unit of measurement specified by the UNITS
parameter.

Example:

Adding a GIF Image to an HTML Report With Internal Cascading Style Sheet

A URL locates the image file GOTHAM.GIF on a server named WEBSRVR1. The TYPE attribute
adds the image to the report heading. POSITION places the image one-quarter inch horizontally
and one-tenth inch vertically from the upper-left corner of the report page. The image is one
inch wide and one inch high as specified by SIZE.

SET HTMLCSS = ON
TABLE FILE GGSALES
SUM UNITS BY PRODUCT
ON TABLE SUBHEAD
"REPORT ON UNITS SOLD"
" "
" "
" "
" "
" "
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=TABHEADING, IMAGE=HTTP://WEBSRVR1/IBI_APPS/IBI_HTML/GGDEMO/GOTHAM.GIF,
     POSITION=(.25 .10), SIZE=(1 1), $
ENDSTYLE
END

1478

The company logo is positioned and sized in the report heading:

21. Laying Out the Report Page

Example:

Adding a GIF Image to a PDF Report

The image file for this example is GOTHAM.GIF. The POSITION attribute places the image one-
quarter inch horizontally and one-quarter vertically from the upper-left corner of the report page.
The image is one-half inch wide and one-half inch high as specified by SIZE.

SET ONLINE-FMT = PDF
TABLE FILE GGSALES
SUM UNITS BY PRODUCT
ON TABLE SUBHEAD
"Report on Units Sold"
" "
" "
" "
" "
" "
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=TABHEADING, IMAGE=GOTHAM.GIF, POSITION=(.25 .25), SIZE=(.5 .5), $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1479

Adding an Image to a Report

The report is:

Example:

Adding a PNG Image to a PDF Report

The image file for this sample is Ibi_logo.png. The POSITION attribute places the image to the
upper-left corner of the report page. The image is one inch wide and half an inch high, as
specified by SIZE.

SET HTMLCSS = ON
TABLE FILE GGSALES
SUM UNITS BY PRODUCT
ON TABLE SUBHEAD
"REPORT ON UNITS SOLD"
" "
" "
" "
" "
" "
ON TABLE SET PAGE-NUM OFF
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=TABHEADING, IMAGE=Ibi_logo.png, POSITION=(0 .30), SIZE=(1 0.5), $
ENDSTYLE
END

1480

The report is:

21. Laying Out the Report Page

Syntax:

How to Add an Image From a BLOB Field to a PDF, DHTML, or HTML Report

For PDF, HTML, and DHTML output against data sources that support the Binary Large Object
(BLOB) data type (Microsoft SQL Server, DB2, Oracle, Informix, and PostgreSQL using its
BYTEA data type), an image can be stored in a BLOB field in the data source.

WebFOCUS StyleSheets used to produce report output in PDF, HTML, or DHTML format can
access a BLOB field as an image source when an instance of the BLOB field contains an exact
binary copy of a GIF or JPG image. HTML and DHTML reports also support PNG images. Images
of different formats (GIF, JPG, PNG) can be mixed within the same BLOB field. WebFOCUS can
determine the format from the header of the image. The image can be inserted in report
columns, headings, footings, subheadings, and subfootings.

The BLOB field must be referenced in a PRINT or LIST command in the request (aggregation is
not supported). Reports containing BLOB images are supported as components in Coordinated
Compound Reports.

With the following SET commands, BLOB images will work for both HTML and DHTML in all
browsers:

SET HTMLEMBEDIMG=AUTO.

SET HTMLARCHIVE=ON (required to support Internet Explorer with images larger than 32K).

SET BASEURL='' (required to make embedded images work as it overrides the default
setting sent from the WebFOCUS Client).

Creating Reports With TIBCO® WebFOCUS Language

 1481

Adding an Image to a Report

SET HTMLCSS=ON (required for image positioning in subheads in HTML reports). Setting
HTMLCSS=ON creates an HTML report with an Internal cascading style sheet. A report with
an Internal cascading style sheet is an HTML page with an HTML cascading style sheet
(CSS) stored between the style tags within the HTML document.

TYPE={REPORT|heading}, IMAGE={url|file|(column)} [,BY=byfield]
[,POSITION=([+|-]x [+|-]y )] [,SIZE=(w h)] [,PRESERVERATIO={ON|OFF}],$

TYPE=DATA, COLUMN=imagefield, IMAGE=(imagefield), SIZE=(wh)
[,PRESERVERATIO={ON|OFF}] ,$

where:

REPORT

Embeds an image in the body of a report. The image appears in the background of the
report. REPORT is the default value (not supported for images stored in BLOB fields, which
are supported for PDF output).

heading

Embeds an image in a heading or footing. Valid values are FOOTING, HEADING, SUBHEAD,
and SUBFOOT.

If the image is to be embedded in a heading, subheading, footing, or subfooting rather
than a column, the StyleSheet declaration is responsible for placing the image in the
heading, subheading, footing, or subfooting. To make the BLOB image accessible to the
StyleSheet, the BLOB field must be referenced in the PRINT or LIST command with the
NOPRINT option. Do not reference the BLOB field name in the heading or footing itself.

Provide sufficient blank space in the heading or footing so that the image does not overlap
the heading or footing text. Also, you may want to place heading or footing text to the right
of the image using spot markers or the POSITION attribute in the StyleSheet.

file

Is the name of the image file. It must reside on the WebFOCUS Reporting Server in a
directory named on EDAPATH or APPPATH. If the file is not on the search path, supply the
full path name.

When specifying a GIF file, you can omit the file extension.

1482

21. Laying Out the Report Page

column

Is a BLOB field in the data source that contains an exact binary copy of a GIF or JPG
image. HTML and DHTML formats also support images in PNG format. Images of different
formats (GIF, JPG, PNG) can be mixed within the same BLOB field. WebFOCUS can
determine the format from the header of the image. The image can be inserted in report
columns, headings, footings, subheadings and subfootings. Use the COLUMN attribute
described in Identifying a Report Component in a WebFOCUS StyleSheet on page 1249.
Enclose column in parentheses.

The field containing the file name or image must be a display field or BY field referenced in
the request.

byfield

Is the sort field that generated the subhead or subfoot.

imagefield

Is any valid column reference for the BLOB field that contains the image. Note that the
BLOB field must be referenced in a PRINT or LIST command in the request.

If omitted, the default size is 1 inch by 1 inch. The width of the column and the spacing
between the lines is automatically adjusted to accommodate the image.

POSITION

Is the starting position of the image.

+|-

x

y

Measures the horizontal or vertical distance from the upper-left corner of the report
component in which the image is embedded.

Is the horizontal starting position of the image from the upper-left corner of the physical
report page, expressed in the unit of measurement specified by the UNITS parameter.

Enclose the x and y values in parentheses. Do not include a comma between them.

Is the vertical starting position of the image from the upper-left corner of the physical
report page, expressed in the unit of measurement specified by the UNITS parameter.

SIZE

Is the size of the image. By default, an image is added at its original size. Note that
images stored in BLOB fields are supported only for PDF, HTML, and DHTML output.

Creating Reports With TIBCO® WebFOCUS Language

 1483

Adding an Image to a Report

w

h

Is the width of the image, expressed in the unit of measurement specified by the UNITS
parameter.

Enclose the w and h values in parentheses. Do not include a comma between them.

Is the height of the image, expressed in the unit of measurement specified by the UNITS
parameter.

If SIZE is omitted, the original dimensions of the image are used (any GIF, JPG, or PNG
image has an original, unscaled size based on the dimensions of its bitmap).

[PRESERVERATIO={ON|OFF}]

Not supported for images in PNG format. PRESERVERATIO=ON specifies that the aspect
ratio (ratio of height to width) of the image should be preserved when it is scaled to the
specified SIZE. This avoids distorting the appearance of the image. The image is scaled to
the largest size possible within the bounds specified by SIZE for which the aspect ratio can
be maintained. Supported for PDF and PS output. OFF does not maintain the aspect ratio.
OFF is the default value.

The actual size of an image stored in a BLOB field may vary from image to image, and
scaling the images to a designated size allows them to better fit into a columnar report.
Note: Images stored in a BLOB field are supported only for PDF, HTML, and DHTML output.

Example:

Inserting an Image From a BLOB Field Into a Report Column

The Microsoft SQL Server data source named retaildetail contains product information for a
sports clothing and shoe retailer. The Microsoft SQL Server data source named retailimage
has the same product ID field as retaildetail and has an image of each product stored in a
field named prodimage whose data type is BLOB.

1484

21. Laying Out the Report Page

The following Master File describes the Microsoft SQL Server data source named retaildetail.

FILENAME=RETAILDETAIL, SUFFIX=SQLMSS  , $
  SEGMENT=SEG01, SEGTYPE=S0, $
    FIELDNAME=FOCLIST, ALIAS=FOCLIST, USAGE=I5, ACTUAL=I4, $
    FIELDNAME=PRODUCTID, ALIAS=ProductId, USAGE=A5, ACTUAL=A5,
      MISSING=ON, $
    FIELDNAME=DEPARTMENT, ALIAS=Department, USAGE=A10, ACTUAL=A10,
      MISSING=ON, $
    FIELDNAME=CATEGORY, ALIAS=Category, USAGE=A30, ACTUAL=A30,
      MISSING=ON, $
    FIELDNAME=SPORTS, ALIAS=Sports, USAGE=A30, ACTUAL=A30,
      MISSING=ON, $
    FIELDNAME=GENDER, ALIAS=Gender, USAGE=A10, ACTUAL=A10,
      MISSING=ON, $
    FIELDNAME=BRAND, ALIAS=Brand, USAGE=A25, ACTUAL=A25,
      MISSING=ON, $
    FIELDNAME=STYLE, ALIAS=Style, USAGE=A25, ACTUAL=A25,
      MISSING=ON, $
    FIELDNAME=COLOR, ALIAS=Color, USAGE=A25, ACTUAL=A25,
      MISSING=ON, $
    FIELDNAME=NAME, ALIAS=Name, USAGE=A80, ACTUAL=A80,
      MISSING=ON, $
    FIELDNAME=DESCRIPTION, ALIAS=Description, USAGE=A1000, ACTUAL=A1000,
      MISSING=ON, $
    FIELDNAME=PRICE, ALIAS=Price, USAGE=D7.2, ACTUAL=D8,
      MISSING=ON, $

The following Master File describes the Microsoft SQL Server data source named retailimage,
which has the same product ID field as retaildetail and has an image of each product stored in
a field named prodimage whose data type is BLOB.

FILENAME=RETAILIMAGE, SUFFIX=SQLMSS  , $
  SEGMENT=RETAILIMAGE, SEGTYPE=S0, $
    FIELDNAME=PRODUCTID, ALIAS=PRODUCTID, USAGE=A5, ACTUAL=A5, $
    FIELDNAME=PRODIMAGE, ALIAS=F02BLOB50000, USAGE=BLOB, ACTUAL=BLOB,
      MISSING=ON, $

Creating Reports With TIBCO® WebFOCUS Language

 1485

Adding an Image to a Report

The following request joins the two data sources and prints product names and prices with the
corresponding image. The output is generated in DHTML format.

-* Rel 7705 DHTML and HTML supports including Image stored in
-* BLOB field in report column, heading, footing, subhead, or
-* subfoot
-* Rel 769 supports PDF format
JOIN PRODUCTID IN RETAILDETAIL TO PRODUCTID IN RETAILIMAGE
TABLE FILE RETAILDETAIL
HEADING CENTER
"Product List"
" "
PRINT NAME/A20 PRICE PRODIMAGE AS 'PICTURE'
BY PRODUCTID NOPRINT
BY NAME NOPRINT
ON NAME UNDER-LINE
ON TABLE SET PAGE NOPAGE
-**************************
-* Lines between asterisk lines required for BLOB image support
-* for HTML and DHTML formats.
ON TABLE SET HTMLEMBEDIMG AUTO
-* Required to support IE8 with images larger than 32K
ON TABLE SET HTMLARCHIVE ON
-*Required for image positioning in subheads in HTML reports
ON TABLE SET HTMLCSS ON
-**************************
ON TABLE PCHOLD FORMAT DHTML
ON TABLE SET STYLE *
TYPE=REPORT,COLOR=BLUE,FONT=ARIAL, GRID=OFF,$
TYPE=HEADING, SIZE = 18, COLOR=RED,$
TYPE=DATA,COLUMN=PRODIMAGE,IMAGE=(PRODIMAGE),SIZE=(1 1),$
ENDSTYLE
END

The image is placed in the report column using the following StyleSheet declaration, which
names the image field, and establishes the size and position in the column for the image.

TYPE=DATA,COLUMN=PRODIMAGE,IMAGE=(PRODIMAGE),SIZE=(1 1),$

1486

The partial output shows that DHTML format preserves the specified spacing.

21. Laying Out the Report Page

Creating Reports With TIBCO® WebFOCUS Language

 1487

Adding an Image to a Report

The following request generates the output in HTML format.

-* Rel 7705 DHTML and HTML supports including Image stored in
-* BLOB field in report column, heading, footing, subhead, or
-* subfoot
-* Rel 769 supports PDF format
JOIN PRODUCTID IN RETAILDETAIL TO PRODUCTID IN RETAILIMAGE
TABLE FILE RETAILDETAIL
HEADING CENTER
"Product List"
" "
PRINT NAME/A20 PRICE PRODIMAGE AS 'PICTURE'
BY PRODUCTID NOPRINT
BY NAME NOPRINT
ON NAME UNDER-LINE
ON TABLE SET PAGE NOPAGE
-**************************
-* Lines between asterisk lines required for BLOB image support
-* for HTML and DHTML formats.
ON TABLE SET HTMLEMBEDIMG AUTO
-* Required to support IE8 with images larger than 32K
ON TABLE SET HTMLARCHIVE ON
-*Required for image positioning in subheads in HTML reports
ON TABLE SET HTMLCSS ON
-**************************
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET STYLE *
TYPE=REPORT,COLOR=BLUE, GRID=OFF, FONT=ARIAL,$
TYPE=HEADING, SIZE = 18, COLOR=RED,$
TYPE=DATA,COLUMN=PRODIMAGE,IMAGE=(PRODIMAGE),SIZE=(1 1),$
ENDSTYLE
END

1488

The partial output shows that the spacing is different because the browser removes blank
spaces for HTML report output.

21. Laying Out the Report Page

Creating Reports With TIBCO® WebFOCUS Language

 1489

Adding an Image to a Report

The following request generates the report output in PDF format.

-* Rel 7705 DHTML and HTML supports including Image stored in
-* BLOB field in report column, heading, footing, subhead, or
-* subfoot
-* Rel 769 supports PDF format
JOIN PRODUCTID IN RETAILDETAIL TO PRODUCTID IN RETAILIMAGE
TABLE FILE RETAILDETAIL
HEADING CENTER
"Product List"
" "
PRINT NAME/A20 PRICE PRODIMAGE AS 'PICTURE'
BY PRODUCTID NOPRINT
BY NAME NOPRINT
ON NAME UNDER-LINE
ON TABLE SET PAGE NOPAGE
-**************************
-* Lines between asterisk lines required for BLOB image support
-* for HTML and DHTML formats.
ON TABLE SET HTMLEMBEDIMG AUTO
-* Required to support IE8 with images larger than 32K
ON TABLE SET HTMLARCHIVE ON
-*Required for image positioning in subheads in HTML reports
ON TABLE SET HTMLCSS ON
-**************************
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT,COLOR=BLUE, GRID=OFF,$
TYPE=HEADING, SIZE = 18, FONT = ARIAL, COLOR=RED,$
TYPE=DATA,COLUMN=PRODIMAGE,IMAGE=(PRODIMAGE),SIZE=(1 1),$
ENDSTYLE
END

1490

The PDF partial output preserves specified spacing providing results similar to DHTML output.

21. Laying Out the Report Page

Creating Reports With TIBCO® WebFOCUS Language

 1491

Adding an Image to a Report

Example:

Inserting an Image From a BLOB Field Into a Subheading

The Microsoft SQL Server data source named retaildetail contains product information for a
sports clothing and shoe retailer. The Microsoft SQL Server data source named retailimage
has the same product ID field as retaildetail and has an image of each product stored in a
field named prodimage whose data type is BLOB.

The following request joins the two data sources and prints product images in a subheading.
The output is generated in DHTML format. It can also be generated in HTML or PDF format.

-* Rel 7705 DHTML and HTML supports including Image stored in
-* BLOB field in HTML report column, heading, footing, subhead,
-* or subfoot
-* Rel 769 supports PDF format
-*SET BASEURL='' - Required for embedded images to work. Overrides default
-* setting from WF Client.
SET BASEURL=''
JOIN PRODUCTID IN RETAILDETAIL TO PRODUCTID IN RETAILIMAGE
TABLE FILE RETAILDETAIL
HEADING CENTER
"Product Catalog"
" "
PRINT NAME NOPRINT PRODIMAGE NOPRINT
BY PRODUCTID NOPRINT
ON PRODUCTID SUBHEAD
""
" ID: <10<PRODUCTID "
" Name: <10<NAME "
" Price: <7<PRICE "
" Image: "
""
""
""
""
""
ON TABLE SET PAGE NOPAGE

-**************************
-* Lines between asterisk lines required for BLOB image support
-* for HTML and DHTML formats.
ON TABLE SET HTMLEMBEDIMG AUTO
-* Required to support IE8 with images larger than 32K
ON TABLE SET HTMLARCHIVE ON
-*Required for image positioning in subheads in HTML reports
ON TABLE SET HTMLCSS ON
-**************************
ON TABLE PCHOLD FORMAT DHTML
ON TABLE SET STYLE *
TYPE=REPORT,COLOR=BLUE,FONT = ARIAL,$
TYPE=HEADING, COLOR = RED, SIZE = 16, JUSTIFY=CENTER,$
TYPE=SUBHEAD,BY=PRODUCTID,IMAGE=(PRODIMAGE),SIZE=(1 1), POSITION=(+2 +1),$
ENDSTYLE
END

1492

The partial output is.

21. Laying Out the Report Page

Creating Reports With TIBCO® WebFOCUS Language

 1493

Adding an Image to a Report

Example:

Sizing an Image From a BLOB Field

The Microsoft SQL Server data source named retaildetail contains product information for a
sports clothing and shoe retailer. The Microsoft SQL Server data source named retailimage
has the same product ID field as retaildetail and has an image of each product stored in a
field named prodimage whose data type is BLOB.

The following request joins the two data sources and displays the same image on three
columns of output using different sizes and different PRESERVERATIO settings. Note that
PRESERVERATIO=ON is not supported with images in PNG format.

The output is generated in DHTML format. It can also be generated in HTML or PDF format.

-* Rel 7705 DHTML and HTML supports including Image stored in
-* BLOB field in report column, heading, footing, subhead, or
-* subfoot
-* Rel 769 supports PDF format
JOIN PRODUCTID IN RETAILDETAIL TO PRODUCTID IN RETAILIMAGE
TABLE FILE RETAILDETAIL
PRINT PRODIMAGE AS '' PRODIMAGE AS '' PRODIMAGE AS ''
BY STYLE NOPRINT
WHERE NAME CONTAINS 'Pant' OR 'Tank'
ON STYLE UNDER-LINE
ON TABLE SET PAGE NOPAGE
-**************************
-* Lines between asterisk lines required for BLOB image support
-* for HTML and DHTML formats.
ON TABLE SET HTMLEMBEDIMG AUTO
-* Required to support IE8 with images larger than 32K
ON TABLE SET HTMLARCHIVE ON
-*Required for image positioning in subheads in HTML reports
ON TABLE SET HTMLCSS ON
-**************************
ON TABLE PCHOLD FORMAT DHTML
ON TABLE SET STYLE *
TYPE=REPORT,COLOR=BLUE,FONT = ARIAL,$
TYPE=DATA,COLUMN=P1,IMAGE=(PRODIMAGE),SIZE=(.75 .75),$
TYPE=DATA,COLUMN=P2,IMAGE=(PRODIMAGE),SIZE=(.75 1),PRESERVERATIO=ON,$
TYPE=DATA,COLUMN=P3,IMAGE=(PRODIMAGE),SIZE=(.75 1),PRESERVERATIO=OFF,$
ENDSTYLE
END

Note that PRESERVERATIO=OFF is specified for the second column to preserve the image
height and width ratio for that column even though the styling SIZE height specifies a different
value than the first column image styling. In addition, PRESERVERATIO=OFF is specified for the
third column, so for that column the image height to width ratio is not preserved and is
rendered as specified by the styling SIZE height and width values specified in the request
(FEX).

1494

The partial output follows.

21. Laying Out the Report Page

Example:

Inserting an Image From a BLOB Field in a Summary Report

In order to insert an image from a BLOB field in a report that displays summary data, you must
include two display commands in the request, a SUM command for the summary information
and a PRINT or LIST command for displaying the image and any other detail data.

Creating Reports With TIBCO® WebFOCUS Language

 1495

Adding an Image to a Report

The Microsoft SQL Server data source named retaildetail contains product information for a
sports clothing and shoe retailer. The Microsoft SQL Server data source named retailimage
has the same product ID field as retaildetail and has an image of each product stored in a
field named prodimage whose data type is BLOB.

The following request joins the two data sources. It contains two display commands, a SUM
command and a PRINT command. The SUM command aggregates the total price for each
category and displays this category name and total price in a subheading, The PRINT command
displays the image for each item in the category along with its individual product number and
price in a subfooting.

The output is generated in DHTML format. It can also be generated in HTML or PDF format.

-* Rel 7705 DHTML and HTML supports including images stored in
-* BLOB field in report column, heading, footing, subhead, or
-* subfoot
-* Rel 769 supports PDF format
SET PRINTPLUS=ON
JOIN PRODUCTID IN RETAILDETAIL TO PRODUCTID IN RETAILIMAGE
TABLE FILE RETAILDETAIL
HEADING CENTER
"Product Price Summary"
" "
SUM PRICE NOPRINT
BY CATEGORY NOPRINT
ON CATEGORY SUBHEAD
" Category: <CATEGORY "
" Total Price: <PRICE "
" "

1496

21. Laying Out the Report Page

PRINT PRICE NOPRINT PRODIMAGE NOPRINT
BY CATEGORY NOPRINT
BY PRODUCTID NOPRINT
ON PRODUCTID SUBFOOT
" "
" "
" "
" "
" "
" "
" Product #: <PRODUCTID "
" Name: <NAME "
" Price: <FST.PRICE "
ON TABLE SET PAGE NOPAGE
-**************************
-* Lines between asterisk lines required for BLOB image support
-* for HTML and DHTML formats.
ON TABLE SET HTMLEMBEDIMG AUTO
-* Required to support IE8 with images larger than 32K
ON TABLE SET HTMLARCHIVE ON
-*Required for image positioning in subheads in HTML reports]
ON TABLE SET HTMLCSS ON
-**************************
ON TABLE PCHOLD FORMAT DHTML
ON TABLE SET STYLE *
TYPE=REPORT,COLOR=BLUE,FONT=ARIAL,$
TYPE=HEADING, COLOR=RED, SIZE=14, STYLE=BOLD, JUSTIFY=CENTER,$
TYPE=SUBHEAD, COLOR=RED, SIZE=12, STYLE=BOLD, JUSTIFY=CENTER,$
TYPE=SUBFOOT,BY=PRODUCTID,IMAGE=(PRODIMAGE),SIZE=(1 1), POSITION=(0 0),$
TYPE=SUBFOOT,BY=PRODUCTID,OBJECT=FIELD, ITEM=1, WRAP=5,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1497

Adding an Image to a Report

The output for the first category is:

1498

21. Laying Out the Report Page

Reference: File Size and Compression Considerations For Images in BLOB Fields

The actual size of an image stored in the BLOB field may vary from image to image, and
scaling the images to a designated size allows them to better fit into a columnar report.

Files that contain many images can be large. Scaling the images to a smaller size using the
SIZE attribute does not decrease the size of the file. Note also that using SET
FILECOMPRESS=ON will not reduce the size of images in a PDF file, since images are already
saved in compressed form.

Associating Bar Graphs With Report Data

To make PDF, HTML, DHTML, PPTX, PPT, and PS reports more powerful, you can insert visual
representations of selected data directly into the report output. These visual representations
are in the form of vertical or horizontal bar graphs that make relationships and trends among
data more obvious. You can add the following:

Vertical Bar Graph. You can apply a vertical bar graph to report columns associated with an
ACROSS sort field. The report output displays a vertical bar graph in a new row above the
associated data values, as shown in the following image.

Bar graphs that emanate above the zero line represent positive values, while bar graphs
that emanate below the zero line represent negative values.

To see how each of these types of reports is generated, see the example following How to
Associate Data Visualization Bar Graphs With Report Columns on page 1504.

Creating Reports With TIBCO® WebFOCUS Language

 1499

Associating Bar Graphs With Report Data

Horizontal Bar Graph. You can apply a horizontal bar graph to report columns. The report
output displays a horizontal bar graph in a new column to the right of the associated data
values, as shown in the following image.

Bar graphs that emanate to the right of the zero line represent positive values, while bar
graphs that emanate to the left of the zero line represent negative values.

The length of each vertical or horizontal bar graph is proportional to the magnitude of its
associated data value. The shortest bar graph is displayed for the value with the minimum
magnitude, the longest bar graph for the value with the maximum magnitude, and bar graphs
of varying length are displayed for each value within the minimum-maximum magnitude range.
Notice in the figure above that a value of 147,490.00 produces a longer horizontal bar graph
than a value of 50,153.00. Therefore, a complete row of vertical bar graphs or a complete
column of horizontal bar graphs forms a bar chart.

You can only apply data visualization bar graphs to numeric report columns (integer, decimal,
floating point single-precision, floating point double-precision, and packed). Bar graphs applied
to alphanumeric, date, or text field formats are ignored. For details about assigning field
formats, see the Describing Data With WebFOCUS Language manual.

1500

21. Laying Out the Report Page

You apply data visualization bar graphs to columns by adding a declaration to your WebFOCUS
StyleSheet that begins with the GRAPHTYPE attribute. This attribute adds either a vertical or
horizontal bar graph to the specified data.

Note: Data visualization bar graphs are not supported in a request that includes the OVER
option.

Reference: Formatting Options for Data Visualization Bar Graphs

You can specify optional formatting attributes for data visualization bar graphs in the
GRAPHTYPE declaration, for example, graph color, length, and width. The following table lists
the formatting attributes and a description of each:

Formatting Attribute

Description

GRAPHBASE

Sets whether the scale should start from zero or the minimum
value.

GRAPHCOLOR

Sets the color of the bar graphs.

GRAPHCOLORNEG

Sets a color for the bar graphs that represent negative values.

GRAPHLENGTH

GRAPHSCALE

GRAPHWIDTH

Sets the length of the longest bar graph. The value for
GRAPHLENGTH determines the length in measurement units
(inches, centimeters, and so on) of the longest bar graph in a
vertical or horizontal bar graph.

The length value is expressed in the current units, which is set
using the UNITS StyleSheet attribute. The GRAPHLENGTH value
is then converted into pixels.

Specifies the relative bar graph scaling for multiple report
columns under a common ACROSS sort field in which you have
applied data visualization graphics. GRAPHSCALE is a report-
level setting (TYPE=REPORT).

Sets the width of the bar graphs. The width value is expressed
in the current units. See GRAPHLENGTH, above, for more
information about units.

Creating Reports With TIBCO® WebFOCUS Language

 1501

Associating Bar Graphs With Report Data

Syntax:

How to Incorporate Data Visualization Formatting Attributes

TYPE=REPORT, [GRAPHSCALE={UNIFORM|DISTINCT}]
TYPE=DATA, GRAPHTYPE=DATA, [{COLUMN|ACROSSCOLUMN|FIELD}=identifier],
 [GRAPHBASE={ZERO|MINIMUM},]
 [GRAPHCOLOR={color|RGB({r g b|#hexcolor}},]
 [GRAPHNEGCOLOR={color|RGB({r g b|#hexcolor}},]
 [GRAPHLENGTH=lengthvalue,]
 [GRAPHWIDTH=widthvalue,] $

Note: TYPE=DATA, GRAPHTYPE=DATA is the equivalent of GRAPHTYPE=DATA.

where:

GRAPHBASE

Specifies whether the scale should start at zero (the default) or the minimum value.
GRAPHBASE=MINIMUM makes it easier to compare values that are not close to zero. If
negative values are present, GRAPHBASE=MINIMUM is ignored and will not be enabled.

GRAPHBASE=MINIMUM is visually indicated in the graph with a break in the bar (the small
piece of the bar before the break symbolizes the compressed space between 0 and the
minimum value).

Note: The minimum value is identified by a double bar of equal heights. For all values
greater than the minimum, the top bar grows proportionally taller. If the minimum value is
actually zero, having this double bar may make it look as if the minimum value is not zero.
Therefore, you should use the default (GRAPHBASE=ZERO) in your procedure if you expect
to have zero values in the column.

GRAPHCOLOR

Specifies the color of the bar graphs. Black is the default color, if you omit this attribute
from the declaration.

color

Is one of the supported color values. In addition to the supported named colors, HEX or
RGB color values are valid options. For a list of supported values, see Color Values in a
Report on page 1701.

RGB(r g b)

Specifies the font color using a mixture of red, green, and blue. (r g b) is the desired
intensity of red, green, and blue, respectively. The values are on a scale of 0 to 255,
where 0 is the least intense and 255 is the most intense. Note that using the three color
components in equal intensities results in shades of gray.

1502

21. Laying Out the Report Page

RGB(#hexcolor)

Is the hexadecimal value for the color. For example, FF0000 is the hexadecimal value for
red. The hexadecimal digits can be in upper or lowercase, and must be preceded by a
pound sign (#).

GRAPHNEGCOLOR

Defines a color for the bar graphs that represent negative values.

GRAPHLENGTH

Specifies the length of the longest bar graph. The default length is 60 pixels for a vertical
bar graph and 80 pixels for a horizontal bar graph.

lengthvalue

Sets the value used to display the vertical or horizontal bar graph for the maximum data
value in the associated report column. This value must be a positive number.

This value is initially expressed in the current units (using the UNITS attribute). This value
is then converted into the corresponding number of pixels.

GRAPHSCALE

Specifies the relative bar graph scaling for multiple report columns under a common
ACROSS sort field in which you have applied data visualization graphics. GRAPHSCALE is a
report-level setting (TYPE=REPORT).

UNIFORM

Scales each vertical bar graph based on the minimum and maximum values of the entire
set of values compiled from each ACROSS column in which you have applied data
visualization graphics

DISTINCT

Scales each vertical bar graph based on the distinct minimum and maximum values for
each ACROSS column in which you have applied data visualization graphics.

GRAPHWIDTH

Specifies the width of the bar graphs in a report.

widthvalue

Sets the value used to display the width of the bar graphs in a report. This value must be a
positive number.

This value is initially expressed in the current units (defined by the UNITS attribute). This
value is then converted into the corresponding number of pixels.

Creating Reports With TIBCO® WebFOCUS Language

 1503

Associating Bar Graphs With Report Data

Syntax:

How to Associate Data Visualization Bar Graphs With Report Columns

To add data visualization graphics to report output, add the following declaration to your
WebFOCUS StyleSheet.

GRAPHTYPE=DATA, {COLUMN|ACROSSCOLUMN}=identifier, $

where:

GRAPHTYPE=DATA

Generates vertical or horizontal bar graphs for the data component of a report. Currently,
you can only specify DATA as the report component.

COLUMN

Displays a horizontal bar graph to the right of the specified report column.

ACROSSCOLUMN

Displays a vertical bar graph above every occurrence of the data value associated with an
ACROSS sort field.

identifier

Is any valid identifier. For details, see Identifying a Report Component in a WebFOCUS
StyleSheet on page 1249.

You can define WHEN conditions and bar graph features associated with those conditions
using StyleSheet syntax. For details, see Formatting Report Data on page 1697.

1504

21. Laying Out the Report Page

Example:

Generating Data Visualization Bar Graphs in a Report

The following illustrates how to generate a bar graph for data in your report. Since this report is
sorted with the BY field CITY, horizontal bar graphs display in the output. You can change this
to vertical bars be changing the sort field to ACROSS CITY and the StyleSheet declaration to
GRAPHTYPE=DATA, ACROSSCOLUMN=DIFFERENCE, $. Bar graphs that represent positive
values display in the color blue. Bar graphs that represent negative values display in the color
red.

DEFINE FILE GGSALES
DIFFERENCE/D7M=BUDDOLLARS-DOLLARS;
END

TABLE FILE GGSALES
BY CITY
SUM BUDDOLLARS/D7M DOLLARS/D7M DIFFERENCE
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
GRID=OFF, $
GRAPHTYPE=DATA, COLUMN=N4, GRAPHCOLOR=BLUE, GRAPHNEGCOLOR=RED, $
ENDSTYLE
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1505


Associating Bar Graphs With Report Data

Controlling Bar Graph Scaling in Horizontal (ACROSS) Sort Fields

You can apply vertical bar graphs to different columns above a common ACROSS sort field. The
entire set of values for each column is grouped over an ACROSS sort field that has bar graphs
applied. Therefore, the longest bar graph corresponds to the maximum value of the entire set
of values.

This action is acceptable for separate column values that have ranges that are close. Many
times, however, there is a marked discrepancy between the sets of values for separate
columns. The following image illustrates such a discrepancy.

As you can see from the figure above, the values for the Dollar Sales field ($11,392,310.00 to
$11,710,379.00) is much larger in magnitude than the set of values for the Difference field
($206,292.00 to -$184,622.00). Also notice that the vertical bar graphs associated with the
Difference values all but disappear when graphed against the entire set of values.

To display separate vertical bar graphs based on the set of values for each column, use the
GRAPHSCALE StyleSheet attribute. This attribute modifies data visualization graphics to use
the minimum and maximum values for each column below a common ACROSS sort field to
construct a distinct vertical bar graph.

Syntax:

How to Set Orientation for Visualization Bars

The VISBARORIENT parameter enables you to set horizontal or vertical orientation for
visualization bars for ACROSS columns.

Note: This parameter is only supported for HTML report output.

SET VISBARORIENT = {H|V}

where:

Indicates horizontal bar orientation for visualization bars.

Indicates vertical bar orientation for visualization bars. This is the default value.

H

V

1506

Example:

Setting Orientation for Visualization Bars

21. Laying Out the Report Page

The following report creates vertical bars for the ACROSS column values (DOLLARS,
BUDDOLLARS, UNITS, BUDUNITS).

SET VISBARORIENT=V
TABLE FILE GGSALES
SUM DOLLARS BUDDOLLARS UNITS BUDUNITS
BY REGION
ACROSS CATEGORY
WHERE CATEGORY EQ 'Coffee' OR 'Food'
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
TYPE =REPORT , BORDER=light,$
GRAPHTYPE=DATA, ACROSSCOLUMN=DOLLARS,
GRAPHCOLOR=GREEN,BACKCOLOR=RGB(#ffff00), $
GRAPHTYPE=DATA, ACROSSCOLUMN=BUDDOLLARS, GRAPHCOLOR=RGB(255 0 0), $
GRAPHTYPE=DATA, ACROSSCOLUMN=UNITS, GRAPHCOLOR=blue, $
GRAPHTYPE=DATA, ACROSSCOLUMN=BUDUNITS, GRAPHCOLOR=thistle, $
ENDSTYLE
END

The output is:

The following report creates horizontal bars for the ACROSS column values ( DOLLARS and
BUDDOLLARS.

Creating Reports With TIBCO® WebFOCUS Language

 1507

Associating Bar Graphs With Report Data

SET VISBARORIENT=H
TABLE FILE GGSALES
SUM DOLLARS BUDDOLLARS
BY REGION
ACROSS CATEGORY
WHERE CATEGORY EQ 'Coffee' OR 'Food'
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
TYPE =REPORT ,BORDER=light,$
GRAPHTYPE=DATA, ACROSSCOLUMN=DOLLARS,
GRAPHCOLOR=GREEN,BACKCOLOR=RGB(#ffff00), $
GRAPHTYPE=DATA, ACROSSCOLUMN=BUDDOLLARS, GRAPHCOLOR=RGB(255 0 0), $
ENDSTYLE
END

The output is:

Applying Scaling to Data Visualization Bar Graphs

The GRAPHSCALE parameter specifies the relative bar graph scaling for multiple report
columns under a common ACROSS sort field in which you have applied data visualization
graphics. GRAPHSCALE can only be set for an entire report (TYPE=REPORT).

Syntax:

How to Apply Scaling to Data Visualization Bar Graphs

TYPE=REPORT, GRAPHSCALE={UNIFORM|DISTINCT}

where:

TYPE=REPORT

Specifies that the declaration applies to the entire report, and not to a specific bar graph
within the report.

GRAPHSCALE

Specifies the relative bar graph scaling for multiple report columns under a common
ACROSS sort field in which you have applied data visualization graphics. GRAPHSCALE is a
report-lever setting (TYPE=REPORT).

1508

21. Laying Out the Report Page

UNIFORM

Scales each vertical bar graph based on the minimum and maximum values of the entire
set of values compiled from each ACROSS column in which you have applied data
visualization graphics.

DISTINCT

Scales each vertical bar graph based on the distinct minimum and maximum values for
each ACROSS column in which you have applied data visualization graphics.

Example:

Using GRAPHSCALE to Display Distinct Vertical Bar Graphs

The following report request displays vertical bar graphs for two columns (DOLLARS and
DIFFERENCE) associated with a common ACROSS field (REGION):

DEFINE FILE GGSALES
Difference/D12.2M=DOLLARS-BUDDOLLARS;
END

TABLE FILE GGSALES
SUM DOLLARS/D12.2M Difference
ACROSS REGION
ON TABLE SET STYLE *
TYPE=REPORT,GRID=OFF,$
GRAPHTYPE=DATA, ACROSSCOLUMN=N1,$
GRAPHTYPE=DATA,ACROSSCOLUMN=N2,$
ENDSTYLE
END

This request produces the following report output:

Since the GRAPHSCALE attribute is not specified, the default setting UNIFORM is applied to
the report. This setting uses the entire set of values (values from Dollar Sales and Difference)
to plot the bar graphs for both columns.

Creating Reports With TIBCO® WebFOCUS Language

 1509


Working With Mailing Labels and Multi-Pane Pages

The following request is the same as the above request, except it has the
GRAPHSCALE=DISTINCT attribute included in the StyleSheet.

DEFINE FILE GGSALES
Difference/D12.2M=DOLLARS-BUDDOLLARS;
END

TABLE FILE GGSALES
SUM DOLLARS/D12.2M Difference
ACROSS REGION
ON TABLE SET STYLE *
GRAPHTYPE=DATA, ACROSSCOLUMN=N1,$
GRAPHTYPE=DATA, ACROSSCOLUMN=N2,$
TYPE=REPORT, GRAPHSCALE=DISTINCT,$
ENDSTYLE
END

Notice the difference in the output:

Now each bar graph is plotted based on the set of values for each field.

Working With Mailing Labels and Multi-Pane Pages

You can print sheets of laser printer mailing labels by dividing each page into a matrix of sub-
pages, each corresponding to a single label. Each page break in the report positions the
printer at the top of the next label.

Multi-pane printing places a whole report on a single printed page. You can create columns or
rows so that when text overflows on one page, it appears in the next column or row on the
same page rather than on the next page.

These features apply to a PDF or PS report.

1510


21. Laying Out the Report Page

Reference: Attributes for Mailing Labels and Multi-Pane Printing

In addition to the attributes in the table, you can use standard margin attributes (for example,
LEFTMARGIN or TOPMARGIN) to position the entire sheet of labels at once, creating an
identical margin for each sheet.

Attribute

Description

Applies to

PAGEMATRIX

Sets the number of columns and rows of labels on a
page.

ELEMENT

GUTTER

Sets the width and height of each label, expressed in
the unit of measurement specified by the UNITS
parameter.

Sets the horizontal and vertical distance between
each label, expressed in the unit of measurement
specified by the UNITS parameter.

MATRIXORDER

Sets the order in which the labels are printed.

LABELPROMPT

Sets the position of the first label on the mailing label
sheet.

PDF

PS

PDF

PS

PDF

PS

PDF

PS

PDF

PS

Procedure: How to Set Up a Report to Print Mailing Labels

1. Create the label as a page heading.

2. Sort the labels but use NOPRINT to suppress sort field display. Only the fields embedded

in the page heading will print.

3.

Insert a page break on a sort field to place each new field value on a separate label.

4. Suppress default page numbers and associated blank lines from the beginning of each

page (SET PAGE-NUM=NOPAGE).

Creating Reports With TIBCO® WebFOCUS Language

 1511

Working With Mailing Labels and Multi-Pane Pages

Syntax:

How to Print Mailing Labels or a Multi-Pane Report

[TYPE=REPORT,] PAGEMATRIX=(c r), ELEMENT=(w h), [GUTTER=(x y),]
  [MATRIXORDER={VERTICAL|HORIZONTAL},]  [LABELPROMPT={OFF|ON},] $

where:

TYPE=REPORT

Applies the settings to the entire report. Not required, as it is the default.

c

r

w

h

Is the number of columns of labels across the page.

Enclose the values c and r in parentheses, and do not include a comma between them.

Is the number of rows of labels down the page.

Is the width of each label.

Enclose the values w and h in parentheses, and do not include a comma between them.

Is the height of each label.

GUTTER

Is the distance between each label.

x

y

Is the horizontal distance between each label.

Enclose the values x and y in parentheses, and do not include a comma between them.

Is the vertical distance between each label.

MATRIXORDER

Is the order in which the labels are printed.

VERTICAL

Prints the labels down the page.

HORIZONTAL

Prints the labels across the page.

1512

21. Laying Out the Report Page

LABELPROMPT

Is the position of the first label on the mailing label sheet.

OFF

ON

Starts the report on the first label on the sheet. OFF is the default value.

Prompts you at run time for the row and column number at which to start printing. All
remaining labels follow consecutively. This feature allows partially used sheets of labels to
be re-used.

Example:

Printing Mailing Labels

The following report prints on 81/2 x 11 sheets of address labels.

SET ONLINE-FMT = PDF
TABLE FILE EMPLOYEE
BY LAST_NAME NOPRINT BY FIRST_NAME NOPRINT
ON FIRST_NAME PAGE-BREAK
HEADING
"<FIRST_NAME <LAST_NAME"
"<ADDRESS_LN1"
"<ADDRESS_LN2"
"<ADDRESS_LN3"
ON TABLE SET PAGE-NUM NOPAGE
ON TABLE SET STYLE LABEMP
END

The labels have the following dimensions, defined in the StyleSheet LABEMP:

UNITS=IN, PAGESIZE=LETTER, LEFTMARGIN=0.256, TOPMARGIN=0.5,
PAGEMATRIX=(2 5), ELEMENT=(4 1), GUTTER=(0.188 0), $

Creating Reports With TIBCO® WebFOCUS Language

 1513

Working With Mailing Labels and Multi-Pane Pages

The first page of labels prints as follows:

1514

21. Laying Out the Report Page

Example:

Printing a Multi-Pane Report

This request divides the first report page in two columns so that the second report page
appears in the second column of the first page. A PAGE-BREAK creates a multi-page report for
the purpose of this example.

SET ONLINE-FMT = PDF
TABLE FILE EMPLOYEE
PRINT LAST_NAME AND CURR_SAL BY

DEPARTMENT
ON DEPARTMENT PAGE-BREAK
HEADING
"PAGE <TABPAGENO"
ON TABLE SET STYLE *
UNITS=IN, PAGESIZE=LETTER, PAGEMATRIX=(2 1), ELEMENT=(3.5 8.0),
MATRIXORDER=VERTICAL, $
TYPE=REPORT, SIZE=8, $
ENDSTYLE
END

The report prints as:

Creating Reports With TIBCO® WebFOCUS Language

 1515

Working With Mailing Labels and Multi-Pane Pages

1516

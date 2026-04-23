Chapter3

Sorting Tabular Reports

Sorting enables you to group or organize report information vertically and horizontally, in
rows and columns, and specify a desired sequence of data items in the report.

Any field in the data source can be the sort field. If you wish, you can select several sort
fields, nesting one within another. Sort fields appear only when their values change.

In this chapter:

Sorting Tabular Reports Overview

Ranking Sort Field Values

Sorting Rows

Sorting Columns

Controlling Display of Sort Field Values

Reformatting Sort Fields

Manipulating Display Field Values in a
Sort Group

Grouping Numeric Data Into Ranges

Restricting Sort Field Values by Highest/
Lowest Rank

Sorting and Aggregating Report Columns

Hiding Sort Values

Sort Performance Considerations

Creating a Matrix Report

Sorting With Multiple Display Commands

Controlling Collation Sequence

Improving Efficiency With External Sorts

Specifying the Sort Order

Hierarchical Reporting: BY HIERARCHY

Sorting Tabular Reports Overview

You sort a report using vertical (BY) and horizontal (ACROSS) phrases:

BY displays the sort field values vertically, creating rows. Vertical sort fields are displayed
in the left-most columns of the report.

ACROSS displays the sort field values horizontally, creating columns. Horizontal sort fields
are displayed across the top of the report.

BY and ACROSS phrases used in the same report create rows and columns, producing a
grid or matrix.

A request can include up to 128 sort phrases consisting of any combination of BY and
ACROSS phrases.

Creating Reports With TIBCO® WebFOCUS Language

 87

Sorting Rows

Additional sorting options include:

Sorting from low to high values or from high to low values, and defining your own sorting
sequence.

Sorting based on case-sensitive or case-insensitive collation sequence.

Leaving the value of the sort field out of the report.

Grouping numeric data into tiles such as percentiles or deciles.

Aggregating and sorting numeric columns simultaneously.

Grouping numeric data into ranges.

Ranking data, and selecting data based on rank.

Reference: Sorting and Displaying Data

There are two ways that you can sort information, depending on the type of display command
you use:

You can sort and display individual values of a field using the PRINT or LIST command.

You can group and aggregate information. For example, you can show the number of field
occurrences per sort value using the COUNT command, or summing the field values using
the SUM command.

When you use the display commands PRINT and LIST, the report may generate several rows
per sort value; specifically, one row for each occurrence of the display field. When you use the
commands SUM and COUNT, the report generates one row for each unique set of sort values.
For related information, see Sorting With Multiple Display Commands on page 180.

For details on all display commands, see Displaying Report Data on page 39.

Sorting Rows

You can sort report information vertically using the BY phrase. This creates rows in your report.
You can include up to 128 sort phrases (BY phrases plus ACROSS phrases) per report request
(127 if using PRINT or LIST display commands).

Sort fields appear when their value changes. However, you can display every sort value using
the BYDISPLAY parameter. For an example, see Controlling Display of Sort Field Values on page
133.

88

3. Sorting Tabular Reports

Syntax:

How to Sort by Rows

BY {HIGHEST|LOWEST} [n] sortfield [AS 'text']

where:

HIGHEST

Sorts in descending order.

LOWEST

Sorts in ascending order. LOWEST is the default value.

n

Specifies that only n sort field values are included in the report.

sortfield

Is the name of the sort field.

text

Is the column heading to use for the sort field column on the report output.

Reference: Usage Notes for Sorting Rows

When using the display command LIST with a BY phrase, the LIST counter is reset to 1
each time the major sort value changes.

The default sort sequence is low-to-high, with the following variations for different operating
systems. In z/OS the sequence is a-z, A-Z, 0-9 for alphanumeric fields; 0-9 for numeric
fields. In UNIX and Windows the sequence is 0-9, A-Z, a-z for alphanumeric fields; 0-9 for
numeric. You can specify other sorting sequences, as described in Specifying the Sort Order
on page 149.

You cannot use text fields as sort fields. Text fields are those described in the Master File
with a FORMAT value of TX.

You can use a temporary field created by a DEFINE command, or by the DEFINE attribute in
a Master File, as a sort field. In order to use a temporary field created by a COMPUTE
command as a sort field, you must use the BY TOTAL phrase instead of the BY phrase.

If you specify several sort fields when reporting from a multi-path data source, all the sort
fields must be in the same path.

Sort phrases cannot contain format information for fields.

Creating Reports With TIBCO® WebFOCUS Language

 89

Sorting Rows

Each sort field value appears only once in the report. For example, if there are six
employees in the MIS department, a request that declares

PRINT LAST_NAME BY DEPARTMENT

prints MIS once, followed by six employee names. You can populate every vertical sort
column cell with a value, even if the value is repeating, using the SET BYDISPLAY
parameter. For details, see Controlling Display of Sort Field Values on page 133.

Example:

Sorting Rows With BY

The following illustrates how to display all employee IDs by department.

TABLE FILE EMPLOYEE
PRINT EMP_ID
BY DEPARTMENT
END

The output displays a row for each EMP_ID in each department:

Using Multiple Vertical (BY) Sort Fields

You can organize information in a report by using more than one sort field. When you specify
several sort fields, the sequence of the BY phrases determines the sort order. The first BY
phrase sets the major sort break, the second BY phrase sets the second sort break, and so
on. Each successive sort is nested within the previous one.

90

3. Sorting Tabular Reports

Example:

Sorting With Multiple Vertical (BY) Sort Fields

The following request uses multiple vertical (BY) sort fields.

TABLE FILE EMPLOYEE
PRINT CURR_SAL
BY DEPARTMENT BY LAST_NAME
WHERE CURR_SAL GT 21500
END

The output is:

DEPARTMENT  LAST_NAME               CURR_SAL
----------  ---------               --------
MIS         BLACKWOOD             $21,780.00
            CROSS                 $27,062.00
PRODUCTION  BANNING               $29,700.00
            IRVING                $26,862.00

Displaying a Row for Data Excluded by a Sort Phrase

In a sort phrase, you can restrict the number of sort values displayed. With the PLUS OTHERS
phrase, you can aggregate all other values to a separate group and display this group as an
additional report row.

Syntax:

How to Display Data Excluded by a Sort Phrase

[RANKED] BY {HIGHEST|LOWEST|TOP|BOTTOM}  n srtfield [AS 'text']
            [PLUS OTHERS AS 'othertext']
            [IN-GROUPS-OF m1 [TOP n2]]
            [IN-RANGES-OF m3 [TOP n4]

where:

LOWEST

Sorts in ascending order, beginning with the lowest value and continuing to the highest
value (a-z, A-Z, 0-9 for alphanumeric fields; 0-9 for numeric fields). BOTTOM is a synonym
for LOWEST.

HIGHEST

Sorts in descending order, beginning with the highest value and continuing to the lowest
value. TOP is a synonym for HIGHEST.

n

Specifies that only n sort field values are included in the report.

srtfield

Is the name of the sort field.

Creating Reports With TIBCO® WebFOCUS Language

 91

Sorting Rows

text

Is the text to be used as the column heading for the sort field values.

othertext

Is the text to be used as the row title for the "others" grouping. This AS phrase must be
the AS phrase immediately following the PLUS OTHERS phrase.

m1

n2

m3

n4

Is the incremental value between sort field groups.

Is an optional number that defines the highest group label to be included in the report.

Is an integer greater than zero indicating the range by which sort field values are grouped.

Is an optional number that defines the highest range label to be included in the report. The
range is extended to include all data values higher than this value.

Reference: Usage Notes for PLUS OTHERS

Alphanumeric group keys are not supported.

Only one PLUS OTHERS phrase is supported in a request.

In a request with multiple display commands, the BY field that has the PLUS OTHERS
phrase must be the lowest level BY field in the request. If it is not, a message will display
and the request will not be processed.

The BY ROWS OVER, TILES, ACROSS, and BY TOTAL phrases are not supported with PLUS
OTHERS.

PLUS OTHERS is not supported in a MATCH FILE request. However, MORE in a TABLE
request is supported.

HOLD is supported for formats PDF, PS, HTML, DOC, and WP.

92

Example:

Displaying a Row Representing Sort Field Values Excluded by a Sort Phrase

The following request displays the top two ED_HRS values and aggregates the values not
included in a row labeled Others:

3. Sorting Tabular Reports

TABLE FILE EMPLOYEE
PRINT CURR_SAL LAST_NAME
  BY HIGHEST 2 ED_HRS
  PLUS OTHERS AS 'Others'
END

The output is:

ED_HRS         CURR_SAL  LAST_NAME
------         --------  ---------
 75.00       $21,780.00  BLACKWOOD
 50.00       $18,480.00  JONES
             $16,100.00  MCKNIGHT
Others      $165,924.00

Example:

Displaying a Row Representing Data Not Included in Any Sort Field Grouping

The following request sorts by highest 2 ED_HRS and groups the sort field values by
increments of 25 ED_HRS. Values that fall below the lowest group label are included in the
Others category. All values above the top group label are included in the top group:

TABLE FILE EMPLOYEE
PRINT CURR_SAL LAST_NAME
  BY HIGHEST 2 ED_HRS
  PLUS OTHERS AS 'Others'
IN-GROUPS-OF 25 TOP 50
END

The output is:

ED_HRS         CURR_SAL  LAST_NAME
------         --------  ---------
 50.00       $18,480.00  JONES
             $21,780.00  BLACKWOOD
             $16,100.00  MCKNIGHT
 25.00       $11,000.00  STEVENS
             $13,200.00  SMITH
             $26,862.00  IRVING
              $9,000.00  GREENSPAN
             $27,062.00  CROSS
Others       $78,800.00

Creating Reports With TIBCO® WebFOCUS Language

 93

Sorting Columns

If the BY HIGHEST phrase is changed to BY LOWEST, all values above the top grouping (50
ED_HRS and above) are included in the Others category:

TABLE FILE EMPLOYEE
PRINT CURR_SAL LAST_NAME
  BY LOWEST 2 ED_HRS
  PLUS OTHERS AS 'Others'
IN-GROUPS-OF 25 TOP 50
END

The output is:

ED_HRS         CURR_SAL  LAST_NAME
------         --------  ---------
   .00        $9,500.00  SMITH
             $29,700.00  BANNING
             $21,120.00  ROMANS
             $18,480.00  MCCOY
 25.00       $11,000.00  STEVENS
             $13,200.00  SMITH
             $26,862.00  IRVING
              $9,000.00  GREENSPAN
             $27,062.00  CROSS
Others       $56,360.00

Sorting Columns

You can sort report information horizontally using the ACROSS phrase. This creates columns in
your report. The total number of ACROSS columns is equal to the total number of ACROSS sort
field values multiplied by the total number of display fields.

A request can include up to 128 sort phrases consisting of any combination of BY and
ACROSS phrases.

The maximum number of display fields your report can contain is determined by a combination
of factors. In general, if a horizontal (ACROSS) sort field contains many data values, you may
exceed the allowed width for reports, or create a report that is difficult to read. For details, see
Displaying Report Data on page 39.

You can produce column totals or summaries for ACROSS sort field values using ACROSS-
TOTAL, SUBTOTAL, SUB-TOTAL, RECOMPUTE, and SUMMARIZE. For details, see Including
Totals and Subtotals on page 367.

94

3. Sorting Tabular Reports

Syntax:

How to Sort Columns

ACROSS sortfield

where:

sortfield

Is the name of the sort field.

Reference: Usage Notes for Sorting Columns

You cannot use text fields as sort fields. Text fields are those described in the Master File
with a FORMAT value of TX.

You can use a temporary field created by a DEFINE command, or by the DEFINE attribute in
a Master File, as a sort field. However, you cannot use a temporary field created by a
COMPUTE command as a sort field. You can accomplish this using the BY TOTAL phrase or
indirectly by first creating a HOLD file that includes the field, and then reporting from the
HOLD file. HOLD files are described in Saving and Reusing Your Report Output on page
471.

For an ACROSS phrase, the SET SPACES parameter controls the distance between ACROSS
sets. For more information, see Laying Out the Report Page on page 1331.

If you specify several sort fields when reporting from a multipath data source, all the sort
fields must be in the same path.

In styled output formats (PDF, HTML, DHTML, PPT, PPTX, and XLSX), the width of ACROSS
titles and ACROSS values above the data columns is defined as the largest width of all
data columns, and associated column titles, within the ACROSS groups. To change the size
of the ACROSS groups, apply SQUEEZE, WRAP, or WIDTH definitions to the data columns
within each group.

Each sort field value is displayed only once in the report unless you change this default
using the SET BYDISPLAY command. For example, if there are six employees in the MIS
department, a report that declares

PRINT LAST_NAME ACROSS DEPARTMENT

prints MIS once, followed by six employee names.

Creating Reports With TIBCO® WebFOCUS Language

 95

Sorting Columns

Example:

Sorting Columns With ACROSS

The following illustrates how to show the total salary outlay for each department. This request
is sorted horizontally with an ACROSS phrase.

TABLE FILE EMPLOYEE
SUM CURR_SAL ACROSS DEPARTMENT
END

The output is:

DEPARTMENT
MIS                    PRODUCTION
---------------------------------
$108,002.00           $114,282.00

Notice that the horizontal sort displays a column for each sort field (department).

Controlling Display of an ACROSS Title for a Single Field

Using the SET ACRSVRBTITL command, you can control the display of an ACROSS column title
in an ACROSS group. The behavior of the title is determined by the number of verb columns in
the ACROSS group. The field count is affected by the following features, which add internal
matrix columns to the report:

Fields in a heading or footing.

Fields whose display is suppressed with the NOPRINT phrase.

Reformatted fields (which are normally counted twice).

A COMPUTE command referencing multiple fields.

Syntax:

How to Control Display of an ACROSS Title for a Single Field

SET ACRSVRBTITL = {HIDEONE|ON|OFF}
ON TABLE SET ACRSVRBTITL {HIDEONE|ON|OFF}

where:

HIDEONE

Suppresses the title when there is only one display field, or there is only one display field
and the request contains one or more of the features that add internal matrix columns to
the report. This value is the default.

Always displays the title even if there is only one display field.

ON

96

3. Sorting Tabular Reports

OFF

Suppresses the title when there is only one display field. Displays the title when there is
only one display field and the request contains one or more of the features that add
internal matrix columns to the report. This is legacy behavior.

Example:

Hiding an ACROSS Title With ACRSVRBTITL

The following request against the GGSALES data source has a display field in the heading:

SET ACRSVRBTITL=HIDEONE
TABLE FILE GGSALES
HEADING
"Sales Report for <CATEGORY with ACRSVRBTITL=HIDEONE"
" "
SUM DOLLARS AS Sales
BY CATEGORY
ACROSS REGION
WHERE CATEGORY EQ 'Food'
ON TABLE SET PAGE NOPAGE
ON TABLE SET ACROSSTITLE SIDE
ON TABLE SET ACROSSLINE SKIP

ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, FONT='ARIAL', SIZE=9, SQUEEZE=ON,$
TYPE=TITLE,JUSTIFY=LEFT,BACKCOLOR=RGB(102 102 102),COLOR=RGB(255 255
255),STYLE=BOLD,$
TYPE=HEADING, SIZE=11, STYLE=BOLD,JUSTIFY=CENTER, $
TYPE=ACROSSTITLE,STYLE=BOLD,$
TYPE=ACROSSVALUE,BACKCOLOR=RGB(218 225 232),$
END

Using the default value for ACRSVRBTITL, HIDEONE, suppresses the ACROSS title Sales, even
though the heading displays a field value that adds a report column to the internal matrix.

The report output is shown in the following image:

If you change the SUM command to the following:

SUM DOLLARS/D12CM

Creating Reports With TIBCO® WebFOCUS Language

 97

Sorting Columns

the field in the heading and the reformatted dollar sales values add report columns to the
internal matrix, but the ACROSS title Sales is still suppressed.

The report output is shown in the following image:

Using the ACRSVRBTITL value ON, without reformatting the dollar sales column, does not
suppress the ACROSS title Sales because the heading displays a field value that adds a report
column to the internal matrix.

The report output is shown in the following image:

If you change the SUM command to the following:

SUM DOLLARS/D12CMC

the field in the heading and the reformatted dollar sales values add report columns to the
internal matrix, so the ACROSS title Sales is not suppressed.

The report output is shown in the following image:

98

3. Sorting Tabular Reports

With the setting ACRSVRBTITL=OFF, the field in the heading adds a report column to the
internal matrix, and the ACROSS title Sales is not suppressed.

The report output is shown in the following image:

If you change the SUM command to the following:

SUM DOLLARS/D12CM

the field in the heading and the reformatted dollar sales values add report columns to the
internal matrix, and the ACROSS title Sales is not suppressed.

The report output is shown in the following image:

Positioning ACROSS Titles on Report Output

In a report that uses the ACROSS sort phrase to sort values horizontally across the page, by
default, two lines are generated on the report output for the ACROSS columns. The first line
displays the name of the sort field (ACROSS title), and the second line displays the values for
that sort field (ACROSS value). The ACROSS field name is left justified above the first ACROSS
value.

Creating Reports With TIBCO® WebFOCUS Language

 99

Sorting Columns

If you want to display both the ACROSS title and the ACROSS values on one line in the PDF,
HTML, EXL2K, or XLSX report output, you can issue the SET ACROSSTITLE = SIDE command.
This command places ACROSS titles to the left of the ACROSS values. By default, the titles are
right justified in the space above the BY field titles. You can change the justification of the
ACROSS title by adding the JUSTIFY attribute to the StyleSheet declaration for the
ACROSSTITLE component. If there are no BY fields, the heading line that is created by default
to display the ACROSS title will not be generated.

This feature is designed for use in requests that have both ACROSS fields and BY fields. For
requests with ACROSS fields but no BY fields, the set command is ignored, and the ACROSS
titles are not moved.

Note that for certain output formats, you can control whether column titles are underlined
using the SET TITLELINE command. SET ACROSSLINE is a synonym for SET TITLELINE. For
information, see Using Headings, Footings, Titles, and Labels on page 1517.

Syntax:

How to Control the Position of ACROSS Field Names

SET ACROSSTITLE = {ABOVE|SIDE}

where:

ABOVE

Displays ACROSS titles above their ACROSS values. ABOVE is the default value.

SIDE

Displays ACROSS titles to the left of their ACROSS values, above the BY columns.

Reference: Usage Notes for SET ACROSSTITLE

When the ACROSS value wraps, the ACROSS title aligns with the top line of the wrapped
ACROSS values.

The ACROSS title spans the width of the BY columns. If the ACROSS title value is larger
than the width of the BY columns on the current page, the value is truncated. The first
panel may have more BY fields than subsequent panels, if SET BYPANEL is set to a value
smaller than the total number of BY fields.

This setting will not create a new column within the report for the title placement.

If the request does not have any BY fields, the ACROSS title is not moved.

With BYPANEL=OFF, the ACROSS title is not displayed on subsequent panels.

100

3. Sorting Tabular Reports

WRAP is not supported for ACROSSTITLE with SET ACROSSTITLE=SIDE.

Example:

Placing the ACROSS Title on the Same Line as the ACROSS Values

The following example against the GGSALES data source has two ACROSS sort fields,
CATEGORY and PRODUCT. SET ACROSSTITLE=SIDE moves the ACROSS title to the left of the
ACROSS values. With BYPANEL=ON the ACROSS titles are repeated in the same location on
each subsequent panel.

SET ACROSSTITLE=SIDE
SET BYPANEL=ON
TABLE FILE GGSALES
SUM
     DOLLARS/I8M AS ''
BY REGION
BY ST
BY CITY
ACROSS CATEGORY
ACROSS PRODUCT
WHERE PRODUCT NE 'Capuccino';
ON TABLE SET PAGE-NUM ON
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
     UNITS=IN,
     SQUEEZE=ON,
     ORIENTATION=PORTRAIT,
$
TYPE=REPORT,
     FONT='ARIAL',
     SIZE=10,
     BORDER=LIGHT,
$
TYPE=ACROSSVALUE,
     WRAP=ON,
$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 101

Sorting Columns

The ACROSS title Category displays to the left of the ACROSS values Coffee, Food, and Gifts.
The ACROSS title Product displays to the left of the ACROSS values Espresso, Latte, Biscotti,
and so on. The ACROSS titles are right-justified above the space occupied by the BY field
names Region, State, and City. Notice that the ACROSS value Croissant wraps onto a second
line, and the ACROSS title is aligned with the top line. The following shows panel 1:

102

The following shows panel 2:

3. Sorting Tabular Reports

Creating Reports With TIBCO® WebFOCUS Language

 103

Sorting Columns

Example:

ACROSS Title Spacing

The following example against the GGSALES data source has two BY fields and two ACROSS
fields. This example does not set borders on and does not enable wrapping of the ACROSS
values. SET ACROSSTITLE=SIDE moves the ACROSS title to the left of the ACROSS values. The
SET BYPANEL=1 command repeats only the first BY field on the second panel. To prevent the
ACROSS titles from being truncated to fit above the BY field on the second panel, the first BY
field has an AS name that is longer than the default name:

SET ACROSSTITLE=SIDE
SET BYPANEL=1
TABLE FILE GGSALES
SUM
     DOLLARS/I8M AS ''
BY ST AS 'State Code'
BY CITY
ACROSS CATEGORY AS 'Categories'
ACROSS PRODUCT AS 'Products'
WHERE PRODUCT NE 'Capuccino';
ON TABLE SET PAGE-NUM ON
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
     UNITS=IN,
     SQUEEZE=ON,
     ORIENTATION=PORTRAIT,
$
TYPE=REPORT,
     FONT='ARIAL',
     SIZE=10,
   $
ENDSTYLE
END

104

The first panel follows:

3. Sorting Tabular Reports

Because of the SET BYPANEL=1 command, the space available above the BY fields on the
second panel is smaller than the space on the initial panel. The AS name State Code adds
space for the ACROSS titles, so the titles are not truncated on the second panel:

Creating Reports With TIBCO® WebFOCUS Language

 105

Sorting Columns

Example:

Specifying Background Color for ACROSS Values With ACROSSTITLE=SIDE

The following request against the GGSALES data source places the ACROSS titles next to the
ACROSS values and sets matching styling of font color and backcolor for the ACROSSTITLES,
ACROSSVALUES, and column titles to white text on grey background color.

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
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
SQUEEZE=ON,UNITS=IN,ORIENTATION=PORTRAIT,$
TYPE=REPORT,FONT='ARIAL',SIZE=10,BORDER=LIGHT,$
TYPE=ACROSSTITLE,COLOR=WHITE, BACKCOLOR=GREY,$
TYPE=ACROSSVALUE,COLOR=WHITE, BACKCOLOR=GREY,$
TYPE=TITLE,COLOR=WHITE, BACKCOLOR=GREY,$
ENDSTYLE
END

The output has a grey background color and white text for the ACROSS titles, ACROSS values,
and column titles.

106

3. Sorting Tabular Reports

Using Multiple Horizontal (ACROSS) Sort Fields

You can sort a report using more than one sort field. When several sort fields are used, the
ACROSS phrase order determines the sorting order. The first ACROSS phrase sets the first
sort break, the second ACROSS phrase sets the second sort break, and so on. Each
successive sort is nested within the previous one.

Example:

Sorting With Multiple Horizontal (ACROSS) Phrases

The following request sorts the sum of current salaries, first by department and then by job
code.

TABLE FILE EMPLOYEE
SUM CURR_SAL
ACROSS DEPARTMENT ACROSS CURR_JOBCODE
WHERE CURR_SAL GT 21500
END

The output is:

DEPARTMENT
                  MIS
PRODUCTION
CURR_JOBCODE
                  A17              B04              A15
A17
------------------------------------------------------------------------
           $27,062.00       $21,780.00       $26,862.00       $29,700.00

Collapsing PRINT With ACROSS

The PRINT command generates a report that has a single line for each record retrieved from
the data source after screening out those that fail IF or WHERE tests. When PRINT is used in
conjunction with an ACROSS phrase, many of the generated columns may be empty. Those
columns display the missing data symbol.

To avoid printing such a sparse report, you can use the SET ACROSSPRT command to
compress the lines in the report. The number of lines is reduced within each sort group by
swapping non-missing values from lower lines with missing values from higher lines, and then
eliminating any lines whose columns all have missing values.

Because data may be moved to different report lines, row-based calculations such as ROW-
TOTAL and ACROSS-TOTAL in a compressed report are different from those in a non-
compressed report. Column calculations are not affected by compressing the report lines.

Syntax:

How to Compress Report Lines

SET ACROSSPRT = {NORMAL|COMPRESS}

Creating Reports With TIBCO® WebFOCUS Language

 107

Sorting Columns

ON TABLE SET ACROSSPRT{NORMAL|COMPRESS}

where:

NORMAL

Does not compress report lines. NORMAL is the default value.

COMPRESS

Compresses report lines by promoting data values up to replace missing values within a
sort group.

Reference: Usage Notes for SET ACROSSPRT

Compression applies only to ACROSS fields, including ACROSS … COLUMNS. It has no
effect on BY fields.

The only data values that are subject to compression are true missing values. If the value
of the stored data is either 0 or blank and the metadata indicates that MISSING is ON, that
value is not subject to compression.

Example:

Compressing Report Output With SET ACROSSPRT

The following request against the GGSALES data source prints unit sales by product across
region:

TABLE FILE GGSALES
PRINT UNITS/I5
BY PRODUCT
ACROSS REGION
WHERE DATE FROM '19971201' TO '19971231';
WHERE PRODUCT EQ 'Capuccino' OR 'Espresso';
ON TABLE SET ACROSSPRT NORMAL
ON TABLE SET PAGE NOPAGE
END

108

Each line of the report represents one sale in one region, so at most one column in each row
has a non-missing value when ACROSSPRT is set to NORMAL.

3. Sorting Tabular Reports

                  Region
                  Midwest     Northeast   Southeast   West
Product           Unit Sales  Unit Sales  Unit Sales  Unit Sales
-----------------------------------------------------------------
Capuccino                  .         936           .           .
                           .         116           .           .
                           .         136           .           .
                           .           .        1616           .
                           .           .        1118           .
                           .           .         774           .
                           .           .           .        1696
                           .           .           .        1519
                           .           .           .         836
Espresso                1333           .           .           .
                         280           .           .           .
                         139           .           .           .
                           .        1363           .           .
                           .         634           .           .
                           .         406           .           .
                           .           .        1028           .
                           .           .        1014           .
                           .           .         885           .
                           .           .           .        1782
                           .           .           .        1399
                           .           .           .         551

Setting ACROSSPRT to COMPRESS promotes non-missing values up to replace missing values
within the same BY group and then eliminates lines consisting of all missing values.

TABLE FILE GGSALES
PRINT UNITS/I5
BY PRODUCT
ACROSS REGION
WHERE DATE FROM '19971201' TO '19971231';
WHERE PRODUCT EQ 'Capuccino' OR 'Espresso';
ON TABLE SET ACROSSPRT COMPRESS
ON TABLE SET PAGE NOPAGE
END

Creating Reports With TIBCO® WebFOCUS Language

 109

Sorting Columns

The output is:

                  Region
                  Midwest     Northeast   Southeast   West
Product           Unit Sales  Unit Sales  Unit Sales  Unit Sales
----------------------------------------------------------------
Capuccino                  .         936        1616        1696
                           .         116        1118        1519
                           .         136         774         836
Espresso                1333        1363        1028        1782
                         280         634        1014        1399
                         139         406         885         551

Hiding Null Columns in ACROSS Groups

Report requests that use the ACROSS sort phrase generate a group of columns (one for each
display field in the request) under each value of the ACROSS field. In many cases, some of
these columns have only missing or null values. You can use the HIDENULLACRS parameter to
hide the display of ACROSS groups containing only null columns in styled output formats. If
there is a BY field with a PAGE-BREAK option, columns are hidden on each page of output
generated by that PAGE-BREAK option. If the request contains no BY page breaks, ACROSS
groups that are missing for the entire report are hidden.

Hiding null ACROSS columns is supported for all styled output formats except for the EXL2K
PIVOT and EXL2K FORMULA options.

Syntax:

How to Hide Null ACROSS Columns

SET HIDENULLACRS = {ON|OFF}

ON TABLE SET HIDENULLACRS {ON|OFF}

where:

ON

Hides columns with missing data in ACROSS groups within a BY-generated page break.

OFF

Does not hide columns. OFF is the default value.

Reference: Usage Notes for Hiding Null Columns Within ACROSS Groups

Aligning items in headings with the associated data columns (HEADALIGN) is not supported
for ACROSS reports.

110

3. Sorting Tabular Reports

Hiding ACROSS columns will not affect items placed in heading elements with spot markers
or explicit positioning. This means that after ACROSS group columns are hidden, items may
align with the ACROSS columns differently than expected.

Reference: Features Not Supported For Hiding Null ACROSS Columns

EXL2K FORMULA.

EXL2K PIVOT.

OVER.

HIDENULLACRS is only supported with page breaks specified in ON byfieldname PAGE-
BREAK phrases or BY fieldname PAGE-BREAK phrases. It is not supported with:

BY field ROWS value OVER.

FML FOR fields (FOR fieldvalue OVER PAGE-BREAK).

Hiding ACROSS Groups and Columns Within BY Page Breaks

Hiding null columns is most useful when a BY sort field has the PAGE-BREAK option, either on
the BY phrase itself or in an ON phrase. The change in value of the BY field determines when a
page break is generated for that BY field. The change in BY field value defines the limits within
which the ACROSS columns will be hidden, even if the BY field value spans multiple physical
pages.

There is no way to specify a particular BY field with this setting, so if the request has multiple
BY fields with page breaks, the setting applies to all of them. If there are no BY fields with
page breaks, an ACROSS column must be missing for the entire report in order to be hidden.

The entire ACROSS group will be hidden either when the ACROSS value is missing or when all
of the rows for all of the display columns under that ACROSS value contain null or missing
values within the given BY field value.

The set of pages generated for a BY field value with a page break will be hidden if all ACROSS
groups within that BY field value are hidden.

When columns are removed from a page or a panel, the existing columns are resituated to fill
the missing space.

Creating Reports With TIBCO® WebFOCUS Language

 111

Sorting Columns

Example:

Hiding Null ACROSS Groups

The following request against the GGSALES data source has a page break on the BY field
named REGION and an ACROSS phrase on the CITY field. The display fields in each ACROSS
group are UNITS and DOLLARS:

SET HIDENULLACRS=OFF
TABLE FILE GGSALES
SUM UNITS DOLLARS
BY REGION PAGE-BREAK
BY ST
ACROSS CITY
WHERE CITY LE 'Memphis'
ON TABLE SET HTMLCSS ON
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET STYLE *
TYPE=REPORT, FONT=ARIAL, SIZE=9,$
ENDSTYLE
END

With SET HIDENULLACRS=OFF, all columns display:

112

3. Sorting Tabular Reports

Running the request with SET HIDENULLACRS=ON eliminates the ACROSS groups for cities
with missing data within each region. For example, the Midwest region has no columns for
Atlanta or Boston:

Creating Reports With TIBCO® WebFOCUS Language

 113

Sorting Columns

Example:

Hiding Columns Within ACROSS Groups

In the following request against the GGSALES data source, REGION is a BY field with a PAGE-
BREAK, and PRODUCT is the ACROSS field. The DEFINE command creates a field named
SHOWDOLLARS that has missing values for the Espresso column within the ACROSS group
Coffee:

SET HIDENULLACRS=OFF
SET BYPANEL=2
DEFINE FILE GGSALES
SHOWDOLLARS/I8M MISSING ON = IF (PRODUCT EQ 'Espresso') THEN MISSING ELSE
DOLLARS;
END
TABLE FILE GGSALES
HEADING
"Page <TABPAGENO "
SUM SHOWDOLLARS AS ''
BY REGION
BY ST
BY CITY
ACROSS PRODUCT
WHERE REGION EQ 'Midwest' OR 'Northeast'
WHERE CATEGORY EQ 'Coffee';
ON REGION PAGE-BREAK
ON TABLE SET PAGE-NUM ON
ON TABLE NOTOTAL
ON TABLE SET HTMLCSS ON
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET STYLE *
     UNITS=IN,
     SQUEEZE=ON,
     ORIENTATION=PORTRAIT,
$
TYPE=REPORT,
     GRID=OFF,
     FONT='ARIAL',
     SIZE=9,
$
ENDSTYLE
END

114

Running the request with SET HIDENULLACRS=OFF displays the Espresso column and any
other column containing missing values within the Coffee group:

3. Sorting Tabular Reports

Creating Reports With TIBCO® WebFOCUS Language

 115

Sorting Columns

Running the request with SET HIDENULLACRS=ON hides columns with missing data within
each region. On page 1 (Midwest), both the Capuccino and Espresso columns are hidden,
while on page 2 (Northeast), only the Espresso column is hidden:

116

3. Sorting Tabular Reports

Example:

Hiding Null Columns With Multiple ACROSS Fields

The following request against the GGSALES data source has two ACROSS fields, PRODUCT and
CATEGORY. The BY field with the page break is REGION. The DEFINE command creates a field
named SHOWDOLLARS that has missing values for the Espresso column within the ACROSS
group Coffee and for the entire ACROSS group Gifts.

SET HIDENULLACRS=OFF
DEFINE FILE GGSALES
SHOWDOLLARS/I8M MISSING ON = IF (PRODUCT EQ 'Espresso' OR
   CATEGORY EQ 'Gifts') THEN MISSING ELSE DOLLARS;
END
TABLE FILE GGSALES
SUM SHOWDOLLARS AS ''
BY REGION
BY ST
BY CITY
ACROSS CATEGORY
ACROSS PRODUCT
WHERE REGION EQ 'Midwest' OR 'Northeast'
ON REGION PAGE-BREAK
HEADING
"Page <TABPAGENO /<TABLASTPAGE "
ON TABLE SET PAGE-NUM OFF
ON TABLE SET BYPANEL ON
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
     UNITS=IN,
     PAGESIZE='Letter',
     SQUEEZE=ON,
     ORIENTATION=PORTRAIT,
$
TYPE=REPORT,
     HEADPANEL=ON,
     GRID=OFF,
     FONT='ARIAL',
     SIZE=8,
$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 117

Sorting Columns

Running the request with SET HIDENULLACRS=OFF displays all of the columns:

118

3. Sorting Tabular Reports

Running the request with SET HIDENULLACRS=ON hides the Espresso product and the entire
Gifts category within each region. On page 1 (Midwest), the Gifts group and the Espresso and
Capuccino columns are hidden, while on page 2 (Northeast), the Gifts group and the Espresso
column are hidden:

Generating Summary Lines and Hiding Null ACROSS Columns

If an entire ACROSS group is hidden, so are the totals generated for the associated BY field
value. If any of the columns for the ACROSS value contain non-missing data, the ACROSS
group will display with the non-missing columns.

Summary elements remain tied to their ACROSS group columns. If an ACROSS group is
hidden, the associated summary value will be hidden, and subsequent values will realign with
their ACROSS columns.

Summary lines generated at BY field breaks display at the end of the final page for that BY
field value. All ACROSS groups that contain any non-null data within the entire BY value (even if
they were hidden on some pages within the BY value) will display on the summary lines so that
associated summary values can be displayed.

Creating Reports With TIBCO® WebFOCUS Language

 119

Sorting Columns

Grand totals can contain ACROSS columns that have been hidden on some pages within a BY
field value. Therefore, they are always placed on a new page and presented for all ACROSS
groups and columns that displayed on any page within the report, regardless of what was
hidden on other pages.

Summary lines defined for BY fields outside of the innermost BY page break may also contain
ACROSS columns that have been hidden for some of the internal BY fields. For this reason,
these summary lines will always present all available ACROSS columns and will be presented
on a new page.

All totals calculated in columns (ACROSSTOTAL, ROWTOTAL) will be hidden if all of the column
totals are missing.

120

Example:

Generating Column Totals and Hiding Null ACROSS Columns

3. Sorting Tabular Reports

In the following request against the GGSALES data source, REGION is a BY field with a PAGE-
BREAK, and PRODUCT is the ACROSS field. The DEFINE command creates a field named
SHOWDOLLARS that has missing values for the Espresso column within the ACROSS group
Coffee. Column totals are generated at the end of the report:

SET HIDENULLACRS=ON
DEFINE FILE GGSALES
SHOWDOLLARS/I8M MISSING ON = IF (PRODUCT EQ 'Espresso') THEN MISSING ELSE
DOLLARS;
END
TABLE FILE GGSALES
SUM SHOWDOLLARS AS ''
BY REGION
BY ST
BY CITY
ACROSS PRODUCT
ON REGION PAGE-BREAK
HEADING
"Page <TABPAGENO /<TABLASTPAGE "
WHERE CATEGORY EQ 'Coffee';
ON TABLE SET PAGE-NUM OFF
ON TABLE SET BYPANEL ON
ON TABLE COLUMN-TOTAL AS 'TOTAL'
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
     UNITS=IN,
     PAGESIZE='Letter',
     SQUEEZE=ON,
     ORIENTATION=PORTRAIT,
$
TYPE=REPORT,
     HEADPANEL=ON,
     GRID=OFF,
     FONT='ARIAL',
     SIZE=9,
$
ENDSTYLE
END

Running the request hides the null columns within each REGION page break and generates a
separate page for the column totals.

Creating Reports With TIBCO® WebFOCUS Language

 121

Sorting Columns

The following shows pages one through three. On page 1, the Espresso and Capuccino
columns are hidden. On pages 2 and 3, the Espresso column is hidden:

122

3. Sorting Tabular Reports

The following shows pages four and five. On page 4, the Espresso column is hidden. Page 5 is
the totals page. The Espresso column is hidden since it was hidden on every detail page.
However, Capuccino is not hidden since it appeared on some pages:

Using Column Styling and Hiding Null ACROSS Columns

Column styling remains attached to the original column, regardless of whether the column
remains in the same place on the report output because of hiding null columns. In particular:

BORDERS and BACKCOLOR will readjust to fit the resulting panel or page layout after the
columns are hidden.

Styling specified for a designated column will remain attached to the designated column
and be unaffected by the hidden columns. For example, if the third ACROSS column is
defined with conditional styling, and the second ACROSS column is hidden, the formatting
will remain on the column that was initially third, even though it becomes the second
column on the output.

For information about styling columns, see Identifying a Report Component in a WebFOCUS
StyleSheet on page 1249.

Creating Reports With TIBCO® WebFOCUS Language

 123

Sorting Columns

Example:

Using Column Styling and Hiding Null ACROSS Columns

In the following request against the GGSALES data source, REGION is a BY field with a PAGE-
BREAK and PRODUCT is the ACROSS field. The DEFINE command creates a field named
SHOWDOLLARS that has missing values for the Capuccino column in the Midwest region, the
Thermos column in the Northeast region, the Scone column in the Southeast region, and the
entire West region. Column totals, row totals, and a subtotal for each region are generated.

Some of the columns are assigned background colors:

Column C5 has BACKCOLOR=WHEAT. C5 is the fifth column counting display fields from
left to right, but not counting BY fields or ROW-TOTAL fields. Column C5 corresponds to the
Croissant column in the Coffee group.

Column P5 has BACKCOLOR=THISTLE. P5 is the fifth column counting display fields, BY
fields, and ROW-TOTAL fields, but not NOPRINT fields. Column P5 corresponds to the
Espresso column in the Coffee group.

Column N7 has BACKCOLOR=MEDIUM GOLDENROD. N7 is the seventh column counting
display fields, BY fields, ROW-TOTAL fields, and NOPRINT fields. Column N7 corresponds to
the Biscotti column in the Food group.

Column B3 has BACKCOLOR=GOLDENROD. B3 is the third BY field, counting all BY fields,
even if not printed. Column B3 corresponds to the CITY sort field.

Column SHOWDOLLARS(6) has BACKCOLOR=SILVER. SHOWDOLLARS(6) is the sixth
occurrence of the SHOWDOLLARS field and corresponds to the Scone column in the Food
group.

The request follows:

124

3. Sorting Tabular Reports

SET HIDENULLACRS=OFF
DEFINE FILE GGSALES
SHOWDOLLARS/I8M MISSING ON =
IF ((PRODUCT EQ 'Capuccino' AND REGION EQ 'Midwest') OR
(PRODUCT EQ 'Coffee Grinder' AND REGION EQ 'Northeast') OR
(PRODUCT EQ 'Scone' AND REGION EQ 'Southeast') OR
(REGION EQ 'West')) THEN MISSING ELSE DOLLARS;
END
TABLE FILE GGSALES
SUM SHOWDOLLARS AS ''
BY REGION
BY ST
BY CITY
ACROSS CATEGORY
ACROSS PRODUCT
ON REGION SUBTOTAL AS '*TOTAL'
ON REGION PAGE-BREAK
HEADING
" Page <TABPAGENO "HEADING
" Capuccino Missing in Coffee Group "
WHEN REGION EQ 'Midwest';
HEADING
" Coffee Grinder Missing in Gifts Group "
WHEN REGION EQ 'Northeast';
HEADING
" Scone Missing in Food Group "
WHEN REGION EQ 'Southeast';
WHERE CATEGORY EQ 'Coffee' OR 'Food'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET BYPANEL ON
ON TABLE ROW-TOTAL AS 'TOTAL'
ON TABLE COLUMN-TOTAL AS 'TOTAL'
ON TABLE SET HTMLCSS ON
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET STYLE *
UNITS=IN,PAGESIZE='Letter',SQUEEZE=ON,ORIENTATION=PORTRAIT,$
TYPE=REPORT,HEADPANEL=ON,GRID=OFF,FONT='ARIAL',SIZE=6,$
TYPE=HEADING, style=bold, size=8,$
TYPE=DATA, COLUMN = C5, BACKCOLOR=WHEAT,$
TYPE=DATA, COLUMN = P5, BACKCOLOR=THISTLE,$
TYPE=DATA, COLUMN = N7, BACKCOLOR=MEDIUM GOLDENROD,$
TYPE=DATA, COLUMN = B3, BACKCOLOR=GOLDENROD,$
TYPE=DATA, COLUMN = SHOWDOLLARS(6), BACKCOLOR=silver,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 125

Sorting Columns

Running the report with SET HIDENULLACRS=OFF shows all columns. A page is generated for
the West region and subtotals are calculated, even though all of the values are missing:

126

3. Sorting Tabular Reports

Creating Reports With TIBCO® WebFOCUS Language

 127

Sorting Columns

Running the report with SET HIDENULLACRS=ON, shows:

On page 1, the Capuccino column is hidden and, therefore, the Espresso column is no
longer P5 on the report, but it still has BACKCOLOR=THISTLE. Similarly, the Biscotti column
has MEDIUM, GOLDENROD, the Croissant column has WHEAT, and the Scone column has
SILVER.

The subtotals for each region are calculated only for columns that display for that region.

No page is generated for the West region since all of its values are missing.

Every column is represented on the page with the grand totals.

The output is:

128

3. Sorting Tabular Reports

Hiding Null ACROSS Columns in an FML Request

An FML request always has a FOR field that defines the order of specific rows. The FOR field
cannot be used to trigger hiding of null ACROSS columns. However, the request can also have
a BY field with a PAGE-BREAK option and this can be used to hide null ACROSS columns.

Creating Reports With TIBCO® WebFOCUS Language

 129

Sorting Columns

Example:

Hiding Null ACROSS Columns in an FML Request

The following FML request against the GGSALES data source has a BY field named REGION
with the PAGE-BREAK option and an ACROSS field named QTR. The FOR field is PRODUCT. The
DEFINE command creates the QTR field and contains missing values for Q4 in the Midwest
region, Q2 in the Northeast region, and for all quarters in the Southeast region.

SET HIDENULLACRS=ON
DEFINE FILE GGSALES
QTR/Q=DATE;
SHOWDOLLARS/D12CM MISSING ON =
          IF REGION EQ 'Midwest' AND QTR EQ 'Q4' THEN MISSING
     ELSE IF REGION EQ 'Northeast' AND QTR EQ 'Q2' THEN MISSING
     ELSE IF REGION EQ 'Southeast' THEN MISSING
     ELSE DOLLARS;
END
TABLE FILE GGSALES
SUM SHOWDOLLARS
BY REGION
ACROSS QTR
FOR PRODUCT
'Biscotti' AS 'Biscotti' LABEL R1 OVER
'Capuccino' AS 'Capuccino' LABEL R2 OVER
'Latte' AS 'Latte' LABEL R3 OVER
'Mug' AS 'Mug' LABEL R4 OVER
'Coffee Pot' AS 'Coffee Pot' LABEL R5 OVER
RECAP R6/D12.2=R1+R2+R3+R4+R5;
 AS ''
ON REGION PAGE-BREAK
ON TABLE SET PAGE-NUM OFF
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET HTMLCSS ON

ON TABLE SET STYLE *
     UNITS=IN,
     SQUEEZE=ON,
     ORIENTATION=PORTRAIT,$
TYPE=REPORT,
     GRID=OFF,
     FONT='ARIAL',
     SIZE=9,$
TYPE=TITLE,
     STYLE=BOLD,$
TYPE=ACROSSTITLE,
     STYLE=BOLD,$
ENDSTYLE
END

130

Running the request with SET HIDENULLACRS=OFF generates all columns and a page for all
regions, including the Southeast regions where all values are missing:

3. Sorting Tabular Reports

Creating Reports With TIBCO® WebFOCUS Language

 131

Sorting Columns

Running the request with SET HIDENULLACRS=ON hides column Q4 for the Midwest region, Q2
for the Northeast region, and the entire page for the Southeast region:

132

3. Sorting Tabular Reports

Controlling Display of Sort Field Values

By default, a sort field value displays only on the first row or column of the set of detail rows or
columns generated for that sort field value. You can control this behavior using the BYDISPLAY
parameter. BYDISPLAY is supported for all output formats and can control display of ACROSS
values as well as BY values.

This feature enables you to avoid specifying the sort field twice, once as a display field and
once for sorting (with the NOPRINT option). For example:

PRINT FIRST_NAME LAST_NAME
BY FIRST_NAME NOPRINT

Syntax:

How to Control Display of Sort Field Values

SET BYDISPLAY = {OFF|ON|BY|ACROSS|ALL}

ON TABLE SET BYDISPLAY {OFF|ON|BY|ACROSS|ALL}

where:

OFF

Displays a sort field value only on the first line or column of the report output for the sort
group and on the first line or column of a page. OFF is the default value.

ON or BY

Displays the relevant BY field value on every line of report output produced. BY is a
synonym for ON.

ACROSS

Displays the relevant ACROSS field value on every column of report output produced.

ALL

Displays the relevant BY field value on every line of report output and the relevant ACROSS
field value on every column of report output.

Creating Reports With TIBCO® WebFOCUS Language

 133

Controlling Display of Sort Field Values

Example:

Controlling Display of Sort Field Values on Report Output

The following request generates a report on which sort field values only display when they
change (BYDISPLAY OFF).

-SET &BYDISP = OFF;
SET BYDISPLAY = &BYDISP
TABLE FILE WF_RETAIL_LITE
HEADING CENTER
" BYDISPLAY = &BYDISP"
" "
SUM QUANTITY_SOLD DAYSDELAYED
BY PRODUCT_CATEGORY
BY PRODUCT_SUBCATEG
ACROSS BUSINESS_REGION
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

The output is shown in the following image.

134

Changing BYDISPLAY to ON or BY displays BY field values on every row, as shown in the
following image.

3. Sorting Tabular Reports

Changing BYDISPLAY to ACROSS displays ACROSS field values over every column, as shown in
the following image.

Creating Reports With TIBCO® WebFOCUS Language

 135

Reformatting Sort Fields

Changing BYDISPLAY to ALL displays BY field values on every row and ACROSS field values
over every column, as shown in the following image.

Reformatting Sort Fields

When displaying a vertical (BY) sort column or horizontal (ACROSS) sort row on report output,
you can reformat the sort field values by specifying the new format in the sort phrase. The
reformatting affects only the sort field value as displayed on the sort row or column. That is, if
the field used as a sort field is referenced in a heading, subheading, footing, subfooting, or
summary line, it displays with its original format.

Syntax:

How to Reformat a Sort Field

{BY [TOTAL]|ACROSS [TOTAL]} sortfield/fmt ...

where:

sortfield

Is the sort field.

fmt

Is the new display format.

Reference: Usage Notes for Reformatting Sort Fields

Reformatting is not supported in an ON phrase.

Reformatting is only applied to the row or column generated by the sort phrase, not to
subheading, subfooting, or summary rows that reference the sort field.

136

3. Sorting Tabular Reports

Field-based reformatting (the format is stored in a field) is not supported for sort fields. For
information on field-based reformatting, see Field-Based Reformatting on page 1736.

BY field reformatting is propagated to HOLD files. ACROSS field reformatting is not
propagated to HOLD files.

The following features issue a warning, ignore the reformatting, and proceed with the
request:

IN-GROUPS/RANGES-OF

ROWS

COLUMNS

FOR field/reformat

All decisions are made based on an original field, therefore any option on a reformatted
sort field should be placed on an original sort field break point. As a consequence,
whenever the sort field value should appear (for example, in SUBTOTALS) an original field
value displays.

Example:

Reformatting Sort Fields

The following request against the GGSALES data source includes the following reformatted sort
fields:

BY CATEGORY, with CATEGORY reformatted as A3.

BY PRODUCT, with PRODUCT reformatted as A4.

ACROSS REGION, with region reformatted as A6.

TABLE FILE GGSALES
SUM UNIT
BY CATEGORY/A3
BY PRODUCT/A4
ACROSS REGION/A6
ON CATEGORY SUBTOTAL
ON CATEGORY SUBHEAD
"CATEGORY IS <CATEGORY "
" "
ON TABLE SET PAGE NOPAGE
END

Creating Reports With TIBCO® WebFOCUS Language

 137

Manipulating Display Field Values in a Sort Group

On the output, the reformatting displays on the BY and ACROSS rows but is not propagated to
the subheading and subtotal rows:

                   REGION
                     Midwes       Northe       Southe       West
CATEGORY  PRODUCT
-----------------------------------------------------------------------
CATEGORY IS Coffee

Cof       Capu              .        44785        73264        72831
          Espr         101154        68127        68030        71675
          Latt         231623       226243       211063       213920

*TOTAL CATEGORY Coffee
                       332777       339155       352357       358426

CATEGORY IS Food

Foo       Bisc          90413       149793       119594        70569
          Croi         139881       137394       156456       197022
          Scon         116127        70732        73779        72776
*TOTAL CATEGORY Food
                       346421       357919       349829       340367

CATEGORY IS Gifts

Gif       Coff          54002        40977        50556        48081
          Coff          47156        46185        49922        47432
          Mug           86718        91497        88474        93881
          Ther          46587        48870        48976        45648
*TOTAL CATEGORY Gifts
                       234463       227529       237928       235042

TOTAL                  913661       924603       940114       933835

Manipulating Display Field Values in a Sort Group

You can use the WITHIN phrase to manipulate a display field values as they are aggregated
within a sort group. This technique can be used with a prefix operator to perform calculations
on a specific aggregate field rather than a report column. In contrast, the SUM and COUNT
commands aggregate an entire column.

The WITHIN phrase requires a BY phrase and/or an ACROSS phrase. A maximum of two
WITHIN phrases can be used per display field. If one WITHIN phrase is used, it must act on a
BY phrase. If two WITHIN phrases are used, the first must act on a BY phrase and the second
on an ACROSS phrase.

138

3. Sorting Tabular Reports

You can also use WITHIN TABLE, which allows you to return the original value within a request
command. The WITHIN TABLE command can also be used when an ACROSS phrase is needed
without a BY phrase. Otherwise, a single WITHIN phrase requires a BY phrase.

Syntax:

How to Use WITHIN to Manipulate Display Fields

{SUM|COUNT} display_field WITHIN by_sort_field [WITHIN across_sort_field]
   BY by_sort_field [ACROSS across_sort_field]

where:

display_field

Is the object of a SUM or COUNT display command.

by_sort_field

Is the object of a BY phrase.

across_sort_field

Is the object of an ACROSS phrase.

Example:

Summing Values Within Sort Groups

The following report shows the units sold and the percent of units sold for each product within
store and within the table:

TABLE FILE SALES
SUM UNIT_SOLD AS 'UNITS'
AND PCT.UNIT_SOLD AS 'PCT,SOLD,WITHIN,TABLE'
AND PCT.UNIT_SOLD WITHIN STORE_CODE AS 'PCT,SOLD,WITHIN,STORE'
BY STORE_CODE SKIP-LINE BY PROD_CODE
END

Creating Reports With TIBCO® WebFOCUS Language

 139

Creating a Matrix Report

The output is:

Creating a Matrix Report

You can create a matrix report by sorting both rows and columns. When you include both BY
and ACROSS phrases in a report request, information is sorted vertically and horizontally,
turning the report into a matrix of information that you read like a grid. A matrix report can have
multiple BY and ACROSS sort fields.

Example:

Creating a Simple Matrix

The following request displays total salary outlay across departments and by job codes,
creating a matrix report.

TABLE FILE EMPLOYEE
SUM CURR_SAL
ACROSS DEPARTMENT
BY CURR_JOBCODE
END

140

3. Sorting Tabular Reports

The output is:

                   DEPARTMENT
                   MIS              PRODUCTION
CURR_JOBCODE
------------------------------------------------
A01                         .        $9,500.00
A07                 $9,000.00       $11,000.00
A15                         .       $26,862.00
A17                $27,062.00       $29,700.00
B02                $18,480.00       $16,100.00
B03                $18,480.00                .
B04                $21,780.00       $21,120.00
B14                $13,200.00                .

Example:

Creating a Matrix With Several Sort Fields

The following request uses several BY and ACROSS sort fields to create a matrix report.

TABLE FILE EMPLOYEE
SUM CURR_SAL
ACROSS DEPARTMENT ACROSS LAST_NAME
BY CURR_JOBCODE BY ED_HRS
WHERE DEPARTMENT EQ 'MIS'
WHERE CURR_SAL GT 21500
END

The output is:

                            DEPARTMENT
                            MIS
                            LAST_NAME
                            BLACKWOOD            CROSS
CURR_JOBCODE  ED_HRS
------------------------------------------------------
A17            45.00                .       $27,062.00
B04            75.00       $21,780.00                .

Controlling Collation Sequence

Collation is defined as a set of rules that apply to the ordering and matching of all language
elements that involve comparison of two values. A wide variety of elements are affected by this
feature. Among these features are sorting, aggregation, WHERE conditions, and StyleSheets.
By default, items are sorted based on their binary values. The COLLATION settings SRV_CI and
SRV_CS, case-insensitive and case-sensitive collation, implement collation based on the
LANGUAGE setting. Case-insensitive collation means that all WHERE clauses and sorts ignore
the case of the elements being compared. COLLATION is a session level setting (it is not
supported in an ON TABLE phrase and should be set in the edasprof server profile).

The collation setting applies only to alphanumeric values.

Creating Reports With TIBCO® WebFOCUS Language

 141

Controlling Collation Sequence

Syntax:

How to Establish Binary or Case-Insensitive Collation Sequence

Add the following command to the server edasprof.prf profile:

SET COLLATION = {BINARY|SRV_CI|SRV_CS|CODEPAGE}

where:

BINARY

Bases the collation sequence on binary values.

SRV_CI

Bases collation sequence on the LANGUAGE setting, and is case-insensitive.

SRV_CS

Bases collation sequence on the LANGUAGE setting, and is case-sensitive.

CODEPAGE

Bases collation sequence on the code page in effect, and is case-sensitive. CODEPAGE is
the default value.

In most cases, CODEPAGE is the same as BINARY. The only differences are for Danish,
Finnish, German, Norwegian, and Swedish in an EBCDIC environment.

Reference: Usage Notes for SET COLLATION

SUFFIX=FIX or SUFFIX=FOCUS/XFOCUS HOLD files created in one mode may not be usable
as targets for a JOIN in another mode if the join field is on alphanumeric data with mixed-
cases.

FIXRETRIEVE is supported only for binary data, so setting COLLATION to anything other than
BINARY will turn FIXRETRIEVE OFF, which may affect join performance.

Rules for Sorting and Aggregation

Records with the same characters in the same order, but with variations in case, are
considered to be identical. If multiple input records have these variations, the value used is
from the first such record.

In a detail level report, the sort value is the same for each output record. That value will be
the one for the input record that had the lowest value (collated first).

142

3. Sorting Tabular Reports

When the MIN (or the MAX) value for two or more alphanumeric display fields having a given
instance of the sort field values is the same by case-insensitive collation, but the two
values vary by case in some positions, the one retained is the last one in the input file
(highest input record number) when SUMPREF=LST and the first (lowest record number)
when SUMPREF=FST.

Example:

Using Binary and Case-Insensitive Collation Sequence for Sorting

The following request creates a FOCUS data source named COLLATE that has some records
with product names that differ only by the case of one letter:

CREATE FILE COLLATE
-RUN
MODIFY FILE COLLATE
FIXFORM PROD_NUM/C4 PRODNAME/C30 QTY_IN_STOCK/C7 PRICE/C12 COST/C12
CHECK OFF
DATA
10042 Hd VCR LCD Menu               43068      179.00      129.00
10052 HD VCR LCD Menu               43068      179.00      129.00
1006Combo Player - 4 HD VCR + DVD   13527      399.00      289.00
1007Combo Player - 4 Hd VCR + DVD   13527      399.00      289.00
1008DVD Upgrade Unit for Cent. VCR    199      199.00      139.00
1010750SL Digital Camcorder 300 X   10758      999.00      750.00
1012650DL Digital Camcorder 150 X    2972      899.00      710.00
1014340SX Digital Camera 65K P        990      249.00      199.00
1015340SX digital Camera 65K P        990      249.00      199.00
1016330DX Digital Camera 1024K P    12707      279.00      199.00
1018250 8MM Camcorder 40 X          60073      399.00      320.00
1019250 8mm Camcorder 40 X          60073      399.00      320.00
1020150 8MM Camcorder 20 X           5961      319.00      240.00
1022120 VHS-C Camcorder 40 X         2300      399.00      259.00
1024110 VHS-C Camcorder 20 X         4000      349.00      249.00
1026AR2 35mm Camera 8 X             12444      129.00       95.00
1029AR2 35MM Camera 8 X             11499      109.00       79.00
1028AR3 35MM Camera 10 X            11499      109.00       79.00
1030QX Portable CD Player           22000      169.00       99.00
1032R5 Micro Digital Tape Recorder   1990       89.00       69.00
1034ZT Digital PDA - Commercial     21000      499.00      349.00
1036ZC Digital PDA - Standard       33000      299.00      249.00
END

The following request prints the values of PRODNAME in the order in which they are
encountered in the input stream:

TABLE FILE COLLATE
PRINT PROD_NUM PRODNAME
END

Creating Reports With TIBCO® WebFOCUS Language

 143

Controlling Collation Sequence

On the output, the rows with product numbers 1004 and 1005 differ only in the case of the
letter d in HD. The record with the lowercase d is before the record with the uppercase D. The
rows with record numbers 1006 and 1007 also differ only in the case of the letter d in HD. In
this case, the record with the uppercase D is before the record with the lowercase d:

Product  Product
Number:  Name:
-------  -------
1004     2 Hd VCR LCD Menu
1005     2 HD VCR LCD Menu
1006     Combo Player - 4 HD VCR + DVD
1007     Combo Player - 4 Hd VCR + DVD
1008     DVD Upgrade Unit for Cent. VCR
1010     750SL Digital Camcorder 300 X
1012     650DL Digital Camcorder 150 X
1014     340SX Digital Camera 65K P
1015     340SX digital Camera 65K P
1016     330DX Digital Camera 1024K P
1018     250 8MM Camcorder 40 X
1019     250 8mm Camcorder 40 X
1020     150 8MM Camcorder 20 X
1022     120 VHS-C Camcorder 40 X
1024     110 VHS-C Camcorder 20 X
1026     AR2 35mm Camera 8 X
1029     AR2 35MM Camera 8 X
1028     AR3 35MM Camera 10 X
1030     QX Portable CD Player
1032     R5 Micro Digital Tape Recorder
1034     ZT Digital PDA - Commercial
1036     ZC Digital PDA - Standard

The next request sorts the output in BINARY order. The setting COLLATION = BINARY is in
effect:

TABLE FILE COLLATE
PRINT PROD_NUM
BY PRODNAME
END

144

3. Sorting Tabular Reports

In an EBCDIC environment, the records with the lowercase letters sort in front of the records
with the uppercase letters, so the row with product number 1007 sorts in front of the row with
product number 1006:

Product                         Product
Name:                           Number:
-------                         -------
AR2 35mm Camera 8 X             1026
AR2 35MM Camera 8 X             1029
AR3 35MM Camera 10 X            1028
Combo Player - 4 Hd VCR + DVD   1007
Combo Player - 4 HD VCR + DVD   1006
DVD Upgrade Unit for Cent. VCR  1008
QX Portable CD Player           1030
R5 Micro Digital Tape Recorder  1032
ZC Digital PDA - Standard       1036
ZT Digital PDA - Commercial     1034
110 VHS-C Camcorder 20 X        1024
120 VHS-C Camcorder 40 X        1022
150 8MM Camcorder 20 X          1020
2 Hd VCR LCD Menu               1004
2 HD VCR LCD Menu               1005
250 8mm Camcorder 40 X          1019
250 8MM Camcorder 40 X          1018
330DX Digital Camera 1024K P    1016
340SX digital Camera 65K P      1015
340SX Digital Camera 65K P      1014
650DL Digital Camcorder 150 X   1012
750SL Digital Camcorder 300 X   1010

Creating Reports With TIBCO® WebFOCUS Language

 145

Controlling Collation Sequence

In an ASCII environment, the records with the uppercase letters sort in front of the records with
the lowercase letters, so the row with product number 1005 sorts in front of the row with
product number 1004:

Product                         Product
Name:                           Number:
-------                         -------
110 VHS-C Camcorder 20 X        1024
120 VHS-C Camcorder 40 X        1022
150 8MM Camcorder 20 X          1020
2 HD VCR LCD Menu               1005
2 Hd VCR LCD Menu               1004
250 8MM Camcorder 40 X          1018
250 8mm Camcorder 40 X          1019
330DX Digital Camera 1024K P    1016
340SX Digital Camera 65K P      1014
340SX digital Camera 65K P      1015
650DL Digital Camcorder 150 X   1012
750SL Digital Camcorder 300 X   1010
AR2 35MM Camera 8 X             1029
AR2 35mm Camera 8 X             1026
AR3 35MM Camera 10 X            1028
Combo Player - 4 HD VCR + DVD   1006
Combo Player - 4 Hd VCR + DVD   1007
DVD Upgrade Unit for Cent. VCR  1008
QX Portable CD Player           1030
R5 Micro Digital Tape Recorder  1032
ZC Digital PDA - Standard       1036
ZT Digital PDA - Commercial     1034

With COLLATION set to SRV_CI and a sort on the PRODNAME field, the uppercase and
lowercase letters have the same value, so the row displays only once for multiple record
numbers. For example, the rows with product numbers 1004 and 1005 display with the same
PRODNAME value and the sort field value for the display is the first one in the input stream.

146

3. Sorting Tabular Reports

The following shows the output in an EBCDIC environment:

Product                         Product
Name:                           Number:
-------                         -------
AR2 35mm Camera 8 X             1026
                                1029
AR3 35MM Camera 10 X            1028
Combo Player - 4 HD VCR + DVD   1006
                                1007
DVD Upgrade Unit for Cent. VCR  1008
QX Portable CD Player           1030
R5 Micro Digital Tape Recorder  1032
ZC Digital PDA - Standard       1036
ZT Digital PDA - Commercial     1034
110 VHS-C Camcorder 20 X        1024
120 VHS-C Camcorder 40 X        1022
150 8MM Camcorder 20 X          1020
2 Hd VCR LCD Menu               1004
                                1005
250 8MM Camcorder 40 X          1018
250 8MM Camcorder 40 X          1019
330DX Digital Camera 1024K P    1016
340SX Digital Camera 65K P      1014
                                1015
650DL Digital Camcorder 150 X   1012
750SL Digital Camcorder 300 X   1010

Creating Reports With TIBCO® WebFOCUS Language

 147

Controlling Collation Sequence

The following shows the output in an ASCII environment:

Product                         Product
Name:                           Number:
-------                         -------
110 VHS-C Camcorder 20 X        1024
120 VHS-C Camcorder 40 X        1022
150 8MM Camcorder 20 X          1020
2 Hd VCR LCD Menu               1004
                                1005
250 8MM Camcorder 40 X          1018
                                1019
330DX Digital Camera 1024K P    1016
340SX Digital Camera 65K P      1014
                                1015
650DL Digital Camcorder 150 X   1012
750SL Digital Camcorder 300 X   1010
AR2 35mm Camera 8 X             1026
                                1029
AR3 35MM Camera 10 X            1028
Combo Player - 4 HD VCR + DVD   1006
                                1007
DVD Upgrade Unit for Cent. VCR  1008
QX Portable CD Player           1030
R5 Micro Digital Tape Recorder  1032
ZC Digital PDA - Standard       1036
ZT Digital PDA - Commercial     1034

Example:

Using Binary and Case-Insensitive Collation Sequence for Selection

The following request against the COLLATE data source selects records in which the
PRODNAME contains the characters 'HD':

TABLE FILE COLLATE
PRINT PROD_NUM PRODNAME
WHERE PRODNAME CONTAINS 'HD'
END

With COLLATION set to BINARY, only the records with an exact match (uppercase HD) are
selected. The output is:

Product  Product
Number:  Name:
-------  -------
1005     2 HD VCR LCD Menu
1006     Combo Player - 4 HD VCR + DVD

Running the same request but changing the COLLATION parameter to SRV_CI selects all
records with any combination of uppercase and lowercase values for H and D. The rows are
displayed in the order in which they appeared in the data source:

148

3. Sorting Tabular Reports

Product  Product
Number:  Name:
-------  -------
1004     2 Hd VCR LCD Menu
1005     2 HD VCR LCD Menu
1006     Combo Player - 4 HD VCR + DVD
1007     Combo Player - 4 Hd VCR + DVD

Specifying the Sort Order

Sort field values are automatically displayed in ascending order, beginning with the lowest
value and continuing to the highest. The default sorting sequence varies for operating systems.
On z/OS it is a-z, A-Z, 0-9 for alphanumeric fields; 0-9 for numeric fields. On UNIX and Windows
it is 0-9, A-Z, a-z for alphanumeric fields; 0-9 for numeric fields.

You have the option of overriding this default and displaying values in descending order,
ranging from the highest value to the lowest value, by including HIGHEST in the sort phrase.

Syntax:

How to Specify the Sort Order

{BY|ACROSS} {LOWEST|HIGHEST} sortfield

where:

LOWEST

Sorts in ascending order, beginning with the lowest value and continuing to the highest
value (a-z, A-Z, 0-9 for alphanumeric fields; 0-9 for numeric fields). This option is the
default.

HIGHEST

Sorts in descending order, beginning with the highest value and continuing to the lowest
value. You can also use TOP as a synonym for HIGHEST.

sortfield

Is the name of the sort field.

Example:

Sorting in Ascending Order

The following report request does not specify a particular sorting order, and so, by default, it
lists salaries ranging from the lowest to the highest.

TABLE FILE EMPLOYEE
PRINT LAST_NAME
BY CURR_SAL
END

Creating Reports With TIBCO® WebFOCUS Language

 149

Specifying the Sort Order

You can specify this same ascending order explicitly by including LOWEST in the sort phrase.

TABLE FILE EMPLOYEE
PRINT LAST_NAME
BY LOWEST CURR_SAL
END

The output is:

Example:

Sorting in Descending Order

The following request lists salaries ranging from the highest to lowest.

TABLE FILE EMPLOYEE
PRINT LAST_NAME
BY HIGHEST CURR_SAL
END

150

The output is:

3. Sorting Tabular Reports

Specifying Your Own Sort Order

Sort field values are automatically displayed in ascending order, beginning with the lowest
value and continuing to the highest.

You can override the default order and display values in your own user-defined sorting
sequence. To do this, you need to decide the following:

1. Which sort field values you want to allow. You can specify every sort field value, or a subset
of values. When you issue your report request, only records containing those values are
included in the report.

2. The order in which you want the values to appear. You can specify any order. For example,
you could specify that an A1 sort field containing a single-letter code be sorted in the order
A, Z, B, C, Y, and so on.

There are two ways to specify your own sorting order, depending on whether you are sorting
rows with BY, or sorting columns with ACROSS:

The BY ROWS OVER phrase, for defining your own row sort sequence.

The ACROSS COLUMNS AND phrase, for defining your own column sort sequence.

Syntax:

How to Define Your Own Sort Order

BY sortfield AS 'coltitle' ROWS value1 [AS 'text1']
OVER value2 [AS 'text2']
[... OVER valuen [ AS 'textn']]
END

Creating Reports With TIBCO® WebFOCUS Language

 151

Specifying the Sort Order

where:

sortfield

Is the last BY field in the report.

coltitle

Is the column title for the BY field on the report output.

value1

Is the sort field value that is first in the sorting sequence.

AS 'text1'

Enables you to assign alternate text for the first row, which replaces the field value in the
output. Enclose the text in single quotation marks.

value2

Is the sort field value that is second in the sorting sequence.

AS 'text2'

Enables you to assign alternate text for the second row, which replaces the field value in
the output. Enclose the text in single quotation marks.

valuen

Is the sort field value that is last in the sorting sequence.

AS 'textn'

Enables you to assign alternate text for the last row, which replaces the field value in the
output. Enclose the text in single quotation marks.

An alternative syntax is

FOR sortfield
value1 OVER value2 [... OVER valuen]

which uses the row-based reporting phrase FOR, described in Creating Financial Reports With
Financial Modeling Language (FML) on page 1817.

Reference: Usage Notes for Defining Your Sort Order

Any sort field value that you do not specify in the BY ROWS OVER phrase is not included in
the sorting sequence, and does not appear in the report.

Sort field values that contain embedded blank spaces should be enclosed in single
quotation marks (').

152

3. Sorting Tabular Reports

Any sort field value that you do specify in the BY ROWS OVER phrase is included in the
report, whether or not there is data.

If missing data is included in the report, it must be inserted at the lowest sort level.

The name of the sort field is not included in the report.

Each report request can contain only one BY ROWS OVER phrase. BY ROWS OVER is not
supported with the FOR phrase. For information about the FOR phrase, see Creating
Financial Reports With Financial Modeling Language (FML) on page 1817.

Example:

Defining Your Row Sort Order

The following illustrates how to sort employees by the banks at which their paychecks are
automatically deposited, and how to define your own label in the sorting sequence for the bank
field.

TABLE FILE EMPLOYEE
PRINT LAST_NAME
BY BANK_NAME ROWS 'BEST BANK' OVER STATE
   OVER ASSOCIATED OVER 'BANK ASSOCIATION'
END

The output is:

Syntax:

How to Define Column Sort Sequence

ACROSS sortfield COLUMNS value1 AND value2 [... AND valuen]

where:

sortfield

Is the name of the sort field.

value1

Is the sort field value that is first in the sorting sequence.

Creating Reports With TIBCO® WebFOCUS Language

 153

Specifying the Sort Order

value2

Is the sort field value that is second in the sorting sequence.

valuen

Is the sort field value that is last in the sorting sequence.

Reference: Usage Notes for Defining Column Sort Sequence

Any sort field value that you do not specify in the ACROSS COLUMNS AND phrase is not
included in the label within the sorting sequence, and does not appear in the report.

Sort field values that contain embedded blank spaces should be enclosed in single
quotation marks.

Any sort field value that you do specify in the ACROSS COLUMNS AND phrase is included in
the report, whether or not there is data.

When using a COMPUTE with an ACROSS COLUMNS phrase, the COLUMNS should be
specified last:

ACROSS acrossfield [AND] COMPUTE compute_expression; COLUMNS values

Each report request may contain only one BY ROWS OVER phrase.

Example:

Defining Column Sort Sequence

The following illustrates how to sum employee salaries by the bank at which they are
automatically deposited, and to define your own label within the sorting sequence for the bank
field.

TABLE FILE EMPLOYEE
SUM CURR_SAL
ACROSS BANK_NAME COLUMNS 'BEST BANK' AND STATE
   AND ASSOCIATED AND 'BANK ASSOCIATION'
END

The output is:

BANK_NAME

BEST BANK          STATE              ASSOCIATED         BANK ASSOCIATION
-------------------------------------------------------------------------
     $29,700.00         $18,480.00         $64,742.00         $27,062.00

154


3. Sorting Tabular Reports

Selecting and Assigning Column Titles to ACROSS Values

When you use the ACROSS COLUMNS phrase to select and order the columns that display on
the report output for an ACROSS sort field, you can assign each selected column a new
column title using an AS phrase.

Syntax:

How to Assign Column Titles To ACROSS Values

ACROSS sortfield [AS title]
 COLUMNS aval1 [AS val1title] [{AND|OR} aval2 [AS val2title] [... {AND|
OR} avaln [AS valntitle]]]

where:

sortfield

Is the ACROSS field name.

title

Is the title for the ACROSS field name.

AND|OR

Is required to separate the selected ACROSS values. AND and OR are synonyms for this
purpose.

aval1, aval2,... avaln

Are the selected ACROSS values to display on the report output.

val1title, val2title ...valntitle

Are the column titles for the selected ACROSS values.

Reference: Usage Notes for Assigning Column Titles to ACROSS Values

Any value you specify as an ACROSS value in the sort phrase will appear on the report
output, even if the value is screened out by an IF or WHERE test, or if the value does not
exist at all in the data source.

Note: For styled output formats, SET HIDENULLACRS=ON removes empty columns in
ACROSS groups from the report output.

Column titles for ACROSS fields appear on a single line of the report output.

Support for AS names for ACROSS values is limited to the TABLE FILE command.

Creating Reports With TIBCO® WebFOCUS Language

 155

Ranking Sort Field Values

When you create a HOLD file with SET ASNAMES = ON, the original field name is
propagated to the output Master File, not the AS name.

Example:

Selecting and Assigning Column Titles to ACROSS Values

The following request against the GGSALES data source selects the columns Coffee Grinder,
Latte, and Coffee Pot for the ACROSS field PRODUCT, and assigns each of them a new column
title:

 TABLE FILE GGSALES
 SUM
 DOLLARS/I8M AS ''
 BY REGION
 ACROSS PRODUCT  AS 'Products'
   COLUMNS 'Coffee Grinder' AS 'Grinder'
    OR Latte AS 'caffellatte'
    AND 'Coffee Pot' AS 'Carafe'
ON TABLE SET PAGE NOPAGE
END

The output is:

             Products
             Grinder          caffellatte      Carafe
Region
----------------------------------------------------------------
Midwest         $666,622       $2,883,566         $599,878
Northeast       $509,200       $2,808,855         $590,780
Southeast       $656,957       $2,637,562         $645,303
West            $603,436       $2,670,405         $613,624

Ranking Sort Field Values

When you sort report rows using the BY phrase, you can indicate the numeric rank of each row.
Ranking sort field values is frequently combined with restricting sort field values by rank.

Note that it is possible for several report rows to have the same rank if they have identical sort
field values.

The default column title for RANKED BY is RANK. You can change the title using an AS phrase.
The RANK field has format I7. Therefore, the RANK column in a report can be up to seven
digits. For more information, see Using Headings, Footings, Titles, and Labels on page 1517.

You can rank aggregated values using the syntax RANKED BY TOTAL. For details, see Sorting
and Aggregating Report Columns on page 173.

156

Syntax:

How to Rank Sort Field Values

RANKED [AS 'name'] BY  {HIGHEST|LOWEST} [n]  sortfield [AS 'text']

3. Sorting Tabular Reports

where:

name

Is the new name for the RANK column title.

sortfield

Is the name of the sort field. The field can be numeric or alphanumeric.

n

Is the number of rank categories to display on the report output.

text

Is the column heading to use for the sort field column on the report output.

Example:

Ranking Sort Field Values

Issue the following request to display a list of employee names in salary order, indicating the
rank of each employee by salary. Note that employees Jones and McCoy have the same rank
since their current salary is the same.

TABLE FILE EMPLOYEE
PRINT LAST_NAME
RANKED AS 'Sequence' BY CURR_SAL
END

Creating Reports With TIBCO® WebFOCUS Language

 157

Ranking Sort Field Values

The output is:

Example:

Ranking and Restricting Sort Field Values

Ranking sort field values is frequently combined with restricting sort field values by rank, as in
the following example.

TABLE FILE EMPLOYEE
PRINT LAST_NAME
RANKED BY HIGHEST 5 CURR_SAL
END

The output is:

RANK         CURR_SAL  LAST_NAME
----         --------  ---------
   1       $29,700.00  BANNING
   2       $27,062.00  CROSS
   3       $26,862.00  IRVING
   4       $21,780.00  BLACKWOOD
   5       $21,120.00  ROMANS

DENSE and SPARSE Ranking

The WebFOCUS sort phrases RANK BY and BY {HIGHEST|LOWEST} n sort the report output and
assign rank numbers to the sequence of data values. When assigning a rank to a data value,
by default WebFOCUS does not skip rank numbers. This means that even when multiple data
values are assigned the same rank, the rank number for the next group of values is the next
sequential integer. This method of assigning rank numbers is called dense.

158

3. Sorting Tabular Reports

Some of the relational engines assign rank numbers using a method called sparse. With
sparse ranking, if multiple data values are assigned the same rank number, the next rank
number will be the previous rank number plus the number of multiples.

You can use the WebFOCUS RANK parameter to control the type of ranking done by
WebFOCUS. In addition, if you are accessing a relational data source, you can set the ranking
method to the type of ranking done by your relational engine so that the rank calculation can
be optimized. Some relational engines have functions for both dense and sparse ranking. In
this case, either setting can be optimized.

Reference: Optimizing Ranking

In order to pass rank processing to a relational engine your request must:

Use the SUM (or WRITE or ADD) command to aggregate values.

Specify the number of rank categories to be displayed. That is, you must specify a value for
n:

[RANKED] BY [HIGHEST] n

Syntax:

How to Control the Ranking Method

SET RANK={DENSE|SPARSE}

where:

DENSE

Specifies dense ranking. With this method, each rank number is the next sequential
integer, even when the same rank is assigned to multiple data values. DENSE is the
default value.

SPARSE

Specifies sparse ranking. With this method, if the same rank number is assigned to
multiple data values, the next rank number will be the previous rank number plus the
number of multiples.

Then, in your request, use one of the following forms of the BY phrase:

RANKED BY {HIGHEST|LOWEST} [n] sortfield [AS 'text']

or

BY {HIGHEST|LOWEST} n sortfield [AS 'text']

Creating Reports With TIBCO® WebFOCUS Language

 159

Ranking Sort Field Values

where:

n

Is the highest rank number to display on the report output when the RANKED BY phrase is
used. When RANKED is not used, it is the number of distinct sort field values to display on
the report output when SET RANK=DENSE, and the total number of lines of output for the
sort field when SET RANK=SPARSE.

sortfield

Is the name of the sort field.

text

Is the column heading to be used for the sort field column on the report output.

Reference: Usage Notes for SET RANK

The RNK. prefix operator is not affected by the RANK parameter.

The rank numbers propagated to a HOLD file depend on the RANK parameter setting.

Example:

Ranking Values in a FOCUS Data Source

The following request against the EMPDATA data source ranks salaries in descending order by
division. The RANK parameter is set to DENSE (the default).

SET RANK = DENSE
TABLE FILE EMPDATA
PRINT LASTNAME FIRSTNAME
RANKED BY HIGHEST 12 SALARY
BY DIV
ON TABLE SET PAGE NOPAGE
END

160

On the output, six employees are included in rank number 6. With dense ranking, the next rank
number is the next highest integer, 7.

3. Sorting Tabular Reports

RANK           SALARY  DIV   LASTNAME         FIRSTNAME
----           ------  ---   --------         ---------
   1      $115,000.00  CE    LASTRA           KAREN
   2       $83,000.00  CORP  SANCHEZ          EVELYN
   3       $80,500.00  SE    NOZAWA           JIM
   4       $79,000.00  CORP  SOPENA           BEN
   5       $70,000.00  WE    CASSANOVA        LOIS
   6       $62,500.00  CE    ADAMS            RUTH
                       CORP  CVEK             MARCUS
                             WANG             JOHN
                       NE    WHITE            VERONICA
                       SE    BELLA            MICHAEL
                             HIRSCHMAN        ROSE
   7       $58,800.00  WE    GOTLIEB          CHRIS
   8       $55,500.00  CORP  VALINO           DANIEL
                       NE    PATEL            DORINA
   9       $54,100.00  CE    ADDAMS           PETER
                       WE    FERNSTEIN        ERWIN
  10       $52,000.00  NE    LIEBER           JEFF
  11       $50,500.00  SE    LEWIS            CASSANDRA
  12       $49,500.00  CE    ROSENTHAL        KATRINA
                       SE    WANG             KATE

Running the same request with SET RANK=SPARSE produces the following output. Since rank
category 6 includes six employees, the next rank number is 6 + 6.

RANK           SALARY  DIV   LASTNAME         FIRSTNAME
----           ------  ---   --------         ---------
   1      $115,000.00  CE    LASTRA           KAREN
   2       $83,000.00  CORP  SANCHEZ          EVELYN
   3       $80,500.00  SE    NOZAWA           JIM
   4       $79,000.00  CORP  SOPENA           BEN
   5       $70,000.00  WE    CASSANOVA        LOIS
   6       $62,500.00  CE    ADAMS            RUTH
                       CORP  CVEK             MARCUS
                             WANG             JOHN
                       NE    WHITE            VERONICA
                       SE    BELLA            MICHAEL
                             HIRSCHMAN        ROSE
  12       $58,800.00  WE    GOTLIEB          CHRIS

Creating Reports With TIBCO® WebFOCUS Language

 161

Ranking Sort Field Values

Example:

Limiting the Number of Sort Field Values

The following request against the EMPDATA data source sorts salaries in descending order by
division and prints the 12 highest salaries. The RANK parameter is set to DENSE (the default).

SET RANK = DENSE
TABLE FILE EMPDATA
PRINT LASTNAME FIRSTNAME
BY HIGHEST 12 SALARY
BY DIV
ON TABLE SET PAGE NOPAGE
END

On the output, 12 distinct salary values are displayed, even though some of the employees
have the same salaries.

     SALARY  DIV   LASTNAME         FIRSTNAME
     ------  ---   --------         ---------
$115,000.00  CE    LASTRA           KAREN
 $83,000.00  CORP  SANCHEZ          EVELYN
 $80,500.00  SE    NOZAWA           JIM
 $79,000.00  CORP  SOPENA           BEN
 $70,000.00  WE    CASSANOVA        LOIS
 $62,500.00  CE    ADAMS            RUTH
             CORP  CVEK             MARCUS
                   WANG             JOHN
             NE    WHITE            VERONICA
             SE    BELLA            MICHAEL
                   HIRSCHMAN        ROSE
 $58,800.00  WE    GOTLIEB          CHRIS
 $55,500.00  CORP  VALINO           DANIEL
             NE    PATEL            DORINA
 $54,100.00  CE    ADDAMS           PETER
             WE    FERNSTEIN        ERWIN
 $52,000.00  NE    LIEBER           JEFF
 $50,500.00  SE    LEWIS            CASSANDRA
 $49,500.00  CE    ROSENTHAL        KATRINA
             SE    WANG             KATE

162

3. Sorting Tabular Reports

Running the same request with SET RANK=SPARSE produces the following output. Since six
employees have salary $62,500, that value is counted 6 times so that only 12 lines (seven
distinct salary values) display on the output.

     SALARY  DIV   LASTNAME         FIRSTNAME
     ------  ---   --------         ---------
$115,000.00  CE    LASTRA           KAREN
 $83,000.00  CORP  SANCHEZ          EVELYN
 $80,500.00  SE    NOZAWA           JIM
 $79,000.00  CORP  SOPENA           BEN
 $70,000.00  WE    CASSANOVA        LOIS
 $62,500.00  CE    ADAMS            RUTH
             CORP  CVEK             MARCUS
                   WANG             JOHN
             NE    WHITE            VERONICA
             SE    BELLA            MICHAEL
                   HIRSCHMAN        ROSE
 $58,800.00  WE    GOTLIEB          CHRIS

Grouping Numeric Data Into Ranges

When you sort a report using a numeric sort field, you can group the sort field values together
and define the range of each group.

There are several ways of defining groups. You can define groups of:

Equal range using the IN-GROUPS-OF phrase.

Each report request can contain a total of five IN-GROUPS-OF phrases plus IN-RANGES-OF
phrases. The IN-GROUPS-OF phrase can only be used once per BY field. The first sort field
range starts from the lowest value of a multiple of the IN-GROUPS-OF value, and the value
displayed is the start point of each range.

Equal range using the IN-RANGES-OF phrase.

Each report request can contain a total of five IN-GROUPS-OF phrases plus IN-RANGES-OF
phrases. The IN-RANGES-OF phrase can only be used once per BY field, and it generates an
additional internal sort phrase that must be counted in the total number of sort phrases.
The first sort field range starts from the lowest value of a multiple of the IN-GROUPS-OF
value. No message is generated if you specify a range of zero, but the values displayed on
the report are unpredictable.

Unequal range using the FOR phrase.

Tiles. These include percentiles, quartiles, or deciles. For details, see Grouping Numeric
Data Into Tiles on page 167.

Creating Reports With TIBCO® WebFOCUS Language

 163

Grouping Numeric Data Into Ranges

The FOR phrase is usually used to produce matrix reports and is part of the Financial Modeling
Language (FML). However, you can also use it to create columnar reports that group sort field
values in unequal ranges.

The FOR phrase displays the sort value for each individual row. The ranges do not have to be
contiguous, that is, you can define your ranges with gaps between them. The FOR phrase is
described in more detail in Creating Financial Reports With Financial Modeling Language (FML)
on page 1817.

Note: If there is not any data for a group, a row for the group still appears in the report.

Syntax:

How to Define Groups of Equal Range

{BY|ACROSS} sortfield IN-GROUPS-OF value [TOP limit]

where:

sortfield

Is the name of the sort field. The sort field must be numeric: its format must be I (integer),
F (floating-point number), D (decimal number), or P (packed number).

value

Is a positive integer that specifies the range by which sort field values are grouped.

limit

Is an optional number that defines the highest group label to be included in the report.

Example:

Defining Groups of Equal Ranges

The following illustrates how to show which employees fall into which salary ranges, and to
define the ranges by $5,000 increments.

TABLE FILE EMPLOYEE
PRINT LAST_NAME
BY CURR_SAL IN-GROUPS-OF 5000
END

164

3. Sorting Tabular Reports

The output is:

  CURR_SAL  LAST_NAME
  --------  ---------
 $5,000.00  SMITH
            GREENSPAN
$10,000.00  STEVENS
            SMITH
$15,000.00  JONES
            MCCOY
            MCKNIGHT
$20,000.00  ROMANS
            BLACKWOOD
$25,000.00  BANNING
            IRVING
            CROSS

Syntax:

How to Define Equal Ranges

{BY|ACROSS} sortfield IN-RANGES-OF value [TOP limit]

where:

sortfield

Is the name of the sort field. The sort field must be numeric: its format must be I (Integer),
F (floating-point), D (double-precision), or P (packed).

value

Is an integer greater than zero indicating the range by which sort field values are grouped.

limit

Is an optional number that defines the highest range label to be included in the report. The
range is extended to include all data values higher than this value.

Note: IN-RANGES-OF generates an internal sort phrase that must be counted in the total
number of sort phrases.

Example:

Defining Equal Ranges

TABLE FILE EMPLOYEE
PRINT LAST_NAME
BY CURR_SAL IN-RANGES-OF 5000
END

Creating Reports With TIBCO® WebFOCUS Language

 165

Grouping Numeric Data Into Ranges

The output is:

Syntax:

How to Define Custom Groups of Data Values

FOR sortfield
begin1 TO end1 [OVER begin2 TO end2 ... ]

where:

sortfield

Is the name of the sort field.

begin

Is a value that identifies the beginning of a range.

end

Is a value that identifies the end of a range.

166

Example:

Defining Custom Groups of Data Values

The following request displays employee salaries, but it groups them in an arbitrary way. Notice
that the starting value of each range prints in the report.

3. Sorting Tabular Reports

TABLE FILE EMPLOYEE
PRINT LAST_NAME
FOR CURR_SAL
9000 TO 13500 OVER
14000 TO 19700 OVER
19800 TO 30000
END

The output is:

Grouping Numeric Data Into Tiles

You can group numeric data into any number of tiles (percentiles, deciles, quartiles, etc.) in
tabular reports. For example, you can group student test scores into deciles to determine
which students are in the top ten percent of the class, or determine which sales
representatives are in the top half of all sales representatives based on total sales.

Grouping is based on the values in the selected vertical (BY) field, and data is apportioned as
equally as possible into the number of tile groups you specify.

The following occurs when you group data into tiles:

A new column, labeled TILE by default, is added to the report output and displays the tile
number assigned to each instance of the tile field. You can change the column heading
with an AS phrase. For details on the AS phrase, see Using Headings, Footings, Titles, and
Labels on page 1517.

Creating Reports With TIBCO® WebFOCUS Language

 167

Grouping Numeric Data Into Ranges

Tiling is calculated within all of the higher-level sort fields in the request, and restarts
whenever a sort field at a higher level than the tile field value changes.

Instances are counted using the tile field. If the request prints fields from lower level
segments, there may be multiple report lines that correspond to one instance of the tile
field.

Instances with the same tile field value are placed in the same tile. For example, consider
the following data, which is to be apportioned into three tiles:

1 5 5 5 8 9

In this case, dividing the instances into groups containing an equal number of records
produces the following:

Group

1

2

3

Data Values

1,5

5,5

8,9

However, because all of the same data values must be in the same tile, the fives (5) that
are in group 2 are moved to group 1. Group 2 remains empty. The final tiles are:

Tile Number

1

2

3

Data Values

1,5,5,5

8,9

Syntax:

How to Group Numeric Data Into Tiles

BY [ {HIGHEST|LOWEST} [k] ] tilefield [AS 'head1']
         IN-GROUPS-OF n TILES [TOP m] [AS 'head2']

where:

HIGHEST

Sorts the data in descending order so that the highest data values are placed in tile 1.

168

3. Sorting Tabular Reports

LOWEST

Sorts the data in ascending order so that the lowest data values are placed in tile 1. This
is the default sort order.

k

Is a positive integer representing the number of tile groups to display in the report. For
example, BY HIGHEST 2 displays the two non-empty tiles with the highest data values.

tilefield

Is the field whose values are used to assign the tile numbers.

head1

Is a heading for the column that displays the values of the tile sort field.

n

m

Is a positive integer not greater than 32,767, specifying the number of tiles to be used in
grouping the data. For example, 100 tiles produces percentiles, while 10 tiles produces
deciles.

Is a positive integer indicating the highest tile value to display in the report. For example,
TOP 3 does not display any data row that is assigned a tile number greater than 3.

head2

Is a new heading for the column that displays the tile numbers.

Note:

The syntax accepts numbers that are not integers for k, n, and m. On z/OS, values with
decimals are rounded to integers; on UNIX and Windows they are truncated. If the numbers
supplied are negative or zero, an error message is generated.

Both k and m limit the number of rows displayed within each sort break in the report. If you
specify both, the more restrictive value controls the display. If k and m are both greater
than n (the number of tiles), n is used.

Creating Reports With TIBCO® WebFOCUS Language

 169

Grouping Numeric Data Into Ranges

Example:

Grouping Data Into Five Tiles

The following illustrates how to group data into five tiles.

TABLE FILE EMPLOYEE
PRINT LAST_NAME FIRST_NAME
BY DEPARTMENT
BY CURR_SAL IN-GROUPS-OF 5 TILES
END

The output is:

Note that the tiles are assigned within the higher-level sort field DEPARTMENT. The MIS
category does not have any data assigned to tile 3. The PRODUCTION category has all five
tiles.

Example:

Displaying the First Three Tile Groups

In this example, the employees with the three lowest salaries are grouped into five tiles.

TABLE FILE EMPLOYEE
PRINT LAST_NAME FIRST_NAME
BY DEPARTMENT
BY LOWEST 3 CURR_SAL IN-GROUPS-OF 5 TILES
END

170

The output is:

3. Sorting Tabular Reports

Note that the request displays three tile groups in each category. Because no data was
assigned to tile 3 in the MIS category, tiles 1, 2, and 4 display for that category.

Example:

Displaying Tiles With a Value of Three or Less

In this example, the employees with the three lowest salaries are listed and grouped into five
tiles, but only the tiles that are in the top 3 (tiles 1, 2, or 3) are displayed in the report. Also,
the heading for the TILES field has been renamed (using the AS phrase) to DECILES.

TABLE FILE EMPLOYEE
PRINT LAST_NAME FIRST_NAME
BY DEPARTMENT
BY LOWEST 3 CURR_SAL IN-GROUPS-OF 5 TILES TOP 3 AS DECILES
END

The output is:

Because no data was assigned to tile 3 in the MIS category, only tiles 1 and 2 display for that
category.

Creating Reports With TIBCO® WebFOCUS Language

 171

Restricting Sort Field Values by Highest/Lowest Rank

Reference: Usage Notes for Tiles

If a request retrieves data from segments that are descendants of the segment containing
the tile field, multiple report rows may correspond to one instance of the tile field. These
additional report rows do not affect the number of instances used to assign the tile values.
However, if you retrieve fields from multiple segments and create a single-segment output
file, this flat file will have multiple instances of the tile field, and this increased number of
instances may affect the tile values assigned. Therefore, when you run the same request
against the multi-level file and the single-segment file, different tile assignments may
result.

Tiles are always calculated on a BY sort field in the request.

Only one tiles calculation is supported per request. However, the request can contain up to
five (the maximum allowed) non-tile IN-GROUP-OF phrases in addition to the TILES phrase.

Comparisons for the purpose of assigning tile numbers use exact data values regardless of
their display format. Therefore, if you display a floating-point value as D7, you may not be
showing enough significant digits to indicate why values are placed in separate tiles.

The tile field can be a real field or a virtual field created with a DEFINE command or a
DEFINE in the Master File. The COMPUTE command cannot be used to create a tile field.

Empty tiles do not display in the report output.

In requests with multiple sort fields, tiles are supported only at the lowest level and only
with the BY LOWEST phrase.

Tiles are supported with output files. However, the field used to calculate the tiles
propagates three fields to a HOLD file (the actual field value, the tile, and a ranking field)
unless you set HOLDLIST to PRINTONLY.

Tiles are not supported with BY TOTAL, TABLEF, FML, and GRAPH.

Restricting Sort Field Values by Highest/Lowest Rank

When you sort report rows using the BY phrase, you can restrict the sort field values to a group
of high or low values. You choose the number of fields to include in the report. For example,
you can choose to display only the 10 highest (or lowest) sort field values in your report by
using BY HIGHEST (or LOWEST).

You can have up to five sort fields with BY HIGHEST or BY LOWEST.

172

3. Sorting Tabular Reports

Syntax:

How to Restrict Sort Field Values by Highest/Lowest Rank

BY {HIGHEST n|LOWEST n} sortfield

where:

HIGHEST n

Specifies that only the highest n sort field values are included in the report. TOP is a
synonym for HIGHEST.

LOWEST n

Specifies that only the lowest n sort field values are included in the report.

sortfield

Is the name of the sort field. The sort field can be numeric or alphanumeric.

Note: HIGHEST/LOWEST n refers to the number of sort field values, not the number of report
rows. If several records have the same sort field value that satisfies the HIGHEST/LOWEST n
criteria, all of them are included in the report.

Example:

Restricting Sort Field Values to a Group

The following request displays the names of the employees earning the five highest salaries.

TABLE FILE EMPLOYEE
PRINT LAST_NAME
BY HIGHEST 5 CURR_SAL
END

The output is:

Sorting and Aggregating Report Columns

Using the BY TOTAL phrase, you can apply aggregation and sorting simultaneously to numeric
columns in your report in one pass of the data. For BY TOTAL to work correctly, you must have
an aggregating display command such as SUM. A non-aggregating display command, such as
PRINT, simply retrieves the data without aggregating it. Records are sorted in either ascending
or descending sequence, based on your query. Ascending order is the default.

Creating Reports With TIBCO® WebFOCUS Language

 173

Sorting and Aggregating Report Columns

You can also use the BY TOTAL phrase to sort based on temporary values calculated by the
COMPUTE command.

Note: On z/OS, the sort on the aggregated value is calculated using an external sort package,
even if EXTSORT = OFF.

Syntax:

How to Sort and Aggregate a Report Column

[RANKED] BY [HIGHEST|LOWEST [n] ]
         TOTAL {display_field|COMPUTE name/format=expression;}

or

[RANKED] BY TOTAL {[HIGHEST|LOWEST [n] ]
        display_field|COMPUTE name/format=expression;}

where:

RANKED

Adds a column to the report in which a rank number is assigned to each aggregated sort
value in the report output. If multiple rows have the same ranking, the rank number only
appears in the first row.

n

Is the number of sort field values you wish to display in the report. If n is omitted, all
values of the calculated sort field are displayed. The default order is from lowest to
highest.

display_field

Can be a field name, a field name preceded by an operator (that is,
prefixoperator.fieldname), or a calculated value.

A BY TOTAL field is treated as a display field when the internal matrix is created. After the
matrix is created, the output lines are aggregated and re-sorted based on all of the sort
fields.

Example:

Sorting and Aggregating Report Columns

In this example, the salary average is calculated and used as a sort field. The two highest
salaries are displayed in the report.

TABLE FILE EMPLOYEE
SUM SALARY CNT.SALARY
BY DEPARTMENT
BY HIGHEST 2 TOTAL AVE.SALARY AS 'HIGHEST,AVERAGE,SALARIES'
BY CURR_JOBCODE
END

174

The output is:

3. Sorting Tabular Reports

Example:

Sorting, Aggregating, and Ranking Report Columns

In this example, the salary average is calculated and used as a sort field. The two highest
salaries are displayed and ranked.

TABLE FILE EMPLOYEE
SUM SALARY CNT.SALARY
BY DEPARTMENT
RANKED BY HIGHEST 2 TOTAL AVE.SALARY AS 'HIGHEST,AVERAGE,SALARIES'
BY CURR_JOBCODE
END

The output is:

Example:

Sorting and Aggregating Report Columns With COMPUTE

In this example, the monthly salary is calculated using a COMPUTE within a sort field. The two
highest monthly salaries are displayed.

TABLE FILE EMPLOYEE
SUM SALARY CNT.SALARY
BY DEPARTMENT
BY HIGHEST 2 TOTAL COMPUTE MONTHLY_SALARY/D12.2M=SALARY/12;
AS 'HIGHEST,MONTHLY,SALARIES'
BY CURR_JOBCODE
END

Creating Reports With TIBCO® WebFOCUS Language

 175

Sorting and Aggregating Report Columns

The output is:

Example:

Using BY TOTAL on a Calculated Value With an ACROSS Phrase

The following request creates the calculated value PROFIT and uses it in the BY TOTAL phrase.
The request also has an ACROSS RATING phrase.

TABLE FILE MOVIES
SUM LISTPR WHOLESALEPR
COMPUTE
PROFIT = LISTPR - WHOLESALEPR;
BY CATEGORY
BY TOTAL PROFIT
ACROSS RATING
WHERE  RATING NE 'NR' OR 'R'
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *GRID = OFF,$
ENDSTYLE
END

The output is shown in the following image.

Reference: Usage Notes for BY TOTAL

When you use BY HIGHEST/LOWEST n with BY TOTAL HIGHEST/LOWEST n, the BY TOTAL
phrase works on the result of the BY phrase (that is, on the n rows that result from the BY
phrase).

176

3. Sorting Tabular Reports

Hiding Sort Values

When you sort a report, you can omit the sort field value itself from the report by using the
phrase NOPRINT. This can be helpful in several situations; for instance, when you use the
same field as a sort field and a display field, or when you want to sort by a field but not display
its values in the report output.

Syntax:

How to Hide Sort Values

{BY|ACROSS} sortfield {NOPRINT|SUP-PRINT}

where:

sortfield

Is the name of the sort field.

You can use SUP-PRINT as a synonym for NOPRINT.

Example:

Hiding Sort Values

If you want to display a list of employees sorted by the date on which they were hired, but you
want the report to contain last name, first name, and then the hire date in the third column,
the following request is insufficient.

TABLE FILE EMPLOYEE
PRINT LAST_NAME FIRST_NAME HIRE_DATE
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 177

Sort Performance Considerations

To list the employees in the order in which they were hired, you would sort the report by the
HIRE_DATE field and hide the sort field occurrence using the NOPRINT phrase.

TABLE FILE EMPLOYEE
PRINT LAST_NAME FIRST_NAME HIRE_DATE
BY HIRE_DATE NOPRINT
END

The output is:

Sort Performance Considerations

The sorting procedure analyzes the request being processed and the amount of sort memory
available in order reduce the amount of disk I/O. The sort strategy is controlled by the
specifics of the request and the values of the SORTMATRIX and SORTMEMORY parameters.

SORTMATRIX

The SORTMATRIX parameter controls whether to employ in-memory sorting with decreased use
of external memory. The syntax is

SET SORTMATRIX = {SMALL|LARGE}

178

3. Sorting Tabular Reports

where:

SMALL

Creates a single sort matrix of up to 2048 rows, and uses a binary search based insertion
sort with aggregation during retrieval. The maximum number of rows in this matrix has
been determined to provide the best performance for this type of sort. If the sort matrix
becomes full, it is written to a file called FOCSORT on disk, the in-memory matrix is
emptied, and retrieval continues, writing to FOCSORT as many times as necessary. When
the end of data is detected, the remaining rows are written to FOCSORT and the merge
routine merges all of the sort strings in FOCSORT (which, in extreme cases, may require
multiple merge phases), while also completing the aggregation.

LARGE

Creates a large matrix or multiple small matrices in memory, when adequate memory is
available as determined by the SORTMEMORY parameter. LARGE is the default value. The
goal of this strategy is to do as much sorting as possible in internal memory before writing
any records to disk. Whether disk I/O is necessary at all in the sorting process depends on
the amount of memory allocated for sorting and the size of the request output. If the
amount of SORTMEMORY is not large enough to meaningfully make use of the LARGE
strategy, the sort will default to the SMALL strategy. The LARGE strategy greatly reduces
the need for disk I/O and, if disk I/O is required after all (for very large output), it virtually
eliminates the need for multiple merge phases.

SORTMEMORY

The SORTMEMORY parameter controls the amount of internal memory available for sorting.
The syntax is

SET SORTMEMORY = {n|512}

where:

n

Is the positive number of megabytes of memory available for sorting. The default value is
512.

Creating Reports With TIBCO® WebFOCUS Language

 179

Sorting With Multiple Display Commands

Sorting With Multiple Display Commands

A request can consist of up to 64 sets of separate display commands (also known as verb
phrases), each with its own sort conditions. In order to display all of the information, a
meaningful relationship has to exist among the separate sort condition sets. The following
rules apply:

Up to 64 display commands and their associated sort conditions can be used. The first
display command does not have to have any sort condition. Only the last display command
may be a detail command, such as PRINT or LIST. Other preceding display commands must
be aggregating commands.

WHERE and IF criteria apply to the records selected for the report as a whole. WHERE and
IF criteria are explained in Selecting Records for Your Report on page 217.

When a sort phrase is used with a display command, the display commands following it
must use the same sorting condition in the same order. For example:

TABLE FILE EMPLOYEE
SUM ED_HRS
SUM CURR_SAL CNT.CURR_SAL
BY DEPARTMENT
PRINT FIRST_NAME
BY DEPARTMENT
BY LAST_NAME
END

The first SUM does not have a sort condition. The second SUM has a sort condition: BY
DEPARTMENT. Because of this sort condition, the PRINT command must have BY
DEPARTMENT as the first sort condition, and other sort conditions may be added as
needed.

Example:

Using Multiple Display and Sort Fields

The following request summarizes several levels of detail in the data source.

TABLE FILE EMPLOYEE
SUM CURR_SAL
SUM CURR_SAL BY DEPARTMENT
SUM CURR_SAL BY DEPARTMENT BY LAST_NAME
END

The command SUM CURR_SAL calculates the total amount of current salaries; SUM
CURR_SAL BY DEPARTMENT calculates the total amounts of current salaries in each
department; SUM CURR_SAL BY DEPARTMENT BY LAST_NAME calculates the total amounts of
current salaries for each employee name.

180

The output is:

3. Sorting Tabular Reports

Controlling Formatting of Reports With Multiple Display Commands

You can use the SET DUPLICATECOL command to reformat report requests that use multiple
display commands, placing aggregated fields in the same column above the displayed field.

By default, each new display command in a request generates additional sort field and display
field columns. With DUPLICATECOL set to OFF, each field occupies only one column in the
request, with the values from each display command stacked under the values for the previous
display command.

Syntax:

How to Control the Format of Reports With Multiple Display Commands

SET DUPLICATECOL={ON|OFF}

where:

ON

Displays the report with each field as a column. This is the default value.

OFF

Displays the report with common fields as a row.

Example:

Displaying Reports With Multiple Display Commands

The following request sums current salaries and education hours for the entire EMPLOYEE data
source and for each department:

TABLE FILE EMPLOYEE
SUM CURR_SAL ED_HRS
SUM CURR_SAL ED_HRS BY DEPARTMENT
END

Creating Reports With TIBCO® WebFOCUS Language

 181

Sorting With Multiple Display Commands

With DUPLICATECOL=ON, the output has separate columns for the grand totals and for the
departmental totals:

   CURR_SAL  ED_HRS  DEPARTMENT         CURR_SAL  ED_HRS
   --------  ------  ----------         --------  ------
$222,284.00  351.00  MIS             $108,002.00  231.00
                     PRODUCTION      $114,282.00  120.00

With DUPLICATECOL=OFF, the output has one column for each field. The grand totals are on
the top row of the report, and the departmental totals are on additional rows below the grand
totals:

DEPARTMENT         CURR_SAL  ED_HRS
----------         --------  ------
                $222,284.00  351.00
MIS             $108,002.00  231.00
PRODUCTION      $114,282.00  120.00

The following request adds a PRINT command sorted by department and by last name to the
previous request:

SET SPACES = 1
TABLE FILE EMPLOYEE
SUM CURR_SAL ED_HRS
SUM CURR_SAL ED_HRS BY DEPARTMENT AS 'DEPT'
PRINT FIRST_NAME CURR_SAL ED_HRS BY DEPARTMENT BY LAST_NAME
END

With DUPLICATECOL=ON, the output has separate columns for the grand totals, for the
departmental totals, and for each last name:

182

3. Sorting Tabular Reports

With DUPLICATECOL=OFF, the output has one column for each field. The grand totals are on
the top row of the report, the departmental totals are on additional rows below the grand
totals, and the values for each last name are on additional rows below their departmental
totals:

DEPT       LAST_NAME       FIRST_NAME        CURR_SAL ED_HRS
----       ---------       ----------        -------- ------
                                          $222,284.00 351.00
MIS                                       $108,002.00 231.00
           BLACKWOOD       ROSEMARIE       $21,780.00  75.00
           CROSS           BARBARA         $27,062.00  45.00
           GREENSPAN       MARY             $9,000.00  25.00
           JONES           DIANE           $18,480.00  50.00
           MCCOY           JOHN            $18,480.00    .00
           SMITH           MARY            $13,200.00  36.00
PRODUCTION                                $114,282.00 120.00
           BANNING         JOHN            $29,700.00    .00
           IRVING          JOAN            $26,862.00  30.00
           MCKNIGHT        ROGER           $16,100.00  50.00
           ROMANS          ANTHONY         $21,120.00   5.00
           SMITH           RICHARD          $9,500.00  10.00
           STEVENS         ALFRED          $11,000.00  25.00

Syntax:

How to Style a Report With SET DUPLICATECOL=ON

In a StyleSheet, you can identify the rows you want to style by specifying which display
command created those rows:

VERBSET = n

where:

n

Is the ordinal number of the display command in the report request.

Example:

Styling Rows Associated With a Specific Display Command

The following request has two display commands:

1. SUM CURR_SAL ED_HRS BY DEPARTMENT (totals by department).

2. PRINT FIRST_NAME CURR_SAL ED_HRS BY DEPARTMENT BY LAST_NAME (values by

employee by department).

Creating Reports With TIBCO® WebFOCUS Language

 183

Sorting With Multiple Display Commands

SET DUPLICATECOL = OFF
TABLE FILE EMPLOYEE
SUM CURR_SAL ED_HRS BY DEPARTMENT
PRINT FIRST_NAME CURR_SAL ED_HRS BY DEPARTMENT BY LAST_NAME

ON TABLE SET STYLE *
TYPE = REPORT, COLUMN= P4, VERBSET = 1, STYLE = ITALIC,    COLOR=BLUE,$
TYPE = REPORT, COLUMN= B2, VERBSET = 2, STYLE = UNDERLINE, COLOR = RED,$
ENDSTYLE
END

On the output:

The fourth displayed column (P4, department total of CURR_SAL) for the SUM command is
italic and blue.

The second BY field (LAST_NAME) for the PRINT command is underlined and red.

When you style specific columns, using P notation means that you count every column that
displays on the report output, including BY columns. Therefore, P1 is the DEPARTMENT
column, P2 is the LAST_NAME column (this is also B2, the second BY field column), P3 is the
FIRST_NAME column, P4 is the displayed version of the CURR_SAL column (the internal matrix
has multiple CURR_SAL columns), and P5 is the displayed ED_HRS column (the internal matrix
has multiple ED_HRS columns).

184

The output is:

3. Sorting Tabular Reports

Reference: Stacking Duplicate Columns in Multi-Verb Requests Based on AS Names

You can use the SET DUPLICATECOL command to reformat report requests that use multiple
display commands, placing aggregated fields in the same column above the displayed field.

By default, each new display command in a request generates additional sort field and display
field columns. With DUPLICATECOL set to OFF, each field occupies only one column in the
request, with the values from each display command stacked under the values for the previous
display command.

In prior releases, the duplicate columns were matched based on field names. Now, fields can
also be matched based on AS names. An AS name will not be matched to a field name. When
a field has an AS name, it will only be matched to other fields that have the same AS name.

Creating Reports With TIBCO® WebFOCUS Language

 185

Sorting With Multiple Display Commands

Example:

Stacking Duplicate Columns in Multi-Verb Requests Based on AS Names

The following request has three display commands. The first sums the CURR_SAL field. The
second sums the SALARY field by department. The third prints the GROSS field by department
and last name. Each field is assigned the same AS name, even the CURR_SAL field.

TABLE FILE EMPLOYEE
SUM CURR_SAL AS CURR_SAL  ED_HRS
SUM SALARY AS CURR_SAL ED_HRS BY DEPARTMENT AS 'DEPT'
PRINT FIRST_NAME GROSS AS CURR_SAL ED_HRS BY DEPARTMENT BY LAST_NAME
ON TABLE SET DUPLICATECOL OFF
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF, SIZE=10, $
VERBSET=1, COLOR=RED,$
VERBSET=2, COLOR=BLUE,$
VERBSET=3,COLOR=BLACK,$
ENDSTYLE
END

186

The partial output is shown in the following image.

3. Sorting Tabular Reports

Creating Reports With TIBCO® WebFOCUS Language

 187

Improving Efficiency With External Sorts

Improving Efficiency With External Sorts

When a report is generated, by default it is sorted using an internal sorting procedure. This
sorting procedure is optimized for reports of up to approximately 180 to 200K, although many
factors affect the size of the data that can be handled by the internal sort.

The FOCSORT file used for the internal sort can grow to any size allowed by the operating
system running and the available disk space. The user does not have to break a request up to
accommodate massive files. In previous releases, the FOCSORT file was limited to 2 GB and
the user received a FOC298 message when the WebFOCUS limit was exceeded. With no limit
enforced by WebFOCUS, the operating system provides whatever warning and error handling it
has for the management of a FOCSORT file that exceeds its limits.

You can generate larger reports somewhat faster by using dedicated sorting products, such as
SyncSort, DFSORT, or, in non-Mainframe environments, the WebFOCUS external sort routines.

To use an external sort, the EXTSORT parameter must be ON. Use of a StyleSheet turns off
external sorting.

Note that in Mainframe environments, external sorting is supported with the French, Spanish,
German, and Scandinavian National Languages (Swedish, Danish, Finnish, and Norwegian). To
specify the National Language Support Environment, use the LANG parameter as described in
the Developing Reporting Applications manual.

Reference: Requirements for External Sorting

You can use the DFSORT and SyncSort external sort products with any TABLE, FML, GRAPH, or
MATCH request in all WebFOCUS Mainframe environments. In other operating environments,
WebFOCUS has its own external sort routines.

Reference: Usage Notes for External Sorting in Non-Mainframe Environments

It is probably best not to use external sort if:

Your request requires a matrix (cannot be converted to a TABLEF request). If your request
needs a matrix and uses external sort, it will go through two sorts, both external and
internal, and it will be hard to realize any performance gains.

To tell if your report is convertible to TABLEF, use ? STAT (as described in How to Query the
Sort Type on page 189) or run an abbreviated version of the request with a low record limit
and external sort on. If the report statistics are printed after the TABLE output, it was
performed as TABLEF; if the statistics are printed before the first screen of TABLE output, it
went through TABLE processing because it was not convertible to TABLEF.

188

3. Sorting Tabular Reports

Your input is sorted or almost sorted.

Your system cannot support a large number of work files (for information, see Sort Work
Files and Return Codes on page 190). In this case the internal sort may do a better job
since internally it implements about 60 logical work files, all sharing space in FOCSORT.

Procedure: How to Determine the Type of Sort Used

To determine which sort is used, the following criteria are evaluated, in this sequence:

1. BINS. If an entire report can be sorted within the work area (BINS), the external sort is not

invoked, even if EXTSORT is set ON.

2. EXTERNAL. If BINS is not large enough to sort the entire report and EXTSORT is set ON,

the external sort utility will be invoked.

Syntax:

How to Control External Sorting

You can turn the external sorting feature on and off using the SET EXTSORT command.

SET EXTSORT = {ON|OFF}

where:

ON

Enables the selective use of a dedicated external sorting product to sort reports. This
value is the default in all Mainframe environments.

OFF

Uses the internal sorting procedure to sort all reports. This value is the default in all non-
Mainframe environments.

Syntax:

How to Query the Sort Type

To determine which sort is being used for a given report, issue the following command after
the report request:

? STAT

The command displays the following values for the SORT USED parameter:

FOCUS

The internal sorting procedure was used to sort the entire report.

Creating Reports With TIBCO® WebFOCUS Language

 189

Improving Efficiency With External Sorts

SQL

You are using a relational data source and the RDBMS supplied data already in order.

EXTERNAL

An external sorting product sorted the report.

NONE

The report did not require sorting.

Providing an Estimate of Input Records or Report Size for Sorting

There are two advantages to providing an estimate for the input size (ESTRECORDS) or the
report size (ESTLINES):

If the request cannot be converted to a TABLEF request and the file size estimate shows
that the external sort will be needed, FOCUS initiates the external sort immediately, which
makes a FOCUS merge unnecessary. Without the estimate, such a request always
performs this merge.

In Mainframe environments, FOCUS passes the file size to the external sort, which enables
it to allocate work files of the appropriate size.

Syntax:

How to Provide an Estimate of Input Records or Report Size for Sorting

ON TABLE SET ESTRECORDS nON TABLE SET ESTLINES n

where:

n

Is the estimated number of records or lines to be sorted.

Sort Work Files and Return Codes

In non-Mainframe environments, external sorts use temporary work files to hold intermediate
sorting results. For each type of external sort, you must be aware of how sort work files are
created and used.

Reference: Sort Work Files on UNIX, Windows, and OpenVMS

While internal sorting uses only one work file, FOCSORT (allocated in the EDATEMP directory),
external sort allows up to 31 work files, allocated on one or more disk drives (spindles) or
directories.

190

3. Sorting Tabular Reports

Warning: Any one or more of these work files may become very large. Count on using many
times the total disk space required by FOCSORT.

By default, five work files are allocated in the /tmp directory on UNIX, or in the directory
pointed to by the TMP environment variable in Windows. This may not be enough sort work
space and, even if the files fit in the directory, five files are probably not enough for optimal
performance. Also, having all of the sort work files on the same disk may further degrade
performance.

You have two other options:

Define the TMPDIR shell variable (UNIX) or TMP environment variable (Windows) to point to
some suitable writable directory. For best results, this directory should be on a disk with a
lot of available space, and not the same disk as the data source or the EDATEMP directory.
Again, you will get five temporary work files allocated on the same spindle, with consequent
performance degradation.

Define 1 to 31 shell variables of the form IBITMPDIR01 ... IBITMPDIR31 to point to one or
more writable directories.

If the UNIX TMPDIR or Windows TMP variable is set, it must be "unset" in order to make
use of the IBITMPDIRnn variables. The UNIX command for unsetting the TMPDIR variable is:

unset TMPDIR

The Windows command for unsetting the TMP variable is:

SET TMP=

Different variables may point to the same directory, if desired. If you wish to allocate n work
files, you must define variables 01 through n. The first variable missing from the
environment determines the number of work files that will be used. (If you define fewer than
five, additional files will be allocated using the system default location to make up the
difference.) The more work files you allocate, and the more separated they are across
different spindles, the better performance you should achieve. The major constraint is the
total disk space available.

The work file names are generated by the ANSI tempnam function, however, the names all
begin with the characters srtwk. If the sorting process ends normally or terminates because of
a detectable error (typically, disk space overflow), all of the allocated work files are deleted.
There is no explicit way to save them. If there is another type of abnormal termination, srtwk
files may be left on the disk. You can and should erase them.

Creating Reports With TIBCO® WebFOCUS Language

 191

Improving Efficiency With External Sorts

Reference: Sort Work Files on IBM i

On IBM i (formerly i5/OS), the number of work files is fixed at 9. They are virtual files.

Reference: WebFOCUS External Sort Return Codes

The WebFOCUS error message FOC909 is issued for all errors from external sort. An additional
three-digit code is supplied, of which the last two digits are of interest. If you get an error
number ending in:

16, external sort did not have enough memory allocated. You can try reducing the number
of work files.

20, an I/O error occurred; in most cases, this means that one of the disks is not writable
or has overflowed. Allocate the work files differently or reduce their number.

28, one of the work files could not be opened. Check to make sure the pathname was
specified correctly and that protections allow writing and reading.

32, an internal logical error was detected in the sort processing. Report this problem to
Information Builders.

Mainframe External Sort Utilities and Message Options

By default, error messages created by a Mainframe external sort product are not displayed.
However, you may wish to display these messages on your screen for diagnostic purposes.

Procedure: How to Select a Sort Utility and Message Options

You use the SET SORTLIB command to both specify the sort utility used at your site and, for
DFSORT and SYNCSORT on z/OS, to display sort messages.

1.

Issue the SET SORTLIB command to specify the sort utility being used:

SET SORTLIB = {sortutility|DEFAULT}

where:

sortutility

Can be one of the following:

DFSORT for DFSORT without messages.

MVSMSGDF for DFSORT with messages.

SYNCSORT for SyncSort without messages.

192

3. Sorting Tabular Reports

MVSMSGSS for SyncSort with standard messages.

MVSMSGSD for SyncSort with debug (verbose) messages.

DEFAULT for DFSORT. However, It is more efficient and highly recommended that
you explicitly specify the sort utility using one of the other values.

2.

If you specified a sort option that produces sort messages on z/OS, you must direct the
sort messages to the batch output stream or a file.

Allocate DDNAME SYSOUT to the batch output stream or a file on z/OS by inserting the
appropriate following DD card into your server batch JCL, if it is not already there. For
example, the following DD card allocates DDNAME SYSOUT to the batch output stream:

//SYSOUT DD SYSOUT=*

Diagnosing External Sort Errors

When an external sort generates an error, you can generate a trace of sort processing and
examine the FOCUS return codes and messages to diagnose the problem.

Procedure: How to Trace Sort Processing

When an external sort problem occurs, one of the following messages is generated:

(FOC909)  CRITICAL ERROR IN EXTERNAL SORT.  RETURN CODE IS: xxxx
(FOC1810) External sort not found
(FOC1899) Load of %1 (external-sort module) under %2 failed

In response to these messages, as well as for any other problem with sorting, it is useful to
trace sort processing. For information on diagnosing external sort problems, see Diagnosing
External Sort Errors on page 193.

1. Allocate DDNAME FSTRACE to the terminal or a file. The following example sends trace

output to the terminal:

//FSTRACE  DD  SYSOUT=*,DCB=(RECFM=FA,LRECL=133,BLKSIZE=133)

2. Activate the trace by adding the following commands in any supported profile or a

FOCEXEC:

SET TRACEUSER = ON
SET TRACEON  = SORT/1/FSTRACE

Reference: External Sort Messages and Return Codes

When you receive a FOC909 message, it includes a return code:

(FOC909)  CRITICAL ERROR IN EXTERNAL SORT.  RETURN CODE IS: xxxx

Creating Reports With TIBCO® WebFOCUS Language

 193

Improving Efficiency With External Sorts

You may also receive one of the following messages:

(FOC1810) External sort not found
(FOC1899) Load of %1 (external-sort module) under %2 failed

The following notes apply when this message or a FOC1800 or FOC1899 message is
generated by a TABLE request:

The most common value for xxxx is 16. However, return code 16 is issued for a number of
problems, including but not limited to the following:

Syntax errors.

Memory shortage.

I/O errors (depending on installation options).

Space problems with output.

Space problems with work files.

In order to diagnose the error, you must generate external sort messages (using the
instructions in How to Select a Sort Utility and Message Options on page 192 and How to
Trace Sort Processing on page 193) and then reproduce the failure.

For return codes not described below, follow the same procedure described for return code
16.

Return code 20 is issued by DFSORT under z/OS if messages were requested (using the
MVSMSGDJ option of the SET SORTLIB command), but the SYSOUT DD card is missing.
DFSORT terminates after issuing the return code. Under the same conditions, SyncSort
attempts to open SYSOUT, producing the following message, and then continues with
messages written to the operator or terminal:

IEC130I SYSOUT DD STATEMENT MISSING.

Return code 36 or a FOC1899 message under z/OS means that the external sort module
could not be found; check the STEPLIBs allocated.

When REBUILD INDEX invokes an external sort that fails, it generates a message similar to the
following:

ERROR OCCURRED IN THE SORT yyyyyyyyzzzzzzzz

In this case, the return code is yyyyyyyy and it is expressed in hex. The final eight digits
(zzzzzzzz) should be ignored.

194

3. Sorting Tabular Reports

Translate the return code into decimal and follow the instructions for return codes in a TABLE
request.

Note also that when a TABLE request generates a non-zero return code from an external sort,
FOCUS is terminated. By contrast, when REBUILD INDEX gets a non-zero return code from an
external sort, the REBUILD command is terminated but FOCUS continues.

Reference: Responding to an Indication of Inadequate Sort Work Space

Before following these instructions, make sure that external sort messages were generated
(for information, see How to Select a Sort Utility and Message Options on page 192) and that
they clearly show that the reason for failure was inadequate sort work space.

1. Make an estimate of the number of lines of output the request will produce.

2. Set the ESTLINES parameter in the request or FOCEXEC. For information, see Providing an

Estimate of Input Records or Report Size for Sorting on page 190.

WebFOCUS will pass this estimate to the external sort utility through the parameter list.

Do not override the DD cards for SORTWKnn, S001WKnn, DFSPARM, or $SORTPARM
without direct instructions from technical support. The instructions in How to Select a Sort
Utility and Message Options on page 192, How to Trace Sort Processing on page 193, and
Providing an Estimate of Input Records or Report Size for Sorting on page 190 should
provide equivalent capabilities.

Aggregation by External Sort (Mainframe Environments Only)

External sorts can be used to perform aggregation with a significant decrease in processing
time in comparison to using the internal sort facility. The gains are most notable with relatively
simple requests against large data sources.

When aggregation is performed by an external sort, the statistical variables &RECORDS and
&LINES are equal because the external sort products do not return a line count for the answer
set. This is a behavior change, and affects any code that checks the value of &LINES. (If you
must test &LINES, do not use this feature.)

Syntax:

How to Use Aggregation in Your External Sort

SET EXTAGGR = aggropt

where:

aggropt

Can be one of the following:

Creating Reports With TIBCO® WebFOCUS Language

 195

Improving Efficiency With External Sorts

OFF disallows aggregation by an external sort.

NOFLOAT allows aggregation if there are no floating point data fields present.

ON allows aggregation by an external sort. This value is the default.

Reference: Usage Notes for Aggregating With an External Sort

You must use SyncSort or DFSORT.

Your query should be simple (that is, it should be able to take advantage of the TABLEF
facility). For related information, see Data Retrieval Using TABLEF on page 1935.

The PRINT display command may not be used in the query.

SET ALL must be equal to OFF.

Only the following column prefixes are allowed: SUM, AVG, CNT, FST.

Columns can be calculated values or have a row total.

When SET EXTAGGR = NOFLOAT and your query aggregates numeric data, the external sort
is not called, and aggregation is performed through the internal sorting procedure.

Example:

Changing Output by Using an External Sort for Aggregation

If you use SUM on an alphanumeric field in your report request without using an external sort,
the last instance of the sorted fields is displayed in the output, by default. Turning on
aggregation in the external sort displays the first record instead. However, you can control the
order of display using the SUMPREFIX parameter. For information about the SUMPREFIX
parameter, see Changing Retrieval Order With Aggregation on page 197.

The following command turns aggregation ON and leaves SUMPREFIX set to LST (the default)
and, therefore, displays the last record:

SET EXTAGGR = ON
SET SUMPREFIX = LST
TABLE FILE CAR
SUM CAR BY COUNTRY
END

The output is:

COUNTRY     CAR
-------     ---
ENGLAND     TRIUMPH
FRANCE      PEUGEOT
ITALY       MASERATI
JAPAN       TOYOTA
W GERMANY   BMW

196

Note: SUMPREFIX is described in Changing Retrieval Order With Aggregation on page 197.

3. Sorting Tabular Reports

With SUMPREFIX = FST, the output is:

COUNTRY     CAR
-------     ---
ENGLAND     JAGUAR
FRANCE      PEUGEOT
ITALY       ALFA ROMEO
JAPAN       DATSUN
W GERMANY   AUDI

Changing Retrieval Order With Aggregation

The SUMPREFIX parameter allows you to specify which value will be displayed when
aggregating an alphanumeric or smart date field in the absence of any prefix operator. The
default value is LST, which will return the physical last value within the sort group. FST will
return the first physical value in the sort group. MIN and MAX return either the minimum value
or maximum value within the sort group.

The SUMPREFIX command allows users to choose the answer set display order.

Syntax:

How to Set Retrieval Order

SET SUMPREFIX = {FST|LST|MIN|MAX}

where:

FST

LST

MIN

MAX

Displays the first value when alphanumeric or smart date data types are aggregated.

Displays the last value when alphanumeric or smart date data types are aggregated. LST is
the default value.

Displays the minimum value in the sort order set by your server code page and
configuration when alphanumeric or smart date data types are aggregated.

Displays the maximum value in the sort order set by your server code page and
configuration when alphanumeric or smart date data types are aggregated.

Creating Reports With TIBCO® WebFOCUS Language

 197

Improving Efficiency With External Sorts

Example:

Displaying the Minimum Value for an Aggregated Alphanumeric Field

The following request sets SUMPREFIX to MIN and displays the aggregated
PRODUCT_CATEGORY and DAYSDELAYED values as well as the minimum, maximum, first, and
last PRODUCT_CATEGORY values. In each row, the aggregated PRODUCT_CATEGORY value
matches the MIN.PRODUCT_CATEGORY value. The DAYSDELAYED numeric field is not affected
by the SUMPREFIX value and is aggregated.

SET SUMPREFIX = MIN
TABLE FILE WF_RETAIL_LITE
SUM PRODUCT_CATEGORY DAYSDELAYED MIN.PRODUCT_CATEGORY MAX.PRODUCT_CATEGORY
     FST.PRODUCT_CATEGORY LST.PRODUCT_CATEGORY
BY BRAND
WHERE BRAND GT 'K' AND BRAND LT 'U'
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

The output is shown in the following image.

Creating a HOLD File With an External Sort (Mainframe Environments Only)

You can use Mainframe external sort packages to create HOLD files, producing substantial
savings in processing time. The gains are most notable with relatively simple requests against
large data sources.

198

3. Sorting Tabular Reports

Syntax:

How to Create HOLD Files With an External Sort

SET EXTHOLD = {OFF|ON}

where:

OFF

Disables HOLD files by an external sort.

ON

Enables HOLD files by an external sort. This value is the default.

Reference: Usage Notes for Creating a HOLD File With an External Sort

The default setting of EXTSORT=ON must be in effect.

EXTHOLD must be ON.

The request must contain a BY field.

The type of HOLD file created must be a FOCUS, XFOCUS, ALPHA, or BINARY file.

Your query should be simple. AUTOTABLEF analyzes a query and determines whether the
combination of display commands and formatting options requires the internal matrix. In
cases where it is determined that a matrix is not necessary to satisfy the query, you may
avoid the extra internal costs associated with creating the matrix. The internal matrix is
stored in a file or data set named FOCSORT. The AUTOTABLEF default is ON, in order to
realize performance gains.

SET ALL must be OFF.

There cannot be an IF/WHERE TOTAL or BY TOTAL in the request.

If a request contains a SUM command, EXTAGGR must be set ON, and the only column
prefixes allowed are SUM. and FST.

Hierarchical Reporting: BY HIERARCHY

Cube data sources such as Essbase or SAP BW are organized into dimensions and facts.
Dimensions are often organized into hierarchies. The synonyms for cube data sources have
attributes that describe the dimension hierarchies, and WebFOCUS has hierarchical reporting
syntax that can automatically report against these hierarchies and display the results indented
to show the hierarchical relationships.

Creating Reports With TIBCO® WebFOCUS Language

 199

Hierarchical Reporting: BY HIERARCHY

WebFOCUS also supports defining dimension hierarchies in synonyms for non-cube data
sources that have hierarchical data. Once hierarchical dimensions are defined in a synonym,
you can issue hierarchical reporting requests against them. Non-cube synonyms with
hierarchical attributes are called virtual cubes.

Dimensions are categories of data, such as Region or Time, that you use to analyze and
compare business performance. Dimensions consist of data elements that are called
members. For example, a Region dimension could have members England and France.

Dimension members are usually organized into hierarchies. Hierarchies can be viewed as tree-
like structures where members are the nodes. For example, the Region dimension may have
the element World at its top level (the root node). The World element may have children nodes
(members) representing continents. Continents, in turn, can have children nodes that
represent countries, and countries can have children nodes representing states or cities.
Nodes with no children are called leaf nodes.

Measures are numeric values, such as Sales Volume or Net Income, that are used to quantify
how your business is performing.

A cube consists of data derived from facts, which are records about individual business
transactions. For example, an individual fact record reflects a sales transaction of a certain
number of items of a certain product at a certain price, which occurred in a certain store at a
certain moment in time. The cube contains summarized fact values for all combinations of
measures and members of different dimensions.

A synonym describes a hierarchy using a set of fields that define the hierarchical structure and
the relationships between the hierarchy members. WebFOCUS has special hierarchical
reporting syntax for reporting on hierarchies.

Hierarchical reporting requests have several phases:

Phase 1, selecting hierarchy members to display.

The hierarchical reporting phrase BY or ON HIERARCHY automatically sorts and formats a
hierarchy with appropriate indentations that show the parent/child relationships. It also
automatically rolls up the measure values for child members to generate the measure
values for the parent members.

If you do not want to see the entire hierarchy, you can use the WHEN phrase to select
hierarchy members for display. The expression in this WHEN phrase must reference only
hierarchy fields, not dimension properties or measures.

Phase 2, screening the retrieved dimension data.

200

3. Sorting Tabular Reports

WHERE criteria are applied to the leaf nodes of the members selected during phase 1.
Therefore, dimension properties can be used in WHERE tests. These tests can also
reference hierarchy fields. However, since the selection criteria are always applied to the
values at the leaf nodes, they cannot select data based on values that occur at higher
levels. For example, in a dimension with Continents, Countries, and Cities, your request will
not display any rows if you use WHERE to select at the Country level, but it may if you use it
to select at the City level. WHERE tests can also reference measures.

Phase 3, screening based on aggregated values.

Measures, being summarized values, can be referenced in WHERE TOTAL tests and
COMPUTE commands because those commands are processed after the hierarchy
selection and aggregation phases of the request.

Syntax:

How to Specify a Hierarchy in a Master File

The data source must have at least one dimension that is organized hierarchically. The
declaration for a dimension is:

DIMENSION=dimname,CAPTION=dimcaption, $

where:

dimname

Is a name for the dimension.

dimcaption

Is a label for the dimension.

The declaration for a hierarchy within the dimension is:

HIERARCHY=hname,CAPTION='hcaption',HRY_DIMENSION=dimname,
HRY_STRUCTURE=RECURSIVE, $

where:

hname

Is a name for the hierarchy.

hcaption

Is a label for the hierarchy.

dimname

Is the name of the dimension for which this hierarchy is defined.

Creating Reports With TIBCO® WebFOCUS Language

 201

Hierarchical Reporting: BY HIERARCHY

Several fields are used to define a parent/child hierarchy. Each has a PROPERTY attribute that
describes which hierarchy property it represents. Each hierarchy must have a unique identifier
field. This field is called the hierarchy field. If the synonym represents a FOCUS data source,
this field must be indexed (FIELDTYPE=I). The declaration for the hierarchy field is:

FIELD=hfield,ALIAS=halias,USAGE= An, [ACTUAL=Am,]
WITHIN='*hierarchy',PROPERTY=UID, [TITLE='title1',] [FIELDTYPE=I,] $

where:

hfield

Is the field name for the hierarchy field.

halias

Is the alias for the hierarchy field. If the data source is relational, this must be the name of
the column in the Relational DBMS.

hierarchy

Is the name of the hierarchy to which this field belongs.

USAGE= An, [ACTUAL=Am,]

Are the USAGE format and, if the data source is not a FOCUS data source, the ACTUAL
format of the field.

title1

Is an optional title for the field.

Other fields defined for the hierarchy include the parent field and the caption field. Each of
these fields has the same name as the hierarchy field with a suffix added. Each has a
PROPERTY attribute that specifies its role in the hierarchy and a REFERENCE attribute that
points to the corresponding hierarchy field.

The following is the declaration for the parent field. The parent field is needed to define the
parent/child relationships in the hierarchy:

FIELD=hfield_PARENT,ALIAS=parentalias,USAGE=An,[ACTUAL=Am,] [TITLE=ptitle,]
      PROPERTY=PARENT_OF, REFERENCE=hfield, $

where:

hfield

Is the hierarchy field.

202

3. Sorting Tabular Reports

parentalias

Is the alias for the parent field. If the data source is relational, this must be the name of
the column in the relational DBMS.

USAGE= An, [ACTUAL=Am,]

Are the USAGE format and, if the data source is not a FOCUS data source, the ACTUAL
format of the field.

ptitle

Is a column title for the parent field.

The following is the declaration for the caption field. A caption is a descriptive title for each
value of the hierarchy field. It is part of the data and, therefore, is different from a TITLE
attribute in the Master File, which is a literal title for the column on the report output.

FIELD=hfield_CAPTION,ALIAS=capalias,USAGE=Ann,[ACTUAL=Amm,]
[TITLE=captitle,]
        PROPERTY=CAPTION, REFERENCE=hfield, $

where:

hfield

Is the hierarchy field.

capalias

Is the alias for the caption field. If the data source is relational, this must be the name of
the column in the relational DBMS.

USAGE= Ann, [ACTUAL=Amm,]

Are the USAGE format and, if the data source is not a FOCUS data source, the ACTUAL
format of the field.

captitle

Is a column title for the caption field.

Creating Reports With TIBCO® WebFOCUS Language

 203

Hierarchical Reporting: BY HIERARCHY

Example:

Sample Master File With a Dimension Hierarchy

The following Master File is based on the CENTGL Master File, which has an FML hierarchy
defined. This version is named NEWGL and it has a dimension hierarchy of accounts in which
GL_ACCOUNT is the hierarchy field, GL_ACCOUNT_PARENT is the parent field, and
GL_ACCOUNT_CAPTION is the caption field. There are other fields based on the hierarchy
(GL_ACCOUNT_LEVEL, GL_ROLLUP_OP, and GL_ACCOUNT_TYPE). In addition, there is a
measure field (GL_ACCOUNT_AMOUNT):

FILE=NEWGL       ,SUFFIX=FOC,$
SEGNAME=ACCOUNTS   ,SEGTYPE=S01
DIMENSION=Accnt,CAPTION=Accnt, $
HIERARCHY=Accnt,CAPTION='Accnt',HRY_DIMENSION=Accnt,
HRY_STRUCTURE=RECURSIVE, $
FIELD=GL_ACCOUNT,GLACCT,A7,WITHIN='*Accnt',PROPERTY=UID,
            TITLE='Ledger,Account', FIELDTYPE=I, $
FIELD=GL_ACCOUNT_PARENT,GLPAR,A7, TITLE=Parent,
            PROPERTY=PARENT_OF, REFERENCE=GL_ACCOUNT, $
FIELD=GL_ACCOUNT_TYPE,GLTYPE,A1, TITLE=Type,$
FIELD=GL_ROLLUP_OP,ROLL,A1, TITLE=Op, $
FIELD=GL_ACCOUNT_LEVEL,GLLEVEL,I3, TITLE=Lev, $
FIELDNAME=GL_ACCOUNT_AMOUNT,GLAMT,D12.2, TITLE=Amount, $
FIELD=GL_ACCOUNT_CAPTION,GLCAP,A30, TITLE=Caption,
            PROPERTY=CAPTION, REFERENCE=GL_ACCOUNT, $
FIELD=SYS_ACCOUNT,ALINE,A6, TITLE='System,Account,Line', MISSING=ON, $

The following procedure loads data into this data source, as long as the Master File is
available to WebFOCUS (on the path or allocated):

CREATE FILE NEWGL NOMSG
-RUN
MODIFY FILE NEWGL
COMPUTE TGL_ACCOUNT_LEVEL/A3=;
COMPUTE TGL_ACCOUNT_AMOUNT/A12=;
FIXFORM GL_ACCOUNT/A4B X3 GL_ACCOUNT_PARENT/A4B X3 GL_ACCOUNT_TYPE/A1B
FIXFORM SYS_ACCOUNT/A4B GL_ROLLUP_OP/A1B
FIXFORM TGL_ACCOUNT_LEVEL/A3B GL_ACCOUNT_CAPTION/A30B
FIXFORM TGL_ACCOUNT_AMOUNT/A12B
COMPUTE GL_ACCOUNT_LEVEL = EDIT(TGL_ACCOUNT_LEVEL);
COMPUTE GL_ACCOUNT_AMOUNT = ATODBL(TGL_ACCOUNT_AMOUNT , '12',
GL_ACCOUNT_AMOUNT);

MATCH GL_ACCOUNT
   ON MATCH REJECT
   ON NOMATCH INCLUDE

204


3. Sorting Tabular Reports

DATA
1000          R.   +  1Profit Before Tax
2000   1000   R.   +  2Gross Margin
2100   2000   R.   +  3Sales Revenue
2200   2100   R.   +  4Retail Sales
2210   2200   R7001+  5Retail - Television                  505.00
2220   2200   R7002+  5Retail - Stereo                      505.00
2230   2200   R7003+  5Retail - Video Player                505.00
2240   2200   R7004+  5Retail - Computer                    505.00
2250   2200   R7005+  5Retail - Video Camera                505.00
2300   2100   R.   +  4Mail Order Sales
2310   2300   R7011+  5Mail Order - Television              505.00
2320   2300   R7012+  5Mail Order - Stereo                  505.00
2330   2300   R7013+  5Mail Order - Video Player            505.00
2340   2300   R7014+  5Mail Order - Computer                505.00
2350   2300   R7015+  5Mail Order - Video Camera            505.00
2400   2100   R.   +  4Internet Sales
2410   2400   R7021+  5Internet - Television                505.00
2420   2400   R7022+  5Internet - Stereo                    505.00
2430   2400   R7023+  5Internet - Video Player              505.00
2440   2400   R7024+  5Internet - Computer                  505.00
2450   2400   R7025+  5Internet - Video Camera              505.00
2500   2000   E.   -  3Cost Of Goods Sold
2600   2500   E.   +  4Variable Material Costs
2610   2600   E7101+  5Television COGS                      505.00
2620   2600   E7102+  5Stereo COGS                          505.00
2630   2600   E7103+  5Video COGS                           505.00
2640   2600   E7104+  5Computer COGS                        505.00
2650   2600   E7105+  5Video Camera COGS                    505.00
2700   2500   E7111+  4Direct Labor                         404.00
2800   2500   E7112+  4Fixed Costs                          404.00
3000   1000   E.   -  2Total Operating Expenses
3100   3000   E.   +  3Selling Expenses
3110   3100   E.   +  4Advertising
3112   3110   E7202+  5TV/Radio                             505.00
3114   3110   E7203+  5Print Media                          505.00
3116   3110   E7206+  5Internet Advertising                 505.00
3120   3100   E7212+  4Promotional Expenses                 404.00
3130   3100   E7213+  4Joint Marketing                      404.00
3140   3100   E7214+  4Bonuses/Commisions                   404.00
3200   3000   E.   +  3General + Admin Expenses
3300   3200   E.   +  4Salaries-Corporate

Creating Reports With TIBCO® WebFOCUS Language

 205

Hierarchical Reporting: BY HIERARCHY

3310   3300   E7301+  5Salaries-Corp Mgmt                   505.00
3320   3300   E7302+  5Salaries-Administration              505.00
3330   3300   E7303+  5IT Contractors                       505.00
3400   3200   E.   +  4Company Benefits
3410   3400   E7311+  5Social Security                      505.00
3420   3400   E7312+  5Unemployment                         505.00
3430   3400   E7313+  5Vacation Pay                         505.00
3440   3400   E7314+  5Sick Pay                             505.00
3450   3400   E.   +  5Insurances
3451   3450   E7321+  6Medical Insurance                    606.00
3452   3450   E7322+  6Dental Insurance                     606.00
3453   3450   E7323+  6Pharmacy Insurance                   606.00
3454   3450   E7324+  6Disability Insurance                 606.00
3455   3450   E7325+  6Life Insurance                       606.00
3500   3200   E.   +  4Depreciation Expenses
3510   3500   E7411+  5Equipment                            505.00
3520   3500   E7412+  5Building                             505.00
3530   3500   E7413+  5Vehicles                             505.00
3600   3200   R7414-  4Gain/(Loss) Sale of Equipment        404.00
3700   3200   E.   +  4Leasehold Expenses
3710   3700   E7421+  5Equipment                            505.00
3720   3700   E7422+  5Buildings                            505.00
3730   3700   R7429-  5Sub-Lease Income                     505.00
3800   3200   E7440+  4Interest Expenses                    404.00
3900   3200   E.   +  4Utilities
3910   3900   E7451+  5Electric                             505.00
3920   3900   E7452+  5Gas                                  505.00
3930   3900   E7453+  5Telephone                            505.00
3940   3900   E7454+  5Water                                505.00
3950   3900   E7455+  5Internet Access                      505.00
5000   1000   E.   -  2Total R+D Costs
5100   5000   E7511+  3Salaries                             303.00
5200   5000   E7521+  3Misc. Equipment                      303.00
END

Syntax:

How to Report on a Hierarchy

In hierarchical reporting, measure values for child dimension members will be rolled up to
generate the parent values. In the data source, the parent members should not have values
for the measures.

SUM measure_field ...
BY hierarchy_field [HIERARCHY [WHEN expression_using_hierarchy_fields;]
[SHOW [TOP|UP n] [TO {BOTTOM|DOWN m}] [byoption [WHEN condition] ...] ]
[WHERE expression_using_dimension_data]
[ON hierarchy_field HIERARCHY [WHEN expression_using_hierarchy_fields;]
[SHOW [TOP|UP n] [TO BOTTOM|DOWN m] [byoption [WHEN condition] ...]]

where:

measure_field

Is the field name of a measure.

206

3. Sorting Tabular Reports

BY hierarchy_field HIERARCHY

Identifies the hierarchy used for sorting. The field must be a hierarchy field.

ON hierarchy_field HIERARCHY

Identifies the hierarchy used for sorting. The field must be a hierarchy field. The request
must include either a BY phrase or a BY HIERARCHY phrase for this field name.

WHEN expression_using_hierarchy_fields;

Selects hierarchy members. The WHEN phrase must immediately follow the word
HIERARCHY to distinguish it from a WHEN phrase associated with a BY option (such as
SUBFOOT). Any expression using only hierarchy fields is supported. The WHEN phrase can
be on the BY HIERARCHY command or the ON HIERARCHY command, but not both.

SHOW

Specifies which levels to show on the report output relative to the levels selected by the
WHEN phrase. If there is no WHEN phrase, the SHOW option is applied to the root node of
the hierarchy. The SHOW option can be specified on the BY HIERARCHY phrase or the ON
HIERARCHY phrase, but not both.

n

TOP

TO

Is the number of ascendants above the set of selected members that will have measure
values. All ascendants appear on the report to show the hierarchical context of the
selected members. However, ascendants that are not included in the SHOW phrase
appear on the report with missing data symbols in the report columns that display
measures. The default for n is 0.

Specifies that ascendant levels to the root node of the hierarchy will be populated with
measure values.

Is required when specifying a SHOW option for descendant levels.

BOTTOM

Specifies all descendants to the leaf nodes of the hierarchy will be populated with
measure values. This is the default value.

m

Is the number of descendants of each selected level that will display. The default for m is
BOTTOM, which displays all descendants.

Creating Reports With TIBCO® WebFOCUS Language

 207

Hierarchical Reporting: BY HIERARCHY

byoption

Is one of the following sort-based options: PAGE-BREAK, REPAGE, RECAP, RECOMPUTE,
SKIP-LINE, SUBFOOT, SUBHEAD, SUBTOTAL, SUB-TOTAL, SUMMARIZE, UNDER-LINE. If you
specify SUBHEAD or SUBFOOT, you must place the WHEN phrase on the line following the
heading or footing text.

condition

Is a logical expression.

expression_using_dimension_data

Screens the rows selected in the BY/ON HIERARCHY and WHEN phrases based on
dimension data. The expression can use dimension properties and hierarchy fields.
However, the selection criteria are always applied to the values at the leaf nodes.
Therefore, you cannot use WHERE to select rows based on hierarchy field values that
occur at higher levels. For example, in a dimension with Continents, Countries, and Cities,
your request will not display any rows if you use WHERE to select a Country name, but it
may if you use it to select a City name.

Example:

Reporting on a Dimension HIerarchy

The following request reports on the entire GL_ACCOUNT hierarchy for the CENTGL2 data
source created in the Describing Data With WebFOCUS Language manual.

TABLE FILE NEWGL
SUM GL_ACCOUNT_AMOUNT
BY GL_ACCOUNT HIERARCHY
ON TABLE SET PAGE NOPAGE
ON TABLE SET STYLE *
TYPE=REPORT,GRID=OFF,$
ENDSTYLE
END

208

Partial output is shown in the following image. The accounts are indented to show the
hierarchical relationships:

3. Sorting Tabular Reports

Creating Reports With TIBCO® WebFOCUS Language

 209

Hierarchical Reporting: BY HIERARCHY

The following is the same request using the GL_ACCOUNT_CAPTION field:

TABLE FILE NEWGL
SUM GL_ACCOUNT_AMOUNT
BY GL_ACCOUNT_CAPTION HIERARCHY
ON TABLE SET PAGE NOPAGE
ON TABLE SET STYLE *
TYPE=REPORT,GRID=OFF,$
ENDSTYLE
END

210

Partial output is shown in the following image:

3. Sorting Tabular Reports

Creating Reports With TIBCO® WebFOCUS Language

 211

Hierarchical Reporting: BY HIERARCHY

Example:

Using WHEN to Select Hierarchy Members

The following request selects certain accounts using the WHEN phrase and populates one
level up and one level down from the selected nodes with values. Note that all levels to the
root node display on the output for context, but if they are not in the members selected, they
are not populated with measure values:

TABLE FILE NEWGL
SUM GL_ACCOUNT_AMOUNT
BY GL_ACCOUNT_CAPTION HIERARCHY
WHEN GL_ACCOUNT GT '2000' AND GL_ACCOUNT LT '3000';
 SHOW UP 1 TO DOWN 1
ON TABLE SET PAGE NOPAGE
ON TABLE SET STYLE *
TYPE=REPORT,GRID=OFF,$
ENDSTYLE
END

212

The output is shown in the following image:

3. Sorting Tabular Reports

Creating Reports With TIBCO® WebFOCUS Language

 213

Hierarchical Reporting: BY HIERARCHY

Example:

Using WHERE to Screen Selected Hierarchy Members

The following request selects members using the WHEN phrase and then screens the output
by applying a WHERE phrase to the selected members:

TABLE FILE NEWGL
SUM GL_ACCOUNT_AMOUNT GL_ACCOUNT_TYPE
BY GL_ACCOUNT HIERARCHY
WHEN GL_ACCOUNT NE '3000';
 SHOW UP 0 TO DOWN 0
WHERE GL_ACCOUNT_TYPE NE 'E'   ;
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF,$
ENDSTYLE
END

214

The output is shown in the following image:

3. Sorting Tabular Reports

Creating Reports With TIBCO® WebFOCUS Language

 215

Hierarchical Reporting: BY HIERARCHY

216

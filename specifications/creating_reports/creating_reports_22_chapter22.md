Chapter22

Using Headings, Footings, Titles, and
Labels

After you have selected the data for a report, you can make it more meaningful by adding
headings, footings, titles, and labels. Headings and footings supply key information,
such as the purpose of a report and its audience. They also provide structure, helping
the user navigate to the detail sought. Titles and labels identify individual pieces of data,
ensuring correct interpretation. These components supply context for data and enhance
the visual appeal of a report.

For information about adding contextual information to specialized report types, see
Creating a Graph on page 1743, Creating Financial Reports With Financial Modeling
Language (FML) on page 1817, and Creating a Free-Form Report on page 1899.

In this chapter:

Creating Headings and Footings

Including an Element in a Heading or
Footing

Applying Font Attributes to a Heading,
Footing, Title, or Label

Adding Borders and Grid Lines

Displaying Syntax Components in
Heading and Footing Objects

Justifying a Heading, Footing, Title, or
Label

Repeating Headings and Footings on
Panels in PDF Report Output

Choosing an Alignment Method for
Heading and Footing Elements

Customizing a Column Title

Controlling Column Title Underlining
Using a SET Command

Controlling Column Title Underlining
Using a StyleSheet Attribute

Creating Labels to Identify Data

Formatting a Heading, Footing, Title, or
Label

Aligning a Heading or Footing Element in
an HTML, XLSX, EXL2K, PDF, PPTX, or
DHTML Report

Aligning a Heading or Footing Element
Across Columns in an HTML or PDF
Report

Aligning Content in a Multi-Line Heading
or Footing

Positioning Headings, Footings, or Items
Within Them

Creating Reports With TIBCO® WebFOCUS Language

 1517

Creating Headings and Footings

Controlling the Vertical Positioning of a
Heading or Footing

Placing a Report Heading or Footing on
Its Own Page

Creating Headings and Footings

There are several types of headings and footings:

Report titles. These are titles you define that display in your browser's title bar when you
run a report or graph in HTML or, as the worksheet tab name in an EXL2K report. For
details see, Creating a Custom Report or Worksheet Title on page 1522.

A report heading, which appears at the top of the first page of a report and a report footing,
which appears on the last page of a report. For details on report headings and footings,
see Creating a Report Heading or Footing on page 1525.

A page heading, which appears at the top of every page of a report and a page footing,
which appears at the bottom of every page of a report. For details on page headings and
footings, see Creating a Page Heading or Footing on page 1532.

A sort heading, which appears in the body of a report to identify the beginning of a group of
related data. And a sort footing, which appears in the body to identify the end of a group of
related data. For details on sort headings and footings, see Creating a Sort Heading or
Footing on page 1543.

The following sample report contains a report heading at the beginning of the report and a
report footing at the end of the report. It also contains a page heading and page footing on
every page of the report.

1518

22. Using Headings, Footings, Titles, and Labels

The following sample report contains sort headings and sort footings, as well as, a page
heading and page footing for reference.

A sort heading looks like this:

A sort footing looks like this:

Limits for Headings and Footings

The following limitations apply to report headings and footings, page headings and footings,
and sort headings and footings:

The space for headings, footings, subheadings, and subfootings is allocated dynamically.
WebFOCUS imposes no limit on the amount of space used.

The maximum number of sort headings plus sort footings in one request is 64.

The maximum limit of nested headings is 64.

If your code for a single heading or footing line is broken into multiple lines in the report
request, you can indicate that they are all a single line of heading using the <0X spot
marker. For more information, see Extending Heading and Footing Code to Multiple Lines in
a Report Request on page 1520.

For PDF and Postscript reports, the heading or footing lines must fit within the maximum
report width to be displayed properly. Also, in order for the report body to be displayed, the
number of heading or footing lines must leave room on the page for at least one detail line
(including column titles).

Creating Reports With TIBCO® WebFOCUS Language

 1519

Creating Headings and Footings

Extending Heading and Footing Code to Multiple Lines in a Report Request

A single line heading or footing code, between double quotation marks, can be a maximum of
32K characters. However, in some editors the maximum length of a line of code in a procedure
is 80 characters. In cases like this, you can use the <0X spot marker to continue your heading
onto the next line. The heading or footing content and spacing appears exactly as it would if
typed on a single line.

Even if you do not need to extend your code beyond the 80-character line limit, this technique
offers convenience, since shorter lines may be easier to read on screen and to print on
printers.

Procedure: How to Extend Heading or Footing Code to Multiple Lines in a Report Request

To extend the length of a single-line heading or footing beyond 80 characters:

1. Begin the heading or footing with double quotation marks (").

2. Split the heading or footing content into multiple lines of up to 76 characters each, using
the <0X spot marker at any point up to the 76th character to continue your heading onto
the next line. (The four remaining spaces are required for the spot marker itself, and a
blank space preceding it.)

3. The heading or footing line can contain a maximum of 410 characters, with each line

ending in an <0X spot marker.

4. Place the closing double quotation marks at the end of the final line of heading or footing

code.

You can use this technique to create a report heading or footing, page heading or footing, or
sort heading or footing of up to 410 characters.

Example:

Extending Heading and Footing Code to Multiple Lines in a Report Request

This request creates a sort heading coded on two lines. The <0X spot marker positions the
first character on the continuation line immediately to the right of the last character on the
previous line. (No spaces are inserted between the spot marker and the start of a continuation
line.)

SET ONLINE-FMT = HTML
SET PAGE-NUM = OFF
JOIN STORE_CODE IN CENTCOMP TO STORE_CODE IN CENTORD

1520

22. Using Headings, Footings, Titles, and Labels

TABLE FILE CENTCOMP
HEADING
"Century Corporation Orders Report"
PRINT PROD_NUM QUANTITY LINEPRICE
BY STORE_CODE NOPRINT
BY ORDER_NUM
ON STORE_CODE SUBHEAD
"Century Corporation orders for store <STORENAME <0X
    (store # <STORE_CODE|) in <STATE|."
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
TYPE=HEADING, FONT='ARIAL', STYLE=BOLD, $
TYPE=SUBHEAD, OBJECT=FIELD, ITEM=2, STYLE=ITALIC, $
TYPE=SUBHEAD, OBJECT=FIELD, ITEM=3, STYLE=BOLD, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1521

Creating Headings and Footings

The partial output is:

Tip: You can use this technique to create a heading of up to 410 characters. Although
demonstrated here for a sort heading, you can use this technique with any heading or footing
line.

Creating a Custom Report or Worksheet Title

You can create a report title that:

Overrides the default report title (FOCUS Report) that appears in the title bar of your
browser in an HTML report or graph.

Replaces the default worksheet tab name with the name you specify in an EXL2K report.

1522

22. Using Headings, Footings, Titles, and Labels

The worksheet tab names for an Excel Table of Contents report are the BY field values that
correspond to the data on the current worksheet. If the user specifies the TITLETEXT keyword
in the stylesheet, it will be ignored.

Excel limits the length of worksheet titles to 31 characters. The following special characters
cannot be used: ':', '?', '*', and '/'.

If you want to use date fields as the bursting BY field, you can include the - character
instead of the / character. The - character is valid in an Excel tab title. However, if you do
use the / character, WebFOCUS will substitute it with the - character.

Syntax:

How to Create a Custom Report Title

Add the following declaration to your WebFOCUS StyleSheet:

TYPE=REPORT, TITLETEXT='title', $

where:

title

Is the text for your title.

The maximum number of characters for:

The worksheet tab name in an EXL2K report is 31. Any text that exceeds 31 characters
will be truncated.

The browser title for an HTML report or graph is 95. This is a limit imposed by the
browser.

Text specified in the title is placed in the file as is and is not encoded. Special
characters, such as <, >, and &, should not be used since they have special meaning
in HTML and may produce unpredictable results.

Note: The words "Microsoft Internet Explorer" are always appended to any HTML report
title.

Creating Reports With TIBCO® WebFOCUS Language

 1523

Creating Headings and Footings

Example:

Creating a Custom Report Title in an HTML Report

The following illustrates how you can replace the default report title in an HTML report using
the TITLETEXT attribute in your StyleSheet.

TABLE FILE SHORT
SUM PROJECTED REGION
BY REGION
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, TITLETEXT='1999 Sales Report', $
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The output is:

1524

22. Using Headings, Footings, Titles, and Labels

Example:

Creating a Custom Report Title in an EXL2K Report

The following illustrates how you can replace the default worksheet tab name in an EXL2K
report using the TITLETEXT attribute in your StyleSheet.

TABLE FILE SHORT
SUM PROJECTED_RETURN
BY REGION
ON TABLE PCHOLD FORMAT EXL2K
ON TABLE SET STYLE *
TYPE=REPORT, TITLETEXT='1999 Sales Report', $
ENDSTYLE
END

The output is:

Creating a Report Heading or Footing

A report heading appears before the first page and is one of the most important components
of a report. It provides a unique name to a report and identifies its purpose or content. A short,
single-line report heading may meet the needs of your user, or you may include multiple lines
of appropriate information.

A report footing appears after the last page of a report. You might add a report footing to
signal the end of data so the user knows that the report is complete. A report footing can also
provide other information, such as the author of the report.

A report heading or footing can include text, fields, Dialogue Manager variables, images, and
spot markers.

Creating Reports With TIBCO® WebFOCUS Language

 1525

Creating Headings and Footings

Syntax:

How to Create a Report Heading

Include the following syntax in a request. Each heading or footing line must begin and end with
a double quotation mark.

ON TABLE [PAGE-BREAK AND] SUBHEAD
 "content ... "
["content ... "]
.
.
.
["content ... "]

where:

PAGE-BREAK

Is an optional command that creates the report heading on the first page by itself,
followed by the page or pages of data. If you do not use PAGE-BREAK, the report
heading appears on the first page of the report, followed by a page heading if one is
supplied, and column titles. For related information, see Placing a Report Heading or
Footing on Its Own Page on page 1692.

SUBHEAD

Is the command required to designate a report heading.

content

Heading or footing content can include the following elements, between double
quotation marks. (If the ending quotation mark is omitted, all subsequent lines of the
request are treated as part of the report heading.)

text

Is text that appears on the first page of a report. You can include multiple lines of
text.

The text must start on a line by itself, following the SUBHEAD command.

Text can be combined with variables and spot markers.

For related information, see Limits for Headings and Footings on page 1519.

variable

Can be any one or a combination of the following:

Fields (real data source fields, virtual fields created with the DEFINE command in a
Master File or report request, calculated values created with the COMPUTE command
in a request, or a system field such as TABPAGENO). You can qualify data source
fields with certain prefix operators.

Dialogue Manager variables.

1526

22. Using Headings, Footings, Titles, and Labels

Images. You can include images in a heading or footing.

For details, see Including an Element in a Heading or Footing on page 1557.

spot marker

Enables you to position items, to identify items to be formatted, and to extend
code beyond the 80-character line limit of some text editors.

<+0> divides a heading or footing into items for formatting. For details, see Identifying
a Heading, Footing, Title, or FML Free Text on page 1273.

</n specifies skipped lines. For details, see Controlling the Vertical Positioning of a
Heading or Footing on page 1685.

<-n to position the next character on the line. For details, see Using Spot Markers to
Refine Positioning on page 1680.

<0X continues a heading or footing specification on the next line of the request. For
details, see Extending Heading and Footing Code to Multiple Lines in a Report Request
on page 1520.

Note: When a closing spot marker is immediately followed by an opening spot marker
(><), a single space text item will be placed between the two spot markers (> <). This
must be considered when applying formatting.

Blank lines

If you omit all text, variables, and spot markers, you have a blank heading or footing
line (for example, " ") which you can use to skip a line in the heading or footing. (You
can also skip a line using a vertical spot marker, such as </1.)

Example:

Creating a Single-Line Report Heading

This request creates a single-line report heading that identifies the content of the report.

TABLE FILE GGSALES
PRINT BUDDOLLARS DOLLARS
BY STCD
WHERE STCD EQ 'R1019'
ON TABLE SUBHEAD
"Sales Report for Store Code R1019"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET WEBVIEWER ON
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1527

Creating Headings and Footings

The output illustrates the placement of a report heading on a multi-page HTML report. The
report heading is at the top of the first page.

1528

22. Using Headings, Footings, Titles, and Labels

Subsequent pages do not contain a heading.

Tip: If you do not see the navigation arrows, click the maximize button.

Creating Reports With TIBCO® WebFOCUS Language

 1529

Creating Headings and Footings

Syntax:

How to Create a Report Footing

Include the following syntax in a request. Each heading or footing line must begin and end with
a double quotation mark.

ON TABLE [PAGE-BREAK AND] SUBFOOT
 "content ... "
["content ... "]
.
.
.
["content ... "]

where:

PAGE-BREAK

Is an optional command that creates the report footing after the last page by itself. If
you do not include PAGE-BREAK, the report footing appears as the last line of the
report. For related information, see Placing a Report Heading or Footing on Its Own
Page on page 1692.

SUBFOOT

Is the command required to designate a report footing.

content

Heading or footing content can include the following elements, between double
quotation marks. (If the ending quotation mark is omitted, all subsequent lines of the
request are treated as part of the report footing unless you are using the <0X spot
marker.)

text

Is text that appears on the last page of a report. You can include multiple lines of
text.

The text must start on a line by itself, following the SUBFOOT command.

Text can be combined with variables and spot markers.

For related information, see Limits for Headings and Footings on page 1519.

variable

Can be any one or a combination of the following:

Fields (real data source fields, virtual fields created with the DEFINE command in a
Master File or report request, calculated values created with the COMPUTE command
in a request, or a system field such as TABPAGENO). You can qualify data source
fields with certain prefix operators.

Dialogue Manager variables.

1530

22. Using Headings, Footings, Titles, and Labels

Images. You can include images in a heading or footing.

For details, see Including an Element in a Heading or Footing on page 1557.

spot marker

Enables you to position items, to identify items to be formatted, and to extend
code beyond the 80-character line limit of the text editor.

<+0> divides a heading or footing into items for formatting. For details, see Identifying
a Heading, Footing, Title, or FML Free Text on page 1273.

</n specifies skipped lines. For details, see Controlling the Vertical Positioning of a
Heading or Footing on page 1685.

<-n to position the next character on the line. For details, see Using Spot Markers to
Refine Positioning on page 1680.

<0X continues a heading or footing specification on the next line of the request. For
details, see Extending Heading and Footing Code to Multiple Lines in a Report Request
on page 1520.

Note: When a closing spot marker is immediately followed by an opening spot marker
(><), a single space text item will be placed between the two spot markers (> <). This
must be considered when applying formatting.

Blank lines

If you omit all text, variables, and spot markers, you have a blank heading or footing
line (for example, " ") which you can use to skip a line in the heading or footing. (You
can also skip a line using a vertical spot marker, such as </1.)

Example:

Creating a Single-Line Report Footing

This request creates a single-line report footing that identifies the author of the report.

TABLE FILE GGSALES
PRINT UNITS
WHERE UNITS GE 1400
BY STCD BY REGION
WHERE REGION EQ 'Northeast'
ON TABLE SUBFOOT
"AUTHOR: MARY SMITH"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET WEBVIEWER ON
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1531

Creating Headings and Footings

The output illustrates the placement of a report footing on a multi-page HTML report. The
report footing follows the data on the last page.

Tip: If you do not see the navigation arrows, click the maximize button.

Creating a Page Heading or Footing

A page heading appears at the top of every page of a report, and a page footing appears at the
bottom of every page.

Add a page heading to identify and reinforce the report content and purpose from page to
page, or include a variable that customizes the heading on each page. For example, consider a
report with employee bank account information, arranged by department. Information for each
department appears on a separate page. The page heading for this report identifies the
department addressed on each page (for example, ACCOUNT REPORT FOR PRODUCTION
DEPARTMENT).

1532

22. Using Headings, Footings, Titles, and Labels

Add a page footing to supply information that warrants repetition on each page, such as the
date of the report, or a reminder that it is confidential. You can also use a page footing to
supply descriptive information about a report, such as PRELIMINARY or DRAFT COPY.

A page heading or footing can include text, fields, Dialogue Manager variables, images, and
spot markers.

In addition, you can use page heading and footing syntax to create a free-form (non-tabular)
report, in which you position data on a page using a layout of your own design. See Creating a
Free-Form Report on page 1899 for details.

A TABLE request can have more than one page heading or footing. For each heading or footing,
a WHEN clause against the data being retrieved can determine whether the heading or footing
displays on the report output.

In a heading, the data for the WHEN clause and data field values displayed in the heading are
based on the first line on the page. In a footing, the data for the WHEN clause and the data
field values displayed in the footing are based on the last line on the page.

The CONDITION StyleSheet attribute enables you to identify a specific WHEN clause so that
you can style each heading or footing separately. For information, see Identifying a Heading or
Footing on page 1277.

Syntax:

How to Create a Page Heading

Include the following syntax in a request. Each heading or footing line must begin and end with
a double quotation mark.

[HEADING [CENTER]]
 "content ... "
["content ... "]
.
.
.
["content ... "]

where:

HEADING

Is an optional command if you place the text before the first display command (for
example, PRINT or SUM); otherwise, it is required to identify the text as a page
heading.

CENTER

Is an optional command that centers the page heading over the report data. For
details, see How to Center a Page Heading or Footing Using Legacy Formatting on page
1622.

Creating Reports With TIBCO® WebFOCUS Language

 1533

Creating Headings and Footings

content

Heading or footing content can include the following elements, between double
quotation marks. (If the ending quotation mark is omitted, all subsequent lines of the
request are treated as part of the page heading.)

text

Is text for the page heading. You can include multiple lines of text.

The text must start on a line by itself, following the HEADING command.

Text can be combined with variables and spot markers.

For related information, see Limits for Headings and Footings on page 1519.

variable

Can be any one or a combination of the following:

Fields (real data source fields, virtual fields created with the DEFINE command in a
Master File or report request, calculated values created with the COMPUTE command
in a request, or a system field such as TABPAGENO). You can qualify data source
fields with certain prefix operators.

Dialogue Manager variables.

Images. You can include images in a heading or footing.

For details, see Including an Element in a Heading or Footing on page 1557.

spot marker

Enables you to position items, to identify items to be formatted, and to extend
code beyond the 80-character line limit of the text editor.

<+0> divides a heading or footing into items for formatting. For details, see Identifying
a Heading, Footing, Title, or FML Free Text on page 1273.

</n specifies skipped lines. For details, see Controlling the Vertical Positioning of a
Heading or Footing on page 1685.

<-n to position the next character on the line. For details, see Using Spot Markers to
Refine Positioning on page 1680.

<0X continues a heading or footing specification on the next line of the request. For
details, see Extending Heading and Footing Code to Multiple Lines in a Report Request
on page 1520.

Note: When a closing spot marker is immediately followed by an opening spot marker
(><), a single space text item will be placed between the two spot markers (> <). This
must be considered when applying formatting.

1534

22. Using Headings, Footings, Titles, and Labels

Blank lines

If you omit all text, variables, and spot markers, you have a blank heading or footing
line (for example, " ") which you can use to skip a line in the heading or footing. (You
can also skip a line using a vertical spot marker, such as </1.)

Example:

Creating a Single-Line Page Heading

This request omits the command HEADING since the page heading text precedes the display
command PRINT. The page heading includes text and an embedded field.

TABLE FILE EMPLOYEE
"ACCOUNT REPORT FOR DEPARTMENT <DEPARTMENT"
PRINT CURR_SAL BY DEPARTMENT BY HIGHEST BANK_ACCT
BY EMP_ID
ON DEPARTMENT PAGE-BREAK
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF,$
ENDSTYLE
END

The output illustrates the placement of a page heading on a multi-page HTML report. The page
heading appears on both pages of the report, identifying the department to which the data
applies. See How to Include a Field Value in a Heading or Footing on page 1558 for
information on embedded field values. The first page of data applies to the MIS department.

Creating Reports With TIBCO® WebFOCUS Language

 1535

Creating Headings and Footings

The second page of data applies to the PRODUCTION department.

Syntax:

How to Create a Page Footing

Include the following syntax in a request. Each heading or footing line must begin and end with
a double quotation mark.

FOOTING [CENTER] [BOTTOM]
  "content ... "
["content ... "]
.
.
.
["content ... "]

where:

FOOTING

Is the required command that identifies the content as a page footing.

CENTER

Is an optional command that centers the page footing over the report data. For details
on CENTER, see How to Center a Page Heading or Footing Using Legacy Formatting on
page 1622.

BOTTOM

Is an optional command that places the footing at the bottom of the page. If you omit
BOTTOM, the page footing appears two lines below the report data. For details on
BOTTOM, see How to Position a Page Footing at the Bottom of a Page on page 1690.

content

Heading or footing content can include the following elements, between double
quotation marks. (If the ending quotation mark is omitted, all subsequent lines of the
request are treated as part of the footing unless you are using the <0X spot marker.)

text

Is text for the page footing. You can include multiple lines of text.

1536

22. Using Headings, Footings, Titles, and Labels

The text must start on a line by itself, following the FOOTING command.

Text can be combined with variables and spot markers.

For related information, see Limits for Headings and Footings on page 1519.

variable

Can be any one of, or a combination of the following:

Fields (real data source fields, virtual fields created with the DEFINE command in a
Master File or report request, calculated values created with the COMPUTE command
in a request, or a system field such as TABPAGENO). You can qualify data source
fields with certain prefix operators.

Dialogue Manager variables.

Images. You can include images in a heading or footing.

For details, see Including an Element in a Heading or Footing on page 1557.

spot marker

Enables you to position items, to identify items to be formatted, and to extend
code beyond the 80-character line limit of the text editor.

<+0> divides a heading or footing into items for formatting. For details, see Identifying
a Heading, Footing, Title, or FML Free Text on page 1273.

</n specifies skipped lines. For details, see Controlling the Vertical Positioning of a
Heading or Footing on page 1685.

<-n positions the next character on the line. For details, see Using Spot Markers to
Refine Positioning on page 1680.

<0X continues a heading or footing specification on the next line of the request. For
details, see Extending Heading and Footing Code to Multiple Lines in a Report Request
on page 1520.

Note: When a closing spot marker is immediately followed by an opening spot marker
(><), a single space text item will be placed between the two spot markers (> <). This
must be considered when applying formatting.

Blank lines

If you omit all text, variables, and spot markers, you have a blank heading or footing
line (for example, " ") which you can use to skip a line in the heading or footing. (You
can also skip a line using a vertical spot marker, such as </1.)

Creating Reports With TIBCO® WebFOCUS Language

 1537

Creating Headings and Footings

Example:

Creating a Multiple-Line Page Footing

This request creates a two-line page footing that identifies the data as preliminary and
indicates when the final report will be available.

TABLE FILE GGSALES
PRINT UNITS DOLLARS
BY CATEGORY BY STCD
WHERE TOTAL DOLLARS GE 25000
FOOTING
"PRELIMINARY SALES FIGURES"
"FINAL TO COME END OF MONTH"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET WEBVIEWER ON
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF,$
ENDSTYLE
END

1538

22. Using Headings, Footings, Titles, and Labels

The partial output illustrates the placement of page footings on a multi-page HTML report. The
page footing appears on both pages of the report.

Creating Reports With TIBCO® WebFOCUS Language

 1539

Creating Headings and Footings

Tip: If you do not see the navigation arrows, click the maximize button.

Syntax:

How to Specify a Heading or Footing With a WHEN Clause

{HEADING [CENTER]|FOOTING}
"text_and_data1"
   .
   .
   .
"text_and_datan"
WHEN expression

where:

text_and_data1, text_and_datan

Is the text and data for each heading or footing line.

expression

Is an expression that resolves to TRUE or FALSE (1 or 0). If its value resolves to TRUE, the
heading or footing is displayed. If the expression resolves to FALSE, the heading or footing
is not displayed.

Reference: Usage Notes for Multiple Headings

HEADING CENTER and FOOTING CENTER apply only to the specific heading or footing in
which they are specified.

A request can have a total of 120 headings, 120 footings, 120 subheadings, and 120
subfootings.

Once you use the BOTTOM option on a footing, all subsequent footings also go to the
bottom of the page.

Freezing HTML and AHTML Headings, Footings, and Column Titles

You may want to scroll the data in a report while freezing headings, column titles, and footings
in order to see the context of the report output while scrolling.

Using StyleSheet attributes, you can set aside a scrollable area for HTML and AHTML report
output.

The HTML HFREEZE reporting feature is supported with the browser versions listed in Web
Browser Support for WebFOCUS. The HFREEZE feature is listed in the 8.1 Browser Support
Matrix in the HTML Reporting Features section JavaScript components row.

1540

Reference: Usage Notes for HTMLARCHIVE With HFREEZE

22. Using Headings, Footings, Titles, and Labels

WebFOCUS interactive reporting features must have a connection to the WebFOCUS client in
order to access the components required to operate successfully.

HTMLARCHIVE can be used to create self-contained HTML pages with user-defined images
when client access is not available.

To generate HTML pages containing user-defined images that can operate interactively, use
one of the following commands:

SET HTMLEMBEDIMG=ON
SET HTMLARCHIVE=ON

Define BASEURL to point directly to the host machine where these files can be accessed using
the following syntax:

SET BASEURL=http://{hostname:portnumber}

For more information on SET BASEURL, see Specifying a Base URL on page 872.

Syntax:

How to Create a Scrollable Area in an HTML Report

TYPE=REPORT,HFREEZE={OFF|ON|TOP|BOTTOM},[SCROLLHEIGHT={AUTO|nn[.n]}], $

where:

HFREEZE=OFF

Does not freeze the heading, column titles, grand totals, and footing. OFF is the default.

HFREEZE=ON

Freezes the heading, column titles, grand totals, and footing.

HFREEZE=TOP

Freezes the heading and column titles.

HFREEZE=BOTTOM

Freezes the grand totals and footing.

SCROLLHEIGHT=AUTO

In an HFREEZE report, the output will be responsive and automatically fit to the height of
the output container when the size of the output container changes.

When AUTOFIT=ON, the report automatically fits to the size of the output container (both
vertically and horizontally) when the size of the output container changes.

Note: The AUTOFIT=ON setting will override the SCROLLHEIGHT setting.

Creating Reports With TIBCO® WebFOCUS Language

 1541

Creating Headings and Footings

nn[.n]

Is the height, in inches, of the scrollable area. The default for non-mobile devices is 4
inches.

Syntax:

How to Create a Scrollable Area in an AHTML Report

TYPE=REPORT,HFREEZE={OFF|ON}, $

where:

HFREEZE=OFF

Does not freeze the heading, column titles, grand totals, and footing. OFF is the default
value.

HFREEZE=ON

Freezes the heading, column titles, grand totals, and footing.

Reference: HFREEZE With Blank Column Titles

The HTML HFREEZE reporting feature supports blank column titles. The vertical HFREEZE scroll
bar will be aligned with the first row of report data.

Reference: Usage Notes for Freezing Areas of HTML Report Output

Report headers and footers can be frozen, while the data lines scroll in HTML and AHTML
reports only. For all other output formats, the StyleSheet attribute HFREEZE is ignored. The
request must include the setting ON TABLE SET HTMLCSS ON, which is the default.

The following HTML features are not supported with HFREEZE:

HFREEZE does not support the placement of images in subheadings and subfootings within
the frozen area in Internet Explorer. HFREEZE does support the placement of images in
subheadings and subfootings within the frozen area in Mozilla Firefox®, Google Chrome™,
and Microsoft Edge®.

Accordion reports

WRAP StyleSheet attribute

Custom HTML tags or JavaScript

Compound Reports

1542

Reference: Usage Notes for Freezing Areas of AHTML Report Output

22. Using Headings, Footings, Titles, and Labels

Report headers and footers can be frozen, while the data lines scroll in AHTML and HTML
reports only. For all other output formats, the StyleSheet attribute HFREEZE is ignored. The
request must include the setting ON TABLE SET HTMLCSS ON, which is the default.

The following AHTML features are not supported with HFREEZE:

SET SUBTOTALS=ABOVE and SET SUBTOTALS=BELOW

In a standard AHTML report, the subtotals display below the data lines and the grandtotal
row is anchored at the bottom of the frozen frame. This behavior occurs regardless of
whether the SET SUBTOTALS command is used.

HFREEZE does not support the placement of images in subheadings and subfootings within
the frozen area.

Accordion reports

Creating a Sort Heading or Footing

A sort heading is text that precedes a change in a sort field value, identifying the beginning of
a group of related data. A sort footing is text that follows a change in a sort field value,
identifying the end of a group of related data.

A sort heading or footing, which appears in the body of a report, helps you identify different
areas of detail in a report. Sort headings or footings can include text, fields, Dialogue Manager
variables, images, and spot markers.

By including a WHEN phrase in a request, you can generate a message, implemented as a sort
heading or footing, for data that meets the criterion you define. For details on conditional
formatting, see Controlling Report Formatting on page 1219.

If you are using a RECAP command to create subtotal values in a calculation, you can replace
the default RECAP label with a more meaningful sort footing by following the RECAP command
for a field with a SUBFOOT command for that field. For details about the RECAP command, see
Including Totals and Subtotals on page 367.

If one or more data fields are embedded in the sort footing, you can omit a display command
from the report request since, by default, data fields in headings and footings are summed. If,
however, a request does contain an explicit SUM command and a display field is also specified
in the sort footing, the field in the sort footing is summed. You can omit the display command
from other types of headings and footings as well. Note that the data for headings is taken
from the first sort group and the data for footings is taken from the last sort group. For related
information, see Limits for Headings and Footings on page 1519.

Creating Reports With TIBCO® WebFOCUS Language

 1543

Creating Headings and Footings

By default, WebFOCUS generates a blank line before a subheading or subfooting. You can
eliminate these automatic blank lines by issuing the SET DROPBLNKLINE=ON command.

Reference: Alignment of Subheadings and Subfootings

By default, with SQUEEZE=ON, the right margin used for borders and backcolor for
subheadings and subfootings is defined based on the maximum width of all heading, footing,
subheading, and subfooting lines. The length of subheading and subfooting lines is tied to the
lengths of the page heading and page footing, not to the size of the data columns in the body
of the report. The ALIGN-BORDERS=BODY attribute in a StyleSheet allows you to align the
subheadings and subfootings with the data/report body on PDF report output instead of the
other heading elements.

1544

22. Using Headings, Footings, Titles, and Labels

Syntax:

How to Create a Sort Heading

Each heading or footing line must begin and end with a double quotation mark, unless you are
using the line continuation spot marker (<ox).

BY fieldname SUBHEAD [NEWPAGE]
 "content ... "
["content ... "]
.
.
.
["content ... "]
[WHEN expression;]
BY fieldname
ON fieldname SUBHEAD [NEWPAGE]
 "content ... "
["content ... "]
.
.
.
["content ... "]
[WHEN expression;]

OR

BY fieldname
ON fieldname SUBHEAD [NEWPAGE]
 "content ... "
["content ... "]
.
.
.
["content ... "]
[WHEN expression;]

where:

fieldname

Is the sort field before which the heading text appears.

content

Heading or footing content can include the following elements, between double
quotation marks. (If the ending quotation mark is omitted, all subsequent lines of the
request are treated as part of the heading.)

text

Is text for the sort heading. You can include multiple lines of text.

The text must start on a line by itself, following the SUBHEAD command.

Text can be combined with variables and spot markers.

For related information, see Limits for Headings and Footings on page 1519.

Creating Reports With TIBCO® WebFOCUS Language

 1545

Creating Headings and Footings

variable

Can be any one of, or a combination of, the following:

Fields (real data source fields, virtual fields created with the DEFINE command in a
Master File or report request, calculated values created with the COMPUTE command
in a request, or a system field such as TABPAGENO). You can qualify data source
fields with certain prefix operators.

Dialogue Manager variables.

Images. You can include images in a heading or footing.

For details, see Including an Element in a Heading or Footing on page 1557.

spot marker

Enables you to position items, to identify items to be formatted, and to extend
code beyond the 80-character line limit of the text editor.

<+0> divides a heading or footing into items for formatting. For details, see Identifying
a Heading, Footing, Title, or FML Free Text on page 1273.

</n specifies skipped lines. For details, see Controlling the Vertical Positioning of a
Heading or Footing on page 1685.

<-n to position the next character on the line. For details, see Using Spot Markers to
Refine Positioning on page 1680.

<0X continues a heading or footing specification on the next line of the request. For
details, see Extending Heading and Footing Code to Multiple Lines in a Report Request
on page 1520.

Note: When a closing spot marker is immediately followed by an opening spot marker
(><), a single space text item will be placed between the two spot markers (> <). This
must be considered when applying formatting.

WHEN expression

Specifies a condition under which a sort heading is displayed, as determined by a
logical expression. You must place the WHEN phrase on a line following the text.

For details on conditional formatting, see Controlling Report Formatting on page 1219. For
related information, see Using Expressions on page 429.

Blank lines

If you omit all text, variables, and spot markers, you have a blank heading or footing
line (for example, " ") which you can use to skip a line in the heading or footing. (You
can also skip a line using a vertical spot marker, such as </1.)

NEWPAGE

Inserts a new page after the sort heading. Column titles appear on every page.

1546

22. Using Headings, Footings, Titles, and Labels

You can use NEWPAGE with PDF reports.In HTML reports, blank space is added instead of
a new page.

Example:

Creating a Sort Heading When a Product Description Changes

This request displays a sort heading each time the product description changes. The sort
heading includes text and an embedded field.

TABLE FILE GGPRODS
PRINT PACKAGE_TYPE AND UNIT_PRICE
WHERE UNIT_PRICE GT 50
BY PRODUCT_DESCRIPTION NOPRINT BY PRODUCT_ID
ON PRODUCT_DESCRIPTION SUBHEAD
"Summary for <PRODUCT_DESCRIPTION"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The sort heading identifies the product that the next line of data applies to.

See Including a Field Value in a Heading or Footing on page 1558 for information on
embedded field values.

Creating Reports With TIBCO® WebFOCUS Language

 1547

Creating Headings and Footings

Example:

Creating a Conditional Sort Heading

This request displays a sort heading for a category only if its sales fall below $17,000,000.

TABLE FILE GGSALES
SUM DOLLARS
BY CATEGORY SUBHEAD
"<CATEGORY ALERT: SALES FALL BELOW $17,000,000"
WHEN DOLLARS LT 17000000;
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

Sales for the category Gifts fall below the specified amount, as the sort heading warns. No
other category is preceded by a sort heading.

See Including a Field Value in a Heading or Footing on page 1558 for information on
embedded field values.

1548

22. Using Headings, Footings, Titles, and Labels

Syntax:

How to Create a Sort Footing

Each heading or footing line must begin and end with a double quotation mark.

For a single sort field, use the syntax

BY fieldname SUBFOOT [WITHIN] [MULTILINES] [NEWPAGE]
 "content ... "
["content ... "]
.
.
.
["content ... "]
[WHEN expression;]
BY fieldname
ON fieldname SUBFOOT [WITHIN] [MULTILINES] [NEWPAGE]
 "content ... "
["content ... "]
.
.
.
["content ... "]
[WHEN expression;]

For multiple sort fields, use the syntax

BY fieldname
ON fieldname SUBFOOT [MULTILINES] [NEWPAGE]
 "content ... "
["content ... "]
.
.
.
["content ... "]
[WHEN expression;]

where:

fieldname

Is the sort field after which the footing text appears.

WITHIN

Causes the fields in the SUBFOOT to be calculated within each value of fieldname.
Without this option, a field in the SUBFOOT is taken from the last line of report output
above the subfooting.

MULTILINES

Suppresses the sort footing when there is only one line of data for a sort field value.
(MULTI-LINES is a synonym for MULTILINES.)

Creating Reports With TIBCO® WebFOCUS Language

 1549

Creating Headings and Footings

content

Heading or footing content can include the following elements, between double
quotation marks. (If the ending quotation mark is omitted, all subsequent lines of the
request are treated as part of the sort footing.)

text

Is text that appears on the first page of a report. You can include multiple lines of
text.

The text must start on a line by itself, following the SUBFOOT command.

Text can be combined with variables and spot markers.

For related information, see Limits for Headings and Footings on page 1519.

variable

Can be any one or a combination of the following:

Fields (real data source fields, a virtual fields created with the DEFINE command in a
Master File or report request, calculated values created with the COMPUTE command
in a request, a system field such as TABPAGENO). You can qualify data source fields
with certain prefix operators.

Dialogue Manager variables.

Images. You can include images in a heading or footing.

For details, see Including an Element in a Heading or Footing on page 1557.

spot marker

Enables you to position items, to identify items to be formatted, and to extend
code beyond the 80-character line limit of the text editor.

<+0> divides a heading or footing into items for formatting. For details, see Identifying
a Heading, Footing, Title, or FML Free Text on page 1273.

</n specifies skipped lines. For details, see Controlling the Vertical Positioning of a
Heading or Footing on page 1685.

<-n to position the next character on the line. For details, see Using Spot Markers to
Refine Positioning on page 1680.

<0X continues a heading or footing specification on the next line of the request. For
details, see Extending Heading and Footing Code to Multiple Lines in a Report Request
on page 1520.

Note: When a closing spot marker is immediately followed by an opening spot marker
(><), a single space text item will be placed between the two spot markers (> <). This
must be considered when applying formatting.

1550

22. Using Headings, Footings, Titles, and Labels

WHEN expression

Specifies a condition under which a sort footing is displayed, as determined by a
logical expression. You must place the WHEN phrase on a line following the text.

For details on conditional formatting, see Controlling Report Formatting on page 1219. For
related information, see Using Expressions on page 429.

Blank lines

If you omit all text, variables, and spot markers, you have a blank heading or footing
line (for example, " ") which you can use to skip a line in the heading or footing. (You
can also skip a line using a vertical spot marker, such as </1.)

NEWPAGE

Inserts a new page before the sort footing.

Creating Reports With TIBCO® WebFOCUS Language

 1551

Creating Headings and Footings

Example:

Creating a Sort Footing When a Product Description Changes

This request displays a sort footing each time the product description changes.

TABLE FILE GGPRODS
PRINT PACKAGE_TYPE AND UNIT_PRICE
WHERE UNIT_PRICE GT 50
BY PRODUCT_DESCRIPTION NOPRINT BY PRODUCT_ID
ON PRODUCT_DESCRIPTION SUBFOOT
"Summary for <PRODUCT_DESCRIPTION"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

See How to Include a Field Value in a Heading or Footing on page 1558 for information on
embedded field values.

1552

22. Using Headings, Footings, Titles, and Labels

Example:

Creating a Conditional Sort Footing With Multiple Sort Options

This report lists orders, order dates, and order totals for the Century Corporation. It uses
conditional sort footings to distinguish between orders that total more than $200,000 and
less than $200,000.

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
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1553

Creating Headings and Footings

The following report appears.

Example:

Suppressing a Sort Footing

This request suppresses the sort footing for any product that has only one line of data (that is,
a product that was only ordered one time on 01/01/96).

TABLE FILE GGORDER
PRINT QUANTITY
BY PRODUCT_CODE NOPRINT BY PRODUCT_DESCRIPTION
WHERE ORDER_DATE EQ '01/01/96'
WHERE STORE_CODE EQ 'R1019'
WHERE PRODUCT_DESCRIPTION EQ 'Hazelnut' OR 'Biscotti' OR 'Croissant'
ON PRODUCT_CODE SUBFOOT MULTILINES
"<PRODUCT_DESCRIPTION has multiple orders."
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

1554

22. Using Headings, Footings, Titles, and Labels

In the output, the sort footing for Biscotti is suppressed.

Example:

Replacing the Default RECAP Label With a Sort Footing

In this request, a SUBFOOT command for the field DEPARTMENT follows a RECAP command for
that field. The RECAP command creates subtotal values for the calculation.

TABLE FILE SHORT
SUM BALANCE AS 'Dollars' ENGLAND_POUND AS 'Sterling'
BY REGION
WHERE REGION EQ 'FAR EAST' OR 'CENTRAL AMERICA' OR 'WESTERN EUROPE';
BY COUNTRY NOPRINT
RECAP EURO/D16=BALANCE * 1.03;
SUBFOOT
" "
"Balance of investments for <COUNTRY> in Euros is <EURO>."
" "
END

Creating Reports With TIBCO® WebFOCUS Language

 1555

Creating Headings and Footings

The sort footing text (for example, "Balance of investments for FRANCE in Euros is
87,336,971.") replaces the default label for the RECAP value (** EURO 87,336,971).

1556

22. Using Headings, Footings, Titles, and Labels

Example:

Omitting a Display Command in a Sort Footing

This request creates a complete report as a sort footing. It does not require a display
command because the sort footing content contains the data fields DEPARTMENT and
SALARY. By default, the field SALARY is summed in the sort footing.

TABLE FILE EMPLOYEE
BY DEPARTMENT NOPRINT SUBFOOT
"<DEPARTMENT DEPARTMENT TOTAL SALARY IS <SALARY"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The output is:

Reference: Usage Notes for Subfoots

SUBFOOT WITHIN is useful where a prefixed field within a sort break would result in a single
value (for example, AVE., MIN, MAX). Use of PCT. or APCT. displays only the last value from
the sort group.

SUBFOOT WITHIN "<prefix.fieldname " does not result in the same value as SUBTOTAL
prefix. The SUBFOOT WITHIN creates a display field that operates on the original input
records. SUBTOTAL with a prefix operates on the internal matrix (so AVE. is the average of
the SUMS or, if a display field had the prefix AVE., the average of the averages). SUBFOOT
WITHIN "<AVE.field " generates an overall average.

Prefix operators are not supported on alphanumeric fields in a WITHIN phrase.

The ST. prefix operator is not supported in a SUBFOOT WITHIN phrase.

Including an Element in a Heading or Footing

You can customize a heading or footing by including:

A field value. See Including a Field Value in a Heading or Footing on page 1558 and
Including a Text Field in a Heading or Footing on page 1565.

Creating Reports With TIBCO® WebFOCUS Language

 1557

Including an Element in a Heading or Footing

A page number. See Including a Page Number in a Heading or Footing on page 1567.

A Dialogue Manager variable. See Including a Dialogue Manager Variable in a Heading or
Footing on page 1567.

An image. See Including an Image in a Heading or Footing on page 1569.

Including a Field Value in a Heading or Footing

You can include a field name in heading or footing text. When the request is run, the output
includes the field value. The result is a customized heading or footing with specific data
identification for the user.

While you can use this technique in any report, it is essential if you are creating a free-form
report. For details, see Creating a Free-Form Report on page 1899.

For requests with multiple display and sort field sets, fields in a report heading or footing, or
page heading or footing, are evaluated as if they were objects of the first display command.
Fields in a sort heading or footing are evaluated as part of the first display command in which
they are referenced. If a field is not referenced, it is evaluated as part of the last display
command.

You can use a prefix operator to derive a field value in a heading or footing. However, the DST.,
MDE., and MDN. prefix operators are not supported in headings or footings in requests that
have an ACROSS phrase or multiple display commands. For a list of operations you can
perform with prefix operators, see Displaying Report Data on page 39.

Two operators are specifically designed for use with a sort footing:

ST. produces a subtotal value of a numeric field at a sort break in a report.

CT. produces a cumulative total of a numeric field.

Syntax:

How to Include a Field Value in a Heading or Footing

<[prefix_operator]fieldname<fieldname[>]

or

<fieldname[>]

where:

<fieldname

Places the field value in the heading or footing, and suppresses trailing blanks in an
alphanumeric field for all values of SET STYLEMODE.

1558

22. Using Headings, Footings, Titles, and Labels

<fieldname>

Places the field value in the heading or footing, and retains trailing blanks in an
alphanumeric field if SET STYLEMODE = FIXED. Suppresses trailing blanks for all other
values of SET STYLEMODE. PDF output retains trailing blanks regardless of the
STYLEMODE setting.

prefix_operator

Performs a calculation directly on the value of a field. A prefix operator is applied to a
single field, and affects only that field.

Note: To display the caret character (<) as text in a heading or footing, use two consecutive
caret symbols (<<).

Example:

Including the Department Name in a Page Heading and Footing

This request includes the field name DEPARTMENT in both the page heading and footing text.
The command HEADING is not required in the request because the page heading text appears
before the command PRINT.

TABLE FILE EMPLOYEE
"<DEPARTMENT : BANK, EMPLOYEES AND SALARIES"
PRINT CURR_SAL
BY DEPARTMENT NOPRINT BY BANK_ACCT
BY LAST_NAME BY FIRST_NAME
ON DEPARTMENT PAGE-BREAK
FOOTING
"<DEPARTMENT EMPLOYEES WITH ELECTRONIC TRANSFER ACCOUNTS"
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET WEBVIEWER ON
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1559

Including an Element in a Heading or Footing

The output displays the output for a multi-page HTML report. On the first page of output, the
value of DEPARTMENT in the page heading and footing is MIS.

1560

22. Using Headings, Footings, Titles, and Labels

On the second page of output, the value of DEPARTMENT is PRODUCTION.

Note: If you do not see the navigation arrows, click the maximize button.

Example:

Displaying a Less Than Symbol in a Heading

The following request computes the difference between REVENUE_US and COGS_US and
displays those rows in which the difference is less than 100,000.

TABLE FILE WF_RETAIL_LITE
HEADING CENTER
" Difference <<  100,000"
" "
SUM COGS_US REVENUE_US
COMPUTE Difference/D20.2 = REVENUE_US - COGS_US;
BY PRODUCT_CATEGORY
WHERE TOTAL Difference LT 100000
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1561

Including an Element in a Heading or Footing

The heading displays the text Difference < 100,000, as shown in the following image.

Example:

Retaining Trailing Blanks in an Alphanumeric Field

Trailing blanks are not retained in standard HTML output. When the output type is HTML,
STYLEMODE is set to FULL by default. To retain trailing blanks in the alphanumeric field
DEPARTMENT, the STYLEMODE setting has been changed to FIXED in this request and the
delimiters < and > have been included around the field name in the sort footing text.

SET STYLEMODE = FIXED
TABLE FILE EMPLOYEE
SUM SALARY
BY DEPARTMENT SUBFOOT
"<DEPARTMENT> DEPARTMENT TOTAL SALARY IS <SALARY"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

Values for DEPARTMENT appear in the sort footing as MIS and PRODUCTION.

Note: SET STYLEMODE=FIXED turns off the HTML formatting of your browser for that report.
The resulting report displays in a fixed font without colors and other web capabilities.

1562

22. Using Headings, Footings, Titles, and Labels

Example:

Using the Prefix Operator TOT in a Page Heading

This request uses the prefix operator TOT to generate grand totals for three fields.

DEFINE FILE SALES
ACTUAL_SALES/D8.2 = UNIT_SOLD - RETURNS;
SALES/F5.1 = 100 * ACTUAL_SALES / UNIT_SOLD;
END
TABLE FILE SALES
"SUMMARY OF ACTUAL SALES"
"UNITS SOLD <TOT.UNIT_SOLD"
"RETURNS <TOT.RETURNS"
"TOTAL SOLD <TOT.ACTUAL_SALES"
" "
"BREAKDOWN BY PRODUCT"
PRINT UNIT_SOLD AND RETURNS AND ACTUAL_SALES
BY PROD_CODE
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT PDF
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1563

Including an Element in a Heading or Footing

The totals appear in the page heading.

Example:

Using Multiple Prefix Operators in a Page Heading

This request uses the prefix operators MAX, MIN, AVE, and TOT. It does not require a display
command because the page heading text contains data fields.

TABLE FILE SALES
"MOST UNITS SOLD WERE <MAX.UNIT_SOLD"
"LEAST UNITS SOLD WERE <MIN.UNIT_SOLD"
"AVERAGE UNITS SOLD WERE <AVE.UNIT_SOLD"
"TOTAL UNITS SOLD WERE <TOT.UNIT_SOLD"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

1564

22. Using Headings, Footings, Titles, and Labels

The prefix operators generate summary data in the page heading.

Example:

Using Multiple Prefix Operators in a Sort Footing

This request uses the prefix operators CNT and AVE in a sort footing. The output does not
contain columns of data. All data is included in the sort footing itself.

TABLE FILE EMPLOYEE
BY DEPARTMENT NOPRINT SUBFOOT
"NUMBER OF EMPLOYEES IN DEPARTMENT <DEPARTMENT = <CNT.LAST_NAME"
"WITH AVERAGE SALARY OF <AVE.CURR_SAL"
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The sort footing is a summary report on the number of employees in a department and their
average salary.

The prefix operators generate summary data in the page heading.

NUMBER OF EMPLOYEES IN DEPARTMENT MIS = 6
WITH AVERAGE SALARY OF $18,000.33
NUMBER OF EMPLOYEES IN DEPARTMENT PRODUCTION = 6
WITH AVERAGE SALARY OF $19,047.00

Including a Text Field in a Heading or Footing

You can include one or more text fields in a heading or footing. A text field has the attribute
FORMAT=TXn in a Master File.

Reference: Limits for Text Fields in a Heading or Footing

You cannot embed a text field in a Financial Modeling Language (FML) report. For details,
see Creating Financial Reports With Financial Modeling Language (FML) on page 1817.

You cannot apply the StyleSheet attribute WRAP to a text field, since a text field is
separated into multiple lines by the character count specified in the FORMAT attribute in
the Master File.

Creating Reports With TIBCO® WebFOCUS Language

 1565

Including an Element in a Heading or Footing

Syntax:

How to Include a Text Field in a Heading or Footing

<TEXTFLD

Example:

Including a Text Field in a Sort Footing

In this example, you create a Master File named TXTFLD.MAS and a corresponding FOCUS data
source named TXTFLD.FOC.

1. Create and save the Master File.

FILENAME = TXTFLD, SUFFIX = FOC,$
SEGNAME=TXTSEG, SEGTYPE = S1,$
   FIELDNAME = CATALOG, FORMAT = A10, $
   FIELDNAME = TEXTFLD,     FORMAT = TX50,$

2. Create and save the following MODIFY procedure. This procedure creates and populates

the data source in a Windows environment.

CREATE FILE TXTFLD
MODIFY FILE TXTFLD
FIXFORM CATALOG/10 TEXTFLD
DATA
COURSE100 This course provides the junior programmer
with the skills needed to code simple reports.%$
COURSE200 This course provides the advanced programmer with
techniques helpful in developing complex
applications.%$
END

3. Run the MODIFY procedure to populate the data source.

4. Create and save the following report request.

TABLE FILE TXTFLD
BY CATALOG SUBFOOT
"<TEXTFLD"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF,$
ENDSTYLE
END

5. Run the report request.

1566

22. Using Headings, Footings, Titles, and Labels

The output is:

                                    CATALOGCOURSE 100
This course provides the junior programmer with
the skills needed to code simple reports
COURSE 200
This course provides the advanced programmer with
techniques helpful in developing complex
applications.

The horizontal space occupied by the text field is determined by the number of characters
specified in the FORMAT attribute in the Master File. In the sample Master File, TX50
means 50 characters wide.

Tip: Since the heading in this example includes a single embedded text field, the default
alignment is satisfactory. However, to include text to introduce the embedded field or add
another embedded field, you may align items in your output to improve readability.

Including a Page Number in a Heading or Footing

You can include a system-generated page number in a heading or footing. For details, see
Laying Out the Report Page on page 1331.

Including a Dialogue Manager Variable in a Heading or Footing

You can include a variable whose values are unknown until run time in a heading or footing.
This technique allows you to customize the heading or footing by supplying a different value
each time the procedure executes.

Variables fall into two categories:

System and statistical variables are predefined and their values are automatically supplied
by the system when a procedure references them. System and statistical variables have
names that begin with &. For example, &DATE generates the current date in report output.

Local (&) and global (&&) variables, whose user-defined values must be supplied at run
time:

A local variable retains its values during the execution of one procedure. Values are lost
after the procedure finishes processing. Values are not passed to other invoked
procedures that contain the same variable name.

A local variable is identified by a single ampersand followed by the variable name.

A global variable retains its value for the duration of the connection to the WebFOCUS
Reporting Server and is passed from the execution of one invoked procedure to the
next.

Creating Reports With TIBCO® WebFOCUS Language

 1567

Including an Element in a Heading or Footing

Because a new session is created on the WebFOCUS Reporting Server each time a
request is submitted, values for global variables are not retained between report
requests. This means that you can use the same global variable in more than one
procedure as long as these procedures are called in the same request.

A global variable is identified by a double ampersand followed by the variable name.

Note: To avoid conflicts, do not name local or global variables beginning with Date, IBI, or
WF. Variable names beginning with these values are reserved for Information Builder use.

For details on Dialogue Manager variables, see the Developing Reporting Applications manual.

Syntax:

How to Include a Dialogue Manager Variable in a Heading or Footing

&[&]variable

where:

&

&&

Introduces a local Dialogue Manager variable.

Introduces a global Dialogue Manager variable.

variable

Is a variable whose value is supplied by the system or by a user at run time.

Example:

Including the Current Date in a Report Heading

This request includes today's date on the second line of the report heading, highlighted in
bold.

TABLE FILE GGSALES
PRINT BUDDOLLARS DOLLARS
BY STCD
WHERE STCD EQ 'R1019'
ON TABLE SUBHEAD
"Sales Report for Store Code R1019"
"&DATE"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF,$
TYPE=TABHEADING, LINE=1, FONT='TIMES', SIZE=10, STYLE=BOLD, $
TYPE=TABHEADING, LINE=2, COLOR=BLUE, $
ENDSTYLE
END

1568

22. Using Headings, Footings, Titles, and Labels

The output is:

Note: You can modify the format of the date. Some formats are:

Variable

Display Format

&DATEtrMMDYY

2002, December 11

&DATEMDYY

&DATEtrMDYY

&DATEQYY

12/11/2002

December 11, 2002

Q4 2002

Including an Image in a Heading or Footing

A StyleSheet enables you to include an image in a heading or footing. An image, such as a
logo, gives corporate identity to a report, or provides visual appeal.

For details on adding and positioning images, see Laying Out the Report Page on page 1331.

Creating Reports With TIBCO® WebFOCUS Language

 1569

Displaying Syntax Components in Heading and Footing Objects

Displaying Syntax Components in Heading and Footing Objects

You can automatically display syntax components from your report or chart request in heading
and footing objects by adding one or more of the following attributes:

<REQUEST.FILTERS. Lists the WHERE and IF conditions in the request.

<REQUEST.VERB_OBJECTS. Lists the display fields referenced in the request.

<REQUEST.SORT_KEYS. Lists all sort fields in the request.

<REQUEST.BYKEYS. Lists all BY sort fields in the request.

<REQUEST.ACROSSKEYS. Lists all ACROSS sort fields in the request.

<REQUEST.VERB_OBJECTS_CONTEXT. Lists the display command syntax used for each
display field.

<REQUEST.SORT_KEYS_CONTEXT. Lists all sort phrases in the request.

Note: The syntax component breaks onto multiple lines if the heading line length extends
beyond the width of the report or chart container.

1570

Example:

Displaying Report Syntax Components

22. Using Headings, Footings, Titles, and Labels

The following request displays all available syntax components from the report request in the
heading. The spot markers (<+0>) are used to separate heading items so they can be styled
separately in the StyleSheet.

TABLE FILE WF_RETAIL_LITE
HEADING
"Display Objects: <+0> <REQUEST.VERB_OBJECTS"
"Sort Fields: <+0> <REQUEST.SORT_KEYS"
"BY Fields: <+0> <REQUEST.BYKEYS"
"ACROSS Fields: <+0> <REQUEST.ACROSSKEYS"
"Filters: <+0> <REQUEST.FILTERS"
" "
"Display Commands: <+0> <REQUEST.VERB_OBJECTS_CONTEXT"
"Sort Phrases: <+0> <REQUEST.SORT_KEYS_CONTEXT
" "
" "
SUM COGS_US REVENUE_US
COMPUTE RATIO/D12.2=REVENUE_US/COGS_US;
BY PRODUCT_CATEGORY SUBTOTAL COGS_US
ACROSS BUSINESS_REGION ACROSS-TOTAL
WHERE BUSINESS_REGION NE 'Oceania'
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
TYPE=REPORT, COLOR = BLUE, SIZE=10, GRID=OFF,$
TYPE=HEADING, ITEM=1, OBJECT=TEXT, FONT=Courier, COLOR=BLUE, STYLE=BOLD,$
TYPE=HEADING, ITEM=2, FONT=Courier, COLOR=TEAL, STYLE=ITALIC,$
TYPE=TITLE, FONT=ARIAL, STYLE=BOLD, COLOR=NAVY,$
TYPE=ACROSSTITLE, FONT=ARIAL, STYLE=BOLD, COLOR=NAVY,$
TYPE=ACROSSVALUE, FONT=ARIAL, STYLE=ITALIC, COLOR=NAVY, SIZE=10,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1571

Repeating Headings and Footings on Panels in PDF Report Output

The output is shown in the following image.

Repeating Headings and Footings on Panels in PDF Report Output

When the columns presented on PDF reports cannot be displayed on a single page, the pages
automatically panel. Paneling places subsequent columns for the same page on overflow
pages. These overflow pages are generated until the entire width of the report is presented,
after which the next vertical page is generated with a new page number and its associated
horizontal panels.

In order to make panels following the initial panel more readable, you can designate that
heading elements from the initial panel should be repeated on each subsequent panel using
the HEADPANEL=ON StyleSheet attribute.

When paneling occurs, if default page numbering is used, the page number presented will
include both the page number and the panel number (for example, 1.1, 1.2, 1.3). Turning
HEADPANEL on will also cause the panel designation to be included in TABPAGENO.

HEADPANEL can be designated for the entire report, causing all headings and footings to be
replicated on the paneled pages. It can also be turned on for just individual headings, footings,
subheadings, or subfootings.

1572

22. Using Headings, Footings, Titles, and Labels

HEADPANEL causes borders from the initial page to be replicated on the paneled pages.
Additional control of subheading and subfooting borders can be gained through the use of
ALIGN-BORDERS which allows for the designation that subitem borders should align with the
body of the data rather than the page or report headings. For more information about using
ALIGN-BORDERS with HEADPANEL see How to Align Subheading and Subfooting Margins With
the Report Body on page 1418.

Syntax:

How to Repeat Heading Elements on Panels

TYPE={REPORT|headfoot [BY=sortcolumn]}, HEADPANEL={ON|OFF}, $

where:

REPORT

Repeats all report headings, footings, page headings, page footings, subheadings,
and subfootings.

headfoot

Identifies a heading or footing. Select from:

TABHEADING, which is a report heading. This appears once at the beginning of the
report and is generated by ON TABLE SUBHEAD.

TABFOOTING, which is a report footing. This appears once at the end of the report and
is generated by ON TABLE SUBFOOT.

HEADING, which is a page heading. This appears at the top of every report page and is
generated by HEADING.

FOOTING, which is a page footing. This appears at the bottom of every report page and
is generated by FOOTING.

SUBHEAD, which is a sort heading. This appears at the beginning of a vertical (BY) sort
group (generated by ON sortfield SUBHEAD).

SUBFOOT, which is a sort footing. This appears at the end of a vertical (BY) sort group
(generated by ON sortfield SUBFOOT).

BY

When there are several sort headings or sort footings, each associated with a
different vertical sort (BY) column, this enables you to identify which sort heading or
sort footing you wish to format.

If there are several sort headings or sort footings associated with different vertical sort
(BY) columns, and you omit this attribute and value, the formatting will be applied to all of
the sort headings or footings.

Creating Reports With TIBCO® WebFOCUS Language

 1573

Repeating Headings and Footings on Panels in PDF Report Output

sortcolumn

Specifies the vertical sort (BY) column associated with one of the report sort headings
or sort footings.

ON

OFF

Repeats the specified heading or footing elements on each panel.

Displays heading or footing elements on the first panel only. OFF is the default value.

Note that the HEADPANEL=ON attribute can only be applied to the entire heading or footing,
not individual lines or items within the heading or footing.

Example:

Repeating All Headings and Footings on Report Panels

The following request against the GGSALES data source sums units sold, budgeted units sold,
dollar sales, and budgeted sales by region, state, city, category, and product. The report has a
page heading and, for each region, a subfooting.

TABLE FILE GGSALES
HEADING
"PRODUCT SALES REPORT"
""
"Page<TABPAGENO"
""
SUM UNITS BUDUNITS DOLLARS BUDDOLLARS
BY REGION NOPRINT
BY ST BY CATEGORY BY PRODUCT
ON REGION SUBFOOT
" "
" SUBFOOT FOR REGION <REGION "
" SUBTOTAL BUDDOLLARS: <ST.BUDDOLLARS SUBTOTAL DOLLARS: <ST.DOLLARS "
" "
ON TABLE SET BYPANEL ON
ON TABLE SET PAGE ON
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE = REPORT, HEADPANEL=OFF,$
ENDSTYLE
END

The request sets BYPANEL ON, so each panel displays the sort field values. However, since
HEADPANEL=OFF for the entire report, the first panel for page 1 has the heading and the
subfooting, but the second panel does not.

1574

22. Using Headings, Footings, Titles, and Labels

The output for page 1 panel 1 has the heading and subfooting, as shown in the following
image. Note that with HEADPANEL=OFF, TABPAGENO does not include the panel number.

Creating Reports With TIBCO® WebFOCUS Language

 1575

Repeating Headings and Footings on Panels in PDF Report Output

The output for page 1 panel 2 does not have the heading or subfooting, as shown in the
following image.

1576

22. Using Headings, Footings, Titles, and Labels

The following output shows panels 1 and 2 if the StyleSheet declaration is changed to set
HEADPANEL=ON for the entire report (TYPE=REPORT, HEADPANEL=ON ,$). The heading and
subfooting are repeated on each panel. With HEADPANEL=ON, TABPAGENO includes the panel
number.

Creating Reports With TIBCO® WebFOCUS Language

 1577

Repeating Headings and Footings on Panels in PDF Report Output

1578

22. Using Headings, Footings, Titles, and Labels

Example:

Repeating a Subfoot on Panels in PDF Report Output

The following request against the GGSALES data source specifies the HEADPANEL=ON
attribute only for the subfoot, not for the entire report. Notice that this request uses the
default page numbering (ON TABLE SET PAGE ON) rather than TABPAGENO to present the page
numbers on each page.

TABLE FILE GGSALES
HEADING
" PRODUCT SALES REPORT"
" "
SUM UNITS BUDUNITS DOLLARS BUDDOLLARS
BY REGION NOPRINT
BY ST BY CITY  BY CATEGORY BY PRODUCT
ON REGION SUBFOOT
" "
" SUBFOOT FOR REGION <REGION "
" SUBTOTAL BUDDOLLARS: <ST.BUDDOLLARS SUBTOTAL DOLLARS:  <ST.DOLLARS "
" "
ON TABLE SET BYPANEL ON
ON TABLE SET PAGE ON
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE = SUBFOOT, HEADPANEL=ON,$

ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1579


Repeating Headings and Footings on Panels in PDF Report Output

Panel 1 displays both the heading and the subfooting, as shown in the following image.

1580

22. Using Headings, Footings, Titles, and Labels

Panel 2 displays only the subfooting, not the heading, as shown in the following image.

Creating Reports With TIBCO® WebFOCUS Language

 1581

Repeating Headings and Footings on Panels in PDF Report Output

Since the page heading is not repeated, if you use the <TABPAGENO system variable to place
the page number in the heading, it will not display the panel number and will not display on the
second panel.

TABLE FILE GGSALES
HEADING
" PRODUCT SALES REPORT PAGE <TABPAGENO"
" "
SUM UNITS BUDUNITS DOLLARS BUDDOLLARS
BY REGION NOPRINT
BY ST BY CITY  BY CATEGORY BY PRODUCT
ON REGION SUBFOOT
" "
" SUBFOOT FOR REGION <REGION "
" SUBTOTAL BUDDOLLARS: <ST.BUDDOLLARS SUBTOTAL DOLLARS:  <ST.DOLLARS "
" "
ON TABLE SET BYPANEL ON
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE = SUBFOOT, HEADPANEL=ON,$

ENDSTYLE
END

1582


22. Using Headings, Footings, Titles, and Labels

The first panel displays the page number in the heading, without the panel number, as shown
in the following image.

Creating Reports With TIBCO® WebFOCUS Language

 1583

Repeating Headings and Footings on Panels in PDF Report Output

The second panel does not display the heading and therefore, does not display the embedded
page number, as shown in the following image.

1584

22. Using Headings, Footings, Titles, and Labels

Example:

Repeating Styled Headings and Footings on Paneled Pages

The following request against the GGSALES data source has a report heading, a page heading
with an image, a footing, a subheading, a subfooting, and a subtotal.

SET BYPANEL=ON
DEFINE FILE GGSALES
SHOWCATPROD/A30 = CATEGORY || ' / ' || PRODUCT;
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
"Subheading Region <REGION"
" "
ON REGION SUBTOTAL AS '*TOTAL'
ON REGION SUBFOOT WITHIN
" "
"Subfooting Region <REGION"
" "
ON TABLE SUBHEAD
"Report Heading"
HEADING
"Page <TABPAGENO  "
" "
" "
" "
FOOTING
" "
"PAGE FOOTING "
ON TABLE SUBFOOT
" "
"Report Footing"
ON TABLE SET PAGE-NUM OFF
-*ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
     UNITS=IN,
     SQUEEZE=ON,
     ORIENTATION=PORTRAIT,
$

Creating Reports With TIBCO® WebFOCUS Language

 1585


Repeating Headings and Footings on Panels in PDF Report Output

TYPE=REPORT,
     FONT='ARIAL',
     SIZE=9,
     HEADPANEL=ON,
     BORDER=ON,
$
TYPE=TITLE,
     STYLE=BOLD,
$
TYPE=TABHEADING,
     SIZE=20,
     STYLE=BOLD,
$
TYPE=TABFOOTING,
     SIZE=20,
     STYLE=BOLD,
$
TYPE=HEADING,
     SIZE=12,
     STYLE=BOLD,
$
TYPE=HEADING,
     LINE=1,
     JUSTIFY=RIGHT,
$
TYPE=HEADING,
     LINE=2,
     JUSTIFY=RIGHT,
$
TYPE=HEADING,
     LINE=3,
     JUSTIFY=RIGHT,
$
TYPE=HEADING,
     LINE=4,
     JUSTIFY=RIGHT,
$
TYPE=HEADING,
     LINE=5,
     JUSTIFY=RIGHT,
$
TYPE=HEADING,
     IMAGE=smplogo1.gif,
     POSITION=(+0.000000 +0.000000),
$
TYPE=FOOTING,
     SIZE=12,
     STYLE=BOLD,
     JUSTIFY=RIGHT,
$
TYPE=SUBHEAD,
     SIZE=10,
     STYLE=BOLD,
$

1586

22. Using Headings, Footings, Titles, and Labels

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

 1587

Repeating Headings and Footings on Panels in PDF Report Output

Since HEADPANEL=ON for the entire report, both panels display all of the heading and footing
elements.

The following image shows page 1 panel 1.

1588

22. Using Headings, Footings, Titles, and Labels

The following image shows page 1 panel 2.

Customizing a Column Title

A column title identifies the data in a report. Use the AS phrase to change the default column
title for customized data identification or more desirable formatting. You can change a column
title:

In a request.

In a Master File.

A column title defaults to the field name in the Master File. For a calculated value (one created
with COMPUTE), the title defaults to the field name in the request.

Creating Reports With TIBCO® WebFOCUS Language

 1589

Customizing a Column Title

Example:

Using Default Column Titles

Consider this request:

TABLE FILE EMPDATA
SUM SALARY
BY DEPT
BY LASTNAME
WHERE DEPT IS 'SALES' OR 'CONSULTING' OR 'ACCOUNTING'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The report output illustrates these default column titles:

The column title for the field named in the display command (SUM) is SALARY.

The column titles for the fields named in the BY phrases are DEPT and LASTNAME.

The output is:

1590

22. Using Headings, Footings, Titles, and Labels

Reference: Limits for Column Titles

The width allotted for column titles has no limit other than the memory available.

A column title for a styled output format can contain up to 16 lines of text.

You can replace a column title for a field named in an ACROSS phrase by only one line of
text.

Syntax:

How to Customize a Column Title in a Request

fieldname AS 'title_line_1 [,title_line_2,...]'

where:

fieldname

Is a field named in a display command (such as PRINT or SUM), ACROSS phrase, or
BY phrase.

title_line_1,title_line_2

Is the customized column title, enclosed in single quotation marks.

To specify a multiple-line column title, separate each line with a comma.

To customize a column title for a calculated value, use the syntax:

COMPUTE fieldname[/format] = expression AS 'title'

For related information, see Creating Temporary Fields on page 277.

Tip:

To suppress the display of a column title, enter two consecutive single quotation marks
without the intervening space. For example:

PRINT LAST_NAME AS ''

To display underscores, enclose blanks in single quotation marks.

If you use an AS phrase for a calculated value, repeat the COMPUTE command before
referencing the next computed field.

Multi-line column titles created with the AS phrase are not supported for ACROSS fields.

Creating Reports With TIBCO® WebFOCUS Language

 1591

Customizing a Column Title

Example:

Customizing Column Titles in a Request

This request customizes the column titles for the field named in the SUM command (SALARY),
and the fields named in the BY phrases (DIV and DEPT).

TABLE FILE EMPDATA
SUM SALARY AS 'Total,Salary'
BY DIV AS 'Division'
BY DEPT AS 'Department'
WHERE DIV EQ 'NE' OR 'SE' OR 'CORP'
HEADING
"Current Salary Report"
ON TABLE SET STYLE *
TYPE=REPORT,GRID=OFF,$
ENDSTYLE
END

The output is:

1592

22. Using Headings, Footings, Titles, and Labels

Example:

Suppressing a Column Title

This request suppresses the column title for LAST_NAME. It also illustrates a multiple-line
column title (EMPLOYEE NUMBER) for the data for EMP_ID.

TABLE FILE EMPLOYEE
PRINT FIRST_NAME AS 'NAME' AND LAST_NAME AS ''
BY DEPARTMENT
BY EMP_ID AS 'EMPLOYEE,NUMBER'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1593

Customizing a Column Title

Example:

Customizing a Column Title for a Calculated Value

This request customizes the column title for the calculated value REV.

TABLE FILE SALES
SUM UNIT_SOLD RETAIL_PRICE
COMPUTE REV/D12.2M = UNIT_SOLD * RETAIL_PRICE;AS 'GENERATED REVENUE'
BY PROD_CODE
WHERE CITY EQ 'NEW YORK'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The output is:

Customizing a Column Title in a Master File

You can change the default column title using the optional TITLE attribute for a field. Any
formatting you apply to the field will be applied to its customized title.

See the Developing Reporting Applications manual for details on the TITLE attribute.

Distinguishing Between Duplicate Field Names

The command SET QUALTITLES determines whether or not duplicate field names appear as
qualified column titles in report output. A qualified column title distinguishes between identical
field names by including the segment.

Column titles specified in an AS phrase are used when duplicate field names are referenced in
a MATCH command, or when duplicate field names exist in a HOLD file.

1594

22. Using Headings, Footings, Titles, and Labels

Syntax:

How to Distinguish Between Duplicate Field Names

SET QUALTITLES = {ON|OFF}

where:

ON

Enables qualified column titles when duplicate field names exist and SET FIELDNAME
is set to NEW (the default). For information on SET commands, see the Developing
Reporting Applications manual.

OFF

Disables qualified column titles. OFF is the default value.

Controlling Column Title Underlining Using a SET Command

The SET TITLELINE command allows you to control whether column titles are underlined for
report output.

Syntax:

How to Control Column Title Underlining Using a SET Command

SET TITLELINE =  (ON|OFF|SKIP)

ON TABLE SET TITLELINE  (ON|OFF|SKIP)

where:

ON

Underlines column titles. ON is the default value.

OFF

Replaces the underline with a blank line.

SKIP

Omits both the underline and the line on which the underline would have displayed.

Note: ACROSSLINE is a synonym for TITLELINE.

Example:

Controlling Column Title Underlining Using a SET Command

The following request has a BY and an ACROSS field.

SET TITLELINE=ON
TABLE FILE GGSALES
SUM UNITS BY PRODUCT
ACROSS REGION
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/javaassist/intl/EN/ENIADefault_combine.sty,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1595

Controlling Column Title Underlining Using a SET Command

With the default value (ON) for SET TITLELINE, the column titles are underlined.

With SET TITLELINE=OFF, the column titles are not underlined, but the blank line where the
underlines would have been is still there.

1596

22. Using Headings, Footings, Titles, and Labels

With SET TITLELINE=SKIP, both the underlines and the blank line are removed.

Controlling Column Title Underlining Using a StyleSheet Attribute

The TITLELINE attribute allows you to control whether column titles are underlined for report
output.

Syntax:

How to Control Column Title Underlining Using a StyleSheet Attribute

TYPE={REPORT|TITLE}, TITLELINE =  (ON|OFF|SKIP)

where:

ON

OFF

Underlines column titles. ON is the default value.

Replaces the underline with a blank line.

SKIP

Omits both the underline and the line on which the underline would have displayed.

Creating Reports With TIBCO® WebFOCUS Language

 1597

Controlling Column Title Underlining Using a StyleSheet Attribute

Example:

Controlling Column Title Underlining Using a StyleSheet Attribute

The following request has a BY and an ACROSS field.

TABLE FILE GGSALES
SUM UNITS BY PRODUCT
ACROSS REGION
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, TITLELINE=ON, GRID=OFF, FONT=ARIAL,$
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/javaassist/intl/EN/ENIADefault_combine.sty,$
ENDSTYLE
END

With the default value (ON) for TITLELINE, the column titles are underlined.

1598

22. Using Headings, Footings, Titles, and Labels

With TITLELINE=OFF, the column titles are not underlined, but the blank line where the
underlines would have been is still there.

With TITLELINE=SKIP, both the underlines and the blank line are removed.

Creating Reports With TIBCO® WebFOCUS Language

 1599

Creating Labels to Identify Data

Creating Labels to Identify Data

Labels enable you to provide meaningful and distinct names for the following report elements
that are otherwise identified by generic labels:

Row and column totals. See Creating a Label for a Row or Column Total on page 1600.

Subtotals for sort groups. See Creating a Label for a Subtotal and a Grand Total on page
1602.

Rows in a financial report. See Creating a Label for a Row in a Financial Report on page
1607.

Creating a Label for a Row or Column Total

A label for a row or column total identifies the sum of values for two or more fields. A label
draws attention to the total. It is particularly important that you create a label for a row or
column total if you have both in one report.

For related information, see Including Totals and Subtotals on page 367.

Syntax:

How to Create a Label for a Row or Column Total

fieldname [AND] ROW-TOTAL[/justification][/format] [AS 'label']
fieldname [AND] COLUMN-TOTAL[/justification] [AS 'label']

or

fieldname [AND] COLUMN-TOTAL[/justification] [AS 'label']

where:

fieldname

Is a field named in a display command.

justification

Is the alignment of the label. Valid values are:

L which left justifies the label.

R which right justifies the label.

C which centers the label.

For related information, see Justifying a Label for a Row or Column Total on page 1629.

format

Is the format of the row or column total. When fields with the same format are
summed, the format of the total is the same as the format of the fields. When fields

1600

22. Using Headings, Footings, Titles, and Labels

with different formats are summed, the default D12.2 is used for either the row or
column total.

label

Is the customized row or column total label. The default label is TOTAL.

You can also specify a row or column total with the ON TABLE phrase. With this syntax, you
cannot include field names with ROW-TOTAL. Field names are optional with COLUMN-TOTAL.

ON TABLE ROW-TOTAL[/justification][/format] [AS 'label']
ON TABLE COLUMN-TOTAL[/justification] [AS 'label']
 [fieldname fieldname fieldname]

If a request queries a field created with COMPUTE, the value of that field is included in a row
or column total. Keep that in mind when customizing a label that identifies the total.

Example:

Creating a Label for a Row and Column Total

This request creates the label Total Population by State for the row total, and the label Total
Population by Gender for the column total. The format D12 for ROW-TOTAL displays that data
with commas.

TABLE FILE GGDEMOG
PRINT MALEPOP98 FEMPOP98
ROW-TOTAL/D12 AS 'Total Population by State'
BY ST
WHERE (ST EQ 'WY' OR 'MT')
ON TABLE COLUMN-TOTAL AS 'Total Population by Gender'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1601

Creating Labels to Identify Data

Example:

Creating a Row Total Label With ACROSS

This request adds the populations of two states, sorts the information using the ACROSS
phrase, and labels the row totals as Total by Gender. There are two row totals within the Total
by Gender column, Male Population and Female Population.

TABLE FILE GGDEMOG
SUM MALEPOP98/D12 FEMPOP98/D12
ROW-TOTAL AS 'Total by Gender'
ACROSS ST
WHERE ST EQ 'WY' OR 'MT';
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The output is:

Creating a Label for a Subtotal and a Grand Total

Frequently, a report contains detailed information for a sort group, and it is useful to provide a
subtotal for such a group, and a grand total for all groups at the end of the report.

For related information see Including Totals and Subtotals on page 367.

Syntax:

How to Create a Label for a Subtotal or a Grand Total

{BY|ON} fieldname {SUB-TOTAL|SUBTOTAL|COLUMN-TOTAL} [MULTILINES]
        [field1 [AND] field2...] [AS 'label'] [WHEN expression;]

where:

fieldname

Is a sort field named on a BY or ON phrase.

MULTILINES

Suppresses a subtotal when there is only one value at a sort break. After it is
specified, MULTILINES suppresses the subtotal for every sort break with only one
detail line. MULTI-LINES is a synonym for MULTILINES.

1602

22. Using Headings, Footings, Titles, and Labels

field1 field2

Are specific fields that will be subtotaled. A specified field overrides the default, which
includes all numeric display fields.

AS 'label'

Is the customized label for the subtotal. You cannot change the default label for a
higher level sort field if using SUB-TOTAL.

WHEN expression

Specifies a conditional subtotal as determined by a logical expression. For details,
see Using Expressions on page 429.

Example:

Creating a Label for a Subtotal and a Grand Total

This request creates a customized label for the subtotal, which is the total dollar amount
deducted from employee paychecks for city taxes per department; and the grand total which is
the total dollar amount for both departments.

TABLE FILE EMPLOYEE
SUM DED_AMT BY DED_CODE BY DEPARTMENT
BY BANK_ACCT
WHERE DED_CODE EQ 'CITY'
WHERE BANK_ACCT NE 0
ON DEPARTMENT SUBTOTAL AS 'Total City Deduction for'
ON TABLE COLUMN-TOTAL AS '**GRAND TOTAL**'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1603

Creating Labels to Identify Data

In the output, the department values MIS and PRODUCTION are included by default in the
customized subtotal label.

Example:

Creating a Label for the Subtotal of a Specific Field

This request creates a customized label, Order Total, for the subtotal for LINEPRICE. It uses
the default label TOTAL for the grand total.

TABLE FILE CENTORD
PRINT PNUM QUANTITY LINEPRICE
BY ORDER_NUM SUBTOTAL LINEPRICE AS 'Order Total'
WHERE ORDER_NUM EQ '28003' OR '28004';
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

1604

22. Using Headings, Footings, Titles, and Labels

The output is:

Syntax:

How to Create a Label for the Subtotal of a Calculated Value

{BY|ON} fieldname {SUMMARIZE|RECOMPUTE} [MULTILINES]
        [field1 [AND] field2...] [AS 'label'] [WHEN expression;]
ON TABLE {SUMMARIZE|RECOMPUTE}

where:

fieldname

Is a sort field named on a BY or ON phrase.

MULTILINES

Suppresses a subtotal when there is only one value at a sort break. After it is
specified, MULTILINES suppresses the subtotal for every sort break with only one
detail line. MULTI-LINES is a synonym for MULTILINES.

field1 field2

Are specific fields that will be subtotaled. Specified fields override the default, which
includes all numeric display fields.

Creating Reports With TIBCO® WebFOCUS Language

 1605

Creating Labels to Identify Data

AS 'label'

Is the customized label for the subtotal. You cannot change the default label for a
higher level sort field if using SUMMARIZE.

WHEN expression

Specifies a conditional subtotal as determined by a logical expression. For details,
see Using Expressions on page 429.

You can also generate a subtotal with the ON TABLE phrase:

ON TABLE {SUMMARIZE|RECOMPUTE}

Example:

Creating a Label for the Subtotal of a Calculated Value

This request creates a customized label for the subtotal, including the calculation for the field
DG_RATIO, created with COMPUTE.

TABLE FILE EMPLOYEE
SUM GROSS DED_AMT AND COMPUTE
DG_RATIO/F4.2 = DED_AMT / GROSS;
BY DEPARTMENT BY BANK_ACCT
WHERE BANK_ACCT NE 0
ON DEPARTMENT SUMMARIZE AS 'SUBTOTAL FOR '
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

1606

22. Using Headings, Footings, Titles, and Labels

In the output, the department values MIS and PRODUCTION are included by default in the
customized subtotal label. The default grand total label is TOTAL.

Creating a Label for a Row in a Financial Report

Financial Modeling Language (FML) meets the special needs associated with creating,
calculating, and presenting financially oriented data. FML reports are structured on a row-by-
row basis. This organization gives you greater control over the data incorporated into a report
and over its presentation.

You identify rows by labels that you can customize for accurate data identification and format
to enhance the visual appearance and clarity of the data.

For details on FML reports, see Creating Financial Reports With Financial Modeling Language
(FML) on page 1817.

Formatting a Heading, Footing, Title, or Label

You can use a variety of strategies for enhancing the context-building elements in a report, that
is, the headings, footings, column and row titles, and labels you assign to row and column
totals and to subtotals. These additions enhance the visual appeal of a report and
communicate a sense of completeness, using font and color for emphasis and distinctions,
and alignment to add structural clarity and facilitate comprehension.

Creating Reports With TIBCO® WebFOCUS Language

 1607

Formatting a Heading, Footing, Title, or Label

You can:

Apply font characteristics to column and row titles, to headings, footing, and elements in
them, and to subtotals, grand totals, and subtotal calculations. For more information, see
Applying Font Attributes to a Heading, Footing, Title, or Label on page 1609.

Add borders around headings and footings and grid lines around headings, footings, and
column titles. For more information, see Laying Out the Report Page on page 1331.

You can also add space between heading or footing content and grid lines. For more
information, see Controlling the Vertical Positioning of a Heading or Footing on page 1685.

Left-justify, right-justify, or center a heading, footing, or individual lines in a multi-line
heading or footing, column titles, and subtotals. For more information, see Justifying a
Heading, Footing, Title, or Label on page 1616. See also How to Center a Page Heading or
Footing Using Legacy Formatting on page 1622 and How to Justify a Column Title Using a
StyleSheet on page 1625.

You can also justify a label for a row or column total. For more information, see Justifying a
Label for a Row or Column Total on page 1629.

Align a heading or footing, or elements within a heading or footing, based on:

Data column position in the main HTML table or on column position in an embedded
HTML table created for the heading or footing in the report. These alignment techniques
are supported for HTML reports. For more information, see Aligning a Heading or Footing
Element in an HTML, XLSX, EXL2K, PDF, PPTX, or DHTML Report on page 1635.

Explicit width and justification specifications for multi-line headings and footings,
including unit measurements (like inches) to enforce the alignment of decimal points in
stacked numeric or alphanumeric data. These alignment techniques are supported for
HTML and PDF reports. For more information, see Aligning Content in a Multi-Line
Heading or Footing on page 1659.

An absolute or relative starting position, defined by either a unit measurement (like
inches) or a column position. These alignment techniques are supported for PDF
reports, although some features are also supported for HTML when used with an
internal cascading style sheet. For more information, see Positioning Headings, Footings,
or Items Within Them on page 1671.

For assistance in determining which of these approaches best suits your needs, see
Choosing an Alignment Method for Heading and Footing Elements on page 1633.

Control the vertical positioning of a heading or footing. For more information, see
Controlling the Vertical Positioning of a Heading or Footing on page 1685.

1608

22. Using Headings, Footings, Titles, and Labels

Position a report or sort heading or footing on a separate page. See Placing a Report
Heading or Footing on Its Own Page on page 1692.

Applying Font Attributes to a Heading, Footing, Title, or Label

You can specify font family, size, color, and style for any report element you can identify in a
StyleSheet:

Row and column titles. Styling is applied to either the default title or a customized title.

Headings and footings, and elements within them, including specific lines in a multi-line
heading or footing, items in a line, text strings, and embedded fields. Note that you can
also specify background color for individual elements.

Labels for subtotals, grand totals, subtotal calculations, and row totals. Styling applies to
default or customized names.

Page numbers in a heading or footing.

Underlines and skipped lines (not supported in HTML reports).

For detailed syntax, see Identifying a Report Component in a WebFOCUS StyleSheet on page
1249. For details on font options, including size, color, and style, see Formatting Report Data
on page 1697.

Example:

Applying Font Characteristics to a Report Heading and Column Titles

This request uses a StyleSheet to select 12-point Arial bold for the report heading (Sales
Report), and 10-point Arial italic for the default column titles (Category, Product, Unit Sales,
Dollar Sales), based on the HTML point scale, which differs from standard point sizes. See
Formatting Report Data on page 1697.

Creating Reports With TIBCO® WebFOCUS Language

 1609

Applying Font Attributes to a Heading, Footing, Title, or Label

For an HTML report, the font name must be enclosed in single quotation marks. The
StyleSheet attribute TYPE = TABHEADING identifies the report heading, and the attribute TYPE
= TITLE identifies the column titles.

TABLE FILE GGSALES
SUM UNITS DOLLARS
BY CATEGORY BY PRODUCT
ON TABLE SUBHEAD
"Sales Report"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID=OFF, $
TYPE = TABHEADING, FONT = 'ARIAL', SIZE = 12, STYLE = BOLD, $
TYPE = TITLE, FONT = 'ARIAL', SIZE = 10, STYLE = ITALIC, $
ENDSTYLE
END

The output is:

1610

22. Using Headings, Footings, Titles, and Labels

Example:

Setting Font Size for a Report Heading Using an Internal Cascading Style Sheet

An internal cascading style sheet enables you to specify an absolute size, measured in points,
rather than the corresponding HTML point scale, thereby providing greater control over the
appearance of fonts in a report. See Formatting Report Data on page 1697 and Controlling
Report Formatting on page 1219.

This request generates an internal cascading style sheet and specifies font characteristics for
the report heading.

TABLE FILE GGSALES
SUM UNITS DOLLARS
BY CATEGORY BY PRODUCT
ON TABLE SUBHEAD
"Sales Report"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID=OFF, $
TYPE = TABHEADING, FONT = 'ARIAL', SIZE = 12, STYLE = BOLD, $
TYPE = TITLE, FONT = 'ARIAL', SIZE = 10, STYLE = ITALIC, $
ENDSTYLE
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1611

Applying Font Attributes to a Heading, Footing, Title, or Label

Example:

Applying Font Styles to a System Variable in a Report Heading

This request includes the system variable &DATE in the heading. Styling is italic to distinguish
it from the rest of the heading text, which is bold. The spot marker <+0> creates two items in
the heading so that each one can be formatted separately.

TABLE FILE GGSALES
PRINT BUDDOLLARS DOLLARS
BY STCD
WHERE STCD EQ 'R1019'
ON TABLE SUBHEAD
"Sales Report for Store Code R1019 <+0>&DATE"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF,$
TYPE=TABHEADING, FONT='TIMES', SIZE=10, STYLE=BOLD,$
TYPE=TABHEADING, ITEM=2, STYLE=ITALIC,$
ENDSTYLE
END

The partial output is:

1612

22. Using Headings, Footings, Titles, and Labels

Adding Borders and Grid Lines

You can add borders and grid lines to headings, footings, titles and labels. For detailed syntax,
see Laying Out the Report Page on page 1331.

Example:

Adding a Grid Around a Report Heading in a PDF Report

This request generates a PDF report with a grid around the heading, created with the GRID
attribute, to set the heading off from the body of the report.

TABLE FILE GGSALES
SUM BUDUNITS UNITS BUDDOLLARS DOLLARS
BY CATEGORY
ON TABLE SUBHEAD
"SALES REPORT"
"**(CONFIDENTIAL)**"
"December 2001 </1"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT PDF
ON TABLE SET SQUEEZE ON
ON TABLE SET STYLESHEET *
TYPE = TABHEADING, JUSTIFY = CENTER, GRID=ON, $
ENDSTYLE
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1613

Adding Borders and Grid Lines

Example:

Emphasizing Column Titles With Horizontal Lines in a PDF Report

This request generates a PDF report with horizontal lines, created with the HGRID attribute,
above and below the column titles.

TABLE FILE GGSALES
SUM BUDUNITS UNITS BUDDOLLARS DOLLARS
BY CATEGORY
ON TABLE SUBHEAD
"SALES REPORT"
"**(CONFIDENTIAL)**"
"December 2001 </1"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT PDF
ON TABLE SET SQUEEZE ON
ON TABLE SET STYLESHEET *
TYPE = TABHEADING, JUSTIFY = CENTER, FONT=ARIAL, SIZE=12, $
TYPE = TITLE, HGRID=ON, $
END

The output is:

1614

22. Using Headings, Footings, Titles, and Labels

Example:

Formatting a Border Around a Report Heading

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

 1615

Justifying a Heading, Footing, Title, or Label

Example:

Formatting a Report Heading With Top and Bottom Borders

This request generates a light blue line above the heading and a heavy double line of the same
color below the heading. The request does not specify border lines for the left and right sides
of the heading.

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
TYPE=TABHEADING, JUSTIFY=CENTER, BORDER-TOP=LIGHT, BORDER-COLOR=BLUE,
       BORDER-BOTTOM=HEAVY, BORDER-BOTTOM-STYLE=DOUBLE,$
ENDSTYLE
END

The output is:

Tip: You can use the same BORDER syntax to generate this output in a PDF or PS report.

Justifying a Heading, Footing, Title, or Label

You can left-justify, right-justify, or center the following report elements:

A heading or footing. See Justifying a Heading or Footing on page 1617.

A column title. See Justifying a Column Title on page 1624.

1616

22. Using Headings, Footings, Titles, and Labels

A label for a row or column total. See Justifying a Label for a Row or Column Total on page
1629.

A label for a subtotal or grand total. See Justifying a Label for a Subtotal or Grand Total on
page 1631.

In addition, you can use justification syntax in combination with other StyleSheet syntax to
align headings and footings with other report elements, based on either unit measurements or
relationships to other report elements, such as columns. For a summary of these options, see
Choosing an Alignment Method for Heading and Footing Elements on page 1633.

Justifying a Heading or Footing

You can left-justify, right-justify, or center a heading or footing in a StyleSheet. By default, a
heading or footing is left justified. In addition, you can justify an individual line or lines in a
multiple-line heading or footing.

To center a page heading or footing over the report data, you can use a legacy formatting
technique that does not require a StyleSheet; simply include the CENTER command in a
HEADING or FOOTING command.

Justification behavior in HTML and PDF. For HTML reports, justification is implemented with
respect to the report width. That means a centered heading is centered over the report
content. In contrast, for PDF reports the default justification area is the page width, rather than
the report width, resulting in headings and footings that are not centered on the report. In
most cases, you can achieve justification based on report width in a PDF report by adding the
command SET SQUEEZE=ON to your request. This command improves the appearance of the
report by eliminating excessive white space between columns and implements justification
over the report content. However, if the heading is wider than the report, it will be centered on
the page, even when SQUEEZE=ON.

Tip: You can also use justification syntax in combination with other StyleSheet syntax to align
headings, footings, and items in them with other report elements, based on either unit
measurements or relationships to other columns. For a summary of these options, see
Choosing an Alignment Method for Heading and Footing Elements on page 1633.

Syntax:

How to Justify a Heading or Footing in a StyleSheet

TYPE = headfoot, [LINE = line_#,] JUSTIFY = option, $

where:

headfoot

Is the type of heading or footing. Valid values are TABHEADING, TABFOOTING,
HEADING, FOOTING, SUBHEAD, and SUBFOOT.

Creating Reports With TIBCO® WebFOCUS Language

 1617

Justifying a Heading, Footing, Title, or Label

line_#

Optionally identifies a line by its position in the heading or footing so that you can
individually align it. If a heading or footing has multiple lines and you omit this option,
the value supplied for JUSTIFY applies to all lines.

option

Is the type of justification. Valid values are:

LEFT which left justifies the heading or footing. LEFT is the default value.

RIGHT which right justifies the heading or footing.

CENTER which centers the heading or footing.

For an alternative way to center a page heading or footing without a StyleSheet, see How
to Center a Page Heading or Footing Using Legacy Formatting on page 1622.

Note: JUSTIFY is not supported with WRAP.

Example:

Justifying a Report Heading

This request centers the report heading PRODUCT REPORT, using the attribute JUSTIFY =
CENTER.

TABLE FILE GGPRODS
SUM UNITS BY PRODUCT_DESCRIPTION BY PRODUCT_ID BY VENDOR_NAME
ON TABLE SUBHEAD
"PRODUCT REPORT"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID=OFF, $
TYPE = REPORT, COLUMN = VENDOR_NAME, JUSTIFY = CENTER, $
TYPE = TABHEADING, JUSTIFY = CENTER, $
ENDSTYLE
END

1618

22. Using Headings, Footings, Titles, and Labels

The output is:

Tip: If you wish to run this report in PDF format, add the code ON TABLE SET SQUEEZE ON to
eliminate excessive white space between columns and to center the heading over the report.

For more information on justifying a column title, see Justifying a Column Title on page 1624.

Example:

Justifying Individual Lines in a Multiple-Line Report Heading

In this request, heading line 1 (SALES REPORT) is centered, heading line 2
(**CONFIDENTIAL**) is also centered, and heading line 3 (December 2001) is right justified.

TABLE FILE GGSALES
SUM BUDUNITS UNITS BUDDOLLARS DOLLARS
BY CATEGORY
ON TABLE SUBHEAD
"SALES REPORT"
"**(CONFIDENTIAL)**"
"December 2001"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID=OFF, $
TYPE = TABHEADING, LINE = 1, JUSTIFY = CENTER, $
TYPE = TABHEADING, LINE = 2, JUSTIFY = CENTER, $
TYPE = TABHEADING, LINE = 3, JUSTIFY = RIGHT, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1619

Justifying a Heading, Footing, Title, or Label

The output is:

Tip: To run this report in PDF format, add the code ON TABLE SET SQUEEZE ON to eliminate
excessive white space between columns and to center the heading over the report.

Example:

Centering All Lines in a Multiple-Line Report Heading

This request centers all lines in a multiple-line report heading using the single StyleSheet
attribute for the entire heading.

TABLE FILE GGSALES
SUM BUDUNITS UNITS BUDDOLLARS DOLLARS
BY CATEGORY
ON TABLE SUBHEAD
"SALES REPORT"
"**(CONFIDENTIAL)**"
"December 2001"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID=OFF, $
TYPE = TABHEADING, JUSTIFY = CENTER, $
ENDSTYLE
END

1620

22. Using Headings, Footings, Titles, and Labels

The output is:

Tip: To run this report in PDF format, add the code ON TABLE SET SQUEEZE ON to eliminate
excessive white space between columns and to center the heading over the report.

Reference: Justification Regions and Behavior

The region in which text is justified depends on the relationship of the sizes of certain
elements in the report:

When SQUEEZE=ON, the maximum width of all the heading types in the report is
calculated. This value is called MaxHeadWidth.

If MaxHeadWidth is less than or equal to the total width of the columns of the report,
headings are justified in the space over the report columns.

If MaxHeadWidth exceeds the total width of the columns of the report, headings are
centered and right-justified in the entire width of the page.

When SQUEEZE=OFF, the maximum width of all the headings are not pre-calculated.
Headings are centered in the entire width of the page.

With a styled, multiple-panel report (in which the width exceeds one page), headings can
only appear in the first panel. Thus, the preceding calculations deal with the total width of
the columns in the first panel rather than the total width of all the columns in the report.

Creating Reports With TIBCO® WebFOCUS Language

 1621

Justifying a Heading, Footing, Title, or Label

Syntax:

How to Center a Page Heading or Footing Using Legacy Formatting

{HEADING|FOOTING} CENTER
 "content ... "
["content ... "]
.
.
.
["content ... "]

where:

HEADING

Is a page heading.

FOOTING

Is a page footing.

CENTER

Centers the page heading or footing over or under the report data.

content

Heading or footing content can include the following elements, between double
quotation marks. If the ending quotation mark is omitted, all subsequent lines of the
request are treated as part of the heading or footing.

text

Is text for the heading or footing. You can include multiple lines of text.

The text must start on a line by itself, following the HEADING or FOOTING command.

Text can be combined with variables and spot markers.

For related information, see Limits for Headings and Footings on page 1519.

variable

Can be any one or a combination of the following:

Fields (real data source fields, a virtual fields created with the DEFINE command in a
Master File or report request, calculated values created with the COMPUTE command
in a request, a system field such as TABPAGENO). You can qualify data source fields
with certain prefix operators.

Dialogue Manager variables.

Images. You can include images in a heading or footing.

For details, see Including an Element in a Heading or Footing on page 1557.

1622

22. Using Headings, Footings, Titles, and Labels

spot marker

Enables you to position items, to identify items to be formatted, and to extend
code beyond the 80-character line limit of the text editor.

<+0> divides a heading or footing into items for formatting. For details, see Identifying
a Heading, Footing, Title, or FML Free Text on page 1273.

</n specifies skipped lines. For details, see Controlling the Vertical Positioning of a
Heading or Footing on page 1685.

<-n to position the next character on the line. For details, see Using Spot Markers to
Refine Positioning on page 1680.

<0X continues a heading or footing specification on the next line of the request. For
details, see Extending Heading and Footing Code to Multiple Lines in a Report Request
on page 1520.

Note: When a closing spot marker is immediately followed by an opening spot marker
(><), a single space text item will be placed between the two spot markers (> <). This
must be considered when applying formatting.

Blank lines

If you omit all text, variables, and spot markers, you have a blank heading or footing
line (for example, " ") which you can use to skip a line in the heading or footing. (You
can also skip a line using a vertical spot marker, such as </1.)

Tip: Do not use the command CENTER with the StyleSheet attribute JUSTIFY = CENTER. A
single method will generate the desired result.

Example:

Centering a Page Heading

This request uses the command CENTER in the page heading syntax.

TABLE FILE EMPLOYEE
HEADING CENTER
"ACCOUNT REPORT FOR DEPARTMENT <DEPARTMENT"
PRINT CURR_SAL BY DEPARTMENT BY HIGHEST BANK_ACCT
BY EMP_ID
ON DEPARTMENT PAGE-BREAK
ON TABLE SET PAGE-NUM OFF
ON TABLE SET WEBVIEWER ON
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, SIZE=10, GRID=OFF,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1623

Justifying a Heading, Footing, Title, or Label

The page heading is centered over the report data, as shown in the first page of output.

Tip: If you do not see the navigation arrows, click the maximize button.

Justifying a Column Title

You can left-justify, right-justify, or center a column title for a display field, BY field, ACROSS
field, or calculated value using a StyleSheet.

If a title is specified with an AS phrase in a request, or with the TITLE attribute in a Master File,
that title will be justified, as specified for the field in StyleSheet syntax, if such syntax exists in
the request. For related information, see Customizing a Column Title on page 1589.

Justification behavior in HTML and PDF. For HTML reports, justification is implemented with
respect to the report width. That means a centered column title is centered over a report
column. In contrast, for PDF reports the default justification area is the page width, rather than
the report width, resulting in column titles that are not centered over the report column. You
can achieve justification based on report width in a PDF report by adding the command SET
SQUEEZE=ON to your request. This command improves the appearance of the report by
eliminating excessive white space between columns and implements justification over the
report content.

1624

22. Using Headings, Footings, Titles, and Labels

You can also justify a column title for a display or BY field using legacy formatting methods.
However, when legacy formatting is applied to an ACROSS field, data values, not column titles,
are justified as specified. See How to Justify a Column Title for a Display or BY Field Using
Legacy Formatting on page 1628.

Syntax:

How to Justify a Column Title Using a StyleSheet

To justify a column title for a vertical sort column (generated by BY) or a display column
(generated by PRINT, LIST, SUM, or COUNT), the StyleSheet syntax is

TYPE=TITLE, [COLUMN=column,] JUSTIFY=option, $
TYPE=ACROSSTITLE, [ACROSS=column,] JUSTIFY=option, $
TYPE=ACROSSVALUE, [COLUMN=column,] JUSTIFY=option, $

To justify a horizontal sort column title (generated by ACROSS), the StyleSheet syntax is

TYPE=ACROSSTITLE, [ACROSS=column,] JUSTIFY=option, $

To justify an ACROSS value or a ROW-TOTAL column title in an HTML report, use

TYPE=ACROSSVALUE, [COLUMN=column,] JUSTIFY=option, $

where:

TITLE

Specifies a vertical sort (BY) title or a display field title.

column

Specifies the column whose title you wish to justify. If you omit this attribute and
value, the formatting will be applied to all of the report's column titles. For details on
identifying columns, see Identifying a Report Component in a WebFOCUS StyleSheet on
page 1249.

ACROSSTITLE

Specifies a horizontal sort (ACROSS) title.

ACROSSVALUE

Specifies a horizontal sort (ACROSS) value or a ROW-TOTAL column title.

option

Is the type of justification. Valid values are:

Creating Reports With TIBCO® WebFOCUS Language

 1625

Justifying a Heading, Footing, Title, or Label

LEFT which left justifies the column title. This value is the default for an alphanumeric
field.

RIGHT which right justifies the column title. This value is the default for a numeric or date
field.

CENTER which centers the column title. You cannot center an ACROSSTITLE in a PDF
report.

Note: JUSTIFY is not supported with WRAP.

Example:

Using a StyleSheet to Justify Column Titles for Display and BY Fields

This request centers the column titles for STORE_NAME and ADDRESS1. The default column
title for STORE_NAME is Store Name, as specified in the Master File with the TITLE attribute.
The default column title for ADDRESS1 is Contact, also specified in the Master File. The
request right-justifies the column title for STATE, which is specified in the AS phrase as St.
Each column is identified by its field name and justified separately.

TABLE FILE GGSTORES
PRINT STORE_NAME STATE AS 'St' BY ADDRESS1
WHERE STATE EQ 'CA'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET SQUEEZE ON
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID=OFF, $
TYPE=TITLE, COLUMN=STORE_NAME, JUSTIFY=CENTER, $
TYPE=TITLE, COLUMN=STATE, JUSTIFY=RIGHT, $
TYPE=TITLE, COLUMN=ADDRESS1, JUSTIFY=CENTER, $
ENDSTYLE
END

The output is:

1626

22. Using Headings, Footings, Titles, and Labels

Example:

Using a StyleSheet to Justify a Column Title for ACROSS and ROW-TOTAL Fields

This request centers the column title, State, created by the ACROSS phrase over the two
values (MT and WY) and the row total column title, Total by Gender, over the two row totals
(Male Population and Female Population). Notice that each across value functions as a title for
one or more columns in the report.

TABLE FILE GGDEMOG
SUM MALEPOP98 FEMPOP98
ROW-TOTAL/D12 AS 'Total by Gender'
ACROSS ST
WHERE ST EQ 'WY' OR 'MT';
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
TYPE=ACROSSTITLE, JUSTIFY=CENTER, FONT='TIMES', SIZE=11, STYLE=BOLD, $
TYPE=ACROSSVALUE, COLUMN=N5, JUSTIFY=CENTER, $
ENDSTYLE
END

The output is:

Example:

Using a StyleSheet to Justify a Column Title for a Calculated Value

This request identifies the column title of the calculated value and left justifies it over the data.

TABLE FILE SALES
SUM UNIT_SOLD RETAIL_PRICE
COMPUTE REV/D12.2M = UNIT_SOLD * RETAIL_PRICE;
BY PROD_CODE
WHERE CITY EQ 'NEW YORK'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
TYPE=TITLE, COLUMN=REV, STYLE=BOLD, JUSTIFY=LEFT, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1627

Justifying a Heading, Footing, Title, or Label

The output is:

Note: To run this report in PDF format, add the code ON TABLE SET SQUEEZE ON to eliminate
excessive white space between columns and to justify column titles properly over the data.

Syntax:

How to Justify a Column Title for a Display or BY Field Using Legacy Formatting

fieldname/justification [/format] [AS 'title']

where:

fieldname

Is the name of the field.

justification

Is the type of justification. Valid values are:

L which left justifies the column title. This value is the default for an alphanumeric field.

R which right justifies the column title. This value is the default for a numeric or date field.

C which centers the column title.

/format

Is an optional format specification for the field. For a display field, you can combine
the justification value with the format value (in either order) to adjust the width of the
column data or to specify display options.

AS 'title'

Is an optional customized column title.

Tip: For an ACROSS field, this syntax justifies data values, not column titles. For syntax that
will justify the title, see How to Justify a Column Title Using a StyleSheet on page 1625.

1628

22. Using Headings, Footings, Titles, and Labels

Example:

Using Legacy Formatting to Justify Column Titles for Display and BY Fields

This request centers the column titles for STORE_NAME and ADDRESS1. The default column
title for STORE_NAME is Store Name, as specified in the Master File with the TITLE attribute.
The default column title for ADDRESS1 is Contact, also specified in the Master File. The
request right justifies the column title for STATE, which is specified in the AS phrase as St.

TABLE FILE GGSTORES
PRINT STORE_NAME/C STATE/R AS 'St' BY ADDRESS1/C
WHERE STATE EQ 'CA'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID=OFF, $
ENDSTYLE
END

The output is:

Note: Add the syntax, ON TABLE SET SQUEEZE ON to your request if you are using PDF format.

Justifying a Label for a Row or Column Total

You can left-justify, right-justify, or center a label for a row or column total. For related
information, see Creating Labels to Identify Data on page 1600.

Syntax:

How to Justify a Label for a Row or Column Total Using Legacy Formatting

ROW-TOTAL/justification [/format] [AS 'label']
COLUMN-TOTAL/justification [AS 'label']

or

COLUMN-TOTAL/justification [AS 'label']

where:

justification

Is the type of justification. Valid values are:

L which Left justifies the label.

Creating Reports With TIBCO® WebFOCUS Language

 1629

Justifying a Heading, Footing, Title, or Label

R which right justifies the label.

C which centers the label.

/format

Is an optional format specification for a row total. You can combine the alignment
value with the format value (in either order) to adjust the width of the column data or
specify display options.

AS 'label'

Is an optional customized label.

Example:

Centering a Label for a Row Total

This request creates the stacked label Total, Population, by State for the row total and centers
it. The format D12 for ROW-TOTAL displays commas by default.

TABLE FILE GGDEMOG
PRINT MALEPOP98 FEMPOP98
ROW-TOTAL/C/D12 AS 'Total,Population,by State'
BY ST
WHERE (ST EQ 'WY' OR 'MT')
ON TABLE COLUMN-TOTAL AS 'Total by Gender'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID=OFF, $
ENDSTYLE
END

The output is:

1630

22. Using Headings, Footings, Titles, and Labels

Justifying a Label for a Subtotal or Grand Total

You cannot directly justify a customized label for a subtotal. However, for HTML, EXL2K, or
XLSX report output, if columns are being totaled or subtotaled by the one subtotal command,
and you do not specify a column in the StyleSheet, formatting is applied to the totals and
subtotals of all columns and to the labeling text that introduces the total and subtotal values.
For related information, see Identifying a Report Component in a WebFOCUS StyleSheet on page
1249.

Example:

Justifying Subtotal and Grand Total Labels

This request subtotals the numeric columns in the report and right-justifies the output,
including the text of the label that precedes the values for the subtotals. Since numeric output
is right-justified by default, in this example the justification specifications in the StyleSheet are
used to reposition the labels. The default label for the automatically generated grand total is
also right-justified.

TABLE FILE EMPLOYEE
SUM DED_AMT BY DED_CODE BY DEPARTMENT
BY BANK_ACCT
WHERE DED_CODE EQ 'CITY'
WHERE BANK_ACCT NE 0
ON DEPARTMENT SUBTOTAL AS 'Total City Deduction for'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
TYPE=SUBTOTAL, STYLE=BOLD, JUSTIFY=RIGHT,$
TYPE=GRANDTOTAL, STYLE=BOLD, JUSTIFY=RIGHT,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1631

Justifying a Heading, Footing, Title, or Label

The output is:

1632

22. Using Headings, Footings, Titles, and Labels

Choosing an Alignment Method for Heading and Footing Elements

To align text and data in headings and footings based on factors other than left/right/center
justification, consider the following descriptions before deciding which alignment method best
suits your needs.

Applies
to ...

HTML

XLSX

EXL2K

PDF

PPTX

DHTML

Alignment Method

1) StyleSheet
Attributes:

HEADALIGN

COLSPAN

JUSTIFY

Details: See Aligning
a Heading or Footing
Element in an HTML,
XLSX, EXL2K, PDF,
PPTX, or DHTML
Report on page
1635.

When to use...

Related
Methods

To align heading or footing items in
HTML and EXL2K reports: If you
expect to display reports in HTML or
EXL2K format, use HEADALIGN
options to align heading and footing
items with either columns in the HTML
table for the body of the report or with
cells in an embedded HTML table. The
browser handles alignment based on
your specifications, without requiring
unit measurements, which are
required with WIDTH and JUSTIFY.

To align heading or footing items in
PDF reports: If you expect to display
reports in PDF format, use the
HEADALIGN=BODY option to align
heading and footing items with
columns in the report body.

To specify a heading or footing item
that spans multiple columns: You can
combine HEADALIGN syntax with the
COLSPAN attribute to achieve this
result. For details, see Aligning a
Heading or Footing Element Across
Columns in an HTML or PDF Report on
page 1653.

Creating Reports With TIBCO® WebFOCUS Language

 1633


Choosing an Alignment Method for Heading and Footing Elements

Applies
to ...

HTML

PDF

PS

Alignment Method

2) StyleSheet
Attributes:

WIDTH

JUSTIFY

Details: See Aligning
Content in a Multi-
Line Heading or
Footing on page
1659.

Related
Methods

For an
HTML, PDF,
or EXL2K
report, you
can align
specific
items with
HEADALIGN
options.

When to use...

For portability between HTML and
PDF: To code a request that can be
used without revision to produce
identical output in HTML (with internal
cascading style sheets) and in PDF,
use WIDTH and JUSTIFY attributes in
your StyleSheet. These settings can
be applied to report, page, and sort
headings and footings.

To align heading or footing items:
Used together, WIDTH and JUSTIFY
allow you to align specific items in the
heading, rather than entire headings
or footings or entire heading or footing
lines, where the implied justification
width is the total width of the report
panel. To right- or center-justify an
item in a heading or footing, you must
know the width of the area you want to
justify it in. That information is
provided by the WIDTH attribute.

To align decimal points in a multi-line
heading or footing: Use this technique
to align decimal points in data that
has varying numbers of decimal
places. You define the width of the
decimal item, then you measure how
far in from the right side of a column
you want to position the decimal point.
This places the decimal point in the
same position in a column, regardless
of the number of decimal places
displayed to its right.

1634

Applies
to ...

PDF

PS

HTML
(limited)

Alignment Method

3) StyleSheet
Attribute:

POSITION

Details: See
Positioning Headings,
Footings, or Items
Within Them on page
1671 and Laying Out
the Report Page on
page 1331.

22. Using Headings, Footings, Titles, and Labels

When to use...

To set starting positions for headings
or footings, or items within them: Use
POSITION syntax to specify absolute
and relative starting positions.

In HTML, with an internal cascading
style sheet, you can use POSITION to
specify the starting point for a heading
or footing line. You can also position
an image in a heading or footing.

To align heading and footing items
with columns: Use POSITION syntax to
align a heading item with a column
position. For example, the syntax

TYPE=SUBHEAD, LINE=1,
ITEM=3,POSITION=SALES, $

places ITEM 3 of the sort heading at
the horizontal position where the
column SALES is.

Related
Methods

For a PDF
report, you
can
accomplish
most
positioning
with WIDTH
and JUSTIFY.

For an HTML
or PDF
report, you
can align a
heading item
with a
column by
setting the
HEADALIGN
attribute to
BODY.

Aligning a Heading or Footing Element in an HTML, XLSX, EXL2K, PDF, PPTX, or DHTML
Report

For HTML output (and for Excel 2000 output, which uses HTML alignment), you can position
text and field items in headings and footings using HEADALIGN options. These options work
within the limitations of HTML and browser technologies to provide a significant degree of
formatting flexibility. Here is how HEADALIGN works.

For PDF output, you can use the HEADALIGN=BODY option to align heading and footing
elements with the report body.

Creating Reports With TIBCO® WebFOCUS Language

 1635

Aligning a Heading or Footing Element in an HTML, XLSX, EXL2K, PDF, PPTX, or DHTML Report

For HTML or Excel 2000 output, when HEADALIGN is set either to BODY or INTERNAL, output is
laid out as an HTML table, which means that the browser determines the widths of the
columns, thereby limiting the precise positioning of items. A basic rule governs the placement
of heading or footing items: each item (text or embedded field) is placed in sequence into the
next HTML table cell (<TD>). When HEADALIGN is set to NONE, the default, all the items in the
heading or footing are strung together, inside a single cell. The browser stretches the heading
table and the report table to accommodate the length of the text.

You can exercise control over the placement of items by overriding the default and choosing
either BODY or INTERNAL:

HEADALIGN=BODY puts heading item cells in the same HTML table (for HTML or EXL2K
output) as the body of the report, ensuring that the items in the heading and the data in the
body of the report line up naturally since they have the same column widths. For PDF
output, HEADALIGN=BODY aligns heading items with data columns. This is a simple and
useful way to align heading items with columns of data. For example, suppose that you
have computed subtotal values that you want to include in a sort footing. Using
HEADALIGN=BODY, you can align the subtotals in the same columns as the data that is
being totaled.

HEADALIGN=INTERNAL puts the heading items in an HTML table of its own. This allows the
heading items to be aligned vertically with each other, independent of the data, since the
widths of the heading items do not affect the width of the report columns and vice versa.

In EXL2K formatted reports, with headings or footings containing multiple items that are
separated by spot markers without spaces, the spot marker adds an additional space
between the items within the text in the cell. The workaround is to use XLSX formatted
reports, instead.

To compare sample output, see Comparing Output Generated With HEADALIGN Options on page
1641.

To break a text string into multiple parts for manipulation across columns, you can use <+0>
spot markers in the request. For details, see Identifying a Report Component in a WebFOCUS
StyleSheet on page 1249.

You can use HEADALIGN options in conjunction with the COLSPAN attribute. COLSPAN allows
heading items to span multiple table columns, thereby providing additional flexibility in how you
can design your headings. For details, see Aligning a Heading or Footing Element Across
Columns in an HTML or PDF Report on page 1653.

If there is more than one heading or footing type in a report, you can individually align any
element within each of them using this syntax.

1636

22. Using Headings, Footings, Titles, and Labels

Tip: For a summary of other alignment methods, see Choosing an Alignment Method for
Heading and Footing Elements on page 1633.

Syntax:

How to Align a Heading or Footing Element in an HTML or PDF Report

TYPE = {REPORT|headfoot}, HEADALIGN = option, $

where:

REPORT

Applies the chosen alignment to all heading and footing elements in a report.

headfoot

Is the type of heading or footing. Valid values are TABHEADING, TABFOOTING,
HEADING, FOOTING, SUBHEAD, and SUBFOOT.

option

Is the type of alignment. Valid values are:

NONE which places heading items in HTML reports in an embedded HTML table inside the
main (body) table, and strings together, in a single cell of the embedded table, all the
heading items (text and fields) on a line. In PDF reports, this uses the default alignment
heading alignment. NONE is the default value.

INTERNAL which places heading items in an HTML table of its own, with each item in a
separate cell. This allows the heading items to be aligned vertically with each other,
independent of the data columns. The widths of the heading items do not affect the widths
of the report columns and vice versa.

Note: HEADALIGN=INTERNAL is not supported in PDF reports.

BODY which aligns heading items with data columns. For HTML output, this places the
items in the cells of the same HTML table as the body of the report. Since they have the
same column widths, the items in the heading and the data in the body of the report line
up naturally. For PDF output, this aligns the heading or footing elements with the data
columns.

Note: HEADALIGN=BODY does not support paneling.

You can combine HEADALIGN options with the COLSPAN attribute to allow heading items to
span multiple HTML table columns. For details, see How to Align a Heading or Footing Element
in an HTML or PDF Report on page 1637.

Creating Reports With TIBCO® WebFOCUS Language

 1637

Aligning a Heading or Footing Element in an HTML, XLSX, EXL2K, PDF, PPTX, or DHTML Report

Example:

Aligning Subfooting Items With Report Columns in PDF Report Output

In the following request against the GGORDER data source, the subfooting has a text object
("Total") and a field object (ST.QUANTITY). The subfooting aligns the items with their report
columns using TYPE=SUBFOOT, HEADALIGN=BODY ,$. The text object is placed in the second
report column using the <+0 spot marker, and the field object is placed in the third report
column using another <+0 spot marker. Then the text item is left aligned (the default) with its
report column. The field object is right aligned with its report column.

TABLE FILE GGORDER
PRINT QUANTITY
ORDER_NUMBER ORDER_DATE STORE_CODE
BY PRODUCT_CODE BY PRODUCT_DESCRIPTION
WHERE ORDER_DATE EQ '01/01/96'
WHERE STORE_CODE EQ 'R1019'
ON PRODUCT_CODE SUBFOOT
" <+0 Total: <+0 <ST.QUANTITY"
ON TABLE SET PAGE-NUM OFF
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLESHEET *
TYPE = SUBFOOT,HEADALIGN=BODY, $
TYPE = SUBFOOT,OBJECT=TEXT,STYLE = BOLD, $
TYPE = SUBFOOT,OBJECT=FIELD,JUSTIFY=RIGHT,STYLE = BOLD, $
ENDSTYLE
END

1638

22. Using Headings, Footings, Titles, and Labels

The output shows that the text Total is aligned with the product names and the subtotal field
object is right aligned with the Ordered Units column.

Example:

Using OVER With HEADALIGN=BODY in a PDF Report

When aligning heading elements with the data line using HEADALIGN=BODY, the first row of
fields serves as the anchor data row. Each heading line contains the number of columns
presented in the anchor data row. Any additional columns that may appear on other data lines
are not presented. If the first row of data contains fewer data value cells than other data rows,
you will be unable to add alignment columns within headings for these additional columns.

Creating Reports With TIBCO® WebFOCUS Language

 1639

Aligning a Heading or Footing Element in an HTML, XLSX, EXL2K, PDF, PPTX, or DHTML Report

In the following example, the first row (the anchor data row) contains a single value. Items
placed in headings to correspond with column two that appears on subsequent rows are not
displayed.

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
TYPE=REPORT, SQUEEZE=ON,FONT=ARIAL, SIZE=8, LEFTGAP=.1, RIGHTGAP=.1,
GAPINTERNAL=ON, LEFTMARGIN=1,$
TYPE=REPORT, BORDER=ON, $
TYPE=HEADING, BORDERALL=ON, HEADALIGN=BODY, $
TYPE=HEADING, LINE=1, ITEM=1, COLSPAN=2, WIDTH=2, JUSTIFY=LEFT, $
TYPE=HEADING, LINE=2, ITEM=1, WIDTH=1, JUSTIFY=LEFT, $
TYPE=HEADING, LINE=2, ITEM=2, WIDTH=1, JUSTIFY=LEFT, $
TYPE=REPORT, COLUMN=PRODUCT(2),   SQUEEZE=2,  $
TYPE=REPORT, COLUMN=UNITS, SQUEEZE=1, $
TYPE=REPORT, COLUMN=DOLLARS, SQUEEZE=1, $
END

1640

22. Using Headings, Footings, Titles, and Labels

The output shows that the heading lines have one column each, while the data lines alternate
between one column and two columns.

Example:

Comparing Output Generated With HEADALIGN Options

The requests that follow illustrate the differences in alignment with each HEADALIGN setting.
The grid lines are exposed in the output to help distinguish the HTML table created for the
body of the report from the embedded HTML tables created for the heading in some variations.

Creating Reports With TIBCO® WebFOCUS Language

 1641

Aligning a Heading or Footing Element in an HTML, XLSX, EXL2K, PDF, PPTX, or DHTML Report

All HEADALIGN settings are compatible with COLSPAN syntax, which allows heading items to
span multiple columns.

TABLE FILE CAR
SUM SALES BY COUNTRY BY CAR BY MODEL
ON COUNTRY SUBHEAD
"This is my subhead"
" "
"Country is:<COUNTRY Car is:<CAR"
"Model is:<MODEL"
IF COUNTRY EQ 'ENGLAND'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLESHEET *
TYPE=SUBHEAD, HEADALIGN=OPTION, $
TYPE=SUBHEAD, LINE=1, ITEM=1, COLSPAN=4, JUSTIFY=CENTER, $
ENDSTYLE
END

HEADALIGN=NONE without the second TYPE=SUBHEAD declaration highlighted in the request
syntax creates a separate table with default left alignment. The text and fields in each heading
line are strung together in a single HTML table cell.

TYPE=SUBHEAD, HEADALIGN=NONE, $

1642

22. Using Headings, Footings, Titles, and Labels

HEADALIGN=NONE with COLSPAN

TYPE=SUBHEAD, HEADALIGN=NONE, $
TYPE=SUBHEAD, LINE=1, ITEM=1, COLSPAN=4, JUSTIFY=CENTER, $

The first line is centered across all four columns of the internal table, based on the
COLSPAN=4 setting.

HEADALIGN=INTERNAL creates a separate HTML table. Columns are generated based on the
number of items (text and fields) in the heading. Each item is placed in a separate cell. These
columns do not correspond to those in the HTML table for the body of the report.

TYPE=SUBHEAD, HEADALIGN=INTERNAL, $

Creating Reports With TIBCO® WebFOCUS Language

 1643

Aligning a Heading or Footing Element in an HTML, XLSX, EXL2K, PDF, PPTX, or DHTML Report

Country is aligned with Model in the first column of the internal table. The value of <COUNTRY
is aligned with the value of <MODEL in the second column.

HEADALIGN=INTERNAL with COLSPAN

TYPE=SUBHEAD, HEADALIGN=INTERNAL, $
TYPE=SUBHEAD, LINE=1, ITEM=1, COLSPAN=4, JUSTIFY=CENTER, $

The first line is centered across all 4 columns of the internal table, based on the COLSPAN=4
setting.

1644

22. Using Headings, Footings, Titles, and Labels

HEADALIGN=BODY places the heading lines within the cells of the main HTML table. As a
result, the columns of the heading correspond to the columns of the main table.

TYPE=SUBHEAD, HEADALIGN=BODY, $

Country is aligned with Model in the first column of the main (body) HTML table. The value of
<COUNTRY is aligned with the value of <MODEL in the second column.

Creating Reports With TIBCO® WebFOCUS Language

 1645

Aligning a Heading or Footing Element in an HTML, XLSX, EXL2K, PDF, PPTX, or DHTML Report

HEADALIGN=BODY with COLSPAN

TYPE=SUBHEAD, HEADALIGN=BODY, $
TYPE=SUBHEAD, LINE=1, ITEM=1, COLSPAN=4, JUSTIFY=CENTER, $

COLSPAN controls the cross-column alignment of the first row of the heading.

Example:

Aligning Elements in a Sort Footing With Data Columns

This request creates an HTML report using HEADALIGN = BODY to align the two elements of
the sort footing (TOTAL IS and the value) with each of the two data columns (Product and
Ordered Units). JUSTIFY = RIGHT, which applies to the entire sort footing, right justifies each
sort footing element under the data column.

TABLE FILE GGORDER
PRINT QUANTITY
BY PRODUCT_CODE NOPRINT BY PRODUCT_DESCRIPTION
WHERE ORDER_DATE EQ '01/01/96'
WHERE STORE_CODE EQ 'R1019'
ON PRODUCT_CODE SUBFOOT
"TOTAL IS: <ST.QUANTITY"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID = OFF, $
TYPE = SUBFOOT, HEADALIGN = BODY, JUSTIFY = RIGHT, $
TYPE = SUBFOOT, OBJECT = FIELD, STYLE = BOLD, $
ENDSTYLE
END

1646

22. Using Headings, Footings, Titles, and Labels

The partial output is:

Creating Reports With TIBCO® WebFOCUS Language

 1647

Aligning a Heading or Footing Element in an HTML, XLSX, EXL2K, PDF, PPTX, or DHTML Report

Example:

Aligning Elements in a Page Heading Using a Separate HTML Table

This request creates an embedded HTML table for a page heading, within the HTML table that
governs alignment in the body of the report. This table has three rows and three columns to
accommodate all the heading elements.

In the first line of the heading, a spot marker (<+0>) creates two text elements: the first
element is blank, and the second element is Gotham Grinds, Inc. In the output, the second
element appears in the second cell of the first row of the embedded table. For related
information, see Identifying a Report Component in a WebFOCUS StyleSheet on page 1249.

The second and fourth lines of the heading are blank.

The spot markers in the third line of the heading split it into three text elements: Orders
Report, blank, Run on: &DATE. In the output, each element appears in a cell in the third row of
the embedded HTML table, in the order specified in the request.

TABLE FILE GGORDER
HEADING
" <+0>Gotham Grinds, Inc."
" "
"Orders Report <+0> <+0> Run on: &DATE"
" "
PRINT ORDER_NUMBER ORDER_DATE STORE_CODE QUANTITY
BY PRODUCT_CODE BY PRODUCT_DESCRIPTION
IF RECORDLIMIT EQ 10
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID = ON, $
TYPE = HEADING, HEADALIGN = INTERNAL, STYLE = BOLD, $
ENDSTYLE
END

GRID=ON in the request enables you to see the embedded HTML table for the heading, and
the main HTML table for the body of the report.

1648

22. Using Headings, Footings, Titles, and Labels

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1649

Aligning a Heading or Footing Element in an HTML, XLSX, EXL2K, PDF, PPTX, or DHTML Report

Notice that the positioning is maintained when the grid is hidden (off).

1650

22. Using Headings, Footings, Titles, and Labels

Example:

Aligning a Text Field With a Column in a Sort Footing

This example uses a Master File and the MODIFY procedure created in the example named
Including a Text Field in a Sort Footing on page 1566. Rerun that example and return here to
align the text field.

The request uses HEADALIGN=BODY to align the text field lines in a sort footing. With this
setting, each element in the footing is aligned with a column in the main HTML table generated
for the report: the first element (the text Course Description:) is aligned with the first data
column, CATALOG. The embedded field is aligned in a second column. The grid is turned on in
this example to make the alignment easier to see.

TABLE FILE TXTFLD
BY CATALOG SUBFOOT
"Course Description: <TEXTFLD"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID = ON, $
TYPE = SUBFOOT, HEADALIGN = BODY, $
ENDSTYLE
END

The output displays a new value for the text field each time the value of CATALOG changes.

Creating Reports With TIBCO® WebFOCUS Language

 1651

Aligning a Heading or Footing Element in an HTML, XLSX, EXL2K, PDF, PPTX, or DHTML Report

Example:

Aligning and Styling a Text Field in a Sort Footing

This example uses a Master File and the MODIFY procedure created in the example named
Including a Text Field in a Sort Footing on page 1566. Rerun that example and return here to
align the text field. This request applies boldface type to the second line of a multiple-line sort
footing, which includes the text Course Description as well as the text of the field TEXTFLD.
Line 1 of the sort footing is the text Evening Course.

TABLE FILE TXTFLD
BY DESCRIPTION AS 'CATALOG' SUBFOOT
"Evening Course"
"Course Description: <TEXTFLD"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID = OFF, $
TYPE = SUBFOOT, HEADALIGN = BODY, $
TYPE = SUBFOOT, LINE = 2, STYLE = BOLD, $
ENDSTYLE
END

The output is:

If the StyleSheet instead identifies the text field as an object for styling

TYPE = SUBFOOT, HEADALIGN = BODY, $
TYPE = SUBFOOT, LINE = 2, OBJECT = FIELD, STYLE = BOLD, $

1652

22. Using Headings, Footings, Titles, and Labels

then only the text in TEXTFLD is bold.

Aligning a Heading or Footing Element Across Columns in an HTML or PDF Report

With HEADALIGN=BODY, each heading or footing element is aligned with a data column in an
HTML or PDF report. With HEADALIGN=INTERNAL, each element is continued in a column of an
HTML table created and aligned specifically for the report heading or footing. By default, every
heading or footing element (ITEM) is placed in the first available column. However, you can
position an item to span multiple columns using the COLSPAN attribute. For details about
HEADALIGN options, see Aligning a Heading or Footing Element in an HTML, XLSX, EXL2K, PDF,
PPTX, or DHTML Report on page 1635.

You must specify the HEADALIGN and COLSPAN attributes in two separate StyleSheet
declarations, since HEADALIGN applies to an entire heading or footing, while COLSPAN applies
to a specific item in a heading or footing.

Syntax:

How to Align a Heading or Footing Element Across Columns in an HTML or PDF Report

TYPE = headfoot, [subtype,] COLSPAN = n, $

where:

headfoot

Is the type of heading or footing. Valid values are TABHEADING, TABFOOTING, HEADING,
FOOTING, SUBHEAD, and SUBFOOT.

Creating Reports With TIBCO® WebFOCUS Language

 1653

Aligning a Heading or Footing Element Across Columns in an HTML or PDF Report

subtype

Are additional attributes that identify the report component. These options can be used
separately or in combination, depending upon the degree of specificity required to identify
an element. Valid values are:

LINE, which identifies a line by its position in a heading or footing. Identifying individual
lines enables you to format each line differently.

If a heading or footing has multiple lines and you apply a StyleSheet declaration that
does not specify LINE, the declaration is applied to all lines. Blank lines are counted
when interpreting the value of LINE.

OBJECT, which identifies an element in a heading or footing as a text string or field
value. Valid values are TEXT or FIELD. TEXT may represent free text or a Dialogue
Manager amper (&) variable.

It is not necessary to specify OBJECT=TEXT unless you are styling both text strings and
embedded fields in the same heading or footing.

ITEM, which identifies an item by its position in a line. To divide a heading or footing
line into items, you can use the <+0> spot marker. For more information, see
Identifying a Report Component in a WebFOCUS StyleSheet on page 1249.

To determine the ITEM for an OBJECT, follow these guidelines:

When used with OBJECT=TEXT, count only the text strings from left to right.

When used with OBJECT=FIELD, count only values from left to right.

When used without OBJECT, count text strings and field values from left to right.

If you apply a StyleSheet declaration that specifies ITEM, the number is counted from the
beginning of each line in the heading or footing, not just from the beginning of the first line.

COLSPAN

Is an attribute that aligns an item in the width spanned by multiple columns.

n

Is the column with which the specified item is aligned.

1654

22. Using Headings, Footings, Titles, and Labels

Example:

Centering a Page Heading Across Three Columns

In this request, HEADALIGN=INTERNAL creates a three-column embedded HTML table for the
heading. The COLSPAN attribute then centers the first line of the heading, Gotham Grinds, Inc.,
over the report, spanning the three columns in the embedded HTML table.

TABLE FILE GGORDER
HEADING
"Gotham Grinds, Inc."
" "
"Orders Report <+0> <+0> Run on: &DATE"
" "
PRINT ORDER_NUMBER ORDER_DATE STORE_CODE QUANTITY
BY PRODUCT_CODE BY PRODUCT_DESCRIPTION
IF RECORDLIMIT EQ 10
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID = OFF, $
TYPE = HEADING, HEADALIGN = INTERNAL, $
TYPE = HEADING, LINE=1, COLSPAN=3, STYLE = BOLD, JUSTIFY=CENTER, $
TYPE = HEADING, LINE=3, ITEM=3, JUSTIFY=RIGHT, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1655

Aligning a Heading or Footing Element Across Columns in an HTML or PDF Report

The output is:

1656

22. Using Headings, Footings, Titles, and Labels

Example:

Aligning a Field Value Across Multiple Columns

In this request, HEADALIGN=BODY aligns the sort footing in the same HTML table as the body
of the report. COLSPAN = 5 positions the first item in the sort footing (the text Total) in the
fifth column of the HTML table. The second item in the sort footing (the field <ST.QUANTITY) is
positioned in the next available column.

The HEADALIGN attribute is on a separate line from the COLSPAN attribute because it applies
to the entire sort footing (and consequently to both items), whereas COLSPAN applies to the
single item Total.

TABLE FILE GGORDER
PRINT ORDER_NUMBER ORDER_DATE STORE_CODE QUANTITY
BY PRODUCT_CODE BY PRODUCT_DESCRIPTION
WHERE ORDER_DATE EQ '01/01/96'
WHERE STORE_CODE EQ 'R1019'
ON PRODUCT_CODE SUBFOOT
"Total: <ST.QUANTITY"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID = OFF, $
TYPE = SUBFOOT, HEADALIGN = BODY, JUSTIFY = RIGHT, STYLE = BOLD, $
TYPE = SUBFOOT, OBJECT = TEXT, COLSPAN = 5, $
ENDSTYLE
END

The partial output is:

Creating Reports With TIBCO® WebFOCUS Language

 1657

Aligning a Heading or Footing Element Across Columns in an HTML or PDF Report

Example:

Aligning a Field Value Across Multiple Columns in a PDF Report

In this request, HEADALIGN=BODY aligns the sort footing in the same grid as the body of the
report. COLSPAN=5 positions the first item in the sort footing (the text Total) in the fifth
column of the report output. The second item in the sort footing (the field <ST.QUANTITY) is
positioned in the next available column. The subfooting items are right justified.

The HEADALIGN attribute is on a separate line from the COLSPAN attribute because it applies
to the entire sort footing (and consequently to both items), whereas COLSPAN applies only to
the text item Total.

TABLE FILE GGORDER
PRINT ORDER_NUMBER ORDER_DATE STORE_CODE QUANTITY
BY PRODUCT_CODE BY PRODUCT_DESCRIPTION
WHERE ORDER_DATE EQ '01/01/96'
WHERE STORE_CODE EQ 'R1019'
ON PRODUCT_CODE SUBFOOT
"Total:<ST.QUANTITY"
""
ON TABLE SET PAGE-NUM OFF
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLESHEET *
TYPE=REPORT, FONT=ARIAL, SQUEEZE=ON,$
TYPE = SUBFOOT, HEADALIGN = BODY, JUSTIFY = RIGHT, STYLE = BOLD, $
TYPE = SUBFOOT, ITEM=1, COLSPAN = 5, $
ENDSTYLE
END

1658

22. Using Headings, Footings, Titles, and Labels

The output shows that the first item in the sort footing (the text Total) is in the fifth column of
the report output. The second item in the sort footing (the field <ST.QUANTITY) is positioned in
the next available column.

Aligning Content in a Multi-Line Heading or Footing

The HEADALIGN and COLSPAN syntax described in Aligning a Heading or Footing Element in an
HTML, XLSX, EXL2K, PDF, PPTX, or DHTML Report on page 1635 is specific to HTML reports.
This topic describes how you can design reports that are printable across HTML and PDF
formats. Using the WIDTH and JUSTIFY syntax in a StyleSheet, you can:

Align vertical sets of text or data as columnar units.

Combine columnar formatting with line-by-line formatting.

Align decimal points when the data displayed has varying numbers of decimal places. See
Aligning Decimals in a Multi-Line Heading or Footing on page 1664.

You can apply WIDTH and JUSTIFY attributes to report headings and footings, page headings
and footings, and sort headings and footings, using either mono-space or proportional fonts.

Creating Reports With TIBCO® WebFOCUS Language

 1659

Aligning Content in a Multi-Line Heading or Footing

These techniques rely on internal cascading style sheets, which support WebFOCUS
StyleSheet attributes that were not previously available for HTML reports. The syntax
associated with these techniques resolves the problem of having to format headings differently
for HTML reports (using HEADALIGN and COLSPAN) and PDF and PS reports (using POSITION
and spot markers).

While the WIDTH and JUSTIFY attributes are particularly useful when you need to format a
multi-line heading or footing, or align stacked decimals, you can also use this syntax to
position items in an individual heading or footing line.

Tip: For a summary of other alignment methods, see Choosing an Alignment Method for
Heading and Footing Elements on page 1633.

Syntax:

How to Align Heading Text and Data in Columns

For a multi-line report or page heading or footing, use the syntax:

TYPE=headfoot, WRAP=OFF, $
TYPE=headfoot, [LINE=line_#,] ITEM=item_#, [OBJECT={TEXT|FIELD}],
 WIDTH=width,   [JUSTIFY=option,] $

For a multi-line sort heading or footing, use the syntax:

TYPE=headfoot, WRAP=OFF, $
TYPE={SUBHEAD|SUBFOOT}, [BY=sortfield] [LINE=line_#,] ITEM=item_#,
 [OBJECT={TEXT|FIELD}], WIDTH=width, [JUSTIFY=option,] $

where:

headfoot

Is the type of heading or footing. Valid values are TABHEADING, TABFOOTING,
HEADING, FOOTING, SUBHEAD, and SUBFOOT.

sortfield

When TYPE=SUBHEAD or SUBFOOT, you can specify alignment for the sort heading or
sort footing associated with a particular sort field. If no sort field is specified,
formatting is applied to the sort headings or footings associated with all sort fields.

LINE

Is an optional entry that identifies a line by its position in a heading or footing.
Identifying individual lines enables you to format each one differently.

If a heading or footing has multiple lines and you apply a StyleSheet declaration that does
not specify LINE, the declaration is applied to all lines. Blank lines are counted when
interpreting the value of LINE.

You can use LINE in combination with ITEM.

1660

22. Using Headings, Footings, Titles, and Labels

ITEM

Is a required entry when you are using WIDTH to control alignment. An item can
identify either:

A vertical set of text or data that you wish to align as a columnar unit. You must identify
each vertical unit as an item.

An item's position in a line. You must identify each line element as an item. See Line
and Item Formatting in a Multi-Line Heading or Footing on page 1662 for information
about acceptable variations.

You can use either or both approaches for a single heading or footing.

To divide a heading or footing line into items, you can use the <+0> spot marker. See,
Identifying a Report Component in a WebFOCUS StyleSheet on page 1249. The number of
items you can identify is limited by the cumulative widths of the items in the heading or
footing, within the physical boundaries of the report page.

You can use ITEM in conjunction with OBJECT to refine the identification of an element
whose width you want to define. To determine the ITEM for an OBJECT, follow these
guidelines:

When used with OBJECT=TEXT, count only the text strings from left to right.

When used with OBJECT=FIELD, count only values from left to right.

When used without OBJECT, count text strings and field values from left to right.

If you apply a StyleSheet declaration that specifies ITEM, the number is counted from the
beginning of each line in the heading or footing, not just from the beginning of the first line.

OBJECT

Is an optional entry that identifies an element in a heading or footing as a text string
or field value. Valid values are TEXT or FIELD. TEXT may represent free text or a
Dialogue Manager amper (&) variable.

It is not necessary to specify OBJECT=TEXT unless you are styling both text strings and
embedded fields in the same heading or footing.

width

Is the measurement expressed in units (inches by default), which is required to
accommodate the longest text string or field value associated with a numbered item.
For details, see How to Measure for Column Width on page 1665.

option

Is the type of justification. Valid values are:

Creating Reports With TIBCO® WebFOCUS Language

 1661

Aligning Content in a Multi-Line Heading or Footing

LEFT which left justifies the heading or footing. LEFT is the default value.

RIGHT which right justifies the heading or footing.

CENTER which centers the heading or footing.

DECIMAL (n)

Is the measurement expressed in units (inches by default), which specifies how far in
from the right side of a column to place the decimal point. With this specification, you
can locate the decimal point in the same position within a column, regardless of the
number of decimal places displayed to its right.

The measurement will be a portion of the width specified for this item. For details, see
How to Measure for Column Width on page 1665.

Note: JUSTIFY is not supported with WRAP.

Reference: Line and Item Formatting in a Multi-Line Heading or Footing

Line formatting maximizes your control over the items you identify on each line:

You can align and stack the same number of items with uniform widths. For example,

Line 1

Line 2

Item 1

Item 1

Item 2

Item 2

Item 3

Item 3

You can also align different numbers of items as long as the items on each line have the
same starting point and the same cumulative width.

Line 1

Line 2

Do not use HEADALIGN or COLSPAN syntax, which are specific to HTML reports and may
conflict with WIDTH and JUSTIFY settings.

For HTML reports, turn WRAP OFF (ON is the default) to ensure proper processing of WIDTH
and JUSTIFY.

Example:

Aligning Data and Text in a Multi-Line Heading or Footing

In the following free-form report, content is defined entirely in the sort heading, where text and
data are stacked to support comparison among countries. Each set of data is aligned
vertically, to appear as a column. To achieve this affect, each vertical unit is identified as an
item: the first column of text is item 1, the next column of data is item 2, and so on.

1662

22. Using Headings, Footings, Titles, and Labels

Note especially the last column, in which decimal data with different numbers of decimal
places is lined up on the decimal point to facilitate reading and comparison.

The chart below breaks out the structure of the previous report:

Item1:

Item 2:

Text

Data values

Item 3:

Text

Item 4:

Values with decimal places

Country

ARGENTINA
BRAZIL, and so on

Exchange Rate

nn.dd

Type

ST.NOTES

Projected Return

n.ddd

Holder

COMM

Balance

nn,nnn,nnn.dd

Creating Reports With TIBCO® WebFOCUS Language

 1663

Aligning Content in a Multi-Line Heading or Footing

For each item, you specify the width of the column and the justification of its content, as
illustrated in the following code.

DEFINE FILE SHORT
BALANCE/D14.2=BALANCE;
END
TABLE FILE SHORT
BY COUNTRY NOPRINT SUBHEAD
"Country:<COUNTRY Exchange Rate:<EXCHANGE_RATE"
"Type:<TYPE Projected Return:<PROJECTED_RETURN"
"Holder:<HOLDER Balance:<BALANCE"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLESHEET *
TYPE=REPORT, FONT='TIMES', $
TYPE=REPORT, GRID=OFF, $
TYPE=SUBHEAD, ITEM=1, WIDTH=1.00, JUSTIFY=RIGHT, $
TYPE=SUBHEAD, ITEM=2, WIDTH=1.25, JUSTIFY=RIGHT, $
TYPE=SUBHEAD, ITEM=3, WIDTH=1.25, JUSTIFY=RIGHT,$
TYPE=SUBHEAD, ITEM=4, WIDTH=1.5,  JUSTIFY=DECIMAL(.6),$
ENDSTYLE
END

This procedure produces a three-line sort heading, broken out as four items, each with a
measured width and defined justification. The decimal item (4) uses a variation on standard
justification to line up the decimal points. For details, see How to Align Heading Text and Data
in Columns on page 1660 and Aligning Decimals in a Multi-Line Heading or Footing on page
1664.

Note: To take advantage of this feature for an HTML report, you must turn on internal
cascading style sheets (SET HTMLCSS=ON). This command enables WebFOCUS StyleSheet
attributes that were not previously available for HTML reports. This line of code is ignored for a
PDF report.

Aligning Decimals in a Multi-Line Heading or Footing

The ability to align heading content in a multi-line heading based on width and justification
values has special benefit in reports that contain data with different numbers of decimal
places. For example, if a figure is in dollars, it is formatted with a decimal point and two places
for zeroes. If in Swiss francs, it is formatted with a decimal place and four zeroes. If in yen, the
decimal is at the end with no zeroes. In addition, sometimes the currency or units do not vary,
but the number of digits of decimal precision varies.

1664

22. Using Headings, Footings, Titles, and Labels

By aligning the decimal points in a vertical stack, you can more easily read and compare these
numbers, as illustrated in the following output:

Floating decimal points

Aligned decimal points

Bond
------------

Galosh Ltd.

Mukluk Inc.

 Face Value
------------

Bond
------------

    Face Value
-------------

22375.5784596

Galosh Ltd.

  22375.5784596

 1212345.457

Mukluk Inc.

1212345.457

Overshoe Inc.

232.45484

Overshoe Inc.

    232.45484

The technique uses a width specification for the item that contains decimals, combined with a
variation on standard left/right/center justification to achieve the proper decimal alignment.
For the syntax that generates this output, see How to Align Heading Text and Data in Columns
on page 1660.

Procedure: How to Measure for Column Width

Determining the width of a heading or footing item is a three-step process:

1.

2.

Identify the maximum number of characters in a text string or field.

For a text string, simply count the characters. For a field, refer to the format specification
in the Master File or in a command such as a DEFINE.

3. Measure the physical space in units (for example, in inches) that is required to display the
number of characters identified in step 1, based on the size of the font you are using. For
example, the following value of the COUNTRY field would measure as follows:

Font

Helvetica

Times New Roman

Courier

Font size

Comparison

Inches

10

10

10

England

England

England

.5

.44

.56

Tip: Consider using a consistent set of fonts in your reports to make your measurements
reusable.

Creating Reports With TIBCO® WebFOCUS Language

 1665

Aligning Content in a Multi-Line Heading or Footing

Procedure: How to Measure for Decimal Alignment

After you have determined the width of an item, you can do a related measurement to
determine the physical space required to display decimal data with a varying number of digits
to the right of the decimal point.

1. Determine the maximum number of decimal places you need to accommodate to the right

of the decimal place, plus the decimal point itself.

2. Measure the physical space in units (for example, in inches) that is required to display the
number of characters identified in step 1, based on the size of the font you are using.

Combining Column and Line Formatting in Headings and Footings

By combining column and line formatting, you can create complex reports in which different
ranges of lines in the same heading or footing have different numbers of aligned columns in
different locations.

Example:

Combining Column and Line Formatting to Align Items in a Sort Heading

This request produces a free-form report in which content is defined in a seven-line sort
heading. Text and data is stacked in two groupings:

The first grouping identifies the country and region (continent).

The second grouping provides financial information for each country/region pair.

Although this is a single sort heading, our goal is to format the information in each grouping a
bit differently to provide emphasis and facilitate comparison. The request also demonstrates a
coding technique that makes formatting changes easier for the report designer. See the
annotations following the code for details.

As you review the sample request, keep in mind that a heading can contain two kinds of items:
text and embedded fields. A text item consists of any characters, even a single blank, between
embedded fields and/or spot markers. In particular, if you have a single run of text that you
want to treat as two items, you can separate the two items using a <+0> spot marker. For
example, in the heading line:

" <+0>Country:<COUNTRY"

item #1 is a single blank space.

item #2, separated by the <+0> spot marker, is the text Country:

item #3 is the embedded field <COUNTRY.

For details about the <+0> spot marker, see Identifying a Report Component in a WebFOCUS
StyleSheet on page 1249.

1666

22. Using Headings, Footings, Titles, and Labels

Request and annotations:

    DEFINE FILE SHORT
    BALANCE/D14.2=BALANCE;
    END
    TABLE FILE SHORT
    BY COUNTRY NOPRINT SUBHEAD
1.  " <+0>Country:<COUNTRY"
2.  " <+0>Region:<REGION"
    " "
3.  "Type:<TYPE <+0>Exchange Rate:<EXCHANGE_RATE"
4.  "Holder:<HOLDER <+0>Projected Return:<PROJECTED_RETURN"
5.  "Risk class:<RISK_CLASS <+0>Balance:<BALANCE"
    " "
    ON TABLE SET PAGE-NUM OFF
6.  ON TABLE SET HTMLCSS ON
    ON TABLE SET STYLESHEET *
    TYPE=REPORT, FONT='TIMES', $
    TYPE=REPORT, GRID=OFF, $
    -* Bottom section of subhead:
7.  TYPE=SUBHEAD, ITEM=1, WIDTH=1.00, JUSTIFY=RIGHT, $
8.  TYPE=SUBHEAD, ITEM=2, WIDTH=1.25, JUSTIFY=RIGHT, $
9.  TYPE=SUBHEAD, ITEM=3, WIDTH=.5, $
10. TYPE=SUBHEAD, ITEM=4, WIDTH=1.25, JUSTIFY=RIGHT,$
11. TYPE=SUBHEAD, ITEM=5, WIDTH=1.5, JUSTIFY=DECIMAL(.6),$
    -* Top section of subhead (overrides above ITEM defaults
    -*   for lines 1 and 2):
12. -SET &INDENT=1.5;
13. TYPE=SUBHEAD, LINE=1, ITEM=1, WIDTH=&INDENT, $
14. TYPE=SUBHEAD, LINE=1, ITEM=2, WIDTH=1, JUSTIFY=LEFT, $
15. TYPE=SUBHEAD, LINE=1, ITEM=3, SIZE=14, WIDTH=2, JUSTIFY=LEFT, $
16. TYPE=SUBHEAD, LINE=2, ITEM=1, WIDTH=&INDENT, $
17. TYPE=SUBHEAD, LINE=2, ITEM=2, WIDTH=1, JUSTIFY=LEFT, $
18. TYPE=SUBHEAD, LINE=2, ITEM=3, WIDTH=2, JUSTIFY=LEFT, $
    ENDSTYLE
    END

Creating Reports With TIBCO® WebFOCUS Language

 1667

Aligning Content in a Multi-Line Heading or Footing

The output highlights the key information and its relationship by aligning text and data,
including decimal data in which decimal points are aligned for easy comparison.

Line #

Description

1-2

Defines the content for the top, two-line section of the sort heading. Each line
contains three items: the first is a blank area (denoted by a space, separated
from the next item by a <+0> spot marker), the second contains text, the third
contains data values related to the text.

1668

22. Using Headings, Footings, Titles, and Labels

Line #

Description

3-5

6

Defines the content for the bottom, three-line section of the sort heading. Each
line contains five items: text, data values related to the text, a blank column
(denoted by a space, separated from the next item by a null spot marker), text,
data values related to the text.

Turns on internal cascading style sheets, a requirement for these formatting
options. This command enables WebFOCUS StyleSheet attributes that were not
previously available for HTML reports. This line of code is ignored for a PDF
report.

Creating Reports With TIBCO® WebFOCUS Language

 1669

Aligning Content in a Multi-Line Heading or Footing

Line #

Description

7-11

Specifies the basic formatting characteristics for the sort heading by breaking
the content into five columns, each identified as an item with a defined width,
and justification information for all but the empty column.

Important: Had additional formatting code (annotated as 12-17) not been
included in the request, the specifications annotated as 7-11 would have
applied to the entire sort heading (that is, the formatting of the three columns in
the top section of the heading would have been based on the specifications for
the first three columns described below). However, that is not the effect we
want to achieve, so a second section of StyleSheet code is defined to override
this formatting for lines 1 and 2 of the sort heading. See annotations 12-18.

The formatting of the bottom, three-line section of the heading is controlled by
the following specifications:

Item 1 identifies a columnar unit that contains text (that is, Type, Holder, Risk
Class). It has a defined width of 1 inch and the text is right justified.

Item 2 identifies a columnar unit that contains data values related to the text in
item 1. It has a defined width of 1.25 inches and the data is right justified.

Item 3 identifies a columnar unit that contains blank space and serves as a
separator between columns. It has a width of .5 inches. Justification is not
relevant.

Item 4 identifies a columnar unit that contains text (e.g., Exchange Rate,
Projected Return, Balance). It has a defined width of 1.25 inches and the text is
right justified.

Item 5 identifies a columnar unit that contains a decimal value. The width of the
column that contains the value is 1.5 inches, with the decimal point anchored .
6 inches in from the right edge of that column.

The common width and justification definitions enforce the proper alignment of
each item.

1670

22. Using Headings, Footings, Titles, and Labels

Line #

Description

12

Defines a variable called &INDENT, with a width setting of 1.5 inches. This
variable defines the width of the blank area (item 1) at the beginning of lines 1
and 2 of the sort heading.

Defining the width as a variable enables you to experiment with different widths
simply by changing the value in one location. For a complex report, this
technique can potentially save a lot of development time. For details, see the
documentation on Dialogue Manager in the Developing Reporting Applications
manual.

13-18

Specifies line-by-line formatting for the top, two-line section of the sort heading.
This code overrides the previous formatting for lines 1 and 2 of the sort heading
because it specifies a line number.

Item 1 on each line refers to the blank area. The width is defined as a variable
and implemented based on the current value of &INDENT.

Item 2 on each line refers to the text area. It has a defined width of 1 inch and
the text is left justified.

Item 3 on each line refers to the data values. It has a defined width of 2 inches
and the data is left justified.

The common width and justification definitions enforce the proper alignment of
each item.

Notice that item 1 in line 15 defines a font size for the data values associated
with the COUNTRY field. All other items on both lines use a default font. Line-by-
line formatting enables you to define a unique characteristic for a single item.

Positioning Headings, Footings, or Items Within Them

For a PDF, PS, or HTML report, you can use the POSITION attribute in a StyleSheet to specify a
starting position for a heading or footing, expressed as a unit measurement. For HTML, this
capability requires an internal cascading style sheet. For details on selecting an alignment
method, see Choosing an Alignment Method for Heading and Footing Elements on page 1633.

Creating Reports With TIBCO® WebFOCUS Language

 1671

Positioning Headings, Footings, or Items Within Them

In addition, for a PDF or PS report, you can use the POSITION attribute to specify an absolute
or relative starting position for an element within a heading or footing or to align an item in a
heading or footing with a report column. An absolute starting position is the distance from the
left margin of the report. A relative starting position is the distance from the preceding object.
For the first item on a heading line this is the left margin of the report.

In an HTML report, you can use related syntax and an internal cascading style sheet to
position an image in a heading or footing. For details on images, see Laying Out the Report
Page on page 1331.

Syntax:

How to Set a Starting Position for a Heading or Footing

Use the following syntax to specify a starting position for an entire heading or footing in
relation to the left margin of a report.

TYPE = headfoot, POSITION = position, $

where:

headfoot

Is the type of heading or footing. Valid values are TABHEADING, TABFOOTING,
HEADING, FOOTING, SUBHEAD, and SUBFOOT.

position

Is the desired distance from the left, expressed by the UNITS attribute (the default is
INCHES).

Note: In an HTML report, this syntax must be used in conjunction with an internal cascading
style sheet.

Example:

Setting a Starting Position for a Report Heading in PDF

This request positions the report heading 1.25 inches from the left margin.

SET ONLINE-FMT=PDF
TABLE FILE GGSALES
PRINT BUDDOLLARS DOLLARS
BY STCD
WHERE BUDDOLLARS GE 25000
WHERE STCD EQ 'R1019'
ON TABLE SUBHEAD
"Sales Report"
" "
ON TABLE SET PAGE-NUM OFF
ON TABLE SET SQUEEZE ON
ON TABLE SET STYLESHEET *
TYPE = TABHEADING, POSITION = 1.25, $
ENDSTYLE
END

1672

22. Using Headings, Footings, Titles, and Labels

The output is:

Example:

Setting a Starting Position for a Report Heading in HTML

The request generates an internal cascading style sheet as part of its HTML code, enabling the
use of the POSITION attribute to specify a starting position for the heading, Sales Report, 1.5
inches from the left margin.

SET ONLINE-FMT = HTML
TABLE FILE GGSALES
PRINT BUDDOLLARS DOLLARS
BY STCD
WHERE BUDDOLLARS GE 25000
WHERE STCD EQ 'R1019'
ON TABLE SUBHEAD
"Sales Report"
" "
ON TABLE SET PAGE-NUM OFF
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
TYPE = TABHEADING, POSITION = 1.5, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1673

Positioning Headings, Footings, or Items Within Them

The output is:

Syntax:

How to Set a Starting Position for a Heading or Footing Element

For a PDF or PS report, use the following syntax to specify a starting position for a heading or
footing element in relation to the preceding item

TYPE = headfoot, [subtype,] POSITION = {+|-}option, $

where:

headfoot

Is the type of heading or footing. Valid values are TABHEADING, TABFOOTING, HEADING,
FOOTING, SUBHEAD, and SUBFOOT.

subtype

Are additional attributes that identify the report component. These options can be used
separately or in combination, depending upon the degree of specificity you need to fully
identify an element. Valid values are:

LINE, which identifies a line by its position in a heading or footing. Identifying individual
lines enables you to format each line differently.

1674

22. Using Headings, Footings, Titles, and Labels

If a heading or footing has multiple lines and you apply a StyleSheet declaration that
does not specify LINE, the declaration is applied to all lines. Blank lines are counted
when interpreting the value of LINE.

ITEM, which identifies an item by its position in a line. To divide a heading or footing
line into items, you can use the <+0> spot marker. For details, see Identifying a Report
Component in a WebFOCUS StyleSheet on page 1249.

To determine an ITEM number for an OBJECT, follow these guidelines:

When used with OBJECT=TEXT, count only the text strings from left to right.

When used with OBJECT=FIELD, count only values from left to right.

When used without OBJECT, count text strings and field values from left to right.

If you apply a StyleSheet declaration that specifies ITEM, the number is counted from
the beginning of each line in the heading or footing, not just from the beginning of the
first line.

OBJECT, which identifies an element in a heading or footing as a text string or field
value. Valid values are TEXT or FIELD. TEXT may represent free text or a Dialogue
Manager amper (&) variable.

It is not necessary to specify OBJECT=TEXT unless you are styling both text strings and
embedded fields in the same heading or footing.

option

Is the alignment method. Valid values are:

position, which is the desired distance, expressed by the UNITS attribute (the default is
inches) for absolute positioning.

+, which starts the heading or footing element at the specified distance to the right of
the preceding item. For the first item in a heading or footing, the preceding item is the
left margin of the report.

-, which starts the heading or footing element at the specified distance to the left of the
preceding item. This is useful if you want to overlap images in a heading.

column_title, which aligns the heading or footing element with the first character of the
designated column.

Creating Reports With TIBCO® WebFOCUS Language

 1675

Positioning Headings, Footings, or Items Within Them

Example:

Setting an Absolute Starting Position for a Heading Item

This request uses the spot marker <+0> to divide the report heading into three text strings. It
starts the third text string, 1st Qtr 2001, 3 inches from the left report margin. This technique
can be used in PDF as well as PS reports.

SET ONLINE-FMT = PDF
TABLE FILE GGSALES
SUM UNITS DOLLARS BY CATEGORY BY PRODUCT
ON TABLE SUBHEAD
"Sales Report - <+0>All Products<+0> 1st Qtr 2001"
" "
ON TABLE SET PAGE-NUM OFF
ON TABLE SET SQUEEZE ON
ON TABLE SET STYLESHEET *
TYPE = TABHEADING, OBJECT = TEXT, ITEM=1, SIZE = 12, STYLE = BOLD, $
TYPE = TABHEADING, OBJECT = TEXT, ITEM=2, STYLE = BOLD, $
TYPE = TABHEADING, OBJECT = TEXT, ITEM=3, POSITION = 3, $
ENDSTYLE
END

The output is:

1676

22. Using Headings, Footings, Titles, and Labels

Example:

Setting a Relative Starting Position for a Heading Item

This request uses the spot marker <+0> to divide the report heading into three text strings. It
starts the third text string, 1st Qtr 2001, one inch to the right of the previous item on the
heading line. Inches is the default unit of measure. This technique can be used in PDF as well
as PS reports.

SET ONLINE-FMT = PDF
TABLE FILE GGSALES
SUM UNITS DOLLARS BY CATEGORY BY PRODUCT
ON TABLE SUBHEAD
"Sales Report - <+0>All Products<+0> 1st Qtr 2001"
" "
ON TABLE SET PAGE-NUM OFF
ON TABLE SET SQUEEZE ON
ON TABLE SET STYLESHEET *
TYPE = TABHEADING, OBJECT = TEXT, ITEM=1, SIZE = 12, STYLE = BOLD, $
TYPE = TABHEADING, OBJECT = TEXT, ITEM=2, STYLE = BOLD, $
TYPE = TABHEADING, OBJECT = TEXT, ITEM=3, POSITION = +1, $
ENDSTYLE
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1677

Positioning Headings, Footings, or Items Within Them

Example:

Aligning a Heading Item With a Column

This request uses the spot marker <+0> to divide the report heading into three text strings. It
starts the second text string at the horizontal position where the column UNITS (Unit Sales) is.
This technique can be used in PDF as well as PS reports.

SET ONLINE-FMT = PDF
TABLE FILE GGSALES
SUM UNITS DOLLARS BY CATEGORY BY PRODUCT
ON TABLE SUBHEAD
"Sales Report - <+0>All Products<+0> 1st Qtr 2001"
" "
ON TABLE SET PAGE-NUM OFF
ON TABLE SET SQUEEZE ON
ON TABLE SET STYLESHEET *
TYPE = TABHEADING, LINE=1, ITEM=2, POSITION=UNITS, $
ENDSTYLE
END

The output is:

Tip: In this request the column (UNITS) is identified by name. However, there are other ways to
identify a column that you wish to format. See Identifying a Report Component in a WebFOCUS
StyleSheet on page 1249.

Using PRINTPLUS

PRINTPLUS includes enhancements to display alternatives offered by WebFOCUS. For example,
you can place a FOOTING after a SUBFOOT in your report. PRINTPLUS provides the flexibility to
produce the exact report you desire.

1678

22. Using Headings, Footings, Titles, and Labels

The PRINTPLUS parameter must be set to ON to use the following TABLE capabilities:

PAGE-BREAK is handled internally to provide the correct spacing of pages. For example, if a
new report page is started and an instruction to skip a line at the top of the new page is
encountered, WebFOCUS knows to suppress the blank line and start at the top of the page.

NOSPLIT is handled internally. (Use NOSPLIT to force a break at a specific spot.)

You can perform RECAPs in cases where pre-specified conditions are met.

A Report SUBFOOT now prints above the footing instead of below it.

Data displays correctly in subfoots when IF/WHERE TOTAL or BY HIGHEST is used.

BY field actions are linked with BY field options so they appear on the same page. The
footing no longer splits on two pages.

Footings and Subfoots always appear on a page with at least one data item, and will never
split between two pages.

Printing beyond the length of the page no longer occurs.

Splitting of fields linked by OVER onto separate pages no longer occurs.

There is no reserved space for conditional output. The output page is fully used.

The order of sort fields is no longer relevant.

Note: PRINTPLUS is not supported for StyleSheets. A warning message is generated in this
case.

Syntax:

How to Use PRINTPLUS

Issue the command

SET PRINTPLUS = {ON|OFF}

Creating Reports With TIBCO® WebFOCUS Language

 1679

Positioning Headings, Footings, or Items Within Them

Example:

Using PRINTPLUS With SUBFOOT and FOOTING

With PRINTPLUS on, the SUBFOOT prints first, followed by the FOOTING.

SET PRINTPLUS = ON
 TABLE FILE CAR
  PRINT CAR MODEL
  BY SEATS BY COUNTRY
  IF COUNTRY EQ ENGLAND OR FRANCE OR ITALY
  ON TABLE SUBFOOT
  " "
  " SUMMARY OF CARS IN COUNTRY BY SEATING CAPACITY"
  FOOTING
  " RELPMEK CAR SURVEY "
ON TABLE SET STYLE *
TYPE=REPORT,GRID=OFF,$
ENDSTYLE
END

The output is:

SEATS

-----

    2

COUNTRY

-------

ENGLAND

ITALY

    4

ENGLAND

CAR

—

TRIUMPH

ALFA ROMEO

ALFA ROMEO

MASERATI

JAGUAR

JENSEN

MODEL

-----

TR7

2000 GT VELOCE

2000 SPIDER VELOCE

DORA 2 DOOR

V12XKE AUTO

INTERCEPTOR III

ITALY

ALFA ROMEO

2000 4 DOOR BERLINA

    5

ENGLAND

FRANCE

JAGUAR

PEUGEOT

XJ12L AUTO

504 4 DOOR

 SUMMARY OF CARS IN COUNTRY BY SEATING CAPACITY

 RELPMEK CAR SURVEY

Using Spot Markers to Refine Positioning

You can employ several types of spot markers to refine the positioning of headings and
footings, and elements within them, in HTML and PDF reports that use proportional fonts. For
maximum control, you can combine spot markers with other alignment techniques. See
Choosing an Alignment Method for Heading and Footing Elements on page 1633.

1680





22. Using Headings, Footings, Titles, and Labels

The following spot markers enable you to position items and to identify items to be formatted:

<+0> divides a heading or footing into items for formatting.

To divide a heading or footing into items that can be formatted separately, place the <+0>
spot marker after the text string or field you wish to specify. It will not add any additional
spaces to your heading or footing. For details, see Identifying a Report Component in a
WebFOCUS StyleSheet on page 1249.

</n specifies skipped lines.

To specify skipped lines in a heading or footing, place the </n> spot marker on the same
line as the text in the request. If you place it on a line by itself, WebFOCUS counts the line
the spot marker is on plus the number of skip-lines you designate. For details, see
Controlling the Vertical Positioning of a Heading or Footing on page 1685.

<-n controls the positioning of a character immediately following a field.

Note: When a closing spot marker is immediately followed by an opening spot marker (><), a
single space text item will be placed between the two spot markers (> <). This must be
considered when applying formatting.

You can also use spot markers to position heading and footing elements at fixed and relative
column locations. Several spot markers control positioning based on the pre-defined width of a
character in a monospace font. This is a legacy formatting technique that is not supported for
proportional fonts.

Example:

Positioning a Character Immediately After a Field in an HTML Report

This request generates an HTML report in which the closing parenthesis and the period in the
sort heading follow immediately after the STORE_CODE and STATE fields, respectively. This
behavior is controlled by the <-1 spot markers, which indicate a relative starting position from
the preceding object. Without these spot markers to indicate that the punctuation characters
should follow the preceding objects, an extra space would appear in each of these positions in
the display.

SET ONLINE-FMT = HTML
SET PAGE-NUM = OFF
JOIN STORE_CODE IN CENTCOMP TO STORE_CODE IN CENTORD

Creating Reports With TIBCO® WebFOCUS Language

 1681

Positioning Headings, Footings, or Items Within Them

TABLE FILE CENTCOMP
HEADING
"Century Corporation Orders Report </1"
PRINT PROD_NUM QUANTITY LINEPRICE
BY STORE_CODE NOPRINT
BY ORDER_NUM
ON STORE_CODE SUBHEAD
"Century Corporation orders for store <STORENAME <0X
(store # <STORE_CODE<-1 ) in <STATE|.</1"
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The partial output is:

Example:

Positioning a Character Immediately After a Field in a PDF or PS Report

In a PDF report, an embedded field in a heading or footing must be followed by a space in the
request to be recognized for processing. However, in the output the space may not be
desirable. This example demonstrates two techniques for positioning punctuation characters
immediately after a field in a PDF report.

1682

22. Using Headings, Footings, Titles, and Labels

The first technique uses the POSITION attribute in a StyleSheet to position the closing
parenthesis immediately after the STORE_CODE value. The second technique uses the <-1
spot marker to position the period immediately after the STATE value. The POSITION
measurement is based on the UNITS designation POINTS. Experimentation demonstrated that
-7 points moves the closing parenthesis to the proper location after the field, using the default
proportional font and size.

SET ONLINE-FMT = PDF
SET PAGE-NUM = OFF
JOIN STORE_CODE IN CENTCOMP TO STORE_CODE IN CENTORD

TABLE FILE CENTCOMP
HEADING
"Century Corporation Orders Report"
PRINT PROD_NUM QUANTITY LINEPRICE
BY STORE_CODE NOPRINT
BY ORDER_NUM
ON STORE_CODE SUBHEAD
"Century Corporation orders for store <STORENAME (store # <STORE_CODE )
in <0X <STATE <-1 . </1"
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, UNITS=POINTS, $
TYPE=SUBHEAD, OBJECT=TEXT, ITEM=3, POSITION= -7, $
ENDSTYLE
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1683


Positioning Headings, Footings, or Items Within Them

Without the spot marker and position measurement, the output would have looked like this:

Example:

Customizing Position Measurements for Font Attributes

This request uses a 12-point Helvetica font. Experimentation demonstrated that the POSITION
value of -2 moves the text in this font and size to the required position.

SET ONLINE-FMT = PDF
SET PAGE-NUM = OFF
JOIN STORE_CODE IN CENTCOMP TO STORE_CODE IN CENTORD

TABLE FILE CENTCOMP
HEADING
"CENTURY CORPORATION ORDERS REPORT"
PRINT PROD_NUM QUANTITY LINEPRICE
BY STORE_CODE NOPRINT WHERE STORE_CODE EQ '1003NY' OR '1003CT' OR
    '1003NJ'
BY ORDER_NUM
ON STORE_CODE SUBHEAD
"CENTURY CORPORATION ORDERS FOR STORE <STORENAME (store # <STORE_CODE)<0X
 IN <STATE <-1 . </1"
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, UNITS=POINTS, FONT='Helvetica', SIZE=12, $
TYPE=SUBHEAD, OBJECT=TEXT, ITEM=3, POSITION= -2, $
ENDSTYLE
END

Tip: You cannot use the POSITION attribute to position a heading element in an in HTML
report. However, you can achieve the same result by placing the horizontal spot markers <-1
immediately after the fields STORE_CODE and STATE. Do not add a space between the field
and the character that will follow it.

1684


22. Using Headings, Footings, Titles, and Labels

The output is:

Controlling the Vertical Positioning of a Heading or Footing

You can use several vertical positioning techniques to enhance the appearance and readability
of a report:

In a report generated in HTML, PDF, or other report formats, you can add one or more lines
above or below heading or footing text using spot markers and free text lines. See How to
Add Blank Lines to a Heading or Footing on page 1686.

In a PDF report you can control the space above or below a heading or footing line or the
distance between text and the surrounding grid lines in a heading or footing line using the
TOPGAP and BOTTOMGAP attributes in a StyleSheet. See How to Control Vertical Spacing in
a Heading or Footing on page 1687. For full information on TOPGAP and BOTTOMGAP, see
Laying Out the Report Page on page 1331.

In a PDF report, you can position a page footing at the bottom of a page, rather than
directly after the report data. See How to Position a Page Footing at the Bottom of a Page on
page 1690.

Creating Reports With TIBCO® WebFOCUS Language

 1685

Controlling the Vertical Positioning of a Heading or Footing

Syntax:

How to Add Blank Lines to a Heading or Footing

Use the following syntax options to add blank lines above or below, or within a heading or
footing, where:

</n

Is a spot marker that specifies the number of lines to skip. It is best to put the spot
marker on the same line as the text in the request. If you place the spot marker </n
on a line by itself, it will add that line in addition to the designated number of skipped
lines.

" "

Indicates a separate line in the heading or footing, with blank content.

You can use these techniques separately or in combination.

Example:

Adding Blank Lines Above and Below a Report Heading

This request creates an HTML report with one blank line between each line of the page
heading and two blank lines between the page heading and the actual report. The first blank
line is added as an empty text line, The next blank lines are added with the skip-line spot
marker.

TABLE FILE GGSALES
SUM BUDUNITS UNITS BUDDOLLARS DOLLARS
BY CATEGORY
ON TABLE SUBHEAD
"SALES REPORT"
" "
"**(CONFIDENTIAL)**</1"
"December 2002 </2"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, TOPMARGIN=0, $
TYPE = TABHEADING, JUSTIFY = CENTER, $
ENDSTYLE
END

1686

22. Using Headings, Footings, Titles, and Labels

The output is:

Syntax:

How to Control Vertical Spacing in a Heading or Footing

In a PDF report, you can use the TOPGAP and BOTTOMGAP attributes to control spacing above
or below a heading or footing line or the distance between heading or footing text and the grid
lines above and below them.

Note: You can use TOPGAP and BOTTOMGAP with multi-line headings. Keep in mind that
between heading lines the top and bottom gap will be inserted, making the spacing between
lines greater than the spacing at the top and bottom of the heading.

TYPE=headfoot, {TOPGAP|BOTTOMGAP}=gap, $

where:

headfoot

Is the type of heading or footing. Valid values are TABHEADING, TABFOOTING,
HEADING, FOOTING, SUBHEAD, and SUBFOOT.

TOPGAP

Indicates how much space to add above a report component.

BOTTOMGAP

Indicates how much space to add below a report component.

gap

Is the amount of blank space, in the unit of measurement specified by the UNITS
parameter (inches, by default).

Creating Reports With TIBCO® WebFOCUS Language

 1687

Controlling the Vertical Positioning of a Heading or Footing

In the absence of grids, the default value is 0.

In the presence of grids, the default value increases to provide space between the grid and
the text.

Example:

Adding Blank Space to Separate Heading Text From Grid Lines in a PDF Report

This request generates a PDF report with blank space added above and below the report
heading to separate the text from the upper and lower grid lines. The space above is added by
the TOPGAP attribute. The space below is added by the BOTTOMGAP attribute.

TABLE FILE GGSALES
SUM BUDUNITS UNITS BUDDOLLARS DOLLARS
BY CATEGORY
ON TABLE SUBHEAD
"SALES REPORT <+0>December 2001"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT PDF
ON TABLE SET SQUEEZE ON
ON TABLE SET STYLESHEET *
TYPE = TABHEADING, GRID=ON, JUSTIFY=CENTER, TOPGAP=.25, BOTTOMGAP=.25, $
TYPE = TABHEADING,  FONT='TIMES', SIZE=12, STYLE=BOLD, $
TYPE = TABHEADING, ITEM=2, SIZE=10, STYLE=ITALIC, $
ENDSTYLE
END

The output is:

1688

22. Using Headings, Footings, Titles, and Labels

Example:

Adjusting Vertical Spacing Below a Sort Footing

The request generates a PDF report in which the sort footings are bolded for emphasis and
space is added below each footing to visually tie the footing text to the preceding data.

TABLE FILE GGPRODS
PRINT PACKAGE_TYPE AND UNIT_PRICE
WHERE UNIT_PRICE GT 50
BY PRODUCT_DESCRIPTION NOPRINT BY PRODUCT_ID
ON PRODUCT_DESCRIPTION SUBFOOT
"Summary for <PRODUCT_DESCRIPTION"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT PDF
ON TABLE SET SQUEEZE ON
ON TABLE SET STYLESHEET *
TYPE=SUBFOOT, STYLE=BOLD, BOTTOMGAP=.25, $
ENDSTYLE
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1689

Controlling the Vertical Positioning of a Heading or Footing

Syntax:

How to Position a Page Footing at the Bottom of a Page

You can position a page footing at the bottom of a page. By default, a page footing appears
two lines below the report data.

FOOTING [BOTTOM]
  "content ... "
["content ... "]
.
.
.
["content ... "]

where:

FOOTING

Is the required command that identifies the content as a page footing.

BOTTOM

Is an optional command that places the footing at the bottom of the page. If you omit
BOTTOM, the page footing appears two lines below the report data. Note: FOOTING
BOTTOM is not supported in an HTML report or by the WebFOCUS Viewer.

content

Footing content can include the following elements, between double quotation marks.
(If the ending quotation mark is omitted, all subsequent lines of the request are
treated as part of the footing.)

text

Is the footing text. You can include multiple lines of text.

The text must start on a line by itself, following the FOOTING command.

Text can be combined with variables and spot markers.

For related information, see Limits for Headings and Footings on page 1519.

variable

Can be any one or a combination of the following:

Fields (real data source fields, virtual fields created with the DEFINE command in a
Master File or report request, calculated values created with the COMPUTE command
in a request, system fields such as TABPAGENO). You can qualify data source fields
with certain prefix operators.

Dialogue Manager variables.

Images. You can include images in a heading or footing.

For details, see Including an Element in a Heading or Footing on page 1557.

1690

22. Using Headings, Footings, Titles, and Labels

spot marker

Enables you to position items, to identify items to be formatted, and to extend
code beyond the 80-character line limit of the text editor.

<+0> divides a heading or footing into items for formatting. For details, see Identifying
a Report Component in a WebFOCUS StyleSheet on page 1249.

</n specifies skipped lines. For details, see Controlling the Vertical Positioning of a
Heading or Footing on page 1685.

<-n to position the next character on the line. For details, see Using Spot Markers to
Refine Positioning on page 1680.

<0X continues a heading or footing specification on the next line of the request. For
details, see Extending Heading and Footing Code to Multiple Lines in a Report Request
on page 1520.

Note: When a closing spot marker is immediately followed by an opening spot marker
(><), a single space text item will be placed between the two spot markers (> <). This
must be considered when applying formatting.

Blank lines

If you omit all text, variables, and spot markers, you have a blank heading or footing
line (for example, " ") which you can use to skip a line in the heading or footing. (You
can also skip a line using a vertical spot marker, such as </1.)

Note: The maximum number of sort headings and sort footings in one request is 33.

Example:

Positioning a Page Footing at the Bottom of a Page

This request produces a PDF report in which the page footing appears at the bottom of the
page, rather than in its default position, two lines below the report data.

TABLE FILE GGSALES
PRINT UNITS DOLLARS
BY CATEGORY BY STCD
WHERE TOTAL DOLLARS GE 25000
FOOTING BOTTOM
"PRELIMINARY SALES FIGURES"
ON TABLE SET ONLINE-FMT PDF
ON TABLE SET PAGE-NUM OFF
END

Creating Reports With TIBCO® WebFOCUS Language

 1691

Placing a Report Heading or Footing on Its Own Page

The following output shows the end of the report, with the footing.

Placing a Report Heading or Footing on Its Own Page

In a PDF report or an HTML report displayed in the WebFOCUS Viewer, you can request that a
report heading or footing appear on its own page to set off important information. For example,
you might want to create a cover page that flags salary information as Confidential and is
separate from the actual data.

Syntax:

How to Position a Report Heading or Footing on Its Own Page

Each heading or footing line must begin and end with a double quotation mark.

ON TABLE PAGE-BREAK AND {SUBHEAD|SUBFOOT}
"content ... "
["content ... "]
.
.
.
["content ... "]

where:

PAGE-BREAK

Determines when a new page starts. Use with the SET LINES command to control the
length of a printed page.

SUBHEAD

Generates a report heading.

1692

22. Using Headings, Footings, Titles, and Labels

SUBFOOT

Generates a report footing.

content

Heading or footing content can include the following elements, between double
quotation marks. If the ending quotation mark is omitted, all subsequent lines of the
request are treated as part of the report heading.

text

Is the heading or footing text. You can include multiple lines of text.

The text must start on a line by itself, following the SUBHEAD or SUBFOOT command.

Text can be combined with variables and spot markers.

For related information, see Limits for Headings and Footings on page 1519.

variable

Can be any one or a combination of the following:

Fields (real data source fields, virtual fields created with the DEFINE command in a
Master File or report request, calculated values created with the COMPUTE command
in a request, system fields such as TABPAGENO). You can qualify data source fields
with certain prefix operators.

Dialogue Manager variables.

Images. You can include images in a heading or footing.

For details, see Including an Element in a Heading or Footing on page 1557.

spot marker

Enables you to position items, to identify items to be formatted, and to extend
code beyond the 80-character line limit of the text editor.

<+0> divides a heading or footing into items for formatting. For details, see Identifying
a Report Component in a WebFOCUS StyleSheet on page 1249.

</n specifies skipped lines. For details, see Controlling the Vertical Positioning of a
Heading or Footing on page 1685.

<-n positions the next character on the line. For details, see Using Spot Markers to
Refine Positioning on page 1680.

<0X continues a heading or footing specification on the next line of the request. For
details, see Extending Heading and Footing Code to Multiple Lines in a Report Request
on page 1520.

Creating Reports With TIBCO® WebFOCUS Language

 1693

Placing a Report Heading or Footing on Its Own Page

Note: When a closing spot marker is immediately followed by an opening spot marker
(><), a single space text item will be placed between the two spot markers (> <). This
must be considered when applying formatting.

Blank lines

If you omit all text, variables, and spot markers, you have a blank heading or footing
line (for example, " ") which you can use to skip a line in the heading or footing. (You
can also skip a line using a vertical spot marker, such as </1.)

Example:

Positioning a Report Heading on a Separate Page

Using PAGE-BREAK, this request generates a two-page report, with important information by
itself on the first page.

TABLE FILE CENTORD
SUM ORDER_DATE LINEPRICE AS 'Order,Total:'
BY HIGHEST 5 ORDER_NUM
ON TABLE PAGE-BREAK AND SUBHEAD
"CONFIDENTIAL COMPANY INFORMATION"
"March 2003"
HEADING
"Order Revenue"
" "
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT PDF
END

The first page of output identifies the confidential nature of the report and the date.

The second page of output contains the column titles and data.

1694

22. Using Headings, Footings, Titles, and Labels

Tip: To produce comparable results in HTML, include the following code in the request to turn
on the WebFOCUS Viewer.

ON TABLE SET ONLINE-FMT HTML
ON TABLE SET WEBVIEWER ON
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The first page will display the report heading. You can navigate to the second page for the
report data.

Example:

Positioning a Report Footing on a Separate Page

Using PAGE-BREAK, this request generates a two-page report with the report footing, which
signals the end of the report, on a page by itself.

TABLE FILE CENTORD
HEADING
"Order Revenue"
" "
SUM ORDER_DATE LINEPRICE AS 'Order,Total:'
BY HIGHEST 5 ORDER_NUM
ON TABLE PAGE-BREAK AND SUBFOOT
"END OF REPORT"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT PDF
END

The first page of output contains the column titles and data.

The last page of output signals the end of the report.

Creating Reports With TIBCO® WebFOCUS Language

 1695

Placing a Report Heading or Footing on Its Own Page

Note: To produce comparable results in HTML, include the following code in the request to turn
on the WebFOCUS Viewer.

ON TABLE SET ONLINE-FMT HTML
ON TABLE SET WEBVIEWER ON
ON TABLE SET STYLESHEET *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The first page of output will contain the column titles and data. You can navigate to the last
page to see END OF REPORT.

1696

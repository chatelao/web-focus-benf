Chapter11

Navigating Within an HTML Report

You can include the following navigation features within a report to control the report
display:

Dynamic TOC. You can add a multi-level table of contents to a report to enhance the
viewing and navigation of data. The TOC can appear as an expandable list of clickable
values or as a series of drop-down form controls. By clicking values in the TOC, you
can toggle between views of the data and quickly locate specific values in the report.

WebFOCUS Viewer. You can divide an HTML report into multiple webpages to speed
the delivery of information to your browser. This feature, also known as on-demand
paging, is implemented in the WebFOCUS Viewer, where you can navigate to
subsequent, previous, or specific pages after your first page of output is displayed.

Hyperlinks between pages. You can define automatic hyperlinks in a report that
contains multiple pages, making it easy to link consecutive report pages together and
navigate to the next or previous page.

For related information, see Navigating Between Reports on page 988.

In this chapter:

Navigating Sort Groups From a Table of Contents

Adding the HTML Table of Contents Tree Control to Reports

Controlling the Display of Sorted Data With Accordion Reports

Navigating a Multi-Page Report With the WebFOCUS Viewer

Linking Report Pages

Navigating Sort Groups From a Table of Contents

You can enhance navigation within a large HTML report by adding a dynamic HTML-based Table
of Contents (TOC). To take advantage of this feature, the report must contain at least one
vertical sort (BY) field. If you include more than one sort field in a report, the hierarchy is
determined by the order in which the sort fields are specified in the request.

The TOC also enhances the display of groups of data. You can view one section (or page) of
the report at a time, or you can view all sections at once. You can control this with a page
break. For more information, see Grouping Sort Fields for Display on page 976.

Creating Reports With TIBCO® WebFOCUS Language

 969

Navigating Sort Groups From a Table of Contents

The TOC displays all values of the first (highest-level) vertical sort field, as well as the values of
any lower level BY fields that you designate for inclusion. These values are displayed as an
expandable series of links or as a series of list controls. Unless otherwise specified in the
request, a new page begins when the highest-level sort field changes.

The display of data for a lower level sort field is controlled by your selection of a higher-level
sort field value. For example, in a report sorted first by country and then by car model, if you
choose Italy from the TOC for country, you will only see a listing of Italian models in the TOC for
cars. Cars produced in other countries are not displayed.

Using the TOC, you can:

View any section of a report by clicking the associated link.

Toggle between a single section and the entire report content by clicking View Entire Report.

Remove the TOC by clicking Remove Table of Contents. This is beneficial when printing the
report from the browser. Double-click anywhere in the report to restore it and continue
navigation.

The TOC itself is an object that initially appears as an icon in the upper-left corner of the report
or as one or more drop-down lists in a page heading or footing or a report heading or footing.

Heading Option. To add the TOC to a heading or footing, you can use a StyleSheet. See
How to Add TOC Drop-down List Controls to a Heading on page 981.

Report Option. To add an HTML TOC object to the upper-left hand corner of a report, you
can use a SET command or a PCHOLD command. See How to Add a TOC Tree Control to a
Report Using a SET Command. on page 971.

The sizing of tables within the HTML report is done by the browser. The columns are sized to fit
the largest data value, and trailing spaces are automatically removed. In standard HTML
reports, the data is presented in a single table, so the column widths are fixed for all data
rows. Both HTML BYTOC (Report)/TOC (Heading) features place the data for each sort key
value into individual tables or sections that are accessed using the HTML control. In the HTML
BYTOC/TOC reports, the column widths in each individual table are determined by the data
presented for each value, rather than the overall report. These different table sizes become
apparent when the View Entire Report option is selected. Set SQUEEZE = OFF to define fixed
column widths across all of the tables.

Reference: Usage Notes for HTMLARCHIVE With HTML Table of Contents

WebFOCUS interactive reporting features must have a connection to the WebFOCUS client in
order to access the components required to operate successfully.

970

11. Navigating Within an HTML Report

HTMLARCHVE can be used to create self-contained HTML pages with user-defined images
when client access is not available.

To generate HTML pages containing user-defined images that can operate interactively, use
one of the following commands:

SET HTMLEMBEDIMG=ON
SET HTMLARCHIVE=ON

Define BASEURL to point directly to the host machine where these files can be accessed using
the following syntax:

SET BASEURL=http://{hostname:portnumber}

For more information on SET BASEURL, see Specifying a Base URL on page 872.

Adding the HTML Table of Contents Tree Control to Reports

You can use three different types of syntax to add an HTML TOC object to a report.

Syntax:

How to Add a TOC Tree Control to a Report Using a SET Command.

Using a SET command, the syntax is

At the beginning of a request:

SET COMPOUND = 'BYTOC [n]'

In a request, use the syntax:

ON TABLE SET COMPOUND 'BYTOC [n]'

where:

n

Represents the number of vertical sort (BY) fields to include in the TOC, beginning with
the first (highest-level) sort field in the request. The hierarchy of sort fields is
determined by the order in which they are specified in the request.

The default value is 1, meaning that only the highest-level sort field and its values are
displayed in the TOC.

By default, a section break is placed after the first (highest-level) sort field, unless
otherwise specified in the request.

Note: Single quotation marks (') should be used when BYTOC is specified with a number in a
SET command.

Creating Reports With TIBCO® WebFOCUS Language

 971

Adding the HTML Table of Contents Tree Control to Reports

Syntax:

How to Add a TOC Tree Control to a Report by Using the PCHOLD Command

Using a PCHOLD command, the syntax is

ON TABLE PCHOLD FORMAT HTML BYTOC [n]

where:

n

Represents the number of vertical sort (BY) fields to include in the TOC, beginning with
the first (highest-level) sort field in the request. The hierarchy of sort fields is
determined by the order in which they are specified in the request.

The default value is 1, meaning that only the highest-level sort field and its values are
displayed in the TOC.

By default, a section break is placed after the first (highest-level) sort field, unless
otherwise specified in the request.

Note: Single quotation marks (') should not be used when BYTOC is specified in a PCHOLD
command with a number.

Syntax:

How to Add a TOC Tree Control to a Report Using a StyleSheet Declaration

The following syntax enables the TOC tree control in the StyleSheet:

TYPE=REPORT, TOC='n',$

or

TYPE=REPORT, TOC='sortfieldname',$

where:

n

Represents the number of vertical sort (BY) fields to include in the TOC, beginning with the
first (highest-level) sort field in the request. The hierarchy of sort fields in the TOC Tree is
determined by the order in which they are listed in the request.

sortfieldname

Specifies the vertical sort (BY) column by its field name.

Note: Single quotation marks (') should be used when TOC is specified in the StyleSheet.

Example:

Adding an HTML TOC as an Object in the Report (Report Option)

You can add an HTML TOC as an icon to the upper-left corner of a report by preceding the
request with a SET command, as illustrated in the following request. The TOC will list values of
the first (highest level) vertical sort field, PLANT:

972

11. Navigating Within an HTML Report

SET COMPOUND='BYTOC 2'

TABLE FILE CENTORD
HEADING
"SALES REPORT"
SUM LINEPRICE BY PLANT BY PRODCAT
ON TABLE SET PAGE-NUM OFF
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

You can also add an HTML TOC as an icon to the upper-left corner of a report by using a SET
command within the request.

TABLE FILE CENTORD
HEADING
"SALES REPORT"
SUM LINEPRICE BY PLANT BY PRODCAT
ON TABLE SET PAGE-NUM OFF
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET COMPOUND 'BYTOC 2'
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The following example shows how you can use a PCHOLD command to run the request:

TABLE FILE CENTORD
HEADING
"SALES REPORT"
SUM LINEPRICE BY PLANT BY PRODCAT
ON TABLE SET PAGE-NUM OFF
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT HTML BYTOC 2
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 973

Adding the HTML Table of Contents Tree Control to Reports

In the following request, the TOC Tree control is enabled in the Report StyleSheet:

TABLE FILE CENTORD
HEADING
"SALES REPORT"
SUM LINEPRICE
BY PLANT BY PRODCAT
ON TABLE SET PAGE-NUM OFF
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=REPORT, TOC='PRODCAT', $
ENDSTYLE
END

Note: Single quotation marks (') should be used when TOC is specified in the StyleSheet.

Run the report. The TOC object displays in the upper-left corner.

974

11. Navigating Within an HTML Report

Double-click the TOC icon to open the Table of Contents Tree control. This displays the values
of the sort fields in the report in the order in which they have been specified.

Note: You can move the TOC by clicking the blue area above Table of Contents and then
dragging it to another area of the report, or double-click on a desired location in the report.

If you wish to display all available fields (the whole report), click the View Entire Report (On/Off)
option.

Creating Reports With TIBCO® WebFOCUS Language

 975

Adding the HTML Table of Contents Tree Control to Reports

Tip: You can also customize the look and feel of the TOC object by editing a .css file. It is
recommended that you make a backup copy prior to editing.

If you are working in a self service or Managed Reporting environment from a browser, go to
the \ibi\WebFOCUS##\ibi_apps\ibi_html\javaassist\intl\xx directory, where ## is the
release of WebFOCUS and xx is the language abbreviation. For English (EN) the .css file
name is toc.css. For all other languages the .css file name is xxtoc.css, where xx is the
language abbreviation.

Note: If you click Remove Table of Contents and then want to view the TOC again, simply
double-click on a desired location in the report.

Reference: Grouping Sort Fields for Display

Data in a TOC report is grouped into sections based on the sort fields. TOC reports only display
one section at a time for easier viewing. Each section contains all of the values for its sort
field. You can customize each section with a page break. By default, a page break is included
in the first (highest level) sort field. You can add page breaks to create additional sections and
group data that is based on lower level sort fields.

When adding a TOC to a heading, add additional page breaks for each lower level sort field.
This ensures that the sorted data is correctly grouped and displayed.

Example:

Customizing Sections of the Report With a Page Break

TABLE FILE SHORT
PRINT PROJECTED_RETURN
BY CONTINENT
BY REGION
BY COUNTRY
BY HOLDER
BY TYPE
ON HOLDER PAGE-BREAK
ON TABLE SET PAGE-NUM OFF
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET COMPOUND 'BYTOC 5'
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
TYPE=REPORT,
GRID=OFF,
FONT='ARIAL',
SIZE=9,
COLOR='BLACK',
BACKCOLOR='NONE',
STYLE=NORMAL,
$
ENDSTYLE
END

976

11. Navigating Within an HTML Report

One section of the report is displayed at a time.

The report is broken into sections based on the values for HOLDER. You will see the detail for
each value of HOLDER in a single section.

Navigation Behavior in a Multi-Level TOC

If you select a value in the TOC, that value flashes (that is, it is highlighted in gray) to draw
your attention to it in the browser window. Where the flash appears, and whether and how the
screen display changes, is controlled by the following factors:

When you change the highest level sort group from the TOC (either from the hierarchy
above the report or from the first drop-down list in a heading or footing), the selected value
flashes three times in the browser window.

When you change a lower-level sort value within the current high-level sort group, the
selected value flashes three times in window. This is because you are still within the same
major sort group, and, therefore, within the same page-break. From the selected value at
the top of the window: you can then scroll quickly to the related details.

If the selected lower level value is already viewable on the screen, and the remaining report
will fit on the screen, the value flashes, but the report does not scroll.

Creating Reports With TIBCO® WebFOCUS Language

 977

Adding the HTML Table of Contents Tree Control to Reports

Example:

Navigating Sorted Data From a Multi-Level TOC

This request adds a dynamic HTML TOC as an icon in the upper-left corner of the report by
including a SET command in the request. The TOC displays a hierarchy consisting of four levels
of sort fields, beginning with the first (highest-level). The sort fields are: CONTINENT, REGION,
COUNTRY, and TYPE.

TABLE FILE SHORT
PRINT PROJECTED_RETURN
BY CONTINENT
BY REGION
BY COUNTRY
BY HOLDER
BY TYPE
ON TABLE SET PAGE-NUM OFF
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET COMPOUND 'BYTOC 5'
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
TYPE=REPORT,
GRID=OFF,
FONT='ARIAL',
SIZE=9,
STYLE=NORMAL,
$
ENDSTYLE
END

978

The output is displayed with the TOC object in the upper-left corner.

11. Navigating Within an HTML Report

Double-click the object to expand the Table of Contents.

Select View Entire Report. Scroll down to see that the report contains data for all of the
continents.

Creating Reports With TIBCO® WebFOCUS Language

 979

Adding the HTML Table of Contents Tree Control to Reports

Scroll back to the top of the report window and reopen the TOC. This time select Americas.
Your selection flashes to highlight it on the screen. Although the report display does not
appear to change, if you scroll down now you will see that the report only contains values for
the Americas.

Scroll up again and double-click anywhere in the report to open the TOC. This time click the +
sign next to Americas, then click the + sign next to South America.

The field values (Argentina and Brazil) are listed in the TOC. These are values of the field
COUNTRY. If you wish to see the field name of a value in the TOC, hover over that value with
your cursor.

980

Select Brazil. Your selection flashes and moves to the top of the window, as shown next.

11. Navigating Within an HTML Report

Scroll down to see the data for Brazil.

Continue to navigate to the detail you want to view by choosing values at any sort level in the
TOC.

Clicking a + sign expands the field to display its values in the TOC.

Clicking an actual value (hyperlink) in the TOC momentarily highlights that value and, if
necessary, adjusts the report display to move the value into view.

The TOC collapses to its icon when you click Table of Contents, but you can continue to
scroll back, expand it, and make additional selections.

Syntax:

How to Add TOC Drop-down List Controls to a Heading

Include the following attribute in your StyleSheet declaration

TYPE=heading, [subtype,] TOC=sort_column, $

where:

heading

Is the type of heading or footing that contains the TOC.
Valid values are:

Creating Reports With TIBCO® WebFOCUS Language

 981

Adding the HTML Table of Contents Tree Control to Reports

TABHEADING

TABFOOTING

HEADING

FOOTING

subtype

Report heading.

Report footing.

Page heading.

Page footing.

Are attributes that identify the location in the heading or footing where each requested
drop-down list will be displayed. These options can be used separately or in
combination, depending upon the degree of specificity required to identify a
component. Valid values are:

LINE_# identifies a line by its position in a heading or footing.

If a heading or footing has multiple lines and you apply a StyleSheet declaration that does
not specify LINE_#, the declaration is applied to all lines. Blank lines are counted when
interpreting the value of LINE.

LINE=n is required for a heading or footing that has multiple lines. Otherwise, you can
omit it.

OBJECT identifies the TOC object in a heading or footing as a text string or field value.
Valid values are TEXT or FIELD.

You can use a field and/or text as a placeholder for a TOC drop-down list. However, field is
preferred. (If the TOC feature is not in effect, the field name is displayed in the report.)

TEXT may represent free text or a Dialogue Manager amper (&) variable.

It is not necessary to specify OBJECT=TEXT unless you are styling both text strings and
embedded fields in the same heading or footing.

For related information, see ITEM_#.

ITEM_# which identifies an item by its position in a line.

To determine an ITEM_# for an OBJECT, follow these guidelines:

When used with OBJECT=TEXT, count only the text strings from left to right.

When used with OBJECT=FIELD, count only the fields from left to right.

If you apply a StyleSheet declaration that specifies ITEM_#, the number is counted from
the beginning of each line in the heading or footing, not just from the beginning of the first
line.

982

11. Navigating Within an HTML Report

sort_column

Identifies the vertical sort columns (BY fields) to include as TOCs. You can identify a
column using the following notations:

TOC=fieldname specifies the sort column by its field name.

TOC=Bn specifies the sort column by its order in the request. For example, B2 denotes the
second BY field (NOPRINT BY fields are included in the count).

TOC=n is the same as TOC=Bn.

Note: You must maintain the hierarchy of BY fields because the TOC objects in headings (the
drop-down lists) are interdependent and corresponds with the hierarchy in the report.

Example:

Adding HTML TOC Drop Down Lists in a Page Heading

This request uses the required StyleSheet attributes to add a TOC to an HTML report. The
drop-down TOC lists the values of the field CONTINENT, identified in the StyleSheet code as
OBJECT=FIELD, ITEM=1, TOC=CONTINENT.

TABLE FILE SHORT
HEADING
"Projected Returns Report for Region:  <REGION in Continent:  <CONTINENT "
" "
SUM PROJECTED_RETURN
BY CONTINENT
BY REGION
BY COUNTRY
BY TYPE
ON TABLE SET PAGE-NUM OFF
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
TYPE=REPORT,
GRID=OFF,
FONT='ARIAL',
SIZE=9,
STYLE=NORMAL,
$
TYPE=HEADING, LINE=1, OBJECT=FIELD, ITEM=1, TOC=CONTINENT, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 983

Adding the HTML Table of Contents Tree Control to Reports

When you run the report. The TOC appears as a drop-down menu in the heading, in place of
the field CONTINENT:

Click the TOC to see the list of sort values: AMERICAS, ASIA, EUROPE.

Click each continent to see the related information. The selected value flashes gray to
highlight it in the window.

984

11. Navigating Within an HTML Report

You can display all available fields (the whole report) by clicking the View Entire Report option.
To remove the TOC, click the Remove Table of Contents option. To restore the TOC, double-click
anywhere in the report or click the Refresh button in your browser.

Example:

Navigating a Multi-Level HTML TOC in a Page Heading

This request uses a StyleSheet to add an HTML TOC that contains drop-down lists in the third
line of the page heading for two sort (BY) fields specified in the request: CONTINENT and
REGION. Each field becomes a place-holder for its TOC. (If the TOC features were not in effect,
the field would display in the report.)

TABLE FILE SHORT
"Projected Return"
" "
"For:<CONTINENT For:<REGION "
SUM PROJECTED_RETURN
BY CONTINENT BY REGION BY COUNTRY BY TYPE
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET HTMLCSS ON
ON CONTINENT PAGE-BREAK
ON TABLE SET STYLE *
TYPE=REPORT,
GRID=OFF,
FONT='ARIAL',
SIZE=9,
STYLE=NORMAL,
$
TYPE=HEADING, LINE=1, STYLE=BOLD, $
TYPE=HEADING, LINE=3, OBJECT=FIELD, ITEM=1, TOC=B1,$
TYPE=HEADING, LINE=3, OBJECT=FIELD, ITEM=2, TOC=REGION,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 985

Adding the HTML Table of Contents Tree Control to Reports

The output is:

986

11. Navigating Within an HTML Report

Click the arrow in the second TOC drop-down list and select North America. Keep in mind that
the values in this drop-down list are related to those in the higher level drop-down list. They are
all part of the same higher level sort group, and therefore, within the same section break. The
selected value, North America, flashes and moves to the top of the browser window. From
there, you can scroll to see the related data, as shown in the image below.

Note that if you select information already in your field of view, the value will be highlighted in
gray and will flash, to draw your attention to it.

Creating Reports With TIBCO® WebFOCUS Language

 987

Adding the HTML Table of Contents Tree Control to Reports

Next, scroll up and choose ASIA from the first TOC list. This selection changes your highest-
level sort group, and affects all of the lists below it. ASIA flashes and moves to the top of the
window, where you see information for the first country (Hong Kong) in the Far East region. The
page number is now 2 since this is the second of the high-level sort groups in the TOC.

Continue to experiment with other selections.

Reference: Navigating Between Reports

Along with techniques and tools for navigating within a report, WebFOCUS provides several
mechanisms for navigating between reports. With these features, a user initiates navigation
from a report display. You can:

Drill down to other reports, URLs, and JavaScript functions. See Linking a Report to Other
Resources on page 819.

Define frames and populate them with reports. See Specifying a Target Frame on page 873.

988

11. Navigating Within an HTML Report

Reference: HTML Table of Contents Limits

The TOC feature:

Applies to HTML output.

Is supported with Internet Explorer. This feature may generate unexpected behavior when
using other browsers. See the Web Browser Support Statement for WebFOCUS (https://
techsupport.informationbuilders.com/tech/wbf/wbf_tmo_027.html) for information on
supported browsers for this and other WebFOCUS features.

Does not support the Dialogue Manager command -HTMLFORM.

Is not supported with Accordion reports.

You cannot designate a TOC for a BY field without also specifying a TOC for its parent (BY)
fields. The reason for this is that the TOC controls are interdependent and require the
physical presence of each parent control to operate correctly. For example, if the request
contains BY COUNTRY BY CAR BY MODEL, a report cannot include a TOC control for CAR
without also including one for COUNTRY.

The size of a TOC-enabled report is limited to the memory available on the WebFOCUS
Client.

If your request has both BYTOC Table of Contents and a Heading Table of Contents in the
StyleSheet, the output will have the Heading TOC.

If you have installed ReportCaster, you can distribute a report with an HTML TOC by including
the following commands in the report request:

The SET BASEURL command set to the URL to connect to the application server on which
WebFOCUS Client is installed. For information, see Specifying a Base URL on page 872.

Controlling the Display of Sorted Data With Accordion Reports

Accordion Reports provide a way to control the amount of sorted data that appears on an
HTML report page. You can produce reports with expandable views for each vertical sort field in
a request with multiple BY fields.

Creating Reports With TIBCO® WebFOCUS Language

 989

Controlling the Display of Sorted Data With Accordion Reports

You can create two types of Accordion Reports:

Accordion By Row. Accordion By Row reports present sort field values and their
corresponding aggregated measures rolled up so that the highest level sort field and the
grand totals are at the top of the report. A tree control can be used to open each dimension
and view the associated aggregated values. Clicking the plus sign (+) next to a sort field
value opens new rows that display the next lower-level sort field values and subtotals. The
lowest-level sort field, when expanded, displays the aggregated data values. This type of
Accordion Report is generated using the SET EXPANDBYROW command.

Using the Accordion By Row enhanced interface, navigation is easier when working with
wide and large reports in a portal page, the data automatically resizes to fit the size of the
container, and the column widths automatically adjust based on the largest data value or
column title, whichever is larger. The SET EXPANDBYROWTREE=ON command in a
procedure enables the enhanced Accordion by Row feature. For more information on the
enhanced interface, see How to Create an Accordion Report With the Enhanced Interface on
page 999.

Note: EXPANDBYROW is functionally stabilized. Any future enhancements will be done for
EXPANDBYROWTREE.

Accordion By Column. Accordion By Column reports present rolled up sort field and data
values. However, they do not automatically display entire report rows. A plus sign appears
to the left of each data value in the column under the highest-level sort heading. For data
associated with lower-level sort fields, a plus sign is placed to the left of each data value,
but the data does not appear unless manually expanded. Data values of the lowest-level
sort field are not expandable. To expand your view of data for any expandable sort field,
click a plus sign and all data associated with the next lower-level sort field appears. When
you expand a data value under the next to lowest sort heading, all of the remaining
associated data values in the report appear. This type of Accordion Report is generated
using the SET EXPANDABLE command.

The use of horizontal sort fields coded with ACROSS phrases is supported with Accordion
Reports. The ACROSS sort headings that appear above vertical sort headings in a standard
HTML report do not display in an Accordion Report until at least one sorted data value has
been manually expanded in each expandable sort column.

Two vertical sort fields coded with BY phrases are required when using Accordion Reports. If
the command syntax does not contain at least two BY phrases, the Accordion Reports
EXPANDABLE, EXPANDBYROW, or EXPANDBYROWTREE command is ignored, no message is
generated, and a standard HTML report is created.

Note: Accordion Reports are only supported for HTML report output.

990

Requirements for Accordion Reports

11. Navigating Within an HTML Report

The following requirements must be taken into consideration when creating Accordion Reports:

Adding a drill-down link to an Accordion Report requires that the TARGET parameter must be
set to a value that specifies a new HTML frame.

Once an Accordion Report is created and delivered to the user, there are no subsequent
calls to the WebFOCUS Reporting Server required when the user is interacting with the
report. However, the collapsible folder controls on the sort fields require JavaScript and
images that reside on the WebFOCUS Client. The user must be connected to the
WebFOCUS Web tier components in order to use this feature. For online, connected users
of WebFOCUS, no change is required to the report.

However, for distribution of reports using ReportCaster, see the following Reference topic to
ensure that the report is delivered correctly as an email attachment or as an archived
report in the Report Library.

Reference: Usage Notes for HTMLARCHIVE With Accordion Reports

WebFOCUS interactive reporting features must have a connection to the WebFOCUS client in
order to access the components required to operate successfully.

HTMLARCHVE can be used to create self-contained HTML pages with user-defined images
when client access is not available.

To generate HTML pages containing user-defined images that can operate interactively, use
one of the following commands:

SET HTMLEMBEDIMG=ON
SET HTMLARCHIVE=ON

Define BASEURL to point directly to the host machine where these files can be accessed using
the following syntax:

SET BASEURL=http://{hostname:portnumber}

For more information on SET BASEURL, see Specifying a Base URL on page 872.

Reference: Distributing Accordion Reports With ReportCaster

Distributing Accordion Reports with ReportCaster requires the use of JavaScript components
and images located on the WebFOCUS Client. To access the JavaScript components and
images from a report distributed by ReportCaster, the scheduled procedure must contain the
SET FOCHTMLURL command, which must be set to an absolute URL instead of the default
value. For example,

Creating Reports With TIBCO® WebFOCUS Language

 991

Controlling the Display of Sorted Data With Accordion Reports

SET FOCHTMLURL = http://hostname[:port]/ibi_apps/ibi_html

where:

hostname[:port]

Is the host name and optional port number (specified only if you are not using the default
port number) where the WebFOCUS Web application is deployed.

ibi_apps/ibi_html

ibi_apps is the site-customized web server alias pointing to the WEBFOCUS81/ibi_apps
directory (where ibi_apps is the default value). ibi_html is a directory within the path to the
JavaScript files that are required to be accessible when viewing an Accordion report.

For more information about coding reports for use with ReportCaster, see the Tips and
Techniques for Coding a ReportCaster Report appendix in the ReportCaster manual.

Creating an Accordion By Row Report

Accordion By Row reports are HTML reports that offer an interactive interface to data
aggregated at multiple levels by presenting the sort fields within an expandable tree. By
default, the report will present the highest dimension or sort field (BY value) and the
aggregated measures associated with each value. The tree control can be used to open or
close each dimension and view the associated aggregated values. Clicking the plus sign (+)
next to a sort field value opens new rows that display the next lower level sort field values and
subtotals. The lowest level sort field, when expanded, displays the aggregated data values.

Using the SET EXPANDBYROW or SET EXPANDBYROWTREE command with HTMLCSS ON
enables any HTML report to be turned into an Accordion By Row request. EXPANDBYROW and
EXPANDBYROWTREE automatically invoke the SET SUBTOTALS=ABOVE command, which
moves the subtotal rows above the subheading and data rows. A SUB-TOTAL command is
automatically added for the next-to-last BY field.

When an Accordion By Row report uses the PRINT command, the innermost level of the
resulting tree contains detail records from the data source. There can be many detail records
for each combination of BY fields, so it may be unclear what distinguishes the various detail
records within the display. In order to make the report more useful, include at least one field in
the report that can be used to distinguish between the detail level rows.

When an Accordion By Row report uses the SUM command, each row, even at the innermost
level of the tree, is actually a subtotal row and is completely described by the combination of
BY fields in the request. Each level will be presented at the aggregated level, and the data
values will represent the aggregation of the lowest level BY.

992

11. Navigating Within an HTML Report

Styling an Accordion By Row report can be done using standard HTML report techniques, but it
is important to keep the report structure in mind. All rows, except the lowest level, are actually
SUBTOTAL rows and the lowest level contains the report DATA.

Accordion By Row reports display the grand total row as an anchor row below the data. This
anchor row displays above both the report and page footings aligned to the left margin of the
report. To generate Accordion By Row reports without the grand total anchor row, add ON
TABLE NOTOTAL to the request.

Using the Accordion By Row enhanced interface, navigation is easier when working with wide
and large reports in a portal page, the data automatically resizes to fit the size of the
container, and the column widths automatically adjust based on the largest data value or
column title, whichever is larger. The SET EXPANDBYROWTREE=ON command in a procedure
enables the enhanced Accordion by Row feature. The SET AUTOFIT ON command in a
procedure automatically resizes the data to fit the size of the container. For more information
on the enhanced interface, see How to Create an Accordion Report With the Enhanced Interface
on page 999.

Accordion reports can also be created to be opened by column, instead of by row. See How to
Create an Accordion Report With the Enhanced Interface on page 999 for information on how
to create Accordion reports using the SET EXPANDABLE command.

Syntax:

How to Create Accordion Reports That Expand By Row

SET EXPANDBYROW = {OFF|ON|n}

ON TABLE SET EXPANDBYROW {OFF|ON|n}

where:

OFF

Does not create an Accordion report. OFF is the default value.

ON

ALL

Creates an Accordion report, which initially displays only the highest sort field level. To see
rows on lower levels, click the plus sign (+) next to one of the displayed sort field values.

Creates an Accordion report in which all sort field levels are initially expanded. To roll up a
sort field level, click the minus sign (-) next to one of the sort field values on that level.

Creating Reports With TIBCO® WebFOCUS Language

 993

Controlling the Display of Sorted Data With Accordion Reports

n

Creates an Accordion report in which n sort field levels are initially expanded. To roll up an
expanded sort field level, click the minus sign (-) next to one of the sort field values on that
level.

Note:

Accordion By Row reports require that the HTMLCSS parameter be set to ON.

By default, a blank line is generated before a subtotal on the report output. You can
eliminate these automatic blank lines by issuing the SET DROPBLNKLINE=ON
command.

Example:

Creating an Accordion By Row SUM Report

The following request against the GGSALES data source has four sort fields, REGION, ST,
CATEGORY, and PRODUCT:

TABLE FILE GGSALES
SUM DOLLARS/D8MC
UNITS/D8C
BUDDOLLARS/D8MC BUDUNITS/D8C
BY REGION
BY ST
BY CATEGORY
BY PRODUCT
ON TABLE SET HTMLCSS ON
ON TABLE SET EXPANDBYROW ON
ON TABLE SET DROPBLNKLINE ON
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET STYLE *
TYPE=REPORT,
    COLOR=RGB(66 70 73),
    FONT='TREBUCHET MS',
    SIZE=9,
    SQUEEZE=ON,
    GRID=OFF,
$
TYPE=REPORT,
    GRID=OFF,
    FONT='TREBUCHET MS',
    COLOR=RGB(52 85 64),
$

994

11. Navigating Within an HTML Report

TYPE=TITLE,
    COLOR='WHITE',
    BACKCOLOR=RGB(52 85 64),
    STYLE=-UNDERLINE,
$
TYPE=HEADING,
    COLOR='WHITE',
    BACKCOLOR=RGB(52 85 64),
$
TYPE=FOOTING,
    COLOR='WHITE',
    BACKCOLOR=RGB(52 85 64),
$
TYPE=SUBTOTAL,
    BACKCOLOR=RGB(72 118 91),
$
TYPE=SUBTOTAL,
    BY=1,
    COLOR='WHITE',
$
TYPE=SUBTOTAL,
    BY=2,
    COLOR='WHITE',
    BACKCOLOR=RGB(132 159 126),
$
TYPE=SUBTOTAL,
    BY=3,
    COLOR='WHITE',
    BACKCOLOR=RGB(158 184 153),
$
TYPE=GRANDTOTAL,
    COLOR='WHITE',
    BACKCOLOR=RGB(52 85 64),
    STYLE=BOLD,
$
ENDSTYLE
END

The initial output shows only the top level BY field (REGION), as shown in the following image.

Creating Reports With TIBCO® WebFOCUS Language

 995

Controlling the Display of Sorted Data With Accordion Reports

Clicking the plus sign (+) next to the Midwest region opens the rows that show the states
associated with that region, as shown in the following image.

Clicking the plus sign (+) next to the state IL opens the rows that show the categories
associated with that state, as shown in the following image.

996

11. Navigating Within an HTML Report

Clicking the plus sign (+) next to the Coffee category shows the products associated with that
category, as shown in the following image. This is the lowest level of the Accordion By Row
report.

Example:

Creating an Accordion By Row PRINT Report

The following request against the EMPLOYEE data source has two sort fields, DEPARTMENT
and YEAR. It uses the PRINT display command.

SET EXPANDBYROW = ALL
DEFINE FILE EMPLOYEE
YEAR/YY = HIRE_DATE;
YEARMO/YYM = HIRE_DATE;
END
TABLE FILE EMPLOYEE
PRINT LAST_NAME AS 'Last,Name' FIRST_NAME AS 'First,Name'
CURR_SAL AS 'Current,Salary' ED_HRS AS 'Education,Hours'
BY DEPARTMENT BY YEAR
WHERE YEAR GT 1980
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
TYPE=REPORT,
    COLOR=RGB(66 70 73),
    FONT='TREBUCHET MS',
    SIZE=9,
    SQUEEZE=ON,
    GRID=OFF,
$

Creating Reports With TIBCO® WebFOCUS Language

 997

Controlling the Display of Sorted Data With Accordion Reports

TYPE=TITLE,
    BACKCOLOR=RGB(102 102 102),
    COLOR=RGB(255 255 255),
    STYLE=-UNDERLINE+BOLD,
$
TYPE=DATA,
    BACKCOLOR=RGB(255 255 255),
$
TYPE=TITLE,
    COLOR='WHITE',
    BACKCOLOR=RGB(52 85 64),
    STYLE=-UNDERLINE,
$
TYPE=HEADING,
    COLOR='WHITE',
    BACKCOLOR=RGB(52 85 64),
$
TYPE=FOOTING,
    COLOR='WHITE',
    BACKCOLOR=RGB(52 85 64),
$
TYPE=SUBTOTAL,
    BACKCOLOR=RGB(72 118 91),
$
TYPE=SUBTOTAL,
    BY=1,
    COLOR='WHITE',
$
TYPE=SUBTOTAL,
    BY=2,
    COLOR='WHITE',
    BACKCOLOR=RGB(132 159 126),
$
TYPE=SUBTOTAL,
    BY=3,
    COLOR='WHITE',
    BACKCOLOR=RGB(158 184 153),
$
TYPE=GRANDTOTAL,
    COLOR='WHITE',
    BACKCOLOR=RGB(52 85 64),
    STYLE=BOLD,
$
ENDSTYLE
END

Including the fields LAST_NAME and FIRST_NAME in the report output distinguishes each detail
line. However, those fields do not apply to the summary lines, so they are blank on the
summary lines.

998

The output is:

11. Navigating Within an HTML Report

Syntax:

How to Create an Accordion Report With the Enhanced Interface

SET EXPANDBYROWTREE = {OFF|ON|ALL|n}
ON TABLE SET EXPANDBYROWTREE {OFF|ON|ALL|n}

Creating Reports With TIBCO® WebFOCUS Language

 999

Controlling the Display of Sorted Data With Accordion Reports

where:

OFF

Does not create an Accordion report, with the enhanced interface. OFF is the default value.

Creates an Accordion report, with the enhanced interface. This setting initially displays only
the highest sort field level. To see rows on lower levels, click the plus sign (+) next to one
of the displayed sort field values.

Creates an Accordion report, with the enhanced interface. This setting displays all sort
field levels initially expanded. To roll up a sort field level, click the minus sign (-) row next
to one of the sort field values on that level.

ON

ALL

n

Creates an Accordion report, with the enhanced interface. This setting displays the n sort
field levels initially expanded. To roll up an expanded sort field level, click the minus sign
(-) next to one of the sort field values on that level.

Example:

Creating an Accordion Report With the Enhanced Interface

The following request against the GGSALES data source has four sort fields, REGION, ST,
CATEGORY, and PRODUCT. The request uses the default StyleSheet and the default plus sign
(+) and minus sign (-) to expand or collapse a row. In order to create the Accordion report, with
the enhanced interface, the SET EXPANDBYROWTREE command must be set to ON. In order to
automatically resize the data to fit the size of the container, the SET AUTOFIT command must
be set to ON.

TABLE FILE GGSALES
SUM DOLLARS/D8MC
UNITS/D8C
BUDDOLLARS/D8MC BUDUNITS/D8C
BY REGION
BY ST
BY CATEGORY
BY PRODUCT
ON TABLE SET EXPANDBYROWTREE ON
ON TABLE SET DROPBLNKLINE ON
ON TABLE SET AUTOFIT ON
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET STYLE *
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/ibi_themes/Warm.sty,$
ENDSTYLE
END

1000

The initial output shows only the top level BY field (REGION), as shown in the following image.

11. Navigating Within an HTML Report

Clicking the plus sign (+) next to the Midwest region opens the rows that show the states
associated with that region, as shown in the following image.

Clicking the plus sign (+) next to the state IL opens the rows that show the categories
associated with that state, as shown in the following image.

Creating Reports With TIBCO® WebFOCUS Language

 1001

Controlling the Display of Sorted Data With Accordion Reports

Clicking the plus sign (+) next to the Coffee category shows the products associated with that
category, as shown in the following image. This is the lowest level of the Accordion By Row
report.

You can use the EBRT_ANCHOR StyleSheet attribute to change the default plus sign (+) and
minus sign (-) to an arrow. Valid settings for the EBRT_ANCHOR attribute are PLUSMINUS and
ARROWS. The following request changes the default plus sign (+) and minus sign (-) to an
arrow, and applies StyleSheet formatting to the request to change the color of the text to white
and the background color to different shades of purple.

Note: The color of the arrows match the color of the SUBTOTAL line, in this case, white.

1002

11. Navigating Within an HTML Report

TABLE FILE GGSALES
SUM DOLLARS/D8MC
UNITS/D8C
BUDDOLLARS/D8MC BUDUNITS/D8C
BY REGION
BY ST
BY CATEGORY
BY PRODUCT
ON TABLE SET EXPANDBYROWTREE ON
ON TABLE SET DROPBLNKLINE ON
ON TABLE SET AUTOFIT ON
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET STYLE *
TYPE=REPORT, EBRT_ANCHOR=ARROWS,
COLOR=RGB(66 70 73), FONT='TREBUCHET MS', SIZE=9, SQUEEZE=ON,$
TYPE=REPORT, FONT='TREBUCHET MS', COLOR=RGB(151 43 153),$
TYPE=TITLE, COLOR='WHITE', BACKCOLOR=RGB(151 43 153), STYLE=-UNDERLINE,$
TYPE=HEADING, COLOR='WHITE', BACKCOLOR=RGB(151 43 153),$
TYPE=FOOTING, COLOR='WHITE', BACKCOLOR=RGB(151 43 153),$
TYPE=SUBTOTAL, COLOR=WHITE, BACKCOLOR=RGB(179 72 180),$
TYPE=SUBTOTAL, BY=2, BACKCOLOR=RGB(208 99 208),$
TYPE=SUBTOTAL, BY=3, BACKCOLOR=RGB(237 127 236),$
TYPE=GRANDTOTAL, COLOR='WHITE', BACKCOLOR=RGB(151 43 153), STYLE=BOLD,$
ENDSTYLE
END

The initial output shows only the top level BY field (REGION), as shown in the following image.

Clicking the arrow next to the Midwest region opens the rows that show the states associated
with that region, as shown in the following image.

Creating Reports With TIBCO® WebFOCUS Language

 1003

Controlling the Display of Sorted Data With Accordion Reports

Clicking the right arrow next to the state IL opens the rows that show the categories
associated with that state, as shown in the following image.

Clicking the right arrow next to the Coffee category shows the products associated with that
category, as shown in the following image. This is the lowest level of the Accordion By Row
report.

You can use the CONTROLCOLOR StyleSheet attribute on the SUBTOTAL line to specify the
color of the arrows. The following syntax shows how to change the color of the arrows to
purple.

1004

11. Navigating Within an HTML Report

TABLE FILE GGSALES
SUM DOLLARS/D8MC
UNITS/D8C
BUDDOLLARS/D8MC BUDUNITS/D8C
BY REGION
BY ST
BY CATEGORY
BY PRODUCT
ON TABLE SET EXPANDBYROWTREE ON
ON TABLE SET DROPBLNKLINE ON
ON TABLE SET AUTOFIT ON
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET STYLE *
TYPE=REPORT, EBRT_ANCHOR=ARROWS,
COLOR=RGB(66 70 73), FONT='TREBUCHET MS', SIZE=9, SQUEEZE=ON,$
TYPE=REPORT, FONT='TREBUCHET MS', COLOR=RGB(151 43 153),$
TYPE=TITLE, COLOR='WHITE', BACKCOLOR=RGB(151 43 153), STYLE=-UNDERLINE,$
TYPE=HEADING, COLOR='WHITE', BACKCOLOR=RGB(151 43 153),$
TYPE=FOOTING, COLOR='WHITE', BACKCOLOR=RGB(151 43 153),$
TYPE=SUBTOTAL, COLOR=WHITE, BACKCOLOR=RGB(179 72 180), CONTROLCOLOR=PURPLE,$
TYPE=SUBTOTAL, BY=2, BACKCOLOR=RGB(208 99 208),$
TYPE=SUBTOTAL, BY=3, BACKCOLOR=RGB(237 127 236),$
TYPE=GRANDTOTAL, COLOR='WHITE', BACKCOLOR=RGB(151 43 153), STYLE=BOLD,$
ENDSTYLE
END

The following output shows the lowest level of the Accordion By Row report, with purple arrows.

Reference: Usage Notes for EXPANDBYROW and EXPANDBYROWTREE

As of Release 8.2 Version 04, grids are supported with EXPANDBYROWTREE.

The maximum length of a BY field value is 245 bytes.

Creating Reports With TIBCO® WebFOCUS Language

 1005

Controlling the Display of Sorted Data With Accordion Reports

EXPANDBYROWTREE is not supported with OLAP. When both OLAP and
EXPANDBYROWTREE are enabled, EXPANDBYROWTREE will be ignored. As a workaround,
use EXPANDBYROW.

EXPANDBYROWTREE is not supported with the AHTML output format. When using
EXPANDBYROWTREE with an active report, EXPANDBYROWTREE will be ignored.

When running an accordion summary report against a SQL Server Analysis Services (SSAS)
cube data source, the PRINT command is used internally to retrieve the data, so that the
report output displayed will be that of a detailed report, instead of a summary report. This
is because the SSAS cube data source contains pre-aggregated data, and therefore SUM
commands are internally changed to PRINT commands.

Accordion By Row Tooltips

By default, EXPANDBYROW and EXPANDBYROWTREE reports display field information in
tooltips activated when you hover the mouse over the values at each level of the tree. Since
the column titles are not displayed above the tree control columns, as they would be in a
standard HTML report, the field list for the tree is presented in the tooltip in the top-left corner
of the report.

Pop-up field descriptions can also be enabled in Accordion By Row reports to present the field
descriptions maintained within the Master File or DEFINE associated with the fields.

Titles can be customized by defining an AS name. To remove pop-up field descriptions from the
expanding tree, define a blank AS name for the column title. In an Accordion By Row report,
pop-up text boxes that display on mouse over present additional information about the fields
and columns within the report. In standard Accordion reports, these pop-up text boxes display
the column title or AS name for all of the BY values in the expandable tree.

As with standard HTML reports, the POPUPDESC parameter can be set ON to display field
descriptions in these pop-up text boxes for all verb columns. Additionally, turning POPUPDESC
ON will cause the BY field pop-up text to present the description value, if available.

The table below represents the order of precedence for descriptions displayed in tooltips when
the EXPANDBYROW or EXPANDBYROWTREE setting is on.

Existing Field Information

Pop-Up Description Off

Pop-Up Description On

Description

AS Name

1

1

2

1006


11. Navigating Within an HTML Report

Existing Field Information

Pop-Up Description Off

Pop-Up Description On

Column Title

Field Name

2

3

3

4

The color and size presentation of the tooltips and pop-up descriptions have been standardized
for a uniform look throughout all reports.

Example:

Creating an Accordion By Row Report Without Pop-Up Field Descriptions

The following example demonstrates how pop-up text will display for the standard Accordion
report in the default presentation, which means pop-up descriptions are not turned on.

Creating Reports With TIBCO® WebFOCUS Language

 1007

Controlling the Display of Sorted Data With Accordion Reports

DEFINE FILE GGSALES.
UNITS/D12C DESCRIPTION ''=UNITS;
TOTSALES/D12CM DESCRIPTION 'DOLLARS*UNITS'=DOLLARS*UNITS;
END
TABLE FILE GGSALES
SUM DOLLARS UNITS AS 'Units'
TOTSALES AS 'Total Sales'
BY REGION
BY CATEGORY AS ''
BY PRODUCT AS 'Product AS Name'
ON TABLE SET EXPANDBYROW ALL
ON TABLE SET DROPBLNKLINE ALL
ON TABLE SET STYLE *
TYPE=REPORT,
    COLOR=RGB(66 70 73),
    FONT='TREBUCHET MS',
    SIZE=9,
    SQUEEZE=ON,
    GRID=OFF,
$
TYPE=TITLE,
    BACKCOLOR=RGB(102 102 102),
    COLOR=RGB(255 255 255),
    STYLE=-UNDERLINE+BOLD,
$
TYPE=DATA,
    BACKCOLOR=RGB(255 255 255),
$
TYPE=SUBTOTAL,
    BACKCOLOR=RGB(200 200 200),
    STYLE=BOLD,
 $
TYPE=GRANDTOTAL,
    BACKCOLOR=RGB(66 70 73),
    COLOR=RGB(255 255 255),
    STYLE=BOLD,
$
ENDSTYLE
END

Fields as defined in the Master File:

FIELD=CATEGORY, ALIAS=E02, FORMAT=A11, INDEX=I, TITLE='Category',
   DESC='Product category',$
FIELD=PRODUCT, ALIAS=E04, FORMAT=A16, TITLE='Product', DESC='Product name',$
 FIELD=REGION, ALIAS=E05, FORMAT=A11, INDEX=I, TITLE='Region',
   DESC='Region code',$
FIELD=UNITS, ALIAS=E10, FORMAT=I08, TITLE='Unit Sales',
   DESC='Number of units sold',$

1008

11. Navigating Within an HTML Report

The following image shows the pop-up description for the tree control, located at the top-left
corner of the table, displaying the list of column titles or AS name for the given BY column
within the underlying tree control.

The following image shows the pop-up text that will display when the mouse hovers over any of
the top level BY values that do not have an AS name, but do have a defined description and
title. In this case, the column titles will display.

The pop-up text for a top level BY value that has an AS name and a defined description will
display the AS name.

Example:

Creating an Accordion By Row Report With Pop-Up Field Descriptions

The following example demonstrates how pop-up text displays with pop-up descriptions turned
on.

Creating Reports With TIBCO® WebFOCUS Language

 1009

Controlling the Display of Sorted Data With Accordion Reports

SET POPUPDESC = ON
DEFINE FILE GGSALES.
UNITS/D12C DESCRIPTION ''=UNITS;
TOTSALES/D12CM DESCRIPTION 'DOLLARS*UNITS'=DOLLARS*UNITS;
END
TABLE FILE GGSALES
SUM DOLLARS UNITS AS 'Units'
TOTSALES AS 'Total Sales'
BY REGION
BY CATEGORY AS ''
BY PRODUCT AS 'Product AS Name'
ON TABLE SET EXPANDBYROW ALL
ON TABLE SET DROPBLNKLINE ALL
ON TABLE SET STYLE *
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/javaassist/intl/EN/ENIADefault_combine.sty,$
ENDSTYLE
END

As with all HTML reports, setting POPUPDESC=ON will activate a text box that displays the field
descriptions for each of the verb column titles.

Additionally, with POPUPDESC set ON, the field description will be presented for the BY
elements within the tree. If no field description is defined, the column title or AS name will
display.

With POPUPDESC=ON, the defined description will display in the pop-up text, as shown in the
following image.

The image that shows the description for the BY value appears in the pop-up text even though
an AS name has been given to this field.

1010

11. Navigating Within an HTML Report

For additional information on pop-up field descriptions with HTML reports, see Displaying
Report Data on page 39.

Accordion By Row With NOPRINT

Hidden, NOPRINT BY fields, can be used in Accordion by Row reports. They allow the
calculation of values for, and the sorting of data by, fields which are hidden. NOPRINT sort
fields are included in the internal matrix and affect the sorting and aggregation of data in the
Accordion report, even though they are not displayed in the report. These NOPRINT sort fields
are defined using the BY sortfield NOPRINT phrase.

Note:

Hidden or NOPRINT fields are not displayed in tooltips or pop-up descriptions.

When using empty or blank AS names, if spaces are added between the quotation marks,
for example, BY fieldname ' ', the spaces will be removed and the functionality will be the
same as BY fieldname ''.

Example:

Creating an Accordion By Row Report With an Explicit NOPRINT

The following request against the EMPLOYEE data source shows salary data for employees,
grouped in categories. The output is sorted by the virtual field NAME_SORT, which
concatenates the LAST_NAME and FIRST_NAME fields. The NAME_SORT field is hidden using
NOPRINT on the sort phrase. To display employee names, the NAME_DISPLAY virtual field is
created, which concatenates the FIRST_NAME field and the LAST_NAME field.

Creating Reports With TIBCO® WebFOCUS Language

 1011

Controlling the Display of Sorted Data With Accordion Reports

DEFINE FILE EMPLOYEE
NAME_SORT/A50=EMPLOYEE.EMPINFO.LAST_NAME || ( ', ' |
EMPLOYEE.EMPINFO.FIRST_NAME );
NAME_DISPLAY/A57=EMPLOYEE.EMPINFO.FIRST_NAME | EMPLOYEE.EMPINFO.LAST_NAME;
NAME_CODE/A1=EDIT(LAST_NAME, '9');
NAME_GROUP/A10=IF NAME_CODE LE 'G' THEN 'A-G' ELSE IF NAME_CODE LE 'P'
 THEN 'H-P' ELSE 'Q-Z';
END
TABLE FILE EMPLOYEE
SUM
EMPLOYEE.EMPINFO.CURR_SAL AS 'Current Salary'
BY NAME_GROUP AS 'Alphabetical Group'
BY LOWEST NAME_SORT NOPRINT
BY LOWEST NAME_DISPLAY AS 'Employee Name'
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE SET EXPANDBYROW 2
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET DROPBLNKLINE ON
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
TYPE=REPORT,
    COLOR=RGB(66 70 73),
    FONT='TREBUCHET MS',
    SIZE=9,
    SQUEEZE=ON,
    GRID=OFF,
$

1012

11. Navigating Within an HTML Report

TYPE=TITLE,
    BACKCOLOR=RGB(102 102 102),
    COLOR=RGB(255 255 255),
    STYLE=-UNDERLINE+BOLD,
$
TYPE=DATA,
    BACKCOLOR=RGB(255 255 255),
$
TYPE=SUBTOTAL
    BY=1,
    BACKCOLOR=RGB(200 200 200),
    STYLE=BOLD,
$
TYPE=SUBTOTAL,
    BY=2,
    BACKCOLOR=RGB(200 220 220),
    STYLE=BOLD,
$
TYPE=SUBTOTAL,
    BY=3,
    BACKCOLOR=RGB(220 220 200),
    STYLE=BOLD,
$
TYPE=GRANDTOTAL,
    BACKCOLOR=RGB(66 70 73),
    COLOR=RGB(255 255 255),
    STYLE=BOLD,
$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1013

Controlling the Display of Sorted Data With Accordion Reports

If you hover the mouse over any value in the NAME_DISPLAY column, the tooltip will display the
AS name, Employee Name, as shown in the following image.

Differences Between Reformatted and Redefined BY Fields

When a sort field is dynamically reformatted, both the original and reformatted fields are
placed in the internal matrix. The original field is not displayed, but is used to sort or aggregate
values.

When using a redefined field, the new column is used to display, sort, or aggregate values.

Example:

Creating an Accordion By Row Report With Dynamically Reformatted BY Fields

The following request against the EMPLOYEE data source shows employees and salaries by
year of hire. The display fields, HIRE_DATE and CURR_SAL, are sorted by HIRE_DATE
reformatted with the format, YY, and by the virtual field NAME_DISPLAY (employee name).

1014

11. Navigating Within an HTML Report

DEFINE FILE EMPLOYEE
NAME_SORT/A50=EMPLOYEE.EMPINFO.LAST_NAME || ( ', ' |
 EMPLOYEE.EMPINFO.FIRST_NAME ); NAME_DISPLAY/
A57=EMPLOYEE.EMPINFO.FIRST_NAME | EMPLOYEE.EMPINFO.LAST_NAME;NAME_CODE/
A1=EDIT(LAST_NAME, '9'); NAME_GROUP/A10=IF NAME_CODE LE 'G'
 THEN 'A-G' ELSE IF NAME_CODE LE  'P' THEN 'H-P' ELSE 'Q-Z';
END
TABLE FILE EMPLOYEE
SUM
HIRE_DATE
EMPLOYEE.EMPINFO.CURR_SAL
BY HIRE_DATE/YY
BY LOWEST NAME_DISPLAY AS 'Employee Name'
ON TABLE SET PAGE-NUM NOLEAD
WHERE HIRE_DATE LT '820101';
ON TABLE SET EXPANDBYROW ALL
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET DROPBLNKLINE ON
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/javaassist/intl/EN/ENIADefault_combine.sty,$
ENDSTYLE
END

In the report generated, there are multiple expandable groups or nodes for the same year,
1981. This occurs because the reformatted values are used for display, but the original values
are still used for sorting and aggregating. In this report, 1981 is the common value used to
represent two different dates, 81/07/01 and 81/11/02. The sorting takes place on the date,
not on the year.

Example:

Creating an Accordion By Row Report With Redefined BY Fields

To sort your data on the reformatted field values instead of the original field values, create a
virtual field containing the BY value with the new format applied. This will allow you to display,
sort, and aggregate on the new redefined BY value.

Creating Reports With TIBCO® WebFOCUS Language

 1015

Controlling the Display of Sorted Data With Accordion Reports

DEFINE FILE EMPLOYEE
NAME_SORT/A50=EMPLOYEE.EMPINFO.LAST_NAME || ( ', ' |
EMPLOYEE.EMPINFO.FIRST_NAME );
NAME_DISPLAY/A57=EMPLOYEE.EMPINFO.FIRST_NAME | EMPLOYEE.EMPINFO.LAST_NAME;
NAME_CODE/A1=EDIT(LAST_NAME, '9');
NAME_GROUP/A10=IF NAME_CODE LE 'G' THEN 'A-G' ELSE IF NAME_CODE LE 'P'
 THEN 'H-P' ELSE 'Q-Z';
DATE_HIRED/YY=HIRE_DATE;
END
TABLE FILE EMPLOYEE
SUM EMPLOYEE.EMPINFO.CURR_SAL
BY DATE_HIRED
BY LOWEST NAME_DISPLAY AS 'Employee Name'
ON TABLE SET PAGE-NUM NOLEAD
WHERE HIRE_DATE LT '820101';
ON TABLE SET EXPANDBYROW ALL
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET DROPBLNKLINE ON
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/javaassist/intl/EN/ENIADefault_combine.sty,$
ENDSTYLE
END

In the above request, the verb fields, HIRE_DATE and CURR_SAL are sorted by the DEFINE
field, DATE_HIRED. The result is a report sorted and aggregated by the redefined date values,
as shown in the following image.

Reference: Usage for SET EXPANDBYROW and EXPANDBYROWTREE

The following features are not supported with Accordion By Row reports:

HFREEZE

HTML Table of Contents

On Demand Paging

1016

11. Navigating Within an HTML Report

TABLEF

OVER

ROW-TOTAL

ON field RECAP

FOR

IN

SEQUENCE

PAGENUM

SUBHEAD

BORDER

MULTILINES

BY HIERARCHY

Compound Reports

Multiple requests in a single HTML report

In certain scenarios, a blank line is generated before a subtotal on the report output. You can
eliminate these automatic blank lines by issuing the SET DROPBLNKLINE=ON command.

Creating an Accordion By Column Report

Accordion By Column reports do not automatically display entire report rows. A plus sign
appears to the left of each data value in the column under the highest-level sort heading. For
data associated with lower-level sort fields, a plus sign is placed to the left of each data value,
but the data does not appear unless manually expanded. Data values of the lowest-level sort
field are not expandable. To expand your view of data for any expandable sort field, click a plus
sign and all data associated with the next lower-level sort field appears. When you expand a
data value under the next to lowest sort heading, all of the remaining associated data values
in the report appear. This type of Accordion Report is generated using the SET EXPANDABLE
command.

Reference: Support for Accordion By Column Reports

The following commands are not supported when using Accordion Reports:

BORDER, COLUMN, FOR, IN, OVER, PAGE-NUM, ROW-TOTAL, TOTAL

Creating Reports With TIBCO® WebFOCUS Language

 1017

Controlling the Display of Sorted Data With Accordion Reports

Data Visualization, HTML BYTOC, OLAP, On Demand Paging (WebFOCUS Viewer), column
freezing, and the ReportCaster burst feature are also not supported with Accordion Reports.

Syntax:

How to Create Accordion by Column Reports

To enable Accordion By Column Reports, specify the following

ON TABLE SET EXPANDABLE = {ON|OFF}

where:

ON

OFF

Enables Accordion By Column Reports.

Disables Accordion By Column Reports. OFF is the default value.

Example:

Creating an Accordion By Column Report

This example shows how to use an EXPANDABLE command to create an Accordion By Column
Report.

TABLE FILE GGSALES
SUM UNITS DOLLARS
BY REGION BY ST BY CITY BY CATEGORY
ON TABLE SET EXPANDABLE ON
END

1018

11. Navigating Within an HTML Report

The following image shows an Accordion by Column Report which displays all data associated
with the first-level sort field, Region, by default. The expanded data values you see are the
result of a report user clicking plus signs to the left of specific first, second- and third-level sort
fields after the report is generated.

Navigating a Multi-Page Report With the WebFOCUS Viewer

Normally, a web server returns an entire HTML report to a browser, which waits for all of the
report before displaying it. On-demand paging, implemented in the WebFOCUS Viewer, returns
one page of a report to a browser instead of the entire report. The web server holds the
remaining pages until the user requests them. This feature shortens the time the user waits to
see the first page and is especially useful for long reports. It also contains navigational
features that enable you to move quickly among the pages of the report.

The WebFOCUS Viewer does not support the table of contents (BYTOC) option because the
table of contents option requires all of the data to be on the same HTML page, even though it
then filters and only exposes part of the page at a time. The WebFOCUS Viewer splits the
output into many pages, only one of which is downloaded to the browser at a time. Accordion
reports are also not supported with the WebFOCUS Viewer.

Note that you can use the HFREEZE StyleSheet option to display column titles on every page of
output returned by the WebFOCUS Viewer.

Creating Reports With TIBCO® WebFOCUS Language

 1019

Navigating a Multi-Page Report With the WebFOCUS Viewer

The following is page 1 of a 31-page report displayed in the WebFOCUS Viewer.

Notice that the WebFOCUS Viewer is divided into two frames:

The Report Frame is the larger upper frame that contains one page of a report.

The Control Frame contains the controls used to navigate the report and to search for a
string in the report. The navigational controls allow you to display the next or previous page,
the first or last page, or a specific page.

Note: You can control whether certain buttons display using SET commands. For more
information, see Controlling Button Display on the WebFOCUS Viewer in the Developing
Reporting Applications manual.

Reference: Usage Notes for HTMLARCHIVE With the WebFOCUS Viewer

WebFOCUS interactive reporting features must have a connection to the WebFOCUS client in
order to access the components required to operate successfully.

HTMLARCHVE can be used to create self-contained HTML pages with user-defined images
when client access is not available.

1020

11. Navigating Within an HTML Report

To generate HTML pages containing user-defined images that can operate interactively, use
one of the following commands:

SET HTMLEMBEDIMG=ON
SET HTMLARCHIVE=ON

Define BASEURL to point directly to the host machine where these files can be accessed using
the following syntax:

SET BASEURL=http://{hostname:portnumber}

For more information on SET BASEURL, see Specifying a Base URL on page 872.

Procedure: How to Navigate in the WebFOCUS Viewer

The WebFOCUS Viewer Control Panel offers several ways to view pages in your report:

To display the previous or the next page in sequence, click the Previous or Next arrow.

To display the first or last page of the report, click the First Page or the Last Page arrow.

To display a specific page:

1. Enter a page number in the page input box.

2. Click the Go to Page button.

To download the entire report as a single document, click the All Pages button. The
WebFOCUS Viewer displays the entire report without the Viewer Control Panel.

You can return to viewing a single page of your report by clicking the Back button on the
browser toolbar.

To locate a text string, enter the text in the input box and click the Find button.

To limit your search by case, toggle the A=a button.

To control the direction of your search, toggle the -->/<-- button.

Using the WebFOCUS Viewer Search Option

The Viewer Control Panel contains controls that offer several ways to search your report. Using
the Viewer search controls, you can select a string of information, such as a phrase that
occurs in your report or a group of numbers, and search for each occurrence of that string. You
can further customize your search by matching capitalization of words exactly (a case-sensitive
search) or by controlling the direction of your search (either forward or backward from your
starting point in the report).

Creating Reports With TIBCO® WebFOCUS Language

 1021

Linking Report Pages

When using the Search option:

1. The first search starts at top of the document.

2. The second and subsequent searches start from the last successfully found search string
in the direction selected in the Viewer Control Panel. Note that the direction control is to
the right of the Search entry field used to specify a search string.

Linking Report Pages

With a StyleSheet, you can insert one or more navigational hyperlinks in a multi-page HTML
report. This feature makes it easy for you to link consecutive report pages together without
creating individual hyperlinks for each page.

You can define any report component as a hyperlink.

Syntax:

How to Link Report Pages

Use the following syntax in an HTML report

URL=#_destination, $

where:

destination

Is one of the following:

#_next goes to the top of the next report page.

#_previous goes to the top of the previous report page.

#_top goes to the top of the current report page.

#_start goes to the first page of the report.

#_end goes to the last page of the report.

Note: In order to use these destinations in a self service applications, the following
command must be issued at the beginning of the FOCEXEC:

SET BASEURL=''

Example:

Linking Report Pages Through Images in a Heading

This request displays two images in the page heading of a long report. It creates a link
between BULLET.GIF and the next page of the report, and GOBACK.GIF and the previous page
of the report.

1022

11. Navigating Within an HTML Report

TABLE FILE GGORDER
ON TABLE SUBHEAD
"COFFEE GRINDER SALES BY STORE"
" "
HEADING
"Next page or previous page."
PRINT QUANTITY AS 'Ordered Units' BY STORE_CODE BY PRODUCT NOPRINT
BY ORDER_NUMBER
WHERE PRODUCT EQ 'Coffee Grinder'
ON STORE_CODE PAGE-BREAK
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=TABHEADING, STYLE=BOLD,$
TYPE=HEADING, IMAGE=/IBI_APPS/IBI_HTML/GGDEMO/BULLET, URL=#_next,
IMAGEALIGN=LEFT,$
TYPE=HEADING, IMAGE=/IBI_APPs/IBI_HTML/GGDEMO/GOBACK, URL=#_previous,
IMAGEALIGN=RIGHT,$
ENDSTYLE
END

The images display in each page heading.

Creating Reports With TIBCO® WebFOCUS Language

 1023

Linking Report Pages

Click the image on the left of page 1 to display page 2.

1024

Click the "go back" image on page 2 to redisplay page 1.

11. Navigating Within an HTML Report

For details on including and positioning images in a report, see Laying Out the Report Page on
page 1331.

Note that if this procedure is part of a self-service application, the following command must be
issued at the start of the procedure:

SET BASEURL = ''

Example:

Linking Pages Through Page Number and Heading Elements

This request creates hyperlinks from the page number to the next page in the report, and from
the text of the page heading, which appears at the top of every report page, back to the
previous page or to the first page.

Creating Reports With TIBCO® WebFOCUS Language

 1025

Linking Report Pages

TABLE FILE GGORDER
ON TABLE SUBHEAD
"COFFEE GRINDER SALES BY STORE"
" "
HEADING
"return to previous page"
"return to beginning"
PRINT QUANTITY AS 'Ordered Units' BY STORE_CODE BY PRODUCT NOPRINT
BY ORDER_NUMBER
WHERE PRODUCT EQ 'Coffee Grinder'
ON STORE_CODE PAGE-BREAK
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=TABHEADING, STYLE=BOLD,$
TYPE=PAGENUM, URL=#_next, $
TYPE=HEADING, LINE=1, URL=#_previous, $
TYPE=HEADING, LINE=2, URL=#_start, $
ENDSTYLE
END

The first page looks as follows:

1026

Click the page number three times to move to PAGE 4.

11. Navigating Within an HTML Report

Click previous page to return to PAGE 3. Click return to beginning to go directly to PAGE 1.

Note that if this procedure is part of a self-service application, the following command must be
issued at the start of the procedure:

SET BASEURL = ''

Creating Reports With TIBCO® WebFOCUS Language

 1027

Linking Report Pages

1028

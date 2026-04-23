Chapter10

Linking a Report to Other Resources

You can use StyleSheet declarations to define links from any report component. You can
use links to:

Create a series of drill-down reports by linking the procedures that generate these
reports.

Link to URLs. These can be other webpages, websites, Servlet programs, or non-
World Wide Web resources, such as an email application.

Execute JavaScript functions to perform additional analysis of the report data.

You can create links from report data as well as graphical images within a report. You
can also create links from a graph. For details on linking from a graph, see Creating a
Graph on page 1743.

In this chapter:

Linking Using StyleSheets

Creating Parameters

Linking to Another Report

Linking With Conditions

Linking to a URL

Linking From a Graphic Image

Linking to a JavaScript Function

Specifying a Base URL

Linking to a Maintain Data Procedure

Specifying a Target Frame

Multi-Drill Feature With Cascading Menus
and User-Defined Styling

Creating a Compound Report

Creating a PDF Compound Report With
Drill Through Links

Linking Using StyleSheets

You can use StyleSheets to define a link from any report component. You can create links from
report data (including headings and footings) as well as graphic images (such as a company
logo or product image), to other reports, procedures, URLs, or JavaScript functions.

Creating Reports With TIBCO® WebFOCUS Language

 819

Linking to Another Report

The links you create can be dynamic. With a dynamic link, your selection passes the value of
the selected report component to the linked report (procedure, URL, or JavaScript function).
The resource uses the passed value to dynamically determine the results that are returned.
You can pass one or more parameters. For details, see Creating Parameters on page 854.

Procedure: How to Create Links Using StyleSheets

This procedure is a basic overview of how to create links using StyleSheets.

1.

Identify the report component that the user selects in the web browser to execute the link.

2. Specify the name of the embedded procedure, URL, or JavaScript function to execute.

3.

Identify the parameters that define the specifics of your link, if necessary.

Linking to Another Report

A link allows you to drill down to a report for more details or execute a procedure by selecting a
designated hot spot (the link) in the report. By linking reports you provide easy access to more
detailed data that supplements the information in your base report. The drill-down report can
contain information that is either independent of the data in the base report or depends and
expands on a specific data value in the base report.

To create a link, you must have a report to link from (the base report) and a report to link to
(the drill-down report). If the drill-down report depends on a specific data value in the base
report, you also need to pass that value to the drill-down report by creating parameters. For
details, see Creating Parameters on page 854.

Syntax:

How to Link to Reports and Procedures

TYPE=type, [subtype], FOCEXEC=fex[(parameters ...)], [TARGET=frame,]
[ALT = 'description',] $

where:

type

Identifies the report component that you select in the web browser to execute the link.
The TYPE attribute and its value must appear at the beginning of the declaration.

subtype

Are any additional attributes, such as COLUMN, LINE, or ITEM, that are needed to
identify the report component that you are formatting. For information on identifying
report components, see Identifying a Report Component in a WebFOCUS StyleSheet on
page 1249.

820

10. Linking a Report to Other Resources

fex

Identifies the file name of the linked procedure to run when you select the report
component.

Note: The procedure cannot be named NONE (all uppercase). Using NONE as the
procedure name will result in a syntax error. Mixed or lowercase is allowed.

To determine the file name in WebFOCUS, see How to Determine a WebFOCUS File Name
on page 822.

The maximum length of a FOCEXEC=fex argument, including any associated parameters, is
2400 characters. The FOCEXEC argument can span more than one line, as described in
Creating and Managing a WebFOCUS StyleSheet on page 1197.

parameters

Values that are passed to the report, URL, or JavaScript function. For details, see
Creating Parameters on page 854.

frame

Identifies the target frame in the webpage in which the output from the drill-down link
is displayed. For details, see Specifying a Target Frame on page 873.

description

Is a textual description of the link supported in an HTML report for compliance with
Section 508 accessibility. Enclose the description in single quotation marks.

The description also displays as a pop-up description when your mouse or cursor hovers
over the link in the report output.

Reference: Usage Notes for Drilldown Reports in PDF Format

When going back to the original report from a drilldown report in PDF format, you must click the
Back button twice quickly. The alternative is to use the drop-down list presented to the right of
the Back button to view the browser history and select the link two steps back. The first history
item will point to the redirection page and be titled based on the method used to access the
WFServlet. The previous item will be titled WebFOCUS Report and will point back to the original
PDF report.

Creating Reports With TIBCO® WebFOCUS Language

 821

Linking to Another Report

Procedure: How to Determine a WebFOCUS File Name

1. Right-click the report name and select Properties. The Report Properties dialog box opens.

2. The file name appears under Name. In the example below, the name of the file is

"salesrep". Do not include the file extension (.fex) or the directory location and slash (/).

Example:

Linking to a Report From a Footing

The following report request summarizes product sales and sorts the data by region, state,
and store code. The store code also displays in the subfootings where links to detailed reports
about the store's sales (by product or by date) display. Each line of the subfoot contains two
text objects and one embedded field. The relevant StyleSheet declarations are highlighted in
the request.

822

10. Linking a Report to Other Resources

The main report is:

TABLE FILE GGSALES
HEADING
"Sales Report"
SUM DOLLARS/I08M
BY REGION BY ST BY STCD
ON STCD SUBFOOT
"View Store <STCD Sales By Product"
" "
"View Store <STCD Sales By Date"
ON REGION PAGE-BREAK
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=HEADING, SIZE=12, STYLE=BOLD, $
TYPE=SUBFOOT, LINE=1, OBJECT=TEXT, ITEM=2, COLOR=GREEN,
     FOCEXEC=PRDSALES(STOREID=STCD), $
TYPE=SUBFOOT, LINE=3, OBJECT=TEXT, ITEM=2, COLOR=BLUE,
     FOCEXEC=HSTSALES(STOREID=STCD), $
ENDSTYLE
END

Using StyleSheet declarations, the subfoot phrase Sales By Product links to a second
procedure named PRDSALES and passes it the value of STCD displayed in the subfoot. The
subfoot phrase Sales By Date links to a procedure named HSTSALES and passes it the value
of STCD displayed in the subfoot.

The request for the linked report HSTSALES is:

TABLE FILE GGSALES
SUM UNITS
BY STCD
BY DATE
WHERE STCD = '&STOREID'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The request for the linked report PRDSALES is:

TABLE FILE GGSALES
SUM UNITS
BY STCD
BY PRODUCT
WHERE STCD = '&STOREID'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 823

Linking to Another Report

The first page of output for the main report follows. If you select Sales By Product for Store
R1020, the value R1020 is passed to the PRDSALES procedure. If you select Sales By Date for
Store R1019, the value R1019 is passed to the HSTSALES procedure.

The output is:

If you click the Sales By Product link for store R1020, the output is:

Store ID

Product

Unit Sales

R1020

Biscotti

     29413

Coffee Grinder

     19339

Coffee Pot

     15785

Croissant

     43300

Espresso

     32237

Latte

Mug

Scone

Thermos

     77344

     30157

     45355

     14651

824

10. Linking a Report to Other Resources

Linking to a URL

You can define a link from any report component to any URL including webpages, websites,
Servlet programs, or non-World Wide Web resources, such as an email application. After you
have defined a link, you can select the report component to access the URL.

The links you create can be dynamic. With a dynamic link, your selection passes the value of
the selected report component to the URL. The resource uses the passed value to dynamically
determine the results that are returned. You can pass one or more parameters. For details,
see Creating Parameters on page 854.

Syntax:

How to Link to a URL

TYPE=type, [subtype], URL=url[(parameters ...)], [TARGET=frame,] [ALT =
'description',] $

where:

type

Identifies the report component that you select in the web browser to execute the link.
The TYPE attribute and its value must appear at the beginning of the declaration.

subtype

Are any additional attributes, such as COLUMN, LINE, or ITEM, that are needed to
identify the report component that you are formatting. For information on identifying
report components, see Identifying a Report Component in a WebFOCUS StyleSheet on
page 1249.

url

Identifies any valid URL, including a URL that specifies a WebFOCUS Servlet program,
or the name of a report column enclosed in parentheses whose value is a valid URL to
which the link will jump.

Note:

The maximum length of a URL=url argument, including any associated variable=object
parameters, is limited by the maximum number of characters allowed by the browser.
For information about this limit for your browser, search on your browser vendor's
support site. The URL argument can span more than one line, as described in Creating
and Managing a WebFOCUS StyleSheet on page 1197.

Note that the length of the URL is limited by the maximum number of characters
allowed by the browser. For information about this limit for your browser, search on your
browser vendor’s support site.

Creating Reports With TIBCO® WebFOCUS Language

 825

Linking to a URL

If the URL refers to a WebFOCUS Servlet program that takes parameters, the URL must
end with a question mark (?).

parameters

Values that are passed to the URL. For details, see Creating Parameters on page
854.

frame

Identifies the target frame in the webpage in which the output from the drill-down link
is displayed. For details, see Specifying a Target Frame on page 873.

description

Is a textual description of the link supported in an HTML report for compliance with
Section 508 accessibility. Enclose the description in single quotation marks.

The description also displays as a pop-up description when your mouse or cursor hovers
over the link in the report output.

Example:

Linking to a URL

The following example illustrates how to link to a URL from a report. The heading Click here to
access the IB homepage is linked to the URL www.ibi.com. The relevant StyleSheet declarations
are highlighted in the request.

Note that webserver indicates the name of the webserver that runs WebFOCUS.

TABLE FILE GGSALES
ON TABLE SET PAGE-NUM OFF
SUM UNITS AND DOLLARS
BY CATEGORY BY REGION
HEADING
"Regional Sales Report"
"Click here to access the IB homepage."
" "
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=HEADING, LINE=2, OBJECT=TEXT, ITEM=1,
   URL=http://www.ibi.com, $
ENDSTYLE
END

826

The output is:

10. Linking a Report to Other Resources

When you click the link the site displays in your browser.

Example:

Linking to a URL to Run a Drilldown WebFOCUS Server Procedure

The following request is initiated from a browser session and runs a drill down report stored on
the WebFOCUS Reporting Server.

This procedure is run from a browser, so the drilldown in the example is specified as a relative
URL (it does not have protocol, host, or port) because it will be submitted using the protocol,
host, and port of the current browser session.

Note: This technique is useful in a Managed Reporting procedure for creating a drill down to a
WebFOCUS Server procedure. The FOCEXEC= technique for running a drill down procedure
does not work because Managed Reporting always looks for the procedure in the Managed
Reporting repository.

Creating Reports With TIBCO® WebFOCUS Language

 827

Linking to a URL

The main procedure is:

TABLE FILE GGSALES
ON TABLE SET PAGE-NUM OFF
SUM UNITS AND DOLLARS
BY CATEGORY BY REGION
HEADING
"Regional Sales Report"
" "
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=DATA, COLUMN=REGION,
URL=/ibi_apps/WFServlet?(IBIF_ex='ggdrill' AREA=REGION
IBIC_server='EDASERVE' IBI_APPS='IBISAMP'),$
ENDSTYLE
END

The drilldown report, which must be in application ibisamp, is:

-DEFAULTS &REGION='$*';
TABLE FILE GGSALES
ON TABLE SET PAGE-NUM OFF
SUM UNITS AND DOLLARS
BY PRODUCT
WHERE REGION = '&AREA'
HEADING
"Sales Report for Region &AREA"
" "
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

828

The output of the main report is:

10. Linking a Report to Other Resources

Creating Reports With TIBCO® WebFOCUS Language

 829

Linking to a URL

If you click the region Northeast, the output is:

Reference: Usage Notes for Linking to a URL

Special characters that should be interpreted as text within a URL must be encoded. For
example, if you need to include a slash character (/) as text in the URL string, you must
use its encoded value, '%2F'. For example, to drill down on the title of a report to a URL,
such as passing 'A' with value '2009/03' to test.asp, the StyleSheet command should be:

TYPE=TITLE, URL=/test.asp?(A='2009%2F03'), $

Defining a Hyperlink Color

You can use the HYPERLINK-COLOR attribute to designate a color for a hyperlink within a
report. This applies to all hyperlinks generated in the report. You can define a single color for
the entire report or different colors for each individual element.

Syntax:

How to Define a Hyperlink Color

TYPE = type, HYPERLINK-COLOR = color

830

10. Linking a Report to Other Resources

where:

type

Is the report component you wish to affect. You can apply this keyword to the entire report
using TYPE=REPORT. The attribute can also individually be set for any other element of the
report. For details, see Identifying a Report Component in a WebFOCUS StyleSheet on page
1249.

color

Can use any style sheet supported color value designation. For available color values that
can be utilized with the syntax, see Color Values in a Report on page 1701.

Example:

Defining a Hyperlink Color

The following PDF request illustrates how to define hyperlink colors for the entire report, as
well as individual elements.

The default font color for the entire report is grey and the default hyperlink color for the
entire report is slate blue.

For the Dollar Sales column (DOLLARS), the font color is green and the hyperlink color is
purple.

For both the Dollar Sales column (DOLLARS) and the Unit Sales column (UNITS),
conditional styling has been applied using the same condition (REGION GE 'O').

For the Unit Sales column (UNITS), when the conditional styling is met, the hyperlink color
is inherited from the default hyperlink color for the report (slate blue).

For the Dollar Sales column (DOLLARS), when the conditional styling is met, the hyperlink
color is purple.

Creating Reports With TIBCO® WebFOCUS Language

 831

Linking to a URL

TABLE FILE GGSALES
SUM DOLLARS/D12CM UNITS/D12C
BY REGION
BY CATEGORY
HEADING
"Hyperlinks of Many Colors"
""
ON TABLE SET PAGE-NUM OFF
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, SQUEEZE=ON, FONT=ARIAL, GRID=OFF, COLOR=GREY,
  HYPERLINK-COLOR='SLATE BLUE',$
TYPE=DATA, COLUMN=UNITS, WHEN=REGION GE 'O', URL='http://www.ibi.com',$
TYPE=DATA, COLUMN=DOLLARS, COLOR=GREEN, HYPERLINK-COLOR='PURPLE',$
TYPE=DATA, COLUMN=DOLLARS, WHEN=REGION GE 'O', URL='http://www.ibi.com',$
ENDSTYLE
END

The output is:

Reference: Usage Notes for HYPERLINK-COLOR

By default, drill-down links are presented in hyperlink blue and underlined.

In HTML and DHTML reports, any designated report font color overrides the drill-down
default font color.

For standard reports, set the HYPERLINK-COLOR attribute using the TYPE=REPORT
declaration of the style sheet.

832

10. Linking a Report to Other Resources

For compound reports, set the HYPERLINK-COLOR attribute using the TYPE=REPORT
declaration of the style sheet of the first component report (excluding anything on the Page
Master).

For PPTX, the hyperlink color is stored as part of the PPTX Slide Master theme. Only one
HYPERLINK-COLOR attribute can be defined for each request (report/compound report).

Linking to a JavaScript Function

You can use a StyleSheet to define a link to a JavaScript function from any report component.
After you have defined the link, you can select the report component to execute the JavaScript
function.

Just as with drill-down links to procedures and URLs, you can specify optional parameters that
allow values of a report component to be passed to the JavaScript function. The function will
use the passed value to dynamically determine the results that are returned to the browser.
For details, see Creating Parameters on page 854.

Note:

JavaScript functions can, in turn, call other JavaScript functions.

You cannot specify a target frame if you are executing a JavaScript function. However, the
JavaScript function itself can specify a target frame for its results.

Syntax:

How to Link to a JavaScript Function

TYPE=type, [subtype], JAVASCRIPT=function[(parameters ...)], $

where:

type

Identifies the report component that you select in the web browser to execute the link.
The TYPE attribute and its value must appear at the beginning of the declaration.

subtype

Are any additional attributes, such as COLUMN, LINE, or ITEM, that are needed to
identify the report component that you are formatting. See Identifying a Report
Component in a WebFOCUS StyleSheet on page 1249 for details.

function

Identifies the JavaScript function to run when you select the report component.

Creating Reports With TIBCO® WebFOCUS Language

 833

Linking to a JavaScript Function

The maximum length of a JAVASCRIPT=function argument, including any associated
parameters, is 2400 characters and can span more than one line. If you split a single
argument across a line, you need to use the \ character at the end of the first line, as
continuation syntax. If you split an argument at a point where a space is required as a
delimiter, the space must be before the \ character or be the first character on the next
line. The \ character does not act as the delimiter.

In this example,

JAVASCRIPT=myfunc(COUNTRY \
CAR MODEL 'ABC'),$

the argument correctly spans two lines.

Note:

You can use the Dialogue Manager -HTMLFORM command to embed the report into an
HTML document in which the function is defined.

When you have an HTML document called by -HTMLFORM, ensure that the file
extension is .HTM (not .HTML).

For more information about the -HTMLFORM command, see the Developing Reporting
Applications manual.

parameters

Values that are passed to the JavaScript function. For details, see Creating
Parameters on page 854.

Example:

Linking to a JavaScript Function

The following displays the report and StyleSheet syntax used to link to a JavaScript function. It
also shows the JavaScript function that is executed, and the result that is displayed in the
browser.

The report request (which contains the inline StyleSheet) is:

834

10. Linking a Report to Other Resources

TABLE FILE GGORDER
SUM PRODUCT_ID
BY STORE_CODE
BY PRODUCT_DESCRIPTION NOPRINT
IF STORE_CODE EQ 'R1250'
ON TABLE HOLD AS JAVATEMP FORMAT HTMTABLE
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=DATA, COLUMN=PRODUCT_ID, JAVASCRIPT=showitem(PRODUCT),$
ENDSTYLE
END
-RUN
-HTMLFORM JAVAFORM

The JAVAFORM.HTM file that contains the JavaScript function is:

<HTML>
<HEAD>
<SCRIPT LANGUAGE="JavaScript">
// This function will display the value in the text box
function showitem(string) {
document.form1.text1.value = string;
}
// End the hiding here
</SCRIPT>
</HEAD>
<BODY>
!IBI.FIL.JAVATEMP;
<HR>
<B>Product Description:</B>
<FORM NAME="form1">
<INPUT TYPE="text" NAME="text1" SIZE="16"> </FORM>
</BODY>
</HTML>

Creating Reports With TIBCO® WebFOCUS Language

 835

Linking to a Maintain Data Procedure

When you execute the report procedure, the following report displays in the web browser. If you
select a Product Code link, the JavaScript function ShowItem executes, and displays the value
of the PRODUCT_DESCRIPTION field (a NOPRINT field) in the text box in the form below the
report. For example, if you select the Product Code G104, "Thermos" displays in the Product
Description field.

Linking to a Maintain Data Procedure

You can provide update capabilities directly from your report by linking it to a Maintain Data
procedure.

The link can be either a URL for the WebFOCUS Servlet or a JavaScript drilldown to the
Maintain Data procedure.

If it is a URL for the WebFOCUS Servlet, it must include the IBIF_cmd command with the
MNTCON RUN or MNTCON EX syntax to invoke an existing Maintain Data form procedure. The
link can pass control to a Maintain form, or run a batch mode Maintain procedure that does
not display a user interface.

836

10. Linking a Report to Other Resources

If it is a JavaScript drilldown, it uses the parent.IbComposer_drillMntdata function.

Syntax:

How to Link to a Maintain Data Procedure Using a URL

TYPE=type, [subtype, ] URL=/ibi_apps/WFServlet? IBIF_cmd='MNTCON
  {RUN|EX} procname' IBIS_passthru='on' IBIS_connect='on'
  [(parameters...)], $

where:

type

Identifies the report component that you select in the web browser to execute the link.
The TYPE attribute and its value must appear at the beginning of the declaration.

subtype

Are any additional attributes, such as COLUMN, LINE, or ITEM, that are needed to
identify the report component that you are formatting. See Identifying a Report
Component in a WebFOCUS StyleSheet on page 1249 for information on identifying
report components.

procname

Is the name of the Maintain Data procedure.

parameters

Values that are passed to the Maintain Data procedure. For details, see Creating
Parameters on page 854.

Example:

Linking to a Maintain Data Procedure

The following report allows you to update the unit price for a product directly from the report
output by linking the report to the appropriate Maintain procedure.

The report request is:

TABLE FILE GGPRODS
PRINT PRODUCT_DESCRIPTION VENDOR_CODE VENDOR_NAME UNIT_PRICE
BY PRODUCT_ID
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=DATA, COLUMN=N1,
    URL=/ibi_apps/WFServlet?(PRODUCT_ID=N1 IBIF_cmd='MNTCON RUN GGUPD1'
IBIS_passthru=\
     'on' IBIS_connect='on'), $
ENDSTYLE
END

The Maintain Data procedure (ggupd1) is:

Creating Reports With TIBCO® WebFOCUS Language

 837

Linking to a Maintain Data Procedure

MAINTAIN FILE ggprods
module import(mntuws FOCCOMP)
$$Declarations
Declare pcode/a4;
Case Top
compute timechk/a0=HHMMSS();
document.referer='/ibi_apps/WFServlet?IBIF_ex=ggprod&IBIS_connect
=on'||
'&timechk='|timechk;
compute pcode = IWC.getAppCGIValue("PRODUCT_ID");
Infer ggprods.prods01.product_id into ggstk1;
Reposition PRODUCT_ID
Stack clear ggstk1 ;
For all next ggprods.prods01.product_id into ggstk1
 where product_id eq pcode;
Winform Show Form1;
EndCase
Case Updte1
for all Update ggprods.prods01.unit_price from ggstk1(1) ;
EndCase
END

Note: This is an interactive form to display data and is created in App Studio.

The report is:

When you click a Product Code, the Maintain procedure ggupd1 is invoked, which uses the
IWC.getAppCGIValue function to retrieve the correct value.

838

10. Linking a Report to Other Resources

Form 1 in the Maintain Data procedure ggupd1 opens and you can update the unit price for
that product:

Syntax:

How to Link to a Maintain Data Procedure Using a JavaScript Drilldown

TYPE=DATA,
     DRILLMENUITEM='DrillDown 1',
          JAVASCRIPT=parent.IbComposer_drillMntdata( \
     'Request2' \
     'mntcase' \
     'stack_field' \
     rptcol \
     ),
          TARGET='_parent',
$

where:

'DrillDown 1'

Is the text that displays for the drilldown link.

'Request2'

Is the name of the Maintain Data procedure.

'mntcase'

Is the name of the Maintain case.

'stack_field'

Is the stack and stack field associated with the report column.

Creating Reports With TIBCO® WebFOCUS Language

 839

Linking to a Maintain Data Procedure

rptcol

Is the report column specification.

Note: Multiple stack fields and report columns can be specified to pass additional values
from the report to Maintain.

In the Maintain procedure, make sure the stack retrieving the values is created and the case
being performed exists.

The following is a sample drilldown from a report against the MOVIES data source to a
Maintain procedure. It passes the value from the first report column (N1) to the Moviecode
field in the Movstk stack in the the LoadData case of the Maintain procedure named
Request2.

TYPE=DATA,
     DRILLMENUITEM='DrillDown 1',
          JAVASCRIPT=parent.IbComposer_drillMntdata( \
     'Request2' \
     'LoadData' \
     'Movstk.Moviecode' \
     N1 \
     ),
          TARGET='_parent',
$

840

10. Linking a Report to Other Resources

The following is the Maintain code needed in order to pass these values from the report. The
Maintain procedure is named Request2.

Creating Reports With TIBCO® WebFOCUS Language

 841

Multi-Drill Feature With Cascading Menus and User-Defined Styling

When the report and the Maintain form are placed on the same HTML page, clicking one of the
links in the report passes the values to the Maintain form, as shown in the following image.

Multi-Drill Feature With Cascading Menus and User-Defined Styling

The multi-drill feature supports multiple menu items, as well as multiple cascading levels, that
you can incorporate into any WebFOCUS report that works with JavaScript (for example, HTML
and DHTML). Styling of the menu can be customized using WebFOCUS StyleSheet syntax.

The multi-drill feature for HTML and DHTML provides:

Flexible cascading menus.

Fully customizable styling at each element and level within the menu.

Menus intelligently positioned in relationship to the data elements selected.

For PDF, PS, PPT, PPTX, EXL2K, and XLSX formats, the first active link is used to create a
hyperlink on the designated location.

Accessibility Support

The multi-drill feature provides 508 accessibility support to the cascading multi-drill menus
available in HTML format.

In reports, for the multi-drill cascading menu options Auto Drill and Auto Link, accessibility
users should:

Turn the Virtual PC cursor setting mode off.

Use keystrokes to navigate to the link in the report.

842

10. Linking a Report to Other Resources

Open the cascading menu item and then press Enter to view the item.

Turn the Virtual PC cursor setting on to navigate through the report.

For more information, see TM4505: WebFOCUS HTML Report Accessibility Support.

Creating Multiple Drill-Down Links

You can customize the drill-down menu at two levels:

Global styling of all menus within the current procedure (fex).

Item level styling for each entry in the menu.

Global Menu Styling

To define styling attributes for all menus within the current procedure (fex):

TYPE=REPORT, OBJECT=MENU, [FONT=font], [SIZE=size], [COLOR=color],
[HOVER-COLOR=hover_color], [BACKCOLOR=backcolor],
[HOVER-BACKCOLOR=hover_backcolor], [BORDER={ON|OFF|n}],
[BORDER-COLOR=border_color], [BORDER-STYLE=border_style]
$

where:

font

Defines the font typeface for the menu item. The default is inherited from the report.

size

Defines the font size for the menu item. The default font size is 9.

color

Defines the text color for the menu item (named colors or RGB/HEX values). The default
text color for the menu item is RGB(#6B6B6B). Also used to define the color of the
SEPARATOR line and the control caret.

hover_color

Defines the text color for the hover over or select menu item (named colors or RGB/HEX
values). The default text color for hover over or select menu item is RGB(#495263).

backcolor

Defines the background color for the menu item (named colors or RGB/HEX values). The
default background color is RGB(#F8F8F8).

Creating Reports With TIBCO® WebFOCUS Language

 843

Multi-Drill Feature With Cascading Menus and User-Defined Styling

hover_backcolor

Defines the background color for hover over or select menu item (named colors or
RGB/HEX values). The default background color for hover over or select menu item is
RGB(#DFDFDF).

BORDER={ON|OFF|n}

where:

ON displays borders around the menu objects and as the separator lines, based on
user defined styling or system defaults.

OFF displays no border around the menu objects.

n is border weight in pixels (valid values 1, 2, 3, light, medium, heavy).

The default border weight is light.

border_color

Defines border coloring to be used for borders around the menu. This will also be used for
the color of the separator lines within the menu. Is one of the preset color values. The
default border color is RGB(#D6D6D6).

border_style

Defines line styles to be used for borders around the menu, as well as separator lines.
Possible values are listed in the following table. This will also be used for separator style
within the menu. The default border style is solid. Seeing the distinction in border style
may require using a heavier weight (for example, border=heavy, or border=3).

Style

NONE

SOLID

DOTTED

DASHED

DOUBLE

GROOVE

RIDGE

844

Description

No border/divider

Solid line

Dotted line

Dashed line

Double line

3D groove

3D ridge

10. Linking a Report to Other Resources

Style

INSET

OUTSET

Note:

Description

3D inset

3D outset

If a multi-drill menu is tagged with the DRILL-SOURCE attribute, it indicates that the menu
was generated by WebFOCUS and should be merged into the existing drilldowns added by
the user for the specified report element, if any. The value of the attribute indicates which
WebFOCUS feature generated the menu. This attribute is reserved for Information Builders
internal use only.

When you create multiple drill-down links, you cannot specify a single drill-down action (for
example, FOCEXEC or URL) before the first DRILLMENUITEM.

Menu Items Styling

The syntax for cascading menus is an extension of the existing multi-drill (DRILLMENUITEM)
syntax. Any syntax that is currently valid should behave the same after the extended syntax is
implemented.

To define individual menus and items attached to a report node or data element:

TYPE=type, [subtype], [DRILLMENUITEM='description', action|'keyword'],
  [NAME=name], [PARENT=parentname],

where:

type

Identifies the report component that you select in the web browser to execute the link. The
TYPE attribute and its value must appear at the beginning of the declaration.

subtype

Are any additional attributes, such as COLUMN, LINE, or ITEM, that are needed to identify
the report component that you are formatting.

Each DRILLMENUITEM item must have a description or a keyword pair. Descriptions without
actions will automatically be inactive by default.

Creating Reports With TIBCO® WebFOCUS Language

 845

Multi-Drill Feature With Cascading Menus and User-Defined Styling

The exception to this rule will be parent items containing children entries linked with the
NAME/PARENT pairing. In this instance, the action will be to present the children in the
cascading menu.

description

Is the text that appears on the pop-up menu of drill-down options on the report output. The
default value is DrillDown n, where n is a consecutive integer, such as DrillDown 1,
DrillDown 2, and so on.

Note:

If DRILLMENUITEM is set to the special value 'SEPARATOR':

A horizontal separator line will be drawn using the styling and color attributes
defined for the menu borders at the location within the menu.

A separator cannot be associated with an action.

The DRILLMENUITEM value cannot be empty or blank.

action

Is the type of link, as described in Drill-Down Action Options on page 846. For example, a
link to a detail report or URL.

The following attributes are optional. They are only required for cascading menus where a
hierarchy must be defined.

name

An optional unique identifier for the current item to use as a link between parent and
children items. Only required if this node serves as a parent to children menu items where
a link must be identified.

parentname

An optional unique identifier/name of the parent menu item for the current child item. Only
required if this node serves as a parent to another item in the hierarchy.

Drill-Down Action Options

Each drill menu item can be linked to a single instance of the actions below:

FOCEXEC=report.fex

Another report. The StyleSheet attribute is FOCEXEC.

TYPE=type, [subtype], FOCEXEC=fex[(parameters...)], [TARGET=frame,]
[ALT='description',] $

846

10. Linking a Report to Other Resources

URL=url string

A URL. The StyleSheet attribute is URL. You pass a valid URL. Note that the length of the
URL is limited by the maximum number of characters allowed by the browser. For
information about this limit for your browser, see the browser support site.

TYPE=type, [subtype], URL=url[(parameters...)], [TARGET=frame,]
[ALT='description',] $

URL=(field)

A URL from a field. The StyleSheet attribute is URL. You pass the name of a report column
whose value is a valid URL to which the link will jump.

TYPE=type, [subtype], URL=url[(parameters ...)], [TARGET=frame,]
[ALT='description',] $

JAVASCRIPT=function

A JavaScript function. The StyleSheet attribute is JAVASCRIPT.

TYPE=type, [subtype], JAVASCRIPT=function[(parameters ...)], $

Note: If a drilldown link calls a JavaScript function that displays a popup message, the drill
menu will remain open until the popup message is dismissed.

Summary of Drill-Down Links

Within a multi-drill menu, you can link to:

Another report. The StyleSheet attribute is FOCEXEC. For details on the syntax, see Linking
to Another Report on page 820.

A URL. The StyleSheet attribute is URL. You pass a valid URL. For details on the syntax,
see Linking to a URL on page 825.

Note that the length of the URL is limited by the maximum number of characters allowed by
the browser. For information about this limit for your browser, search on your browser
vendor support site.

A URL from a field. The StyleSheet attribute is URL. You pass the name of a report column
whose value is a valid URL to which the link will jump. For details on the syntax, see Linking
to a URL on page 825.

A JavaScript function. The StyleSheet attribute is JAVASCRIPT. For details on the syntax,
see Linking to a JavaScript Function on page 833.

A Maintain Data procedure. The StyleSheet attribute is URL with the keyword MNTCON EX.
For details on the syntax, see Linking to a Maintain Data Procedure on page 836.

Creating Reports With TIBCO® WebFOCUS Language

 847

Multi-Drill Feature With Cascading Menus and User-Defined Styling

A WebFOCUS compiled Maintain Data procedure. The StyleSheet attribute is URL with the
keyword MNTCON RUN. For details on the syntax, see Linking to a Maintain Data Procedure
on page 836.

Sample Drill Menu Stylesheet Code

TABLE FILE GGSALES
SUM
   GGSALES.SALES01.UNITS
   GGSALES.SALES01.DOLLARS
BY GGSALES.SALES01.REGION
BY GGSALES.SALES01.CATEGORY
BY GGSALES.SALES01.PRODUCT
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE SET ASNAMES ON
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET HTMLEMBEDIMG ON
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
FONT=TAHOMA, GRID=OFF,$

848

10. Linking a Report to Other Resources

TYPE=DATA,COLUMN=B2,
  DRILLMENUITEM='Sales Details', NAME=menu2,
  DRILLMENUITEM='By Month',
    PARENT=menu2, NAME=menu21,
    FOCEXEC=detailreport.fex(PARAMETER=CATEGORY),TARGET=_blank,
  DRILLMENUITEM='By Quarter',
    PARENT=menu2, NAME=menu23,
    FOCEXEC=detailreport.fex(PARAMETER=CATEGORY),TARGET=_blank,
  DRILLMENUITEM=SEPARATOR, PARENT=menu2,
  DRILLMENUITEM='By Product',
    PARENT=menu2, NAME=menu24,
    FOCEXEC=detailreport.fex(PARAMETER=CATEGORY),TARGET=_blank,
  DRILLMENUITEM='By Customer',
    PARENT=menu2,NAME=menu25,
    FOCEXEC=detailreport.fex(PARAMETER=CATEGORY),TARGET=_blank,
  DRILLMENUITEM=SEPARATOR, PARENT=menu2,
  DRILLMENUITEM='Profitablity Analysis',
    PARENT=menu2,NAME=menu3,
  DRILLMENUITEM='By Month',
    PARENT=menu3, NAME=menu31,
    FOCEXEC=detailreport.fex(PARAMETER=CATEGORY),TARGET=_blank,
  DRILLMENUITEM='By Region',
    PARENT=menu3, NAME=menu32,
    FOCEXEC=detailreport.fex(PARAMETER=CATEGORY),TARGET=_blank,
  DRILLMENUITEM='Forecasts',
    FOCEXEC=detailreport.fex(PARAMETER=CATEGORY),TARGET=_blank,
$
TYPE=DATA,COLUMN=B3,
  DRILLMENUITEM='IBI Links',NAME=menu4a,
  DRILLMENUITEM='Information Builders',
    PARENT=menu4a, NAME=menu41,
    URL=http://www.ibi.com,TARGET=_blank,
  DRILLMENUITEM='Summit 2015',
    PARENT=menu4a, NAME=menu42,
    URL=http://www.ibi.com,TARGET=_blank,
  DRILLMENUITEM='Competative Analysis',
    PARENT=menu4a, NAME=menu43,
    URL=http://www.ibi.com,TARGET=_blank,
  DRILLMENUITEM='External Links', NAME=menu4b,
  DRILLMENUITEM='Google',
    PARENT=menu4b, NAME=menu45, URL=http://www.google.com,TARGET=_blank,
  DRILLMENUITEM='Weather',
    PARENT=menu4b, NAME=menu46, URL=http://www.weather.com,TARGET=_blank,
  DRILLMENUITEM='CNN',
    PARENT=menu4b,NAME=menu47, URL=http://www.cnn.com,TARGET=_blank,
$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 849

Multi-Drill Feature With Cascading Menus and User-Defined Styling

This code generates a menu structure that looks like the following images.

850

10. Linking a Report to Other Resources

Creating Reports With TIBCO® WebFOCUS Language

 851

Multi-Drill Feature With Cascading Menus and User-Defined Styling

To apply custom styling to the menus, add the following syntax to the StyleSheet:

TYPE=REPORT, OBJECT=MENU, FONT="COMIC SANS MS", COLOR=NAVY,
BACKCOLOR=GREY, HOVER-COLOR=GREY, HOVER-BACKCOLOR=NAVY, $

The menu structure will now look like the following images.

852

10. Linking a Report to Other Resources

Reference: Usage Notes for Multi-Drill Menus

The following interactive reports are supported with the multi-drill cascading menus with user
defined styling:

HFREEZE

Accordion by Row (EXPANDBYROW, EXPANDBYROWTREE)

Accordion by Column (EXPANDABLE)

OLAP

HTML TOC

Note: As of Release 8.2 Version 01, when the Multi-Drill and On Demand Paging features are
enabled in a report, the cascading Multi-Drill menus do not display. Instead, the legacy Multi-
Drill menus generated prior to Release 8.2.01 will be generated. Cascading menus are not
available and all hyperlinks display on the same level on the menu.

Applying Conditional Styling

You can apply conditional styling to a report component, using a phrase such as WHEN, and
use it to select one of a number of different actions, depending on the value of fields in the
report.

The WHEN condition must precede the DRILLMENUITEM syntax.

For details on creating conditions, see Linking With Conditions on page 865.

Example:

Applying Conditional Styling to a Multiple Drill-Down Report

Add the following boldface code to the sample summary report in Creating Multiple Drill-Down
Links on page 843. Notice that the WHEN condition precedes the code for DRILLMENUITEM,
as required.

When you run the summary report, the State field is in red instead of blue whenever budget
dollars is greater than dollar sales, and the pop-up menu of drill-down options shows Detail
Budget Report instead of DrillDown 1 and DrillDown 2.

Creating Reports With TIBCO® WebFOCUS Language

 853

Creating Parameters

.
.
.
TYPE=DATA,
     COLUMN=N1,
     COLOR='BLUE',
     STYLE=UNDERLINE,
     DRILLMENUITEM='DrillDown 1',
          URL=http://www.informationbuilders.com?,
     DRILLMENUITEM='DrillDown 2',
          FOCEXEC=DETAILREPORT(PARAMETER=N1),$

TYPE=DATA,
     COLUMN=N1,
     COLOR='RED',
     STYLE=UNDERLINE,
     WHEN=BUDDOLLARS GT DOLLARS,
     DRILLMENUITEM='Detail Budget Report',
          FOCEXEC=DETAILREPORT(PARAMETER=N1),$.
.
.

Sample output is:

Creating Parameters

If your drill-down report depends on a specific data value in the base report, you must create a
parameter (or parameters) that can pass one or more values to the report you are drilling down
to.

854

10. Linking a Report to Other Resources

Parameters are useful when you want to create a dynamic link. For example, your first report is
a summary report that lists the total number of products ordered by a company on a specific
date. You can drill down from a specific product in that report to a more detailed report that
shows the name of the product's vendor and the individual number of units ordered by order
number. With a dynamic link, you create only one drill-down report that uses the value passed
from the first report to determine what information to display, instead of several static reports.

You can create multiple parameters. The entire string of parameters must be enclosed in
parentheses, separated from each other by a blank space, and cannot exceed 2400
characters.

You can use any combination of the following methods to create parameters in your StyleSheet
declaration. You can specify:

A constant value.

The name or the position of a field.

The name of an amper variable to pass its value. Amper variables can only be used with
inline StyleSheets. For details on inline StyleSheets, see Creating and Managing a
WebFOCUS StyleSheet on page 1197.

Syntax:

How to Create Parameters

parameter=value

where:

parameter

Is the name of the variable in the linked procedure.

Note: To avoid conflicts, do not name variables beginning with Date, IBI, or WF. Variable
names beginning with these values are reserved for Information Builders use.

value

Identifies the value to be passed. Values can be any of the following:

'constant_value' identifies an actual value to be passed. The value must be enclosed
in single quotation marks.

field identifies the field in the report whose value is to be passed to the procedure. You
can identify the field using either the field name or the field position. For details on field
position, see Identifying a Report Component in a WebFOCUS StyleSheet on page 1249.

'&variable' identifies an amper variable whose value is to be passed to the procedure.
The name of the amper variable must be enclosed in single quotation marks. You can use
amper variables only in inline StyleSheets.

Creating Reports With TIBCO® WebFOCUS Language

 855

Creating Parameters

Note: The usual use of an amper variable is to pass a constant value. If the amper
variable corresponds to an alphanumeric field, the amper variable would have to be
embedded in single quotation marks, for example:

'&ABC'.

The entire string of parameter names and values must be enclosed in parentheses. Each
parameter=value pair must be separated by a blank space. You can include multiple
parameters in your request but the entire string cannot exceed 2400 characters.

Note: If the drill-down report contains a -DEFAULTS statement that sets a default value to the
same amper variable passed from the main report, the amper variable value passed down
overwrites the -DEFAULTS statement in the target procedure.

Example:

Creating Parameters by Specifying a Constant Value

The following example illustrates how to create parameters by specifying a constant value. The
relevant StyleSheet declarations are highlighted in the request.

Main report:

SET LOOKGRAPH BAR
SET 3D=OFF
GRAPH FILE SHORT
HEADING
"Sum of Balance Across Short Date"
"Click Any Bar For a Report on Projected Returns Since June 29, 1998 "
SUM BALANCE
ACROSS SHORT_DATE
ON GRAPH SET STYLE *
TYPE=DATA, ACROSSCOLUMN=N1,FOCEXEC=PROJRET(Short_Date='06291998'),$
ENDSTYLE
END

Drill-down report (PROJRET):

TABLE FILE SHORT
HEADING
"Projected Returns Since June 29, 1998 "
SUM PROJECTED_RETURN
BY SHORT_DATE
BY REGION
WHERE SHORT_DATE GE '&Short_Date';
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

856

The output for the main report is:

10. Linking a Report to Other Resources

When you click a bar the output is:

Projected Returns Since June 29, 1998

Date of

Statement

Region

06/29/1998

CENTRAL AMERICA

EASTERN EUROPE

FAR EAST

MIDDLE EAST

NORTH AMERICA

SOUTH AMERICA

WESTERN EUROPE

06/30/1998

CENTRAL AMERICA

EASTERN EUROPE

 Projected

Annualized

Return

     1.360

     2.300

     1.300

     1.140

     1.780

     1.200

     1.140

     1.360

     2.350

Creating Reports With TIBCO® WebFOCUS Language

 857

Creating Parameters

FAR EAST

MIDDLE EAST

NORTH AMERICA

SOUTH AMERICA

WESTERN EUROPE

07/01/1998

CENTRAL AMERICA

EASTERN EUROPE

FAR EAST

MIDDLE
EAST

NORTH AMERICA

SOUTH AMERICA

WESTERN EUROPE

     1.300

     1.140

     1.780

     1.200

     1.140

     1.360

     2.300

     1.300

     1.140

     1.780

     1.200

     1.140

Example:

Creating Parameters By Specifying a Field

The following example illustrates how to create a parameter by specifying a field, in this case
CATEGORY. The SALES drill-down report (the report that is linked to the main report) sets the
CATEGORY field equal to &TYPE. In the base report, TYPE is set to equal the field CATEGORY.

When you run the report, the values for the field CATEGORY (Coffee, Food, Gifts) are linked to
a report that contains the product and regional breakdowns for the respective value.

Main report:

TABLE FILE GGSALES
SUM UNITS DOLLARS
BY CATEGORY
HEADING
"* Click category to see product and regional breakdowns."
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=DATA, COLUMN=CATEGORY, FOCEXEC=SALES (TYPE=CATEGORY), $
ENDSTYLE
FOOTING
"This report was created on &DATE ."
END

Drill-down report (SALES):

858

10. Linking a Report to Other Resources

TABLE FILE GGSALES
ON TABLE SET PAGE-NUM OFF
SUM UNITS DOLLARS
BY CATEGORY BY PRODUCT
ACROSS REGION
WHERE CATEGORY = '&TYPE';
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The output for the main report is:

Click Coffee and the product and regional breakdown for Coffee displays:

Example:

Creating Parameters by Specifying an Amper Variable

The following request illustrates how to create a parameter by specifying an amper variable.
The relevant StyleSheet declarations are highlighted in the request.

Creating Reports With TIBCO® WebFOCUS Language

 859

Creating Parameters

Main report:

SET3D=OFF
GRAPH FILE EMPLOYEE
HEADING
"Salary Report Per Employee ID"
"Click A Bar For The List of Employees in the '&DEPARTMENT' Department"
SUM SALARY
ACROSS EMP_ID AS 'EMPLOYEE ID'
ON GRAPH SET STYLE *
TYPE=DATA, ACROSSCOLUMN=SALARY,
FOCEXEC=EMPBYDEP(DEPARTMENT='&DEPARTMENT'), $
ENDSTYLE
END

Linked report (EMPBYDEP):

TABLE FILE EMPLOYEE
HEADING
"List Of Employees in the '&DEPARTMENT' Department "
PRINT FIRST_NAME LAST_NAME
BY DEPARTMENT
WHERE DEPARTMENT EQ '&DEPARTMENT';
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

When the main report request is run, the following prompt opens:

860

Enter MIS and click Submit. The output is:

10. Linking a Report to Other Resources

When you click a bar on the graph, the output is:

List Of Employees in the 'MIS' Department

DEPARTMENT

FIRST NAME

LAST NAME

MIS

MARY

DIANE

JOHN

  SMITH

  JONES

  MCCOY

ROSEMARIE

  BLACKWOOD

MARY

  GREENSPAN

BARBARA

  CROSS

Creating Reports With TIBCO® WebFOCUS Language

 861

Creating Parameters

Example:

Using DRILLMETHOD in a Drill-Down Request

The following example illustrates how to use the DRILLMETHOD parameter to control the
method used in a drill-down request.

When DRILLMETHOD is set to POST, parameters and values are not included in the URL or
stored in the logs, which makes this method more secure.

When DRILLMETHOD is set to GET, parameters and values are included in the URL and
stored in the logs.

The following drill-down request against the GGSALES data source includes a SET
DRILLMETHOD=POST command and two parameters, one for CATEGORY and one for
PRODUCT.

SET DRILLMETHOD=POST
TABLE FILE GGSALES
SUM DOLLARS BUDDOLLARS
BY CATEGORY
BY PRODUCT
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET STYLE *
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/ibi_themes/Warm.sty,$
TYPE=DATA, COLUMN=N1, TARGET='_blank', FOCEXEC=IBFS:/WFC/Repository/
My_Workspace/~admin/child_report.fex(PARA1=CATEGORY PARA2=PRODUCT), $
ENDSTYLE
END
-RUN

Note: You can also use DRILLMETHOD in a StyleSheet command for each drill down, for
example:

TYPE=DATA, COLUMN=N1, DRILLMETHOD='POST', FOCEXEC=drilldown.fex, $

The following request is the child report.

TABLE FILE GGSALES
SUM DOLLARS BUDDOLLARS
BY CATEGORY
BY PRODUCT
WHERE CATEGORY EQ &PARA1.QUOTEDSTRING AND PRODUCT EQ &PARA2.QUOTEDSTRING;
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET STYLE *
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/ibi_themes/Warm.sty,$
ENDSTYLE
END

862

10. Linking a Report to Other Resources

When you run the drill-down request with DRILLMETHOD=POST and select a category, for
example, Coffee, the parameters and values are not included in the URL, as shown in the
following image.

If you run the drill-down request with DRILLMETHOD=GET, and select a category, for example,
Coffee, the parameters and values are included in the URL, as shown in the following image.

Note: For more information about the SET DRILLMETHOD command, see Customizing Your
Environment in the Developing Reporting Applications manual.

Example:

Using Multiple Parameters

When using multiple parameters, the entire string must be enclosed in parentheses and
separated from each other by a blank space. The relevant StyleSheet declarations are
highlighted in the request.

Main report:

SET 3D=OFF
GRAPH FILE EMPLOYEE
SUM CURR_SAL
ACROSS DEPARTMENT
ON GRAPH SET STYLE *
TYPE=DATA, ACROSSCOLUMN=CURR_SAL,
FOCEXEC=REPORT2 (DEPARTMENT='&DEPARTMENT' LAST_NAME='SMITH'), $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 863

Creating Parameters

Drill-down report (REPORT2):

TABLE FILE EMPLOYEE
PRINT SALARY
BY DEPARTMENT
BY FIRST_NAME
BY LAST_NAME
WHERE DEPARTMENT EQ '&DEPARTMENT'
WHERE LAST_NAME EQ '&LAST_NAME'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

When the main report request is run, the following prompt opens:

864

Enter MIS and click Submit. The output is:

10. Linking a Report to Other Resources

When you click the MIS bar, the output is:

DEPARTMENT

FIRST NAME

LAST NAME

SALARY

MIS

MARY

SMITH

$13,200.00

Linking With Conditions

You can create conditions when linking to a report, URL, or JavaScript function from a report or
graph. For example, you may only be interested in displaying current salaries for a particular
department. You can accomplish this by creating a WHEN condition.

For complete details on WHEN, see Controlling Report Formatting on page 1219.

Note: Linking with conditions is not supported in GRAPH requests.

Syntax:

How to Link With Conditions

To specify a conditional link to a report use:

TYPE=type, [subtype], FOCEXEC=fex[(parameters...)],
   WHEN=expression,[TARGET=frame,] $

Creating Reports With TIBCO® WebFOCUS Language

 865

Linking With Conditions

To specify a conditional link to a URL use:

TYPE=type, [subtype], URL=url[(parameters...)],
   WHEN=expression,[TARGET=frame,] $

To specify a conditional link to a JavaScript function use:

TYPE=type, [subtype], JAVASCRIPT=function[(parameters...)],
   WHEN=expression,[TARGET=frame,] $

where:

type

Identifies the report component that you select in the web browser to execute the link.
The TYPE attribute and its value must appear at the beginning of the declaration.

subtype

Are any additional attributes, such as COLUMN, LINE, or ITEM, that are needed to
identify the report component that you are formatting. For information on identifying
report components, see Identifying a Report Component in a WebFOCUS StyleSheet on
page 1249.

fex

Identifies the file name of the linked procedure to run when you select the report
component. For details about linking to another procedure, see Linking to Another
Report on page 820.

url

Identifies any valid URL, or the name of a report column enclosed in parentheses
whose value is a valid URL. For details about linking to a URL, see Linking to a URL on
page 825.

function

Identifies the JavaScript function to run when you select the report component. For
details about calling a JavaScript function, see Linking to a JavaScript Function on
page 833.

parameters

Values that are passed to the report, URL, or JavaScript function. For details, see
Creating Parameters on page 854.

expression

Is any Boolean expression that would be valid on the right side of a COMPUTE
expression.

Note: IF... THEN... ELSE logic is not necessary in a WHEN clause and is not supported. All
non-numeric literals in a WHEN expression must be specified within single quotation
marks.

866

10. Linking a Report to Other Resources

frame

Identifies the target frame in the webpage in which the output from the drill-down link
is displayed. For details, see Specifying a Target Frame on page 873.

Example:

Linking With Conditions

In this example, we only want to link the MIS value of the DEPARTMENT field to REPORT3. To
do this we include the phrase WHEN=DEPARTMENT EQ 'MIS' in the StyleSheet declaration.
The relevant declarations are highlighted in the requests.

Main report:

TABLE FILE EMPLOYEE
SUM CURR_SAL AS 'Total,Current,Salaries'
BY DEPARTMENT AS 'Department'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=DATA, COLUMN=N1, FOCEXEC=REPORT3(DEPARTMENT=N1),
     WHEN=DEPARTMENT EQ 'MIS', $
ENDSTYLE
END

Drill-down report (REPORT3):

TABLE FILE EMPLOYEE
PRINT SALARY
BY DEPARTMENT
BY LAST_NAME
WHERE DEPARTMENT EQ '&DEPARTMENT'
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

In the following output, note that only the MIS department is linked:

When you click MIS, the following output displays:

Creating Reports With TIBCO® WebFOCUS Language

 867

Linking From a Graphic Image

DEPARTMENT

LAST NAME

SALARY

MIS

  BLACKWOOD

$21,780.00

  CROSS

$27,062.00

$25,755.00

  GREENSPAN

 $9,000.00

 $8,650.00

  JONES

$18,480.00

  MCCOY

  SMITH

$17,750.00

$18,480.00

$13,200.00

Linking From a Graphic Image

You can link to a report or procedure from an image in an HTML report. The image can be
attached to the entire report or to the report heading or footing (this includes table headings/
table footings, and sub-headings/sub-footings).

The syntax for linking from a graphic image is the same as for linking from a report component.
The only difference is adding IMAGE=image to the StyleSheet declaration.

Note: You can only link to a report or procedure from an image when you are using HTML
format.

Syntax:

How to Specify Links From a Graphic Image

To specify a link from an image in a report or procedure use:

TYPE=type, [subtype], IMAGE=image, FOCEXEC=fex
   [(parameters ...)],[TARGET=frame,] $

To specify a link from an image in an URL use:

TYPE=type, [subtype], IMAGE=image, URL=url
   [(parameters ...)],[TARGET=frame,] $

To specify a link from an image in a JavaScript function use:

TYPE=type, [subtype], IMAGE=image, JAVASCRIPT=function
   [(parameters ...)],$

868

10. Linking a Report to Other Resources

where:

type

Identifies the report component that the user selects to execute the link. The TYPE
attribute and its value must appear at the beginning of the declaration. You can
specify the following types of components:

REPORT enables you to drill down from a graphical image that is attached to the entire
report.

TABHEADING or TABFOOTING enables you to drill down from a graphical image that is
attached to a report heading or footing.

HEADING or FOOTING enables you to drill down from a graphical image that is attached to
a page heading or footing.

SUBHEAD or SUBFOOT enables you to drill down from a graphical image that is attached to
a sub heading or sub footing.

Report components are described in Identifying a Report Component in a WebFOCUS
StyleSheet on page 1249.

subtype

Are any additional attributes, such as COLUMN, LINE, or ITEM, that are needed to
identify the report component that you are formatting. See Identifying a Report
Component in a WebFOCUS StyleSheet on page 1249 for information on identifying
report components.

image

Specifies the file name of a graphical image file. The image must exist as a separate
graphic file in a format that your browser supports. Most browsers support GIF and
JPEG file types.

You can specify a local image file, or identify an image elsewhere on the network using a
URL. URLs can be absolute, such as, http://www.ibi.com/graphic.gif, or relative alias that
can be identified to the application server or web server, such as, /ibi_apps/ibi_html/
ibi_logo.gif.

Alternatively, you can specify an alphanumeric field in the report (either a BY sort field or a
display field) whose value corresponds to the name of the image file. For information about
using StyleSheets to incorporate and position graphical images in a report, see Laying Out
the Report Page on page 1331.

fex

Identifies the file name of the linked procedure to run when the user selects the report
component. For details about linking to another procedure, see Linking to Another
Report on page 820.

Creating Reports With TIBCO® WebFOCUS Language

 869

Linking From a Graphic Image

url

Identifies any valid URL, or the name of a report column enclosed in parentheses
whose value is a valid URL. For details about linking to an URL, see Linking to a URL
on page 825.

function

Identifies the JavaScript function to run when the user selects the report component.
For details about calling a JavaScript function, see Linking to a JavaScript Function on
page 833.

parameters

Are values that are passed to the report, URL, or JavaScript function. You can pass
one or more parameters. The entire string of parameters must be enclosed in
parentheses, and separated from each other by a blank space. For details, see
Creating Parameters on page 854.

frame

Identifies the target frame in the webpage in which the output from the drill-down link
is displayed. For details, see Specifying a Target Frame on page 873.

Note: You cannot specify a target frame if you are executing a JavaScript function. However,
the JavaScript function itself can specify a target frame for its results.

Example:

Specifying a Link From an Image

The following example illustrates how to link a report from an image. The relevant StyleSheet
declarations are highlighted in the request.

Main report:

TABLE FILE EMPLOYEE
PRINT LAST_NAME BY EMP_ID
HEADING
"List Of Employees By Employee ID"
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=HEADING, STYLE=BOLD, $
TYPE=REPORT, GRID=OFF, $
TYPE=REPORT,
IMAGE=E:\IBI\WEBFOCUS81\APPS\IBINCCEN\IMAGES\LEFTLOGO.GIF,
     FOCEXEC=IMAGE-D, $
ENDSTYLE
END

Note: The IBINCCEN directory contains the English version of the samples.

Drill-down report (IMAGE-D):

870

10. Linking a Report to Other Resources

TABLE FILE EMPDATA
PRINT SALARY
BY DIV
WHERE DIV LE 'CORP';
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The output for the main report is:

When you click the graphic, the output is:

DIV

SALARY

Creating Reports With TIBCO® WebFOCUS Language

 871

Specifying a Base URL

CE

CORP

 $62,500.00

 $54,100.00

 $25,400.00

$115,000.00

 $33,300.00

 $25,000.00

 $49,000.00

 $40,900.00

 $43,000.00

 $45,000.00

 $55,500.00

 $83,000.00

 $32,000.00

 $62,500.00

 $79,000.00

 $35,200.00

 $62,500.00

 $26,400.00

Specifying a Base URL

If you want to link to files, images, and Java files, but do not know their full, physical URLs, you
can specify a default location where the browser searches for relative URLs.

To specify a default URL location, use the SET BASEURL command. Using SET BASEURL puts
<BASE HREF="url"> into the HTML file that WebFOCUS generates. When a report is run, the
specified directory is searched for the HTML files, graphics files, and Java applet CLASS files
that are called by the generated webpage.

For more details on specifying URLs, see Navigating Within an HTML Report on page 969.

872

10. Linking a Report to Other Resources

Syntax:

How to Specify a Base URL

SET BASEURL=url

where:

url

Is the default location where the browser searches for relative URLs specified in the
HTML documents created by your application.

The URL must begin with http:// and end with a closing delimiter (/).

Example:

Specifying a Base URL

The following illustrates how to specify a base URL:

SET BASEURL=http://host[:port]/ibi_apps/ibi_html/

where:

host

Is the host name where the WebFOCUS Web application is deployed.

port

Is the port number (specified only if you are not using the default port number) where the
WebFOCUS Web application is deployed.

If you are including a graphic image in your report that is stored in the specified base URL, you
can add the following declaration to your StyleSheet instead of typing the entire URL:

TYPE=HEADING, IMAGE=ib_logo.gif, ..., $

Note: If the URL is at a remote website, it may take longer to retrieve. Whenever possible,
store graphic image files on your WebFOCUS system.

Specifying a Target Frame

You can use frames to subdivide application HTML pages into separate scrollable sections.
Frames enable users to explore various information items on a page by scrolling through a
section, instead of linking to a separate page. When defining a link from a report component to
a report procedure or URL, you can specify that the results of the drill-down link be displayed in
a target frame on a webpage.

Creating Reports With TIBCO® WebFOCUS Language

 873

Specifying a Target Frame

There are two ways to specify a target frame. You can specify:

A target frame in a StyleSheet declaration using the TARGET attribute. You can use
StyleSheets to specify that drill-down links from a report or graph are displayed in a target
frame on the webpage displaying the report or graph. However, using StyleSheets to specify
target frames adds extra HTML syntax to every HREF that is generated.

Note: When specifying a target frame from the Report canvas, manually added commands
in the StyleSheet are not recognized. The Report canvas removes commands that it does
not generate itself.

A default target frame with a SET command. SET TARGETFRAME puts the HTML code
<BASE TARGET="framename"> into the header of the HTML file that WebFOCUS displays.
All drill-down links from the base report or graph are directed to the specified frame, unless
overridden by the TARGET attribute in the StyleSheet.

To use the TARGET attribute or the SET TARGETFRAME command, you must create multiple
frames on the webpage.

Note: You cannot specify a target frame if you are executing a JavaScript function. However,
the JavaScript function itself can specify a target frame for its results.

Syntax:

How to Specify a Target Frame

To specify a target frame in a report or procedure use:

TYPE=type, [subtype], FOCEXEC=fex[(parameters ...)], [TARGET=frame,] $

To specify a target frame for an URL use:

TYPE=type, [subtype], URL=url[(parameters ...)], [TARGET=frame,] $

where:

type

Identifies the report component that the user selects in the web browser to execute
the link. The TYPE attribute and its value must appear at the beginning of the
declaration.

subtype

Are any additional attributes, such as COLUMN, LINE, or ITEM, that are needed to
identify the report component that you are formatting. See Identifying a Report
Component in a WebFOCUS StyleSheet on page 1249 for information on identifying
report components.

874

10. Linking a Report to Other Resources

fex

Identifies the file name of the linked procedure to run when the user selects the report
component. For details about linking to another procedure, see Linking to Another
Report on page 820.

url

Identifies any valid URL, or the name of a report column enclosed in parentheses
whose value is a valid URL to which the link will jump. For details about linking to an
URL, see Linking to a URL on page 825.

parameters

Are values being passed to the procedure or URL. You can pass one or more
parameters. The entire string of values must be enclosed in parentheses, and
separated from each other by a blank space. For details, see Creating Parameters on
page 854.

frame

Identifies the target frame in the web page in which the output from the drill-down link
(either a FOCEXEC or URL) is displayed.

If the name of the target frame contains embedded spaces, the name will be correctly
interpreted without enclosing the name in quotation marks. For example:

TYPE=DATA, COLUMN=N1,
FOCEXEC=MYREPORT, TARGET=MY FRAME, $

The name of the target frame is correctly interpreted to be MY FRAME.

You can also use the following standard HTML frame names: _BLANK, _SELF, _PARENT,
_TOP.

Syntax:

How to Specify a Default Target Frame

SET TARGETFRAME=frame

where:

frame

Identifies the target frame in the webpage in which the output from the drill-down link
(either a FOCEXEC or URL) is displayed.

Creating Reports With TIBCO® WebFOCUS Language

 875

Creating a Compound Report

Example:

Specifying a Target Frame

The following illustrates how to specify a default target frame:

SET TARGETFRAME=_SELF

The following illustrates how to specify a target frame in a request. The relevant StyleSheet
declaration is highlighted in the request.

TABLE FILE EMPLOYEE
PRINT CURR_SAL
BY DEPARTMENT
ON TABLE SET STYLE *
TYPE=DATA, COLUMN=N1, URL=http:\\www.informationbuilders.com,
     TARGET=_SELF, $
ENDSTYLE
END

Creating a Compound Report

Compound reports combine multiple reports into a single file. This enables you to concatenate
reports with styled formats (such as PDF, DHTML, PS, EXL2K, or XLSX). You can also embed
image files, including graphs saved as images, in a compound report.

Three types of compound reports exist:

Legacy Compound Reports (or, simply, Compound Reports). These reports string the
individual reports or graphs together sequentially into a single output file. The functionality
for this type of compound report has been stabilized. The syntax is included in this
document for upward compatibility, and applications using this technique will continue to
work. For more information, see Creating a Compound PDF or PS Report on page 934 and
Creating a Compound Excel Report Using EXL2K on page 943.

Compound Layout Reports. A Compound Layout report is comprised of individual
component reports or graphs, either embedded or external. Reports and graphs can be
positioned anywhere on the page. You can assign specific pages to combinations of reports
and specify how to handle overflow onto additional pages. For more information, see
Creating a Compound Layout Report With Document Syntax on page 877.

Coordinated Compound Layout Reports. A Coordinated Compound Layout report is
coordinated so that all reports and graphs that contain a common sort field are burst into
separate page layouts. Pages are generated for each value of the common sort field, with
every component displaying the data it retrieved for that value on that page. You create a
Coordinated Compound Layout report by specifying MERGE=ON in the SECTION declaration
for the Compound Layout report.

876

10. Linking a Report to Other Resources

In a Coordinated Compound Layout report, if at least one component contains data for a
specific sort field value, a page is generated for that value even though some of the
components may be missing. For more information about Coordinated Compound Layout
reports with missing data, see Coordinated Compound Layout Reports With Missing Data on
page 912.

While the length of the report will always include all of the rows of data generated by the query,
the width of the report is limited by the size of the defined component container. This means
that paneling is not supported for compound reports, although it is for non-compound PDF
reports. For non-compound PDF documents, if the width of the report data is wider than the
defined page size, a panel (or horizontal overflow page) is automatically generated. This
paneling feature is not supported for compound PDF documents, so each compound
component must fit within the width of the defined container in order for the report to be
successfully generated. The container size is defined within each type of report.

In legacy compound syntax, if one of the component reports is too large to fit within the
defined page width, execution is halted and the user is presented with an error message
stating that paneling is not supported.

In Compound Layout Syntax, if a component is too wide to fit within the defined container,
the report wraps the contents within the container. The container size is defined through a
combination of the POSITION and DIMENSIONS parameters for the component within the
compound syntax. For more information about compound layout syntax, see Creating a
Compound Layout Report With Document Syntax on page 877.

For information about creating PDF Compound Reports with Drill Through links, see How to
Create a Drill Through in a PDF Compound Report on page 956.

Creating a Compound Layout Report With Document Syntax

Typically, you create a compound layout report by using the options in the Document canvas.
Alternatively, you may create a compound layout report by modifying the syntax in any text
editor.

Syntax for a compound layout report is structured by a compound layout block, which places all
of the layout information in a single block that precedes the report. This block begins with a
COMPOUND LAYOUT declaration and is terminated with END. The language it contains is
based on StyleSheet syntax and is parsed by the StyleSheet parser.

This is supported with styled formats, such as PDF, PS, DHTML, EXL2K, or XLSX.

Tip: For details about StyleSheet syntax, see Creating and Managing a WebFOCUS StyleSheet
on page 1197.

Creating Reports With TIBCO® WebFOCUS Language

 877

Creating a Compound Report

The compound layout block consists of SECTION, PAGELAYOUT, and COMPONENT
declarations. The general structure of the compound layout block of syntax is:

COMPOUND LAYOUT PCHOLD AS filename FORMAT format

SECTION
    PAGELAYOUT
      COMPONENT
      COMPONENT
    ...
    PAGELAYOUT
      COMPONENT
      COMPONENT
    ...
  ...
END
...
COMPOUND END

Note on Compound Layout Declaration: The available compound layout output formats are
PDF, DHTML, PowerPoint, AHTML, Excel, FLEX, and APDF. The selected compound layout
format will override any report output format from the individual components. The output file
name can be defined using an AS filename phrase in the COMPOUND block. If none is defined,
the file name is taken from the ON TABLE HOLD phrase in the first component report.

END signifies the end of the COMPOUND LAYOUT block, whereas COMPOUND END signifies
the end of the compound report.

Additionally, the syntax SET COMPONENT=report(n) is added after each component, followed
by the actual WebFOCUS code to generate the report.

Reference: SECTION Declaration and Syntax

A compound report section, or SECTION declaration, is a grouping of component reports within
a compound report. While the current functionality only supports reports with a single section,
this structure is used to support more complex reports. The SECTION declaration is mandatory
when creating a compound layout report.

The SECTION syntax appears as:

SECTION=section-name, LAYOUT=ON, [MERGE=ON|OFF,]
 [UNITS=IN|CM|PTS,] [PAGESIZE=size,] [ORIENTATION=PORTRAIT|LANDSCAPE,]
 [LEFTMARGIN=m,] [RIGHTMARGIN=m,] [TOPMARGIN=m,] [BOTTOMMARGIN=m,] $

878

10. Linking a Report to Other Resources

where:

section-name

Is the unique identifier of the section, up to 16 characters.

LAYOUT=ON

Specifies that the section uses a complex layout.

Note: LAYOUT=ON is the only applicable option at this time.

MERGE={ON|OFF}

Specifies whether the section is coordinated (merged) based on the value of the initial BY
field.

Note: The default value is OFF.

m

Specifies the margins (LEFT, RIGHT, TOP, BOTTOM) in inches, centimeters, or points.

If the optional items, UNITS, PAGESIZE, ORIENTATION, or MARGIN are present in the SECTION
declaration, they override any settings of these parameters within the component reports,
global SET commands, ON TABLE SET commands, and StyleSheet keywords.

Reference: PAGELAYOUT Declaration

A SECTION consists of one or more PAGELAYOUT declarations, each of which group together a
number of COMPONENT declarations that are laid out on that particular page of the section.

The PAGELAYOUT keyword brackets a group of COMPONENT declarations that follow, up to the
next PAGELAYOUT keyword, or the end of the section.

The PAGELAYOUT syntax appears as:

PAGELAYOUT={n|ALL},
 [TOPMARGIN=m,] [BOTTOMMARGIN=m,]$

where:

{n|ALL}

Specifies on what page of a multi-page layout the components appear. The value (n) is
either a page number within the current section, or ALL to indicate that the component
appears on every page of the section.

The PAGELAYOUT values are numbered starting with 1. For example, if a compound
report is printed on two sides of a page, the component reports on the front side would
be specified as PAGELAYOUT 1, and the reverse side would be PAGELAYOUT 2.

Note: Syntax is required even if the report only contains a single page.

PAGELAYOUT=1, $

Creating Reports With TIBCO® WebFOCUS Language

 879

Creating a Compound Report

The PAGELAYOUT=ALL syntax specifies a component that appears on every page. This
is useful for components that generate page headers or footers.

PAGELAYOUT=ALL, $

m

Defines the boundaries (TOP, BOTTOM) for flowing reports in current units. For a
description of flowing reports, see COMPONENT Declaration on page 881.

Reference: Page Masters

Components included in a declaration for PAGELAYOUT=ALL appear on every page of the report
output. This is useful for creating a design theme for the compound report output:

Page masters must have a default report component (since COMPONENT is a required
syntax element), but that report component should not display any data, except in the
heading. If the component displays data or graphics in the heading, you must leave space
for the heading on every page, being careful to place the other components in areas on the
page that do not overlap with the heading.

For example, the following report does not display any data:

SET COMPONENT='DfltCmpt1'
TABLE FILE SYSCOLUM
SUM TBNAME NOPRINT
IF READLIMIT EQ 1
ON TABLE SET PREVIEW ON
ON TABLE SET PAGE-NUM NOLEAD
END

Page masters for coordinated compound reports must have the same primary BY field as
other components in the compound layout report. The best way to create the default
component for the page master in a coordinated compound report is to use one of the data
sources for one of the compound layout reports. For example, if a component report for
PAGELAYOUT1 is against the GGSALES data source, and the primary BY field is PCD, the
default component for the page master could be:

SET COMPONENT='DfltCmpt1'
TABLE FILE GGSALES
SUM UNITS NOPRINT
BY PCD NOPRINT
IF READLIMIT EQ 1
ON TABLE SET PREVIEW ON
ON TABLE SET PAGE-NUM NOLEAD
END

880

10. Linking a Report to Other Resources

Note that the recommended way to create a design theme with repeating text and images
on a page master is to place drawing objects on the page master. For information, see How
to Draw Objects With Document Syntax on page 895.

Page master styling for size and orientation only applies to the default document level.
Page master elements do not automatically resize and position for various page
orientations throughout the document. For documents requiring mixed page orientations,
each page layout can be defined with its own orientation. In this scenario, styling elements
should be applied to the individual page layouts so that the styling can be appropriately
applied for each change in page orientation.

Reference: COMPONENT Declaration

The order of COMPONENT declarations in the COMPOUND LAYOUT block must match the order
in which the component reports are executed, and there must be a COMPONENT declaration
for each component report.

There are two types of components: fixed and flowing. A fixed component fills the container
defined by the dimension parameters on the page and, if additional data exists, it overflows
onto the next page in the same fixed size in the same location. The size and location of the
fixed overflow component can be customized on the overflow page (using the OVERFLOW-
POSITION and OVERFLOW-DIMENSION parameters). In a flowing component, the data flows
from the top of the defined component to the bottom page margin and then begins to flow
again on the top page margin of the overflow page, until the data is complete. The starting
position of each type of component is defined by the POSITION parameter.

You can also specify the starting position of a component relative to another component, using
the RELATIVE-TO, RELATIVE-POINT, and POSITION-POINT keywords. In this case, the relative
coordinates of the component's POSITION are interpreted based on where the component, to
which it is relative, ends. If the relative component is a flowing component, you can optionally
use the REQUIRED-SPACE keyword in conjunction with the RELATIVE-TO keyword to specify
where to start the current component.

The fixed or flowing aspect of the component is determined by the DIMENSION parameter. For
a fixed component, the DIMENSION parameter specifies sizes for the dimensions of the
bounding box. However, for a flowing component the DIMENSION parameter specifies asterisks
(* *) for the dimensions.

Creating Reports With TIBCO® WebFOCUS Language

 881

Creating a Compound Report

The COMPONENT syntax appears as:

COMPONENT=component-name, TYPE=component-type,
    POSITION=(x y), DIMENSION=(xsize ysize),
    [OVERFLOW-POSITION=(x y),] [OVERFLOW-DIMENSION=(xsize ysize),]
    [RELATIVE-TO=relative_component_name,]
    [RELATIVE-POINT=relative-value, POSITION-POINT=position-value,
      REQUIRED-SPACE=required-space-value,]
    [DRILLMAP=((L1 targetreport)),]  $

where:

component-name

The name of the component must be a unique identifier, up to 16 characters. It
designates a component report that appears later in the request (in the same procedure
(FOCEXEC) or in a called procedure), and is identified by SET COMPONENT=component-
name syntax, using the same name.

Note: The SET syntax only tags styled reports that can participate in a compound report,
so it can be placed before unstyled reports that precede the report to be named. For
example, reports that generate extract files.

component-type

Specifies the type of component being declared. Currently, only REPORT is supported.

POSITION=(x y)

Specifies the (x y) coordinate on the page where the upper-left corner of the component is
to be placed. All coordinates are in current UNITs (default inches), and (0 0) is the upper-
left corner of the physical page.

Note: By default, coordinates are absolute locations on the physical page. If x or y is
preceded by a plus sign (+) or a minus sign ( - ), for example, (+.25 +0), the coordinate is
relative to the top-left page margin. If the RELATIVE-TO keyword is present, then a relative
coordinate is relative to the named object of RELATIVE-TO declared in the keyword.

DIMENSION=(xsize ysize)

Specifies the size of the bounding box of the component (in current UNITs).

For a fixed component, xsize and ysize must be numeric dimension sizes.

For a flowing component, xsize and ysize must both be asterisks DIMENSION = (* *).

OVERFLOW-POSITION=(x y) and OVERFLOW-DIMENSION=(xsize ysize)

These optional items specify the position and dimension on subsequent pages, if it
overflows its initial bounding box.

882

10. Linking a Report to Other Resources

OVERFLOW-POSITION and OVERFLOW-DIMENSION are supported for flowing components,
as well. For example:

COMPONENT='report2', TEXT='report2', TOC-LEVEL=2,
POSITION=(0.5 1.7), DIMENSION=(* *), OVERFLOW-POSITION=(0.5 1.7),
OVERFLOW-DIMENSION=(* *),

RELATIVE-TO=relative_component_name

Specifies another component with respect to which relative coordinates of the current
component's POSITION are interpreted.

The relative component must either have a fixed position, or be generated prior to the
current component.

RELATIVE-POINT=relative-value and POSITION-POINT=position-value

These optional parameters designate which point on the current component is positioned
relative to which point on the relative component (for example, TOP-LEFT of the current
component relative to BOTTOM-LEFT of the relative component).

Can be set to any combination of the following values:

TOP-LEFT

TOP-CENTER

TOP-RIGHT

CENTER-LEFT

CENTER

CENTER-RIGHT

BOTTOM-LEFT

BOTTOM-CENTER

BOTTOM-RIGHT

REQUIRED-SPACE=required-space-value

Specifies the minimum amount of space that must be left on the page, from where the
relative component ends, in order to start the current component. If there is not enough
space left from where the relative component ends, the current component will start on the
next page.

Creating Reports With TIBCO® WebFOCUS Language

 883

Creating a Compound Report

Can be one of the following:

An (x y) pair that specifies, in current units, the minimum horizontal and vertical space
left on the page after the relative component and that is needed in order to start the
current component.

AUTO, which will automatically calculate the remaining available space left on the page
after the relative component and determine if the entire current component can fit into
that space. If it cannot fit in the available space, it will start the current component on
the next page.

DRILLMAP=((L1 targetreport))

Identifies the link identifier and the target report for a Drill Through hyperlink from this
report. L1 is a sufficient link identifier at this time. For more information on Drill Through
reports, see How to Create a Drill Through in a PDF Compound Report on page 956.

Note: The double parentheses are required.

Example:

Creating a Compound Layout Report With Document Syntax

In this simple example using the GGSALES Master File, the MERGE keyword specifies that a
Coordinated Compound Layout Report is to be generated. Since the first BY field of each
component is REGION, a page will be generated for each value of REGION, with the first report
(Sales) positioned at (1 1) and the second report (Units) at (6.25 1).

Enter the following syntax in the Text Editor.

884

10. Linking a Report to Other Resources

SET PAGE-NUM=OFF
COMPOUND LAYOUT PCHOLD FORMAT PDF
SECTION=S1, LAYOUT=ON, MERGE=ON, ORIENTATION=LANDSCAPE, $
PAGELAYOUT=1, $
COMPONENT=Sales, TYPE=REPORT, POSITION=(1 1), DIMENSION=(4 4), $
COMPONENT=Units, TYPE=REPORT, POSITION=(6.25 1), DIMENSION=(4 4), $
END
SET COMPONENT=Sales
TABLE FILE GGSALES
"Sales report for <REGION"
" "
SUM DOLLARS/F8M
BY REGION NOPRINT
BY ST
BY CITY
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, FONT=HELVETICA, COLOR=RED, SQUEEZE=ON, $
END
SET COMPONENT=Units
TABLE FILE GGSALES
"Number of unit sales per product for <REGION"
" "
SUM CNT.UNITS AS 'Number of units sold'
BY REGION NOPRINT
BY PRODUCT
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, FONT=HELVETICA, COLOR=BLUE, SQUEEZE=ON, $
ENDSTYLE
END
COMPOUND END

The following syntax is an example of what the same report might look like if the component
reports were in pre-existing procedures (FOCEXECs), as indicated by R1 and R2.

SET PAGE-NUM=OFF
SET SQUEEZE=ON
COMPOUND LAYOUT PCHOLD FORMAT PDF
SECTION=S1, LAYOUT=ON, MERGE=ON, ORIENTATION=LANDSCAPE, $
PAGELAYOUT=1, $
COMPONENT=R1, TYPE=REPORT, POSITION=(1 1), DIMENSION=(4 4), $
COMPONENT=R2, TYPE=REPORT, POSITION=(6 1), DIMENSION=(4 4), $
END
SET COMPONENT=R1
EX REPORT1
SET COMPONENT=R2
EX REPORT2
COMPOUND END

Creating Reports With TIBCO® WebFOCUS Language

 885

Creating a Compound Report

The first page of output is:

Example:

Creating a Coordinated Graph With Document Syntax

This example, using the GGSALES Master File, generates a Coordinated Compound Layout
report that contains a graph and a report (by replacing the first report in the previous example
with a graph). Note that a graph request with two BY fields will generate a graph for each value
of the first BY field (REGION), and that these files are named by appending sequence numbers
to the HOLD file name. For example, HOLD0.SVG, HOLD1.SVG, and so on.

To place these graphs into a report as a component of a Coordinated Compound Layout report,
several COMPUTE commands are required to construct the name of each graph file
(HOLD0.SVG, HOLD1.SVG, and so on). Additionally, a COMPUTE command will add the image
files into the HEADING of the TABLE request so that they are associated with the same value
of REGION, from which they were originally produced.

Enter the following syntax in the Text Editor.

SET PAGE-NUM=OFF
COMPOUND LAYOUT PCHOLD FORMAT PDF
SECTION=S1, LAYOUT=ON, MERGE=ON, ORIENTATION=LANDSCAPE, $
PAGELAYOUT=1, $
COMPONENT=Sales, TYPE=REPORT, POSITION=(0.25 1), DIMENSION=(4 4), $
COMPONENT=Fuel, TYPE=REPORT, POSITION=(7.25 1), DIMENSION=(4 4), $
END

886

10. Linking a Report to Other Resources

SET COMPONENT=Sales
GRAPH FILE GGSALES
SUM PCT.DOLLARS
BY REGION NOPRINT
BY PRODUCT
ON GRAPH SET LOOKGRAPH HBAR
ON GRAPH HOLD AS HOLD FORMAT SVG
ON GRAPH SET GRAPHSTYLE *
setPlace(true);
setColorMode(1);
setDepthRadius(0);
setDepthAngle(0);
setDisplay(getO1MajorGrid(),false);
setTransparentBorderColor(getFrame(),true);
setDisplay(getDataText(),true);
setTextFormatPreset(getDataText(),28);
setFontSizeAbsolute(getDataText(),true);
setFontSizeInPoints(getDataText(),9);
setPlaceResize(getDataText(),0);
setFontStyle(getDataText(),0);
setTransparentBorderColor(getSeries(0),true);
setDisplay(getO1AxisLine(),false);
setFontSizeAbsolute(getO1Label(),true);
setFontSizeInPoints(getO1Label(),9);
setPlaceResize(getO1Label(),0);
setFontSizeAbsolute(getY1Label(),true);
setFontSizeInPoints(getY1Label(),9);
setPlaceResize(getY1Label(),0);
setTextFormatPreset(getY1Label(),28);
setGridStyle(getY1MajorGrid(),3);
setDisplay(getY1AxisLine(),false);
setDisplay(getY1MajorGrid(),false);
setDisplay(getY1Label(),false);
setDataTextPosition(3);
setTextString(getO1Title(),"");
setTextString(getY1Title(),"");
setFontStyle(getTitle(),0);
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 887

Creating a Compound Report

TABLE FILE GGSALES
"Percent of Sales by Product in <REGION"
" "
SUM
COMPUTE CNTR/I4 = CNTR + 1; NOPRINT
COMPUTE CNTR2/A4 = IF &FOCGRAPHCNT EQ 1 THEN ' ' ELSE
FTOA(CNTR-1,'(F4)','A4'); NOPRINT
COMPUTE IMG/A16 = 'HOLD'||LJUST(4,CNTR2,'A4')|| '.svg'; NOPRINT
BY REGION NOPRINT
ON REGION PAGE-BREAK
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
type=HEADING, IMAGE=(IMG), position=(0 0), $
TYPE=REPORT,PAGE-LOCATION=OFF,$
TYPE=REPORT, FONT=HELVETICA, COLOR=BLACK, SQUEEZE=ON, $
ENDSTYLE
END

SET COMPONENT=Fuel
TABLE FILE GGSALES
"Sales report for <REGION"
" "
SUM DOLLARS/F8M
BY REGION NOPRINT
BY ST
BY CITY
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, FONT=HELVETICA, COLOR=RED, SQUEEZE=ON, $
ENDSTYLE
END
COMPOUND END

888

The first page of output is:

10. Linking a Report to Other Resources

Example:

Creating Multi-Page Layouts With Document Syntax

In this example using the GGSALES Master File, multi-page layouts allow components to be
placed in fixed locations on multiple pages. For example, a Coordinated Compound Layout
report can contain component reports R1 and R2 for each value of the first sort field on the
odd-numbered pages (front side), and R3 on the even-numbered pages (reverse side).
Additionally, you can place the same heading that contains a logo and some text with the
embedded value of the first sort field at the top of each side.

For the heading report, create a procedure (named HEADER.FEX), and enter the following
syntax:

TABLE FILE GGSALES
" "
"Report package for <REGION"
BY REGION NOPRINT
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, FONT=HELVETICA, SIZE=20, $
TYPE=REPORT, IMAGE=poweredbyibi.gif, POSITION=(+.25 +.25), $
TYPE=HEADING, LINE=2, ITEM=1, POSITION=4, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 889

Creating a Compound Report

We will use components R1 and R2 from the previous example. If you did not already do so,
save them as REPORT1.FEX and REPORT2.FEX. Enter the following syntax as the R3 report
component, by creating a procedure named REPORT3.FEX.

TABLE FILE GGSALES
"Report R3 for <REGION"
BY REGION NOPRINT
SUM DOLLARS BY ST
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, FONT=HELVETICA, COLOR=GREEN, $
ENDSTYLE
END

From the Text Editor, enter the following syntax specifying that the R1 and R2 report
components appear on page 1. The R3 report component appears on page 2, and the heading
report will appear on all pages of the document.

SET PAGE-NUM=OFF
SET SQUEEZE=ON
COMPOUND LAYOUT PCHOLD FORMAT PDF
SECTION=S1, LAYOUT=ON, MERGE=ON, ORIENTATION=LANDSCAPE, $
PAGELAYOUT=ALL, $
COMPONENT=HEADER, TYPE=REPORT, POSITION=(1 1), DIMENSION=(4 4), $
PAGELAYOUT=1, $
COMPONENT=R1, TYPE=REPORT, POSITION=(1 3), DIMENSION=(4 4), $
COMPONENT=R2, TYPE=REPORT, POSITION=(6 3), DIMENSION=(4 4), $
PAGELAYOUT=2, $
COMPONENT=R3, TYPE=REPORT, POSITION=(4 3), DIMENSION=(4 4), $
END

SET COMPONENT=HEADER
EX HEADER
SET COMPONENT=R1
EX REPORT1
SET COMPONENT=R2
EX REPORT2
SET COMPONENT=R3
EX REPORT3
COMPOUND END

890

Page 1 of the output is:

10. Linking a Report to Other Resources

Page 2 of the output is:

Creating Reports With TIBCO® WebFOCUS Language

 891

Creating a Compound Report

Example:

Creating Page Overflow With Document Syntax

A common type of report contains a fixed layout at the top of the page, followed by a report
containing detail records of unfixed length. For example, a brokerage statement may contain
the customer name and address, an asset-allocation graph, and a comparison of the portfolio
with market indexes at the top, followed by a list of securities held in the account. If the list of
securities overflows the first page, we would like it to continue on the second page,
underneath the common heading which appears on all pages (a logo, account number, page
number for instance). The OVERFLOW-POSITION and OVERFLOW-DIMENSION syntax enables us
to specify where on the overflow page the report continues and what its maximum length on
each overflow page should be. (Note that its width should not vary from one page to the next.)

The following example, using the GGSales Master File, demonstrates how you can use
OVERFLOW-POSITION and OVERFLOW-DIMENSION to reposition the second report component
(R2) so that it begins below the first component on the initial page, and two inches below the
top of the page on subsequent pages. Note that this leaves enough space for the header
report component (HEADER) at the top of each page.

Additionally, PAGELAYOUT=ALL forces the HEADER component to appear at the top of each
overflow page.

Enter the following syntax in the Text Editor.

SET PAGE-NUM=OFF
COMPOUND LAYOUT PCHOLD FORMAT PDF
SECTION=Example, LAYOUT=ON, MERGE=OFF, $
 PAGELAYOUT=1, $
    COMPONENT=R1, TYPE=REPORT, POSITION=(1.5 2), DIMENSION=(8 3), $
    COMPONENT=R2, TYPE=REPORT, POSITION=(.5 5), DIMENSION=(8 5),
        OVERFLOW-POSITION=(.5 2), OVERFLOW-DIMENSION=(8 8.5), $
  PAGELAYOUT=ALL, $
    COMPONENT=HEADER, TYPE=REPORT, POSITION=(1.25 1), DIMENSION=(6 1), $
END

SET COMPONENT=R1
TABLE FILE GGSALES
HEADING CENTER
"Report 1"
"Sales Summary by Category"
" "
SUM UNITS BUDUNITS DOLLARS BUDDOLLARS BY CATEGORY
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, FONT=HELVETICA, SQUEEZE=ON, $
ENDSTYLE
END

892

10. Linking a Report to Other Resources

SET COMPONENT=R2
TABLE FILE GGSALES
HEADING CENTER
"Report 2"
"Sales Detail Report"
" "
SUM UNITS BUDUNITS DOLLARS BUDDOLLARS
BY CATEGORY BY PRODUCT BY REGION
ON CATEGORY UNDER-LINE
ON PRODUCT SUB-TOTAL
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, FONT=HELVETICA, SQUEEZE=ON, $
ENDSTYLE
END

SET COMPONENT=HEADER
TABLE FILE GGSALES
HEADING
"Gotham Grinds sales to Information Builders, October 1997"
BY CATEGORY NOPRINT
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, IMAGE=gotham.gif, POSITION=(3.25 .25), DIMENSION=(2 .75), $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 893

Creating a Compound Report

The first page of output is:

894

The second page of output is:

10. Linking a Report to Other Resources

Syntax:

How to Draw Objects With Document Syntax

A variety of objects can be drawn on the page to enhance a report. The currently supported
objects include Lines, Boxes, Static text strings, and Images.

The syntax for drawing these objects may appear in the StyleSheet of a report, but they may
also be included within a PAGELAYOUT grouping in the COMPOUND LAYOUT declarations. The
syntax for each drawing object is described below.

Lines. To draw a line from point (x1 y1) to point (x2 y2), enter the following syntax:

OBJECT=LINE, POSITION=(x1 y1), ENDPOINT=(x2 y2),
        [BORDER=b,] [BORDER-COLOR=c,] [BORDER-STYLE=s,]$

Optionally, the border attributes BORDER, BORDER-COLOR, and BORDER-STYLE follow the
existing BORDER syntax, as shown below:

Creating Reports With TIBCO® WebFOCUS Language

 895

Creating a Compound Report

OBJECT=LINE, POSITION=(1 1), ENDPOINT=(8 1),
        BORDER=HEAVY, BORDER-COLOR=RED, BORDER-STYLE=DASHED, $

Boxes. To draw a box, whose upper left corner is at (x y), and whose dimensions are xdim
by ydim, enter the following syntax:

OBJECT=BOX, POSITION=(x y), DIMENSION=(xdim ydim),
        BACKCOLOR=c,
        [BORDER=b,] [BORDER-COLOR=bc,] [BORDER-STYLE=bs,] $

Tip: The background color, which is c, specifies the color with which the box is filled and
can be any valid color. For example, yellow or RGB(200 200 200).

As in the BORDER syntax, the individual sides of the box can be styled separately. For
example:

OBJECT=BOX, POSITION=(1 1), DIMENSION=(2 3),
        BACKCOLOR=YELLOW,
        BORDER=HEAVY, BORDER-TOP-COLOR=RED, BORDER-BOTTOM-COLOR=BLUE, $

Note that, as in the BORDER syntax, attributes of lines or boxes that are not explicitly
specified have the following defaults:

Color: black

Style: solid

Width border attribute: medium

Static text strings. Static text strings display text that you enter as part of the object
description.

You can format the text displayed in the text object by including markup tags within the text
portion of the text object. A report with markup tags in a text object is called a markup
report. A markup report can be generated as a PDF, DHTML, PPT, or PPTX output file.
WebFOCUS supports a subset of HTML tags and its own page numbering tags. To activate
these markup tags (so that they are treated as formatting elements instead of displaying
as text), add the attribute MARKUP=ON to the string object. For additional information, see
Text Formatting Markup Tags for a Text Object on page 901.

To draw a static text string at position (x y), enter the following syntax:

OBJECT=STRING, POSITION=(X Y), TEXT='any text you like', [MARKUP={ON|
OFF},] [FONT=f,] [SIZE=sz,] [STYLE=st,] [COLOR=c,]
        [WRAP=ON, DIMENSION=(xdim ydim),] [LINESPACING=linesoption ,]
 $

896

10. Linking a Report to Other Resources

where:

POSITION=(xy)

Specifies the (x y) coordinate on the page where the upper-left corner of the
component is to be placed. All coordinates are in current UNITs (default is inches),
and (0 0) is the upper-left corner of the physical page.

Note: By default, coordinates are absolute locations on the physical page. If x or y is
preceded by a plus sign (+) or minus sign ( - ), for example, (+.25 +0), the coordinate
is relative to the left or top page margin.

TEXT='any text you like'

Is the text to be placed in the text object.

Note: If your text contains any open caret characters (<), you must put a blank space
after each open caret that is part of the text. If you do not, everything following the
open caret will be interpreted as the start of a markup tag and will not display as text.

MARKUP={ON|OFF}

ON causes the markup tags to be interpreted as formatting options. OFF displays the
tags as text. OFF is the default value.

FONT=f

Is the default font to be used for the text.

SIZE=sz

Is the default font size to be used for the text.

STYLE=st

Is the default font style to be used for the text.

COLOR=c

Is the default font color to be used for the text.

WRAP=ON

Specifies that the text should wrap when it reaches the end of the text object
bounding box.

DIMENSION=(xdimydim)

Specifies the size of the text object bounding box (in current UNITs).

LINESPACING=linesoption

Determines the amount of vertical space between lines of text in a paragraph. Two
types of LINESPACING attributes are supported:

LINESPACING={SINGLE|1.5LINES|DOUBLE}

or

Creating Reports With TIBCO® WebFOCUS Language

 897

Creating a Compound Report

LINESPACING=type(value)

where:

SINGLE

Accommodates the largest font in that line, plus a small amount of extra space. The
amount of extra space varies depending on the font used. SINGLE is the default
option.

1.5LINES

Is one-and-one-half times that of single line spacing.

DOUBLE

Is twice that of single line spacing.

type(value)

Can be one of the following where value is a positive number:

Type

Value

Example

MULTIPLE

The percentage by which to
increase or decrease the line
space.

LINESPACING=MULTIPLE(1.2)
increases line space by 20
percent.

MIN

EXACT

The minimum line space (in
the unit specified by UNITS
parameter) needed to fit the
largest font on the line.

The fixed line space (in the
unit specified by UNITS
parameter) that WebFOCUS
does not adjust.

LINESPACING=MIN(0.5)
provides a minimum line space
of 0.5 inch when UNITS=IN.

LINESPACING=EXACT(.3)
provides a fixed line space of
0.3 inch when UNITS=IN.

Optionally, you may specify the FONT, SIZE, STYLE, and COLOR attributes as you would for
any textual object in a report. For example:

898

10. Linking a Report to Other Resources

OBJECT=STRING, POSITION=(1 1), TEXT='Hello world!',
        FONT=TIMES, SIZE=12, STYLE=BOLD, COLOR=RED, $

Note: A position of a string is measured from its bottom left to allow strings with different
heights to be aligned to a common base-line. However, if WRAP=ON is present, it indicates
that the string should be wrapped to a bounding box whose top-left corner is at (x y) and
whose dimensions are (xdim ydim). In this case, the top left of the text string is positioned
at point (x y).

Images. An image can be drawn as a drawing object by entering the following syntax:

OBJECT=IMAGE, IMAGE=file, POSITION=(x y), DIMENSION=(xdim ydim), $

Note: The image file name=file can be any image file valid in a PDF report. POSITION is
used as with a conventional image, and DIMENSION is used in place of the SIZE attribute
of a conventional image.

Creating Reports With TIBCO® WebFOCUS Language

 899

Creating a Compound Report

Example:

Drawing Objects With Document syntax

The following example shows how drawing objects can be placed inside the COMPOUND
LAYOUT syntax using the GGSALES Master File. Note that a drawing object, like a
COMPONENT, appears on the page whose PAGELAYOUT declaration it follows.

SET PAGE-NUM=OFF
SET SQUEEZE=ON
COMPOUND LAYOUT PCHOLD FORMAT PDF
SECTION=S1, LAYOUT=ON, MERGE=ON, ORIENTATION=LANDSCAPE, $
PAGELAYOUT=1, $
COMPONENT=Sales, TYPE=REPORT, POSITION=(1 1), DIMENSION=(4 4), $
COMPONENT=Budget, TYPE=REPORT, POSITION=(6.25 1), DIMENSION=(4 4), $
OBJECT=IMAGE, IMAGE=gglogo.gif, POSITION=(1 4.5), DIMENSION=(1 1), $
OBJECT=BOX, POSITION=(1 1), DIMENSION=(5 3), BACKCOLOR=GOLDENROD, $
END
SET COMPONENT=Sales
TABLE FILE GGSALES
"Sales report for <REGION"
" "
SUM DOLLARS
BY REGION NOPRINT
BY CATEGORY
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, FONT=HELVETICA, STYLE=BOLD, $
ENDSTYLE
END
SET COMPONENT=Budget
TABLE FILE GGSALES
"Budget report for <REGION"
" "
SUM BUDDOLLARS
BY REGION NOPRINT
BY CATEGORY
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, FONT=HELVETICA, COLOR=BLUE, $
ENDSTYLE
END
COMPOUND END

900

The first page of output is:

10. Linking a Report to Other Resources

Note: A drawing object will not be drawn unless there is at least one COMPONENT in its
PAGELAYOUT.

Syntax:

How to Display Grids With Document Syntax

The SET LAYOUTGRID command can be used as an aid to manually develop report layouts.
Displaying grids superimposes a light one-inch by one-inch grid on the page so that the
locations of the various report components can be verified. Currently, the grid only works in
inches.

Enter the following syntax to display grids:

SET LAYOUTGRID=ON

Reference: Text Formatting Markup Tags for a Text Object

Note: If your text contains any open caret characters (<), you must put a blank space after
each open caret that is part of the text. If you do not, everything following the open caret will
be interpreted as the start of a markup tag and will not display as text.

Font Properties

The font tag supports three attributes: face, size, and color (where the color must be specified
as the hexadecimal number code for the color):

<font face="font" size=[+|-]n color=color_code>text</font>

Creating Reports With TIBCO® WebFOCUS Language

 901

Creating a Compound Report

For example:

<font face="New Century Schoolbook">Test1</font>
<font face="Times" size=12>test2</font>
<font face="Times New Roman" color=#0000FF size=+4>Test3</font>
<font size=-2 face="Times New Roman" color=#0000FF >Test4</font>

Text Styles

The supported text styles are bold, italic, underline, and superscript:

Bold: <b>text</b>

Italic: <i>text</i>

Underline: <u>text</u>

Superscript: <sup>text</sup>

Line Breaks

The line break tag after a portion of text begins the next portion of text on a new line. Note that
there is no closing tag for a line break:

<br>

Text Alignment

The alignment options pertain to wrapped text, as well as specified line breaks. Both horizontal
justification and vertical alignment are supported.

Horizontal Justification

Left Justification:

<left>text</left>

Right Justification:

<right>text</right>

Center Justification:

 <center>text</center>

Full Justification:

 <full>text</full>

Vertical Alignment

902

10. Linking a Report to Other Resources

Top Alignment:

<top>text</top>

Middle Alignment:

<mid>text</mid>

Bottom Alignment:

<bottom>text</bottom>

Unordered (Bullet) List

The unordered (ul) list tag encloses a bullet list. Each item is enclosed in a list item tag (li).
The start tag and end tag for the list must each be on its own line. Each list item must start on
a new line:

<ul>
<li>list item1</li>
<li>list item2</li>
  .
  .
  .
</ul>

By default, the bullet type is disc. You can also specify circle or square:

<ul type=disc>

<ul type=circle>

<ul type=square>

Ordered (Number or Letter) List

The ordered (ol) list tag encloses a list in which each item has a consecutive number or letter.
Each item is enclosed in a list item tag (li). The start tag and end tag for the list must each be
on its own line. Each list item must start on a new line:

<ol>
<li>list item1</li>
<li>list item2</li>
  .
  .
  .
</ol>

Creating Reports With TIBCO® WebFOCUS Language

 903

Creating a Compound Report

By default, Arabic numerals (type=1) are used for the ordering of the list. You can specify the
following types of order:

Arabic numerals (the default): <ol type=1>

Lowercase letters: <ol type=a>

Uppercase letters: <ol type=A>

Lowercase Roman numerals: <ol type=I>

Uppercase Roman numerals: <ol type=I>

Hyperlinks

Hyperlinks can be included within text markup in PDF documents.

The syntax for the anchor markup tag is a subset of the HTML anchor syntax:

<a href="hyperlink">Text to display</a>

where:

hyperlink

Is the hyperlink to jump to when the text is clicked.

Text to display

Is the text to display for the hyperlink.

For example:

<a href="http://www.example.com/help.htm">Click here for help</a>

No other attributes are supported in the anchor markup tag.

Page Numbering and Dates

There are two pseudo-HTML tags for embedding page numbers in text on a Page Master for a
Coordinated Compound Layout report:

Current page number: <ibi-page-number/>

Total number of pages: <ibi-total-pages/>

Note that when MARKUP=ON, space is allocated for the largest number of pages, so there may
be a wide gap between the page number and the text that follows. To remove the extra space
in the text object that has the page numbering tags:

If specific styling of the text object is not required, do not insert markup tags, and turn
MARKUP=OFF.

904

10. Linking a Report to Other Resources

MARKUP=OFF, TEXT='Page <ibi-page-number/> of <ibi-total-pages/> of Sales
Report', $

This displays the following

Page 1 of 100 of Sales Report

If specific styling of the text object is required, you must set MARKUP=ON. With
MARKUP=ON, set WRAP=OFF and do not place any styling tags between the page number
variables within the string. Tags can be used around the complete Page n of m string. The
following code produces a page number string without the extra spaces:

MARKUP=ON, WRAP=OFF, TEXT='<font face="ARIAL" size=10><i>Page <ibi-page-
number/> of <ibi-total-pages/> of Sales Report </i>', $

This displays the following

To display a date in the report output, insert a WebFOCUS date variable in a text object on a
Page Master (such as &DATEtrMDYY) in the text object.

Creating Reports With TIBCO® WebFOCUS Language

 905

Creating a Compound Report

Example:

Formatting a Compound Layout Text Object With Markup Tags

The following request displays a text object with markup tags in a PDF output file.

Note: Text markup syntax cannot contain hidden carriage return or line feed characters. For
purposes of presenting the example in this documentation, line feed characters have been
added so that the sample code wraps to fit within the printed page. To run this example in your
environment, copy the code into a text editor and delete any line feed characters within the
text markup object by going to the end of each line and pressing Delete. In some instances,
you may need to add a space to maintain the structure of the string. For additional information
on displaying carriage returns within the text object see Text Formatting Markup Tags for a Text
Object on page 901.

SET PAGE-NUM=OFF
SET LAYOUTGRID=ON
TABLE FILE GGSALES
BY REGION NOPRINT
ON TABLE PCHOLD AS LINESP1 FORMAT PDF
ON TABLE SET STYLE *
type=report, size=8, $
object=string, position=(1 1), dimension=(7 3), wrap=on, markup=on,
 linespacing=multiple(3),
 text='<b><font face="Arial" size=12>This paragraph is triple-spaced
 (LINESPACING=MULTIPLE(3)):</font></b>
 <full>Our <i>primary</I> goal for fiscal 2006 was to accelerate our
 transformation to customer centricity. In this letter, I’d like to
 give you an update on this work, which contributed to the 22-percent
 increase in earnings from continuing operations we garnered for fiscal
 2006. Since the past is often prologue to the future, I’d like to
 describe how customer centricity is influencing not only our goals for
 fiscal 2007, but also our long-term plans. At Gotham Grinds, customer
 centricity means treating each customer as a unique individual, meeting
 their needs with end-to-end solutions, and engaging and energizing our
 employees to serve them.</full>', $
ENDSTYLE
END

In this request:

No fields from the data source are displayed. Only the text object displays on the output.

The SET LAYOUTGRID command displays a grid to indicate the coordinates and dimensions
of the text object.

The OBJECT=STRING declaration specifies triple spacing: LINESPACING=MULTIPLE(3).

The following text is displayed in boldface, in the Arial font face, and with a font size of 12
(the default is 8 from the TYPE=REPORT declaration):

‘This paragraph is triple-spaced (LINESPACING=MULTIPLE(3)):’

The markup for this formatting is:

906

10. Linking a Report to Other Resources

<b><font face="Arial" size=12>This paragraph is triple-spaced
(LINESPACING=MULTIPLE(3)):</font></b>

Note, however, that the image has been resized to fit the page so the font may appear
smaller:

The remainder of the text is displayed with full justification (left and right sides align):

<full>Our ... </full>

The following markup displays the text ‘primary’ in italics:

<i>primary</I>

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 907

Creating a Compound Report

Example:

Drawing Text and Line objects on a Page Master

The following request places a line on the page master between the header report and the
component reports and places a line and a text string on the bottom of each page:

SET PAGE-NUM=OFF
SET SQUEEZE=ON
COMPOUND LAYOUT PCHOLD FORMAT PDF
SECTION=S1, LAYOUT=ON, MERGE=ON, ORIENTATION=LANDSCAPE, $
PAGELAYOUT=ALL, $
COMPONENT=HEADER, TYPE=REPORT, POSITION=(1 1), DIMENSION=(4 4), $
OBJECT=STRING, POSITION=(1 6.6), MARKUP=ON,
TEXT='<font face="Arial" color=#0000FF size=12> Page <ibi-page-number/>
        </font> ', WRAP=ON, DIMENSION=(4 4),$
OBJECT=LINE, POSITION=(1 2.5), ENDPOINT=(9.5 2.5),
        BORDER-COLOR=BLUE,$
OBJECT=LINE, POSITION=(1 6.5), ENDPOINT=(9.5 6.5),
        BORDER-COLOR=BLUE,$
PAGELAYOUT=1, $
COMPONENT=R1, TYPE=REPORT, POSITION=(1 3), DIMENSION=(4 4), $
COMPONENT=R2, TYPE=REPORT, POSITION=(6 3), DIMENSION=(4 4), $
PAGELAYOUT=2, $
COMPONENT=R3, TYPE=REPORT, POSITION=(4 3), DIMENSION=(4 4), $
END

908

10. Linking a Report to Other Resources

SET COMPONENT=HEADER
TABLE FILE GGSALES
" "
"Report package for <REGION"
BY REGION NOPRINT
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, FONT=HELVETICA, SIZE=20, $
TYPE=REPORT, IMAGE=gglogo.gif, POSITION=(+.25 +.25), $
TYPE=HEADING, LINE=2, ITEM=1, POSITION=1.5, $
ENDSTYLE
END
SET COMPONENT=R1
TABLE FILE GGSALES
"Sales report for <REGION"
" "
SUM DOLLARS/F8M
BY REGION NOPRINT
BY ST
BY CITY
ON TABLE SET STYLE *
TYPE=REPORT, FONT=HELVETICA, COLOR=RED, SQUEEZE=ON, $
ENDSTYLE
END
SET COMPONENT=R2
TABLE FILE GGSALES
"Number of unit sales per product for <REGION"
" "
SUM CNT.UNITS AS 'Number of units sold'
BY REGION NOPRINT
BY PRODUCT
ON TABLE SET STYLE *
TYPE=REPORT, FONT=HELVETICA, COLOR=BLUE, SQUEEZE=ON, $
ENDSTYLE
END
SET COMPONENT=R3
TABLE FILE GGSALES
"Report R3 for <REGION"
BY REGION NOPRINT
SUM DOLLARS BY ST
ON TABLE SET STYLE *
TYPE=REPORT, FONT=HELVETICA, COLOR=GREEN, $
ENDSTYLE
END
COMPOUND END

Creating Reports With TIBCO® WebFOCUS Language

 909

Creating a Compound Report

The first page of output is:

910

The second page of output has the same drawing objects:

10. Linking a Report to Other Resources

Example:

Vertically Aligning Text Markup in PDF Report Output

The following request creates three boxes and places a text string object within each of them:

In the left box, the text is aligned vertically at the top.

In the middle box, the text is aligned vertically at the middle.

Creating Reports With TIBCO® WebFOCUS Language

 911

Creating a Compound Report

In the right box, the text is aligned vertically at the bottom.

Note: Text markup syntax cannot contain hidden carriage return or line feed characters. For
purposes of presenting the example in this documentation, line feed characters have been
added so that the sample code wraps to fit within the printed page. To run this example in your
environment, copy the code into a text editor and delete any line feed characters within the
text markup object by going to the end of each line and pressing Delete. In some instances,
you may need to add a space to maintain the structure of the string. For additional information
on displaying carriage returns within the text object see Text Formatting Markup Tags for a Text
Object on page 901.

SET PAGE-NUM=OFF
TABLE FILE GGSALES
BY REGION NOPRINT
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
type=report, font=arial, size=10, $
object=box, position=(1 1), dimension=(6 1), $
object=line, position=(3 1), endpoint=(3 2), $
object=line, position=(5 1), endpoint=(5 2), $
object=string, text='<top>Vertically aligned text within a text object
using top alignment.</top>', position=(1.05 1), dimension=(2 1),
linespacing=exact(.15), markup=on, wrap=on, $
object=string, text='<mid>Vertically aligned text within a text object
using middle alignment.</mid>', position=(3.05 1), dimension=(2 1),
linespacing=exact(.15), markup=on, wrap=on, $
object=string, text='<bottom>Vertically aligned text within a text object
using bottom alignment.</bottom>', position=(5.05 .9), dimension=(2
1),linespacing=exact(.15), markup=on, wrap=on, $
ENDSTYLE
END

The output is:

Reference: Coordinated Compound Layout Reports With Missing Data

A Coordinated Compound Layout report is comprised of individual component reports or graphs
with a common first sort field. The compound procedure generates an output document with a
separate page (or set of pages) for each individual value of the sort field, with the embedded
components segmented to display the data that corresponds to that sort field value.

912

10. Linking a Report to Other Resources

A Coordinated Compound Layout report page is generated in the designated page layout for
every sort field value found in at least one of the component reports, presenting the
appropriate data for those components where data exists for that value, and presenting an
empty component report where data does not exist.

The way an empty component is represented on the report page is dependent on how the
component positioning is defined within the Coordinated Compound Layout report.
Components can be defined with absolute positioning or relative to other components in the
layout. If the empty component and subsequent components on the page are defined with
absolute positioning, the empty component report will display as blank space in the designated
location. If relative positioning is defined between the empty component and subsequent
components, the subsequent components will float up on the page, and no empty space will
be displayed in the area defined for the empty component.

In compound reports with relative positioning defined between reports, when an empty report
is encountered, the report following the empty report is positioned vertically relative to the
bottom of the last non-empty report and horizontally relative to the page margin. This means
that when a report contains no data, the subsequent report will float up (vertically) and begin
relative to the previous report but it will not move horizontally on the page relative to either of
the previous reports

Using POSITION = (X Y), the placement of a report is designated by the left coordinate
(X = horizontal) and the top coordinate (Y = vertical). Each of these coordinates can be defined
independently as relative to the previous report or in a fixed position on the page.

To define positioning so that the report floats up on the page to replace the empty report but is
anchored in a fixed left position on the page, you can define the Y coordinate (top) as relative
and anchor the X coordinate (left). To anchor one of the position coordinates, change the
reference from a relative position (+/-) to an absolute position. For example:

Both coordinates relative: POSITION(+0.003 +0.621)

Anchor horizontal / flow vertical: POSITION( 0.520 +0.621)

You do not need to change or add any WebFOCUS syntax to your request in order to take
advantage of this feature. You will, however, want to pay attention to how you select and relate
the data within your coordinated components to ensure you are generating the desired output.

Example:

Setup: Creating a Coordinated Compound Report With Missing Data

In this example, we will create a set of statements reporting the outstanding inventory orders
for a select group of stores. Each store may have unfilled orders in any of three inventory
categories: Food, Coffee, and Gifts.

Creating Reports With TIBCO® WebFOCUS Language

 913

Creating a Compound Report

To demonstrate how this works we will first build a set of data files: a header file containing
contact information for the selected set of stores, and transaction files for each inventory
category. We are selecting specific data to demonstrate how this will work when different
component reports are empty.

After creating the data files, we will build four component reports, one to display the header
information and one for each inventory category.

Finally, we will bring them together in a Coordinated Compound Layout report that merges all of
this information into a single statement page for each store.

Example:

Step 1: Creating the Data Files

The following four data files will be created from a join of the GGORDER and GGSALES data
sources:

Data File
Created

Type of Information Included

Stores included

GGHDR

Store information

R1019, R1020, R1040, R1041

GG1

GG2

GG3

Order transactions for Coffee

R1019, R1040, R1088

Order transactions for Food

R1019, R1020, R1041, R1088

Order transactions for Gifts

R1019, R1020, R1040, R1088

The APP HOLD, JOIN, and DEFINE commands are:

APP HOLD baseapp
JOIN
 GGORDER.ORDER01.STORE_CODE IN GGORDER TO
   UNIQUE GGSTORES.STORES01.STORE_CODE
   IN GGSTORES AS J1
END
DEFINE FILE GGORDER
PRODUCT_CATEGORY/A15=IF (PRODUCT_DESCRIPTION IN
                     ('Biscotti','Croissant','Scone')) THEN 'Food'
                     ELSE IF (PRODUCT_DESCRIPTION IN
                     ('French Roast','Hazelnut','Kona')) THEN 'Coffee' ELSE
'Gifts';
END

914

10. Linking a Report to Other Resources

The following procedure creates the data source GGHDR:

TABLE FILE GGORDER
SUM
     FST.STORE_NAME
     FST.ADDRESS1
     FST.ADDRESS2
     FST.CITY
     FST.STATE
     FST.ZIP
BY STORE_CODE
WHERE STORE_CODE IN ('R1019','R1020','R1040','R1041');
ON TABLE NOTOTAL
ON TABLE HOLD AS GGHDR FORMAT FOCUS INDEX 'STORE_CODE'
END

The following procedure creates the data source GG1:

TABLE FILE GGORDER
PRINT
     QUANTITY
     UNIT_PRICE
     PACKAGE_TYPE
     SIZE
     VENDOR_NAME
     PRODUCT_CATEGORY
BY STORE_CODE
BY ORDER_DATE
BY PRODUCT_DESCRIPTION
WHERE ( PRODUCT_CATEGORY EQ 'Coffee' ) AND ( ORDER_DATE GE '09/01/97' );
WHERE STORE_CODE IN ('R1019','R1040','R1088');
ON TABLE HOLD AS GG1 FORMAT FOCUS INDEX 'STORE_CODE'
END

The following procedure creates the data source GG2:

TABLE FILE GGORDER
PRINT
     QUANTITY
     UNIT_PRICE
     PACKAGE_TYPE
     SIZE
     VENDOR_NAME
     PRODUCT_CATEGORY
BY STORE_CODE
BY ORDER_DATE
BY PRODUCT_DESCRIPTION
WHERE ( PRODUCT_CATEGORY EQ 'Food' ) AND ( ORDER_DATE GE '09/01/97' );
WHERE STORE_CODE IN ('R1019','R1020','R1041','R1088');
ON TABLE HOLD AS GG2 FORMAT FOCUS INDEX 'STORE_CODE'
END

Creating Reports With TIBCO® WebFOCUS Language

 915

Creating a Compound Report

The following procedure creates the data source GG3:

TABLE FILE GGORDER
PRINT
     QUANTITY
     UNIT_PRICE
     PACKAGE_TYPE
     SIZE
     VENDOR_NAME
     PRODUCT_CATEGORY
BY STORE_CODE
BY ORDER_DATE
BY PRODUCT_DESCRIPTION
WHERE ( PRODUCT_CATEGORY EQ 'Gifts' ) AND ( ORDER_DATE GE '09/01/97' );
WHERE STORE_CODE IN ('R1019','R1020','R1040','R1088');
ON TABLE HOLD AS GG3 FORMAT FOCUS INDEX 'STORE_CODE'
END

Example:

Step 2: Creating the Component Reports

The following procedure, GGHDR.FEX, creates the first report component for the Coordinated
Compound Layout report from the GGHDR data source. This will function as a header for each
page of the Compound Layout report. The shared sort field for all of the report components is
STORE_CODE. On each page of the PDF output file, this procedure lists the name and address
of one store:

TABLE FILE GGHDR
BY STORE_CODE NOPRINT
HEADING
"<STORE_NAME "
"<ADDRESS1 "
"<ADDRESS2 "
"<CITY , <STATE   <ZIP "
" "
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
TYPE=HEADING,
     SIZE=10,
     STYLE=BOLD,
     COLOR=BLUE,$
ENDSTYLE
END

916

10. Linking a Report to Other Resources

The following procedure, GGRPT1.FEX, creates the second report component for the
Coordinated Compound Layout report. For the same store code value in the header report, it
displays data from the GG1 data source about the product category Coffee:

TABLE FILE GG1
SUM
     QUANTITY
     UNIT_PRICE
     FST.PACKAGE_TYPE AS ',Package'
     FST.SIZE AS ',Size'
     VENDOR_NAME
BY STORE_CODE AS 'Store'
BY PRODUCT_DESCRIPTION
HEADING
"<PRODUCT_CATEGORY"
" "
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
TYPE=DATA,
     SIZE=10,$
TYPE=TITLE,
     STYLE=BOLD,
     SIZE=10,$
TYPE=HEADING,
     SIZE=10,
     STYLE=BOLD,
    COLOR=RED,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 917

Creating a Compound Report

The following procedure, GGRPT2.FEX, creates the third report component for the Coordinated
Compound Layout report. For the same store code value in the header report, it displays data
from the GG2 data source about the product category Food:

TABLE FILE GG2
SUM
     QUANTITY
     UNIT_PRICE
     FST.PACKAGE_TYPE AS ',Package'
     FST.SIZE AS ',Size'
     VENDOR_NAME
BY STORE_CODE
BY PRODUCT_DESCRIPTION
HEADING
"<PRODUCT_CATEGORY"
" "
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
TYPE=DATA,
    SIZE=10,$
TYPE=TITLE,
     STYLE=BOLD,
     SIZE=10,$
TYPE=HEADING,
     SIZE=10,
     STYLE=BOLD,
     COLOR=RED,$
ENDSTYLE
END

918

10. Linking a Report to Other Resources

The following procedure, GGRPT3.FEX, creates the final report component for the Coordinated
Compound Layout report. For the same store code value in the header report, it displays data
from the GG3 data source about the product category Gifts:

TABLE FILE GG3
SUM
     QUANTITY
     UNIT_PRICE
     FST.PACKAGE_TYPE AS ',Package'
     FST.SIZE AS ',Size'
     VENDOR_NAME
BY STORE_CODE
BY PRODUCT_DESCRIPTION
HEADING
"<PRODUCT_CATEGORY"
" "
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
TYPE=DATA,
     SIZE=10,$
TYPE=TITLE,
     STYLE=BOLD,
     SIZE=10,$
TYPE=HEADING,
     SIZE=10,
     STYLE=BOLD,
     COLOR=RED,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 919

Creating a Compound Report

Example:

Step 3: Building the Coordinated Compound Layout Report

The following procedure, GGCMPD.FEX, combines the four components into a Coordinated
Compound Layout report. The reports and relative positioning for each component is presented
in the following diagram:

920

10. Linking a Report to Other Resources

The Coordinated Compound Layout syntax is:

SET HTMLARCHIVE=ON
COMPOUND LAYOUT PCHOLD FORMAT PDF
UNITS=IN, $
SECTION=section1, LAYOUT=ON, MERGE=ON, ORIENTATION=PORTRAIT,
   PAGESIZE=Letter,  $
PAGELAYOUT=1, NAME='Page layout 1', text='Page layout 1',
   TOC-LEVEL=1, BOTTOMMARGIN=0.5, TOPMARGIN=0.5,  $
COMPONENT='report1', TEXT='report1', TOC-LEVEL=2,
   POSITION=(0.667 1.083), DIMENSION=(3.417 1.412),  $
COMPONENT='report2', TEXT='report2', TOC-LEVEL=2,
   POSITION=(0.837 2.584), DIMENSION=(* *),  $
COMPONENT='report3', TEXT='report3', TOC-LEVEL=2,
   POSITION=(-0.006 +0.084), DIMENSION=(* *),
   RELATIVE-TO='report2', RELATIVE-POINT=BOTTOM-LEFT,
   POSITION-POINT=TOP-LEFT, $
COMPONENT='report4', TEXT='report4', TOC-LEVEL=2,
   POSITION=(+0.010 +0.080), DIMENSION=(* *),
   RELATIVE-TO='report3', RELATIVE-POINT=BOTTOM-LEFT,
   POSITION-POINT=TOP-LEFT, $
END
SET COMPONENT='report1'
-INCLUDE GGHDR.FEX
SET COMPONENT='report2'
-INCLUDE GGRPT1.FEX
SET COMPONENT='report3'
-INCLUDE GGRPT2.FEX
SET COMPONENT='report4'
-INCLUDE GGRPT3.FEX
COMPOUND END

Creating Reports With TIBCO® WebFOCUS Language

 921

Creating a Compound Report

On the first page of the PDF output file, all components have data and appear on the report
output:

922

10. Linking a Report to Other Resources

On the second page, report GGRPT2.FEX did not retrieve any data for the store in the header.
Therefore, the Coffee component is missing. Note that because Component 3 and 4 are
positioned RELATIVE-TO the components defined above them in the Compound Layout syntax,
the Food and Gifts components move up instead of leaving blank space where the Coffee
component would have been:

Creating Reports With TIBCO® WebFOCUS Language

 923

Creating a Compound Report

On page 5, the header report did not retrieve any data for a store code value present in the
other three components. A page is still generated for this store code. Since the second
component (Coffee report) was positioned absolutely in the Compound Layout syntax, not
RELATIVE-TO the first component (header report), the space where the header report would
have been is left blank:

Generating a Table of Contents With BY Field Entries for PPTX and PDF Compound Layout Reports

Using compound layout syntax, you can generate a Table of Contents for a PPTX and PDF
compound report.

924

10. Linking a Report to Other Resources

In PPTX, the Table of Contents can be presented as a Table of Contents page placed at the
beginning of the document. In PDF, the Table of Contents can be presented as either PDF
bookmarks displayed by Adobe Reader®, or as a Table of Contents page placed at the
beginning of the document, or both. Both the Table of Contents entries and the bookmarks (in
PDF) provide links to each of the components and included sort fields. These links position the
reader on the page where the Table of Contents link is located.

Include any report or graph component in the Table of Contents at a specific level by defining a
TOC Description and TOC Level in the compound layout syntax for the component. Additionally,
the BY field values of any of the report components can be presented within the TOC tree
indented one level within the component report entry. BYTOC entries are supported for report
components only (not graph components).

Compound reports defining the Table of Contents page or Bookmarks (in PDF) based on BY
field entries are supported for both non-coordinated (MERGE=OFF) and coordinated reports
(MERGE=ON). For coordinated reports, the primary sort key is presented as the top-level entry
for individual instances of the report, and subsequent keys are presented within the
appropriate components within the tree. These coordinated reports can also be burst into
separate documents by the primary sort key and distributed using ReportCaster.

Table of Contents Features

The Table of Contents (TOC) page shows a summary of the contents of the document, along
with page numbers, and can be printed with the document. The entries in the Table of
Contents enable you to easily navigate to a particular section while viewing the document
online. The entries can link to any component of the compound output (page, report, or graph),
any object (image, text box) within the compound report, and vertical sort field values (BY field
values) within each component report.

The actual content of the Table of Contents is represented as a text element in the compound
layout syntax. When using a Table of Contents page, you can:

Customize the title of the Table of Contents, as well as format all of the text.

Specify a TOC level for each component to be included in the Table of Contents.

Enable TOC page numbering so that each element in the Table of Contents is numbered.
You can also add tab leaders (dots) from the entry to the page number for easier selection
of the contents.

Control which reports and graphs show up in the Table of Contents by customizing the
object properties.

Use hypertext links in the Table of Contents page which enable you to click on an entry and
jump to the specified page in the document.

Creating Reports With TIBCO® WebFOCUS Language

 925

Creating a Compound Report

Note: If the Table of Contents overflows to more than one page at run time, the remaining
content is executed with the same size and dimensions as the first page until the entire TOC
has been output.

Syntax:

How to Generate a Table of Contents in a PPTX Compound Layout Report

The following example creates a Table of Contents page for a compound PPTX report. Each
component is at TOC level 1 and each component has two levels of BY fields under the level 1
entries.

COMPOUND LAYOUT PCHOLD FORMAT PPTX
OBJECT=TOC, NAME='text1',
TEXT='<font face="ARIAL" size=10>Table of Contents</font>',
MARKUP=ON, TOC-NUMBERING=ON, POSITION=(0.854 0.854),
DIMENSION=(7.000 9.500), font='ARIAL', color=RGB(0 0 0),
size=10, METADATA=' TOCTITLE: Table of Contents', $
SECTION=S1, LAYOUT=ON, MERGE=OFF, ORIENTATION=PORTRAIT, $
PAGELAYOUT=1, $
COMPONENT=report1, TEXT='Sales By Product', TOC-LEVEL=1, BYTOC=2,
POSITION=(1 1), DIMENSION=(* *), $
COMPONENT=report2, TEXT='Sales By Region', TOC-LEVEL=1, BYTOC=2,
POSITION=(+0.00 +0.519), DIMENSION=(* *), RELATIVE-TO='report1',
RELATIVE-POINT=BOTTOM-LEFT, POSITION-POINT=TOP-LEFT, $
END
SET COMPONENT=report1
TABLE FILE GGSALES
SUM DOLLARS/F8M
BY CATEGORY
BY PRODUCT
BY REGION
BY ST
HEADING
"Sales by Category"
ON TABLE HOLD FORMAT PPTX
ON TABLE SET STYLE *
TYPE=REPORT, SQUEEZE=ON, $
ENDSTYLE
END
SET COMPONENT=report2
TABLE FILE GGSALES
SUM DOLLARS/F8M
BY REGION
BY ST
BY CATEGORY
BY PRODUCT
HEADING
"Sales by Region"
ON TABLE HOLD FORMAT PPTX
ON TABLE SET STYLE *
TYPE=REPORT, SQUEEZE=ON, $
ENDSTYLE
END
COMPOUND END

926

10. Linking a Report to Other Resources

The output shows that each component report is at Table of Contents level 1 and has two
levels of sort fields under it, as shown in the following image. For the Sales by Product report,
the BY fields are Category and Product. For the Sales by Region report, the BY fields are
Region and State. Each entry in the Table of Contents is a link to the page containing that
value.

Creating Reports With TIBCO® WebFOCUS Language

 927

Creating a Compound Report

From PowerPoint presentation view, clicking any entry on the Table of Contents page opens the
page containing that entry. For example, clicking the Sales by Region Southeast entry displays
the following page.

928

10. Linking a Report to Other Resources

Syntax:

How to Generate a Table of Contents in a PDF Compound Layout Report

You can generate bookmarks, a Table of Contents page, or both by including the BOOKMARKS
and/or TOC object in the compound layout syntax. Then in the component definitions, specify
the Table of Contents level and description and, optionally, the BYTOC levels.

TOC Attributes

COMPOUND LAYOUT PCHOLD FORMAT PDF
[OBJECT=BOOKMARKS, $]
[OBJECT=TOC, NAME='text1',
   TEXT='<font face="font1" size=sz1>Table of Contents</font>',
   MARKUP=ON, TOC-NUMBERING={OFF|ON}, POSITION=(xy), [TOC-FILL=DOTS,]
   DIMENSION=(mn),
   font='font2', color={color|RGB(rgb)}, size=sz2,
   METADATA=' TOCTITLE: Table of Contents', $]

where:

OBJECT=BOOKMARKS

Generates PDF bookmarks for the Table of Contents entries specified in the COMPONENT
declarations.

OBJECT=TOC

Generates a Table of Contents page for the Table of Contents entries specified in the
COMPONENT declarations.

NAME='text1'

Specifies a name for the Table of Contents page item.

TEXT='<font face="font1" size=sz1>Table of Contents</font>'

Specifies the title and text characteristics for the Table of Contents title. In order for this
information to be interpreted correctly, the MARKUP=ON attribute must be specified. The
text will not wrap and must fit within the width of the overall text element.

MARKUP=ON

Causes the markup tags used with the Table of Contents title to be interpreted as
formatting options, not as text.

TOC-NUMBERING={OFF|ON}

Specifies whether the entries on the Table of Contents page are numbered. ON is the
default value.

POSITION=(xy)

Defines the x and y coordinates for the object on the page.

DIMENSION=(ab)

Defines the size of the bounding box for the object.

Creating Reports With TIBCO® WebFOCUS Language

 929

Creating a Compound Report

font='font2', color={color|RGB(rgb)},size=sz2,

Specifies text characteristics for the Table of Contents body. If omitted, the attributes are
taken from the TEXT attribute.

TOC-FILL=DOTS

Places tab leader dots from the entry to the page number. If this attribute is not included,
the entry and the page number are separated by blank space.

Component Entries

COMPONENT=component1, TITLE='title1', TOC-LEVEL=n, [BYTOC=m,]
   POSITION=(xy),DIMENSION=(ab), $

where:

component1

Is a component to be included in the Table of Contents.

title1

Is the title for the component to be used as the TOC entry.

TOC-LEVEL=n

Defines n as the Table of Contents level for the report, graph, or page layout object. This
option defines the hierarchical order of objects within the Table of Contents.

0 = the object is not shown in the Table of Contents.

1 = the object is shown as a first level item in the Table of Contents.

2 = the object is shown as a second level item in the Table of Contents and so on.

BYTOC=m

Specifies the number of BY fields to be included within the current component entry (m).

POSITION=(xy)

Defines the x and y coordinates for the object on the page.

DIMENSION=(ab)

Defines the size of the bounding box for the object.

Reference: Usage Notes for Table of Contents

General Notes

The Table of Contents entry is a link to the overall page, not a direct link to the location of
the selected data element on the page.

930

10. Linking a Report to Other Resources

Reports used for headings or footings on overflow pages (DisplayOn=OVERFLOW-ONLY)
should not be included in any TOC or BYTOC entries. These components will generate
duplicate entries in the Table of Contents because they are repeated on the second page
and all subsequent pages of a given page layout based on page count rather than sort field
values.

For an uncoordinated document, the TOC presents all of the page layouts and components
designated in the TOC parameters.

For a coordinated document, the TOC presents a reference to each of the coordinated sort
fields, with a link to the first page of the associated pages for that common sort field.

BYTOC Notes

If the BYTOC value designated is greater than the count of BY fields in the component
report, the value defaults to the total count of available BY fields.

Any valid field that can be used as a BY field can be used in a BYTOC entry, including those
taken directly from a data source or created in a DEFINE.

BY fields designated not to be displayed within the body of the component report (NOPRINT
fields) will still be displayed within the Table of Contents.

The TOC-level values defined cannot skip levels. Any skip in level will cause the bookmarks
below that level not to display.

Example:

Creating Bookmarks and a Table of Contents Page

The following example has two component reports. Both PDF bookmarks and a Table of
Contents page are generated. Each component is at TOC level 1 and each has two levels of BY
fields under the Level 1 entries:

COMPOUND LAYOUT PCHOLD FORMAT PDF
OBJECT=BOOKMARKS, $
OBJECT=TOC, NAME='text1',
  TEXT='<font face="ARIAL" size=10>Table of Contents</font>',
  MARKUP=ON, TOC-NUMBERING=ON, POSITION=(0.854 0.854),
  DIMENSION=(7.000 9.500), font='ARIAL', color=RGB(0 0 0),
  size=10, METADATA=' TOCTITLE: Table of Contents', $
SECTION=S1, LAYOUT=ON, MERGE=OFF, ORIENTATION=PORTRAIT, $
PAGELAYOUT=1, $
COMPONENT=report1, TEXT='Sales By Product', TOC-LEVEL=1, BYTOC=2,
  POSITION=(1 1), DIMENSION=(* *), $
COMPONENT=report2, TEXT='Sales By Region', TOC-LEVEL=1, BYTOC=2,
  POSITION=(+0.00 +0.519), DIMENSION=(* *), RELATIVE-TO='report1',
  RELATIVE-POINT=BOTTOM-LEFT, POSITION-POINT=TOP-LEFT, $
END

Creating Reports With TIBCO® WebFOCUS Language

 931

Creating a Compound Report

SET COMPONENT=report1
TABLE FILE GGSALES
SUM DOLLARS/F8M
BY CATEGORY
BY PRODUCT
BY REGION
BY ST
HEADING
"Sales by Category"
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, SQUEEZE=ON, $
ENDSTYLE
END

SET COMPONENT=report2
TABLE FILE GGSALES
SUM DOLLARS/F8M
BY REGION
BY ST
BY CATEGORY
BY PRODUCT
HEADING
"Sales by Region"
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, SQUEEZE=ON, $
ENDSTYLE
END
COMPOUND END

932

10. Linking a Report to Other Resources

The output shows that each component reports is at Table of Contents level 1 and has two
levels of sort fields under it. For the Sales by Product report, the BY fields are Category and
Product. For the Sales by Region report, the BY fields are Region and State. Each entry in the
Table of Contents is a link to the page containing that value:

Creating Reports With TIBCO® WebFOCUS Language

 933

Creating a Compound Report

Clicking any entry on the Table of Contents page or in the bookmarks pane opens the page
containing that entry. For example, clicking the Sales by Region/Southeast entry opens the
following page:

Creating a Compound PDF or PS Report

Compound reports combine multiple reports into a single PDF or PS file. The first PDF or PS
report defines the format for the concatenated report, enabling you to intersperse intermediate
reports of other formats into one encompassing report. Using compound reports, you can
gather data from different data sources and combine reports into one governing report that
runs each request and concatenates the output into a single PDF or PS file.

You can then run or distribute the report with ReportCaster, which displays the compound PDF
report in Adobe Reader or sends the compound PS report directly to a printer. See the
ReportCaster documentation for details about this product.

This is supported with styled formats, such as PDF, PS, EXL2K, or XLSX.

For information about creating Drill Through PDF Compound Reports, see How to Create a Drill
Through in a PDF Compound Report on page 956. For information about creating Excel
Compound Reports, see Creating a Compound Excel Report Using EXL2K on page 943.

934

Syntax:

How to Display Compound Reports

For a compound report that may contain different report types, use the syntax

10. Linking a Report to Other Resources

SET COMPOUND= {OPEN|CLOSE} [NOBREAK]

or

ON TABLE SET COMPOUND {OPEN|CLOSE}

Note that when you are using this syntax, you must also include the following code to identify
the display format of each of the reports to be concatenated:

ON TABLE {PCHOLD|HOLD|SAVE} [AS name] FORMAT formatname

If all of the reports in the compound set are of the same type, either PDF or PS, you can use
the following, more compact, syntax

ON TABLE {PCHOLD|HOLD|SAVE} [AS name] FORMAT {PDF|PS} {OPEN|CLOSE}
[NOBREAK]

where:

name

Is the name of the generated file. The name is taken from the first request in the
compound report. If no name is specified in the first report, the name HOLD is used.

OPEN

Is specified with the first report, and begins the concatenation process. A report that
contains the OPEN attribute must be PDF or PS format.

CLOSE

Is specified with the last report, and ends the concatenation process.

NOBREAK

Is an optional phrase that suppresses page breaks. By default, each report is displayed on
a separate page.

You can use NOBREAK selectively in a request to control which reports are displayed on
the same page.

Creating Reports With TIBCO® WebFOCUS Language

 935

Creating a Compound Report

Note:

Compound reports cannot be nested.

You can save or hold the output from a compound report. For details, see Saving and
Reusing Your Report Output on page 471.

Multi-Pane reports cannot be used in a Compound Report.

Example:

Creating a Compound PDF Report

The following illustrates how to combine three separate PDF reports into one by creating a
compound report. Notice that:

Report 1 specifies ON TABLE PCHOLD FORMAT PDF OPEN. This defines the report as the
first report and sets the format for the entire compound report as PDF.

Report 2 species only the format, ON TABLE PCHOLD FORMAT PDF.

Report 3 specifies ON TABLE PCHOLD FORMAT PDF CLOSE. This defines the report as the
last report.

Note that in this example, all reports are set to PDF format. However, when you create a
compound report, only the first report must be in either PDF or PS format. Subsequent reports
can be in any styled format. For an illustration, see How to Embed Graphics in a Compound
Report on page 938.

Report 1:

SET PAGE-NUM=OFF
TABLE FILE CENTORD
HEADING
"Sales Report"
" "
SUM LINEPRICE
BY PRODCAT
ON TABLE SET STYLE *
TYPE=HEADING, SIZE=18, $
ENDSTYLE
ON TABLE PCHOLD FORMAT PDF OPEN NOBREAK
END

936

10. Linking a Report to Other Resources

Report 2:

TABLE FILE CENTORD
HEADING
"Inventory Report"
" "
SUM QUANTITY
BY PRODCAT
ON TABLE SET STYLE *
TYPE=HEADING, SIZE=18, $
ENDSTYLE
ON TABLE PCHOLD FORMAT PDF NOBREAK
END

Report 3:

TABLE FILE CENTORD
HEADING
"Cost of Goods Sold Report"
" "
SUM LINE_COGS
BY PRODCAT
ON TABLE SET STYLE *
TYPE=HEADING, SIZE=18, $
ENDSTYLE
ON TABLE PCHOLD FORMAT PDF CLOSE
END

Creating Reports With TIBCO® WebFOCUS Language

 937

Creating a Compound Report

The output displays as a PDF report. Because the syntax for reports 1 and 2 contain the
NOBREAK command, the three reports appear on a single page. (Without NOBREAK, each
report displays on a separate page.)

Syntax:

How to Embed Graphics in a Compound Report

You can embed a graphic, such as a logo or a WebFOCUS graph captured as a GIF file, in a
compound report. The graphic file must be embedded in a particular report within the set of
compound reports.

To save a graph as a graphic image, include the following syntax in your graph request:

HOLD FORMAT GIF

For details on saving a graph as an image file, see Creating a Graph on page 1743.

938

10. Linking a Report to Other Resources

To embed a graphic in a compound report, you must identify the image file in the StyleSheet
declaration of the report in which you want to include it, along with size and position
specifications if desired. For details about embedding and positioning graphics in reports, see
Adding an Image to a Report on page 1462.

Example:

Combining Report Formats and Graphs in a Compound Report

This request generates a compound report from three different report types (PDF, HTML, and
EXL2K), and embeds a graph in each report. Notice that each graph is saved as a GIF file in
the graph request. The graph is then identified, sized, and positioned within the StyleSheet
declaration (TYPE=REPORT, IMAGE=graphname...) of the report in which it is being embedded).
Variations on the SET COMPOUND= syntax (OPEN, NOBREAK, CLOSE) combine the three
reports on the same page. Key lines of code are highlighted in the following request.

Report 1:

SET GRMERGE = ON
GRAPH FILE SHORT
SUM PROJECTED_RETURN AS 'Return on Investment'
BY HOLDER
ACROSS CONTINENT
ON GRAPH SET LOOKGRAPH 3D_BAR
ON GRAPH SET GRAPHEDIT SERVER
ON GRAPH HOLD AS SLSGRPH1 FORMAT GIF
END

SET COMPOUND='OPEN NOBREAK'
TABLE FILE SHORT
SUM PROJECTED_RETURN AS 'Return on Investment'
BY CONTINENT
BY HOLDER
HEADING
"Investment Report"
" "

ON TABLE SET STYLE *
TYPE=DATA, BACKCOLOR=( BY=B2 'SILVER' 'WHITE' ), $
TYPE=HEADING, SIZE=14, STYLE=BOLD, $
TYPE=REPORT, IMAGE=SLSGRPH1.gif, POSITION=(4.5 0.5), SIZE=(3.5 2.5), $
ENDSTYLE
ON TABLE PCHOLD FORMAT PDF

END

Creating Reports With TIBCO® WebFOCUS Language

 939

Creating a Compound Report

Report 2:

GRAPH FILE TRADES
SUM AMOUNT
BY CONTINENT
ON GRAPH SET LOOKGRAPH PIE
ON GRAPH SET GRAPHEDIT SERVER
ON GRAPH HOLD AS TRDSGR1 FORMAT GIF
END

SET COMPOUND=NOBREAK
TABLE FILE TRADES
SUM AMOUNT AS 'Amount'
BY CONTINENT AS 'Continent'
BY REGION AS 'Region'
HEADING
"Trades Report"
" "
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
 TYPE=DATA, BACKCOLOR=( BY=B2 'SILVER' 'WHITE' ), $
TYPE=HEADING, SIZE=14, STYLE=BOLD, $
TYPE=REPORT, IMAGE=TRDSGR1.gif, POSITION=(4 3), SIZE=(4 2.5), $
ENDSTYLE
ON TABLE PCHOLD FORMAT HTML
END

940

10. Linking a Report to Other Resources

Report 3:

GRAPH FILE SHORT
SUM BALANCE
BY CONTINENT
ON GRAPH SET LOOKGRAPH 3D_BAR
ON GRAPH SET GRAPHEDIT SERVER
ON GRAPH SET STYLE *
TYPE=DATA, COLOR=RED,$
ENDSTYLE
ON GRAPH HOLD AS BALGR1 FORMAT GIF
END

SET COMPOUND=CLOSE
TABLE FILE SHORT
SUM BALANCE AS 'Balance'
BY CONTINENT AS 'Continent'
BY REGION AS 'Region'
HEADING
"Balance by Region"
" "
ON TABLE SET STYLE *
 TYPE=DATA, BACKCOLOR=( BY=B2 'SILVER' 'WHITE' ), $
TYPE=HEADING, SIZE=14, STYLE=BOLD, $
TYPE=REPORT, IMAGE=BALGR1.gif, POSITION=(4 6), SIZE=(4 2.5), $
ENDSTYLE
ON TABLE PCHOLD FORMAT EXL2K
END

Creating Reports With TIBCO® WebFOCUS Language

 941


Creating a Compound Report

The output is:

942

Creating a Compound Excel Report Using EXL2K

10. Linking a Report to Other Resources

Excel Compound Reports generate multiple worksheet reports using the EXL2K output format.

The syntax of Excel Compound Reports is identical to that of PDF Compound Reports. By
default, each of the component reports from the compound report is placed in a new Excel
worksheet (analogous to a new page in PDF). If the NOBREAK keyword is used, the next report
follows the current report on the same worksheet (analogous to starting the report on the
same page in PDF).

Output, whether sent to the client using PCHOLD or saved in a file using HOLD, is generated in
Microsoft Web Archive format. This format is labeled Single File Web Page in the Excel Save As
dialog. Excel provides the conventionally given file suffixes: .mht or .mhtml. WebFOCUS uses
the same .xht suffix that is used for EXL2K reports.Since the output is always a single file, it
can be easily distributed using ReportCaster.

The components of an Excel compound report can be FORMULA or PIVOT reports (subject to
the restrictions). They cannot be Table of Contents (TOC) reports.

Note: Excel 2002 (Office XP) or higher must be installed. Excel Compound Reports will not
work with earlier versions of Excel since they do not support the Web Archive file format.

Reference: Guidelines for Using the OPEN, CLOSE, and NOBREAK Keywords and SET COMPOUND

As with PDF, the keywords OPEN, CLOSE, and NOBREAK are used to control Excel compound
reports. They can be specified with the HOLD or PCHOLD command or with a separate SET
COMPOUND command.

OPEN is used on the first report of a sequence of component reports to specify that a
compound report be produced.

CLOSE is used to designate the last report in a compound report.

NOBREAK specifies that the next report be placed on the same worksheet as the current
report. If it is not present, the default behavior is to place the next report on a separate
worksheet.

NOBREAK may appear with OPEN on the first report, or alone on a report between the first
and last reports. (Using CLOSE is irrelevant, since it refers to the placement of the next
report, and no report follows the final report on which CLOSE appears.)

When used with the HOLD/PCHOLD syntax, the compound report keywords OPEN, CLOSE,
and NOBREAK must appear immediately after FORMAT EXL2K, and before any additional
keywords, such as FORMULA or PIVOT. For example, you can specify:

ON TABLE PCHOLD FORMAT EXL2K OPEN

Creating Reports With TIBCO® WebFOCUS Language

 943

Creating a Compound Report

ON TABLE HOLD AS MYHOLD FORMAT EXL2K OPEN NOBREAK

ON TABLE PCHOLD FORMAT EXL2K NOBREAK FORMULA

ON TABLE HOLD FORMAT EXL2K CLOSE PIVOT PAGEFIELDS COUNTRY

As with PDF compound reports, compound report keywords can be alternatively specified
using SET COMPOUND:

SET COMPOUND = OPEN

SET COMPOUND = 'OPEN NOBREAK'

SET COMPOUND = NOBREAK

SET COMPOUND = CLOSE

Reference: Guidelines for Producing Excel Compound Reports Using EXL2K

Pivot Tables and NOBREAK. Pivot Table Reports may appear in compound reports, but they
may not be combined with another report on the same worksheet using NOBREAK.

Naming of Worksheets. The default worksheet tab names will be Sheet1, Sheet2, and so
on. You have the option to specify a different worksheet tab name by using the TITLETEXT
keyword in the stylesheet. For example:

TYPE=REPORT, TITLETEXT='Summary Report', $

Excel limits the length of worksheet titles to 31 characters. The following special characters
cannot be used: ':', '?', '*', and '/'.

File Names and Formats. The output file name (AS name, or HOLD by default) is obtained
from the first report of the compound report (the report with the OPEN keyword). Output file
names on subsequent reports are ignored.

The HOLD FORMAT syntax used in the first component report in a compound report applies
to all subsequent reports in the compound report, regardless of their format.

NOBREAK Behavior. When NOBREAK is specified, the following report appears on the row
immediately after the last row of the report with the NOBREAK. If additional spacing is
required between the reports, a FOOTING or an ON TABLE SUBFOOT can be placed on the
report with the NOBREAK, or a HEADING or an ON TABLE SUBHEAD can be placed on the
following report. This allows the most flexibility, since if blank rows were added by default
there would be no way to remove them.

944

Example:

Creating a Simple Compound Report Using EXL2K

10. Linking a Report to Other Resources

SET PAGE-NUM=OFF
TABLE FILE CAR
HEADING
"Sales Report"
" "
SUM SALES
BY COUNTRY
ON TABLE SET STYLE *
type=report, titletext='Sales Rpt', $
type=heading, size=18, $
ENDSTYLE
ON TABLE PCHOLD AS EX1 FORMAT EXL2K OPEN
END

TABLE FILE CAR
HEADING
"Inventory Report"
" "
SUM RC
BY COUNTRY
ON TABLE SET STYLE *
type=report, titletext='Inv. Rpt', $
type=heading, size=18, $
ENDSTYLE
ON TABLE HOLD AS EX1 FORMAT EXL2K
END

TABLE FILE CAR
HEADING
"Cost of Goods Sold Report"
" "
SUM DC
BY COUNTRY
ON TABLE SET STYLE *
type=report, titletext='Cost Rpt', $
type=heading, size=18, $
ENDSTYLE
ON TABLE HOLD AS EX1 FORMAT EXL2K CLOSE
END

Creating Reports With TIBCO® WebFOCUS Language

 945

Creating a Compound Report

The output for each tab in the Excel worksheet is:

946

10. Linking a Report to Other Resources

Example:

Creating a Compound Report With Pivot Tables and Formulas

SET PAGE-NUM=OFF
TABLE FILE CAR
HEADING
"Sales Report"
" "
PRINT RCOST
BY COUNTRY
ON TABLE SET STYLE *
type=report, titletext='Sales Rpt', $
type=heading, size=18, $
ENDSTYLE
ON TABLE PCHOLD AS PIV1 FORMAT EXL2K OPEN
END

Creating Reports With TIBCO® WebFOCUS Language

 947

Creating a Compound Report

TABLE FILE CAR
HEADING
"Inventory Report"
" "
PRINT SALES
BY COUNTRY
ON TABLE SET STYLE *
type=report, titletext='Inv. Rpt', $
type=heading, size=18, $
ENDSTYLE
ON TABLE HOLD AS PPPP FORMAT EXL2K PIVOT
PAGEFIELDS TYPE SEATS
CACHEFIELDS MODEL MPG RPM
END

TABLE FILE CAR
SUM RCOST
BY COUNTRY BY CAR BY MODEL BY TYPE BY SEATS SUMMARIZE
ON MODEL SUB-TOTAL
ON TABLE HOLD AS XFOCB FORMAT EXL2K FORMULA
END

TABLE FILE CAR
HEADING
"Cost of Goods Sold Report"
" "
PRINT DCOST
BY COUNTRY
ON TABLE SET STYLE *
type=report, titletext='Cost Rpt', $
type=heading, size=18, $
ENDSTYLE
ON TABLE HOLD AS ONE FORMAT EXL2K CLOSE PIVOT
PAGEFIELDS RCOST
CACHEFIELDS MODEL TYPE SALES ACCEL SEATS
END

948

The output for each tab in the Excel worksheet is:

10. Linking a Report to Other Resources

Creating Reports With TIBCO® WebFOCUS Language

 949

Creating a Compound Report

950

10. Linking a Report to Other Resources

Example:

Creating a Compound Report Using NOBREAK

In this example, the first two reports are on the first worksheet, and the last two reports are on
the second worksheet, since NOBREAK appears on both the first and third reports.

TABLE FILE GGSALES
HEADING
"Report 1: Coffee - Budget"
SUM BUDDOLLARS BUDUNITS COLUMN-TOTAL AS 'Total'
BY REGION
IF CATEGORY EQ Coffee
ON TABLE PCHOLD FORMAT EXL2K OPEN NOBREAK
ON TABLE SET STYLE *
type=report, font=Arial, size = 10, style=normal, $
type=title, style=bold, $
type=heading,   size=12, style=bold, color=blue, $
type=grandtotal,  style=bold,  $
ENDSTYLE
END

TABLE FILE GGSALES
HEADING
" "
"Report 2: Coffee - Actual "
SUM DOLLARS UNITS COLUMN-TOTAL AS 'Total'
BY REGION
IF CATEGORY EQ Coffee
ON TABLE PCHOLD FORMAT EXL2K
ON TABLE SET STYLE *
type=report, font=Arial, size=10, style=normal, $
type=grandtotal,  style=bold, $
type=heading,  size=12, style=bold, color=blue, $
ENDSTYLE
END

TABLE FILE GGSALES
HEADING
"Report 3: Food - Budget"
SUM BUDDOLLARS BUDUNITS COLUMN-TOTAL AS 'Total'
BY REGION
IF CATEGORY EQ Food
ON TABLE PCHOLD FORMAT EXL2K NOBREAK
ON TABLE SET STYLE *
type=REPORT, font=Arial, size=10, style=normal, $
type=HEADING,  style=bold, size=12, color=blue, $
type=title, style=bold, $
type=grandtotal,  style=bold,  $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 951

Creating a Compound Report

TABLE FILE GGSALES
HEADING
" "
"Report 4: Food - Actual"
SUM DOLLARS UNITS COLUMN-TOTAL AS 'Total'
BY REGION
IF CATEGORY EQ Food
ON TABLE PCHOLD FORMAT EXL2K CLOSE
ON TABLE SET STYLE *
type=report, font=Arial, size=10,  $
type=title, style=bold, $
type=heading,size=12, style=bold,  color=blue,$
type=grandtotal, style=bold,  $
ENDSTYLE
END

952

The output is:

10. Linking a Report to Other Resources

Creating Reports With TIBCO® WebFOCUS Language

 953

Creating a PDF Compound Report With Drill Through Links

Creating a PDF Compound Report With Drill Through Links

A common technique in business reporting is to create two related reports:

Summary Report. Contains condensed information for a category such as a business
account, with summed data such as total balances and total sales.

Detail Report. For specified fields in the associated summary report, a detail report
contains all the component values that contributed to each summary field value.

Drill Through provides a way to easily relate the data in these two types of reports. For
example, a user scanning a summary report account may see an unusual figure in one of the
accounts, requiring examination of the specific data behind that figure.

There are two forms of Compound Drill Through reports:

Legacy Drill Through Compound Reports. These reports use the legacy compound report
syntax (PCHOLD with the OPEN and CLOSE options) to create the compound report.

Drill Through Compound Layout Reports. These reports use document syntax declarations
to create the compound procedure and define which reports will be related through
hyperlinks.

In both types of Compound Drill Through reports, the syntax for creating hyperlinks between
reports within the PDF file are exactly the same.

Reference: Drill Through and Drill Down Compared

Using Drill Down, you can construct a summary report in which clicking a hyperlink displays
detail data. A Drill Down is implemented dynamically. Clicking a hyperlink causes a new report
to run. The detail report typically displays only the detail data for a selected field on the
summary report.

In contrast, Drill Through reports are static. Drill Through creates a PDF document that
contains the summary report plus the detail report, with the detail report containing all the
detail data for designated fields in the summary report. Clicking a Drill Through hyperlink
navigates internally in the PDF file. No additional reports are run. You can save the PDF file to
disk or distribute it using ReportCaster. When opened with Adobe Reader, it retains its full Drill
Through functionality.

Drill Through provides flexibility in the appearance of reports and location of hyperlinks:

Drill Through hyperlinks may appear in headings and subheadings, as well as, in rows of
data.

You can format the reports using a WebFOCUS StyleSheet.

954

10. Linking a Report to Other Resources

You can indicate a hyperlink by color, font, underlining, and so forth.

You can mix conventional Drill Down hyperlinks freely in the same report with Drill Through
hyperlinks.

The PDF file created with Drill Through can consist of more than two reports.

Reference: Use With Other Features

You can use Drill Through with other WebFOCUS features:

Compound reports that contain linked Drill Through reports may also contain unrelated
reports, before or after the Drill Through reports. For example, you can add to the
compound report package a PDF report that contains embedded graphs.

You can add Drill Down and URL hyperlinks to a PDF report that contains Drill Through
hyperlinks.

Since Drill Through reports are standard PDF compound reports packaged into a single PDF
file, you can distribute them using ReportCaster.

Reports with DRILLTHROUGH syntax can be rendered in all other styled output formats:
HTML, PostScript, EXL2K, and so on. In these other formats, the DRILLTHROUGH syntax is
ignored. It is useful, for example, to generate a PostScript version of a Drill Through report,
which is formatted identically to the PDF version, but which you can send directly to a
PostScript printer using ReportCaster or operating system commands.

Drill Through automates the process of navigating quickly and easily from general to
specific information in related reports packaged in a single PDF compound report. Drill
Through syntax sets up hyperlinks that take you from an item in a summary report to a
corresponding item in a detail report.

Procedure: How to Create a Drill Through in a PDF Compound Layout Report

To create a Drill Through in a PDF Compound Layout report:

1. Create the summary report with a DRILLTHROUGH hyperlink.

2. Create the detail report with sort values that match the hyperlink field values.

3. Create the Compound Layout report with page layouts for each component report, and

define a DRILLMAP attribute within the calling report to specify the targets of the drill
through hyperlinks.

Creating Reports With TIBCO® WebFOCUS Language

 955

Creating a PDF Compound Report With Drill Through Links

Procedure: How to Create a Drill Through in a PDF Compound Report

To create a Drill Through in a PDF Compound Report:

1. Create the summary report.

2. Create the detail report.

3. Connect the reports with hyperlinks.

4. Merge the summary and detail reports into a PDF compound report.

Syntax:

How to Specify Drill Through Hyperlinks

TYPE=type, [element,] [styling_attributes,]
     DRILLTHROUGH={DOWN|FIRST}(link_fields) , $

where:

type

Is one of the following StyleSheet types:

DATA

HEADING

FOOTING

SUBHEAD

SUBFOOT

SUBTOTAL

RECAP

element

Is one or more identifying elements allowed in a WebFOCUS StyleSheet and Drill
Through report. An element can describe a specific column (for example,
COLUMN=PRODUCT) or heading item (for example, LINE=2, OBJECT=field, ITEM=3).

styling_attributes

Optionally specify the appearance of the hyperlink (for example, COLOR=RED,
STYLE=BOLD).

DOWN

Links to the next (the following) report.

FIRST

Links to the first Drill Through report in the sequence.

956

10. Linking a Report to Other Resources

link_fields

Specifies blank-delimited link field pairs with the following format:

T1=S1 T2=S2 T3=S3...

T1, T2, and T3 represent column references in the target (linked) report, and S1,
S2, and S3 represent column references in the source (current) report. There may
be more than three pairs.

A column reference can be the name of a field or any of the other symbols valid in
WebFOCUS StyleSheets syntax (for example, Bn, Cn, Pn, Nn, An, subscripted field
name, and so on).

The order of the syntax is similar to Drill Down syntax, in which the parameter pairs
specify the column reference in the current (source) report on the right and the name
of the Dialogue Manager variable in the Drill Down (target) procedure on the left.

If the column reference in the target report is identical to the column reference in the
source report, you can use a single column reference, for example, COUNTRY instead
of COUNTRY=COUNTRY.

Example:

Specifying Drill Through Hyperlinks

The following StyleSheet declaration places a hyperlink on the PRODUCT field on each DATA
line, specifies that the fields to link to the next report are CATEGORY and PRODUCT, specifies
the action DOWN, so that clicking a hyperlink brings you to the location in the next report that
has the corresponding values of the two link fields, and uses the default appearance for the
hyperlinks, which is blue, underlined text. Since the target fields in the detail report have
identical names in the summary report, you can use the notation CATEGORY rather than
CATEGORY=CATEGORY.

TYPE=DATA, COLUMN=PRODUCT, DRILLTHROUGH=DOWN(CATEGORY PRODUCT), $

Syntax:

How to Specify Which Compound Layout Reports Will be Related Through Hyperlinks

The target report is specified in the DRILLMAP attribute of the COMPONENT declaration for the
calling report.

DRILLMAP=((L1 targetreport))

where:

L1

Is the link identifier.

targetreport

Is the component name of hyperlink destination.

Creating Reports With TIBCO® WebFOCUS Language

 957

Creating a PDF Compound Report With Drill Through Links

Note: The double parentheses around the DRILLMAP values are required.

Example:

Sample Component Declarations With DRILLMAP Attributes

The following COMPONENT declaration for REPORT1 specifies a DRILLMAP attribute that points
to REPORT2:

COMPONENT='REPORT1', TEXT='REPORT1', TOC-LEVEL=2,
DRILLMAP=((L1 REPORT2)), POSITION=(0.750 1.083), DIMENSION=(7.000 3.167),
METADATA='Z-INDEX: 100; LEFT: 0.75in; OVERFLOW: auto; WIDTH: 7in;
POSITION: absolute; TOP: 1.083in; HEIGHT: 3.167in', $

The following COMPONENT declaration for REPORT2 specifies a DRILLMAP attribute that points
to REPORT1:

COMPONENT='REPORT2', TEXT='REPORT2', TOC-LEVEL=2,
DRILLMAP=((L1 REPORT1)), POSITION=(0.500 0.667), DIMENSION=(7.417 7.000),
METADATA='Z-INDEX: 100; LEFT: 0.5in; OVERFLOW: auto; WIDTH: 7.417in;
POSITION: absolute; TOP: 0.667in; HEIGHT: 7in', $

Reference: Usage Notes for Drill Through

As of Release 8.2 Version 01, individual component reports containing Drill Through
designations can be run standalone. You will see a warning message in the Message
Viewer indicating that outside of the compound report, the Drill Through will not be active.

Only one Drill Through behavior can be specified per report.

The field specified to contain a Drill Through behavior must also be present in the target
report.

The originating report containing the Drill Through link must be rendered (by the Reporting
Server) prior to the target report. The order of reports must be handled by the user.

Live Drill Through links are only generated for PDF output. Reports with DRILLTHROUGH
syntax can be rendered in all other styled output formats: HTML, PostScript, EXL2K, and so
on. In these other formats, the DRILLTHROUGH syntax is ignored. It is useful, for example,
to generate a PostScript version of a Drill Through report, which is formatted identically to
the PDF version, but which you can send directly to a PostScript printer using ReportCaster
or operating system commands.

Drill Through is only supported for reports (TABLE).

958

10. Linking a Report to Other Resources

Sample Drill Through PDF Compound Reports

The following examples illustrate how to use Drill Through syntax to create a compound report
with a summary and detail report and navigate between them.

Example:

Creating the Summary Report (Step 1)

The following syntax generates a sample summary report:

TABLE FILE GGSALES
SUM UNITS DOLLARS BY CATEGORY BY PRODUCT
ON TABLE PCHOLD FORMAT PDF
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 959

Creating a PDF Compound Report With Drill Through Links

Example:

Creating the Detail Report (Step 2)

The following syntax generates a sample detail report:

The first page of the output is:

SET SQUEEZE=ON
TABLE FILE GGSALES
SUM UNITS BUDUNITS DOLLARS
BY CATEGORY NOPRINT BY PRODUCT NOPRINT
ON CATEGORY PAGE-BREAK
HEADING CENTER
"Category: <CATEGORY"
" "
ON PRODUCT SUBHEAD
"**** Product: <PRODUCT"
ON PRODUCT SUBFOOT
" "
"<25 **** Return to Summary ****"
ON PRODUCT PAGE-BREAK
BY REGION BY CITY
ON TABLE PCHOLD FORMAT PDF
END

960

Example:

Connecting the Reports With Hyperlinks (Step 3)

The example illustrates the following:

10. Linking a Report to Other Resources

When you place a Drill Through hyperlink on a sort-break element, ensure the sort-break is
at least at the level of the last sort field participating in the Drill Through. For example, in
the second report, the Drill Through hyperlink is on the subfooting associated with
PRODUCT rather than the heading (with a sort break) associated with CATEGORY.

Although the code can infer a value of PRODUCT for the CATEGORY heading (you can verify
this by embedding the field <PRODUCT> in the heading), it is always the value of the first
PRODUCT within that CATEGORY. Typically you want a Drill Through hyperlink for each value
of PRODUCT within each CATEGORY.

You do not need to place the hyperlink on an embedded item. You can just as effectively
place it on a text item. Any item in the subfooting is associated with the same values of
CATEGORY and PRODUCT. Similarly, you can place a hyperlink on any field in a DATA line,
and the values of the associated link fields will be identical. Conventional Drill Down
hyperlinks also work this way.

The summary report:

Places a hyperlink on the PRODUCT field on each DATA line.

Specifies that the fields to link to the next report are CATEGORY and PRODUCT. Since the
target fields in the detail report have identical names in the summary report, you can use
the notation CATEGORY rather than CATEGORY=CATEGORY.

Specifies the action DOWN, so that clicking a hyperlink brings you to the location in the
next report that has the corresponding values of the two link fields.

Uses the default appearance for the hyperlinks, which is blue, underlined text.

The summary report is:

TABLE FILE GGSALES
SUM UNITS DOLLARS BY CATEGORY BY PRODUCT
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=DATA, COLUMN=PRODUCT, DRILLTHROUGH=DOWN(CATEGORY PRODUCT), $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 961

Creating a PDF Compound Report With Drill Through Links

The detail report:

Places a hyperlink in the subfooting associated with the link field PRODUCT. Since
CATEGORY is a higher level BY field than PRODUCT, each PRODUCT subheading is also
associated with a unique value of CATEGORY.

Places a hyperlink on the first item of the second line of the subfooting, which is the text
Return to Summary.

Specifies action FIRST, so that clicking the hyperlink jumps to the line in the first (summary)
report that contains the same values of the two link fields CATEGORY and PRODUCT.

Uses the COLOR attribute to display the hyperlink as red, underlined text.

The detail report is:

SET SQUEEZE=ON
TABLE FILE GGSALES
SUM UNITS BUDUNITS DOLLARS
BY CATEGORY NOPRINT BY PRODUCT NOPRINT
ON CATEGORY PAGE-BREAK
HEADING CENTER
"Category: <CATEGORY"
" "
ON PRODUCT SUBHEAD
"**** Product: <PRODUCT"
ON PRODUCT SUBFOOT
" "
"<25 **** Return to Summary ****"
ON PRODUCT PAGE-BREAK
BY REGION BY CITY
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=SUBFOOT, LINE=2, ITEM=1, DRILLTHROUGH=FIRST(CATEGORY PRODUCT),
COLOR=RED, $
ENDSTYLE
END

The next step is the only step that is different for creating a Compound Layout report or a
legacy Compound Report.

Example:

Creating the Compound Layout Report (Step 4)

Perform this version of Step 4 if you are creating a Compound Layout report.

To create the Compound Layout report:

Add a COMPOUND LAYOUT and SECTION declaration to the top of the procedure.

Add PAGELAYOUT and COMPONENT declarations for the two reports. Add DRILLMAP
attributes to the COMPONENT declarations.

962

10. Linking a Report to Other Resources

Add SET COMPONENT commands and the two reports.

End the procedure with a COMPOUND END command:

SET HTMLARCHIVE=ON
COMPOUND LAYOUT PCHOLD FORMAT PDF
UNITS=IN, $
SECTION=section1, LAYOUT=ON, METADATA='0.5^0.5^0.5^0.5', MERGE=OFF,
   ORIENTATION=PORTRAIT, PAGESIZE=Letter,  $
PAGELAYOUT=1, NAME='Page layout 1', text='Page layout 1', TOC-LEVEL=1,
   BOTTOMMARGIN=0.5, TOPMARGIN=0.5, METADATA='BOTTOMMARGIN=0.5,
   TOPMARGIN=0.5,LEFTMARGIN=0,RIGHTMARGIN=0, $
COMPONENT='REPORT1', TEXT='REPORT1', TOC-LEVEL=2,
DRILLMAP=((L1 REPORT2)), POSITION=(0.750 1.083), DIMENSION=(7.000 3.167),
   METADATA='Z-INDEX: 100; LEFT: 0.75in; OVERFLOW: auto; WIDTH: 7in;
   POSITION: absolute; TOP: 1.083in; HEIGHT: 3.167in', $
PAGELAYOUT=2, NAME='Page layout 2', text='Page layout 2', TOC-LEVEL=1,
   BOTTOMMARGIN=0.5, TOPMARGIN=0.5, METADATA='BOTTOMMARGIN=0.5,
   TOPMARGIN=0.5,LEFTMARGIN=0,RIGHTMARGIN=0, $
COMPONENT='REPORT2', TEXT='REPORT2', TOC-LEVEL=2,
DRILLMAP=((L1 REPORT1)), POSITION=(0.500 0.667), DIMENSION=(7.417 7.000),
   METADATA='Z-INDEX: 100; LEFT: 0.5in; OVERFLOW: auto; WIDTH: 7.417in;
   POSITION: absolute; TOP: 0.667in; HEIGHT: 7in', $
END

-* Add Report1 code and SET COMPONENT command
SET COMPONENT='REPORT1'
TABLE FILE GGSALES
SUM UNITS DOLLARS BY CATEGORY BY PRODUCT
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=DATA, COLUMN=PRODUCT, DRILLTHROUGH=DOWN(CATEGORY PRODUCT), $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 963

Creating a PDF Compound Report With Drill Through Links

-* Add report2 code and SET COMPONENT command
SET COMPONENT='REPORT2'
SET SQUEEZE=ON
TABLE FILE GGSALES
SUM UNITS BUDUNITS DOLLARS
BY CATEGORY NOPRINT BY PRODUCT NOPRINT
ON CATEGORY PAGE-BREAK
HEADING CENTER
"Category: <CATEGORY"
" "
ON PRODUCT SUBHEAD
"**** Product: <PRODUCT"
ON PRODUCT SUBFOOT
" "
"<25 **** Return to Summary ****"
ON PRODUCT PAGE-BREAK
BY REGION BY CITY
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=SUBFOOT, LINE=2, ITEM=1, DRILLTHROUGH=FIRST(CATEGORY PRODUCT),
COLOR=RED, $
ENDSTYLE
END
COMPOUND END

Example: Merging Summary and Detail Reports Into a PDF Compound Report (Step 4)

Perform this version of Step 4 if you are creating a legacy compound report.

The next step is to combine the reports into a single PDF Compound Report. You can:

Code the OPEN and CLOSE options on the [PC]HOLD FORMAT PDF command.

Code the OPEN and CLOSE options on the SET COMPOUND command before the
component report syntax.

Drill Through does not support the NOBREAK option, which displays compound reports without
intervening page breaks.

964

This example uses the OPEN and CLOSE options on the PCHOLD FORMAT PDF command:

10. Linking a Report to Other Resources

TABLE FILE GGSALES
SUM UNITS DOLLARS BY CATEGORY BY PRODUCT
ON TABLE PCHOLD FORMAT PDF OPEN
ON TABLE SET STYLE *
TYPE=DATA, COLUMN=PRODUCT, DRILLTHROUGH=DOWN(CATEGORY PRODUCT), $
ENDSTYLE
END

SET SQUEEZE=ON
TABLE FILE GGSALES
SUM UNITS BUDUNITS DOLLARS
BY CATEGORY NOPRINT BY PRODUCT NOPRINT
ON CATEGORY PAGE-BREAK
HEADING CENTER
"Category: <CATEGORY"
" "
ON PRODUCT SUBHEAD
"**** Product: <PRODUCT"
ON PRODUCT SUBFOOT
" "
"<25 **** Return to Summary ****"
ON PRODUCT PAGE-BREAK
BY REGION BY CITY
ON TABLE PCHOLD FORMAT PDF CLOSE
ON TABLE SET STYLE *
TYPE=SUBFOOT, LINE=2, ITEM=1, DRILLTHROUGH=FIRST(CATEGORY PRODUCT),
COLOR=RED, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 965

Creating a PDF Compound Report With Drill Through Links

Example:

Run the Drill Through Report (Step 5)

Run the compound report. The first page of output has the summary report with the hyperlinks
to the individual products in blue and underlined:

Click the hyperlink Croissant for the category Food. You jump to that detail information. In the
detail report, the hyperlink back to the summary report is in red and underlined:

Click the hyperlink Return to Summary to return to the first page (summary report).

966

10. Linking a Report to Other Resources

Reference: Guidelines on Links For FIRST

The following guidelines apply:

The set of link fields used with FIRST must correspond to the set of link fields used with
DOWN on the first report.

The action of a FIRST hyperlink in the last report should return to the corresponding line in
the first report. The chosen set of links must uniquely identify that line of the first report.

The DOWN hyperlink on the line of the first report must uniquely identify that line of the first
report to locate the matching line of the detail report. The set of links for the DOWN in the
first report and the FIRST link in the last report are the same, since they both must uniquely
identify a line in the first report.

Reference: Rules For Drill Through Hyperlinks

Reports linked with Drill Through must follow certain rules to ensure that the hyperlinks
between them work correctly. The following are key concepts:

Source report. The report from which you are linking. The source report contains hyperlinks
to the target report.

Target report. The report to which you are linking.

Link field. One of a set of corresponding fields of the same data type that exist in both the
source and target reports. Link fields locate the position in the target report to which a
hyperlink in the source report jumps.

Source and target terminology refer to each pair of linked reports. For example, if there are
three reports linked with Drill Through, the second report is generally the target report of the
first report, and also the source report of the third report.

To process a report as a Drill Through, you must identify the link fields in the source report that
relate to the target report:

Choose meaningful link fields whose values match in the source and target reports. For
example, if a field in the source report contains a part number and a field in the target
report contains a Social Security number, the field values will not match and you cannot
construct hyperlinks.

Specify as many link fields as necessary to uniquely locate the position in the target report
that corresponds to the link fields in the source report. For example, if the source report is
sorted by STATE and CITY, specifying CITY alone as the link field will be problematic if
different states contain a city with the same name.

Creating Reports With TIBCO® WebFOCUS Language

 967

Creating a PDF Compound Report With Drill Through Links

The link fields in the source and target reports must have the same internal (actual) format:
the stopped data type and internal length must be identical. Formatting options, such as
number of displayed digits and comma suppression, may differ. For example, an A20 field
must link to another A20 field. However, an I6C field may link to an I8 field, since internally
both are four-byte fields.

The link fields must be sort fields or verb objects in both the source and target reports. You
can include a NOPRINT (non-display) field, which is useful when constructing a report in
which a field is in embedded in heading text.

Designing Drill Through reports is very similar to designing Drill Down reports. Choosing the
link fields for a Drill Through report is similar to choosing the parameter fields in a Drill
Down report. Likewise, the syntax of a Drill Through closely parallels the syntax of a Drill
Down.

Since Drill Through reports are linked by corresponding values of link fields, the hyperlinks
must appear on report elements associated with a particular value of a link field. However,
hyperlinks do not have to appear on any link itself.

Not all line types are appropriate for placement of a Drill Through hyperlink. For example, if
a page break occurs on a BY field that is also a Drill Through link, each page heading is
clearly associated with a value in that field. However, if a page break occurs because of
page overflow, avoid placing a Drill Through link in a heading. Similarly, subheadings,
subfootings, subtotals, and recaps are associated only with the values of particular BY
fields.

968

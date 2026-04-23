Chapter20

Using an External Cascading Style Sheet

Cascading style sheets (CSS) provide a standard way of formatting HTML documents. To
format WebFOCUS HTML report output using an external CSS, simply link the CSS to the
report (using the WebFOCUS StyleSheet CSSURL attribute) and, optionally, apply the CSS
classes to specific report components (using the CLASS attribute).

In this chapter:

What Is a Cascading Style Sheet?

Why Use an External Cascading Style Sheet?

Formatting a Report With an External Cascading Style Sheet

Working With an External Cascading Style Sheet

Applying External Cascading Style Sheet Formatting

Combining an External CSS With Other Formatting Methods

Linking to an External Cascading Style Sheet

Inheritance and External Cascading Style Sheets

Using External Cascading Style Sheets With Non-HTML Reports

Requirements for Using an External Cascading Style Sheet

FAQ About Using External Cascading Style Sheets

Troubleshooting External Cascading Style Sheets

What Is a Cascading Style Sheet?

Cascading style sheets (CSS) are an extension to HTML that allow you to specify formatting for
an HTML document. You can use two kinds of CSS with WebFOCUS:

An internal cascading style sheet, which is stored internally in the HTML document that it
formats. For information about generating and using an internal CSS for a WebFOCUS
report, see Generating an Internal Cascading Style Sheet for HTML Reports on page 1220.

Creating Reports With TIBCO® WebFOCUS Language

 1293

What Is a Cascading Style Sheet?

An external cascading style sheet, which is stored in a separate file that can be shared by
multiple documents. The external CSS file can reside on any web server accessible to the
browser. You specify its location using the CSSURL WebFOCUS StyleSheet attribute, the
CSSURL SET parameter, or (in special cases) the LINK element.

You can define classes in a cascading style sheet, and format a report component by
assigning one of these CSS classes to it. Classes are described in What Are Cascading Style
Sheet Rules and Classes? on page 1294.

Cascading style sheets are called cascading because several different style sheets can be
active for a single document at the same time. For example, one style sheet may be
associated with the document itself, another style sheet may be linked to the first one, and yet
another may be associated with the web browser on which the document is being displayed.
When multiple style sheets are in effect, they are applied to the document in a pre-determined
sequence set by the browser: their formatting instructions can be thought of as cascading from
one style sheet to the next.

The benefits of using an external cascading style sheet to format a report are described in Why
Use an External Cascading Style Sheet? on page 1295.

You will find external cascading style sheets relevant if you:

Develop reports, since you now have an improved way of formatting those reports.

Are responsible for presentation guidelines for web documents, since you will now be able
to apply your existing cascading style sheets to reports.

For information about internal cascading style sheets, see Generating an Internal Cascading
Style Sheet for HTML Reports on page 1220.

Need more information about CSS? This WebFOCUS documentation assumes that you have a
working knowledge of cascading style sheets. Teaching about CSS is beyond the scope of this
documentation, but many sources of information are available to you. A useful place to begin
online is the World Wide Web Consortium's cascading style sheets home page (http://
www.w3.org/Style/CSS/).

What Are Cascading Style Sheet Rules and Classes?

A cascading style sheet (CSS) defines formatting in statements called rules. For example, this
is a simple rule that makes the background color of the body of an HTML page yellow:

BODY {background: yellow}

Each rule has a selector (BODY in this example) and a declaration (background: yellow). A
declaration has a property (background) and a value assigned to the property (yellow).

1294

20. Using an External Cascading Style Sheet

A declaration defines formatting, and a selector determines to what the formatting will be
applied. A selector can be any HTML element. A selector can also be a class. You can define a
class simply by creating a rule for it. By creating rules for classes of an element, you can
define different formatting for the same element.

For example, you may wish to display text in a different color depending on whether it is in a
sort column, aggregate column, or detail column in a report. To accomplish this you could
create three classes of the BODY element, sortColumn, aggregateColumn, and detailColumn:

BODY.sortColumn {color: blue}
BODY.aggregateColumn {color: green}
BODY.detailColumn {color: black}

You can also define a generic class, that is, a class that is not limited to a single element. For
example:

.pageFooting {font-weight: bolder}

You can use a generic class to specify formatting for any WebFOCUS report component.

Using external cascading style sheet rules and classes to format a report is described in
Formatting a Report With an External Cascading Style Sheet on page 1296.

Why Use an External Cascading Style Sheet?

If you already use WebFOCUS StyleSheets to format reports, you can realize these additional
benefits by combining them with external cascading style sheets:

Increased formatting options. Almost any formatting that you can specify in a cascading
style sheet you can apply to a report. This enables you to take advantage of formatting
options that are unavailable via native WebFOCUS StyleSheet attributes. For example, you
can use browser-based measurements so that the person who views the report can control
the size of fonts, margins, and other elements whose size has been specified in the CSS in
terms of em, a unit of relative measurement. You can also use CSS to control line height
and letter spacing, and in general can use CSS to exercise more control over positioning
items in a report.

Improved performance. Cascading style sheets enable WebFOCUS to generate more
concise HTML output. This reduces the bandwidth used by the network to return a report to
a browser, and displays the report faster.

Reduced effort. Enterprises that already use cascading style sheets can now also apply
them to WebFOCUS reports, avoiding duplication of effort to specify and maintain
formatting instructions.

Creating Reports With TIBCO® WebFOCUS Language

 1295

Formatting a Report With an External Cascading Style Sheet

Easier standards conformance. You can ensure that reports conform to your enterprise's
formatting guidelines, because now formatting instructions for all your Web documents can
be specified in one set of cascading style sheets (instead of replicating some of them in
WebFOCUS StyleSheets).

Formatting a Report With an External Cascading Style Sheet

There are just three items required to format a report with an external cascading style sheet
(CSS):

An external cascading style sheet that specifies the formatting to be applied to the report.
For more information, see Working With an External Cascading Style Sheet on page 1302.

A WebFOCUS StyleSheet in which you apply external CSS formatting to the components of
your report. However, you do not need a WebFOCUS StyleSheet when you apply formatting
to the entire report. For more information, see Applying External Cascading Style Sheet
Formatting on page 1306.

(Although you can also use a WebFOCUS StyleSheet to specify additional formatting
outside of the external CSS, this is subject to restrictions. For more information, see
Combining an External CSS With Other Formatting Methods on page 1308.)

A link to the external cascading style sheet from the report. For more information, see
Linking to an External Cascading Style Sheet on page 1310.

To find out how to use these three items to format a report, see How to Format a Report Using
an External Cascading Style Sheet on page 1298.

1296

20. Using an External Cascading Style Sheet

For an example that demonstrates how these items work together, see Linking to the
ReportStyles External Cascading Style Sheet on page 1299 and the following diagram:

Creating Reports With TIBCO® WebFOCUS Language

 1297

Formatting a Report With an External Cascading Style Sheet

Procedure: How to Format a Report Using an External Cascading Style Sheet

To format a report using an external cascading style sheet (CSS):

1. Specify the report formatting in the CSS. Determine which cascading style sheet you will
use, which of its rules specify default formatting for your report, and which of its classes
are suitable for you to apply to the report components. Alternatively, if you are creating a
new CSS, or extending an existing one, define new rules to specify formatting for your
report. To specify formatting for:

A report component, you can use a rule for any generic class (that is, any class not
declared for an element). For an example, see A CSS Rule for the ColumnTitle Class on
page 1299.

Graphs differ from other types of reports: to specify formatting for the page in which
the graph appears, or for the graph heading or footing, you can use a rule for the BODY
element, but not a rule for a class. You cannot format other graph components.

The entire report, use a rule for the BODY or TD elements (not a rule for a class of
these elements), and skip Step 2. This is an effective way of specifying the default
formatting of a report, and generates more efficient report output than does applying a
CSS class to the entire report. For an example, see A CSS Rule for the TD Element on
page 1299.

Graphs differ from other types of reports: you can use a rule for the BODY element, but
not one for TD. A rule for BODY will format the page in which the graph appears, and its
heading and footing, but not the graph itself.

For more information, see Working With an External Cascading Style Sheet on page 1302.

2. Assign classes to report components. In a WebFOCUS StyleSheet, assign a cascading

style sheet class to each report component that you want to format. Specify the class
using the CLASS attribute. You can assign each component a different class, and you can
assign the same class to multiple components.

For an example, see Applying a CSS Class to ACROSS Values in a Report on page 1299.
For more information, see Applying External Cascading Style Sheet Formatting on page
1306.

3. Link to the CSS. Link to the external cascading style sheet by assigning the CSS file URL

to either the CSSURL WebFOCUS StyleSheet attribute or to the CSSURL SET parameter.
For instructions, see Using the CSSURL Attribute and Parameter on page 1310.

There is one exception: if you embed the report output in an existing HTML page using the
-HTMLFORM command, include a LINK element in that HTML page instead of setting
CSSURL.

1298

20. Using an External Cascading Style Sheet

For an example, see Linking to the ReportStyles External Cascading Style Sheet on page
1299. For more information, see Linking to an External Cascading Style Sheet on page
1310.

Problems? If you encounter problems, see Troubleshooting External Cascading Style Sheets on
page 1327.

Reference: A CSS Rule for the ColumnTitle Class

This cascading style sheet (CSS) rule declares the ColumnTitle generic class (that is, a class
not tied to an element):

.ColumnTitle {font-family:helvetica; font-weight:bold; color:blue;}

Reference: A CSS Rule for the TD Element

This cascading style sheet (CSS) rule for the TD element specifies the element's font family:

TD {font-family:helvetica}

Because this rule is for the TD element, its formatting is applied to an entire report, not just a
component of the report.

For a more comprehensive example of using a rule for the TD element to provide general report
formatting, see Linking to the ReportStyles External Cascading Style Sheet on page 1299.

Reference: Applying a CSS Class to ACROSS Values in a Report

This WebFOCUS StyleSheet declaration formats ACROSS values by applying the formatting
specified for the ColumnTitle class:

TYPE=AcrossValue, CLASS=ColumnTitle, $

Reference: Linking to the ReportStyles External Cascading Style Sheet

This WebFOCUS StyleSheet declaration links to the ReportStyles external cascading style
sheet:

TYPE=REPORT, CSSURL=http://webserv1/css/reportstyles.css

or

TYPE=REPORT, CSSURL=IBFS:/WFC/Repository/css/reportstyles.css

Creating Reports With TIBCO® WebFOCUS Language

 1299

Formatting a Report With an External Cascading Style Sheet

You could accomplish the same thing using a SET command:

SET CSSURL=http://webserv1/css/reportstyles.css

Or within a request:

ON TABLE SET CSSURL=http://webserv1/css/reportstyles.css

Alternatively, if you want to embed your report output in an existing HTML page using -
HTMLFORM, you would specify the link by coding the LINK element in the HTML page in which
the report will be embedded, instead of setting CSSURL:

<HEAD>
<TITLE>Accounts Receivable Report</TITLE>
<LINK REL="STYLESHEET" HREF="http://srv3/css/reports.css"
TYPE="text/css">
</HEAD>

Example:

Formatting a Report Using an External CSS

This report displays the products currently offered by Gotham Grinds, and is formatted using
an external cascading style sheet (CSS). The report is formatted so that:

Its default font family is Arial.

The report heading overrides the default with a font family of Times New Roman. The
heading is also in a larger font and center justified.

All column titles are in a bolder font and have a light-blue background.

When a product unit price is less than $27, the report displays the product row in green
italics.

The report request and inline WebFOCUS StyleSheet are shown in the following procedure,
curprods.fex. The external cascading style sheet, named report01.css, follows the procedure.

curprods.fex

    TABLE FILE GGPRODS
    HEADING
    "</1 Current Products</1"
    PRINT PRODUCT_DESCRIPTION UNIT_PRICE
    BY PRODUCT_ID
    ON TABLE SET PAGE-NUM OFF

1.  ON TABLE SET STYLE *
2.  TYPE=REPORT, CSSURL=http://websrv2/css/report01.css, $
3.  TYPE=HEADING, CLASS=headText, $
4.  TYPE=TITLE, CLASS=reportTitles, $
5.  TYPE=DATA, CLASS=lowCost, WHEN=N3 LT 27, $
6.  ENDSTYLE
    END

1300


20. Using an External Cascading Style Sheet

Note: To specify a path that points to a WebFOCUS repository that contains the report01.css
file, use the following syntax for the CSSURL parameter on the TYPE=REPORT line in the
request:

TYPE=REPORT, CSSURL=IBFS:/WFC/Repository/css/report01.css, $

Where css is the folder in the WebFOCUS repository where the report01.css file resides.

report01.css

7.  BODY  {font-family:Arial, sans-serif}
8.  TABLE {border:0}
8.  TD    {border:0}
9.  .reportTitles {font-weight:bolder; background:lightblue;}
10. .lowCost {color:green; font-style:italic;}
11. .headText {font-family:Times New Roman, serif; font-size:larger;
               text-align:center}

1. Begin the inline WebFOCUS StyleSheet.

2. Link to the external cascading style sheet, report01.css.

3. Format the report heading using the cascading style sheet rule for the headText class.

4. Format the report column titles using the CSS rule for the reportTitles class.

5. For each report row for which the product unit cost is less than $27, format that row using

the CSS rule for the lowCost class.

6. End the inline WebFOCUS StyleSheet.

7. This CSS rule for the BODY element specifies the font family Arial and, if Arial is

unavailable, the generic font family sans serif.

Because this is a rule for BODY, it is applied to the entire report: all text in the report will
default to Arial. You can override this for a particular report component by applying a rule
for a generic class to that component, as is done in this procedure with the rule for the
headText class (see line 11).

8. These CSS rules for the TABLE and TD elements remove the report default grid.

9. This CSS rule for the generic class reportTitles specifies a bolder relative font weight and a

light blue background color.

The WebFOCUS StyleSheet applies this to the report column titles (see line 4).

10.This CSS rule for the generic class lowCost specifies the text color green and the font style

italic.

The WebFOCUS StyleSheet applies this rule conditionally to report rows for which the
product unit cost is less than $27 (see line 5).

Creating Reports With TIBCO® WebFOCUS Language

 1301

Working With an External Cascading Style Sheet

11.The CSS rule for the generic class headText specifies the font family Times New Roman
and, if Times New Roman is unavailable, the generic font family serif. It also specifies a
larger relative font size and center justification.

The WebFOCUS StyleSheet applies this rule to the report heading. It overrides the default
font family specified in the rule for the BODY element (see line 7).

The procedure displays this report:

Working With an External Cascading Style Sheet

When you work with an external cascading style sheet (CSS) to specify report formatting, you
need to know about:

Choosing an existing or new external CSS. For more information, see Choosing an External
Cascading Style Sheet on page 1303.

Where an external CSS can reside. For more information, see External Cascading Style
Sheet Location on page 1303.

How you can apply multiple cascading style sheets to one report. For more information, see
Using Several External Cascading Style Sheets on page 1303.

Editing an external CSS. For more information, see Editing an External Cascading Style
Sheet on page 1304.

1302

20. Using an External Cascading Style Sheet

Using CSS rules and classes to specify report formatting. For more information, see
Choosing a Cascading Style Sheet Rule on page 1304.

Suggestions for naming cascading style sheet classes. For more information, see Naming a
Cascading Style Sheet Class on page 1305.

Combining other formatting methods, such as WebFOCUS StyleSheets or TABLE language
instructions, with an external CSS. For more information, see Combining an External CSS
With Other Formatting Methods on page 1308.

Choosing an External Cascading Style Sheet

To format a report using an external cascading style sheet (CSS), you can choose to:

Apply an existing CSS with no changes. The external cascading style sheet can be one
that you use for other documents, and can contain all kinds of rules, not only rules that
format reports. For example, the CSS could include rules to format other elements in the
webpages used by your WebFOCUS applications, as well as rules for other kinds of
webpages. This enables you to use one cascading style sheet to format all of your web
documents.

Edit an existing CSS to add or modify rules. For example, you might edit a cascading style
sheet to add new generic classes to format report components.

Create a new CSS. You can create a new cascading style sheet to format your reports. See
the recommendations in Naming a Cascading Style Sheet Class on page 1305 about
naming classes.

To create an external cascading style sheet, use a text editor or a third-party web development
tool.

External Cascading Style Sheet Location

An external cascading style sheet (CSS) can reside on any web server platform. However, if
CSSURL (the StyleSheet attribute or the SET parameter) specifies a relative URL, the
cascading style sheet must reside on the web server used by WebFOCUS.

Using Several External Cascading Style Sheets

Although each report procedure can link to only one external cascading style sheet (CSS), you
can use several cascading style sheets to format a report by linking to one CSS that then
imports several others. For information about importing one CSS into another, see your third-
party CSS documentation.

Creating Reports With TIBCO® WebFOCUS Language

 1303

Working With an External Cascading Style Sheet

Editing an External Cascading Style Sheet

You can edit an external cascading style sheet (CSS) using a text editor or a third-party web
development tool.

If the formatting of a report is specified entirely using a cascading style sheet, and you edit
that CSS, the next time someone displays the report it will reflect the changes to the CSS
without the report having to be rerun.

However, if the report does not reflect the changes, it may be because the web browser is
continuing to use the old version of the CSS that it had stored in cache. The person displaying
the report may need to reload the CSS file from the web server by clicking the Refresh button
of the browser in Microsoft Internet Explorer to ensure that the browser uses the most current
version of the CSS to format the report.

Choosing a Cascading Style Sheet Rule

You can format different parts of a report using different types of rules.

To format:

The entire report

Any report component

Use a rule for:

BODY or TD

A generic class (that is, one declared without
an element)

To choose between using a rule for BODY or for TD, note that a rule for:

BODY will specify default formatting for the entire webpage in which the report appears,
including the report itself. (Note that this relies upon CSS inheritance which, like all CSS
behavior, is implemented by the web browser of each user and is browser-dependent.)

Graphs differ from other types of reports: a rule for BODY will format the page in which the
graph appears, and its heading and footing, but not the graph itself.

1304

20. Using an External Cascading Style Sheet

TD will specify default formatting only for the report, and for any other table cells that you
may have on the page. TD is the table data (that is, table cell) element. WebFOCUS
generates most HTML report output as an HTML table, placing each report item in a
separate cell. This enables a rule for TD to format the entire report.

Graphs differ from other types of reports: to specify default formatting for a graph, use a
rule for BODY, not for TD. See the previous note regarding formatting graphs using a rule
for BODY.

When you use a rule for a class to format a report component, you must assign the class to
the component in a WebFOCUS StyleSheet using the CLASS attribute, as described in How to
Use the CLASS Attribute to Apply CSS Formatting on page 1307.

If you wish to apply several CSS properties to a single report component, we recommend that
you declare them in a single class. This generates more efficient output than does declaring
one property per class.

The owner of each cascading style sheet should consider making available a list of all the
classes in that CSS that can be used to format reports, so that everyone who develops reports
knows from which classes they may choose.

For an example of a rule for:

A generic class to format a report component, see A CSS Rule for the ColumnTitle Class on
page 1299.

The TD element to format an entire report, see A CSS Rule for the TD Element on page
1299.

Naming a Cascading Style Sheet Class

When you provide a name for a new class, note that class names are case-sensitive (although
some web browsers may not enforce case sensitivity).

When you create a new class, we recommend naming it after the function, not the appearance,
of the report component to which you will be applying it. This ensures that the name remains
meaningful even if you later change the appearance of the report component. For example, if
you want all report titles to be red, the class you declare to format titles might be named Title,
but not Red.

Creating Reports With TIBCO® WebFOCUS Language

 1305

Applying External Cascading Style Sheet Formatting

Applying External Cascading Style Sheet Formatting

You can apply external cascading style sheet (CSS) formatting to:

A report component (for example, to make a column italic). Assign a cascading style sheet
class to the report component using the WebFOCUS StyleSheet CLASS attribute. For
information about the CLASS attribute, see How to Use the CLASS Attribute to Apply CSS
Formatting on page 1307. For information about specifying different types of report
components, see Identifying a Report Component in a WebFOCUS StyleSheet on page
1249..

When formatting a tabular or free-form report, you can format any report component by
assigning a CSS class.

When formatting a graph report, you can format the graph heading and footing, and can
specify the background color and background image of the page in which the graph
appears, in a rule for the BODY element. (Note that when formatting a graph heading or
footing, you cannot format individual lines, strings, and field values. If you wish to center a
heading or footing, it is recommended that you do so using the CENTER option of the
HEADING or FOOTING command, not in a style sheet.)

When working with the WebFOCUS StyleSheet CLASS attribute, you must edit the
WebFOCUS StyleSheet using the WebFOCUS text editor.

An entire report (for example, to make the entire report italic). You specify the formatting in
the external CSS in a rule for the BODY or TD elements (for graphs, specify the formatting
in a rule for the BODY element only. This will format the page in which the graph appears,
and the graph heading and footing, but not the graph itself). You must also link the report
to the CSS. You do not need a rule for a class of an element, and you do not need a
WebFOCUS StyleSheet declaration. For an example, see A CSS Rule for the TD Element on
page 1299.

We recommend that when you use an external cascading style sheet to format a report, you do
not also use a WebFOCUS StyleSheet to specify the report formatting, unless you also
generate an internal cascading style sheet. For more information, see Combining an External
CSS With Other Formatting Methods on page 1308.

1306

20. Using an External Cascading Style Sheet

Syntax:

How to Use the CLASS Attribute to Apply CSS Formatting

To apply an external cascading style sheet (CSS) class to a report component, use the
following syntax in a WebFOCUS StyleSheet declaration

TYPE = type, [subtype,] CLASS = classname, [when,] [link,] $

where:

type

Identifies the report component to which you are applying the class formatting. For tabular
and free-form reports, it can be any component, as described in Identifying a Report
Component in a WebFOCUS StyleSheet on page 1249. You cannot specify a component of
a graph report: to format a graph's heading and footing, and the background color and
background image of the page in which the graph appears, use a rule for the BODY
element without a WebFOCUS StyleSheet declaration.

Each report component can be formatted by one class. If you specify several classes for a
report component:

1. The classes that are in declarations with conditional formatting are evaluated first. For
each cell in the report component, the first class whose condition is satisfied by the
cell row is assigned to the cell.

2. If none of the conditions is satisfied, or if there are no conditional declarations, the
class in the first unconditional declaration is assigned to the report component. All
following declarations for that component are ignored.

subtype

Is an optional attribute and value needed to completely specify some kinds of report
components. For example, COLUMN and a column identifier are needed to specify a
particular report column.

classname

Is the name of the cascading style sheet class whose formatting you are applying to the
report component. You can assign the same class to multiple report components.

Class names can be up to 511 characters and are case-sensitive: you must use the same
case found in the class rule in the external cascading style sheet. (Note, however, that
some web browsers may not enforce case sensitivity.)

when

Is an optional WHEN attribute and value. Supply this if you want to apply the formatting
conditionally. For more information, see Formatting Reports: An Overview on page 1187.

Creating Reports With TIBCO® WebFOCUS Language

 1307

Combining an External CSS With Other Formatting Methods

link

Is an optional FOCEXEC, URL, or JAVASCRIPT attribute and value. Supply this if you want to
link the report component to another resource, such as a report to which the user can drill
down. For more information, see Linking a Report to Other Resources on page 819.

For an example, see Applying a CSS Class to ACROSS Values in a Report on page 1299.

Combining an External CSS With Other Formatting Methods

When you use an external cascading style sheet (CSS) to format a report, you can use other
formatting methods at the same time. Some of these other methods are subject to
restrictions. The other methods that you can use with an external CSS are:

WebFOCUS StyleSheets. An effective way of combining an external CSS with a WebFOCUS
StyleSheet is to link to an external CSS to provide default formatting, and use a WebFOCUS
StyleSheet to override those defaults for individual report components. Note that if you
combine a WebFOCUS StyleSheet and an external cascading style sheet, you should
generate an internal cascading style sheet to avoid reducing the performance benefits
associated with an external CSS.

Do not attempt to format the same property of the same report component using both an
external CSS class (through the CLASS attribute) and a WebFOCUS StyleSheet attribute,
since the two formatting instructions could conflict with each other.

For complete instructions about using an external CSS with a WebFOCUS StyleSheet, see
Combining an External CSS With a WebFOCUS StyleSheet on page 1309.

TABLE language instructions. You can use TABLE language (or GRAPH language)
formatting instructions, such as HEADING CENTER, PAGE-BREAK, and spot markers (for
example, </3). However, you should not apply both a TABLE (or GRAPH) language
instruction, and an external cascading style sheet rule, to perform the same formatting on
the same report component, because they might conflict with each other.

For example, you should not specify both of the following for the same report:

HEADING CENTER in the report request.

Text-align in an external CSS, applied to the report page heading.

Both of these will attempt to align the report page heading.

1308

Combining an External CSS With a WebFOCUS StyleSheet

20. Using an External Cascading Style Sheet

When you use an external cascading style sheet (CSS) to format a report, you can use a
WebFOCUS StyleSheet at the same time. You may do this with or without generating an
internal cascading style sheet.

An effective way of doing this is to link to an external CSS to provide default formatting, and
use a WebFOCUS StyleSheet to override those defaults for individual report components. The
cascading style sheet BODY or TD rule will provide the default formatting for the report. If you
wish, you can override the defaults for individual report components via native WebFOCUS
StyleSheet attributes. This enables you to conform to your organization's formatting standards
as they are implemented in a CSS, while allowing you to customize those standards for
WebFOCUS reports using WebFOCUS StyleSheet attributes. For information about using a
BODY or TD rule for default formatting, see Choosing a Cascading Style Sheet Rule on page
1304. For an example, see Inheritance and External Cascading Style Sheets on page 1314.

Performance considerations. Note that, unless you generate an internal cascading style sheet
from the WebFOCUS StyleSheet, combining an external CSS and a WebFOCUS StyleSheet may
reduce the performance benefits associated with the external CSS. This is because a report
that uses both an external CSS and native WebFOCUS StyleSheet attributes generates more
HTML code than the same report using an external CSS alone, although it still generates less
code than if the report had used native WebFOCUS StyleSheet attributes alone. (Reducing the
amount of generated HTML code can reduce network load and browser display time.) For
information about generating an internal cascading style sheet, see Generating an Internal
Cascading Style Sheet for HTML Reports on page 1220.

You cannot double-format. You should not attempt to format the same property of the same
report component using both an external CSS class (via the CLASS attribute) and a WebFOCUS
StyleSheet attribute, since the class and the StyleSheet attribute could conflict with each
other.

For example, you should not include the following declarations in the same StyleSheet
because they would both try to assign a color to the Country column:

TYPE=Data, COLUMN=Country, COLOR=Orange, $
TYPE=Data, CLASS=TextColor, $

Creating Reports With TIBCO® WebFOCUS Language

 1309

Linking to an External Cascading Style Sheet

You can specify classes and WebFOCUS StyleSheet attributes that format different properties
of the same report component, and that format different report components. For example, the
following declarations are acceptable in the same StyleSheet:

1. TYPE=Heading, COLOR=Green, $
1. TYPE=Heading, CLASS=HeadingFontSize, $
2. TYPE=Data, Column=Country, BACKCOLOR=Yellow, $
2. TYPE=Data, Column=Car, CLASS=DataBackgroundColor, $
3. TYPE=Data, Column=Model, FOCEXEC=NewSales(CarGroup=Car), $

1. These two declarations are compatible because they format different properties (color and

font size).

2. These two declarations are compatible because they format different report components

(the Country column and the Car column).

3. This declaration will be compatible with all CSS classes, since it does not format a report

component, but instead defines a hyperlink.

Linking to an External Cascading Style Sheet

To format a report using an external cascading style sheet (CSS), you must link the cascading
style sheet to the report in one of the following ways:

For most report procedures, assign the CSS file's URL to the CSSURL attribute or
parameter. For more information, see Using the CSSURL Attribute and Parameter on page
1310.

For report output that you are embedding in an existing HTML page using the -HTMLFORM
command, include a LINK element in the existing HTML page to point to the external CSS
file. For example, if you are embedding a report from an output (HOLD) file that was
generated in HTMTABLE format, use LINK. For more information, see your third-party CSS
documentation. For an example, see Linking to the ReportStyles External Cascading Style
Sheet on page 1299.

Using the CSSURL Attribute and Parameter

You can link an external cascading style sheet (CSS) to a report using the CSSURL WebFOCUS
StyleSheet attribute or the CSSURL SET parameter. To choose between them, consider the
advantages of:

An attribute. Using CSSURL as a StyleSheet attribute enables you to specify:

A longer URL, since the maximum URL length is 255 characters in the attribute,
compared with 69 characters in the parameter.

1310

20. Using an External Cascading Style Sheet

All formatting information in one place, since you can specify the link to the external
CSS and the references to CSS classes within the WebFOCUS StyleSheet. This makes it
easier for you to maintain your formatting logic.

A SET parameter. Using CSSURL as a SET parameter enables you to quickly redirect a link
(from one CSS to another) for many reports at once. You do this by putting the SET
CSSURL command in its own procedure, and merging that into report procedures using a -
INCLUDE Dialogue Manager statement in each report procedure.

If you specify CSSURL in several ways, the specification with the most local scope takes
precedence. The order of precedence, from highest (1) to lowest (3), is:

For more information about the CSS attribute, see How to Use the CSSURL Attribute to Link to
an External CSS on page 1311. For more information about the CSS parameter, see How to
Use the CSSURL Parameter to Link to an External CSS on page 1313.

Syntax:

How to Use the CSSURL Attribute to Link to an External CSS

To link an external cascading style sheet (CSS) to report using a WebFOCUS StyleSheet
attribute, use the following syntax

[TYPE=REPORT,] CSSURL={url|ibfs}, $

where:

TYPE=REPORT

Specifies that this attribute is being applied to the entire report. If it is omitted, the
StyleSheet declaration defaults to it.

url

Is the URL of the external cascading style sheet. If the external CSS resides on a web
server platform that is case-sensitive, you must specify it using the correct case.

The URL can be up to 255 characters. If your external cascading style sheet URL exceeds
this limit, you can shorten the URL by defining an alias (also known as a virtual directory)
on the web server to represent part of the path.

You can specify an absolute or relative URL. If it is relative, the external CSS must reside
on the web server used by WebFOCUS.

ibfs

Is a path that points to a WebFOCUS repository that contains the external cascading style
sheet file. This path is internally converted to a web-accessible URL that points to the
location of the .css file.

Creating Reports With TIBCO® WebFOCUS Language

 1311

Linking to an External Cascading Style Sheet

Example:

Linking to an External Cascading Style Sheet Using the CSSURL Attribute

This report displays the products currently offered by Gotham Grinds. It is formatted using an
external cascading style sheet (CSS), and links to the CSS using the CSSURL attribute in the
WebFOCUS StyleSheet:

TABLE FILE GGPRODS
HEADING
"</1 Current Products</1"
PRINT PRODUCT_DESCRIPTION UNIT_PRICE
BY PRODUCT_ID
ON TABLE SET PAGE-NUM OFF
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET STYLESHEET *
TYPE=REPORT, CSSURL=http://websrv2/css/report01.css, $
TYPE=HEADING, CLASS=headText, $
TYPE=TITLE, CLASS=reportTitles, $
TYPE=DATA, CLASS=lowCost, WHEN=N3 LT 27, $
ENDSTYLE

END

The request produces this report:

1312


20. Using an External Cascading Style Sheet

Note: To specify a path that points to a WebFOCUS repository that contains the report01.css
file, use the following syntax for the CSSURL parameter on the TYPE=REPORT line in the
request:

TYPE=REPORT, CSSURL=IBFS:/WFC/Repository/css/report01.css, $

Where css is the folder in the WebFOCUS repository where the report01.css file resides.

Syntax:

How to Use the CSSURL Parameter to Link to an External CSS

To link an external cascading style sheet (CSS) to a report using a SET parameter, issue the
following SET command in a procedure

SET CSSURL = css_url

or the following ON TABLE SET command in a report request

ON TABLE SET CSSURL css_url

where:

css_url

Is the URL of the external cascading style sheet. If the external CSS resides on a web
server platform that is case-sensitive, you must specify it using the correct case.

The URL can be up to:

69 characters long in a SET command.

57 characters long in an ON TABLE SET command.

If your external cascading style sheet URL exceeds this limit, you can shorten the URL by
defining an alias (also known as a virtual directory) on the web server to represent part of
the path.

You can specify an absolute or relative URL. If it is relative, the external CSS must reside
on the web server used by WebFOCUS.

For an example, see Linking to the ReportStyles External Cascading Style Sheet on page 1299.

If you specify CSSURL multiple times, the last value specified using ON TABLE SET overrides
all the other values within that report request. If CSSURL is not specified within a report
request, the last value specified using SET overrides all the others.

For general information about using SET commands, see Customizing Your Environment in the
Developing Reporting Applications manual.

Creating Reports With TIBCO® WebFOCUS Language

 1313

Inheritance and External Cascading Style Sheets

Inheritance and External Cascading Style Sheets

In a report that is formatted using an external cascading style sheet (CSS), a report component
inherits formatting from the TD element and from all elements that TD nests within, such as
BODY. (Note that inheritance, like all CSS behavior, is implemented by the web browser of
each user and is browser-dependent.)

This differs from a report that is formatted using a WebFOCUS StyleSheet, in which a report
component inherits formatting from a higher-level component. When you format a report using
external cascading style sheet classes, a class assigned to a report component does not
inherit formatting from a class that has been assigned to a higher-level component.

Example:

A Report Column Inheriting Formatting From the TD Element

This report displays a list of the vendors that supply products to Gotham Grinds. Its formatting
instructions specify that:

The entire report has an orange default background color. This is specified in a rule for the
TD element.

The report data is displayed in an italic Arial font. The report data inherits the orange
background color from the rule for TD.

The report PRODUCT_ID data has a yellow background color, overriding the default
specified in the rule for TD.

If the formatting of the report had been specified in a WebFOCUS StyleSheet instead of in
an external CSS, PRODUCT_ID would inherit the italic Arial font from its parent report
component (that is, from the report data). Instead, because its formatting is specified in an
external CSS, PRODUCT_ID inherits formatting from the rule for the TD element, not from a
higher-level report component, and so it does not inherit the italic Arial font.

The report request and inline WebFOCUS StyleSheet are shown in the following procedure,
prodvend.fex. The external cascading style sheet, named report02.css, follows the procedure.

prodvend.fex

   TABLE FILE GGPRODS
   PRINT PRODUCT_DESCRIPTION VENDOR_NAME
   BY PRODUCT_ID
   ON TABLE SET PAGE-NUM OFF

   ON TABLE SET STYLE *
1. TYPE=REPORT, CSSURL = http://websrv2/css/report02.css, $
2. TYPE=DATA, CLASS=Data, $
3. TYPE=DATA, COLUMN=PRODUCT_ID, CLASS=Sort, $
    ENDSTYLE

1314

20. Using an External Cascading Style Sheet

    END

report02.css

4. TD    {background:orange; border:0}
5. TABLE {border:0}
6. .Data {font-style:italic; font-family:Arial}
7. .Sort {background:yellow}

1. Set CSSURL to link to the external cascading style sheet report01.css.

2. Format the report data using the CSS rule for the Data class.

3. Format the report PRODUCT_ID data using the CSS rule for the Sort class. (This overrides

the declaration for report data in general in line 2.)

4. This CSS rule for the TD element specifies an orange background. Because it is a rule for

TD, it is applied to the entire report. You can override this for a particular report component
by applying a rule for a generic class to that component, as is done in this procedure with
the rule for the Sort class (see line 7).

5. These CSS rules for the TD and TABLE elements remove the default grid for the report.

6. This CSS rule for the generic class Data specifies an Arial font family and an italic font

style. The WebFOCUS StyleSheet applies this to the report data (see line 2).

This rule inherits background color from the rule for the TD element (line 4).

7. This CSS rule for the generic class Sort specifies a yellow background. The WebFOCUS

StyleSheet applies this rule to data for PRODUCT_ID (see line 3).

This rule overrides the default background color specified in line 4.

Creating Reports With TIBCO® WebFOCUS Language

 1315

Using External Cascading Style Sheets With Non-HTML Reports

The procedure displays this report:

Using External Cascading Style Sheets With Non-HTML Reports

You can use an external cascading style sheet (CSS) to format a report that is generated as
HTML, but not one that is generated as a different output type, such as PDF. If you have a
report that you will sometimes generate as HTML and sometimes generate as a different
output type, and you wish to gain the benefits of cascading style sheets, we recommend that
you use this technique:

Shared formatting. Specify formatting that is shared by all output types in WebFOCUS
StyleSheet macros. (For example, setting a font style to italic is something that can be
applied to both HTML and PDF report output, so you would specify it in a macro.) Define
two versions of each macro:

One version for HTML output. This version specifies formatting using a cascading style
sheet class.

One version for non-HTML output. This version specifies formatting using native
WebFOCUS StyleSheet attributes.

Unique formatting. Specify formatting that is applicable only to HTML output, or only to
non-HTML output, in standard WebFOCUS StyleSheet declarations. Place each of these
declarations in the WebFOCUS StyleSheet section that contains macro definitions for that
type of output. (For example, turning a grid on or off is applicable to HTML output, but not
to Excel 2000, so you would place it with the macro definitions for HTML.)

1316

20. Using an External Cascading Style Sheet

Branch between the HTML and non-HTML declarations using Dialogue Manager.

You can see the basic code for this technique in How to Use an External CSS With Multiple
Output Types on page 1318.

Creating Reports With TIBCO® WebFOCUS Language

 1317

Using External Cascading Style Sheets With Non-HTML Reports

Syntax:

How to Use an External CSS With Multiple Output Types

If you have a report that you will sometimes generate as HTML and sometimes as other types
of output, and you wish to gain the benefits of cascading style sheets (CSS), we recommend
that you use this technique:

1.  -DEFAULTS &FORMAT='output_type';
2.  SET ONLINE-FMT = &FORMAT
    TABLE FILE datasource
     report_logic

    ON TABLE SET STYLE *
3.  TYPE=REPORT, CSSURL = CascadingStyleSheetURL, $
4.  -IF &FORMAT NE 'HTML' GOTO NONHTML;
5.  DEFMACRO=macro1, CLASS=class1, $
    DEFMACRO=macro2, CLASS=class2, $
     .
     .
     .
6.  TYPE=component3, CLASS=class3, $
     .
     .
     .
7.  -GOTO SHARED
8.  -NONHTML
9.  DEFMACRO=macro1, attribute1=value1, $
    DEFMACRO=macro2, attribute2=value2, $
     .
     .
     .
10. TYPE=component4, attribute4=value4, $
     .
     .
     .
11. -SHARED
12. TYPE=component1, MACRO=macro1, $
    TYPE=component2, MACRO=macro2, $
     .
     .
     .
    ENDSTYLE
    END

1. Assign the type of report output (for example, HTML, PDF, PS, or EXL2K) to the Dialogue

Manager variable &FORMAT. You will use this variable to toggle the WebFOCUS StyleSheet
between formatting for HTML output and formatting for non-HTML output, and also to
provide a value for SET ONLINE-FMT.

You can use forms and other presentation logic to enable the application user to select the
type of report output.

2. Set the report output type to the value of &FORMAT. In this procedure, SET ONLINE-FMT
sets the display type for the report. Alternatively, you could use ON TABLE HOLD to save

1318

20. Using an External Cascading Style Sheet

the report as a file and set its file type.

3. Set CSSURL to link to the external cascading style sheet to be used for formatting the

report HTML output. When the report generates non-HTML output, this command will be
ignored.

4. Branch to the WebFOCUS StyleSheet declarations for the current type of report output

(which is indicated by &FORMAT).

5. Define the HTML version of the WebFOCUS StyleSheet macros. These macros specify

formatting that is shared by all output types.

This HTML version of the macros is implemented using external cascading style sheet
classes.

6. If there is any formatting that is applicable only to HTML output, specify it here, using

external cascading style sheet classes.

7. Branch to the WebFOCUS StyleSheet declarations that apply the macros to the report

components.

8. This label marks the beginning of the macro definitions and unique formatting declarations

for non-HTML report output.

9. Define the non-HTML version of the WebFOCUS StyleSheet macros. These macros specify

formatting that is shared by all output types.

This non-HTML version of the macros is implemented using native WebFOCUS StyleSheet
attributes.

10.If there is any formatting that is applicable only to non-HTML output, specify it here using

native WebFOCUS StyleSheet attributes.

11.This label marks the beginning of the declarations that apply macros to the report.

12.These are the macros that were defined earlier and are being applied to the report.

Creating Reports With TIBCO® WebFOCUS Language

 1319

Using External Cascading Style Sheets With Non-HTML Reports

Example:

Using an External CSS With PDF and HTML Output

This report procedure (videorpt.fex) can generate both HTML and PDF output. When it
generates HTML output, it uses an external cascading style sheet (reports.css) to format the
report. When it generates PDF output, it uses an inline WebFOCUS StyleSheet. In both cases,
the report provides a light blue background for the LASTNAME column and makes all column
titles bold.

The procedure as shown is set to generate HTML output.

videorpt.fex

1.  -DEFAULTS &FORMAT='HTML';
2.  SET CSSURL = http://websrv2/css/reports.css
3.  SET ONLINE-FMT = &FORMAT
    TABLE FILE VIDEOTRK
    PRINT LASTNAME AS 'Last Name' FIRSTNAME AS 'First Name'
    BY LOWEST 5 CUSTID AS 'Cust ID'
    ON TABLE SET PAGE-NUM OFF
    ON TABLE SET STYLE *
4.  -IF &FORMAT NE 'HTML' GOTO NONHTML;
5.  DEFMACRO=boldTitles, CLASS=bold, $
    DEFMACRO=blueColumn, CLASS=blueBack, $
6.  -GOTO SHARED
7.  -NONHTML
8.  DEFMACRO=boldTitles, STYLE=bold, $
    DEFMACRO=blueColumn, BACKCOLOR=light blue, $
9.  -SHARED
10. TYPE=DATA, COLUMN=LastName, MACRO=blueColumn, $
    TYPE=TITLE, MACRO=boldTitles, $
    ENDSTYLE
    END

reports.css

11. .bold {font-weight: bolder}
12. .blueBack {background: lightblue}
13. TABLE {border:0}
13. TD    {border:0}

1. Assign a default value to &FORMAT to toggle the WebFOCUS StyleSheet between formatting

for HTML output and formatting for PDF output. It is currently set to HTML output.

2. Set CSSURL to link to the external cascading style sheet reports.css to format the HTML

output of the report.

3. Set the display type of the report to the value of &FORMAT.

4. Branch to the WebFOCUS StyleSheet declarations for the current type of report output

(HTML).

5. Define the HTML version of the WebFOCUS StyleSheet macros, which are implemented

using external cascading style sheet classes.

1320

20. Using an External Cascading Style Sheet

6. Branch to the WebFOCUS StyleSheet declarations that apply the macros to the components

for the report.

7. This label marks the beginning of the macro definitions for PDF report output.

8. These declarations define the PDF version of the WebFOCUS StyleSheet macros, which are
implemented using native WebFOCUS StyleSheet attributes. These macro definitions will be
ignored because &FORMAT is set to HTML.

9. This label marks the beginning of the declarations that apply macros to the report.

10.These are the macros that were defined earlier and are being applied to the report.

11.This cascading style sheet declaration makes text bolder than it had been.

12.This cascading style sheet declaration makes a background light blue.

13.These CSS rules for the TABLE and TD elements remove the default grid for the report.

The procedure displays this report:

Requirements for Using an External Cascading Style Sheet

When you use an external cascading style sheet (CSS) to format a report, be aware of the
following requirements:

Generate HTML report output. You can use an external cascading style sheet to format
any report that you generate as HTML, whether you save the report output in a file or send
it directly to a web browser. You cannot use an external CSS for a report generated in a
different format, such as PDF or Excel.

If you wish to use an external CSS with a report that you will sometimes generate as HTML
and sometimes as a different format, such as PDF, see Using External Cascading Style
Sheets With Non-HTML Reports on page 1316.

If you are not generating an internal cascading style sheet, do not specify external CSS
classes (CLASS=) and native WebFOCUS StyleSheet attributes in the same WebFOCUS
StyleSheet (other than the exceptions noted in the next paragraph). Doing so could create
formatting conflicts.

Creating Reports With TIBCO® WebFOCUS Language

 1321

Requirements for Using an External Cascading Style Sheet

Exceptions. Even when specifying external CSS classes, you should use native WebFOCUS
StyleSheet attributes to:

Create hyperlinks (using the FOCEXEC, JAVASCRIPT, and URL attributes). However, if
you wish to format a hyperlink, you should do so using the cascading style sheet.

Make a WebFOCUS StyleSheet declaration conditional (using the WHEN attribute).

Embed an image (using the IMAGE attribute). However, if you wish to format the image
(for example, to position it), you should do so using the cascading style sheet.

For more information, see Combining an External CSS With Other Formatting Methods on
page 1308.

Do not specify the same formatting using TABLE/GRAPH and CSS. You can use TABLE
language (or GRAPH language) formatting instructions, such as HEADING CENTER, PAGE-
BREAK, and spot markers (for example, </3). However, you should not apply both a TABLE
(or GRAPH) language instruction, and an external cascading style sheet rule, to perform the
same formatting on the same report component. For more information, see Combining an
External CSS With Other Formatting Methods on page 1308.

SET STYLEMODE. If you wish to use cascading style sheets to format a report in the usual
way, you can set STYLEMODE to FULL (the default) or PAGED. If you set it to FIXED and link
to an external cascading style sheet, the report will inherit formatting from the BODY and
PRE elements, but you will not be able to format the report using classes and the TD
element.

Use a cascading style sheet-enabled web browser. Each user who wishes to display a
report formatted using a cascading style sheet must have a web browser that supports
CSS. All versions of Microsoft Internet Explorer that are certified for use with WebFOCUS
support cascading style sheets.

Note that how a cascading style sheet rule formats your report is determined entirely by the
support of your web browser and implementation of cascading style sheets, not by
WebFOCUS. Some web browsers may not fully support the latest CSS version, or may
implement a CSS feature in different ways.

Do not override the cascading style sheet specified for the report. If a browser has been
customized to ignore cascading style sheets or to employ the personal cascading style
sheet of the user, and the user wishes to view reports as they were intended to be seen
(with the specified cascading style sheet), the user must reset his or her browser to accept
the cascading style sheet of each document.

1322

20. Using an External Cascading Style Sheet

For instructions about checking or changing a browser setting, see the browser Help. For
information about how conflicts between CSS rules are resolved (for example, between a
rule specified in a CSS document and a rule specified in the reader web browser CSS), see
your third-party CSS documentation.

Reference: Usage Notes for External Cascading Style Sheets With SET HTMLCSS ON

Styling only to the CLASS, referenced from the external cascading style sheet, is honored
when internal and external styling is applied to multiple subtypes in an element. The
internal styling applied to the element is ignored. With HTMLCSS OFF, only the internal
styling applied to each subtype is honored.

In a report with no borders specified in the external cascading style sheet, borders in the
internal styling are respected and only grids are shown when HTMLCSS is OFF.

Border style specified in the external cascading style sheet overrides that specified in the
internal style sheet. With HTMLCSS OFF, both grids and the border style specified in the
external cascading style sheet are displayed.

Border weights are consistent in all elements of the report. With HTMLCSS OFF, different
border weights are seen in different elements of the report.

When the heading of the report contains multiple lines, the border outlines the entire
heading. With HTMLCSS OFF, the border outlines each line in the heading.

FAQ About Using External Cascading Style Sheets

This topic answers the most frequently asked questions (FAQ) about using external cascading
style sheets (CSS) to format reports.

Does it answer your question? We invite you to send us any questions that you would like
answered. Each question will get a response, and will also be considered for inclusion in a
future release of FAQ. (We also invite your comments on anything in this document.)

How do I specify a report default formatting using CSS?

You can specify default formatting for an entire report in an external cascading style sheet rule
for the BODY or TD element. For more information, see Choosing an External Cascading Style
Sheet on page 1303.

Creating Reports With TIBCO® WebFOCUS Language

 1323

FAQ About Using External Cascading Style Sheets

Do I always need to use the CLASS attribute?

No. You need the CLASS attribute in a WebFOCUS StyleSheet if you specify formatting for an
individual report component. (You use CLASS to assign a rule for a generic class to the report
component.) When you specify formatting for the entire report, you do so in a rule for the BODY
or TD element, not a rule for a class, so you omit the CLASS attribute.

If you place a reference to a CSS class in your stylesheet, it will be applied to the <A> tag as
well as the <TD> tag. For example, if you have the class ".class1" in your external CSS,
WebFOCUS would generate the following HTML for a value with a drilldown:

<TD CLASS='class1'>
<A class='class1' HREF="...">ENGLAND</A>
</TD>

For example, if you want red hyperlinks without underlines, issue:

SET CSSURL=http://myserver/mycss.css
TABLE FILE CAR
SUM SALES BY COUNTRY
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET STYLE *
type=data, column=country, focexec=fex1, class=class1, $
END

where mycss.css contains:

.class1 { color:red; text-decoration:none }

1324

The output is:

20. Using an External Cascading Style Sheet

For more information, see Applying External Cascading Style Sheet Formatting on page 1306.

Can I use a cascading style sheet and a WebFOCUS StyleSheet together?

When you link to an external cascading style sheet, you can also specify native WebFOCUS
StyleSheet attributes in a WebFOCUS StyleSheet. However, if you do not generate an internal
cascading style sheet, you should not specify CSS classes (CLASS=) and native WebFOCUS
StyleSheet attributes in the same WebFOCUS StyleSheet (except to specify a condition for
conditional formatting, to specify a link to another resource, and to embed an image). For more
information, see Combining an External CSS With Other Formatting Methods on page 1308. For
information about internal cascading style sheets, see Generating an Internal Cascading Style
Sheet for HTML Reports on page 1220.

Creating Reports With TIBCO® WebFOCUS Language

 1325

FAQ About Using External Cascading Style Sheets

Which version of CSS does WebFOCUS support?

Support for different versions of cascading style sheets (such as CSS2) is determined entirely
by your web browser support and implementation of cascading style sheets, not by
WebFOCUS. Note that some web browsers may not fully support the latest CSS version, or may
implement a CSS feature in different ways. For more information, see Requirements for Using
an External Cascading Style Sheet on page 1321, and Troubleshooting External Cascading Style
Sheets on page 1327.

Can I use CSS to format reports generated as PDF, PostScript, or Excel 2000?

No, you can only use external cascading style sheets to format reports that are generated as
HTML.

Which types of reports can I format using an external cascading style sheet?

You can format all types of reports using an external CSS:

Tabular reports, including regular (column-oriented) reports and Financial Modeling
Language (FML, also known as extended matrix or row-oriented) reports.

Graphs. Note that, while you can format a graph heading and footing, and the background
color and background image of the page in which the graph appears, the graph itself is
generated using Java and so cannot be formatted using CSS.

Free-form reports. Most people choose to generate free-form reports using output types
other than HTML, making CSS a rarely-used option for formatting free form.

1326

Troubleshooting External Cascading Style Sheets

20. Using an External Cascading Style Sheet

This topic will help you solve some common problems encountered when formatting reports
with external cascading style sheets (CSS).

Which problems have you needed to troubleshoot? If you have troubleshooting suggestions
that you think others will find helpful, we invite you to send them to us so that we can consider
including them in a future release.

Symptom: The report does not reflect recent changes to the cascading style sheet.

Reason: When you run a report that references an external cascading style sheet, your web
browser stores the CSS file in its memory or disk cache. When you later edit the CSS and
run the report again, your browser may continue to use the earlier version of the CSS file
that it had stored.

Solution: Click your browser Refresh button (Microsoft Internet Explorer) to reload the CSS
file from the web server. This ensures that your web browser will use the most current
version of the cascading style sheet to format the report.

Symptom: The report is not using any of the cascading style sheet formatting.

Reason 1: You may have specified an incorrect URL when you attempted to link to the
external cascading style sheet.

Solution 1: Check the URL that specifies the link (in the CSSURL attribute or in the SET
CSSURL command, or if the report procedure uses -HTMLFORM, in the LINK element) and
correct it, if necessary.

Reason 2: Your web browser may not support cascading style sheets.

Solution 2: All versions of Microsoft Internet Explorer that are certified for use with
WebFOCUS support cascading style sheets. Check to be sure that your browser is certified.
If it is not, install an appropriate version of Internet Explorer or Communicator.

Reason 3: Your web browser may be set to ignore cascading style sheets.

Solution 3: Reset your browser to accept a document cascading style sheet. For
instructions about checking or changing a browser setting, see the browser Help.

Reason 4: Some web browsers, if they do not support a single property specified in a rule,
ignore the entire rule. If this is true of your web browser, and all of your report formatting is
specified in a single rule (for example, a rule for TD or BODY), but the browser does not
support one of the properties specified for the rule, none of the formatting will be applied to
the report.

Creating Reports With TIBCO® WebFOCUS Language

 1327

Troubleshooting External Cascading Style Sheets

Solution 4: Remove the unsupported property, or upgrade your browser to a version that
supports the property.

Reason 5: Some web browsers implement CSS inheritance rules for nested elements in
ways that do not conform to the CSS standard. If you are using such a browser, and for
example, you specify all formatting in a rule for the BODY element, your browser may not
apply the rule to other elements nested within BODY.

Solution 5: Specify the report formatting in a rule for a different element (for example, if the
browser does not correctly implement inheritance from BODY, use a rule for TD), or else
upgrade your browser to a version that correctly supports inheritance.

Reason 6: The CSS file was not found on the server path when the report that references
the .css file was run.

Solution 6: Make sure the directory with the CSS file is on the server search path.

Symptom: The report reflects some, but not all, of the CSS formatting.

Reason 1: How a cascading style sheet rule formats your report is determined entirely by
your web browser support and implementation of cascading style sheets, not by
WebFOCUS. You may be experiencing this symptom because your browser does not
support the level of cascading style sheets that you are using, leaving some CSS features
unimplemented.

Solution 1: Upgrade your browser to a version that supports all the CSS features used to
format the report, or edit the cascading style sheet to remove features that are
unsupported by some of the browsers that will be used to display the report.

Reason 2: Your web browser may be set to use your personal cascading style sheet, and
some of the rules you had specified there may override rules specified in the cascading
style sheet assigned to the report. For information about how conflicts between rules in
different cascading style sheets are resolved, see your third-party CSS documentation.

Solution 2: Reset your browser to accept the cascading style sheet for each document, or
edit the rules in the two cascading style sheets so that they no longer conflict.

Reason 3: Some web browsers, if they do not support a property specified in a rule, ignore
the entire rule. If this is true of your web browser, and the browser does not support one of
the properties specified in the rule for one of the classes assigned to the report, none of
the report components to which that rule has been assigned will be formatted.

Solution 3: Remove the unsupported property, or upgrade your browser to a version that
supports the property.

1328

20. Using an External Cascading Style Sheet

Reason 4: Each report component can be assigned only one cascading style sheet class. If
you have specified more than one class, only the first one specified is assigned to the
component; the others are ignored.

If a class has not yet been assigned to a report cell, and you specify conditional formatting
for it, only the first class whose condition is satisfied by that row is assigned to the cell.
The others are ignored.

Solution 4: Do not assign more than one CSS class to each report component. If you need
to apply multiple attributes, bundle them into a single class.

Reason 5: Some web browsers implement CSS inheritance rules for nested elements in
ways that do not conform to the CSS standard. If you are using such a browser, and for
example, you specify some formatting in a rule for the BODY element, your browser may not
apply the rule to other elements nested within BODY.

Solution 5: Specify the report formatting in a rule for a different element (for example, if the
browser does not correctly implement inheritance from BODY, use a rule for TD), or else
upgrade your browser to a version that correctly supports inheritance.

Reason 6: External cascading style sheets can be subject to certain restrictions when used
with other formatting methods. For example, if a WebFOCUS StyleSheet report does not
generate an internal cascading style sheet, but it references external CSS classes and also
specifies native WebFOCUS StyleSheet attributes, there may be a formatting conflict.

Solution 6: The solution depends on the kind of formatting conflict. In the example above,
the solution is to generate an internal cascading style sheet. For a complete description of
which formatting methods are compatible with an external CSS, and how to avoid
formatting conflicts, see Combining an External CSS With Other Formatting Methods on page
1308.

Symptom: A report distributed with ReportCaster does not have the CSS styling, but it does
have CSS styling when run interactively.

Reason: The mail server to which ReportCaster is distributing reports may not support
externally referenced CSS files. For example, Gmail strips the CSS from HTML email, you
must use an inline CSS for GMail. For information, see:

http://www.ajaxapp.com/2009/02/19/gmail-strips-css-of-html-email-you-must-use-inline-css-
for-gmail/

Solution: Issue the WebFOCUS command SET HTMLCSS=ON in your procedure, or issue
the command ON TABLE SET HTMLCSS ON in your request. This creates reports with an
inline CSS.

Creating Reports With TIBCO® WebFOCUS Language

 1329

Troubleshooting External Cascading Style Sheets

1330

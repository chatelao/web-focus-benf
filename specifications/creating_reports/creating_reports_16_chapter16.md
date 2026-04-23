Chapter16

Formatting Reports: An Overview

To create an effective report, you need to account for:

Content. The data in your report.

Formatting. How to present that content to a reader in a way that achieves maximum
impact.

There are many formatting options that you can use to give your report a professional
appearance and affect how people read and interpret it. For example, you can control:

The appearance of the data, which you can change to emphasize important values.

The headings, footings, and other text with which you "frame" the data to give it
context.

The layout of the report on the page or screen, which you can adjust for different
display environments and for audiences with different vision needs.

The following topics provide an overview of formatting tabular reports (including Financial
Modeling Language reports) and free-form reports. For information about formatting
graphs, see Creating a Graph on page 1743.

In this chapter:

What Kinds of Formatting Can I Do?

How to Specify Formatting in a Report

Standard and Legacy Formatting

Techniques for Quick and Easy Formatting

Navigating From a Report to Other Resources

What Kinds of Formatting Can I Do?

There are many kinds of formatting that you can apply to a report:

The appearance of the report data, such as its font, size, style (italic, bold, or underlined),
color (of the foreground and the background), position, and justification. You can also draw
boxes or lines around data. You can use these properties to emphasize critical values and
to draw attention to important data relationships.

Creating Reports With TIBCO® WebFOCUS Language

 1187

What Kinds of Formatting Can I Do?

You can also select which character to use to mark decimal position, using either a period
(.) or a comma (,), to match the convention of the country in which the report will be read.
You can even choose which character to use to represent a null value and missing data.
For more information, see Formatting Report Data on page 1697.

Providing context for data by "framing" it with headings, footings, and customized column
titles. You can include fields and images within headings and footings. As with data, you
can specify a heading, footing, and column title font, size, style, color, position, and
justification, as well as enclose it within boxes or lines. You can use these framing devices
to explain the context of the data and to engage the interest of the reader. For more
information, see Using Headings, Footings, Titles, and Labels on page 1517.

Laying out the report on the screen or printed page. You can choose the report margins,
where to place headings and footings, where to place background images (watermarks),
and how to arrange the report columns (adjusting the space around and between columns,
adjusting column width and column order, and even stacking one column above another to
reduce report width). You can visually distinguish between different columns, rows, or sort
groups using color and lines. If you wish, you can draw borders around parts of a report or
around the entire report.

You can lay out the report to optimize it for different display environments such as screens
of different sizes and resolutions, and printed pages of different sizes. You can create
multiple report panes on a single page to print labels. You can even combine several
reports into a single file to display or print them as a group. For more information, see
Laying Out the Report Page on page 1331.

Conditionally formatting a report based on the report data. You specify a condition that, at
run time, is automatically evaluated for each instance of the report component you specify,
such as each value of a sort column. The formatting option is applied to each instance of
the report component for which the condition is true. For example, in a sales report, you
can draw attention to sales staff who exceeded quota by making their names bold and
using a different color. For more information, see Controlling Report Formatting on page
1219.

Choosing a display format, such as HTML (the default), PDF (Adobe Acrobat Portable
Document Format), Excel 2000, or PostScript, to suit the viewing and processing needs of
the readers. For more information and a list of all the display formats available to you, see
Choosing a Display Format on page 575.

1188

16. Formatting Reports: An Overview

Making a report accessible to all users regardless of their physical abilities, their browser
type, or their screen settings. For example, you can design a report fonts, colors, layout,
and other formatting to make it easier to read by audiences with special vision needs, and
provide text descriptions of tables and graphics to make their information accessible to
people who use speech-based or Braille-based browsers. You can ensure that a report
conforms to any accessibility guidelines, such as Section 508 of the U.S. Rehabilitation
Act, to which the report is subject.

Example:

Advantages of Formatting a Report

The following pair of reports shows order number, order date, and total order revenue for
Century Corporation in the third quarter of 2000. Compare the formatted version (on the left)
with the unformatted version (on the right):

Creating Reports With TIBCO® WebFOCUS Language

 1189

How to Specify Formatting in a Report

Consider how the formatting applied to the version on the left:

Catches the interest of the reader with a heading and use of color.

Makes the significance of the report clearer using the heading, and by changing the last
column title from the default "Line Total" to "Order Total."

Makes the report easier and more appealing to read by increasing the space between
rows, by reformatting the order date, and by using proportional fonts.

Draws the attention of the reader to important data. In this case, to orders exceeding
$500,000, by conditionally formatting these rows with background color, font color, and (for
the order total) bold font style.

How to Specify Formatting in a Report

You can specify your report formatting using a style sheet. A style sheet is a set of
declarations that defines the appearance of a report. For some types of formatting, you may
need to supplement style sheets with other features, such as SET parameters and TABLE
commands. In each case, this manual describes everything required to achieve a given kind of
formatting.

Benefits of using style sheets. For some types of formatting you can choose between using a
style sheet or a different feature. Style sheets are usually preferred because they enable you
to centralize and reuse formatting logic. This provides you with several advantages:

Productivity. By using just a few lines of code (a single style sheet), you can format dozens
of reports, reducing the development time of each report.

Easy maintenance. You can change formatting for dozens of reports at one time by editing
a single style sheet.

Consistent appearance. Your enterprise can guarantee a consistent look for its reports by
assigning the same style sheet(s) to them.

Rapid reformatting. You can change the appearance of a report quickly and easily by
switching the style sheet assigned to it.

Prioritizing. You can focus on your first priority (report content), because you can quickly
address report presentation by applying an existing style sheet.

There are different kinds of style sheets that you can use to format a report. You can learn
about them and how to choose between them in How to Choose a Type of Style Sheet on page
1193.

1190

Example:

Specifying Formatting for the Order Revenue Report

This report displays the order number, order date, and total order revenue for Century
Corporation for the third quarter of 2000:

16. Formatting Reports: An Overview

The report is formatted by a WebFOCUS StyleSheet and by formatting commands in the report
procedure itself. The procedure, Revenue.fex, is shown below, followed by the StyleSheet file,
OrderRev.sty:

Revenue.fex

Creating Reports With TIBCO® WebFOCUS Language

 1191

How to Specify Formatting in a Report

   TABLE FILE CENTORD
1.HEADING
1. " "
1. "C e n t u r y C o r p o r a t i o n"
1. " "
1. "Order Revenue - 2000 Q3"
1. " "
1. "page <TABPAGENO"
1. " "
2. SUM ORDER_DATE/MtDY ORDER_NUM LINEPRICE AS 'Order,Total:'
   BY LOWEST 9 ORDER_DATE NOPRINT
   WHERE (ORDER_DATE GE '2000/10/01') AND (ORDER_DATE LE '2000/12/31');
   ON TABLE SET ONLINE-FMT PDF
3. ON TABLE SET SQUEEZE ON
4. ON TABLE SET STYLESHEET OrderRev
   END

OrderRev.sty

5. TYPE=Report, GRID=Off, UNITS=Inches, TOPGAP=0.06, BOTTOMGAP=0.06, $
6. TYPE=Data, FONT='Times', $
7. TYPE=Data, BACKCOLOR=Aqua, COLOR=Navy,
7.      WHEN=LinePrice GT 500000, $
7. TYPE=Data, COLUMN=LINEPRICE, BACKCOLOR=Aqua, COLOR=Navy, STYLE=Bold,
7.      WHEN=LinePrice GT 500000, $
8. TYPE=Title, FONT='Helvetica', $
9. TYPE=Heading, FONT='Helvetica', STYLE=Bold, SIZE=14, JUSTIFY=Center,
9.                       BACKCOLOR=Dark Turquoise, COLOR=White, $
9. TYPE=Heading, LINE=6, BACKCOLOR=White, COLOR=Dark Turquoise, $
9. TYPE=Heading, LINE=7, BACKCOLOR=White, $

1. Adds a page heading to the report.

2. Reformats the order date from (for example) 2000/10/07 to Oct. 7, 00.

3. Aligns the heading with the report margins instead of the page margins.

4. Identifies a StyleSheet file to format the report.

5. Increases spacing between report lines.

6. Uses a proportional serif font for the report data.

7. Highlights each order that totals more than $500,000 by applying a navy font and an aqua

background, and by bolding the order total.

8. Uses a proportional sans serif font for the report column titles.

9. Formats the report heading by centering it, applying a larger sans serif font, coloring most

of it with a dark turquoise background and white lettering, and applying the inverse coloring
to the page number (the sixth line of the heading).

This is only a summary of what these formatting instructions do. You can find complete
explanations in the topics that describe each formatting feature.

1192

16. Formatting Reports: An Overview

The formatting logic that you apply to your own reports may be briefer or more extensive than
this example, depending on the report and on what formatting you choose to apply.

How to Choose a Type of Style Sheet

You can choose between two types of style sheets to format a report:

WebFOCUS StyleSheets (often abbreviated to "StyleSheets"), the native WebFOCUS style
sheet language. These provide you with the flexibility to format reports in many display
formats, including HTML, PDF, Excel 2000, and PostScript. You can choose between saving
the StyleSheet as a separate file, which you can assign to multiple reports, or saving it
within one report request.

If you are generating a report in HTML format, you can boost its performance, and increase
the number of formatting options available to it, by having the WebFOCUS StyleSheet
dynamically generate an "internal" cascading style sheet (CSS). (CSS is the standard style
sheet language designed for HTML documents. The internal CSS generated by WebFOCUS
is internal to the report output, instead of being saved as a separate file.) For more
information about generating an internal cascading style sheet, see Generating an Internal
Cascading Style Sheet for HTML Reports on page 1220.

External cascading style sheets, the standard style sheet language designed for HTML
documents. You can apply an external cascading style sheet to any WebFOCUS report in
HTML format. (An external cascading style sheet is one that is saved as a separate file,
instead of within the document it formats, and so is "external" to the document.)

How do you choose between the two types of style sheets? Consider choosing:

A WebFOCUS StyleSheet if:

You want to display a report in different display formats, such as PDF and Excel 2000.
WebFOCUS StyleSheets are supported for many kinds of display formats, but cascading
style sheets work for reports in HTML format only.

An external cascading style sheet for any of the following reasons:

Your enterprise already uses cascading style sheets to format HTML documents, and it
wants reports to conform to these same presentation guidelines.

You want to apply the same formatting to other kinds of HTML documents in your
enterprise.

Creating Reports With TIBCO® WebFOCUS Language

 1193

Standard and Legacy Formatting

Standard and Legacy Formatting

New releases of WebFOCUS often introduce improved ways of formatting reports. Some of
these new features are advances over earlier features that performed similar formatting, but
with fewer options or less functionality. The new feature becomes the standard, and the earlier
one is then considered a "legacy" feature.

When you create a new application and have a choice between using a standard or a legacy
feature, we encourage you to use the standard feature. When you are maintaining an earlier
application that incorporates a legacy feature, you may choose to retain the legacy feature to
save time, or to convert the application to the standard feature in order to leverage its new
functionality.

As an example of the difference between standard and legacy formatting, consider the
standard and legacy methods of laying out a report on a page:

The standard way is to specify the page margins using TOPMARGIN, BOTTOMMARGIN,
LEFTMARGIN, and RIGHTMARGIN. (You can apply these keywords as StyleSheet attributes
or SET command parameters.) You can specify the margins in inches, centimeters, or
points, as determined by UNITS (which you can also issue as a StyleSheet attribute or a
SET command parameter). This is simple, and enables you to design reports the same way
that you design other kinds of documents.

The legacy way is to specify the height of the report output on the page, measured in
report lines (using the LINES parameter of the SET command); and the width of the report,
measured in characters (using the WIDTH parameter of the SET command). The top and
bottom margins will each be half the difference of the page height and the report height,
measured in character lines; the left and right margins will each be half the difference of
the page width and the report width, measured in characters. This legacy method limits you
to using a monospace font, such as Courier.

Techniques for Quick and Easy Formatting

You can apply several formatting techniques to save yourself time and effort. Most of these
techniques enable you to use code provided for you by WebFOCUS, or to leverage code that
you write yourself:

Inheritance and overrides. Each report component inherits StyleSheet attributes from its
"parent" report component. This powerful feature lets you define common formatting in a
single declaration for a parent component, and lets descendant components automatically
inherit the formatting, while enabling you to override the inherited values when you wish. By
designing your StyleSheet to take advantage of inheritance, you can write less code and
can quickly update formatting for multiple report components.

1194

16. Formatting Reports: An Overview

For example, if you declare all the report data to be blue, all data in all columns will be
displayed as blue. If you also declare all vertical sort (BY) columns to be orange, this will
override the blue for sort columns, which will be displayed as orange. If you also declare
the EMP_ID sort column green, it will override the orange and be displayed as green. For
more information, see WebFOCUS StyleSheet Attribute Inheritance on page 1207.

Macros. If you are going to specify the same attribute and value in several declarations in a
StyleSheet, you can create a "macro" that enables you to apply the attribute repeatedly
throughout the StyleSheet without coding it each time. Then, if you ever need to change the
value, you can change it once (in the macro), and have the change applied automatically
throughout the StyleSheet.

For example, if there are several parts of a report that you wish to emphasize (such as,
titles of important columns, data values that exceed a threshold, and sort headings), and
you want all of these to be bold and purple, you could define a macro that sets font style to
bold and color to purple, and then apply the macro to all of these report components. For
more information, see Reusing WebFOCUS StyleSheet Declarations With Macros on page
1204.

Defaults. Many WebFOCUS StyleSheet attributes have default values. Instead of explicitly
specifying every StyleSheet attribute, you can omit some and accept their defaults. For
example, you can accept the default font instead of specifying a font. You can find each
default value of an attribute documented where its syntax is described.

Navigating From a Report to Other Resources

You can enable someone reading a report to navigate to other reports and Internet resources,
and even to navigate within the report itself. Although navigation is not considered formatting,
you can support some kinds of navigation by using a StyleSheet.

You can enable someone reading a report to:

Drill down to a related report. For more information, see Linking to Another Report on page
820.

Link to a webpage, compose and send an email message, and connect to other kinds of
Internet resources. For more information, see Linking to a URL on page 825.

Execute JavaScript functions to perform additional analysis of report data. For more
information, see Linking to a JavaScript Function on page 833.

Creating Reports With TIBCO® WebFOCUS Language

 1195

Navigating From a Report to Other Resources

Use a table of contents to jump directly to the data that interests that reader. The report
generates the table of contents dynamically based on sort values, and enables the reader
to see any report section, or the entire report, simply by selecting it from the table of
contents. For more information, see Navigating Sort Groups From a Table of Contents on
page 969.

Jump from one report page to the next, to the top of the current report page, or to the
beginning or end of the report. For more information, see Linking Report Pages on page
1022.

1196

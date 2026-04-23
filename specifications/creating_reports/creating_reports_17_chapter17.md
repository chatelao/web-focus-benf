Chapter17 Creating and Managing a WebFOCUS

StyleSheet

A StyleSheet enables you to format and produce attractive reports that highlight key
information. With StyleSheets, you can specify various characteristics of your report and
format report components individually.

You can use a StyleSheet to:

Format report components individually.

Incorporate graphical elements.

Define dynamic hyperlinks.

Format data that meets specified conditions.

Create macros that enable you to streamline your formatting specifications.

You can also use external cascading style sheets and you can enable internal cascading
style sheets for HTML reports. For details, see Using an External Cascading Style Sheet
on page 1293 and Controlling Report Formatting on page 1219.

Unless otherwise noted, all StyleSheet references in this chapter refer to WebFOCUS
StyleSheets.

In this chapter:

Creating a WebFOCUS StyleSheet

General WebFOCUS StyleSheet Syntax

Reusing WebFOCUS StyleSheet Declarations With Macros

WebFOCUS StyleSheet Attribute Inheritance

Creating Reports With the ENWarm StyleSheet

Creating a WebFOCUS StyleSheet

You can create a StyleSheet:

Within a report request, as an inline StyleSheet. This is useful when you need to apply a
StyleSheet to only one report. For details, see Creating a WebFOCUS StyleSheet Within a
Report Request on page 1198.

Creating Reports With TIBCO® WebFOCUS Language

 1197

Creating a WebFOCUS StyleSheet

Outside of a report request, as a separate file. This enables you to apply one StyleSheet to
multiple reports. For details, see Creating and Applying a WebFOCUS StyleSheet File on page
1200.

Note: You can also include a StyleSheet file in another StyleSheet. This enables you to apply
the styles in the included StyleSheet file, but override specific attributes. For information, see
How to Include a StyleSheet File in Another StyleSheet on page 1199.

Creating a WebFOCUS StyleSheet Within a Report Request

You can create a StyleSheet within a report request. This enables you to create and maintain
the formatting for your report directly in the report request. This type of StyleSheet is known as
an inline StyleSheet.

Syntax:

How to Create a WebFOCUS StyleSheet Within a Report Request

ON TABLE SET STYLE[SHEET] *
declaration
[declaration]
.
.
.
[ENDSTYLE]

where:

SHEET

Can be omitted to make the command shorter, and has no effect on its behavior.

declaration

Is a StyleSheet declaration. StyleSheet declarations usually specify the report
component you want to format and the formatting you want to apply. For more
information about declarations, see General WebFOCUS StyleSheet Syntax on page
1202.

ENDSTYLE

Indicates the end of an inline StyleSheet. You can omit ENDSTYLE if it is followed
immediately by END in the report request.

Example:

Creating a WebFOCUS StyleSheet Within a Report Request

The following illustrates an inline StyleSheet. The StyleSheet is highlighted in the request.

1198

17. Creating and Managing a WebFOCUS StyleSheet

TABLE FILE GGSALES
SUM UNITS DOLLARS BY CATEGORY BY PRODUCT
HEADING
"Sales Report"
FOOTING CENTER
"**End of Report**"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=HEADING, FONT=ARIAL, SIZE=12, STYLE=BOLD, $
TYPE=TITLE, STYLE=ITALIC, $
TYPE=DATA, COLUMN=N1, STYLE=BOLD, COLOR=BLUE, $
TYPE=FOOTING, COLOR=RED, STYLE=BOLD, $
ENDSTYLE
END

The output is:

Syntax:

How to Include a StyleSheet File in Another StyleSheet

INCLUDE = stysheet,$

Creating Reports With TIBCO® WebFOCUS Language

 1199

Creating a WebFOCUS StyleSheet

where:

stysheet

Is the StyleSheet file to include.

StyleSheet declarations are applied in the order in which they are found in the StyleSheet.
Therefore, if you want to include a StyleSheet file and then override some of the attributes
within it, place the INCLUDE statement first, then the declarations that override specific
attributes below it.

Example:

Including a StyleSheet File in Another StyleSheet

The following request includes one of the distributed WebFOCUS StyleSheet Sin the inline
report StyleSheet and overrides the heading style to be bold and italic.

HEADING CENTER
"Test of Stylesheet with Include"
" "
SUM DOLLARS BUDDOLLARS
BY CATEGORY
ON TABLE HOLD AS STYLE2 FORMAT HTML
ON TABLE SET STYLE *
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/javaassist/intl/EN/
ENIADefault_combine.sty,$
TYPE=HEADING, STYLE = BOLD+ITALIC,$
END

The output is shown in the following image.

Creating and Applying a WebFOCUS StyleSheet File

You can create a StyleSheet as a separate file and apply it to as many reports as you wish. A
StyleSheet file contains only declarations and optional comments. Unlike an inline StyleSheet,
a StyleSheet file does not contain the ON TABLE SET STYLESHEET and ENDSTYLE commands.
You can apply a StyleSheet file to a report using the SET STYLESHEET command, as described
in How to Apply a WebFOCUS StyleSheet File to a Report on page 1201. For information about
StyleSheet declarations, see General WebFOCUS StyleSheet Syntax on page 1202.

1200

17. Creating and Managing a WebFOCUS StyleSheet

As an alternative to creating a new StyleSheet file, you can use one of the sample StyleSheet
files provided with WebFOCUS as a template.

Whether you create a StyleSheet file, or copy and customize an existing one, you need to store
it in the correct location, as described in Naming and Storing a WebFOCUS StyleSheet File on
page 1201.

Reference: Naming and Storing a WebFOCUS StyleSheet File

When you create a StyleSheet file to be used in:

WebFOCUS, upload the file to the WebFOCUS repository to a folder in which you are
permitted to create content, and that users running procedures that reference the
StyleSheet are permitted to read.

If you create a StyleSheet for a self-service application, you can deploy your StyleSheet file
to the apps\baseapp directory where it can be shared by multiple applications. You can
also deploy the StyleSheet file to the same location as the report procedure it works with if
you are only applying the file to that particular procedure.

You should name a StyleSheet file filename.sty, where filename can include letters, numbers,
and underscores (_), and otherwise must be valid for the operating environments on which it
resides.

Syntax:

How to Apply a WebFOCUS StyleSheet File to a Report

To apply your StyleSheet file at the beginning of your report request, use

SET STYLE[SHEET] = stylesheet

To apply your StyleSheet file within your report request use

ON TABLE SET STYLE[SHEET] stylesheet

where:

SHEET

Can be omitted to make the command shorter, and has no effect on its behavior.

stylesheet

Is the name of the StyleSheet file. Do not include the file extension.

Creating Reports With TIBCO® WebFOCUS Language

 1201

General WebFOCUS StyleSheet Syntax

General WebFOCUS StyleSheet Syntax

A StyleSheet consists of declarations that identify the report components you wish to format
and the formatting you wish to apply. A declaration usually begins with the TYPE attribute and
is followed by the attribute=value pairs you assign to the report component. You can also
include comments that provide context for your StyleSheet. Comments do not affect
StyleSheet behavior. For details, see Adding a Comment to a WebFOCUS StyleSheet on page
1204.

For information about identifying a report component, see Identifying a Report Component in a
WebFOCUS StyleSheet on page 1249.

Syntax:

How to Specify a WebFOCUS StyleSheet Declaration

Each StyleSheet declaration specifies a series of attributes in the form

attribute = value, [attribute = value, ...] $

where:

attribute

Is the attribute you are specifying, such as TYPE, COLUMN, COLOR, or FONT.

value

Is the value you assign to the attribute.

Example:

Sample WebFOCUS StyleSheet

Following is a request that includes an inline StyleSheet. The StyleSheet begins with ON TABLE
SET STYLE * and ends with ENDSTYLE.

1202

17. Creating and Managing a WebFOCUS StyleSheet

TABLE FILE CENTORD
HEADING
" "
"C e n t u r y  C o r p o r a t i o n"
" "
"Order Revenue - 2000 Q3"
" "
"page <TABPAGENO"
" "
SUM ORDER_DATE/MtDY ORDER_NUM LINEPRICE AS 'Order,Total:'
BY LOWEST 9 ORDER_DATE NOPRINT
WHERE (ORDER_DATE GE '2000/10/01') AND (ORDER_DATE LE '2000/12/31');
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET HTMLCSS ON

ON TABLE SET STYLESHEET *
TYPE=Report, GRID=Off, UNITS=Inches, $
TYPE=Data, FONT='Times', $
TYPE=Data, BACKCOLOR=Aqua, COLOR=Navy,
     WHEN=LinePrice GT 500000, $
TYPE=Data, COLUMN=LinePrice, BACKCOLOR=Aqua, COLOR=Navy, STYLE=Bold,
     WHEN=LinePrice GT 500000, $
TYPE=Title, FONT='Helvetica', $
TYPE=Heading, FONT='Helvetica', STYLE=Bold, SIZE=14, JUSTIFY=Center,
     COLOR=White, BACKCOLOR=Dark Turquoise, $
TYPE=Heading, LINE=6, BACKCOLOR=White, COLOR=Dark Turquoise, $
TYPE=Heading, LINE=7, BACKCOLOR=White, $
ENDSTYLE

END

Improving WebFOCUS StyleSheet Readability

There are many ways to structure your StyleSheet declarations in order to make the StyleSheet
easy to read. You can do any one, or a combination, of the following:

Begin a declaration in any column using blank spaces or tabs.

Include blank lines between declarations.

Create declarations in all uppercase, all lowercase, or mixed case.

Use more than one declaration to format a single report component.

Include blank spaces or tabs in between the attribute, equal sign (=), value, comma, and
dollar sign ($).

Creating Reports With TIBCO® WebFOCUS Language

 1203



Reusing WebFOCUS StyleSheet Declarations With Macros

Split a single declaration across a line. The declaration will continue to be processed until
the terminating dollar sign. For example, you can split a declaration like this:

TYPE=HEADING, FONT=ARIAL,
SIZE=14, STYLE=BOLD, $

Split an attribute=value pair across a line. Use the backslash (\) character as continuation
syntax at the end of the first line if you are splitting an attribute or value in a declaration
across a line. For example:

TYPE=TITLE, COLUMN=N2, STY\
LE=BOLD+ITALIC, COLOR=BLUE, $

Adding a Comment to a WebFOCUS StyleSheet

You can add comments to a StyleSheet to give context to a declaration. Comments do not
affect StyleSheet behavior.

You can add a comment:

On a declaration line. Add the desired text after the dollar sign ($). For example,

TYPE=HEADING, STYLE=BOLD, COLOR=BLUE, SIZE=14, $ Sample comment

On its own line. Begin the line with either a dollar sign ($), or a hyphen and an asterisk (-*),
followed by the desired text. For example,

-* This is a sample comment
$ This is another sample comment

Note: You can add comments anywhere in your request, not only in StyleSheets.

Reusing WebFOCUS StyleSheet Declarations With Macros

If you frequently use a group of attributes within a StyleSheet declaration, you can create a
StyleSheet macro that groups the sequence of attributes together, enabling you to apply them
repeatedly throughout the StyleSheet without recoding them.

Defining a WebFOCUS StyleSheet Macro

A StyleSheet macro must be defined in the StyleSheet that references it and the macro
definition must precede its use in the StyleSheet.

To define a macro, use the DEFMACRO attribute followed by the desired styling attributes.

1204

17. Creating and Managing a WebFOCUS StyleSheet

Syntax:

How to Define a WebFOCUS StyleSheet Macro

DEFMACRO = macroname, attribute1 = value1, [attribute2 = value2,]... $

where:

macroname

Is the name you assign to the macro you are creating.

attribute

Is any StyleSheet attribute, such as an attribute to format a report component, insert
a graphic, define a hyperlink, or apply a condition for conditional formatting (WHEN).

value

Is the value you want to assign to the attribute.

Applying a WebFOCUS StyleSheet Macro

A StyleSheet macro applies all the formatting defined in the macro to the report component
specified in the declaration. To apply a macro, use the MACRO attribute. You can apply one
macro per declaration.

When applying a StyleSheet macro to a report component, you can override any attribute
defined in the macro by specifying the same attribute with the new value in that declaration,
following the MACRO attribute.

Syntax:

How to Apply a WebFOCUS StyleSheet Macro

TYPE=type, [subtype,] MACRO=macroname, [condition,] $

where:

type

Is the report component you wish to affect. You can specify any report component.

subtype

Are any additional attributes, such as COLUMN, ACROSS, or ITEM, that are needed to
identify the report component to which you are applying the macro. For information about
how to specify different types of report components, see Identifying a Report Component in
a WebFOCUS StyleSheet on page 1249.

macroname

Is the name of the macro to apply to the specified report component. The macro must be
defined in the same StyleSheet.

Creating Reports With TIBCO® WebFOCUS Language

 1205

Reusing WebFOCUS StyleSheet Declarations With Macros

condition

Is an optional WHEN attribute that you can specify if you wish to make this declaration
conditional. For information about conditional declarations, see Controlling Report
Formatting on page 1219.

Example:

Defining, Applying, and Overriding a WebFOCUS StyleSheet Macro

The following annotated example illustrates how to define, apply, and override macros in your
StyleSheet:

   TABLE FILE GGSALES
    SUM UNITS DOLLARS
    BY CATEGORY BY PRODUCT
    HEADING
    "Sales Report"
    FOOTING
    "Sales Report - Page <TABPAGENO"
    ON TABLE SET STYLE *
    TYPE=REPORT, GRID=OFF,$
1.  DEFMACRO=A, STYLE=BOLD, SIZE=12, $
2.  DEFMACRO=BI, STYLE=BOLD+ITALIC, COLOR=PURPLE, $
3.  TYPE=HEADING, MACRO=A, $
4.  TYPE=FOOTING, MACRO=BI, COLOR=BLACK, $
5.  TYPE=DATA, COLUMN=N1, MACRO=BI, $
   ENDSTYLE
   END

1. Defines the A macro.

2. Defines the BI macro.

3. Illustrates how the A macro is applied to the heading.

4. Illustrates how the BI macro is applied to the footing and is partially overridden by the

attribute value pair COLOR=BLACK.

5. Illustrates how the BI macro is applied to the data in the BY sort field CATEGORY (specified

by TYPE=DATA, COLUMN=N1).

1206

17. Creating and Managing a WebFOCUS StyleSheet

The output is:

WebFOCUS StyleSheet Attribute Inheritance

Each report component inherits StyleSheet attributes from its parent component. You can
override an inherited attribute by explicitly specifying the same attribute with a different value
in the declaration for the child component. Since each component inherits automatically, you
need specify only those attributes that differ from, or that augment, the inherited attributes of
a component.

Inheritance enables you to define common formatting in a single declaration, and to apply it
automatically to all child components, except for those components for which you specify
different attribute values to override the inherited values. You benefit from less coding and a
more concise StyleSheet.

For example, you could specify that all report titles should be blue and bold:

TYPE=TITLE, COLOR=BLUE, STYLE=BOLD, $

Each column title will inherit this formatting, appearing in blue and bold by default. However,
you can choose to format one column differently, allowing it to inherit the blue color, but
specifying that it override the bold style and that it add a yellow background color:

Creating Reports With TIBCO® WebFOCUS Language

 1207

WebFOCUS StyleSheet Attribute Inheritance

TYPE=TITLE, COLUMN=N2, STYLE=-BOLD, BACKCOLOR=YELLOW, $

Reference: WebFOCUS StyleSheet Inheritance Hierarchy

Report components inherit StyleSheet attributes according to a hierarchy. The root of the
hierarchy is the entire report, specified in a StyleSheet declaration by TYPE=REPORT.
Declarations that omit TYPE default to TYPE=REPORT and are also applied to the entire report.
Attributes that are unspecified for the entire report default to values that are determined
according to the display format of the report, such as HTML or PDF.

Each report component inherits from its parent component. Component X is a parent of
component Y if X is specified by a subset of all the "type" attributes that specify Y, and if
those shared type attributes have the same values. For example,

A component specified by TYPE=x, subtype=y, elementtype=z is a child of the component
specified by TYPE=x, subtype=y and inherits attributes from it.

The component specified by TYPE=x, subtype=y is a child of the component specified by
TYPE=x, and inherits from it.

The component specified by TYPE=x, where x is any value other than REPORT, is a child of
the entire report (TYPE=REPORT) and inherits from it.

The component specified by TYPE=DATA, subtype=z does not inherit from TYPE=REPORT,
subtype=z. The rule is that a style for individual components (subtype=z) can only inherit
from a style with the same type. The only exception is that any style can inherit from the
top-level TYPE=REPORT component (the default style that has only TYPE=REPORT, with no
other components, such as COLUMN, and so on).

For example, in the following syntax, by defining specific styling for the column at the DATA
level, the overall style from TYPE=REPORT will be applied (FONT=TAHOMA), but not
TYPE=REPORT, COLUMN=N2 (COLOR=GREEN). To apply the color green to the data in
column 2, you have to explicitly make it green.

TYPE=REPORT, FONT=TAHOMA, $
TYPE=REPORT, COLUMN=N2, COLOR=GREEN, $
TYPE=DATA, COLUMN=N2, STYLE=+UNDERLINE+BOLD, $

When you use an external cascading style sheet (CSS), a report component inherits formatting
from parent HTML elements, not from a parent report component. For more information, see
Inheritance and External Cascading Style Sheets on page 1314.

Example:

Augmenting Inherited WebFOCUS StyleSheet Attributes

The following illustrates how to augment inherited StyleSheet attributes. The StyleSheet
declarations discussed in this example are highlighted in the report request.

1208

17. Creating and Managing a WebFOCUS StyleSheet

The page heading in this report has two lines. The first StyleSheet declaration identifies the
report component HEADING to be formatted in bold and have 12-point font size. This will
format both lines of the heading with these styles.

To augment the format for the second line of the heading, a second declaration has been
added that specifies the heading line number and the additional style characteristic. In this
case we have added the declaration TYPE=HEADING, LINE=2, STYLE=ITALIC. The second line
of the heading will inherit the bold style and 12-point font size from the first HEADING
declaration, and will also receive the italic style defined in the second declaration.

TABLE FILE GGSALES
SUM UNITS DOLLARS
BY CATEGORY BY PRODUCT
HEADING
"Sales Report:"
"First Quarter"
ON TABLE SET PAGE-NUM OFF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=HEADING, STYLE=BOLD, SIZE=12, $
TYPE=HEADING, LINE=2, STYLE=ITALIC, $
ENDSTYLE
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1209

WebFOCUS StyleSheet Attribute Inheritance

Example:

Overriding Inherited WebFOCUS StyleSheet Attributes

The following illustrates how to override StyleSheet inheritance. The StyleSheet declarations
discussed in this example are highlighted in the report request.

   TABLE FILE GGSALES
HEADING
"Sales Report"
SUM UNITS DOLLARS
BY CATEGORY BY PRODUCT BY DATE NOPRINT
WHERE DATE GE 19960101 AND DATE LE 19960401
ON TABLE SET STYLEMODE PAGED
ON TABLE SET LINES 20
FOOTING
"Page <TABPAGENO of <TABLASTPAGE"
ON TABLE SET STYLE *
   TYPE=REPORT, GRID=OFF, $
1. TYPE=REPORT, BACKCOLOR=BLUE, COLOR=WHITE, $
2. TYPE=HEADING, BACKCOLOR=WHITE, COLOR=BLACK, STYLE=BOLD, SIZE=12, $
3. TYPE=FOOTING, SIZE=11, STYLE=BOLD+ITALIC, BACKCOLOR=WHITE,
    COLOR=BLACK, $
4. TYPE=FOOTING, OBJECT=FIELD, ITEM=1, STYLE=-ITALIC, $
   ENDSTYLE
   END

1. Formats the entire report (all components) to appear with a blue background and white

font.

2. Overrides the inherited format for the page heading (defined in the TYPE=REPORT
declaration) by specifying the background color as white and the font as black.

3. Formats the page footing as font size 11, with a bold and italic style and overrides the

report color by specifying BACKCOLOR=WHITE and COLOR=BLACK.

4. Since the <TABPAGENO system variable is part of the page footing, it inherits all of the

formatting specified in the first TYPE=FOOTING declaration. This declaration overrides the
inherited format for the page footing by specifying OBJECT=FIELD, ITEM=1, and removing
the italic style (STYLE=-ITALIC). Note that ITEM=1 needs to be specified since there are two
embedded fields in the footing.

1210

17. Creating and Managing a WebFOCUS StyleSheet

The output is:

Creating Reports With the ENWarm StyleSheet

The ENWarm StyleSheet (ENWarm.sty) is the new default style sheet for the WebFOCUS
toolset. Using a clean and simple layout and design, you can take advantage of this style
sheet when working with styling options for your reports and charts. Consistent text and color
schemes, as well as a common look and feel, provide you with predictability across all of your
reporting and charting activities.

In addition, there is an ENFlat StyleSheet, which offers the look and feel of ENWarm, with a
different color scheme. It is recommend that you use this StyleSheet with active reports.

This section explains the specifications of the ENWarm StyleSheet and how it applies to report
styling, and active reports.

Creating Reports With TIBCO® WebFOCUS Language

 1211

Creating Reports With the ENWarm StyleSheet

Report Styling

The following topic explains the specifications of the ENWarm StyleSheet and how it apples to
report styling.

Data, Report, and Title Styling

Styling for the data, report, and title elements are shown in the following image.

Title

Bold

Report

Arial

9 pt

Font color: RGB (20, 20, 20)

Title line skip

Hyperlink color: RGB (51, 102, 255)

Page color: White

Data

Top border: RGB (219, 219, 219)

Bottom border: RGB (219, 219, 219)

Top gap: .05

Bottom gap: .05

1212

17. Creating and Managing a WebFOCUS StyleSheet

Headings and Footings Styling

The headers and footers are defined in your report and pages, as shown in the following
image.

The ENWarm StyleSheet style settings are as follows:

Heading

14 pt

Bold

Font color: RGB (75, 75, 75)

Left justify

Page Heading

12 pt

Bold

Font color: RGB (75, 75, 75)

Left justify

Page Footing

10 pt

Font color: RGB (102, 102, 102)

Report Footing

10 pt

Creating Reports With TIBCO® WebFOCUS Language

 1213

Creating Reports With the ENWarm StyleSheet

Font color: RGB (102, 102, 102)

Subheading and Subfooting Styling

Styling for the subheading element is shown in the following image.

Subheading

Background color: RGB (246, 246, 246)

Top border: RGB (219, 219, 219)

Subheading Data

Bold

1214

17. Creating and Managing a WebFOCUS StyleSheet

Styling for the subfooting element is shown in the following image.

Subfooting Data

Bold

Across Styling

Across styling for a report is shown in the following image.

Creating Reports With TIBCO® WebFOCUS Language

 1215

Creating Reports With the ENWarm StyleSheet

Across Title

Right justify on outer BY field

Across Data

Center justify

Row Total Data

Bold

Subtotal and Column Total Styling

Subtotal

Bold

Column Total

Bold

Top Border: RGB (102, 102, 102)

Active Reports

The following topic explains the specifications of the ENWarm StyleSheet and how it apples to
active reports.

1216

17. Creating and Managing a WebFOCUS StyleSheet

Pagination, Menu, and Hover Text Styling in WebFOCUS Active Reports

Styling for pagination, menu, and hover text elements in WebFOCUS active reports are shown
in the following image.

Pagination

Location: Bottom

Background color: None

Left justify

Menu

Text color: RGB (#6B6B6B)

Creating Reports With TIBCO® WebFOCUS Language

 1217

Creating Reports With the ENWarm StyleSheet

Background color: RGB (#F8F8F8)

Hover text color: RGB (#495263)

Hover background color: RGB (#DFDFDF)

Hover

Background color: RGB (243, 243, 243)

AR Iconset

Blue

Usage Notes for ENWarm.sty

AHTML does not support borders.

Sort objects can contain multiple BY fields. In procedures where the sort object is the first
BY field, the ENWarm StyleSheet defines attributes specifically for the first BY field and,
therefore, is not supported.

Sort Objects are not supported with any reference to a BY column in the StyleSheet.
ENWarm styles the first BY subhead to distinguish a break.

Horizontal borders are used to distinguish each data row. When borders are present in a
report, the following behavior will change:

Blank line between heading and titles.

Blank line between end of data and footing.

FML bar will not show the bar line.

Note: For scenarios involving these usage notes, use the endeflt StyleSheet as an alternative
to the ENWarm StyleSheet.

1218

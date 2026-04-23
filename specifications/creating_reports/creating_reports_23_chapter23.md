Chapter23

Formatting Report Data

This chapter covers information about formatting and positioning text in a report. You can
select the size, color, font, and style for the text of your report, in addition to being able
to adjust the position of text within a report.

In this chapter:

Specifying Font Format in a Report

Specifying Background Color in a Report

Alternating Background Color By Wrapped Line

Specifying Data Format in a Report

Positioning Data in a Report

Specifying Font Format in a Report

Using StyleSheet attributes, you can enhance the appearance of a report by specifying the
font, size, and color of the font. Font format can be designated for a report as a whole, or for
headings, footings, and columns individually.

Syntax:

How to Specify Font Size in a Report

To specify a font size, use the following syntax within a StyleSheet.

TYPE = type, [subtype,] SIZE=pts, $

where:

type

Is the report component you wish to affect, such as REPORT, HEADING, or TITLE.

subtype

Is any additional attribute, such as COLUMN, ACROSS, ITEM etc. that is needed to
identify the report component that you are formatting. See Identifying a Report
Component in a WebFOCUS StyleSheet on page 1249 for more information about how
to specify different report components.

Creating Reports With TIBCO® WebFOCUS Language

 1697

Specifying Font Format in a Report

pts

Is the size of the font in points. The default value is 10, which corresponds to the
HTML default font size 3. For more information on the correlation between point size
and html font size, see Usage Notes for Changing Font Size on page 1698.

Example:

Specifying Font Size in a Report

In the following report request, the point size of column titles is set to 12:

TABLE FILE GGSALES
ON TABLE SET PAGE-NUM OFF
SUM UNITS DOLLARS BY CATEGORY
ON TABLE SET STYLE *
TYPE=TITLE, SIZE=12, $
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The output is:

Reference: Usage Notes for Changing Font Size

Point size is fixed, except in an HTML report. Relative point size uses a different scale than
HTML font size. The following table lists the point size and the corresponding HTML font size:

Size in Points

Corresponding HTML Font Size

8 or smaller

9

10

11

12

13

1

2

3

4

5

6

1698

23. Formatting Report Data

Size in Points

Corresponding HTML Font Size

14 or larger

7

Syntax:

How to Specify Bold or Italic Font Style in a Report

To specify a font style, use the following syntax within a StyleSheet.

TYPE=type, [subtype,] STYLE=[+|-]txtsty[{+|-}txtsty], $

where:

type

Is the report component you wish to affect, such as REPORT, HEADING, or TITLE.

subtype

Is any additional attribute, such as COLUMN, ACROSS, ITEM etc. that is needed to
identify the report component that you are formatting. See Identifying a Report
Component in a WebFOCUS StyleSheet on page 1249 for more information about how
to specify different report components.

txtsty

Is one of the following values: NORMAL, BOLD, ITALIC. The default value is NORMAL.

Note that if you specify a style that is not supported for the font you are using, the
specified font will display without the style.

+

-

Enables you to specify a combination of font styles. You can add additional font styles
to an attribute that already has one or more font styles applied to it.

Enables you to remove a font style from an attribute.

Example:

Specifying Font Style in a Report

In the following report, the column titles are specified to have bold and italic font styles:

TABLE FILE GGSALES
SUM UNITS DOLLARS BY CATEGORY
ON TABLE SET STYLE *
TYPE=TITLE, STYLE=BOLD+ITALIC, $
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1699

Specifying Font Format in a Report

The output is:

Example:

Adding and Removing Inherited Font Style in a Report

In the following report request, the font styles bold and italics are specified for the entire
report. The inherited italics are removed from the heading, and both styles are removed from
the column titles:

TABLE FILE GGSALES
HEADING
"Sales Report by Category"
SUM UNITS DOLLARS BY CATEGORY
ON TABLE SET STYLE *
TYPE=REPORT, STYLE=BOLD+ITALIC, $
TYPE=HEADING, STYLE=-ITALIC, $
TYPE=TITLE, STYLE=-BOLD-ITALIC, $
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The output is:

1700

23. Formatting Report Data

Syntax:

How to Specify Font Color in a Report

To specify a color for the font of a report or a report component, use the following syntax within
a StyleSheet.

TYPE=type, [subtype,] COLOR={color|RGB({r g b|#hexcolor})},$

where:

type

Is the report component you wish to affect, such as REPORT, HEADING, or TITLE.

subtype

Is any additional attribute, such as COLUMN, ACROSS, ITEM etc. that is needed to
identify the report component that you are formatting. See Identifying a Report
Component in a WebFOCUS StyleSheet on page 1249 for more information about how
to specify different report components.

color

Is one of the preset color values such as GREY or GOLD. If the display or output
device does not support colors, it substitutes shades of gray. The default value is
BLACK. For a complete list of available color values, see Color Values in a Report on
page 1701.

RGB(r g b)

Specifies the font color using a mixture of red, green, and blue.

(r g b) Is the desired intensity of red, green, and blue, respectively. The values are on a
scale of 0 to 255, where 0 is the least intense and 255 is the most intense. Note that
using the three color components in equal intensities results in shades of gray.

RGB(#hexcolor)

Is the hexadecimal value for the color. For example, FF0000 is the hexadecimal value
for red. The hexadecimal digits can be in upper or lower case and must be preceded
by a pound sign (#).

Reference: Color Values in a Report

The following chart lists all available color values that can be utilized with the syntax

COLOR=color, or BACKCOLOR=color,

where color is one of the following values:

AQUA (CYAN)

MEDIUM FOREST GREEN (OLIVE)

Creating Reports With TIBCO® WebFOCUS Language

 1701

Specifying Font Format in a Report

AQUAMARINE

BLACK

BLUE VIOLET

CADET BLUE

CORAL

MEDIUM GOLDENROD

MEDIUM ORCHID

MEDIUM SLATE BLUE

MEDIUM SPRING GREEN

MEDIUM TURQUOISE

CORNFLOWER BLUE

MEDIUM VIOLET RED

CYAN (AQUA)

DARK GREEN

MIDNIGHT BLUE

NAVY (NAVY BLUE)

DARK OLIVE GREEN

OLIVE (MEDIUM FOREST GREEN)

DARK ORCHID

ORANGE

DARK SLATE BLUE (PURPLE)

ORANGE RED

DARK SLATE GREY

DARK TURQUOISE

DIM GREY (GRAY, GREY)

FIREBRICK

ORCHID

PALE GREEN

PINK

PLUM

FOREST GREEN (GREEN)

PURPLE (DARK SLATE BLUE)

FUCHSIA (MAGENTA)

GOLD

GOLDENROD

GRAY (DIM GREY, GREY)

GREEN (FOREST GREEN)

RED

SALMON

SEA GREEN

SIENNA

SILVER

1702

23. Formatting Report Data

GREEN YELLOW

SKY BLUE

GREY (DIM GREY, GRAY)

SLATE BLUE

INDIAN RED

KHAKI

LIGHT BLUE

LIGHT GREY

LIGHT STEEL BLUE

LIME

LIME GREEN

MAGENTA (FUCHSIA)

MAROON

MEDIUM AQUAMARINE

STEEL BLUE (TEAL)

TAN

TEAL (STEEL BLUE)

THISTLE

TURQUOISE

VIOLET

VIOLET RED

WHEAT

WHITE

YELLOW

MEDIUM BLUE

YELLOW GREEN

Specifying Fonts for Reports

You can specify your own fonts in a report by using the FONT attribute in a StyleSheet. If you
are specifying a font for an HTML report, the web browser must support the font. If the web
browser does not support the font, it reverts to its default behavior of using the default
proportional font.

Syntax:

How to Specify Fonts in a Report

To specify a font for your report, use the following syntax within a StyleSheet.

TYPE=type, [subtype,] FONT='font[,font]',$

where:

type

Is the report component you wish to affect, such as REPORT, HEADING, or TITLE.

Creating Reports With TIBCO® WebFOCUS Language

 1703

Specifying Font Format in a Report

subtype

Is any additional attribute, such as COLUMN, ACROSS, ITEM etc. that is needed to
identify the report component that you are formatting. See Identifying a Report
Component in a WebFOCUS StyleSheet on page 1249 for more information about how
to specify different report components.

font

Is the name of the font. You must enclose the value in single quotes. If you are
creating an HTML report, you can specify more than one font within the single quotes
to accommodate more than one browser.

Note: In an HTML report, specifying different fonts for several different report components
significantly increases the size of the source code.

Example:

Specifying Multiple Fonts in an HTML Report

To control how a report looks on more than one platform, you can specify both a common
Windows font and a common UNIX font in a request. The web browser searches for the first
font in the list. If the browser does not find the first font, it searches for the next font in the
list. If none of the fonts are identified, the browser uses the default proportional font.

In this example, the web browser first searches for the Arial font. If the browser does not find
Arial, it searches for the Helvetica font. If neither font is identified, the browser uses the
default proportional font.

TYPE=REPORT, FONT='ARIAL,HELVETICA',$

Syntax:

How to Specify the Default Browser Fonts for HTML Reports

A browser assigns specific fonts as the default proportional and default monospaced fonts. To
specify a default browser font for an HTML report, you use the reserved names, DEFAULT-
PROPORTIONAL and DEFAULT-FIXED in the StyleSheet of your report. The browser displays the
report accordingly.

To select the default fixed or proportional font of the browser, use the following syntax. Note
that you must specify TYPE to indicate which report components you wish to affect.

FONT={DEFAULT-PROPORTIONAL|DEFAULT-FIXED},$

where:

DEFAULT-PROPORTIONAL

Specifies the default proportional font of the web browser.

DEFAULT-FIXED

Specifies the default monospaced font of the web browser.

1704

23. Formatting Report Data

Example:

Specifying Default Browser Fonts

In this example, the web browser uses the default monospace font for the entire report except
the report heading and the column headings. For these headings, the web browser uses the
default proportional font.

TABLE FILE GGSALES
HEADING
"Sales Report"
SUM UNITS DOLLARS BY CATEGORY BY PRODUCT
ON TABLE SET STYLE *
TYPE=REPORT,FONT=DEFAULT-FIXED,$
TYPE=TITLE,FONT=DEFAULT-PROPORTIONAL,$
TYPE=HEADING,FONT=DEFAULT-PROPORTIONAL,$
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

The output is:

Specifying Background Color in a Report

Using StyleSheet attributes, you can enhance the appearance of a report by specifying a
background color. You can designate background colors for a report as a whole, or for
headings, footings, and columns individually.

Additionally, alternating backcolors (banded) can be specified for the background of the data
lines in a report. These alternating colors are not supported for stacked columns (OVER, FOLD-
LINE).

Creating Reports With TIBCO® WebFOCUS Language

 1705

Specifying Background Color in a Report

Syntax:

How to Specify Background Color in a Report

To specify a color for the background of a report, use the following syntax within a StyleSheet.

Note that when using BACKCOLOR in a PDF report, extra space is added to the top, bottom,
right, and left of each cell of data in the report. This is for readability and to prevent truncation.

TYPE=type, [subtype,] BACKCOLOR={color|RGB({r g b|#hexcolor})}, $

where:

type

Is the report component you wish to affect, such as REPORT, HEADING, or TITLE. In a
HEADING, FOOTING, SUBHEADING, or SUBFOOTING, you can specify a background color for
individual elements.

subtype

Is any additional attribute, such as COLUMN, ACROSS, ITEM, that is needed to identify the
report component that you are formatting. In a HEADING, FOOTING, SUBHEADING, or
SUBFOOTING, you can specify a background color for individual elements. For more
information about how to specify different report components, see Identifying a Report
Component in a WebFOCUS StyleSheet on page 1249.

color

Is the background color, which fills the space of the specified report component. The
default value is NONE. If you are creating a report in HTML format, background colors will
only appear in web browsers that support them.

RGB (r g b)

Specifies the font color using a mixture of red, green, and blue.

(r g b) Is the desired intensity of red, green, and blue, respectively. The values are on a
scale of 0 to 255, where 0 is the least intense and 255 is the most intense. Note that
using the three color components in equal intensities results in shades of gray.

RGB (#hexcolor)

Is the hexadecimal value for the color. For example, FF0000 is the hexadecimal value for
red. The hexadecimal digits can be in upper or lower case and must be preceded by a
pound sign (#).

1706

23. Formatting Report Data

Example:

Specifying Background and Font Color in a Report

You can use color in a report to emphasize important information in a report. In the following
report request, the data in the Dollar Sales column has been specified as RED on the
condition that the Dollars value is less than 2,500,000. The background color is set to LIGHT
BLUE:

TABLE FILE GGSALES
ON TABLE SET PAGE-NUM OFF
HEADING
"Sales Report"
SUM UNITS DOLLARS BY CATEGORY BY PRODUCT
ON TABLE SET STYLE *
TYPE=REPORT, BACKCOLOR=LIGHT BLUE, $
TYPE=DATA, COLUMN=DOLLARS, COLOR=RED, WHEN=DOLLARS LT 2500000, $
TYPE=REPORT, GRID=OFF, $
TYPE=HEADING, JUSTIFY=CENTER, SIZE=12,$
ENDSTYLE
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1707

Specifying Background Color in a Report

Syntax:

How to Specify Alternating Data Background Color in a Report

To specify alternating colors for the background of the data in a report, use the following
syntax within a StyleSheet.

Note that when using BACKCOLOR in a PDF report, extra space is added to the top, bottom,
right, and left of each cell of data in the report. This is for readability and to prevent truncation.

TYPE=DATA,BACKCOLOR=({c1|RGB({r1 g1 b1|#hc1})} {c2|RGB({r2 g2 b2|#hc2})}),
$

where:

c1, c2

Are the background colors for the data in the report. The default value is NONE. If you
are creating a report in HTML format, background colors will only appear in web
browsers that support them. Color names that contain a space must be enclosed in
single quotation marks, as a space is the delimiter between the alternating color
values.

RGB(r1 g1 b1), RGB(r2 g2 b2)

Specifies the font colors using a mixture of red, green, and blue.

(r g b) Is the desired intensity of red, green, and blue, respectively. The values are on a
scale of 0 to 255, where 0 is the least intense and 255 is the most intense. Note that
using the three color components in equal intensities results in shades of gray.

RGB(#hc1), RGB(#hc2)

Are the hexadecimal values for the colors. For example, FF0000 is the hexadecimal
value for red. The hexadecimal digits can be in upper or lower case and must be
preceded by a pound sign (#).

Example:

Specifying Alternating Background Colors for the Data Lines in a Report

The following request against the GGSALES data source produces alternating light blue and
white data rows on the report output:

TABLE FILE GGSALES
ON TABLE SET PAGE-NUM OFF
HEADING
"Sales Report"
SUM UNITS DOLLARS
BY CATEGORY
BY PRODUCT
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=DATA, BACKCOLOR=('LIGHT BLUE' WHITE),$
TYPE=HEADING, JUSTIFY=CENTER, SIZE=12,$
ENDSTYLE
END

1708

The output is:

23. Formatting Report Data

Alternating Background Color By Wrapped Line

The ALTBACKPERLINE attribute alternates the background color by line for reports that use
positioned drivers, for example PDF, DHTML, PPT, and PPTX. This enables you to wrap a long
field value, and alternate the background color of each line for that value, independent of
borders. In order to apply alternating background color per line, you need to explicitly add the
SET ALTBACKPERLINE=ON command to procedures that use WRAP.

Reference: Alternate Background Color By Wrapped Line

SET ALTBACKPERLINE = {ON|OFF}

where:

ON

Alternates background color by line.

OFF

Alternates background color by row. This is the default value.

Creating Reports With TIBCO® WebFOCUS Language

 1709

Alternating Background Color By Wrapped Line

Example:

Alternating Background Color By Wrapped Line

The following report request prints a COMPUTE field with a long line of text, using WRAP and
without using the SET ALTBACKPERLINE command. The default alternating background color is
applied by row.

TABLE FILE WF_RETAIL PRINT
COMPUTE LONG_LINE/A1000 = 'This is a very long line of data, set up so that'
                           |'it wraps onto the next line within a report'
                           |'and to test the alternate color syntax'
                           |'in style sheets.';
BY PRODUCT_CATEGORY BY PRODUCT_SUBCATEG BY MODEL
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET PAGE OFF
ON TABLE SET STYLE *
UNITS=IN, PAGESIZE='A4', LEFTMARGIN=0.19, TOPMARGIN=0.00,
BOTTOMMARGIN=0.00, SQUEEZE=ON, ORIENTATION=LANDSCAPE, $
TYPE=REPORT, FONT='ARIAL', SIZE=8, COLOR=BLACK, BACKCOLOR='NONE',
STYLE=NORMAL, $
TYPE=REPORT, COLUMN=N4, WRAP=1, $
TYPE=DATA, COLUMN=N4, BACKCOLOR=(RGB(235 240 178) RGB(255 255 255)), $
ENDSTYLE
END

1710

The output is:

23. Formatting Report Data

Creating Reports With TIBCO® WebFOCUS Language

 1711

Specifying Data Format in a Report

With the SET ALTBACKPERLINE=ON command added to the request, the alternating
background color is applied by line, as shown in the following output.

Specifying Data Format in a Report

You can affect how data is represented in a report in several ways:

You can change the format of the numeric values that appear in a column.

You can determine whether or not you wish to use Continental Decimal Notation (CDN).

You can set a specific character or set of characters to represent fields that do not contain
data.

1712

23. Formatting Report Data

Changing the Format of Values in a Report Column

A field format is defined in the Master File. You can, however, change the format of a report
column. Field formats are described in full detail in the Describing Data With WebFOCUS
Language manual.

Syntax:

How to Change Format of Values in a Column

fieldname [alignment] [/format]

where:

fieldname

Is a display field—that is, a field displayed by the PRINT, LIST, SUM, or COUNT
command, a row-total, or a column-total.

alignment

Specifies the position of the column title.

/R specifies a right justified column title.

/L specifies a left justified column title.

/C specifies a centered column title.

format

Is any valid field format, preceded by a slash (/). Field formats are described in the
Describing Data With WebFOCUS Language manual. Field formats cannot be used with
a column total.

Example:

Changing the Format of Values in a Column

The UNIT_PRICE field has a format of D7.2 as defined in the GGPRODS Master File. To add a
floating dollar sign to the display, the field format can be redefined as follows:

TABLE FILE GGPRODS
PRINT UNIT_PRICE/D7.2M
END

Creating Reports With TIBCO® WebFOCUS Language

 1713

Specifying Data Format in a Report

The output is:

    Unit
   Price  $58.00
  $81.00
  $76.00
  $13.00
  $17.00
  $28.00
  $26.00
  $96.00
 $125.00
 $140.00

Example:

Using Multiple Format Specifications in a Column

The following request illustrates column title justification with a format specification, a BY field
specification, and an AS phrase specification:

TABLE FILE CAR
PRINT MODEL/A10 STANDARD/A15/R AS 'RJUST,STANDARD'
BY CAR/C
WHERE CAR EQ 'JAGUAR' OR 'TOYOTA'
END

The output is:

                                        RJUST
       CAR        MODEL              STANDARD
----------------  -----       ---------------
JAGUAR            V12XKE AUT  POWER STEERING
                  XJ12L AUTO  RECLINING BUCKE
                              WHITEWALL RADIA
                              WRAP AROUND BUM
                              4 WHEEL DISC BR
TOYOTA            COROLLA 4   BODY SIDE MOLDI
                              MACPHERSON STRU

Reference: Usage Notes for Changing Column Format

Each time you reformat a column, the field is counted twice against the limit for display
fields in a single report. For details, see Controlling Report Formatting on page 1219.

If you create an extract file from the report—that is, a HOLD, PCHOLD, SAVE, or SAVB file—
the extract file will contain fields for both the original format and the redefined format,
unless HOLDLIST=PRINTONLY. Extract files are described in Saving and Reusing Your
Report Output on page 471.

When the size of a word in a text field instance is greater than the format of the text field in
the Master File, the word wraps to a second line, and the next word begins on the same
line.

1714

23. Formatting Report Data

You may specify justification for display fields, BY fields, and ACROSS fields. For ACROSS
fields, data values, not column titles, are justified as specified.

For display commands only, the justification parameter may be combined with a format
specification. The format specification may precede or follow the justification parameter.

If a title is specified with an AS phrase or in the Master File, that title will be justified as
specified in FORMAT.

When multiple ACROSS fields are requested, justification is performed on the lowest
ACROSS level only. All other justification parameters for ACROSS fields are ignored.

Controlling Missing Values for a Reformatted Field

When a field is reformatted in a request (for example, SUM field/format), an internal COMPUTE
field is created to contain the reformatted field value and display on the report output. If the
original field has a missing value, that missing value can be propagated to the internal field by
setting the COMPMISS parameter ON. If the missing value is not propagated to the internal
field, it displays a zero (if it is numeric) or a blank (if it is alphanumeric). If the missing value is
propagated to the internal field, it displays the missing data symbol on the report output.

Syntax:

How to Control Missing Values in Reformatted Fields

SET COMPMISS = {ON|OFF}

where:

ON

OFF

Propagates a missing value to a reformatted field. ON is the default value.

Displays a blank or zero for a reformatted field.

Example:

Controlling Missing Values in Reformatted Fields

The following procedure prints the RETURNS field from the SALES data source for store 14Z.
With COMPMISS OFF, the missing values display as zeros in the column for the reformatted
field value.

Note: Before trying this example, you must make sure that the SALEMISS procedure, which
adds missing values to the SALES data source, has been run.

Creating Reports With TIBCO® WebFOCUS Language

 1715

Specifying Data Format in a Report

SET COMPMISS = OFF
TABLE FILE SALES
PRINT RETURNS RETURNS/D12.2 AS 'REFORMATTED,RETURNS'
BY STORE_CODE
WHERE STORE_CODE EQ '14Z'
END

The output is:

                        REFORMATTED
STORE_CODE  RETURNS     RETURNS
----------  -------     -----------
14Z               2            2.00
                  2            2.00
                  0             .00
                  .             .00
                  4            4.00
                  0             .00
                  3            3.00
                  4            4.00
                  .             .00
                  4            4.00

With COMPMISS ON, the column for the reformatted version of RETURNS displays the missing
data symbol when a value is missing:

SET COMPMISS = ON
TABLE FILE SALES
PRINT RETURNS RETURNS/D12.2 AS 'REFORMATTED,RETURNS'
BY STORE_CODE
WHERE STORE_CODE EQ '14Z'
END

The output is:

                        REFORMATTED
STORE_CODE  RETURNS     RETURNS
----------  -------     -----------
14Z               2            2.00
                  2            2.00
                  0             .00
                  .               .
                  4            4.00
                  0             .00
                  3            3.00
                  4            4.00
                  .               .
                  4            4.00

1716

23. Formatting Report Data

Reference: Usage Notes for SET COMPMISS

If you create a HOLD file with COMPMISS ON, the HOLD Master File for the reformatted
field indicates MISSING = ON (as does the original field). With COMPMISS = OFF, the
reformatted field does NOT have MISSING = ON in the generated Master File.

The COMPMISS parameter cannot be set in an ON TABLE command.

Using Commas vs. Decimals (Continental Decimal Notation)

The CDN parameter determines the characters used for punctuation in numbers. For
information about the CDN parameter values, see the Developing Reporting Applications
manual.

Setting Characters to Represent Null and Missing Values

You can alter the appearance of your report output by specifying your own string of characters
that will appear when no data is available for a field.

Syntax:

How to Set Characters to Represent a Null or Missing Value

To specify a string for NODATA fields, use the following syntax

ON TABLE SET NODATA character string

where:

NODATA

Indicates that a NODATA character will be set.

character string

Is the string of characters that you want to appear when no data is available for a
field. The default value is a period (.).

Syntax:

How to Set the NODATA Character as a SET Command

To specify a character for NODATA fields, use the following syntax

SET NODATA=character

where:

character

Is the character or characters that you want to appear when no data is available for a
field. The maximum number of characters is 11. The default value is a period (.).

Creating Reports With TIBCO® WebFOCUS Language

 1717

Specifying Data Format in a Report

Example:

Setting the NODATA Character in a Request

This request changes the NODATA character for missing data from a period (default) to the
word NONE.

TABLE FILE EMPLOYEE
PRINT CURR_SAL
BY LAST_NAME BY FIRST_NAME
ACROSS DEPARTMENT
ON TABLE SET NODATA NONE
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, SQUEEZE=OFF,$
ENDSTYLE
END

This request produces the following report.

DEPARTMENT

LAST_NAME

FIRST_NAME

MIS

PRODUCTION

BANNING

JOHN

      NONE

$29,700.00

BLACKWOOD

ROSEMARIE

$21,780.00

      NONE

CROSS

GREENSPAN

IRVING

JONES

MCCOY

MCKNIGHT

ROMANS

SMITH

STEVENS

BARBARA

$27,062.00

      NONE

MARY

JOAN

DIANE

JOHN

ROGER

ANTHONY

MARY

RICHARD

ALFRED

 $9,000.00

      NONE

       NONE

$26,862.00

$18,480.00

      NONE

$18,480.00

      NONE

      NONE

$16,100.00

      NONE

$21,120.00

$13,200.00

      NONE

      NONE

 $9,500.00

      NONE

$11,000.00

Using Conditional Grid Formatting in a Field

You can use conditional grid formatting in order to emphasize a particular cell or field in a
report.

1718

23. Formatting Report Data

Example:

Creating a Report Using Conditional Grid Formatting

TABLE FILE CAR
SUM SALES BY CAR
ON TABLE SET STYLE *
ON TABLE PCHOLD FORMAT PDF
TYPE=DATA, COLUMN=SALES, GRID=HEAVY, WHEN=CAR EQ 'DATSUN', $
ENDSTYLE
END

The output is:

Positioning Data in a Report

You can position data within a report by selecting a justification (right, left or center) of a
column or by specifying whether or not you wish to have data wrap within a cell. For information
on positioning a column on the page, see Laying Out the Report Page on page 1331.

Controlling Wrapping of Report Data

You can control the wrapping of report data in a report, thus preventing line breaks within
report cells. When using HTML output, most web browsers will, by default, wrap alphanumeric
report data that does not fit on a single line in a cell.

This bumps the contents of the cell onto a second line. A web browser wraps data based on
its algorithmic settings. Use the WRAP attribute if you wish to suppress a web browser data
wrapping.

Creating Reports With TIBCO® WebFOCUS Language

 1719

Positioning Data in a Report

By default, WRAP is set to ON for HTML output, allowing each individual browser to define the
width of each column in the report. For PDF, PS, DHTML, PPT, and PPTX output, WRAP is set
OFF by default. For these positioned output formats in which the location of each item in the
report is explicitly defined, WRAP = ON is not a valid value, except when specified for
ACROSSVALUE. For other elements of the report, such as headers, footers, titles, or data,
define the width of wrapped lines by using a numerical value, as in WRAP = n.

In PDF and PostScript report output, you can control the line spacing in wrapped lines by using
the WRAPGAP attribute.

Wrapping Data in PDF Reports That Use the OVER Phrase

OVER allows the presentation of a single data record across multiple lines within a report. By
default, when OVER is defined within a request, the report shifts from a columnar presentation
to a row level presentation. The field titles are displayed to the left of each value, rather than
at the top of each column. This layout was not designed to be aligned in any specific fashion
but to allow for the presentation of multiple elements of data within a small area. In many
cases, reports that place columns over each other use blank AS names in order to align the
columns properly. You can use the WRAP attribute to wrap data in PDF reports that use OVER
and this technique works well with blank AS names.

Wrapping Data in PDF Reports That Use the ACROSS Phrase

In a request that uses ACROSS, the output displays each value of the ACROSS field above the
set of data columns applicable to that ACROSS value.

If the ACROSS value is longer than the width of its columns, you can wrap the ACROSS value
within the width of its underlying columns.

By default, the width of each ACROSS value group (the ACROSS value and the data columns
within) is defined as the largest of either the sum of the width of the data columns or the
largest ACROSS value for that group. With wrapping, the size of each ACROSS wrap will be
defined by the width defined based on this rule including all data columns and any non-
wrapped across fields.

The width of each ACROSS column for a given ACROSS group is defined as the length of the
largest value for that ACROSS group. A single width is used for each group so in groups where
the values are shorter than the longest value, you will see a larger right gap within the cell.

For reports containing multiple ACROSS fields, you can wrap individual ACROSS fields or all of
them. Each designated value will wrap within the defined ACROSS group.

1720

Syntax:

How to Control Wrapping of Report Data

To control wrapping of text inside a report, use the following syntax within a StyleSheet.

23. Formatting Report Data

TYPE=type, [subtype,] WRAP=value, $

where:

type

Is the report component you wish to affect, such as REPORT, HEADING, or TITLE.

subtype

Is any additional attribute, such as COLUMN, ACROSS, ITEM etc. that is needed to identify
the report component that you are formatting. See Identifying a Report Component in a
WebFOCUS StyleSheet on page 1249 for more information about how to specify different
report components.

value

Is one of the following:

ON, which turns on data wrapping. ON is the default value for HTML report output. For
PDF, PS, DHTML, PPT, and PPTX report output, WRAP is set OFF by default. For these
positioned output formats in which the location of each item in the report is explicitly
defined, WRAP = ON is not a valid value, except when specified for ACROSSVALUE. For
other elements of the report, such as headers, footers, titles, or data, define the width
of wrapped lines by using a numerical value, as in WRAP = n. For HTML reports, WRAP
is supported with all fields. For PDF reports, WRAP is supported only with embedded
fields, not text.

Note: This setting is not supported when using WRAP with OVER in PDF report output.

OFF, which turns off data wrapping. This is the default value for PDF, PS, DHTML, PPT,
and PPTX report output.

n, which represents a specific numeric value that the column width can be set to. The
value represents the measure specified with the UNITS parameter. This setting is
supported for wrapping data in PDF reports that use the OVER phrase.

Note: WRAP=ON and WRAP=n are not supported with JUSTIFY.

Creating Reports With TIBCO® WebFOCUS Language

 1721

Positioning Data in a Report

Example:

Allowing the Web Browser to Wrap Report Data

The following example, with WRAP=ON, wraps report data based on the web browser
functionality. Note that because this value is the default, there is no need to specify WRAP=ON
in the report request syntax.

TABLE FILE GGPRODS
PRINT SIZE UNIT_PRICE PACKAGE_TYPE
VENDOR_CODE VENDOR_NAME
BY PRODUCT_ID BY PRODUCT_DESCRIPTION
ON TABLE SET STYLE *
TYPE=REPORT, GRID=ON, $
ENDSTYLE
END

Note: Wrap is determined by the size of your browser window, so you may need to shrink your
window to see the example wrap the data as in the following image.

Notice that records in the Vendor Name column break to a second line.

Example:

Suppressing the Wrapping of Report Data

The following report request, with WRAP=OFF, suppresses the web browser data wrapping:

TABLE FILE GGPRODS
PRINT SIZE UNIT_PRICE PACKAGE_TYPE
VENDOR_CODE VENDOR_NAME
BY PRODUCT_ID BY PRODUCT_DESCRIPTION
ON TABLE SET STYLE *
TYPE=REPORT, WRAP=OFF, $
TYPE=REPORT, GRID=ON, $
ENDSTYLE
END

1722

The output is:

23. Formatting Report Data

Example: Wrapping Columns With OVER

The following request against the GGPRODS data source places the column VENDOR_NAME on
a new line with the OVER phrase. By default, wrap is turned off and must be defined explicitly
within the StyleSheet:

TABLE FILE GGPRODS
PRINT SIZE UNIT_PRICE PACKAGE_TYPE OVER
VENDOR_NAME
BY PRODUCT_ID BY PRODUCT_DESCRIPTION
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, SQUEEZE=ON, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1723

Positioning Data in a Report

The partial output is shown in the following image.

The following version of the request turns wrapping on and sets a column width of 1.5 for the
VENDOR_NAME column, which has been placed on a new line because of the OVER phrase:

TABLE FILE GGPRODS
PRINT SIZE UNIT_PRICE PACKAGE_TYPE OVER
VENDOR_NAME
BY PRODUCT_ID BY PRODUCT_DESCRIPTION
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, COLUMN=VENDOR_NAME, WRAP=1.5,$
ENDSTYLE
END

1724

The partial output shows that the VENDOR_NAME column now wraps. Notice that turning WRAP
ON causes the OVER value, not the OVER TITLE, to wrap:

23. Formatting Report Data

Syntax:

How to Wrap ACROSS Values

Wrapping ACROSS Values is supported for HTML and PDF output formats.

TYPE=ACROSSVALUE, [ACROSS={fieldname|Nn|An}] WRAP={OFF|ON} ,$

where:

ACROSS

If you have a request with multiple ACROSS fields, you can identify each field using
the ACROSS identifier. You only need to include the ACROSS identifier if you have
multiple ACROSS fields in your request.

fieldname

Specifies a horizontal sort row by its field name.

Nn

Identifies a column by its position in the report. To determine this value, count vertical
sort (BY) fields, display fields, and ROW-TOTAL fields, from left to right, including
NOPRINT fields.

Creating Reports With TIBCO® WebFOCUS Language

 1725

Positioning Data in a Report

An

OFF

ON

Specifies a horizontal sort row by its position in the sequence of horizontal sort rows.
To determine this value, count horizontal sort (ACROSS) fields. Cannot be combined
with a field name specification in the same StyleSheet.

Turns off wrapping of the ACROSS values. OFF is the default value.

Turns on wrapping of the ACROSS values.

Note: WRAP=ON is not supported with JUSTIFY.

Example: Wrapping ACROSS Values in PDF Report Output

In the following request against the GGPRODS data source, VENDOR_NAME is an ACROSS
field:

TABLE FILE GGPRODS
HEADING
" PRODUCT REPORT"
" "
PRINT PRODUCT_ID UNIT_PRICE/D5
ACROSS VENDOR_NAME
BY SIZE
WHERE VENDOR_NAME GT 'B' AND VENDOR_NAME LT 'F'
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=REPORT, COLUMN=PRODUCT_ID, WIDTH=.25, $
TYPE=REPORT, COLUMN=UNIT_PRICE, WIDTH=.25, $
ENDSTYLE
END

As shown in the following image, the output is too wide for one panel because some of the
ACROSS field values (vendor names) are longer than the sum of the product code and unit
price columns under them.

1726

The following version of the request wraps the ACROSS values (TYPE=ACROSSVALUE,
WRAP=ON ,$):

23. Formatting Report Data

TABLE FILE GGPRODS
HEADING
" PRODUCT REPORT"
" "
PRINT PRODUCT_ID UNIT_PRICE/D5
ACROSS VENDOR_NAME
BY SIZE
WHERE VENDOR_NAME GT 'B' AND VENDOR_NAME LT 'F'
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, $
TYPE=REPORT, COLUMN=PRODUCT_ID, WIDTH=.25, $
TYPE=REPORT, COLUMN=UNIT_PRICE, WIDTH=.25, $
TYPE = ACROSSVALUE, WRAP=ON,$
ENDSTYLE
END

The report now fits on one panel, as shown in the following image.

Reference: OVER With Blank Column Titles

When OVER fields are defined with blank AS names (the value of the title of the column is set
to empty ' '), they can be used to build a report with multiple data lines that present in an
aligned grid fashion.

In this type of report, the column titles are usually indicated by adding multiple corresponding
lines to the page headings rather than using the default titles that display to the left of the
column field values. To present OVER fields with unique titles that take advantage of these
new alignment features, you can place the column titles in independent fields and include
them as fields within the given request.

Creating Reports With TIBCO® WebFOCUS Language

 1727

Positioning Data in a Report

Example:

Using OVER and WRAP With Blank AS Names

The following example demonstrates using OVER with blank AS names and WRAP to build a
multi-data line report:

TABLE FILE GGPRODS
PRINT PACKAGE_TYPE AS '' SIZE  AS '' OVER
VENDOR_NAME AS ''
BY PRODUCT_ID  AS ''
BY PRODUCT_DESCRIPTION  AS ''
ON TABLE SUBHEAD
"Gotham Grinds"
"Products Details"
HEADING
" Code <+0>Description<+0>Size  <+0>Package"
-*" <+0> <+0>Vendor"
" <+0>Vendor"
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, FONT=ARIAL, SIZE=10, SQUEEZE=ON,$
TYPE=REPORT, COLUMN=PACKAGE_TYPE, SQUEEZE=.5 ,$
TYPE=REPORT, COLUMN=VENDOR_NAME, WRAP=1 ,$
TYPE=REPORT, BORDER=ON, $
TYPE=HEADING, LINE=1, ITEM=1, BORDER=ON, $
TYPE=HEADING, LINE=1, ITEM=2, BORDER=ON, POSITION=PRODUCT_DESCRIPTION,$
TYPE=HEADING, LINE=1, ITEM=3, BORDER=ON, POSITION=SIZE ,$
TYPE=HEADING, LINE=1, ITEM=4, BORDER=ON, POSITION=PACKAGE_TYPE, $
TYPE=HEADING, LINE=2, ITEM=1, BORDER=ON, $
TYPE=HEADING, LINE=2, ITEM=2, BORDER=ON, POSITION=PACKAGE_TYPE,$
ENDSTYLE
END

1728

23. Formatting Report Data

On the report output, the Package Type and Size have been placed over the vendor name. The
page heading has the corresponding titles. In the heading, the titles Package and Size have
also been placed over the title Vendor Name. Note that the vendor name data wraps to
maintain the alignment.

Reference: OVER and WRAP With Non-Blank Column Titles

The width of both the column title and the column data for each OVER value is determined by
the single SQUEEZE or WRAP value. The title will automatically size to the same width as the
wrapped data column. If the column title is wider than the width defined for the column wrap,
you can either define a smaller title or add your titles as OVER fields that can be sized
independently.

The following examples demonstrate how to build a report with OVER and WRAP that has
column titles longer than the designated WRAP size.

Creating Reports With TIBCO® WebFOCUS Language

 1729

Positioning Data in a Report

Example:

Using OVER and WRAP With Column Titles

The following request defines two virtual fields to contain the column titles for the Product
Name and Vendor Name fields. It then prints each virtual field next to its related data field and
gives each a blank AS name. The first virtual field and data field are placed over the second
virtual field and data field:

DEFINE FILE GGPRODS
TITLE_PROD/A20 = 'Product Description';
TITLE_VEND/A20 = 'Vendor Name';
END
TABLE FILE GGPRODS
PRINT TITLE_PROD AS '' PRODUCT_DESCRIPTION  AS '' OVER
TITLE_VEND AS '' VENDOR_NAME  AS ''
BY PRODUCT_ID  AS ''
ON TABLE SUBHEAD
"Gotham Grinds"
"Products Details"
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, FONT=ARIAL, SIZE=10, SQUEEZE=ON,$
TYPE=REPORT, COLUMN=TITLE_PROD , SQUEEZE=1.25 ,$
TYPE=REPORT, COLUMN=TITLE_VEND , SQUEEZE=1.25 ,$
TYPE=REPORT, COLUMN=PRODUCT_DESCRIPTION, WRAP=.75 ,$
TYPE=REPORT, COLUMN=VENDOR_NAME, WRAP=.75 ,$
TYPE=REPORT, BORDER=ON, $
ENDSTYLE
END

1730

The output shows that the titles and data align properly.

23. Formatting Report Data

Syntax:

How to Control Spacing Between Wrapped Lines

You can use the WRAPGAP attribute in a StyleSheet to control spacing between wrapped lines
in the data elements in PDF and PostScript report output.

TYPE=DATA, WRAPGAP={ON|OFF|n}

where:

ON

Does not leave any space between wrapped lines. ON is equivalent to specifying 0.0 for n.

OFF

Places wrapped data on the next line. OFF is the default value.

Creating Reports With TIBCO® WebFOCUS Language

 1731

Positioning Data in a Report

n

Is a number greater than or equal to zero that specifies how much space to leave between
wrapped lines (using the unit of measurement specified by the UNITS attribute). Setting n
to zero does not leave any space between wrapped lines, and is equivalent to specifying
WRAPGAP=ON.

Example:

Specifying Spacing for Wrapped Lines

In the following request, wrapping is turned on for the ADDRESS_LN3 column of the report:

TABLE FILE EMPLOYEE
PRINT ADDRESS_LN3
BY LAST_NAME BY FIRST_NAME
WHERE LAST_NAME LE 'CROSS'
  ON TABLE PCHOLD FORMAT PDF
ON TABLE SET PAGE NOPAGE
ON TABLE SET STYLE *
type=report, grid=on, $
type=data, topgap=0.2, bottomgap=0.2,  $
type=data, wrapgap=off, $
type=REPORT, column=ADDRESS_LN3, wrap=1.0 ,$
ENDSTYLE
END

1732

With WRAPGAP=OFF, each wrapped line is placed on the next report line:

23. Formatting Report Data

Creating Reports With TIBCO® WebFOCUS Language

 1733

Positioning Data in a Report

With WRAPGAP=ON, the wrapped lines are placed directly under each other:

Reference: Usage Notes for WRAPGAP

You can only specify WRAPGAP for columns that have wrapping enabled (WRAP attribute or
parameter set to ON or a number). The TOPGAP and BOTTOMGAP attributes specify how much
vertical space to leave above and below a report component. Increasing the values or these
attributes makes a decrease in spacing between wrapped lines more noticeable.

Justifying Report Columns

You can adjust text within a column by specifying whether report columns are left justified,
right justified, or centered. By default, alphanumeric columns are left justified, numeric
columns are right justified, and heading and footing elements are left justified. However, you
can change the default using the JUSTIFY attribute. For information on justifying column titles
using /R /L and /C, see Using Headings, Footings, Titles, and Labels on page 1517.

1734

Syntax:

How to Justify a Report Column

To left justify, right justify, or center a column, use the following syntax within a StyleSheet.

TYPE=type, [subtype,] [COLUMN=column,] JUSTIFY=option, $

23. Formatting Report Data

where:

type

Is the report component you wish to affect, such as REPORT, HEADING, or TITLE.

subtype

Is any additional attribute, such as COLUMN, ACROSS, ITEM etc. that is needed to identify
the report component that you are formatting. For more information about how to specify
different report components, see Identifying a Report Component in a WebFOCUS
StyleSheet on page 1249.

column

Is the column or group of columns you wish to justify. This attribute is only necessary if you
wish to justify a specific column or set of columns. Omitting this attribute justifies the
entire report.

option

Is the justification you wish to select:

LEFT, which specifies that the column will be left justified.

RIGHT, which specifies that the column will be right justified.

CENTER, which specifies that the column will be centered.

Note: JUSTIFY is not supported with WRAP=ON or WRAP=n.

Example:

Justifying Data in a Report Column

The following example displays the StyleSheet syntax used to center the data in the Vendor
Name column. The header is also center justified.

TABLE FILE GGPRODS
HEADING
"PRODUCT REPORT"
SUM UNITS BY PRODUCT_DESCRIPTION BY PRODUCT_ID BY VENDOR_NAME
ON TABLE SET STYLE *
TYPE=REPORT, COLUMN=VENDOR_NAME, JUSTIFY=CENTER,  $
TYPE=HEADING, JUSTIFY=CENTER, $
TYPE=REPORT, GRID=OFF, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1735

Positioning Data in a Report

The output is:

Field-Based Reformatting

Field-based reformatting allows you to apply different formats to each row in a single report
column by using a field to identify the format that applies to each row. For example, you can
use this technique to apply the appropriate decimal currency formats when each row
represents a different country.

The field that contains the format specifications can be:

A real field in the data source.

A temporary field created with a DEFINE command.

A DEFINE in the Master File.

A COMPUTE command. If the field is created with a COMPUTE command, the command
must appear in the request prior to using the calculated field for reformatting.

The field that contains the formats must be alphanumeric and be at least eight characters in
length. Only the first eight characters are used for formatting.

The field-based format may specify a length longer than the length of the original field.
However, if the new length is more than one-third larger than the original length, the report
column width may not be large enough to hold the value (indicated by asterisks in the field).

1736

23. Formatting Report Data

You can apply a field-based format to any type of field. However, the new format must be
compatible with the original format:

A numeric field can be reformatted to any other numeric format with any edit format
options.

An alphanumeric field can be reformatted to a different length.

Any date field can be reformatted to any other date format type.

Any date-time field can be reformatted to any other date-time format.

If the field-based format is invalid or specifies an impermissible type conversion, the field
displays with plus signs (++++) on the report output. If the format field is blank or missing, the
value is displayed without reformatting.

Syntax:

How to Define and Apply a Format Field

With a DEFINE command:

DEFINE FILE filename
format_field/A8 = expression;
END

In a Master File:

DEFINE format_field/A8 = expression; $

In a request:

COMPUTE format_field/A8 = expression;

where:

format_field

Is the name of the field that contains the format for each row.

expression

Is the expression that assigns the format values to the format field.

Creating Reports With TIBCO® WebFOCUS Language

 1737

Positioning Data in a Report

After the format field is defined, you can apply it in a report request:

TABLE FILE filename
displayfieldname/format_field[/just]
END

where:

display

Is any valid display command.

fieldname

Is a field in the request to be reformatted.

format_field

Is the name of the field that contains the formats. If the name of the format field is
the same as an explicit format, the explicit format will be used. For example, a field
named I8 cannot be used for field-based reformatting because it will be interpreted as
the explicit format I8.

just

Is a justification option, L, R, or C. The justification option can be placed before or
after the format field, separated from the format by a slash.

Example:

Displaying Different Decimal Places for Currency Values

DEFINE FILE CAR
CFORMAT/A8 = DECODE COUNTRY('ENGLAND' 'D10.1' 'JAPAN' 'D10' ELSE
'D10.2');
END

TABLE FILE CAR
SUM SALES/CFORMAT/C DEALER_COST/CFORMAT
BY COUNTRY
END

The output is:

COUNTRY       SALES    DEALER_COST
-------     ---------  -----------
ENGLAND      12,000.0     37,853.0
FRANCE            .00     4,631.00
ITALY       30,200.00    41,235.00
JAPAN          78,030        5,512
W GERMANY   88,190.00    54,563.00

1738


23. Formatting Report Data

Displaying Multi-Line An and AnV Fields

Using StyleSheet attributes, you can display An (character) and AnV (varchar) fields that
contain line breaks on multiple lines in a PDF or PostScript report. Line breaks can be based
on line-feeds, carriage-returns, or a combination of both. If you do not add these StyleSheet
attributes, all line-feed and carriage-return formatting within these fields will be ignored, and all
characters will be displayed on one line that wraps to fit the width of the report.

Syntax:

How to Display An and AnV Fields Containing Line Breaks on Multiple Lines

TYPE=REPORT,LINEBREAK='type',$

where:

REPORT

Is the type of report component. TYPE must be REPORT. Otherwise an error will result.

'type'

Specifies that line breaks will be inserted in a report based on the following:

LF inserts a line break after each line-feed character found in all An and AnV fields.

CR inserts a line break after each carriage-return character found in all An and AnV fields.

LFCR inserts a line break after each combination of a line-feed character followed by a
carriage-return character found in all An and AnV fields.

CRLF inserts a line break after each combination of a carriage-return character followed by
a line-feed character found in all An and AnV fields.

Note: This feature is supported in PDF, PPTX, or PS formats.

Creating Reports With TIBCO® WebFOCUS Language

 1739

Positioning Data in a Report

Example:

Displaying an Alphanumeric Field With Line Breaks in a PDF Report

The following request defines an alphanumeric named ANLB field with a semicolon (in an
EDCDIC environment) or a circumflex (in an ASCII environment) in the middle. The CTRAN
function then replaces the semicolon or circumflex with a carriage return character and stores
this string in a field named ANLBC. On the report output, this field displays on two lines:

DEFINE FILE EMPLOYEE
ANLB/A40 ='THIS IS AN An FIELD;WITH A LINE BREAK.';
ANLBC/A40 = CTRAN(40, ANLB, 094, 013  , ANLBC);
END
TABLE FILE EMPLOYEE
PRINT LAST_NAME ANLBC
WHERE LAST_NAME EQ 'BLACKWOOD'
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT,LINEBREAK='CR',$
ENDSTYLE
END

The output is:

Example:

Using an Alphanumeric Field With a Line Break in a Subfoot

The following request defines an alphanumeric named ANLB field with a semicolon in the
middle. The CTRAN function then replaces the semicolon (hex 094 in an EBCDIC environment,
hex 059 in an ASCII environment) with a carriage return character and stores this string in a
field named ANLBC. In the subfoot, this field displays on two lines.

The following report request is for an EBCDIC environment:

1740

23. Formatting Report Data

DEFINE FILE EMPLOYEE
ANLB/A40 ='THIS IS AN An FIELD;WITH A LINE BREAK.';
ANLBC/A40 = CTRAN(40, ANLB, 094, 013  , ANLBC);
END
TABLE FILE EMPLOYEE
PRINT FIRST_NAME
BY LAST_NAME
WHERE LAST_NAME EQ 'BLACKWOOD'
ON LAST_NAME SUBFOOT
  " "
  " <ANLBC "
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT,LINEBREAK='CR',$
ENDSTYLE
END

The following report request is for an ASCII environment:

DEFINE FILE EMPLOYEE
ANLB/A40 ='THIS IS AN An FIELD;WITH A LINE BREAK.';
ANLBC/A40 = CTRAN(40, ANLB, 059, 013  , ANLBC);
END
TABLE FILE EMPLOYEE
PRINT FIRST_NAME
BY LAST_NAME
WHERE LAST_NAME EQ 'BLACKWOOD'
ON LAST_NAME SUBFOOT
  " "
  " <ANLBC "
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT,LINEBREAK='CR',$
ENDSTYLE
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1741

Positioning Data in a Report

1742

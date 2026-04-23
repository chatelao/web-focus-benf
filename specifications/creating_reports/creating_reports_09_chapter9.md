Chapter9

Choosing a Display Format

You can choose from several different display formats when you display a report on the
screen. Some display formats are best suited for particular kinds of uses. For example,
you can choose to display the report as:

An HTML page, which is optimized for display in a web browser.

A PDF document, which is useful when you want the report to look the same whether
displayed on a screen or printed.

A DHTML file, which is HTML output that has most of the features normally
associated with output formatted for printing, such as PDF or PostScript output.

An Excel 2007 worksheet, where you can work with the data in Excel 2007 or higher.

An Excel 2000 worksheet, where you can work with the data in Excel 2000 or 2003.

You can learn which display formats are available in Report Display Formats on page
576.

If you wish to send a report to a file instead of to the screen, you can learn about the file
formats that are available in Saving and Reusing Your Report Output on page 471.

In this chapter:

Report Display Formats

Preserving Leading and Internal Blanks in Report Output

Using Web Display Format: HTML

Using Print Display Formats: PDF, PS

Using Word Processing Display Formats: DOC, WP

Saving Report Output in Excel XLSX Format

Using PowerPoint PPT Display Format

Saving Report Output in PPTX Format

Creating Reports With TIBCO® WebFOCUS Language

 575

Report Display Formats

Report Display Formats

You can choose from among several display formats for your report:

Web format: HTML. For more information, see Using Web Display Format: HTML on page
581.

Print formats: PDF (Adobe Acrobat Portable Document Format) and PostScript (PS). For
more information, see Using Print Display Formats: PDF, PS on page 584.

Word-processing formats: WP and DOC. For more information, see Using Word Processing
Display Formats: DOC, WP on page 643.

Worksheet formats: Excel 2007/2010 XML-based format, Excel 2000/2003 HTML-based
format, with variations for Excel 2000 PivotTable and Excel 2000 FORMULA, Excel 97
HTML-based format, and Excel binary format. For more information, see Saving Report
Output in Excel XLSX Format on page 644.

A note about DHTML and HTML: DHTML is the absolute positioning version of HTML. As
architected, format HTML generates output in a table-based format that leaves the exact
positioning to the browser that is presenting the report. Format DHTML on the other hand is
designed to render with the user-defined positioning in the same way as PDF. This means
things should position on the page precisely as defined in the report procedure. PDF, DHTML,
PPT, PPTX, and PS are position-based. HTML and EXL2K are table or cell based. Therefore,
DHTML output looks more like PDF rather than HTML.

For information about which file formats are available for saving and reusing (as opposed to
displaying) report data, see Saving and Reusing Your Report Output on page 471.

Note: For styled output formats, setting the LINES parameter to 999 or higher generates
continuous forms. When continuous forms are specified, but the output format has a physical
page size (as is the case with PDF output), the column titles repeat at the top of the physical
page, without page numbers.

Syntax:

How to Choose a Display Format Using PCHOLD

You can display a report on screen using the ON TABLE PCHOLD command in a report request.

ON TABLE PCHOLD FORMAT formatname

where:

formatname

Can be one of the following:

576

DOC

EXCEL

XLSX

EXL2K

EXL2K FORMULA

9. Choosing a Display Format

Specifies that the report will be displayed as a plain-text word
processing document, with page breaks, in Microsoft Word within
your web browser. See ○k

Using Word Processing Display Formats: DOC, WP on page 643.

Specifies that the report will be displayed as an Excel
spreadsheet. See Saving Report Output in Excel XLSX Format on
page 644.

Specifies that the report will be displayed as an Excel
2007/2010 worksheet. See Saving Report Output in Excel XLSX
Format on page 644.

Specifies that the report will be displayed as an Excel
2000/2003 worksheet.

Specifies that the report will be displayed as an Excel
2000/2003 worksheet, with WebFOCUS totals and other
calculated values translated to active Excel formulas. (If your
report does not contain any formulas, consider using EXL2K
format since EXL2K FORMULA requires additional processing
time.)

EXL2K PIVOT

Specifies that the report will be displayed as an Excel
2000/2003 PivotTable.

EXL97

HTML

PDF

PostScript
(PS)

Specifies that the report will be displayed as an Excel 97
worksheet.

Specifies that the report will be displayed as an HTML page. See
Using Web Display Format: HTML on page 581.

Specifies that the report will be displayed as a PDF document
(Adobe Acrobat's Portable Document Format). See Using PDF
Display Format on page 585.

Specifies that the report will be displayed as a PostScript
document. You must have installed a third party tool capable of
displaying PS. See Using PostScript (PS) Display Format on page
620.

Creating Reports With TIBCO® WebFOCUS Language

 577

Report Display Formats

WP

Specifies that the report will be displayed as a plain-text word
processing document in the web browser. See Using Word
Processing Display Formats: DOC, WP on page 643.

Syntax:

How to Choose a Display Format Using SET ONLINE-FMT

For a limited set of formats, you can display a report on screen using the SET command
ONLINE-FMT parameter.

Outside of a report request, use the following syntax to specify a format for all report requests
within the procedure

SET ONLINE-FMT = formatname

Within a report request, use the following syntax to specify a format for that request only

ON TABLE SET ONLINE-FMT formatname

where:

formatname

Can be one of the following:

HTML (default)

Specifies that the report will be displayed as an HTML page. See
Using Web Display Format: HTML on page 581.

PDF

XLSX

EXL2K

EXL97

Specifies that the report will be displayed as a PDF document
(Adobe Acrobat Portable Document Format). See Using PDF
Display Format on page 585.

Specifies that the report will be displayed as an Excel
2007/2010 worksheet. See Saving Report Output in Excel XLSX
Format on page 644.

Specifies that the report will be displayed as an Excel
2000/2003 worksheet.

Specifies that the report will be displayed as an Excel 97
worksheet.

578

9. Choosing a Display Format

PostScript (PS)

Specifies that the report will be displayed as a PostScript
document. You must have installed a third party tool capable of
displaying PS. See Using PostScript (PS) Display Format on page
620.

STANDARD

Specifies that the report will be displayed using a legacy
character-based and line-based layout and a monospaced font.

Tip: ONLINE-FMT syntax will be superseded by PCHOLD syntax in future releases of WebFOCUS
(see How to Choose a Display Format Using PCHOLD on page 576). At present, they can be
used interchangeably.

Reference: Specifying MIME Types for WebFOCUS Reports

In addition to creating reports in HTML format for display in a web browser, you can generate
reports that can be returned to the browser and opened in a desktop application or in a helper
application. In order for the browser to recognize and call the correct desktop application, you
must associate the MIME (Multipurpose Internet Mail Extension) type of the report with a
specific application.

For details, see the Developing Reporting Applications manual.

Preserving Leading and Internal Blanks in Report Output

By default, HTML browsers and Excel remove leading and trailing blanks from text and
compress multiple internal blanks to a single blank.

If you want to preserve leading and internal blanks in HTML and EXL2K report output, you can
issue the SET SHOWBLANKS=ON command.

Even if you issue this command, trailing blanks will not be preserved except in heading,
subheading, footing, and subfooting lines that use the default heading or footing alignment.

Creating Reports With TIBCO® WebFOCUS Language

 579

Preserving Leading and Internal Blanks in Report Output

Syntax:

How to Preserve Leading and Internal Blanks in HTML and EXL2K Reports

In a FOCEXEC or in a profile, use the following syntax:

SET SHOWBLANKS = {OFF|ON}

In a request, use the following syntax

ON TABLE SET SHOWBLANKS {OFF|ON}

where:

OFF

Removes leading blanks and compresses internal blanks in HTML and EXL2K report
output.

ON

Preserves leading blanks and internal blanks in HTML and EXL2K report output. Also
preserves trailing blanks in heading, subheading, footing, and subfooting lines that use the
default heading or footing alignment.

Example:

Preserving Leading and Internal Blanks in HTML and EXL2K Report Output

The following request creates a virtual field that adds leading blanks to the value ACTION and
both leading and internal blanks to the values TRAIN/EX and SCI/FI in the CATEGORY field. It
also adds trailing blanks to the value COMEDY:

SET SHOWBLANKS = OFF
DEFINE FILE MOVIES
NEWCAT/A30 = IF CATEGORY EQ 'ACTION' THEN '  ACTION'
        ELSE IF CATEGORY EQ 'SCI/FI' THEN 'SCIENCE   FICTION'
        ELSE IF CATEGORY EQ 'TRAIN/EX' THEN '   TRAINING    EXERCISE'
        ELSE IF CATEGORY EQ 'COMEDY' THEN 'COMEDY     '
        ELSE                'GENERAL';
END
TABLE FILE MOVIES
SUM CATEGORY LISTPR/D12.2 COPIES
BY NEWCAT

ON TABLE SET STYLE *
GRID=OFF,$
TYPE=REPORT, FONT=COURIER NEW,$
ENDSTYLE
END

580

With SHOWBLANKS OFF, these additional blanks are removed:

9. Choosing a Display Format

With SHOWBLANKS ON, the additional leading and internal blanks are preserved. Note that
trailing blanks are not preserved:

Using Web Display Format: HTML

You can display a report as an HTML page. HTML supports most style sheet options
(especially when used with an internal cascading style sheet), allowing for full report
formatting.

By default, leading and internal blanks are compressed on the report output. For information
on preserving them, see Preserving Leading and Internal Blanks in Report Output on page 579.

For more information, see Controlling Report Formatting on page 1219.

HTML is the default display format when WebFOCUS is installed. An HTML report opens in your
web browser.

If you do not wish to rely on the default, you can specify that a report display as an HTML page
when you run the report. You can use either:

PCHOLD command. For more information, see How to Choose a Display Format Using
PCHOLD on page 576.

ONLINE-FMT parameter of the SET command. For more information, see How to Choose a
Display Format Using SET ONLINE-FMT on page 578.

Creating Reports With TIBCO® WebFOCUS Language

 581

Using Web Display Format: HTML

HTML display format requires that the SET command's STYLESHEET parameter be set to any
value except OFF. Appropriate values include ON (the default), the name of a StyleSheet file, or
an inline StyleSheet (*).

Reporting and formatting options that are supported for HTML are described and illustrated
extensively throughout the WebFOCUS language documentation.

You can additionally customize the display of HTML reports with any JavaScript or VBScript
function using the JSURL SET parameter. For details, see the Developing Reporting Applications
manual.

Example:

Customizing the Display of an HTML Report

The following example illustrates how you can customize the display of an HTML report by
calling your own JavaScript function in addition to the Information Builders default JavaScript
functions. Use the JSURL SET parameter to accomplish this.

The JavaScript function shown here disables the right-click menu when you run a report.

1. Create a js file and save it in a location accessible by the web server.

For example, the following disables the right-click menu in an HTML report:

function setnocontextclick () {
   if (document.body != null) {
      document.body.oncontextmenu=new Function("return false");
   }
   else
      window.setTimeout("setnocontextclick()",100);
}
function killmenuOnLoadFunc(arrayofonloads,currentindex) {
     setnocontextclick();
}

This file is saved as killmenu.js in the ibi_apps/ibi_html directory.

Note: The onload function must be named in the format.

customfunctionnameOnLoadFunc

where:

customfunctionname

Is the name of the JavaScript file that contains the function code.

2. Add the JSURL parameter to your TABLE request. You can add the command to the

edasprof.prf file if you want the js file to run with every HTML report that is run on that
server.

3. Run the report.

582

9. Choosing a Display Format

SET JSURL=/ibi_apps/ibi_html/killmenu.js
TABLE FILE CENTORD
SUM QUANTITY
BY PLANTLNG
END

The right-click menu option is not available in the report output.

Example:

Disabling Default WebFOCUS JavaScript Functions

You can disable or modify default WebFOCUS JavaScript functions using the JSURL SET
parameter. The following example illustrates how all WebFOCUS default functions can be
displayed in an alert box and disabled.

1. Create a js file and save it in a location accessible by the web server.

This file is saved as disable.js in the ibi_apps/ibi_html directory. The arrayofonloads array
consists of two string parameters, str1 and str2. str1 is the name of the function to call on
load. str2 is a Boolean (true/false) that indicates whether or not to perform the action
described by str1. The currentindex parameter is a sequence number that defines the order
in which the function is loaded when the page is displayed.

function disableOnLoadFunc(arrayofonloads,currentindex) {
  buffer ="";
   for (var index=0;index<arrayofonloads.length;index++) {
      buffer += arrayofonloads[index].str1+"\n" ;
      arrayofonloads[index].str2=false;
   }
   alert(buffer);
}

2. Add the JSURL parameter to your TABLE request.

3. Run the report.

-OLAP ON
SET AUTODRILL = ON
SET JSURL=/ibi_apps/ibi_html/disable.js
TABLE FILE CENTORD
SUM QUANTITY
BY PLANTLNG
END

Creating Reports With TIBCO® WebFOCUS Language

 583

Using Print Display Formats: PDF, PS

The output looks like this:

Reference: Usage Notes for HTML Report Output

The default behavior for HTML format when borders are turned on is to display column titles
without the underline. To display column titles with underlines when borders are on, set
GRID OFF.

The AUTOFIT parameter automatically resizes HTML report output to fit the container
(window or frame). For procedures that contain multiple report output, if AUTOFIT is set to
ON in any of the report output procedures, the setting will apply to all report output on the
page.

AUTOFIT is supported using the Accordion, On Demand Paging, HTML TOC, and HFREEZE
interactive reporting features.

For more information on the AUTOFIT parameter, see the Developing Reporting Applications
manual.

Using Print Display Formats: PDF, PS

PDF (Adobe Acrobat Portable Document Format) is most often used to distribute and share
electronic documents through the web. It is especially useful if you want a report to maintain
its presentation and layout regardless of a browser or printer type. For details, see Using PDF
Display Format on page 585.

584

9. Choosing a Display Format

PS (PostScript format), a print-oriented page description language, is most often used to send
a report directly to a printer. While used less frequently as an online display format, you can
display PS report output on your monitor before printing it. For details, see Using PostScript
(PS) Display Format on page 620.

With the exception of drill-downs, all of the report formatting features that are supported for
PDF are also supported for PostScript output.

You can specify that a report display as a PDF or PS document when you run the report. You
can use either:

PCHOLD command. For more information, see How to Choose a Display Format Using
PCHOLD on page 576.

ONLINE-FMT parameter of the SET command. For more information, see How to Choose a
Display Format Using SET ONLINE-FMT on page 578.

You can combine multiple styled reports into a single PDF or PS file. For details, see Laying
Out the Report Page on page 1331.

PDF and PS reports, including compound reports, can be distributed using ReportCaster. See
the ReportCaster documentation for details.

Using PDF Display Format

You can display a report as a PDF document. PDF (Adobe Acrobat Portable Document Format)
supports most StyleSheet attributes, allowing for full report formatting. The wide range of
StyleSheet features supported for PDF are described throughout this documentation.

PDF prints and displays a document consistently, regardless of the application software,
hardware, and operating system used to create or display the document.

The report opens in Adobe Acrobat or Acrobat Reader within a web browser. To display a PDF
report, a computer must have Adobe Acrobat Reader installed. For free downloads of Acrobat
Reader, go to http://www.adobe.com.

Limit: Adobe Acrobat PDF format limits the number of pages, hyperlinks, and images in a
document. For information about what limits this creates for a WebFOCUS report in PDF
format, see Saving and Reusing Your Report Output on page 471.

Other print-oriented display formats. You can also display a report as a PostScript document.
For more information, see Using PostScript (PS) Display Format on page 620.

Creating Reports With TIBCO® WebFOCUS Language

 585

Using Print Display Formats: PDF, PS

Syntax:

How to Compress a PDF Output File

File compression can be used to minimize the physical size of the PDF output file. Using this
PDF-specific feature, you can generate smaller PDF files, making them easier to store and
distribute, while having no visible effect on the formatting or content of the reports they
contain.

SET FILECOMPRESS = {ON|OFF}

where:

ON

OFF

Compresses PDF output files.

Does not compress PDF output files. OFF is the default value.

This command applies to PDF output only. It is ignored by all other output formats, such as
HTML and Excel.

Displaying Watermarks in PDF Output

Watermarks are images or text strings that are placed on the bottom layer of a document and
displayed through the transparent layered content.

WebFOCUS backcolor does not support transparency. Therefore, standard images placed
below it on the page may be obscured. To resolve this, in PDF reports, WebFOCUS mirrors the
approach taken by standard printers, and places an opaque image on the top of the document
layers. With this approach, the layers of the document will be visible beneath the transparent
watermark image.

Watermark images are provided by the report developer. When creating a transparent image,
the image needs to be created in GIF format with a transparent background.

Reference: Inserting Images in PDF Reports With Backcolor

Watermarks are supported for PDF output in compound reports and in single TABLE requests.
Each document supports a single active watermark image. This image is designated as the
watermark image, by defining the placement order within the Z-INDEX attribute.

The first image with a Z-INDEX value will be considered the active watermark for the current
document. Any subsequent images, defined with style sheet attributes for Z-INDEX or OPACITY,
will be displayed as standard WebFOCUS images.

Watermark images are designated by defining the following attributes in the style sheet for the
transparent GIF.

586

Z-INDEX=TOP

OPACITY=n

9. Choosing a Display Format

Designates that the image is to be handled as a watermark
image and should always be placed on top of all other objects on
the page. This value will be respected as the topmost layer and
will be supported with other layers in future releases.

Where n represents the percent (%) of OPACITY to be applied to
the image. The greater the OPACITY, the less transparent the
image. Less of the underlying report will be visible below the
image. The value for n can be any number from 0 through 100. If
a value is not specified, it defaults to 100%, presenting a fully
opaque image.

Within a single TABLE request:

TYPE=<REPORT|HEADING>, OBJECT=IMAGE, IMAGE=<image.gif>,
Z-INDEX=TOP, OPACITY=15, POSITION=(.25 .25), DIMENSION=(8 10.5),$

Within compound syntax:

On Page Master

PAGELAYOUT=ALL, NAME='Page Master', $
OBJECT=IMAGE, IMAGE= internalonlyport.GIF, Z-INDEX=TOP, OPACITY=15,
POSITION=(.25 .25), DIMENSION=(8 10.5),$

On Page Layout

PAGELAYOUT=1, NAME='Page Layout1', $
OBJECT=IMAGE, IMAGE= internalonlyport.GIF, Z-INDEX=TOP, OPACITY=15,
POSITION=(.25 .25), DIMENSION=(8 10.5),$

Example:

Inserting Transparent Images Into a PDF Report

The following request against the GGSALES data source places the coffee image (coffee.gif) on
the page and layers the watermark image (internalonlyport.gif) on top. These images are
displayed on every page of the report.

Creating Reports With TIBCO® WebFOCUS Language

 587

Using Print Display Formats: PDF, PS

TABLE FILE GGSALES
SUM
     GGSALES.SALES01.DOLLARS/D12CM
     GGSALES.SALES01.UNITS/D12C
     GGSALES.SALES01.BUDDOLLARS/D12CM
     GGSALES.SALES01.BUDUNITS/D12C
BY GGSALES.SALES01.REGION
BY GGSALES.SALES01.CATEGORY
BY GGSALES.SALES01.PRODUCT
HEADING
"Gotham Grinds"
"Product Sales By Region"
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
   INCLUDE = endeflt,
   TOPMARGIN=.5,
   BOTTOMMARGIN=.5,
   LEFTMARGIN=1,
   RIGHTMARGIN=1,
$
TYPE=REPORT,
    OBJECT=IMAGE,
    IMAGE=internalonlyport.gif,
    POSITION=(+0.70000 +0.70000),
    SIZE=(7 7.5),
    Z-INDEX=TOP, OPACITY=15,
$
TYPE=REPORT,
    OBJECT=IMAGE,
    IMAGE=coffee.gif,
    POSITION=(+1.0 +0.5),
    SIZE=(.5 .5),
$ENDSTYLE
END

588

The output is:

9. Choosing a Display Format

Creating Reports With TIBCO® WebFOCUS Language

 589

Using Print Display Formats: PDF, PS

Features Supported

The following core PDF features are supported with watermarks:

Standard TABLE requests, including reports with paneling

Compound report (MERGE=OFF)

Coordinated compound report (MERGE=ON)

Old compound syntax (OPEN/CLOSE)

Drilldown

Drillthrough

Bookmarks

Borders/backcolor

Limits

OPACITY must be between 0 and 100, inclusive.

A single watermark image is supported for a single document.

Usage Notes

For new compound syntax, the first watermark image found in the syntax will be used for
the report. Any other watermark images found in the code will be ignored or displayed as
standard WebFOCUS images.

For old compound syntax, the watermark image must be in the first report. If it is not in the
first report, a FOC3362 message is generated.

The embedded PDF viewer for a browser may not display NLS characters correctly. If NLS
characters do not display correctly, use font embedding, as described in Adding PostScript
Type 1 Fonts for PS and PDF Formats on page 625, or configure your browser to use
Adobe Reader.

Scaling PDF Report Output to Fit the Page Width

By default, if PDF report output is too wide to fit on a single page, the report generates multiple
panels of the same page for the columns that do not fit. The page numbers specify the page
and panel numbers. For example, page numbers 1.1 and 1.2 represent page 1/panel 1 and
page 1/panel 2.

590

9. Choosing a Display Format

You can scale the output to fit across the width of the page using the PAGE-SCALE StyleSheet
attribute or the PAGE-SCALE SET parameter.

Reference: Usage Notes for PAGE-SCALE

PAGE-SCALE is supported for PDF report output only.

When a page is scaled to fit more content on the page horizontally, fewer vertical pages
may be generated, as well.

Example:

Scaling PDF Report Output to Fit the Page Width

The following request generates PDF report output without using page scaling.

SET SQUEEZE=ON
DEFINE FILE WF_RETAIL_LITE
SHOWPIC/A100='C:\ibi\WebFOCUS82\samples\web_resource\signin\images
\favicon.jpg';
END

TABLE FILE WF_RETAIL_LITE
PRINT  PRODUCT_CATEGORY
COGS_US REVENUE_US MSRP_US DISCOUNT_US GROSS_PROFIT_US QUANTITY_SOLD
BY SHOWPIC NOPRINT
BY CONTINENT_NAME
BY COUNTRY_NAME
WHERE COUNTRY_NAME EQ 'FRANCE' OR 'ITALY'
WHERE RECORDLIMIT=3000;
ON TABLE SUBHEAD
" "
" "
" Report Without PDF Scaling "
" "
" "
ON COUNTRY_NAME SUBHEAD
" "
" "
ON TABLE PCHOLD FORMAT PDF

ON TABLE SET STYLE *
TYPE=DATA, COLUMN=CONTINENT_NAME, FONT=COMIC SANS MS,
  COLOR=BLUE, STYLE=BOLD+ITALIC, $
TYPE=DATA, COLUMN=PRODUCT_CATEGORY, COLOR=FUSCHIA, $
TYPE=HEADING, STYLE=BOLD, COLOR=RGB(0 35 95), SIZE=12, JUSTIFY=CENTER, $
TYPE=SUBHEAD, SIZE=18, STYLE=BOLD, COLOR=RED, $
TYPE=SUBHEAD, IMAGE=(SHOWPIC), SIZE=(.5 .5), $
TYPE=TABHEADING, SIZE=12, STYLE=BOLD, JUSTIFY=CENTER, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 591

Using Print Display Formats: PDF, PS

Note: The image displayed in the subheading is distributed with WebFOCUS. The path to the
image is dependent on your platform and installation options. The path in the request uses the
default installation directory on Windows.

592

The output is too wide for the page and is paneled. Page 1.1 has the columns that fit across
the width of the page, as shown in the following image.

9. Choosing a Display Format

Creating Reports With TIBCO® WebFOCUS Language

 593

Using Print Display Formats: PDF, PS

Page 1.2 has the remaining columns, as shown in the following image.

594

9. Choosing a Display Format

The following version of the request uses page scaling.

SET SQUEEZE=ON
DEFINE FILE WF_RETAIL_LITE
SHOWPIC/A100='C:\ibi\WebFOCUS82\samples\web_resource\signin\images
\favicon.jpg';
END

TABLE FILE WF_RETAIL_LITE
PRINT  PRODUCT_CATEGORY
COGS_US REVENUE_US MSRP_US DISCOUNT_US GROSS_PROFIT_US QUANTITY_SOLD
BY SHOWPIC NOPRINT
BY CONTINENT_NAME
BY COUNTRY_NAME
WHERE COUNTRY_NAME EQ 'FRANCE' OR 'ITALY'
WHERE RECORDLIMIT=3000;
ON TABLE SUBHEAD
" "
" "
" Report With PDF Scaling "
" "
" "
ON COUNTRY_NAME SUBHEAD
" "
" "
ON TABLE PCHOLD FORMAT PDF

ON TABLE SET STYLE *
TYPE=REPORT, PAGE-SCALE=AUTO, $
TYPE=DATA, COLUMN=CONTINENT_NAME, FONT=COMIC SANS MS,
  COLOR=BLUE, STYLE=BOLD+ITALIC, $
TYPE=DATA, COLUMN=PRODUCT_CATEGORY, COLOR=FUSCHIA, $
TYPE=HEADING, STYLE=BOLD, COLOR=RGB(0 35 95), SIZE=12, JUSTIFY=CENTER, $
TYPE=SUBHEAD, SIZE=18, STYLE=BOLD, COLOR=RED, $
TYPE=SUBHEAD, IMAGE=(SHOWPIC), SIZE=(.5 .5), $
TYPE=TABHEADING, SIZE=12, STYLE=BOLD, JUSTIFY=CENTER, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 595

Using Print Display Formats: PDF, PS

The output is shown in the following image. All of the columns fit across the width of the page,
with no paneling.

596

9. Choosing a Display Format

Aligning a PDF Report Within a Page

You can left-align, center, or right-align an entire PDF report within a page by using the
JUSTIFYREPORT StyleSheet attribute.

To left-align, center, or right-align a PDF report, include the following syntax in your procedure.

TYPE=REPORT, JUSTIFYREPORT={LEFT|CENTER|RIGHT},$

Example:

Left-Aligning a PDF Report Within a Page

To left-align a PDF report, include the TYPE=REPORT, JUSTIFYREPORT=LEFT attribute, as
shown in the following procedure.

TABLE FILE GGSALES
SUM BUDDOLLARS
BY REGION
BY CATEGORY

HEADING
"Budget Dollars By Region and Product Category "
" "
FOOTING
"End of Report "
" "
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE PCHOLD FORMAT PDF

ON TABLE SET STYLE *
SQUEEZE=ON, GRID=ON, $
TYPE=REPORT, JUSTIFYREPORT=LEFT,$
ENDSTYLE

END

Creating Reports With TIBCO® WebFOCUS Language

 597

Using Print Display Formats: PDF, PS

The output is:

Example:

Centering a PDF Report Within a Page

To center a PDF report, include the TYPE=REPORT, JUSTIFYREPORT=CENTER attribute, as
shown in the following procedure.

TABLE FILE GGSALES
SUM BUDDOLLARS
BY REGION
BY CATEGORY

HEADING
"Budget Dollars By Region and Product Category "
" "
FOOTING
"End of Report "
" "
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE PCHOLD FORMAT PDF

ON TABLE SET STYLE *
SQUEEZE=ON, GRID=ON, $
TYPE=REPORT, JUSTIFYREPORT=CENTER,$
ENDSTYLE

END

598

The output is:

9. Choosing a Display Format

Example:

Right-Aligning a PDF Report Within a Page

To right-align a PDF report, include the TYPE=REPORT, JUSTIFYREPORT=RIGHT attribute, as
shown in the following procedure.

TABLE FILE GGSALES
SUM BUDDOLLARS
BY REGION
BY CATEGORY

HEADING
"Budget Dollars By Region and Product Category "
" "
FOOTING
"End of Report "
" "
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE PCHOLD FORMAT PDF

ON TABLE SET STYLE *
SQUEEZE=ON, GRID=ON, $
TYPE=REPORT, JUSTIFYREPORT=RIGHT,$
ENDSTYLE

END

Creating Reports With TIBCO® WebFOCUS Language

 599

Using Print Display Formats: PDF, PS

The output is:

WebFOCUS PDF Report Accessibility Support

WebFOCUS PDF report accessibility provides support for assistive technologies, such as
screen readers.

Note: For information on accessibility principles and font types and usage, see the WebAIM
website at https://webaim.org/techniques/fonts/#intro.

WebFOCUS PDF report output complies with accessibility requirements as a result of the
following features:

A SET command that activates accessibility changes to WebFOCUS PDF output code.

As of Release 8206, a DisplayOn=DOC-HEADING StyleSheet attribute that identifies the
main document heading in a compound report.

In a single standalone report (non-compound document), the first ON TABLE SUBHEAD
string is automatically tagged as <H1>. Other page headings and footings, as many as
there are available, are tagged as <H2>.

In a compound report, the DisplayOn=DOC-HEADING attribute should be added to a
single fixed-positioned component that will contain the ON TABLE SUBHEAD string. The
DOC-HEADING attribute indicates that the ON TABLE SUBHEAD string entered in the
fixed-positioned component will be tagged as <H1> and represent the main document
heading, which will be displayed once on the first physical page of the document. Other
page headings and footings, as many as there are available, are tagged as <H2>.

600

9. Choosing a Display Format

A USEASTITLES StyleSheet attribute that places and aligns custom column titles in a
heading.

A BOOKMARK StyleSheet attribute that enables you to go directly to a destination in a
document.

An ALT StyleSheet attribute that describes an image embedded in a report.

An ALT StyleSheet attribute that provides a description of a drill-down component.

A LANG attribute that identifies the default language of the document.

Report output, with the SET ACCESSPDF command enabled, is created with
BYDISPLAY=ON, which produces a value in each cell for sort (BY) fields.

Note: It is the responsibility of the report developer to follow general accessibility standards in
order for the report to be 508 compliant.

Controlling PDF Code For Accessibility

The SET ACCESSPDF command enables accessibility for PDF reports.

Syntax:

How to Control PDF Code Accessibility

For all requests in a procedure or in a profile:

SET ACCESSPDF = {508|OFF}

For a single request:

ON TABLE SET ACCESSPDF {508|OFF}

where:

508

Generates a PDF file compliant with Section 508 accessibility requirements.

OFF

Generates a PDF file that is non-compliant with Section 508 accessibility requirements.
This value is the default.

Example:

Controlling PDF Code for Accessibility

The following request generates accessible PDF report output. The SET and SUBHEAD
commands that enable accessibility appear in boldface.

Creating Reports With TIBCO® WebFOCUS Language

 601

Using Print Display Formats: PDF, PS

TABLE FILE GGSALES
SUM
   DOLLARS/D12M
BY REGION
BY CATEGORY
ON REGION SUBTOTAL AS 'Total for '
HEADING
" "
"Sales Report"
" "
ON TABLE SET ACCESSPDF 508
ON TABLE SET PAGE-NUM OFF
ON TABLE COLUMN-TOTAL AS 'Grand Total'
ON TABLE SUBHEAD "Regional Totals by Category"
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=REPORT, FONT='ARIAL',$
TYPE=TITLE,  COLUMN=N1, FONT='ARIAL', STYLE=BOLD,$
TYPE=TITLE,  COLUMN=N2, FONT='ARIAL', STYLE=BOLD,$
TYPE=TITLE,  COLUMN=N3, FONT='ARIAL', STYLE=BOLD,$
TYPE=HEADING, SIZE=14, STYLE=BOLD,$
TYPE=TABHEADING, SIZE=16, STYLE=BOLD,$
TYPE=SUBTOTAL, BY=1, STYLE=BOLD,$
TYPE=GRANDTOTAL, FONT='ARIAL', STYLE=BOLD,$
ENDSTYLE
END

WebFOCUS generates the following tags when SET ACCESSPDF is set to 508.

Page Heading

Heading tags <H1> and <H2> and are automatically generated by WebFOCUS.

602

9. Choosing a Display Format

Column Titles

Row tags <TR> and header cell tags <TH> are generated by WebFOCUS. The column title is
aligned with the appropriate data columns.

Creating Reports With TIBCO® WebFOCUS Language

 603

Using Print Display Formats: PDF, PS

Data Cells

Row tags <TR> and header cell tags <TH> are generated by WebFOCUS.

604

The output is:

9. Choosing a Display Format

Aligning Elements in a Page Heading With Column Data

The USEASTITLES StyleSheet attribute for PDF reports enables you to place and align custom
column titles (AS='text') in the heading, rather than use the default column titles. The
USEASTITLES attribute associates column titles in the heading with the appropriate data
column.

Syntax:

How to Align Elements in a Page Heading With Column Data

TYPE=HEADING, USEASTITLES=ON, HEADALIGN=BODY,$

Creating Reports With TIBCO® WebFOCUS Language

 605

Using Print Display Formats: PDF, PS

USEASTITLES=ON can only be set for the entire HEADING. HEADALIGN=BODY must also be set
for the HEADING.

To use this attribute in App Studio:

The Report Output Format is PDF.

The Alignment Grid is enabled for the Page Heading.

Add a Page Heading to the report.

Right-click the Page Heading and select Alignment Grid.

On the Insert Alignment Grid dialog box, select the Align with Data option and click OK.

In the Page Heading, right-click the alignment grid and select Align column title (Section
508).

Example:

Aligning Elements in a Page Heading to Column Data

The USEASTITLES attribute that enables the alignment of the heading elements is in bold.
Note that the HEADALIGN=BODY attribute is also in bold.

606

9. Choosing a Display Format

TABLE FILE GGSALES
SUM
   DOLLARS/D12M AS ''
BY REGION AS ''
BY CATEGORY AS ''
ON REGION SUBTOTAL AS 'Total for '
HEADING
" "
"Sales Report"
" <+0> <+0> "
"Region<+0>Category<+0>Dollar Sales"
ON TABLE SET ACCESSPDF 508
ON TABLE SET PAGE-NUM OFF
ON TABLE COLUMN-TOTAL AS 'Grand Total'
ON TABLE SUBHEAD "Regional Totals by Category <+1"
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
$
TYPE=REPORT, FONT='ARIAL',$
TYPE=TITLE, COLUMN=N1, FONT='ARIAL', STYLE=BOLD,$
TYPE=TITLE, COLUMN=N2, FONT='ARIAL', STYLE=BOLD,$
TYPE=TITLE, COLUMN=N3, FONT='ARIAL', STYLE=BOLD,$
TYPE=HEADING, SIZE=14, STYLE=BOLD,
HEADALIGN=BODY, USEASTITLES=ON,$
TYPE=HEADING, LINE=2, OBJECT=TEXT, ITEM=1, COLSPAN=3, JUSTIFY=LEFT,$
TYPE=HEADING, LINE=3, OBJECT=TEXT, ITEM=1, COLSPAN=1, JUSTIFY=LEFT,$
TYPE=HEADING, LINE=3, OBJECT=TEXT, ITEM=2, SIZE=10, COLSPAN=1,
     JUSTIFY=RIGHT,$
TYPE=HEADING, LINE=3, OBJECT=TEXT, ITEM=3, SIZE=10, COLSPAN=1,
     JUSTIFY=RIGHT,$
TYPE=HEADING, LINE=4, OBJECT=TEXT, ITEM=1, SIZE=11, COLSPAN=1,
     JUSTIFY=LEFT,$
TYPE=HEADING, LINE=4, OBJECT=TEXT, ITEM=2, SIZE=11, COLSPAN=1,
     JUSTIFY=LEFT,$
TYPE=HEADING, LINE=4, OBJECT=TEXT, ITEM=3, SIZE=11, COLSPAN=1,
     JUSTIFY=RIGHT,$
TYPE=TABHEADING, SIZE=16, STYLE=BOLD,$
TYPE=SUBTOTAL, BY=1, STYLE=BOLD,$
TYPE=GRANDTOTAL, FONT='ARIAL', STYLE=BOLD,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 607

Using Print Display Formats: PDF, PS

WebFOCUS generates the following tags when the USEASTITLES attribute is used.

Page Heading and Column Titles

Row tags <TR> and header cell tags <TH> are generated by WebFOCUS. Along with the Page
Heading, the column titles are also tagged as header cells <TH>.

608

The output is:

9. Choosing a Display Format

Adding Bookmarks

Bookmarks are links in the navigation pane that enable you to go directly to a destination in
the document. Using bookmarks enables you to jump from the tagged items in the navigation
pane directly to the page where the item is located. The benefit of using bookmarks in
conjunction with a screen reader is that you will be able to navigate a defined hierarchy without
having to listen to the reading of the entire document. For more information about navigating
PDF Bookmarks, see the Adobe documentation on the Adobe Web site, www.adobe.com.

Creating Reports With TIBCO® WebFOCUS Language

 609

Using Print Display Formats: PDF, PS

Note:

Since a PDF document is a complete file, you can use bookmarks and scrolling to navigate
through the file. You can easily navigate through a document, especially documents that
are two or more pages in length.

You can generate bookmarks within WebFOCUS by including the BOOKMARKS and/or TOC
object in the compound layout syntax. Then, in the component definitions, specify the Table
of Contents level and description. You can also optionally specify the BYTOC levels.

For 508 compliance, it is recommended that the Bookmark object be used.

Example:

Adding Bookmarks to the Compound Layout

The BOOKMARK attribute that enables the alignment is in bold. The TOC-LEVEL=1 and
BYTOC=2 attributes for both reports are also in bold. These attributes are explained below:

TOC-LEVEL=n

Defines n as the Table of Contents level for the report layout object. This option defines the
hierarchical order of objects within the Table of Contents.

0 = the object is not shown in the Table of Contents.

1 = the object is shown as a first-level item in the Table of Contents.

2 = the object is shown as a second-level item in the Table of Contents, and so on.

BYTOC=m

Specifies the number of BY fields to be included within the current component entry (m).

The following request adds bookmarks and specifies the main document heading for the
compound report. The report0 component uses the DisplayOn=DOC-HEADING attribute to
indicate that the ON TABLE SUBHEAD string from the report0 component should be tagged as
the main document heading in the PDF output.

610

9. Choosing a Display Format

SET ACCESSPDF = 508
COMPOUND LAYOUT PCHOLD FORMAT PDF
OBJECT=BOOKMARKS,$
SECTION=S1, LAYOUT=ON, MERGE=OFF, ORIENTATION=PORTRAIT,$
PAGELAYOUT=1,$
COMPONENT=report0, position=(1 0.5), Dimension=(* *),
DisplayOn=DOC-HEADING, $
COMPONENT=report1, TEXT='This is the Title for Report 1',
TOC-LEVEL=1,
BYTOC=2,
POSITION=(1 1), DIMENSION=(* *),$
COMPONENT=report2, TEXT='Sales By Region',
TOC-LEVEL=1,
BYTOC=2,
POSITION=(+0.00 +0.519), DIMENSION=(* *), RELATIVE-TO='report1',
REQUIRED-SPACE=(*3.5), RELATIVE-POINT=BOTTOM-LEFT, POSITION-POINT=TOP-LEFT,$
END

SET COMPONENT=report0
TABLE FILE GGSALES
BY CATEGORY NOPRINT
ON TABLE SUBHEAD
" "
"DOLLAR SALES REPORT"
" "
" "
ON TABLE SET PAGE-NUM OFF
ON TABLE HOLD FORMAT PDF
ON TABLE SET STYLE *
TYPE=TABHEADING , SIZE=18, FONT=ARIAL, STYLE=BOLD, JUSTIFY=CENTER,$
ENDSTYLE
END

SET COMPONENT=report1
TABLE FILE GGSALES
SUM DOLLARS/F8M
BY CATEGORY
BY PRODUCT
BY REGION
BY ST
ON CATEGORY PAGE-BREAK
WHERE PRODUCT NE 'Capuccino'
ON CATEGORY SUBTOTAL AS 'Subtotal for: '
HEADING
"Sales by Category"
" "
ON TABLE HOLD FORMAT PDF
ON TABLE SET PAGE-NUM OFF
ON TABLE NOTOTAL
ON TABLE SET STYLE *
TYPE=REPORT, SIZE=10, FONT=ARIAL,$
TYPE=HEADING, SIZE=14, FONT=ARIAL, STYLE=BOLD, JUSTIFY=CENTER,$
TYPE=SUBTOTAL, SIZE=10, STYLE=BOLD,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 611

Using Print Display Formats: PDF, PS

SET COMPONENT=report2
TABLE FILE GGSALES
SUM DOLLARS/F8M
BY REGION
BY ST
BY CATEGORY
BY PRODUCT
ON REGION PAGE-BREAK
WHERE PRODUCT NE 'Capuccino'
ON REGION SUBTOTAL AS 'Subtotal for: '
HEADING
"Sales by Region"
" "
ON TABLE HOLD FORMAT PDF
ON TABLE SET PAGE-NUM OFF
ON TABLE NOTOTAL
ON TABLE SET STYLE *
TYPE=REPORT, SIZE=10, FONT=ARIAL,$
TYPE=HEADING, SIZE=14, FONT=ARIAL, STYLE=BOLD, JUSTIFY=CENTER,$
TYPE=SUBTOTAL, SIZE=10, STYLE=BOLD,$
ENDSTYLE
END
COMPOUND END

The report output, with bookmarks, is shown below.

612

9. Choosing a Display Format

Notice that the hierarchy tree in the Bookmarks pane has two levels for each report and is
determined with the BYTOC attribute. The title for each report in the Bookmarks tree is
determined with the TEXT attribute, as shown in the following image.

The first three pages of the PDF output, with the Tags panel, are shown in the following
images. Note that only the first page of output contains the <H1> heading, DOLLAR SALES
REPORT. The other headings are tagged as <H2>.

Creating Reports With TIBCO® WebFOCUS Language

 613

Using Print Display Formats: PDF, PS

Page 1

614

9. Choosing a Display Format

Page 2

Page 3

Creating Reports With TIBCO® WebFOCUS Language

 615

Using Print Display Formats: PDF, PS

Adding Descriptive Text to an Image

The ALT attribute in a WebFOCUS StyleSheet adds descriptive text to an embedded image in a
PDF report. The ALT attribute in the StyleSheet generates a PDF ALT attribute on the <IMG>
tag.

The ALT tag is displayed in the PDF when you hover the mouse over the image.

Procedure: How to Add Descriptive Text to an Image

ALT='description'

where:

description

Is a brief description of the image, enclosed in single quotation marks (‘). The length can
be a maximum of 256 characters.

For details on the StyleSheet syntax for adding an image, see the Creating Reports With
WebFOCUS Language manual.

Example:

Adding Descriptive Text to an Image

This request adds the Information Builders logo to a report heading. It uses the WebFOCUS
StyleSheet ALT attribute to add descriptive text (Information Builders logo) that identifies the
image.

616

9. Choosing a Display Format

TABLE FILE GGSALES
SUM
   DOLLARS/D12N
BY REGION
BY CATEGORY
ON REGION SUBTOTAL AS 'Total sales: '
ON REGION PAGE-BREAK
HEADING
"Sales Report"
" "
" "
ON TABLE SET ACCESSPDF 508
ON TABLE SET PAGE-NUM OFF
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT PDF
ON TABLE SUBHEAD "Regional Totals by Category"
ON TABLE SET STYLE *
     UNITS=IN,
     SQUEEZE=ON,
     ORIENTATION=PORTRAIT,
$
TYPE=REPORT, GRID=OFF, FONT='ARIAL', SIZE=9,$
TYPE=TITLE, STYLE=BOLD,$
TYPE=HEADING, SIZE=12, STYLE=BOLD, JUSTIFY=CENTER,$
TYPE=TABHEADING, SIZE=14, STYLE=BOLD, JUSTIFY=CENTER,$
TYPE=SUBTOTAL, BACKCOLOR=RGB(210 210 210), STYLE=BOLD,$
TYPE=REPORT, IMAGE=smplogo1.gif, ALT='Information Builders logo',
POSITION=(1.19 .9), SIZE=(.8 .2),$
ENDSTYLE
END

The report is:

When the request is run, hovering the mouse over the image displays the descriptive text. This
text is read by accessibility tools, such as JAWS.

Creating Reports With TIBCO® WebFOCUS Language

 617

Using Print Display Formats: PDF, PS

Describing Drill Down Information

When ACCESSPDF is enabled, the developer can provide a description of the Drill Down using
the ALT attribute in a WebFOCUS StyleSheet. In the PDF report, JAWS will read the value of the
Drill Down component along with the ALT text.

Including a description of the detail component of a Drill Down report supports accessibility.

Syntax:

How to Add Descriptive Drill Down Information

ALT='description'

where:

description

Is the description of the Drill Down information in a report, enclosed in single quotation
marks (‘). The length can be a maximum of 256 characters.

For details on the StyleSheet syntax for Drill Down reports, see the Creating Reports With
WebFOCUS Language manual.

TABLE FILE GGSALES
SUM
   DOLLARS/D12N
BY REGION
BY CATEGORY
ON REGION SUBTOTAL AS 'Total sales: '
HEADING
" "
ON TABLE SET ACCESSPDF 508
ON TABLE SET PAGE-NUM OFF
ON TABLE NOTOTAL
ON TABLE SUBHEAD "Sales Report"
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET STYLE *
     UNITS=IN,
     SQUEEZE=ON,
     ORIENTATION=PORTRAIT,
     SUMMARY='508 Sales report example',
     TITLETEXT='508 Sales report example',
$
TYPE=REPORT, GRID=OFF, FONT='ARIAL', SIZE=9,$
TYPE=DATA, COLUMN=N2,
ALT='Drill Down to detail report.', \
     FOCEXEC=508drill01detail( REGION=N1 CATEGORY=N2 ),$
TYPE=TITLE, STYLE=BOLD,$
TYPE=TABHEADING, SIZE=12, STYLE=BOLD, JUSTIFY=CENTER,$
TYPE=HEADING, SIZE=12, STYLE=BOLD, JUSTIFY=CENTER,$
TYPE=SUBTOTAL, BACKCOLOR=RGB(210 210 210), STYLE=BOLD,$
ENDSTYLE
END

618

Note the ALT attribute and associated text in BOLD.

The report is:

9. Choosing a Display Format

When you hover the mouse over Coffee for the Midwest region, the URL information for the
Drill Down appears in the box. Screen readers, such as JAWS, will not read hover text. With
ACCESSPDF enabled, the ALT text or 'Drill Down to detail report' is appended to the value for
the Drill Down or 'Coffee' in this example. When you navigate to Coffee, the screen reader will
respond with Coffee Drill Down to detail report.

Creating Reports With TIBCO® WebFOCUS Language

 619

Using Print Display Formats: PDF, PS

Note:

Users that use screen readers, such as JAWS, may need more information regarding the
Drill Down link. In the above example, notice that there are multiple hyperlinks for the value
Coffee. This functionality, along with the 'read current cell' command, allows the user to
understand the difference in those values. The screen reader command to 'read current
cell' in JAWS is the Ctrl+Alt+Num5 shortcut. In this example, JAWS would respond to the
'read current cell' command with column two, row two, region Midwest, link Coffee Drill
Down to detail report.

If you are opening the output in Adobe Reader, make sure you specify the FOCEXURL
setting to provide the URL context of the WebFOCUS environment the Drill Down is to call
back to. In addition, the FOCEXURL value has to have the parameter to specify that the
request is a Drill Down request. For example:

-SET &FOCEXURL='http://host:port/ibi_apps/WFServlet?IBIF_webapp=
   /ibi_apps' | '&';
-SET &FOCEXURL=&FOCEXURL | 'IBIMR_drill=IBFS,RUNFEX,IBIF_ex,true' | '&';
-SET &FOCEXURL=&FOCEXURL | 'IBIC_server=EDASERVE' | '&';
-SET &FOCEXURL=&FOCEXURL | 'IBIAPP_app=ibisamp' | '&';
SET FOCEXURL='&FOCEXURL'

Accessibility Limitations

Reports using the following elements are not accessible:

If a procedure does not contain the SET PAGE-NUM=OFF or ON TABLE SET PAGE-NUM OFF
command, the page number will be announced two times by the screen reader.

ACROSS and OVER reports.

Financial Modeling Language (FML).

FOLD-LINE. Accessibility is disabled when FOLD-LINE is used in a report.

Fixed monetary edit options (N, !d, !e, !l and !y) including the Credit Negative (CR). A
unique cell is created for the noted monetary options or CR option.

Text included or designed in FOOTING, SUBHEAD, SUBFOOT, RECAP, SUMMARIZE, and
RECOMPUTE commands do not generate row header tags.

Using PostScript (PS) Display Format

You can display a report as a PostScript document. PostScript (format PS) is a print-oriented
page description language. As a display format, it may be helpful if you wish to see the report
output on your monitor before printing it using PostScript.

620

9. Choosing a Display Format

To display a PostScript report, a computer must have a third-party PostScript application
installed, such as GSview (a graphical interface for Ghostscript).

If you are sending a PS report to a printer from WebFOCUS or from ReportCaster, you can
select the size of the paper on which to print the output. The PostScript code that is generated
works on PS printers that support Language Level 2 or above. It is ignored, without harmful
effects, on Level 1 printers. For details, see How to Select Paper Size in a PostScript (PS)
Report on page 621. This capability is only supported for the PostScript format.

Other print-oriented display formats. You can also display a report as a PDF document. For
more information, see Using PDF Display Format on page 585.

Procedure: How to Select Paper Size in a PostScript (PS) Report

PAGESIZE and ORIENTATION are two WebFOCUS StyleSheet options that are used to display a
report. You can enable these features in printed documents using the SET parameter
PSPAGESETUP. You can then select the size of the paper on which to print a PostScript report
by selecting a PAGESIZE option.

Complete these steps:

1. Place the following SET parameter before or within your request

SET PSPAGESETUP= ON

or

ON TABLE SET PSPAGESETUP ON

OFF is the default setting.

2.

Include your PAGESIZE specification in a SET command or StyleSheet declaration in the
request

SET PAGESIZE= option

or

ON TABLE SET PAGESIZE option

or

PAGESIZE=option, $

where:

option

Can be any paper size supported for your printer. LETTER is the default setting.

Creating Reports With TIBCO® WebFOCUS Language

 621

Using Print Display Formats: PDF, PS

Note: If you send a job to a printer that does not have the requested paper size loaded, the
printer may stop and instruct its operator to load the specified paper. To ensure control over
your printing, it is best to set paper size in individual requests (rather than as an installation-
wide default) so that you can load paper as required.

Example:

Selecting Paper Size Using SET Command in a PostScript Report

This example automatically prints a document on legal paper as specified in the two SET
commands that precede the report request. The referenced printer is a PostScript Level 2 or
higher printer, which will automatically select legal paper and print the document in landscape
mode.

SET PSPAGESETUP=ON
SET PAGESIZE=LEGAL
SET ORIENTATION=LANDSCAPE
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
ON TABLE HOLD FORMAT PS
END

-RUN
DOS COPY HOLD.PS \\IBIPRINTA\28C2

Selecting Paper Size Using a SET Command and a StyleSheet

This request automatically prints a document on legal paper based on the paper size and
orientation specifications in the StyleSheet declaration. The referenced printer is a PostScript
Level 2 or higher printer, which will automatically select legal paper and print the document in
landscape mode.

622

9. Choosing a Display Format

SET PSPAGESETUP=ON
TABLE FILE CAR
SUM RC DC SALES BY COUNTRY BY CAR BY MODEL
ON TABLE HOLD FORMAT PS
ON TABLE SET STYLE *
UNITS=IN,
     PAGESIZE='Legal',
     LEFTMARGIN=1.000000,
     RIGHTMARGIN=0.500000,
     TOPMARGIN=1.500000,
     BOTTOMMARGIN=0.500000,
     SQUEEZE=ON,
     ORIENTATION=LANDSCAPE,$
GRAPHTYPE=DATA, COLUMN=RC, GRAPHPATTERN=EMPTY, $
GRAPHTYPE=DATA, COLUMN=DC, GRAPHPATTERN=SLANT, $
GRAPHTYPE=DATA, COLUMN=SALES,
GRAPHPATTERN=HORIZONTAL, $
ENDSTYLE
END
-RUN
DOS COPY HOLD.PS \\IBIPRINTA\28C2

WebFOCUS Font Support

You can add and configure PostScript Type 1 fonts to significantly expand your options for
displaying and printing PS and PDF reports, beyond those provided by the basic set of fonts
distributed with Adobe Reader. Thousands of PostScript fonts are available to make your
reports more stylish and useful, including some that support symbols and bar codes.

The font map files for Type 1 fonts are stored as XML files (fontmap.xml and fontuser.xml). All
font mappings in these files are used for both PDF and PostScript report output.

The font definitions for DHTML also cover PowerPoint (PPT and PPTX). For XLSX, you can define
a new default font in the fontuser.xml file. This allows ease in customizing the look and feel of
XLSX workbooks. WebFOCUS uses Arial as the default font. However, you can change the
default font to match the Microsoft Office standard font, Calibri, or your corporate standard.

You can also add and configure a set of TrueType or OpenType fonts to be embedded in PDF
output files.

Note: You can use OpenType font files (OTF) only with content in Compact Font Format (CFF).

Reference: Support for the Symbol Font

To use the Symbol font, specify font=symbol in your WebFOCUS StyleSheet:

Some versions of Firefox 3 do not support the Symbol font and will substitute it with
another font. For information about Firefox support for the Symbol font, refer to Firefox
sources.

Creating Reports With TIBCO® WebFOCUS Language

 623

Using Print Display Formats: PDF, PS

The Euro character displays in PDF output because the Adobe Symbol character set
includes the Euro character.

The Euro character does not display in DHTML, PPT, and PPTX report output because the
Windows Symbol character set does not include the Euro character.

The following style options can be rendered with the Symbol font:

DHTML, PPT, and PPTX support style=normal, bold, italic, and bold+italic.

PDF supports only style=normal. Any other style specified in the StyleSheet will be
mapped to normal.

How WebFOCUS Uses Type 1 Fonts

WebFOCUS generates a PDF or PS document from scratch. In order to do that, it must
physically embed all the objects it displays or prints, including images and fonts, in the
document itself.

When you execute a report and specify one of these formats as your display format, the
WebFOCUS Reporting Server retrieves the data and begins to format the report. Fonts and
images specified in the StyleSheet must be available to the Reporting Server to create the
output file. It reads the font information from the font files and embeds that information into
the document. The font itself is stored on the Reporting Server.

To ensure that the Reporting Server can locate the required information, you must define and
map it in the following files:

Font file, usually a PFB (Printer Font Binary) file. This file contains the information about
the shape to draw for each character of the font. The information in the font file is scalable,
which means that a single font file can be used to generate characters of any size. Note,
however, that bold and italic variations of the typeface are separate fonts. An alternative
ASCII format, PFA, can also be used by WebFOCUS. In addition to PFB and PFA font files,
you can use OTF font files to enable more flexibility in customizing PDF files, such as
support for expanded character sets and layout features, and cross-platform compatibility.

Adobe Font Metrics (AFM) file. This file is distributed with all Adobe fonts. It contains
information about the size of each character in each font. WebFOCUS uses this information
to lay out the report on the page. Note that the three built-in fonts also have AFM files,
which are distributed with WebFOCUS. However, these fonts do not require font files, since
the fonts are built in to Adobe Reader.

Note: A Printer Font Metrics (PFM) file is also available. This file is used by applications
such as Adobe Reader for laying out text, however it is not supported by WebFOCUS. You
must use the AFM file.

624

9. Choosing a Display Format

WebFOCUS Font Map files. These configuration files map the name of a font to the
appropriate font metrics and font files (AFM, PFB (or PFA), or OTF). The mapping determines
which actual font is used when you specify a font using the FONT attribute in a WebFOCUS
StyleSheet. For example, if your StyleSheet contains the following declaration, WebFOCUS
will search the font map for a font mapping with a matching name and style, and use the
font specified by the mapping:

TYPE=REPORT, FONT=HELVETICA, STYLE=ITALIC, $

There are two files WebFOCUS uses for mapping fonts, both in an XML-based format:

The default font map file, fontmap.xml, contains the font definitions for all output formats
that are supported with WebFOCUS, as originally installed. Users should not modify this
file.

The user font map file, fontuser.xml, contains font definitions added by the user. The
following sections describe how to add your fonts to this file.

The user font map is searched before the default font map, so font definitions in the user map
will override definitions of the same font in the default map.

You can also use a variety of utilities to convert Windows True Type fonts (such as Arial and
Tahoma) into Type 1 fonts. Verify that you are licensed for this type of font use. Then, after you
convert them, you can define and map these fonts for use by WebFOCUS.

One such utility is TTF2PT1.

For information about the Windows version, go to:

http://gnuwin32.sourceforge.net/packages/ttf2pt1.htm

For information about UNIX versions, go to: http://ttf2pt1.sourceforge.net/download.html

Adding PostScript Type 1 Fonts for PS and PDF Formats

This section describes how to add PostScript type 1 fonts to the fontuser.xml file.

Procedure: How to Configure Type 1 PostScript Fonts on the Windows and UNIX Platforms

Locate the necessary font files (AFM, PFB (or PFA), or OTF). These files should be available in
the location where the fonts were originally installed. You will be copying these files to a
location from which they can be accessed by the WebFOCUS Reporting Server.

Creating Reports With TIBCO® WebFOCUS Language

 625

Using Print Display Formats: PDF, PS

Tip:

You may need to run an installer program to install these in a directory on your Windows or
UNIX machine. Note that the fonts do not have to be installed on a client machine in order
to be used, since they will be embedded in the PDF or PostScript files created by
WebFOCUS. PDF files with these embedded fonts can be displayed on any machine that
has Adobe Reader (or a similar PDF viewer), and PostScript files with these embedded
fonts can be printed on any PostScript printer (or displayed in a PostScript viewer such as
GhostView).

Note that PFB files are binary, so if they are FTPed from another machine, they must be
FTPed in BINARY mode.

The maximum number of embedded fonts supported in a PDF report is 63.

After you have located the font files you wish to add, you can set up WebFOCUS to use one or
more Type 1 fonts.

1.

For each font you wish to add, copy the AFM, PFB (or PFA), and OTF files into the etc
subdirectory of your WebFOCUS configuration directory. On a Windows machine, the
location is usually:

drive:\ibi\srv82\wfs\etc

where:

wfs

Is your WebFOCUS configuration directory (it may have a different name depending on
installation options, but should always be a directory directly under drive:\ibi\srv82).
Note that home is the other directory directly under drive:\ibi\srv82.

Under Unix, the location is /ibi/srv82/wfs/etc, assuming that the WebFOCUS server
was installed in /ibi/srv82.

Keeping user font files in this directory allows user font files to remain separate from
the default font files (under \ibi\srv82\home) so they can be easily preserved if
WebFOCUS is updated to a new release.

After you copy these files, you can rename them to any descriptive name.

2. The user font map file, fontuser.xml, is created by the installer in the same directory. Using

a text editor, add your font definitions to this file using the syntax described in the
following section, How to Add Fonts to the Font Map on page 628.

626

Procedure: How to Configure Type 1 PostScript Fonts on z/OS Under PDS Deployment

9. Choosing a Display Format

After you have located the font files you wish to add, you can configure WebFOCUS to use one
or more Type 1 fonts.

1. Copy the AFM (font metrics) file into the PDS allocated to DDNAME EDACCFG in the

Reporting Server JCL. You can copy this file from another machine using FTP in standard
ASCII (text) mode. The member name of the AFM file in this PDS will match the metricsfile
value in the font map file.

Note: If the Windows font file names contain underscore characters or are longer than
eight characters, you must rename them, since these are not valid for z/OS member
names.

2. You can use either PFB (binary) fonts or PFA (ASCII) fonts:

If you are using PFB (binary) fonts, create a partitioned data set, put the PFB file in it
(for example, using FTP in BINARY mode), and concatenate this data set to the data
set already allocated to DDNAME EDAHBIN in the WebFOCUS Reporting Server JCL.

This PDS should be created with the following DCB attributes:

RECFM: VB    LRECL: 1028    BLKSIZE: 27998

The member name in this PDS should match the fontfile name in the font map file.

If you copy the PFB font file into the PDS using FTP, you must use BINARY mode. The
member name of the PFB file in this PDS will match the fontfile value in the font map
file.

If you are using PFA (ASCII) font files, create a PDS (separate from the one you use for
PFB fonts), put the PFA file in it (for example, using FTP in regular, ASCII mode), and
concatenate this data set to the data set already allocated to DDNAME EDAHETC in
the Reporting Server JCL. This PDS should be created with the following DCB
attributes:

RECFM: VB    LRECL: 2044    BLKSIZE: 27998

The member name in this PDS should match the fontfile value in the font map file.
Note that you can use PFB and PFA files simultaneously. The fonttype attribute in the
font map file (PFB or PFA) tells WebFOCUS which PDS to search for the specified
member name.

3. The user font map file is in member FONTUSER in the data set allocated to DDNAME
EDACCFG. Using a text editor, add your font definition to the user font map using the
syntax described in How to Add Fonts to the Font Map on page 628.

Creating Reports With TIBCO® WebFOCUS Language

 627

Using Print Display Formats: PDF, PS

Syntax:

How to Add Fonts to the Font Map

The Type 1 PostScript fonts used with the PostScript and PDF output formats use separate
font files for each variant of the font: normal, bold, italic, and bold-italic. This grouping of
related fonts is called a font family.

The XML font map syntax uses two XML tags, <family> and <font>, to represent this structure.
The example uses the family name Garamond. For example:

<family name="garamond">
  <font style="normal"
        metricsfile="gdrg" fontfile="gdrg" fonttype="PFB" />
  <font style="bold"
        metricsfile="gdb"  fontfile="gdb" fonttype="PFB" />
  <font style="italic"
        metricsfile="gdi"  fontfile="gdi" fonttype="PFB" />
  <font style="bold+italic"
        metricsfile="gdbi" fontfile="gdbi" fonttype="PFB" />
</family>

The following example uses the family name otf. For example:

<family name="otf">
  <font style="normal"
        metricsfile="otfn"  fontfile="otfn" fonttype="OTF" />
  <font style="bold"
        metricsfile="otfb"  fontfile="otfb" fonttype="OTF" />
  <font style="italic"
        metricsfile="otfi"  fontfile="otfi" fonttype="OTF" />
  <font style="bold+italic"
        metricsfile="otfbi" fontfile="otfbi" fonttype="OTF" />
</family>

The basics of the XML syntax are:

Tag names (such as family and font) and attribute names (such as style or metricsfile) must
be in lowercase. Attribute values, such as font file names, are case-insensitive.

Attribute values, which is the text after the equal sign (=), must be in double quotation
marks (for example, "bold")

Elements that have no explicit end-tag must end with />. (For example, the family tag has
the closing tag </family>, but the font tag has no closing tag, so it ends with />.)

Comments are enclosed in special delimiters:

<!-- This is a comment -->

Line breaks may be placed between attribute-value pairs.

A more complete description of XML syntax can be found here:

628

9. Choosing a Display Format

http://en.wikipedia.org/wiki/Xml

The family element

The family element specifies the name of a font family. This family name, specified in the
name attribute of the family element, is the name by which the font will be referenced in a
StyleSheet. It corresponds to the value of the FONT attribute in the StyleSheet. The end-tag </
family> closes the family element, and any number of additional family elements may follow.

Font family names should be composed of letters (A-Z, a-z), digits, and limited special
characters, such as a minus sign (-), underscore (_), and blank. Font family names should have
a maximum length of 40 characters. Since the font name is only a reference to a mapping in
the font map, it does not need to be related to the actual name of the font (which WebFOCUS
obtains from the mapped AFM file) or the file name of the font.

Font elements

Nested within each family element are one or more font elements that specify the font files for
each font in the family. For example, there may be one font element for the font Garamond
Regular (normal), one for Garamond Italic (italic). Since a font element has no child elements,
it is closed with "/>".

The actual name of the font as used in the PDF or PostScript document is taken from the font
metric file.

Fonts defined in the user font file (fontuser.xml) can override default font definitions in
fontmap.xml. Thus, you should be careful to choose family names that do not conflict with
existing definitions, unless you actually wish to override these definitions (which should
generally not be done).

Each font element contains the following attributes:

style: This attribute specifies the style of the font and corresponds to the STYLE attribute
in the StyleSheet. The allowed values are "normal", "bold", "italic", and "bold+italic". For
example, the font defined in the following bold italic font element:

<font style="bold+italic" metricsfile="gdbi" fontfile="gdbi"
fonttype="PFB" />

could be referenced in the StyleSheet like this:

TYPE=REPORT, FONT=GARAMOND, STYLE=BOLD+ITALIC, $

Although most fonts have a font file for each of the four styles, some specialized fonts
such as bar code fonts might only have a single style (usually "normal"). Only the styles
that exist for a particular font need to be specified in the font map file.

Creating Reports With TIBCO® WebFOCUS Language

 629

Using Print Display Formats: PDF, PS

The actual names of the fonts may vary. Some fonts may be called "oblique" rather than
"italic", or "heavy" rather than "bold". However, the font map and StyleSheet always use
the keywords "normal", "bold", "italic" and "bold+italic".

metricsfile: This attribute specifies the name of the Adobe Font Metrics (AFM) file that
provides the measurements of the font. You should only use the base name of the file (for
example, "gdrg", not "gdrg.afm"). On Windows and UNIX systems, the file is assumed to
have the extension .afm and reside in the wfs/etc directory. On z/OS with PDS deployment,
the name refers to a member in the PDS allocated to EDACCFG. For information about file
locations, see How to Configure Type 1 PostScript Fonts on the Windows and UNIX Platforms
on page 625 orHow to Configure Type 1 PostScript Fonts on z/OS Under PDS Deployment on
page 627.

File names should be composed of letters and numbers, and should not contain blanks. On
Windows and UNIX systems, the file names may also contain underscore characters. On
UNIX systems, the file names should not contain uppercase letters. Since the files must be
located in specific directories, no directory paths or drive letters are allowed.

fonttype: This attribute specifies the type of the font file. The allowed values are "PFA",
"PFB", or "OTF".

fontfile: This attribute specifies the name of the PFB or PFA file that contains the font itself.
As with metricsfile, the value specifies only the base file name (the fonttype attribute
specifies the type). On Windows and UNIX, the file is assumed to have the extension .pfb
for binary (PFB) font files or .pfa for ASCII (PFA) font files, and should reside in the same
directory as the AFM files (wfs/etc). On z/OS with PDS deployment, the name refers to a
member in the appropriate PDS.

Additional items of XML syntax include the XML header on the first line of the file and the
<fontmap> and <when> elements that enclose all of the family elements. The <when> tag
allows the same font mappings to be used for both PDF and PostScript reports across output
formats. These can include PDF, PS, and DHTML. PPT and PPTX formats will use fonts
specified for DHTML. If no <when> is specified, the font will be available for all formats.

630

9. Choosing a Display Format

The following is a complete example of a user font map:

<?xml version="1.0" encoding="UTF-8" ?>
<!-- Example of a user font map file with two font families. -->
<fontmap version="1">
    <when format="PDF PS">
        <family name="garamond">
            <font style="normal"
                  metricsfile="gdrg" fontfile="gdrg" fonttype="PFB" />
            <font style="bold"
                  metricsfile="gdb"  fontfile="gdb"  fonttype="PFB" />
            <font style="italic"
                  metricsfile="gdi"  fontfile="gdi"  fonttype="PFB" />
            <font style="bold+italic"
                  metricsfile="gdbi" fontfile="gdbi" fonttype="PFB" />
        </family>
        <!-- This font only has a "normal" style, others omitted. -->
        <family name="ocra">
            <font style="normal"
                  metricsfile="ocra" fontfile="ocra" fonttype="PFB" />
        </family>
    </when>
</fontmap>

Example: WebFOCUS StyleSheet Declaration

Once the font map files have been set up, the newly mapped fonts can be used in a
WebFOCUS StyleSheet. For example, to use the Garamond fonts:

ON TABLE SET STYLE *
type=report, font=garamond, size=12, $
type=title, font=garamond, style=bold, color=blue, $
ENDSTYLE

Since the style attribute has been omitted for the report font in the StyleSheet, it defaults to
normal. Attributes such as size and color can also be applied.

Reference: Editing the Font Map File

There is a byte order mark (BOM) at the beginning of the user font map file (fontuser.xml),
which must be preserved for this file to be read correctly.

If you are using a Unicode-aware editor, such as Notepad on Windows, to edit the file, the BOM
will not be visible, but you can preserve it by making sure that you select an encoding of UTF-8
in the Save-As dialog. In most other editors, such as vi on UNIX or the ISPF editor under z/OS,
the BOM will display as three or four strange-looking characters at the beginning of the file. As
long as you do not delete or modify these characters, the BOM will be preserved.

Creating Reports With TIBCO® WebFOCUS Language

 631

Using Print Display Formats: PDF, PS

Reference: The WebFOCUS Default Font Map

Since the user font map is searched before the WebFOCUS default font map, font definitions in
the user font map file will override mappings of the same font in the default font map file.
Since you usually would not want to override existing font mappings, you can check which font
names are already used by WebFOCUS by examining the default font map file.

On Windows platforms, it can be found in

drive:\ibi\srv77\home\etc\style\fontmap.xml

On UNIX, it can be found in a similarly named directory.

On z/OS with PDS deployment, the default font map file is in the FONTMAP member of the
prefix.P.HOME.ERR partitioned data set. Unlike the user font map file, this file has separate
sections containing definitions for PS, PDF, and DHTML formats.

Note: The DHTML mappings are used for the DHTML and PowerPoint output formats, which do
not support user-added fonts.

Since the font mappings in the default font map file are for fonts that are already assumed to
exist on the user machines (for example, built-in Adobe Reader fonts, standard PostScript
printer fonts, or standard Windows fonts), they do not reference font files, only font metrics
files. Fonts provided by the user should reference both font files and metrics files.

AFM files for the default fonts can be found in drive:\ibi\srv77\home\etc\style (or members of
prefix.P.HOME.ERR with z/OS under PDS deployment).

Procedure: How to Define a Default Font in the Font Map

An individual default font can be set for each output type and/or language setting within an
output type. This setting should be defined in the fontuser.xml file rather than the fontmap.xml
file. Fontmap.xml may be updated by a future release installation, so customizations may be
lost. Additionally, the settings in fontuser.xml override settings in fontmap.xml.

Note:

Fontmap.xml can be found in ..\ibi\srvXX\home\etc\style, where XX is your server release.

Fontuser.xml can be found in ..\ibi\srvXX\wfs\etc, where XX is your server release.

To designate the default font use the following steps:

1. Copy the selected font entry from frontmap.xml to fontuser xml.

a. Within fontmap.xml, find the entry for the font family within the desired output format

to be designated as the default.

632

9. Choosing a Display Format

b. Copy the entire entry into the appropriate format area within fontuser.xml.

2.

In fontuser.xml, within the entry for the font to be designated as the default font and style,
add the following attribute:

default="yes"

For example, the following code defines the default fonts to be Helvetica bold for PDF,
Calibri for XLSX, and Arial Italic for DHTML:

<fontmap version="1">
<when format="PDF PS">
  <family name="Helvetica" htmlfont="Arial">
     <font style="normal" metricsfile="pdhelv"   />
     <font style="bold"   metricsfile="pdhelvb"  default="yes"  />
     <font style="italic"  metricsfile="pdhelvi"  />
     <font style="bold+italic" metricsfile="pdhelvbi" />
  </family>
</when>
<when format="XLSX">
  <family name="Calibri" htmlfont="Calibri">
     <font style="normal"      metricsfile="ttcali"  default="yes" />
     <font style="bold"        metricsfile="ttcalib"  />
     <font style="italic"      metricsfile="ttcalii"  />
     <font style="bold+italic" metricsfile="ttcalibi" />
  </family>
</when>
<when format="DHTML">
  <family name="Arial">
     <font style="normal"  metricsfile="ttarial"  />
     <font style="bold"    metricsfile="ttarialb" />
     <font style="italic"  metricsfile="ttariali" default="yes"  />
     <font style="bold+italic" metricsfile="ttariabi" />
  </family>
</when>
</fontmap>

If multiple fonts in a font map family, such as PDF, have the default="yes" attribute, the
last font with that attribute becomes the default font. Fonts in fontuser.xml are processed
after those in fontmap.xml, so a default font set in fontuser.xml can override the one set
in fontmap.xml.

A default font set in the PDF section of the font map does not affect a default in the
DHTML section, and a default for one specific language does not override the default for
other languages.

Creating Reports With TIBCO® WebFOCUS Language

 633

Using Print Display Formats: PDF, PS

Embedding TrueType Fonts Into WebFOCUS PDF Reports Generated in Windows

You can have WebFOCUS embed the following TrueType fonts into PDF output files generated
in Windows:

Arial Unicode MS

Courier New

Lucida Sans Unicode

Tahoma

Times New Roman

Trebuchet MS

Note:

Custom TrueType font embedding is supported, as long as you provide the AFM and TTF
files. Only TTF fonts that have format 4 layer with platform ID 3 and platform specific ID 1
are supported.

The addition of the font file and font type attributes activates the embedding feature. To
use any of these fonts and font styles without embedding, do not add the font file and font
style attributes into the font map definition for each individual style.

Procedure: How to Add TrueType Fonts for Embedding Into PDF Output Files

1. Make the fonts available to the Reporting Server by copying the TrueType font files from

the Windows font directory (C:\Windows\fonts) to the WebFOCUS server configuration
directory:

drive:\ibi\srv82\wfs\etc

where:

drive

Is the drive on which the Reporting Server is installed.

wfs

Is your WebFOCUS configuration directory (it may have a different name depending on
installation options, but should always be a directory directly under drive:\ibi\srv82).
Note that home is the other directory directly under drive:\ibi\srv82.

634

For each of the supported fonts, you will need to copy the following font files. You will also
need to know the metrics file name associated with each font file:

9. Choosing a Display Format

Arial Unicode MS

Style

Normal

Bold

Italic

Metrics File Name

Font File Name

pdarum.afm

arialuni.ttf

pdarumb.afm

arialuni.ttf

pdarumi.afm

arialuni.ttf

Bold Italic

pdarumbi.afm

arialuni.ttf

Courier New

Style

Normal

Bold

Italic

Metrics File Name

Font File Name

pdconu.afm

cour.ttf

pdconub.afm

courbd.ttf

pdconui.afm

couri.ttf

Bold Italic

pdconubi.afm

courbi.ttf

Lucida Sans Unicode

Style

Normal

Bold

Italic

Metrics File Name

Font File Name

pdlusu.afm

l_10646.ttf

pdlusub.afm

l_10646.ttf

pdlusui.afm

l_10646.ttf

Bold Italic

pdlusubi.afm

l_10646.ttf

Creating Reports With TIBCO® WebFOCUS Language

 635

Using Print Display Formats: PDF, PS

Tahoma

Style

Normal

Bold

Italic

Metrics File Name

Font File Name

pdtaho.afm

tahoma.ttf

pdtahob.afm

tahomabd.ttf

pdtahoi.afm

tahoma.ttf

Bold italic

pdtahobi.afm

tahomabd.ttf

Times New Roman

Style

Normal

Bold

Italic

Metrics File Name

Font File Name

pdtimu.afm

times.ttf

pdtimub.afm

timesbd.ttf

pdtimui.afm

timesi.ttf

Bold Italic

pdtimubi.afm

timesbi.ttf

Trebuchet MS

Style

Normal

Bold

Italic

Metrics File Name

Font File Name

pdtrbu.afm

trebuc.ttf

pdtrbub.afm

trebucbd.ttf

pdtrbui.afm

trebucit.ttf

Bold Italic

pdtrbubi.afm

trebucbi.ttf

2. Add the fonts to the user font map file, fontuser.xml. This file is also located in the

Reporting Server configuration directory drive:\ibi\srv82\wfs\etc.

The fontuser.xml file has a sample family tag. Copy the sample family tag between <when
format="PDF PS"> and </when>, then edit it for the font you are adding. For more
information on editing font map syntax, see How to Add Fonts to the Font Map on page
628.

636

9. Choosing a Display Format

The following shows a user font map file with the Arial Unicode MS font added:

<?xml version="1.0" encoding="UTF-8" ?>
<!-- Example of a user font map file defining Arial Unicode MS true
type fonts -->
<fontmap version="1">
<when format="PDF">
    <family name = "Arial Unicode MS">
       <font style="normal" metricsfile="pdarum"
          fontfile="arialuni" fonttype="TTF" />
       <font style="bold" metricsfile="pdarumb"
          fontfile="arialuni" fonttype="TTF" />
       <font style="bold+italic" metricsfile="pdarumbi"
          fontfile="arialuni" fonttype="TTF" />
       <font style="italic" metricsfile="pdarumi"
          fontfile="arialuni" fonttype="TTF" />
   </family>
 </when>
</fontmap>

Note that the font file name does not include the extension. The extension, TTF, is entered
as the fonttype attribute.

3.

In a report request, specify the font family names and the style attributes in the
stylesheet, and hold the report output in PDF format.

An example follows of the contents of a fontuser.xml file with all of the supported embedded
fonts defined. You can select only the ones you need for your environment:

<fontmap version="1">
  <when format="PDF PS">

<family name = "Arial Unicode MS">
    <font style="normal"
          metricsfile="pdarum"   fontfile="arialuni" fonttype="TTF" />
    <font style="bold"
          metricsfile="pdarumb"  fontfile="arialuni" fonttype="TTF" />
    <font style="bold+italic"
          metricsfile="pdarumbi" fontfile="arialuni" fonttype="TTF" />
    <font style="italic"
          metricsfile="pdarumi"  fontfile="arialuni" fonttype="TTF" />
  </family>

<family name="Trebuchet MS">
    <font style="normal"
          metricsfile="pdtrbu"   fontfile="trebuc"   fonttype="TTF" />
    <font style="bold"
          metricsfile="pdtrbub"  fontfile="trebucbd"  fonttype="TTF" />
    <font style="italic"
          metricsfile="pdtrbui"  fontfile="trebucit"  fonttype="TTF" />
    <font style="bold+italic"
          metricsfile="pdtrbubi" fontfile="trebucbi" fonttype="TTF" />
  </family>

Creating Reports With TIBCO® WebFOCUS Language

 637

Using Print Display Formats: PDF, PS

<family name="Times New Roman">
    <font style="normal"
          metricsfile="pdtimu"   fontfile="times"   fonttype="TTF" />
    <font style="bold"
          metricsfile="pdtimub"  fontfile="timesbd" fonttype="TTF" />
    <font style="italic"
          metricsfile="pdtimui"  fontfile="timesi"  fonttype="TTF" />
    <font style="bold+italic"
          metricsfile="pdtimubi" fontfile="timesbi" fonttype="TTF" />
  </family>

<family name="Lucida Sans Unicode">
    <font style="normal"
          metricsfile="pdlusu"   fontfile="L_10646"   fonttype="TTF" />
    <font style="bold"
          metricsfile="pdlusub"  fontfile="L_10646"  fonttype="TTF" />
    <font style="italic"
          metricsfile="pdlusui"  fontfile="L_10646"  fonttype="TTF" />
    <font style="bold+italic"
          metricsfile="pdlusubi" fontfile="L_10646"  fonttype="TTF" />
  </family>

<family name = "Courier New">
    <font style="normal"
          metricsfile="pdconu"   fontfile="cour" fonttype="TTF" />
    <font style="bold"
          metricsfile="pdconub"  fontfile="courbd" fonttype="TTF" />
    <font style="bold+italic"
          metricsfile="pdconubi" fontfile="courbi" fonttype="TTF" />
    <font style="italic"
          metricsfile="pdconui"  fontfile="couri" fonttype="TTF" />
  </family>

<family name = "Tahoma">
    <font style="normal"
          metricsfile="pdtaho" fontfile="tahoma" fonttype="TTF" />
    <font style="bold"
          metricsfile="pdtahob" fontfile="tahomabd" fonttype="TTF" />
    <font style="bold+italic"
          metricsfile="pdtahobi" fontfile="tahomabd" fonttype="TTF" />
    <font style="italic"
          metricsfile="pdtahoi" fontfile="tahoma" fonttype="TTF" />
  </family>
  </when>
</fontmap>

638

9. Choosing a Display Format

Example:

Embedding TrueType Fonts in a PDF Output File

The font files trebuc.ttf, trebudbd.ttf, trebucit.ttf, trebucbi.ttf, tahoma.ttf, and tahomabd.ttf
have been copied to the Reporting Server configuration directory, drive:\ibi\srv82\wfs\etc. In
addition, the Trebuchet MS and Tahoma fonts have been added to the fontuser.xml file:

<fontmap version="1">
  <when format="PDF PS">
    <!-- family/font tags should be added here -->
    <family name="Trebuchet MS">
      <font style="normal"
          metricsfile="pdtrbu"   fontfile="trebuc"   fonttype="TTF" />
      <font style="bold"
          metricsfile="pdtrbub"  fontfile="trebucbd"  fonttype="TTF" />
      <font style="italic"
          metricsfile="pdtrbui"  fontfile="trebucit"  fonttype="TTF" />
      <font style="bold+italic"
          metricsfile="pdtrbubi" fontfile="trebucbi" fonttype="TTF" />
    </family>
    <family name="Tahoma">
      <font style="normal"
          metricsfile="pdtaho"   fontfile="tahoma"   fonttype="TTF" />
      <font style="bold"
          metricsfile="pdtahob"  fontfile="tahomabd"  fonttype="TTF" />
    </family>
  </when>
</fontmap>

The following request against the GGSALES data source specifies the Trebuchet MS font for
the column headings and the bold style of Tahoma for the data in the PDF report output:

TABLE FILE GGSALES
SUM DOLLARS UNITS
BY REGION
ON TABLE PCHOLD FORMAT PDF
ON TABLE SET PAGE NOPAGE
ON TABLE SET STYLE *
TYPE = TITLE, FONT='Trebuchet MS',$
TYPE = DATA, FONT='Tahoma', style=bold, size=10, color=blue, $
END

Creating Reports With TIBCO® WebFOCUS Language

 639

Using Print Display Formats: PDF, PS

The output is:

640

9. Choosing a Display Format

Note: Except for OpenType fonts, in order to reduce the size of a generated PDF document,
only the subset of used characters of a font are included into the PDF document.

To confirm that a subset of the font is embedded, save a copy of the PDF file and open it in
Adobe Reader. On the File menu, select Properties. In the Font tab, look for the words
Embedded Subset next to the font name, as shown in the following image for the Tahoma and
Trebuchet MS fonts.

Creating PDF Files on z/OS for Use With UNIX Systems

PDF files created with HOLD FORMAT PDF present a challenge if you work in a z/OS
environment and use UNIX-based systems as the server for Adobe or as an intermediate
transfer point.

Creating Reports With TIBCO® WebFOCUS Language

 641

Using Print Display Formats: PDF, PS

The end of each PDF file has a table containing the byte offset, including line termination
characters, of each PDF object in the file. The offsets indicate that each line is terminated by
two characters, a carriage return and a line feed, which is the standard Windows text file
format. However, records in a UNIX text file are terminated by one character, a line feed only.
When using default settings, the offsets in a PDF file will be incorrect, causing an error when
Acrobat attempts to open the file. If the file is then transferred in BINARY mode to Windows, it
cannot be opened in Acrobat for Windows, as the carriage-return character was not inserted.

One solution has been to transfer the file to the UNIX system in text mode and then transfer in
text mode to the Windows system, as the carriage return is added by the transfer facility when
transferring to Windows.

If that is not possible or desirable, you can use the SET PDFLINETERM=SPACE command to
facilitate binary transfer to Windows from an ASCII-based UNIX system. This command causes
an extra space character to be appended to each record of the PDF output file. This extra
space acts as a placeholder for the expected carriage return character and makes the object
offsets in the file correct when it is transferred from z/OS to a UNIX system. This enables a
UNIX server to open a PDF file in that environment.

Note: A text mode transfer is always required when transferring a text file from a mainframe to
any other environment (Windows, ASCII Unix, or EBCDIC Unix).

Syntax:

How to Specify Line Termination Characters When Creating a PDF File

In a profile, a FOCEXEC, or from the command line, issue the following command:

SET PDFLINETERM={STANDARD|SPACE}

In a TABLE request, issue the following command

ON TABLE SET PDFLINETERM {STANDARD|SPACE}

where:

STANDARD

Creates a PDF file without any extra characters. This file will be a valid PDF file if
transferred in text mode to a Windows machine, but not to a UNIX machine. If
subsequently transferred from a UNIX machine to a Windows machine in text mode, it will
be a valid PDF file on the Windows machine.

642

9. Choosing a Display Format

SPACE

Creates a PDF file with an extra space character appended to each record. This file will be
a valid PDF file if transferred in text mode to a UNIX machine, but not to a Windows
machine. If subsequently transferred from an ASCII UNIX machine to a Windows machine
in binary mode, it will be a valid PDF file on the Windows machine.

Reference: Required PDFLINETERM Settings Based on Environment

The following chart will assist you in determining the correct setting to use, based on your
environment:

Transferring from z/OS to:

SET PDFLINETERM=

EBCDIC UNIX (text transfer)

ASCII UNIX (text transfer)

ASCII UNIX (text); then to Windows (binary)

UNIX (text); then to Windows (text)

Directly to Windows (text)

SPACE

SPACE

SPACE

STANDARD

STANDARD

Using Word Processing Display Formats: DOC, WP

You can display a report as a plain text word processing document using:

DOC format. The report opens in Microsoft Word within your web browser. When Word
opens the report, it may prompt you for information about converting text. If it does, accept
the default selection. The computer on which the report is being displayed must have Word
installed.

DOC format includes page breaks, including an initial page break before the beginning of
the report. If you wish to omit page breaks, issue the SET PAGE = NOPAGE command at the
beginning of the procedure.

DOC format does not support StyleSheets.

WP format. The report opens as plain text within your web browser.

Creating Reports With TIBCO® WebFOCUS Language

 643

Saving Report Output in Excel XLSX Format

If you issue the SET PAGE = OFF command, or include TABPAGENO in a heading or footing,
WP will indicate page breaks by including the character "1" in the first column at each
break, which is recognized as a page break control in the S/390 environment. WP format
does not include page breaks that are recognized by most browsers or word processing
programs.

WP format does not support StyleSheets.

You can specify that a report display as a plain text word processing document via the PCHOLD
command when you run the report in WebFOCUS. For more information, see How to Choose a
Display Format Using PCHOLD on page 576.

Saving Report Output in Excel XLSX Format

With Excel® 2007, Microsoft® introduced enhanced spreadsheet functionality in a new
workbook file format. Using WebFOCUS, you can retrieve data from any WebFOCUS supported
data source and generate a native XLSX format (Excel 2007, Excel 2010, and Excel 2013)
workbook for data analysis and distribution. This section applies to Excel 2007, Excel 2010,
and Excel 2013, unless otherwise indicated.

The WebFOCUS XLSX/EXL07 format supports the following Microsoft Office software products:

Microsoft Office 2013/2010/2007 and Microsoft Office 2000/2003 with the Microsoft
Office Compatibility Pack.

Open Office Support (FORMAT EXL07/XLSX). Core Excel functionality generated by the
EXL07/XLSX format is supported for Open Office as of WebFOCUS 8. For details on Open
Office, see http://www.openoffice.org/.

MAC Office 2008 and 2011. FORMAT EXL07/XLSX is certified with WebFOCUS 8.

WebFOCUS generates XLSX workbooks based on the Microsoft XLSX standard. These
workbooks are accessible through all browsers and mobile applications that support native
Microsoft XLSX files.

Microsoft Office 365™. Microsoft Office 365 offers the local installation of Microsoft Excel
2013. It works with the Office 2010 release and provides limited functionality with Office
2007. Microsoft Office 365 also permits uploading Microsoft Excel files to the cloud, where
they can be accessed on most devices using Office Online. For information on the Microsoft
Office 365 plans and features, see Office 365 for business FAQ.

You can use Microsoft Office 365 to access a WebFOCUS XLSX report. First, display the
XSLX report on the screen using the PCHOLD command, and then save the report to
OneDrive® for Business. Once the file is in the cloud, you can access the file using Office
Online.

644

9. Choosing a Display Format

For information on the differences in features available in Excel Online and in Microsoft
Office 2013, see Office Online Service Description.

For more information on working with Office Online and OneDrive for Business, see Using
Office Online in OneDrive.

Overview of EXL07/XLSX Format

FORMAT EXL07 and FORMAT XLSX are synonyms and can be used interchangeably. The FILE
SAVED message will always display "XLSX FILE SAVED", regardless of the syntax specified.

The WebFOCUS procedure generates a new workbook containing a single worksheet with the
report output containing your defined report elements (headings and subtotals), as well as
StyleSheet syntax (such as conditional styling and drill downs):

You can define a new default font for XLSX in the fontuser.xml file. This allows ease in
customizing the look and feel of XLSX workbooks. WebFOCUS uses Arial as the default
font. However, you can change the default font to match the Microsoft Office standard font,
Calibri, or your corporate standard.

XLSX format accurately displays formatted numeric, character, and date formats.

XLSX FORMULA enables you to convert summed information (such as column totals, row
totals, and calculated values) into Excel formulas that will automatically update as you edit
the Excel worksheet.

ReportCaster supports distribution of XLSX workbooks and XLSX FORMULA workbooks.

Within each generated worksheet, the columns in the report are automatically sized to fit
the largest value in the column (SQUEEZE=ON). WebFOCUS calculates the width of each
data column based on the font and size requirement of all cells in that column using font
metrics developed for other styled formats, including PDF and DHTML. Calculations are
based on the data and title elements of the report. Heading and footing elements are not
used in the sizing calculation and will be sized based on the data column requirements.

By default, there is a standard height for the data and Title rows. Heading, Footing,
Subhead, and Subfoot rows are taller than the data rows to support wrapping and for a
clearer distinction between headings and data.

Using the TITLETEXT StyleSheet attribute, tab names within the workbook can be
customized to provide better descriptions of the worksheet content.

Creating Reports With TIBCO® WebFOCUS Language

 645

Saving Report Output in Excel XLSX Format

Unlike the HTML-based (EXL2K) format, which removes all blanks, XLSX, by default, retains
leading, internal, and trailing blanks in cells within the worksheet. For more information on
how to affect these blanks, see Preserving Leading and Internal Blanks in Report Output on
page 686.

An XLSX worksheet can contain 1,048,576 rows by 16,384 columns. WebFOCUS will
generate worksheets larger than these defined limits, but Excel is not able to open the
workbook. For more information on how to support overflow in worksheets, see Overcoming
the Excel 2007/2010 Row Limit Using Overflow Worksheets on page 713.

Because of the new format of the zipped XLSX files, native HTML symbols, such as a caret
(<), cannot be supported as tag characters. For XLSX, unlike other output formats,
HTMLENCODE defaults to ON. HTMLENCODE set to OFF will cause any data containing
HTML tag characters to be omitted from the cell. For more information on the SET
HTMLENCODE command, see the Developing Reporting Applications manual.

Building the .xlsx Workbook File

Microsoft changed the format and structure of the Excel workbook in Excel 2007. The new .xlsx
file is a binary compilation of a group of xml files. Generating this new file format using
WebFOCUS is a two-step process that consists of generating the xml files containing the report
output and zipping the xml documents into the binary .xlsx format. The Reporting Server
performs the xml generation process. The zipping process can be completed either by the
client (WebFOCUS Servlet) or the server (JSCOM3):

WebFOCUS Servlet. The WebFOCUS Client within the application server performs the
zipping process. This can be done within the local client or through a remotely accessed
client. The servlet method is the default approach defined for each WebFOCUS Client, with
the client pointing to itself, by default.

JSCOM3. The Java layer of the Reporting Server performs the zipping operation. This option
should be used when the WebFOCUS Servlet is configured on a secured web or application
server. This is because JSCOM3 does not require URL access to a remote WebFOCUS
Client.

Syntax:

How to Select the Method for Zipping the .xlsx File

You designate the method and location where the zipping will occur by setting EXCELSERVURL
to a URL (for the WebFOCUS Servlet) or to a blank (for JSCOM3). You can set this value for a
specific procedure or for the entire environment:

For a procedure. Issue the SET EXCELSERVURL command within the procedure.

646

9. Choosing a Display Format

For the entire environment. Edit the IBIF_excelservurl variable in the WebFOCUS
Administration Console by selecting:

Configuration/Client Settings/General/IBIF_excelservurl

For more information on accessing the WebFOCUS Administration Console and setting the
IBIF_excelservurl variable, see the WebFOCUS Security and Administration manual.

The value you assign to EXCELSERVURL determines whether the WebFOCUS Servlet or
JSCOM3 performs the zipping operation:

Specifying the Servlet. To specify that the WebFOCUS Servlet should be used, set the
EXCELSERVURL parameter or the IBIF_variable to the URL. For example,

In a procedure:

SET EXCELSERVURL = http://servername:8080/ibi_apps

In the WebFOCUS Administration Console:

IBIF_excelservurl = http://servername:8080/ibi_apps

Specifying JSCOM3. To specify that JSCOM3 should be used within the current Reporting
Server, set EXCELSERVURL to a blank or an empty string.

In a procedure:

SET EXCELSERVURL = ''

In the WebFOCUS Administration Console:

IBIF_excelservurl = ''

By default, each WebFOCUS Client contains the following URL definition that points to itself:

&URL_PROTOCOL://&servername:&server_port&IBIF_webapp

Creating Reports With TIBCO® WebFOCUS Language

 647

Saving Report Output in Excel XLSX Format

Syntax:

How to Generate an Excel XLSX Workbook

You can specify that a report should be saved to an XLSX workbook, displayed in the browser,
or displayed in the Excel application.

ON TABLE {PCHOLD|HOLD} AS name FORMAT XLSX

where:

PCHOLD

Displays the generated workbook in either the browser or the Excel application, based on
your desktop settings. For information, see Viewing Excel Workbooks in the Browser vs. the
Excel Application on page 650.

HOLD

Saves a workbook with an .xlsx extension to the designated location.

name

Specifies a file name for the generated workbook.

Note: To assign a file name to the generated workbook, set the Save Report option to YES for
the .xlsx file extension in the WebFOCUS Client Redirection Settings. When opened in the Excel
application, the generated workbook will retain the designated AS name. For more information,
see the WebFOCUS Security and Administration manual.

Opening XLSX Report Output

To open XLSX workbooks, Excel 2013, 2010, or 2007 must be installed on the desktop.

648

Reference: Opening XLSX Report Output in Excel 2000/2003

9. Choosing a Display Format

Excel 2000 and Excel 2003 can be updated to read Excel XLSX workbooks using the Microsoft
Office Compatibility Pack available from the Microsoft download site (http://
www.microsoft.com/downloads/en/default.aspx). When the file extension of the file being
opened is .xlsx (XLSX workbook), the Microsoft Office Compatibility Pack performs the
necessary conversion to allow Excel 2000/2003 to read and open it.

In addition to the Microsoft Office Compatibility Pack, it is important to enable the WebFOCUS
Client Redirection Settings Save As option so that Excel 2000/2003 will be able to open the
XLSX report output without users first having to save it to their machine with the .xlxs file
extension. The WebFOCUS Client processing Redirection Settings Save As option configures
how the WebFOCUS Client sends each report output file type to the user machine. This option
can be set as follows:

Save As Option disabled (NO). The WebFOCUS Client Redirection Setting Save As is
disabled by default. When the Save As option is disabled, the WebFOCUS Client sends
report output to the user machine in memory with the application association specified for
the report format in the WebFOCUS Client Redirection Settings configuration file
(mime.wfs).

A user machine that does not have Excel 2007/2010 installed will not recognize the
application association for Excel 2007/2010 and Excel will display a message.

The Excel 2000/2003 user can select Save and provide a file name with the .xlsx
extension to save the report output to their machine. The user can then open the .xlsx file
directly from Excel 2000/2003.

Creating Reports With TIBCO® WebFOCUS Language

 649

Saving Report Output in Excel XLSX Format

Save As Option enabled (YES). When the WebFOCUS Redirection Save As option is
enabled, the WebFOCUS Client sends the report output to the user as a file with the
extension specified in the WebFOCUS Client Redirection Settings configuration file
(mime.wfs).

Upon receiving the file, Windows will display the File Download prompt asking the user to
Open or Save the file with the identified application type. The File Download prompt
displays the Name with the .xlsx file extension for the report output that is recognized as an
Excel XLSX file type.

Note: The download prompt will display for all users, including users who have Excel
2007/2010 installed on their machines.

If an Excel 2000/2003 user chooses to open the file, the Microsoft Office Compatibility
Pack will recognize the .xlsx file extension and perform the necessary conversion to allow
Excel 2000/2003 to read the Excel XLSX workbook.

If an Excel 2007/2010 user chooses to open the file, Excel will recognize the .xlsx file
extension and read the Excel XLSX workbook.

For additional information on WebFOCUS Client Redirection Settings, see the WebFOCUS
Security and Administration Guide.

Reference: Viewing Excel Workbooks in the Browser vs. the Excel Application

Your Operating System and desktop settings determine whether Excel output sent to the client
is displayed in an Internet Browser window or within the Excel application. When Excel output
has been defined within the Windows environment to Browse in same window, the workbook
generated by a WebFOCUS request is opened within an Internet Explorer® browser window.
When the Browse in same window option is unchecked for the .xls file type, the browser
window created by WebFOCUS is blank because the report output is displayed in the stand-
alone Excel application window.

In Windows XP and earlier, file type specific settings are managed on the desktop within
Windows Explorer by selecting Tools/Folder Options, clicking the File Types tab, selecting
the extension (.xls or .xlsx), clicking the Advanced button, and checking the Browse in same
window box.

650

9. Choosing a Display Format

In Windows 7, Microsoft removed the desktop settings that support opening worksheets in
the browser. This means that to change this behavior, you can no longer simply navigate to
the Folder Options dialog box, but that you must change a registry setting. This change is
documented in the Microsoft Knowledge Base Article ID 927009 at the following web site:

http://support.microsoft.com/kb/927009

Note: This works the same for both EXL2K and XLSX formats. The only difference is the
selection of file type based on the version of Excel output you will be generating.

Formatting Values Within Cells in XLSX Report Output

WebFOCUS formats defined in Master Files or within a FOCEXEC will be represented in the
resulting cells in an Excel XLSX worksheet. Where possible, the WebFOCUS formats are
translated to custom Excel formats and applied to values passed as raw data. Each data value
passed to a cell in Excel is defined with a value and a format mask pair. The data format is
associated with the cell rather than embedded in the value. This technique provides enhanced
support for editing worksheets generated by WebFOCUS. New values entered into existing cells
will retain the cell formats and continue to display in the style defined for the column within the
report.

The following types of data can be passed to Excel:

Numeric. Where corresponding Excel format masks can be defined, numeric values are
passed as raw values with associated format masks. In instances where an equivalent
format mask cannot be defined, the numeric value is passed as a text string.

Alphanumeric. Alphanumeric formats are passed to Excel as text strings, with General
format defined. By default, General format presents all text fields as left-justified. Alignment
and other styling attributes can be applied to these cells to override the default.

Date formats. Data that contain sufficient elements to define a valid Excel date format are
passed as raw date values with the WebFOCUS formats translated to Excel date format
masks. In WebFOCUS formats that do not contain sufficient information to create valid
Excel date values, the dates are converted to text strings.

Date-Time formats. Date-time values are passed as raw date-time values with WebFOCUS
formats translated to Excel date-time format masks using Custom formats.

Text. Text values are passed as strings with General Format defined (as with alphanumeric
data).

Note: This behavior is a change from EXL2K format, where cells containing dates and more
complex numeric formats were passed as formatted text.

Creating Reports With TIBCO® WebFOCUS Language

 651

Saving Report Output in Excel XLSX Format

Displaying Formatted Numeric Values in XLSX Report Output

Each numeric WebFOCUS format is translated to a custom numeric Excel format. The numeric
value is displayed in the Excel formula bar for the selected cell. Within the actual cell, the
value with the format mask applied displays.

The WebFOCUS formats for the following numeric data types are translated into Excel XLSX
format masks supporting full editing within the resulting workbook:

Data types: E, F, D, I, P

Comma edit option (C)

Zero suppression (S)

Leading zero (L)

Floating currency symbol (M)

Comma suppression (c)

Right-side minus sign (-)

Credit negative (CR)

Bracket negative (B)

Fixed extended currency symbol (!d, !e, !l, !y)

Floating extended currency symbol (!D, !E, !L, !Y)

Percent (%)

Example:

Passing Numeric Formats to XLSX Report Output

In the following example, the DOLLARS field is assigned different numeric formats to
demonstrate different available options. The column titles have been edited to display the
WebFOCUS format options that have been applied:

TABLE FILE GGSALES
SUM DOLLARS/D12.2 AS 'D12.2'
    DOLLARS/D12C  AS 'D12C'
    DOLLARS/D12CM AS 'D12CM'
BY REGION
BY CATEGORY
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET BYDISPLAY ON
END

652

9. Choosing a Display Format

In the resulting worksheet, notice that cell C2 containing the DOLLAR value for Midwest Coffee
presents the value with the WebFOCUS format D12.2, which presents the comma (,) and two
decimal places. On the formula bar, the actual value is presented without any formatting.
Examine each of the DOLLAR values in each row to see that the value as displayed in the
formula bar remains the same, and only the display values presented in each cell change.

Also notice that with SET BYDISPLAY ON, the BY field values are repeated for every row on the
worksheet. This creates fully qualified data rows that can be used with various data sorting,
filtering, and table features in Excel without losing valuable information. This setting is
recommended as a best practice for all worksheets.

The following example uses Fixed Dollar (N) format, as well as multiple combined format
options. Each WebFOCUS format option is translated to the appropriate Excel XLSX format
mask and applied to the cell value:

TABLE FILE GGSALES
SUM BUDDOLLARS/D12N
    DOLLARS/D12M
COMPUTE OVERBUDGET/D12BMc = BUDDOLLARS-DOLLARS; AS 'Over Budget'
BY REGION
BY CATEGORY
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET BYDISPLAY ON
END

Creating Reports With TIBCO® WebFOCUS Language

 653

Saving Report Output in Excel XLSX Format

Notice the fixed numeric format defined for the BUDDOLLARS column (Column C) presents the
local currency symbol in a fixed position within each cell, regardless of the size of the data
value. On the formula bar, the values in the Over Budget calculated field is passed as a
negative value where appropriate. In the actual cells, the bracketed styling is applied to the
negative values as part of the custom Excel XLSX format mask.

Using Numeric Formats in Report Headings and Footings

By default, headings and footings are passed to Excel as a single character string. Spot
markers are not supported for positioning within each line. Numeric fields and dates passed in
headings and footings are passed as text strings within the overall heading or footing
contents.

To display numeric fields and dates within headings and footings as numeric or date values,
use HEADALIGN=BODY in the StyleSheet to define each of the items in the heading as an
individual cell. Each cell containing numeric or date values will then be passed as the
appropriate value with the associated format mask.

Using Numeric Format Punctuation in Headings and Footings

For data columns, all currency formats are translated using the Excel XLSX format masks that
use the punctuation rules defined by the regional settings of the desktop.

654

9. Choosing a Display Format

In languages that use Continental Decimal Notation, the currency definitions designate that a
comma (,) is used as the decimal separator, and a period (.) is used as the thousands
separator, so D12.2CM may present the value as $ 9.999,99 rather than the English (United
States) value $ 9,999.99. In headings and footings, you can designate that punctuation
should be converted to Continental Decimal notation by issuing the SET CDN=ON command.
With this setting in effect, the data embedded within heading and footing text strings will be
formatted using the converted punctuation. Specify HEADALIGN=BODY to delineate items as
individual cells and to retain the numeric formatting within the field, which will follow the same
rules as the report data within the data columns.

Reference: Usage Note for Sorting an XSLX Report That Contains a Footing

In XLSX format, the report footer is included as a part of the data table in Excel. This is not the
same behavior in EXL2K. In EXL2K format, the footer is not included as a part of the table.

For example, if you run the following procedure and sort the data table, the report footer is part
of the data table, as shown in the image below the request:

TABLE FILE WF_RETAIL_LITE
PRINT COUNTRY_NAME AS Country
STATE_PROV_NAME AS State
PRODUCT_CATEGORY AS Category
WHERE RECORDLIMIT EQ 10
FOOTING
""
"TEST FOOTING TEST FOOTING"
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET STYLE *
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 655

Saving Report Output in Excel XLSX Format

The output is:

The workaround is to add a named data range to the procedure, as shown in the following
procedure:

TABLE FILE WF_RETAIL_LITE
PRINT COUNTRY_NAME AS Country
STATE_PROV_NAME AS State
PRODUCT_CATEGORY AS Category
WHERE RECORDLIMIT EQ 10
FOOTING
""
"TEST FOOTING TEST FOOTING"
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET STYLE *
TYPE=DATA, IN-RANGES=DATA, $
TYPE=TITLE, IN-RANGES=DATA, $
ENDSTYLE
END

656

The report footer is not part of the data table, as shown in the following image:

9. Choosing a Display Format

Passing Dates to XLSX Report Output

Most translated and smart dates can be sent to Excel as standard date values with format
masks, enabling Excel to use them in functions, formulas, and sort sequences.

Excel 2007 only supports mixed-case date text strings so all month and day names are
displayed in mixed-case, regardless of how the case has been specified in the WebFOCUS
format. For example, the WebFOCUS date format WRYMTRD presents the date text information
in uppercase in all non-Excel formats. Excel transforms this value to mixed-case automatically.

In HTML, the date format displays as:

In XLSX, the date format displays as:

Creating Reports With TIBCO® WebFOCUS Language

 657

Saving Report Output in Excel XLSX Format

Example:

Translating WebFOCUS Dates to Excel XLSX Dates

The following request against the GGSALES data source creates the date January 1, 2010 and
converts it to four date formats with translated text:

DEFINE FILE GGSALES
NEWDATE/MDYY = '01/01/2010';
WRMtrDY/WRMtrDY = NEWDATE;
wDMTY/wDMTY = NEWDATE;
wrDMTRY/wrDMTRY = NEWDATE;
wrYMtrD/wrYMtrD = NEWDATE;
END
TABLE FILE GGSALES
SUM DATE NOPRINT
NEWDATE WRMtrDY wDMTY wrDMTRY wrYMtrD
ON TABLE PCHOLD FORMAT XLSX
END

The following table shows how the dates should appear.

WebFOCUS Format WebFOCUS Display

XLSX Display

XLSX Value

WRMtrDY

FRIDAY, January 1 10

Friday, January 1 10

1/1/2010

wDMTY

wrDMTY

wrYMtrD

Fri, 1 JAN 10

Fri, 1 Jan 10

1/1/2010

Friday, 1 JANUARY 10

Friday, 1 January 10

1/1/2010

FRIDAY, 10 JANUARY 1

Friday, 10 January 1

1/1/2010

In Excel 2007/2010, all of the cells have a date value with format masks, and all month and
day names are in mixed-case, regardless of how the case has been specified in the
WebFOCUS format. The output is:

Passing Dates Without a Day Component

Date formats that do not specify the day value explicitly are defined as the date value of the
first day of the month. Therefore, the value placed in the cell may be different from the day
component value in the source data field and may produce unexpected results when used for
sorting or date calculations in an Excel formula.

658

9. Choosing a Display Format

The following table shows how WebFOCUS date formats are represented in XLSX. The table
shows how the value is preserved in the cell and how the display is generated using the format
mask that corresponds to the WebFOCUS date format.

DATEFLD/MDYY = '01/02/2010'

WebFOCUS Format

XLSX Display

XLSX Value

DMYY

MY

MTY

MTDY

02/01/2010

1/2/2010

01/10

Jan, 10

Jan 2, 10

1/1/2010

1/1/2010

1/2/2010

Example:

Passing WebFOCUS Dates With and Without a Day Component to XLSX Report Output

The following request against the GGSALES data source creates the date January 2, 2010 and
passes it to Excel with formats MDYY, DMYY, MY, and MTDY:

DEFINE FILE GGSALES
NEWDATE/MDYY = '01/02/2010';
END
TABLE FILE GGSALES
SUM DATE NOPRINT
NEWDATE AS 'MDYY' NEWDATE/DMYY AS 'DMYY' NEWDATE/MY AS 'MY'
        NEWDATE/MTY AS 'MTY' NEWDATE/MTDY AS 'MTDY'
ON TABLE PCHOLD FORMAT XLSX
END

Columns D and E have actual date values with format masks, displayed by Excel 2007/2010
in mixed-case. Since the MTY format does not have a day component, the date value stored is
the first of January 2010 (1/1/2010), not the second of January 2010 (1/2/2010):

Passing Date Components for Use in Excel Formulas

Dates formatted as individual components (for example, D, Y, M, W) are passed to Excel as
numeric values that can be used as parameters to Excel date functions. The values are
passed as General format that are recognized by Excel as numbers.

Creating Reports With TIBCO® WebFOCUS Language

 659

Saving Report Output in Excel XLSX Format

Example:

Passing Numeric Date Components to XLSX Report Output

The following request against the GGSALES data source creates the date January 1, 2010 and
extracts numeric date components, passing them to Excel 2007/2010:

DEFINE FILE GGSALES
NEWDATE/MDYY = '01/01/2010';
D/D = NEWDATE;
Y/Y = NEWDATE;
W/W = NEWDATE;
w/w = NEWDATE;
M/M = NEWDATE;
YY/YY = NEWDATE;
END
TABLE FILE GGSALES
SUM DATE NOPRINT
NEWDATE D Y W w M YY
ON TABLE PCHOLD FORMAT XLSX
END

The output is:

Passing Quarter Formats

Date formats that contain a Quarter component are always passed to Excel as text strings
since Excel does not support Quarter formats.

Example:

Passing Dates With a Quarter Component to XLSX Report Output

The following request against the GGSALES data source creates the date January 1, 2010 and
converts it to date formats that contain a Quarter component:

DEFINE FILE GGSALES
NEWDATE/MDYY = '01/01/2010';
Q/Q = NEWDATE;
QY/QY = NEWDATE;
YBQ/YBQ = NEWDATE;
END
TABLE FILE GGSALES
SUM DATE NOPRINT
NEWDATE Q QY YBQ
ON TABLE PCHOLD FORMAT XLSX
END

In XLSX, the cells containing dates with Quarter components have General format. To see this,
open the Format Cells dialog box.

660

The output is:

9. Choosing a Display Format

Passing Date Components Defined as Translated Text

Date formats that do not contain sufficient information to present a valid date result in Excel
are not translated to a value, including formats that do not contain year and/or month
information. These dates will be sent to Excel as text. In the absence of complete information,
the year defaults to the current year, so the value sent would be incorrect if this type of format
was passed as a date value. The following formats will not be sent as values:

MT, MTR, Mt, Mtr

W, w, WR, wr

When date formats are passed to XLSX with format masks, all month and day names are in
mixed-case, regardless of how the case has been specified in the WebFOCUS format. However,
since the values in this example are always sent as text, the casing defined in the WebFOCUS
format is applied in the resulting cell.

Example:

Passing Date Components Defined as Translated Text to XLSX Report Output

The following request against the GGSALES data source creates the date January 1, 2010 and
converts it to date formats that are defined as either month name or day name:

DEFINE FILE GGSALES
NEWDATE/MDYY = '01/01/2010';
MT/MT = NEWDATE;
MTR/MTR = NEWDATE;
Mtr/Mtr = NEWDATE;
WR/WR = NEWDATE;
wr/wr = NEWDATE;
END
TABLE FILE GGSALES
SUM DATE NOPRINT
NEWDATE MT MTR Mtr WR wr
ON TABLE PCHOLD FORMAT XLSX
END

In Excel 2007 or 2010, the cells containing the days have General format. To see this, open
the Format Cells dialog box.

Creating Reports With TIBCO® WebFOCUS Language

 661

Saving Report Output in Excel XLSX Format

The output is:

Reference: Usage Notes for Date Values in XLSX Report Output

The following date formats are not supported in XLSX. They will translate into Excel General
format and possibly produce unpredictable results:

JUL, YYJUL, and I2MT.

Dates stored as a packed or alphanumeric field with date display options.

Passing Date-Time to XLSX

Most WebFOCUS date-time formats can be sent to XLSX as standard date/time values with
format masks, enabling Excel to use them in functions, formulas, and sort sequences.

As with the Date formats, Excel only supports mixed-case to date-time fields, so if the date-
time format contains text and is supported by Excel, the text will be in mixed-case, regardless
of the casing defined within the WebFOCUS format.

Example:

Passing Date-Time to XLSX

The following request shows an example against the GGSALES data source.

DEFINE FILE GGSALES
DT1/HYYMDm WITH REGION = DT(20100506 16:17:01.993876);
DPT1/HDMTYYm = DT1;
ALPHA_DATE1/A30 = HCNVRT(DT1,'(HYYMDm)',30,'A30');
END
TABLE FILE GGSALES
PRINT
ALPHA_DATE1
DT1 AS 'HYYMDm'
DPT1 AS 'HDMTYYm'
DT1/HdMTYYBS   AS 'HdMTYYBS'
DT1/HdMTYYBs   AS 'HdMTYYBs'
ON TABLE SET SPACES 1
IF RECORDLIMIT EQ 1
ON TABLE PCHOLD FORMAT XLSX
END

662

The output is:

9. Choosing a Display Format

Note: Minutes by themselves are not supported in Excel and will be sent as an integer to XLSX
with a Custom format.

Also, Excel time formats only support to the milliseconds. WebFOCUS formats that display
microseconds will send the value to Excel, but the value will be rounded to milliseconds within
the worksheet if the cell is edited.

The following table shows how the date-time values appear.

WebFOCUS Format

XLSX Displays

XLSX Value

HYYMDm

HDMTYYm

HdMTYYBS

HdMTYYBs

2010/05/06 16:17:01.993

5/6/2010 4:17:02 PM

06 May 2010 16:17:01.993

5/6/2010 4:17:02 PM

6 May 2010 16:17:01

5/6/2010 4:17:01 PM

6 May 2010 16:17:01.993

5/6/2010 4:17:02 PM

Generating Native Excel Formulas in XLSX Report Output

When you display or save a tabular report request using XLSX FORMULA, the resulting
worksheet contains an Excel formula that computes and displays the results of any type of
summed information, such as column totals, row totals, subtotals, and calculated values,
rather than static numbers. A formula for a calculated value is generated by translating the
internal form of the WebFOCUS expression into an Excel formula. Worksheets saved using the
XLSX FORMULA format are interactive, allowing for "what if" scenarios that immediately reflect
any additions or modifications made to the data.

Understanding Formula Versus Value

The XLSX FORMULA format will generate formulas rather than values for the following
WebFOCUS TABLE commands: ROW-TOTAL, COLUMN-TOTAL, SUB-TOTAL, SUBTOTAL, and
SUMMARIZE, as well as for calculations performed by functions.

A DEFINE field will always generate a constant value and not a formula.

Creating Reports With TIBCO® WebFOCUS Language

 663

Saving Report Output in Excel XLSX Format

COMPUTE will generate the formula, except when the COMPUTE is equal to a single
variable. In that case, the constant is placed and not the formula.

If your report contains a calculated value (generated by the COMPUTE or RECOMPUTE
command), all of the fields referenced by the calculated value must be displayed in the
report in order for a cell reference to be included in the formula. If the referenced column is
not displayed in the workbook, the data value will be placed in the formula, rather than a
cell reference. Additionally, if the value cannot be reliably calculated based on the
information passed to Excel, the value, rather than an expression, will be used. For
example, using the LAST function in WebFOCUS cannot be translated correctly into Excel. In
this instance, the LAST value is used in the expression, rather than a cell reference.

XLSX FORMULA is not supported with financial reports created with the Report canvas or the
underlying Financial Modeling Language (FML).

For more information, see Translation Support for FORMAT XLSX FORMULA on page 664.

Reference: Translation Support for FORMAT XLSX FORMULA

This topic describes translation support for FORMAT XLSX FORMULA. Use of unsupported
WebFOCUS features may produce unreliable results.

All standard operators are supported. These include arithmetic operators, relational
operators, string operators, IF/THEN/ELSE, and logical operators. However, column
notation is not supported.

The IS-PRESENT, IS-MISSING, IS-FROM, FROM, NOT-FROM, IS-MORE-THAN, IS-LESS-THAN,
CONTAINS, and OMITS operators are not supported.

The logical operators AND and OR are not supported in conditional (IF-THEN-ELSE) or logical
expressions.

The following functions are supported:

ABS, ARGLEN, ATODBL, BYTVAL, CHARGET, CTRAN, DMOD, DOWK, DOWK, DOWKL, EXP,
FMOD, HEXBYT, HHMMSS, IMOD, LCWORD, LOCASE, LOG, MAX, MIN, OVRLAY, POSIT,
RDUNIF, SQRT, SUBSTR, TODAY, and UPCASE. The EDIT function is supported for
converting formats (one argument variant). It is not supported for editing strings.

The functions CTRFLD, LJUST, and RJUST are not recommended for justifying data in Excel
columns. With the use of Excel proportional fonts, the StyleSheet JUSTIFY attribute is more
appropriate.

Be cautious when using functions that use decimal values as an argument (BYTVAL,
CTRAN, HEXBYT). Based on whether the operating environment is EBCDIC or ASCII, the
results may be different.

664

XLSX FORMULA is not supported with the following WebFOCUS commands and phrases:

9. Choosing a Display Format

DEFINE

OVER

FOR

NOPRINT

Multiple display (PRINT, LIST, SUM, and COUNT) commands

SEQUENCE StyleSheet attribute

RECAP

SET HIDENULLACRS

SET SUBTOTALS = ABOVE

LAST

The BYDISPLAY ON setting is recommended to allow the sort field value to be available on
all rows for recalculations.

If an expression requires more than 1024 characters, WebFOCUS will place the value into
the cell, and not the formula.

Conditional styling is based on the values in the original report. If the worksheet values are
changed and the formulas are recomputed, the styling will not reflect the updated
information.

Syntax:

How to Save Reports as FORMAT XLSX FORMULA

Add the following syntax to your request to take advantage of Excel formulas in your workbook:

ON TABLE {PCHOLD|HOLD} FORMAT XLSX FORMULA

where:

PCHOLD

Displays the output in an XLSX workbook.

HOLD

Saves the output for reuse in an Excel worksheet. For details, see Saving and Reusing Your
Report Output on page 471.

Creating Reports With TIBCO® WebFOCUS Language

 665

Saving Report Output in Excel XLSX Format

Example:

Generating Native Excel Formulas for Column Totals

The following example illustrates how a column total in a report request is translated to an
Excel formula when you use the XLSX FORMULA format. Notice that the formatting of the
column total (TYPE=GRANDTOTAL) is retained in the Excel workbook. When you select the total
in the report, the equation =SUM(B4:B10) displays in the formula bar, representing the column
total as a sum of cell ranges.

TABLE FILE SHORT
HEADING
"Projected Return By Region"
" "
SUM PROJECTED_RETURN AS 'RETURN'
BY REGION AS 'REGION'
ON TABLE COLUMN-TOTAL
ON TABLE PCHOLD FORMAT XLSX FORMULA
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, FONT='ARIAL', SIZE=9, TITLETEXT=’By Region’,$
TYPE=TITLE, BACKCOLOR=RGB(102 102 102), COLOR=RGB(255 255 255),$
TYPE=HEADING, SIZE=12, STYLE=BOLD, JUSTIFY=CENTER,$
TYPE=GRANDTOTAL, BACKCOLOR=RGB(210 210 210), STYLE=BOLD,$
END

The output is:

666

WebFOCUS can translate any total (subtotal, row total, or column total) to an Excel formula.
For related information, see Translation Support for FORMAT XLSX FORMULA on page 664.

Example:

Generating Native Excel Formulas for Row Totals

9. Choosing a Display Format

The following request calculates totals for returns and balances across continents. The row
totals are represented as sums of cell ranges.

TABLE FILE SHORT
HEADING
"Projected Return Across Continent"
" "
SUM PROJECTED_RETURN AS 'Return' AND BALANCE AS 'Balance'
ACROSS CONTINENT AS 'CONTINENT'
BY REGION AS 'REGION'
ON CONTINENT ROW-TOTAL AS 'TOTAL'
ON TABLE COLUMN-TOTAL AS 'TOTAL'
ON TABLE PCHOLD FORMAT XLSX FORMULA
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, FONT='ARIAL', SIZE=9, TITLETEXT=’Across Continent’,$
TYPE=TITLE, BACKCOLOR=RGB(102 102 102), COLOR=RGB(255 255 255),$
TYPE=HEADING, SIZE=12, STYLE=BOLD, JUSTIFY=CENTER,$
TYPE=ACROSSTITLE, STYLE=BOLD,$
TYPE=GRANDTOTAL, BACKCOLOR=RGB(210 210 210), STYLE=BOLD,$
END

The following output highlights the formula that calculates the row total in cell
I12=C12+E12+G12.

Example:

Generating Native Excel Formulas for Calculated Values

The following request totals the columns for retail cost and dealer cost, and calculates the
value of a field called PROFIT by subtracting the DOLLARS from the BUDDOLLARS.

Creating Reports With TIBCO® WebFOCUS Language

 667

Saving Report Output in Excel XLSX Format

The formula for the calculated values is generated by translating the internal form of the
WebFOCUS expression (PROFIT/D12.2MC = BUDDOLLARS - DOLLARS;) into an Excel formula.
In this example, the formulas appear in cells B8, C8, and D8.

All fields referenced in the calculation should be displayed in the report for a valid formula to
be created using cell references. Otherwise, it may be created using values not in the report. If
the fields used in the calculation are not present in the report and there is a subsequent
RECOMPUTE, the formula created for the RECOMPUTE will not be correct.

TABLE FILE GGSALES
ON TABLE SET PAGE-NUM OFF
SUM BUDDOLLARS/I8MC AND DOLLARS/I8MC
COMPUTE PROFIT/D12.2MC = BUDDOLLARS - DOLLARS;
BY REGION
HEADING
"Profit By Region"
" "
ON TABLE COLUMN-TOTAL
ON TABLE PCHOLD FORMAT XLSX FORMULA
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, FONT='ARIAL', SIZE=9, TITLETEXT=’By Region’,$
TYPE=TITLE, BACKCOLOR=RGB(102 102 102), COLOR=RGB(255 255 255),$
TYPE=HEADING, SIZE=12, STYLE=BOLD, JUSTIFY=CENTER,$
TYPE=GRANDTOTAL, BACKCOLOR=RGB(210 210 210), STYLE=BOLD,$
END

The following output highlights the formula that calculates for the column total of PROFIT:
D8=SUM(D4:D7).

668

Example:

Generating a Native Excel Formula for a Function

9. Choosing a Display Format

The following example illustrates how functions are translated to Excel reports. The function
IMOD divides ACCTNUMBER by 1000 and returns the remainder to LAST3_ACCT. The Excel
formula corresponds to =TRUNC((MOD($C3,(1000)))). TRUNC is used when the answer
returned from an equation is being placed into an Integer field, to be sure there are no
decimals.

TABLE FILE EMPLOYEE
PRINT ACCTNUMBER AS 'Account Number'
COMPUTE LAST3_ACCT/I3L = IMOD(ACCTNUMBER, 1000, LAST3_ACCT);
BY LAST_NAME AS 'Last Name'
BY FIRST_NAME AS 'First Name'
WHERE (ACCTNUMBER NE 000000000) AND (DEPARTMENT EQ 'MIS');
ON TABLE PCHOLD FORMAT XLSX FORMULA
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, FONT='ARIAL', SIZE=9,$
TYPE=TITLE, BACKCOLOR=RGB(102 102 102), COLOR=RGB(255 255 255), STYLE=BOLD,$
END

The output is:

Reference: Generating a Formula With Recomputed Values

If your report contains a calculated value (generated by the COMPUTE or RECOMPUTE
command), all of the fields referenced by the calculated value must be displayed in the
report in order for cell references to be included in the formula. If a referenced column is
not displayed in the workbook, the data value will be placed in the formula, rather than a
cell reference. In the case of RECOMPUTE, the value used may be an incorrect value from
the last detail record of the sort break.

Creating Reports With TIBCO® WebFOCUS Language

 669

Saving Report Output in Excel XLSX Format

Example:

Generating a Formula With Recomputed Values

The following request computes the difference (DIFF) by subtracting budgeted dollars from
dollar sales. The budgeted dollars field used in the expression is not included in the SUM
command. The value of DIFF is recomputed on the region level.

TABLE FILE GGSALES
HEADING
"Profit By Region"
" "
SUM DOLLARS/I8CM
COMPUTE DIFF/I8CM=DOLLARS - BUDDOLLARS;
BY REGION
BY CATEGORY
ON REGION RECOMPUTE
ON TABLE PCHOLD FORMAT XLSX FORMULA
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, FONT='ARIAL', SIZE=9, TITLETEXT=’By Region’,$
TYPE=TITLE, BACKCOLOR=RGB(102 102 102), COLOR=RGB(255 255 255),$
TYPE=HEADING, SIZE=12, STYLE=BOLD, JUSTIFY=CENTER,$
TYPE=SUBTOTAL, BACKCOLOR=RGB(210 210 210),$
TYPE=GRANDTOTAL, BACKCOLOR=RGB(166 166 166), STYLE=BOLD,$
END

670

9. Choosing a Display Format

The output shows that the formula is subtracting a data value that is not displayed on the
worksheet. It is actually the BUDDOLLARS value from the current hardcoded value, since there
is no cell reference.

If you add the BUDDOLLARS column to the request, the formula can be recomputed correctly.

SUM DOLLARS/I8MC BUDDOLLARS/I8MC

Creating Reports With TIBCO® WebFOCUS Language

 671

Saving Report Output in Excel XLSX Format

The formula generated with the new SUM command contains cell references for both fields
used in the calculation.

Using XLSX FORMULA With Prefix Operators

XLSX FORMULA output supports prefix operators that are used on summary lines generated by
WebFOCUS commands, such as SUBTOTAL and RECOMPUTE. Where a corresponding formula
exists in Excel, these prefix operators are translated into the equivalent Excel summarization
formula. The results of prefix operators used directly against retrieved data continue to be
passed to Excel as values, not formulas.

The following table identifies the prefix operators supported by XLSX FORMULA when used on
summary lines, and the Excel formula equivalent placed in the generated worksheet.

Prefix Operator

Excel Formula Equivalent

SUM.

=SUM()

672

9. Choosing a Display Format

Prefix Operator

Excel Formula Equivalent

AVE.

CNT.

MIN.

MAX.

=AVERAGE()

=COUNT()

=MIN()

=MAX()

The following prefix operators are not translated to formulas when used on summary lines in
XLSX FORMULA.

ASQ.

FST.

LST.

Note:

When using a prefix operator on a field specified directly against retrieved data, there is no
space between the prefix operator and the field on which it operates.

For example, in the following aggregating display command, the AVE. prefix operator
operates on the DOLLARS field.

SUM AVE.DOLLARS

When using a prefix operator on a summary line, you must leave a space between the
prefix operator and the aggregated field on which it operates.

In the following summary command, the MAX. prefix operator operates on the DOLLARS
field at the REGION sort break. Note the required blank space between the prefix operator
and the field name.

ON REGION RECOMPUTE MAX. DOLLARS

Example:

Using a Summary Prefix Operator With FORMAT XLSX FORMULA

In the following request against the GGSALES data source, the RECOMPUTE command for the
REGION sort field calculates the maximum of the aggregated DOLLARS field and the minimum
of the aggregated BUDDOLLARS field.

Creating Reports With TIBCO® WebFOCUS Language

 673

Saving Report Output in Excel XLSX Format

TABLE FILE GGSALES
SUM UNITS DOLLARS/I8MC BUDDOLLARS/I8MC
AND COMPUTE DIFF/I8MC= DOLLARS-BUDDOLLARS;
BY REGION
BY CATEGORY
WHERE CATEGORY EQ 'Food' OR 'Coffee'
WHERE REGION EQ 'West' OR 'Midwest'
ON REGION RECOMPUTE MAX. DOLLARS MIN. BUDDOLLARS DIFF
ON TABLE PCHOLD FORMAT XLSX FORMULA
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, FONT='ARIAL', SIZE=9,$
TYPE=TITLE, BACKCOLOR=RGB(102 102 102), COLOR=RGB(255 255 255),$
TYPE=SUBTOTAL, BACKCOLOR=RGB(210 210 210),$
TYPE=GRANDTOTAL, BACKCOLOR=RGB(166 166 166), STYLE=BOLD,$
END

In the output, shown in the following image, the cell that represents the recomputed DOLLARS
for the Midwest region has been generated as the following formula.

=MIN(E2:E3)

Example:

Using a Prefix Operator on a Display Command With FORMAT XLSX FORMULA

In the following request against the GGSALES data source, the CNT., AVE., and PCT. Prefix
operators are used in the SUM display command.

TABLE FILE GGSALES
SUM UNITS
CNT.UNITS
AVE.UNITS
PCT.UNITS
BY REGION
BY ST
ON TABLE PCHOLD FORMAT XLSX FORMULA
END

674

The output shows that the prefix operators were not passed to Excel as formulas. They were
passed as data values.

9. Choosing a Display Format

NODATA With Formulas

Support for full Excel functionality requires that only valid numeric values are placed into cells
that will be used for formula references.

The null value (NODATA='') is supported for calculations. When cells containing the default
NODATA symbol (.) are used in a formula, they will cause a formula error.

For example:

Creating Reports With TIBCO® WebFOCUS Language

 675

Saving Report Output in Excel XLSX Format

SET NODATA=''
TABLE FILE GGSALES
SUM DOLLARS/D12CM UNITS/D12C AND ROW-TOTAL AND COLUMN-TOTAL
COMPUTE REVENUE/D12CM=DOLLARS*UNITS; AS 'Revenue'
BY LOWEST GGSALES.SALES01.CATEGORY
BY GGSALES.SALES01.PRODUCT
ACROSS REGION
ON TABLE PCHOLD FORMAT XLSX FORMULA
END
------------------------
SET NODATA=''
DEFINE FILE GGSALES
DOLLARMOD/D12CM MISSING ON=IF REGION GT 'V' THEN MISSING ELSE DOLLAR;
END
TABLE FILE GGSALES
SUM DOLLARMOD/D12CM UNITS/D12C AND ROW-TOTAL AND COLUMN-TOTAL
COMPUTE REVENUE/D12CM=DOLLARMOD*UNITS; AS 'Revenue'
BY REGION
BY LOWEST GGSALES.SALES01.CATEGORY
BY GGSALES.SALES01.PRODUCT
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE PCHOLD FORMAT XLSX FORMULA
END

Reference: Usage Notes for XLSX With Formulas

Formulas are defined within a single worksheet. They will not be assigned across
worksheets.

BYTOC compound workbooks can contain formulas. A separate worksheet/tab is generated
for each primary key value and formulas are defined with references within that sheet. In
BYTOC compound workbooks, a separate tab is generated for overall grand totals. These
will not contain formula references to the component worksheets.

Controlling Column Width and Wrapping in XLSX Report Output

Column width and data wrapping can be controlled in an Excel worksheet when using
FORMAT XLSX.

To size the column without wrapping and define the exact size width, use SQUEEZE=ON. If
a data value is wider than the specified width of the column, a portion of the data will be
hidden from view, but fully visible in the formula bar. You can adjust the column width in
Excel after the worksheet has been generated.

The default behavior is for all data to wrap within the defined column width. You can also
specify the exact width of a column using WRAP=ON.

WRAP is not supported for Date format fields.

676

9. Choosing a Display Format

Syntax:

How to Set Column Width in XLSX Report Output

TYPE=REPORT, [COLUMN=column,] SQUEEZE=value,$

where:

column

Identifies a particular column. If COLUMN is not included in the declaration, default
SQUEEZE behavior is applied to the entire report.

value

Is one of the following:

ON

OFF

n

Note:

Automatically sizes the columns based on the largest data value in the column. This is
the default behavior.

Sizes the columns based on the maximum size defined for the field in the Master File
or Define.

Represents a specific numeric value for which the column width can be set. The value
represents the measure specified with the UNITS parameter (the default is inches).
This is the most commonly used SQUEEZE setting in an XLSX report. This turns off
data wrapping.

SQUEEZE can be applied to the entire report by using the ON TABLE SET SQUEEZE ON
command.

SQUEEZE is not supported for columns created with the OVER phrase or with TABLEF.

Syntax:

How to Wrap Data in XLSX Report Output

TYPE=REPORT, [COLUMN=column,] WRAP=value,$

where:

column

Designates a particular column to apply wrapping behavior to. If COLUMN is not included in
the declaration, wrapping will be applied to the entire report.

Creating Reports With TIBCO® WebFOCUS Language

 677

Saving Report Output in Excel XLSX Format

value

Is one of the following:

ON

OFF

n

Turns on data wrapping. ON is the default value. With this setting, the column width is
determined by the client (Excel). Data wraps if it exceeds the width of the column and
the row height expands to meet the new height of the wrapped data.

Turns off data wrapping. Data will not wrap in any cell in the column.

Represents a specific numeric value that the column width can be set to. The value
represents the measure specified with the UNITS parameter (the default is inches).

This setting implies ON. However, the column width is set to the specified width
unless the data is wider than the column width, in which case, wrapping will occur as
for ON.

Note: WRAP is not supported for Date format fields.

Example:

Controlling Column Width and Wrapping in XLSX Report Output

The following example illustrates how to turn on and turn off data wrapping in a column and
how to set the column width for a particular column. The UNITS in this example are set to
inches (the default).

DEFINE FILE GGSALES
PROFIT/D14.3 = BUDDOLLARS-DOLLARS;
DESCRIPTION/A80 = 'Subtract Total Sales Quota from Reported Sales to
calculate profit.';
END

TABLE FILE GGSALES
SUM
DESCRIPTION AS 'DEFAULT'
DESCRIPTION AS 'WRAP = 2'
DESCRIPTION AS 'WRAP = OFF'
DESCRIPTION AS 'SQUEEZE = 1.5'
PROFIT
BY REGION NOPRINT
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET STYLE *
TYPE=REPORT, COLUMN=DESCRIPTION(2), WRAP=2,$
TYPE=REPORT, COLUMN=DESCRIPTION(3), WRAP=OFF,$
TYPE=REPORT, COLUMN=DESCRIPTION(4), SQUEEZE=1.5,$
END

678

9. Choosing a Display Format

where:

1. The column titled "DEFAULT" illustrates the default column width and wrapping behavior.

2. The column titled "WRAP=2" sets the column width to 2 inches with data wrapping on.

3. The column titled "WRAP=OFF" turns off data wrapping for that column.

4. The column titled "SQUEEZE=1.5" sets the column width to 1.5 inches with data wrapping

off.

Since the output spans two pages, the output is shown below in two separate images.

The following XLSX output displays the different behavior for the "DEFAULT" and "WRAP=2"
columns.

The following XLSX output displays the output for the "WRAP=OFF" and "SQUEEZE=1.5"
columns.

Creating Reports With TIBCO® WebFOCUS Language

 679

Saving Report Output in Excel XLSX Format

Synchronizing WebFOCUS Page Breaks With Excel Page Breaks

When using the BY_field PAGE-BREAK phrase, WebFOCUS page breaks are automatically
synchronized with Microsoft Excel page breaks.

Example:

Synchronizing WebFOCUS Page Breaks With Excel Page Breaks in Format XLSX Report
Output

The following request generates format XLSX report output with WebFOCUS page breaks that
are inserted using the BY REGION PAGE-BREAK phrase.

TABLE FILE GGSALES
HEADING
"Sales Report by Region"
" "
SUM UNITS BUDUNITS DOLLARS BUDDOLLARS
BY REGION PAGE-BREAK
BY DATE
BY CATEGORY
WHERE CITY LE 'Memphis'
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET STYLE *
TOPMARGIN=1.25, BOTTOMMARGIN=1, $
TYPE=REPORT, FONT=ARIAL, SIZE=9, $
TYPE=TITLE, STYLE=BOLD, SIZE=10, $
TYPE=HEADING, STYLE=BOLD, SIZE=12, $
ENDSTYLE
END

680

9. Choosing a Display Format

Using Print Preview in Excel, output for pages 1 and 2 for the Midwest Region are shown in the
following images. The default Excel page breaks are synchronized with the page breaks
specified in the WebFOCUS request. The page heading and column titles are displayed only
when the BY value changes.

Page 1 Output

Creating Reports With TIBCO® WebFOCUS Language

 681

Saving Report Output in Excel XLSX Format

Page 2 Output

682

9. Choosing a Display Format

To repeat the page heading and column titles on each printed page, use the BY_field PAGE-
BREAK phrase in combination with the XLSXPAGETITLES=ON StyleSheet attribute, as shown in
the following procedure.

Note: You can also use XLSXPAGETITLES as a SET command.

TABLE FILE GGSALES
HEADING
"Sales Report by Region"
" "
SUM UNITS BUDUNITS DOLLARS BUDDOLLARS
BY REGION PAGE-BREAK
BY DATE
BY CATEGORY
WHERE CITY LE 'Memphis'
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET STYLE *
XLSXPAGETITLES=ON,
TOPMARGIN=1.25, BOTTOMMARGIN=1, $
TYPE=REPORT, FONT=ARIAL, SIZE=9, $
TYPE=TITLE, STYLE=BOLD, SIZE=10, $
TYPE=HEADING, STYLE=BOLD, SIZE=12, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 683

Saving Report Output in Excel XLSX Format

Using Print Preview in Excel, output for pages 1 and 2 for the Midwest Region are shown in the
following images. Notice that the page heading and column titles are repeated on each printed
page.

Page 1 Output

684

Page 2 Output

9. Choosing a Display Format

Note: If your report contains OVER or ACROSS phrases, use the BY_field PAGE-BREAK phrase
in combination with the XLSXPAGETITLES=ALL StyleSheet or SET command.

Creating Reports With TIBCO® WebFOCUS Language

 685

Saving Report Output in Excel XLSX Format

Preserving Leading and Internal Blanks in Report Output

The SHOWBLANKS command allows you to preserve leading blanks in data cells and headings
in XLSX reports. In XLSX, internal blanks will always be retained, but leading and trailing blanks
in data fields are removed. You can use the SHOWBLANKS command to retain leading and
trailing blanks.

Since XLSX is not HTML-based like EXL2K, setting SHOWBLANKS OFF will not affect internal
blanks. By default, EXL2K reduces all embedded blanks to a single blank, while XLSX
preserves all embedded blanks. This difference in spacing may cause additional differences in
how fields wrap within a cell.

SET SHOWBLANKS

XLSX (not HTML-based)

EXL2K (HTML-based)

SET SHOWBLANKS = ON

Leading and embedded
blanks are preserved.

Leading and embedded blanks are
preserved.

SET SHOWBLANKS =
OFF

Leading blanks are
removed, but embedded
blanks are respected.

Leading and embedded blanks are
removed.

Blanks are handled differently in headings:

By default, in standard headings containing multiple items (without HEADALIGN=BODY),
items are concatenated together into a single text object. All blanks are retained.

Fields placed in headings with HEADALIGN=BODY behave the same way as data elements.

Variables placed in headings with HEADALIGN=BODY respect all leading, embedded blanks,
and trailing blanks. With SHOWBLANKS=OFF, only embedded blanks are retained. With
SHOWBLANKS=ON all leading, embedded, and trailing blanks are retained.

Syntax:

How to Preserve Leading and Internal Blanks in XLSX Reports

In a FOCEXEC or in a profile, use the following syntax:

SET SHOWBLANKS = {OFF|ON}

In a request, use the following syntax

ON TABLE SET SHOWBLANKS {OFF|ON}

686

9. Choosing a Display Format

where:

OFF

Removes leading blanks and preserves internal blanks in XLSX report output. OFF is the
default value.

ON

Preserves leading and internal blanks in XLSX report output. Also preserves trailing blanks
in heading, subheading, footing, subfooting lines that use the default heading or footing
alignment.

Example:

Preserving Leading and Internal Blanks in XLSX Report Output

The following request creates a variable called SHOWVAR that contains leading, internal, and
trailing blanks.

SET SHOWBLANKS = OFF

-SET &SHOWVAR= '  AB  C  ';
DEFINE FILE CAR
SHOWFIELD/A9 = '  AB  C  ';
END

TABLE FILE CAR
ON TABLE SUBHEAD
"SHOWBLANKS OFF"
"/&SHOWVAR/"
""
HEADING
"In Heading:"
"SHOWVAR<+0>&SHOWVAR"
"SHOWFIELD<+0><SHOWFIELD"
""
"In DATA":
PRINT SHOWFIELD
BY COUNTRY
WHERE RECORDLIMIT EQ 1;
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET STYLE *
HEADALIGN=BODY,SQUEEZE=ON,$
TYPE=TABHEADING,COLSPAN=2,$
END

The following outputs show the differences in XLSX generated using SET SHOWBLANKS = OFF
and SET SHOWBLANKS = ON.

Creating Reports With TIBCO® WebFOCUS Language

 687

Saving Report Output in Excel XLSX Format

SET SHOWBLANKS = OFF with HEADALIGN=BODY (no leading blanks or trailing blanks)

SET SHOWBLANKS = OFF without HEADALIGN=BODY (preserved blanks and concatenated
heading items)

688

SET SHOWBLANKS = ON with HEADALIGN=BODY (leading blanks and trailing blanks)

9. Choosing a Display Format

SET SHOWBLANKS = ON without HEADALIGN=BODY (preserved blanks and concatenated
heading items)

Creating Reports With TIBCO® WebFOCUS Language

 689

Saving Report Output in Excel XLSX Format

Support for Drill Downs With XLSX Report Output

Drill downs are supported within the data elements in a report in XLSX format in the same
manner as they are supported in EXL2K format. Hyperlink connections can be defined in the
StyleSheet declaration of any data column to provide access to any external web source or to
execute a FOCEXEC. Drill downs to FOCEXECs can contain data-driven parameters and can
generate any of the supported output formats, including XLSX, PDF, HTML, DHTML, and PPT.

Drill downs within text embedded in headings, subheadings, subfootings, and footings will be
implemented for XLSX format in a future release.

Note:

When the limit of 65530 hyperlinks for a worksheet is reached, a warning message
displays and no further links can be inserted. For more information on drill downs, see
Linking Using StyleSheets on page 819.

The JAVASCRIPT and IMAGE drill-down options are not supported with FORMAT XLSX.

Redirection and Excel Drill-Down Reports

The WebFOCUS Client can use redirection when passing the report output to the client
application. When redirection is enabled, the WebFOCUS Client saves report output in a
temporary directory when a request is executed. Then, an HTTP call is made from the browser
to retrieve the temporary stored output for display. When redirection is disabled, the report
output is sent directly to the browser without any buffering.

Redirection is disabled by default for the .xlsx file extension because this enables drill downs
to run successfully whether the user machine is configured to launch Excel in the browser or
as an application outside of the browser.

When redirection is enabled, drill downs within Excel reports will work differently depending on
whether the workbook is opened in the browser (only applies to Windows XP) or in the Excel
application. For information about launching Excel in the browser or as an application, see
Viewing Excel Workbooks in the Browser vs. the Excel Application on page 650.

For workbooks opened outside the browser in the Excel application: The current security
context and any previously established session-related cookies are not retained, changing
the user authorization, so drill-down reports will not have the information required to access
the redirected files. The initial workbook will open within Excel, but the target drill-down
workbook will not open and you will receive a message stating You are not allowed to
access this viewer file. The drill-down feature in Microsoft Office products functioned in
WebFOCUS Release 7.7.x because anonymous drill-down access was permitted.

690

9. Choosing a Display Format

The following options are available to allow the feature in WebFOCUS Release 8.x:

Configure WebFOCUS authentication to allow anonymous access. For more information,
see the WebFOCUS Security and Administration manual.

Use SSO with IIS/Tomcat Integrated Windows Authentication. Renegotiation occurs
automatically and the Excel and PowerPoint reports display correctly.

As of WebFOCUS Release 8.x, the Remember Me feature can be enabled on the Sign-in
page. If the end user uses the Remember Me feature, a persistent cookie is used.

For more information on how Microsoft Office products work with session related
information, see the Microsoft Office support site at http://support.microsoft.com/kb/
218153.

For workbooks opened in the browser (only applies to Windows XP): Drill downs will work
with redirection enabled because the browser session has access to the HTTP header
and/or cookies that need to be sent with the HTTP request to the WebFOCUS Client in
order to obtain the redirected target workbook file.

Note: For Windows 7, Excel applications no longer display in a browser window.

For additional information about redirection options, see WebFOCUS Administration Console
Client Settings described in the WebFOCUS Security and Administration manual.

Excel Page Settings

Excel page settings for the XLSX workbook default to the WebFOCUS standards:

Orientation: Portrait

Page Size: Letter

,75 inches (Excel default)

.75 inches (Excel default)

To customize these page settings, turn the XLSXPAGESETS attribute ON and define individual
attributes.

If XLSXPAGESETS is turned on, but the page margin attributes are not defined within the
procedure, the values will be set to the WebFOCUS default of .25 inches.

Syntax:

How to Define Excel Page Settings

[TYPE=REPORT,] XLSXPAGESETS={ON|OFF} [,PAGESIZE={pagesize|LETTER}]
 [,ORIENTATION={PORTRAIT|LANDSCAPE}] [,TOPMARGIN=n] [,BOTTOMMARGIN=m],$

Creating Reports With TIBCO® WebFOCUS Language

 691

Saving Report Output in Excel XLSX Format

where:

XLSPAGESETS={ON|OFF}

ON causes the page settings defined in the WebFOCUS request to be applied to the Excel
worksheet page settings. OFF retains the default page settings defined in the standard
Excel workbook. OFF is the default value.

Defines the top margin for the worksheet in the units identified by the UNITS parameter
(inches, by default). The default value is .25.

n

m

Defines the bottom margin for the worksheet in the units identified by the UNITS
parameter (inches, by default). The default value is .25.

pagesize

Is one of the PAGESIZE values supported in a WebFOCUS StyleSheet. LETTER is the
default page size.

PORTRAIT|LANDSCAPE

PORTRAIT displays the report across the narrower dimension of a vertical page, producing
a page that is longer than it is wide. PORTRAIT is the default value.

LANDSCAPE displays the report across the wider dimension of a horizontal page, producing
a page that is wider than it is long.

Adding an Image to a Report

WebFOCUS supports the placement of images within each area or node of the report on the
worksheet. An image, such as a logo, gives corporate identity to a report, or provides visual
appeal. Data specific images can be placed in headers, footers, and data columns to provide
additional clarity and style.

The image must reside on the WebFOCUS Reporting Server in a directory named on EDAPATH
or APPPATH. If the file is not on the search path, supply the full path name.

Inserting Images Into Excel XLSX Reports

Images can be placed in any available WebFOCUS reporting node or element of a worksheet.
Supported image formats include .gif and .jpg.

692

9. Choosing a Display Format

Usage Considerations

All images will be placed in the top-left corner of the first cell of the defined area, based on
the top and left gap. Defined explicit positioning and justification have not been
implemented yet.

Standard page setting keywords can be used in conjunction with XLSXPAGESETS to control
the page layout in standard reports (not compound).

Images placed within a report cell in a row or column is anchored to the top-left corner of
the cell. The cell is automatically sized to the height and width to fit the largest image
(SQUEEZE=ON).

Additional lines may need to be added within a heading, footing, subhead, or subfoot to
accommodate the placement of the image.

Syntax:

How to Insert Images Into WebFOCUS Report Elements in XLSX Reports

TYPE={REPORT|heading|data}, IMAGE={url|file|(column)} [,BY=byfield]
[,SIZE=(w h)] ,$

where:

REPORT

Embeds an image in the body of a report. The image appears in the background of the
report. REPORT is the default value.

heading

Embeds an image in a heading or footing. Valid values are TABHEADING, TABFOOTING,
FOOTING, HEADING, SUBHEAD, and SUBFOOT. Provide sufficient blank space in the
heading or footing so that the image does not overlap the heading or footing text. You may
also want to place heading or footing text to the right of the image using spot markers.

data

Defines a cell within a data column to place the image. Must be used with COLUMNS=
attributes to identify the specific report column where the image should be anchored.

url

Is the URL of the image file.

Creating Reports With TIBCO® WebFOCUS Language

 693

Saving Report Output in Excel XLSX Format

file

Is the name of the image file. It must reside on the WebFOCUS Reporting Server in a
directory named on EDAPATH or APPPATH. If the file is not on the search path, supply the
full path name. When specifying a GIF file, you can omit the file extension.

column

Is an alphanumeric field in the data source that contains the name of an image file.
Enclose the column in parentheses ( ). The field containing the file name or image must be
a display field or BY field referenced in the request. Note that the value of the field is
interpreted exactly as if it were typed as the URL of the image in the StyleSheet. If you
omit the suffix, .GIF is supplied, by default. You can use the SET BASEURL command for
supplying the base URL of the images. This way, the value of the field does not have to
include the complete URL. This syntax is useful, for example, if you want to embed an
image in a SUBHEAD, and you want a different image for each value of the BY field on
which the SUBHEAD occurs.

byfield

Is the sort field that generates the subhead or subfoot.

SIZE

Is the size of the image. By default, an image is added at its original size.

w

h

Is the width of the image, expressed in the unit of measurement specified by the UNITS
parameter. Enclose the w and h values in parentheses. Do not include a comma between
them.

Is the height of the image, expressed in the unit of measurement specified by the UNITS
parameter.

Example:

Adding a GIF Image to a Single Table Request

DEFINE FILE GGSALES
SHOWCAT/A100=CATEGORY || '.GIF';
END
TABLE FILE GGSALES
SUM DOLLARS/D12CM UNITS/D12C
BY LOWEST CATEGORY NOPRINT
BY SHOWCAT NOPRINT
BY PRODUCT
ACROSS REGION
WHERE CATEGORY NE 'Gifts'

694

9. Choosing a Display Format

ON CATEGORY SUBHEAD
" "
“Image in SUBHEAD for Category <CATEGORY "
" "
ON TABLE SUBHEAD
" "
" "
" Report Heading "
" "
ON CATEGORY SUBFOOT
"ON CATEGORY SUBFOOT"

ON TABLE SUBFOOT
"Report Footing"
" "
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE NOTOTAL
ON TABLE SET ACROSSTITLE SIDE
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, FONT='ARIAL', SIZE=9, TITLETEXT='Food and Coffee',$
TYPE=REPORT, COLUMN=PRODUCT, SQUEEZE=1,$
TYPE=TITLE, BACKCOLOR=RGB(90 90 90), COLOR=RGB(255 255 255), STYLE=BOLD,$
TYPE=ACROSSTITLE, STYLE=BOLD, BACKCOLOR=RGB(90 90 90),
COLOR=RGB(255 255 255),$
TYPE=ACROSSVALUE, BACKCOLOR=RGB(218 225 232), STYLE=BOLD, JUSTIFY=CENTER,$
TYPE=HEADING, STYLE=BOLD, COLOR=RGB(0 35 95), SIZE=12, JUSTIFY=Center,$
TYPE=FOOTING, BACKCOLOR=RGB(90 90 90), SIZE=12, COLOR=RGB(255 255 255),
STYLE=BOLD, JUSTIFY=CENTER,$
TYPE=SUBHEAD, SIZE=12, STYLE=BOLD, BACKCOLOR=RGB(218 225 232),
JUSTIFY=CENTER,$
TYPE=SUBHEAD, IMAGE=(SHOWCAT), SIZE=(.6 .6),$
TYPE=SUBFOOT, SIZE=10, STYLE=BOLD, JUSTIFY=CENTER,$
TYPE=TABHEADING, SIZE=12, STYLE=BOLD, JUSTIFY=CENTER,$
TYPE=TABHEADING, IMAGE=gglogo.gif,$
TYPE=TABFOOTING, SIZE=12, STYLE=BOLD, JUSTIFY=RIGHT,$
TYPE=TABFOOTING, IMAGE=logo.gif, SIZE=(1.67 .6),$
END

Creating Reports With TIBCO® WebFOCUS Language

 695

Saving Report Output in Excel XLSX Format

In the following request, since the referenced images are not part of the existing GGSALES
table, the image files (.gif) are being built in the DEFINE and then referenced in the TABLE
request. You can NOPRINT fields if you do not want them to display as columns, but the fields
must be referenced in the table to include them in the internal matrix. This will allow the
images to be placed in the headings, footings, or data cells. The specific location is defined
using StyleSheet definitions for attaching the image based on field value.

Example:

Adding a GIF Image to a Compound Request

Note: Compound Layout syntax cannot contain hidden carriage return or line feed characters.
For purposes of presenting this example, line feed characters have been added so that the
sample code wraps to fit within the printed page. To run this example in your environment,
copy the code into a text editor and delete any line feed characters within the Compound
Layout syntax by going to the end of each line and pressing Delete. In some instances, you
may need to add a space to maintain the structure of the string.

696

9. Choosing a Display Format

APP PATH IBISAMP
SET HTMLARCHIVE=ON
*-HOLD_SOURCE
COMPOUND LAYOUT PCHOLD FORMAT XLSX
UNITS=IN,$
SECTION=section1, LAYOUT=ON, METADATA='prop_with_names, Margins_Left=0.5,
Margins_Top=0.5, Margins_Right=0.5, Margins_Bottom=0.5,
thumbnailscale=4', MERGE=OFF, ORIENTATION=LANDSCAPE, PAGESIZE=Legal,
SHOW_GLOBALFILTER=OFF,$
PAGELAYOUT=1, NAME='Page layout 1', text='Page layout 1', TOC-LEVEL=1,
BOTTOMMARGIN=0.5, TOPMARGIN=0.5, METADATA='BOTTOMMARGIN=0.5, TOPMARGIN=0.5,
LEFTMARGIN=0,RIGHTMARGIN=0,',$
COMPONENT='report1', TEXT='report1', TOC-LEVEL=2, POSITION=(0.650 0.917),
DIMENSION=(7.250 3.000), BYTOC=0,  ARREPORTSIZE=DIMENSION,
METADATA='left: 0.65in; top: 0.917in; width: 7.25in; height: 3in;
position: absolute; z-index: 1;',$
COMPONENT='chart1', TEXT='chart1', TOC-LEVEL=2, POSITION=(0.735 4.332),
DIMENSION=(7.167 2.917), COMPONENT-TYPE=GRAPH,  ARREPORTSIZE=DIMENSION,
METADATA='left: 0.735in; top: 4.332in; width: 7.167in; height: 2.917in;
position: absolute; z-index: 2;',$
END

SET COMPONENT='report1'
-*component_type report
DEFINE FILE GGSALES
SHOWCAT/A100=CATEGORY || '.GIF';
SHOWDATEQ/Q=DATE;
SHOWDATEY/YY=DATE;
SHOWDATEQY/YYQ=DATE;
END

Creating Reports With TIBCO® WebFOCUS Language

 697

Saving Report Output in Excel XLSX Format

TABLE FILE GGSALES
SUM DOLLARS/D12CM AS 'Dollars'
BY REGION AS ''
BY LOWEST CATEGORY
BY SHOWCAT AS 'Data Image'
ACROSS SHOWDATEY AS ''
ACROSS SHOWDATEQ AS ''
WHERE REGION NE 'Midwest' OR 'West'
ON TABLE SET HIDENULLACRS ON
HEADING
" "
"Image in Page Heading "
ON REGION SUBHEAD
" <+0> SUBHEAD: <REGION"
FOOTING
" "
"Image in Page Footing"
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET STYLE *
TYPE=REPORT, SIZE=10, BACKCOLOR=NONE, GRID=OFF, FONT='ARIAL',
XLSXPAGESETS=ON, TOPMARGIN=1, BOTTOMMARGIN=1, ORIENTATION=LANDSCAPE,
PAGESIZE=LEGAL, TITLETEXT='With Images',$
TYPE=REPORT, COLUMN=REGION, SQUEEZE=1.5, JUSTIFY=CENTER,$
TYPE=DATA, BACKCOLOR=NONE,$
TYPE=DATA, COLUMN=SHOWCAT, IMAGE=(SHOWCAT), SIZE=(.5 .5),$
TYPE=TITLE, BACKCOLOR=RGB(218 225 232), BORDER=LIGHT,
STYLE=-UNDERLINE+BOLD,$
TYPE=HEADING, IMAGE=GGLOGO.GIF, SIZE=(.65 .65),$
TYPE=HEADING, SIZE=12, STYLE=BOLD, JUSTIFY=CENTER,$
TYPE=SUBHEAD, SIZE=10, STYLE=BOLD, BORDER-TOP=LIGHT,$
TYPE=SUBHEAD, BY=1, JUSTIFY=CENTER, BORDER-TOP=LIGHT,$
TYPE=SUBFOOT, STYLE=BOLD,$
TYPE=FOOTING, SIZE=12, STYLE=+BOLD, JUSTIFY=CENTER,$
TYPE=FOOTING, IMAGE=logo.gif, SIZE=(1.67 .6),$
TYPE=ACROSS, JUSTIFY=CENTER, BORDER=LIGHT,$
TYPE=ACROSSTITLE, STYLE=-UNDERLINE+BOLD,$
TYPE=ACROSSVALUE, BACKCOLOR=RGB(218 225 232), STYLE=-UNDERLINE+BOLD,$
END

698

9. Choosing a Display Format

SET COMPONENT='chart1'
ENGINE INT CACHE SET ON
-DEFAULTH &WF_STYLE_UNITS='PIXELS';
-DEFAULTH &WF_STYLE_HEIGHT='1005.0';
-DEFAULTH &WF_STYLE_WIDTH='1070.0';
-DEFAULTH &WF_TITLE='WebFOCUS Report';
GRAPH FILE GGSALES
HEADING
"Sales Graph"
SUM
GGSALES.SALES01.DOLLARS
BY SHOWDATEY AS Year
BY GGSALES.SALES01.REGION
ON GRAPH PCHOLD FORMAT XLSX
ON GRAPH SET VZERO OFF
ON GRAPH SET HTMLENCODE ON
ON GRAPH SET GRAPHDEFAULT OFF
ON GRAPH SET GRWIDTH 1
ON GRAPH SET UNITS &WF_STYLE_UNITS
ON GRAPH SET HAXIS 1000
ON GRAPH SET VAXIS 1000
ON GRAPH SET GRMERGE ADVANCED
ON GRAPH SET GRLEGEND 0
ON GRAPH SET GRXAXIS 2
ON GRAPH SET LOOKGRAPH HBAR
ON GRAPH SET STYLE *

*GRAPH_SCRIPT
setPieDepth(0);
setPieTilt(0);
setDepthRadius(0);
setCurveFitEquationDisplay(false);
setPlace(true);
setPieFeelerTextDisplay(1);
setUseSeriesShapes(true);
setMarkerSizeDefault(50);
setScaleMustIncludeZero(getX1Axis(), false);
setScaleMustIncludeZero(getY1Axis(), false);
setScaleMustIncludeZero(getY2Axis(), false);
setMarkerSizeDefault(60);
*END
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/javaassist/intl/EN/
ENIADefault_combine.sty,$
TYPE=REPORT, TITLETEXT='Graph Over Time',$
*GRAPH_SCRIPT
setReportParsingErrors(false);
setSelectionEnableMove(false);
*END
ENDSTYLE
END
COMPOUND END

Creating Reports With TIBCO® WebFOCUS Language

 699

Saving Report Output in Excel XLSX Format

The output is shown in the following images.

700

9. Choosing a Display Format

Example:

Adding a GIF Image to a BYTOC Compound Request

The following syntax is a portion of the code from the previous example to show the
COMPOUND BYTOC syntax. By adding the ON TABLE SET COMPOUND BYTOC command to the
compound report above, you can turn the report into a Compound Table of Contents report.
The BYTOC syntax can be added to a stand-alone request or to a component of a compound
document.

TABLE FILE GGSALES
SUM DOLLARS/D12CM AS 'Dollars'
SHOWREG
NOPRINT
BY REGION AS ''
BY LOWEST CATEGORY
BY SHOWCAT AS 'Data Image'
WHERE REGION NE 'Midwest' OR 'West'
ACROSS SHOWDATEY AS '' ACROSS SHOWDATEQ AS ''
ON TABLE SET HIDENULLACRS ON
HEADING
"Image in Page Heading"
ON REGION SUBHEAD
"<+0> Image in SUBHEAD:<REGION"
FOOTING
" "
"Image in Page Footing"
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET COMPOUND BYTOC
ON TABLE SET STYLE *

Creating Reports With TIBCO® WebFOCUS Language

 701

Saving Report Output in Excel XLSX Format

The output is:

Inserting Text and Images Into XLSX Workbook Headers and Footers

WebFOCUS supports the insertion of text and images into Excel headers and footers and the
definition of key page settings to support the placement of text and images in relationship to
the overall worksheet and the Excel generated page breaks. This access to the Excel page
functionality is designed to enhance overall usability of the worksheets for users who will be
printing these reports. Page settings including orientation, page size, and page margins will
directly affect the layout of each Excel page based on values defined within the FOCEXEC.
Images and text can be included on headers and footers on every printed page, on the first
page of the report only, or only on all subsequent pages. The WebFOCUS headings and
footings continue to display within the worksheet. With this feature, WebFOCUS can insert
logos to be printed once at the top of a report and watermark images that need to be
displayed on every printed page.

Syntax:

How to Insert Text and Images Into XLSX Workbook Headers and Footers

To place images in XLSX Workbook headers and footers, the syntax is:

TYPE={PAGEHEADER|PAGEFOOTER},OBJECT=IMAGE,
 IMAGE=imagename, JUSTIFY={LEFT|CENTER|RIGHT}
 [,DISPLAYON={FIRST|NOT-FIRST}] [,SIZE=(w h)],$

702

9. Choosing a Display Format

To place text in XLSX Workbook headers and footers, the syntax is:

TYPE={PAGEHEADER|PAGEFOOTER},OBJECT=STRING,
 TEXT=text, JUSTIFY={LEFT|CENTER|RIGHT}
 [,DISPLAYON={FIRST|NOT-FIRST}] ,$

where:

PAGEHEADER

Places the text or image in the worksheet header.

PAGEFOOTER

Places the text or image in the worksheet footer.

imagename

Is the name of a valid image file to be placed in the header or footer. The image must be
located in the defined application path on the Reporting Server. The image types supported
are GIF and JPEG.

text

Is the text to be placed in the header or footer.

JUSTIFY={LEFT|CENTER|RIGHT}

Identifies the area in the header or footer to contain the text or image and the justification
or placement within that defined area.

DISPLAYON

Defines whether the text or image should be placed on the first page only or on all pages
except the first. Omit this attribute to place the text or image on all pages.

Valid values are:

FIRST places the text or image only on the first page.

NOT-FIRST places the text or image on every page, except the first page.

SIZE=(w h)

Is the size of the image. By default, an image is added at its original size.

w is the width of the image, expressed in the unit of measurement specified by the UNITS
parameter.

h is the height of the image, expressed in the unit of measurement specified by the UNITS
parameter.

Creating Reports With TIBCO® WebFOCUS Language

 703

Saving Report Output in Excel XLSX Format

Example:

Inserting Images in Excel Headers and Footers and Defining Page Settings

The following request against the GGSALES data source places the image ibi_logo.gif on the
left header area of the first page and the right header area of every subsequent page of the
resulting worksheet. It places the image webfocus1.gif in the center area of the footer on every
page.

TABLE FILE GGSALES
SUM DOLLARS UNITS BUDDOLLARS BUDUNITS
BY REGION
BY ST
BY CATEGORY
BY PRODUCT
ON TABLE SET BYDISPLAY ON
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET STYLE *
FONT=ARIAL,SIZE=12,
XLSXPAGESETS=ON,TOPMARGIN=1,BOTTOMMARGIN=1,ORIENTATION=LANDSCAPE,
PAGESIZE=LETTER,$
TYPE=TITLE, COLOR=WHITE, BACKCOLOR=GREY,$
TYPE=PAGEHEADER, OBJECT=IMAGE, JUSTIFY=LEFT, IMAGE=IBI_LOGO.GIF,
DISPLAYON=FIRST,$
TYPE=PAGEHEADER, OBJECT=IMAGE, JUSTIFY=RIGHT, IMAGE=IBI_LOGO.GIF,
DISPLAYON=NOT-FIRST,$
TYPE=PAGEFOOTER, OBJECT=IMAGE, JUSTIFY=CENTER, IMAGE=WEBFOCUS1.GIF,$
END

704

The first page of output has the image ibilogo.gif in the left area of the header and the image
webfocus1.gif in the center area of the footer.

9. Choosing a Display Format

Creating Reports With TIBCO® WebFOCUS Language

 705

Saving Report Output in Excel XLSX Format

The second page of output has the image ibilogo.gif in the right area of the header and the
image webfocus1.gif in the center area of the footer.

Reference: Usage Notes for Inserting Text and Images Into XLSX Worksheet Headers and Footers

In Microsoft Excel, the maximum number of characters in a page header or page footer is
255. This limit is for the entire page header or page footer (across the left, center, and
right), and includes symbols or any other characters that Microsoft Excel needs to use, in
addition to the text string itself. Any text string that exceeds this limit will be truncated.

The Excel headers and footers are not automatically sized based on contents of the areas.
Define page margins within the page settings (XLSPAGESETS) to account for the space
required to display the images within each page of the report.

The image sizing based on the specified height and width is not proportional. Sizing may
cause image distortion.

BLOB image fields are not supported in this release.

706

Reference: Displaying Watermarks on XLSX Report Output

9. Choosing a Display Format

Watermark images can be placed into the Excel headers to display on every printed page of the
generated worksheet.

Excel places images on the page starting in the header from left to right and then the footer
from left to right. Large images placed in the header may overlap images before them in the
presentation order. For page layouts with a logo in the left area and watermark centered on the
page, watermark image background must be transparent so it does not overlay the logo image.

In Excel, images are placed first on the page. All other contents of the worksheet are then
placed on top of the images. Text in cells and styling, such as background color and drawing
objects, are placed on top of the images. Excel supports transparency in drawing objects and
images, but not in cell background color. BACKCOLOR will cover over images placed on the
page.

Example:

Placing a Watermark in an XLSX Header

The following request against the GGSALES data source uses the image internaluseonly.gif as
a watermark to display in the background of every page of the worksheet. Although the image
is placed in the center area of the header, it is large enough to span the entire worksheet
page. It has a transparent background, so it does not cover the logo images placed at the left
in the header and the center in the footer.

TABLE FILE GGSALES
SUM DOLLARS UNITS BUDDOLLARS BUDUNITS
BY REGION
BY ST
BY CATEGORY
BY PRODUCT
ON TABLE SET BYDISPLAY ON
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET STYLE *
XLSXPAGESETS=ON,
TOPMARGIN=1,BOTTOMMARGIN=1,LEFTMARGIN=1, RIGHTMARGIN=1,
ORIENTATION=LANDSCAPE,PAGESIZE=LETTER,$
TYPE=PAGEHEADER, OBJECT=IMAGE, JUSTIFY=LEFT, IMAGE=IBI_LOGO.GIF,
DISPLAYON=FIRST,$
TYPE=PAGEHEADER, OBJECT=IMAGE, JUSTIFY=CENTER, IMAGE=WFINTERNALUSEONLY.GIF,$
TYPE=PAGEFOOTER, OBJECT=IMAGE, JUSTIFY=RIGHT, IMAGE=WEBFOCUS1.GIF,$
END

Creating Reports With TIBCO® WebFOCUS Language

 707

Saving Report Output in Excel XLSX Format

The first page of the generated worksheet shows the watermark image beneath the data. This
image is displayed on every page of the worksheet.

Creating Excel XLSX Worksheets Using Templates

XLSX report output can be generated based on Excel templates. This feature allows for the
integration of WebFOCUS reports into workbooks containing multiple worksheets. Any native
Excel template can be used to generate a new workbook containing a WebFOCUS report.

The following Excel file types can be used as template files to generate XLSX workbooks.

Template File Type

Output Workbook Generated

Template (.xltx)

Workbook (.xlsx)

708

9. Choosing a Display Format

Template File Type

Output Workbook Generated

Macro-Enabled Template (.xltm)

Macro-Enabled workbook (.xlsm)

Workbook (.xlsx)

Workbook (.xlsx)

Macro-Enabled workbook (.xlsm)

Macro-Enabled workbook (.xlsm)

WebFOCUS XLSX TEMPLATE format provides support for basic Excel templates (.xltx) files.
These templates cannot contain macros or other content that Microsoft considers active, as
well as templates with active content (XLTM/XLSM). Additionally, macro-enabled templates
(.xltm) allow for the inclusion of active content (macros and VB script) into templates.

A WebFOCUS EXL07 template procedure generates a native Excel workbook with the standard
Excel extension, based on the defined template file. The WebFOCUS request will replace an
existing worksheet within the template workbook, and any formulas or references defined in
other worksheets to cells within the replaced worksheet will automatically update when the
workbook is opened.

Since the template feature replaces existing worksheets, the designated worksheet must exist
in the template workbook. Any content on the replaced worksheet within the template will not
be retained. Content contained on any other worksheets will be retained and updated.

Named ranges can be defined within the procedure using the INRANGES attribute to designate
cell groupings that can be referenced by other worksheets.

An Excel 2007/2010 template can be generated by saving any workbook with the .xltx
extension. The template file should be stored within your application path (EDAPATH or APP
PATH) rather than the default Excel template directory so that it can be accessed by the
Reporting Server when the procedure is executed.

The EXL07 TEMPLATE feature is supported for basic EXL07 format reports. The following
features are not supported with EXL07 TEMPLATE in this release: FORMULA, EXL97, EXCEL,
and compound Excel reports.

In most cases, existing Excel 2003/2000 templates created as .mht files can easily be
converted to Excel 2013/2010/2007 templates by opening the .mht file in Excel
2013/2010/2007 and resaving the file as either an Excel template (.xltx) or a macro enabled
(.xltm) file. Native Excel formulas and functionality should be retained within these templates.
Use .xltms to retain active content, including macros. This new XLTX template can be used
with XLSX procedures.

Creating Reports With TIBCO® WebFOCUS Language

 709

Saving Report Output in Excel XLSX Format

Syntax:

How to Create an XLSX Report Using Any Supported Template File Type

To support the expanded template files types, the template file name attribute has been
enhanced to allow for the inclusion of the file extension. If no extension is specified within the
template name, the file extension will default to .XLTX.

ON TABLE PCHOLD FORMAT XLSX TEMPLATE template_name SHEETNUMBER n

where:

template_name

Is the name of the Excel template file (workbook), up to 64 characters including the file
name and extension, residing on the WebFOCUS Reporting Server application directory
search path. For example, IPOLICY.XLTX, PRINTSHEETS.XLTM, or DASHBOARD.XLSM. If the
extension is not provided, it defaults to .XLTX.

n

Is the number of the existing Excel worksheet being replaced in the template file
(workbook).

Reference: Usage Notes for XLSX Templates

The workbook template used by the WebFOCUS procedure must contain valid worksheets.

The worksheet that is updated must exist in the workbook, as WebFOCUS is replacing the
worksheet rather than inserting a worksheet. If the sheet designated does not exist, the
procedure will return an error.

In any template file, at least one of the sheets in the workbook must contain a cell with a
valid value (blank or any other value). To replace a worksheet in a template that contains
only empty worksheets, replace one of the cells in any of the sheets with a space and
save. This will instantiate the worksheets so they are accessible to WebFOCUS for
updating.

The supported file name length has been extended to 64 characters. Any procedure
referencing a template with a longer file name produces a message.

Creating Excel Table of Contents Reports

Excel Table of Contents (BYTOC) enables you to generate a separate worksheet within an
instance of the report for each value of the first BY field in the WebFOCUS report.

710

9. Choosing a Display Format

Syntax:

How to Use the Excel Table of Contents Feature

There are three different ways that BYTOC can be invoked:

ON TABLE {HOLD|PCHOLD} FORMAT XLSX BYTOC

SET COMPOUND=BYTOC

ON TABLE SET COMPOUND BYTOC

Since a BYTOC report generates separate worksheets according to the value of the first BY
field in the report, the report must contain at least one BY field. The primary BY field may be a
NOPRINT field.

The BYTOC feature is not supported with the XLSX TEMPLATE format.

Example:

Creating a Simple BYTOC Report

The following request against the GGSALES data source creates separate tabs based on the
REGION sort field.

TABLE FILE GGSALES
SUM UNITS/D12C DOLLARS/D12CM
BY REGION NOPRINT
BY CATEGORY
BY PRODUCT
HEADING
"<REGION Region Sales"
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET BYDISPLAY ON
ON TABLE SET COMPOUND BYTOC
ON TABLE SET STYLE *
TYPE=REPORT, FONT=ARIAL, SIZE=9,$
TYPE=HEADING, SIZE=12,$
TYPE=TITLE, BACKCOLOR=GREY, COLOR=WHITE,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 711

Saving Report Output in Excel XLSX Format

The output is:

Reference: How to Name Worksheets

The worksheet tab names are the BY field values that correspond to the data on the
current worksheet. If the user specifies the TITLETEXT keyword in the StyleSheet, it will be
ignored.

Excel limits the length of worksheet titles to 31 characters. The following special characters
cannot be used: ':', '?', '*', and '/'.

If you want to use date fields as the bursting BY field, you can include the - character
instead of the / character. The - character is valid in an Excel tab title. However, if you do
use the / character, WebFOCUS will substitute it with the - character.

Naming XLSX Worksheets With Case Sensitive Data

Excel requires each sheet name to be unique. Excel is case insensitive meaning it evaluates
two values as being the same when the values contain the same characters but have different
casing. For example, Excel evaluates the values WEST and West to be the same value.
WebFOCUS XLSX format identifies duplicate names and adds a unique number to the name to
allow Excel to maintain both sheets.

712

9. Choosing a Display Format

By default, WebFOCUS sort processing is case-sensitive, so the same field value with different
casing is considered to be two different values when used as a sort (BY) field. In an Excel
BYTOC report, WebFOCUS will generate sheets with sheet names for each value of the primary
sort (BY) key based on case sensitivity. To account for this, XLSX has been enhanced to add
counters where duplicate tab names are found in the data to ensure the names are unique.

For example, if the report had EAST and East as the values for the Region, each worksheet
would be displayed as EAST(1) and East(2), as shown in the following image.

Overcoming the Excel 2007/2010 Row Limit Using Overflow Worksheets

The maximum number of rows supported by Excel 2007/2010 on a worksheet is 1,048,576
(1MB). When you create an XLSX output file from a WebFOCUS report, the number of rows
generated can be greater than this maximum.

To avoid creating an incomplete output file, you can have extra rows flow onto a new
worksheet, called an overflow worksheet. The name of each overflow worksheet will be the
name of the original worksheet appended with an increment number.

In addition, when the overflow worksheet feature is enabled, you can set a target value for the
maximum number of rows to be included on a worksheet. By default, the row limit will be set to
the default value for the LINES parameter (57).

Note: By default, when generating XLSX output, the WebFOCUS page heading and page footing
commands generate only worksheet headings and worksheet footings.

Creating Reports With TIBCO® WebFOCUS Language

 713

Saving Report Output in Excel XLSX Format

Syntax:

How to Enable Overflow Worksheets

Add the ROWOVERFLOW attribute to your WebFOCUS StyleSheet

TYPE=REPORT, ROWOVERFLOW={ON|OFF|PBON}, [ROWLIMIT={n|MAX},]$

where:

ON

Enables overflow worksheets.

OFF

Disables overflow worksheets. OFF is the default value.

PBON

Inserts WebFOCUS page breaks that display the page heading, footing, and column titles
at the appropriate places within the worksheet rows. This option does not cause a new
worksheet to start when a WebFOCUS page break occurs.

ROWLIMIT=n

Sets a target value for the number of rows to be included on a worksheet to n rows. The
default value is the LINES value (by default, 57).

ROWLIMIT=MAX

Sets a target value for the number of rows to be included on a worksheet to 1,048,000
rows for XLSX output.

Reference: Usage Notes for XLSX Overflow Worksheets

The report heading is placed once at the start of the first sheet. The report footing is
placed once at the bottom of the last overflow sheet.

Unless the PBON setting is used, worksheet headings and column titles are repeated at
the top of the original sheet and each subsequent overflow sheet. worksheet footings are
placed at the bottom of the original sheet and each subsequent overflow sheet. The data
values are displayed on the top data row of each overflow sheet as they would be on a
standard new page.

Report total lines are displayed at the bottom of the last overflow sheet directly above the
final page and table footings.

Subheadings, subfootings, and subtotal lines display within the data flow as normal. No
special consideration is made to retain groupings within a given sheet.

714

9. Choosing a Display Format

If ROWOVERFLOW=PBON, the page headings and footings and column titles display within
the worksheet when a WebFOCUS command causes a page break.

For XLSX output, if the ROWOVERFLOW attribute is specified in the StyleSheet and
ROWLIMIT is greater than 1MB, the following message is presented and no output file is
generated:

(FOC3338) The row limit for EXCEL XLSX worksheets is 1048576.

Output types that contain formula references (EXL2K PIVOT and EXL2K FORMULA) are not
supported, as formula references are not automatically updated to reflect placement on
new overflow worksheets.

The overflow worksheet feature applies to rows only, not columns. A new worksheet will not
automatically be created if a report generates more than the Excel 2007/2010 limit or
16,384 columns.

ROWOVERFLOW is supported for BYTOC reports for XLSX.

As named ranges in Excel cannot run across multiple worksheets, the IN-RANGES phrase
that defines named ranges in the resulting workbook is not supported with the
ROWOVERFLOW feature. When they exist together in the same request, ROWOVERFLOW
takes precedence and the IN-RANGES phrase is ignored.

Example:

Creating Overflow Worksheets

The following request creates XLSX report output with overflow worksheets. The
ROWOVERFLOW=ON attribute in the StyleSheet activates the overflow feature. Without this
attribute, one worksheet would have been generated instead of three.

TABLE FILE GGSALES
-* ****Report Heading****
ON TABLE SUBHEAD
"SALES BY REGION, CATEGORY, AND PRODUCT"
" "
-* ****Worksheet Heading****
HEADING
"SALES REPORT WORKSHEET <TABPAGENO"
" "
-* ****Worksheet Footing****
FOOTING
" "
"END OF WORKSHEET <TABPAGENO"
PRINT DOLLARS UNITS BUDDOLLARS BUDUNITS
BY REGION
BY CATEGORY
BY PRODUCT
BY DATE

Creating Reports With TIBCO® WebFOCUS Language

 715

Saving Report Output in Excel XLSX Format

-* ****Subfoot****
ON REGION SUBFOOT
" "
" End of Region <REGION"
" "
-* ****Subhead****
ON REGION SUBHESD
" "
"Category <CATEGORY for Region <REGION"
" "
-* ****Report Footing****
ON TABLE SUBFOOT
" "
"END OF REPORT"
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET STYLE *
TYPE=REPORT, TITLETEXT=EXLOVER, ROWOVERFLOW=ON, ROWLIMIT=2000,$
ENDSTYLE
END

The report heading displays on the first worksheet only, the page heading and column titles
display on each worksheet, and the subhead and subfoot display whenever the associated sort
field changes value. The following image shows the top of the first worksheet, displaying the
report heading, page heading, column titles, and first subhead.

716

9. Choosing a Display Format

Note that the TITLETEXT attribute in the StyleSheet specified the name EXLOVER, so the three
worksheets were generated with the names EXLOVER1, EXLOVER2, and EXLOVER3. If there
had been no TITLETEXT attribute, the sheets would have been named SHEET1, SHEET2, and
SHEET3.

The worksheet footing displays at the bottom of each worksheet and the report footing
displays at the bottom of the last worksheet. The following image shows the bottom of the last
worksheet, displaying the last subfoot, the page footing, and the report footing.

Creating Reports With TIBCO® WebFOCUS Language

 717

Saving Report Output in Excel XLSX Format

Example:

Creating Overflow Worksheets With WebFOCUS Page Breaks

The following request creates XLSX report output with overflow worksheets. The
ROWOVERFLOW=PBON attribute in the StyleSheet activates the overflow feature, and the
ROWLIMIT=250 sets the maximum number of rows in each worksheet to approximately 250.
Without this attribute, one worksheet would have been generated. The PRODUCT sort phrase
specifies a page break.

TABLE FILE GGSALES
-* ****Report Heading****
ON TABLE SUBHEAD
"SALES BY REGION, CATEGORY, AND PRODUCT"
" "
PRINT DOLLARS UNITS BUDDOLLARS BUDUNITS
BY REGION
BY HIGHEST CATEGORY
BY PRODUCT PAGE-BREAK
BY DATE
WHERE DATE GE '19971001'
-* ****Page Heading****
HEADING
" Product: <PRODUCT in Category: <CATEGORY for Region: <REGION"
-* ****Page Footing****
FOOTING
" "
-* ****Report Footing****
ON TABLE SUBFOOT
" "
"END OF REPORT"
ON TABLE SET BYDISPLAY ON
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET STYLE *
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/javaassist/intl/EN/
ENIADefault_combine.sty,$
TITLETEXT=EXLOVER, ROWOVERFLOW=PBON, ROWLIMIT=250,
$
ENDSTYLE
END

718

9. Choosing a Display Format

The report heading displays on the first worksheet only, the page heading, footing, and column
titles display on each worksheet and at each WebFOCUS page break (each time the product
changes), and the subhead and subfoot display whenever the associated sort field changes
value. The following image shows the top of the first worksheet.

Excel Compound Reports Using XLSX

Excel compound reports generate compound workbooks that can contain multiple worksheet
reports using the XLSX output format.

Creating Reports With TIBCO® WebFOCUS Language

 719

Saving Report Output in Excel XLSX Format

You can use standard Compound Layout syntax to generate XLSX compound workbooks. By
default, each of the component reports from the compound report is placed in a new Excel
worksheet (analogous to a new page in PDF).

The components of an Excel compound report can include standard tables, Table of Content
(BYTOC), and ROWOVERFLOW reports.

Component graphs will be added to worksheets as images.

Reference: Usage Notes for Excel Compound Reports Using XLSX

Images and graphs can be embedded within a component, but images and drawing objects
(lines, boxes, strings) defined in Compound Layout syntax on a page layout will not be
included in the generated workbook.

Graphs and images are not supported in Excel headers and footers within XLSX compound
workbooks.

Coordinated compound reports that generate individual instances of the overall report for
each unique primary key are not available in XLSX.

Note: Since multiple tables are generated, WebFOCUS will ensure that each tab name is
unique.

720

Example:

Compound Excel Report including Table of Contents (BYTOC)

9. Choosing a Display Format

SET PAGE-NUM=OFF
COMPOUND LAYOUT PCHOLD FORMAT XLSX
SECTION=Example, LAYOUT=ON, MERGE=OFF,$
PAGELAYOUT=1,$
COMPONENT=R1, TYPE=REPORT,TEXT='report1', POSITION=(0.833 0.729),
DIMENSION=(6.250 1.771),$
COMPONENT=R2, TYPE=REPORT,TEXT='report2', POSITION=(0.833 2.917),
DIMENSION=(6.250 1.875),$
COMPONENT=R3, TYPE=REPORT,TEXT='report3', POSITION=(0.938 5.313),
DIMENSION=(6.250 1.354),$
COMPONENT=R4, TYPE=REPORT,TEXT='report4', POSITION=(0.938 7.083),
DIMENSION=(6.042 1.146),$
END
SET COMPONENT=R1
TABLE FILE GGSALES
HEADING CENTER
"Gotham Grinds Sales to Information Builders"
" "
"Report 1"
"Sales Summary by Region"
" "
SUM UNITS/D12C BUDUNITS/D12C DOLLARS/D12CM BUDDOLLARS/D12CM
BY REGION
ON TABLE HOLD FORMAT XLSX
ON TABLE SET STYLE *
TYPE=REPORT, TITLETEXT=Region Summary,$
TYPE=REPORT, TOPMARGIN=1.5, BOTTOMMARGIN=1, PAGESIZE=LETTER,$
TYPE=TITLE, COLOR=WHITE, BACKCOLOR=GREY,$
TYPE=HEADING, LINE=1, OBJECT=TEXT, COLOR=PURPLE, JUSTIFY=CENTER, STYLE=BOLD,
$
TYPE=HEADING, LINE=3, OBJECT=TEXT, COLOR=BLUE, JUSTIFY=CENTER, STYLE=BOLD,$
TYPE=HEADING, LINE=4, OBJECT=TEXT, COLOR=PURPLE, JUSTIFY=CENTER, STYLE=BOLD,
$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 721

Saving Report Output in Excel XLSX Format

SET COMPONENT=R2
TABLE FILE GGSALES
SUM UNITS/D12C DOLLARS/D12CM
BY REGION BY CATEGORY BY PRODUCT
HEADING CENTER
"Gotham Grinds Sales to Information Builders"
" "
"Report 2"
"Sales Detail By Region"
ON REGION SUBHEAD
"<REGION Region Sales"
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET BYDISPLAY ON
ON TABLE SET COMPOUND BYTOC
ON TABLE SET STYLE *
TYPE=REPORT, TOPMARGIN=1.5, BOTTOMMARGIN=1, PAGESIZE=LETTER,$
TYPE=REPORT, TITLETEXT='Region-',$
TYPE=TITLE, COLOR=WHITE, BACKCOLOR=GREY,$
TYPE=HEADING, LINE=1, COLOR=PURPLE, JUSTIFY=CENTER,STYLE=BOLD,$
TYPE=HEADING, LINE=3, COLOR=BLUE, JUSTIFY=CENTER, STYLE=BOLD,$
TYPE=HEADING, LINE=4, COLOR=PURPLE, JUSTIFY=CENTER, STYLE=BOLD,$
ENDSTYLE
END

SET COMPONENT=R3
TABLE FILE GGSALES
HEADING CENTER
"Gotham Grinds Sales to Information Builders"
" "
"Report 3"
"Sales Summary by Category"
" "
SUM UNITS/D12C BUDUNITS/D12C DOLLARS/D12CM BUDDOLLARS/D12CM
BY CATEGORY
ON TABLE HOLD FORMAT XLSX
ON TABLE SET STYLE *
TYPE=REPORT, TITLETEXT=Sales Summary,$
TYPE=REPORT, TOPMARGIN=1.5, BOTTOMMARGIN=1, PAGESIZE=LETTER,$
TYPE=TITLE, COLOR=WHITE, BACKCOLOR=GREY,$
TYPE=HEADING,LINE=1,COLOR=PURPLE, JUSTIFY=CENTER, STYLE=BOLD,$
TYPE=HEADING,LINE=3,OBJECT=TEXT,COLOR=BLUE, JUSTIFY=CENTER, STYLE=BOLD,$
TYPE=HEADING,LINE=4,OBJECT=TEXT,COLOR=PURPLE, JUSTIFY=CENTER, STYLE=BOLD,$
ENDSTYLE
END

722

9. Choosing a Display Format

SET COMPONENT=R4
TABLE FILE GGSALES
HEADING CENTER
"Gotham Grinds Sales to Information Builders"
" "
"Report 4"
"Sales Detail Report By Category"
" "
SUM UNITS/D12C BUDUNITS/D12C DOLLARS/D12CM BUDDOLLARS/D12CM
BY CATEGORY BY PRODUCT BY REGION
ON TABLE SET BYDISPLAY ON
ON TABLE HOLD FORMAT XLSX
ON TABLE SET STYLE *
TYPE=REPORT, TITLETEXT=Sales Detail,$
TYPE=REPORT, TOPMARGIN=1.5, BOTTOMMARGIN=1, PAGESIZE=LETTER,$
TYPE=TITLE, COLOR=WHITE, BACKCOLOR=GREY,$
TYPE=HEADING,LINE=1,OBJECT=TEXT,COLOR=PURPLE, JUSTIFY=CENTER, STYLE=BOLD,$
TYPE=HEADING,LINE=3,OBJECT=TEXT,COLOR=BLUE, JUSTIFY=CENTER, STYLE=BOLD,$
TYPE=HEADING,LINE=4,OBJECT=TEXT,COLOR=PURPLE, JUSTIFY=CENTER, STYLE=BOLD,$
ENDSTYLE
END
COMPOUND END

The output is:

Report 1: Summary Report by Region

Creating Reports With TIBCO® WebFOCUS Language

 723

Saving Report Output in Excel XLSX Format

Report 2: BYTOC Reports by Region

The following image is tiled to show multiple worksheet reports, one for each region.

724

Report 3: Sales Summary Report by Category

9. Choosing a Display Format

Creating Reports With TIBCO® WebFOCUS Language

 725

Saving Report Output in Excel XLSX Format

Report 4: Sales Detail Report by Category

Reference: Guidelines for Using the Legacy OPEN, CLOSE, and NOBREAK Keywords and SET

COMPOUND

The keywords OPEN, CLOSE, and NOBREAK are used to control Excel compound reports. They
can be specified with the HOLD or PCHOLD command or with a separate SET COMPOUND
command.

OPEN is used on the first report of a sequence of component reports to specify that a
compound report should be started.

CLOSE is used to designate the last report in a compound report.

NOBREAK specifies that the next report be placed on the same worksheet as the current
report. If it is not present, the default behavior is to place the next report on a separate
worksheet.

726

9. Choosing a Display Format

When used with the HOLD or PCHOLD syntax, the compound report keywords OPEN,
CLOSE, and NOBREAK must appear immediately after FORMAT XLSX. For example, you can
specify:

ON TABLE PCHOLD FORMAT XLSX OPEN

ON TABLE HOLD AS MYHOLD FORMAT XLSX OPEN NOBREAK

As with PDF compound reports, compound report keywords can be alternatively specified
using SET COMPOUND:

SET COMPOUND = OPEN

SET COMPOUND = 'OPEN NOBREAK'

SET COMPOUND = NOBREAK

SET COMPOUND = CLOSE

Reference: Guidelines for Producing Excel Compound Reports Using XLSX

Naming of Worksheets. The default worksheet tab names will be Sheet1, Sheet2, and so
on. You have the option to specify a different worksheet tab name by using the TITLETEXT
keyword in the StyleSheet. For example:

TYPE=REPORT, TITLETEXT='Summary Report',$

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
following report. This allows the most flexibility, since if blank rows were added by default,
there would be no way to remove them.

Creating Reports With TIBCO® WebFOCUS Language

 727

Saving Report Output in Excel XLSX Format

Example:

Creating a Simple Compound Report Using XLSX

SET PAGE-NUM=OFF
TABLE FILE GGSALES
HEADING
"Report 1: Coffee - Budget"
" "
SUM BUDDOLLARS BUDUNITS COLUMN-TOTAL AS 'Total'
BY REGION
ON TABLE SET STYLE *
TYPE=REPORT, TITLETEXT=Coffee Budget,$
TYPE=HEADING, SIZE=14,$
ENDSTYLE
ON TABLE PCHOLD AS EX1 FORMAT XLSX OPEN
END

TABLE FILE GGSALES
HEADING
"Report 2: Coffee - Actual "
SUM DOLLARS UNITS COLUMN-TOTAL AS 'Total'
BY REGION
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET STYLE *
TYPE=REPORT, TITLETEXT=Coffee Actual,$
TYPE=HEADING, SIZE=14,$
ENDSTYLE
END

TABLE FILE GGSALES
HEADING
"Report 3: Food - Budget"
SUM BUDDOLLARS BUDUNITS COLUMN-TOTAL AS 'Total'
BY REGION
ON TABLE SET STYLE *
TYPE=REPORT, TITLETEXT=Food Budget,$
TYPE=HEADING, SIZE=14,$
ENDSTYLE
ON TABLE PCHOLD FORMAT XLSX CLOSE
END

728

The output is:

9. Choosing a Display Format

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
ON TABLE PCHOLD FORMAT XLSX OPEN NOBREAK
ON TABLE SET STYLE *
TYPE=REPORT, TITLETEXT=Coffee, FONT=ARIAL, SIZE=10, STYLE=NORMAL,$
TYPE=TITLE, STYLE=BOLD,$
TYPE=HEADING, SIZE=12, STYLE=BOLD, COLOR=BLUE,$
TYPE=GRANDTOTAL, STYLE=BOLD,$
END

TABLE FILE GGSALES
HEADING
" "
"Report 2: Coffee - Actual "
SUM DOLLARS UNITS COLUMN-TOTAL AS 'Total'
BY REGION
IF CATEGORY EQ Coffee
ON TABLE PCHOLD FORMAT XLSX
ON TABLE SET STYLE *
TYPE=REPORT, FONT=ARIAL, SIZE=10, STYLE=NORMAL,$
TYPE=GRANDTOTAL, STYLE=BOLD,$
TYPE=HEADING, SIZE=12, STYLE=BOLD, COLOR=BLUE,$
END

Creating Reports With TIBCO® WebFOCUS Language

 729

Saving Report Output in Excel XLSX Format

TABLE FILE GGSALES
HEADING
"Report 3: Food - Budget"
SUM BUDDOLLARS BUDUNITS COLUMN-TOTAL AS 'Total'
BY REGION
IF CATEGORY EQ Food
ON TABLE PCHOLD FORMAT XLSX NOBREAK
ON TABLE SET STYLE *
TYPE=REPORT, TITLETEXT=Food, FONT=ARIAL, SIZE=10, STYLE=NORMAL,$
TYPE=HEADING, STYLE=BOLD, SIZE=12, COLOR=BLUE,$
TYPE=TITLE, STYLE=BOLD,$
TYPE=GRANDTOTAL, STYLE=BOLD,$
END

TABLE FILE GGSALES
HEADING
" "
"Report 4: Food - Actual"
SUM DOLLARS UNITS COLUMN-TOTAL AS 'Total'
BY REGION
IF CATEGORY EQ Food
ON TABLE PCHOLD FORMAT XLSX CLOSE
ON TABLE SET STYLE *
TYPE=REPORT, FONT=ARIAL, SIZE=10,  $
TYPE=TITLE, STYLE=BOLD,$
TYPE=HEADING, SIZE=12, STYLE=BOLD, COLOR=BLUE,$
TYPE=GRANDTOTAL, STYLE=BOLD,$
END

730

Report output is displayed in two separate tabs.

9. Choosing a Display Format

Using XLSX FORMULA With Compound Reports

In new compound syntax, the implementation of compound workbooks with XLSX FORMULA
can be activated in either of the following ways. Each of these approaches will generate a
workbook with all of the component reports in FORMULA mode.

1. Add FORMAT XLSX FORMULA to the compound syntax header, as shown in the following

syntax:

Creating Reports With TIBCO® WebFOCUS Language

 731

Saving Report Output in Excel XLSX Format

COMPOUND LAYOUT PCHOLD FORMAT XLSX FORMULA
UNITS=IN, $
SECTION=section1, LAYOUT=ON, METADATA='prop_with_names, Margins_Left=0.5,
Margins_Top=0.5, Margins_Right=0.5, Margins_Bottom=0.5, thumbnailscale=4,
MERGE=OFF, ORIENTATION=PORTRAIT, PAGESIZE=Letter, SHOW_GLOBALFILTER=OFF,
$
PAGELAYOUT=1, NAME='Page layout 1', text='Page layout 1', TOC-LEVEL=1,
BOTTOMMARGIN=0.5, TOPMARGIN=0.5, METADATA='BOTTOMMARGIN=0.5,
TOPMARGIN=0.5,LEFTMARGIN=0,RIGHTMARGIN=0,', $
COMPONENT='report1', TEXT='report1', TOC-LEVEL=2, POSITION=(0.567 0.667),
DIMENSION=(6.883 2.314), BYTOC=0, ARREPORTSIZE=DIMENSION,
METADATA='left: 0.567in; top: 0.667in; width: 6.883in; height: 2.314in;
position: absolute; z-index: 1;', $
COMPONENT='report2', TEXT='report2', TOC-LEVEL=2, POSITION=(0.567 3.250),
DIMENSION=(7.000 2.833), BYTOC=0, ARREPORTSIZE=DIMENSION,
METADATA='left: 0.567in; top: 3.25in; width: 7in; height: 2.833in;
position: absolute; z-index: 2;', $
END

2. Define XLSX FORMULA as the output setting for the first component, as shown in the

following syntax:

SET COMPONENT='report1'
-*component_type report
-*File: IBFS:/localhost/EDA/9999/APPPATH/xlsx2015/Report1.fex
-*Created by WebFOCUS AppStudio
DEFINE FILE GGSALES
D_UOVERBUD/D12C=GGSALES.SALES01.UNITS - GGSALES.SALES01.BUDUNITS;
END
TABLE FILE GGSALES
SUM
     GGSALES.SALES01.UNITS
     GGSALES.SALES01.BUDUNITS
     GGSALES.SALES01.DOLLARS
     GGSALES.SALES01.BUDDOLLARS
     GGSALES.SALES01.D_UOVERBUD
     COMPUTE C_DOVERBUD/D12.2CM = GGSALES.SALES01.DOLLARS -
       GGSALES.SALES01.BUDDOLLARS;
BY GGSALES.SALES01.REGION
BY GGSALES.SALES01.CATEGORY
HEADING
"XLSX FORMULA - the difference betweem DEFINE & COMPUTES"
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE SET ASNAMES ON
ON TABLE COLUMN-TOTAL AS 'TOTAL'
ON TABLE PCHOLD FORMAT XLSX FORMULA
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
     INCLUDE = endeflt,
$
ENDSTYLE

732

9. Choosing a Display Format

Note:

Although both of these approaches will work, from a tool perspective, it is advantageous to
use the first approach (add FORMAT XLSX FORMULA to the compound syntax header) since
the user may not have control of the first table when system tables are generated with
page masters and in other page layout scenarios. This approach ensures that the XLSX
FORMULA designation is always moved to the first table.

If you change the format for the compound workbook so that the compound header
requests XLSX, not XLSX FORMULA, this will not automatically turn off FORMULA. When
FORMULA is set in the first component, this will always override the compound heading
setting. This may cause confusion when you think you have turned FORMULA off at the
document level, but it is actually retained at the first component level.

WebFOCUS Pivot Support for XLSX

The WebFOCUS XLSX format can generate a workbook based on a template that contains
predefined pivot tables. These pivot tables can be built based on data fed from a report and/or
exist independently of the WebFOCUS data on other worksheets.

Example:

Feeding Data From a WebFOCUS Report Into a Pivot Table and Pivot Chart

The following sample procedure shows how to feed data from a WebFOCUS report into a pivot
table and pivot chart within an existing Excel template called wf2pivot.xltx.

Note: Template names containing embedded blanks must be enclosed in single quotation
marks.

TABLE FILE GGSALES
PRINT
UNITS/D12C DOLLARS/D12CM
BUDUNITS/D12C BUDDOLLARS/D12CM
BY LOWEST REGION
BY LOWEST ST
BY HIGHEST CATEGORY
BY LOWEST PRODUCT
ON TABLE SET BYDISPLAY ON
ON TABLE PCHOLD AS PIVOTWITHCHART FORMAT XLSX TEMPLATE wf2pivot.xltx
SHEETNUMBER 2
ON TABLE SET STYLE *
TYPE=DATA,IN-RANGES='DATAwithHEADERS',$
TYPE=TITLE,IN-RANGES='DATAwithHEADERS',$
ENDSTYLE
END

The wf2pivot.xltx template file must be in the Reporting Server path. The following images
show the default of the first and second worksheets in the wf2pivot.xltx template, before
executing the sample procedure.

Creating Reports With TIBCO® WebFOCUS Language

 733

Saving Report Output in Excel XLSX Format

The first worksheet, PivotTablewithChart, contains an empty pivot table and pivot chart. It also
contains an empty PivotTableFieldList. The first worksheet is shown in the following image.

734

The second worksheet, Source Data, contains one column called FieldsToBeAdded, for which
there is initially no data. The second worksheet is shown in the following image.

9. Choosing a Display Format

When you run the sample procedure, a pivotwithchart.xlsx workbook is generated, with the
WebFOCUS report data stored in the second worksheet.

The following images show the first and second worksheets in the pivotwithchart.xlsx workbook
after you run the sample procedure.

Creating Reports With TIBCO® WebFOCUS Language

 735

Saving Report Output in Excel XLSX Format

First Worksheet

736

Second Worksheet

9. Choosing a Display Format

In the PivotTablewithChart worksheet, note that the PivotTableFieldList is populated with the
fields from the WebFOCUS report. There is one check box for each field in the report
procedure. All the check boxes are not selected, by default.

The data used to populate the check boxes is obtained from the Source Data worksheet,
where the data from the WebFOCUS report was saved upon executing the sample procedure.

Creating Reports With TIBCO® WebFOCUS Language

 737

Saving Report Output in Excel XLSX Format

To start building a pivot report and pivot chart, you can select the check boxes for the desired
fields in the PivotTableFieldList. For example, selecting the check boxes for Product, Unit
Sales, and Budget Units will automatically feed the data from the Source Data worksheet into
the pivot table and pivot chart in the PivotTablewithChart worksheet. The resulting pivot table
and pivot chart are shown in the following image.

The wf2pivot.xltx template is provided, by default, with the WebFOCUS Reporting Server
installation as part of the Legacy Samples. For information on how to download the Reporting
Server Legacy Samples, see the Server Administration manual.

You can use the WebFOCUS XLSX template as is, or you can customize it to meet the your
business requirements.

Note: The wf2pivot.xltx template includes a pivot table and pivot chart on the same worksheet,
but you can use a macro-enabled template to generate a pivot table and a pivot chart on
separate worksheets, which are linked to a common data source.

FORMAT XLSX Limitations

Format XLSX does not support the following features, currently supported for EXL2K:

Cell locking

XLSX reports are available on a z/OS USS server but are not currently supported on a z/OS
PDS server or on a z/OS USS server with the setting DYNAM TEMP ALLOC MVS.

For additional support on the implementation of features supported by the XLSX format, see
WebFOCUS XLSX Format Supported Features Roadmap, located at the following link:

738

9. Choosing a Display Format

https://techsupport.informationbuilders.com/tech/wbf/wbf_rln_formatXLSX_support.html

Using PowerPoint PPT Display Format

Specifying PowerPoint (PPT) as the output format creates a PowerPoint document with a single
slide that includes the report.

You can add multiple graphs and images to a PowerPoint presentation. The PowerPoint output
format can contain a variety of graphs positioned anywhere on a slide to create a visual layout.

You can also place report output on a specific slide in a PowerPoint template.

Using PowerPoint PPT Templates

A WebFOCUS report can be placed inside of an existing PowerPoint presentation. This enables
you to populate existing presentations with preset Slide Masters, styling, and other business
content. PowerPoint PPT templates are stored on the server with a .MHT extension and can be
distributed automatically with ReportCaster.

Syntax:

How to Create PowerPoint PPT Report Output

ON TABLE {PCHOLD|HOLD|SAVE} [AS name] FORMAT PPT
      [TEMPLATE 'template' SLIDENUMBER n]

where:

name

Is the name of the PowerPoint output file.

template

Is the name of the PowerPoint template file. The template file must have at least one
blank slide and must be saved as a Web Archive (.MHT extension) on your WebFOCUS
Reporting Server application directory.

Tip: Since the Reporting Server cannot differentiate between Excel and PowerPoint
template files (.MHT), it is important to apply a naming convention to your template files.
This will help you organize and distinguish the different Excel and PowerPoint template files
when developing your reports. For example, Excel_template.MHT or PPT_template.MHT.

n

Is the number of the slide on which to place the report output. This number is optional if
the template has only one slide.

Creating Reports With TIBCO® WebFOCUS Language

 739

Saving Report Output in PPTX Format

Example:

Using a PowerPoint PPT Template

The following request against the GGSALES data source inserts a WebFOCUS report into a
PowerPoint template named mytemplate.mht, which is stored in the application directory:

TABLE FILE GGSALES
HEADING
" "
" "
" "
" "
" "
SUM DOLLARS UNITS CATEGORY
BY  REGION
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT PPT TEMPLATE 'mytemplate' SLIDENUMBER 1
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
TYPE=REPORT, FONT=ARIAL, SIZE=10,$
TYPE=HEADING, image=gglogo.gif, POSITION=(0.000000 0.000000),$
ENDSTYLE
END

The output is:

Saving Report Output in PPTX Format

WebFOCUS Release 8.0 Version 08 introduced the capability to retrieve data from any
WebFOCUS supported data source and to generate a PPTX formatted (PowerPoint 2007,
PowerPoint 2010, and PowerPoint 2013) presentation. This section, which describes important
PPTX features, applies to PowerPoint 2007, PowerPoint 2010, and PowerPoint 2013, unless
otherwise indicated.

The PPTX format in WebFOCUS supports the following Microsoft Office software products:

Microsoft Office 2013/2010/2007.

740

9. Choosing a Display Format

Microsoft Office 2000/2003 with the Microsoft Office Compatibility Pack.

Note: As per the Microsoft Support has ended for Office 2003 statement, support and
updates for Office 2003 are no longer available. Although you will still be able to start and
work in the Microsoft Office 2003 application, Microsoft recommends that you upgrade to a
newer version of Office to get continuing support and updates. If you are using Office 2003,
see end of support page for Windows XP SP3 and Office 2003 for more information.

Open Office Support (FORMAT PPTX). Core PowerPoint functionality generated by the PPTX
format is supported for Open Office as of WebFOCUS Release 8.0 Version 08. For details
on Open Office, see http://www.openoffice.org/.

MAC Office 2008 and 2011. FORMAT PPTX is supported as of WebFOCUS Release 8.0.08.

WebFOCUS generates PPTX presentations based on the Microsoft PPTX standard. These
presentations are accessible through all browsers and the Microsoft PowerPoint mobile
application.

Microsoft Office 365™. Microsoft Office 365 offers the local installation of PowerPoint
2013. It works with the Office 2010 release and provides limited functionality with Office
2007. Microsoft Office 365 also permits uploading Microsoft PowerPoint files to the cloud,
where they can be accessed on most devices using Office Online. For information on the
Microsoft Office 365 plans and features, see Office 365 for business FAQ.

You can use Microsoft Office 365 to access a WebFOCUS PPTX report. First, display the
PPTX report on the screen using the PCHOLD command, and then save the report to
OneDrive® for Business. Once the file is in the cloud, you can access the file using Office
Online.

For information on the differences in features available in PowerPoint Online and in
Microsoft Office 2013, see Office Online Service Description.

For more information on working with Office Online and OneDrive for Business, see Using
Office Online in OneDrive.

Creating Reports With TIBCO® WebFOCUS Language

 741

Saving Report Output in PPTX Format

Building the .pptx Presentation File

Microsoft changed the format and structure of the PowerPoint presentation file in PowerPoint
2007. The new .pptx file is a binary compilation of a group of .xml files. Generating this new
file format using WebFOCUS is a two-step process that consists of generating the .xml files
containing the report output and zipping the .xml documents into the binary .pptx format. The
Reporting Server performs the xml generation process. The zipping process can be completed
either by the Client (WebFOCUS Servlet) or the Server (JSCOM3):

WebFOCUS Servlet. The WebFOCUS Client within the application server performs the
zipping process. This can be done within the local client or through a remotely accessed
client. The servlet method is the default approach defined for each WebFOCUS Client, with
the client pointing to itself, by default.

JSCOM3. The Java layer of the Reporting Server performs the zipping operation. This option
should be used when the WebFOCUS Servlet is configured on a secured web or application
server. This is because JSCOM3 does not require URL access to a remote WebFOCUS
Client.

Syntax:

How to Select the Method for Zipping the .pptx File

You designate the method and location where the zipping will occur by setting EXCELSERVURL
to a URL (for the WebFOCUS Servlet) or to a blank (for JSCOM3). Even though this setting is
prefaced with EXCEL, when applied, the same results are achieved for PowerPoint. You can set
this value for a specific procedure or for the entire environment:

For a procedure. Issue the SET EXCELSERVURL command within the procedure.

For the entire environment. Edit the IBIF_excelservurl variable in the WebFOCUS
Administration Console by selecting Configuration/Client Settings/General/IBIF_excelservurl.

For more information on accessing the WebFOCUS Administration Console and setting the
IBIF_excelservurl variable, see the WebFOCUS Security and Administration manual.

The value you assign to EXCELSERVURL determines whether the WebFOCUS Servlet or
JSCOM3 performs the zipping operation:

Specifying the Servlet. To specify that the WebFOCUS Servlet should be used, set the
EXCELSERVURL parameter or the IBIF_excelservurl variable to the URL of a WebFOCUS
Release 8.0 Version 09 or higher client configuration.

In a procedure:

SET EXCELSERVURL = http://servername:8080/ibi_apps

In the WebFOCUS Administration Console:

742

9. Choosing a Display Format

IBIF_excelservurl = http://servername:8080/ibi_apps

Specifying JSCOM3. To specify that JSCOM3 should be used within the current Reporting
Server, set EXCELSERVURL to a blank or an empty string.

In a procedure:

SET EXCELSERVURL = ' '

In the WebFOCUS Administration Console:

IBIF_excelservurl = ' '

By default, each WebFOCUS Client contains the following URL definition that points to
itself:

&URL_PROTOCOL://&servername:&server_port&IBIF_webapp

Syntax:

How to Generate a PPTX Presentation

You can specify that a report should be saved to a PPTX presentation, displayed in the
browser, or displayed in the PowerPoint application.

ON TABLE {PCHOLD|HOLD} AS name FORMAT PPTX

where:

PCHOLD

Displays the generated presentation in either the browser or the PowerPoint application,
based on your desktop settings. For information, see Viewing PowerPoint Presentations in
the Browser vs. the PowerPoint Application on page 745.

HOLD

Saves a presentation with a .pptx extension to the designated location.

name

Specifies a file name for the generated presentation.

Note: To assign a file name to the generated presentation, set the Save Report option to
YES for the .pptx file extension in the WebFOCUS Client Redirection Settings. When opened
in the PowerPoint application, the generated presentation will retain the designated AS
name. For more information on the Redirection Settings, see the WebFOCUS Security and
Administration manual.

Creating Reports With TIBCO® WebFOCUS Language

 743

Saving Report Output in PPTX Format

Opening PPTX Report Output

To open PPTX presentations, the user must have an account for Microsoft Office365 or
Microsoft PowerPoint 2013, 2010, or 2007 must be installed on the desktop.

Upon execution of a report with FORMAT PPTX, the user is prompted to Open or Save the PPTX
file. The file name displayed before the .pptx extension is an internally generated name.

The WebFOCUS procedure generates a presentation containing as many slides as required to
display output. A report may contain defined elements, such as headings, subtotals, and titles,
as well as StyleSheet syntax, such as conditional styling and drill downs.

Opening PPTX Report Output in Microsoft PowerPoint 2000/2003

PowerPoint 2000 and PowerPoint 2003 can be updated to read PowerPoint PPTX presentations
using the Microsoft Office Compatibility Pack available from the Microsoft download site
(http://www.microsoft.com/downloads/en/default.aspx). When the file extension of the file
being opened is .pptx (PPTX presentation), the Microsoft Office Compatibility Pack performs the
necessary conversion to allow PowerPoint 2000/2003 to read and open it.

In addition to the Microsoft Office Compatibility Pack, it is important to enable the WebFOCUS
Client Redirection Settings Save As option so that PowerPoint 2000/2003 will be able to open
the PPTX report output without users first having to save it to their machine with the .pptx file
extension. The WebFOCUS Client processing Redirection Settings Save As option configures
how the WebFOCUS Client sends each report output file type to the user machine.

This option can be set as follows:

Save As Option disabled (NO). The WebFOCUS Client Redirection Setting Save As is
disabled, by default. When the Save As option is disabled, the WebFOCUS Client sends
report output to the user machine in memory with the application association specified for
the report format in the WebFOCUS Client Redirection Settings configuration file
(mime.wfs).

A user machine that does not have PowerPoint 2007 or higher installed will not recognize
the application association for PowerPoint and PowerPoint will display a message. The
PowerPoint 2000/2003 user can select Save and provide a file name with the .pptx
extension to save the report output to their machine. The user can then open the .pptx file
directly from PowerPoint 2000/2003.

744

9. Choosing a Display Format

Save As Option enabled (YES). When the WebFOCUS Redirection Save As option is
enabled, the WebFOCUS Client sends the report output to the user as a file with the
extension specified in the WebFOCUS Client Redirection Settings configuration file
(mime.wfs). Upon receiving the file, Windows will display the File Download prompt asking
the user to Open or Save the file with the identified application type. The File Download
prompt displays the Name with the .pptx file extension for the report output that is
recognized as a PowerPoint PPTX file type.

Note: The download prompt will display for all users, including users who have PowerPoint
2007 or higher installed on their machines.

If a PowerPoint 2000/2003 user chooses to open the file, the Microsoft Office
Compatibility Pack will recognize the .pptx file extension and perform the necessary
conversion to allow PowerPoint 2000/2003 to read the PowerPoint PPTX presentation.

If a PowerPoint 2007 or higher user chooses to open the file, PowerPoint will recognize
the .pptx file extension and read the PowerPoint PPTX presentation.

For additional information on WebFOCUS Client Redirection Settings, see the WebFOCUS
Security and Administration manual.

Viewing PowerPoint Presentations in the Browser vs. the PowerPoint Application

Your Operating System and desktop settings determine whether PowerPoint output sent to the
client is displayed in an Internet Browser window or within the PowerPoint application. When
PowerPoint output has been defined within the Windows environment to Browse in same
window, the workbook generated by a WebFOCUS request is opened within an Internet
Explorer® browser window. When the Browse in same window option is unchecked for the .ppt
file type, the browser window created by WebFOCUS is blank because the report output is
displayed in the stand-alone PowerPoint application window.

In Windows XP and earlier, file type specific settings are managed on the desktop within
Windows Explorer by selecting Tools/Folder Options, clicking the File Types tab, selecting
the extension (.ppt or .pptx), clicking the Advanced button, and checking the Browse in
same window check box.

As per the Microsoft Support has ended for Office 2003 statement, support and updates for
Office 2003 are no longer available. Although you will still be able to start and work in the
Microsoft Office 2003 application, Microsoft recommends that you upgrade to a newer
version of Office to get continuing support and updates. If your organization uses Office
2003, go to the end of support page for Windows XP SP3 and Office 2003 for more
information.

Creating Reports With TIBCO® WebFOCUS Language

 745

Saving Report Output in PPTX Format

In Windows 7, Microsoft removed the desktop settings that support opening worksheets in
the browser. This means that to change this behavior, you can no longer simply navigate to
the Folder Options dialog box, but you must change a registry setting. This change is
documented in the Microsoft Knowledge Base Article ID 927009 at the following website:

http://support.microsoft.com/kb/927009

Note: This works the same for both PPT and PPTX formats. The only difference is the
selection of file type based on the version of PowerPoint output you will be generating.

Grouping Tables and Components in a PowerPoint Slide

When table elements are placed on a PowerPoint slide, the elements are placed in individual
text boxes to allow for explicit positioning to match the other positioned drivers, such as PDF
and DHTML.

The PPTXGROUP parameter enables you to group elements together in a PPTX report. You can
rotate, flip, move, or resize objects within a group at the same time as though they were a
single object. You can also change the attributes of all of the objects in a group at one time,
including font, color, or size, and you can ungroup a group of objects at any time, and then
regroup them later.

In WebFOCUS, grouping is done within each report component. Objects within the report
component (or stand-alone report), including data, all headings and footings, and images, are
grouped together. In compound reports, each component report is grouped individually and
non-component elements, such as drawing objects, lines, and images, are not included in any
group.

Syntax:

How to Group Tables and Components in a PowerPoint Slide

SET PPTXGROUP = {ON|OFF}

The command can also be issued from within a report using:

ON TABLE SET PPTXGROUP = {ON|OFF}

In a StyleSheet:

TYPE=REPORT, PPTXGROUP = {ON|OFF}

where:

ON

Enables you to group elements together in a PPTX report.

746

9. Choosing a Display Format

OFF

Indicates no grouping of elements, which is the legacy behavior. OFF is the default value.

Example:

Displaying Group Tables and Components in a Standard Report

In the following standard report, the grouping is defined for the core report elements, excluding
images and drawing objects, defined at the TYPE=REPORT level.

TABLE FILE GGSALES
SUM DOLLARS/D12CM UNITS/D12C BUDDOLLARS/D12CM BUDUNITS/D12C
COMPUTE SHOWCAT/A100=CATEGORY||'.GIF';
BY REGION
BY CATEGORY
ON TABLE SUBHEAD
"Report Heading Here"
" "
" "
" "
HEADING
"Page Heading here"
FOOTING
"Page Footing here"
ON TABLE SUBFOOT
"Report Footing Here"
ON TABLE PCHOLD AS GROUPTEST FORMAT PPTX
ON TABLE SET STYLE *
TYPE=REPORT, PPTXGROUP = ON, SQUEEZE=ON, FONT=TAHOMA,SIZE=12,
ORIENTATION=LANDSCAPE, $
TYPE=REPORT, OBJECT=LINE, POSITION=(9 1), DIMENSION=(1 5), COLOR=BLUE, $
TYPE=REPORT, IMAGE=IBILOGO, POSITION=(0 0), $
TYPE=TABHEADING, IMAGE=GGLOGO.GIF, POSITION=(6.5 .10), $
TYPE=DATA,COLUMN=SHOWCAT, IMAGE=(SHOWCAT), PRESERVERATIO=ON,
SIZE=(.5 .5), $
END

Creating Reports With TIBCO® WebFOCUS Language

 747

Saving Report Output in PPTX Format

The output is:

Example:

Displaying Group Tables and Components in a Compound Report

In the following compound report, the grouping is defined for the component report. Additional
objects on the page, including the chart image, logo image, lines, and text box are not included
in the grouping.

748

9. Choosing a Display Format

SET HTMLARCHIVE=ON
SET PPTXGRAPHTYPE=PNG
SET PPTXGROUP=ON
COMPOUND LAYOUT PCHOLD FORMAT PPTX
UNITS=IN, $
SECTION=section1, LAYOUT=ON, MERGE=OFF, ORIENTATION=LANDSCAPE, PAGESIZE=PPT
Slide, $
PAGELAYOUT=1, NAME='Page layout 1', TEXT='Page layout 1', BOTTOMMARGIN=0.5,
TOPMARGIN=0.5, $
OBJECT=STRING, NAME='text1', TEXT='<left>Grouping is supported within the
component reports of a compound report:
<ul type=disc>
<LI>Each table / report is grouped together. </LI>
<LI>Drawing objects such as images and lines are not included in any group.
</LI>
<LI>Charts are inserted as images.</LI></ul><div><br></div><br></left>',
POSITION=(2.764 4.958), MARKUP=ON, WRAP=ON, DIMENSION=(4.000 1.992),
FONT='TREBUCHET MS', COLOR=RGB(0 0 0), SIZE=10, $
COMPONENT='report1', TEXT='report1', POSITION=(1.028 2.083),
DIMENSION=(4.431 1.667), $
COMPONENT='chart2', TEXT='chart2', POSITION=(4.972 1.319), DIMENSION=(4.456
3.085), COMPONENT-TYPE=GRAPH, $
OBJECT=BOX, NAME='line1', POSITION=(0.498 6.500),
DIMENSION=(9.167 0.022), BACKCOLOR=BLACK, BORDER-COLOR=BLACK, $
OBJECT=BOX, NAME='line2', POSITION=(0.502 1.097),
DIMENSION=(9.167 0.022), BACKCOLOR=BLACK, BORDER-COLOR=BLACK, $
OBJECT=IMAGE, NAME='image4', IMAGE=ibologo.gif, ALT='',
POSITION=(0.502 0.499), DIMENSION=(1.861 0.506), $
END

SET COMPONENT='report1'
TABLE FILE GGSALES
SUM
   GGSALES.SALES01.DOLLARS
BY GGSALES.SALES01.REGION
ACROSS LOWEST GGSALES.SALES01.CATEGORY
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
     INCLUDE=IBFS:/FILE/IBI_HTML_DIR/ibi_themes/Warm.sty,$
$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 749

Saving Report Output in PPTX Format

SET COMPONENT='chart2'
SET PAGE-NUM=NOLEAD
SET ARGRAPHENGINE=JSCHART
SET EMBEDHEADING=ON
SET GRAPHDEFAULT=OFF
GRAPH FILE GGSALES
SUM GGSALES.SALES01.DOLLARS
BY GGSALES.SALES01.CATEGORY
ACROSS GGSALES.SALES01.REGION
ON GRAPH PCHOLD FORMAT HTML
ON GRAPH SET VZERO OFF
ON GRAPH SET GRWIDTH 1
ON GRAPH SET UNITS 'PIXELS'
ON GRAPH SET HAXIS 770.0
ON GRAPH SET VAXIS 405.0
ON GRAPH SET GRMERGE ADVANCED
ON GRAPH SET GRMULTIGRAPH 0
ON GRAPH SET GRLEGEND 1
ON GRAPH SET GRXAXIS 1
ON GRAPH SET LOOKGRAPH HBAR
ON GRAPH SET STYLE *

*GRAPH_SCRIPT
setPieDepth(0);
setPieTilt(0);
setDepthRadius(0);
setCurveFitEquationDisplay(false);
setPlace(true);
*END
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/ibi_themes/Warm.sty,$
TYPE=REPORT, TITLETEXT='WebFOCUS Report', $
*GRAPH_SCRIPT
setLegendPosition(4);
*GRAPH_JS_FINAL
"blaProperties": {
    "orientation": "horizontal"
},
"agnosticSettings": {
    "chartTypeFullName": "Bar_Clustered_Horizontal"
}
*END
ENDSTYLE
END
-RUN

COMPOUND END

750

The output is:

9. Choosing a Display Format

Date and Page/Slide Number

You can add the date and page numbers to both single and Compound Reports.

For single reports, use the TABPAGENO feature and the associated attributes.

For Compound Reports, add your data and page number to text objects. For more
information, see Text Formatting Markup Tags for a Text Object on page 751.

Text Formatting Markup Tags for a Text Object

Note: If your text contains any open caret characters (<), you must put a blank space after
each open caret that is part of the text, for example, “< 250”. If you do not, everything
following the open caret will be interpreted as the start of a markup tag and will not display as
text.

Creating Reports With TIBCO® WebFOCUS Language

 751

Saving Report Output in PPTX Format

Font Properties

The font tag supports three attributes: face, size, and color (where the color must be specified
as the hexadecimal number code for the color):

<font face="font" size=[+|-]n color=color_code>text</font>

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

752

9. Choosing a Display Format

Full Justification:

 <full>text</full>

Vertical Alignment

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

Creating Reports With TIBCO® WebFOCUS Language

 753

Saving Report Output in PPTX Format

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

By default, Arabic numerals (type=1) are used for the ordering of the list. You can specify the
following types of order:

Arabic numerals (the default): <ol type=1>

Lowercase letters: <ol type=a>

Uppercase letters: <ol type=A>

Lowercase Roman numerals: <ol type=I>

Uppercase Roman numerals: <ol type=I>

Hyperlinks

Hyperlinks can be included within text markup in a PPTX output file.

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

754

9. Choosing a Display Format

Page Numbering

There are two pseudo-HTML tags for embedding page numbers in text on a Page Master for a
Coordinated Compound Layout report:

Current page number: <ibi-page-number/>

Total number of pages: <ibi-total-pages/>

Note that when MARKUP=ON, space is allocated for the largest number of pages, so there may
be a wide gap between the page number and the text that follows. To remove the extra space
in the text object that has the page numbering tags:

If specific styling of the text object is not required, do not insert markup tags, and turn
MARKUP=OFF.

MARKUP=OFF, TEXT='Page <ibi-page-number/> of <ibi-total-pages/> of Sales
Report', $

This displays the following output:

Page 1 of 100 of Sales Report

If specific styling of the text object is required, you must set MARKUP=ON. With
MARKUP=ON, set WRAP=OFF and do not place any styling tags between the page number
variables within the string. Tags can be used around the complete Page n of m string. The
following code produces a page number string without the extra spaces:

MARKUP=ON, WRAP=OFF, TEXT='<font face="ARIAL" size=10><i>Page <ibi-page-
number/> of <ibi-total-pages/> of Sales Report </i>', $

This displays the following output:

Dates

To display a date in the report output, insert a WebFOCUS date variable in a text object on a
Page Master (such as &DATEtrMDYY) in the text object.

Creating Reports With TIBCO® WebFOCUS Language

 755

Saving Report Output in PPTX Format

Example:

Formatting a Compound Layout Text Object With Markup Tags

The following request displays a text object with markup tags in a PPTX output file.

Important: Text markup syntax cannot contain hidden carriage return or line feed characters.
For purposes of presenting the example in this documentation, line feed characters have been
added so that the sample code wraps to fit within the printed page. To run this example in your
environment, copy the code into a text editor and delete any line feed characters within the
text markup object by going to the end of each line and pressing the Delete key. In some
instances, you may need to add a space to maintain the structure of the string. For additional
information on displaying carriage returns within the text object see Text Formatting Markup
Tags for a Text Object on page 751.

SET PAGE-NUM=OFF
SET LAYOUTGRID=ON
TABLE FILE GGSALES
BY REGION NOPRINT
ON TABLE PCHOLD AS LINESP1 FORMAT PPTX
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

756

9. Choosing a Display Format

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

 757

Saving Report Output in PPTX Format

Example:

Drawing Text and Line objects on a Page Master

The following request places a line on the Page Master between the header report and the
component reports and places a line and a text string on the bottom of each page:

SET PAGE-NUM=OFF
SET SQUEEZE=ON
COMPOUND LAYOUT PCHOLD FORMAT PPTX
SECTION=S1, LAYOUT=ON, MERGE=ON, ORIENTATION=LANDSCAPE, $
PAGELAYOUT=ALL, $
COMPONENT=HEADER, TYPE=REPORT, POSITION=(1 1), DIMENSION=(4 4), $
OBJECT=STRING, POSITION=(1 6.6), MARKUP=ON,
TEXT='<font face="Arial" color=#0000FF size=12> Slide <ibi-page-number/>
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

758

9. Choosing a Display Format

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
END
SET COMPONENT=R3
TABLE FILE GGSALES
"Report R3 for <REGION"
BY REGION NOPRINT
SUM DOLLARS BY ST
ON TABLE SET STYLE *
TYPE=REPORT, FONT=HELVETICA, COLOR=GREEN, $
END
COMPOUND END

Creating Reports With TIBCO® WebFOCUS Language

 759

Saving Report Output in PPTX Format

The first page of output is:

The second page of output has the same drawing objects:

760

Example:

Vertically Aligning Text Markup in PPTX Report Output

The following request creates three boxes and places a text string object within each of them:

9. Choosing a Display Format

In the left box, the text is aligned vertically at the top.

In the middle box, the text is aligned vertically at the middle.

In the right box, the text is aligned vertically at the bottom.

Important: Text markup syntax cannot contain hidden carriage return or line feed characters.
For purposes of presenting the example in this documentation, line feed characters have been
added so that the sample code wraps to fit within the printed page. To run this example in your
environment, copy the code into a text editor and delete any line feed characters within the
text markup object by going to the end of each line and pressing the Delete key. In some
instances, you may need to add a space to maintain the structure of the string. For additional
information on displaying carriage returns within the text object see Text Formatting Markup
Tags for a Text Object on page 751.

SET PAGE-NUM=OFF
TABLE FILE GGSALES
BY REGION NOPRINT
ON TABLE PCHOLD FORMAT PPTX
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
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 761

Saving Report Output in PPTX Format

Display Unordered Lists With Bullets, Discs, Squares, and Circles

The unordered (ul) list tag encloses a bulleted list in which each item is marked by a bullet of a
particular shape or design. Each item or point is enclosed in a list item tag (li). The start and
end tags for each point may occupy one continuous line or be placed on different lines. When
each list is placed on a new line, insert a backslash (\) after each closing tag.

Example:

Displaying Unordered Lists With Bullets, Squares, and Circles

The following request displays a bulleted list with bullets of particular shapes and designs.

<ul>
<li>list item1</li>\
<li>list item2</li>\
</ul>

SET HTMLARCHIVE=ON
COMPOUND LAYOUT PCHOLD FORMAT PPTX
UNITS=IN, $
SECTION=section1, LAYOUT=ON, MERGE=OFF, ORIENTATION=PORTRAIT,
PAGESIZE=Letter, SHOW_GLOBALFILTER=OFF, $
PAGELAYOUT=1, NAME='Page layout 1', text='Page layout 1',
BOTTOMMARGIN=0.5, TOPMARGIN=0.5, $
OBJECT=STRING, NAME='text1', TEXT='<font face="TREBUCHET MS" size=10>\
<UL>
<LI>The first level of a bulleted line </LI>\
<UL>
<LI><b>Second level:</b> Indented or nested line one</LI>\
<LI><b>Second level:</b> Indented or nested line two</LI>\
<LI><b>Second level:</b> Indented or nested line three</LI>\
<UL>\
<LI>Third level: Indented or nested line one</LI>\
<LI>Third level: Indented or nested line two</LI>\
</UL>\

<BR><BR><BR><U><DIV><BR></DIV></U></font>', POSITION=(0.938 0.938),
MARKUP=ON, WRAP=ON, DIMENSION=(6.563 4.167), $
COMPONENT='DfltCmpt1', POSITION=(0 0), DIMENSION=(0 0), $
END
SET COMPONENT='DfltCmpt1'
TABLE FILE SYSCOLUM
" "
SUM TBNAME NOPRINT
IF READLIMIT EQ 1
ON TABLE SET PREVIEW ON
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
END
COMPOUND END

762

The output is:

9. Choosing a Display Format

The default bullet type is disc. You may also specify circle or square, as shown in the following
request.

SET HTMLARCHIVE=ON
COMPOUND LAYOUT PCHOLD FORMAT PPTX
UNITS=IN, $
SECTION=section1, LAYOUT=ON, MERGE=OFF, ORIENTATION=PORTRAIT,
PAGESIZE=Letter, SHOW_GLOBALFILTER=OFF, $
PAGELAYOUT=1, NAME='Page layout 1', text='Page layout 1',
BOTTOMMARGIN=0.5, TOPMARGIN=0.5, $
OBJECT=STRING, NAME='text1', TEXT='<font face="TREBUCHET MS" size=10>\
<UL type=square>\
<LI> line 1, showing a square </LI>\
<UL type=circle>\
<LI> line 2, showing a circle </LI>\
<UL type=disc>\
<LI> line 3, showing a disc </LI>\
</UL>\
<BR><BR><BR><U><DIV><BR></DIV></U></font>', POSITION=(0.938 0.938),
MARKUP=ON, WRAP=ON, DIMENSION=(6.563 4.167), $
COMPONENT='DfltCmpt1', POSITION=(0 0), DIMENSION=(0 0), $
END
SET COMPONENT='DfltCmpt1'
TABLE FILE SYSCOLUM
" "
SUM TBNAME NOPRINT
IF READLIMIT EQ 1
ON TABLE SET PREVIEW ON
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
END
COMPOUND END

Creating Reports With TIBCO® WebFOCUS Language

 763

Saving Report Output in PPTX Format

The output is:

Inserting Images In Various Elements of PowerPoint PPTX Reports

WebFOCUS supports the placement of images within each element or node of the report. An
image, such as a logo, gives corporate identity to a report, or provides visual appeal. Data
specific images can be placed in headers and footers to provide additional clarity and style.
The image must reside on the WebFOCUS Reporting Server in a directory named on EDAPATH
or APPPATH. If the file is not on the search path, supply the full path name.

All images will be placed in the defined area, based on the explicit positioning defined by the
POSITION attribute within the style sheet.

Images can be placed in any available WebFOCUS reporting node or element. Supported image
formats include .gif, .jpg, and .png. Images may be positioned and resized by using the
POSITION and SIZE attributes to set the x, y coordinates and height, width settings,
respectively. Justification of images is not supported.

Note: The highest quality image format for charts is PNG, which allows for transparency, as
well as better integration with the styling within slide backgrounds.

764

Syntax:

How to Insert Images Into WebFOCUS PPTX Reports

TYPE={REPORT|HEADING|data}, IMAGE={file|(column)}
[,BY=byfield] [,SIZE=(w h)] ,$

9. Choosing a Display Format

where:

REPORT

Embeds an image in the body of a report. The image appears in the background of the
report. REPORT is the default value.

HEADING

Embeds an image in a heading or footing. Valid values are TABHEADING, TABFOOTING,
FOOTING, HEADING, SUBHEAD, and SUBFOOT. Provide sufficient blank space in the
heading or footing so that the image does not overlap the heading or footing text. You may
also want to place heading or footing text to the right of the image using spot markers.

data

Defines a data column in which to place the image. Must be used with COLUMNS=column
title to identify the specific report column where the image should be anchored.

file

Is the name of the image file. It must reside on the WebFOCUS Reporting Server in a
directory named on EDAPATH or APPPATH. If the file is not on the search path, supply the
full path name. When specifying a GIF file, you can omit the file extension.

Example:

Inserting Images in the Headers and Footers of a Report

The following request inserts images in the headers and footers of a report.

Creating Reports With TIBCO® WebFOCUS Language

 765

Saving Report Output in PPTX Format

TABLE FILE EMPDATA
SUM
EMPDATA.EMPDATA.SALARY
BY LOWEST EMPDATA.EMPDATA.DEPT
BY EMPDATA.EMPDATA.LASTNAME
ON EMPDATA.EMPDATA.DEPT SUBFOOT "Subfoot"
" "
ON EMPDATA.EMPDATA.DEPT PAGE-BREAK
ON TABLE SUBHEAD
"Report Heading"
" "
HEADING
"Page Heading"
" "
FOOTING
"Page Footing"
" "
ON TABLE SUBFOOT "Report Footing"
" "
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
PAGESIZE='PPT Slide',
  ORIENTATION=LANDSCAPE,
$
TYPE=REPORT,
  OBJECT=STATUS-AREA,
  JUSTIFY=LEFT,
  PAGE-LOCATION=BOTTOM,
$

766

9. Choosing a Display Format

TYPE=REPORT,
  GRID=OFF,
  FONT='ARIAL',
  SIZE=12,
  STYLE=NORMAL,
  SQUEEZE=ON,
  TOPGAP=0.05,
  BOTTOMGAP=0.05,
  BORDER-COLOR=RGB(219 219 219),
  TITLELINE=SKIP,
  TOPMARGIN=.75,
  LEFTMARGIN=.5,
$
TYPE=TITLE,
  COLOR=RGB(51 51 51),
  STYLE=-UNDERLINE +BOLD,
$
TYPE=DATA,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$
TYPE=SUBTOTAL,
  STYLE=BOLD,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$
TYPE=TABHEADING,
  SIZE=14,
  JUSTIFY=LEFT,
$
TYPE=TABHEADING,
  IMAGE=smplogo1.gif,
  POSITION=(+4.500000 +0.000000),
$
TYPE=TABFOOTING,
  SIZE=10,
$

Creating Reports With TIBCO® WebFOCUS Language

 767

Saving Report Output in PPTX Format

TYPE=SUBHEAD,
  BACKCOLOR=RGB(246 246 246),
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$
TYPE=SUBHEAD,
  BY=1,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(102 102 102),
$
TYPE=SUBHEAD,
  OBJECT=FIELD,
  STYLE=BOLD,
$
TYPE=SUBFOOT,
  SIZE=9,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$
TYPE=TABFOOTING,
  IMAGE=smplogo1.gif,
  POSITION=(+4.500000 +0.000000),
$

TYPE=HEADING,
  SIZE=12,
$
TYPE=HEADING,
  IMAGE=poweredbyibi.gif,
  POSITION=(+4.500000 +0.000000),
$
TYPE=FOOTING,
  SIZE=10,
$
TYPE=FOOTING,
  STYLE=BOLD,
  JUSTIFY=LEFT,
  IMAGE=poweredbyibi.gif,
  POSITION=(+4.500000 +0.000000),
$
TYPE=SUBFOOT,
  SIZE=10,
$
TYPE=SUBFOOT,
  IMAGE=webfocus1.gif,
  POSITION=(+4.500000 +0.000000),
  SIZE=(1.000000 0.500000),
$
ENDSTYLE
END

768

The output is:

9. Choosing a Display Format

Example:

Inserting Images in the Data Cells of a Report

The following request inserts images in the data cells of a report.

Creating Reports With TIBCO® WebFOCUS Language

 769

Saving Report Output in PPTX Format

APP PATH IBISAMP IBIDEMO
TABLE FILE GGSALES
SUM DOLLARS/D17M AS 'Revenue'
COMPUTE Surplus/A15 = IF DOLLARS GE 4000000 THEN 'g1.gif' ELSE 'r1.gif';
BY REGION
BY ST
ON TABLE SUBHEAD
"Current Year Revenue"
FOOTING
"Revenue in excess of 4 million"
"Revenue less than 4 million"
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET SQUEEZE ON
ON TABLE SET STYLE *
TYPE=REPORT,
     GRID=OFF,
     FONT='ARIAL',
     SIZE=14,
     STYLE=NORMAL,
     SQUEEZE=ON,
     TOPGAP=0.05,
     BOTTOMGAP=0.05,
     BORDER-COLOR=RGB(219 219 219),
     TITLELINE=SKIP,
     ORIENTATION = LANDSCAPE,TOPMARGIN=1,LEFTMARGIN=1,
$
TYPE=DATA, COLUMN=Surplus, IMAGE=(Surplus), SIZE=(.2 .2),$
TYPE=FOOTING,IMAGE=g1.gif, position=(.122 .055), SIZE=(.2 .2 ),$
TYPE=FOOTING,line=1,item=1,position=.5,$
TYPE=FOOTING,IMAGE='r1.gif', position=(.122 .33), SIZE=(.2 .2),$
TYPE=FOOTING,line=2,item=1, position=.5,$
TYPE=DATA,
     BORDER-TOP=LIGHT,
     BORDER-TOP-COLOR=RGB(219 219 219),
$

770

9. Choosing a Display Format

TYPE=TITLE,
     COLOR=RGB(51 51 51),
     STYLE=-UNDERLINE +BOLD,
$
TYPE=TABHEADING,
     SIZE=18,
     JUSTIFY=LEFT,
$
TYPE=TABFOOTING,
     SIZE=10,
$
TYPE=HEADING,
     JUSTIFY=LEFT,
     SIZE=12,
$
TYPE=SUBHEAD,
     BACKCOLOR=RGB(246 246 246),
     BORDER-TOP=LIGHT,
     BORDER-TOP-COLOR=RGB(219 219 219),
$
TYPE=SUBHEAD,
      BY=1,
      BORDER-TOP=LIGHT,
      BORDER-TOP-COLOR=RGB(102 102 102),
$
TYPE=SUBHEAD,
     OBJECT=FIELD,
     STYLE=BOLD,
$
TYPE=SUBFOOT,
     SIZE=9,
     BORDER-TOP=LIGHT,
     BORDER-TOP-COLOR=RGB(219 219 219),
$
END

Creating Reports With TIBCO® WebFOCUS Language

 771

Saving Report Output in PPTX Format

The report output is as follows:

Displaying PPTX Charts in PNG Image Format

The PPTXGRAPHTYPE attribute enhances the quality of charts embedded into PowerPoint
(PPTX) slides. As of Release 8.2.01M, you can use the PNG output format to enhance the
image and text quality and support transparency.

This is useful for a number of important scenarios, including use of templates with background
color and for overlapping a chart with other components and drawing objects.

Syntax:

How to Display PPTX Charts in PNG Image Format

SET PPTXGRAPHTYPE={PNG|PNG_NOSCALE|JPEG}

772

9. Choosing a Display Format

where:

PNG

Scales the PNG image to twice its dimensions to get significantly improved quality. This
may cause problems if you have non-scalable items in the chart, such as text with
absolute point sizes (including embedded scales headings). The output file is also larger
due to the larger bitmap. Text within the chart is noticeable sharper than the legacy JPEG
format.

PNG preserves font sizes in the chart when it is internally rescaled for increased
resolution. It converts absolute font sizes set in the stylesheet (*GRAPH_SCRIPT) to sizes
expressed in virtual coordinates (which are relative to the dimensions of the chart) and
generates font sizes for embedded headings and footings in virtual coordinates.

PNG_NOSCALE

Renders in PNG, but does not scale. This produces slightly better quality than JPEG. Going
from JPEG to PNG_NOSCALE makes the chart sharper, but has only a slight effect on the
text.

JPEG

Indicates legacy format. This is the default value.

Example:

Displaying a PNG Chart With Transparency

Transparency enables greater control over how components and drawing objects can be placed
together on a slide. The following report contains a text box, report, and chart that can be
intertwined on the page because the background of the chart does not cover the contents of
the other objects.

SET PPTXGRAPHTYPE=PNG

COMPOUND LAYOUT PCHOLD FORMAT PPTX
UNITS=IN, $
SECTION=section1, LAYOUT=ON, MERGE=OFF, ORIENTATION=LANDSCAPE,
PAGESIZE=PPT Slide, $
PAGELAYOUT=1, NAME='Page layout 1', text='Page layout 1',
BOTTOMMARGIN=0.5, TOPMARGIN=0.5, $
COMPONENT='report1', TEXT='report1', POSITION=(5.088 1.375),
DIMENSION=(2.260 2.500), $
COMPONENT='chart2', TEXT='chart2', POSITION=(0.815 1.351),
DIMENSION=(5.104 2.917), COMPONENT-TYPE=GRAPH,  $
OBJECT=STRING, NAME='text1', TEXT='<left>PNG charts can be defined with
transparency to allow the background to show through and allow for
overlapping components to optimize the use of space on the slide.
</left>',
POSITION=(0.500 0.979), MARKUP=ON, WRAP=ON, DIMENSION=(4.635 0.729),
font='TREBUCHET MS', color=RGB(0 0 0), size=10, $
END

Creating Reports With TIBCO® WebFOCUS Language

 773

Saving Report Output in PPTX Format

SET COMPONENT='report1'
TABLE FILE GGSALES
SUM
   GGSALES.SALES01.DOLLARS
BY GGSALES.SALES01.REGION
ACROSS LOWEST GGSALES.SALES01.CATEGORY
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/ibi_themes/Warm.sty,$
$
ENDSTYLE
END

SET COMPONENT='chart2'
GRAPH FILE ggsales
SUM GGSALES.SALES01.DOLLARS
BY GGSALES.SALES01.CATEGORY
ACROSS GGSALES.SALES01.REGION
ON GRAPH PCHOLD FORMAT HTML
ON GRAPH SET VZERO OFF
ON GRAPH SET HTMLENCODE ON
ON GRAPH SET GRAPHDEFAULT OFF
ON GRAPH SET EMBEDHEADING ON
ON GRAPH SET GRWIDTH 1
ON GRAPH SET UNITS 'PIXELS'
ON GRAPH SET HAXIS 770.0
ON GRAPH SET VAXIS 405.0
ON GRAPH SET GRMERGE ADVANCED
ON GRAPH SET GRMULTIGRAPH 0
ON GRAPH SET GRLEGEND 1
ON GRAPH SET GRXAXIS 1
ON GRAPH SET LOOKGRAPH HBAR
ON GRAPH SET STYLE *

774

9. Choosing a Display Format

*GRAPH_SCRIPT
setPieDepth(0);
setPieTilt(0);
setDepthRadius(0);
setPlace(true);
setCurveFitEquationDisplay(false);
*END
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/ibi_themes/Warm.sty,$
TYPE=REPORT, TITLETEXT='WebFOCUS Report', $
*GRAPH_SCRIPT
setFillColor(getChartBackground(),new Color(255,255,255,0));
setLegendPosition(4);
*GRAPH_JS_FINAL
"blaProperties": {
    "orientation": "horizontal"
},
"agnosticSettings": {
    "chartTypeFullName": "Bar_Clustered_Horizontal"
}
*END
ENDSTYLE
END
-RUN

COMPOUND END

The output is:

Example:

Displaying a PNG Image With Transparency in a Designated Template

The following compound report places a chart defined with transparency on a slide from the
designated template that contains background colors and patterns.

Creating Reports With TIBCO® WebFOCUS Language

 775

Saving Report Output in PPTX Format

SET PPTXGRAPHTYPE=PNG

COMPOUND LAYOUT PCHOLD FORMAT PPTX
UNITS=IN, $
SECTION=section1, LAYOUT=ON, MERGE=OFF, ORIENTATION=LANDSCAPE,
PAGESIZE=Letter, $
PAGELAYOUT=1, NAME='Page layout 1', text='Page layout 1', $
COMPONENT='ppt_template', $
COMPONENT='chart1', TEXT='chart1', POSITION=(0.500 2.10),
DIMENSION=(9.336 3.437),
COMPONENT-TYPE=GRAPH, ARREPORTSIZE=DIMENSION, $
END

SET COMPONENT='ppt_template'
TABLE FILE SYSCOLUM
SUM TBNAME NOPRINT
IF READLIMIT EQ 1
ON TABLE PCHOLD FORMAT PPTX TEMPLATE 'golden.potx' SLIDENUMBER 1
END

SET COMPONENT='chart1'
GRAPH FILE ggsales
SUM GGSALES.SALES01.DOLLARS
BY GGSALES.SALES01.CATEGORY
BY GGSALES.SALES01.REGION
BY GGSALES.SALES01.ST
ON GRAPH PCHOLD FORMAT HTML
ON GRAPH SET EMBEDHEADING ON
ON GRAPH SET GRWIDTH 1
ON GRAPH SET UNITS PIXELS
ON GRAPH SET HAXIS 770.0
ON GRAPH SET VAXIS 405.0
ON GRAPH SET GRMERGE ADVANCED
ON GRAPH SET GRMULTIGRAPH 1
ON GRAPH SET GRLEGEND 0
ON GRAPH SET GRXAXIS 2
ON GRAPH SET LOOKGRAPH VBAR
ON GRAPH SET STYLE *

776

9. Choosing a Display Format

*GRAPH_SCRIPT
setPieDepth(0);
setPieTilt(0);
setDepthRadius(0);
setCurveFitEquationDisplay(false);
setPlace(true);
*END
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/ibi_themes/Warm.sty,$
TYPE=REPORT, TITLETEXT='WebFOCUS Report', $
*GRAPH_SCRIPT
setFillType(getChartBackground(),2);
setGradientNumPins(getChartBackground(),2);
setFillColor(getChartBackground(),new Color(255,255,255,0));
setFillType(getChartBackground(),1);
*END
ENDSTYLE
END
-RUN
COMPOUND END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 777

Saving Report Output in PPTX Format

Drill Down From Microsoft PowerPoint

Two types of drill downs are supported:

WebFOCUS content

External URL

When working in the WebFOCUS Repository or Content environment, drill-down hyperlinks in
PPTX reports will not work when Microsoft PowerPoint opens in a PowerPoint application
window instead of in a browser. The current security context and any previously established
session-related cookies are not retained and this changes user authorization. The
recommendation is to configure one of the three security models described below, to allow
successful drill down from reports displayed in a Microsoft PowerPoint application.

The Remember Me Security Model

The Remember Me Security model is a method of user authentication that enables WebFOCUS
to store a trusted sign-in cookie locally, on the workstation, for a default period of 14 days.
WebFOCUS does not however, store the user password in the sign-in cookie. Enable the
Remember Me feature on the Sign-in page. If the end-user uses the Remember Me feature, a
persistent cookie is used.

Public Access

Public Access is useful for procedures that are available to everyone within an organization or
the general public and do not require authentication. Set up WebFOCUS security such that the
PUBLIC user has the necessary permissions to drill down to reports.

Integrated Windows Authentication

Integrated Windows Authentication (IWA) is enabled by configuring the browser. Use SSO with
IIS/Tomcat Integrated Windows Authentication. Renegotiation occurs automatically and the
PowerPoint formatted reports display correctly.

Refer to the WebFOCUS Security and Administration manual for details on these authentication
models.

Example:

Drilling Down to an External URL

The following request places a reference to an external URL on the grand total line tag.

778

9. Choosing a Display Format

TABLE FILE GGSALES
SUM
  GGSALES.SALES01.BUDDOLLARS/D12CM
  GGSALES.SALES01.DOLLARS/D12CM
BY GGSALES.SALES01.REGION
BY GGSALES.SALES01.CATEGORY
BY GGSALES.SALES01.PRODUCT
HEADING
"REVENUE BY REGION "
ON GGSALES.SALES01.REGION SUBTOTAL AS '*TOTAL'
WHERE GGSALES.SALES01.CATEGORY NE 'Gifts';
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE COLUMN-TOTAL AS 'TOTAL'
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
PAGESIZE='PPT Slide',
  ORIENTATION=LANDSCAPE,
$

Creating Reports With TIBCO® WebFOCUS Language

 779

Saving Report Output in PPTX Format

TYPE=REPORT,
  OBJECT=STATUS-AREA,
  JUSTIFY=LEFT,
  PAGE-LOCATION=BOTTOM,
$
TYPE=REPORT,
  GRID=OFF,
  FONT='ARIAL',
  SIZE=12,
  STYLE=NORMAL,
  SQUEEZE=ON,
  TOPGAP=0.05,
  BOTTOMGAP=0.05,
  BORDER-COLOR=RGB(219 219 219),
  TITLELINE=SKIP,
  TOPMARGIN=1,
  LEFTMARGIN=1,
$
TYPE=TITLE,
  COLOR=RGB(51 51 51),
  STYLE=-UNDERLINE +BOLD,
$
TYPE=DATA,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$
TYPE=HEADING,
  JUSTIFY=LEFT,
  SIZE=14,
$
TYPE=SUBTOTAL,
  STYLE=BOLD,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$
TYPE=GRANDTOTAL,
  OBJECT=TAG,
  URL=http://www.ibi.com,
$

TYPE=REPORT,
  OBJECT=STATUS-AREA,
  JUSTIFY=LEFT,
  PAGE-LOCATION=BOTTOM,
$
TYPE=GRANDTOTAL,
  COLOR=RGB(51 51 51),
  STYLE=BOLD,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(102 102 102),
$
ENDSTYLE
END

780

The output is:

9. Choosing a Display Format

PowerPoint PPTX Presentations Using Templates

PPTX report output can be generated based on PowerPoint templates. This feature allows for
the integration of WebFOCUS reports into presentations containing multiple slides. Any native
PowerPoint template can be used to generate a new presentation containing a WebFOCUS
report.

The following PowerPoint file types can be used as template files to generate PPTX
presentations.

Template File Type

Presentation Output Generated

Template (.potx)

Presentation (.pptx)

Macro-Enabled Template (.potm)

Macro-Enabled presentation (.pptm)

Presentation (.pptx)

Presentation (.pptx)

Macro-Enabled presentation (.pptm)

Macro-Enabled presentation (.pptm)

Creating Reports With TIBCO® WebFOCUS Language

 781

Saving Report Output in PPTX Format

Note: For more information on working with active content in macro-enabled templates, see the
Microsoft webpage: https://support.office.com/en-nz/article/Enable-or-disable-macros-in-Office-
documents-7b4fdd2e-174f-47e2-9611-9efe4f860b12

Example:

Using Standard PowerPoint Templates (POTX)

In the following request, the report occupies multiple slides. The designated slide is replaced
by as many slides as are needed to display the report output.

TABLE FILE TRAINING
SUM
TRAINING.TRAINING.EXPENSES/D12CM
BY TRAINING.TRAINING.LOCATION
BY TRAINING.TRAINING.PIN
BY LOWEST TRAINING.TRAINING.COURSECODE
BY TRAINING.TRAINING.COURSESTART
BY TRAINING.TRAINING.GRADE
ON TRAINING.TRAINING.LOCATION SUBTOTAL AS 'TOTAL EXPENSES FOR'
ON TRAINING.TRAINING.LOCATION PAGE-BREAK
HEADING
"MONTHLY EXPENSES BY STATE"
" "
ON TABLE SET ASNAMES ON
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT PPTX TEMPLATE 'ibi_template.potx' SLIDENUMBER 2
ON TABLE SET STYLE *
PAGESIZE='PPT Slide',
  ORIENTATION=LANDSCAPE,
$
TYPE=REPORT,
  OBJECT=STATUS-AREA,
  JUSTIFY=LEFT,
  PAGE-LOCATION=BOTTOM,
$
TYPE=REPORT,
  GRID=OFF,
  FONT='ARIAL',
  SIZE=14,
  STYLE=NORMAL,
  SQUEEZE=ON,
  TOPGAP=0.05,
  BOTTOMGAP=0.05,
  BORDER-COLOR=RGB(219 219 219),
  TITLELINE=SKIP,
  TOPMARGIN=.1,
  LEFTMARGIN=1.5,
$

782

9. Choosing a Display Format

TYPE=TITLE,
  COLOR=RGB(51 51 51),
  STYLE=-UNDERLINE +BOLD,
$
TYPE=DATA,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$
TYPE=HEADING,
  JUSTIFY=LEFT,
  SIZE=16,
$
TYPE=SUBTOTAL,
  STYLE=BOLD,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$
ENDSTYLE
END

The output is:

Example:

Using a Multi-Report Request to Populate Designated Slides in a Template

The following request is a technique for inserting different components across multiple slides.

Creating Reports With TIBCO® WebFOCUS Language

 783

Saving Report Output in PPTX Format

-* Replace Slide #2
TABLE FILE GGSALES
HEADING
"FIRST SLIDE"
SUM
DOLLARS/D12CM UNITS
BY REGION AS 'My Field'
BY CATEGORY
ON TABLE COLUMN-TOTAL
ON TABLE HOLD AS SLIDE_A FORMAT PPTX TEMPLATE 'ibi_template.potx'
SLIDENUMBER 2
ON TABLE SET STYLE *
TYPE=REPORT,
  OBJECT=STATUS-AREA,
  JUSTIFY=LEFT,
  PAGE-LOCATION=BOTTOM,
$
TYPE=REPORT,
  GRID=OFF,
  FONT='ARIAL',
  SIZE=14,
  STYLE=NORMAL,
  SQUEEZE=ON,
  TOPGAP=0.05,
  BOTTOMGAP=0.05,
  BORDER-COLOR=RGB(219 219 219),
  TITLELINE=SKIP,
  ORIENTATION = LANDSCAPE,
  TOPMARGIN=.1,
  LEFTMARGIN=1.5,
$
TYPE=TITLE,
  COLOR=RGB(51 51 51),
  STYLE=-UNDERLINE +BOLD,
$

784

9. Choosing a Display Format

TYPE=DATA,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$
TYPE=HEADING,
  JUSTIFY=LEFT,
  SIZE=16,
$
TYPE=DATA,
  COLUMN=DOLLARS,
  COLOR=BLUE,
$
TYPE=REPORT,
  COLUMN=REGION,
  COLOR=RED,
$
TYPE=REPORT,
  COLUMN=CATEGORY,
  COLOR=GREEN,
$
TYPE=GRANDTOTAL,
  COLOR=RGB(51 51 51),
  STYLE=BOLD,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(102 102 102),
$
END
-* Replace Slide #3
TABLE FILE GGSALES HEADING
"SECOND SLIDE"
SUM DOLLARS/D12CM UNITS
BY REGION AS 'My Field'
BY CATEGORY
ON TABLE COLUMN-TOTAL
ON TABLE HOLD AS SLIDE_1 FORMAT PPTX TEMPLATE 'slide_a.pptx' SLIDENUMBER 3
ON TABLE COLUMN-TOTAL
ON TABLE SET STYLE *
$
TYPE=REPORT,
  OBJECT=STATUS-AREA,
  JUSTIFY=LEFT,
  PAGE-LOCATION=BOTTOM,
$

Creating Reports With TIBCO® WebFOCUS Language

 785

Saving Report Output in PPTX Format

TYPE=REPORT,
  GRID=OFF,
  FONT='ARIAL',
  SIZE=14,
  STYLE=NORMAL,
  SQUEEZE=ON,
  TOPGAP=0.05,
  BOTTOMGAP=0.05,
  BORDER-COLOR=RGB(219 219 219),
  TITLELINE=SKIP,
  ORIENTATION = LANDSCAPE,
  TOPMARGIN=.1,
  LEFTMARGIN=1.5,
$
TYPE=TITLE,
  COLOR=RGB(51 51 51),
  STYLE=-UNDERLINE +BOLD,
$
TYPE=DATA,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$
TYPE=HEADING,
  JUSTIFY=LEFT,
  SIZE=16,
$
TYPE=DATA,
  COLUMN=DOLLARS,
  COLOR=BLUE,
$
TYPE=REPORT,
  COLUMN=REGION,
  COLOR=RED,
$
TYPE=REPORT,
  COLUMN=CATEGORY,
  COLOR=GREEN,
$
TYPE=GRANDTOTAL,
  COLOR=RGB(51 51 51),
  STYLE=BOLD,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(102 102 102),
$
END

786

9. Choosing a Display Format

-* Replace Slide #4
TABLE FILE GGSALES
HEADING
"THIRD SLIDE"
SUM
DOLLARS/D12CM
UNITS
BY REGION AS 'My Field'
BY CATEGORY
ON TABLE COLUMN-TOTAL
ON TABLE PCHOLD AS THRID_SLIDE FORMAT PPTX TEMPLATE 'SLIDE_1.pptx'
SLIDENUMBER 4
ON TABLE SET STYLE *
TYPE=REPORT,
  OBJECT=STATUS-AREA,
  JUSTIFY=LEFT,
  PAGE-LOCATION=BOTTOM,
$
TYPE=REPORT,
  GRID=OFF,
  FONT='ARIAL',
  SIZE=14,
  STYLE=NORMAL,
  SQUEEZE=ON,
  TOPGAP=0.05,
  BOTTOMGAP=0.05,
  BORDER-COLOR=RGB(219 219 219),
  TITLELINE=SKIP,
  ORIENTATION = LANDSCAPE,
  TOPMARGIN=.1,
  LEFTMARGIN=1.5,
$
TYPE=TITLE,
  COLOR=RGB(51 51 51),
  STYLE=-UNDERLINE +BOLD,
$
TYPE=DATA,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$
TYPE=HEADING,
  JUSTIFY=LEFT,
  SIZE=16,

Creating Reports With TIBCO® WebFOCUS Language

 787

Saving Report Output in PPTX Format

$
TYPE=DATA,
  COLUMN=DOLLARS,
  COLOR=BLUE,
$
TYPE=REPORT,
  COLUMN=REGION,
  COLOR=RED,
$
TYPE=REPORT,
  COLUMN=CATEGORY,
  COLOR=GREEN,
$
TYPE=GRANDTOTAL,
  COLOR=RGB(51 51 51),
  STYLE=BOLD,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(102 102 102),
$
END

The output is:

PowerPoint PPTX Compound Syntax

PowerPoint Compound Documents generate presentations that may contain multiple slides.
The components of a PowerPoint Compound Document can include standard tables and
charts.

788

Example:

Generating a Compound Document

The following request creates a slide deck, which presents the selected information in
standard tables and charts.

9. Choosing a Display Format

SET HTMLARCHIVE=ON
COMPOUND LAYOUT PCHOLD FORMAT PPTX
UNITS=IN, $
SECTION=section1, LAYOUT=ON, MERGE=OFF,
ORIENTATION=LANDSCAPE, PAGESIZE=PPT Slide, SHOW_GLOBALFILTER=OFF, $
PAGELAYOUT=1, NAME='Page layout 1', text='Page layout 1',
BOTTOMMARGIN=0.2, TOPMARGIN=0.5, LEFTMARGIN=2.0, $
COMPONENT='chart1', TEXT='chart1', POSITION=(0.707 0.520),
DIMENSION=(8.750 2.917), COMPONENT-TYPE=GRAPH, $
COMPONENT='report1', TEXT='report1', POSITION=(0.500 3.542),
DIMENSION=(9.271 3.646), $
END
SET COMPONENT='chart1'
ENGINE INT CACHE SET ON
-DEFAULTH &WF_STYLE_UNITS='PIXELS';
-DEFAULTH &WF_STYLE_HEIGHT='405.0';
-DEFAULTH &WF_STYLE_WIDTH='770.0';
-DEFAULTH &WF_TITLE='WebFOCUS Report';
GRAPH FILE ibisamp/ggsales
SUM GGSALES.SALES01.DOLLARS
BY GGSALES.SALES01.REGION
BY TOTAL HIGHEST GGSALES.SALES01.DOLLARS NOPRINT
BY GGSALES.SALES01.ST
ON GRAPH PCHOLD FORMAT PPTX
ON GRAPH SET HTMLENCODE ON
ON GRAPH SET GRAPHDEFAULT OFF
ON GRAPH SET ARGRAPHENGIN JSCHART
ON GRAPH SET EMBEDHEADING ON
ON GRAPH SET VZERO OFF
ON GRAPH SET GRWIDTH 1

Creating Reports With TIBCO® WebFOCUS Language

 789

Saving Report Output in PPTX Format

ON GRAPH SET UNITS &WF_STYLE_UNITS
ON GRAPH SET HAXIS &WF_STYLE_WIDTH
ON GRAPH SET VAXIS &WF_STYLE_HEIGHT
ON GRAPH SET GRMERGE ADVANCED
ON GRAPH SET GRMULTIGRAPH 1
ON GRAPH SET GRLEGEND 0
ON GRAPH SET GRXAXIS 2
ON GRAPH SET LOOKGRAPH VBAR
ON GRAPH SET STYLE *
*GRAPH_SCRIPT
setPieDepth(0);
setPieTilt(0);
setDepthRadius(0);
setCurveFitEquationDisplay(false);
setPlace(true);
setPieFeelerTextDisplay(1);
setUseSeriesShapes(true);
setMarkerSizeDefault(50);
*END
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/javaassist/intl/EN/combine_templates/
warm.sty,$
TYPE=REPORT, TITLETEXT=&WF_TITLE.QUOTEDSTRING, $
*GRAPH_SCRIPT
setReportParsingErrors(false);
setSelectionEnableMove(false);
setFillType(getSeries(0),2);
setGradientPinLeftColor0(getSeries(0),new Color(0,127,192));
setGradientPinRightColor0(getSeries(0),new Color(0,127,192));
setGradientPinLeftColor2(getSeries(0),new Color(0,127,192));
setGradientPinRightColor2(getSeries(0),new Color(0,127,192));
setGradientPinLeftColor1(getSeries(0),new Color(0,64,128));
setGradientPinRightColor1(getSeries(0),new Color(0,64,128));
setGradientPinPosition0(getSeries(0),0.0);
setGradientPinPosition1(getSeries(0),1.0);
setPieTilt(0);
setPieDepth(0);
setDepthRadius(0);
setDepthAngle(0);
setFillType(getSeries(7),2);
setGradientPinPosition0(getSeries(7),0.0);
setGradientPinPosition1(getSeries(7),1.0);
setFillType(getSeries(9),2);
setGradientDirection(getSeries(9),16);
setGradientPinPosition0(getSeries(9),0.0);
setGradientPinPosition1(getSeries(9),1.0);
*END
ENDSTYLE
END
-RUN

790

9. Choosing a Display Format

SET COMPONENT='report1'
TABLE FILE IBISAMP/GGSALES
SUM
  GGSALES.SALES01.BUDDOLLARS/D12CM
  GGSALES.SALES01.DOLLARS/D12CM
  GGSALES.SALES01.BUDUNITS/D12C
  GGSALES.SALES01.UNITS/D12C
BY GGSALES.SALES01.REGION
BY GGSALES.SALES01.PRODUCT
ON GGSALES.SALES01.REGION SUBTOTAL AS 'TOTAL FOR:'
ON GGSALES.SALES01.REGION PAGE-BREAK
HEADING
"Q3 SALES REPORT BY REGION"
WHERE GGSALES.SALES01.PRODUCT NE 'Coffee Pot' OR 'Mug' OR 'Thermos';
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE SET ASNAMES ON
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
  PAGESIZE='PPT Slide',
  LEFTMARGIN=1.000000,
  TOPMARGIN=0.500000,
  BOTTOMMARGIN=0.000000,
  SQUEEZE=ON,
  ORIENTATION=LANDSCAPE,
$
TYPE=REPORT,
  BORDER-TOP-COLOR=RGB(219 219 219),
  BORDER-BOTTOM-COLOR=RGB(219 219 219),
  BORDER-LEFT-COLOR=RGB(219 219 219),
  BORDER-RIGHT-COLOR=RGB(219 219 219),
  FONT='ARIAL',
  SIZE=12,
    TITLELINE=SKIP,
  STYLE=NORMAL,
  TOPGAP=0.041667,
$
TYPE=DATA,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$

Creating Reports With TIBCO® WebFOCUS Language

 791

Saving Report Output in PPTX Format

TYPE=TITLE,
  COLOR=RGB(51 51 51),
  STYLE=-UNDERLINE+BOLD,
$
TYPE=HEADING,
  SIZE=14,
  JUSTIFY=LEFT,
$
TYPE=SUBTOTAL,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
  STYLE=BOLD,
$
TYPE=REPORT,
  OBJECT=STATUS-AREA,
  JUSTIFY=LEFT,
  PAGE-LOCATION=BOTTOM,
$
ENDSTYLE
END
COMPOUND END

The resulting Compound Document output is:

792

Coordinated Compound Layout Reports

9. Choosing a Display Format

A Coordinated Compound Layout report is coordinated so that all reports and graphs that
contain a common sort field are burst into separate page layouts. Pages are generated for
each value of the common sort field, with every component displaying the data it retrieved for
that value on that page. You create a Coordinated Compound Layout report by specifying
MERGE=ON in the SECTION declaration for the Compound Layout report.

In a Coordinated Compound Layout report, if at least one component contains data for a
specific sort field value, a page is generated for that value even though some of the
components may be missing.

While the length of the report will always include all of the rows of data generated by the query,
the width of the report is limited by the size of the defined component container. This means
that paneling is not supported for Compound Reports, although it is for non-Compound PPTX
Reports.

If the width of the report data is wider than the defined page size, a panel (or horizontal
overflow page) is automatically generated.

In legacy compound syntax, if one of the component reports is too large to fit within the
defined page width, execution is halted and the user is presented with an error message
stating that paneling is not supported.

In Compound Layout syntax, if a component is too wide to fit within the defined container, the
report wraps the contents within the container. The container size is defined through a
combination of the POSITION and DIMENSIONS parameters for the component within the
compound syntax.

Example:

Generating a Coordinated Compound Layout Report

The following request generates a Coordinated Compound Layout report. This Compound
Report is coordinated by Region, so that individual slides are generated for each value of the
primary Key, Region.

Creating Reports With TIBCO® WebFOCUS Language

 793

Saving Report Output in PPTX Format

SET HTMLARCHIVE=ON
*-HOLD_SOURCE
COMPOUND LAYOUT PCHOLD FORMAT PPTX
UNITS=IN, $
SECTION=section1, LAYOUT=ON, MERGE=ON, ORIENTATION=LANDSCAPE,
PAGESIZE=PPT Slide, SHOW_GLOBALFILTER=OFF,$
PAGELAYOUT=1, NAME='Page layout 1', text='Page layout 1', BOTTOMMARGIN=0.5,
TOPMARGIN=0.5, $
COMPONENT='report1', TEXT='report1', POSITION=(0.500 0.625),
DIMENSION=(* *), $
COMPONENT='report2', TEXT='report2', POSITION=(0.712 0.771),
DIMENSION=(* *), $
COMPONENT='report3', TEXT='report3', POSITION=(5.702 0.759),
DIMENSION=(* *), $
END
SET COMPONENT='report1'
TABLE FILE WF_RETAIL
BY WF_RETAIL.WF_RETAIL_GEOGRAPHY_CUSTOMER.BUSINESS_REGION NOPRINT
HEADING
"PROFIT REPORTS FOR <WF_RETAIL.WF_RETAIL_GEOGRAPHY_CUSTOMER.BUSINESS_REGION
<+15>
DISCOUNTS APPLIED: <WF_RETAIL.WF_RETAIL_GEOGRAPHY_CUSTOMER.BUSINESS_REGION"
" "
ON TABLE SET ASNAMES ON
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *

794

9. Choosing a Display Format

TYPE=REPORT,
  GRID=OFF,
  FONT='ARIAL',
  SIZE=9,
  STYLE=NORMAL,
  SQUEEZE=ON,
  TOPGAP=0.05,
  BOTTOMGAP=0.05,
  PAGECOLOR='WHITE',
  BORDER-COLOR=RGB(219 219 219),
  TITLELINE=SKIP,
    TOPMARGIN=.5,
    LEFTMARGIN=.15,
$
TYPE=HEADING,
  JUSTIFY=LEFT,
  SIZE=14,
$
ENDSTYLE
END
SET COMPONENT='report2'
TABLE FILE WF_RETAIL
SUM
WF_RETAIL.WF_RETAIL_SALES.COGS_US
WF_RETAIL.WF_RETAIL_SALES.GROSS_PROFIT_US
BY WF_RETAIL.WF_RETAIL_GEOGRAPHY_CUSTOMER.BUSINESS_REGION NOPRINT
BY WF_RETAIL.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY
ON WF_RETAIL.WF_RETAIL_GEOGRAPHY_CUSTOMER.BUSINESS_REGION SUBTOTAL AS
'TOTAL FOR'
ON TABLE SET ASNAMES ON
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
PAGESIZE='PPT Slide',
  ORIENTATION=LANDSCAPE,
$
TYPE=REPORT,
  OBJECT=STATUS-AREA,
  JUSTIFY=LEFT,
  PAGE-LOCATION=BOTTOM,
$

Creating Reports With TIBCO® WebFOCUS Language

 795

Saving Report Output in PPTX Format

TYPE=REPORT,
  GRID=OFF,
  FONT='ARIAL',
  SIZE=14,
  STYLE=NORMAL,
  SQUEEZE=ON,
  TOPGAP=0.05,
  BOTTOMGAP=0.05,
  PAGECOLOR='WHITE',
  BORDER-COLOR=RGB(219 219 219),
  TITLELINE=SKIP,
    TOPMARGIN=.5,
    LEFTMARGIN=.15,
$
TYPE=DATA,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$
TYPE=TITLE,
  COLOR=RGB(51 51 51),
  STYLE=-UNDERLINE +BOLD,
$
TYPE=DATA,
  COLUMN=ROWTOTAL(*),
  STYLE=BOLD,
$
TYPE=TITLE,
  COLUMN=ROWTOTAL(*),
  COLOR=RGB(51 51 51),
  STYLE=-UNDERLINE +BOLD,
$
TYPE=SUBTOTAL,
  STYLE=BOLD,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$
ENDSTYLE
END
SET COMPONENT='report3'
TABLE FILE WF_RETAIL
SUM
WF_RETAIL.WF_RETAIL_SALES.DISCOUNT_US
BY WF_RETAIL.WF_RETAIL_GEOGRAPHY_CUSTOMER.BUSINESS_REGION NOPRINT
BY WF_RETAIL.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY
ON WF_RETAIL.WF_RETAIL_GEOGRAPHY_CUSTOMER.BUSINESS_REGION SUBTOTAL
AS 'TOTAL FOR'

796

9. Choosing a Display Format

ON TABLE SET ASNAMES ON
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
PAGESIZE='PPT Slide',
  ORIENTATION=LANDSCAPE,
$
TYPE=REPORT,
  OBJECT=STATUS-AREA,
  JUSTIFY=LEFT,
  PAGE-LOCATION=BOTTOM,
$
TYPE=REPORT,
  GRID=OFF,
  FONT='ARIAL',
  SIZE=14,
  STYLE=NORMAL,
  SQUEEZE=ON,
  TOPGAP=0.05,
  BOTTOMGAP=0.05,
  PAGECOLOR='WHITE',
  BORDER-COLOR=RGB(219 219 219),
  TITLELINE=SKIP,
$
TYPE=DATA,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$
TYPE=TITLE,
  COLOR=RGB(51 51 51),
  STYLE=-UNDERLINE +BOLD,
$
TYPE=DATA,
  COLUMN=ROWTOTAL(*),
  STYLE=BOLD,
$

TYPE=TITLE,
  COLUMN=ROWTOTAL(*),
  COLOR=RGB(51 51 51),
  STYLE=-UNDERLINE +BOLD,
$
TYPE=SUBTOTAL,
  STYLE=BOLD,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$
ENDSTYLE
END
COMPOUND END

Creating Reports With TIBCO® WebFOCUS Language

 797

Saving Report Output in PPTX Format

The output is:

Templates for Compound Reports

For Compound Reports, the template is defined in the first component report. For compound
reports with Page Masters, this table will be the default table used to substantiate the page
layout. For uncoordinated standard compound reports, this default component can be created
using the system table, as shown in the following request.

SET COMPONENT='ppt_template'
TABLE FILE SYSCOLUM
SUM TBNAME NOPRINT
IF READLIMIT EQ 1
ON TABLE PCHOLD FORMAT PPTX TEMPLATE 'template_plus.potx' SLIDENUMBER 1
END

For Coordinated Compound Reports, this table must contain the same primary key as the other
components in the report. This includes any preprocessing of the data to define the universe of
available primary key values including JOINS and DEFINES.

SET COMPONENT='ppt_template'
TABLE FILE GGSALES
BY REGION NOPRINT
IF READLIMIT EQ 1
ON TABLE PCHOLD FORMAT PPTX TEMPLATE 'template_plus.potx' SLIDENUMBER 1
END

798

9. Choosing a Display Format

Adding Images to a Compound Request

Images may be inserted on the Page Master, Page Layout, and PowerPoint template (POTX) to
enhance the Compound Document. Images inserted on the Page Master will be visible on
every Page Layout within the Compound Document. Images on a Page Layout will be displayed
only on that page. If the Document is to be displayed on a PowerPoint Template, images may
be saved on the Template so that they will be displayed as positioned on the individual slides.

Important: Compound Layout syntax cannot contain hidden carriage return or line feed
characters. For purposes of presenting this example, line feed characters have been added so
that the sample code wraps to fit within the printed page. To run this example in your
environment, copy the code into a text editor and delete any line feed characters within the
Compound Layout syntax by going to the end of each line and pressing the Delete key.

Example:

Adding Images to a Compound Request

The following compound syntax creates a Document with images in the Page Master, the Page
Layout, and that is displayed on a PowerPoint template on which an image has been inserted.

SET HTMLARCHIVE=ON
*-HOLD_SOURCE
COMPOUND LAYOUT PCHOLD FORMAT PPTX
UNITS=IN, $
SECTION=section1, LAYOUT=ON, MERGE=OFF,
ORIENTATION=LANDSCAPE, PAGESIZE=PPT Slide, SHOW_GLOBALFILTER=OFF, $
PAGELAYOUT=ALL, NAME='Page Master', $
COMPONENT='ppt_template', $
OBJECT=BOX, NAME='line1', POSITION=(0.052 0.500), DIMENSION=(10.000 0.031),
BACKCOLOR=RGB(176 196 222), BORDER-COLOR=RGB(176 196 222), $
OBJECT=BOX, NAME='line2', POSITION=(-12.000 -10.000), DIMENSION=(0.000
0.000), BACKCOLOR=BLACK, BORDER-COLOR=BLACK, $
OBJECT=BOX, NAME='line3', POSITION=(0.479 0.000), DIMENSION=(0.025 7.600),
BACKCOLOR=RGB(176 196 222), BORDER-COLOR=RGB(176 196 222), $
OBJECT=IMAGE, NAME='image1', IMAGE=webfocus1.gif, ALT='',
POSITION=(0.601 6.700), DIMENSION=(1.248 0.436), $
PAGELAYOUT=1, NAME='Page layout 1', text='Page layout 1',
BOTTOMMARGIN=0.15, TOPMARGIN=0.5, $
COMPONENT='report1', TEXT='report1', POSITION=(1.853 1.289),
DIMENSION=(6.458 5.417), $
OBJECT=IMAGE, NAME='image2', IMAGE=analyst_logo.gif, ALT='',
POSITION=(0.499 0.509), DIMENSION=(2.081 0.477), $
END

Creating Reports With TIBCO® WebFOCUS Language

 799

Saving Report Output in PPTX Format

SET COMPONENT='ppt_template'
TABLE FILE SYSCOLUM
SUM TBNAME NOPRINT
IF READLIMIT EQ 1
ON TABLE PCHOLD FORMAT PPTX TEMPLATE '_ibi_template.potx' SLIDENUMBER 2
END
SET COMPONENT='report1'
TABLE FILE IBISAMP/EMPDATA
SUM
  EMPDATA.EMPDATA.SALARY
BY LOWEST EMPDATA.EMPDATA.DEPT
BY EMPDATA.EMPDATA.LASTNAME
ON EMPDATA.EMPDATA.DEPT SUBFOOT
"Subfoot"
" "
ON EMPDATA.EMPDATA.DEPT PAGE-BREAK
ON TABLE SUBHEAD
"Report Heading "
" "
" "
HEADING
"Page Heading "
" "
FOOTING
"Page Footing"
" "
ON TABLE SUBFOOT
"Report Footing"
WHERE EMPDATA.EMPDATA.SALARY GE 40900;
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE SET ASNAMES ON
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
  PAGESIZE='PPT Slide',
    ORIENTATION=LANDSCAPE,
$
TYPE=REPORT,
  OBJECT=STATUS-AREA,
  JUSTIFY=LEFT,
  PAGE-LOCATION=BOTTOM,
$

800

9. Choosing a Display Format

TYPE=REPORT,
  GRID=OFF,
  FONT='ARIAL',
  SIZE=14,
  STYLE=NORMAL,
  SQUEEZE=ON,
  TOPGAP=0.05,
  BOTTOMGAP=0.05,
  BORDER-COLOR=RGB(219 219 219),
  TITLELINE=SKIP,
  TOPMARGIN=.25,
  LEFTMARGIN=2,
  BOTTOMMARGIN=0.05,
$
TYPE=TITLE,
  COLOR=RGB(51 51 51),
  STYLE=-UNDERLINE +BOLD,
$
TYPE=DATA,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$
TYPE=HEADING,
  JUSTIFY=LEFT,
  SIZE=16,
$
TYPE=HEADING,
  IMAGE=smplogo1.gif,
  POSITION=(+4.500000 +0.000000),
$
TYPE=TABFOOTING,
  IMAGE=smplogo1.gif,
  POSITION=(+4.500000 +0.000000),
$
TYPE=TABFOOTING,
  SIZE=10,
$
TYPE=FOOTING,
  SIZE=10,
$
TYPE=FOOTING,
  IMAGE=smplogo1.gif,
  POSITION=(+4.500000 +0.000000),
$

Creating Reports With TIBCO® WebFOCUS Language

 801

Saving Report Output in PPTX Format

TYPE=SUBFOOT,
  SIZE=9,
  BORDER-TOP=LIGHT,
  BORDER-TOP-COLOR=RGB(219 219 219),
$
TYPE=SUBFOOT,
  BY=1,
  IMAGE=smplogo1.gif,
  POSITION=(+4.500000 +0.000000),
$
ENDSTYLE
END
COMPOUND END

The output is:

802

Template Masters and Slide Layouts

9. Choosing a Display Format

A Microsoft PPTX 2007 and higher template can contain one or more Slide Masters, defining a
variety of different Slide Layouts.

A Slide Master is the top slide in a hierarchy of slides that stores information about the theme
and Slide Layouts of a presentation, including the background, color, fonts, effects,
placeholder sizes, and positioning.

You can incorporate two or more different styles or themes, such as backgrounds, color
schemes, fonts, and effects, by inserting an individual Slide Master into the template for each
different theme.

Note: Additional information on Microsoft PowerPoint Slide Layouts is available in an article
titled What is a slide layout? on the Microsoft support site.

By default, the first Slide Layout in the first Slide Master is applied to slides on which
WebFOCUS data is displayed.

With this new feature, WebFOCUS enables the developer to select any Slide Layout in any
Slide Master in a PowerPoint template (POTX/POTM) or Presentation file (PPTX/PPTM). One
Slide Layout may be applied to a slide or slides, displaying the output of a standard report,
while one or different Slide Layouts may be applied to each Page Layout in a PPTX formatted
Compound Document. The WebFOCUS generated ouput is placed on top of the styling on the
selected Slide Layout.

Identifying Slide Master Attributes in PowerPoint

To identify Slide Masters and Slide Layouts in a template, open the file in the PowerPoint
application, select the Home tab, and click the Layout button on the ribbon.

Creating Reports With TIBCO® WebFOCUS Language

 803

Saving Report Output in PPTX Format

A context menu displays all Slide Layouts with labels, as shown in the following image.

To view the Slide Master, select the View tab, and in the Master Views group on the ribbon,
click the Slide Master button, as shown in the following image.

804

The Master View opens to show the Slide Master and its associated Slide Layouts, as shown
in the following image.

9. Choosing a Display Format

Creating Reports With TIBCO® WebFOCUS Language

 805

Saving Report Output in PPTX Format

The following image shows the Slide Master view of the template used in this example. It
contains two Slide Masters: (1) Trek and (2) Oriel. Within each Master, the image displays the
layouts selected for the report generation. Notice that the Slide Master and Layout names can
be identified by hovering over the slide image. Use the name without the Slide Master or Slide
Layout suffixes.

806

9. Choosing a Display Format

Syntax:

How to Identify Slide Master Attributes in PowerPoint

For single reports:

TYPE=REPORT,SLIDE-MASTER='slidemaster_name',SLIDE-LAYOUT='layout_name', $

For Compound syntax:

PAGELAYOUT=n, NAME='Page layout (n)', SLIDE-MASTER='slidemaster_name',
SLIDE-LAYOUT='layout_name', $

Note: Slide Masters and Slide Layouts can be defined on the Page Master within the Section
syntax or on any Page Layout.

Example:

Compound Report Accessing Multiple Masters

The following syntax creates a full PPTX presentation based on a template with two Slide
Masters and four individual Slide Layouts. Each of the five individual procedures (.fex) shown
in this example need to be copied to a separate file.

COMPOUND LAYOUT PCHOLD FORMAT PPTX
UNITS=IN, $
SECTION=section1, LAYOUT=ON, SLIDE-MASTER='TREK',
SLIDE-LAYOUT='Title and Content',
MERGE=OFF, ORIENTATION=LANDSCAPE,
PAGESIZE=PPT Slide, SHOW_GLOBALFILTER=OFF, $
PAGELAYOUT=1, NAME='Page layout 1', SLIDE-MASTER='TREK',
SLIDE-LAYOUT='Title Slide', text='Page layout 1',
BOTTOMMARGIN=0.5, TOPMARGIN=0.5, $
COMPONENT='ppt_template', $
OBJECT=STRING, NAME='text1', TEXT='Gotham Grinds Sales Summary',
POSITION=(1.083 3.117), MARKUP=OFF, WRAP=ON, DIMENSION=(6.799 0.620),
font='TREBUCHET MS', color=RGB(0 0 0), size=36, $
OBJECT=STRING, NAME='text2', TEXT='Profit By Category',
POSITION=(1.100 3.733), MARKUP=OFF, WRAP=ON, DIMENSION=(6.833 0.500),
font='TREBUCHET MS', color=RGB(0 0 0), size=18, $
OBJECT=STRING, NAME='text3', TEXT='Prepared By:<br><br>Anne T Jones,
EVP of Sales<br>Joe F Smith, VP of Sales<br><br>&DATEtrMDYY',
POSITION=(5.683 5.433), MARKUP=ON, WRAP=ON, DIMENSION=(4.049 1.721),
font='TREBUCHET MS', color=RGB(0 0 0), size=18, $
PAGELAYOUT=2, NAME='Page layout 2', text='Page layout 2',
BOTTOMMARGIN=0.025, TOPMARGIN=4.8, $

Creating Reports With TIBCO® WebFOCUS Language

 807

Saving Report Output in PPTX Format

OBJECT=STRING, NAME='pl2_text2', TEXT='Sales By Region',
POSITION=(0.5 0.325), MARKUP=ON, WRAP=ON, DIMENSION=(4.146 0.609),
font='TREBUCHET MS', color=RGB(0 0 0), style=bold, size=24, $
OBJECT=STRING, NAME='pl2_text3', TEXT=' ', POSITION=(0.5 .725), MARKUP=ON,
WRAP=ON, DIMENSION=(4.146 0.609), font='TREBUCHET MS', color=RGB(0 0 0),
style=bold, size=20, $
COMPONENT='report1', TEXT='report1', POSITION=(2.2 4.8),
DIMENSION=(* *), $
COMPONENT='chart1', TEXT='chart1', POSITION=(0.733 1.25),
DIMENSION=(8.680 3.10), COMPONENT-TYPE=GRAPH, $
PAGELAYOUT=5, NAME='Page layout 5', SLIDE-MASTER='ORIEL',
SLIDE-LAYOUT='Section Header', text='Page layout 3',
BOTTOMMARGIN=0.5, TOPMARGIN=0.5, $
OBJECT=STRING, NAME='pl3text1', TEXT='Sales Performance Regional
Breakdowns', POSITION=(1.0 3.35), MARKUP=OFF, WRAP=ON,
DIMENSION=(6.799 0.620), font='TREBUCHET MS', color=RGB(0 0 0), size=24,$
COMPONENT='DfltCmpt2_3', POSITION=(0 0), DIMENSION=(0 0), $
PAGELAYOUT=6, NAME='Page layout 2', text='Page layout 4',
SLIDE-MASTER='ORIEL', SLIDE-LAYOUT='Title and Content',
BOTTOMMARGIN=0.025, TOPMARGIN=4.8, $
OBJECT=STRING, NAME='pl4_text2', TEXT='Sales By Category',
POSITION=(0.5 0.325), MARKUP=ON, WRAP=ON, DIMENSION=(4.146 0.609),
font='TREBUCHET MS', color=RGB(0 0 0), style=bold, size=24, $
OBJECT=STRING, NAME='pl4_text3', TEXT=' ', POSITION=(0.5 .725), MARKUP=ON,
WRAP=ON, DIMENSION=(4.146 0.609), font='TREBUCHET MS', color=RGB(0 0 0),
style=bold, size=20, $
COMPONENT='report2_2', TEXT='report2', POSITION=(2.2 4.8),
DIMENSION=(* *), $
COMPONENT='chart2_2', TEXT='chart2', POSITION=(0.733 1.25),
DIMENSION=(8.680 3.10), COMPONENT-TYPE=GRAPH, $
COMPONENT='report2_3', TEXT='report3', POSITION=(0.5 .725),
DIMENSION=(3 3), $
PAGELAYOUT=9, NAME='Page layout 9', SLIDE-MASTER='TREK',
SLIDE-LAYOUT='Thank You', text='Page layout 3',
BOTTOMMARGIN=0.5, TOPMARGIN=0.5, $
COMPONENT='DfltCmpt9', POSITION=(0 0), DIMENSION=(0 0), $
END

SET COMPONENT='ppt_template'
TABLE FILE SYSCOLUM
SUM TBNAME NOPRINT
IF READLIMIT EQ 1
ON TABLE PCHOLD FORMAT PPTX TEMPLATE 'template_plus.potx' SLIDENUMBER 1
END

808

9. Choosing a Display Format

SET COMPONENT='report1'
-INCLUDE GG_RPT1

SET COMPONENT='chart1'
-INCLUDE GG_CHART1

SET COMPONENT='DfltCmpt2_3'
TABLE FILE SYSCOLUM
" "
SUM TBNAME NOPRINT
IF READLIMIT EQ 1
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
END

SET COMPONENT='report2_2'
-INCLUDE GG_RPT2
SET COMPONENT='chart2_2'
-INCLUDE GG_CHART2
SET COMPONENT='report2_3'
-INCLUDE GG_RPT3

SET COMPONENT='DfltCmpt9'
TABLE FILE SYSCOLUM
" "
SUM TBNAME NOPRINT
IF READLIMIT EQ 1
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
END

COMPOUND END

-*gg_rpt1.fex
TABLE FILE GGSALES
SUM DOLLARS/D12CM BUDDOLLARS/D12CM UNITS/D12 BUDUNITS/D12
BY REGION
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
     INCLUDE = warm,
$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 809

Saving Report Output in PPTX Format

-*gg_rpt2.fex
TABLE FILE GGSALES
SUM DOLLARS/D12CM BUDDOLLARS/D12CM UNITS/D12 BUDUNITS/D12
BY REGION NOPRINT
BY CATEGORY
ON REGION PAGE-BREAK
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
     INCLUDE = warm,
$
ENDSTYLE
END

-*gg_chart1.fex
ENGINE INT CACHE SET ON
-DEFAULTH &WF_STYLE_UNITS='INCHES';
-DEFAULTH &WF_STYLE_HEIGHT='4.21875';
-DEFAULTH &WF_STYLE_WIDTH='8.020833';
-DEFAULTH &WF_TITLE='WebFOCUS Report';
GRAPH FILE GGSALES
SUM DOLLARS UNITS
BY REGION NOPRINT
ON GRAPH PCHOLD FORMAT PPTX
ON GRAPH SET HTMLENCODE ON
ON GRAPH SET GRAPHDEFAULT OFF
ON GRAPH SET ARGRAPHENGIN JSCHART
ON GRAPH SET VZERO OFF
ON GRAPH SET GRWIDTH 1
ON GRAPH SET UNITS &WF_STYLE_UNITS
ON GRAPH SET HAXIS &WF_STYLE_WIDTH
ON GRAPH SET VAXIS &WF_STYLE_HEIGHT
ON GRAPH SET GRMERGE ADVANCED
ON GRAPH SET GRMULTIGRAPH 0
ON GRAPH SET GRLEGEND 1
ON GRAPH SET GRXAXIS 0
ON GRAPH SET LOOKGRAPH VBAR
ON GRAPH SET STYLE *
*GRAPH_SCRIPT
setPieDepth(0);
setPieTilt(0);
setDepthRadius(0);
setCurveFitEquationDisplay(false);
setPlace(true);
*END

810

9. Choosing a Display Format

INCLUDE = warm,$
TYPE=REPORT, TITLETEXT=&WF_TITLE.QUOTEDSTRING, $
*GRAPH_SCRIPT
setReportParsingErrors(false);
setSelectionEnableMove(false);
setTransparentBorderColor(getChartBackground(),true);
setTransparentFillColor(getFrameSide(),true);
setTransparentBorderColor(getFrameSide(),true);
setTransparentFillColor(getFrameBottom(),true);
setTransparentBorderColor(getFrameBottom(),true);
*GRAPH_SCRIPT
-* Make the chart background, borders, etc. transparent:
setTransparentFillColor(getChartBackground(),true);
setFillColor(getChartBackground(),new Color(255,255,255,0));
setTransparentBorderColor(getChartBackground(),true);
setTransparentFillColor(getFrameSide(),true);
setTransparentBorderColor(getFrameSide(),true);
setTransparentFillColor(getFrameBottom(),true);
setTransparentBorderColor(getFrameBottom(),true);
setPlace(true);
*END
ENDSTYLE
END
-RUN

-*gg_chart2.fex
-DEFAULTH &WF_STYLE_UNITS='INCHES';
-DEFAULTH &WF_STYLE_HEIGHT='4.21875';
-DEFAULTH &WF_STYLE_WIDTH='8.020833';
-DEFAULTH &WF_TITLE='WebFOCUS Report';
GRAPH FILE GGSALES
SUM DOLLARS UNITS
BY REGION NOPRINT
BY CATEGORY
ON GRAPH PCHOLD FORMAT PPTX
ON GRAPH SET HTMLENCODE ON
ON GRAPH SET GRAPHDEFAULT OFF
ON GRAPH SET ARGRAPHENGIN JSCHART
ON GRAPH SET VZERO OFF
ON GRAPH SET GRWIDTH 1
ON GRAPH SET UNITS &WF_STYLE_UNITS
ON GRAPH SET HAXIS &WF_STYLE_WIDTH
ON GRAPH SET VAXIS &WF_STYLE_HEIGHT
ON GRAPH SET GRMERGE ADVANCED
ON GRAPH SET GRMULTIGRAPH 1
ON GRAPH SET GRLEGEND 1
ON GRAPH SET GRXAXIS 0
ON GRAPH SET LOOKGRAPH VBAR
ON GRAPH SET STYLE *

Creating Reports With TIBCO® WebFOCUS Language

 811

Saving Report Output in PPTX Format

*GRAPH_SCRIPT
setPieDepth(0);
setPieTilt(0);
setDepthRadius(0);
setCurveFitEquationDisplay(false);
setPlace(true);
*END
INCLUDE = warm,$
TYPE=REPORT, TITLETEXT=&WF_TITLE.QUOTEDSTRING, $
*GRAPH_SCRIPT
setReportParsingErrors(false);
setSelectionEnableMove(false);
setTransparentBorderColor(getChartBackground(),true);
setTransparentFillColor(getFrameSide(),true);
setTransparentBorderColor(getFrameSide(),true);
setTransparentFillColor(getFrameBottom(),true);
setTransparentBorderColor(getFrameBottom(),true);
*GRAPH_SCRIPT
-* Make the chart background, borders, etc. transparent:
setTransparentFillColor(getChartBackground(),true);
setFillColor(getChartBackground(),new Color(255,255,255,0));
setTransparentBorderColor(getChartBackground(),true);
setTransparentFillColor(getFrameSide(),true);
setTransparentBorderColor(getFrameSide(),true);
setTransparentFillColor(getFrameBottom(),true);
setTransparentBorderColor(getFrameBottom(),true);
setPlace(true);
*END
ENDSTYLE
END
-RUN

-*gg_rpt3.fex
TABLE FILE GGSALES
BY REGION PAGE-BREAK NOPRINT
HEADING
"<REGION"
ON TABLE SET PAGE-NUM NOLEAD
ON TABLE PCHOLD FORMAT PPTX
ON TABLE SET STYLE *
     INCLUDE = warm,
$
TYPE=HEADING, SIZE=20,
$
ENDSTYLE
END

812

The output is:

9. Choosing a Display Format

Creating Reports With TIBCO® WebFOCUS Language

 813

Saving Report Output in PPTX Format

Merging WebFOCUS Content With PowerPoint Template Content

Using the TEMPLATE-ACTION Stylesheet attribute, you can merge WebFOCUS content with
PowerPoint template content. The MERGE action allows you to edit components, such as
comments in native PowerPoint text boxes, in the resulting PowerPoint PPTX output.

Syntax:

How to Merge WebFOCUS Content With PowerPoint Template Content

To merge WebFOCUS content with PowerPoint template content, include the following
StyleSheet syntax in your procedure.

TYPE=REPORT, TEMPLATE-ACTION=MERGE ,$

Note: You can include the TEMPLATE-ACTION=REPLACE StyleSheet attribute to retain the
default behavior, which causes WebFOCUS output to override all target slide content.

Example: Merging WebFOCUS Content With PowerPoint Template Content

The following example shows how to merge WebFOCUS content with the PowerPoint template
content shown in the image below. The name of the PowerPoint template is my_template.potx.

814

9. Choosing a Display Format

Merge Procedure

The following procedure includes the TEMPLATE-ACTION=MERGE StyleSheet attribute to merge
WebFOCUS content with PowerPoint template content, my_template.potx.

TABLE FILE GGSALES
HEADING CENTER
"Sales for Region: <REGION"
SUM DOLLARS
BY REGION NOPRINT PAGE-BREAK
BY CATEGORY
BY PRODUCT

ON TABLE HOLD AS MERGEPPTX FORMAT PPTX TEMPLATE 'my_template.potx'
SLIDENUMBER 2

ON TABLE SET STYLE *
TYPE=REPORT, PAGESIZE=PPT-SLIDE, ORIENTATION=LANDSCAPE,
  TEMPLATE-ACTION=MERGE,
  LEFTMARGIN=2.75, TOPMARGIN=.75, BOTTOMMARGIN=1.5,
  FONT=ARIAL, SQUEEZE=ON, BORDER=LIGHT, STYPE=BOLD, SIZE=16, $
ENDSTYLE

END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 815

Saving Report Output in PPTX Format

Example:

Overriding Target Slide Content

The following procedure includes the TEMPLATE-ACTION=REPLACE StyleSheet attribute to
retain the default behavior and override all target slide content.

TABLE FILE GGSALES
HEADING CENTER
"Sales for Region: <REGION"
SUM DOLLARS
BY REGION NOPRINT PAGE-BREAK
BY CATEGORY
BY PRODUCT

ON TABLE HOLD AS REPLACEPPTX FORMAT PPTX TEMPLATE 'my_template.potx'
SLIDENUMBER 2
ON TABLE SET STYLE *
TYPE=REPORT, PAGESIZE=PPT-SLIDE, ORIENTATION=LANDSCAPE,
  TEMPLATE-ACTION=REPLACE,
  LEFTMARGIN=2.75, TOPMARGIN=.75, BOTTOMMARGIN=1.5,
  FONT=ARIAL, SQUEEZE=ON, BORDER=LIGHT, STYPE=BOLD, SIZE=16, $
ENDSTYLE

END

The output is:

816

9. Choosing a Display Format

ReportCaster Distribution and ReportCaster Bursting

ReportCaster Distribution is supported for simple reports, reports with images, PPTX
Templates, Coordinated Compound Reports, and graphs. Bursting is supported for simple
reports, reports with images, PPTX Templates, and Coordinated Compound Reports. For more
information, see the ReportCaster manual.

PPTX Limitations

The following is a limitation when using PPTX output format:

Justification of images in report elements.

In Compound syntax, the following are limitations when using PPTX output format:

Paneled reports.

Nested syntax.

Multi-pane reports or reports with multiple columns.

OPEN, CLOSE, or NOBREAK command.

Related Information

For related information on these topics, see the following WebFOCUS manuals:

Describing Data With WebFOCUS Language

Developing Reporting Applications

Using Functions

ReportCaster

Creating Reports With TIBCO® WebFOCUS Language

 817

Saving Report Output in PPTX Format

818

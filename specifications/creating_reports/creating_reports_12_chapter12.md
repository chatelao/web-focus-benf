Chapter12

Bursting Reports Into Multiple HTML Files

Bursting separates a single report into multiple HTML files based on the value of the first
sort field in your report.

In this chapter:

Bursting Reports Overview

Bursting Reports Overview

When bursting separates a single report into multiple HTML files, each file contains all the
requested information for one specific value of the sort field. By providing direct access to
different sections of your report, this technique enables you to:

Provide easier navigation of large reports. Bursting automatically creates an index file with
direct links to each of the resulting files.

Tailor the distribution of your report so that recipients can easily navigate to the section
they need.

Use standard heading and footing commands to label the index page and/or each of the
resulting report files.

Syntax:

How to Burst Reports Into Multiple HTML Files

ON sortfield PCSEND LOCATION dir [AS burstname] FORMAT HTML

where:

sortfield

Specifies the sort field based upon which bursting will occur. Each burst file will contain
report output for only one sort group.

You can burst reports based on the value of the first sort field only. You cannot burst
reports based on the value of subsequent sort fields.

You can burst a report into a maximum of 10,000 separate files. Therefore, you can burst
a report only if the number of individual values of the first sort field does not exceed
10,000.

Creating Reports With TIBCO® WebFOCUS Language

 1029

Bursting Reports Overview

PCSEND

Initiates bursting. You can only use one PCSEND command in a request.

dir

Specifies the location on the web server where the HTML index file and report files are
stored. The LOCATION parameter is required and must specify a directory from which the
web server reads HTML files. There is no default.

On UNIX, Windows, and OpenVMS platforms, the directory value must specify a fully
qualified directory path.

Note for z/OS Web390 users: On z/OS platforms, the directory value must specify the
ddname of an allocated PDS. No dynamic allocation of datasets is provided. The PDS is
allocated to a ddname other than the Web390 standard WWWHTM. The alternate ddname
must be WWWxxx, where xxx are any three alphanumeric characters. The Web390 web
server requires an entry in its mime table to recognize the allocated PDS as having HTML
output.

If the LOCATION parameter specifies an invalid directory or specifies a directory that
cannot be written to, an error message is returned.

burstname

Specifies the name of the HTML index file, which contains a list of hyperlinks to the
bursted HTML report files. The hyperlinks to the bursted HTML report files will be
numbered from 0 to 9999. If no file name is specified for the HTML index file, the default
name is HOLD.

Each bursted HTML report file will use the first four characters of the index file name,
followed by numerics 0000 through 9999.

Note: The report request can contain display fields with missing values. The report request can
also contain NOPRINT fields. For details, see Handling Records With Missing Field Values on
page 1035.

Reference: Rules for Headings and Footings on Index Pages and Bursted Reports

To include a heading or footing on the HTML index page, use the commands:

ON TABLE SUBHEAD

1030

12. Bursting Reports Into Multiple HTML Files

and

ON TABLE SUBFOOT

These headings and footings can contain embedded fields. The heading or footing is not
included in the HTML report output pages. Default styling is applied to the HTML index
page.

To include a standard heading or footing on all HTML report output pages, use the
commands:

HEADING

and

FOOTING

These headings and footings can contain embedded fields. Default styling is applied to the
HTML report output pages.

To include headings and footings that change each time the sortfield changes, use the
commands:

ON sortfield SUBHEAD

and

ON sortfield SUBFOOT

These subheadings or subfootings can include embedded fields, such as the sortfield used
in the PCSEND command. Default styling is applied to the HTML report output pages.

For details on including heading and footings in reports, see Using Headings, Footings, Titles,
and Labels on page 1517.

Creating Reports With TIBCO® WebFOCUS Language

 1031

Bursting Reports Overview

Example:

Bursting a Report

The following report procedure creates an HTML report output file for each different REGION
value in the GGSALES data source. The report output files are named test0000.html,
test0001.html, test0002.html, and so forth. The HTML index page is named test.html and
contains a hyperlink for each REGION data value. The directory you select depends on where
WebFOCUS is installed. In this example, the index page is stored in the directory e:\ibi
\WebFOCUS82\temp.

TABLE FILE GGSALES
HEADING
"Regional Report"
SUM UNITS AND DOLLARS
BY REGION BY STCD BY CATEGORY
ON TABLE SET PAGE NOPAGE
ON TABLE SUBHEAD
"Year-end Sales:"
"Regional Summary by Store"
ON REGION PCSEND LOCATION E:\IBI\WebFOCUS82\temp AS TEST FORMAT HTML
END

After running this request, no report output is returned, but the following message displays if
the request was successful:

The bursted files were successfully created.

Separate HTML files are created for each value of the major sort field REGION and are stored
in the location specified in the request.

The HTML index page created by the procedure follows:

Selecting the Midwest hyperlink displays the following HTML report:

Regional Report

1032

12. Bursting Reports Into Multiple HTML Files

Region

Store ID

Category

Unit Sales

Dollar Sales

Midwest

R1019

Coffee

    113253

     1393610

Food

Gifts

    107615

     1351523

     78869

      969845

R1020

Coffee

    109581

     1398779

Food

Gifts

    118068

     1522847

     79932

     1002775

R1250

Coffee

    109943

     1386124

Food

Gifts

    115731

     1463901

     72053

      911261

Notice that the headings specified in the ON TABLE SUBHEAD command are displayed on the
HTML index page. See Rules for Headings and Footings on Index Pages and Bursted Reports on
page 1030.

Creating Reports With TIBCO® WebFOCUS Language

 1033















Bursting Reports Overview

1034

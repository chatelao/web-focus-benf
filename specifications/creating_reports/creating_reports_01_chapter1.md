Chapter1

Creating Reports Overview

WebFOCUS is a complete information control system with comprehensive features for
retrieving and analyzing data that enables you to create reports quickly and easily. It
provides facilities for creating highly complex reports, but its strength lies in the
simplicity of the request language. You can begin with simple queries and progress to
complex reports as you learn about additional facilities.

WebFOCUS serves the needs of both end users with no formal training in data
processing, and data processing professionals who need powerful tools for developing
complete applications. A variety of tools are available that enable you to create reports
and charts even if you do not know HTML or WebFOCUS reporting language commands
and syntax.

In this chapter:

Requirements for Creating a Report

Report Types

Developing Your Report Request

Customizing a Report

Selecting a Report Output Destination

Requirements for Creating a Report

To create a report, only two things are required:

Data. You need data from which to report. If the data is protected by an underlying security
system, you may need permission to report from the data source. In addition, the server
must be able to locate the data source. For more information on data source locations, see
the Developing Reporting Applications manual.

You can report from many different types of data sources (with variations for different
operating environments), including the following:

Relational data sources, such as DB2, Teradata, Oracle, and Sybase.

Hierarchical data sources, such as IMS and FOCUS.

Creating Reports With TIBCO® WebFOCUS Language

 29

Report Types

Indexed data sources, such as ISAM and VSAM.

Network data sources, such as CA-IDMS.

Sequential data sources, both fixed-format and delimited format.

Multi-dimensional data sources, such as SAP BW and Essbase.

XML data sources.

For a complete list, see the Describing Data With WebFOCUS Language manual.

A data description. You need a Master File, which describes the data source from which
you are reporting. The Master File is a map of the segments in the data source and all of
the fields in each segment. For some types of data sources, the Master File is
supplemented by an Access File. For more information on Master Files and Access Files,
see the Describing Data With WebFOCUS Language manual.

By looking at the Master File, you can determine what fields are in the data source, what
they are named, and how they are formatted. You can also determine how the segments in
the data source relate to each other. Although you can create a very simple report without
this information, knowing the structure of the data source enables you to generate creative
and sophisticated reports.

You can supplement the information in the Master File by generating a picture of the data
source structure (that is, of how the data source segments relate to each other). Use the
following command:

CHECK FILE filename PICTURE RETRIEVE

In the picture, segments are shown in the order in which they are retrieved. Four fields of
each segment appear. For details see Displaying Report Data on page 39.

Report Types

With WebFOCUS, you can create the following basic report types using graphical tools:

Tabular reports. Displays information in rows and columns. This is the basic report type,
incorporating the fundamental reporting concepts. Most of the other report formats build on
these concepts. You can display these reports in formats such as HTML, Excel®, and PDF.

30

1. Creating Reports Overview

Financial reports. Specifically designed to handle the task of creating, calculating, and
presenting financially oriented data, such as balance sheets, consolidations, and budgets.
You can build these reports with the Report canvas. The Matrix Report canvas enables you
to define the content of the report on a row-by-row basis. This organization provides a
number of advantages. You can:

Identify and display a title for each row of the report.

Perform row-based calculations and include the results at any point on the report.

Include the same record in multiple categories.

Include many types of formatting enhancements on a cell-by-cell basis.

Save individual rows and row titles in extract files.

Free-form reports. Presents detailed information about a single record in a form-like context
that is often used with letters and forms. If your goal is to present a detailed picture of one
record per report page, you can use free-form reports to:

Position headers, footers, free text, and fields precisely on a page.

Customize your headers and footers by including fields as display variables.

Incorporate prefix operators in your headers and footers to perform calculations on the
aggregated values of a single field.

Use vertical (BY) sorting to put one or more report records on each page.

For details about free-form reports, see Creating a Free-Form Report on page 1899.

Graphs, which can present the same kinds of information as tabular reports, but in a wide
variety of two-dimensional and three-dimensional graph types.

For details, see Creating a Graph on page 1743.

SQL requests, which retrieve information using the SQL reporting language, and can directly
incorporate WebFOCUS formatting commands. For details, see Using SQL to Create Reports
on page 1907.

Creating Reports With TIBCO® WebFOCUS Language

 31

Developing Your Report Request

Drill Through reports. Allow users to create a PDF document that contains a summary
report plus a detail report, where the detail report contains all the detail data for
designated fields in the summary report. Clicking a Drill Through hyperlink navigates
internally in the PDF file and no additional reports are run. Drill Through reports are static.
You can save the PDF file to disk or distribute it using ReportCaster. When opened with
Acrobat® Reader, it retains its full Drill Through functionality. For more information about
the Drill Through feature, see Creating a PDF Compound Report With Drill Through Links on
page 954. For more information about Compound Reports, see Creating a Compound
Report on page 876.

Excel Compound reports. Provides a way to generate multiple worksheet reports using the
EXL2K output format. By default, each of the component reports from the compound report
is placed in a new Excel worksheet. If the NOBREAK keyword is used, the next report
follows the current report on the same worksheet.

For more information, see Creating a Compound Excel Report Using EXL2K on page 943.

Excel Table of Contents reports. Provides a way to generate a multiple worksheet report
where a separate worksheet is generated for each value of the first BY field in the
WebFOCUS report.

For more information, see Choosing a Display Format on page 575.

Developing Your Report Request

The only requirement for reporting is identifying a data source. Beyond that, the structure of a
report request is very flexible and you only need to include the report elements you want. For
example, you only need to include sorting instructions if you want your report to be sorted, or
selection criteria if you want to report on a subset of your data.

A report request begins with the TABLE FILE command and ends with the END command. The
commands and phrases between the beginning and end of a request define the contents and
format of a report. These parts of the request are optional; you only need to include the
commands and phrases that produce the report functions you want.

The following are the most frequently used options for structuring a report request.

Specifying fields and columns. Each column in your report represents a field. You can
specify which fields you want to display, which fields you want to use to sort the report,
which fields you want to use to select records, and which data source fields you want to
use in creating temporary fields. Therefore, specifying the fields you want in a report is
fundamentally tied to how you want to use those fields in your report.

32

1. Creating Reports Overview

Displaying data. You can display data in your report by listing all the records for a field
(detailed presentation), or by totaling the records for a field (summary presentation). You
can also perform calculations and other operations on fields, such as finding the highest
value of a field or calculating the average sum of squares of all the values of a field, and
present the results of the operation in your report.

Sorting a report column. Sorting a report enables you to organize column information.
WebFOCUS displays the sort field, which is the field that controls the sorting order, at the
left of the report if you are sorting vertically, or at the top, if you are sorting horizontally.
Sort fields appear when their values change. You can also choose not to display sort fields.

You can sort information vertically, down a column, or horizontally, across a row. You can
also combine vertical sorting and horizontal sorting to create a simple matrix.

Selecting records. When you generate a report, you may not want to include every record.
Selecting records enables you to define a subset of the data source based on your criteria
and then report on that subset. Your selection criteria can be as simple or complex as you
wish.

Showing subtotals and totals. You can display column and row totals, grand totals, and
section subtotals in your report.

Customizing the presentation. A successful report depends upon the information
presented and how it is presented. A report that identifies related groups of information
and draws attention to important facts will be more effective than one that simply shows
columns of data. For example, you can:

Give column titles more meaningful names.

Control the display of columns in your report.

Create headings and footings for different levels of the report (including each sort group,
each page, and the entire report), and dynamically control the display of headings and
footings based on conditions you set.

Add fonts, colors, grids, and images.

Highlight a group of related information and separate it from other groups by inserting
blank lines, underlines, and page breaks.

Creating temporary fields. When you create a report, you are not limited to the fields that
already exist in the data source. You can create temporary fields, deriving their values from
real data source fields, and include them in your report.

For details see, Creating Temporary Fields on page 277.

Creating Reports With TIBCO® WebFOCUS Language

 33

Developing Your Report Request

Joining data sources. You can join two or more data sources to create a larger integrated
data structure from which you can report in a single request.

For details, see Joining Data Sources on page 1069.

Storing and reusing the results. You can store your report data as a data source against
which you can make additional queries. This is especially helpful for creating a subset of
your data source and for generating two-step reports. You can also format the new data
source for use by other data processing tools, such as spreadsheets and word processors.

For details, see Saving and Reusing Your Report Output on page 471.

You can run the request as an ad hoc query or save it as a procedure. Saving a report request
as a procedure enables you to run or edit it at any time.

Starting a Report Request

A report request begins with the designation of a data source. You can then specify the details
of your report request. A data source can be specified in the following ways:

The TABLE FILE filename command sets the data source for a single request.

The FILE SET parameter sets a data source for all requests within a procedure.

For details on the FILE SET parameter, see the Developing Reporting Applications manual.

Syntax:

How to Begin a Report Request

To begin a report request, use the command

TABLE FILE filename

where:

filename

Is the data source for the report.

Completing a Report Request

To complete a report request, use the END or RUN command. These commands must be typed
on a line by themselves. To discontinue a report request without executing it, enter the QUIT
command.

34

1. Creating Reports Overview

If you plan to issue consecutive report requests against the same data source during one
session, you have the option of using the RUN command. RUN keeps the TABLE facility and
the data source active for the duration of the TABLE session. After viewing one report you do
not need to repeat the TABLE command to produce another report. You terminate the TABLE
session by issuing the END command after the last request.

Creating a Report Example

The example in this topic is a simple report request that illustrates some of the basic
functions of WebFOCUS. However, there are many more functions not shown here that you can
find information on throughout this documentation.

Example:

Creating a Simple Report

The following annotated example illustrates some of the basic functions of WebFOCUS. The
numbered explanation in this example corresponds with the code in this request. This request
can be generated by typing the commands into a text editor.

1.  JOIN PIN IN EMPDATA TO ALL PIN IN TRAINING AS J1
2.  DEFINE FILE EMPDATA
    YEAR/YY=COURSESTART;
3.  END

4.  TABLE FILE EMPDATA
5.  HEADING CENTER
    "Education Cost vs. Salary"
6.  SUM EXPENSES AS 'Education,Cost' SALARY AS 'Current,Salary'
7.  AND COMPUTE PERCENT/D8.2=EXPENSES/SALARY * 100; AS 'Percent'
8.  BY DIV
    BY DEPT
9.  WHERE YEAR EQ 1991
10. ON TABLE SUMMARIZE
11. ON TABLE SET STYLE *
    TYPE=HEADING, STYLE=BOLD, COLOR=BLUE,$
    TYPE=REPORT, FONT=TIMES, SIZE=8,$
    TYPE=REPORT, GRID=OFF,$
    ENDSTYLE
12. END

Creating Reports With TIBCO® WebFOCUS Language

 35


Developing Your Report Request

The output is:

The request processes in the following way:

1. The JOIN command joins the EMPDATA and TRAINING data sources, allowing the request to

access information from both data sources as if it were a single structure.

2. The DEFINE command creates a virtual field which extracts the year from the

COURSESTART field in the TRAINING data source.

3. The END command ends the DEFINE command.

4. The TABLE command begins the report request.

5. The HEADING command adds the heading, Education Cost vs. Salary to the report output.

6. The SUM command adds the values within both the EXPENSES field and the SALARY field.

The AS phrase changes the name of the column headings.

7. The COMPUTE command creates a calculated value using the values that have been

aggregated in the SUM command and sorted with the BY command.

8. The BY phrase sorts the data in the report by the DIV field, and then by the DEPT field.

9. The WHERE command includes only the data that falls in the year 1991.

10.The ON TABLE SUMMARIZE command adds all values in both the EXPENSES and SALARY

columns, and recalculates the Percent column.

11.The StyleSheet information formats the report heading and content.

12.The END command ends the report request.

36

Customizing a Report

1. Creating Reports Overview

A successful report depends on the information presented and how it is presented. A report
that identifies related groups of information and draws attention to important facts will be
more effective than one that simply shows columns of data.

When you have selected the data that is going to be included in your report and how you want
it to appear, you can then continue developing your report with custom formatting. There are
many things you can add to your request in order to make your report more effective. You can:

Add titles, headings, and footings. You can also change column titles with the AS phrase,
and create headings and footings for different levels of the report (including each sort
group, each page, and the entire report).

Change the format of a field and the justification of a column title. For details, see
Formatting Report Data on page 1697.

Determine the width of a report column. For details, see Formatting Report Data on page
1697.

Dynamically control the display of subtotals, headings, and footings based on conditions
you define. For details, see Controlling Report Formatting on page 1219.

Highlight a group of related information and separate it from other groups by inserting blank
lines or underlines between each group.

Emphasize data using color to highlight certain values in your report based on conditions
you define. For details, see Formatting Report Data on page 1697.

Format your report using external cascading style sheets. For details, see Using an External
Cascading Style Sheet on page 1293.

Add drill-down capability to your report. This adds extra value by linking your report to other
reports or URLs that provide more detail. For details, see Linking a Report to Other
Resources on page 819.

Creating Reports With TIBCO® WebFOCUS Language

 37

Selecting a Report Output Destination

Selecting a Report Output Destination

After you create a report, you can send it:

To the screen. When you run a report, the default output destination is the screen. Reports
run in WebFOCUS usually appear in a web browser, or in a helper application (such as,
Adobe® Reader® or Microsoft® Excel), within a web browser.

You can also view reports outside of the browser in a standalone helper application such
as Adobe Reader or Microsoft Excel. In Windows Folder Options, File Types (Advanced
Settings), uncheck the Browse in same window option for the file type; such as .pdf or .xls.
When the Browse in same window option is not selected, the browser window created by
WebFOCUS is blank because the report output is displayed in the helper application
window.

Note that if you selected the Save Report check box in the configuration pane of the
WebFOCUS Administration Console (under Redirection Settings), you will be prompted
whether to save or open the output file. If the procedure contained a PCHOLD command
that specified an AS name for the output file, the name is retained if you choose to save
the file. If no AS name was specified, a random filename is generated.

If the output is produced as a result of a GRAPH request, the returned HTML file contains a
link to the actual graph output, which is stored as a temporary image file (for example, as a
JPEG, GIF, or SVG file). The image file will eventually expire and be deleted from the server.
For information about saving the graph output, see Creating a Graph on page 1743.

To a file. You can store the results of your report for reuse using the HOLD, SAVE, or SAVB
commands. For details see Saving and Reusing Your Report Output on page 471.

To a printer. If you wish to print a report using a format such as PDF or HTML, first display
the report using the desired format, and then print the report from the display application
(for example, from Adobe Reader or from the web browser).

You cannot send a report directly to a printer in WebFOCUS.

38

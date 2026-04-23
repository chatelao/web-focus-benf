Chapter26

Creating a Free-Form Report

You can present data in an unrestricted or free-form format using a layout of your own
design.

Whereas tabular and matrix reports present data in columns and rows for the purpose of
comparison across records, and graphic reports present data visually using charts and
graphs, free-form reports reflect your chosen positioning of data on a page. Free-form
reporting meets your needs when your goal is to present a customized picture of a data
source record on each page of a report.

Note: You can create free-form reports with PDF, HTML, and Styled formats. HTML output
has all report pages on one HTML page. Page breaks are retained in PDF output.

In this chapter:

Creating a Free-Form Report

Designing a Free-Form Report

Creating a Free-Form Report

You can create a free-form report from a TABLE request that omits the display commands that
control columnar and matrix formatting (PRINT, LIST, SUM, and COUNT). Instead, the request
includes the following report features:

Heading

Footing

Contains the body of the report. It displays the text characters,
graphic characters, and data fields that make up the report.

Contains the footing of the report. This is the text that appears at
the bottom of each page of the report. The footing may display the
same characters and data fields as the heading.

Prefix operators

Indicates field calculations and manipulation.

Temporary fields

Derives new values from existing fields in a data source.

Creating Reports With TIBCO® WebFOCUS Language

 1899

Creating a Free-Form Report

BY phrases

Specifies the report sort order, and determines how many records
are included on each page.

WHERE criteria

Selects records for the report.

When creating a free-form report, you can:

Design your report to include text, data fields, and graphic characters. See Designing a
Free-Form Report on page 1903.

Customize the layout of your report. See Laying Out a Free-Form Report on page 1905.

Select the sort order and the records that are included in your report. See Sorting and
Selecting Records in a Free-Form Report on page 1906.

Example:

Creating a Free-Form Report

Suppose that you are a Personnel Manager and it is your responsibility to administer your
company education policies. This education policy states that the number of hours of outside
education that an employee may take at the company expense is determined by the number of
hours of in-house education completed by the employee.

To do your job efficiently, you want a report that shows the in-house education history of each
employee. Each employee information should display on a separate page so that it can be
placed in the employee personnel file and referenced when an employee requests approval to
take outside courses.

To meet this requirement, you create the EMPLOYEE EDUCATION HOURS REPORT, which
displays a separate page for each employee. Notice that pages 1 and 2 of the report provide
information about employees in the MIS department, while page 6 provides information for an
employee in the Production department.

1900

The following diagram simulates the output you would see if you ran the procedure in the
example named Request for EMPLOYEE EDUCATION HOURS REPORT on page 1902.

26. Creating a Free-Form Report

Creating Reports With TIBCO® WebFOCUS Language

 1901

Creating a Free-Form Report

Example:

Request for EMPLOYEE EDUCATION HOURS REPORT

The following request produces the EMPLOYEE EDUCATION HOURS REPORT. Numbers to the
left of the request correspond to numbers in the following annotations:

1. SET STYLE = OFF
   SET STYLEMODE=FIXED
   SET ONLINE-FMT = PDF
2. DEFINE FILE EMPLOYEE
      CR_EARNED/I2 = IF ED_HRS GE 50 THEN 9
         ELSE IF ED_HRS GE 30 THEN 6
         ELSE 3;
      END
3. TABLE FILE EMPLOYEE
   BY DEPARTMENT
4. HEADING
   " "
   "<13>EMPLOYEE EDUCATION HOURS REPORT"
5. "<14>FOR THE <DEPARTMENT DEPARTMENT"
6. "</2"
   "EMPLOYEE NAME:    <23><FIRST_NAME <LAST_NAME>"
   "EMPLOYEE ADDRESS: <23><ADDRESS_LN1>"
   "<23><ADDRESS_LN2>"
   "<23><ADDRESS_LN3>"
   "</1"
   "JOB CODE: <JOBCODE>"
   "JOB DESCRIPTION: <JOB_DESC>"
   "</1"
7. "MOST RECENT COURSE TAKEN ON: <MAX.DATE_ATTEND>"
   "TOTAL NUMBER OF EDUCATION HOURS: <ED_HRS>"
   "</1"
8. "<10>|-------------------------------------|"
9. "<10>| EDUCATION CREDITS EARNED <CR_EARNED>|"
   "<10>|-------------------------------------|"
10.BY EMP_ID NOPRINT PAGE-BREAK
11.WHERE ED_HRS GT 0
12.FOOTING
   "<15>PRIVATE AND CONFIDENTIAL"
   END

The following explains the role of each line of the request in producing the sample report:

1. Two SET commands are required to view the desired display in a browser. The SET STYLE =
OFF command enables a free-form design by ignoring default StyleSheet parameters. SET
STYLEMODE = FIXED turns off HTML formatting and allows the report designer to determine
where items in the report are placed, using spot markers and skip-line commands.

2. The DEFINE command creates a virtual field for the report. The calculation reflects the

company policy for earning outside education credits. The result is stored in CR_EARNED
and appears later in the report.

3. A free-form report begins with a standard TABLE FILE command. The sample report uses

the EMPLOYEE data source.

1902

26. Creating a Free-Form Report

4. The heading section, initiated by the HEADING command, defines the body of the report.
Most of the text and data fields that display in the report are specified in the heading
section. In this request, the heading section continues until the second BY phrase BY
EMP_ID NOPRINT PAGE-BREAK.

5. This line illustrates the following:

The second line of the text in the page heading.

A data field embedded in the text: <DEPARTMENT.

The start position of the line, column 14: <14>.

6. You can enhance the readability of a report using skip-line commands. The command </2,

when coded on a line by itself, generates two blank lines, as seen between the page
heading and employee name.

7. This line illustrates how to perform a field calculation in a free-form report using a prefix

operator. In this case, we requested the date on which the most recent course was taken
—that is, the maximum value for the DATE_ATTEND field.

8. The next three lines illustrate the use of special characters to create a graphic in the

report. The box around EDUCATION CREDITS EARNED may need adjustment for output
displayed in a proportional font.

9. The value of the field created by the DEFINE command displays in the box, highlighting the
number of education credits an employee has earned. This line demonstrates that you can
display a virtual field in the body of your report.

10.This line illustrates the use of sorting in a free-form report. The report specifications require
that information for only one employee displays per page. This is achieved by using the BY
and PAGE-BREAK commands. Note that in order to produce a report with page breaks, the
report output must be PDF.

11.You can specify record selection in a free-form report. As a result of the WHERE criterion,
the report includes only employees who have accumulated in-house education credits.

12.Since we have designed a personnel report, it is important to have the words PRIVATE AND
CONFIDENTIAL at the end of each report page. The FOOTING command accomplishes this.

Designing a Free-Form Report

To design the body of a free-form report, use the HEADING and FOOTING commands. They
enable you to:

Incorporate text, data fields, and graphic characters in your report.

Lay out your report by positioning text and data in exact column locations and skipping
lines for readability.

Creating Reports With TIBCO® WebFOCUS Language

 1903

Designing a Free-Form Report

Use the HEADING command to define the body of a free-form report, and the FOOTING
command to define what appears at the bottom of each page of a report. A footing is optional.
You can define an entire report using just a heading.

Incorporating Text in a Free-Form Report

You can specify text anywhere in a free-form report, for a variety of purposes. In the sample
request (see the example named Request for EMPLOYEE EDUCATION HOURS REPORT on page
1902) text is used:

As a report title:

"<13>EMPLOYEE EDUCATION HOURS REPORT"

As a label for data fields:

"EMPLOYEE NAME:   <FIRST_NAME <LAST_NAME>"

With a data field and graphic characters:

"<10>| EDUCATION CREDITS EARNED <CR_EARNED>|"

As a page footing:

"<15>PRIVATE AND CONFIDENTIAL"

Incorporating Data Fields in a Free-Form Report

The crucial element in any report, free-form or otherwise, is the data. The data fields available
in a request include data fields in the Master File, cross-referenced fields, and virtual fields
created with the DEFINE command.

The sample request (see Request for EMPLOYEE EDUCATION HOURS REPORT on page 1902)
references all three types of data fields:

ED_HRS is found in the EMPLOYEE Master File:

"TOTAL NUMBER OF EDUCATION HOURS: <ED_HRS>"

DATE_ATTEND is found in the EDUCFILE Master File, which is cross-referenced in the
EMPLOYEE Master File:

"MOST RECENT COURSE TAKEN ON: <MAX.DATE_ATTEND>"

CR_EARNED is created with the DEFINE command before the TABLE FILE command, and is
referenced as follows:

1904

26. Creating a Free-Form Report

"<10>| EDUCATION CREDITS EARNED <CR_EARNED>|"

You can also apply a prefix operator to a data field to select a particular value (for example,
the maximum value within a sort group) or to perform a calculation (for example, to compute
the average value of a field). You can use any available prefix operator in a free-form report.

In the sample request, the MAX prefix operator selects the most recent completion date of an
in-house course:

"MOST RECENT COURSE TAKEN ON: <MAX.DATE_ATTEND>"

As is true with all types of reports, you must understand the structure of the data source to
use the prefix operators correctly.

Incorporating Graphic Characters in a Free-Form Report

Graphics in a report can be as creative as your imagination. The sample report (see Creating a
Free-Form Report on page 1899) uses special characters to enclose text and a virtual field in a
box. Some other ideas include:

Highlighting key data fields using asterisks or other special characters available directly
from your keyboard, or using the HEXBYT function. See the Using Functions manual for
details on HEXBYT.

Enclosing the entire report in a box to give it a form-like appearance.

Using double lines to separate the body of the report from its page heading and page
footing.

The use of special characters to create graphics is limited by what can be entered and viewed
from your workstation and what can be printed on your printer. If you have difficulty producing
the graphics that you want, be sure to check with someone in your organization who knows
what is available.

Laying Out a Free-Form Report

To provide spacing in a report and position text and data fields, use the spot marker feature of
the HEADING and FOOTING commands.

Note: To take advantage of this feature in an HTML report, include the SET STYLEMODE=FIXED
command in your request.

Creating Reports With TIBCO® WebFOCUS Language

 1905

Designing a Free-Form Report

The sample request (see the example named Request for EMPLOYEE EDUCATION HOURS
REPORT on page 1902) illustrates this feature. The first two examples show how to position
text and data fields on your report, while the third example shows how to skip lines:

The spot marker <13> positions the specified text in column 13 of the report:

"<13>EMPLOYEE EDUCATION HOURS REPORT"

The spot marker <23> positions the specified data field in column 23 of the report:

"<23><ADDRESS_LN2>"

The spot marker </1 on a line by itself skips two lines after displaying the job description:

"JOB DESCRIPTION: <JOB_DESC>""</1""MOST RECENT COURSE TAKEN ON:
<MAX.DATE_ATTEND>"

When designing a free-form report, take advantage of sort field options, such as NOPRINT,
PAGE-BREAK (PDF output only), and UNDER-LINE. The sample request uses PAGE-BREAK to
place each employee information on a separate page:

BY EMP_ID NOPRINT PAGE-BREAK

Sorting and Selecting Records in a Free-Form Report

As with tabular and matrix reports, you can both sort a report and conditionally select records
for it. Use the same commands as for tabular and matrix reports. For example, use the BY
phrase to sort a report and define WHERE criteria to select records from the data source.

1906

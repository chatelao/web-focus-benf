Appendix D

Referring to Fields in a Report Request

When creating a report, you refer to fields in several parts of the request. For example, in
display commands (PRINT, SUM), in sort phrases (BY, ACROSS), and in selection criteria
(WHERE, WHERE TOTAL, IF).

Several methods are available for referring to a field. You can:

Refer to individual fields by using the alias specified in the Master File, referring to
the name defined in the Master File, or using the shortest unique truncation of the
field name or alias. For details, see Referring to an Individual Field on page 1993.

Refer to fields using qualified field names. For details, see Referring to Fields Using
Qualified Field Names on page 1994.

Refer to all fields in a segment using only one field name. For details, see Referring
to All of the Fields in a Segment on page 1995.

You can also view a list of all the fields that are included in the currently active data
source, or a specified Master File. For details, see the Developing Reporting Applications
manual.

In this appendix:

Referring to an Individual Field

Referring to Fields Using Qualified Field Names

Referring to All of the Fields in a Segment

Displaying a List of Field Names

Referring to an Individual Field

You can refer to an individual field in any one of the following ways:

Using the field name defined in the Master File.

Using the alias (the field name synonym) defined in the Master File.

Using the shortest unique truncation of the field name or the alias. When a truncation is
used, it must be unique. If it is not unique, an error message is displayed.

Creating Reports With TIBCO® WebFOCUS Language

 1993

Referring to Fields Using Qualified Field Names

Adding the letter S to the end of a field name defined in the Master File.

Example:

Referring to an Individual Field

In the following requests, DEPARTMENT is the complete field name, DPT is the alias, and DEP
is a unique truncation of DEPARTMENT. All these examples produce the same output.

1. TABLE FILE EMPLOYEE
   PRINT DEPARTMENT
   END

2. TABLE FILE EMPLOYEE
   PRINT DPT
   END

3. TABLE FILE EMPLOYEE
   PRINT DEP
   END

Note: If you use a truncation that is not unique, the following message will appear:

(FOC016) THE TRUNCATED FIELDNAME IS NOT UNIQUE : D

Referring to Fields Using Qualified Field Names

Field names and aliases have a maximum length of 512 characters. They can also be qualified
by prepending up to two qualifiers and qualification characters. However, text fields and
indexed field names in Master Files for FOCUS data sources are limited to 12 characters,
although the aliases for text and indexed fields can have the same length as general field
names. Field names are always displayed as column titles in reports, unless a TITLE attribute
or an AS phrase is used to provide an alternative name. For related information, see Using
Headings, Footings, Titles, and Labels on page 1517.

You may use the file name, segment name, or both as a qualifier for a specified field.

Syntax:

How to Activate Long and Qualified Field Names

The SET FIELDNAME command enables you to activate long (up to 512 characters) and
qualified field names.

SET FIELDNAME = fieldname

where:

fieldname

Specifies the activation status of long and qualified field names. Valid identifiers include:

1994

D. Referring to Fields in a Report Request

NEW specifies that 512-character and qualified field names are supported. NEW is the
default value.

NOTRUNC supports the 512-character maximum. It does not permit unique truncations of
field names.

OLD is no longer operational and will function as NEW.

Example:

Using a Qualified Field Name to Refer to a Field

EMPLOYEE.EMPINFO.EMP_ID

Is the fully-qualified name of the field EMP_ID in the EMPINFO segment of the EMPLOYEE file.

Reference: Usage Notes for Long and Qualified Field Names

? SET displays the current value of FIELDNAME. In addition, a Dialogue Manager variable called
&FOCFIELDNAME is available. &FOCFIELDNAME may have a value of NEW or NOTRUNC.

For additional information about using qualified field names in report requests, see the
Describing Data With WebFOCUS Language manual.

Referring to All of the Fields in a Segment

If you want to generate a report that displays all of a segment fields, you can refer to the
complete segment without specifying every field. You only need to specify one field in the
segment (any field will do) prefixed with the SEG. operator.

Example:

Referring to All Fields in a Segment

The segment PRODS01in the GGPRODS Master File contains the PRODUCT_ID,
PRODUCT_DESCRIPTION, VENDOR_CODE, VENDOR_NAME, PACKAGE_TYPE, SIZE, and
UNIT_PRICE fields.

SEGMENT=PRODS01
FIELDNAME = PRODUCT_ID
FIELDNAME = PRODUCT_DESCRIPTION
FIELDNAME = VENDOR_CODE
FIELDNAME = VENDOR_NAME
FIELDNAME = PACKAGE_TYPE
FIELDNAME = SIZE
FIELDNAME = UNIT_PRICE

Creating Reports With TIBCO® WebFOCUS Language

 1995

Displaying a List of Field Names

To write a report that includes data from every field in the segment, you can issue either of the
following requests:

1. TABLE FILE GGPRODS
   PRINT PRODUCT_ID AND PRODUCT_DESCRIPTION AND VENDOR_CODE AND
    VENDOR_NAME AND PACKAGE_TYPE AND SIZE AND UNIT_PRICE
   END

2. TABLE FILE GGPRODS
   PRINT SEG.PRODUCT_ID
   END

Displaying a List of Field Names

If you want to see a list of all the fields that are included in the currently active data source,
you can issue the ?F field name query.

This is useful if you need to refer to a list of field names, or need to check the spelling of a
field name, without exiting from the request process. It will also show you the entire 66-
character field name.

You can issue the ?F query from the Editor in WebFOCUS.

More information on all of the query (?) commands appears in the Developing Reporting
Applications manual.

Listing Field Names, Aliases, and Format Information

The ?FF query displays field name, alias, and format information for a specified Master File,
grouped by segment.

You can issue the ?FF query from the Editor in WebFOCUS.

If your software supports MODIFY or FSCAN, you can also issue ?FF from these facilities.

Note:

If duplicate field names match a specified string, the display includes the field name
qualified by the segment name with both ?F and ?FF.

Field names longer than 31 characters are truncated in the display, and a caret (>) is
appended in the 32nd position to indicate that the field name is longer than the display.

1996

Legal and Third-Party Notices

SOME TIBCO SOFTWARE EMBEDS OR BUNDLES OTHER TIBCO SOFTWARE. USE OF SUCH
EMBEDDED OR BUNDLED TIBCO SOFTWARE IS SOLELY TO ENABLE THE FUNCTIONALITY (OR
PROVIDE LIMITED ADD-ON FUNCTIONALITY) OF THE LICENSED TIBCO SOFTWARE. THE
EMBEDDED OR BUNDLED SOFTWARE IS NOT LICENSED TO BE USED OR ACCESSED BY ANY
OTHER TIBCO SOFTWARE OR FOR ANY OTHER PURPOSE.

USE OF TIBCO SOFTWARE AND THIS DOCUMENT IS SUBJECT TO THE TERMS AND CONDITIONS
OF A LICENSE AGREEMENT FOUND IN EITHER A SEPARATELY EXECUTED SOFTWARE LICENSE
AGREEMENT, OR, IF THERE IS NO SUCH SEPARATE AGREEMENT, THE CLICKWRAP END USER
LICENSE AGREEMENT WHICH IS DISPLAYED DURING DOWNLOAD OR INSTALLATION OF THE
SOFTWARE (AND WHICH IS DUPLICATED IN THE LICENSE FILE) OR IF THERE IS NO SUCH
SOFTWARE LICENSE AGREEMENT OR CLICKWRAP END USER LICENSE AGREEMENT, THE
LICENSE(S) LOCATED IN THE "LICENSE" FILE(S) OF THE SOFTWARE. USE OF THIS DOCUMENT
IS SUBJECT TO THOSE TERMS AND CONDITIONS, AND YOUR USE HEREOF SHALL CONSTITUTE
ACCEPTANCE OF AND AN AGREEMENT TO BE BOUND BY THE SAME.

This document is subject to U.S. and international copyright laws and treaties. No part of this
document may be reproduced in any form without the written authorization of TIBCO Software
Inc.

TIBCO, the TIBCO logo, the TIBCO O logo, FOCUS, iWay, Omni-Gen, Omni-HealthData, and
WebFOCUS are either registered trademarks or trademarks of TIBCO Software Inc. in the
United States and/or other countries.

Java and all Java based trademarks and logos are trademarks or registered trademarks of
Oracle Corporation and/or its affiliates.

All other product and company names and marks mentioned in this document are the property
of their respective owners and are mentioned for identification purposes only.

This software may be available on multiple operating systems. However, not all operating
system platforms for a specific software version are released at the same time. See the
readme file for the availability of this software version on a specific operating system platform.

THIS DOCUMENT IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS
OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.

THIS DOCUMENT COULD INCLUDE TECHNICAL INACCURACIES OR TYPOGRAPHICAL ERRORS.
CHANGES ARE PERIODICALLY ADDED TO THE INFORMATION HEREIN; THESE CHANGES WILL
BE INCORPORATED IN NEW EDITIONS OF THIS DOCUMENT. TIBCO SOFTWARE INC. MAY MAKE
IMPROVEMENTS AND/OR CHANGES IN THE PRODUCT(S) AND/OR THE PROGRAM(S)
DESCRIBED IN THIS DOCUMENT AT ANY TIME.

 1997

THE CONTENTS OF THIS DOCUMENT MAY BE MODIFIED AND/OR QUALIFIED, DIRECTLY OR
INDIRECTLY, BY OTHER DOCUMENTATION WHICH ACCOMPANIES THIS SOFTWARE, INCLUDING
BUT NOT LIMITED TO ANY RELEASE NOTES AND "READ ME" FILES.

This and other products of TIBCO Software Inc. may be covered by registered patents. Please
refer to TIBCO's Virtual Patent Marking document (https://www.tibco.com/patents) for details.

Copyright © 2021. TIBCO Software Inc. All Rights Reserved.

1998

Index

_ masking character 248

- subtraction operator[/] 435

-n spot marker 1680

-SET command 429

? DEFINE command 287

? FILTER command 269, 270

? JOIN command 1151

? STAT command 189

?F command 1996

?FF command 1996

[F]DEFCENT attribute 451

[F]YRTHRESH attribute 451

* multiplication operator 432, 435

** exponentiation operator 435

/ division operator 432, 435

/n spot marker 1680

&FOCFIELDNAME variable 1995

% masking character 248, 250, 251

+ addition operator 435

$ masking character 248, 250

$* masking character 248, 250, 252

0X spot marker 1520

3D graphs 1749

508 compliance 1473

A

absolute starting positions 1676

ACCEPT attribute 495

Accordion By Column Reports 1017

Accordion Reports 989, 991, 1018

Accordion Reports and ACROSS phrase 989

Accordion Reports and BY phrase 989

Accordion Reports and distributing with

ReportCaster 991

Accordion Reports and drill-downs 991

Accordion Reports and HTML report 989

ACROSS attribute 1265, 1266

ACROSS COLUMNS AND phrase 151, 153, 154

ACROSS phrase 41, 63, 87, 94–96, 107, 301,

302, 989

ACROSS subtype 1265, 1274

ACROSS summary commands 413

ACROSS values 374, 375, 1273, 1275

ACROSS with ROW-TOTAL 371

ACROSS-TOTAL component 374, 375

ACROSSCOLUMN attribute 1252, 1254, 1504

ACROSSCOLUMN subtype 1505, 1788, 1791

ACROSSPRT parameter 107

ACROSSTITLE component 1274, 1275

ACROSSVALUE and drill-downs 1275

ACROSSVALUE component 1265, 1274, 1275

ACRSVRBTITL parameter 96

ADD command 50

ADD option 287

ADD parameter 1860

Creating Reports With TIBCO® WebFOCUS Language

 1999

Index

adding attributes to WebFOCUS StyleSheets 981,

adding HTML reports to dynamic tables of

983

contents 969

adding blank lines to headings and footings 1686

adding HTML tables of contents to headings 983

adding blank rows 1847

adding HTML tables of contents to reports 971,

adding blank spaces around a report 1343

972

adding calculated values in financial reports 1849

adding HTML tables of contents to WebFOCUS

adding color to graphs 1788, 1789

StyleSheets 971, 972

adding columns to financial reports 1849

adding HTML TOCs (tables of contents) to

adding comments to WebFOCUS StyleSheets

headings 981

1204

adding images to a report 1462, 1468

adding conditional styling to graphs 1789

adding labels to graphs 1798, 1799

adding declarations to font map files 625

adding line breaks to text fields 1739

adding dynamic tables of contents to headings

adding PostScript fonts 623

983

adding PostScript Type 1 fonts 623

adding dynamic tables of contents to reports 969,

adding PostScript Type1 fonts in Unix 625

971, 972

adding PostScript Type1 fonts in Windows 625

adding dynamic tables of contents to WebFOCUS

adding PostScript Type1 fonts in z/OS 627

StyleSheets 971, 972

adding rows to financial reports 1820, 1823

adding dynamic TOCs (tables of contents) to

adding tables of contents (TOCs) to HTML reports

headings 981

969

adding fields to graph footings 1798

adding tag rows to financial reports 1820, 1821,

adding fields to graph headings 1798

1856

adding fields to headings and footings 1798

adding text rows to financial reports 1847

adding financial data to reports 1829

adding TOCs (tables of contents) to HTML reports

adding fonts for PostScript (PS) format 623

969

adding fonts in PS (PostScript) format 584

adding underlines 1449, 1450

adding footings to graphs 1798

adding underlines to columns 1454, 1455

adding graphics to a report 938, 1462, 1466,

adding underlines to financial reports 1872

1468, 1474, 1476, 1481

adding values 51

adding headings to graphs 1798

adding values for numeric fields 51

2000

adding virtual fields 287

addition operator 435

addressing columns 1839

aggregate values 226

aggregation 195

Index

alphanumeric fields and text fields 360

ALT attribute 1465, 1466, 1473

alternate file views 1929–1931

alternate indexes 274

alternating background color 1708

aggregation and external sorting 196, 197

amper variables 1790, 1798

AHTML format 512

AHTMLTAB format 512

aliases 1916, 1993, 1994

displaying 1996

AND operator 235, 465

AnV fields 460, 461

APDF display format 513

applying FORECAST command to conditional

aligning decimal points 1662, 1664, 1666

formatting 1237

aligning footings 1666

aligning heading items 1678

aligning headings 1662, 1666

applying FORECAST command to conditional

styling 1223

applying graphs to columns 1499

aligning headings and footings 1633, 1635,

applying graphs to report columns 1499

1637, 1648, 1653

aligning sort headings 1666

aligning text fields 1651, 1652

applying grids to a report 1432, 1433

applying macros 1205, 1206

applying selection criteria in graph requests 1781,

aligning using HTML tables 1648

1798

alignment methods 1633

alignment with OVER 1360

area graphs 1749, 1764

arithmetic expressions 432

ALL parameter 226, 1059, 1073

arithmetic operators 432, 435

ALL parameter and JOIN command 1072, 1073

around headings and footings of border 1405

ALL parameter and missing values 1059–1061

AS CAPTION phrase 1856, 1857

ALL parameters 1060

ALL prefix 1059

AS phrase 473, 486

ascending sort order 149

ALL prefix and missing values 1059

ASNAMES command 484–488

ALLOCATE command 472

ALPHA format 512

ASQ calculations on field values 61

assigning cascading style sheet classes to report

alphanumeric fields 247–255, 389

components 1306, 1307

Creating Reports With TIBCO® WebFOCUS Language

 2001

Index

assigning classes in cascading style sheets to

base dates 440, 441

ACROSS values 1299

BASEURL SET parameter 872, 873

assigning classes in cascading style sheets to

basic date support in graphs 1780

report components 1304, 1307

BINARY format 513

assigning external cascading style sheet classes

BINARY HOLD format 513

to report components 1307

BINARY output file format 513

associating bar graphs with report columns 1499,

BINS parameter 189

1504

bipolar graphs 1749

associating graphs with columns 1504

blank lines 1440, 1442, 1685

associating graphs with report columns 1504

blank lines, removing 1456

attribute inheritance 1207, 1208

blank rows 1847

attributes 820, 837, 873, 1202, 1508, 1796,

blank spaces 1340

1872

augmenting attributes 1208

blank spaces above data values 1345

blank spaces between columns 1346

AUTOINDEX parameter 1932–1934

blanks 1050

AUTOPATH parameter 1932

BLEND-MODE parameter 1120

AUTOTABLEF parameter 65, 67

BLOB image in reports 1476, 1481

AVE field 60

AVE prefix operators 60

B

BACKCOLOR 1706, 1708

background color 1706

background color, alternating 1708

background images 1462, 1474, 1475

BACKIMAGE attribute 1462, 1465, 1474, 1475

bar graphs 1749, 1761

BAR

command 1454, 1455, 1872

rows 1872

2002

BODY element 1304

Boolean expressions 465, 466

Boolean operator 465

Boolean operators 465

BORDER attribute 1403, 1405, 1407, 1615,

1872

border colors 1405

border styles 1405

borders 1402, 1407, 1613, 1881

adding for cells 1881, 1885

adding for rows 1883, 1885

BOTTOM 207

bottom margins 1337

Index

BOTTOMGAP attribute 1341, 1343, 1687

calculating maximum values for field values 61

BOTTOMMARGIN attribute 1337, 1339

calculating median of field values 62

breaks 1377

calculating MIN field values 61

browser fonts 1704, 1705

calculating minimum field values 61

browser fonts in HTML Reports 1704

calculating minimum values for field values 61

browser support for cascading style sheets 1323

calculating mode of field values 62

browser support for HTML tables of contents 989

calculating row Percentages 63

browser titles 1522

bubble charts 1767

calculating row totals 367–370

calculating trends 357

bursting reports 1029, 1032

calculating values for temporary fields 297

BY 91

BY HIERARCHY 207

calculation on field values 65

calculations 1845

BY phrase 41, 52, 63, 87–90, 138, 1256, 1828

calculations and functions 1845, 1846

with financial reports 1828, 1829

calculations counting field values 70

BY ROWS OVER phrase 151–153

calculations on counting field values 70

BY subtype 1256, 1268, 1279

BY TOTAL phrase 173–175

calculations on field values 56, 60, 61, 138

calculations on sum numeric field values 70

BYLASTPAGE system variable 1389, 1392

calculations on SUM numeric field values 70

byte precision 54, 55

C

calculations on TOT field values 70

calculations on total field values 70

calling functions 1845, 1846

calculated values 278–280, 301, 302, 367, 371,

CAPTION parameter 1855, 1860, 1867, 1868

383–385, 1589, 1849

sorting reports 302

calculating column and row totals 367, 368

calculating column Percentages 63

calculating column totals 367–371

calculating dates 441, 442

calculating MAX field values 61

calculating maximum field values 61

captions 1522

in a hierarchy 1859

in Master Files 1855, 1867, 1868

CAR data source 1945, 1947

carriage-returns 1739

Cartesian product 1184, 1185

Cartesian product answer sets 1920

Creating Reports With TIBCO® WebFOCUS Language

 2003

Index

Cartesian product answer sets and SQL Translator

CDN (Continental Decimal Notation) and SQL

1920

Translator 1920

cascading style sheet (CSS) 1193, 1220, 1221,

CDN parameter 1717

1293, 1302

cells 1843, 1844

browser support 1321, 1323, 1327

formatting 1871, 1874, 1876, 1881

choosing 1303

notation 1844

class for ACROSS values 1299

CENTER command 1617

classes 1294, 1304, 1323

conditional styling 1321

editing 1304

example 1300

external 1293

FAQS 1323

file location 1303

formatting 1306, 1308

images 1309, 1321

inheritance 1314, 1327

internal 1219

CENTFIN data source 1967

CENTHR data source 1967

CENTINV data source 1967

CENTORD data source 1967

CENTQA data source 1967

Century Corp data sources 1967

changing column order 1354

changing row titles 1870

PICKUP rows 1896

RECAP rows 1871

TAG rows 1870

linking 1298, 1299, 1310–1313

character expressions 430, 456

location 1303

multiple 1303

character strings 247, 458

Chart of Accounts hierarchy 1853, 1855

multiple output formats 1316, 1318, 1320

charts 1749

naming classes 1305, 1307

personal 1327

refreshing 1304, 1327

charts of accounts 1856

CHECK FILE command 1150

CHECK FILE command and join structures 1149,

report formatting 1296, 1298

1150

requirements 1321

CHECK PICTURE command 45

rules 1294, 1299, 1304, 1323

CHECK STYLE command 1200

troubleshooting 1327

choosing formatting reports style sheets 1193

CDN (Continental Decimal Notation) 1717, 1920

choosing report formatting style sheets 1193

2004

Index

CLASS attribute 1299, 1306, 1307, 1323

column

clearing conditional join structures 1152

clearing join structures 1151, 1152

clearing virtual fields 287, 288

CMS requirements 188

addresses 1839

columns 1252, 1712

addresses 1838–1840

formatting 1874

CNOTATION SET parameter 302, 303, 1840,

in financial reports 1820

1841

CNT prefix operator 70

notation 1840, 1841

numbers 1836

collapsing PRINT with ACROSS 107

reference numbers 1840

collation sequence 141

COLLATION SET parameter 141

COLOR attribute 1701

color graph settings 1815

color settings 1336

color settings in graphs 1815

color values 1701

color, background 1706

values 1841

COM format 514

COM HOLD format 514

COM output file format 514

COM PCHOLD format 514

COM SAVE format 514

combination of summary commands 408

combinations of subtotals 407

color, background, alternating 1708

combining expressions 235

COLSPAN attribute 1653

combining external cascading style sheets with

column and row totals in calculated values 367

other formatting methods 1308, 1309

COLUMN attribute 1252, 1253, 1264, 1504

combining fields in date expressions 444, 445

column formats 1713

column notation 302, 303

combining mixed format reports 935, 936, 938,

939

column reference numbers 302

combining multiple values 1823

COLUMN subtype 1625, 1735, 1875

combining PDF reports 935, 936

column titles 84, 1589, 1591, 1592, 1713

combining records 1823, 1824

column titles for calculated values 1594

combining report formats 939

column total labels 1600

column totals 367, 370, 371

combining report formatting cascading style

sheets and other formatting methods 1323

COLUMN-TOTAL phrase 367–369

combining values 1823, 1824, 1826

Creating Reports With TIBCO® WebFOCUS Language

 2005

Index

COMMA format 514

COMMA HOLD format 514

compound reports 525, 877, 934

compound reports in PDF format 936

COMMA output file format 514

compressing PDF output files 586

COMMA SAVE format 514

comma-delimited files 1071

COMPUTE command 52, 297–299, 301, 302,

383, 403, 421, 422, 424, 429

command support for Accordion Reports 1017

COMPUTE command expressions 429

commands 1204, 1205

comments 1202, 1204

COMPUTE component 1272

computing the average field values 60

comments in WebFOCUS StyleSheets 1202, 1204

COMT format 515

common high-order sort fields 1166, 1167, 1169,

COMT HOLD format 515

1180, 1181, 1183

COMT output file format 515

comparing characters with masks 248–252

COMT PCHOLD format 515

comparing decimal values 1664

COMT SAVE format 515

comparing records 1158, 1164, 1165

concatenated data sources and MATCH FILE

compiling expressions 1936

compiling virtual fields 1936

complex expressions 429

command 1178

concatenating character strings 458

concatenating data sources 1173–1175

COMPMISS parameter 1054, 1715

concatenating data sources and field names 1177

compound display formats for reports 877, 934

concatenation 458

compound expressions 235

COMPOUND parameter 935

concatenation data sources 1175, 1178

concatenation for data sources 1173

compound report display formats 877, 934

concatenation operators 458

Compound report syntax

COMPONENT 881

displaying a grid 901

draw objects 895

example 884

page overflow 892

PAGELAYOUT 879

SECTION 878

2006

concatenation usage formats 1176

conditional drill-down 865–867

conditional drill-down and multiple links 853

conditional expression types 467

conditional expressions 430, 467, 468

conditional formatting 1553

conditional formatting and WHEN phrase 1239,

1241–1244, 1553

Index

conditional grid formatting 1718, 1719

constants 1830

conditional join structures 1069, 1071, 1081,

in FML requests 1829, 1830

1101, 1102, 1104, 1149

CONTAINS operator 247

conditional operators 236, 243, 244

contiguous columns 1837

conditional sort headings 1548

contiguous columns in financial reports 1837

conditional styling 853, 1219, 1222, 1239,

Continental Decimal Notation (CDN) 1717, 1920

1241–1244, 1321

Continental Decimal Notation (CDN) and SQL

conditional styling and graphs 1788, 1789

Translator 1920

conditional styling and style sheets 1225, 1234

controlling attributes 484, 490, 491, 495

conditional styling and WebFOCUS StyleSheets

controlling attributes and HOLD Master Files 492

1222, 1223, 1225, 1226, 1228, 1231, 1232,

controlling column order 1346, 1353, 1354

1234

controlling column reference numbers 302, 1840

conditional text 427, 428

controlling column spacing 1346, 1352, 1353

conditionally displaying page breaks 1241

controlling display of sort field values 989

conditionally displaying skipped lines 1241

controlling field names 485–488

conditionally displaying summary lines 1241

controlling field names HOLD Master Files 485

conditionally displaying underlines 1241

controlling fields 490

configuring PostScript fonts 625, 627

converting data types for join structures 1101

configuring PostScript fonts in z/OS 627

converting TABLE requests 1744, 1746

configuring PostScript Type 1 fonts 625

converting TABLE requests to GRAPH requests

connected point plot graphs 1749, 1760

1744, 1746

consolidating financial data 1856, 1859, 1860,

COUNT * command 53, 54

1862, 1863

in multiple rows 1863

single row 1860, 1862

constant dates 439, 443

constants 1830

COUNT command 52, 53, 88

COUNT command for unique segments 53

count of occurrences 70

counting field values 52

COUNTWIDTH SET parameter 52, 54, 55

in Financial Modeling Language (FML) 1829

COURSE data source 1952, 1953

in financial reports 1829

CREATE TABLE command 1917, 1918

in FML (Financial Modeling Language) 1829

CREATE VIEW command 1918, 1919

Creating Reports With TIBCO® WebFOCUS Language

 2007

Index

creating bar graphs 1754, 1755

creating style sheets 1198

creating calculated values 297, 299, 300

creating tag rows 1821, 1822

creating financial reports 1818, 1823

creating temporary fields with COMPUTE phrases

creating FOCUS data sources 479, 482–484

297

creating free-form reports 1899, 1900,

creating temporary fields with DEFINE FUNCTION

1902–1906

creating graphs 1743

364

creating vertical bar graphs 1754, 1755

creating HOLD files 473–476, 479, 480, 482

creating virtual fields 280–282, 284, 286, 290

creating horizontal bar graphs 1754, 1755

creating WebFOCUS StyleSheets 1197, 1198

creating links 819, 820

cross-century dates 442

creating matrix report with OVER 1355

cross-referenced fields 1092

creating matrix reports with OVER 1357

cross-referenced files 1072, 1081

creating multiple virtual fields 287

CSS (cascading style sheets) 1193, 1220, 1221

creating numeric expressions 432

CSS location 1303

creating output files 473

CSSURL (StyleSheets) attribute 1299

creating parameters 854, 856, 858

CSSURL attribute 1299, 1303, 1310, 1311

creating parameters for drill-down reports 854

CSSURL attribute example 1312

creating parameters for drill-downs 1798

CSSURL attribute HTMTABLE format 1310

creating PCHOLD files 509

CSSURL parameter 1299, 1303, 1310, 1313

creating pie graphs 1756, 1757

CSSURL parameter HTMTABLE format 1310

creating reports 32, 34

creating rows 1820–1822

from multiple records 1823

in financial reports 1820

creating SAVB files 508

creating SAVE files 506, 507

creating scatter graphs 1758

CT. prefix operator 1558

custom report titles 1522

custom sort order 151

custom worksheet names 1522

customizing column titles in a Master File 1594

customizing graphs 1787, 1805

customizing reports 37, 1903

creating single-line footings 1531

customizing sort order 151

creating single-line headings 1527, 1535

creating sort headings 1545

2008

D

data 1262, 1263

retrieval 1820, 1895, 1896

date constants 439

date expressions 439, 444

date fields 439

date formats 1921, 1922

date formats and SQL Translator 1921, 1922

date support in graphs 1780

date value formats 440

date values 440

date-time data types 450

date-time expression types 439

date-time expressions 439

date-time field formats 450

date-time format 454

date-time format and display fields 450

date-time values 439, 1923–1925

date-time values and SQL Translator 1923–1925

DATEFORMAT parameter 449, 450

DATEFORMAT setting 450

dates 441

dates in graphs 1780, 1781

DATREC format 516

Db2 format 516

Db2 HOLD format 516

Db2 output file format 516

DBAFILE attribute 1072

DBAJOIN 1141

DBASE format 517

Index

DBASE HOLD format 517

DBASE output file format 517

decimal points 1662, 1664, 1666

decimal values 1662, 1666

declarations 1202, 1203

declaring filters 266

default browser type 1704

default column titles 1590

default font types 1703

default proportional fonts 1703

default StyleSheet values 1248

DEFAULT- FIXED attribute 1704

DEFAULT- PROPORTIONAL attribute 1704

DEFINE and dates 292, 293, 442

DEFINE attribute 429

DEFINE command 282, 284, 287, 429

DEFINE command and join structures 1094,

1095, 1097, 1144, 1145, 1147

DEFINE command and missing values 1038–1042

DEFINE command expressions 429

DEFINE compiler 1936

DEFINE FILE RETURN command 1147

DEFINE FILE SAVE command 291, 1147

DEFINE function 361

command 361

creating temporary fields 362

deleting 361, 366

displaying 361

displaying 365

limitations 361

Creating Reports With TIBCO® WebFOCUS Language

 2009

Index

DEFINE function 361

limitations 363

querying 361

DEFINE functions 364

Define tool 287

DIF PCHOLD format 518

DIF SAVE format 518

direct percent 65

direct percent of counts (PCT.CNT) 65

display ADD command 50

defining custom groups 166, 167

display commands 39, 88, 1170

defining field formats 1713

defining filters 265–267

defining macros 1206

defining virtual fields 284

display commands and graph format 1751

display commands and MATCH FILE command

1170, 1171

display COUNT command 52, 88

DEFMACRO command 1204–1206

display DOC formats for reports 643

DEFMACRO commands 1204

DELETE command 1927

display field values 41, 42

display fields 56, 57, 1714

deleting underlines 1449, 1450

display fields and graph format 1751

delimited file, creating 549

delimited output files 517

display fields for prefix operators 56

display formats for compound reports 939

descending sort order 149, 150

display formats for EXCEL reports 576

designating missing values 1066

display formats for EXL2K PIVOT reports 576

determining column width 1346–1350

display formats for EXL2K reports 576, 578

DFIX 549

DFIX format 517

DFSORT utility 188

DHTML HOLD format 517

DHTML output format 517

Dialect Translation 1907

Dialogue Manager 429, 1817

display formats for HTML reports 578

display formats for PDF reports 578, 584, 585

display formats for PostScript reports 578, 584,

620, 622

display formats for reports 575, 576, 578, 579

display LIST * command 42

display LIST command 88

Dialogue Manager variables 1557

display LIST commands 39, 41

FOCFIELDNAME 1995

DIF format 518

DIF output file format 518

2010

display PRINT * command 42

display PRINT command 88

display PRINT commands 39, 41

Index

display SUM command 50, 51, 88

displaying PRINT commands 39

display SUM commands 39

displaying reports 217, 575, 576, 578, 581, 584,

display values 39

display WRITE command 50

displaying ADD command 50

585, 620, 643

displaying reports as PDF 934

displaying reports as PostScript 934

displaying all fields in a segment 44

displaying reports in a browser 581

displaying all fields in segments 44

displaying reports in PDFs 877

displaying captions 1856

displaying reports in PostScripts 877

displaying children 1856, 1858, 1859

displaying reports in WebFOCUS Viewer 1021

displaying compound reports 935

displaying retrieval order 45

displaying empty reports 1246

displaying retrieval order for multi-path data

displaying error messages 192, 193

sources 47

displaying excluded values 91

displaying field descriptions 84

displaying field names 1996

displaying structure for multi-path data sources

45, 46

displaying sub-totals 381–383

displaying field values 39, 41–43

displaying subtotals 375–377, 380–383

displaying grand totals 375, 376

displaying graph data 1769

displaying SUM command 50

displaying summary lines 428

displaying hierarchy values as captions 1859

displaying values 39

displaying HOLD Master Files 473, 477

displaying WRITE command 50

displaying join structures 1149–1151

distinct prefix operators 65, 66

displaying LIST * command 42

displaying LIST command 41

displaying LIST commands 39

displaying missing values 1782

division operator 432, 435

DOC format 518, 576, 643

DOC output file format 518

DOC PCHOLD format 518

displaying missing values in graphs 1783

DOC report display formats 643

displaying parents and children 1856, 1858,

DOC SAVE format 518

1859

displaying PRINT * command 42

displaying PRINT command 41

double exponential smoothing 324, 347, 348

FORECAST_DOUBLEXP 324

Creating Reports With TIBCO® WebFOCUS Language

 2011

Index

drill through compound reports in PDF format

dynamically formatting virtual fields 293, 294

954–956, 959, 961, 967

drill through PDF compound reports 954–956,

E

959–961, 967

drill through reports 954–956, 959–961, 964,

967

drill-down reports 819, 820, 866, 867, 1796

drill-down reports compared 954

drill-downs 1796, 1798

drill-downs and ACROSSVALUE 1275

drill-downs and graphs 1790

drilling down graphs 1790, 1792

drilling down reports 820

DRILLMENUITEM attribute 1796

DRILLMETHOD 862

DRILLTHROUGH command 956

DROP VIEW command 1918

DROP VIEW command and SQL Translator 1919

DROPBLNKLINE parameter 1456

DST prefix operator 66

DST prefix operator restrictions 65

DST prefix operators 65

duplicate field names as column titles 1594,

1595

DUPLICATECOL parameter 181

dynamic reformatting 1736, 1737

dynamic reporting 1853

dynamic tables of contents 969

dynamic tables of contents for multiple sort

groups 976

2012

editing font map files in Windows 625

editing font map files in z/OS 627

editing metrics files in Windows 625

editing metrics files in z/OS 627

EDUCFILE data source 1942, 1943

ELEMENT attribute 1511, 1512

elements in footings 1557

elements in headings 1557

embedded fields 1284, 1285

embedded fields in footings 1284

embedded quotation marks 457, 458

embedding compound reports graphs 938

embedding compound reports images 938

embedding graphics 938

embedding images 938

EMPDATA data source 1951

EMPLOYEE data source 1937, 1939, 1940

empty reports 1246

EMPTYREPORT SET parameter 1246

END command 34

ending a report request 34

EQ operator 246, 465

equijoins 1069, 1071, 1082

error files 1983

error messages 1983

escape characters 253–255

ESSBASE hierarchies 1853

Index

establishing segment locations 290

EXL2K PIVOT report display format 576

estimating number of records 190

EXL2K report display format 576

ESTLINES parameter 190

ESTRECORDS parameter 190

ex_forecast_dist 356

ex_forecast_mov 355

ex_forecast_mult 354

ex_regress_mult 359

Excel 2000 alignment 1635

Excel 2007

EXL2K SAVE format 519

EXL97 display format 520

EXPANDABLE command 989, 1018

expanding byte precision 55

expanding byte precision for COUNT command 54

expanding precision 55

explicit labels 1832–1834

EXPN and numeric functions 434

TOCs (tables of contents) 712

EXPN function 434

EXCEL display format 576

Excel formats 576

EXCEL report display format 576

Excel reports 712

EXCEPT operator 1921

exponential moving average 313, 314, 320, 336,

337, 345

FORECAST_EXPAVE 320

exponentiation operator 435

exporting from data sources 473, 476

EXCLUDES operator 256, 257

expression dates 430, 443

excluding missing values from tests 1051

expression types 430

existing data 246, 247

EXL07 display format

TOCs (tables of contents) 712

EXL2K alignment 1635

expressions 277, 429, 1921

expressions and SQL Translator 1921

expressions IF phrase 429

expressions, relational 466

EXL2K display format 519, 576, 578

EXTAGGR parameter 195

EXL2K FORMULA 520

extending heading and footing code 1520

EXL2K FORMULA display format 520, 576

extending underlines 1451

EXL2K output file format 519

EXL2K PCHOLD format 519

EXL2K PIVOT 520

external cascading style sheet class for ACROSS

values 1299

external cascading style sheet classes 1294

EXL2K PIVOT display format 576

external cascading style sheet rules 1294, 1299

EXL2K PIVOT format 520

Creating Reports With TIBCO® WebFOCUS Language

 2013

Index

external cascading style sheet rules BODY

extract files and missing values 1051, 1052

element 1304

EXTRACT function 1925

external cascading style sheet rules TD element

extracting date components 444

1304

EXTSORT parameter 188, 189

external cascading style sheets 1193, 1295,

EXTUNDERLINE attribute 1451

1302

benefits 1295

browser support 1321, 1323, 1327

choosing 1303

class names 1305

classes 1304, 1323

editing 1304

images 1321

linking to 1310

multiple 1303

multiple output formats 1316, 1318

report formatting 1296

requirements 1321

rules 1304, 1323

troubleshooting 1327

external files 1828

external report formatting cascading style sheets

1298

external sorting 188, 189, 192, 193

external sorting and aggregation 195

external sorting and HOLD files 198, 199

external sorting by aggregation 195–197

external sorting requirements 188

EXTHOLD parameter 199

extract files 472, 500, 503, 505, 563

2014

F

FIELD attribute 1504

field dates 439

field format expressions 432

field formats 432, 443

field names 486–488, 1920, 1921, 1993

aliases 1993, 1994

displaying 1996

long 1994, 1995

qualified 1993–1995

truncated 1993, 1994

field padding 558–560

field references for COMPUTE command 301

field reformatting and missing values 1054, 1715

field values 39, 138, 1547, 1559

field values in headings and footings 1557–1559

field-based reformatting 292–294, 1736–1738

FIELDNAME command 1994

fields 277, 432, 1713, 1993

in report requests 1993, 1994

file location of external cascading style sheets

1303

file names 820

FILECOMPRESS parameter 586

Index

FILEDEF command 472, 498

FILTER parameter 265–268

financial reports 30, 1187, 1817, 1853

supplying data as constants 1830

FILTER query command 265, 269, 270

fixed scales 1800, 1805

filters 265, 266, 268–270, 272

FIXRETRIEVE parameter 496, 497

FINANCE data source 1949, 1950

FLEX display format 521

financial data 1859

retrieving 1894

FML (Financial Modeling Language) 1255, 1817,

1818, 1990

retrieving values for rows 1821, 1822

and Dialogue Manager 1817

Financial Modeling Language (FML) 1255, 1817,

FML hierarchies 1853, 1855, 1856, 1858, 1859

1990

displaying 1853, 1856

Financial Modeling Language (FML) and Dialogue

indenting captions 1889

Manager 1817

Financial Report Painter 30

indenting row titles 1889

indenting text or numbers 1872

financial reports 30, 1187, 1817, 1853

loading into memory 1867, 1868

adding data 1820, 1829

FML Painter 30

charts of accounts 1853, 1856, 1858, 1859

FOCEXEC attribute 820

external files 1828

FOCEXEC attributes 820

formatting 1871, 1872, 1874, 1876

FOCFIELDNAME variable 1995

formatting options 1871, 1874

FOCFIRSTPAGE SET parameter 1388, 1389, 1395

hierarchies 1856, 1860, 1867–1869

FOCHTMLURL parameter 991

HOLD files 1897

inserting text rows 1847

pop-up field descriptions and 85

FOCPOST files 1894

inserting variables in text rows 1848, 1849

FOCUS data sources 218, 479

inter-row calculations 1831, 1832

FOCUS file structure 479, 481

records in multiple rows 1827

FOCUS format 521

recursive models 1852

repeating rows 1835

FOCUS StyleSheets 1871

FOLD-LINE command 1347, 1356

saving intermediate results 1894

FONT attribute 1703, 1704

sorting with BY 1828

sorting with FOR 1828

font attributes 1609, 1684

font colors 1697, 1701, 1706, 1708

Creating Reports With TIBCO® WebFOCUS Language

 2015

Index

font file 625, 627

font files 623

font inherited styles 1700

font map files 623, 625

font sizes 1697, 1698

font styles 1699

fonts 623, 1607, 1697, 1703

fonts and labels 1609

fonts and system variables 1612

fonts and titles 1609

FORECAST 314, 339, 354–356

linear regression analysis 336, 337

linear regression equation 351, 353

predicting values 336

processing 314, 337

simple moving average 336, 337, 341, 343

triple exponential smoothing 349, 350

format ALPHA 512

format dates 440, 441

FORMAT DFIX 549

fonts in headings and footings 1609, 1611

format DHTML 517

fonts in HTML reports 1704

fonts in HTML Reports 1704

footing code 1520

formatting blank lines 1444, 1445

formatting carriage-returns for text fields 1739

formatting cells 1871, 1874, 1876

FOOTING command 1536, 1617, 1903

formatting cells and labels 1876

FOOTING component 1277, 1279

formatting columns 1712–1714, 1871, 1874,

footing limitations 1519

1877

footings 1273, 1517, 1518, 1532, 1536

formatting dates in graphs 1781

footings for bursted reports 1030

formatting fields 432, 443

FOR field

formatting financial reports 1454, 1455

reusing values 1826

formatting footings 1607

FOR phrase 65, 67, 152, 166, 167, 1817, 1818,

formatting graphs 1759, 1760, 1772

1821, 1828, 1829

reusing values 1826

syntax 1990

FORECAST 314, 339, 354–356

formatting heading and footing lines 1662

formatting headings 1607

formatting HOLD files 473

formatting labels 1607

calculating trends 336

formatting line-feeds for text fields 1739

double exponential smoothing 347, 348

formatting output files 511

exponential moving average 336, 337, 345

formatting PCHOLD files 509

limit 315, 340

2016

Index

formatting reports 1187, 1189, 1293, 1296,

GAPINTERNAL attribute 1360

1298, 1323, 1501, 1502, 1911

GE operator 245, 465

formatting reports and SQL Translator 1911

generating TABLEF commands 1927

formatting reports in FML (Financial Modeling

GET 862

Language) 1454, 1455

GET CHILDREN parameter 1856, 1860

formatting rows 1871, 1874–1876, 1878

GGDEMOG data source 1961

formatting rows and labels 1874–1876

GGORDER data source 1961

formatting SAVB files 508

formatting SAVE files 506

GGPRODS data source 1961

GGSALES data source 1961

formatting skipped lines 1444, 1445

GGSTORES data source 1961

formatting text 1880

formatting text fields 1652, 1739

formatting text rows 1879

formatting titles 1607

GIF files 521

GIF format 521

Gotham Grinds data sources 1961

grand totals 375, 1602

FORMULTIPLE parameter 1826, 1827

GRANDTOTAL component 1256, 1257, 1267,

free text 1273, 1847, 1848, 1879

1268, 1270

formatting 1874, 1878–1880

GRAPH command 1744

free-form reports 30, 1187, 1323, 1662, 1666,

GRAPH command compared to TABLE command

1899, 1906

1745

FREETEXT component 1276, 1277, 1879, 1880

graph footings 1798

freezing HTML headings 1540

FROM ... TO operator 243, 244

FST prefix operator 68, 69

full outer join 1105

functions 429, 1845

FYRTHRESH attribute

graph formats 1751, 1759

graph formats and display commands 1751

graph formats and display fields 1751

graph formats and sort phrases 1751

graph formatting 1298

graph formatting BODY element 1304

date-time data type and 450

graph formatting in external cascading style

G

Gantt charts 1768

sheets 1306, 1323

graph formatting TD element 1304

Creating Reports With TIBCO® WebFOCUS Language

 2017

Index

graph formatting with external cascading style

grouping numeric data into tiles 167, 168,

sheets 1298

graph headings 1798

graph height 1800, 1801

graph SET parameters 1800

graph styling 1798, 1799

graph titles 1522

graph types 1749

graph width 1800, 1801

GRAPHBASE attribute 1502

170–172

grouping sort fields 969, 976

groups of values 1826

identifying 1826

GRWIDTH parameter 1778

GT operator 245, 246, 465

GTREND parameter 1771

GUTTER attribute 1511, 1512

GRAPHCOLOR attribute 1231, 1501, 1502

H

graphic elements 868, 870

graphics 868, 1569

graphics in footings 1569

graphics in headings 1569

GRAPHLENGTH attribute 1501, 1502

GRAPHNEGCOLOR attribute 1502

graphs 30, 1743, 1744

displaying multiple graphs in columns 1778

GRAPHSCALE attribute 1502, 1506, 1508, 1509

GRAPHSERVURL SET parameter 1809–1811

GRAPHTYPE attribute 1231, 1499, 1501, 1504

GRAPHWIDTH attribute 1501, 1502

GRID attribute 1403, 1404, 1408, 1409

grids 1402, 1404, 1408, 1432, 1433, 1613

GRMERGE parameter 1773, 1782

group fields 1093

group fields and join structures 1093

group key values 257, 258

grouping numeric data 163–167

2018

H data type 450

HAUTO parameter 1805

HAXIS parameter 1800

HEADALIGN attribute 1635, 1637, 1641, 1646

heading code 1520

HEADING command 1533, 1617, 1903

HEADING component 1277, 1279, 1280

heading limitations 1519

headings 1273, 1517, 1518, 1532

headings and footings for HTML index pages 1030

headings for bursted reports 1030

headings for graphs 1798

headings on panels 1572

HEADPANEL attribute 1572

helper applications 579

HGRID attribute 1403, 1432, 1433, 1614

HIDENULLACRS parameter 110

hiding columns 1372, 1375

hiding display fields 1371

hiding fields 1372, 1375

hiding fields in y-axis 1771

hiding rows 1892, 1893

hiding sort field values 177, 989

hiding y-axis fields 1771

hierarchical reporting

BOTTOM 207

BY HIERARCHY 207

hierarchical sort 207

SHOW 207

TOP 207

using WHEN 207

Index

HOLD files and missing values 1051, 1052

HOLD files for financial reports 1897

HOLD files text fields 511

HOLD format ALPHA 512

HOLD format DATREC 516

HOLD format DFIX 517

HOLD format GIF 521

HOLD format INGRES 522

HOLD format INTERNAL 523, 558–560

HOLD format JPEG 523

HOLD format PowerPoint 526

HOLD format Red Brick 526

hierarchies 1853, 1860, 1868, 1869

HOLD format SQL_SCRIPT 527

displaying 1853

hierarchy of sort fields 971

HOLD format SQLDBC 527

HOLD format SQLINF 527

high-order sort fields 1166, 1167, 1169, 1180,

HOLD format SQLMAC 528

1181, 1183

HMAX parameter 1805

HMIN parameter 1805

HOLD format SQLMSS 528

HOLD format SQLODBC 528

HOLD format SQLORA 528

HOLD AT CLIENT command 473, 509

HOLD format SQLPSTGR 529

HOLD command 472, 473

HOLD format SQLSYB 529

HOLD file INTERNAL format 560, 561

HOLD file JSON format 524

HOLD file keys and indexes 505

HOLD file structured 563

HOLD format SYLK 529

HOLD format TAB 530

HOLD format TABT 530

HOLD FORMAT VISDIS 531

HOLD file suppressing field padding 558–560

HOLD format WK1 532

HOLD file text fields 547, 548

HOLD format WP 532

HOLD files 472, 473, 481, 496, 497, 563, 1158

HOLD format XFOCUS 533

HOLD files and external sorting 198, 199

HOLD format

HOLD files and merge phrases 1158, 1164, 1165

XML 534

Creating Reports With TIBCO® WebFOCUS Language

 2019

Index

HOLD formats 511

HOLD formats AHTML 512

HOLD formats AHTMLTAB 512

HOLD formats APDF 513

HOLD formats EXL97 520

HOLD formats FLEX 521

HOLD formats FOCUS 521

HTML5-only charts 1769

HTMLCSS SET parameter 1220

HTMLFORM command 1310

HTMTABLE format 522, 1310

hyperlinks 1022, 1321

hyperlinks in HTML reports 1022

HOLD Master Files 473, 477, 484, 486–488,

I

490, 491, 495, 498

HOLDATTR command 484, 495

HOLDATTR parameter 495

HOLDLIST command 484, 490–492

horizontal bar graphs 1499

horizontal labels 1799

horizontal waterfall graphs 1768

host fields 1099

host files 1072, 1081

HTML alignment 1635

HTML display formats for reports 581

HTML format 522, 576, 578, 581

HTML heading freezing 1540

HTML index pages 1029

HTML report display formats 581

HTML reports 84, 969, 1022, 1704

JavaScript files 1790

pop-up field descriptions 85

VBScript files 1790

HTML tables of contents 969, 971

HTML tables of contents for multiple sort groups

976

2020

identifying across columns in a style sheet 1254

identifying ACROSS phrase sort data 1265

identifying across totals in a style sheet 1266

identifying ACROSS-TOTAL values 1266

identifying ACROSSVALUE component 1266

identifying cells 1843, 1844, 1874

identifying column report components 1252

identifying columns 1253, 1254, 1264, 1835,

1874

by address 1838, 1839

by number 1836

by relative address 1839

by value 1841

contiguous columns 1837

in financial reports 1835, 1836

identifying data 1261

identifying data report components 1262, 1263

identifying embedded fields in report components

1284, 1285

identifying footings in a style sheet 1277, 1279

identifying free text in FML reports 1277

identifying free text in report components 1277

Index

identifying headings in a style sheet 1277, 1279,

IF/THEN/ELSE statements 467

1280

IMAGE attribute 868, 938, 1462, 1465–1467,

identifying page numbers in report components

1475, 1476, 1481

1288–1290

IMAGEALIGN attribute 1465, 1466

identifying ranges of multiple values 1825

IMAGEBREAK attribute 1465, 1466

identifying report components 1249, 1250

images 868, 870, 1557, 1569

identifying report components for totals and

images and WebFOCUS StyleSheets 1466

subtotals 1256–1258, 1267, 1268, 1270

images in footings 1557, 1569

identifying rows 1832–1834, 1874

images in headings 1557, 1569

in financial reports 1833, 1834

improving performance 198, 1082, 1927, 1929

in WebFOCUS StyleSheets 1874–1876

IN command 1368, 1369

identifying skipped lines in report components

IN-GROUPS-OF option 1779

1288–1290

IN-GROUPS-OF phrase 163, 164

identifying sort value report components 1275

IN-RANGES-OF phrase 163, 165

identifying sort values 1273, 1275

INCLUDES operator 256, 257

identifying subtotal calculations in a style sheet

including JavaScript in an HTML report 582

1272

indentation

identifying subtotals in a style sheet 1270, 1271

specifying between levels 1889

identifying text strings in report components

indenting captions 1859

1282, 1284

independent paths 221, 223

identifying title report components 1273–1276

index optimized retrieval 1926

identifying totals in a style sheet 1270

index pages 1029

identifying underlines in report components 1288,

index pages for headings and footings 1030

1289

INGRES formats 522

IF command with LIKE or UNLIKE 249

inheritance in style sheets 1314, 1327

IF operator 236, 239

inheritance style sheets 1208

IF phrase 218, 249, 259, 260, 429, 1782

inheriting attributes 1207, 1208

IF phrase expressions 429

IF-THEN-ELSE expressions

inline StyleSheets 1198

inline WebFOCUS StyleSheets 1202

and missing tests 1045

inner join 1069, 1085, 1090

Creating Reports With TIBCO® WebFOCUS Language

 2021

Index

inner join structures 1090

INSERT command 1927

INSERT INTO command 1917

inserting blank lines 1440

inserting page breaks 1239

inserting skipped lines 1239

inserting summary lines 1239

JavaScript functions in HTML reports 582

JavaScript requirements 991

JavaScript requirements for Accordion Reports

991

JavaScript

requirements for pop-up field descriptions 85

JOBFILE data source 1940, 1941

inserting text in financial reports 1847, 1848

JOBHIST data source;sample data sources

inserting underlines 1239, 1440

JOBHIST 1953

inserting variables in free text 1848, 1849

JOBLIST data source;sample data sources

inter-row calculations 1831

JOBLIST 1953

internal cascading style sheets (CSS) 1220, 1221

JOIN AS_ROOT 1115

internal cascading style sheets (CSS) and

JOIN CLEAR command 1152

StyleSheets 1309

JOIN command 1071, 1076, 1077, 1081, 1082,

INTERNAL format 523, 558–560

1095, 1102, 1913, 1915–1917

internal matrixes 302, 1840

JOIN command and ALL parameter 1072, 1073

internal storage and field formats 441

JOIN command and SQL Translator 1913,

interpolating X and Y axis values 1771

1915–1917

INTERSECT operator 1921

join structures 1071, 1081, 1082, 1092, 1101,

irrelevant report data 1035, 1036

1913, 1915

IS NOT operator 248, 249

IS operator 248, 249

join structures and CHECK FILE command 1149,

1150

ISO standard date-time formats 454

join structures and DBA security 1072

ITEM attribute 1282

join structures and DEFINE command 1094,

ITEM subtype 1282, 1284, 1654

1095, 1097, 1144, 1145, 1147

ITEMS data source 1959, 1960

join structures and group fields 1093

J

JavaScript files 1790

JavaScript functions 833, 834, 1795

2022

join structures and numeric data types 1101

join structures and qualified field names 1916

join structures and virtual fields 1094, 1095,

1097, 1145, 1147

join structures and WHERE phrase 1149

K

Index

join types 1069

join

from multi-fact synonym 1124

full outer 1105

joining data sources 272, 1071, 1072, 1081,

1100

joining fields 1100, 1101

joins 1069

JPEG format 523

JSCHART format 523

JSON format 524

JSURL parameter 1790

JSURL SET parameter 582

justification regions 1621

JUSTIFY attribute 1617, 1618, 1625, 1665, 1734

justifying column titles 1624–1629

justifying columns 1734

justifying data 1719, 1735

justifying field values 1657

justifying footings 1616

justifying grand totals 1631

justifying headings 1616

justifying headings and footings 1616–1620,

1622, 1623, 1655

justifying labels 1616

justifying report columns 1734

justifying row totals 1629, 1630

justifying subtotals 1631

justifying titles 1616

KEEPDEFINES parameter 1144, 1145

KEEPFILTERS SET parameter 271, 272

key fields 479, 481

keyed retrieval 496, 497

L

LABEL attribute 1255, 1276, 1874–1876

LABEL subtype 1875, 1881

LABELPROMPT attribute 1511, 1512

labels 1510, 1512, 1513, 1517, 1600, 1832

for rows 1833, 1834

formatting rows 1879

lagging values 1074

landscape orientation 1335

last page number 1390

last page number in a sort group 1392

LE operator 245, 465

LEDGER data source 1948, 1949

left margins 1337

left outer join 1069, 1088

left outer join structures 1090

LEFTGAP attribute 1341, 1343, 1346

LEFTMARGIN attribute 1337, 1339, 1340

legacy features 1194

legacy report formatting 1194

LIKE operator 248, 249

limit FORECAST 315, 340

limitations for headings and footings 1519

limitations in display fields 55

Creating Reports With TIBCO® WebFOCUS Language

 2023

Index

limitations of dynamic tables of contents 989

linking report pages and heading text 1025

limitations of HTML tables of contents 989

linking report pages and images 1022

limiting data for graphs 1781

linking report pages and page numbers 1025

limiting display fields 55

limits column titles 1591

limits for display fields 55

LINE attribute 1281

line breaks 1739

linking report pages in HTML reports 1022

linking reports 969, 1022, 1222

linking reports with WebFOCUS StyleSheets 1022

linking summary and detail data 954, 959

linking summary and detail data drill through

line graphs 1749, 1752, 1753, 1760

reports 955, 956

LINE subtype 1281, 1282, 1284, 1654

linking to a Maintain procedure 836, 837

line termination characters 642

linking to external cascading style sheets 1299,

line-by-line formatting 1662

1310

line-feeds 1739

linking to JavaScript functions 833, 834, 1795

linear regression 313, 357, 359

linking to Maintain procedures 837

linear regression analysis 314, 336, 337

linking to Uniform Resource Locators (URLs) 825,

linear regression analysis FORECAST 336, 337

826, 1793

linear regression equation 331, 351, 353

linking to URLs (Uniform Resource Locators) 825,

FORECAST_LINEAR 331

826, 1793

linear regression in graphs 1771

linking with conditions 865–867

linear scales 1750, 1751

LINES SET parameter 1378

links 819, 820

LIST * command 42

LINK element 1298, 1299, 1310

LIST command 39, 41, 54, 88

linking from graphics 868

list records 41

linking graphic elements 868, 870

listing join structures 1151

linking graphs 1792

linking images 868, 870

listing records 41, 42

literals 1921

linking report components 819, 820, 822, 825,

LOAD CHART command 1867, 1868

826, 833, 834, 865, 868, 870, 872, 873, 1793,

load procedures 1937

1795

linking report pages 1022

2024

loading a hierarchy into memory 1867, 1868

Index

LOCATOR data source;sample data sources

Master Files 29, 246, 265, 1855, 1937

LOCATOR 1954

logarithmic scales 1750, 1751

logical expression types 465

for FML hierarchies 1855, 1867, 1868

for hierarchies 1855

hierarchies in 1867, 1868

logical expressions 235, 247, 430, 465

MATCH command 1156, 1158–1160, 1594,

logical operator 247

1595, 1989

logical operators 235, 236, 465

MATCH FILE command 1156, 1158, 1160, 1164,

long field names 1993–1995

1165

LOOKGRAPH parameter 1759, 1760

MATCH FILE command and concatenated data

LOTUS format 524

LST prefix operator 68

sources 1178

MATCH FILE command and display commands

LT operator 245, 246, 465

1170, 1171

M

MACRO attribute 1205

macros 1194, 1204–1206

macros style sheets 1204, 1205

mailing labels 1510–1513

Maintain procedures 836, 837

maintaining across joins 272

maintaining filters 272

maintaining filters across joins 271

margins 1337, 1339

masked fields 248, 250

masking characters 248, 250, 1826

retrieving multiple values with 1826

retrieving values with 1826

masks 248, 249

Master Files 29, 246, 265, 1855, 1937

for financial reports 1855

MATCH FILE command and merge phrases 1158,

1164

MATCH FILE commands 1158

MATCHCOLUMNORDER parameter 1158

matrix reports 140, 141, 367, 370

matrix type reports 140

MATRIXORDER attribute 1511, 1512

MAX prefix operator 61

MAX prefix operators 61

maximum prefix operators 61

MDE prefix operator 62

MDN prefix operator 62

measurement units 1338

measuring fonts 1665

measuring for column width alignment 1665

measuring for decimal alignment 1665

merge phrases 1158, 1165

merge phrases and HOLD files 1158, 1164, 1165

Creating Reports With TIBCO® WebFOCUS Language

 2025

Index

merge phrases and MATCH FILE command 1158,

missing values and extract files 1052

1164

missing values and segment instances 1036,

merging data sources 1156, 1158–1160,

1056–1058

1164–1167, 1169–1171, 1178, 1180, 1181,

missing values and temporary fields 1040

1183

missing values for reformatted fields 1054, 1715

merging data sources and display commands

missing

1170, 1171

in IF-THEN-ELSE expressions 1045

merging data sources and PRINT command 1170,

MORE phrase 1173–1175, 1178

1171

MORE phrase and universal concatenation 1174,

merging data sources and SUM command 1171

1175

merging multiple graphs 1773

MOVIES data source 1959

merging multiple OLAP graphs 1776

multi-fact synonym

metrics file 623, 625, 627

MIME types 579

MIN prefix operator 61

MIN prefix operators 61

and join 1115, 1124

multi-pane reports 1510, 1515

multi-path data sources 45–47, 50, 290

multi-segment data sources 256, 257

minimum prefix operators 61

multi-segment files 256

MISSING attribute 246, 1036, 1049–1051

multi-table HTML reports 1377, 1378, 1381

MISSING attribute and extract files 1052

multi-verb requests 180

MISSING attribute and Master Files 1038, 1039

MULTILINES command 377, 383, 1602, 1605

MISSING attribute and virtual fields 1039

multipath join structures 1090

MISSING attribute limits 1039

MULTIPATH parameter 221–223, 226

missing descendants 1059–1061

multiple display commands 180

missing instances 1036

multiple display commands and ROW-TOTAL 371

missing value data sources 1035

multiple drill-down links and WHEN phrase 853

missing values 246, 1035–1037, 1059, 1060,

multiple drill-down links conditional styling 853

1717, 1782

multiple drill-down reports 1796

missing values and ALL parameter 1059–1061

multiple drill-downs 1796

missing values and ALL prefix 1059

multiple graphs 1772

missing values and DEFINE command 1038–1042

multiple parameters 863

2026

multiple records 1823

NOSPLIT command 1383, 1384

multiple sort fields 90, 91, 107, 180

NOT FROM ... TO operator 243, 244

Index

multiple values 1823

multiple verbs 180

multiple virtual fields 286

multiple web pages 1377

multiple WHERE phrases 220

multiple Y-axis graphs 1768

multiple-line footings 1538

multiplication operator 432, 435

multivariate REGRESS 357–359

N

naming extract files 472

naming output files 472

naming StyleSheet files 1201

naming WebFOCUS StyleSheet files 1201

NOT LIKE operator 248

NOT operator 465

NOTOTAL command 425, 426

null values 1717

numeric constants 1921

numeric data 163, 167

numeric data types 1100

numeric data types and join structures 1101

numeric expressions 430, 435–438

evaluating 437

numeric fields 50

numeric functions 434

numeric operator expressions 432, 435

O

National Language Support (NLS) 188

OBJECT attribute 1282

native-mode arithmetic 437

OBJECT subtype 1654, 1660

navigating between reports 988

OLAPGRMERGE parameter 1776

NE operator 246, 247, 465

NLS (National Language Support) 188

OMITS operator 247

ON phrase 1239

NOBREAK phrase 935

ON TABLE SET command 1313

NODATA character 1035, 1036, 1066, 1067,

on-demand paging 1019, 1021

1717, 1718

non-numeric fields 50, 51

non-recursive models 1852

ONFIELD SET parameter 1240

ONLINE-FMT parameter 578

operand formats 437, 438

non-unique join structures 1069, 1072, 1073

operators 432, 465

NOPRINT command 177, 1372, 1375, 1771,

operators prefix 57

1892

optimized join structures 1926

Creating Reports With TIBCO® WebFOCUS Language

 2027

Index

optimizing join structures 1926

output file format SQLORA 528

optimizing sorting data 188

OR operator 235, 465, 1824

order of evaluation 435, 436

output file format SQLPSTGR 529

output file format SQLSYB 529

output file format SYLK 529

ORIENTATION attribute 1332, 1335, 1336

output file format TAB 530

outer join 1069, 1120

output file AHTML format 512

output file AHTMLTAB format 512

output file format 512

output file format DATREC 516

output file format DFIX 517

output file format GIF 521

output file format HTML 522

output file format TABT 530

output file format WK1 532

output file format WP 532

output file format XFOCUS 533

output file formats 511, 520

XML 534

output file JSON format 524

output file text fields 547, 548

output file format HTMTABLE 522

output files 472, 500

output file format INGRES 522

output file format INTERNAL 523

output file format JPEG 523

output files and missing values 1052

output files text fields 511

output format VISDIS 531

output file format JSCHART 523

output formats 511

output file format LOTUS 524

output file format PDF 524

OVER and column alignment 1360

OVER command 1347, 1357

output file format PDF OPEN/CLOSE 525

overriding attribute inheritance 1210

output file format PostScript (PS) 526

overriding macros 1206

output file format PPT 526

output file format Red Brick 526

output file format SQL_SCRIPT 527

output file format SQLDBC 527

output file format SQLINF 527

output file format SQLMAC 528

output file format SQLMSS 528

output file format SQLODBC 528

2028

P

padded fields 558–560

PAGE BREAK command 1873

page breaks 1377, 1379

page breaks in financial reports 1873

page colors 1331, 1336, 1337

page count 1390, 1392

Index

page footings 1532, 1536, 1538

PCHOLD format 512

page headings 1532, 1533

page layout 1331

page margins 1337, 1339

PCHOLD format DFIX 517

PCHOLD format HTML 522

PCHOLD format HTMTABLE 522

page numbers 1288–1290, 1388, 1390, 1392,

PCHOLD format JSCHART 523

1395, 1397

page numbers in footings 1557

PCHOLD format LOTUS 524

PCHOLD format PDF 524

page numbers in headings 1557

PCHOLD format PDF OPEN/CLOSE 525

page numbers in headings and footings 1567

PCHOLD format PS (PostScript) 526

page orientation 1331, 1335, 1336

page size 1331, 1332

PAGE-BREAK command 1379, 1692

PCHOLD format TAB 530

PCHOLD format TABT 530

PCHOLD format WK1 532

PAGE-NUM SET parameter 1388, 1389, 1397

PCHOLD format WP 532

PAGECOLOR attribute 1332, 1336, 1337

PCHOLD formats 511, 520, 961

PAGEMATRIX attribute 1511, 1512

PAGENUM component 1288–1290

PAGESIZE attribute 1332

PAGESIZE option 621, 622

paginating a report 1377

PCHOLD formats APDF 513

PCHOLD formats FLEX 521

PCHOLD formats in PDF 959

PCHOLD formats PDF 964

PCHOLD formats PDF OPEN/CLOSE 964

panels, repeating headings 1572

PCSEND command 1029

paper size settings 621, 622

parameters 854, 856, 858, 863

parent instances 1059–1061

PCT percent 63

PCT prefix operators 63

PCT.CNT prefix operator 65

parent segments in qualified field values 256

PDF (Portable Document Format) 524

Pareto graphs 1768

PCHOLD AHTML format 512

PDF compound reports 936

PDF display format 576, 578, 585

PCHOLD command 472, 509, 576, 643, 972

PDF display format for compound reports 877,

PCHOLD command and PDF format 936

934

PCHOLD file JSON format 524

PCHOLD files 509

PDF format 576, 584

PDF format on UNIX 641

Creating Reports With TIBCO® WebFOCUS Language

 2029

Index

PDF OPEN/CLOSE and PCHOLD formats 961

positional field references for COMPUTE command

PDF OPEN/CLOSE format 525

301

PDF report display formats 576, 578, 585

positional labels 1832–1834

PDFLINETERM parameter 641–643

positional referencing for columns 301

percent (PCT) 63

percentiles 167

positioning columns 1340–1342, 1346,

1367–1369

performance 188, 1927, 1929

positioning columns for WebFOCUS StyleSheets

performing calculations on dates 441

1734

PERSINFO data source;sample data sources

positioning footings 1671, 1689–1691

PERSINFO 1955

positioning headings 1671, 1688

PICTURE RETRIEVE command 45

positioning headings and footings 1671–1674,

pie graph 1756

1691

pie graphs 1749, 1757, 1762

positioning report components 1340, 1341

placing footings on a separate page 1692, 1694,

positioning reports for headers and footers 1734

1695

positioning with spot markers 1680–1682

placing headings on a separate page 1692, 1694,

POST 862

1695

plotting dates 1779

plotting dates in graphs 1779

PLUS OTHERS phrase 91

polar charts 1767

pop-up field descriptions 84

JavaScript requirements 85

ReportCaster and 85

portrait orientation 1335

POST command 1895

posted data

retrieving 1895, 1896

posting data 1894, 1895

in financial reports 1894

posting financial data 1894

PostScript (PS) format 526, 584

PostScript (PS) reports 621, 622

PostScript display format 576, 578, 620

POSITION attribute 1341–1343, 1465, 1476,

PostScript display format for compound reports

1479–1481, 1671, 1672

877, 934

positional column referenced calculated values

PostScript display formats for reports 621, 622

300

2030

PostScript fonts 623, 625

PostScript fonts in UNIX 625

Index

PostScript fonts in Windows 625

PostScript fonts in z/OS 627

PostScript format 576

PostScript formats 623

PRINTPLUS parameter 1678

procedures sorting data 188

producing a direct percent of a count 65

product position graphs 1768

PostScript report display formats 578, 620–622

protecting virtual fields 291

PostScript Type1 fonts 623

PowerPoint format 526

PPT format 526

precision 54

predicting values 357

PS (PostScript) format 584

Q

qualified field names 1916, 1920, 1921,

1993–1995

prefix operators 56, 57, 389–391, 403, 405, 411,

qualified field names and SQL join structures

413, 414, 1558

MDE 62

MDN 62

preserving field names 484

preserving missing values 1051, 1052, 1056

preserving virtual fields 291

preventing breaks 1383

preventing page breaks 1383

PRINT * command 42

PRINT command 39, 41–43, 88, 1170, 1171

PRINT command and merging data sources 1170,

1171

PRINT command unique segments 50

print display formats 584

PRINT OFFLINE parameter 1815

printing graphs 1814

printing labels 1510, 1511, 1513

printing multi-pane reports 1515

PRINTONLY parameter 490, 492

1916

qualified field names and SQL Translator 1920,

1921

qualified field values 138, 256

QUALTITLES command 1594, 1595

query ? STAT command 189

query commands

? DEFINE 287

?F 1996

?FF 1996

querying HOLD files 473, 477

querying sort types 189

QUIT command 34

quotation marks 457

quote-delimited string 457, 458

R

radar graphs 1749, 1767

Creating Reports With TIBCO® WebFOCUS Language

 2031

Index

range of records

combining 1825

range of values 1825

combining 1825

range tests 243–246

ranges 163–167

RECORDLIMIT relational operator 258, 259

records 41, 218, 1823

in multiple rows 1826, 1827

reusing 1826, 1827

recursive join structures 1076–1078, 1916

recursive models 1852

specifying in financial reports 1825

recursive structures 1076, 1077

RANKED BY phrase 157, 158

RANKED BY TOTAL phrase 156, 175

Red Brick format 526

REDBRICK format 526

ranking columns 175

redefining formats for fields 1713

ranking sort field values 72, 156–158, 172, 173

reducing report width 1355

reading selection values from a file 260–262

ref_regress_usage 358

reading values from a file 262, 263

reformatting fields 292–294, 1736, 1737

READLIMIT operator 258

REGION data source 1950

READLIMIT relational operator 258

REGRESS method 357

RECAP and sort footings 1555

relational expressions 235, 465, 466

RECAP command 421–424, 429, 1817, 1818,

relational operator 248

1831, 1832

relational operators 236, 239, 243, 245–248,

and FML reports 1831

250, 465

RECAP component 1256, 1267, 1268, 1272

relative column addresses 1839, 1840

RECAP expressions 1832

relative point sizes and HTML fonts 1698

creating 1831

RECAP rows 1831

formatting 1881

relative starting positions 1677

removing grids 1409

renaming column titles 1589, 1591, 1592

RECOMPUTE command 383, 385, 389, 390, 403,

renaming column totals 367, 1600

407–409, 411–414

renaming HOLD files AS phrase 473

RECOMPUTE command and propagation to grand

renaming PCHOLD files 509

total 397

renaming row totals 367, 1600

RECOMPUTE prefix operators 413

REPAGE command 1379, 1388, 1389

RECORDLIMIT operator 258, 259

repeating fields 1076

2032

Index

repeating fields in join structures 1076

report styling in external cascading style sheets

repeating rows 1835

report columns 173

1306

report styling with external cascading style sheets

REPORT component 1250, 1251

1293, 1296, 1298

report components 820, 822, 825, 826, 833,

report SUM columns 173

834, 865, 868, 870, 872, 873, 1202, 1249,

report titles 1522–1524

1298, 1697, 1793, 1795

reporting against hierarchies 1853, 1856,

report components, column 1249

1858–1860, 1869

report components, entire report 1249

reporting commands 1985

report components, row 1249

reporting options 1985

report display EXL2K formats 578

reports 29, 32, 34, 820, 969, 1029, 1697, 1703,

report display formats 575, 576, 578, 579

1993

report display PDF formats 584

report display PostScript formats 584

report footings 1525, 1530

report formatting 1187, 1189, 1194

creating 29, 30, 35

creating requests 32

customizing 32, 37

displaying 38

report formatting in external cascading style

displaying data 32

sheets 1306

report formatting methods 1191

report formatting with external cascading style

sheets 1293, 1296, 1298

financial 30

free-form 30

output 32

printing 38

report formatting, inheritance in style sheets 1314

requests 34

report headings 1525, 1526

report navigating 1195

report output formats 1316, 1318, 1320

report pagination 1377

report requests 1907

running 34

saving 38

selecting data 32

sorting data 32

specifying fields 32

report requests and SQL statements 1907

types 30

report styling 1293

requirements for external sorting 188

reserved words 1910

Creating Reports With TIBCO® WebFOCUS Language

 2033

Index

restricting sort field values 156, 158, 172, 173

ROW-TOTAL with ACROSS and multiple display

restrictions for distinct prefix operators 65, 67

commands 371

restrictions for DST prefix operators 67

rows 1255, 1256

restructuring data 1931

retrieval data 221, 223

retrieval limits 258, 259

retrieval logic 1929

retrieval order 196, 197

retrieving data 221, 223

retrieving values for 1821

ROWTOTAL attribute 1258

RPCT prefix operator 63

RPCT row percent 63

rules in external cascading style sheets 1299

RUN command 34

retrieving HOLD Master Files 498

retrieving records 68, 69, 258, 259, 1082

S

returned fields 443

reusing output reports 471

reusing report output 471

right margins 1337

RIGHTGAP attribute 1341, 1343

RIGHTMARGIN attribute 1337, 1339

RNK. prefix operator 72

rotating data sources 1929

rounding numeric values 432

row formatting 1871, 1874

row labels 1832, 1834

row percent (RPCT) 63

row titles 1276, 1870, 1871

PICKUP rows 1896

RECAP rows 1871

TAG rows 1870

row total labels 1600

row totals 367, 370, 371, 374, 375, 1600

ROW-TOTAL phrase 367–369

2034

SALES data source 1943–1945

SALHIST data source;sample data sources

SALHIST 1956

SAME DB 500

SAME_DB extract files 500, 501, 503, 505

SAME_DB HOLD files 500, 501, 503, 505

SAME_DB HOLD format 500, 501, 503

SAME_DB HOLD format columns 505

SAME_DB output files 500, 501, 503, 505

sample data sources 1937

CAR 1945, 1947

Century Corp 1967

COURSE 1952, 1953

EDUCFILE 1942, 1943

EMPLOYEE 1937, 1939, 1940

FINANCE 1949, 1950

Gotham Grinds 1961

ITEMS 1959, 1960

JOBFILE 1940, 1941

sample data sources 1937

LEDGER 1948, 1949

MOVIES 1959

REGION 1950

SALES 1943–1945

TRAINING 1951, 1952

VIDEOTR2 1960, 1961

VideoTrk 1956–1958

SAVB command 506

SAVB files 506

SAVE AHTML format 512

SAVE AHTMLTAB format 512

SAVE command 472, 506

SAVE files 506

SAVE format 512

SAVE format EXL2K 520

SAVE format HTML 522

SAVE format HTMTABLE 522

SAVE format LOTUS 524

SAVE format PDF 524

SAVE format SYLK 529

SAVE format TAB 530

SAVE format TABT 530

SAVE format WP 532

SAVE formats 511, 520

Index

saving intermediate report results 1894

saving output files 472

saving report output 471, 472

saving reports 471, 472

saving rows 1894, 1895

saving virtual fields 1143–1145, 1147

scalar functions 1921

scale graphs 1750, 1751

scales 1750, 1751

scaling 1506, 1508

scaling and vertical bar graphs 1509

scatter graphs 1749, 1758, 1763

screening conditions 265

screening segments 1149

screening values 302

scrollable area for HTML output 1540

search option of WebFOCUS Viewer 1021

SEG. operator 1995

segment instances 1035, 1059–1061

segment instances and missing values

1056–1058

segment locations 289

segment types 68, 69

segments 221, 226, 1036, 1995

SEGTYPE parameter 496

saving drill-down reports with HTMTABLE 1796

selecting graph types 1749

saving graphs as GIF files 1809, 1811

selecting paper size 621, 622

saving graphs as GIF files using SET

selecting paper size for PS (PostScript) format

GRAPHSERVURL 1809

584

saving HOLD Master Files 498, 499

selecting paper size for style sheets 622

Creating Reports With TIBCO® WebFOCUS Language

 2035

Index

selecting paper size PostScript (PS) format 621

SET COMPMISS parameter 1054, 1715

selecting PostScript (PS) format paper size 622

SET COMPOUND parameter 935

selecting records 217, 218, 221, 223, 226–228,

SET COMPUTE = NEW command 1936

235, 236, 239, 243, 247, 248, 256–264, 274,

SET COUNTWIDTH parameter 54

1906

SET CSSURL command 1313

selecting records with IF phrase 261, 262, 264

SET DATEFORMAT parameter 450

selecting records with VSAM 274

SET DEFINES command 1936

selecting sort procedures 189

SET DUPLICATECOL command 181

selecting sort types 189

selecting style sheets 1193

SET EMPTYREPORT parameter 1246

SET EXPANDABLE parameter 989, 1018

selecting values using WHERE phrase 261

SET EXTSORT parameter 188

selecting values with IF phrase 264

SET FILECOMPRESS command 586

selection criteria 217–221, 223, 236, 239, 243,

SET FILTER parameter 265, 268

260–264, 427

selection values 263

SET FOCFIRSTPAGE parameter 1388

SET FORMULTIPLE parameter 1826, 1827

selection values with IF phrase 264

SET GRAPHSERVURL parameter 1809–1811

sending graphs directly to a printer 1815

SET GRMERGE parameter 1773, 1782

SEQUENCE attribute 1354

SET GRWIDTH parameter 1778

sequential conditional formatting 1223

SET GTREND parameter 1771

SET ACROSSPRT 107

SET ALL parameter 1059–1061

SET ASNAMES parameter 484

SET AUTOINDEX parameter 1932

SET HAUTO parameter 1805

SET HAXIS parameter 1800

SET HMAX parameter 1805

SET HMIN parameter 1805

SET AUTOPATH parameter 1932

SET HOLDATTR parameter 484, 495

SET BLANKINDENT parameter 1889

SET HOLDLIST parameter 484, 490–492

SET BYTOC parameter 971

SET CDN parameter 1717

SET HOLDMISS parameter 1051

SET HTMLCSS parameter 1220

SET CNOTATION parameter 302, 303, 1840,

SET JSURL parameter 582

1841

SET KEEPFILTER parameter 271, 272

SET commands 971, 972

SET LINES parameter 1378

2036

Index

SET LOOKGRAPH parameter 1759, 1760

SET SUMARYLINES parameter 397

SET NODATA command 1717

SET NODATA parameter 1717

SET OLAPGRMERGE parameter 1776

SET ONLINE-FMT parameter 578

SET PAGE-NUM parameter 1388

SET parameter ESTLINES 190

SET SUMMARYLINES parameter 398, 408

SET UNITS parameter 1221

SET VAXIS parameter 1800

SET VMAX parameter 1806

SET VMIN parameter 1806

SET WEBVIEWER parameter 1377

SET parameter ESTRECORDS 190

SET WPMINWIDTH 533

SET parameter EXTAGGR 195

SET parameter EXTHOLD 199

SET parameter NULL=ON 531

setting conditions for linking reports 1222

setting fixed scales 1800, 1805, 1806

setting graph height 1800

SET parameters 579, 641, 1198, 1890, 1932

setting graph height and width 1800

ACRSVRBTITL 96

DBAJOIN 1141

DROPBLNKLINE 1456

DUPLICATECOL 181

FIELDNAME 1994

HIDENULLACRS 110

JSURL 1790

setting page colors 1337

setting paper size for PostScript (PS) reports 622

setting retrieval order 197

setting x-axis fixed scales 1800, 1805

setting y-axis fixed scales 1800, 1806

sheet names 1522

SHOW for SAP BW 207

MATCHCOLUMNORDER 1158

SHOWBLANKS SET parameter 579

SET PDFLINETERM parameter 641–643

simple moving average 314, 315, 336, 337, 341,

SET PRINTPLUS parameter 1678

343

SET PSPAGESETUP parameter 621, 622

FORECAST_MOVAVE 315

SET QUALITIES parameter 1594, 1595

single-line footings 1531

SET SHOWBLANKS parameter 579

single-line headings 1527

SET SPACES parameter 1347

SIZE attribute 1465, 1476, 1479–1481

SET SQLTOPTTF parameter 1927

SKIP-LINE option 1440, 1442, 1443

SET STYLE * parameter 1805, 1807

SKIPLINE attribute 1444, 1445

SET STYLEMODE parameter 1378

SKIPLINE component 1288–1290

SET STYLESHEET parameter 1200, 1248

skipped lines 1288–1290, 1442, 1443

Creating Reports With TIBCO® WebFOCUS Language

 2037

Index

sort field values 172

sorting reports 87, 88, 1906

sort fields 87, 969, 972, 1828

sorting rows by 88–91

sort fields for multi-path data sources 89

sorting with COMPUTE command 175

sort fields using multi-path data sources 95

SORTWORK files 190

sort footing limitations 1519

SPACES SET parameter 1347, 1353

sort footings 1518, 1543, 1549, 1552

spacing between columns 1346, 1352, 1353

sort footings and RECAP 1555

specifying date-time values 450

sort footings omitting a display command 1557

specifying fields 32

sort heading limitations 1519

specifying fonts for reports 1703

sort headings 1518, 1543, 1545, 1547, 1662

specifying sort order 149–154

sort multiple fields 90, 107

sort order 90, 107, 163–167

sort phrases 41, 1751

specifying Uniform Resource Locators (URLs) 872

specifying URLs 1467

specifying URLs (Uniform Resource Locators) 872,

sort phrases and graph format 1751

873

sort sequence 89, 95, 1828

sort temporary fields 89, 94

sort values 88, 89, 163

spectral charts 1768

spot markers 1284, 1520

SQL join structures 1913, 1915

sorted by calculated values 175

SQL join structures and qualified field names

sorting a hierarchy 207

sorting alphabetically 1377

1916

SQL SELECT statement 1912

sorting by calculated values 173–175

SQL statements 1907–1909

sorting by columns 95, 96, 107, 175

SQL statements and FOCUS TABLE requests

sorting by rows 89

sorting columns 174

sorting columns by 94

1907

SQL Translation Services 1907–1909

SQL Translator 1907

sorting data 91, 188, 189

SQL Translator and aliases 1916

sorting data by columns 95, 96

SQL Translator and Cartesian product answer sets

sorting data by multiple fields 90, 107

1920

sorting data by rows 88–91

SQL Translator and Continental Decimal Notation

sorting report columns 173, 174

(CDN) 1920

2038

Index

SQL Translator and CREATE TABLE command

SQLODBC formats 528

1917, 1918

SQLORA formats 528

SQL Translator and CREATE VIEW command

SQLPSTGR formats 529

1918, 1919

SQLSYB formats 529

SQL Translator and date formats 1921, 1922

SQLTOPTTF parameter 1927

SQL Translator and date-time values 1923–1925

SQUEEZE attribute 1348–1350

SQL Translator and DELETE command 1927

ST. prefix operator 1558

SQL Translator and DROP VIEW command 1918,

stacking columns 1346, 1355

1919

stacking columns with FOLD-LINE 1356

SQL Translator and expressions 1921

stacking columns with OVER 1357

SQL Translator and field names 1920, 1921

STAT query 189

SQL Translator and index optimized retrieval 1926

stock charts 1765

SQL Translator and INSERT command 1927

storing StyleSheet files 1201

SQL Translator and INSERT INTO command 1917

storing WebFOCUS StyleSheet files 1201

SQL Translator and JOIN command 1913,

structure diagrams 1937

1915–1917

structured HOLD files 563

SQL Translator and join structures 1926

STYLE * parameter 1805, 1807

SQL Translator and reserved words 1910

STYLE attribute 1449, 1699

SQL Translator and SQLTOPTTF parameter 1927

style sheet attributes 1298

SQL Translator and time and timestamp fields

style sheet CLASS attribute (StyleSheets) 1306,

1921, 1922

1307

SQL Translator and UPDATE command 1927

style sheet CSSURL attribute (StyleSheets) 1310,

SQL Translator commands 1910, 1912

1311

SQL Translator commands and formatting

style sheet types 1220

commands 1911

SQL_SCRIPT format 527

SQLDBC format 527

SQLINF format 527

SQLMAC formats 528

SQLMSS formats 528

style sheets 1190, 1197, 1221, 1697, 1871

cascading style sheets (CSS) 1293

multiple output formats 1320

STYLEMODE parameter 1321

STYLEMODE SET parameter 1378

StyleSheet attributes 1871

Creating Reports With TIBCO® WebFOCUS Language

 2039

Index

StyleSheet CLASS attribute 1306, 1307

subroutines 1845

STYLESHEET command 1200

subtotal calculated values 383

StyleSheet CSSURL attribute 1310, 1311

SUBTOTAL command 377, 380–382, 389–391,

StyleSheet declarations 1203, 1204

405, 407, 409–413

StyleSheet files 1200, 1201

STYLESHEET parameter 981

SUBTOTAL command and propagation to grand

total 397

STYLESHEET SET parameter 1248

SUBTOTAL component 1256, 1267, 1268, 1271

StyleSheets and external CSS 1309

subtotal labels 1602

styling ACROSS-TOTAL component 1266

SUBTOTAL prefix operators 413

styling free-form reports 1323

SUBTOTAL SUMMARYLINES command 408

styling graphs 1799

subtotals 383–385, 407, 408, 421–424,

styling reports 1293, 1501, 1502

1256–1258, 1267, 1268, 1600, 1602

styling reports in external cascading style sheets

subtraction operator 435

1306

subtype attribute 820, 825, 833, 837, 1793,

styling reports with external cascading style

1795, 1796

sheets 1293, 1296, 1298

subtypes 820, 1654, 1875

sub-total calculated values 383

SUM command 39, 50, 51, 88, 1170, 1171

SUB-TOTAL command 377, 380–382, 389–391,

SUM command and merging data sources 1170,

405, 407, 408, 410–413

1171

SUB-TOTAL command and propagation to grand

SUM prefix operator 70

total 397

SUMMARIZE command 383, 384, 389, 390, 403,

SUB-TOTAL prefix operators 413

405, 407, 408, 413

SUBFOOT command 1530

SUMMARIZE command and propagation to grand

SUBFOOT command report footings 1530

total 397

SUBFOOT command sort footings 1549

SUMMARIZE prefix operators 413

SUBFOOT component 1277, 1279

summary commands 407, 411

SUBHEAD command 1526, 1545

summary lines 427, 428

report headings 1526

summary values 389, 390, 414

SUBHEAD component 1277, 1279

SUMMARYLINES SET parameter 397, 398, 408

subquery file 527

summing columns 174

2040

summing field values 88

summing report columns 174

summing values 88

SUMPREFIX parameter 197

Index

TABHEADING component 1277, 1279

TABLASTPAGE system variable 1388–1391

TABLE command 1986

TABLE command compared to GRAPH command

SUP-PRINT command 177, 1372, 1375

1745

supplying data directly in FML 1829, 1830

TABLE FILE command 32, 34

supplying images descriptions for screen readers

TABLE requests 1907

1473

supported data sources 1071

suppressing column titles 1593

suppressing display fields 1371

TABLEF command 1927, 1935, 1988

TABLEF command and data retrieval 1935, 1936

TABLEF command and SQL Translator 1927

tables of contents (TOCs) 969

suppressing display in financial reports 1892,

TABPAGENO system variable 1388–1390

1893

suppressing field padding 558–560

TABT format 530

tag names 1077

suppressing grand totals 425, 426

TAG rows 1892, 1893

suppressing page numbers 1398

suppressing rows 1892, 1893

suppressing display in financial reports 1892,

1893

suppressing rows in financial reports 1892, 1893

tag values 1821

suppressing sort field values 177

suppressing sort footings 1554

suppressing wrapping data 1722

SYLK format 529

syn_regress_mult 357

SyncSort utility 188

T

TAB format 530

tab names 1525

tab-delimited output files 530

TABFOOTING component 1277, 1279

reusing 1821, 1826, 1827, 1860

TARGET attribute 873

target frames 873–876

TARGET parameter 991

TARGETFRAME SET parameter 873–876

TD element 1304

temporary fields 277–280

calculated values 297

creating 32

DEFINE FUNCTION 361

evaluation 279

types 278

Creating Reports With TIBCO® WebFOCUS Language

 2041

Index

temporary sort fields 95

timestamp fields and SQL Translator 1922

temporary tables 500, 503, 505

TITLE attribute 495, 1591, 1594

temporary tables extract files 501

TITLE component 1274, 1275

temporary tables HOLD files 503, 505

titles 1273, 1517, 1518, 1522

temporary tables output files 501, 503, 505

titles of column 1275

testing character strings 247–255

titles of columns 1273, 1274

testing data fields 248, 249

TITLETEXT attribute 1523, 1524

testing for blanks or zeros 1050

TO phrase 1825

testing for existing data 246, 247, 1050

TOCs (tables of contents) 969

testing for missing segment instances 1066

TOP 207

testing for missing values 1048, 1049, 1066

top margins 1337

testing multi-segment files 256

TOPGAP attribute 1341, 1343, 1345, 1687

TEXT component 1282

text field output files 547, 548

text fields 89, 1652

TOPMARGIN attribute 1337, 1339

TOT prefix operator 70

total page count 1390

text fields and alphanumeric fields 360

totals 367, 374, 375, 1256–1258, 1267, 1268

text fields in DEFINE and COMPUTE 360

trailing blanks 1562

text fields in headings and footings 1565, 1566

TRAINING data source 1951, 1952

text fields output files 511

treating as literal masking characters 253, 254

text rows 1847, 1848

formatting 1878

text strings 1284

treating as literal wildcard characters 253, 254

treating literal masking characters 255

treating literal wildcard characters 255

three-dimensional graphs 1763

triple exponential smoothing 326, 349, 350

TILE column 167, 168, 171

tile fields 167, 168, 171, 172

FORECAST_SEASONAL 326

truncated field names 1993

TILES phrase 167, 168, 171, 172

truncating decimal values 438

time fields 1921

TYPE attribute 820, 825, 833, 837, 1202, 1449,

time fields and SQL Translator 1922

1508, 1609, 1793, 1795, 1796

timestamp data type 450

timestamp fields 1921

2042

U

UNDER-LINE option 1440, 1446

UNDERLINE attribute 1447, 1448

UNDERLINE component 1288, 1289

underlines 1288, 1289, 1440

underlines in Financial Modeling Language (FML)

reports 1454, 1455

underlines in financial reports 1872

underlining values 1446–1448

Uniform Resource Locators (URLs) 825, 826,

872, 873, 1467, 1793

UNION operator 1921

unique join structures 1069, 1072, 1073, 1085

unique segments 42, 43, 53

unique segments for PRINT command 45

UNITS attribute 1221, 1337

units of measurement 1221, 1338

universal concatenation 1173

universal concatenation and field names 1176,

1177

Index

using ACROSSVALUE component for a numeric

column reference 1266

using BY phrase with Accordion Reports 989

using concatenation with AnV fields 461

using CONTAINS and OMITS with AnV fields 461

using drill-down reports conditions 866, 867

using drill-downs with Accordion Reports 991

using EDIT function with AnV fields 461

using LIKE fields with AnV fields 462

using multiple parameters 863

using operators with AnV fields 462

V

value dates 440

value format for dates 441

values 1824

for columns 1841

in multiple rows 1826, 1827

reusing 1827

variable length character expressions 460, 461

universal concatenation and MORE phrase

variables 357

1173–1175

UNIX 641–643

UNIX PDF files 641–643

UNIX PDF format 643

UNLIKE 249

UPDATE command 1927

URLs (Uniform Resource Locators) 825, 826,

872, 873, 1467, 1793

dependent and independent 357

VAUTO parameter 1806

VAXIS parameter 1800

VBScript files 1790

VBScript in an HTML report 582

verbs 39, 88

verbs, multiple 180

VERBSET attribute 183

using ACROSS phrase with Accordion Reports 989

verifying external sorting 189

Creating Reports With TIBCO® WebFOCUS Language

 2043

Index

vertical bar graphs 1499

WebFOCUS StyleSheet CLASS attribute 1299

vertical bar graphs and scaling 1506, 1508, 1509

WebFOCUS StyleSheet CSSURL attribute 1299

vertical labels 1799

WebFOCUS StyleSheet declarations 1202–1204

vertical scaling 1506, 1508, 1509

WebFOCUS StyleSheet files 1200, 1201

vertical spacing 1685, 1687, 1689

WebFOCUS StyleSheets 969, 981, 983, 1022,

vertical waterfall graphs 1768

VGRID attribute 1403, 1432

1193, 1197, 1198, 1222, 1501, 1504, 1697,

1734

VIDEOTR2 data source 1960, 1961

WebFOCUS StyleSheets and adding graphics

VideoTrk data source 1956–1958

1462, 1474

viewing reports 969

WebFOCUS StyleSheets and conditional styling

virtual fields 265, 266, 278–280, 289, 290

1222, 1223, 1225, 1226, 1228, 1231, 1232,

calculated values 279

1234

VISDIS 531

WebFOCUS StyleSheets and data visualization

Visual Discovery format 531

1499, 1501, 1502, 1504

VMAX parameter 1806

VMIN parameter 1806

VMSORT utility 188

VSAM data sources 274

WebFOCUS StyleSheets and graphics 1466,

1476, 1481

WebFOCUS StyleSheets and graphs 1787

WebFOCUS StyleSheets and links 819, 820

VSAM record selection efficiencies 274

WebFOCUS StyleSheets and multi-pane reports

VZERO parameter 1783

1510, 1515

WebFOCUS StyleSheets and parameters 854, 858

W

waterfall graphs 1768

web browser support for cascading style sheets

1323

WebFOCUS font map files 625

WebFOCUS Font Map files 623

WebFOCUS inheritance StyleSheets 1207, 1208

WebFOCUS macros StyleSheets 1204, 1205

WebFOCUS style sheets 1202, 1204, 1207, 1208

2044

WebFOCUS StyleSheets macros 1204

WebFOCUS Viewer 969, 1019

WebFOCUS Viewer search option 1021

WEBVIEWER SET parameter 1377

WHEN attribute 1222, 1223

WHEN EXISTS phrase 1893

WHEN for SAP BW 207

WHEN phrase 378, 427, 429, 1241

WHEN phrase and conditional formatting 1239,

WPMINWIDTH parameter 533

1241–1244, 1553

WRAP attribute 1719, 1721

WHEN phrase expressions 429

wrapgap StyleSheet attribute 1731

WHEN=FORECAST attribute 315, 340, 1225

wrapping data 1719

WHERE operator 236, 239, 245, 246

wrapping data by Web browser functionality 1722

Index

WHERE phrase 218–220, 226, 228, 235, 248,

wrapping data reports 1719

250, 260, 261, 263, 429, 1782

WRITE command 50

WHERE phrase and existing data 1050

WHERE phrase and join structures 1149

X

WHERE phrase and missing values 1049, 1051

WHERE phrase expressions 429

WHERE tests 242

WHERE TOTAL phrase 226–228, 1782

WHERE_GROUPED 228

WHERE-based join structures 1069

WIDTH attribute 1665

width of borders 1405

x-axis 1769, 1772

XFOCUS format 533

XLSX display format 519

XLSX output file format 519

XLSX PCHOLD format 519

XLSX SAVE format 519

XML format 534

width of columns 1347–1350, 1352

Y

wildcard characters 248, 250

window titles 1522

WITH CHILDREN parameter 1856

WITHIN phrase 138

WK1 format 532

worksheet names 1525

worksheet titles 1522

WP display formats for reports 643

WP format 532, 576, 643

WP report display formats 643

y-axis 1769

y-axis fields 1771

Y2K attributes in Master Files 450

Year 2000 attributes in Master Files 450

YRTHRESH attribute 450

Z

z/OS requirements 188

zeros 1050

Creating Reports With TIBCO® WebFOCUS Language

 2045

Index

2046

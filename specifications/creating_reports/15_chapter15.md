Chapter15

Merging Data Sources

You can gather data for your reports by merging the contents of data structures with the
MATCH command, or concatenating data sources with the MORE phrase, and reporting
from the combined data.

In this chapter:

Merging Data

Types of MATCH Processing

MATCH Processing With Common High-Order Sort Fields

Fine-Tuning MATCH Processing

Universal Concatenation

Merging Concatenated Data Sources

Cartesian Product

Merging Data

You can merge two or more data sources, and specify which records to merge and which to
sort out, using the MATCH command. The command creates a new data source (a HOLD file),
into which it merges fields from the selected records. You can report from the new data source
and use it as you would use any other HOLD file.

You select the records to be merged into the new data source by specifying sort fields in the
MATCH command. You specify one set of sort fields (using the BY phrase), for the first data
source, and a second set of sort fields for the second data source. The MATCH command
compares all sort fields that have been specified in common for both data sources, and then
merges all records from the first data source whose sort values match those in the second
data source into the new HOLD file. You can specify up to 128 sort sets. This includes the
number of common sort fields.

In addition to merging data source records that share values, you can merge records based on
other relationships. For example, you can merge all records in each data source whose sort
values are not matched in the other data source. Yet another type of merge combines all
records from the first data source with any matching records from the second data source.

Creating Reports With TIBCO® WebFOCUS Language

 1155

Merging Data

You can merge up to 16 sets of data in one Match request. For example, you can merge
different data sources, or data from the same data source.

Note: The limit of 16 applies to the most complex request. Simpler requests may be able to
merge more data sources.

Syntax:

How to Merge Data Sources

The syntax of the MATCH command is similar to that of the TABLE command:

MATCH FILE file1
.
.
.
RUN
FILE file2
.
.
.
[AFTER MATCH merge_phrase]
RUN
FILE file3
.
.
.
[AFTER MATCH merge_phrase]
END

where:

file1

Is the first data source from which MATCH retrieves requested records.

merge_phrase

Specifies how the retrieved records from the files are to be compared. For details, see
Merge Phrases on page 1163.

file2/file3

Are additional data sources from which MATCH retrieves requested records.

Note that a RUN command must follow each AFTER MATCH command (except for the last one).
The END command must follow the final AFTER MATCH command.

MATCH generates a HOLD file. You can print the contents of the HOLD file using the PRINT
command with the wildcard character (*).

1156

Types of MATCH Processing

15. Merging Data Sources

There are two types of MATCH processing, grouped and ungrouped. Grouped processing is the
newer type of MATCH processing, and is the processing used by default. Ungrouped
processing is the legacy MATCH processing. If you need to invoke legacy processing, you can
use the SET MATCHCOLUMNORDER = UNGROUPED command.

In all MATCH requests:

The two sides of the merge, the OLD and the NEW, are matched together based on their
common high-order BY fields. In order for actual matching to take place between the OLD
and NEW files, the high-order BY fields have to be the same. If there are no common high-
order BY fields, the records are concatenated on a record-by-record basis.

The output selected from the OLD and NEW sides is based on the AFTER MATCH
command.

The output stage of the MATCH differs for grouped and ungrouped processing.

With grouped processing, the output file has each common sort key (BY field) followed its
display fields in the order specified in the request. As a result, ungrouped processing is
limited to flat file output.

In contrast, with grouped processing, fields in the request are grouped with their highest
common sort fields in the output file. This enables you to generate multi-segment
hierarchical output files in FOCUS or XFOCUS format by using multiple display commands
on each side of the merge. In fact, you can create the output file using any format that has
a corresponding Master File.

For standard MATCH requests that use the same sort keys on both sides of the MATCH (OLD
and NEW), grouped and ungrouped processing produce the same output.

However, in requests that use multiple display commands or differing sort fields on each side
of the merge, the grouping of fields with their sort keys can produce output files in which the
field order is different from the legacy processing. In any case where the new behavior
generates output that is different from previous results and not desireable, the SET
MATCHCOLUMNORDER command is available to return the legacy results.

For example, if you use MATCH to create output that includes a list of products with columns
of aggregations based on differing sorts, MATCHCOLUMNORDER=UNGROUPED will ensure that
the sequence of the column output will remain what it was in the past.

Creating Reports With TIBCO® WebFOCUS Language

 1157

Types of MATCH Processing

The way MATCH merges data depends on the order in which you name data sources in the
request, the BY fields, display commands, the type of processing, and the merge phrases you
use. In general, however, processing is as follows:

1. MATCH retrieves requested records from the first data source you name, and writes them

to a temporary work area.

2. MATCH retrieves requested records from the second data source you name, and writes

them to a temporary work area.

3. It compares the common high-order sort fields from the retrieved records as specified in

the merge phrase (for example, OLD-OR-NEW). For more information, see Merge Phrases on
page 1163.

4. If the default grouped processing is in effect, it may re-order the fields to group them under

their common sort fields.

5. It writes the merged results of the comparison to a temporary data source (if there are

more MATCH operations). It cycles through all data sources named until END is
encountered.

6. It writes final records to the HOLD file.

Syntax:

How to Controlling MATCH Processing

SET MATCHCOLUMNORDER = {GROUPED|UNGROUPED}

where:

GROUPED

Groups fields in the output file under their common high-order sort fields. This is the
default value.

UNGROUPED

Does not group fields in the output file with their common hig-order sort fields, but lays
them out as specified in the MATCH request.

Reference: Usage Notes for Match Requests

With ungrouped processing, you cannot specify a format for the HOLD file generated by
MATCH. It will be created as a single-segment BINARY or ALPHA HOLD file, depending on
the value of the HOLDFORMAT parameter. The merge process does not change the original
data sources.

1158

15. Merging Data Sources

Alias names are assigned sequentially (E01, E02, ...) in the HOLD Master File that results
from the MATCH request. When the same field name is used mutliple times in the MATCH,
users distinguish between them in requests against the HOLD file by referencing these
alias names instead of the field names.

With grouped processing, fields are rearranged in the Master File, and this causes the alias
names to represent different fields from the same alias names assigned with ungrouped
processing. This can produce different results if you switch from one type of processing to
the other.

To avoid using alias names, use the AS phrase in your MATCH request to create distinct
field names (except for the common high-order BY fields, which have to be the same), and
use those field names in requests against the HOLD file.

The ACROSS, BY HIGHEST/LOWEST n, IN-GROUPS-OF, WHERE TOTAL, and IF TOTAL
phrases, and the COMPUTE command, are not permitted in a MATCH request. You can,
however, use the DEFINE command.

Up to 128 BY phrases and the maximun number of display fields can be used in each
MATCH request. The count of sort sets includes the number of common sort fields. The
maximum number of display fields is determined by a combination of factors.

For details, see Displaying Report Data on page 39.

You must specify at least one BY field for each file used in the MATCH request.

When used with MATCH, the SET HOLDLIST parameter behaves as if HOLDLIST were set to
ALL.

The following prefix operators are not supported in MATCH requests: DST., DST.CNT., RNK.,
ST., and CT.

Creating Reports With TIBCO® WebFOCUS Language

 1159

Types of MATCH Processing

Example: Merging Data Sources

In the following request, the high-order sort field is the same for both files, so the result is the
same using grouped and ungrouped processing.

MATCH FILE EDUCFILE
SUM COURSE_CODE
BY EMP_ID
RUN
FILE EMPLOYEE
SUM LAST_NAME AND FIRST_NAME
BY EMP_ID BY CURR_SAL
AFTER MATCH HOLD OLD-OR-NEW
END
-******************************
-*  PRINT CONTENTS OF HOLD FILE
-******************************
TABLE FILE HOLD
PRINT *
END

The merge phrase used in this example was OLD-OR-NEW. This means that records from both
the first (old) data source plus the records from the second (new) data source appear in the
HOLD file.

The output is:

EMP_ID     COURSE_CODE         CURR_SAL  LAST_NAME        FIRST_NAME
------     -----------         --------  ---------        ----------
071382660  101               $11,000.00  STEVENS          ALFRED
112847612  103               $13,200.00  SMITH            MARY
117593129  203               $18,480.00  JONES            DIANE
119265415  108                $9,500.00  SMITH            RICHARD
119329144                    $29,700.00  BANNING          JOHN
123764317                    $26,862.00  IRVING           JOAN
126724188                    $21,120.00  ROMANS           ANTHONY
212289111  103                     $.00
219984371                    $18,480.00  MCCOY            JOHN
315548712  108                     $.00
326179357  301               $21,780.00  BLACKWOOD        ROSEMARIE
451123478  101               $16,100.00  MCKNIGHT         ROGER
543729165                     $9,000.00  GREENSPAN        MARY
818692173  302               $27,062.00  CROSS            BARBARA

1160

Example:

Comparing Grouped and Ungrouped Processing

The following MATCH request has two SUM commands and one PRINT command for each file,
with all sort fields common to both files. The SET MATCHCOLUMNORDER = UNGROUPED
command is issued to invoke legacy processing.

15. Merging Data Sources

SET MATCHCOLUMNORDER = UNGROUPED
MATCH FILE GGSALES
SUM DOLLARS
BY ST
SUM BUDDOLLARS BY ST BY CITY
PRINT UNITS BY ST BY CITY BY CATEGORY
RUN
FILE GGSALES
SUM DOLLARS
BY ST
SUM BUDDOLLARS BY ST BY CITY
PRINT BUDUNITS BY ST BY CITY BY CATEGORY
AFTER MATCH HOLD OLD-OR-NEW
END
TABLE FILE HOLD
PRINT *
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, SIZE=9,$
ENDSTYLE
END

The HOLD Master File follows. Since the sort fields are common to both files, the two files
were merged based on those fields. However, note that the order of fields in the Master File
follows the order in the request, the highest-level sort field followed by its display field, then
the next sort field followed by its display fields, and so on.

FILENAME=HOLD, SUFFIX=FIX     , IOTYPE=BINARY, $
  SEGMENT=HOLD, SEGTYPE=S1, $
    FIELDNAME=ST, ALIAS=E01, USAGE=A02, ACTUAL=A04, $
    FIELDNAME=DOLLARS, ALIAS=E02, USAGE=I08, ACTUAL=I04, $
    FIELDNAME=CITY, ALIAS=E03, USAGE=A20, ACTUAL=A20, $
    FIELDNAME=BUDDOLLARS, ALIAS=E04, USAGE=I08, ACTUAL=I04, $
    FIELDNAME=CATEGORY, ALIAS=E05, USAGE=A11, ACTUAL=A12, $
    FIELDNAME=UNITS, ALIAS=E06, USAGE=I08, ACTUAL=I04, $
    FIELDNAME=DOLLARS, ALIAS=E07, USAGE=I08, ACTUAL=I04, $
    FIELDNAME=BUDDOLLARS, ALIAS=E08, USAGE=I08, ACTUAL=I04, $
    FIELDNAME=BUDUNITS, ALIAS=E09, USAGE=I08, ACTUAL=I04, $

Creating Reports With TIBCO® WebFOCUS Language

 1161

Types of MATCH Processing

The partial output is shown in the following image.

Changing the UNGROUPED setting to GROUPED produces the following Master File. The fields
that have the same common sort fields from both files are moved to be under those sort fields
in the Master File.

FILENAME=HOLD, SUFFIX=FIX     , IOTYPE=BINARY, $
  SEGMENT=HOLD, SEGTYPE=S1, $
    FIELDNAME=ST, ALIAS=E01, USAGE=A02, ACTUAL=A04, $
    FIELDNAME=DOLLARS, ALIAS=E02, USAGE=I08, ACTUAL=I04, $
    FIELDNAME=DOLLARS, ALIAS=E03, USAGE=I08, ACTUAL=I04, $
    FIELDNAME=CITY, ALIAS=E04, USAGE=A20, ACTUAL=A20, $
    FIELDNAME=BUDDOLLARS, ALIAS=E05, USAGE=I08, ACTUAL=I04, $
    FIELDNAME=BUDDOLLARS, ALIAS=E06, USAGE=I08, ACTUAL=I04, $
    FIELDNAME=CATEGORY, ALIAS=E07, USAGE=A11, ACTUAL=A12, $
    FIELDNAME=UNITS, ALIAS=E08, USAGE=I08, ACTUAL=I04, $
    FIELDNAME=BUDUNITS, ALIAS=E09, USAGE=I08, ACTUAL=I04, $

The partial output is shown in the following image.

For the request that uses the GROUPED value for MATCHCOLUMNORDER, you can change the
HOLD command to produce a FORMAT FOCUS output file, as follows.

AFTER MATCH HOLD FORMAT FOCUS OLD-OR-NEW

1162

15. Merging Data Sources

The following hierarchical multi-segment Master File is generated.

FILENAME=HOLD    , SUFFIX=FOC     , $
  SEGMENT=SEG01, SEGTYPE=S1, $
    FIELDNAME=ST, ALIAS=E01, USAGE=A02,
      TITLE='State', DESCRIPTION='State', $
    FIELDNAME=DOLLARS, ALIAS=E02, USAGE=I08,
      TITLE='Dollar Sales', DESCRIPTION='Total dollar amount of reported
sales', $
    FIELDNAME=DOLLARS, ALIAS=E03, USAGE=I08,
      TITLE='Dollar Sales', DESCRIPTION='Total dollar amount of reported
sales', $
  SEGMENT=SEG02, SEGTYPE=S1, PARENT=SEG01, $
    FIELDNAME=CITY, ALIAS=E04, USAGE=A20,
      TITLE='City', DESCRIPTION='City', $
    FIELDNAME=BUDDOLLARS, ALIAS=E05, USAGE=I08,
      TITLE='Budget Dollars', DESCRIPTION='Total sales quota in dollars', $
    FIELDNAME=BUDDOLLARS, ALIAS=E06, USAGE=I08,
      TITLE='Budget Dollars', DESCRIPTION='Total sales quota in dollars', $
  SEGMENT=SEG03, SEGTYPE=S2, PARENT=SEG02, $
    FIELDNAME=CATEGORY, ALIAS=E07, USAGE=A11,
      TITLE='Category', DESCRIPTION='Product category', $
    FIELDNAME=FOCLIST, ALIAS=E08, USAGE=I5, $
    FIELDNAME=UNITS, ALIAS=E09, USAGE=I08,
      TITLE='Unit Sales', DESCRIPTION='Number of units sold', $
  SEGMENT=SEG04, SEGTYPE=S1, PARENT=SEG03, $
    FIELDNAME=FOCLIST, ALIAS=E10, USAGE=I5, $
    FIELDNAME=BUDUNITS, ALIAS=E11, USAGE=I08,
      TITLE='Budget Units', DESCRIPTION='Number of units budgeted', $

Reference: Merge Phrases

MATCH logic depends on the concept of old and new data sources. Old refers to the first data
source named in the request, and new refers to the second data source. The result of each
merge creates a HOLD file until the END command is encountered.

Creating Reports With TIBCO® WebFOCUS Language

 1163

Types of MATCH Processing

The following diagram illustrates the general merge process:

1164

15. Merging Data Sources

Syntax:

How to Specify Merge Phrases

AFTER MATCH HOLD [AS 'name'] mergetype

where:

AS 'name'

Specifies the name of the extract data source created by the MATCH command. The
default is HOLD.

mergetype

Specifies how the retrieved records from the files are to be compared.

The results of each phrase are graphically represented using Venn diagrams. In the
diagrams, the left circle represents the old data source, the right circle represents the new
data source, and the shaded areas represent the data that is written to the HOLD file.

OLD-OR-NEW specifies that all records from both the old data source and the new data
source appear in the HOLD file. This is the default if the AFTER MATCH line is omitted.

OLD-AND-NEW specifies that records that appear in both the old and new data sources
appear in the HOLD file. (The intersection of the sets.)

OLD-NOT-NEW specifies that records that appear only in the old data source appear in the
HOLD file.

Creating Reports With TIBCO® WebFOCUS Language

 1165

MATCH Processing With Common High-Order Sort Fields

NEW-NOT-OLD specifies that records that appear only in the new data source appear in the
HOLD file.

OLD-NOR-NEW specifies that only records that are in the old data source but not in the new
data source, or in the new data source but not in the old, appear in the HOLD file (the
complete set of non-matching records from both data sources).

OLD specifies that all records from the old data source, and any matching records from the
new data source, are merged into the HOLD file.

NEW specifies that all records from the new data source, and any matching records from
the old data source, are merged into the HOLD file.

MATCH Processing With Common High-Order Sort Fields

When you construct your MATCH so that the first sort (BY) field (called the common high-order
sort field) used for both data sources is the same, the match compares the values of the
common high-order sort fields. If the entire sequence of sort fields is common to both files, all
are compared.

1166

15. Merging Data Sources

At least one pair of sort fields is required. Field formats must be the same. In some cases, you
can redefine a field format using the DEFINE command. If the field names differ, use the AS
phrase to rename the second sort field to match the first. When the AS phrase is used in a
MATCH request, the specified field is automatically renamed in the resulting HOLD file.

When you are merging files with common sort fields, the following assumptions are made:

If one of the sort fields is a subset of the other, a one-to-many relationship is assumed.

If neither of the sort fields is a subset of the other, a one-to-one relationship is assumed.
At most, one matching record is retrieved.

Example: MATCH Processing With Common High-Order Sort Fields

To understand common high-order sort fields more clearly, consider some of the data from the
following data sources

EMPLOYEE Data Source

EDUCFILE Data Source

071382660

STEVENS

071382660

119329144

BANNING

212289111

112847612

SMITH

112847612

101

103

103

and this MATCH request:

MATCH FILE EMPLOYEE
SUM LAST_NAME BY EMP_ID
RUN
FILE EDUCFILE
SUM COURSE_CODE BY EMP_ID
AFTER MATCH HOLD OLD-OR-NEW
END

MATCH processing occurs as follows:

Since there is a common high-order sort field (EMP_ID), the MATCH logic begins by
matching the EMP_ID values in records from the EMPLOYEE and EDUCFILE files.

There are records from both files with an EMP_ID value of 071382660. Since there is a
match, this record is written to the HOLD file:

Record n: 071382660 STEVENS 101

There are records from both files with an EMP_ID value of 112847612. Since there is a
match, this record is written to the HOLD file:

Creating Reports With TIBCO® WebFOCUS Language

 1167

MATCH Processing With Common High-Order Sort Fields

Record n: 112847612 SMITH 103

The records do not match where a record from the EMPLOYEE file has an EMP_ID value of
119329144 and a record from the EDUCFILE file has an EMP_ID value of 212289111. The
record with the lower value is written to the HOLD file and a space is inserted for the
missing value:

Record n: 119329144 BANNING

Similarly, the 212289111 record exists only in the EDUCFILE file, and is written as:

Record n: 212289111 103

The following code produces a report of the records in the HOLD file:

TABLE FILE HOLD
PRINT *
END

The output is:

EMP_ID

071382660

112847612

117593129

119265415

119329144

123764317

126724188

212289111

219984371

315548712

326179357

451123478

543729165

818692173

1168

LAST_NAME

STEVENS

SMITH

JONES

SMITH

BANNING

IRVING

ROMANS

MCCOY

BLACKWOOD

MCKNIGHT

GREENSPAN

CROSS

COURSE_CODE

101

103

203

108

103

108

301

101

302








Example: Merging With a Common High-Order Sort Field

This request combines data from the EMPLOYEE and EMPDATA data sources. The sort fields
are EID and PIN.

15. Merging Data Sources

MATCH FILE EMPLOYEE
PRINT LN FN DPT
BY EID
RUN
FILE EMPDATA
PRINT LN FN DEPT
BY PIN
AFTER MATCH HOLD OLD-OR-NEW
END

TABLE FILE HOLD
PRINT *
END

Example: Merging Without a Common High-Order Sort Field

If there are no common high-order sort fields, a match is performed on a record-by-record
basis. The following request matches the data and produces the HOLD file:

MATCH FILE EMPLOYEE
PRINT LAST_NAME AND FIRST_NAME
BY EMP_ID
RUN
FILE EMPDATA
PRINT PIN
BY LASTNAME
BY FIRSTNAME
AFTER MATCH HOLD OLD-OR-NEW
END

TABLE FILE HOLD
PRINT *
END

The retrieved records from the two data sources are written to the HOLD file; no values are
compared. The output is:

EMP_ID

LAST_NAME

FIRST_NAME

LASTNAME

FIRSTNAM
E

PIN

071382660

STEVENS

ALFRED

  ADAMS

RUTH

000000040

112847612

SMITH

117593129

JONES

MARY

DIANE

  ADDAMS

PETER

000000050

  ANDERSON

TIM

000000100

119265415

SMITH

RICHARD

  BELLA

MICHAEL

000000020

Creating Reports With TIBCO® WebFOCUS Language

 1169



Fine-Tuning MATCH Processing

119329144

BANNING

123764317

IRVING

JOHN

JOAN

  CASSANOVA

LOIS

000000030

MARIE

000000270

CASTALANETT
A

126724188

ROMANS

ANTHONY

  CHISOLM

HENRY

000000360

219984371

MCCOY

JOHN

  CONRAD

ADAM

000000250

326179357

BLACKWOOD

ROSEMARIE

  CONTI

MARSHALL

000000410

451123478

MCKNIGHT

ROGER

  CVEK

MARCUS

000000130

543729165

GREENSPAN

MARY

  DONATELLO

ERICA

000000320

818692173

CROSS

BARBARA

  DUBOIS

ERIC

000000210

  ELLNER

DAVID

000000380

  FERNSTEIN

ERWIN

000000350

  GORDON

LAURA

000000180

  GOTLIEB

CHRIS

000000340

  GRAFF

ELAINE

000000390

  HIRSCHMAN

ROSE

000000160

  KASHMAN

YOLANDA

000000240

  LASTRA

KAREN

000000200

  LEWIS

CASSANDR
A

000000220

.
.
.

Fine-Tuning MATCH Processing

You can fine-tune the MATCH process using the PRINT and SUM commands. To understand
their difference, you should have an understanding of the one-to-many relationship: SUM
generates one record from many, while PRINT displays each individual record. Through proper
choices of BY fields, it is possible to use only the SUM command and get the same result that
PRINT would produce.

1170





























Example:

Using Display Commands in MATCH Processing

To illustrate the effects of PRINT and SUM on the MATCH process, consider data sources A
and B and the series of requests that follow:

15. Merging Data Sources

     A               B

F1  F2  F3      F1  F4  F5

1   x   100     1   a   10
2   y   200     1   b   20
                2   c   30
                2   d   40

Request 1: This request sums the fields F2 and F3 from file A, sums the fields F4 and F5 from
file B, and uses F1 as the common high-order sort field.

MATCH FILE A
SUM F2 AND F3 BY F1
RUN
FILE B
SUM F4 AND F5 BY F1
AFTER MATCH HOLD OLD-OR-NEW
END

The HOLD file contains the following data:

F1   F2   F3   F4   F5

1    x    100  b    30
2    y    200  d    70

Note that the resulting file contains only 1 record for each common high-order sort field.

Request 2: This request sums fields F2 and F3 from file A, prints fields F4 and F5 from file B,
and uses F1 as the common high-order sort field.

MATCH FILE A
SUM F2 AND F3 BY F1
RUN
FILE B PRINT F4 AND F5 BY F1
AFTER MATCH HOLD OLD-OR-NEW
END

The HOLD file contains:

F1   F2   F3   F4   F5

1    x    100  a    10
1    x    100  b    20
2    y    200  c    30
2    y    200  d    40

Creating Reports With TIBCO® WebFOCUS Language

 1171





Fine-Tuning MATCH Processing

Note that the records from file A are duplicated for each record from file B.

Request 3: This request prints fields F2 and F3 from file A, sums fields F4 and F5 from file B,
and uses F1 as the common high-order sort field.

MATCH FILE A
PRINT F2 AND F3 BY F1
RUN
FILE B
SUM F4 AND F5 BY F1
AFTER MATCH HOLD OLD-OR-NEW
END

The HOLD file contains:

F1   F2   F3   F4   F5

1    x    100  b    30
2    y    200  d    70

Note that each record from file A is included, but only the last record from file B for each
common high-order sort field is included.

Request 4: This request prints fields F2 and F3 from file A, prints fields F4 and F5 from file B,
and uses F1 as the common high-order sort field.

MATCH FILE A
PRINT F2 AND F3 BY F1
RUN
FILE B PRINT F4 AND F5 BY F1
AFTER MATCH HOLD OLD-OR-NEW
END

The HOLD file contains:

F1   F2   F3   F4   F5

1    x    100  a    10
1         0    b    20
2    y    200  c    30
2         0    d    40

Note the blank value for F2 and the 0 for F3.

1172



Request 5: This request sums the fields F2 and F3 from file A, sums the field F5 from file B
and sorts it by field F1, the common high-order sort field, and by F4.

15. Merging Data Sources

MATCH FILE A
SUM F2 AND F3 BY F1
RUN
FILE B
SUM F5 BY F1 BY F4
AFTER MATCH HOLD OLD-OR-NEW
END

The HOLD file contains:

F1   F2   F3   F4   F5

1    x    100  a    10
1    x    100  b    20
2    y    200  c    30
2    y    200  d    40

Note that the records for file A are printed for every occurrence of the record in file B.

Universal Concatenation

With universal concatenation, you can retrieve data from unlike data sources in a single
request; all data, regardless of source, appears to come from a single file. The MORE phrase
can concatenate all types of data sources (such as, FOCUS, DB2, IMS, and VSAM), provided
they share corresponding fields with the same format. You can use WHERE and IF selection
tests in conjunction with MORE. For related information, see Selecting Records for Your Report
on page 217.

To use MORE, you must divide your request into:

One main request that retrieves the first data source and defines the data fields, sorting
criteria, and output format for all data.

Subrequests that define the data sources and fields to be concatenated to the data of the
main request. The fields printed and sorted by the main request must exist in each
concatenated data source. If they do not, you must create them as virtual fields.

During retrieval, data is gathered from each data source in turn, then all data is sorted and the
output formatted as specified in the main request.

Creating Reports With TIBCO® WebFOCUS Language

 1173


Universal Concatenation

Syntax:

How to Concatenate Data Sources

The MORE phrase, which is accessible within the TABLE and MATCH commands, specifies how
to concatenate data from sources with dissimilar Master Files.

{TABLE|MATCH}  FILE file1main request
MORE
FILE file2
  subrequest
MORE
FILE file3
  subrequest
MORE
   .
   .
   .
{END|RUN}

where:

TABLE|MATCH

Begins the request that concatenates the data sources.

file1

Is the name of the first data source.

main request

Is a request, without END or RUN, that retrieves the first data source and defines the data
fields, sorting criteria, and output format for all data. WHERE and IF criteria in the main
request apply only to file1.

When concatenating files within the TABLE command, you can also define calculated
values for the first data source.

MORE

Begins a subrequest. There is no limit to the number of subrequests, other than available
memory.

FILE file2

Defines file2 as the second data source for concatenation.

subrequest

Is a subrequest. Subrequests can only include WHERE and IF phrases.

1174

15. Merging Data Sources

END|RUN

Ends the request.

Example:

Concatenating Data Sources

Both the EMPLOYEE and the EXPERSON data sources contain employee information. You can
concatenate their common data into a single file:

EMPLOYEE contains the field values EMP_ID=123456789 and CURR_SAL=50.00.

EXPERSON contains the field values SSN=987654321 and WAGE=100.00.

The following annotated request concatenates the two data sources:

   DEFINE FILE EXPERSON
1. EMP_ID/A9 = SSN;
   CURR_SAL/D12.2 = WAGE;
   END
2. TABLE FILE EMPLOYEE
   PRINT CURR_SAL
   BY EMP_ID
3. MORE
   FILE EXPERSON
   END

1. The request must re-map the field names and formats in the EXPERSON data source to

match those used in the main request.

2. The main request names the first data source in the concatenation, EMPLOYEE. It also

defines the print and sort fields for both data sources.

3. The MORE phrase starts the subrequest that concatenates the next data source,

EXPERSON. No display commands are allowed in the subrequest. IF and WHERE criteria are
the only report components permitted in a subrequest.

Creating Reports With TIBCO® WebFOCUS Language

 1175

Universal Concatenation

Field Name and Format Matching

All fields referenced in the main request must either exist with the same names and formats in
all the concatenated files, or be remapped to those names and formats using virtual fields.
Referenced fields include those used in COMPUTE commands, headings, aggregation phrases,
sort phrases, and the PRINT, LIST, SUM, COUNT, WRITE, or ADD commands.

A successful format match means that:

Usage Format Type

Correspondence

A

I, F, D

P

DATE (new)

DATE (old)

DATE -TIME

Format type and length must be equal.

Format type must be the same.

Format type and scale must be equal.

Format information (type, length, components, and order) must
always correspond.

Edit options must be the same.

Format information (type, length, components, and order) must
always correspond.

Text (TX) fields and CLOB fields (if supported) cannot be concatenated.

1176

Example: Matching Field Names and Formats

The following annotated example concatenates data from the EMPDATA and SALHIST data
sources.

15. Merging Data Sources

   DEFINE FILE EMPDATA
1. NEWID/A11=EDIT (ID,'999-99-9999');
   END

   DEFINE FILE SALHIST
2. NEWID/A11=EDIT (ID,'999-99-9999');
   CSAL/D12.2M=OLDSALARY;
   END

3. TABLE FILE EMPDATA
   HEADING
   "EMPLOYEE SALARIES"
   " "
   PRINT CSAL
   BY NEWID
4. WHERE CSAL GT 65000
5. MORE
   FILE SALHIST
6. WHERE OLDSALARY GT 65000
   END

1. Defines NEWID in the EMPDATA data source with the same name and format as the sort

field referenced in the main request.

2. Defines NEWID in the SALHIST data source with the same name and format as the sort

field referenced in the main request.

3. The main request. This contains all the formatting for the resulting report and names the

first file to be concatenated. It also contains all printing and sorting information. The fields
printed and the sort fields must exist as real or DEFINE fields in each file.

4. The WHERE criterion in the main request applies only to the EMPDATA data source.

5. The MORE phrase concatenates the SALHIST data source to the EMPDATA data source.

6. This WHERE criterion applies only to the SALHIST data source. Notice that it references a

field that is not defined in the EMPDATA data source.

The output is:

EMPLOYEE SALARIES

NEWID

000-00-0030

SALARY

 $70,000.00

Creating Reports With TIBCO® WebFOCUS Language

 1177






Merging Concatenated Data Sources

000-00-0070

000-00-0200

000-00-0230

000-00-0300

 $70,000.00

 $83,000.00

 $83,000.00

 $79,100.00

$115,000.00

$115,000.00

$102,500.00

 $89,500.00

 $80,500.00

 $80,500.00

 $75,000.00

 $70,800.00

 $79,000.00

 $79,000.00

 $75,000.00

 $70,000.00

When you concatenate data, record sets are simply appended, not grouped or aggregated
across files. Therefore, if duplicate sort fields exist, they show up twice in the report output.

Merging Concatenated Data Sources

You can use the MORE phrase in a MATCH request to merge up to 16 sets of concatenated
data sources.

You must meet all MATCH requirements in the main request. All data sources to be merged
must be sorted by at least one field with a common format.

The MATCH request results in a HOLD file containing the merged data. You can specify how
you want each successive file merged using an AFTER MATCH command. For example, you can
retain:

All records from both files (OLD-OR-NEW). This is the default.

Only records common to both files (OLD-AND-NEW).

Records from the first file with no match in the second file (OLD-NOT-NEW).

1178

15. Merging Data Sources

Records from the second file with no match in the first file (NEW-NOT-OLD).

All non-matching records from both files; that is, records that were in either one of the files
but not in both (OLD-NOR-NEW).

All records from the first file with all matching records from the second file (OLD).

All records from the second file with all matching records from the first file (NEW).

Syntax:

How to Merge Concatenated Data Sources

1. MATCH FILE file1main request
   MORE
2. FILE file2subrequest
   MORE
3. FILE file3subrequest
   RUN
4. FILE file4main request
5. [AFTER MATCH merge_phrase]
   MORE
6. FILE file5subrequest
   MORE
7. FILE file6subrequest
   RUN
8. FILE file7main request
9. [AFTER MATCH merge_phrase]
   MORE
10.FILE file8subrequest
   MORE
11.FILE file9subrequest
   END

1. Starts the first answer set in the MATCH. File1 is the first data source in the first answer

set.

2. Concatenates file2 to file1 in the first MATCH answer set.

3. Concatenates file3 to file1 and file2 in the first MATCH answer set.

4. Starts the second answer set in the MATCH. File4 is the first data source in the second

answer set.

5. All data concatenated in the first answer set is merged with the data concatenated in the
second answer set using the AFTER MATCH merge_phrase in the second answer set.

6. Concatenates file5 to file4 in the second MATCH answer set.

7. Concatenates file6 to file4 and file5 in the second MATCH answer set.

8. Starts the third answer set in the MATCH. File7 is the first data source in the third answer

set.

Creating Reports With TIBCO® WebFOCUS Language

 1179

Merging Concatenated Data Sources

9. All merged data from the first and second answer sets, now a HOLD file, is merged with the
data concatenated in the third answer set using the AFTER MATCH merge_phrase in the
third answer set. This final set of merged data is stored in a HOLD file.

10.Concatenates file8 to file7 in the third MATCH answer set.

11.Concatenates file9 to file7 and file8 in the third MATCH answer set.

Using Sort Fields in MATCH Requests

If the data sources in the MATCH share common high-order sort fields with identical names
and formats, the MATCH process merges records with matching sort field values from each of
the files. If the two data sources in the MATCH have the same sort field with different names,
you can change one of the names with an AS phrase.

If the files in the MATCH do not share a high-order sort field, the fields are not compared.
Instead, the fields from the first record in each data source are merged to create the first
record in the HOLD file, and so on for all remaining records.

1180

Example: Merging Concatenated Data Sources With Common High-Order Sort Fields

The following annotated sample stored procedure illustrates MATCH with MORE, using a
common sort field:

15. Merging Data Sources

1. DEFINE FILE EMPDATA
   CURR_SAL/D12.2M = CSAL;
   FIRST_NAME/A10 = FN;
   EID/A9 = PIN;
   END

   -*Start MATCH.

2. MATCH FILE EMPLOYEE
      SUM CURR_SAL AS 'CURRENT'
          FIRST_NAME AS 'FIRST'
      BY EID AS 'SSN'
   -*Concatenate file EMPDATA to EMPLOYEE to form first MATCH answer set.
3.    MORE
      FILE EMPDATA
      RUN
   -*Second MATCH answer set:

4. FILE TRAINING
      PRINT EXPENSES
5.    BY PIN AS 'SSN'
6.    AFTER MATCH HOLD OLD-OR-NEW
   END

   -*Print merged file:

7. TABLE FILE HOLD
      PRINT *
   END

1. Defines the EMPDATA fields needed for concatenating it to EMPLOYEE.

2. Starts the MATCH and the main request in the concatenation. The main request defines all
printing and sorting for the concatenated files. The sort field is called SSN in the resulting
file.

3. Concatenates file EMPDATA to EMPLOYEE. This concatenated file becomes the OLD file in

the MATCH.

4. Creates the NEW file in the MATCH.

5. Uses an AS phrase to change the name of the sort field in the NEW file to the same name

as the sort field in the OLD file.

6. Defines the merge procedure. All records from the NEW file, the OLD file, and both files are

included in the final HOLD file.

7. Prints the values from the merged file.

Creating Reports With TIBCO® WebFOCUS Language

 1181






Merging Concatenated Data Sources

The first page of output is:

SSN                CURRENT  FIRST        EXPENSES
---                -------  -----        --------
000000010       $55,500.00  DANIEL       2,300.00
000000020       $62,500.00  MICHAEL             .
000000030       $70,000.00  LOIS         2,600.00
000000030       $70,000.00  LOIS         2,300.00
000000040       $62,500.00  RUTH         3,400.00
000000050       $54,100.00  PETER        3,300.00
000000060       $55,500.00  DORINA              .
000000070       $83,000.00  EVELYN              .
000000080       $43,400.00  PAMELA       3,200.00
000000080       $43,400.00  PAMELA       3,350.00
000000090       $33,000.00  MARIANNE            .
000000100       $32,400.00  TIM          3,100.00
000000110       $19,300.00  ANTHONY      1,800.00
000000110       $19,300.00  ANTHONY      2,500.00
000000110       $19,300.00  ANTHONY      2,400.00
000000120       $49,500.00  KATE         2,200.00
000000130       $62,500.00  MARCUS              .

1182

Example: Merging Concatenated Data Sources Without a Common Sort Field

In this example, the merged data sources do not share a sort field:

15. Merging Data Sources

DEFINE FILE EMPDATA
CURR_SAL/D12.2M = CSAL;
FIRST_NAME/A10 = FN;
EID/A9 = PIN;
END

-*Start MATCH

MATCH FILE EMPLOYEE
SUM CURR_SAL AS 'CURRENT'
    FIRST_NAME AS 'FIRST'
BY EID AS 'SSN'

-*Concatenate EMPDATA to EMPLOYEE to form the first MATCH answer set

MORE
FILE EMPDATA
RUN

-*Second MATCH answer set:

FILE TRAINING
PRINT EXPENSES
BY PIN AS 'EID'
AFTER MATCH HOLD OLD-OR-NEW
END

-*Print merged file:

TABLE FILE HOLD
PRINT *
END

The AS phrase changes the answer set. Since the sort fields no longer have the same names,
the fields are merged with no regard to matching records.

Creating Reports With TIBCO® WebFOCUS Language

 1183









Cartesian Product

The first page of output is:

SSN                CURRENT  FIRST       EID         EXPENSES
---                -------  -----       ---         --------
000000010       $55,500.00  DANIEL      000000010   2,300.00
000000020       $62,500.00  MICHAEL     000000030   2,600.00
000000030       $70,000.00  LOIS        000000030   2,300.00
000000040       $62,500.00  RUTH        000000040   3,400.00
000000050       $54,100.00  PETER       000000050   3,300.00
000000060       $55,500.00  DORINA      000000080   3,200.00
000000070       $83,000.00  EVELYN      000000080   3,350.00
000000080       $43,400.00  PAMELA      000000100   3,100.00
000000090       $33,000.00  MARIANNE    000000110   1,800.00
000000100       $32,400.00  TIM         000000110   2,500.00
000000110       $19,300.00  ANTHONY     000000110   2,400.00
000000120       $49,500.00  KATE        000000120   2,200.00
000000130       $62,500.00  MARCUS      000000140   3,600.00
000000140       $62,500.00  VERONICA    000000150   3,400.00
000000150       $40,900.00  KARL        000000160   1,000.00
000000160       $62,500.00  ROSE        000000180   1,250.00
000000170       $30,800.00  WILLIAM     000000190   3,150.00

Cartesian Product

Cartesian product enables you to generate a report containing all combinations of non-related
records or data instances in a multi-path request. This means that if a parent segment has
three child instances on one path and two child instances on another path, when CARTESIAN
is ON a request that references the parent segment and both children generates 16 records.
When CARTESIAN is OFF, the same request generates only three records.

For related information about controlling how selection tests are applied to child segments on
independent paths, see Selecting Records for Your Report on page 217.

Syntax:

How to Enable/Disable Cartesian Product

SET CARTESIAN = {OFF|ON}

where:

OFF

Disables Cartesian product. OFF is the default setting.

ON

Enables Cartesian product and generates all possible combinations of non-related records.

SET CARTESIAN may also be issued within a request.

Reference: Usage Notes for Cartesian Product

Cartesian product is performed on the lowest segment common to all paths, whether or not
a field in that segment is referenced.

1184

15. Merging Data Sources

Short paths do not display in requests with Cartesian product.

The SET CARTESIAN parameter is disabled when ACROSS is specified, and a warning
message is issued.

The SUM display command and the TOT. prefix operator have no effect on Cartesian
product.

SUM, COMPUTE, and WITHIN in combination with the PRINT display command are
performed on the Cartesian product.

ON TABLE COLUMN-TOTAL is automatically generated on the Cartesian product.

NOSPLIT is disabled if specified in combination with the SET CARTESIAN parameter, and no
warning message is issued.

MATCH is not supported with the SET CARTESIAN parameter. A warning message is not
issued if MATCH is requested, and the request is processed as if CARTESIAN is set to OFF.

TABLEF is not supported with the SET CARTESIAN parameter.

Example:

Reporting With Cartesian Product

When CARTESIAN is set to ON, the following multi-path request produces a report containing
all possible combinations of models and standards for each car:

SET CARTESIAN=ON
TABLE FILE CAR
PRINT MODEL STANDARD
BY CAR
IF CAR EQ 'JAGUAR'
END

The output in an ASCII environment is:

CAR

MODEL

STANDARD

JAGUAR

V12XKE AUTO

4 WHEEL DISC BRAKES

V12XKE AUTO

V12XKE AUTO

V12XKE AUTO

V12XKE AUTO

XJ12L AUTO

XJ12L AUTO

POWER STEERING

RECLINING BUCKET SEATS

WHITEWALL RADIAL PLY TIRES

WRAP AROUND BUMPERS

4 WHEEL DISC BRAKES

POWER STEERING

Creating Reports With TIBCO® WebFOCUS Language

 1185

Cartesian Product

XJ12L AUTO

XJ12L AUTO

XJ12L AUTO

RECLINING BUCKET SEATS

WHITEWALL RADIAL PLY TIRES

WRAP AROUND BUMPERS

When CARTESIAN is set to OFF (the default), the same request results in a report from the CAR
data source containing a list of models and standards without logical relationships.

The output in an ASCII environment is:

CAR

MODEL

STANDARD

JAGUAR

V12XKE AUTO

4 WHEEL DISC BRAKES

XJ12L AUTO

POWER STEERING

.

.

.

RECLINING BUCKET SEATS

WHITEWALL RADIAL PLY TIRES

WRAP AROUND BUMPERS

1186

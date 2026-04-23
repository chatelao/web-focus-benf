Chapter8

Saving and Reusing Your Report Output

When you run a report request, by default the data values are collected and presented in
a viewable form, complete with column titles and formatting features. Instead of viewing
the data values, you can save them to a special data file to:

Display as a webpage, as a printed document, or in a text document.

Process in another application, such as a spreadsheet, a database, a word
processor, or a 3GL program.

Send to another location, such as a browser or PC.

Extract a subset of the original data source in order to generate multi-step reports.

Extract a data source to a structured extract file that retains information about the
segment relationships in order to facilitate migration of data sources and reports
between operating environments.

In this chapter:

Saving Your Report Output

Creating a PCHOLD File

Creating a HOLD File

Choosing Output File Formats

Holding Report Output in FOCUS Format

Controlling Attributes in HOLD Master
Files

Merging Data Into an Existing Data
Source With ON TABLE MERGE

Using Text Fields in Output Files

Keyed Retrieval From HOLD Files

Creating a Delimited Sequential File

Saving and Retrieving HOLD Files

Using DBMS Temporary Tables as HOLD
Files

Creating SAVE and SAVB Files

Saving Report Output in INTERNAL
Format

Creating A Subquery or Sequential File
With HOLD FORMAT SQL_SCRIPT

Creating a Structured HOLD File

Creating Reports With TIBCO® WebFOCUS Language

 471

Saving Your Report Output

Saving Your Report Output

The following commands extract and save report output in a variety of file formats:

HOLD. The HOLD command creates a data source containing the output of a report
request. By default, the data is stored in binary format, but you can specify a different
format, such as FOCUS, HTML, or Excel. For some formats, the HOLD command also
creates a corresponding Master File. You can then write other report requests that in turn
extract or save data from the HOLD file. See Creating a HOLD File on page 473.

SAVE and SAVB. The SAVE command is identical to a HOLD command, except that it does
not create a Master File, and ALPHA is the default format. If you wish to create a SAVE file
in BINARY format, use a variation of the SAVE command called SAVB.

As with a HOLD file, you can specify a variety of formats suitable for use with other
software products. See Creating SAVE and SAVB Files on page 506.

PCHOLD. The PCHOLD command creates a data source containing the output of a report
request, and downloads the HOLD data source and the optional Master File to a client
computer or browser. As with a HOLD file, you can specify a variety of file formats. See
Creating a PCHOLD File on page 509.

Tip: When saving or holding output files, it is recommended to have an Allocation in place for
the file. This is not applicable for PCHOLD files.

Naming and Storing Report Output Files

During a session, a report output file remains usable until it is erased or overwritten. A
subsequent output file created during the same session replaces the initial version, unless you
give it another name by using the AS phrase.

A FILEDEF command is automatically issued when you create an output file. The ddname used
to identify the file is the same as the name of the report output file (HOLD, SAVE, or SAVB, or
the name in the AS phrase), if not already allocated.

By default, report output files created with HOLD, SAVE, or SAVB are written to temporary
space. When the session ends, these files are no longer available unless you save the output
to a specific location.

To save report output files to a specific location, use an ALLOCATE or FILEDEF command. For
details, see Saving and Retrieving HOLD Files on page 498. You can dynamically allocate an
output file using the DYNAM ALLOCATE or TSO ALLOCATE command in z/OS.

For details, see the Developing Reporting Applications manual.

472

8. Saving and Reusing Your Report Output

When you create a HOLD file using the syntax ON TABLE HOLD AS name, the name can contain
up to the maximum number of characters supported by your operating system. For information,
see the section Naming a Master File in the Describing Data With WebFOCUS Language manual.

While a numeric name or a name beginning with a number is valid on many operating systems,
such names are discouraged because they:

Cause errors (FOC14069) when a request attempts to access data using a SUFFIX=EDA
synonym that points to a file starting with a number. (Note that a SUFFIX=EDA synonym is
created by the Adapter for Remote Servers.)

May cause problems when an external application (such as an API application) that does
not accept files starting with numbers interacts with a SUFFIX=EDA synonym that points to
a file starting with a number.

May be problematic to a third party application that does not work with numeric file names
or with file names that begin with numbers.

Creating a HOLD File

You can use the HOLD command to create report output files for a range of purposes:

As a tool for data extraction, the HOLD command enables you to retrieve and process data,
then extract the results for further processing. Your report request can create a new data
source, complete with a corresponding Master File, from which you can generate new
reports.

The output Master File contains only the fields in the report request. The fields in a HOLD
file have the original names specified in the Master File that are retrieved if the report is
displayed or printed. You can alter the field names in the output Master File using the AS
phrase in conjunction with the command SET ASNAMES. See Controlling Field Names in a
HOLD Master File on page 485.

The HOLD command enables you to specify the appropriate formats for displaying or
processing report output files in other software applications. See Choosing Output File
Formats on page 511.

When an application requires a data format that is not among the HOLD options, you can
use a subroutine to process each output record as it is written to the HOLD data source.

If your environment supports the SET parameter SAVEMATRIX, you can preserve the internal
matrix of your last report in order to keep it available for subsequent HOLD, SAVE, and SAVB
commands when the request is followed by Dialogue Manager commands. For details on
SAVEMATRIX, see the Developing Reporting Applications manual.

Creating Reports With TIBCO® WebFOCUS Language

 473

Creating a HOLD File

Syntax:

How to Create a HOLD File

From a report request, use

ON TABLE HOLD [AS filename] [FORMAT fmt] [DATASET dataset]
       [MISSING {ON|OFF}]
       [PERSISTENCE {STAGE|PERMANENT}]

or

hold_field HOLD [AS filename] [FORMAT fmt] [DATASET dataset]
       [MISSING {ON|OFF}]
       [PERSISTENCE {STAGE|PERMANENT}]

where:

HOLD

Extracts and saves report output. BINARY is the default format used when the HOLD
command is issued without an explicit format. The output is saved with an associated
Master File.

Note: Change the default output format to ALPHA by issuing the SET HOLDFORMAT
command.

hold_field

Is the name of the last display field in the request.

AS filename

Specifies a name for the HOLD file. If you do not specify a file name, HOLD becomes
the default. Since each subsequent HOLD command overwrites the previous HOLD
file, it is advisable to code a distinct file name in each request to direct the extracted
data to a separate file, thereby preventing it from being overwritten by the next HOLD
command.

The name can contain up to the maximum number of characters supported by your
operating system. For information, see the section Naming a Master File in the Describing
Data With WebFOCUS Language manual.

FORMAT fmt

Specifies the format of the HOLD output file. BINARY is the default format for reporting
servers.

To display as a webpage, choose: HTML, HTMTABLE, DHTML

To display as a printed document, choose: PDF, PS

To use in a text document, choose: ALPHA, DOC, WP

To use in a spreadsheet application, choose: DIF, EXCEL, EXL97, EXL2K [PIVOT],
LOTUS, SYLK

474

8. Saving and Reusing Your Report Output

To use in a database application, choose: COMMA, COM, COMT, DB2, DATREC, DFIX,
FOCUS, INGRES, REDBRICK, SQL, SQLDBC, SQLORA, SQLINF, SQLMSS, SQLSYB,
SQLODBC, TAB, TABT, XFOCUS

To use with a 3-GL program, choose: INTERNAL

To use for additional reporting, choose: ALPHA, BINARY, FOCUS

To use as a transaction file for modifying a data source, choose: ALPHA, BINARY

To use for interactive analysis without connection to a server, choose: AHTML, APDF,
FLEX

For details about all available formats, see Choosing Output File Formats on page 511.

dataset

Can be a fully-qualified data set or file name or an n-part name (app/.../filename.ext).

You can specify a data set or file to contain the report output within the request itself,
rather than relying on an external or default specification. This allows you to place a
permanent hold file in any folder, directory or data set that you can write to, whether or not
that location is included in your APP PATH. The accompanying HOLD Master File will have
the DATASET attribute pointing to the file that was generated.

The case in which the data set name is added in the Master File depends on the value of
the FILECASE parameter. By default, lowercase is used. The actual data set is created with
its name in the case that conforms to the standards of your operating environment.

Note:

On z/OS, the file cannot already exist or be allocated when the HOLD command is
issued. Therefore, If the file already exists you must free the allocation and then delete
the file before running the request.

You can use a USS naming convention for the DATASET attribute to store the file in the
USS environment (for text output types).

MISSING

Controls whether fields with the attribute MISSING=ON in the Master File are carried
over into the HOLD file. MISSING ON is the default attribute. If the HOLD command
specifies MISSING OFF, fields with the MISSING attribute are not carried over. For
related information, see Handling Records With Missing Field Values on page 1035.
Also see the Developing Reporting Applications manual for the SET HOLDMISS, SET
NULL, and SET HNODATA parameters, which control how missing values are
propagated to alphanumeric and comma-delimited files.

Creating Reports With TIBCO® WebFOCUS Language

 475

Creating a HOLD File

PERSISTENCE

Applies only to Relational HOLD files (FORMAT sqlengine). Specifies how to create
intermediate tables that will be used only during UPLOAD and EBL requests to accelerate
performance by keeping all processing on the DBMS server instead of downloading data
into a HOLD file. The actual type of the intermediate table will be determined at run time,
based on specific DBMS-supported features and the data-populating mechanisms being
used. Valid values are:

STAGE. Will create either a Volatile or GLOBAL TEMPORARY table, for a DBMS that
supports that functionality. For a DBMS that does not support that functionality, a
message will display and the table will not be created.

PERMANENT. Will create a regular SQL table with a uniquely-generated name that will
be used in the request and will be available for further use after the request ends, but
will be dropped at the end of the session. This is the default value for PERSISTENCE for
HOLD FORMAT sqlengine.

Syntax:

How to Set the Default HOLD Format

SET HOLDFORMAT = {BINARY|ALPHA}

or

ON TABLE SET HOLDFORMAT {BINARY|ALPHA}

where:

BINARY

Sets the default HOLD file format to BINARY.

ALPHA

Sets the default HOLD file format to ALPHA.

Example:

Extracting Data to a HOLD File

The following request extracts data from the EMPLOYEE data source and creates a HOLD file.

TABLE FILE EMPLOYEE
SUM CURR_SAL AND ED_HRS
BY DEPARTMENT
LIST CURR_SAL AND ED_HRS AND BANK_ACCT
BY DEPARTMENT
BY LAST_NAME BY FIRST_NAME
ON TABLE HOLD
END

The following message appears:

476

8. Saving and Reusing Your Report Output

NUMBER OF RECORDS IN TABLE=  12 LINES=     12

To display the report generated by this request issue a report request against the HOLD file.

Tip: If you wish to view the information in the HOLD Master File before reporting against it, you
can issue the query command ? HOLD.

Syntax:

How to Query a HOLD Master File

If the HOLD format option you select creates a Master File, you can issue the following
command to display the fields, aliases, and formats in the HOLD Master File:

? HOLD

This command shows field names up to 32 characters. If a field name exceeds 32 characters,
a caret (>) in the 32nd position indicates a longer field name.

If you have renamed the HOLD file using AS filename, use the following syntax:

? HOLD filename

Tip: You must issue the ? HOLD query in the same session in which the HOLD file is created.

Example:

Reporting Against a HOLD Master File

In the following HOLD file, the formats shown are the values of the FORMAT attribute. You can
see the values of the ACTUAL attribute by displaying the HOLD Master File using TED or any
text editor. USAGE and ACTUAL formats for text fields specify only the length of the first line of
each logical record in the HOLD file. The USAGE format is the same as the field format in the
original Master File. The ACTUAL format is rounded up to a full (internal) word boundary, as is
done for alphanumeric fields.

The following request contains the query command ? HOLD, which displays the fields, aliases,
and formats in the associated Master File and creates a HOLD file.

TABLE FILE EMPLOYEE
SUM CURR_SAL AND ED_HRS
BY DEPARTMENT
LIST CURR_SAL AND ED_HRS AND BANK_ACCT
BY DEPARTMENT
BY LAST_NAME BY FIRST_NAME
ON TABLE HOLD
END

? HOLD

Creating Reports With TIBCO® WebFOCUS Language

 477


Creating a HOLD File

The output is:

NUMBER OF RECORDS IN TABLE=     12     LINES=         12

DEFINITION OF HOLD FILE: HOLD

FIELDNAME

DEPARTMENT

CURR_SAL

ED_HRS

LAST_NAME

FIRST_NAME

LIST

CURR_SAL

ED_HRS

BANK_ACCT

ALIAS

FORMAT

E01

E02

E03

E04

E05

E06

E07

E08

E09

A10

D12.2M

F6.2

A15

A10

I5

D12.2M

F6.2

I9S

You can now issue the following report request against the HOLD file:

TABLE FILE HOLD
PRINT E07 AS 'SALARY OF,EMPLOYEE' AND LAST_NAME AND FIRST_NAME
BY HIGHEST E03 AS 'TOTAL,DEPT,ED_HRS'
BY E01
BY HIGHEST E08 AS 'EMPLOYEE,ED_HRS'
END

478

8. Saving and Reusing Your Report Output

The output is:

TOTAL

DEPT                EMPLOYEE        SALARY
OF
ED_HRS  DEPARTMENT  ED_HRS          EMPLOYEE   LAST_NAME
FIRST_NAME
------  ----------  --------        ---------  ---------
----------
231.00  MIS            75.00       $21,780.00  BLACKWOOD
ROSEMARIE
                       50.00       $18,480.00  JONES
DIANE
                       45.00       $27,062.00  CROSS
BARBARA
                       36.00       $13,200.00  SMITH
MARY
                       25.00        $9,000.00  GREENSPAN
MARY
                         .00       $18,480.00  MCCOY
JOHN
120.00  PRODUCTION     50.00       $16,100.00  MCKNIGHT
ROGER
                       30.00       $26,862.00  IRVING
JOAN
                       25.00       $11,000.00  STEVENS
ALFRED
                       10.00        $9,500.00  SMITH
RICHARD
                        5.00       $21,120.00  ROMANS
ANTHONY
                         .00       $29,700.00  BANNING          JOHN

Holding Report Output in FOCUS Format

Whether issued within a request or after the request has been executed, the HOLD command
can create a FOCUS data source and a corresponding Master File from the data extracted by
the report request. This feature enables you to create:

A FOCUS data source from any other supported data source type.

A subset of an existing FOCUS data source.

Tip: If you are working in an environment that supports SCAN, FSCAN, MODIFY, or Maintain,
and you create a HOLD file in FOCUS format, you can update, as well as report against, the
HOLD file. See your documentation on these facilities for details.

Note: Holding a file in FOCUS format may generate the (FOC441) warning: The file exists
already. Create will write over it. Issuing the SET WARNING=OFF command
suppresses this message.

Creating Reports With TIBCO® WebFOCUS Language

 479


Holding Report Output in FOCUS Format

Syntax:

How to Create HOLD Files in FOCUS Format

In a report request, use

ON TABLE HOLD [AS filename] FORMAT FOCUS [INDEX field1 field2 ...]

where:

AS filename

Specifies a name for the HOLD file. If you do not specify a file name, HOLD becomes
the default. Since each subsequent HOLD command overwrites the previous HOLD
file, it is advisable to provide a distinct file name in each request to direct the
extracted data to a separate file, thereby preventing it from being overwritten by the
next HOLD command.

The name can be up to 64 characters long.

Note: If you use a name longer than eight characters on z/OS, an eight-character member
name is generated as described in the Describing Data With WebFOCUS Language manual.
To relate the long name to the short member name, the $ VIRT attribute is generated on
the top line in the Master File. The resulting HOLD file is a temporary data file. To allocate
the long Master File name to a permanent data file, issue the DYNAM ALLOCATE command
with the LONGNAME option prior to the HOLD request. The ddname in the command must
refer to an existing member of the MASTER data set.

INDEX field1...

Enables you to index FOCUS fields. All fields specified after INDEX are specified as
FIELDTYPE=I in the Master File. Up to four fields can be indexed.

Note: Since the number of index field names is variable, a command name that follows the
HOLD command and starts with the same characters as a field name may be counted as
another index field, generating an error. For example, if the command following HOLD
starts with ON TABLE and a field name starts with the characters 'ON', the ON in the
command will be considered a truncated field name to add to the index. To avoid this
issue, either set the FIELDNAME parameter to NOTRUNC, so that command names will not
be confused with truncated field names, or move the HOLD command to the end of the
procedure right before the END command.

Note that once you use this format from Hot Screen, you cannot issue another HOLD
command while in the same Hot Screen session.

480

8. Saving and Reusing Your Report Output

Reference: Operating System Notes for HOLD Files in FOCUS Format

The HOLD file is dynamically allocated if it is not currently allocated in z/OS. This means the
system may delete the file at the end of the session, even if you have not done so. Since
HOLD files are usually deleted, this is the desired default. However, if you want to save the
Master File, allocate it to ddname HOLDMAST as a permanent data set. The allocation can be
performed in the standard FOCUS CLIST. For example:

ALLOC F(HOLDMAST)  DA('qualif.HOLDMAST') SHR REUSE

Note that ddname HOLDMAST must not refer to the same data set referred to by the MASTER
and FOCEXEC ddnames.

Reference: Controlling the FOCUS File Structure

The structure of the FOCUS data source varies according to the report request. The rules are
as follows:

Each aggregation command (SUM, COUNT, WRITE) creates a segment, with each new BY
field in the request becoming a key. In a request that uses multiple display commands, the
key to any newly created segment does not contain keys that are in the parent segment.

If a PRINT or LIST command is used to create a segment, all the BY fields, together with
the internal FOCLIST field, form the key.

All fields specified after INDEX are indexed; that is, FIELDTYPE=I is specified in the Master
File. Up to four fields may be indexed.

If the data in the HOLD file is longer than a page (4K for FOCUS data sources or 16K for
XFOCUS data sources), it cannot be stored in a single segment. Data that is too long to
become a single segment will become a parent segment with unique child segments. For a
FOCUS data source, the fields will be grouped into normal FOCUS page size segments and
added as unique segments up to the total maximum of 32K of data. For an XFOCUS data
source, the root segment can hold the first 16K of data, and additional data up to the 32K
total, will be placed in a single unique segment. BY fields must all occur in the portion of
the data assigned to the root segment.

To control whether the ACCEPT and TITLE attributes are propagated to the Master File
associated with the HOLD file, use the SET HOLDATTR command. To control the FIELDNAME
attribute in the Master File of the HOLD file, use the SET ASNAMES command. For more
information on how to control the TITLE, ACCEPT, and FIELDNAME attributes in a HOLD Master
File, see Controlling Attributes in HOLD Master Files on page 484.

Creating Reports With TIBCO® WebFOCUS Language

 481

Holding Report Output in FOCUS Format

Example:

Creating a HOLD File in FOCUS Format

The following example creates a subset of the CAR data source.

TABLE FILE CAR
SUM SALES BY COUNTRY BY CAR BY MODEL
ON TABLE HOLD AS X1 FORMAT FOCUS
END

This request creates a single-segment FOCUS data source with a SEGTYPE of S3 (because it
has three BY fields) named X1.

The X1 Master File is created by the request:

FILE=X1, SUFFIX=FOC
 SEGMENT=SEG01 ,SEGTYPE=S03
  FIELDNAME=COUNTRY      ,ALIAS=E01    ,USAGE=A10   ,$
  FIELDNAME=CAR          ,ALIAS=E02    ,USAGE=A16   ,$
  FIELDNAME=MODEL        ,ALIAS=E03    ,USAGE=A24   ,$
  FIELDNAME=SALES        ,ALIAS=E04    ,USAGE=I6    ,$

Example:

Using PRINT to Create a FOCUS Data Source With a FOCLIST Field

This example creates a single-segment FOCUS data source with a SEGTYPE of S4 because of
the three BY fields and the FOCLIST FIELD.

TABLE FILE CAR
PRINT SALES BY COUNTRY BY CAR BY MODEL
ON TABLE HOLD AS X2 FORMAT FOCUS INDEX MODEL
END

The Master File created by this request is:

FILE=X2, SUFFIX=FOC
 SEGMENT=SEG01, SEGTYPE=S04
  FIELDNAME=COUNTRY      ,ALIAS=E01    ,USAGE=A10   ,$
  FIELDNAME=CAR          ,ALIAS=E02    ,USAGE=A16   ,$
  FIELDNAME=MODEL        ,ALIAS=E03    ,USAGE=A24   ,FIELDTYPE=I,$
  FIELDNAME=FOCLIST      ,ALIAS=E04    ,USAGE=I5    ,$
  FIELDNAME=SALES        ,ALIAS=E05    ,USAGE=I6    ,$

482

8. Saving and Reusing Your Report Output

Example:

Creating a Two-Segment FOCUS Data Source

The following request contains two SUM commands. The first, SUM SALES BY COUNTRY,
creates a segment with COUNTRY as the key and the summed values of SALES as a data field.
The second, SUM SALES BY COUNTRY BY CAR BY MODEL, creates a descendant segment,
with CAR and MODEL as the keys and SALES as a non-key field.

The COUNTRY field does not form part of the key to the second segment. COUNTRY is a key in
the path to the second segment. Any repetition of this value is redundant.

TABLE FILE CAR
SUM SALES BY COUNTRY
SUM SALES BY COUNTRY BY CAR BY MODEL
ON TABLE HOLD AS X3 FORMAT FOCUS
END

This creates a two-segment FOCUS data source:

The Master File for this newly-created FOCUS data source is:

FILE=X3, SUFFIX=FOC
 SEGMENT=SEG01, SEGTYPE=S01
  FIELDNAME=COUNTRY       ,ALIAS=E01    ,USAGE=A10    ,$
  FIELDNAME=SALES         ,ALIAS=E02    ,USAGE=I6     ,$
 SEGMENT=SEG02, SEGTYPE=S02,PARENT=SEG01
  FIELDNAME=CAR           ,ALIAS=E03    ,USAGE=A16    ,$
  FIELDNAME=MODEL         ,ALIAS=E04    ,USAGE=A24    ,$
  FIELDNAME=SALES         ,ALIAS=E05    ,USAGE=I6     ,$

Creating Reports With TIBCO® WebFOCUS Language

 483

Controlling Attributes in HOLD Master Files

Example:

Creating a Three-Segment FOCUS Data Source

In this example, each display command creates one segment.

The key to the root segment is the BY field, COUNTRY, while the keys to the descendant
segments are the new BY fields. The last segment uses the internal FOCLIST field as part of
the key, since the display command is PRINT.

TABLE FILE CAR
SUM SALES BY COUNTRY BY CAR
SUM SALES BY COUNTRY BY CAR BY MODEL
PRINT SALES BY COUNTRY BY CAR BY MODEL BY BODY
ON TABLE HOLD AS X4 FORMAT FOCUS INDEX COUNTRY MODEL
END

The Master File is:

FILE=X4, SUFFIX=FOC
 SEGMENT=SEG01, SEGTYPE =S02
  FIELDNAME=COUNTRY   ,ALIAS=E01     ,USAGE=A10   ,FIELDTYPE=I,$
  FIELDNAME=CAR       ,ALIAS=E02     ,USAGE=A16   ,$
  FIELDNAME=SALES     ,ALIAS=E03     ,USAGE=I6    ,$
 SEGMENT=SEG02, SEGTYPE =S01 ,PARENT=SEG01
  FIELDNAME=MODEL     ,ALIAS=E04     ,USAGE=A24   ,FIELDTYPE=I,$
  FIELDNAME=SALES     ,ALIAS=E05     ,USAGE=I6    ,$
 SEGMENT=SEG03, SEGTYPE =S02 ,PARENT=SEG02
  FIELDNAME=BODYTYPE  ,ALIAS=E06     ,USAGE=A12   ,$
  FIELDNAME=FOCLIST   ,ALIAS=E07     ,USAGE=I5    ,$
  FIELDNAME=SALES     ,ALIAS=E08     ,USAGE=I6    ,$

Controlling Attributes in HOLD Master Files

The commands SET ASNAMES, SET HOLDLIST, and SET HOLDATTR enable you to control the
FIELDNAME, TITLE, and ACCEPT attributes in HOLD Master Files. These commands are issued
prior to the report request and remain in effect for the duration of the session, unless you
change them.

The SET ASNAMES command designates text specified in an AS phrase as the field name
in the HOLD Master File, and concatenates it to the beginning of the first field name
specified in an ACROSS phrase. See Controlling Field Names in a HOLD Master File on page
485.

The SET HOLDLIST command restricts fields in HOLD and PCHOLD files to those appearing
in a request. That is, non-displaying fields in a request (those designated as NOPRINT
fields) are not included in the HOLD file. You can also distinguish between implicitly and
explicitly non-displaying fields. See Controlling Fields in a HOLD Master File on page 490.

484

8. Saving and Reusing Your Report Output

The SET HOLDATTR command propagates TITLE and ACCEPT attributes used in the original
Master File to the HOLD Master File. See Controlling Attributes in the HOLD Master File on
page 495.

In addition, the SET HOLDSTAT command enables you to include comments and DBA
information in the HOLD Master File. For more information about SET HOLDSTAT, see the
Describing Data With WebFOCUS Language manual. For details about SET commands, see the
Developing Reporting Applications manual.

Controlling Field Names in a HOLD Master File

When SET ASNAMES is set to ON, MIXED or FOCUS, the literal specified in an AS phrase in a
report request is used as the field name in a HOLD Master File. This command also controls
how ACROSS fields are named in HOLD files.

Syntax:

How to Control Field Names in a HOLD Master File

SET ASNAMES = [ON|OFF|MIXED|FOCUS|FLIP]

where:

OFF

Does not use the literal specified in an AS phrase as a field name in HOLD files, and
does not affect the way ACROSS fields are named.

ON

Uppercases the literal specified in an AS phrase and propagates it as the field name
in the HOLD Master File. Creates names for ACROSS fields that consist of the AS
name value concatenated to the beginning of the ACROSS field value and controls the
way ACROSS fields are named in HOLD files of any format.

MIXED

Uses the literal specified in an AS phrase for the field name, retaining the case of the
AS name, and creates names for ACROSS fields that consist of the AS name value
concatenated to the beginning of the ACROSS field value.

FOCUS

Uses the literal specified in an AS phrase as the field name and controls the way
ACROSS fields are named only in HOLD files in FOCUS format. FOCUS is the default
value.

FLIP

Propagates the field names in the original Master File to the alias names in the HOLD
Master File and the alias names in the original Master File to the field names in the HOLD
Master File.

Creating Reports With TIBCO® WebFOCUS Language

 485

Controlling Attributes in HOLD Master Files

Reference: Usage Notes for Controlling Field Names in HOLD Files

If no AS phrase is specified for a field, the field name from the original Master File is used.
The TITLE attribute specified in the Master File is not used unless SET HOLDATTRS was
previously issued.

To ensure that fields referenced more than once in a request have unique names in the
HOLD Master File, use SET ASNAMES.

Special characters and blanks used in the AS phrase are preserved in the field name that
is created when SET ASNAMES is used. Use single quotation marks around the non-
standard field names when referring to them in the newly created Master File.

Text specified in an AS phrase that contains more than 66 characters is truncated to 66
characters in the Master File.

When generating field names and aliases for a HOLD file with the default setting for the
ASNAMES parameter, if the HOLD file is a relational data source, the field names and
aliases from the original Master File are propagated to the HOLD Master File. The alias
names become the column names in the generated relational table. The AS name also
becomes the TITLE attribute in the HOLD Master File.

When you set the ASNAMES parameter to FLIP, for relational HOLD files, the field names
from the original Master File or the AS names specified in the request become the alias
names in the HOLD Master File as well as the column names in the generated relational
table and the TITLE attributes in the HOLD Master File. The alias names in the original
Master File become the field names in the HOLD Master File, except when there is an AS
name, in which case the original field name becomes the HOLD field name.

If the HOLD file is not relational, field names from the original Master File are propagated to
the HOLD Master File, but alias name are not propagated, and default aliases of the form
E01, E02, and so on, are generated in the HOLD Master File.

For SET ASNAMES=FLIP, for non-relational HOLD files, the field names from the original
Master File or the AS names from the request become the alias names in the HOLD Master
File, and default field names are generated in the form F01, F02, and so on.

Duplicate field names may occur in the newly created Master File as a result of truncation
or the way AS phrases have been specified. In this case, refer to the fields by their aliases
(E01, E02, and so forth).

When commas are used as delimiters to break lines in the column heading, only the literal
up to the first comma is used as the field name in the Master File. For example, the
following produces the field name PLACE in the HOLD Master File:

486

8. Saving and Reusing Your Report Output

PRINT COUNTRY AS 'PLACE,OF,ORIGIN'

When ACROSS is used in a report request and the results are extracted to a HOLD file, the
columns generated by the ACROSS phrase all have the same field name in the HOLD
Master File. If SET ASNAMES is issued, each new column may have a unique field name.
This unique field name consists of the ASNAME value specified in the request's display
command, concatenated to the beginning of the value of the field used in the ACROSS
phrase. If several field names have the same letters, this approach does not work.

If an AS phrase is used for the fields in the ACROSS phrase, each new column has a field
name composed of the literal in the AS phrase concatenated to the beginning of the value
of the first field used in the ACROSS phrase.

Example:

Controlling Field Names in the HOLD Master File

In the following example, SET ASNAMES=ON causes the text in the AS phrase to be used as
field names in the HOLD1 Master File. The two fields in the HOLD1 Master File, NATION and
AUTOMOBILE, contain the data for COUNTRY and CAR.

SET ASNAMES=ON
TABLE FILE CAR
PRINT CAR AS 'AUTOMOBILE'
BY COUNTRY AS 'NATION'
ON TABLE HOLD AS HOLD1
END

The request produces the following Master File:

FILE=HOLD1, SUFFIX=FIX
 SEGMENT=HOLD1, SEGTYPE=S01,$
  FIELDNAME=NATION      ,ALIAS=E01   ,USAGE=A10  ,ACTUAL=A12     ,$
  FIELDNAME=AUTOMOBILE  ,ALIAS=E02   ,USAGE=A16  ,ACTUAL=A16     ,$

Example:

Providing Unique Field Names With SET ASNAMES

The following request generates a HOLD Master File with one unique field name for SALES and
one for AVE.SALES. Both SALES and AVE.SALES would be named SALES, if SET ASNAMES had
not been used.

SET ASNAMES=ON
TABLE FILE CAR
SUM SALES AND AVE.SALES AS 'AVERAGESALES'
BY CAR
ON TABLE HOLD AS HOLD2
END

Creating Reports With TIBCO® WebFOCUS Language

 487

Controlling Attributes in HOLD Master Files

The request produces the following Master File:

FILE=HOLD2, SUFFIX=FIX
 SEGMENT=HOLD2, SEGTYPE=S01,$
  FIELDNAME=CAR             ,ALIAS=E01  ,USAGE=A16 ,ACTUAL=A16   ,$
  FIELDNAME=SALES           ,ALIAS=E02  ,USAGE=I6  ,ACTUAL=I04   ,$
  FIELDNAME=AVERAGESALES    ,ALIAS=E03  ,USAGE=I6  ,ACTUAL=I04   ,$

Example:

Using SET ASNAMES With the ACROSS Phrase

The following request produces a HOLD Master File with the literal CASH concatenated to each
value of COUNTRY.

SET ASNAMES=ON
TABLE FILE CAR
SUM SALES AS 'CASH'
ACROSS COUNTRY
ON TABLE HOLD AS HOLD3
END

The request produces the following Master File:

FILE=HOLD3, SUFFIX=FIX
 SEGMENT=HOLD3, SEGTYPE=S01,$
  FIELDNAME=CASHENGLAND     ,ALIAS=E01   ,USAGE=I6  ,ACTUAL=I04  ,$
  FIELDNAME=CASHFRANCE      ,ALIAS=E02   ,USAGE=I6  ,ACTUAL=I04  ,$
  FIELDNAME=CASHITALY       ,ALIAS=E03   ,USAGE=I6  ,ACTUAL=I04  ,$
  FIELDNAME=CASHJAPAN       ,ALIAS=E04   ,USAGE=I6  ,ACTUAL=I04  ,$
  FIELDNAME=CASHW GERMANY   ,ALIAS=E05   ,USAGE=I6  ,ACTUAL=I04  ,$

Without the SET ASNAMES command, every field in the HOLD FILE is named COUNTRY.

To generate field names for ACROSS values that include only the field value, use the AS
phrase followed by two single quotation marks, as follows:

SET ASNAMES=ON
TABLE FILE CAR
SUM SALES AS ''
ACROSS COUNTRY
ON TABLE HOLD AS HOLD4
END

The resulting Master File looks like this:

FILE=HOLD4, SUFFIX=FIX
 SEGMENT=HOLD4, SEGTYPE=S0,$
  FIELDNAME=ENGLAND    ,ALIAS=E01   ,USAGE=I6  ,ACTUAL=I04    ,$
  FIELDNAME=FRANCE     ,ALIAS=E02   ,USAGE=I6  ,ACTUALI04     ,$
  FIELDNAME=ITALY      ,ALIAS=E03   ,USAGE=I6  ,ACTUALI04     ,$
  FIELDNAME=JAPAN      ,ALIAS=E04   ,USAGE=I6  ,ACTUALI04     ,$
  FIELDNAME=W GERMANY  ,ALIAS=E05   ,USAGE=I6  ,ACTUALI04     ,$

488

8. Saving and Reusing Your Report Output

Example:

Generating a HOLD File With SET ASNAMES=FLIP

The following request generates a HOLD file in ALPHA format using the OFF value for SET
ASNAMES. The field CURR_SAL has the AS name SALARY in the request:

SET ASNAMES=OFF
TABLE FILE EMPLOYEE
SUM CURR_SAL AS SALARY PCT_INC
BY DEPARTMENT
ON TABLE HOLD FORMAT ALPHA
END

In the HOLD Master File, AS names have not been propagated, the field names are from the
original Master File, and default alias names are generated:

FILENAME=HOLD    , SUFFIX=FIX     , IOTYPE=STREAM, $
  SEGMENT=HOLD, SEGTYPE=S1, $
    FIELDNAME=DEPARTMENT, ALIAS=E01, USAGE=A10, ACTUAL=A10, $
    FIELDNAME=CURR_SAL, ALIAS=E02, USAGE=D12.2M, ACTUAL=A12, $
    FIELDNAME=PCT_INC, ALIAS=E03, USAGE=F6.2, ACTUAL=A06, $

The following version of the request generates a relational table:

SET ASNAMES=OFF
TABLE FILE EMPLOYEE
SUM CURR_SAL AS SALARY PCT_INC
BY DEPARTMENT
ON TABLE HOLD FORMAT SQLMSS
END

The field names from the original Master File have been propagated to the field names in the
HOLD Maser File, and the alias names from the original Master File have been propagated to
the HOLD Master File. The AS name for CURR_SAL has become the TITLE in the HOLD Master
File:

FILENAME=HOLD   , SUFFIX=SQLMSS  , $
  SEGMENT=SEG01, SEGTYPE=S0, $
    FIELDNAME=DEPARTMENT, ALIAS=DPT, USAGE=A10, ACTUAL=A10, $
    FIELDNAME=CURR_SAL, ALIAS=CSAL, USAGE=D12.2M, ACTUAL=D8,
      TITLE='SALARY', $
    FIELDNAME=PCT_INC, ALIAS=PI, USAGE=F6.2, ACTUAL=F4, $

Changing SET ASNAMES to ON propagates the AS name SALARY to the field name in the HOLD
Master File. The following is the Master File for the HOLD file in ALPHA format:

FILENAME=HOLD    , SUFFIX=FIX     , IOTYPE=STREAM, $
  SEGMENT=HOLD, SEGTYPE=S1, $
    FIELDNAME=DEPARTMENT, ALIAS=E01, USAGE=A10, ACTUAL=A10, $
    FIELDNAME=SALARY, ALIAS=E02, USAGE=D12.2M, ACTUAL=A12, $
    FIELDNAME=PCT_INC, ALIAS=E03, USAGE=F6.2, ACTUAL=A06, $

Creating Reports With TIBCO® WebFOCUS Language

 489

Controlling Attributes in HOLD Master Files

The following is the Master File for the HOLD file in relational format:

FILENAME=HOLD   , SUFFIX=SQLMSS  , $
  SEGMENT=SEG01, SEGTYPE=S0, $
    FIELDNAME=DEPARTMENT, ALIAS=DPT, USAGE=A10, ACTUAL=A10, $
    FIELDNAME=SALARY, ALIAS=CURR_SAL, USAGE=D12.2M, ACTUAL=D8,
      TITLE='SALARY', $
    FIELDNAME=PCT_INC, ALIAS=PI, USAGE=F6.2, ACTUAL=F4, $

Changing SET ASNAMES to FLIP propagates the AS name SALARY to the alias name in the
HOLD Master File. In the ALPHA HOLD file, the other field names have been propagated to the
alias names in the HOLD Master File, and default field names have been generated:

FILENAME=HOLD    , SUFFIX=FIX     , IOTYPE=STREAM, $
  SEGMENT=HOLD, SEGTYPE=S1, $
    FIELDNAME=F01, ALIAS=DEPARTMENT, USAGE=A10, ACTUAL=A10, $
    FIELDNAME=F02, ALIAS=SALARY, USAGE=D12.2M, ACTUAL=A12, $
    FIELDNAME=F03, ALIAS=PCT_INC, USAGE=F6.2, ACTUAL=A06, $

In the relational HOLD file, changing SET ASNAMES to FLIP propagates the AS name SALARY
to the alias name in the HOLD Master File. For that field, the field name from the original
Master File becomes the field name in the HOLD Master File and the TITLE attribute. The other
field names have been propagated to the alias names in the HOLD Master File, and the
corresponding alias names from the original Master File have been propagated to the field
names in the HOLD Master File:

FILENAME=HOLD   , SUFFIX=SQLMSS  , $
  SEGMENT=SEG01, SEGTYPE=S0, $
    FIELDNAME=DPT, ALIAS=DEPARTMENT, USAGE=A10, ACTUAL=A10, $
    FIELDNAME=CURR_SAL, ALIAS=SALARY, USAGE=D12.2M, ACTUAL=D8,
      TITLE='SALARY', $
    FIELDNAME=PI, ALIAS=PCT_INC, USAGE=F6.2, ACTUAL=F4, $

Controlling Fields in a HOLD Master File

You can use the SET HOLDLIST command to restrict fields in HOLD Master Files to those
appearing in a request.

Syntax:

How to Control Fields in a HOLD File

SET HOLDLIST = {PRINTONLY|ALL|ALLKEYS|EXPLICIT}

where:

PRINTONLY

Specifies that only those fields that would appear in the report are included in the
generated HOLD file. Non-displaying fields in a request (those designated as NOPRINT
fields explicitly or implicitly) are not included in the HOLD file.

490

8. Saving and Reusing Your Report Output

ALL

Specifies that all display fields referenced in a request appear in a HOLD file,
including calculated values. ALL is the default value. OLD may be used as a synonym
for ALL.

Note: Vertical sort (BY) fields specified in the request with the NOPRINT option are not
included in the HOLD file even if HOLDLIST=ALL.

ALLKEYS

Propagates all fields, including NOPRINTed BY fields.

The ALLKEYS setting enables caching of all of the data necessary for manipulating an
active report.

EXPLICIT

Includes fields in the HOLD or PCHOLD file that are explicitly omitted from the report
output using the NOPRINT option in the request, but does not include fields that are
implicitly NOPRINTed. For example, if a field is reformatted in the request, two
versions of the field exist, the one with the new format and the one with the original
format, which is implicitly NOPRINTed

Note that SET HOLDLIST may also be issued from within a TABLE request. When used with
MATCH, SET HOLDLIST always behaves as if HOLDLIST is set to ALL.

Example:

Using HOLDLIST=ALL

When HOLDLIST is set to ALL, the following TABLE request produces a HOLD file containing all
specified fields, including NOPRINT fields and values calculated with the COMPUTE command.

SET HOLDLIST=ALL

TABLE FILE CAR
PRINT CAR MODEL NOPRINT
COMPUTE TEMPSEATS=SEATS+1;
BY COUNTRY
ON TABLE HOLD
END

? HOLD

The output is:

NUMBER OF RECORDS IN TABLE=     18

LINE=           18

DEFINITION OF HOLD FILE: HOLD

FIELDNAME

ALIAS

FORMAT

Creating Reports With TIBCO® WebFOCUS Language

 491




Controlling Attributes in HOLD Master Files

COUNTRY

CAR

MODEL

SEATS

TEMPSEATS

E01

E02

E03

E04

E05

A10

A16

A24

I3

D12.2

Example:

Using HOLDLIST= PRINTONLY

When HOLDLIST is set to PRINTONLY, the following TABLE request produces a HOLD file
containing only fields that would appear in report output:

SET HOLDLIST=PRINTONLY

TABLE FILE CAR
PRINT CAR MODEL NOPRINT
COMPUTE TEMPSEATS=SEATS+1;
BY COUNTRY
ON TABLE HOLD
END

? HOLD

The output is:

NUMBER OF RECORDS IN TABLE=    18

LINES=

18

DEFINITION OF HOLD FILE: HOLD

FIELDNAME

COUNTRY

CAR

TEMPSEATS

ALIAS

FORMAT

E01

E02

E03

A10

A16

D12.2

492




8. Saving and Reusing Your Report Output

Example:

Comparing Master Files Created Using Different HOLDLIST Settings

The following request against the GGSALES data source has two reformatted display fields
(DOLLARS, UNITS). The DOLLARS field is also an explicit NOPRINT field. The BY field named
CATEGORY is also an explicit NOPRINT field:

SET HOLDLIST=ALL
TABLE FILE GGSALES
SUM UNITS/I5 DOLLARS/D12.2 NOPRINT
BY REGION BY CATEGORY NOPRINT
ON TABLE HOLD FORMAT FOCUS
END

Running the request with SET HOLDLIST=ALL generates the following HOLD Master File. Note
that the DOLLARS and UNITS fields are included twice, once with the original format (which
would have been implicitly NOPRINTed if the report had been printed rather than held) and
once with the new format. However the NOPRINTed BY field (CATEGORY) is not included:

FILENAME=HOLD, SUFFIX=FOC     , $
  SEGMENT=SEG01, SEGTYPE=S1, $
    FIELDNAME=REGION, ALIAS=E01, USAGE=A11,
      TITLE='Region', DESCRIPTION='Region code', $
    FIELDNAME=UNITS, ALIAS=E02, USAGE=I08,
      TITLE='Unit Sales', DESCRIPTION='Number of units sold', $
    FIELDNAME=UNITS, ALIAS=E03, USAGE=I5,
      TITLE='Unit Sales', $
    FIELDNAME=DOLLARS, ALIAS=E04, USAGE=I08,
      TITLE='Dollar Sales', DESCRIPTION='Total dollar amount of reported
sales', $
    FIELDNAME=DOLLARS, ALIAS=E05, USAGE=D12.2,
      TITLE='Dollar Sales', $

Creating Reports With TIBCO® WebFOCUS Language

 493

Controlling Attributes in HOLD Master Files

Running the request with SET HOLDLIST=ALLKEYS generates the following HOLD Master File.
Note that the DOLLARS and UNITS fields are included twice, once with the original format,
which would have been implicitly NOPRINTed if the report had been printed rather than held,
and once with the new format. The NOPRINTed BY field (CATEGORY) is included:

FILENAME=HOLD, SUFFIX=FOC     , $
  SEGMENT=SEG01, SEGTYPE=S2, $
    FIELDNAME=REGION, ALIAS=E01, USAGE=A11,
      TITLE='Region', DESCRIPTION='Region code', $
    FIELDNAME=CATEGORY, ALIAS=E02, USAGE=A11,
      TITLE='Category', DESCRIPTION='Product category', $
    FIELDNAME=UNITS, ALIAS=E03, USAGE=I08,
      TITLE='Unit Sales', DESCRIPTION='Number of units sold', $
    FIELDNAME=UNITS, ALIAS=E04, USAGE=I5,
      TITLE='Unit Sales', $
    FIELDNAME=DOLLARS, ALIAS=E05, USAGE=I08,
      TITLE='Dollar Sales', DESCRIPTION='Total dollar amount of reported
sales', $
    FIELDNAME=DOLLARS, ALIAS=E06, USAGE=D12.2,
      TITLE='Dollar Sales', $

Running the request with SET HOLDLIST=PRINTONLY generates the following HOLD Master
File. Only the fields that would have actually printed on the report output are included: REGION
and UNITS with the new format (I5). All explicitly and implicitly NOPRINTed fields are excluded,
including the NOPRINTed BY field (CATEGORY):

FILENAME=HOLD , SUFFIX=FOC     , $
  SEGMENT=SEG01, SEGTYPE=S1, $
    FIELDNAME=REGION, ALIAS=E01, USAGE=A11,
      TITLE='Region', DESCRIPTION='Region code', $
    FIELDNAME=UNITS, ALIAS=E02, USAGE=I5,
      TITLE='Unit Sales', $

Running the request with SET HOLDLIST=EXPLICIT generates the following HOLD Master File.
The fields that would have actually printed on the report output are included and so are the
explicitly NOPRINTed fields (the display field DOLLARS and the BY field CATEGORY). The
implicitly NOPRINTed fields (DOLLARS and UNITS with their original formats) are omitted:

FILENAME=HOLD, SUFFIX=FOC     , $
  SEGMENT=SEG01, SEGTYPE=S2, $
    FIELDNAME=REGION, ALIAS=E01, USAGE=A11,
      TITLE='Region', DESCRIPTION='Region code', $
    FIELDNAME=CATEGORY, ALIAS=E02, USAGE=A11,
      TITLE='Category', DESCRIPTION='Product category', $
    FIELDNAME=UNITS, ALIAS=E03, USAGE=I5,
      TITLE='Unit Sales', $
    FIELDNAME=DOLLARS, ALIAS=E04, USAGE=D12.2,
      TITLE='Dollar Sales', $

494

8. Saving and Reusing Your Report Output

Controlling Attributes in the HOLD Master File

The SET HOLDATTR command controls whether the TITLE and ACCEPT attributes, as well as
other attributes in the original Master File, are propagated to the HOLD Master File. SET
HOLDATTR does not affect the way fields are named in the HOLD Master File.

Note that if a field in a data source does not have the TITLE attribute specified in the Master
File, but there is an AS phrase specified for the field in a report request, the corresponding
field in the HOLD file is named according to the AS phrase.

Syntax:

How to Control TITLE and ACCEPT Attributes

SET HOLDATTR =[ON|OFF|FOCUS|CUBE]

where:

ON

Uses the TITLE attribute as specified in the original Master File in HOLD files in any
format. The ACCEPT attribute is propagated to the HOLD Master File only for HOLD
files in FOCUS format. PROPERTY attributes are also propagated.

OFF

Does not use the TITLE or ACCEPT attributes from the original Master File in the HOLD
Master File.

FOCUS

Uses the TITLE and ACCEPT attributes only for HOLD files in FOCUS format. PROPERTY
attributes are also propagated. FOCUS is the default value.

CUBE

Propagates folders and DV_ROLE attributes, as well as TITLE attributes to the HOLD
Master File. It also propagates the field name as the alias value.

Example:

Controlling TITLE and ACCEPT Attributes in a HOLD Master File

In this example, the Master File for the CAR data source specifies TITLE and ACCEPT
attributes:

FILENAME=CAR2, SUFFIX=FOC
SEGNAME=ORIGIN, SEGTYPE=S1
  FIELDNAME =COUNTRY, COUNTRY, A10, TITLE='COUNTRY OF ORIGIN',
             ACCEPT='CANADA' OR 'ENGLAND' OR 'FRANCE' OR 'ITALY' OR
                    'JAPAN' OR 'W GERMANY',
             FIELDTYPE=I,$
SEGNAME=COMP, SEGTYPE=S1, PARENT=ORIGIN
  FIELDNAME=CAR, CARS, A16, TITLE='NAME OF CAR',$
.
.
.

Creating Reports With TIBCO® WebFOCUS Language

 495

Keyed Retrieval From HOLD Files

Using SET HOLDATTR=FOCUS, the following request

SET HOLDATTR = FOCUS
TABLE FILE CAR2
PRINT CAR
BY COUNTRY ON TABLE HOLD FORMAT FOCUS AS HOLD5
END

produces this HOLD Master File:

FILE=HOLD5, SUFFIX=FOC
 SEGMENT=SEG01, SEGTYPE=S02
  FIELDNAME=COUNTRY ,USAGE=E01   ,ACTUAL=A10
      TITLE='COUNTRY OF ORIGIN',
      ACCEPT=CANADA ENGLAND FRANCE ITALY JAPAN 'W GERMANY',$
  FIELDNAME=FOCLIST ,USAGE=E02   ,ACTUAL=I5     ,$
  FIELDNAME=CAR     ,USAGE=E03   ,ACTUAL=A16    ,
      TITLE='NAME OF CAR' ,$

Keyed Retrieval From HOLD Files

Keyed retrieval is supported with any single-segment SUFFIX=FIX data source or HOLD file that
is sorted based on the key. Keyed retrieval can reduce the IOs incurred in reading extract files,
by using the SEGTYPE parameter in the Master File to identify which fields comprise the logical
key for sequential files. When FIXRETRIEVE is:

ON, the retrieval process stops when an equality or range test on the key holds true.

OFF, all of the records from the sequential file are read and screening conditions are
applied when creating the final report.

The ON TABLE HOLD command enables you to read one of the many supported data sources
and create extract files. You can then join these fixed-format sequential files to other data
sources to narrow your view of the data. The concept of a logical key in a fixed-format file
enables qualified keyed searches for all records that match IF/WHERE tests for the first n KEY
fields identified by the SEGTYPE attribute. Retrieval stops when the screening test detects
values greater than those specified in the IF/WHERE test.

When a Master File is created for the extract file, a SEGTYPE of either Sn or SHn is added,
based on the BY fields in the request. For example, PRINT field BY field creates a HOLD Master
File with SEGTYPE=S1. Using BY HIGHEST field creates a Master with SEGTYPE=SH1.

496

8. Saving and Reusing Your Report Output

Syntax:

How to Control Keyed Retrieval for a HOLD File

SET FIXRET[RIEVE] = {ON|OFF}

where:

ON

OFF

Enables keyed retrieval. ON is the default setting.

Disables keyed retrieval.

Example: Master File for Keyed Retrieval From a HOLD File

The following Master File describes a fixed-format sequential file with sorted values of
SEQ_NO, in ascending order from 1 to 100,000.

FILE=SORTED,SUFFIX=FIX,$
SEGNAME=ONE,SEGTYPE=S1,$
 FIELD=MYKEY,MK,I8,I8,$
 FIELD=MFIELD,MF,A10,A10,$

TABLE FILE SORTED
 PRINT MFIELD
 WHERE MYKEY EQ 100
END

In this instance, with FIXRETRIEVE=ON, retrieval stops when MYKEY reaches 101, vastly
reducing the potential number of IOs, as only 101 records are read out of a possible 100,000.

Example:

Selection Criteria for Keyed Retrieval From an Extract File

Selection criteria that include lists of equality values use keyed retrieval. For example,

{IF|WHERE} MYKEY EQ x OR y OR z

IF and WHERE tests can also include range tests. For example,

{IF|WHERE} MYKEY IS-FROM x TO y

The maximum number of vertical (BY) sort fields remains 32.

Creating Reports With TIBCO® WebFOCUS Language

 497


Saving and Retrieving HOLD Files

In using this feature, keep in mind that when adding unsorted records to a sorted HOLD file,
records that are out of sequence are not retrieved. For example, suppose that a sorted file
contains the following three records:

Key

1 1200

2 2340

3 4875

and you add the following record at the bottom of the file:

1 1620

With FIXRETRIEVE=ON, the new record with a key value of 1 is omitted, as retrieval stops as
soon as a key value of 2 is encountered.

Saving and Retrieving HOLD Files

In WebFOCUS, HOLD files are saved to a temporary directory during processing and deleted
after the connection to the server is broken. If you wish to retain these files for later use, you
can save the HOLD data source and its associated Master File to a specific location using APP
commands.

To report against the HOLD Master File at a later time, you can add the application to your APP
path, if it is not already there, or you can use a two-part name (appname/mastername) in the
TABLE FILE command.

To report against the saved HOLD data file, you can issue a FILEDEF command that specifies
where to find the file before you issue the TABLE FILE command.

Syntax:

How to Specify a Storage Location for a HOLD Master File (Windows, UNIX, OpenVMS)

APP MAP appname path_to_directory APP HOLDDATA appname APP HOLDMETA
appname

where:

APP MAP

Associates a directory location with an application name.

APP HOLDDATA

Specifies the application name for HOLD data files.

APP HOLDMETA

Specifies the application name for HOLD Master Files.

498

8. Saving and Reusing Your Report Output

path_to_directory

Specifies the directory in which to store the files.

appname

Is an application name.

You should add the APP commands to a supported profile so that they will be available to all of
your procedures rather than issuing them in every procedure that needs to access the
application directory. In addition, you should add the application to your path so that it will be
found by your procedures.

Example:

Specifying a Storage Location for HOLD Data and Master Files

The following example for WebFOCUS on UNIX illustrates how to create an application named
holdapp and store HOLD data files and Master Files in the \ggtmp directory that is mapped to
that application.

Place the following commands in any supported profile:

APP MAP holdapp /ggtmp
APP HOLDDATA holdapp
APP HOLDMETA holdapp

The following request creates a HOLD Master file named sales.mas and a HOLD data file
named sales.ftm that will be stored in the /ggtmp directory:

TABLE FILE GGSALES
PRINT SEQ_NO CATEGORY PRODUCT
ON TABLE HOLD AS SALES
END

To issue a TABLE request against the HOLD file, you must first issue a FILEDEF command that
points to the HOLD data file. The DDNAME for the FILEDEF is the AS name specified in the
HOLD command. If no AS name was specified, the DDNAME is HOLD:

FILEDEF SALES DIR \ggtmp\sales.ftm

You must also make sure that WebFOCUS can find the Master File. One way to do this is to
make sure that the application is in your application path. You can add it to the path with the
following command:

APP APPENDPATH holdapp

Then you can issue a request against the HOLD file:

TABLE FILE SALES
PRINT *
END

Creating Reports With TIBCO® WebFOCUS Language

 499

Using DBMS Temporary Tables as HOLD Files

Alternatively, you can issue the TABLE request against the HOLD file using a two-part name
(application name and Master File name):

TABLE FILE holdapp/sales
PRINT *
END

Reference: Allocating HOLD Files on z/OS

The HOLD file is dynamically allocated if it is not currently allocated on z/OS. This means the
system may delete the file at the end of the session, even if you have not. Since HOLD files
are usually deleted, this is a desired default. However, if you want to save the file, we
recommend that you allocate the HOLD Master File to the ddname HOLDMAST as a permanent
data set, and allocate the HOLD data file to a permanent data set as well. The allocations can
be performed within the standard Reporting Server CLIST or batch JCL or in a profile or
procedure. For example, if your procedure had the following command:

ON TABLE HOLD AS SALES

you could use allocations similar to the following:

ALLOC F(HOLDMAST)  DA('qualif.HOLDMAST.DATA') SHR REUSE
ALLOC F(SALES)  DA('qualif.SALES.DATA') SHR REUSE

Note that ddname HOLDMAST must not refer to the same PDS referred to by the MASTER and
FOCEXEC ddnames.

Using DBMS Temporary Tables as HOLD Files

You can create a report output file (that is, a HOLD file), as a native DBMS temporary table.
This increases performance by keeping the entire reporting operation on the DBMS server,
instead of downloading data to your computer and then back to the DBMS server.

For example, if you temporarily store report output for immediate use by another procedure,
storing it as a temporary table instead of creating a standard HOLD file avoids the overhead of
transmitting the interim data to your computer.

The temporary table columns are created from the following report elements

Display columns

Sort (BY) columns

COMPUTE columns

except for those for which NOPRINT is specified.

500

8. Saving and Reusing Your Report Output

The temporary table that you create from your report will be the same data source type (that is,
the same DBMS) as the data source from which you reported. If the data source from which
you reported contains multiple tables, all must be of the same data source type and reside on
the same instance of the DBMS server.

You can choose between several types of table persistence.

You can create extract files as native DBMS tables with the following adapters:

Db2 (on z/OS, UNIX, and Windows)

Informix

Microsoft SQL Server

MySQL

Oracle

Teradata

Syntax:

How to Save Report Output as a Native Temporary Table Using Commands

The syntax to save report output as a native DBMS temporary table is

ON TABLE HOLD [AS filename] FORMAT SAME_DB [PERSISTENCE persistValue]

where:

filename

Specifies the name of the HOLD file. If you omit AS filename, the name of the
temporary table defaults to "HOLD".

Because each subsequent HOLD command overwrites the previous HOLD file, it is
recommended to specify a name in each request to direct the extracted data to a separate
file, thereby preventing an earlier file from being overwritten by a later one.

PERSISTENCE

Specifies the type of table persistence and related table properties. This is optional
for DBMSs that support volatile tables, and required otherwise. For information about
support for volatile tables for a particular DBMS, see Temporary Table Properties for
SAME_DB Persistence Values on page 503, and consult your DBMS vendor
documentation.

Creating Reports With TIBCO® WebFOCUS Language

 501

Using DBMS Temporary Tables as HOLD Files

persistValue

Is one of the following:

VOLATILE

Specifies that the table is local to the DBMS session. A temporary synonym (a
Master File and Access File), is generated automatically. It expires when the
server session ends.

This is the default persistence setting for all DBMSs that support volatile tables.

For information about support for the volatile setting, and about persistence and other
table properties, for a particular DBMS, see Temporary Table Properties for SAME_DB
Persistence Values on page 503, and consult your DBMS vendor documentation.

GLOBAL_TEMPORARY

Specifies that while the table exists, its definition will be visible to other database
sessions and users though its data will not be. A permanent synonym (a Master
File and Access File), is generated automatically.

For information about support for the global temporary setting, and about persistence
and other table properties, for a particular DBMS, see Temporary Table Properties for
SAME_DB Persistence Values on page 503, and consult your DBMS vendor
documentation.

PERMANENT

Specifies that a regular permanent table will be created. A permanent synonym (a
Master File and Access File), is generated automatically.

502

8. Saving and Reusing Your Report Output

Reference: Temporary Table Properties for SAME_DB Persistence Values

The following chart provides additional detail about persistence and other properties of
temporary tables of different data source types that are supported for use with HOLD format
SAME_DB.

DBMS

VOLATILE

GLOBAL_TEMPORARY

Db2

Db2 on Linux, UNIX, and
Windows, and Db2 for z/OS: a
volatile table is created using
the DECLARE GLOBAL
TEMPORARY TABLE command
with the ON COMMIT
PRESERVE ROWS option.
Declared global temporary
tables persist and are visible
only within the current
session (connection).
SESSION is the schema name
for all declared global
temporary tables.

Db2 on Linux, UNIX, and Windows, and Db2
for z/OS: a global temporary table is
created using the CREATE GLOBAL
TEMPORARY TABLE command. The
definition of a created global temporary
table is visible to other sessions, but the
data is not. The data is deleted at the end
of each transaction (COMMIT or ROLLBACK
command). The table definition persists
after the session ends.

Global tables require the following setting
to be in effect:

ENGINE DB2 SET AUTOCOMMIT ON FIN

For information on creating user-defined
tablespaces on Linux, UNIX, and Windows
for volatile and global temporary tables,
see the Adapter Administration manual.

This type of table is not supported by
Informix.

Informix

A volatile table is created
using the CREATE TEMP
TABLE command with the
WITH NO LOG option. The
definition and the data
persist, and are visible, only
within the current session.

Creating Reports With TIBCO® WebFOCUS Language

 503

Using DBMS Temporary Tables as HOLD Files

DBMS

VOLATILE

GLOBAL_TEMPORARY

The name of a global temporary table is
prefixed with two number signs (##).
Therefore, the name of a global temporary
table used as a HOLD file is the name
specified by the HOLD phrase, prefixed with
two number signs (##). The table is
dropped automatically when the session
that created the table ends and all other
tasks have stopped referencing it. The
table definition and data are visible to other
sessions.

This type of table is not supported by
MySQL.

Microsoft
SQL Server

MySQL

A volatile table is created as a
local temporary table whose
name is prefixed with a single
number sign (#). Therefore,
the name of a volatile table
used as a HOLD file is the
name specified by the HOLD
phrase, prefixed with a
number sign (#). The table
definition and the data
persist, and are visible, only
within the current session.

A volatile table is created
using the CREATE
TEMPORARY TABLE
command. A temporary table
persists and is visible only
within the current session
(connection). If a temporary
table has the same name as
a permanent table, the
permanent table becomes
invisible.

Oracle

This type of table is not
supported by Oracle.

The table definition is visible to all
sessions. Its data is visible only to the
session that inserts data into it. The table
definition persists for the same period as
the definition of a regular table.

504

8. Saving and Reusing Your Report Output

DBMS

VOLATILE

GLOBAL_TEMPORARY

Teradata

A volatile table definition and
data are visible only within the
session that created the table
and inserted the data. The
volatile table is created with
the ON COMMIT PRESERVE
ROWS option.

A global temporary table persists for the
same duration as a permanent table. The
definition is visible to all sessions, but the
data is visible only to the session that
inserted the data. The global temporary
table is created with the ON COMMIT
PRESERVE ROWS option.

Column Names in the HOLD File

Each HOLD file column is assigned its name:

1. From the AS name specified for the column in the report request.

2. If there is no AS name specified, the name is assigned from the alias specified in the
synonym. (The alias is identical to the column name in the original relational table.)

3. In all other cases, the name is assigned from the field name as it is specified in the

synonym.

Primary Keys and Indexes in the HOLD File

A primary key or an index is created for the HOLD table. The key or index definition is
generated from the sort (BY) keys of the TABLE command, except for undisplayed sort keys
(that is, sort keys for which NOPRINT is specified). To determine whether a primary key or an
index will be created:

1. If these sort keys provide uniqueness and do not allow nulls (that is, if in the synonym, the
MISSING attribute column is unselected or OFF), and if the DBMS supports primary keys on
the type of table being created, a primary key is created.

2. If these sort keys provide uniqueness but either

a. some of the columns allow nulls.

b.

the DBMS does not support primary keys on the type of table being created then a
unique index is created.

3. If these sort keys do not provide uniqueness, a non-unique index is created.

4. If there are no displayed sort keys (that is, no sort keys for which NOPRINT has not been

specified), no primary key or index is created.

Creating Reports With TIBCO® WebFOCUS Language

 505

Creating SAVE and SAVB Files

Creating SAVE and SAVB Files

The SAVE command, by default, captures report output in ALPHA format as a simple sequential
data source, without headings or subtotals. However, you can specify a variety of other formats
for SAVE files, which are compatible with many software products. For example, you can
specify SAVE formats to display report output in a webpage, a text document, a spreadsheet or
word processing application, or to be used as input to other programming languages. For a list
of supported formats, see Choosing Output File Formats on page 511.

Regardless of format, the SAVE command does not create a Master File.

The SAVB command is a variation on the SAVE command. SAVB creates a data source without
a Master File, but numeric fields are stored in BINARY format. You can use the SAVB file as
input to a variety of applications. SAVB output is the same as the default output created by the
HOLD command.

Syntax:

How to Create a SAVE File

From a report request, use

ON TABLE SAVE [AS filename] [FORMAT fmt] [MISSING {ON|OFF}]

or

save_field SAVE [AS filename] [FORMAT fmt] [MISSING {ON|OFF}]

where:

save_field

Is the name of the last field in the request, excluding BY or ACROSS fields.

AS filename

Specifies a name for the SAVE file. If you do not specify a file name, SAVE is used as
the default. Since each subsequent SAVE command overwrites the previous SAVE file,
it is advisable to code a distinct file name in each request to direct the extracted data
to a separate file, thereby preventing it from being overwritten by the next SAVE
command.

You can also include a path, enclosed in single quotation marks, indicating where to store
the SAVE file. For example:

ON TABLE SAVE FILENAME 'install_dir:\dir\filename.ext' FORMAT fmt

FORMAT fmt

Specifies the format of the SAVE file. ALPHA is the default format.

To display as or in a webpage:

HTML, HTMTABLE, DHTML

506

8. Saving and Reusing Your Report Output

To use in a text document:

ALPHA, DOC, PDF, WP,  Text

To use in a spreadsheet application:

DIF, EXCEL, EXL2K, LOTUS, (WK1), SYLK

To use in a database application:

COMMA, COM, COMT

For details about all available formats, see Choosing Output File Formats on page 511.

MISSING

Ensures that fields with the MISSING attribute set to ON are carried over into the
SAVE file. MISSING OFF is the default attribute. See Handling Records With Missing
Field Values on page 1035.

Example:

Creating a SAVE File

The following request extracts data from the EMPLOYEE data source and creates a SAVE file.

TABLE FILE EMPLOYEE
PRINT LAST_NAME AND FIRST_NAME
BY DEPARTMENT
ON TABLE SAVE
END

A description of the ALPHA (default SAVE format) file layout appears after the records are
retrieved.

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 507

Creating SAVE and SAVB Files

Syntax:

How to Create a SAVB File

From a request, use

ON TABLE SAVB [AS filename] [MISSING {ON|OFF}]

or

save_field SAVB [AS filename] [MISSING {ON|OFF}]

where:

save_field

Is the name of the last field in the request, excluding BY and ACROSS fields.

AS filename

Specifies a name for the SAVB file. If you do not specify a file name, SAVB is used as
the default. Since each subsequent SAVB command overwrites the previous SAVB file,
it is advisable to code a distinct file name in each request to direct the extracted data
to a separate file, thereby preventing it from being overwritten by the next SAVB
command.

You can also include a path, enclosed in single quotation marks, indicating where you wish
to store the SAVB file. For example:

ON TABLE SAVB FILENAME 'c:\dir\filename.ext '

MISSING

Ensures that fields with the MISSING attribute set to ON are carried over into the
SAVB file. The default is MISSING OFF. See Handling Records With Missing Field
Values on page 1035.

Example:

Creating a SAVB File

The following request extracts data from the SALES data source and creates a SAVB file.

TABLE FILE SALES
PRINT PROD_CODE AND AREA
BY DATE
WHERE CITY IS 'STAMFORD' OR 'UNIONDALE'
ON TABLE SAVB
END

A description of the BINARY file is appears after the records are retrieved.

508

The output is:

8. Saving and Reusing Your Report Output

Creating a PCHOLD File

The PCHOLD command enables you to extract data from the WebFOCUS Reporting Server by
way of the WebFOCUS client, and automatically display the data in HTML format in your
browser.

In addition, if you have established a helper application, you can use the command ON TABLE
PCHOLD to display the data in the helper application's viewer. For example, if a procedure
contains the ON TABLE PCHOLD FORMAT EXCEL command, data is not returned to the browser
in HTML format. Instead, data is returned and imported into an Excel spreadsheet, or other
spreadsheet program you specify to your browser.

In contrast, when data access is handled directly by the Reporting Server (without intervention
by the WebFOCUS Client), the data is extracted to a PCHOLD file and automatically delivered to
your PC for local reporting.

Note: If your environment supports the SET parameter SAVEMATRIX, you can preserve the
internal matrix of your last report in order to keep it available for subsequent HOLD, SAVE, and
SAVB commands when the request is followed by Dialogue Manager commands. For details on
SAVEMATRIX, see the Developing Reporting Applications manual.

Syntax:

How to Create a PCHOLD File

The syntax for PCHOLD in a report request is

ON TABLE PCHOLD [AS filename] [FORMAT fmt] [DATASET name.ext]

where:

PCHOLD

Enables you to extract and automatically display data in HTML format in your browser.
HOLD AT CLIENT is a synonym for PCHOLD. The PCHOLD command does not have a

Creating Reports With TIBCO® WebFOCUS Language

 509

Creating a PCHOLD File

default format. You must specify a format when using PCHOLD. The output is saved
with a Master File. For details about the behavior of PCHOLD, see Creating a HOLD
File on page 473.

If you specify an ON TABLE PCHOLD command without a FORMAT, XML/HTML code is
returned to the browser.

AS filename

Specifies a name for the PCHOLD file. If you do not specify a file name, PCHOLD
becomes the default. Since each subsequent PCHOLD command overwrites the
previous PCHOLD file, it is advisable to code a distinct file name in each request to
direct the extracted data to a separate file, thereby preventing it from being
overwritten by the next PCHOLD command.

FORMAT fmt

Specifies the format of the PCHOLD file.

To display as or in a webpage, choose:

HTML, HTMTABLE, DHTML, VISDIS

To display as a printed document, choose:

PDF, PS

To use in a text document, choose:

ALPHA, DOC, WP

To use in a spreadsheet application, choose:

DIF, XLSX, EXL2K [PIVOT], LOTUS

To use for additional reporting, choose:

ALPHA, DFIX, COM, COMT, TAB, TABT

To use in another application choose:

XML

To generate active output, choose:

AHTML, APDF, AFLEX

For details about all available formats, see Choosing Output File Formats on page 511.

510

8. Saving and Reusing Your Report Output

DATASET name.ext

Is used with FORMAT ALPHA to specify a file name and extension for the report output. The
result depends on the Redirection Settings in the WebFOCUS Administration Console for
the specified extension. If the extension is defined in the WebFOCUS Administration
Console, and the Save Report value is yes, the report output will be saved in your
Downloads directory with the specified file name and extension.

Choosing Output File Formats

You can select from a wide range of output formats to preserve your report output for use in
any of the following ways:

To display as or in a webpage, as a printed document, or in a text document.

To process in another application, such as a spreadsheet, a database, a word processor,
or a 3GL program.

To send to another location, such as a browser or PC.

To extract a subset of the original data source in order to generate multi-step reports.

For details on each of the supported formats, including the commands that support them
(HOLD, PCHOLD, SAVE) and the operating environments in which they are available, see the
reference topics for the following formats.

AHTML

DFIX

AHTMLTAB

DHTML

ALPHA

APDF

BINARY

COMMA

COM

COMT

DATREC

DB2

DBASE

DIF

DOC

EXL2K

EXL2K
FORMULA

EXL2K PIVOT

EXL97

FLEX

FOCUS

GIF

HTML

HTMTABLE

INGRES

INTERNAL

JPEG

JSCHART

JSON

LOTUS

PDF

POSTSCRIPT
(PS)

PPT

PPTX

REDBRICK

SQL

SQL_SCRIPT

SQLDBC

SQLINF

SQLMAC

SQLMSS

SQLODBC

SQLORA

SQLPSTGR

SQLSYB

SYLK

TAB

TABT

VISDIS

WK1

WP

XFOCUS

XLSX

XML

Creating Reports With TIBCO® WebFOCUS Language

 511

Choosing Output File Formats

Reference: FORMAT AHTML

Description: Saves report output as an active report (HTML file that can be used for offline
analysis and interactive functions without any connection to a server). All of the data and
JavaScript code are stored within the HTML file, which also makes the output highly
compressible for email and transparent to security systems. For more information about active
reports, see the Active Technologies User's Guide.

Use: For offline analysis of data.

Supported with the commands: HOLD, PCHOLD, SAVE.

Available in: WebFOCUS, FOCUS, App Studio.

Reference: FORMAT AHTMLTAB

Description: Creates an output file that contains only data and parameters used in an HTML
active report. The output produced is not a complete HTML active report. However, the file can
be included in another HTML document using the Dialogue Manager command -HTMLFORM.
For details, see the documentation on Dialogue Manager in the Developing Reporting
Applications manual.

Note: When issuing HOLD AS name FORMAT AHTMLTAB to embed an HTML active report into
another HTML document, you must include Active Technologies JavaScript code into the HTML
BODY using:

<BODY>
!IBI.OBJ.ACTIVEREPORTJS;

Use: For embedding HTML active reports into an existing HTML document.

Supported with the commands: HOLD, SAVE.

Available in: WebFOCUS, App Studio.

Reference: FORMAT ALPHA

Description: Saves report output as fixed-format character data and can be created as a HOLD
file.

ALPHA is the default SAVE format. The output file contains data only.

Text fields are supported in ALPHA-formatted files. See Using Text Fields in Output Files on
page 547.

To control missing data characters that are propagated to fields with the MISSING=ON
attribute, use the SET HNODATA command. For more information, see the Developing
Reporting Applications manual.

512

8. Saving and Reusing Your Report Output

Use: For display in a text document. For further reporting in FOCUS, WebFOCUS, or App Studio.
As a transaction file for modifying a data source.

Supported with the commands: HOLD, PCHOLD, SAVE.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT APDF

Description: Saves report output as an Adobe® Flex® report (Adobe® Flash® file) embedded in
a PDF file. The resulting PDF active report can be used for offline analysis and interactive
functions without any connection to a server.

In order to run a report created using the APDF format, Adobe Reader 9 or higher is required so
the Flash run-time code included in the Acrobat client can render the Flash content.

Use: For offline analysis of data.

Supported with the command: HOLD, PCHOLD, SAVE.

Available in: FOCUS, WebFOCUS, App Studio, InfoAssist.

Reference: FORMAT BINARY

Description: Saves report data and stores numeric fields as binary numbers. When created as
a HOLD file, also creates a Master File.

BINARY is the default format for HOLD files. When created in BINARY format:

The HOLD file is a sequential single-segment data source. The HOLD Master File is a
subset of the original Master File, and may also contain fields that have been created using
the COMPUTE or DEFINE commands or generated in an ACROSS phrase.

By default, fields with format I remain four-byte binary integers. Format F fields remain in
four-byte floating-point format. Format D fields remain in eight-byte double-precision floating-
point, and format P fields remain in packed decimal notation and occupy eight bytes (for
fields less than or equal to eight bytes long) or 16 bytes (for packed decimal fields longer
than eight bytes). Alphanumeric fields (format A) are stored in character format.

Every data field in the sequential extract record is aligned on the start of a full four-byte
word. Therefore, if the format is A1, the field is padded with three bytes of blanks on the
right. This alignment makes it easier for user-coded subroutines to process these data
fields. (Under some circumstances, you may wish to prevent the padding of integer and
packed decimal fields. Do so with HOLD FORMAT INTERNAL. See Saving Report Output in
INTERNAL Format on page 558.)

The output file contains data only.

Creating Reports With TIBCO® WebFOCUS Language

 513

Choosing Output File Formats

Use: For further reporting in FOCUS, WebFOCUS, or App Studio. As a transaction file for
modifying a data source.

Supported with the commands: HOLD

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT COMMA

Description: Saves the data values as a variable-length text file, with fields separated by
commas and with character values enclosed in double quotation marks. All blanks within fields
are retained. This format is the industry standard comma-delimited format.

This format does not have the safety feature of the double quote added within a text field
containing a double quote.

The extension for this format is PRN. This format type does not create a Master File.

Note:

Smart date fields and dates formatted as I or P fields with date format options are treated
as numeric, and are not enclosed in double quotation marks in the output file. Dates
formatted as alphanumeric fields with date format options are treated as alphanumeric,
and enclosed in double quotation marks.

Continental decimal notation (CDN=ON|SPACE|QUOTE|QUOTEP) is not supported. A comma
within a number is interpreted as two separate columns by a destination application such
as Microsoft Access.

The output file contains data only.

Use: For further processing in a database application. This format type can be imported into
applications such as Excel or Lotus.

Supported with the commands: HOLD, SAVE.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT COM

Description: Saves the data values as a variable-length text file with fields separated by
commas and with character values enclosed in double quotation marks. Leading blanks are
removed from numeric fields, and trailing blanks are removed from character fields. To issue a
request against this data source, the setting PCOMMA=ON is required.

This format also includes a built-in safety feature, which allows embedded quotes within
character fields. A second double quote (") is inserted adjacent to the existing one. For
example, if you input Joe "Smitty" Smith, the output is Joe ""Smitty"" Smith.

514

8. Saving and Reusing Your Report Output

The extension for this format is CSV. A Master File is created for this format type when the
command used to create the output file is HOLD. The SUFFIX in the generated Master File is
COM.

Note:

Smart date fields and dates formatted as I or P fields with date format options are treated
as numeric, and are not enclosed in double quotation marks in the output file. Dates
formatted as alphanumeric fields with date format options are treated as alphanumeric,
and enclosed in double quotation marks.

Continental decimal notation (CDN=ON|SPACE|QUOTE|QUOTEP) is not supported. A comma
within a number is interpreted as two separate columns by a destination application such
as Microsoft Access.

To create a variable-length comma- or tab-delimited HOLD file that differentiates between a
missing value and a blank string or zero value, use the SET NULL=ON command. For more
information, see the Developing Reporting Applications manual.

Use: For further processing in a database application. This format type can be imported into
applications such as Excel or Lotus.

Supported with the commands: HOLD, SAVE, PCHOLD.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT COMT

Description: Saves the column headings in the first row of the output file. It produces a
variable-length text file with fields separated by commas, and with character values enclosed in
double quotation marks. Leading blanks are removed from numeric fields, and trailing blanks
are removed from character fields. This format is required by certain software packages such
as Microsoft Access.

This format also includes a built-in safety feature, which allows embedded quotes within
character fields. A second double quote (") is inserted adjacent to the existing one. For
example, if you input Joe "Smitty" Smith, the output is Joe ""Smitty"" Smith.

The extension for this format is CSV. A Master File is created for this format type when the
command used to create the output file is HOLD. The SUFFIX in the generated Master File is
COMT.

Creating Reports With TIBCO® WebFOCUS Language

 515

Choosing Output File Formats

Note:

Smart date fields and dates formatted as I or P fields with date format options are treated
as numeric, and are not enclosed in double quotation marks in the output file. Dates
formatted as alphanumeric fields with date format options are treated as alphanumeric,
and enclosed in double quotation marks.

Continental decimal notation (CDN=ON|SPACE|QUOTE|QUOTEP) is not supported. A comma
within a number is interpreted as two separate columns by a destination application such
as Microsoft Access.

To create a variable-length comma- or tab-delimited HOLD file that differentiates between a
missing value and a blank string or zero value, use the SET NULL=ON command. For more
information, see the Developing Reporting Applications manual.

Use: For further processing in a database application. This format type can be imported into
applications such as Excel or Lotus.

Supported with the commands: HOLD, SAVE, PCHOLD.

Available in: FOCUS, App Studio, WebFOCUS.

Reference: FORMAT DATREC

Description: Saves report output as a sequential file with a Master File, and stores numeric
fields as binary numbers without aligning them on fullword boundaries. The last field consists
of one byte for each of the other fields in the Master File that indicates whether the
corresponding field is missing.

Use: For further reporting in FOCUS, WebFOCUS, or App Studio. As a transaction file for
modifying a data source.

Supported with the command: HOLD.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT DB2

Description: Creates a Db2 table, if you have the Adapter for Db2 and permission to create
tables.

Use: For further processing in a database application.

Supported with the command: HOLD.

Available in: WebFOCUS, App Studio, FOCUS.

516

8. Saving and Reusing Your Report Output

Reference: FORMAT DBASE

Description: Creates an extract file in dBase format that includes column headings in the first
row.

Note: Blank field names display as blank column titles. This may result in an error when
attempting to use the file as input to various applications.

Use: For importing data to Windows-based applications such as MS Access and Excel.

Supported with the command: HOLD.

Available in: App Studio.

Reference: FORMAT DFIX

Description: Creates a delimited output file. You can specify the delimiter, whether
alphanumeric fields should be enclosed within a special character such as a double quotation
mark, and whether the file should be generated with a header record containing the field
names.

For more information, see Creating a Delimited Sequential File on page 549.

Use: For importing data to Windows-based applications such as MS Access and Excel.

Supported with the command: HOLD, PCHOLD.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT DHTML

Description: Provides HTML output that has most of the features normally associated with
output formatted for printing such as PDF or PostScript output. You can create an HTML file
(.htm) or a Web Archive file (.mht). The type of output file produced is controlled by the value of
the HTMLARCHIVE parameter. HTMLARCHIVE=ON creates a Web Archive file.

Some of the features supported by format DHTML are:

Absolute positioning. DHTML precisely places text and images inside an HTML report,
allowing you to use the same StyleSheet syntax to lay out HTML as you use for PDF or PS
output.

On demand paging. On demand paging is available with SET HTMLARCHIVE=OFF.

PDF StyleSheet features. For example, the following features are supported: grids,
background colors, OVER, bursting, coordinated compound reports.

Creating Reports With TIBCO® WebFOCUS Language

 517

Choosing Output File Formats

Note:

The font map file for DHTML reports is dhtml.fmp.

Legacy compound reports are not supported.

Drillthrough reports are not supported.

Use: For display as a webpage.

Supported with the commands: HOLD, PCHOLD, SAVE.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT DIF

Description: Captures the entire report output, excluding headings, footings, subheads, and
subfoots, and creates a character file that can be easily incorporated into most spreadsheet
packages.

For example, running a TABLE request with HEADING/FOOTING and ON TABLE PCHOLD
FORMAT DIF does not display the report output with headings and footings. As a workaround,
use another format (such as HTML, PDF, or EXL2K).

Note: Microsoft Excel SR-1 is no longer supported for HOLD FORMAT DIF. To open these
reports, use either Microsoft Excel SR-2 or Microsoft Excel 2000.

Use: For display or processing in a spreadsheet application.

Supported with the commands: HOLD, PCHOLD, SAVE.

The PCHOLD variation transfers the data from a web server to a browser.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT DOC

Description: Captures the entire report output, including headings, footings, and subtotals,
and creates a text file with layout and line breaks that can be easily incorporated into most
word processing packages. DOC format uses a form-feed character to indicate page control
information.

Note: A request that contains ON TABLE PCHOLD FORMAT DOC results in a blank first page in
the report when displayed in Microsoft XP Office. To eliminate this, include SET PAGE=NOPAGE
in your request.

Use: For display in a text document.

Supported with the commands: HOLD, PCHOLD, SAVE.

518

8. Saving and Reusing Your Report Output

The PCHOLD variation transfers the data from a web server to a browser.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT XLSX

Description: Generates fully styled reports in Excel 2007 XML format. You must have
Excel 2007 or higher installed to use this output format. For details, see Choosing a Display
Format on page 575.

An Excel 2007 worksheet can contain 1,048,576 rows by 16,384 columns. WebFOCUS will
generate worksheets larger than these defined limits, but Excel 2007 will have difficulty
opening the resulting workbook, and the data that exceeds the Excel 2007 limits will be
truncated.

For information about creating overflow worksheets for the additional rows when the number of
rows becomes too high for a single worksheet, see Overcoming the Excel 2007/2010 Row
Limit Using Overflow Worksheets on page 713.

Use: For display or processing in a spreadsheet application.

Supported with the commands: HOLD, PCHOLD, SAVE.

For Internet Explorer, the PCHOLD variation launches Excel 2007 in the browser. For details,
and for information about working with XLSX files, see Choosing a Display Format on page
575.

Available in: WebFOCUS, App Studio.

Reference: FORMAT EXL2K

Description: Generates fully styled reports in Excel 2000 HTML format. You must have Excel
2000 installed to use this output format. For details, see Choosing a Display Format on page
575.

ACROSS column titles are supported for EXL2K output format.

For EXL2K output format, a report can include 65,536 rows and/or 256 columns. Rows and
columns in excess of these limits are truncated from the worksheet when opened in Excel.

For information about creating overflow worksheets for the additional rows when the number of
rows becomes too high for a single worksheet, see Overcoming the Excel 2007/2010 Row
Limit Using Overflow Worksheets on page 713.

Use: For display or processing in a spreadsheet application.

Supported with the commands: HOLD, PCHOLD, SAVE.

Creating Reports With TIBCO® WebFOCUS Language

 519

Choosing Output File Formats

For Internet Explorer, the PCHOLD variation launches Excel 2000 in the browser. For details,
and for information about working with EXL2K files, see Choosing a Display Format on page
575.

Available in: WebFOCUS, App Studio.

Reference: FORMAT EXL2K FORMULA

Description: Specifies that the report will be displayed as an Excel 2000 spreadsheet, with
WebFOCUS totals and other calculated values translated to active Excel formulas. For details,
see Choosing a Display Format on page 575.

Use: For display or processing in a spreadsheet application.

Supported with the commands: HOLD, PCHOLD, SAVE.

Available in: WebFOCUS, FOCUS, App Studio.

Reference: FORMAT EXL2K PIVOT

Description: Generates fully styled reports in Excel 2000 HTML format, with added pivoting
capabilities. Requires Excel 2000 on your PC. For details, see Choosing a Display Format on
page 575.

Use: For display or processing in a spreadsheet application.

Supported with the commands: HOLD, PCHOLD, SAVE.

For Internet Explorer, the PCHOLD variation transfers the data from a web server to a browser,
which launches Excel 2000.

Available in: WebFOCUS, FOCUS, App Studio.

Reference: FORMAT EXL97

Description: Enables you to view and save reports in Excel 97 that include full styling. For
details on working with Excel formats, see Choosing a Display Format on page 575.

Leading zeros do not display for FORMAT EXL97.

Use: For display or processing in a spreadsheet application.

Supported with the command: HOLD, PCHOLD, SAVE.

Available in: FOCUS, WebFOCUS, App Studio.

520

8. Saving and Reusing Your Report Output

Reference: FORMAT FLEX

Description: Saves report output as an active report in an Adobe Flash player compatible (.swf)
file that can be used for offline analysis and interactive functions without any connection to a
server. Internet Explorer, Mozilla Firefox, and Opera internet browsers recognize an active
report in the Adobe Flex format as a Shockwave Flash Object.

In order to run a report created using the Active Technologies for Adobe Flash player (FLEX)
format, Adobe Flash Player 9.0.28 or higher is required.

Use: For offline analysis of data.

Supported with the command: HOLD, SAVE.

Available in: FOCUS, WebFOCUS, App Studio.

Reference: FORMAT FOCUS

Description: Creates a FOCUS data source. Four files result: a HOLD data file, a HOLD Master
File, and two work files. See Holding Report Output in FOCUS Format on page 479.

Text fields are supported for FOCUS output files. See Using Text Fields in Output Files on page
547.

Use: For further processing in a database application.

Supported with the command: HOLD.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT GIF

Description: Saves the output of a graph request as a GIF file.

Use: The resulting GIF file can be embedded in the heading/footing or body of a PDF or HTML
report. This technique is useful when you want to create a single PDF or HTML report that
contains multiple outputs, such as output from a TABLE request and a GRAPH request. You
can distribute this type of report using ReportCaster.

When running graphs in GIF format on a UNIX platform with the HEADLESS configuration, the
graph may not display properly. You may see a red X instead of your image. This is due to
Sun's methodology of creating images without a head, which does not currently support GIF
graphics.

Supported with the commands: HOLD.

Available in: WebFOCUS, App Studio.

Creating Reports With TIBCO® WebFOCUS Language

 521

Choosing Output File Formats

For details see Creating a Graph on page 1743.

Reference: FORMAT HTML

Description: Creates a complete HTML document that can be viewed in a web browser. The
PCHOLD variation transfers the data from a web server to a browser.

The following StyleSheet features are supported with HTML: JAVASCRIPT (drill down to
JavaScript), TARGET, COLSPAN, HEADALIGN, IMAGEALIGN, IMAGEBREAK, GUTTER,
BACKIMAGE, BACKCOLOR, IMAGE, GRIDS.

Use: For display as a webpage.

Supported with the commands: HOLD, PCHOLD, SAVE.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT HTMTABLE

Description: Creates an output file that contains only an HTML table. The output produced is
not a complete HTML document.

However, the file can be included in another HTML document using the Dialogue Manager
command -HTMLFORM. For details see the documentation on Dialogue Manager in the
Developing Reporting Applications manual.

Note: When issuing HOLD AS name FORMAT HTMTABLE, you must specify a different name
than the .htm filename used in the -HTMLFORM name.

The following StyleSheet features are supported with HTML: JAVASCRIPT (drill down to
JavaScript), TARGET, COLSPAN, HEADALIGN, IMAGEALIGN, IMAGEBREAK, BACKCOLOR, IMAGE,
GRIDS.

Internal cascading style sheets (CSS) are supported for FORMAT HTMTABLE. The CSS code is
placed immediately before the TABLE command.

Use: For embedding reports and graphs in an existing HTML document.

Supported with the commands: HOLD, PCHOLD, SAVE.

The PCHOLD variation also transfers the data from a web server to a browser.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT INGRES

Description: Creates an Ingres table, if you have the Adapter for Ingres and permission to
create tables.

522

8. Saving and Reusing Your Report Output

Use: For further processing in a database application.

Supported with the command: HOLD.

Available in: WebFOCUS, App Studio, FOCUS when used as a client to the WebFOCUS
Reporting Server.

Reference: FORMAT INTERNAL

Description: Saves report output without padding the values of integer and packed fields. See
Saving Report Output in INTERNAL Format on page 558.

Use: For accurate processing by 3GL programs.

Supported with the command: HOLD, SAVB.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT JPEG

Description: Saves the output of a graph request as a JPEG file.

Use: The resulting JPEG file can be embedded in the heading/footing or body of a PDF or HTML
report. This technique is useful when you want to create a single PDF or HTML report that
contains multiple outputs, such as output from a TABLE request and a GRAPH request. You
can distribute this type of report using ReportCaster. JPEG (.jpg) files behave the same as GIF
files.

Note: For JPEG files, only the .jpg extension is supported. The .jpeg extension is not
supported.

Supported with the commands: HOLD.

Available in: WebFOCUS, App Studio.

For details, see Linking From a Graphic Image on page 868 and Adding an Image to a Report
on page 1462.

Reference: FORMAT JSCHART

Description: Saves the output of a graph request as an HTML5 graph.

Use: The charts are rendered in the browser as high quality interactive vector graphics using a
built-in JavaScript engine. Note that older browsers do not support all of the features of the
HTML5 standard. You must include the following command to create an HTML5 graph:

ON GRAPH PCHOLD FORMAT JSCHART

Creating Reports With TIBCO® WebFOCUS Language

 523

Choosing Output File Formats

Supported with the commands: ON GRAPH PCHOLD, ON GRAPH HOLD.

Available in: WebFOCUS, App Studio.

For details, see Creating an HTML5 Graph on page 1747.

Reference: FORMAT JSON

Description: JSON (JavaScript Object Notation) is a plain text format that consists of name:
value pairs and is based on JavaScript. It can be parsed by many types of software and it often
used for storing and exchanging data. The field names and values in a report request can be
held in a FORMAT JSON file. Subtotals, headings, footings, and ACROSS fields are not
propagated to the HOLD file. A synonym is generated for the HOLD file. Adding the syntax
STRUCTURE HIERARCHY to the HOLD command generates a JSON output file that identifies
the sort fields and display fields in the request.

Use: For data interchange between systems and applications.

Supported with the commands: HOLD, PCHOLD

Available in: WebFOCUS, FOCUS

Reference: FORMAT LOTUS

Description: Captures all the columns of the report in a character file that LOTUS 1-2-3 can
then import. All alphanumeric fields are enclosed in quotation marks. Columns are separated
by commas.

Use: For display and processing in a spreadsheet application.

Supported with the commands: HOLD, PCHOLD, SAVE (WebFOCUS only).

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT PDF

Description: Saves the report output in Adobe Portable Document Format (PDF), which enables
precise placement of output (all formatting options such as headings, footings, and titles)
correctly aligned on the physical page, so the report looks exactly as it does when printed.

In WebFOCUS, PDF format also supports StyleSheets that contain drill down parameters, links
to arbitrary URLs, and embedded GIF or JPEG images in report, page, and sort headings and
footings.

524

8. Saving and Reusing Your Report Output

PDF format does not support OLAP reports since Java applets cannot be embedded inside PDF
documents. However, an OLAP report can drill down to a PDF-formatted report. PDF does not
support drill downs when sorting across column. When you drill down from one report to
another report, do not use the following characters: + (plus sign); # (number sign); &
(ampersand); \ (backslash).

A PDF object is a page, hyperlink, or image. The Portable Document Format (PDF) limits the
number of objects that a PDF document can contain. WebFOCUS imposes the following object
limits for each PDF report:

Object

Pages

Images

Hyperlinks per page

Total pages with hyperlinks

Total hyperlinks

Limit

10,000

900

500

100

44,500

PDF format retains all formatting options, such as a headings, footings, and titles.

The following fonts are supported: Courier (fixed width), Times (proportional width), and
Helvetica (proportional width). PDF format maps all fonts to Courier, Helvetica, or Times. The
font styles that can be used are Normal (default), Bold, Italic, Underline, and combinations of
these.

The following StyleSheet features are supported with PDF: PAGESIZE, ORIENTATION, UNITS,
TOPMARGIN, BOTTOMMARGIN, LEFTMARGIN, RIGHTMARGIN, POSITION, SQUEEZE, FOCEXEC
(drill down to FOCEXEC), URL (drill down to URL), HGRID, VGRID, BACKCOLOR. Note when you
use BACKCOLOR with PDF reports, extra space is added to the top, bottom, right, and left of
each cell of data in the report. This is for readability and to prevent data truncation.

Use: For display as a printed document.

Supported with the commands: HOLD, PCHOLD, SAVE (WebFOCUS only).

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT PDF OPEN/CLOSE

Description: Saves multiple reports into one PDF report.

Creating Reports With TIBCO® WebFOCUS Language

 525

Choosing Output File Formats

Use: For combining multiple reports into a single PDF file, also known as a compound report.
For complete details, see Laying Out the Report Page on page 1331.

Supported with the command: PCHOLD.

Available in: WebFOCUS, App Studio, FOCUS

Reference: FORMAT POSTSCRIPT (PS)

Description: Creates an output file in PostScript format, which supports headings, footings,
and totals.

PS is an abbreviation for POSTSCRIPT.

PostScript format supports headings, footings, and totals. PS supports ISO Latin font
encoding.

Use: For display as a printed document.

Supported with the command: HOLD, PCHOLD.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT PPT

Description: Creates an output file in PowerPoint® format in which each page of report output
becomes a separate slide in the file with all styling applied.

Use: For use in a slide presentation.

Supported with the command: HOLD, SAVE.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT PPTX

Description: Creates an output file in PowerPoint format in which each page of report output
becomes a separate slide in the file with all styling applied.

Use: For use in a slide presentation.

Supported with the command: HOLD, SAVE.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT REDBRICK

Description: Creates a Red Brick table, if you have the Adapter for Red Brick and permission to
create tables.

526

8. Saving and Reusing Your Report Output

Use: For further processing in a database application.

Supported with the command: HOLD.

Available in: WebFOCUS, App Studio, FOCUS when used as a client to the WebFOCUS
Reporting Server.

Reference: FORMAT SQL_SCRIPT

Description: Creates an SQL subquery file or a file of data values with a corresponding
synonym.

When used in a request against a relational data source, the HOLD FORMAT SQL_SCRIPT
command generates the SQL SELECT statement needed to execute the current query. It then
stores it in the application folder as a file with a .sql extension, along with the Master and
Access File pair that describes the SQL answer set.

When used in a request against any other type of data source, the HOLD FORMAT SQL_SCRIPT
command executes the current query and stores the retrieved values in the application folder
as a sequential file with a .ftm extension, along with the Master File that describes the
retrieved data.

Use: You can use the output from HOLD FORMAT SQL_SCRIPT as the target file for the
DB_INFILE function. For information about the DB_INFILE function, see the Using Functions
manual.

Supported with the command: HOLD.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT SQLDBC

Description: Creates a Teradata table, if you have the Adapter for Teradata and permission to
create tables.

Use: For processing in a database application.

Supported with the command: HOLD.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT SQLINF

Description: Creates an Informix table, if you have the Adapter for Informix and permission to
create tables.

Use: For processing in a database application.

Creating Reports With TIBCO® WebFOCUS Language

 527

Choosing Output File Formats

Supported with the command: HOLD.

Available in: WebFOCUS, App Studio, FOCUS when used as a client to the WebFOCUS
Reporting Server.

Reference: FORMAT SQLMAC

Description: Creates a Microsoft Access table, if you have the Adapter for Microsoft Access
and permission to create tables.

Use: For processing in a database application.

Supported with the command: HOLD.

Available in: WebFOCUS, App Studio.

Reference: FORMAT SQLMSS

Description: Creates a Microsoft SQL Server table, if you have the Adapter for Microsoft SQL
and permission to create tables.

Use: For processing in a database application.

Supported with the command: HOLD.

Available in: WebFOCUS, App Studio, FOCUS when used as a client to the WebFOCUS
Reporting Server.

Reference: FORMAT SQLODBC

Description: Creates an SQLODBC table if you have the current Adapter for ODBC and
permission to create tables.

Use: For processing in a database application.

Supported with the command: HOLD.

Available in: WebFOCUS, App Studio, FOCUS when used as a client to the WebFOCUS
Reporting Server.

Reference: FORMAT SQLORA

Description: Creates an Oracle table, if you have the Adapter for Oracle and permission to
create tables.

Use: For processing in a database application.

Supported with the command: HOLD.

528

8. Saving and Reusing Your Report Output

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT SQLPSTGR

Description: Creates a PostgreSQL table, if you have the Adapter for PostgreSQL and
permission to create tables.

Use: For processing in a database application.

Supported with the command: HOLD.

Available in: WebFOCUS, App Studio, FOCUS when used as a client to the WebFOCUS
Reporting Server.

Reference: FORMAT SQLSYB

Description: Creates a Sybase table, if you have the Adapter for Sybase and permission to
create tables.

Use: For processing in a database application.

Supported with the command: HOLD.

Available in: WebFOCUS, App Studio, FOCUS when used as a client to the WebFOCUS
Reporting Server.

Reference: FORMAT SYLK

Description: Captures all the columns of the report request in a character file for Microsoft's
spreadsheet program Multiplan. The generated file cannot have more than 9,999 rows.

Use: For display and processing in a spreadsheet application.

Supported with the command: HOLD, SAVE.

Available in: WebFOCUS, App Studio, FOCUS.

Creating Reports With TIBCO® WebFOCUS Language

 529

Choosing Output File Formats

Reference: FORMAT TAB

Description: Creates an output file in tab-delimited format. The TAB format includes a built-in
safety feature, which allows embedded quotes within character fields. A second double quote
(") is inserted adjacent to the existing one. For example, if you input Joe "Smitty" Smith, the
output is Joe ""Smitty"" Smith. The TAB format also includes the following features:

All trailing blanks are stripped from alpha [An] fields.

All leading blanks are stripped from numeric [/Dx.y, /Fx.y, /Px.y, and /In] fields.

There is a 32K record length limit in the output file.

A Master File is created when the HOLD command is used to create the output file. The
Master File behaves exactly as in FORMAT ALPHA, except for the inclusion of double
quotes.

Note: To create a variable-length comma- or tab-delimited HOLD file that differentiates between
a missing value and a blank string or zero value, use the SET NULL=ON command. For more
information, see the Developing Reporting Applications manual.

Use: For importing data to Windows-based applications such as MS Access and Excel.

Supported with the command: HOLD, SAVE, PCHOLD.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT TABT

Description: Creates an output file in tab-delimited format that includes column headings in
the first row. The TABT format includes a built-in safety feature, which allows embedded quotes
within character fields. A second double quote (") is inserted adjacent to the existing one. For
example, if you input Joe "Smitty" Smith, the output is Joe ""Smitty"" Smith. The TABT format
also includes the following features:

The first row contains field names.

All trailing blanks are stripped from alpha [An] fields.

All leading blanks are stripped from numeric [/Dx.y, /Fx.y, /Px.y, and /In] fields.

There is a 32K record length limit in the output file.

A Master File is created when the HOLD command is used to create the output file. The
Master File behaves exactly as in FORMAT ALPHA, except for the inclusion of double
quotes.

530

8. Saving and Reusing Your Report Output

Note:

Blank field names display as blank column titles. This may result in an error when
attempting to use the file as input to various applications.

To create a variable-length comma- or tab-delimited HOLD file that differentiates between a
missing value and a blank string or zero value, use the SET NULL=ON command. For more
information, see the Developing Reporting Applications manual.

Use: For importing data to Windows-based applications such as MS Access and Excel.

Supported with the command: HOLD, SAVE, PCHOLD.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT VISDIS

Description: WebFOCUS has a data visualization tool called Visual Discovery that creates
graphs using a tab-delimited data file as input. The first record of the data file contains the
column titles for the data values. The next record can contain the Visual Discovery field
formats. If this record is not present, Visual Discovery attempts to determine the formats of
the data fields by reading the first 50 records from the data file, a process that is not
guaranteed to create accurate representations of the WebFOCUS formats.

The following table identifies format conversions for HOLD FORMAT VISDIS:

FOCUS Format

Integer

Decimal/Packed

Alphanumeric

Date format (smart date)

Visual Discovery Format

I

R

S

D%format%format%format (for example, D
%Y%M%D). If the year is not a four-digit
year, the format returned is S.

Other

S

Note: No Master File is created for format VISDIS.

Use: HOLD FORMAT VISDIS creates a tab-delimited output file with the extension .txt in which
the first record has the column titles and the second record contains Visual Discovery formats
based on the FOCUS field formats of the data.

Creating Reports With TIBCO® WebFOCUS Language

 531

Choosing Output File Formats

Supported with the command: HOLD, SAVE, PCHOLD

Available in: WebFOCUS, FOCUS.

Reference: FORMAT WK1

Description: Captures all the columns of the report in a character file that LOTUS 1-2-3
Release 2 can then import.

Use: For display and processing in a spreadsheet application.

Supported with the commands: HOLD, PCHOLD.

Available in: App Studio.

Reference: FORMAT WP

Description: Captures the entire report output, including headings, footings, and subtotals,
and creates a text file that can easily be incorporated into most word processing packages.

Text fields are supported in WP format. See Using Text Fields in Output Files on page 547.

To control whether a carriage control character is included in column 1 of each page of the
report output, use:

[ON TABLE] HOLD AS filename FORMAT WP [CC|NOCC]

NOCC excludes carriage control characters. The position reserved for those characters remains
in the file, but is blank. CC includes carriage control characters and, in z/OS, creates the
HOLD file with RECFM VBA. To include page control information in the WP file, you can also
specify the TABPAGENO option in a heading or the SET PAGE=OFF command. The character 1
in the column 1 indicates the start of a new page.

The following rules summarize FORMAT WP carriage control options:

The CC option always inserts the carriage control character.

The NOCC option always omits the carriage control character.

When you issue HOLD FORMAT WP without the CC or NOCC option:

SET PAGE NUM=OFF and SET PAGE NUM=TOP always insert the carriage control
character.

SET PAGE NUM=NOPAGE always omits the carriage control character.

SET PAGE NUM=ON inserts the carriage control character if TABPAGENO is included in
the heading and omits the carriage control character if TABPAGENO is not included in
the heading.

532

8. Saving and Reusing Your Report Output

Tip: HOLD FORMAT WP does not change the number of lines per page. In order to do so, issue
one or a combination of the commands SET PRINT=OFFLINE, SET SCREEN=PAPER, or SET
SCREEN=OFF.

The WP file is created with a record format of VB in z/OS when the carriage control character is
omitted and with a record format of VBA when the carriage control character is inserted.

The maximum record length for HOLD FORMAT WP is 358 characters, 356 of which can
represent data. For larger output, use PCHOLD FORMAT WP.

If you need the report width to remain fixed across releases for later processing of the output
file, you can set the width you need using the SET WPMINWIDTH command. This parameter
specifies the minimum width of the output file. It will be automatically increased if the width
you set cannot accommodate the fields propagated to the output file in the request. The
LRECL of the output file will be four bytes more than the report width on z/OS because the file
is variable length and needs an additional four bytes to hold the actual length of each record
instance. In other operating environments, the length of the record is the value of
WPMIDWIDTH.

FORMAT WP retains headings, footings, and subtotals.

Use: For display in a text document.

Supported with the commands: HOLD, PCHOLD, SAVE.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT XFOCUS

Description: Creates an XFOCUS data source.

Use: For further processing in a database application.

Supported with the command: HOLD.

Available in: WebFOCUS, App Studio, FOCUS.

Reference: FORMAT XML

Description: Creates an XML output file based on an internal DTD that includes the rows that
are displayed in the final report output. It does not honor the HOLDLIST setting. It does not
honor the ASNAMES setting. The parameter HOLDATTRS ON is automatically invoked. The XML
file generated is based on the structure and layout of the report request. The metadata
included in the DTD for each column is FIELDNAME, ALIAS, data type, width, FOCUS format,
DESCRIPTION, ACCEPTS, HELP_MESSAGE, TITLE, WITHIN, PROPERTY, REFERENCE, VALIGN,
and column title. FORMAT XML does not create a Master File.

Creating Reports With TIBCO® WebFOCUS Language

 533

Merging Data Into an Existing Data Source With ON TABLE MERGE

Note: When using an HTML Autoprompt page (select Run in new Window option), BI Portal, or
an HTML page created with HTML canvas, browsers running in Standards Mode displaying
output in an iframe do not display XML. When running a WebFOCUS request with PCHOLD
FORMAT XML, the result will display in a new window.

Use: For further processing.

Supported with the command: HOLD, PCHOLD.

Available in: WebFOCUS, FOCUS.

Merging Data Into an Existing Data Source With ON TABLE MERGE

The ON TABLE MERGE clause in a TABLE or TABLEF command enables you to insert, update,
and delete records in an existing single-segment data source.

Data sources that support insert, update, and delete operations, either for individual records
or bulk load, can take advantage of the full set of options for ON TABLE MERGE. Relational
data sources support all of these options. Other data sources, such as delimited and fixed
format sequential data sources, can only have records appended to the existing data source.

Reference: ON TABLE MERGE Processing

An ON TABLE MERGE request consists of two sections.

A TABLE or TABLEF request that retrieves the data from the source file to be merged into
the target file.

All TABLE syntax is supported, from any type of data source that has an accompanying
synonym. The request can include joins, DEFINEs, COMPUTEs, and any other supported
syntax. The records retrieved are either passed directly to a Relational DBMS in an SQL
request (when the request can be optimized), loaded using the SQL MERGE command
(when the request cannot be optimized but the database supports the SQL MERGE
command), or stored in an internally-generated HOLD file that is used as the input to a
MODIFY request.

An ON TABLE MERGE clause that specifies the existing target data source for the merge,
the UPDATE, DELETE, or INSERT commands, and the calculations of the field values to be
updated or inserted.

The target must be a single-segment file with a corresponding synonym, and it must have a
Write Adapter that enables WebFOCUS to update it.

534

8. Saving and Reusing Your Report Output

Supported Merge Phrases

MATCHING expression. Specifies the expression that selects the source and target
records to be passed to the UPDATE, DELETE, or INSERT commands. If records are only to
be appended, no MATCHING phrase is used.

WHEN MATCHED [AND expression] UPDATE. Updates matching records. Optionally,
provides an additional expression that can be used to perform different updates to different
sets of target records. To perform multiple sets of updates, include multiple WHEN
MATCHED UPDATE phrases.

The new target field values are calculated using expressions specified following the WHEN
MATCHED UPDATE phrase.

WHEN MATCHED [AND expression] DELETE. Deletes matching records. Optionally,
provides an additional expression that can be used to delete multiple sets of target
records. To delete multiple sets of records, include multiple WHEN MATCHED DELETE
phrases.

WHEN NOT MATCHED INSERT. Is used to insert new records when no field values satisfy
the MATCHING expression.

The new target field values are calculated using expressions specified following the WHEN
NOT MATCHED INSERT phrase.

INSERT. When there is no MATCHING phrase and no WHEN NOT MATCHED phrase, INSERT
is used to append new records.

The new target field values are calculated using expressions specified following the INSERT
phrase.

Properties of the Generated MERGE Request

The merge request can be generated in several ways.

Optimized request. If the source and target are in the same database (have the same
suffix and use the same connection), and MERGE (or INSERT from SELECT, for INSERT) is
supported by the DBMS, the whole request passed to the DBMS in an SQL request.

With an optimized request, the MATCHING expression can be any expression, and if any
record fails in the merge request, the entire merge is rejected.

Creating Reports With TIBCO® WebFOCUS Language

 535

Merging Data Into an Existing Data Source With ON TABLE MERGE

Non-Optimized request. If for any reason, the request cannot be optimized, for example if
the target and source are from different databases or use different connections, or, if the
TABLE request contains syntax that cannot be optimized, one of the following methods is
used to do the merge.

If the target database supports bulk load into a temporary table, and also supports
MERGE, then the data is loaded using bulk load into the target database as a temporary
table, and the target table is updated using the SQL MERGE command with the
temporary table as input.

If the target database supports MERGE but not bulk load, then the data will be loaded
on a record-by-record basis, one request per record. This is more efficient than using a
MODIFY request (which happens if the target database does not support MERGE), as
MODIFY uses two requests per record (SELECT+INSERT or SELECT+UPDATE).

If the target database does not support MERGE, a HOLD file of the values retrieved by
the TABLE request is generated in DATREC (fast binary) format.

With a DATREC HOLD file, the processing is done by a simple MODIFY request. The
MATCHING expression must match on all key fields, and processing is done on a record-
by-record basis, so if a record fails the merge request, the request continues with the
next record.

No logs are generated for an ON TABLE MERGE request. Therefore, when working with
production files, creating a backup of the source file prior to running the request is
recommended. At the end of the merge processing, messages are generated that indicate if
the merge was successful and how many records were affected. The following image shows an
example of the messages displayed for an optimized request.

The following image shows an example of the messages displayed for a non-optimized request.

536

8. Saving and Reusing Your Report Output

If not all records were processed and you want to know which records were rejected, you must
either enable traces or look in the Session Log.

Syntax:

How to Merge Data Into an Existing Data Source With ON TABLE MERGE

In the following syntax, at least one UPDATE, DELETE, or INSERT command must be supplied.
Multiple UPDATE and DELETE commands are supported, when multiple expressions provide
separate update or delete conditions and target field values.

{TABLEF|TABLE} FILE
...
ON TABLE MERGE INTO FILE target_mf
[MATCHING matching_expression;]

[
   WHEN MATCHED [AND matching_expression2;] UPDATE
     target_field1=expression1;
     target_field2=expression2; ...
   ...
]

[
   WHEN MATCHED [AND matching_expression3;] DELETE
   ...
]

[
 [WHEN NOT MATCHED] INSERT
  target_field3=expression3;
  target_field4=expression4; ...
]
END

where:

target_mf

Is the name of the Master File for the target data source that is to be updated.

MATCHING matching_expression

Is the expression to match in order to apply the INSERT, UPDATE, and DELETE commands.
The expression can be complex. For a non-optimized request, where the merge is
performed by a MODIFY procedure, all key fields must be matched in the expression. Omit
this phrase when using the INSERT command to append records. If the field names are the
same in the source and target files, use the prefix SRC. to reference fields in the source
file, and the prefix TRG. to reference fields in the target file.

Creating Reports With TIBCO® WebFOCUS Language

 537


Merging Data Into an Existing Data Source With ON TABLE MERGE

matching_expression2

Is an additional expression to match in order to apply the UPDATE command. If the field
names are the same in the source and target files, use the prefix SRC. to reference fields
in the source file, and the prefix TRG. to reference fields in the target file.

target_field1, target_field2 ...

Are one or more fields to be updated in the target data source.

expression1, expression2

Are expressions used to calculate the target field values to be used for updating the
existing target field values. These expressions can use fields from the TABLE request and
the target data source. If the field names are the same in the source and target files, use
the prefix SRC. to reference fields in the source file, and the prefix TRG. to reference fields
in the target file.

matching_expression3

Is an additional expression to match in order to apply the DELETE command. If the field
names are the same in the source and target files, use the prefix SRC. to reference fields
in the source file, and the prefix TRG. to reference fields in the target file.

target_field3, target_field4 ...

Are the target field values for the new record to be inserted when the value of
matching_expression is not found in the target data source.

expression3, expression4, expression5

Are expressions used to calculate the target field values to be used for inserting the new
record. These expressions can use fields from the TABLE request. Use the prefix SRC. to
reference these fields.

538

8. Saving and Reusing Your Report Output

Example:

Updating and Inserting Records Using ON TABLE MERGE

This example uses source and target data sources from the DataMigrator - General tutorial. To
access the tutorial, click the New button (+) on the Applications page ribbon and click
Tutorials, or right-click an application folder, point to New, and click Tutorials. Scroll down to
the DataMigrator - General tutorial. Select or enter values for the DBMS, Connection, prefix,
and application, and click Create.

The following request updates records in the table dmrpts from records in the table dminv,
when the field value PROD_NUM in dminv (SRC.PROD_NUM) matches the field value
PROD_NUM in dmrpts (TRG.PROD_NUM). When the PROD_NUM fields do not match, records
are inserted.

TABLE FILE dminv
PRINT
   PROD_NUM
 COMPUTE QUANTITY =  SUM.QTY_IN_STOCK;
 COMPUTE LINEPRICE =  SUM.PRICE;
 COMPUTE LINECOST = SUM.COST;
 COMPUTE LINECOGS = LINECOST * QUANTITY;

ON TABLE MERGE INTO FILE dmrpts
MATCHING TRG.PROD_NUM EQ SRC.PROD_NUM;

WHEN MATCHED UPDATE
  QUANTITY=SRC.QUANTITY;
  YRMTH = TRG.YRMTH+1;
  LINEPRICE=SRC.LINEPRICE;
  LINECOGS=SRC.LINECOGS;
  PROFIT=SRC.LINECOGS - SRC.LINECOST;

WHEN NOT MATCHED INSERT
  STORE_CODE='1004NY';
  PROD_NUM=SRC.PROD_NUM;
  YRMTH=202101;
  QUANTITY=SRC.QUANTITY;
  LINEPRICE=SRC.LINEPRICE;
  LINECOGS=SRC.LINECOGS;
  PROFIT=SRC.LINECOGS - SRC.LINECOST;
END

The following TABLE request prints the values in the updated dmrpts target.

TABLE FILE DMRPTS
PRINT *
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 539



Merging Data Into an Existing Data Source With ON TABLE MERGE

The following image of the last page of the output shows the updated values in the existing
records, and the inserted records (the last two rows).

540

8. Saving and Reusing Your Report Output

Example:

Appending a Record With ON TABLE MERGE

This example uses GGSALES as the source and a DATREC version of GGPRODS, named
GGDATREC, as the target. The following image shows GGDATREC in its original state.

The following request appends one record to the GGDATREC target using ON TABLE MERGE.
There is no MATCHING or WHEN NOT MATCHED phrase.

TABLE FILE ggsales
SUM
   FST.PCD
   FST.PRODUCT
   FST.UNITS
   FST.DOLLARS

ON TABLE MERGE INTO FILE GGDATREC
INSERT
  PRODUCT_ID=SRC.PCD;
  PRODUCT_DESCRIPTION=SRC.PRODUCT;
  VENDOR_CODE='V400';
  VENDOR_NAME='Acme Foods';
  PACKAGE_TYPE='Case';
  SIZE = 18;
  UNIT_PRICE = SRC.DOLLARS/SRC.UNITS;
END

The following TABLE request prints the values in the updated ggdatrec target.

TABLE FILE GGDATREC
PRINT *
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 541


Merging Data Into an Existing Data Source With ON TABLE MERGE

The following image shows the appended record (the last row).

Example:

Deleting Records Using ON TABLE MERGE

The following request uses the dminv table and a single-segment version of the dmord table
generated by the DataMigrator - General tutorial.

The following request displays all of the plant locations in the dmordsgl data source.

TABLE FILE DMORDSGL
SUM QUANTITY
BY PLANT
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
END

The output is shown in the following image.

542

8. Saving and Reusing Your Report Output

The following ON TABLE MERGE request deletes records where the source product number
matches the target product number and the plant is 'LA'.

TABLE FILE dminv
PRINT
PROD_NUM
ON TABLE MERGE INTO FILE dmordsgl
MATCHING TRG.PROD_NUM EQ SRC.PROD_NUM;
WHEN MATCHED AND PLANT EQ 'LA'; DELETE
END

Running this request and then the request to display the plants shows that the records with
the LA plant have been deleted, as shown in the following image.

Reference: Best Practices for ON TABLE MERGE

We strongly recommend that you make a backup copy of your target data source prior to
using ON TABLE MERGE, in case you need to restore it to its original contents.

Always use the SRC. and TRG. prefixes in the merge expressions, for safety and clarity.

The TABLE commands prior to the ON TABLE MERGE clause internally generate a HOLD file,
and the merge is done from the HOLD file into the target file. The HOLD file generates alias
names for the source fields in the form E01, E02, and so on. These names are unique to
each field, while field names in the TABLE request may generate duplicate field names in
the HOLD file. Unique names must be used, so either use the alias names, or assign a
new name to a duplicate field name using the AS phrase. For example, the following
request generates three fields named DOLLARS:

TABLE FILE GGSALES
SUM DOLLARS MAX.DOLLARS MIN.DOLLARS
BY UNITS
ON TABLE HOLD
END

Creating Reports With TIBCO® WebFOCUS Language

 543

Merging Data Into an Existing Data Source With ON TABLE MERGE

The generated Master File shows the duplicate field names and unique alias names.

FILENAME=HOLD, SUFFIX=FIX     , IOTYPE=BINARY, $
  SEGMENT=HOLD, SEGTYPE=S1, $
    FIELDNAME=UNITS, ALIAS=E01, USAGE=I08, ACTUAL=I04, $
    FIELDNAME=DOLLARS, ALIAS=E02, USAGE=I08, ACTUAL=I04, $
    FIELDNAME=DOLLARS, ALIAS=E03, USAGE=I08, ACTUAL=I04, $
    FIELDNAME=DOLLARS, ALIAS=E04, USAGE=I08, ACTUAL=I04, $

The following version of the request generates unique field names using the AS phrase.

TABLE FILE GGSALES
SUM DOLLARS AS TOTDOLL
MAX.DOLLARS AS MAXDOLL
MIN.DOLLARS AS MINDOLL
BY UNITS
ON TABLE SET ASNAMES ON
ON TABLE HOLD AS UNIQNAME
END

This request generates the following Master File.

FILENAME=UNIQNAME, SUFFIX=FIX     , IOTYPE=BINARY, $
  SEGMENT=UNIQNAME, SEGTYPE=S1, $
    FIELDNAME=UNITS, ALIAS=E01, USAGE=I08, ACTUAL=I04, $
    FIELDNAME=TOTDOLL, ALIAS=E02, USAGE=I08, ACTUAL=I04, $
    FIELDNAME=MAXDOLL, ALIAS=E03, USAGE=I08, ACTUAL=I04, $
    FIELDNAME=MINDOLL, ALIAS=E04, USAGE=I08, ACTUAL=I04, $

Using this Master File, you can use either field names or alias names. Also note that in an
ON TABLE MERGE request, the ON TABLE SET ASNAMES ON command is not needed in
order for the AS names to be propagated to the HOLD Master File.

When an ON TABLE MERGE request is optimized, an SQL request is generated and passed
to the DBMS. For example, the following request is optimized when the dminv and dmrpts
tables use the same adapter and connection:

544

8. Saving and Reusing Your Report Output

TABLE FILE dminv
PRINT
 PROD_NUM
 COMPUTE QUANTITY =  SUM.QTY_IN_STOCK;
 COMPUTE LINEPRICE =  SUM.PRICE;
 COMPUTE LINECOST = SUM.COST;
 COMPUTE LINECOGS = LINECOST * QUANTITY
ON TABLE MERGE INTO FILE dmrpts
MATCHING TRG.PROD_NUM EQ SRC.PROD_NUM;
 WHEN MATCHED UPDATE
  YRMTH=TRG.YRMTH + 1;
  QUANTITY=SRC.QUANTITY;
  LINEPRICE=SRC.LINEPRICE;
  LINECOGS=SRC.LINECOGS;
  PROFIT=SRC.LINECOGS - SRC.LINECOST;

 WHEN NOT MATCHED INSERT
  STORE_CODE='1004NY';
  PROD_NUM=SRC.PROD_NUM;
  YRMTH=202101;
  QUANTITY=SRC.QUANTITY;
  LINEPRICE=SRC.LINEPRICE;
  LINECOGS=SRC.LINECOGS;
  PROFIT=SRC.LINECOGS - SRC.LINECOST;
END

The following messages indicate that the request was optimized.

(FOC2659) FULL OPTIMIZATION OF MERGE WITH SUBSELECT HAS BEEN DONE
(FOC2661) TARGET FILE ibisamp/dmrpts

(FOC2665) MERGE PROCESS STARTED AT 15.33.19
(FOC1796) ROWS AFFECTED BY MERGE STATEMENT: 182

You can open the Session Log from the User Options menu on the Web Console title bar.
The Session Log shows that the following SQL request was generated.

SELECT
  T1."PROD_NUM" AS "E01",
  T1."QTY_IN_STOCK" AS "E02",
  T1."PRICE" AS "E03",
  T1."COST" AS "E04",
  (T1."COST" * T1."QTY_IN_STOCK") AS "E05",
  '1004NY' AS "E06",
  202101 AS "E07",
  T1."QTY_IN_STOCK" AS "E08",
  ((T1."COST" * T1."QTY_IN_STOCK") - T1."COST") AS "E09"
   FROM
  dminv T1;

Creating Reports With TIBCO® WebFOCUS Language

 545


Merging Data Into an Existing Data Source With ON TABLE MERGE

MERGE INTO dmrpts AS T3
  USING ( SELECT
  T1."PROD_NUM" AS "E01",
  T1."QTY_IN_STOCK" AS "E02",
  T1."PRICE" AS "E03",
  T1."COST" AS "E04",
  (T1."COST" * T1."QTY_IN_STOCK") AS "E05",
  '1004NY' AS "E06",
  202101 AS "E07",
  T1."QTY_IN_STOCK" AS "E08",
  ((T1."COST" * T1."QTY_IN_STOCK") - T1."COST") AS "E09"
   FROM
  dminv T1) T2
  ON
  (T3."PROD_NUM" =
  T2."E01")

 WHEN MATCHED THEN UPDATE SET
  "YRMTH" = ("YRMTH" + 1),
  "QUANTITY" =
  T2."E08",
  "LINEPRICE" =
  T2."E03",
  "LINECOGS" =
  T2."E05",
  "PROFIT" =
  T2."E09"

WHEN NOT MATCHED THEN INSERT (
  "PROD_NUM",
  "STORE_CODE",
  "YRMTH",
  "QUANTITY",
  "LINEPRICE",
  "LINECOGS",
  "PROFIT")
  VALUES (
  T2."E01",
  T2."E06",
  T2."E07",
  T2."E08",
  T2."E03",
  T2."E05",
  T2."E09");

546

8. Saving and Reusing Your Report Output

Example:

Using Alias Names With ON TABLE MERGE

The following request uses alias names from the source HOLD file in the expressions used to
insert fields into the target file.

TABLE FILE dminv
PRINT
   PROD_NUM
   COMPUTE YM = 202102;
   COMPUTE QUANTITY = QTY_IN_STOCK;
   COMPUTE LINEPRICE = PRICE;
   COMPUTE LINECOGS = LINEPRICE * QUANTITY;
ON TABLE MERGE INTO FILE ibisamp/dmrpts
 INSERT
  STORE_CODE='AAAA';
  PROD_NUM=SRC.E01;
  YRMTH=SRC.E02;
  QUANTITY=SRC.E03;
  LINEPRICE=SRC.E04;
  LINECOGS=SRC.E05;
  PROFIT=SRC.E04 - SRC.E05;
END

Using Text Fields in Output Files

Text fields can be propagated to HOLD and SAVE files that have the following formats: ALPHA,
WP, and FOCUS or XFOCUS. However, although a Master File is generated for format ALPHA,
you cannot issue a TABLE request against a HOLD file of format ALPHA that contains text
fields.

Reference: Rules for Text Fields in Output Files

You can include as many text fields in the file as needed. However, you must specify text
fields after non-text fields in the display list (PRINT..., SUM..., and so forth).

You can specify only one text field in the display list, and no non-text fields, in a request
that includes an ACROSS phrase.

The following rules apply to missing data for text fields in HOLD and SAVE files:

A blank line is valid data. An end-of-text mark indicates the end of the field.

If there is no text for a field, a single period (.) followed by blanks appears in the HOLD or
SAVE file.

If MISSING=ON during data extraction, a period (.) is written out to the HOLD or SAVE file.

If MISSING=OFF during data extraction, a blank is written out to the HOLD or SAVE file.

See Handling Records With Missing Field Values on page 1035.

Creating Reports With TIBCO® WebFOCUS Language

 547

Using Text Fields in Output Files

In environments that support FIXFORM, due to limitations in the use of text fields with
FIXFORM, the following restriction applies:

When you use the command FIXFORM FROM HOLD, the HOLD file may not contain more
than one text field, and the text field must be the last field in the Master File.

When HOLD files are read using FIXFORM, the interpretation of missing text depends on
whether the field's designation is MISSING=ON in the Master File, conditional ©) in the
FIXFORM format description, or some combination of the two.

Example:

Applying Text Field Rules in HOLD Files

The following request extracts data to a HOLD file named CRSEHOLD:

TABLE FILE COURSE
PRINT COURSECODE DESCRIPTN1
ON TABLE HOLD AS CRSEHOLD
END

The following request prints the data from the HOLD file:

TABLE FILE CRSEHOLD
PRINT *
END

The partial output is:

COURSECODE

DESCRIPTN1

AMA130

AMA680

AMA800

BIT420

BIT640

BIT650

EDP090

EDP130

EDP390

EDP690

EDP750

MC230

MC90

FOR PROJECT LEADERS AND SYS ANALYSTS.

FOR INDUSTRIAL MARKETERS.

FOR MANAGERS AND HUMAN RESOURCE STAFF.

FOR SENIOR MANAGERS. ANALYZE AND IMPROVE

FOR ADMINISTRATOR OF LABOR CONTRACTS.

FOR PROGRAMMERS, PROJECT LEADERS AND

FOR PRODUCTION MANAGERS. TO DELEGATE AND

FOR PROGRAMMERS, PROJECT LEADERS AND

FOR MANAGERS. HELP APPLY MANAGERIAL

FOR EXEC MANAGERS AND MKTG RESEARCH

FOR MARKETING MANAGERS. ENABLE TO

FOR PROGRAMMERS, PROJECT LEADERS AND

FOR VICE PRES OF SALES AND MARKETING.

548

8. Saving and Reusing Your Report Output

NAMA40

NAMA730

NAMA930

PDR330

PDR740

PDR870

PU168

PU440

SFC280
  .
  .
  .

FOR MARKETING VICE PRES AND MANAGERS.

FOR MANAGERS OF SALESPEOPLE. TO ENHANCE

FOR FINANCIAL MANAGERS. EXPLORE CONCEPTS

FOR EXECUTIVE SECRETARIES. TO KNOW THE

FOR EXPERIENCED MARKETING MANAGERS. HELP

FOR DESIGNERS AND TRAINING COORDINATORS.

FOR MARKETING, PRODUCT, ADVERTISING

FOR GENERAL MANAGERS. TO EXPLORE

FOR MANAGERS AND SECRETARIES. HELP

Creating a Delimited Sequential File

You can use the HOLD FORMAT DFIX command to create an alphanumeric sequential file
delimited by any character or combination of characters. You can also specify whether to
enclose alphanumeric values in quotation marks or some other enclosure, whether to include a
header record that lists the names of the fields, whether to preserve leading and trailing blank
spaces in alphanumeric data, and whether to insert a delimiter between records in the
resulting file. (Note that when RDELIMITER is included, the RECFM is UB).

A Master File and an Access File are created to describe the delimited sequential file that is
generated. The SUFFIX value in the Master File is DFIX. The Access File specifies the delimiter,
the enclosure character (if any), whether to preserve leading and trailing blank spaces in
alphanumeric data, whether there is a header record, and the record delimiter, if there is to be
one. The Master and Access Files are useful if you will later read the sequential file using
WebFOCUS.

Syntax:

How to Create a Delimited Sequential File

ON TABLE {HOLD|PCHOLD} [AS filename] FORMAT DFIX
 DELIMITER delimiter
 [ENCLOSURE enclosure] [HEADER {YES|NO}]
 [PRESERVESPACE {YES|NO}]  [RDELIMITER rdelimiter]

where:

filename

Is the name of the file to be created. If you do not specify a name, the default name is
HOLD.

Creating Reports With TIBCO® WebFOCUS Language

 549

Creating a Delimited Sequential File

delimiter

Is the delimiter sequence consisting of up to 30 printable or non-printable non-null
characters. This represents character semantics. For example, if you are using DBCS
characters, the delimiter can be up to 60 bytes. Characters may also be represented by
their 0x hex values which is the required specification method for non-printable characters.
If you use a mixture of printable and non-printable characters, you must enter them all as
hexadecimal values. To create a tab delimited file, you can specify the DELIMITER value as
TAB or as its hexadecimal equivalent (0x09 on ASCII platforms or 0x05 on EBCDIC
platforms). To create a single-quote delimited file, you must specify the single quote
DELIMITER value as its hexadecimal equivalent (0x27 on ASCII platforms or 0x7D on
EBCDIC platforms), otherwise the request will be mis-interpreted and result in an unusable
HOLD file.

enclosure

Is the enclosure sequence. It can be up to four printable or non-printable characters used
to enclose each alphanumeric value in the file. This represents character semantics. For
example, if you are using DBCS characters, the enclosure can be up to 8 bytes. Most
alphanumeric characters can be used as all or part of the enclosure sequence. However,
numeric digits and symbols used in numbers, such as a period (.), plus sign (+), or minus
sign (-) cannot be used in the enclosure sequence. Also note that, in order to specify a
single quotation mark as the enclosure character, you must enter four consecutive single
quotation marks. The most common enclosure is one double quotation mark.

If you use a mixture of printable and non-printable characters, you must enter them all as
hexadecimal values. For printable characters, you can either use the characters
themselves or their hexadecimal equivalents (for example, the ampersand character may
be interpreted as the beginning of a variable name rather than as part of the enclosure.)

HEADER {YES|NO}

Specifies whether to include a header record that contains the names of the fields in
the delimited sequential file generated by the request.

PRESERVESPACE {YES|NO}

Specifies whether to retain leading and trailing blanks in alphanumeric data. YES
preserves leading and trailing blanks. NO only preserves leading and trailing blanks that
are included within the enclosure characters. NO is the default value.

Note: PRESERVESPACE is overridden by the ENCLOSURE option. Therefore, exclude the
enclosure option in order to have the PRESERVESPACE setting respected.

550

8. Saving and Reusing Your Report Output

rdelimiter

Is the record delimiter sequence consisting of up to 30 printable or non-printable non-null
characters. This represents character semantics. For example, if you are using DBCS
characters, the delimiter can be up to 60 bytes. For a non-printable character, enter the
hexadecimal value that represents the character. If you use a mixture of printable and non-
printable characters, you must enter them all as hexadecimal values. For printable
characters you can either use the characters themselves or their hexadecimal equivalents
(for example, the ampersand character may be interpreted as the beginning of a variable
name rather than as part of the delimiter). To use a tab character as the record delimiter,
you can specify the delimiter value as TAB or as its hexadecimal equivalent (0x09 on ASCII
platforms or 0x05 on EBCDIC platforms). The comma (,) is not supported as a record
delimiter.

Note that numeric digits and symbols used in numbers, such as a period (.), plus sign (+),
or minus sign (-) cannot be used in the delimiter sequence. When RDELIMITER is included,
the RECFM is UB.

Reference: Usage Notes for HOLD FORMAT DFIX

Missing data is indicated by no data. So, with enclosure, a missing alphanumeric field is
indicated by two enclosure characters, while a missing numeric field is indicated by two
delimiters.

Text fields are not supported with HOLD FORMAT DFIX.

While HOLD FORMAT DFIX creates a single segment file, you can manually add segments to
the resulting Master and Access File. In the Access File, you can specify a separate
delimiter and/or enclosure for each segment.

The extension of the generated sequential file is ftm.

HOLD FORMAT DFIX with the PRESERVESPACE YES option creates a file in which leading
and trailing blank spaces are preserved in alphanumeric data. It also adds the attribute
PRESERVESPACE=YES in the Access File. This attribute causes leading and trailing blank
spaces to be preserved when reading a FORMAT DFIX file.

Creating Reports With TIBCO® WebFOCUS Language

 551

Creating a Delimited Sequential File

Example:

Creating a Pipe-Delimited File

The following request against the CENTORD data source creates a sequential file named PIPE1
with fields separated by the pipe character (|). Alphanumeric values are not enclosed in
quotation marks, and there is no header record:

TABLE FILE CENTORD
SUM QUANTITY LINEPRICE BY REGION BY YEAR
ON TABLE HOLD AS PIPE1 FORMAT DFIX DELIMITER |
END

The PIPE1 Master File specifies the SUFFIX value as DFIX:

FILENAME=PIPE1   , SUFFIX=DFIX    , $
  SEGMENT=PIPE1, SEGTYPE=S2, $
    FIELDNAME=REGION, ALIAS=E01, USAGE=A5, ACTUAL=A05, $
    FIELDNAME=YEAR, ALIAS=E02, USAGE=YY, ACTUAL=A04, $
    FIELDNAME=QUANTITY, ALIAS=E03, USAGE=I8C, ACTUAL=A08, $
    FIELDNAME=LINEPRICE, ALIAS=E04, USAGE=D12.2MC, ACTUAL=A12, $

The PIPE1 Access File specifies the delimiter:

SEGNAME=PIPE1, DELIMITER=|, HEADER=NO, $

The PIPE1 sequential file contains the following data. Each data value is separated from the
next value by a pipe character:

EAST|2000|3907|1145655.77
EAST|2001|495922|127004359.88
EAST|2002|543678|137470917.05
NORTH|2001|337168|85750735.54
NORTH|2002|370031|92609802.80
SOUTH|2000|3141|852550.45
SOUTH|2001|393155|99822662.88
SOUTH|2002|431575|107858412.0
WEST|2001|155252|39167974.18
WEST|2002|170421|42339953.45

The following version of the HOLD command specifies both the delimiter and an enclosure
character (“):

ON TABLE HOLD AS PIPE1 FORMAT DFIX DELIMITER | ENCLOSURE "

The Master File remains the same, but the Access File now specifies the enclosure character:

SEGNAME=PIPE1, DELIMITER=|, ENCLOSURE=", HEADER=NO, $

552

8. Saving and Reusing Your Report Output

In the delimited file that is created, each data value is separated from the next by a pipe
character, and alphanumeric values are enclosed within double quotation marks:

"EAST"|2000|3907|1145655.77
"EAST"|2001|495922|127004359.88
"EAST"|2002|543678|137470917.05
"NORTH"|2001|337168|85750735.54
"NORTH"|2002|370031|92609802.80
"SOUTH"|2000|3141|852550.45
"SOUTH"|2001|393155|99822662.88
"SOUTH"|2002|431575|107858412.01
"WEST"|2001|155252|39167974.18
"WEST"|2002|170421|42339953.45

This version of the HOLD command adds a header record to the generated file:

ON TABLE HOLD AS PIPE1 FORMAT DFIX DELIMITER |  ENCLOSURE "  HEADER YES

The Master File remains the same, but the Access File now specifies that the generated
sequential file should contain a header record with column names as its first record:

SEGNAME=PIPE1, DELIMITER=|, ENCLOSURE=", HEADER=YES, $

In the delimited file that is created, each data value is separated from the next by a pipe
character, and alphanumeric values are enclosed within double quotation marks. The first
record contains the column names:

"REGION"|"YEAR"|"QUANTITY"|"LINEPRICE"
"EAST"|2000|3907|1145655.77
"EAST"|2001|495922|127004359.88
"EAST"|2002|543678|137470917.05
"NORTH"|2001|337168|85750735.54
"NORTH"|2002|370031|92609802.80
"SOUTH"|2000|3141|852550.45
"SOUTH"|2001|393155|99822662.88
"SOUTH"|2002|431575|107858412.01
"WEST"|2001|155252|39167974.18
"WEST"|2002|170421|42339953.45

Example:

Creating a Tab-Delimited File

The following request against the CENTORD data source creates a sequential file named TAB1
with fields separated by a tab character:

TABLE FILE CENTORD
SUM QUANTITY LINEPRICE BY REGION BY YEAR
ON TABLE HOLD AS TAB1 FORMAT DFIX DELIMITER TAB
END

Creating Reports With TIBCO® WebFOCUS Language

 553

Creating a Delimited Sequential File

As the tab character is not printable, the TAB1 Access File specifies the delimiter using its
hexadecimal value.

The following is the Access File in an EBCDIC environment:

SEGNAME=TAB1, DELIMITER=0x05, HEADER=NO, $

The following is the Access File in an ASCII environment:

SEGNAME=TAB1, DELIMITER=0x09, HEADER=NO, $

Example:

Creating a Delimited File With Blank Spaces Preserved

The following request against the GGSALES data source creates a comma-delimited file. The
original alphanumeric data has trailing blank spaces. The PRESERVESPACE YES option in the
HOLD command preserves these trailing blank spaces:

APP HOLDDATA APP1
APP HOLDMETA APP1
TABLE FILE GGSALES
SUM DOLLARS UNITS
BY REGION
BY CATEGORY
BY PRODUCT
ON TABLE HOLD AS DFIX1 FORMAT DFIX DELIMITER , PRESERVESPACE YES
END

The following Master File is generated:

FILENAME=DFIX1   , SUFFIX=DFIX    , $
  SEGMENT=DFIX1, SEGTYPE=S3, $
    FIELDNAME=REGION, ALIAS=E01, USAGE=A11, ACTUAL=A11, $
    FIELDNAME=CATEGORY, ALIAS=E02, USAGE=A11, ACTUAL=A11, $
    FIELDNAME=PRODUCT, ALIAS=E03, USAGE=A16, ACTUAL=A16, $
    FIELDNAME=DOLLARS, ALIAS=E04, USAGE=I08, ACTUAL=A08, $
    FIELDNAME=UNITS, ALIAS=E05, USAGE=I08, ACTUAL=A08, $

The following Access File is generated:

SEGNAME=DFIX1, DELIMITER=',', HEADER=NO, PRESERVESPACE=YES, $

554

8. Saving and Reusing Your Report Output

In the DFIX1 file, the alphanumeric fields contain all of the blank spaces that existed in the
original file:

Midwest    ,Coffee     ,Espresso        ,1294947,101154
Midwest    ,Coffee     ,Latte           ,2883566,231623
Midwest    ,Food       ,Biscotti        ,1091727,86105
Midwest    ,Food       ,Croissant       ,1751124,139182
Midwest    ,Food       ,Scone           ,1495420,116127
Midwest    ,Gifts      ,Coffee Grinder  ,619154,50393
Midwest    ,Gifts      ,Coffee Pot      ,599878,47156
Midwest    ,Gifts      ,Mug             ,1086943,86718
Midwest    ,Gifts      ,Thermos         ,577906,46587
Northeast  ,Coffee     ,Capuccino       ,542095,44785
Northeast  ,Coffee     ,Espresso        ,850107,68127
Northeast  ,Coffee     ,Latte           ,2771815,222866
Northeast  ,Food       ,Biscotti        ,1802005,145242
Northeast  ,Food       ,Croissant       ,1670818,137394
Northeast  ,Food       ,Scone           ,907171,70732
Northeast  ,Gifts      ,Coffee Grinder  ,509200,40977
Northeast  ,Gifts      ,Coffee Pot      ,590780,46185
Northeast  ,Gifts      ,Mug             ,1144211,91497
Northeast  ,Gifts      ,Thermos         ,604098,48870
Southeast  ,Coffee     ,Capuccino       ,944000,73264
Southeast  ,Coffee     ,Espresso        ,853572,68030
Southeast  ,Coffee     ,Latte           ,2617836,209654
Southeast  ,Food       ,Biscotti        ,1505717,119594
Southeast  ,Food       ,Croissant       ,1902359,156456
Southeast  ,Food       ,Scone           ,900655,73779
Southeast  ,Gifts      ,Coffee Grinder  ,605777,47083
Southeast  ,Gifts      ,Coffee Pot      ,645303,49922
Southeast  ,Gifts      ,Mug             ,1102703,88474
Southeast  ,Gifts      ,Thermos         ,632457,48976
West       ,Coffee     ,Capuccino       ,895495,71168
West       ,Coffee     ,Espresso        ,907617,71675
West       ,Coffee     ,Latte           ,2670405,213920
West       ,Food       ,Biscotti        ,863868,70436
West       ,Food       ,Croissant       ,2425601,197022
West       ,Food       ,Scone           ,912868,72776
West       ,Gifts      ,Coffee Grinder  ,603436,48081
West       ,Gifts      ,Coffee Pot      ,613624,47432
West       ,Gifts      ,Mug             ,1188664,93881
West       ,Gifts      ,Thermos         ,571368,45648

Creating Reports With TIBCO® WebFOCUS Language

 555

Creating a Delimited Sequential File

Creating the same file with PRESERVESPACE NO removes the trailing blank spaces:

Midwest,Coffee,Espresso,1294947,101154
Midwest,Coffee,Latte,2883566,231623
Midwest,Food,Biscotti,1091727,86105
Midwest,Food,Croissant,1751124,139182
Midwest,Food,Scone,1495420,116127
Midwest,Gifts,Coffee Grinder,619154,50393
Midwest,Gifts,Coffee Pot,599878,47156
Midwest,Gifts,Mug,1086943,86718
Midwest,Gifts,Thermos,577906,46587
Northeast,Coffee,Capuccino,542095,44785
Northeast,Coffee,Espresso,850107,68127
Northeast,Coffee,Latte,2771815,222866
Northeast,Food,Biscotti,1802005,145242
Northeast,Food,Croissant,1670818,137394
Northeast,Food,Scone,907171,70732
Northeast,Gifts,Coffee Grinder,509200,40977
Northeast,Gifts,Coffee Pot,590780,46185
Northeast,Gifts,Mug,1144211,91497
Northeast,Gifts,Thermos,604098,48870
Southeast,Coffee,Capuccino,944000,73264
Southeast,Coffee,Espresso,853572,68030
Southeast,Coffee,Latte,2617836,209654
Southeast,Food,Biscotti,1505717,119594
Southeast,Food,Croissant,1902359,156456
Southeast,Food,Scone,900655,73779
Southeast,Gifts,Coffee Grinder,605777,47083
Southeast,Gifts,Coffee Pot,645303,49922
Southeast,Gifts,Mug,1102703,88474
Southeast,Gifts,Thermos,632457,48976
West,Coffee,Capuccino,895495,71168
West,Coffee,Espresso,907617,71675
West,Coffee,Latte,2670405,213920
West,Food,Biscotti,863868,70436
West,Food,Croissant,2425601,197022
West,Food,Scone,912868,72776
West,Gifts,Coffee Grinder,603436,48081
West,Gifts,Coffee Pot,613624,47432
West,Gifts,Mug,1188664,93881
West,Gifts,Thermos,571368,45648

Example:

Specifying a Record Delimiter

The following request against the GGSALES data source, the field delimiter is a comma, the
enclosure character is a single quotation mark, and the record delimiter consists of both
printable and non-printable characters, so it is specified as the following hexadecimal
sequence:

0x: character sequence identifying the delimiter as hexadecimal character codes.

2C: hexadecimal value for comma (,).

556

8. Saving and Reusing Your Report Output

24: hexadecimal value for dollar sign ($).

0D: hexadecimal value for carriage return.

0A: hexadecimal value for new line.

TABLE FILE GGSALES
PRINT DOLLARS UNITS CATEGORY REGION
ON TABLE HOLD AS RDELIM1 FORMAT DFIX DELIMITER , ENCLOSURE ''''
HEADER NO RDELIMITER 0x2C240D0A
END

The generated Master File follows:

FILENAME=RDELIM1 , SUFFIX=DFIX    , $
  SEGMENT=RDELIM1, SEGTYPE=S0, $
    FIELDNAME=DOLLARS, ALIAS=E01, USAGE=I08, ACTUAL=A08, $
    FIELDNAME=UNITS, ALIAS=E02, USAGE=I08, ACTUAL=A08, $
    FIELDNAME=CATEGORY, ALIAS=E03, USAGE=A11, ACTUAL=A11, $
    FIELDNAME=REGION, ALIAS=E04, USAGE=A11, ACTUAL=A11, $

The Access File contains the delimiters and enclosure characters:

SEGNAME=RDELIM1,
  DELIMITER=',',
  ENCLOSURE='''',
  HEADER=NO,
  RDELIMITER=0x2C240D0A,
  PRESERVESPACE=NO, $

Each row of the resulting DFIX file ends with the comma-dollar combination and a carriage
return and line space. a partial listing follows:

20805,1387,'Coffee','Northeast',$
20748,1729,'Coffee','Northeast',$
20376,1698,'Coffee','Northeast',$
20028,1669,'Coffee','Northeast',$
19905,1327,'Coffee','Northeast',$
19470,1770,'Coffee','Northeast',$
19118,1738,'Coffee','Northeast',$
18720,1560,'Coffee','Northeast',$
18432,1536,'Coffee','Northeast',$
17985,1199,'Coffee','Northeast',$
17630,1763,'Coffee','Northeast',$
16646,1189,'Coffee','Northeast',$
15650,1565,'Coffee','Northeast',$
15450,1545,'Coffee','Northeast',$
15435,1029,'Coffee','Northeast',$
14270,1427,'Coffee','Northeast',$

Creating Reports With TIBCO® WebFOCUS Language

 557

Saving Report Output in INTERNAL Format

Example: Missing Data in the HOLD File

The following request against the CENTORD data source creates missing alphanumeric and
numeric values in the resulting comma-delimited HOLD file:

DEFINE FILE CENTORD
AREA/A5 MISSING ON = IF REGION EQ 'EAST' THEN MISSING ELSE REGION;
MQUANTITY/I9 MISSING ON = IF REGION EQ 'WEST' THEN MISSING ELSE 200;
END

TABLE FILE CENTORD
SUM QUANTITY MQUANTITY LINEPRICE BY AREA BY YEAR
WHERE AREA NE 'NORTH' OR 'SOUTH'
  ON TABLE HOLD AS MISS1 FORMAT DFIX DELIMITER , ENCLOSURE "
END

In the MISS1 HOLD file, the missing alphanumeric values are indicated by two enclosure
characters in a row ("") and the missing numeric values are indicated by two delimiters in a
row (,,):

"",2000,3907,600,1145655.77
"",2001,495922,343000,127004359.88
"",2002,543678,343000,137470917.05
"WEST",2001,155252,,39167974.18
"WEST",2002,170421,,42339953.45

Saving Report Output in INTERNAL Format

HOLD files pad binary integer and packed decimal data values to a full word boundary. For
example, a three-digit integer field (I3), is stored as four bytes in a HOLD file. In order for third
generation programs, such as COBOL, to be able to read HOLD files in an exact manner, you
may need to save the fields in the HOLD file without any padding.

To suppress field padding in the HOLD file, you must reformat the fields in the request in order
to override the default ACTUAL formats that correspond to the USAGE formats in the Master
File:

Reformat the integer and packed fields that you do not want to be padded in the HOLD file
to the correct display lengths.

Specify HOLD FORMAT INTERNAL for the report output.

558


8. Saving and Reusing Your Report Output

Syntax:

How to Suppress Field Padding in HOLD Files

SET HOLDLIST = PRINTONLY
TABLE FILE filename
display_command fieldname/[In|Pn.d]
.
.
ON TABLE HOLD AS name FORMAT INTERNAL
END

where:

PRINTONLY

Causes your report request to propagate the HOLD file with only the specified fields
displaying in the report output. If you do not issue this setting, an extra field
containing the padded field length is included in the HOLD file. See Controlling
Attributes in HOLD Master Files on page 484.

fieldname/[In|Pn.d]

Specify correct lengths in the formats for integer and packed fields where you wish to
suppress padding. These formats override the ACTUAL formats used for the display
formats in the Master File. See Usage Notes for Suppressing Padded Fields in HOLD
Files on page 560.

Note that floating point double-precision (D) and floating point single-precision (F) are not
affected by HOLD FORMAT INTERNAL.

FORMAT INTERNAL

Saves the HOLD file without padding for specified integer and packed decimal fields.

Creating Reports With TIBCO® WebFOCUS Language

 559

Saving Report Output in INTERNAL Format

Reference: Usage Notes for Suppressing Padded Fields in HOLD Files

Integer fields (I) of one, two, three, or four bytes produce four-byte integers without HOLD
FORMAT INTERNAL.

For packed decimal fields (Pn.d), n is the total number of digits and d is the number of
digits to the right of the decimal point. The number of bytes is derived by dividing n by 2
and adding 1.

The syntax is

bytes = INT (n/2) + 1

where:

INT (n/2)

Is the greatest integer after dividing by 2.

HOLD FORMAT INTERNAL does not affect floating point double-precision (D) and floating
point single-precision (F) fields. D remains at eight bytes, and F at four bytes.

Alphanumeric fields automatically inherit their length from their source Master File, and are
not padded to a full word boundary.

If a format override is not large enough to contain the data values, the values are
truncated. Truncation may cause the data in the HOLD file to be incorrect in the case of an
integer. For packed data and integers, truncation occurs for the high order digits so the
remaining low order digits resemble the digits from the correct values.

To avoid incorrect results, be sure that the format you specify is large enough to contain
the data values.

If you use the HOLDMISS=ON setting to propagate missing values to the HOLD file, short
packed fields and fields with formats I1, I2, and I3 are not large enough to hold the missing
value.

Example:

Creating a HOLD File Without HOLD FORMAT INTERNAL

In this example, the values of ACTUAL for RETAIL_COST, DEALER_COST, and SEATS are all
padded to a full word. Alphanumeric fields also occupy full words.

TABLE FILE CAR
PRINT CAR COUNTRY RETAIL_COST DEALER_COST SEATS
ON TABLE HOLD AS DJG
END

560

8. Saving and Reusing Your Report Output

The request creates the following Master File:

FILE=DJG, SUFFIX=FIX
 SEGMENT=DJG, SEGTYPE=S0
  FIELDNAME=CAR          ,ALIAS=E01  ,USAGE=A16  ,ACTUAL=A16    ,$
  FIELDNAME=COUNTRY      ,ALIAS=E02  ,USAGE=A10  ,ACTUAL=A12    ,$
  FIELDNAME=RETAIL_COST  ,ALIAS=E03  ,USAGE=D7   ,ACTUAL=D08    ,$
  FIELDNAME=DEALER_COST  ,ALIAS=E04  ,USAGE=D7   ,ACTUAL=D08    ,$
  FIELDNAME=SEATS        ,ALIAS=E05  ,USAGE=I3   ,ACTUAL=I04    ,$

Example:

Creating a HOLD File With HOLD FORMAT INTERNAL

In this example, DEALER_COST and RETAIL_COST are defined in the Master File as D fields,
but the request overrides RETAIL_COST as an I2 field and DEALER_COST as a P3 field.

SET HOLDLIST=PRINTONLY
TABLE FILE CAR
PRINT CAR COUNTRY RETAIL_COST/I2 DEALER_COST/P3 SEATS/I1
ON TABLE HOLD AS HINT3 FORMAT INTERNAL
END

This creates the following Master File:

FILE=HINT3, SUFFIX=FIX
 SEGMENT=HINT3, SEGTYPE=S0
  FIELDNAME=CAR          ,ALIAS=E01   ,USAGE=A16  ,ACTUAL=A16   ,$
  FIELDNAME=COUNTRY      ,ALIAS=E02   ,USAGE=A10  ,ACTUAL=A10   ,$
  FIELDNAME=RETAIL_COST  ,ALIAS=E03   ,USAGE=I6   ,ACTUAL=I02   ,$
  FIELDNAME=DEALER_COST  ,ALIAS=E04   ,USAGE=P4   ,ACTUAL=P02   ,$
  FIELDNAME=SEATS        ,ALIAS=E05   ,USAGE=I4   ,ACTUAL=I01   ,$

The ACTUAL formats for the overridden fields are I2, P2, and I1. DEALER_COST has an ACTUAL
of P2 because P3, the format override, means 3 display digits that can be stored in 2 actual
digits. Note that the alphanumeric field is also not padded.

Creating A Subquery or Sequential File With HOLD FORMAT SQL_SCRIPT

When used in a request against a relational data source, the HOLD FORMAT SQL_SCRIPT
command generates the SQL SELECT statement needed to execute the current query and
stores it in the application folder as a file with a .sql extension along with the Master and
Access File pair that describes the SQL answer set.

When used in a request against any other type of data source, the HOLD FORMAT SQL_SCRIPT
command executes the current query and stores the retrieved values in the application folder
as a sequential file with a .ftm extension along with the Master File that describes the
retrieved data.

You can use the output from HOLD FORMAT SQL_SCRIPT as the target file for the DB_INFILE
function. For information about the DB_INFILE function, see the Using Functions manual.

Creating Reports With TIBCO® WebFOCUS Language

 561

Creating A Subquery or Sequential File With HOLD FORMAT SQL_SCRIPT

Note: Once you have the .sql file and its accompanying Master File, you can customize the .sql
file using global Dialogue Manager variables. You must declare these global variables in the
Master File. For information about parameterizing Master Files with global variables, see the
Describing Data With WebFOCUS Language manual.

Syntax:

How to Create an SQL Script or Sequential File Using HOLD FORMAT SQL_SCRIPT

ON TABLE HOLD AS script_name FORMAT SQL_SCRIPT

where:

script_name

Is the name of the .sql file or the .ftm file created as a result of the HOLD FORMAT
SQL_SCRIPT command.

Example:

Creating an SQL Script File Using HOLD FORMAT SQL_SCRIPT

The following request against the WF_RETAIL relational data source creates an SQL Script file
in the baseapp application:

APP HOLD baseapp
TABLE FILE WF_RETAIL_LITE
SUM BUSINESS_REGION STATE_PROV_CODE_ISO_3166_2
BY BUSINESS_REGION NOPRINT BY STATE_PROV_CODE_ISO_3166_2 NOPRINT
WHERE BUSINESS_REGION EQ 'North America' OR 'EMEA'
WHERE STATE_PROV_CODE_ISO_3166_2 EQ 'AR' OR 'IA' OR 'KS' OR 'KY' OR 'WY' OR
'CT' OR 'MA' OR '04' OR '11' OR '14'
OR 'NJ' OR 'NY' OR 'RI'
ON TABLE HOLD AS RETAIL_SCRIPT FORMAT SQL_SCRIPT
END

WF_RETAIL is a sample data source you can create by right-clicking an application on the
Reporting Server Web Console and selecting New and then Samples from the context menu.

The result of this request is a script file named retail_script.sql and a corresponding Master
and Access File.

The retail_script.sql file contains the following SQL SELECT statement:

 SELECT      MAX(T3."BUSINESS_REGION") AS "VB001_MAX_BUSINESS_REGION",
MAX(T3."STATE_PROV_CODE_ISO_3166_2")
AS "VB002_MAX_STATE_PROV_CODE_ISO_"     FROM     wrd_wf_retail_geography
T3
WHERE     (T3."STATE_PROV_CODE_ISO_3166_2" IN('AR', 'IA', 'KS', 'KY', 'WY',
'CT', 'MA', '04', '11', '14', 'NJ', 'NY', 'RI'))
AND     (T3."BUSINESS_REGION" IN('North America', 'EMEA'))     GROUP BY
T3."BUSINESS_REGION",    T3."STATE_PROV_CODE_ISO_3166_2"

562

8. Saving and Reusing Your Report Output

The retail_script.mas Master File follows:

FILENAME=RETAIL_SCRIPT, SUFFIX=MSODBC  , $
  SEGMENT=RETAIL_SCRIPT, SEGTYPE=S0, $
    FIELDNAME=BUSINESS_REGION, ALIAS=VB001_MAX_BUSINESS_REGION, USAGE=A15V,
ACTUAL=A15V,
      MISSING=ON,
      TITLE='Customer,Business,Region', $
    FIELDNAME=STATE_PROV_CODE_ISO_3166_2,
ALIAS=VB002_MAX_STATE_PROV_CODE_ISO_, USAGE=A5V, ACTUAL=A5V,
      MISSING=ON,
      TITLE='Customer,State,Province,ISO-3166-2,Code', $

The retail_script.acx Access File follows:

SEGNAME=RETAIL_SCRIPT,
   CONNECTION=CON01,
   DATASET=RETAIL_SCRIPT.SQL,
   SUBQUERY=Y, $

Example:

Creating a Sequential File Using HOLD FORMAT SQL_SCRIPT

The following request against the EMPLOYEE data source creates a sequential file containing
the values retrieved by the request along with a corresponding Master File:

APP HOLD baseapp
TABLE FILE EMPLOYEE
PRINT LAST_NAME FIRST_NAME
WHERE DEPARTMENT EQ 'MIS'
ON TABLE HOLD AS EMPVALUES FORMAT SQL_SCRIPT
END

The sequential file empvalues.ftm contains the following data:

SMITH           MARY        JONES           DIANE       MCCOY
JOHN        BLACKWOOD       ROSEMARIE   GREENSPAN       MARY
CROSS           BARBARA

The empvalues.mas Master File follows:

FILENAME=EMPVALUES, SUFFIX=DATREC  , IOTYPE=BINARY, $
  SEGMENT=EMPVALUE, SEGTYPE=S0, $
    FIELDNAME=LAST_NAME, ALIAS=E01, USAGE=A15, ACTUAL=A15, $
    FIELDNAME=FIRST_NAME, ALIAS=E02, USAGE=A10, ACTUAL=A10, $
    FIELDNAME=NULLFLAG, ALIAS=__NULLFLAG__, USAGE=A2, ACTUAL=A2B,
ACCESS_PROPERTY=(INTERNAL), $

Creating a Structured HOLD File

Structured HOLD Files facilitate migration of data sources and reports between operating
environments.

Creating Reports With TIBCO® WebFOCUS Language

 563

Creating a Structured HOLD File

Other HOLD formats capture data from the original sources and may retain some implicit
structural elements from the request itself. However, they do not propagate most of the
information about the original data sources accessed and their inter-relationships to the HOLD
Master File or data source. Structured HOLD files, however, extract the data to a structure that
parallels the original data sources. Subsequent requests against the HOLD file can use these
retained data relationships to recreate the same types of relationships in other environments
or in other types of data sources.

A Structured HOLD File can be created in ALPHA, BINARY, or FOCUS format:

A Structured HOLD file created in either ALPHA or BINARY format is a flat file that saves the
segment instances that contain the data that satisfy the conditions of the TABLE request.
Multiple segments are generated based on the original structure read by the TABLE
request. Segments are identified by assigning a RECTYPE for differentiation. Child
segments in the original data source become a unique segment in the HOLD file

A Structured HOLD file in FOCUS format uses normal FOCUS segments to retain the original
structure.

In all cases the HOLD file contains all of the original segment instances required to provide the
complete report based on the TABLE request itself. Regardless of the display command used
in the original request (PRINT, LIST, SUM, COUNT), the Structured HOLD File is created as if
the request used PRINT. Aggregation is ignored.

The HOLD file contains either all of the fields in the structure identified by the request that are
used to satisfy the request, or all of the display fields and BY fields. The file does not contain
DEFINE fields not specifically referenced in the request. It does contain all fields needed to
evaluate any DEFINE fields referenced in the request.

Structured HOLD files are only supported for TABLE and TABLEF commands. They can be
created anywhere a HOLD file is supported. You must activate Structured HOLD files in a
specific request by issuing the ON TABLE SET EXTRACT command in the request prior to
creating the Structured HOLD File.

Syntax:

How to Activate Structured HOLD Files for a Request

ON TABLE SET EXTRACT {ON|*|OFF}

where:

ON

Activates Structured HOLD Files for this request and extracts all fields mentioned in
the request.

564

8. Saving and Reusing Your Report Output

*

OFF

Activates Structured HOLD Files for this request and indicates that a block of extract
options follows. For example, you can exclude specific fields from the Structured
HOLD File. For information, see How to Specify Options for Generating Structured HOLD
Files on page 565.

Deactivates Structured HOLD files for this request. OFF is the default value.

Syntax:

How to Create a Structured HOLD File

Before issuing the HOLD command, activate Structured HOLD Files for the request by issuing
the ON TABLE SET EXTRACT command described in How to Activate Structured HOLD Files for a
Request on page 564. Then issue the HOLD command to create the Structured HOLD File:

[ON TABLE] {HOLD|PCHOLD} [AS name] FORMAT {ALPHA|BINARY|FOCUS}

where:

name

Is the name of the HOLD file. If omitted, the name becomes HOLD by default.

FORMAT

Is ALPHA, BINARY or FOCUS.

Note: You can issue a SET command to set the default HOLD format to either ALPHA or
BINARY:

SET HOLDFORMAT=ALPHA
SET HOLDFORMAT=BINARY

Syntax:

How to Specify Options for Generating Structured HOLD Files

To specify options for creating the extract, such excluding specific fields, use the * option of
the SET EXTRACT command:

ON TABLE SET EXTRACT *
EXCLUDE = (fieldname1, fieldname2, fieldname3 , ..., fieldnamen),$
FIELDS={ALL|EXPLICIT},$
ENDEXTRACT
ON TABLE HOLD AS name FORMAT {ALPHA|BINARY|FOCUS}

where:

EXCLUDE=(fieldname1, fieldname2, fieldname3,..., fieldnamen)

Excludes the specified fields from the HOLD file.

,$

Is required syntax for delimiting elements in the extract block.

Creating Reports With TIBCO® WebFOCUS Language

 565

Creating a Structured HOLD File

ALL

Includes all real fields and all DEFINE fields that are used in running the request.

EXPLICIT

Includes only those real fields and DEFINE fields that are in the display list or the BY
sort field listing. DEFINE fields that are not explicitly referenced, and fields that are
used to evaluate DEFINEs, are not included.

ENDEXTRACT

Ends the extract block.

Example:

Creating a Structured HOLD File in ALPHA Format

TABLE FILE EMPLOYEE
PRINT LAST_NAME FIRST_NAME JOBCODE ED_HRS
BY DEPARTMENT
BY HIGHEST SALARY
ON TABLE SET EXTRACT ON
ON TABLE HOLD FORMAT ALPHA
END

This request produces the following HOLD Master File:

FILENAME=HOLD    , SUFFIX=FIX     , $
  SEGMENT=EMPINFO, SEGTYPE=S0, $
    FIELDNAME=RECTYPE, ALIAS=R, USAGE=A3, ACTUAL=A3, $
    FIELDNAME=LAST_NAME, ALIAS='LN', USAGE=A15, ACTUAL=A15, $
    FIELDNAME=FIRST_NAME, ALIAS='FN', USAGE=A10, ACTUAL=A10, $
    FIELDNAME=DEPARTMENT, ALIAS='DPT', USAGE=A10, ACTUAL=A10, $
    FIELDNAME=ED_HRS, ALIAS='OJT', USAGE=F6.2, ACTUAL=A06, $
  SEGMENT=PAYINFO, SEGTYPE=S0, PARENT=EMPINFO, $
    FIELDNAME=RECTYPE, ALIAS=1, USAGE=A3, ACTUAL=A3, $
    FIELDNAME=SALARY, ALIAS='SAL', USAGE=D12.2M, ACTUAL=A12, $
    FIELDNAME=JOBCODE, ALIAS='JBC', USAGE=A3, ACTUAL=A03, $

Note the RECTYPE field generated for ALPHA or BINARY Structured HOLD files. Each record in
the HOLD file begins with the RECTYPE to indicate the segment to which it belonged in the
original structure. The root segment has RECTYPE=R. The RECTYPEs for other segments are
sequential numbers assigned in top to bottom, left to right order.

566

8. Saving and Reusing Your Report Output

Following are the first several records in the HOLD file:

R  STEVENS        ALFRED    PRODUCTION 25.00
1      11000.00A07
1      10000.00A07
R  SMITH          MARY      MIS        36.00
1      13200.00B14
R  JONES          DIANE     MIS        50.00
1      18480.00B03
1      17750.00B02
R  SMITH          RICHARD   PRODUCTION 10.00
1       9500.00A01
1       9050.00B01

Example:

Creating a Structured HOLD File in FOCUS Format

TABLE FILE EMPLOYEE
PRINT LAST_NAME FIRST_NAME JOBCODE ED_HRS
BY DEPARTMENT
BY HIGHEST SALARY
ON TABLE SET EXTRACT ON
ON TABLE HOLD FORMAT FOCUS
END

This request produces the following HOLD Master File:

FILENAME=HOLD    , SUFFIX=FOC     , $
  SEGMENT=EMPINFO, SEGTYPE=S0, $
    FIELDNAME=LAST_NAME, ALIAS='LN', USAGE=A15, $
    FIELDNAME=FIRST_NAME, ALIAS='FN', USAGE=A10, $
    FIELDNAME=DEPARTMENT, ALIAS='DPT', USAGE=A10, $
    FIELDNAME=ED_HRS, ALIAS='OJT', USAGE=F6.2, $
  SEGMENT=PAYINFO, SEGTYPE=S0, PARENT=EMPINFO, $
    FIELDNAME=SALARY, ALIAS='SAL', USAGE=D12.2M, $
    FIELDNAME=JOBCODE, ALIAS='JBC', USAGE=A3, $

Example:

Reconstituting a Structured HOLD File

The following request reconstitutes the original FOCUS data source from the Structured HOLD
File created in the example named Creating a Structured HOLD File in ALPHA Format:

TABLE FILE HOLD
PRINT LAST_NAME FIRST_NAME JOBCODE ED_HRS
BY DEPARTMENT
BY HIGHEST SALARY
ON TABLE SET EXTRACT ON
ON TABLE HOLD AS RECONST FORMAT FOCUS
END

Creating Reports With TIBCO® WebFOCUS Language

 567

Creating a Structured HOLD File

This request produces the following Master File:

FILENAME=RECONST    , SUFFIX=FOC     , $
  SEGMENT=EMPINFO, SEGTYPE=S0, $
    FIELDNAME=LAST_NAME, ALIAS='LN', USAGE=A15, $
    FIELDNAME=FIRST_NAME, ALIAS='FN', USAGE=A10, $
    FIELDNAME=DEPARTMENT, ALIAS='DPT', USAGE=A10,
    FIELDNAME=ED_HRS, ALIAS='OJT', USAGE=F6.2, $
  SEGMENT=PAYINFO, SEGTYPE=S0, PARENT=EMPINFO, $
    FIELDNAME=SALARY, ALIAS='SAL', USAGE=D12.2M, $
    FIELDNAME=JOBCODE, ALIAS='JBC', USAGE=A3, $

The following request prints the report output:

TABLE FILE RECONST
PRINT LAST_NAME FIRST_NAME JOBCODE ED_HRS
BY DEPARTMENT
BY HIGHEST SALARY
END

The output is:

DEPARTMENT           SALARY  LAST_NAME        FIRST_NAME  JOBCODE  ED_HRS
----------           ------  ---------        ----------  -------  ------
MIS              $27,062.00  CROSS            BARBARA     A17       45.00
                 $25,775.00  CROSS            BARBARA     A16       45.00
                 $21,780.00  BLACKWOOD        ROSEMARIE   B04       75.00
                 $18,480.00  JONES            DIANE       B03       50.00
                             MCCOY            JOHN        B02         .00
                 $17,750.00  JONES            DIANE       B02       50.00
                 $13,200.00  SMITH            MARY        B14       36.00
                  $9,000.00  GREENSPAN        MARY        A07       25.00
                  $8,650.00  GREENSPAN        MARY        B01       25.00
PRODUCTION       $29,700.00  BANNING          JOHN        A17         .00
                 $26,862.00  IRVING           JOAN        A15       30.00
                 $24,420.00  IRVING           JOAN        A14       30.00
                 $21,120.00  ROMANS           ANTHONY     B04        5.00
                 $16,100.00  MCKNIGHT         ROGER       B02       50.00
                 $15,000.00  MCKNIGHT         ROGER       B02       50.00
                 $11,000.00  STEVENS          ALFRED      A07       25.00
                 $10,000.00  STEVENS          ALFRED      A07       25.00
                  $9,500.00  SMITH            RICHARD     A01       10.00
                  $9,050.00  SMITH            RICHARD     B01       10.00

568

8. Saving and Reusing Your Report Output

Example:

Excluding Fields From Structured HOLD Files

This request excludes the SALARY field used for sequencing.

TABLE FILE EMPLOYEE
PRINT LAST_NAME FIRST_NAME JOBCODE ED_HRS
BY DEPARTMENT
BY HIGHEST SALARY
ON TABLE SET EXTRACT *
EXCLUDE=(SALARY),$
ENDEXTRACT
ON TABLE HOLD FORMAT FOCUS
END

This request produces the following HOLD Master File:

FILENAME=HOLD   , SUFFIX=FOC     , $
  SEGMENT=EMPINFO, SEGTYPE=S0, $
    FIELDNAME=LAST_NAME, ALIAS='LN', USAGE=A15, $
    FIELDNAME=FIRST_NAME, ALIAS='FN', USAGE=A10, $
    FIELDNAME=DEPARTMENT, ALIAS='DPT', USAGE=A10, $
    FIELDNAME=ED_HRS, ALIAS='OJT', USAGE=F6.2, $
  SEGMENT=PAYINFO, SEGTYPE=S0, PARENT=EMPINFO, $
    FIELDNAME=JOBCODE, ALIAS='JBC', USAGE=A3, $

Reference: Elements Included in a Structured HOLD File

Structured HOLD files contain all original segment instances required to complete the TABLE or
TABLEF request. Regardless of the display command used in the original request (PRINT, LIST,
SUM, or COUNT), the structured HOLD file will be created as if the command was PRINT.

Specifically, the extract file contains the following elements:

All real fields named in the request such as display objects, sort fields, and fields used in
selection criteria (WHERE/IF tests).

Note that fields referenced multiple times in a request are included only once in the HOLD
file.

Fields used in FILTER FILE condition.

Prefix operators are ignored except for ALL. (which just affects the amount of data collected
and does not imply a calculation).

Field based reformatting (FIELD1/FIELD2=) causes the original field and the format field to
be included.

Creating Reports With TIBCO® WebFOCUS Language

 569

Creating a Structured HOLD File

A GROUP field if referenced explicitly or when all of its members are referenced in the
request.

Note: If a group member is specifically excluded (EXCLUDE) or not referenced, its GROUP is
not added to the extract Master File (this applies to nested and overlapping groups, as
well). If a GROUP and its elements are all named in a request, the GROUP is not added as
a real field in the extract HOLD file.

For FIELDS=ALL, all DEFINE fields used in the request become real fields in the structured
HOLD File and are included along with other fields used in the DEFINE expression (including
other DEFINE fields). Use EXCLUDE to reduce the number of fields included in the EXTRACT
output.

For FIELDS=EXPLICIT, display objects and sort fields are included. DEFINE fields become
real fields if referenced in the request, but fields used to create them will not be included
unless referenced explicitly. This reduces the number of fields returned in the request.

Reference: Elements Not Included in a Structured HOLD File

Prefix operators on WHERE fields are evaluated in data selection but not included in the
extract output.

Prefix operators on display objects are ignored (except ALL).

Using Structured HOLD File syntax in MATCH, MORE, and GRAPH requests produces error
messages and exits the procedure.

WHERE/IF TOTAL tests are not supported in Structured HOLD File requests and result in
cancellation of the request.

Reformatting of real fields is ignored (only the real field is included).

Computed fields are not included, but fields used in COMPUTE expressions are included in
the extract file.

Reference: Structural and Behavioral Notes

Structured HOLD File requests are subject to the same limitations on number and size of
fields as any other TABLE request.

570

8. Saving and Reusing Your Report Output

Structural Notes

The following SET parameters are turned off or ignored in Structured HOLD File requests:

AUTOINDEX

AUTOPATH

AUTOSTRATEGY

EXTHOLD

EXTSORT

HOLDATTR

All SET and ON TABLE SET commands used to control output format are ignored in
creating the extract file.

Alternate views are respected and reflected in the structure of the extract file.

Indexed views specified in the request are respected and reflected in the structure of the
output file.

If a request would generate a file containing two independent orphan segments because
the parent segment is specifically excluded, a dummy system segment is created in the to
act as parent of the two unrelated segments. There is only one instance of data for that
segment. Both orphan segments refer to that system segment as parent. If the parent is
missing because it was not mentioned in the request, it is activated during the request and
included as the parent the segments.

In the event that two unique (U) segments are included without the parent segment, the
unique segments are converted to segments with SEGTYPE S0 that reference the system
segment as parent.

JOIN and JOIN WHERE structures are supported.

SQL Optimization Notes

SQL optimization for aggregation must be turned off for EXTRACT requests.

BY/ACROSS/FOR Notes

BY and ACROSS sort fields become additional display objects.

BY. . .ROWS and ACROSS . . .COLUMNS function only as implicit WHEREs to limit field
values included.

Creating Reports With TIBCO® WebFOCUS Language

 571

Creating a Structured HOLD File

FOR fields are included.

RECAP fields are excluded (like COMPUTEs).

Summarization fields referencing previously identified fields are ignored in creating
Structured HOLD Files. These include: SUMMARIZE, RECOMPUTE, SUBTOTAL, SUB-TOTAL
ACROSS-TOTAL, ROW-TOTAL and COLUMN-TOTAL.

Formatting Notes

Structured HOLD File processing ignores all formatting elements, including: IN, OVER,
NOPRINT, SUP-PRINT, FOLD-LINE, SKIP-LINE, UNDER-LINE, PAGE-BREAK, TABPAGENO, AS,
and column title justification. However, fields referenced within formatting commands, such
as HEADING, FOOTING, SUBHEAD, and SUBFOOT, and any WHEN expressions associated
with them, are included.

All STYLE and STYLESHEET commands are ignored in producing extract output.

AnV and AnW fields are supported. TX fields are exported in FOCUS files only.

In the event that the FIELDNAME and ALIAS are the same for a real field and that field is
redefined as itself (possibly with a different format), two fields are created in the HOLD
Master File with identical field names and aliases. In this situation, the second version of
the field can never be accessed if referenced by name. You can use FIELDS=EXPLICIT to
include only the second version of the field. The following DEFINE illustrates and example of
creating a duplicate field name and alias:

DEFINE FILE CAR
COUNTRY/A25=COUNTRY;
END

DBA Notes

DBA controls on source files are respected when running Structured HOLD File requests
with the exception of RESTRICT=NOPRINT, where fields named in a request are not
displayed (such fields cannot be exported and should be specifically EXCLUDED).

DBA restrictions do not carry over to the HOLD Master File.

Reconstituting Extract Files

To reconstitute a FOCUS or flat file from a Structured HOLD file, you use the same syntax
used to generate the Structured HOLD File. The ON TABLE SET EXTRACT syntax must be
used to preserve multipath structures.

572

8. Saving and Reusing Your Report Output

All reconstituted FOCUS segments are SEGTYPE=S0, as neither KEY nor INDEX information
is retained. An INDEX can be reinserted using REBUILD INDEX.

Creating Reports With TIBCO® WebFOCUS Language

 573

Creating a Structured HOLD File

574

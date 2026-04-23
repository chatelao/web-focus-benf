Chapter2

Identifying a Data Source

In order to interpret data, your application needs to know the name you are using to
identify the data source and what type of data source it is. For example, is it a DB2 data
source, a Teradata data source, or a FOCUS data source?

In this chapter:

Identifying a Data Source Overview

Specifying a Data Source Name: FILENAME

Identifying a Data Source Type: SUFFIX

Specifying a Code Page in a Master File

Specifying Byte Order

Specifying Data Type: IOTYPE

Providing Descriptive Information for a Data Source: REMARKS

Specifying a Physical File Name: DATASET

Creating and Using a Master File Profile

Storing Localized Metadata in Language Files

Identifying a Data Source Overview

In a Master File, you identify the name and the type of data source in a data source
declaration. A data source declaration can include the following attributes:

FILENAME, which identifies the name of the data source.

SUFFIX, which identifies the type of data source.

REMARKS, which allows you to provide descriptive information about the data source for
display in graphical tools.

ACCESSFILE, which identifies the name of the optional Access File for a FOCUS data
source. See Describing a FOCUS Data Source on page 293.

DATASET, which identifies the physical file name if your data source has a non-standard
name.

Describing Data With TIBCO WebFOCUS® Language

 31

Specifying a Data Source Name: FILENAME

You can identify a Master File profile (MFD_PROFILE) procedure to run during Master File
processing. For more information, see Creating and Using a Master File Profile on page 46.

You can optionally specify a sliding date window that assigns a century value to dates stored
with two-digit years, using these data source attributes:

FDEFCENT, which identifies the century.

FYRTHRESH, which identifies the year.

Specifying a Data Source Name: FILENAME

The FILENAME attribute specifies the name of the data source described by the Master File.
This is the first attribute specified in a Master File. You can abbreviate the FILENAME attribute
to FILE.

Note: You can encrypt a Master File using the ENCRYPT command described in Hiding
Restriction Rules: The ENCRYPT Command on page 436. However, the first line of a Master
File that is going to be encrypted cannot be longer than 68 characters. If it is longer than 68
characters, you must break it up onto multiple lines.

Syntax:

How to Specify a Data Source Name

FILE[NAME] = data_source_name

where:

data_source_name

Is the name of the data source that the Master File describes. The name can be a
maximum of 64 characters.

The file name must contain at least one alphabetic character, and the remaining
characters can be any combination of letters, numbers, and underscores (_). The file name
must start with an alphabetic character on z/OS.

Example:

Specifying a Data Source Name

The following example specifies the data source name EMPLOYEE:

FILENAME = EMPLOYEE

Identifying a Data Source Type: SUFFIX

The SUFFIX attribute identifies the type of data source you are using. For example, a DB2 data
source or a FOCUS data source. Based on the value of SUFFIX, the appropriate data adapter is
used to access the data source.

32

2. Identifying a Data Source

The SUFFIX attribute is required for most types of data sources. It is optional for a fixed-format
sequential data source. However, if you refer to a fixed-format sequential data source in a JOIN
command, then the SUFFIX attribute must be declared in the Master File.

Note: Maintain Data does not support the following suffixes: BWBAPI, COMT, DBASE, FPA,
SQLSAP, SOAP, TABT, XML, and XFOCUS.

Syntax:

How to Identify a Data Source Type

SUFFIX = data_source_type

where:

data_source_type

Indicates the type of data source or the name of a customized data access module. The
default value is FIX, which represents a fixed-format sequential data source.

Example:

Specifying the Type for a FOCUS Data Source

The following example specifies the data source type FOC, representing a FOCUS data source
which has 4K database pages:

SUFFIX = FOC

The following example specifies the data source type XFOCUS, representing an XFOCUS data
source which has 16K database pages:

SUFFIX = XFOCUS

Reference: SUFFIX Values

The following table indicates the SUFFIX value for many of the supported data source types:

Data Source Type

SUFFIX Value

ADABAS

ALLBASE/SQL

CA-Datacom/DB

CA-IDMS/DB

ADBSIN or ADBSINX

SQLALB or ALLBASE

DATACOM

IDMSR

Describing Data With TIBCO WebFOCUS® Language

 33

Identifying a Data Source Type: SUFFIX

Data Source Type

SUFFIX Value

CA-IDMS/SQL

C-ISAM

DB2

DB2/2

DB2/400

DB2/6000

DBMS

DMS

SQLIDMS

C-ISAM

DB2 or SQLDS

SQLDBM

SQL400 (SQL access)

DBFILE (native access)

DB2

DBMS

VSAM (keyed access)

FIX (non-keyed access)

Digital Standard MUMPS

Enscribe

DSM

ENSC

Fixed-format sequential

FIX This value is the default.

PRIVATE (for FOCSAM user exit)

FOCUS

FOC

Free-format (also known as
comma-delimited) sequential

COM, COMMA, COMT

Image/SQL

IMS

INFOAccess

Information/Management

IMAGE

IMS

SQLIAX

INFOMAN

34

Data Source Type

SUFFIX Value

2. Identifying a Data Source

Informix

Ingres

KSAM

Micronetics Standard MUMPS

Model 204

Native Interface

NETISAM

NOMAD

NonStop SQL

Nucleus

ODBC

OpenIngres

Open M/SQL

Oracle

PACE

Progress

Rdb

Red Brick

RMS

SQLINF

SQLING

KSAM

MSM

M204IN

SQLSAP

C-ISAM

NMDIN

NSSQL

SQLNUC

SQLODBC

SQLING

SQLMSQ

SQLORA

VSAM

SQLPRO

SQLRDB

SQLRED

RMS

Describing Data With TIBCO WebFOCUS® Language

 35

Specifying a Code Page in a Master File

Data Source Type

SUFFIX Value

SQL/DS

SQL Server

StorHouse

Sybase

Tab Delimited

Teradata

Token Delimited

TurboIMAGE

Unify

uniVerse

VSAM

SQLDS

SQLMSS

SQLSTH

SQLSYB

TABT, TAB

SQLDBC

DFIX

IMAGE

OMNIDEX (using OMNIDEX IMS indices)

SQLUNIFY

UNIVERSE

VSAM

Non-standard data source

Name of the customized data access routine

PRIVATE (for FOCSAM user exit)

Specifying a Code Page in a Master File

The FILE declaration in a Master File can specify the code page to be used to retrieve the data
in that file. If the file is included as a segment in a cluster join, having the code page specified
ensures that the data from that segment is retrieved using the correct code page even if the
FILE declaration for the cluster specifies a different code page or defaults to the default code
page.

Syntax:

How to Specify a Code Page for a Master File

CODEPAGE = codepage

36

2. Identifying a Data Source

where:

codepage

Is the code page to use to read the file.

Specifying Byte Order

Operating environments differ in whether the most-significant or least-significant byte is
ordered first when storing numeric data. Ordering the most significant byte first is called big-
endian (BE), and ordering the least significant byte first is called small-endian (SE).

You may need to specify the byte order in the Master File if you are reading data from a
different operating environment.

Syntax:

How to Specify Byte Order

BYTEORDER={BE|SE}

where:

BE

Specifies that the most significant byte is ordered first. Hardware using this order includes
IBM zSeries and POWER.

SE

Specifies that the least significant byte is ordered first, also called reverse byte. Hardware
using this order includes Intel x86, x86-64, and DEC Alpha.

Specifying Data Type: IOTYPE

IOTYPE is generated when a HOLD file is created to tell WebFOCUS how to read the data file in
the absence of LRECL/RECFM information from a FILEDEF or allocation. It indicates the type of
data that was included in the file when the hold file was created. It is only recommended for
Master Files generated automatically as a result of a HOLD command. The values can be:

BINARY. Numeric data is stored in binary format in the generated file.

STREAM. All data in the generated file is in alphanumeric format.

IOTYPE applies only to the following HOLD formats:

FORMAT

SUFFIX

ALPHA

FIX

IOTYPE

STREAM

Describing Data With TIBCO WebFOCUS® Language

 37

Providing Descriptive Information for a Data Source: REMARKS

FORMAT

SUFFIX

BINARY

INTERNAL

no format

FIX

FIX

FIX

IOTYPE

BINARY

BINARY

Depends on the HOLDFORMAT parameter. If
HOLDFORMAT is:

BINARY, then IOTYPE is BINARY.

ALPHA, then IOTYPE is STREAM.

Providing Descriptive Information for a Data Source: REMARKS

The optional REMARKS attribute provides descriptive information about the data source. This
descriptive information appears in graphical tools.

You can also include descriptive information as a comment following a $ symbol in the Master
File. For more information, see Understanding a Data Source Description on page 17. These
descriptions, however, are useful only for those who view the Master File source code. They do
not appear in graphical tools.

Master Files support REMARKS and DESCRIPTION attributes in multiple languages. For
information, see Using Multilingual Descriptions in a Master File on page 198.

Syntax:

How to Document a Data Source

REMARKS = 'descriptive_text'

where:

descriptive_text

Is descriptive information about the data source. The text can be a maximum of 2K
characters long and must be enclosed within single quotation marks.

The descriptive text cannot span more than one line in the Master File. If necessary, place
the entire REMARKS attribute on a line by itself. For longer descriptions, break the
declaration into lines with the descriptive text on a line by itself.

Example:

Providing Descriptive Information for an Oracle Table

The following example shows the data source declaration for the Oracle table ORDERS. The
data source declaration includes descriptive information about the table.

38

2. Identifying a Data Source

FILENAME=ORDERS, SUFFIX=SQLORA,
REMARKS='This Oracle table tracks daily, weekly, and monthly orders.' ,$

Since the descriptive information would not fit on the same line as the other data source
attributes, the REMARKS attribute appears on a line by itself.

Specifying a Physical File Name: DATASET

You can add the DATASET attribute to the Master File to specify a physical location for the data
source to be allocated. In addition, the DATASET attribute permits you to bypass the search
mechanism for default data source location. DATASET eliminates the need to allocate data
sources using JCL, FILEDEF, DYNAM, and USE commands.

For UNIX, Windows, and OpenVMS, the user allocation command is FILEDEF.

For z/OS, the user allocation command is DYNAM ALLOC or TSO ALLOC.

DATASET can also be included in a HOLD command, which can include DATASET as one of its
options. The Master File generated by the HOLD command includes the DATASET attribute at
the file level. For information about the HOLD command, see the Creating Reports With
WebFOCUS Language manual.

Note: You cannot use both the ACCESSFILE attribute and the DATASET attribute in the same
Master File. For information on the ACCESSFILE attribute, see Describing a FOCUS Data Source
on page 293.

DATASET Behavior in a FOCUS Data Source

You can use the DATASET attribute on the file level of a FOCUS (including XFOCUS), fixed-
format sequential, or VSAM Master File. You can use the DATASET attribute on the segment
level of a FOCUS Master File. For information on specifying the DATASET attribute on the
segment level of a FOCUS Master File, see Describing a FOCUS Data Source on page 293.

If the Master File name is present in the USE list, or the user explicitly allocated the data file,
the DATASET attribute is ignored.

If DATASET is used in a Master File whose data source is managed by the FOCUS Database
Server, the DATASET attribute is ignored on the server side because the FOCUS Database
Server does not read Master Files for servicing table requests.

The DATASET attribute in the Master File has the lowest priority:

An explicit allocation of a user overrides the DATASET attribute if you first issue the
allocation command and then issue a CHECK FILE command to clear the previous DATASET
allocation.

Describing Data With TIBCO WebFOCUS® Language

 39

Specifying a Physical File Name: DATASET

The USE command for FOCUS data sources overrides DATASET attributes and explicit
allocations.

An alternative to the DATASET attribute for allocating FOCUS data sources is an Access File.
For detailed information, see Describing a FOCUS Data Source on page 293.

Note: If a DATASET allocation is in effect, a CHECK FILE command must be issued in order to
override it by an explicit allocation command. The CHECK FILE command will undo the
allocation created by DATASET.

Syntax:

How to Use the DATASET Attribute at the File Level

{DATASET|DATA}='filename [ON sinkname]'

In z/OS, the syntax is:

{DATASET|DATA}='qualifier.qualifier ...'

or

{DATASET|DATA}='ddname ON sinkname'

In UNIX, the syntax is:

{DATASET|DATA}='/filesystem/filename.foc [ON sinkname]'

In Windows, the syntax is:

{DATASET|DATA}='drive:\directory\filename.foc [ON sinkname]'

In OpenVMS, the syntax is:

{DATASET|DATA}='[device:[directory]]filename[.foc] [ON sinkname]'

where:

filename

Is the platform-dependent physical name of the data source.

sinkname

Indicates that the data source is located on the FOCUS Database Server. This attribute is
valid only for FOCUS or XFOCUS data sources.

40

Example:

Allocating a FOCUS Data Source Using the DATASET Attribute

The following example illustrates how to allocate a FOCUS data source using the DATASET
attribute.

2. Identifying a Data Source

For z/OS,

FILENAME=CAR,SUFFIX=FOC,
DATASET='USER1.CAR.FOCUS'
SEGNAME=ORIGIN,SEGTYPE=S1
FIELDNAME=COUNTRY,COUNTRY,A10,FIELDTYPE=I,$
SEGNAME=COMP,SEGTYPE=S1,PARENT=ORIGIN
FIELDNAME=CAR,CARS,A16,$
SEGNAME=CARREC,SEGTYPE=S1,PARENT=COMP
.
.
.

For UNIX,

FILENAME=CAR,SUFFIX=FOC,
DATASET='/filesystem/filename.foc'
SEGNAME=ORIGIN,SEGTYPE=S1
FIELDNAME=COUNTRY,COUNTRY,A10,FIELDTYPE=I,$
SEGNAME=COMP,SEGTYPE=S1,PARENT=ORIGIN
FIELDNAME=CAR,CARS,A16,$
SEGNAME=CARREC,SEGTYPE=S1,PARENT=COMP
.
.
.

For Windows,

FILENAME=CAR,SUFFIX=FOC,
DATASET='drive:\directory\filename.foc'
SEGNAME=ORIGIN,SEGTYPE=S1
FIELDNAME=COUNTRY,COUNTRY,A10,FIELDTYPE=I,$
SEGNAME=COMP,SEGTYPE=S1,PARENT=ORIGIN
FIELDNAME=CAR,CARS,A16,$
SEGNAME=CARREC,SEGTYPE=S1,PARENT=COMP
.
.
.

Describing Data With TIBCO WebFOCUS® Language

 41

Specifying a Physical File Name: DATASET

For OpenVMS,

FILENAME=CAR,SUFFIX=FOC,
DATASET='device:[directory]filename.foc' SEGNAME=ORIGIN,SEGTYPE=S1
FIELDNAME=COUNTRY,COUNTRY,A10,FIELDTYPE=I,$
SEGNAME=COMP,SEGTYPE=S1,PARENT=ORIGIN
FIELDNAME=CAR,CARS,A16,$
SEGNAME=CARREC,SEGTYPE=S1,PARENT=COMP
.
.
.

Example:

Allocating a Data Source for the FOCUS Database Server

The following example illustrates how to allocate a FOCUS data source with the DATASET
attribute using ON sink.

For z/OS,

FILENAME=CAR,SUFFIX=FOC,
DATASET='CAR ON SINK1'
SEGNAME=ORIGIN,SEGTYPE=S1
FIELDNAME=COUNTRY,COUNTRY,A10,FIELDTYPE=I,$
SEGNAME=COMP,SEGTYPE=S1,PARENT=ORIGIN
FIELDNAME=CAR,CARS,A16,$
SEGNAME=CARREC,SEGTYPE=S1,PARENT=COMP
.
.
.

Note: The ddname CAR is allocated by the FOCUS Database Server JCL.

For UNIX,

FILENAME=CAR,SUFFIX=FOC, DATASET='filename ON sink'
SEGNAME=ORIGIN,SEGTYPE=S1
FIELDNAME=COUNTRY,COUNTRY,A10,FIELDTYPE=I,$
SEGNAME=COMP,SEGTYPE=S1,PARENT=ORIGIN
FIELDNAME=CAR,CARS,A16,$
SEGNAME=CARREC,SEGTYPE=S1,PARENT=COMP
.
.
.

42

2. Identifying a Data Source

For Windows,

FILENAME=CAR,SUFFIX=FOC,
DATASET='filename ON sink'
SEGNAME=ORIGIN,SEGTYPE=S1
FIELDNAME=COUNTRY,COUNTRY,A10,FIELDTYPE=I,$
SEGNAME=COMP,SEGTYPE=S1,PARENT=ORIGIN
FIELDNAME=CAR,CARS,A16,$
SEGNAME=CARREC,SEGTYPE=S1,PARENT=COMP
.
.
.

For OpenVMS,

FILENAME=CAR,SUFFIX=FOC,
DATASET='filename ON sink'
SEGNAME=ORIGIN,SEGTYPE=S1
FIELDNAME=COUNTRY,COUNTRY,A10,FIELDTYPE=I,$
SEGNAME=COMP,SEGTYPE=S1,PARENT=ORIGIN
FIELDNAME=CAR,CARS,A16,$
SEGNAME=CARREC,SEGTYPE=S1,PARENT=COMP
.
.
.

DATASET Behavior in a Fixed-Format Sequential Data Source

The DATASET attribute for a fixed-format sequential file can be used only at the file declaration
level of the Master File and cannot contain ON sink. If the DATASET attribute contains ON sink,
a message is issued and the operation is terminated.

An explicit allocation of data for this Master File is checked for when the DATASET attribute is
detected. If an explicit allocation exists, the DATASET attribute is ignored. If this Master File
name is not allocated, an internal command is issued to perform the allocation. This allocation
is stored temporarily and is released when a new Master File is used or when the session
terminates.

There is a second parameter for DATASET, required for the UNIX, Windows, and OpenVMS
platforms, which when used with SUFFIX=FIX data sources, tells whether it contains binary or
text data. This parameter provides information on whether there are line break characters in
the data source. This distinguishes a text data source from a binary data source. The default is
binary.

Describing Data With TIBCO WebFOCUS® Language

 43

Specifying a Physical File Name: DATASET

Syntax:

How to Use the DATASET Attribute With a Fixed-Format Data Source

{DATASET|DATA}='filename {BINARY|TEXT}'

where:

filename

Is the platform-dependent physical name of the data source.

BINARY

Indicates that it is a binary data source. BINARY is the default value.

TEXT

Indicates that it is a text data source.

The DATASET attribute in the Master File has the lowest priority. An explicit allocation of a user
overrides DATASET attributes.

Note: If a DATASET allocation is in effect, a CHECK FILE command must be issued to override
it by an explicit allocation command. The CHECK FILE command deallocates the allocation
created by DATASET.

Example:

Allocating a Fixed-Format Data Source Using the DATASET Attribute

The following examples illustrate how to allocate a fixed-format data source using the DATASET
attribute.

For z/OS:

FILE=XX,  SUFFIX=FIX,  DATASET='USER1.SEQFILE1'
   .
   .
   .

For Windows:

FILE=XX,  SUFFIX=FIX,  DATASET='C:\DATA\FILENAME.FTM   TEXT'
   .
   .
   .

For UNIX:

FILE=XX,  SUFFIX=FIX,  DATASET='/u22/class/data/filename.ftm'
   .
   .
   .

For a binary data source:

44

2. Identifying a Data Source

FILE=XX,  SUFFIX=FIX,  DATASET='/u22/class/data/filename.ftm   BINARY'
   .
   .
   .

DATASET Behavior in a VSAM Data Source

The DATASET attribute for a VSAM data source can be used on the file declaration level of the
Master File and cannot contain ON sink. If the DATASET attribute contains ON sink, a message
is issued and the operation is terminated.

An explicit allocation of data for this Master File is checked for when the DATASET attribute is
detected. If an explicit allocation is found, the DATASET attribute is ignored. If this Master File
name is not allocated, an internal command is issued to perform the allocation. This allocation
is stored temporarily and is released when a new Master File is used or when the session
terminates.

The DATASET attribute may also appear on the field declaration level of the Master File to
specify where to find an alternate index. Because of VSAM naming conventions (names are
truncated to 8 characters), the name of the field alias will be used as the ddname. If a user
allocation is found for the Master File or alternate index ddname, the DATASET attribute is
ignored.

Note: There is no limit on how many alternate indices you may have. It is also acceptable for
some alternate indices to have the DATASET attribute while others do not. However, if a file
level DATASET attribute is missing, the field level DATASET will be ignored.

Syntax:

How to Use the DATASET Attribute With a VSAM, ISAM, or C-ISAM Data Source

{DATASET|DATA}='filename'

where:

filename

Is the platform-dependent physical name of the data source or alternate index.

The DATASET attribute in the Master File has the lowest priority. An explicit allocation of a user
overrides DATASET attributes.

Note: If a DATASET allocation is in effect, a CHECK FILE command must be issued in order to
override it by an explicit allocation command. The CHECK FILE command deallocates the
allocation created by DATASET.

Describing Data With TIBCO WebFOCUS® Language

 45


Creating and Using a Master File Profile

Example:

Allocating a VSAM Data Source Using the DATASET Attribute

The following example illustrates how to allocate a VSAM data source on the file declaration
level and for an alternate index:

FILE=EXERVSM1, SUFFIX=VSAM, DATASET='VSAM1.CLUSTER1',$
SEGNAME=ROOT , SEGTYPE=S0,$
 GROUP=KEY1  , ALIAS=KEY , FORMAT=A4, ACTUAL=A4 ,$
  FIELD=FLD1 , ALIAS=F1  , FORMAT=A4, ACTUAL=A4 ,$
  FIELD=FLD2 , ALIAS=F2  , FORMAT=A4, ACTUAL=A4 ,$
  FIELD=FLD3 , ALIAS=DD1 , FORMAT=A4, ACTUAL=A4 , FIELDTYPE = I ,
        DATASET='VSAM1.INDEX1' ,$
  FIELD=FLD4 , ALIAS=F4  , FORMAT=A4, ACTUAL=A4 ,$
  FIELD=FLD5 , ALIAS=F5  , FORMAT=A4, ACTUAL=A4 ,$
  FIELD=FLD6 , ALIAS=F6  , FORMAT=A4, ACTUAL=A4 ,$
  FIELD=FLD7 , ALIAS=F7  , FORMAT=A4, ACTUAL=A4 ,$

Example:

Allocating a C-ISAM Data Source Using the DATASET Attribute

The following example illustrates how to allocate a C-ISAM data source on the file declaration
level and for an alternate index:

FILENAME=EMPLOYEE, SUFFIX=CISAM ,
DATASET=/qa/edamvt/CISAM/employee, $
SEGMENT=SEG1, SEGTYPE=S0, $
GROUP=G5, ALIAS=KEY, ELEMENTS=1, $
FIELDNAME=EMPLOYEE_ID5, ALIAS=E3, USAGE=I11, ACTUAL=I4, $
FIELDNAME=SSN5, ALIAS=KEY1, USAGE=A11, ACTUAL=A11, FIELDTYPE=I,$
FIELDNAME=FILLER, ALIAS=E5, USAGE=A1, ACTUAL=A1, $
FIELDNAME=LAST_NAME5, ALIAS=E6, USAGE=A20, ACTUAL=A20, $
FIELDNAME=FIRST_NAME5, ALIAS=E7, USAGE=A15, ACTUAL=A15, $
FIELDNAME=FILLER, ALIAS=E8, USAGE=A1, ACTUAL=A1, $
FIELDNAME=BIRTHDATE5, ALIAS=E9, USAGE=I11, ACTUAL=I4, $
FIELDNAME=SEX5, ALIAS=E10, USAGE=A1, ACTUAL=A1, $
FIELDNAME=FILLER, ALIAS=E11, USAGE=A3, ACTUAL=A3, $
FIELDNAME=ETHNIC_GROU5, ALIAS=E12, USAGE=A15, ACTUAL=A15, $
FIELDNAME=FILLER, ALIAS=E13, USAGE=A1, ACTUAL=A1, $
FIELDNAME=STREET5, ALIAS=E14, USAGE=A20, ACTUAL=A20, $
FIELDNAME=CITY5, ALIAS=E15, USAGE=A15, ACTUAL=A15, $
FIELDNAME=FILLER, ALIAS=E16, USAGE=A1, ACTUAL=A1, $

Creating and Using a Master File Profile

This release introduces a profile that you can reference in the Master File and is executed
during Master File processing. The Master File profile (MFD_PROFILE) is a FOCEXEC that
suspends processing of the Master File for a request, executes, and then returns to
processing of the Master File. The profile can be used for many purposes but is especially
useful for:

Setting the values of global variables defined in the Master File.

46

2. Identifying a Data Source

Creating a lookup file for Master File DEFINE commands or DBA attributes.

Dynamically creating a DBA rule for the connected user by reading an external table of
entitlements.

Dynamically creating a DBAFILE, which can be derived from an external data source and
used to restrict access during execution of any request that references the Master File.

Note: You can also create a DBA rule dynamically in the Master File for a specific user
without having to create a DBAFILE with rules for all users.

Syntax:

How to Invoke a Master File Profile

Add the MFD_PROFILE attribute to the FILE declaration in the Master File:

FILE = filename, SUFFIX = suffix, MFD_PROFILE = app/fexname,$

where:

filename

Is any valid file name.

suffix

Is the suffix value that specifies the file type described by the Master File. MFD_PROFILE is
supported for any file type.

app

Is the name of the application containing the FOCEXEC to be executed. Specifying the
application name ensures that the correct version of the profile is executed, in case there
is another FOCEXEC with the same name higher on the application path.

fexname

Is the name of the MFD_PROFILE FOCEXEC.

Reference: Usage Notes for MFD_PROFILE

The MFD_PROFILE is executed for every TABLE, TABLEF, MATCH, GRAPH, CREATE, DEFINE,
CHECK, ?F, and ?FF request against a Master File that contains the MFD_PROFILE
attribute.

In a MATCH request or a request using MORE, all of the MFD_PROFILE procedures
specified in any of the Master Files involved in the request will be executed prior to the
request. The profiles will execute in the reverse of their order in the request (the profile for
the Master File mentioned last in the request executes first).

Describing Data With TIBCO WebFOCUS® Language

 47

Creating and Using a Master File Profile

The MFD_PROFILE is not executed as a result of the MODIFY, MAINTAIN, or -READFILE
commands.

The MFD_PROFILE is not executed when selecting segments or fields from the WebFOCUS
tools.

If multiple MFD_PROFILEs set values for the same global variables, the resulting variable
values will depend on the order in which the profile procedures run.

In a join between multiple Master Files that have MFD_PROFILE attributes, the profiles will
all be executed.

The name of the calling Master File is passed as the first parameter (&1) to the
MFD_PROFILE procedure.

If the MFD_PROFILE contains sensitive information, it should be encrypted. If it creates a
file (such as a DBAFILE) that contains sensitive information, that file should also be
encrypted.

Any file created by the MFD_PROFILE that will be used in conjunction with the calling Master
File must be on the application path, preferably as high on the path as possible. To ensure
that the file is deleted when the user logs off, you can place it in edatemp.

If the MFD_PROFILE is not on the application path, the following warning message will be
issued.

FOC(36373)  WARNING: MFD_PROFILE DOES NOT EXIST

If you want the lack of the profile to terminate processing, turn the ERROROUT parameter to
ON.

The MFD_PROFILE procedure should not issue a request against its calling Master File,
unless you add a counter to make sure it executes only once. Otherwise, an infinite loop
will result. If there is a reason why the MFD_PROFILE needs to execute a request against
itself, add a global Dialogue Manager variable as a counter to make sure it is executed only
once, as shown in the following sample.

-DEFAULT &&COUNTER=1;
-IF &&COUNTER EQ 1 THEN GOTO START;
-SET &&COUNTER= 2;
-GOTO DONE
-START
MFD_PROFILE request against same Master as original request END
-SET &&COUNTER=2;
-DONE

48

2. Identifying a Data Source

The first time the MFD_PROFILE is invoked, &&COUNTER is set to 1, so the part of the
MFD_PROFILE request that references the same Master File is executed, and &&COUNTER
is set to 2. Since executing this request references the Master with the MFD_PROFILE, it is
invoked again. However, since &&COUNTER will now be 2, the MFD_PROFILE request will
branch around the part that once again references the same Master File, preventing the
MFD_PROFILE from being invoked in an infinite loop.

A request against a Business View will invoke the MFD_PROFILE from the original Master
File.

If the MFD_PROFILE creates a DBAFILE, an initial DBAFILE specifying authorized users and
any restrictions at the SEGMENT or FIELD level must exist prior to using WebFOCUS tools
or commands other than TABLE, TABLEF, GRAPH or MATCH. The initial DBAFILE may be
created without VALUE restrictions. When the actual TABLE request runs, or you click Run
from a tool, the MFD_PROFILE procedure is executed, and VALUE restrictions are applied.

Be careful not to issue any command that affects the environment that was established
prior to executing the MFD_PROFILE. For example, if the MFD_PROFILE establishes any
joins that you want to clear before exiting the MFD_PROFILE, give those joins unique names
and issue a JOIN CLEAR command that clears only those joins. Do not issue the JOIN
CLEAR * command as that will clear any joins established prior to executing the
MFD_PROFILE.

Example:

Creating a Lookup File and Setting a Global Variable Using an MFD_PROFILE

The following version of the EMPDATA Master File:

Specifies an MFD_PROFILE named DDBAEMP.

Defines a variable to be used as the TITLE attribute for the PIN field.

Defines the fields TYPE_EMP and EMP_TYPE to classify employees as full-time or part-time
based on the values in the JOBS lookup file.

Has DBA restrictions. For user HR3, the VALUE clause does a lookup of values in the JOBS
lookup file.

Describing Data With TIBCO WebFOCUS® Language

 49

Creating and Using a Master File Profile

The edited EMPDATA Master File is

FILENAME=EMPDATA, SUFFIX=FOC, MFD_PROFILE=baseapp/DDBAEMP,$
VARIABLE NAME = Emptitle, USAGE=A30, DEFAULT=EMPID,$
SEGMENT=EMPDATA,SEGTYPE=S0, $
 FIELDNAME=PIN   , ALIAS=ID, USAGE=A9, INDEX=I,   TITLE='&&Emptitle',$
 FIELDNAME=LASTNAME,     ALIAS=LN,       FORMAT=A15,             $
 FIELDNAME=FIRSTNAME,    ALIAS=FN,       FORMAT=A10,             $
 FIELDNAME=MIDINITIAL,   ALIAS=MI,       FORMAT=A1,              $
 FIELDNAME=DIV,          ALIAS=CDIV,     FORMAT=A4,              $
 FIELDNAME=DEPT,         ALIAS=CDEPT,    FORMAT=A20,             $
 FIELDNAME=JOBCLASS,     ALIAS=CJCLAS,   FORMAT=A8,              $
 FIELDNAME=TITLE,        ALIAS=CFUNC,    FORMAT=A20,             $
 FIELDNAME=SALARY,       ALIAS=CSAL,     FORMAT=D12.2M,          $
 FIELDNAME=HIREDATE,     ALIAS=HDAT,     FORMAT=YMD,             $
$
DEFINE AREA/A13=DECODE DIV (NE 'NORTH EASTERN' SE 'SOUTH EASTERN'
CE 'CENTRAL' WE 'WESTERN' CORP 'CORPORATE' ELSE 'INVALID AREA');$
DEFINE TYPE_EMP/I1 = DECODE JOBCLASS(JOBS ELSE 1);,$
DEFINE EMP_TYPE/A10 = IF TYPE_EMP EQ 1
          THEN 'FULL_TIME'  ELSE 'PART_TIME';
END
DBA=USERD,$
USER=USER1,ACCESS=R,RESTRICT=FIELD,NAME=SALARY,$
USER=USER2,ACCESS=R,RESTRICT=VALUE,NAME=SYSTEM,
                VALUE=DEPT EQ SALES OR MARKETING,$
USER=HR1,ACCESS=R,RESTRICT=VALUE,NAME=SYSTEM,
            VALUE=SALARY FROM 20000 TO 35000,$
USER=HR2,ACCESS=R,RESTRICT=VALUE,NAME=EMPDATA,VALUE=SALARY GT 0,$
USER=HR3,ACCESS=R,RESTRICT=VALUE,NAME=SYSTEM,VALUE=JOBCLASS EQ (JOBS),$

The DDBAEMP procedure sets a value for the global variable &&Emptitle and creates the JOBS
lookup file:

FILEDEF JOBS DISK jobs.ftm

-RUN
-SET &&Emptitle = 'Employee ID';
TABLE FILE JOBLIST
PRINT JOBCLASS
WHERE JOBDESC  CONTAINS '2ND' OR '3RD'
ON TABLE HOLD AS JOBS
END

The following request against the EMPDATA data source allocates the JOBS file and sets the
user password to HR3. The EMP_TYPE field and the DBA VALUE restriction for user HR3 use
the JOBS file created by the MFD_PROFILE as a lookup table:

FILEDEF JOBS DISK jobs.ftm

50

2. Identifying a Data Source

-SET &PASS = 'HR3';
SET PASS = &PASS
-RUN
TABLE FILE EMPDATA
" Password used is &PASS "
" "
"USER1 -- Can't see Salary, reject request"
"USER2 -- Can see Sales and Marketing departments only"
"HR1   -- Can see salaries from 20 TO 35 K "
"HR2   -- Can see everyone "
"HR3   -- Can see Part Time only "
" "
PRINT PIN SALARY DEPT EMP_TYPE
ON TABLE SET PAGE NOPAGE
ON TABLE SET STYLE *
TYPE=REPORT, GRID=OFF, FONT=ARIAL,$
END

On the output, the column title for the PIN field is the value of the &&Emptitle variable set in
the MFD_PROFILE procedure, and the JOBS file created by the profile was used in limiting the
report output to Part Time employees, which are the only ones user HR3 is allowed to see:

Describing Data With TIBCO WebFOCUS® Language

 51

Creating and Using a Master File Profile

Example:

Creating a DBAFILE Using an MFD_PROFILE

The following version of the EMPDATA Master File specifies an MFD_PROFILE named DDEMP2
and a DBAFILE named DBAEMP2. The MFD_PROFILE will create the DBAFILE by reading
security attributes from a sequential file named security.data.

The Master File is:

FILENAME=EMPDATA, SUFFIX=FOC, MFD_PROFILE=baseapp/DDEMP2,$
SEGMENT=EMPDATA,SEGTYPE=S0, $
 FIELDNAME=PIN   , ALIAS=ID, USAGE=A9, INDEX=I,   TITLE='Employee Id',$
 FIELDNAME=LASTNAME,     ALIAS=LN,       FORMAT=A15,             $
 FIELDNAME=FIRSTNAME,    ALIAS=FN,       FORMAT=A10,             $
 FIELDNAME=MIDINITIAL,   ALIAS=MI,       FORMAT=A1,              $
 FIELDNAME=DIV,          ALIAS=CDIV,     FORMAT=A4,              $
 FIELDNAME=DEPT,         ALIAS=CDEPT,    FORMAT=A20,             $
 FIELDNAME=JOBCLASS,     ALIAS=CJCLAS,   FORMAT=A8,              $
 FIELDNAME=TITLE,        ALIAS=CFUNC,    FORMAT=A20,             $
 FIELDNAME=SALARY,       ALIAS=CSAL,     FORMAT=D12.2M,          $
 FIELDNAME=HIREDATE,     ALIAS=HDAT,     FORMAT=YMD,             $
$
DEFINE AREA/A13=DECODE DIV (NE 'NORTH EASTERN' SE 'SOUTH EASTERN'
CE 'CENTRAL' WE 'WESTERN' CORP 'CORPORATE' ELSE 'INVALID AREA');$
END
DBA=USERD,DBAFILE=DBAEMP2,$

The file with the security attributes (security.data) follows. The security attributes are the
USER, ACCESS, RESTRICT, NAME, and VALUE attributes:

USER1       R   NOPRINT     SALARY
USER2       R   VALUE       SYSTEM  DEPT EQ SALES OR MARKETING
HR1         R   VALUE       SYSTEM  SALARY FROM 20000 TO 35000
HR1         W   SEGMENT     EMPDATA
HR2         R   VALUE       EMPDATA SALARY GT 0

According to these attributes, a user with the password:

USER1 cannot print the values in the SALARY field.

USER2 can only see the SALES and MARKETING departments.

HR1 can only see salaries from 20000 to 35000. HR1 can also write to the EMPDATA
segment.

HR2 can see everything in the EMPDATA segment.

52

2. Identifying a Data Source

The DDEMP2 profile procedure:

Uses the Dialogue Manager command -WRITE to write records into the DBAEMP2 Master
File. It first writes the FILE declaration, a SEGMENT declaration, a FIELD declaration, the
END declaration that starts the DBA section of the Master File, and the DBA password
(which must be the same as the DBA password in the EMPDATA Master File). The
EDAEMP2 Master File will be written to edatemp.

The rest of the DBA section will be created by reading each record from the security.data
file and writing a corresponding DBA record to the DBAEMP2 Master File.

Uses the Master File name passed as argument &1 to write a FILE declaration for the
EMPDATA Master File, which will then be followed by the DBA declarations specific to that
Master File.

Loops to read each record in the security.data file using the Dialogue Manager command -
READFILE. It checks if there is a RESTRICT attribute and, if so, checks if it has a VALUE
attribute. Depending on which attributes are present, it writes a record to the DBAEMP2
Master File.

The DDEMP2 profile procedure follows:

-* FILEDEF the input security.data file (Windows)
FILEDEF SECURITY DISK c:\ibi\apps\baseapp\security.data (LRECL 81

-* DYNAM the output DBAEMP2 Master File and the input file (z/OS)
DYNAM OUTFI DA USER1.DBAEMP2.MASTER SHR REU
DYNAM SECURITY DA USER1.SECURITY.DATA SHR REU

-RUN
-* Write out the first part of the DBAEMP2 Master File
-WRITE OUTFI FILE=DBAEMP2,SUFFIX=FIX,$
-WRITE OUTFI SEGNAME=ONE,SEGTYPE=S0
-WRITE OUTFI FIELD=ONE,,A1,A1,$
-WRITE OUTFI END
-WRITE OUTFI DBA=USERD,$
-* Write out a FILE declaration for the calling Master File, passed as &1
-WRITE OUTFI FILE=&1,$
-* Initialize the variables to be read from the security.data file
-SET &USER=' ';
-SET &ACCESS=' ';
-SET &RESTRICT=' ';
-SET &NAME = ' ';
-SET &VALUE = ' ';

Describing Data With TIBCO WebFOCUS® Language

 53

Creating and Using a Master File Profile

-* Establish the loop for each record of the security.data file
-SET &DONE =  N ;
-REPEAT ENDLP WHILE &DONE EQ N ;
-* Read a record from security.data
-READFILE SECURITY
-* Check if the end of the security.data file was reached and,
-*   if so, branch out of the loop
-SET &DONE =  IF &IORETURN EQ 1 THEN 'Y' ELSE 'N';
-IF &DONE EQ 'Y' GOTO ENDLP1;
-* If there is a RESTRICT attribute, go to the label -CHKSTR.
-IF &RESTRICT NE ' ' THEN GOTO CHKRSTR;
-* If there is no RESTRICT attribute,
-*  write the USER and ACCESS attributes, and loop for the next record
-WRITE OUTFI USER=&USER , ACCESS=&ACCESS ,$
-GOTO ENDLP

-CHKRSTR
-* If there is a RESTRICT attribute, check if it has a VALUE attribute
-* and, if so, go to the label -CHKVAL
-IF &VALUE NE ' ' THEN GOTO CHKVAL;
-* If there is no VALUE attribute,
-*  write USER, ACCESS, RESTRICT, and NAME, and loop for next record
-WRITE OUTFI USER=&USER, ACCESS=&ACCESS, RESTRICT=&RESTRICT, NAME=&NAME,$
-GOTO ENDLP

-CHKVAL
-* If there is a VALUE attribute, write out USER, ACCESS, RESTRICT,
-*  NAME, and VALUE, and loop for next record
-WRITE OUTFI  USER=&USER, ACCESS=&ACCESS,RESTRICT=&RESTRICT,NAME=&NAME, VALUE =
&VALUE ,$
-ENDLP
-ENDLP1

When run, this procedure creates the following DBAFILE:

FILE=DBAEMP2,SUFFIX=FIX,$
SEGNAME=ONE,SEGTYPE=S0
  FIELD=ONE,,A1,A1,$
END
DBA=USERD,$
FILE=EMPDATA,$
USER=USER1,ACCESS=R,RESTRICT=NOPRINT,NAME=SALARY   ,$
USER=USER2, ACCESS=R, RESTRICT=VALUE, NAME=SYSTEM,
  VALUE=DEPT EQ SALES OR MARKETING ,$
USER=HR1,   ACCESS=R, RESTRICT=VALUE, NAME=SYSTEM,
  VALUE = SALARY FROM 20000 TO 35000,$
USER=HR1,   ACCESS=W, RESTRICT=SEGMENT, NAME=EMPDATA  ,$
USER=HR2,   ACCESS=R, RESTRICT=VALUE, NAME=EMPDATA,
  VALUE = SALARY GT 0 ,$

54

2. Identifying a Data Source

The following request prints the PIN, SALARY, TITLE, and DEPT fields from EMPDATA:

TABLE FILE EMPDATA
PRINT SALARY TITLE DEPT
BY PIN
WHERE PIN GE '000000010'  AND PIN LE  '000000200'
ON TABLE SET PAGE NOPAGE
ON TABLE PCHOLD FORMAT PDF
END

To run the request, you must first set a valid user password. The MFD_PROFILE procedure will
be run first and will create the dbaemp2.mas DBAFILE.

Running the request by first issuing the SET PASS=USER1 command produces the following
report in which the salaries display as zeros because of the RESTRICT=NOPRINT attribute for
the SALARY field:

Running the request by first issuing the SET PASS=USER2 command produces the following
report in which only the SALES and MARKETING departments display because of the VALUE
restriction for the DEPT field:

Describing Data With TIBCO WebFOCUS® Language

 55

Creating and Using a Master File Profile

Running the request by first issuing the SET PASS=HR1 command produces the following
report in which only the salaries between 20000 and 35000 display because of the VALUE
restriction for the DEPT field:

Example:

Creating a Dynamic DBA Rule in a Master File

The sequential data source named VALTEST.DATA contains a list of user names and their
associated value restrictions:

SALLY               CURR_SAL LT 20000
JOHN                DEPARTMENT EQ PRODUCTION
TOM                 CURR_SAL GE 20000

Before reading this file, you must FILEDEF or allocate it:

FILEDEF VALTEST DISK baseapp/valtest.data

Or, on z/OS under PDS deployment:

DYNAM ALLOC DD VALTEST DA USER1.VALTEST.DATA SHR REU

The following Master File named EMPDBA is a view of the EMPLOYEE data source. It has a
DBA section that uses the global variable &&UID for the USER attribute and the global variable
&&VAL for the value test against the EMPINFO segment. It also identifies a Master File profile
named DBAEMP3. This profile will obtain the user ID of the connected user and find the correct
VALUE restriction by reading the VALTEST.DATA file. By setting the global variables to the
correct values, it will insert the appropriate DBA rule into the Master File.

Note: You can use the system variable &FOCSECUSER instead of the global variable &&UID.

56

2. Identifying a Data Source

FILENAME=EMPLOYEE, SUFFIX=FOC, MFD_PROFILE=DBAEMP3,$
VARIABLE NAME=&&UID, USAGE=A8 , $
VARIABLE NAME=&&VAL, USAGE=A25, $

SEGNAME=EMPINFO,  SEGTYPE=S1
 FIELDNAME=EMP_ID,       ALIAS=EID,     FORMAT=A9,       $
 FIELDNAME=LAST_NAME,    ALIAS=LN,      FORMAT=A15,      $
 FIELDNAME=FIRST_NAME,   ALIAS=FN,      FORMAT=A10,      $
 FIELDNAME=HIRE_DATE,    ALIAS=HDT,     FORMAT=I6YMD,    $
 FIELDNAME=DEPARTMENT,   ALIAS=DPT,     FORMAT=A10,      $
 FIELDNAME=CURR_SAL,     ALIAS=CSAL,    FORMAT=D12.2M,   $
 FIELDNAME=CURR_JOBCODE, ALIAS=CJC,     FORMAT=A3,       $
 FIELDNAME=ED_HRS,       ALIAS=OJT,     FORMAT=F6.2,     $
END
DBA=DBAUSER1,$
USER=&&UID,ACCESS=R,RESTRICT=VALUE,NAME=EMPINFO,VALUE=&&VAL,$

The following is the MFD_PROFILE procedure:

SET MESSAGE = OFF
-SET &VALUETEST = 'NOTFOUND';
-* Find the user ID of the connected user
-SET &&UID = GETUSER('A20');
-SET &&UID = TRUNCATE(&&UID);
-* Create a HOLD file with the value test for the connected user
TABLE FILE VALTEST
PRINT VALUETEST
WHERE USERNAME EQ '&&UID'
ON TABLE HOLD AS USERVAL FORMAT ALPHA
END
-RUN
-READ USERVAL &VALUETEST.A30
-* If the user name was not in the file, type a message and exit
-IF &VALUETEST NE 'NOTFOUND' GOTO SETVALUE;
-TYPE USER WASN'T THERE
-EXIT
-SETVALUE
-* Set the global variable for the value test to the correct test
-SET &&VAL = ''|&VALUETEST||'';
-* Set the USER parameter to the user ID of the connected user
SET USER = &&UID

The following request displays a report against the EMPDBA view of the EMPLOYEE data
source:

USE
EMPLOYEE AS EMPDBA
END
-RUN
TABLE FILE EMPDBA
PRINT LN FN CURR_SAL
BY DEPARTMENT
ON TABLE SET PAGE NOPAGE
END

Describing Data With TIBCO WebFOCUS® Language

 57

Storing Localized Metadata in Language Files

Running the request when SALLY is the connected user produces a report of employees whose
salaries are less than $20,000:

DEPARTMENT  LAST_NAME        FIRST_NAME         CURR_SAL
----------  ---------        ----------         --------
MIS         SMITH            MARY             $13,200.00
            JONES            DIANE            $18,480.00
            MCCOY            JOHN             $18,480.00
            GREENSPAN        MARY              $9,000.00
PRODUCTION  STEVENS          ALFRED           $11,000.00
            SMITH            RICHARD           $9,500.00
            MCKNIGHT         ROGER            $16,100.00

Running the request when TOM is the connected user produces a report of employees whose
salaries are greater than or equal to $20,000:

DEPARTMENT  LAST_NAME        FIRST_NAME         CURR_SAL
----------  ---------        ----------         --------
MIS         BLACKWOOD        ROSEMARIE        $21,780.00
            CROSS            BARBARA          $27,062.00
PRODUCTION  BANNING          JOHN             $29,700.00
            IRVING           JOAN             $26,862.00
            ROMANS           ANTHONY          $21,120.00

Running the request when JOHN is the connected user produces a report that includes only the
PRODUCTION department:

DEPARTMENT  LAST_NAME        FIRST_NAME         CURR_SAL
----------  ---------        ----------         --------
PRODUCTION  STEVENS          ALFRED           $11,000.00
            SMITH            RICHARD           $9,500.00
            BANNING          JOHN             $29,700.00
            IRVING           JOAN             $26,862.00
            ROMANS           ANTHONY          $21,120.00
            MCKNIGHT         ROGER            $16,100.00

Storing Localized Metadata in Language Files

If you want to centralize localized column titles, descriptions, and prompts, and apply them to
multiple Master Files, you can create a set of translation files and use the TRANS_FILE
attribute in a Master File to invoke them. You can set up the files totally manually, or you can
use the LNGPREP utility to prepare the files for translation.

LNGPREP Utility: Preparing Metadata Language Files

The LNGPREP utility extracts TITLE, DESCRIPTION, CAPTION, and PROMPT attribute values from
application Master Files into specially formatted language translation files for each language
you need. Once you have the contents of these language files translated, your users can run
these applications in the language they select.

58

2. Identifying a Data Source

LNGPREP does two things. It extracts attribute values from a Master File into language files,
and it inserts or updates the TRANS_FILE attribute in the Master File with a value identifying
the application folder where the language files reside and a prefix used for naming the set of
language files. If the Master File is part of a cluster, LNGPREP will extract translatable strings
from every Master File referenced in the cluster, and will update each with the same
TRANS_FILE value.

LNGPREP requires an input file listing the three-character codes of the languages you need.

The name of each language file starts with the prefix specified in the TRANS_FILE value,
followed by a three-character language code, and the extension .lng.

For example, assume the language input file contains the French and Spanish language codes:

fre
spa

If the Master File specifies:

trans_file = xlate/xl_

The language translation files would be in the xlate application folder, named:

xl_fre.lng for French.

xl_spa.lng for Spanish.

Reference: The Base Language File

Each Master File must have a single base language in which the DESCRIPTION, TITLE,
CAPTION, and PROMPT attributes are specified. This language does not need to be English.

LNGPREP extracts these attribute values into the base language file, whose language code, for
historical reasons, is eng. In this case, eng does not mean English. It means whatever
language the Master File is written in.

The base language file (prefixeng.lng) should never be hand edited. All other lng files must be
hand edited by translators, to translate the string values from the base language to the
appropriate language.

Describing Data With TIBCO WebFOCUS® Language

 59

Storing Localized Metadata in Language Files

Translating Applications into English

Since language code eng is reserved to mean base language, you cannot use it to contain
English translations of an application whose base language is not English. In those cases, use
any of the other English dialect language codes, such as AME, UKE, CAE, or AUE. For example,
if the base language is German, specify AME in the languages file, run LNGPREP, and it will
produce prefixeng.lng and prefixame.lng files, both in German. Translate the contents of
prefixame.lng into English. Leave prefixeng.lng untouched.

Reference: How Translated Master File Attributes Display

Each language file contains a line for each attribute value from a related set of Master Files.
Each attribute value has a unique index number assigned to it. For example, if the Master File
contains FIELDNAME=PRODUCT_CATEGORY, TITLE='Product,Category', and that TITLE happens
to be the 39th translatable attribute value, LNGPREP will produce lng files all containing the
line:

39 = Product,Category

Your French translator will edit prefixfre.lng, leaving the index values unchanged while
translating the string values, producing, in this case,

39 = Produit,Catégorie

At run time, when the TITLE for field PRODUCT_CATEGORY needs to be displayed, if
WebFOCUS is configured for LANG=FRE, WebFOCUS looks up "Product,Category" in
prefixeng.lng, finds index value 39, looks up 39 in prefixfre.lng, and displays the TITLE as
"Produit,Catégorie."

LNGPREP Modes

You can run LNGPREP from the Web Console using the Prepare Translation Files option, or you
can run it using syntax. In either case, you must first create a configuration file containing the
three-character language codes for each translation file you need, one language code on each
line. The first invocation of LNGPREP for a given Master File adds the TRANS_FILE attribute in
that and all related Master Files, creates the base language file by scanning the Master Files
for supported attribute values, and creates a copy of the base language file with the correct
name for each additional language. Then, a translator has to translate the values in each
additional language file from the base language to the correct language for that file.

On each subsequent run, LNGPREP will check for updates to the list of related Master Files
and attribute values and update the files as needed. Translators will then have to translate any
attribute values added to the language files.

60

2. Identifying a Data Source

Reference: LNGPREP Best Practice

The recommended best practice is to create an app directory solely for the purpose of
containing .lng files, and use this appname and a common prefix value for all LNGPREP
commands. In addition, put the languages fn.cfg file in this app folder. This will create one set
of .lng files for all apps, minimizing the time and effort spent on translation.

Procedure: How to Prepare Metadata Language Files Using the Web Console

1. Right-click a synonym, point to Metadata Management, then click Prepare Translation Files,

as shown in the following image.

The Set Translation Files page opens, as shown in the following image.

2. Enter the following values or accept the defaults.

Application for Translation Files

Is the name of the application where the language files will be stored. You can click
the ellipsis to select an application from the current application path. By default, it is
the application where the synonym resides.

Prefix

Is the prefix value for the translation files for the selected synonym.

Describing Data With TIBCO WebFOCUS® Language

 61

Storing Localized Metadata in Language Files

Languages File

Is the file containing the list of language codes for which translation files should be
prepared. The file must have the extension .cfg, be stored in an application directory
on the application path, and have one language code on each line. You can click the
ellipsis to select the application where the languages file is stored.

3. Click OK.

The language files are prepared using the application, prefix, and languages configuration
file you specified. A status page will open listing the language files created and the Master
Files processed.

Syntax:

How to Run the LNGPREP Command Using Syntax

LNGPREP FILE n_part_name LNGAPP appname LNGPREFIX prefix
        LNGFILE appname/fn

where:

n_part_name

Specifies the n-part (app1/app2...) name of a Master File.

appname

Specifies the location where .lng files will be written and updated.

prefix

Specifies the literal characters that will precede the three-character language code in the
names of the .lng files.

appname/fn

Specifies the appname and filename of a user-created .cfg file containing the list of three-
character language codes, one per line. For example, the following file named langretail.cfg
contains language codes for American English, French, and Japanese:

ame
fre
jpn

Example:

Sample LNGPREP Command

Assume the lnglist.cfg file contains the language codes fre (French) and spa (Spanish):

fre
spa

Issue the following LNGPREP command:

LNGPREP FILE weather/forecast LNGAPP xlate LNGPREFIX tq_ LNGFILE  xlate/lnglist

62

2. Identifying a Data Source

Alternately, you can right-click the forecast synonym, point to Metadata Management, and
select Prepare Translation Files. The Set Translation File for weather/forecast.mas page opens,
as shown in the following image. Enter the values shown in the following image and click OK.

The following language files will be created:

xlate/tq_eng.lng

xlate/tq_fre.lng

xlate/tq_spa.lng

The Master File weather/forecast.mas will be updated with the following attribute:

TRANS_FILE= xlate/tq_

Translators then have to translate the values in xlate/tq_fre.lng and xlate/tq_spa.lng.

Describing Data With TIBCO WebFOCUS® Language

 63

Storing Localized Metadata in Language Files

64

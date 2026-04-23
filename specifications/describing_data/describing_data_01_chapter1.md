Chapter1

Understanding a Data Source Description

Information Builders products provide a flexible data description language, which you can
use with many types of data sources, including:

Relational, such as DB2, Oracle, Sybase, and Teradata.

Hierarchical, such as IMS, FOCUS, and XFOCUS.

Network, such as CA-IDMS.

Indexed, such as ISAM and VSAM.

Sequential, both fixed-format and free-format.

Multidimensional, such as Essbase.

You can also use the data description language and related facilities to:

Join different types of data sources to create a temporary structure from which your
request can read or write.

Define a subset of fields or columns to be available to users.

Logically rearrange a data source to access the data in a different order.

In this chapter:

A Note About Data Source Terminology

What Is a Data Source Description?

How an Application Uses a Data Source Description

What Does a Master File Describe?

Creating a Data Source Description

Naming a Master File

What Is in a Master File?

Describing Data With TIBCO WebFOCUS® Language

 17

A Note About Data Source Terminology

A Note About Data Source Terminology

Different types of data sources make use of similar concepts but refer to each differently. For
example, the smallest meaningful element of data is called a field by many hierarchical
database management systems and indexed data access methods, but called a column by
relational database management systems.

There are other cases in which a common concept is identified by a number of different terms.
For simplicity, we use a single set of standardized terms. For example, we usually refer to the
smallest meaningful element of data as a field, regardless of the type of data source.
However, when required for clarity, we use the term specific to a given data source. Each time
we introduce a new standard term, we define it and compare it to equivalent terms used with
different types of data sources.

What Is a Data Source Description?

When your application accesses a data source, it needs to know how to interpret the data that
it finds. Your application needs to know about:

The overall structure of the data. For example, is the data relational, hierarchical, or
sequential? Depending upon the structure, how is it arranged or indexed?

The specific data elements. For example, what fields are stored in the data source, and
what is the data type of each field (character, date, integer, or some other type)?

To obtain the necessary information, your application reads a data source description, also
called a synonym. The primary component of a synonym is called a Master File. A Master File
describes the structure of a data source and its fields. For example, it includes information
such as field names and data types.

For some data sources, an Access File supplements a Master File. An Access File includes
additional information that completes the description of the data source. For example, it
includes the full data source name and location. You require one Master File and, for some
data sources, one Access File to describe a data source.

18

How an Application Uses a Data Source Description

1. Understanding a Data Source Description

Master Files and Access Files are stored separately, apart from the associated data source.
Your application uses a data source Master File (and if required, the corresponding Access
File) to interpret the data source in the following way:

1. Identifies, locates, and reads the Master File for the data source named in a request.

If the Master File is already in memory, your application uses the memory image and then
proceeds to locate and read the data source.

If the Master File is not in memory, the application locates the Master File on a storage
device and loads it into memory, replacing any existing Master File in memory.

If your Master File references other data sources as cross-referenced segments, or if a
JOIN command is in effect for this file, the cross-referenced Master Files are also read into
memory.

2. If there is a profile for the Master File, indicated by the presence of the MFD_PROFILE

attribute in the FILE declaration, that profile is executed.

3. Reads the security rules if Information Builders data source security (DBA) has been

specified for the data source, and ensures that user access is allowed based on any DBA
security specified.

4. Locates and reads the Access File for the data source named in the request, if that data

source requires an Access File.

5. Locates and reads the data source.

The data source contents are interpreted based on the information in the Master File and,
if applicable, the Access File.

Note: You can encrypt a Master File using the ENCRYPT command described in Hiding
Restriction Rules: The ENCRYPT Command on page 436. However, the first line of a Master
File that is going to be encrypted cannot be longer than 68 characters. If it is longer than 68
characters, you must break it up onto multiple lines.

What Does a Master File Describe?

A Master File enables you to:

Identify the name and type of a data source.

Identify and relate groups of fields.

Describe individual fields.

Describing Data With TIBCO WebFOCUS® Language

 19

What Does a Master File Describe?

Note:

Every Master File must contain at least one segment declaration and one field declaration.
If a required attribute is not assigned a specific value, a comma must be used as a
placeholder.

The maximum number of segments supported in a structure is 1024. This structure can be
created by joining or combining data sources.

The maximum number of segments in a single FOCUS data source is 64. XFOCUS data
sources can have up to 512 segments. The maximum number of segments plus indices for
a single FOCUS data source is 191.

The total length of all fields can be up to 256K.

Identifying a Data Source

In order to interpret data, your application needs to know the name you are using to identify
the data source and what type of data source it is. For example, is it a DB2 data source, an
Oracle data source, or a FOCUS data source?

For more information, see Identifying a Data Source on page 31.

Identifying and Relating a Group of Fields

A Master File identifies and relates groups of fields that have a one-to-one correspondence
with each other. In Master File terms, a segment and in relational terms, a table.

You can join data sources of the same type (using a Master File or a JOIN command) and data
sources of different types (using a JOIN command). For example, you can join two DB2 data
sources to a FOCUS data source, and then to a VSAM data source.

For more information about defining and relating groups of fields, see Describing a Group of
Fields on page 65.

Describing a Field

Every field has several characteristics that you must describe in a Master File, such as type of
data and length or scale. A Master File can also indicate optional field characteristics. For
example, a Master File can specify if the field can have a missing value, and can provide
descriptive information for the field.

A Master File usually describes all of the fields in a data source. In some cases, however, you
can create a logical view of the data source in which only a subset of the fields is available,
and then describe only those fields in your Master File.

For more information, see Describing an Individual Field on page 103.

20

1. Understanding a Data Source Description

Note: Master Files/data source descriptions must contain uppercase field and segment
names if you are using them with Maintain Data.

Creating a Data Source Description

You can create a Master File and Access File for a data source in several ways. If the data
source:

Has an existing description, such as a native schema or catalog, or a COBOL File
Description. You can use a tool to automatically generate the Master File and Access File
from the existing description.

Does not have an existing description, you can create a Master File and (if required) an
Access File by coding them using Information Builders data source description language,
and specify their attributes using any text editor.

Creating a Master File and Access File Using an Editor

You can create a Master File and an Access File by:

Coding them using a text editor. You can do this in all Information Builders products. The
information that you require about Master File syntax is contained in this documentation.
For information about Access File syntax, see your data adapter documentation or
Describing a FOCUS Data Source on page 293.

After editing a Master File, issue the CHECK FILE command to validate the new Master File
and to refresh your session image.

Specifying their attributes using the Master File Editor or the Synonym Editor. The Master
File Editor is available in Maintain Data.

Naming a Master File

Master File names for FOCUS and fixed-format sequential data sources can be up to 64
characters long on z/OS, UNIX, and Windows platforms. Except where noted, this length is
supported in all functional areas that reference a Master File.

Describing Data With TIBCO WebFOCUS® Language

 21

Naming a Master File

Using Long Master File Names on z/OS

In the z/OS environment, file and member names are limited to eight characters. Therefore,
longer Master File names are assigned eight-character names to be used when interacting with
the operating system. Use the following to implement Master File names longer than eight
characters:

A LONGNAME option for the DYNAM ALLOCATE command, which creates the long Master
File name and performs the allocation. This DYNAM option is described in How to Allocate a
Long Master File Name in z/OS on page 24.

An eight-character naming convention for member names associated with long Master File
names. This convention is described in Member Names for Long Master File Names in z/OS
on page 22.

A long Master File attribute, $ VIRT, which contains the long name to be used when
interacting with the Master File and the operating system. This attribute is described in How
to Implement a Long Master File Name in z/OS on page 23.

Member Names for Long Master File Names in z/OS

The DYNAM ALLOC command with the LONGNAME option automatically creates a member for
the long Master File name in the PDS allocated to ddname HOLDMAST.

The member name consists of three parts: a prefix consisting of the leftmost characters from
the long name, followed by a left brace character ({), followed by an index number. This naming
convention is in effect for all long Master Files allocated using DYNAM or created using the
HOLD command. The length of the prefix depends on how many long names have a common
set of leftmost characters:

The first ten names that share six or more leftmost characters have a six-character prefix
and a one-character index number, starting from zero.

Starting with the eleventh long name that shares the same leftmost six characters, the
prefix becomes five characters, and the index number becomes two characters, starting
from 00.

This process can continue until the prefix is one character and the index number is six
characters. If you delete one of these members from the HOLDMAST PDS, the member name
will be reused for the next new long name created with the same prefix.

22

1. Understanding a Data Source Description

Example:

Long Master File Names and Corresponding Member Names

The following table lists sample long names with the corresponding member names that would
be assigned under z/OS.

Long Name

Member Name

EMPLOYEES_ACCOUNTING

EMPLOYEES_DEVELOPMENT

EMPLOYEES_DISTRIBUTION

EMPLOYEES_FINANCE

EMPLOYEES_INTERNATIONAL

EMPLOYEES_MARKETING

EMPLOYEES_OPERATIONS

EMPLOYEES_PERSONNEL

EMPLOYEES_PUBLICATIONS

EMPLOYEES_RESEARCH

EMPLOYEES_SALES

EMPLOYEES_SUPPORT

EMPLOY{0

EMPLOY{1

EMPLOY{2

EMPLOY{3

EMPLOY{4

EMPLOY{5

EMPLOY{6

EMPLOY{7

EMPLOY{8

EMPLOY{9

EMPLO{00

EMPLO{01

Syntax:

How to Implement a Long Master File Name in z/OS

To relate the short name to its corresponding long name, the first line of a long Master File
contains the following attribute

$ VIRT = long_filename

Describing Data With TIBCO WebFOCUS® Language

 23

Naming a Master File

where:

long_filename

Is the long name, up to 64 characters in length.

Syntax:

How to Allocate a Long Master File Name in z/OS

DYNAM ALLOC DD ddname LONGNAME long_filename DS physical_filename

where:

ddname

Is the one-character to eight-character member name in a PDS allocated to DD MASTER.

long_filename

Is the long Master File name. The DYNAM command creates a copy of the short Master
File in the PDS allocated to DD HOLDMAST. The member in HOLDMAST conforms to the
eight-character naming convention for long names. The Master File has the $ VIRT attribute
on the top line, which contains the long name.

Note: The copy, not the member ddname, is the Master File used when you reference the
long name in a request.

physical_filename

Is the data set name of the FOCUS or fixed-format sequential data source.

After you have allocated the long name, you can reference the data source using the long
Master File name or the short ddname.

Syntax:

How to Free an Allocation for a Long Master File Name

DYNAM FREE LONGNAME long_filename

where:

long_filename

Is the long Master File name.

After issuing the DYNAM FREE LONGNAME command, you cannot reference the data source
using the long Master File name. However, you can reference it using the short ddname that
was specified in the DYNAM ALLOC command.

24

1. Understanding a Data Source Description

Example:

Using a Long Master File Name on z/OS

To reference the EMPLOYEE data source as EMPLOYEE_DATA, dynamically allocate the long
name:

DYNAM ALLOC DD EMPLOYEE LONGNAME EMPLOYEE_DATA -
  DS USER1.EMPLOYEE.FOCUS SHR REU

You can now issue a request using the long name:

TABLE FILE EMPLOYEE_DATA
PRINT CURR_SAL
BY LAST_NAME BY FIRST_NAME
END

The output is:

LAST_NAME        FIRST_NAME         CURR_SAL
---------        ----------         --------
BANNING          JOHN             $29,710.00
BLACKWOOD        ROSEMARIE        $21,790.00
CROSS            BARBARA          $27,072.00
GREENSPAN        MARY              $9,010.00
IRVING           JOAN             $26,872.00
JONES            DIANE            $18,490.00
MCCOY            JOHN             $18,490.00
MCKNIGHT         ROGER            $16,110.00
ROMANS           ANTHONY          $21,130.00
SMITH            MARY             $13,210.00
                 RICHARD           $9,510.00
STEVENS          ALFRED           $11,010.00

In this example, the long Master File will exist in the HOLDMAST PDS as member EMPLOY{0.
The index number after the bracket depends on the number of existing long Master Files
containing the same first six leftmost characters. The content of the EMPLOYEE_DATA Master
File is virtually identical to the short Master File used in the allocation. The only difference is
the $ VIRT keyword on line one, which contains the long name. The FILENAME parameter also
contains the long name, up to 64 characters.

$ VIRT=EMPLOYEE_DATA
$ Created from EMPLOYEE      MASTER
FILENAME=EMPLOYEE_DATA,
SUFFIX=FOC
SEGNAME=EMPINFO,  SEGTYPE=S1
 FIELDNAME=EMP_ID,    ALIAS=EID, FORMAT=A9,  $
 FIELDNAME=LAST_NAME, ALIAS=LN,  FORMAT=A15, $
         .
         .
         .

Describing Data With TIBCO WebFOCUS® Language

 25

What Is in a Master File?

Reference: Usage Notes for Long Master File Names

The FOCUS Database Server (FDS) is not supported on any platform.

The DATASET attribute is not supported in a long name Master File.

The ACCESSFILE attribute is not supported with long name Master Files.

An external index is not supported.

The LONGNAME option of the DYNAM command may only be issued from within a
procedure (FOCEXEC) or Remote Procedure Call (RPC). It cannot be used to preallocate long
Master Files in JCL or CLISTS.

Long Master Files are not designed to be edited on z/OS. Each time the DYNAM command
is issued with the LONGNAME attribute, it overlays the existing member in HOLDMAST. You
must make any edits (such as the addition of fields or DBA attributes, or use of the
REBUILD utility) to an existing short Master File.

? FDT and ? FILE longfilename will show an internal DD alias of @000000n, where n is less
than or equal to the number of existing long file allocations. Use this internal DDNAME in
all queries that require a valid DDNAME, such as USE commands.

What Is in a Master File?

A Master File describes a data source using a series of declarations:

A data source declaration.

A segment declaration for each segment within the data source.

A field declaration for each field within a segment.

Declarations for other objects that can be optionally added to the data source description,
such as FILTER, DEFINE, COMPUTE, and SORTOBJ definitions.

The specifications for an Access File are similar, although the details vary by type of data
source. The appropriate documentation for your adapter indicates whether you require an
Access File and, if so, what the Access File attributes are.

26

1. Understanding a Data Source Description

Syntax:

How to Specify a Declaration

Each declaration specifies a series of attributes in the form

attribute = value, attribute = value, ... ,$

where:

attribute

Is a Master File keyword that identifies a file, segment, or field property. You can specify
any Master File attribute by its full name, its alias, or its shortest unique truncation. For
example, you can use the full attribute FILENAME or the shorter form FILE.

value

Is the value of the attribute.

A comma follows each attribute assignment, and each field declaration ends with a dollar sign
($). Commas and dollar signs are optional at the end of data source and segment
declarations.

Each declaration should begin on a new line. You can extend a declaration across as many
lines as you want. For a given declaration you can put each attribute assignment on a separate
line, combine several attributes on each line, or include the entire declaration on a single line.

For more information on data source declarations, see Identifying a Data Source on page
31.

For more information on segment declarations, see Describing a Group of Fields on page
65.

For more information on field declarations, see Describing an Individual Field on page 103.

Note: In a Master File, the attribute name must be in English. The attribute value can be in any
supported national language.

Improving Readability

Begin each attribute assignment in any position. You can include blank spaces between the
elements in a declaration. This makes it easy for you to indent segment or field declarations to
make the Master File easier to read. To position text, use blank spaces, not the Tab character.

You can also include blank lines to separate declarations. Blank spaces and lines are not
required and are ignored by the application.

Describing Data With TIBCO WebFOCUS® Language

 27

What Is in a Master File?

Example:

Improving Readability With Blank Spaces and Blank Lines

The following declarations show how to improve readability by adding blank spaces and blank
lines within and between declarations:

SEGNAME=EMPINFO, SEGTYPE=S1 ,$
  FIELDNAME=EMP_ID, ALIAS=EID, USAGE=A9 ,$

SEGNAME=EMPINFO, SEGTYPE=S1 ,$
  FIELDNAME = EMP_ID, ALIAS = EID, USAGE = A9 ,$

SEGNAME=EMPINFO,SEGTYPE=S1,$
  FIELDNAME = EMP_ID, ALIAS = EID, USAGE = A9 ,$

Example:

Improving Readability by Extending a Declaration Across Lines

The following example extends a field declaration across several lines:

FIELDNAME = MEMBERSHIP, ALIAS = BELONGS, USAGE = A1, MISSING = ON,
  DESCRIPTION = This field indicates the applicant's membership status,
  ACCEPT = Y OR N, FIELDTYPE = I,
  HELPMESSAGE = 'Please enter Y for Yes or N for No' ,$

Adding a Comment

You can add comments to any declaration by:

Typing a comment in a declaration line after the terminating dollar sign.

Creating an entire comment line by placing a dollar sign at the beginning of the line.

Adding a comment line terminates the previous declaration if it has not already been
terminated. Everything on a line following the dollar sign is ignored.

Comments placed after a dollar sign are useful only for those who view the Master File source
code. They do not appear in graphical tools. For information about providing descriptions for
display in graphical tools using the REMARKS or DESCRIPTION attribute, see Identifying a Data
Source on page 31, and Describing an Individual Field on page 103.

Example:

Adding a Comment in a Master File

The following example contains two comments. The first comment follows the dollar sign on
the data source declaration. The second comment is on a line by itself after the data source
declaration.

FILENAME = EMPLOYEE, SUFFIX = FOC ,$ This is the personnel data source.
$ This data source tracks employee salaries and raises.
SEGNAME = EMPINFO, SEGTYPE = S1 ,$

28

1. Understanding a Data Source Description

Editing and Validating a Master File

After you manually create or edit a Master File, you should issue the CHECK FILE command to
validate it. CHECK FILE reads the new or revised Master File into memory and highlights any
errors in your Master File so that you can correct them before reading the data source.

The CHECK FILE PICTURE command displays a diagram illustrating the structure of a data
source. You can also use this command to view information in the Master File, such as names
of segments and fields, and the order in which information is retrieved from the data source
when you run a request against it.

For more information, see Checking and Changing a Master File: CHECK on page 395.

Describing Data With TIBCO WebFOCUS® Language

 29

What Is in a Master File?

30

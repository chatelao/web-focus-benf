Chapter14

Joining Data Sources

You can join two or more related data sources to create a larger integrated data structure
from which you can report in a single request. The joined structure is virtual. It is a way of
accessing multiple data sources as if they were a single data source. Up to 1022 joins
can be in effect at one time, for a total of 1023 segments, depending on the number of
active segments and the number and length of the fields (there is a 32K limit on the
length of all fields).

For details about data sources you can use in a join, see Data Sources You Can and
Cannot Join on page 1071.

In this chapter:

Types of Joins

How the JOIN Command Works

Creating an Equijoin

Using a Conditional Join

Full Outer Joins

Reporting Against a Multi-Fact Cluster
Synonym

Navigating Joins Between Cluster
Synonyms

Cross Database Join Optimization

Invoking Context Analysis for a Star
Schema With a Fan Trap

Adding DBA Restrictions to the Join
Condition: SET DBAJOIN

Preserving Virtual Fields During Join
Parsing

Displaying Joined Structures

Clearing Joined Structures

Types of Joins

When you join two data sources, some records in one of the files may lack corresponding
records in the other file. When a report omits records that are not in both files, the join is
called an inner join. When a report displays all matching records, plus all records from the host
file that lack corresponding cross-referenced records, the join is called a left outer join. When a
report displays all matching records plus all records from both files that lack corresponding
records in the other file, the join is called a full outer join. Full outer joins are supported for
relational data sources only.

Creating Reports With TIBCO® WebFOCUS Language

 1069

The SET ALL command globally determines how all joins are implemented. If the SET ALL=ON
command is issued, all joins are treated as outer joins. With SET ALL=OFF, the default, all
joins are treated as inner joins.

Each JOIN command can specify explicitly which type of join to perform, locally overruling the
global setting. This syntax is supported for FOCUS, XFOCUS, Relational, VSAM, IMS, and
Adabas. If you do not specify the type of join in the JOIN command, the ALL parameter setting
determines the type of join to perform.

You can also join data sources using one of two techniques for determining how to match
records from the separate data sources. The first technique is known as an equijoin and the
second is known as a conditional join. When deciding which of the two join techniques to use,
it is important to know that when there is an equality condition between two data sources, it is
more efficient to use an equijoin rather than a conditional join.

You can use an equijoin structure when you are joining two or more data sources that have two
fields, one in each data source, with formats (character, numeric, or date) and values in
common. Joining a product code field in a sales data source (the host file) to the product code
field in a product data source (the cross-referenced file) is an example of an equijoin. For more
information on using equijoins, see Creating an Equijoin on page 1082.

The conditional join uses WHERE-based syntax to specify joins based on WHERE criteria, not
just on equality between fields. Additionally, the host and cross-referenced join fields do not
have to contain matching formats. Suppose you have a data source that lists employees by
their ID number (the host file), and another data source that lists training courses and the
employees who attended those courses (the cross-referenced file). Using a conditional join,
you could join an employee ID in the host file to an employee ID in the cross-referenced file to
determine which employees took training courses in a given date range (the WHERE condition).
For more information on conditional joins, see Using a Conditional Join on page 1101.

Joins can also be unique or non-unique. A unique, or one-to-one, join structure matches one
value in the host data source to one value in the cross-referenced data source. Joining an
employee ID in an employee data source to an employee ID in a salary data source is an
example of a unique equijoin structure.

A non-unique, or one-to-many, join structure matches one value in the host data source to
multiple values in the cross-referenced field. Joining an employee ID in a company's employee
data source to an employee ID in a data source that lists all the training classes offered by
that company results in a listing of all courses taken by each employee, or a joining of the one
instance of each ID in the host file to the multiple instances of that ID in the cross-referenced
file.

Types of Joins

1070

14. Joining Data Sources

For more information on unique and non-unique joins, see Unique and Non-Unique Joined
Structures on page 1072.

Example:

Joined Data Structure

Consider the SALES and PRODUCT data sources. Each store record in SALES may contain
many instances of the PROD_CODE field. It would be redundant to store the associated
product information with each instance of the product code. Instead, PROD_CODE in the
SALES data source is joined to PROD_CODE in the PRODUCT data source. PRODUCT contains
a single instance of each product code and related product information, thus saving space and
making it easier to maintain product information. The joined structure, which is an example of
an equijoin, is illustrated below:

Reference: Data Sources You Can and Cannot Join

The use of data sources as host files and cross-referenced files in joined structures depends
on the types of data sources you are joining:

Typically, joins can be established between any FOCUS-readable files.

Data sources protected by DBA security may be joined, with certain restrictions. For details,
see Notes on DBA Security for Joined Data Structures on page 1072.

Conditional joins are supported only for FOCUS, VSAM, ADABAS, IMS, and all relational
data sources.

Creating Reports With TIBCO® WebFOCUS Language

 1071

Types of Joins

Reference: Notes on DBA Security for Joined Data Structures

You can join a data source with DBA protection to another data source with DBA protection,
as long as they use the same password.

In addition, you can join DBA protected data sources with different passwords by adding the
DBAFILE attribute to your security definition. The DBAFILE attribute names a central Master
File that contains different passwords and restrictions for several Master Files. If you use a
DBAFILE, a user can set separate passwords for each file using the syntax:

SET PASS = pswd1 IN file1, pswd2 IN file2

Individual DBA information remains in effect for each file in the JOIN. For details about the
DBAFILE attribute, see the Describing Data With WebFOCUS Language manual.

You can also join a DBA-protected host file to an unprotected cross-referenced file. The
DBA information is taken from the host file.

Unique and Non-Unique Joined Structures

In a unique joined structure, one value in the host field corresponds to one value in the cross-
referenced field. In a non-unique joined structure, one value in the host field corresponds to
multiple values in the cross-referenced field.

The ALL parameter in a JOIN command indicates that the joined structure is non-unique.

Omit the ALL parameter only when you are sure that the joined structure is unique. Omitting
the ALL parameter reduces overhead.

The ALL parameter does not interfere with the proper creation of the joined structure even if
it is unique. Use the ALL parameter if you are not sure whether the joined structure is
unique. This ensures that your reports contain all relevant data from the cross-referenced
file, regardless of whether the structure is unique.

1072

14. Joining Data Sources

Example:

A Unique Equijoin Structure

The following example illustrates a unique joined structure. Two FOCUS data sources are
joined together: an EMPDATA data source and a SALHIST data source. Both data sources are
organized by PIN, and they are joined on a PIN field in the root segments of both files. Each
PIN has one segment instance in the EMPDATA data source, and one instance in the SALHIST
data source. To join these two data sources, issue this JOIN command:

JOIN PIN IN EMPDATA TO PIN IN SALHIST

Example:

A Non-Unique Equijoin Structure

If a field value in the host file can appear in many segment instances in the cross-referenced
file, then you should include the ALL phrase in the JOIN syntax. This structure is called a non-
unique joined structure.

For example, assume that two FOCUS data sources are joined together: the JOB data source
and an EDUCFILE data source which records employee attendance at in-house courses. The
joined structure is shown in the following diagram.

The JOB data source is organized by employee, but the EDUCFILE data source is organized by
course. The data sources are joined on the EMP_ID field. Since an employee has one position
but can attend several courses, the employee has one segment instance in the JOB data
source but can have as many instances in the EDUCFILE data source as courses attended.

Creating Reports With TIBCO® WebFOCUS Language

 1073

Types of Joins

To join these two data sources, issue the following JOIN command, using the ALL phrase:

JOIN EMP_ID IN JOB TO ALL EMP_ID IN EDUCFILE

Syntax:

How to Correct for Lagging Values With a Unique Join

If a parent segment has two or more unique child segments that each have multiple children,
the report may incorrectly display a missing value. The remainder of the child values may then
be misaligned in the report. These misaligned values are called lagging values. The JOINOPT
parameter ensures proper alignment of your output by correcting for lagging values.

SET JOINOPT={NEW|OLD|GNTINT}

where:

NEW

Specifies that segments be retrieved from left to right and from top to bottom, which
results in the display of all data for each record, properly aligned. Missing values only
occur when they exist in the data.

OLD

Specifies that segments be retrieved as unique segments, which results in the display of
missing data in a report where all records should have values. This might cause lagging
values. OLD is the default value.

1074

14. Joining Data Sources

GNTINT

Specifies that segments be retrieved from left to right and from top to bottom, which
results in the display of all data for each record, properly aligned. Missing values only
occur when they exist in the data.

Note: The value GNTINT both corrects for lagging values and enables joins between
different numeric data types, as described in Joining Fields With Different Numeric Data
Types on page 1100.

Example:

Correcting for Lagging Values in a Procedure With Unique Segments and Multiple
Children

This example is a hypothetical scenario in which you would use the JOINOPT parameter to
correct for lagging values. Lagging values display missing data such that each value appears
off by one line.

A single-segment host file (ROUTES) is joined to two files (ORIGIN and DEST), each having two
segments. The files are joined to produce a report that shows each train number, along with
the city that corresponds to each station.

The following request prints the city of origin (OR_CITY) and the destination city (DE_CITY).
Note that missing data is generated, causing the data for stations and corresponding cities to
lag, or be off by one line.

TABLE FILE ROUTES
PRINT TRAIN_NUM
OR_STATION OR_CITY
DE_STATION DE_CITY
END

The output is:

TRAIN_NUM   OR_STATION   OR_CITY    DE_STATION   DE_CITY
---------   ----------   -------    ----------   -------
101         NYC          NEW YORK   ATL          .
202         BOS          BOSTON     BLT          ATLANTA
303         DET          DETROIT    BOS          BALTIMORE
404         CHI          CHICAGO    DET          BOSTON
505         BOS          BOSTON     STL          DETROIT
505         BOS          .          STL          ST. LOUIS

Creating Reports With TIBCO® WebFOCUS Language

 1075

Types of Joins

Issuing SET JOINOPT=NEW enables segments to be retrieved in the expected order (from left
to right and from top to bottom), without missing data.

SET JOINOPT=NEW
TABLE FILE ROUTES
PRINT TRAIN_NUM
OR_STATION OR_CITY
DE_STATION DE_CITY
END

The correct report has only 5 lines instead of 6, and the station and city data is properly
aligned. The output is:

TRAIN_NUM   OR_STATION    OR_CITY    DE_STATION   DE_CITY
---------   ----------    -------    ----------   -------
101         NYC           NEW YORK   ATL          ATLANTA
202         BOS           BOSTON     BLT          BALTIMORE
303         DET           DETROIT    BOS          BOSTON
404         CHI           CHICAGO    DET          DETROIT
505         BOS           BOSTON     STL          ST. LOUIS

Recursive Joined Structures

You can join a FOCUS or IMS data source to itself, creating a recursive structure. In the most
common type of recursive structure, a parent segment is joined to a descendant segment, so
that the parent becomes the child of the descendant. This technique (useful for storing bills of
materials, for example) enables you to report from data sources as if they have more segment
levels than is actually the case.

Example:

Understanding Recursive Joined Structures

For example, the GENERIC data source shown below consists of Segments A and B.

1076

14. Joining Data Sources

The following request creates a recursive structure:

JOIN FIELD_B IN GENERIC TAG G1 TO FIELD_A IN GENERIC TAG G2 AS RECURSIV

This results in the joined structure (shown below).

Note that the two segments are repeated on the bottom. To refer to the fields in the repeated
segments (other than the field to which you are joining), prefix the tag names to the field
names and aliases and separate them with a period, or append the first four characters of the
JOIN name to the field names and aliases. In the above example, the JOIN name is RECURSIV.
You should refer to FIELD_B in the bottom segment as G2.FIELD_B (or RECUFIELD_B). For
related information, see Usage Notes for Recursive Joined Structures on page 1077.

Reference: Usage Notes for Recursive Joined Structures

You must either specify a unique JOIN name, or use tag names in the JOIN command.
Otherwise, you will not be able to refer to the fields in the repeated segments at the bottom
of the join structure.

Creating Reports With TIBCO® WebFOCUS Language

 1077

Types of Joins

If you use tag names in a recursive joined structure, note the following guidelines:

If tag names are specified in a recursive join, duplicate field names must be qualified
with the tag name.

If a join name is specified and tag names are not specified in a recursive join, duplicate
field names must be prefixed with the first four characters of the join name.

If both a join name and a tag name are specified in a recursive join, the tag name must
be used as a qualifier.

The tag name must be used as the field name qualifier in order to retrieve duplicate
field names in a non-recursive join. If you do not qualify the field name, the first
occurrence is retrieved.

You may use a DEFINE-based join (see How to Join From a Virtual Field to a Real Field on
page 1095) to join a virtual field in a descendant segment to a field in the parent segment.

You can extend a recursive structure by issuing multiple JOIN commands from the bottom
repeat segment in the structure to the parent segment, creating a structure up to 16 levels
deep.

For FOCUS data sources, the field in the parent segment to which you are joining must be
indexed.

For IMS data sources, the following applies:

The parent segment must be the root segment of the data source.

The field to which you are joining must be both a key field and a primary or secondary
index.

You need a duplicate PCB in the PSB for every recursive join you create.

Example:

Using Recursive Joined Structures

This example explains how to use recursive joins to store and report on a bill of materials.
Suppose you are designing a data source called AIRCRAFT that contains the bill of materials
for an aircraft manufactured by a company. The data source records data on three levels of
airplane parts:

Major divisions, such as the cockpit or cabin.

Parts of divisions, such as instrument panels and seats.

1078

14. Joining Data Sources

Subparts, such as nuts and bolts.

The data source must record each part, the part description, and the smaller parts composing
the part. Some parts, such as nuts and bolts, are common throughout the aircraft. If you
design a three-segment structure, one segment for each level of parts, descriptions of
common parts are repeated in every place they are used.

To reduce this repetition, design a data source that has only two segments (shown in the
following diagram). The top segment describes each part of the aircraft, large and small. The
bottom segment lists the component parts without descriptions.

Every part (except for the largest divisions) appears in both the top segment, where it is
described, and in the bottom segment, where it is listed as one of the components of a larger
part. (The smallest parts, such as nuts and bolts, appear in the top segment without an
instance of a child in the bottom segment.) Note that each part, no matter how often it is used
in the aircraft, is described only once.

If you join the bottom segment to the top segment, the descriptions of component parts in the
bottom segment can be retrieved. The first-level major divisions can also be related to third-
level small parts, going from the first level to the second level to the third level. Thus, the
structure behaves as a three-level data source, although it is actually a more efficient two-level
source.

Creating Reports With TIBCO® WebFOCUS Language

 1079

Types of Joins

For example, CABIN is a first-level division appearing in the top segment. It lists SEATS as a
component in the bottom segment. SEATS also appears in the top segment. It lists BOLTS as
a component in the bottom segment. If you join the bottom segment to the top segment, you
can go from CABIN to SEATS and from SEATS to BOLTS.

Join the bottom segment to the top segment with this JOIN command:

JOIN SUBPART IN AIRCRAFT TO PART IN AIRCRAFT AS SUB

This creates the following recursive structure.

1080

14. Joining Data Sources

You can then produce a report on all three levels of data with this TABLE command (the field
SUBDESCRIPT describes the contents of the field SUBPART):

TABLE FILE AIRCRAFT
PRINT SUBPART BY PART BY SUBPART BY SUBDESCRIPT
END

How the JOIN Command Works

The JOIN command enables you to report from two or more related data sources with a single
request. Joined data sources remain physically separate, but are treated as one. Up to 1022
joins can be in effect at any one time.

When two data sources are joined, one is called the host file; the other is called the cross-
referenced file. Each time a record is retrieved from the host file, the corresponding fields in
the cross-referenced file are identified if they are referenced in the report request. The records
in the cross-referenced file containing the corresponding values are then retrieved.

Two data sources can be joined using a conditional join whenever you can define an
expression that determines how to relate records in the host file to records in the cross-
referenced file. Two data sources can be joined using an equijoin when they have fields in each
data source with formats (character, numeric, or date) and values in common. The common
formats ensure proper interpretation of the values. For example, suppose that you need to
read data from two data sources: one named JOB, containing job information, and a second
named SALARY, containing salary information. You can join these two data sources if each has
a field identifying the same group of employees in the same way: by last name, serial number,
or social security number. The join becomes effective when common values (for example,
common social security numbers) are retrieved for the joined fields.

After you issue the JOIN command, you can issue a single TABLE, TABLEF, MATCH FILE, or
GRAPH request to read the joined data source. You only need to specify the first data source
(host file) to produce a report from two or more data sources. For example, assume you are
writing a report from the JOB and SALARY data sources. You execute the following equijoin:

JOIN EMP_ID IN JOB TO ALL EMP_ID IN SALARY

This command joins the field EMP_ID in the JOB file to the field EMP_ID in the SALARY file.
JOB is the host file and SALARY is the cross-referenced file. You then execute this report
request:

TABLE FILE JOB
PRINT SALARY AND JOB_TITLE BY EMP_ID
END

Creating Reports With TIBCO® WebFOCUS Language

 1081

Creating an Equijoin

The first record retrieved is a JOB file record for employee #071382660. Next, all records in
the SALARY data source containing employee #071382660 are retrieved. This process
continues until all the records have been read.

You can base your join on:

Real fields that have been declared in the Master Files of the host and cross-referenced
data sources, respectively. See How to Join Real Fields on page 1082.

A virtual field in the host data source (that has either been defined in the Master File or
with a DEFINE command) and a real field that has been declared in the Master File of the
cross-referenced data source. See How to Join From a Virtual Field to a Real Field on page
1095.

A condition you specify in the JOIN command itself. See How to Create a Conditional JOIN
on page 1102.

Reference: Increasing Retrieval Speed in Joined Data Sources

You can increase retrieval speed in joined structures by using an external index. However, the
target segment for the index cannot be a cross-referenced segment. For related information,
see Improving Report Processing on page 1929.

Creating an Equijoin

The most common joined structures are based on real fields that have been declared in the
Master Files of the host and cross-referenced data sources, respectively.

Syntax:

How to Join Real Fields

The following JOIN syntax requires that the fields you are using to join the files are real fields
declared in the Master File. This join may be a simple one based on one field in each file to be
joined, or a multi-field join for data sources that support this type of behavior. The following
syntax describes the simple and multi-field variations:

JOIN [LEFT_OUTER|RIGHT_OUTER|INNER] hfld1 [AND hfld2 ...] IN hostfile [TAG
tag1]
     TO [UNIQUE|MULTIPLE]
     crfield [AND crfld2 ...] IN crfile [TAG tag2] [AS joinname]
END

where:

JOIN hfld1

Is the name of a field in the host file containing values shared with a field in the cross-
referenced file. This field is called the host field.

1082

14. Joining Data Sources

AND hfld2...

Can be an additional field in the host file, with the caveats noted below. The phrase
beginning with AND is required when specifying multiple fields.

For adapters that support multi-field and concatenated joins, and FOCUS or XFOCUS
data sources when SET NFOC=ON (the default), you can specify up to 128 fields. See
your data adapter documentation for specific information about supported join features
for each adapter.

When you are joining two FOCUS data sources, and SET NFOC=OFF, you can specify up
to four alphanumeric fields in the host file that, if concatenated, contain values shared
with the cross-referenced file. You may not specify more than one field in the cross-
referenced file when the suffix of the file is FOC. For example, assume the cross-
referenced file contains a phone number field with an area code-prefix-exchange format.
The host file has an area code field, a prefix field, and an exchange field. You can
specify these three fields to join them to the phone number field in the cross-
referenced file. The JOIN command treats the three fields as one. Other data sources
do not have this restriction on the cross-referenced file.

INNER

Specifies an inner join. If you do not specify the type of join in the JOIN command, the
ALL parameter setting determines the type of join to perform.

LEFT_OUTER

Specifies a left outer join. If you do not specify the type of join in the JOIN command,
the ALL parameter setting determines the type of join to perform.

Note that in a left outer join, host records with a missing cross-referenced instance are
included in the report output. To control how tests against missing cross-referenced
segment instances are processed, use the SET SHORTPATH command described in
Handling Records With Missing Field Values on page 1035.

RIGHT_OUTER

Specifies a right outer join. This option is available for relational data sources that
support this type of join. Using this option requires that you issue the SET
SHORTPATH = SQL command.

Note that in a right outer join, cross-referenced records with a missing host instance are
included in the report output.

IN hostfile

Is the name of the host file.

TAG tag1

Is a tag name of up to 66 characters (usually the name of the Master File), which is
used as a unique qualifier for fields and aliases in the host file.

Creating Reports With TIBCO® WebFOCUS Language

 1083

Creating an Equijoin

The tag name for the host file must be the same in all the JOIN commands of a joined
structure.

TO [UNIQUE|MULTIPLE] crfld1

Is the name of a field in the cross-referenced file containing values that match those
of hfld1 (or of concatenated host fields). This field is called the cross-referenced field.

Note: Unique returns only one instance and, if there is no matching instance in the cross-
referenced file, it supplies default values (blank for alphanumeric fields and zero for
numeric fields).

Use the MULTIPLE parameter when crfld1 may have multiple instances in common with
one value in hfld1. Note that ALL is a synonym for MULTIPLE, and omitting this parameter
entirely is a synonym for UNIQUE. See Unique and Non-Unique Joined Structures on page
1072 for more information.

AND crfld2...

Is the name of a field in the cross-referenced file with values in common with hfld2.

Note: crfld2 may be qualified. This field is only available for data adapters that support
multi-field joins.

IN crfile

Is the name of the cross-referenced file.

TAG tag2

Is a tag name of up to 66 characters (usually the name of the Master File), which is
used as a unique qualifier for fields and aliases in cross-referenced files. In a
recursive join structure, if no tag name is provided, all field names and aliases are
prefixed with the first four characters of the join name. For related information, see
Usage Notes for Recursive Joined Structures on page 1077.

The tag name for the host file must be the same in all the JOIN commands of a joined
structure.

AS joinname

Is an optional name of up to eight characters that you may assign to the join
structure. You must assign a unique name to a join structure if:

You want to ensure that a subsequent JOIN command does not overwrite it.

You want to clear it selectively later.

The structure is recursive. See Recursive Joined Structures on page 1076.

Note: If you do not assign a name to the join structure with the AS phrase, the name is
assumed to be blank. A join without a name overwrites an existing join without a name.

1084

END

Required when the JOIN command is longer than one line. It terminates the command.
It must be on a line by itself.

14. Joining Data Sources

Example:

Creating a Simple Unique Joined Structure

An example of a simple unique join is shown below:

JOIN JOBCODE IN EMPLOYEE TO JOBCODE IN JOBFILE AS JJOIN

Example:

Creating an Inner Join

The following procedure creates three FOCUS data sources:

EMPINFO, which contains the fields EMP_ID, LAST_NAME, FIRST_NAME, and
CURR_JOBCODE from the EMPINFO segment of the EMPLOYEE data source.

JOBINFO, which contains the JOBCODE and JOB_DESC fields from the JOBFILE data source.

EDINFO, which contains the EMP_ID, COURSE_CODE, and COURSE_NAME fields from the
EDUCFILE data source.

Creating Reports With TIBCO® WebFOCUS Language

 1085

Creating an Equijoin

The procedure then adds an employee to EMPINFO named Fred Newman who has no matching
record in the JOBINFO or EDINFO data sources.

TABLE FILE EMPLOYEE
SUM LAST_NAME FIRST_NAME CURR_JOBCODE
BY EMP_ID
ON TABLE HOLD AS EMPINFO FORMAT FOCUS INDEX EMP_ID CURR_JOBCODE
END
-RUN

TABLE FILE JOBFILE
SUM JOB_DESC
BY JOBCODE
ON TABLE HOLD AS JOBINFO FORMAT FOCUS INDEX JOBCODE
END
-RUN

TABLE FILE EDUCFILE
SUM COURSE_CODE COURSE_NAME
BY EMP_ID
ON TABLE HOLD AS EDINFO FORMAT FOCUS INDEX EMP_ID
END
-RUN

MODIFY FILE EMPINFO
FREEFORM EMP_ID LAST_NAME FIRST_NAME CURR_JOBCODE
MATCH EMP_ID
ON NOMATCH INCLUDE
ON MATCH REJECT
DATA
111111111, NEWMAN, FRED, C07,$
END

The following request prints the contents of EMPINFO. Note that Fred Newman has been added
to the data source:

TABLE FILE EMPINFO
PRINT *
END

1086




14. Joining Data Sources

The output is:

EMP_ID     LAST_NAME        FIRST_NAME  CURR_JOBCODE
------     ---------        ----------  ------------
071382660  STEVENS          ALFRED      A07
112847612  SMITH            MARY        B14
117593129  JONES            DIANE       B03
119265415  SMITH            RICHARD     A01
119329144  BANNING          JOHN        A17
123764317  IRVING           JOAN        A15
126724188  ROMANS           ANTHONY     B04
219984371  MCCOY            JOHN        B02
326179357  BLACKWOOD        ROSEMARIE   B04
451123478  MCKNIGHT         ROGER       B02
543729165  GREENSPAN        MARY        A07
818692173  CROSS            BARBARA     A17
111111111  NEWMAN           FRED        C07

The following JOIN command creates an inner join between the EMPINFO data source and the
JOBINFO data source.

JOIN CLEAR *
JOIN INNER CURR_JOBCODE IN EMPINFO TO MULTIPLE JOBCODE IN JOBINFO AS J0

Note that the JOIN command specifies a multiple join. In a unique join, the cross-referenced
segment is never considered missing, and all records from the host file display on the report
output. Default values (blank for alphanumeric fields and zero for numeric fields) display if no
actual data exists.

The following request displays fields from the joined structure:

TABLE FILE EMPINFO
PRINT LAST_NAME FIRST_NAME JOB_DESC
END

Fred Newman is omitted from the report output because his job code does not have a match in
the JOBINFO data source:

LAST_NAME  FIRST_NAME  JOB_DESC
---------  ----------  --------
STEVENS    ALFRED      SECRETARY
SMITH      MARY        FILE QUALITY
JONES      DIANE       PROGRAMMER ANALYST
SMITH      RICHARD     PRODUCTION CLERK
BANNING    JOHN        DEPARTMENT MANAGER
IRVING     JOAN        ASSIST.MANAGER
ROMANS     ANTHONY     SYSTEMS ANALYST
MCCOY      JOHN        PROGRAMMER
BLACKWOOD  ROSEMARIE   SYSTEMS ANALYST
MCKNIGHT   ROGER       PROGRAMMER
GREENSPAN  MARY        SECRETARY
CROSS      BARBARA     DEPARTMENT MANAGER

Creating Reports With TIBCO® WebFOCUS Language

 1087

Creating an Equijoin

Example:

Creating a Left Outer Join

The following JOIN command creates a left outer join between the EMPINFO data source and
the EDINFO data source:

JOIN CLEAR *
JOIN LEFT_OUTER EMP_ID IN EMPINFO TO MULTIPLE EMP_ID IN EDINFO AS J1

The following request displays fields from the joined structure:

TABLE FILE EMPINFO
PRINT LAST_NAME FIRST_NAME COURSE_NAME
END

All employee records display on the report output. The records for those employees with no
matching records in the EDINFO data source display the missing data character (.) in the
COURSE_NAME column. If the join were unique, blanks would display instead of the missing
data character.

LAST_NAME  FIRST_NAME  COURSE_NAME
---------  ----------  -----------
STEVENS    ALFRED      FILE DESCRPT & MAINT
SMITH      MARY        BASIC REPORT PREP FOR PROG
JONES      DIANE       FOCUS INTERNALS
SMITH      RICHARD     BASIC RPT NON-DP MGRS
BANNING    JOHN        .
IRVING     JOAN        .
ROMANS     ANTHONY     .
MCCOY      JOHN        .
BLACKWOOD  ROSEMARIE   DECISION SUPPORT WORKSHOP
MCKNIGHT   ROGER       FILE DESCRPT & MAINT
GREENSPAN  MARY        .
CROSS      BARBARA     HOST LANGUAGE INTERFACE
NEWMAN     FRED        .

Example:

Creating a Right Outer Join

The following requests generate two Microsoft SQL Server tables to join, and then issues a
request against the join.

The following request generates the WF_SALES table. The field ID_PRODUCT will be used in
the right outer join command.

TABLE FILE WF_RETAIL_LITE
SUM GROSS_PROFIT_US PRODUCT_CATEGORY PRODUCT_SUBCATEG
BY ID_PRODUCT
WHERE ID_PRODUCT FROM 2150 TO 4000
ON TABLE HOLD AS WF_SALES FORMAT SQLMSS
END

1088

14. Joining Data Sources

The following request generates the WF_PRODUCT table. The field ID_PRODUCT will be used in
the right outer join command.

TABLE FILE WF_RETAIL_LITE
SUM PRICE_DOLLARS PRODUCT_CATEGORY PRODUCT_SUBCATEG PRODUCT_NAME
BY ID_PRODUCT
WHERE ID_PRODUCT FROM 3000 TO 5000
ON TABLE HOLD AS WF_PRODUCT FORMAT SQLMSS
END

The following request issues the SET SHORTPATH=SQL and JOIN commands and displays
values from the joined tables:

SET SHORTPATH = SQL
JOIN RIGHT_OUTER ID_PRODUCT IN WF_PRODUCT TAG T1 TO ALL ID_PRODUCT IN
WF_SALES TAG T2
END
TABLE FILE WF_PRODUCT
PRINT T1.ID_PRODUCT AS 'Product ID'
PRICE_DOLLARS AS Price
T2.ID_PRODUCT AS 'Sales ID'
GROSS_PROFIT_US
BY T1.ID_PRODUCT NOPRINT
ON TABLE SET PAGE NOPAGE
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

You can generate a trace that shows the resulting SQL by adding the following commands.

SET TRACEUSER=ON
SET TRACESTAMP=OFF
SET TRACEOFF=ALL
SET TRACEON = STMTRACE//CLIENT

The trace shows that the request was optimized as a right outer join to the RDBMS.

SELECT
T1."ID_PRODUCT",
T1."PRICE_DOLLARS",
T2."ID_PRODUCT",
T2."GROSS_PROFIT_US"
FROM
( WF_PRODUCT T1
RIGHT OUTER JOIN
WF_SALES T2
ON T2."ID_PRODUCT" = T1."ID_PRODUCT" )
ORDER BY
T1."ID_PRODUCT";

Creating Reports With TIBCO® WebFOCUS Language

 1089

Creating an Equijoin

The output, shown in the following image, has a row for each ID_PRODUCT value that is in the
WF_PRODUCT table. The columns from WF_SALES rows that do not have a matching
ID_PRODUCT value display the NODATA symbol.

Example:

Creating Two Inner Joins With a Multipath Structure

The following JOIN commands create an inner join between the EMPINFO and JOBINFO data
sources and an inner join between the EMPINFO and EDINFO data sources:

JOIN CLEAR *
JOIN INNER CURR_JOBCODE IN EMPINFO TO MULTIPLE JOBCODE IN JOBINFO AS J0
JOIN INNER EMP_ID IN EMPINFO TO MULTIPLE EMP_ID IN EDINFO AS J1

1090

The structure created by the two joins has two independent paths:

14. Joining Data Sources

         SEG01
 01      S1
**************
*EMP_ID      **I
*CURR_JOBCODE**I
*LAST_NAME   **
*FIRST_NAME  **
*            **
***************
 **************
       I
       +-----------------+
       I                 I
       I SEG01           I SEG01
 02    I KM        03    I KM
..............    ..............
:EMP_ID      ::K  :JOBCODE     ::K
:COURSE_CODE ::   :JOB_DESC    ::
:COURSE_NAME ::   :            ::
:            ::   :            ::
:            ::   :            ::
:............::   :............::
 .............:    .............:
 JOINED  EDINFO    JOINED  JOBINFO

The following request displays fields from the joined structure:

SET MULTIPATH=SIMPLE
TABLE FILE EMPINFO
PRINT LAST_NAME FIRST_NAME IN 12 COURSE_NAME JOB_DESC
END

With MULTIPATH=SIMPLE, the independent paths create independent joins. All employee
records accepted by either join display on the report output. Only Fred Newman (who has no
matching record in either of the cross-referenced files) is omitted:

LAST_NAME  FIRST_NAME  COURSE_NAME                     JOB_DESC
---------  ----------  -----------                     --------
STEVENS    ALFRED      FILE DESCRPT & MAINT            SECRETARY
SMITH      MARY        BASIC REPORT PREP FOR PROG      FILE QUALITY
JONES      DIANE       FOCUS INTERNALS                 PROGRAMMER ANALYST
SMITH      RICHARD     BASIC RPT NON-DP MGRS           PRODUCTION CLERK
BANNING    JOHN        .                               DEPARTMENT MANAGER
IRVING     JOAN        .                               ASSIST.MANAGER
ROMANS     ANTHONY     .                               SYSTEMS ANALYST
MCCOY      JOHN        .                               PROGRAMMER
BLACKWOOD  ROSEMARIE   DECISION SUPPORT WORKSHOP       SYSTEMS ANALYST
MCKNIGHT   ROGER       FILE DESCRPT & MAINT            PROGRAMMER
GREENSPAN  MARY        .                               SECRETARY
CROSS      BARBARA     HOST LANGUAGE INTERFACE         DEPARTMENT MANAGER

Creating Reports With TIBCO® WebFOCUS Language

 1091

Creating an Equijoin

With MULTIPATH=COMPOUND, only employees with matching records in both of the cross-
referenced files display on the report output:

LAST_NAME  FIRST_NAME  COURSE_NAME                     JOB_DESC
---------  ----------  -----------                     --------
STEVENS    ALFRED      FILE DESCRPT & MAINT            SECRETARY
SMITH      MARY        BASIC REPORT PREP FOR PROG      FILE QUALITY
JONES      DIANE       FOCUS INTERNALS                 PROGRAMMER ANALYST
SMITH      RICHARD     BASIC RPT NON-DP MGRS           PRODUCTION CLERK
BLACKWOOD  ROSEMARIE   DECISION SUPPORT WORKSHOP       SYSTEMS ANALYST
MCKNIGHT   ROGER       FILE DESCRPT & MAINT            PROGRAMMER
CROSS      BARBARA     HOST LANGUAGE INTERFACE         DEPARTMENT MANAGER

Reference: Requirements for Cross-Referenced Fields in an Equijoin

The cross-referenced fields used in a JOIN must have the following characteristics in specific
data sources:

In relational data sources and in a CA-DATACOM/DB data source, the cross-referenced field
can be any field.

In FOCUS and XFOCUS data sources, the cross-referenced field must be indexed. Indexed
fields have the attribute FIELDTYPE=I or INDEX=I or INDEX=ON in the Master File. If the
cross-referenced field does not have this attribute, append the attribute to the field
declaration in the Master File and rebuild the file using the REBUILD utility with the INDEX
option. This adds an index to your FOCUS or XFOCUS data source.

Note: The indexed fields can be external. See the Describing Data With WebFOCUS
Language manual for more information about indexed fields and the Rebuild tool.

In IMS data sources, the cross-referenced field must be a key field in the root segment. It
can be a primary or secondary index.

In fixed format or delimited sequential files, any field can be a cross-referenced field.
However, both the host and cross-referenced file must be retrieved in ascending order on
the named (key) fields, if the command ENGINE INT CACHE SET OFF is in effect. In this
situation, if the data is not in the same sort order, errors are displayed and a many-to-many
join is not supported. However, if ENGINE INT CACHE SET ON is in effect, the files do not
have to be in ascending order and a many-to-many join is supported. ON is the default
value. A delimited file used as the cross-referenced file in the join must consist of only one
segment. If the join is based on multiple fields, a fixed format sequential file must consist
of a single segment. If the cross-referenced fixed format sequential file contains only one
segment, the host file must have a segment declaration.

1092

Reference: Restrictions on Group Fields

When group fields are used in a joined structure, the group in the host file and the group in the
cross-referenced file must have the same number of elements:

14. Joining Data Sources

In ISAM data sources, the field must be the full primary key if you issue a unique join, or an
initial subset of the primary key if you issue a non-unique join. In the Master File, the
primary key is described by a key GROUP; the initial subset is the first field in that group.

In VSAM KSDS data sources, the field must be the full primary or alternate key if you issue
a unique join, or an initial subset of the primary or alternate key if you issue a non-unique
join. In the Master File, the primary key is described by a key GROUP. The initial subset is
the first field in that group.

In VSAM ESDS data sources, the field can be any field, as long as the file is already sorted
on that field.

In Model 204 data sources, the field must be a key field. In the Access File, the types of
key fields are alphanumeric (KEY), ordered character (ORA), ordered numeric (ORN),
numeric range (RNG), invisible (IVK), and invisible range (IVR).

In ADABAS data sources, the field must be a descriptor field, a superdescriptor defined
with the .SPR or .NOP field name suffix, or a subdescriptor defined with the .NOP field
name suffix. The field description in the Master File must contain the attribute
FIELDTYPE=I.

In the Access File, the cross-referenced segment must specify ACCESS=ADBS and either
CALLTYPE=FIND or CALLTYPE=RL. If CALLTYPE=RL, the host field can be joined to the high-
order portion of a descriptor, superdescriptor, or subdescriptor, if the high-order portion is
longer than the host field.

In CA-IDMS/DB data sources, the field must be an indexed field on a network record
identified by the attribute FIELDTYPE=I in the Master File, a CA-IDMS/DB CALC field on a
network record identified by the CLCFLD phrase in the Access File, or any field on an LRF or
ASF record.

For a partial key join using fixed format or delimited sequential files, the setting ENGINE INT
CACHE SET OFF must be in effect.

Reference: Usage Notes for Inner and Outer JOIN Command Syntax

The SET ALL and SET CARTESIAN commands are ignored by the syntax.

The ALL. parameter is not supported. If the ALL. parameter is used, the following message
displays:

Creating Reports With TIBCO® WebFOCUS Language

 1093

Creating an Equijoin

(FOC32452) Use of ALL. with LEFT_OUTER/INNER not allowed

If you define multiple joins, the resulting structure can be a single path or multi-path data
source.

If the setting MULTIPATH=SIMPLE is in effect and the report is based on multiple paths,
each of the individual joins is constructed separately without regard to the other joins,
and the matching records from each of the separate paths displays on the report
output. Therefore, the output can contain records that would have been omitted if only
one of the joins was in effect.

If the setting MULTIPATH=COMPOUND is in effect with a multi-path report, or if the
report displays data only from a single path, the report output displays only those
records that satisfy all of the joins.

Joining From a Virtual Field to a Real Field Using an Equijoin

You can use DEFINE-based JOIN syntax to create a virtual host field that you can join to a real
cross-referenced field. The DEFINE expression that creates the virtual host field may contain
only fields in the host file and constants. (It may not contain fields in the cross-referenced file.)
You can do more than one join from a virtual field.

You can create the virtual host field in a separate DEFINE command or in a Master File. For
information on Master Files, see the Describing Data With WebFOCUS Language manual.

The same report request can use JOIN-based virtual fields, and virtual fields unrelated to the
join.

Note that if you are creating a virtual field in a DEFINE command, you must issue the DEFINE
after the JOIN command, but before the TABLE request since a JOIN command clears all fields
created by DEFINE commands for the host file and the joined structure. Virtual fields defined in
Master Files are not cleared.

Tip: If a DEFINE command precedes the JOIN command, you can set KEEPDEFINES ON to
reinstate virtual fields during the parsing of a subsequent JOIN command. For more
information, see Preserving Virtual Fields Using KEEPDEFINES on page 1144.

1094

Syntax:

How to Join From a Virtual Field to a Real Field

14. Joining Data Sources

The DEFINE-based JOIN command enables you to join a virtual field in the host file to a real
field in the cross-referenced file. The syntax is:

JOIN [LEFT_OUTER|RIGHT_OUTER|INNER] deffld WITH host_field ...
     IN hostfile [TAG tag1]
     TO [UNIQUE|MULTIPLE]
     cr_field IN crfile [TAG tag2] [AS joinname]
END

where:

JOIN deffld

Is the name of a virtual field for the host file (the host field). The virtual field can be
defined in the Master File or with a DEFINE command. For related information, see
Notes on Using Virtual Fields With Joined Data Sources on page 1097.

WITH host_field

Is the name of any real field in the host segment with which you want to associate the
virtual field. This association is required to locate the virtual field.

Note: The WITH field referenced in the JOIN command must be in the same segment as
the WITH field referenced in the DEFINE that creates the virtual field or no output will be
produced.

The WITH phrase is required unless the KEEPDEFINES parameter is set to ON and deffld
was defined prior to issuing the JOIN command.

To determine which segment contains the virtual field, use the ? DEFINE query after
issuing the DEFINE command. See the Developing Reporting Applications manual for
details about Query commands.

INNER

Specifies an inner join. If you do not specify the type of join in the JOIN command, the
ALL parameter setting determines the type of join to perform.

LEFT_OUTER

Specifies a left outer join. If you do not specify the type of join in the JOIN command,
the ALL parameter setting determines the type of join to perform.

RIGHT_OUTER

Specifies a right outer join. This option is available for relational data sources that
support this type of join. The SET SHORTPATH = SQL command must be in effect in
order to issue a right outer join.

IN hostfile

Is the name of the host file.

Creating Reports With TIBCO® WebFOCUS Language

 1095

Creating an Equijoin

TAG tag1

Is a tag name of up to 66 characters (usually the name of the Master File), which is
used as a unique qualifier for fields and aliases in host files.

The tag name for the host file must be the same in all JOIN commands of a joined
structure.

TO [UNIQUE|MULTIPLE] crfld1

Is the name of a real field in the cross-referenced data source whose values match
those of the virtual field. This must be a real field declared in the Master File.

Note: UNIQUE returns only one instance and, if there is no matching instance in the cross-
referenced file, it supplies default values (blank for alphanumeric fields and zero for
numeric fields).

Use the MULTIPLE parameter when crfld1 may have multiple instances in common with
one value in hfld1. Note that ALL is a synonym for MULTIPLE, and omitting this parameter
entirely is a synonym for UNIQUE. See Unique and Non-Unique Joined Structures on page
1072 for more information.

IN crfile

Is the name of the cross-referenced file.

TAG tag2

Is a tag name of up to 66 characters (usually the name of the Master File), which is
used as a unique qualifier for fields and aliases in cross-referenced files. In a
recursive joined structure, if no tag name is provided, all field names and aliases are
prefixed with the first four characters of the join name. For related information, see
Unique and Non-Unique Joined Structures on page 1072.

The tag name for the host file must be the same in all JOIN commands of a joined
structure.

AS joinname

Is an optional name of up to eight characters that you may assign to the joined
structure. You must assign a unique name to a join structure if:

You want to ensure that a subsequent JOIN command does not overwrite it.

You want to clear it selectively later.

The structure is recursive, and you do not specify tag names. See Recursive Joined
Structures on page 1076.

If you do not assign a name to the joined structure with the AS phrase, the name is
assumed to be blank. A join without a name overwrites an existing join without a name.

1096

14. Joining Data Sources

END

Required when the JOIN command is longer than one line. It terminates the command.
It must be on a line by itself.

Reference: Notes on Using Virtual Fields With Joined Data Sources

Requests reading joined data sources can contain virtual fields that are defined either:

In the Master File of the host data source.

In a DEFINE command, in which the syntax

DEFINE FILE hostfile

identifies the host data source in the joined structure.

Note: The expression defining the host field for the join can use only host fields and
constants.

All other virtual fields can contain real fields from the host file and the cross-referenced file.

Tip: Since issuing the JOIN command clears all DEFINE commands for the host file and the
joined structure, you must issue the DEFINE command after the JOIN or turn KEEPDEFINES
ON to preserve the virtual fields. For more information, see Preserving Virtual Fields During
Join Parsing on page 1143.

Example:

Creating a Virtual Host Field for a Joined Structure

Suppose that a retail chain sends four store managers to attend classes. Each person,
identified by an ID number, manages a store in a different city. The stores and the cities in
which they are located are contained in the SALES data source. The manager IDs, the classes,
and dates the managers attended are contained in the EDUCFILE data source.

The following procedure lists the courses that the managers attended, identifying the
managers by the cities in which they work. Note the three elements in the procedure:

The JOIN command joins the SALES data source to the EDUCFILE data source, based on
the values common to the ID_NUM field (which contains manager IDs) in SALES and the
EMP_ID field in EDUCFILE. Note that the ID_NUM field does not exist yet and will be
created by the DEFINE command.

The DEFINE command creates the ID_NUM field, assigning to it the IDs of the managers
working in the four cities.

The TABLE command produces the report.

Creating Reports With TIBCO® WebFOCUS Language

 1097

Creating an Equijoin

The procedure is:

JOIN ID_NUM WITH CITY IN SALES TO ALL EMP_ID IN EDUCFILE AS SALEDUC

DEFINE FILE SALES
ID_NUM/A9 = DECODE CITY ('NEW YORK' 451123478 'NEWARK' 119265415
                         'STAMFORD' 818692173 'UNIONDALE' 112847612);
END

TABLE FILE SALES
PRINT DATE_ATTEND BY CITY BY COURSE_NAME
END

The output is:

CITY                    COURSE_NAME                 DATE_ATTEND
----                    -----------                 -----------
NEW YORK                FILE DESCRPT & MAINT           81/11/15
NEWARK                  BASIC RPT NON-DP MGRS          82/08/24
STAMFORD                BASIC REPORT PREP DP MGRS      82/08/02
                        HOST LANGUAGE INTERFACE        82/10/21
UNIONDALE               BASIC REPORT PREP FOR PROG     81/11/16
                        FILE DESCRPT & MAINT           81/11/15

Join Modes in an Equijoin

The JOIN_LENGTH_MODE (JOINLM) parameter controls processing of equality joined field pairs
for record-based non-SQL Adapters, such as DFIX, VSAM, and FIX. This setting controls
processing when two alphanumeric fields of different lengths or two numeric fields of different
data types and precisions are joined.

For SQL data sources, joins are normally either optimized (sent to the SQL engine for
processing) or managed to comply with SQL processing rules.

There are two supported modes of handling compatible, but not identical, joined fields:

SQL compliance mode. The JOIN command processor assures strict value equality of
joined fields. Detected truncation of significant characters during host to cross-referenced
conversion generates atarget not found condition, in which case the join is not done. If a
shorter host field is joined to a longer cross-referenced file, the shorter host field value is
extended to the length of the cross-referenced field with non-significant characters,
according to the data type, and the join is processed.

FOCUS reporting mode. The JOIN command processor assures partial value equality of
joined fields.

When joining a shorter to a longer field, a search range is created to find all cross-
referenced values that are prefixed with the host value.

1098

14. Joining Data Sources

When joining a longer to a shorter field, the host value is unconditionally truncated to
the cross referenced field length. If the truncation removes non-blank characters, the
match will not be done and the comparison will fail, rejecting the records.

Syntax:

How to Control the Join Mode for Record-Based Data Sources

SET JOIN_LENGTH_MODE|JOINLM} = {SQL|RANGE}

where:

SQL

Sets SQL compliant mode. which assures strict equality between host and cross-
referenced field values. This is the default value.

RANGE

Sets FOCUS reporting mode, which supports partial key joins.

Data Formats of Shared Fields

Generally, the fields containing the shared values in the host and cross-referenced files must
have the same data formats.

If you specify multiple host file fields, the JOIN command treats the fields as one concatenated
field. Add the field format lengths to obtain the length of the concatenated field. You must
observe the following rules:

If the host field is alphanumeric, the cross-referenced field must also be alphanumeric and
have the same length.

The formats may have different edit options.

Note that a text field cannot be used to join data sources.

If the host field is a numeric field, the host field format, as specified by the USAGE (or
FORMAT) attribute in the Master File, must agree in type (I, P, F, or D) with the format of the
cross-referenced field as specified by the USAGE (or FORMAT) attribute. For details, see
Joining Fields With Different Numeric Data Types on page 1100.

Creating Reports With TIBCO® WebFOCUS Language

 1099

Creating an Equijoin

The edit options may differ. The length may also differ, but with the following effect:

If the format of the host field (as specified by the USAGE attribute) is packed decimal
(P) or integer (I) and is longer than the cross-referenced field format (specified by the
USAGE attribute for FOCUS data sources or the ACTUAL attribute for other data
sources), only the length of the cross-referenced field format is compared, using only
the right-most digits of the shorter field. For example, if a five-digit packed decimal
format field is joined to a three-digit packed decimal format field, when a host record
with a five-digit number is retrieved, all cross-referenced records with the last three
digits of that number are also retrieved.

If the format of the host field is double precision (D), the left-most eight bytes of each
field are compared.

If the host field is a date field, the cross-referenced field must also be a date field. Date
and date-time fields must have the same components, not necessarily in the same order.

The host and cross-referenced fields can be described as groups in the Master File if they
contain the same number of component fields. The corresponding component fields in each
group (for example, the first field in the host group and the first field in the cross-referenced
group) must obey the above rules. For related information, see Restrictions on Group Fields
on page 1093.

If the host field is not a group field, the cross-referenced field can still be a group. If the
host field is a group, the cross-referenced field must also be a group.

Joining Fields With Different Numeric Data Types

You can join two or more data sources containing different numeric data types. For example,
you can join a field with a short packed decimal format to a field with a long packed decimal
format, or a field with an integer format to a field with a packed decimal format. This provides
enormous flexibility for creating reports from joined data sources.

When joining a shorter field to a longer field, the cross-referenced value is padded to the
length of the host field, adding spaces (for alpha fields) or hexadecimal zeros (for numeric
fields). This new value is used for searches in the cross-referenced file.

When joining a longer field to a shorter field, the FROM value is truncated. If part of your
value is truncated due to the length of the USAGE in the cross-referenced file, only records
matching the truncated value will be found in the cross-referenced file.

Note:

For comparison on packed decimal fields to be accomplished properly, all signs for positive
values are converted to hex C and all signs for negative values are converted to hex D.

1100

The JOINOPT parameter also corrects for lagging values in a unique join. For information,
see How to Correct for Lagging Values With a Unique Join on page 1074.

14. Joining Data Sources

Syntax:

How to Enable Joins With Data Type Conversion

To enable joins with data type conversion, issue the command

SET JOINOPT = [GNTINT|OLD]

where:

GNTINT

Enables joins with data type conversion.

OLD

Disables joins with data type conversion. This value is the default.

Example:

Issuing Joins With Data Type Conversion

Since you can join a field with a short packed decimal format to a field with a long packed
decimal format, a join can be defined in the following Master Files:

FILE=PACKED,SUFFIX=FIX,$
  SEGNAME=ONE,SEGTYPE=S0
   FIELD=FIRST,,P8,P4,INDEX=I,$

FILE=PACKED2,SUFFIX=FIX,$
  SEGNAME=ONE,SEGTYPE=S0
   FIELD=PFIRST,,P31,P16,INDEX=I,$

The JOIN command might look like this:

JOIN FIRST IN PACKED TO ALL PFIRST IN PACKED2 AS J1

When joining packed fields, the preferred sign format of X'C' for positive values and X'D' for
negative values is still required. All other non-preferred signs are converted to either X'C' or
X'D'.

Using a Conditional Join

Using conditional JOIN syntax, you can establish joins based on conditions other than equality
between fields. In addition, the host and cross-referenced join fields do not have to contain
matching formats, and the cross-referenced field does not have to be indexed.

The conditional join is supported for FOCUS and for VSAM, ADABAS, IMS, IDMS, and all
relational data sources. Because each data source differs in its ability to handle complex
WHERE criteria, the optimization of the conditional JOIN syntax differs depending on the
specific data sources involved in the join and the complexity of the WHERE criteria.

Creating Reports With TIBCO® WebFOCUS Language

 1101

Using a Conditional Join

The standard ? JOIN command lists every join currently in effect, and indicates any that are
based on WHERE criteria.

Syntax:

How to Create a Conditional JOIN

The syntax of the conditional (WHERE-based) JOIN command is

JOIN [LEFT_OUTER|RIGHT_OUTER|INNER] FILE hostfile AT hfld1     [WITH
hfld2] [TAG tag1]
     TO {UNIQUE|MULTIPLE}
     FILE crfile AT crfld [TAG tag2] [AS joinname]
     [WHERE expression1;
     [WHERE expression2;
     ...]
END

where:

INNER

Specifies an inner join. If you do not specify the type of join in the JOIN command, the ALL
parameter setting determines the type of join to perform.

LEFT_OUTER

Specifies a left outer join. If you do not specify the type of join in the JOIN command, the
ALL parameter setting determines the type of join to perform.

RIGHT_OUTER

Specifies a right outer join. The command SET SHORTPATH = SQL must be in effect.

hostfile

Is the host Master File.

AT

Links the correct parent segment or host to the correct child or cross-referenced segment.
The field values used as the AT parameter are not used to cause the link. They are simply
used as segment references.

hfld1

Is a field name in the host Master File whose segment will be joined to the cross-
referenced data source. The field name must be at the lowest level segment in its data
source that is referenced.

tag1

Is the optional tag name of up to 66 characters that is used as a unique qualifier for fields
and aliases in the host data source.

1102

14. Joining Data Sources

hfld2

Is a data source field with which to associate a DEFINE-based conditional JOIN. For a
DEFINE-based conditional join, the KEEPDEFINES setting must be ON, and you must create
the virtual fields before issuing the JOIN command.

MULTIPLE

Specifies a one-to-many relationship between hostfile and crfile. Note that ALL is a
synonym for MULTIPLE.

UNIQUE

Specifies a one-to-one relationship between hostfile and crfile. Note that ONE is a synonym
for UNIQUE.

Note: Regardless of the character of the JOIN—INNER or LEFT_OUTER—the join to UNIQUE
will return only one instance of the cross-referenced file, and if this instance does not
match based on the evaluation of the WHERE expression, default values (spaces for
alphanumeric fields and 0 for numerical fields) are returned. There are never short paths
or missing values in the cross-referenced file.

crfile

Is the cross-referenced Master File.

crfld

Is a field name in the cross-referenced Master File. It can be any field in the segment.

tag2

Is the optional tag name of up to 66 characters that is used as a unique qualifier for fields
and aliases in the cross-referenced data source.

joinname

Is the name associated with the joined structure.

expression1, expression2

Are any expressions that are acceptable in a DEFINE FILE command. All fields used in the
expressions must lie on a single path.

You must include the connection between the tables in the WHERE conditions. The AT
references do not actually perform a JOIN between the fields as with a standard JOIN.

If you do not include any WHERE conditions in the join, a cartesian product is generated.

END

The END command is required to terminate the command and must be on a line by itself.

Creating Reports With TIBCO® WebFOCUS Language

 1103

Using a Conditional Join

Note: Single line JOIN syntax is not supported.

Example:

Using a Conditional Join

The following example joins the VIDEOTRK and MOVIES data sources on the conditions that:

The transaction date (in VIDEOTRK) is more than ten years after the release date (in
MOVIES).

The movie codes match in both data sources.

The join is performed at the segment that contains MOVIECODE in the VIDEOTRK data source,
because the join must occur at the lowest segment referenced.

The following request displays the title, most recent transaction date, and release date for
each movie in the join, and computes the number of years between this transaction date and
the release date:

JOIN FILE VIDEOTRK AT MOVIECODE TAG V1 TO ALL
     FILE MOVIES   AT RELDATE   TAG M1 AS JW1
  WHERE DATEDIF(RELDATE, TRANSDATE,'Y') GT 10;
  WHERE V1.MOVIECODE EQ M1.MOVIECODE;
END
TABLE FILE VIDEOTRK
 SUM TITLE/A25 AS 'Title'
     TRANSDATE AS 'Last,Transaction'
     RELDATE AS 'Release,Date'
 COMPUTE YEARS/I5 = (TRANSDATE - RELDATE)/365;  AS 'Years,Difference'
 BY TITLE NOPRINT
 BY HIGHEST 1 TRANSDATE NOPRINT
END

1104

14. Joining Data Sources

The output is:

                           Last         Release   Years
Title                      Transaction  Date      Difference
-----                      -----------  -------   ----------
ALICE IN WONDERLAND        91/06/22     51/07/21          39
ALIEN                      91/06/18     80/04/04          11
ALL THAT JAZZ              91/06/25     80/05/11          11
ANNIE HALL                 91/06/24     78/04/16          13
BAMBI                      91/06/22     42/07/03          49
BIRDS, THE                 91/06/23     63/09/27          27
CABARET                    91/06/25     73/07/14          17
CASABLANCA                 91/06/27     42/03/28          49
CITIZEN KANE               91/06/22     41/08/11          49
CYRANO DE BERGERAC         91/06/20     50/11/09          40
DEATH IN VENICE            91/06/26     73/07/27          17
DOG DAY AFTERNOON          91/06/23     76/04/04          15
EAST OF EDEN               91/06/20     55/01/12          36
GONE WITH THE WIND         91/06/24     39/06/04          52
JAWS                       91/06/27     78/05/13          13
MALTESE FALCON, THE        91/06/19     41/11/14          49
MARTY                      91/06/19     55/10/26          35
NORTH BY NORTHWEST         91/06/21     59/02/09          32
ON THE WATERFRONT          91/06/24     54/07/06          36
PHILADELPHIA STORY, THE    91/06/21     40/05/06          51
PSYCHO                     91/06/17     60/05/16          31
REAR WINDOW                91/06/17     54/12/15          36
SHAGGY DOG, THE            91/06/25     59/01/09          32
SLEEPING BEAUTY            91/06/24     75/08/30          15
TIN DRUM, THE              91/06/17     80/03/01          11
VERTIGO                    91/06/27     58/11/25          32

Full Outer Joins

The WebFOCUS join command and conditional join command have a FULL OUTER join option.

A full outer join returns all rows from the source data source and all rows from the target data
source. Where values do not exist for the rows in either data source, null values are returned.
WebFOCUS substitutes default values on the report output (blanks for alphanumeric columns,
the NODATA symbol for numeric columns).

Full outer joins and right outer joins are supported whether or not the underlying data source
supports them. When the underlying data source has support for these joins, the join
processing is passed to the database engine. When it does not support them, all necessary
data is returned and the join processing is handled by WebFOCUS.

Note: The command SET SHORTPATH = SQL must be in effect in order to issue a full outer
join.

Syntax:

How to Specify a Full Outer Join

The following syntax generates a full outer equijoin based on real fields:

Creating Reports With TIBCO® WebFOCUS Language

 1105

Full Outer Joins

JOIN FULL_OUTER hfld1 [AND hfld2 ...] IN table1 [TAG tag1] TO {UNIQUE|
MULTIPLE} cfld [AND cfld2 ...] IN table2 [TAG tag2] [AS joinname]
END

where:

hfld1

Is the name of a field in the host table containing values shared with a field in the cross-
referenced table. This field is called the host field.

AND hfld2...

Can be an additional field in the host table. The phrase beginning with AND is required
when specifying multiple fields.

For relational adapters that support multi-field and concatenated joins, you can specify
up to 20 fields. See your adapter documentation for specific information about
supported join features.

IN table1

Is the name of the host table.

TAG tag1

Is a tag name of up to 66 characters (usually the name of the Master File), which is used
as a unique qualifier for fields and aliases in the host table.

The tag name for the host table must be the same in all the JOIN commands of a joined
structure.

TO [UNIQUE|MULTIPLE] crfld1

Is the name of a field in the cross-referenced table containing values that match those of
hfld1 (or of concatenated host fields). This field is called the cross-referenced field.

Note: UNIQUE returns only one instance and, if there is no matching instance in the cross-
referenced table, it returns null values.

Use the MULTIPLE parameter when crfld1 may have multiple instances in common with
one value in hfld1. Note that ALL is a synonym for MULTIPLE, and omitting this parameter
entirely is a synonym for UNIQUE.

AND crfld2...

Is the name of a field in the cross-referenced table with values in common with hfld2.

Note: crfld2 may be qualified. This field is only available for adapters that support multi-
field joins.

1106

14. Joining Data Sources

IN crfile

Is the name of the cross-referenced table.

TAG tag2

Is a tag name of up to 66 characters (usually the name of the Master File), which is used
as a unique qualifier for fields and aliases in cross-referenced tables. In a recursive join
structure, if no tag name is provided, all field names and aliases are prefixed with the first
four characters of the join name.

The tag name for the host table must be the same in all the JOIN commands of a joined
structure.

AS joinname

Is an optional name of up to eight characters that you may assign to the join structure.
You must assign a unique name to a join structure if:

You want to ensure that a subsequent JOIN command does not overwrite it.

You want to clear it selectively later.

The structure is recursive.

Note: If you do not assign a name to the join structure with the AS phrase, the name is
assumed to be blank. A join without a name overwrites an existing join without a name.

END

Required when the JOIN command is longer than one line. It terminates the command and
must be on a line by itself.

The following syntax generates a DEFINE-based full outer join:

JOIN FULL_OUTER deffld WITH host_field ...
     IN table1 [TAG tag1]
     TO [UNIQUE|MULTIPLE]
     cr_field IN table2 [TAG tag2] [AS joinname]
END

where:

deffld

Is the name of a virtual field for the host file (the host field). The virtual field can be
defined in the Master File or with a DEFINE command.

WITH host_field

Is the name of any real field in the host segment with which you want to associate the
virtual field. This association is required to locate the virtual field.

Creating Reports With TIBCO® WebFOCUS Language

 1107

Full Outer Joins

The WITH phrase is required unless the KEEPDEFINES parameter is set to ON and deffld
was defined prior to issuing the JOIN command.

To determine which segment contains the virtual field, use the ? DEFINE query after
issuing the DEFINE command.

IN table1

Is the name of the host table.

TAG tag1

Is a tag name of up to 66 characters (usually the name of the Master File), which is used
as a unique qualifier for fields and aliases in host tables.

The tag name for the host table must be the same in all JOIN commands of a joined
structure.

TO [UNIQUE|MULTIPLE] crfld1

Is the name of a real field in the cross-referenced table whose values match those of the
virtual field. This must be a real field declared in the Master File.

Note: UNIQUE returns only one instance and, if there is no matching instance in the cross-
referenced table, it returns null values.

Use the MULTIPLE parameter when crfld1 may have multiple instances in common with
one value in hfld1. Note that ALL is a synonym for MULTIPLE, and omitting this parameter
entirely is a synonym for UNIQUE.

IN crfile

Is the name of the cross-referenced table.

TAG tag2

Is a tag name of up to 66 characters (usually the name of the Master File), which is used
as a unique qualifier for fields and aliases in cross-referenced tables. In a recursive joined
structure, if no tag name is provided, all field names and aliases are prefixed with the first
four characters of the join name.

The tag name for the host file must be the same in all JOIN commands of a joined
structure.

AS joinname

Is an optional name of up to eight characters that you may assign to the joined structure.
You must assign a unique name to a join structure if:

You want to ensure that a subsequent JOIN command does not overwrite it.

1108

14. Joining Data Sources

You want to clear it selectively later.

The structure is recursive, and you do not specify tag names.

If you do not assign a name to the joined structure with the AS phrase, the name is
assumed to be blank. A join without a name overwrites an existing join without a name.

END

Required when the JOIN command is longer than one line. It terminates the command and
must be on a line by itself.

The following syntax generates a full outer conditional join:

JOIN FULL_OUTER FILE table1 AT hfld1 [WITH hfld2] [TAG tag1]
     TO {UNIQUE|MULTIPLE}
     FILE table2 AT crfld [TAG tag2] [AS joinname]
     [WHERE expression1;
     [WHERE expression2;
     ...]
END

where:

table1

Is the host Master File.

AT

Links the correct parent segment or host to the correct child or cross-referenced segment.
The field values used as the AT parameter are not used to cause the link. They are used
as segment references.

hfld1

Is the field name in the host Master File whose segment will be joined to the cross-
referenced table. The field name must be at the lowest level segment in its data source
that is referenced.

tag1

Is the optional tag name that is used as a unique qualifier for fields and aliases in the
host table.

hfld2

Is a table column with which to associate a DEFINE-based conditional JOIN. For a DEFINE-
based conditional join, the KEEPDEFINES setting must be ON, and you must create the
virtual fields before issuing the JOIN command.

Creating Reports With TIBCO® WebFOCUS Language

 1109

Full Outer Joins

MULTIPLE

Specifies a one-to-many relationship between table1 and table2. Note that ALL is a
synonym for MULTIPLE.

UNIQUE

Specifies a one-to-one relationship between table1 and table2. Note that ONE is a synonym
for UNIQUE.

Note: The join to UNIQUE will return only one instance of the cross-referenced table, and if
this instance does not match based on the evaluation of the WHERE expression, null
values are returned.

crfile

Is the cross-referenced Master File.

crfld

Is the join field name in the cross-referenced Master File. It can be any field in the
segment.

tag2

Is the optional tag name that is used as a unique qualifier for fields and aliases in the
cross-referenced table.

joinname

Is the name associated with the joined structure.

expression1, expression2

Are any expressions that are acceptable in a DEFINE FILE command. All fields used in the
expressions must lie on a single path.

END

The END command is required to terminate the command and must be on a line by itself.

Example:

Optimizing a Full Outer Join of Microsoft SQL Server Tables

The following requests generate two Microsoft SQL Server tables to join, and then issues a
request against the join. The tables are generated using the wf_retail sample that you can
create using the WebFOCUS - Retail Demo tutorial in the server Web Console.

The following request generates the WF_SALES table. The field ID_PRODUCT will be used in
the full outer join command. The generated table will contain ID_PRODUCT values from 2150
to 4000:

1110

14. Joining Data Sources

TABLE FILE WF_RETAIL_LITE
SUM GROSS_PROFIT_US PRODUCT_CATEGORY PRODUCT_SUBCATEG
BY ID_PRODUCT
WHERE ID_PRODUCT FROM 2150 TO 4000
ON TABLE HOLD AS WF_SALES FORMAT SQLMSS
END

The following request generates the WF_PRODUCT table. The field ID_PRODUCT will be used in
the full outer join command. The generated table will contain ID_PRODUCT values from 3000
to 5000:

TABLE FILE WF_RETAIL_LITE
SUM PRICE_DOLLARS PRODUCT_CATEGORY PRODUCT_SUBCATEG PRODUCT_NAME
BY ID_PRODUCT
WHERE ID_PRODUCT FROM 3000 TO 5000
ON TABLE HOLD AS WF_PRODUCT FORMAT SQLMSS
END

The following request issues the SET SHORTPATH = SQL and JOIN commands and displays
values from the joined tables:

SET SHORTPATH = SQL
SET TRACEUSER=ON
SET TRACESTAMP=OFF
SET TRACEOFF=ALL
SET TRACEON = STMTRACE//CLIENT
JOIN FULL_OUTER ID_PRODUCT IN WF_PRODUCT TAG T1
 TO ALL ID_PRODUCT IN WF_SALES TAG T2
END
TABLE FILE WF_PRODUCT
PRINT T1.ID_PRODUCT AS 'Product ID'
PRICE_DOLLARS AS Price
T2.ID_PRODUCT AS 'Sales ID'
GROSS_PROFIT_US
BY T1.ID_PRODUCT NOPRINT
ON TABLE SET PAGE NOPAGE
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1111

Full Outer Joins

The trace shows that the full outer join was optimized (translated to SQL) so that SQL Server
could process the join:

SELECT
T1."ID_PRODUCT",
T1."PRICE_DOLLARS",
T2."ID_PRODUCT",
T2."GROSS_PROFIT_US"
FROM
( WF_PRODUCT T1
FULL OUTER JOIN
WF_SALES T2
ON T2."ID_PRODUCT" = T1."ID_PRODUCT" )
ORDER BY
T1."ID_PRODUCT";

1112

14. Joining Data Sources

The output has a row for each ID_PRODUCT value that is in either table. Rows with
ID_PRODUCT values from 2150 to 2167 are only in the WF_SALES table, so the columns from
WF_PRODUCT display the NODATA symbol. Rows with ID_PRODUCT values above 4000 are
only in the WF_PRODUCT table, so the columns from WF_SALES display the NODATA symbol.
Rows with ID_PRODUCT values from 2000 to 4000 are in both tables, so all columns have
values, as shown in the following image.

Reporting Against a Multi-Fact Cluster Synonym

A cluster synonym is a synonym in which each segment is added to the cluster by reference
using a CRFILE attribute that points to the base synonym. Child segments are joined to their
parents using a JOIN WHERE attribute. A cluster Master File can have multiple root segments.
In this case, the root segments are usually fact tables and the child segments are usually
dimension tables, as found in a star schema. This type of structure is called a multi-fact
cluster.

Creating Reports With TIBCO® WebFOCUS Language

 1113

Reporting Against a Multi-Fact Cluster Synonym

A dimension table can be a child of multiple fact tables (called a shared dimension) or be a
child of a single fact table (called a non-shared dimension). In most cases, the fact tables are
used for aggregation and the dimension tables are used for sorting.

The following image shows a simple multi-fact structure.

For information about creating a multi-fact cluster Master File, see the Describing Data With
WebFOCUS Language manual.

The following list shows the rules for creating a report request against a multi-fact cluster
Master File.

You can report against only the fact tables, as long as you aggregate (SUM) at least one
fact from each fact table and have at most one sort phrase.

The first sort field in the request must be from a shared dimension.

Any number of shared dimensions can be referenced in the request.

Multiple non-shared dimensions can be included in the request, as long as they have the
same parent. More than one non-shared dimension from different parents cannot be
referenced in a request.

The MATCH FILE command is not supported for reporting against a multi-fact synonym.

1114

14. Joining Data Sources

Example:

Reporting Against a Multi-Fact Cluster Synonym

The following request against the WF_RETAIL_LITE multi-fact cluster synonym sums the
COGS_US measure from the WF_RETAIL_SALES segment and the DAYSDELAYED measure
from the WF_RETAIL_SHIPMENTS segment. The first BY field, BRAND, is in the shared
dimension WF_RETAIL_PRODUCT. The second BY field, TIME_QTR, is from the non-shared
dimension WF_RETAIL_TIME_DELIVERED.

TABLE FILE WF_RETAIL_LITE
SUM COGS_US DAYSDELAYED
BY BRAND
BY WF_RETAIL_TIME_DELIVERED.TIME_QTR
WHERE BRAND EQ 'Denon' OR 'Grado'
WHERE DAYSDELAYED GT 1
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
INCLUDE=IBFS:/FILE/IBI_HTML_DIR/ibi_themes/Warm.sty,$
END

The output is shown in the following image. The sum of DAYSDELAYED is totaled for each
value of the shared dimension and, within each value of the shared dimension, for each value
of the non-shared dimension.

Adding a New Fact To Multi-Fact Synonyms: JOIN AS_ROOT

The JOIN AS_ROOT command adds a new fact table as an additional root to an existing fact-
based cluster (star schema). The source Master File has a parent fact segment and at least
one child dimension segment. The JOIN AS_ROOT command supports a unique join from a
child dimension segment (at any level) to an additional fact parent.

Creating Reports With TIBCO® WebFOCUS Language

 1115

Reporting Against a Multi-Fact Cluster Synonym

Syntax:

How to Add an Additional Parent Segment

JOIN AS_ROOT sfld1 [AND sfld2 ...] IN [app1/]sfile TO UNIQUE tfld1 [AND
tfld2 ...] IN [app2/]tfile AS jname
END

where:

sfld1 [AND sfld2 ...]

Are fields in the child (dimension) segment of the source file that match values of fields in
the target file.

[app1/]sfile

Is the source file.

TO UNIQUE tfld1 [AND tfld2 ...]

Are fields in the target file that match values of fields in the child segment of the source
file. The join must be unique.

[app2/]tfile

Is the target file.

jname

Is the join name.

END

Is required to end the JOIN command.

Example:

Joining AS_ROOT From the WebFOCUS Retail Data Source to an Excel File

The following request joins the product category and product subcategory fields in the
WebFOCUS Retail data source to an Excel file named PROJECTED.

1116

To generate the WebFOCUS Retail data source in the Web Console, click Tutorials from the
Applications page.

14. Joining Data Sources

Select WebFOCUS - Retail Demo. Select your configured relational adapter (or select the flat file
option if you do not have a relational adapter configured), check Limit Tutorial Data, and then
click Create.

The Master File for the Excel File is:

FILENAME=PROJECTED, SUFFIX=DIREXCEL,
 DATASET=app2/projected.xlsx, $
  SEGMENT=PROJECTED, SEGTYPE=S0, $
    FIELDNAME=PRODUCT_CATEGORY, ALIAS='Product  Category', USAGE=A16V,
ACTUAL=A16V,
      MISSING=ON,
      TITLE='Product  Category',
      WITHIN='*PRODUCT', $
    FIELDNAME=PRODUCT_SUBCATEGORY, ALIAS='Product     Subcategory',
USAGE=A25V, ACTUAL=A25V,
      MISSING=ON,
      TITLE='Product     Subcategory',
      WITHIN=PRODUCT_CATEGORY, $
    FIELDNAME=PROJECTED_COG, ALIAS='              Projected COG',
USAGE=P15.2C, ACTUAL=A15,
      MISSING=ON,
      TITLE='              Projected COG', MEASURE_GROUP=PROJECTED,
      PROPERTY=MEASURE,  $
    FIELDNAME=PROJECTED_SALE_UNITS, ALIAS='             Projected Sale
Units', USAGE=I9, ACTUAL=A11,
      MISSING=ON,
      TITLE='             Projected Sale Units', MEASURE_GROUP=PROJECTED,
      PROPERTY=MEASURE,  $
 MEASUREGROUP=PROJECTED, CAPTION='PROJECTED', $
 DIMENSION=PRODUCT, CAPTION='Product', $
  HIERARCHY=PRODUCT, CAPTION='Product', HRY_DIMENSION=PRODUCT,
HRY_STRUCTURE=STANDARD, $

Creating Reports With TIBCO® WebFOCUS Language

 1117

Reporting Against a Multi-Fact Cluster Synonym

The following image shows the data in the Excel file.

The following request joins from the wf_retail_product segment of the wf_retail data source to
the excel file as a new root and reports from both parent segments:

JOIN AS_ROOT PRODUCT_CATEGORY AND PRODUCT_SUBCATEG IN WF_RETAIL
  TO UNIQUE PRODUCT_CATEGORY AND PRODUCT_SUBCATEGORY IN PROJECTED
  AS J1
END
TABLE FILE WF_RETAIL
SUM PROJECTED_SALE_UNITS REVENUE_US
BY PRODUCT_CATEGORY
ON TABLE SET PAGE NOPAGE
END

1118

The output is:

14. Joining Data Sources

Creating Reports With TIBCO® WebFOCUS Language

 1119

Reporting Against a Multi-Fact Cluster Synonym

Generating Outer Joins of Cluster Synonym Contexts

Reporting against multiple root segments and a shared dimension generates multiple contexts
in a cluster synonym. For example, in the following image Sales and Products form one
context, while Shipments and Products form a second context.

When a request contains fields from both contexts, by default, an inner join is passed to the
SQL engine. This retrieves only matching values of the shared dimension fields from both
contexts.

You can use the BLEND-MODE parameter to generate a full outer join instead of an inner join
and retrieve all values from both contexts.

1120

14. Joining Data Sources

Syntax:

How to Control Join Processing of Cluster Synonym Contexts

You can set the blend mode parameter from the server Web Console and store the setting in a
profile or procedure. On the Adapters page, click Change Common Adapter Settings on the
ribbon, and select Select all values from the BLEND-MODE drop-down list in the Request
Transformation Settings section, as shown in the following image.

You can also use the following syntax to set the blend mode parameter.

ENGINE INT SET BLEND-MODE {COMMON-VALUES|ALL-VALUES}

where:

COMMON-VALUES

Generates an inner join of cluster synonym contexts and returns only matching values of
the shared dimension fields. This is the default value.

ALL-VALUES

Generates a full outer join of cluster synonym contexts and returns all values of the shared
dimension fields. Missing values are returned for fields from contexts that do not have a
matching value of the shared dimension fields.

Creating Reports With TIBCO® WebFOCUS Language

 1121

Reporting Against a Multi-Fact Cluster Synonym

Example:

Controlling Join Processing of Cluster Synonym Contexts

The following Excel file (excelroot.xlsx) will be uploaded to the server using the Adapter for
Excel and joined as a root to the WF_RETAIL Master File, creating two contexts. A report
request will then be issued against the two roots and the shared dimension.

Note that this file has no data for product categories Camcorder, Stereo Systems, and Video
Production. It has a product category named Displays that does not exist in WF_RETAIL.

The following is the Master File generated for this Excel file.

FILENAME=EXCELROOT, SUFFIX=DIREXCEL,
 DATASET=ibisamp/excelroot.xlsx, $
  SEGMENT=EXCELROOT, SEGTYPE=S0, $
    FIELDNAME=PRODUCT_CATEGORY, ALIAS='Product Category', USAGE=A15V,
ACTUAL=A15V,
      MISSING=ON,
      TITLE='Product Category', $
    FIELDNAME=PRODUCT_SUBCATEGORY, ALIAS='Product Subcategory', USAGE=A31V,
ACTUAL=A31V,
      MISSING=ON,
      TITLE='Product Subcategory', $
    FIELDNAME=PROJECTED_COG, ALIAS='Projected COG', USAGE=D15.2:C,
ACTUAL=A64V,
      MISSING=ON,
      TITLE='Projected COG',
      CURRENCY_DISPLAY=LEFT_FLOAT,  CURRENCY_ISO_CODE=USD,  $
    FIELDNAME=PROJECTED_SALE_UNITS, ALIAS='Projected Sale Units', USAGE=I9,
ACTUAL=A11V,
      MISSING=ON,
      TITLE='Projected Sale Units', $

1122

14. Joining Data Sources

The following request joins the Excel file as a root and generates a report that contains fields
from both roots and the shared dimension. Using the default value for BLEND-MODE produces
an inner join that returns only common values of PRODUCT_CATEGORY.

JOIN AS_ROOT PRODUCT_CATEGORY AND PRODUCT_SUBCATEG IN ibisamp/WF_RETAIL
  TO PRODUCT_CATEGORY AND PRODUCT_SUBCATEGORY IN ibisamp/EXCELROOT
  AS J1
  END
TABLE FILE ibisamp/WF_RETAIL
SUM COGS_US PROJECTED_SALE_UNITS
BY PRODUCT_CATEGORY
ON TABLE SET PAGE NOPAGE
ON TABLE SET STYLE *
GRID=OFF,$
END

The output is shown in the following image.

The following version of the request issues the ENGINE INT SET BLEND-MODE ALL-VALUES
command to produce a full outer join that returns all values of PRODUCT_CATEGORY.

ENGINE INT SET BLEND-MODE ALL-VALUES
JOIN AS_ROOT PRODUCT_CATEGORY AND PRODUCT_SUBCATEG IN ibisamp/WF_RETAIL
  TO PRODUCT_CATEGORY AND PRODUCT_SUBCATEGORY IN ibisamp/EXCELROOT
  AS J1
  END
TABLE FILE ibisamp/WF_RETAIL
SUM COGS_US PROJECTED_SALE_UNITS
BY PRODUCT_CATEGORY
ON TABLE SET PAGE NOPAGE
ON TABLE SET STYLE *
GRID=OFF,$
END

The output is shown in the following image. Note the missing value indicators:

For the Projected Sale Units field in the rows that correspond to product categories
Camcorder, Stereo Systems, and Video Production, which are not represented in the Excel
file.

Creating Reports With TIBCO® WebFOCUS Language

 1123

Reporting Against a Multi-Fact Cluster Synonym

For the Cost of Goods field in the row that corresponds to product category Displays, which
is not represented in the WF_RETAIL data source.

Joining From a Multi-Fact Synonym

Multi-parent synonyms are now supported as the source for a join to a single segment in a
target synonym.

A join from a multi-parent synonym is subject to the following conditions:

Conditional joins are not supported (JOIN WHERE).

The join must be unique. That is, the TO ALL or TO MULTIPLE phrase is not supported.

The target of the join cannot be a multi-parent synonym.

The target of the JOIN must be a single segment, either in a single segment synonym or
one segment in a single parent, multi-segment synonym.

All fields in the JOIN must be FROM/TO a single segment. Any single segment in the source
synonym can be used in the join.

1124

Example:

Joining From a Multi-Fact Synonym

14. Joining Data Sources

The following Master File describes a multi-parent structure based on the WebFOCUS Retail
tutorial. The two fact tables wf_retail_sales and wf_retail_shipments are parents of the
dimension table wf_retail_product.

FILENAME=WF_RETAIL_MULTI_PARENT, $
  SEGMENT=WF_RETAIL_SHIPMENTS, CRFILE=WFRETAIL/FACTS/WF_RETAIL_SHIPMENTS,
CRINCLUDE=ALL,
    DESCRIPTION='Shipments Fact', $
  SEGMENT=WF_RETAIL_SALES, PARENT=., CRFILE=WFRETAIL/FACTS/WF_RETAIL_SALES,
CRINCLUDE=ALL,
    DESCRIPTION='Sales Fact', $
  SEGMENT=WF_RETAIL_PRODUCT, CRFILE=WFRETAIL/DIMENSIONS/WF_RETAIL_PRODUCT,
CRINCLUDE=ALL,
    DESCRIPTION='Product Dimension', $
   PARENT=WF_RETAIL_SHIPMENTS, SEGTYPE=KU,
    JOIN_WHERE=WF_RETAIL_SHIPMENTS.ID_PRODUCT EQ
WF_RETAIL_PRODUCT.ID_PRODUCT;, $
   PARENT=WF_RETAIL_SALES, SEGTYPE=KU,
    JOIN_WHERE=WF_RETAIL_SALES.ID_PRODUCT EQ WF_RETAIL_PRODUCT.ID_PRODUCT;,
$

The following image shows the joins between these tables in the Synonym Editor of the Data
Management Console (DMC).

Creating Reports With TIBCO® WebFOCUS Language

 1125

Reporting Against a Multi-Fact Cluster Synonym

The following request joins the product segment to the dimension table wf_retail_vendor based
on the vendor ID and issues a request against the joined structure:

JOIN ID_VENDOR IN WF_RETAIL_MULTI_PARENT TO ID_VENDOR IN WF_RETAIL_VENDOR
AS J1
TABLE FILE WF_RETAIL_MULTI_PARENT
SUM COGS_US DAYSDELAYED
BY PRODUCT_CATEGORY
BY VENDOR_NAME
WHERE PRODUCT_CATEGORY LT 'S'
ON TABLE SET PAGE NOPAGE
END

1126

The output is:

14. Joining Data Sources

Creating Reports With TIBCO® WebFOCUS Language

 1127

Navigating Joins Between Cluster Synonyms

Navigating Joins Between Cluster Synonyms

By default, when joining cluster synonyms, a hierarchy of segments is constructed from all of
the joined files, and the resulting hierarchy is navigated in top-to-bottom, left-to-right order.

Therefore, if a left outer join is specified from a host synonym to a cluster that has an inner
join, the inner join will be performed last and may remove rows from the host file,
counteracting the purpose of the left outer join. Using the SET FOCTRANSFORM =
NESTED_CLUSTERS/ON command, you can force the joins in the target cluster to be
performed prior to the join between the host and target synonyms. When you use this setting,
SQL scripts are used to join the tables in the target cluster prior to implementing the join to
the host file. The left outer join will be performed last and will retain all rows in the host
synonym.

The syntax is:

SET FOCTRANSFORM = {NESTED_CLUSTERS/OFF|NESTED_CLUSTERS/ON}

where:

NESTED_CLUSTERS/OFF

Maintains the left-to-right, top-to-bottom order of segment navigation. This is the default
value.

NESTED_CLUSTERS/ON

Performs the joins in the target cluster synonym prior to joining the host synonym to the
result.

Reference: Usage Notes for Joins to Cluster Synonyms

Using the SET FOCTRANSFORM = NESTED_CLUSTERS feature requires that the joins be
optimized. The command SET SHORTPATH = SQL must be in effect for combinations of
inner and outer joins with the setting FOCTRANSFORM = NESTED_CLUSTERS/OFF, in order
for the request to be optimized. The SHORTPATH = SQL setting has no effect on
optimization with the setting FOCTRANSFORM = NESTED_CLUSTERS/ON.

You cannot join to a non-root segment of a cluster synonym. If you issue a join to a non-root
segment, the following message displays and the request terminates:

(FOC906) JOIN TO NON-ROOT SEGMENT segname IS NOT ALLOWED FOR
NESTED_CLUSTERS

1128

Example:

Navigating Joins Between Cluster Synonyms

14. Joining Data Sources

This example uses SQL Server data sources generated from a file of citibike trips uploaded
from https://www.citibikenyc.com/system-data, and from a file of zip codes for the stations
used for the trips (you can download this file from https://techsupport.informationbuilders.com/
public/station_zip.csv).

A cluster synonym named station_trip_cls joins the station zip data source to a data source
containing partial trip data (with only a few rows). The following shows the inner join defined in
the cluster synonym:

FILENAME=STATION_TRIP_CLS, $
  SEGMENT=STATION_ZIP_OLEDB, CRFILE=CITIBIKE/STATION_ZIP_OLEDB,
CRINCLUDE=ALL, $
  SEGMENT=CITIBIKE_PARTIAL_OLEDB, SEGTYPE=KU, PARENT=STATION_ZIP_OLEDB,
    CRFILE=CITIBIKE/CITIBIKE_PARTIAL_OLEDB, CRINCLUDE=ALL, CRJOINTYPE=INNER,
    JOIN_WHERE=STATION_ID EQ START_STATION_ID;, $

The following request issues a left outer join from a larger version of the trip data file to the
cluster:

SET FOCTRANSFORM = NESTED_CLUSTERS/&VALUE
SET SHORTPATH = SQL
JOIN LEFT_OUTER START_STATION_ID IN CITIBIKE_TRIPDATA TAG T1 TO ALL
STATION_ID IN STATION_TRIP_CLS TAG T2 AS J1
TABLE FILE CITIBIKE_TRIPDATA
" NESTED_CLUSTERS/&VALUE"
" "
SUM CNT.T1.START_STATION_ID AS T1,Station CNT.ZIP_CODE
CNT.T2.START_STATION_ID AS T2,Station
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

Running the request with &VALUE set to OFF generates the following trace:

SELECT
   COUNT(T1."START_STATION_ID"),
   COUNT(T2."ZIP_CODE"),
   COUNT(T3."START_STATION_ID")
   FROM
   ( ( citibike_tripdata_mssqloledb T1
   LEFT OUTER JOIN
   station_zip_oledb T2
   ON T2."STATION_ID" = T1."START_STATION_ID" )
   INNER JOIN
   citibike_partial_msoledb T3
   ON (T3."START_STATION_ID" = T2."STATION_ID") );

Creating Reports With TIBCO® WebFOCUS Language

 1129

Navigating Joins Between Cluster Synonyms

The output is shown in the following image. The inner join was done last, reducing the number
of stations in the host file to the same number as in the cluster.

Running the request with &VALUE set to ON generates the following trace. Two SQL scripts are
generated, one for the host file and one for the join in the cluster. Then, the left outer join is
performed against the result of the inner join:

SELECT
   T1."START_STATION_ID" AS "SK001_START_STATION_ID",
    COUNT(T1."START_STATION_ID") AS "VB001_CNT_START_STATION_ID"
    FROM
   citibike_tripdata_mssqloledb T1
    GROUP BY
   T1."START_STATION_ID";
   (FOC2546) SQL SCRIPT
__CITIBIKE_TRIPDATA_OLEDB_CITIBIKE_TRIPDATA_OLEDB.SQL CREATED SUCCESSFULLY
(BUT NOT EXECUTED)
   _EDATEMP/__citibike_tripdata_oledb_citibike_tripdata_oledb HELD AS
SQL_SCRIPT
    SELECT
  T1."STATION_ID" AS "SK001_STATION_ID",
    COUNT(T1."ZIP_CODE") AS "VB001_CNT_ZIP_CODE",
    COUNT(T2."START_STATION_ID") AS "VB002_CNT_START_STATION_ID"
    FROM
   station_zip_oledb T1,
   citibike_partial_msoledb T2
    WHERE
   (T2."START_STATION_ID" = T1."STATION_ID")
    GROUP BY
   T1."STATION_ID";
  (FOC2546) SQL SCRIPT
__CITIBIKE_TRIPDATA_OLEDB_STATION_PARTIAL_OLEDB_CLS.SQL CREATED
SUCCESSFULLY (BUT NOT EXECUTED)
  _EDATEMP/__citibike_tripdata_oledb_station_partial_oledb_cls HELD AS
SQL_SCRIPT

1130

14. Joining Data Sources

    SELECT
    SUM(T1."VB001_CNT_START_STATION_ID"),
    SUM(T2."VB001_CNT_ZIP_CODE"),
    SUM(T2."VB002_CNT_START_STATION_ID")
    FROM
   (
   ( /* vvv */
      SELECT
     T1."START_STATION_ID" AS "SK001_START_STATION_ID",
      COUNT(T1."START_STATION_ID") AS
     "VB001_CNT_START_STATION_ID"
      FROM
     citibike_tripdata_mssqloledb T1
      GROUP BY
     T1."START_STATION_ID"
   ) /* ^^^ */ T1
    LEFT OUTER JOIN
   ( /* vvv */
      SELECT
     T1."STATION_ID" AS "SK001_STATION_ID",
      COUNT(T1."ZIP_CODE") AS "VB001_CNT_ZIP_CODE",
      COUNT(T2."START_STATION_ID") AS
     "VB002_CNT_START_STATION_ID"
      FROM
     station_zip_oledb T1,
     citibike_partial_msoledb T2
      WHERE
     (T2."START_STATION_ID" = T1."STATION_ID")
      GROUP BY
     T1."STATION_ID"
   ) /* ^^^ */ T2
    ON T2."SK001_STATION_ID" = T1."SK001_START_STATION_ID" );

The output is shown in the following image. The left outer join was done last, maintaining the
original number of stations in the host file.

Cross Database Join Optimization

Retrieval performance has been optimized under certain conditions when you join tables from
different Relational database systems.

Creating Reports With TIBCO® WebFOCUS Language

 1131

Cross Database Join Optimization

One type of performance optimization results from extracting data from the cross-referenced
table prior to performing the join, or issuing a sub-select. You can disable this optimization
process by issuing the following command:

SQL SET HOLDSQLJOIN = OFF
END

By default, this parameter is ON.

The following performance optimization procedures have been implemented:

For a non-aggregated query, the cross-referenced (TO) table is saved as a file in an internal
binary format. This is faster than joining to a table in a different database system.

For an aggregated query, for the cross-referenced table joined from any aggregation
functions (min, max, sum, avg, count), the retrieval is passed to the relational database in
a sub-select. This can result in retrieving a much smaller answer set, which improves
performance.

For a request with a clause that tests if two columns are equal or both are NULL, the TO
table is held in an internal binary format, also improving performance.

You can view the generated query in either the Session Log or the trace file.

1132

The following SQL request joins a Microsoft SQL Server named citibike_mssql table to a
MySQL table named station_zip_mysql.

14. Joining Data Sources

SQL
SELECT
   T1.TRIPDURATION,
   T1.START_STATION_NAME ,
   T1.END_STATION_NAME ,
   T1.BIKEID ,
   T1.BIRTH_YEAR ,
   T1.GENDER ,
   T1.STARTTIME ,
   T1.STOPTIME ,
   T1.USERTYPE ,   T2.ZIP_CODE ,
   T2.COUNTY ,
   T2.CITY
FROM
   citibike.citibike_mssql T1
     INNER JOIN /*Join 1*/
    citibike.station_zip_mysql T2
       ON
      T1.START_STATION_ID = T2.STATION_ID
;
TABLE
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

When this request is run, the Session Log shows the generated request. First the
station_zip_mysql table is held in an internal format:

TABLEF FILE STATION_ZIP_MYSQL
 PRINT
   ZIP_CODE
   COUNTY
   CITY
   STATION_ID
ON TABLE SET CARTESIAN ON
ON TABLE SET ASNAMES ON
ON TABLE SET HOLDLIST PRINTONLY
 ON TABLE HOLD
  AS SQLHLD01
  FORMAT DATREC
END

Creating Reports With TIBCO® WebFOCUS Language

 1133

Cross Database Join Optimization

Next, the citibike_mssql table is joined to the HOLD file.

JOIN INNER
   CITIBIKE_MSSQL2.START_STATION_ID
  IN CITIBIKE_MSSQL
 TO ALL
   E04
  IN SQLHLD01
 AS SQLJNM01
END

Finally, the joined structure is queried to produce the output.

TABLEF FILE CITIBIKE_MSSQL
 PRINT
   CITIBIKE_MSSQL.TRIPDURATION
   CITIBIKE_MSSQL.START_STATION_NAME
   CITIBIKE_MSSQL.END_STATION_NAME
   CITIBIKE_MSSQL.BIKEID
   CITIBIKE_MSSQL.BIRTH_YEAR
   CITIBIKE_MSSQL.GENDER
   CITIBIKE_MSSQL.STARTTIME
   CITIBIKE_MSSQL.STOPTIME
   CITIBIKE_MSSQL.USERTYPE
   SQLHLD01.E01
   SQLHLD01.E02
   SQLHLD01.E03
   SQLHLD01.E04 NOPRINT
ON TABLE SET CARTESIAN ON
ON TABLE SET ASNAMES ON
ON TABLE SET HOLDLIST PRINTONLY
END

Additional performance improvements result from the following conversions:

If there is more than one cluster of tables from the same DBMS in the FROM clause, joins
between those tables are passed to the corresponding DBMS.

If there is a WHERE condition on fields from the outer table in a left or right outer join, and
this condition always fails for null values, that join is converted to an inner join.

If there is WHERE condition on fields from the left, right, or both tables in a full outer join,
and this condition always fails for null values, that join is converted to a left, right, or inner
join.

Merge sub-select phrases if from, where, group by, and having are the same and re-use the
temporary table created for the merge sub-select statement.

1134

For example, following flow creates three left outer joins between Microsoft SQL Server tables
and Oracle tables. The Oracle synonyms start with the characters o_.

14. Joining Data Sources

Creating Reports With TIBCO® WebFOCUS Language

 1135

Cross Database Join Optimization

The following SQL statement corresponds to the joins generated by the flow.

SQL
SELECT
   T1.ID_SALES ,
   T1.ID_STORE ,
   T1.ID_CURRENCY ,
   T1.ID_CUSTOMER ,
   T1.ID_DISCOUNT ,
   T1.ID_PRODUCT ,
   T1.ID_TIME ,
   T1.COGS_LOCAL ,
   T1.COGS_US ,
   T1.DISCOUNT_LOCAL ,
   T1.DISCOUNT_US ,
   T1.GROSS_PROFIT_LOCAL ,
   T1.GROSS_PROFIT_US ,
   T1.MSRP_LOCAL ,
   T1.MSRP_US ,
   T1.QUANTITY_SOLD ,
   T1.REVENUE_LOCAL ,
   T1.REVENUE_US ,
   T2.ID_AGE ,
   T2.ID_EDUCATION ,
   T2.ID_GEOGRAPHY ,
   T2.ID_INCOME ,
   T2.ID_INDUSTRY ,
   T2.ID_MARITAL_STATUS ,
   T2.ID_OCCUPATION ,
   T2.ID_TIME_MIN ,
   T2.ID_TIME_MAX ,
   T2.EMAIL_ADDRESS ,
   T2.FIRSTNAME ,
   T2.FULLNAME ,
   T2.GENDER ,
   T2.LASTNAME ,
   T2.INCOME ,
   T3.CURRENCY_NAME ,
   T3.CURRENCY_RATE ,
   T4.AGE ,
   T4.AGE_RANGE ,
   T4.AGE_GROUP

1136

14. Joining Data Sources

FROM
   ((("ibisamp/facts".wf_retail_sales T1
     LEFT OUTER JOIN /*Join 1*/
    "ibisamp/dimensions".o_wf_retail_customer T2
       ON
      T1.ID_CUSTOMER = T2.ID_CUSTOMER )
     LEFT OUTER JOIN /*Join 2*/
    "ibisamp/dimensions".wf_retail_currency T3
       ON
      T1.ID_CURRENCY = T3.ID_CURRENCY )
     LEFT OUTER JOIN /*Join 3*/
    "ibisamp/dimensions".o_wf_retail_age T4
       ON
      T2.ID_AGE = T4.ID_AGE )
 WHERE
   T1.REVENUE_US > 600  AND
   T2.LASTNAME LIKE 'C%'  AND
   T3.CURRENCY_NAME = 'US Dollar'  AND
   T4.AGE  BETWEEN 35 AND 40
;
END

Creating Reports With TIBCO® WebFOCUS Language

 1137

Cross Database Join Optimization

The Session Log shows the joins that were generated. The left outer joins were converted to
inner joins, as shown in the following partial listing.

JOIN INNER
   SQLAPP01.ID_AGE
  IN 'ibisamp/dimensions/o_wf_retail_customer' TAG SQLAPP01
 TO ALL
   ID_AGE
  IN 'ibisamp/dimensions/o_wf_retail_age' TAG SQLJTG01
 AS SQLJNM01
END
DEFINE FILE 'ibisamp/dimensions/o_wf_retail_customer' TEMP
 SQLDEF01/I1 WITH SQLJTG01.O_WF_RETAIL_AGE.ID_AGE = 1;
END
TABLEF FILE 'ibisamp/dimensions/o_wf_retail_customer'
 PRINT
   SQLAPP01.ID_AGE
   SQLAPP01.ID_EDUCATION
   SQLAPP01.ID_GEOGRAPHY
   SQLAPP01.ID_INCOME
   SQLAPP01.ID_INDUSTRY
   SQLAPP01.ID_MARITAL_STATUS
   SQLAPP01.ID_OCCUPATION
   SQLAPP01.ID_TIME_MIN
   SQLAPP01.ID_TIME_MAX
   SQLAPP01.EMAIL_ADDRESS
   SQLAPP01.FIRSTNAME
   SQLAPP01.FULLNAME
   SQLAPP01.GENDER
   SQLAPP01.LASTNAME
   SQLAPP01.INCOME
   SQLJTG01.AGE
   SQLJTG01.AGE_RANGE
   SQLJTG01.AGE_GROUP
   SQLAPP01.ID_CUSTOMER
   SQLDEF01 AS (,'SQL$$HIDDEN01',)
   SQLJTG01.ID_AGE NOPRINT

WHERE ( SQLAPP01.LASTNAME LIKE 'C%' ) ;
 WHERE (  ( SQLJTG01.AGE FROM 35 TO 40
 AND SQLJTG01.AGE NE MISSING) ) ;
ON TABLE SET HOLDATTRS ON
ON TABLE SET CARTESIAN ON
ON TABLE SET ASNAMES MIXED
ON TABLE SET HOLDLIST PRINTONLY
 ON TABLE HOLD
  AS SQLHLD01
  FORMAT DATREC
END

1138

In addition, joins that use the same DBMS are passed to that DBMS, as shown in the following
partial listing.

14. Joining Data Sources

   SELECT
  T1."ID_CUSTOMER",
  T1."ID_AGE",
  T1."ID_EDUCATION",
  T1."ID_GEOGRAPHY",
  T1."ID_INCOME",
  T1."ID_INDUSTRY",
  T1."ID_MARITAL_STATUS",
  T1."ID_OCCUPATION",
  T1."ID_TIME_MIN",
  T1."ID_TIME_MAX",
  T1."EMAIL_ADDRESS",
  T1."FIRSTNAME",
  T1."FULLNAME",
  T1."GENDER",
  T1."LASTNAME",
  T1."INCOME",
  T2."ID_AGE",
  T2."AGE",
  T2."AGE_RANGE",
  T2."AGE_GROUP"
   FROM
  wf_retail_customer_t T1,
  wf_retail_age_t T2
   WHERE
  (T2."ID_AGE" = T1."ID_AGE") AND
  (T1."LASTNAME" LIKE 'C%') AND
  (T2."AGE" IS NOT NULL) AND
  (T2."AGE" BETWEEN 35 AND 40);

Invoking Context Analysis for a Star Schema With a Fan Trap

When a star schema contains a segment with aggregated facts and a lower-level segment with
the related detail-level facts, a request that performs aggregation on both levels and returns
them sorted by the higher level can experience the multiplicative effect. This means that the
fact values that are already aggregated may be re-aggregated and, therefore, return multiplied
values.

When the adapter detects the multiplicative effect, it turns optimization off in order to handle
the request processing and circumvent the multiplicative effect. However, performance is
degraded when a request is not optimized.

A new context analysis process has been introduced in this release that detects the
multiplicative effect and generates SQL script commands that retrieve the correct values for
each segment context. These scripts are then passed to the RDBMS as subqueries in an
optimized SQL statement.

Creating Reports With TIBCO® WebFOCUS Language

 1139

Adding DBA Restrictions to the Join Condition: SET DBAJOIN

To activate the context analysis feature, click Change Common Adapter Settings on the
Adapters page of the Web Console. Then select Yes for the FCA parameter in the
Miscellaneous Settings section and click Save, as shown in the following image.

Adding DBA Restrictions to the Join Condition: SET DBAJOIN

When DBA restrictions are applied to a request on a multi-segment structure, by default, the
restrictions are added as WHERE conditions in the report request. When the DBAJOIN
parameter is set ON, DBA restrictions are treated as internal to the file or segment for which
they are specified, and are added to the join syntax.

Note: DBA restrictions with DBAJOIN OFF apply to the entire record instance that is being
retrieved. Therefore, the entire record instance is suppressed when any part of that instance is
restricted. DBAJOIN ON applies the DBA only to the segment where the data value appears,
allowing the rest of the record instance to be displayed, if applicable.

This difference is important when the file or segment being restricted has a parent in the
structure and the join is an outer or unique join.

1140

14. Joining Data Sources

When restrictions are treated as report filters, lower-level segment instances that do not
satisfy them are omitted from the report output, along with their host segments. Since host
segments are omitted, the output does not reflect a true outer or unique join.

When the restrictions are treated as join conditions, lower-level values from segment instances
that do not satisfy them are displayed as missing values, and the report output displays all
host rows.

Syntax:

How to Add DBA Restrictions to the Join Condition

SET DBAJOIN = {OFF|ON}

where:
OFF

Treats DBA restrictions as WHERE filters in the report request. OFF is the default value.

ON

Treats DBA restrictions as join conditions.

Example:

Using the DBAJOIN Setting With Relational Tables

The following request creates two tables, EMPINFOSQL and EDINFOSQL:

TABLE FILE EMPLOYEE
SUM LAST_NAME FIRST_NAME CURR_JOBCODE
BY EMP_ID
ON TABLE HOLD AS EMPINFOSQL FORMAT SQLMSS
END
-RUN
TABLE FILE EDUCFILE
SUM COURSE_CODE COURSE_NAME
BY EMP_ID
ON TABLE HOLD AS EDINFOSQL FORMAT SQLMSS
END

Add the following DBA attributes to the end of the generated EMPINFOSQL Master File. With
the restrictions listed, USER2 cannot retrieve course codes of 300 or above:

END
DBA=USER1,$
USER=USER2, ACCESS = R, $
FILENAME=EDINFOSQL,$
USER=USER2, ACCESS = R, RESTRICT = VALUE, NAME=SYSTEM, VALUE=COURSE_CODE LT
300;,$

Add the following DBA attributes to the end of the generated EDINFOSQL Master File:

END
DBA=USER1,DBAFILE=EMPINFOSQL,$

Creating Reports With TIBCO® WebFOCUS Language

 1141

Adding DBA Restrictions to the Join Condition: SET DBAJOIN

Issue the following request:

SET USER=USER2
SET DBAJOIN=OFF
JOIN LEFT_OUTER EMP_ID IN EMPINFOSQL TO MULTIPLE EMP_ID IN EDINFOSQL AS J1
TABLE FILE EMPINFOSQL
PRINT LAST_NAME FIRST_NAME COURSE_CODE COURSE_NAME
ON TABLE SET PAGE NOPAGE
ON TABLE SET STYLE *
GRID=OFF,$
END

On the report output, all host and child rows with course codes 300 or above have been
omitted, as shown in the following image:

In the generated SQL the DBA restriction has been added to the WHERE predicate in the
SELECT statement:

SELECT
  T1."EID",
  T1."LN",
  T1."FN",
  T2."CC",
  T2."CD"
   FROM
  EMPINFOSQL T1,
  EDINFOSQL T2
   WHERE
  (T2."EID" = T1."EID") AND
  (T2."CC" < '300;');

1142

Rerun the request with SET DBAJOIN=ON. The output now displays all host rows, with missing
values substituted for lower-level segment instances that did not satisfy the DBA restriction, as
shown on the following image:

14. Joining Data Sources

In the generated SQL, the DBA restriction has been added to the join, and there is no WHERE
predicate:

SELECT
  T1."EID",
  T1."LN",
  T1."FN",
  T2."EID",
  T2."CC",
  T2."CD"
   FROM
  ( EMPINFOSQL T1
   LEFT OUTER JOIN EDINFOSQL T2
   ON T2."EID" = T1."EID" AND
      (T2."CC" < '300;') );

Preserving Virtual Fields During Join Parsing

There are two ways to preserve virtual fields during join parsing. One way is to use
KEEPDEFINES, and the second is to use DEFINE FILE SAVE and DEFINE FILE RETURN.

Creating Reports With TIBCO® WebFOCUS Language

 1143

Preserving Virtual Fields During Join Parsing

Preserving Virtual Fields Using KEEPDEFINES

The KEEPDEFINES parameter determines if a virtual field created by the DEFINE command for a
host or joined structure is retained or cleared after the JOIN command is run. It applies when
the DEFINE command precedes the JOIN command.

The prior virtual fields constitute what is called a context. Each new context creates a new
layer or command environment. When you first enter the new environment, all virtual fields
defined in the previous layer are available in the new layer. Overwriting or clearing a virtual field
definition affects only the current layer. When you return to the previous layer, its virtual field
definitions are intact.

New DEFINE fields issued after the JOIN command constitute another context, and by so doing
generate a stack of contexts. In each context, all virtual fields of all prior contexts are
accessible.

By default the KEEPDEFINES setting is OFF. With this setting, a JOIN command removes
prior virtual fields.

When KEEPDEFINES is set to ON, virtual fields are reinstated during the parsing of a
subsequent JOIN command.

A JOIN CLEAR as_name command removes all the contexts that were created after the JOIN
as_name was issued.

For DEFINE-based conditional joins, the KEEPDEFINES setting must be ON. You then must
create all virtual fields before issuing the DEFINE-based conditional JOIN command. This differs
from traditional DEFINE-based joins in which the virtual field is created after the JOIN
command. In addition, a virtual field may be part of the JOIN syntax or WHERE syntax.

DEFINE commands issued after the JOIN command do not replace or clear the virtual fields
created before the join, since a new file context is created.

Syntax:

How to Use KEEPDEFINES

SET KEEPDEFINES = {ON|OFF}

where:

ON

OFF

Retains the virtual field after a JOIN command is run.

Clears the virtual field after a JOIN command is run. This value is the default.

1144

14. Joining Data Sources

Reference: Usage Notes for KEEPDEFINES

Virtual fields defined prior to setting KEEPDEFINES ON are not preserved after a JOIN
command.

Example:

Preserving Virtual Fields During Join Parsing With KEEPDEFINES

The first virtual field, DAYSKEPT, is defined prior to issuing any joins, but after setting
KEEPDEFINES to ON. DAYSKEPT is the number of days between the return date and rental
date for a videotape:

SET KEEPDEFINES = ON
DEFINE FILE VIDEOTRK
DAYSKEPT/I5 = RETURNDATE - TRANSDATE;
END

The ? DEFINE query command shows that this is the only virtual field defined at this point:

? DEFINE

FILE     FIELD NAME                  FORMAT  SEGMENT   VIEW       TYPE
VIDEOTRK DAYSKEPT                    I5            4

The following request prints all transactions in which the number of days kept is two:

TABLE FILE VIDEOTRK
PRINT MOVIECODE TRANSDATE RETURNDATE DAYSKEPT
COMPUTE ACTUAL_DAYS/I2 = RETURNDATE-TRANSDATE;
WHERE DAYSKEPT EQ 2
END

The first few lines of output show that each return date is two days after the transaction date:

MOVIECODE  TRANSDATE  RETURNDATE  DAYSKEPT  ACTUAL_DAYS
---------  ---------  ----------  --------  -----------
001MCA     91/06/27   91/06/29           2            2
692PAR     91/06/27   91/06/29           2            2
259MGM     91/06/19   91/06/21           2            2

Now, the VIDEOTRK data source is joined to the MOVIES data source. The ? DEFINE query
shows that the join did not clear the DAYSKEPT virtual field:

JOIN  MOVIECODE IN VIDEOTRK TO ALL MOVIECODE IN MOVIES AS J1
? DEFINE

FILE     FIELD NAME                  FORMAT  SEGMENT   VIEW       TYPE
VIDEOTRK DAYSKEPT                    I5            4

Creating Reports With TIBCO® WebFOCUS Language

 1145

Preserving Virtual Fields During Join Parsing

Next a new virtual field, YEARS, is defined for the join between VIDEOTRK and MOVIES:

DEFINE FILE VIDEOTRK
YEARS/I5 = (TRANSDATE - RELDATE)/365;
END

The ? DEFINE query shows that the virtual field created prior to the join was not cleared by this
new virtual field because it was in a separate context:

? DEFINE

FILE     FIELD NAME                   FORMAT  SEGMENT   VIEW     TYPE
VIDEOTRK DAYSKEPT                     I5            4
VIDEOTRK YEARS                        I5            5

Next, the field DAYSKEPT is re-defined so that it is the number of actual days plus one:

DEFINE FILE VIDEOTRK
DAYSKEPT/I5 = RETURNDATE - TRANSDATE + 1;
END

The ? DEFINE query shows that there are two versions of the DAYSKEPT virtual field. However,
YEARS was cleared because it was in the same context (after the join) as the new version of
DAYSKEPT, and the DEFINE command did not specify the ADD option:

? DEFINE

FILE     FIELD NAME                   FORMAT  SEGMENT   VIEW     TYPE
VIDEOTRK DAYSKEPT                     I5            4
VIDEOTRK DAYSKEPT                     I5            4

The same request now uses the new definition for DAYSKEPT. Note that the number of days
between the return date and transaction date is actually one day, not two because of the
change in the definition of DAYSKEPT:

MOVIECODE  TRANSDATE  RETURNDATE  DAYSKEPT  ACTUAL_DAYS
---------  ---------  ----------  --------  -----------
040ORI     91/06/20   91/06/21           2            1
505MGM     91/06/21   91/06/22           2            1
710VES     91/06/26   91/06/27           2            1

Now, J1 is cleared. The redefinition for DAYSKEPT is also cleared:

JOIN CLEAR J1
? DEFINE

FILE     FIELD NAME                   FORMAT  SEGMENT   VIEW         TYPE
VIDEOTRK DAYSKEPT                     I5            4

1146

14. Joining Data Sources

The report output shows that the original definition for DAYSKEPT is now in effect:

MOVIECODE  TRANSDATE  RETURNDATE  DAYSKEPT  ACTUAL_DAYS
---------  ---------  ----------  --------  -----------
001MCA     91/06/27   91/06/29           2            2
692PAR     91/06/27   91/06/29           2            2
259MGM     91/06/19   91/06/21           2            2

Preserving Virtual Fields Using DEFINE FILE SAVE and RETURN

The DEFINE FILE SAVE command forms a new context for virtual fields, which can then be
removed with DEFINE FILE RETURN. For details, see Creating Temporary Fields on page 277.

Example:

Preserving Virtual Fields With DEFINE FILE SAVE and RETURN

The following command enables you to preserve virtual fields within a file context:

SET KEEPDEFINES=ON

The following command defines virtual field A for the VIDEOTRK data source and places it in
the current context:

DEFINE FILE VIDEOTRK
 A/A5='JAWS';
 END

The following command creates a new context and saves virtual field B in this context:

DEFINE FILE VIDEOTRK SAVE
 B/A5='ROCKY';
 END
? DEFINE

The output of the ? DEFINE query lists virtual fields A and B:

FILE     FIELD NAME                FORMAT  SEGMENT   VIEW         TYPE
VIDEOTRK A                         A5
VIDEOTRK B                         A5

The following DEFINE command creates virtual field C. All previously defined virtual fields are
cleared because the ADD option was not used in the DEFINE command:

DEFINE FILE VIDEOTRK
 C/A10='AIRPLANE';
 END
? DEFINE

The output of the ? DEFINE query shows that C is the only virtual field defined:

FILE     FIELD NAME                FORMAT  SEGMENT   VIEW         TYPE
VIDEOTRK C                         A10

Creating Reports With TIBCO® WebFOCUS Language

 1147

Preserving Virtual Fields During Join Parsing

The following JOIN command creates a new context. Because KEEPDEFINES is set to ON,
virtual field C is not cleared by the JOIN command:

JOIN MOVIECODE IN VIDEOTRK TAG V1 TO MOVIECODE IN MOVIES TAG M1 AS J1
? DEFINE

The output of the ? DEFINE query shows that field C is still defined:

FILE     FIELD NAME                 FORMAT  SEGMENT   VIEW         TYPE
VIDEOTRK C                          A10

The next DEFINE command creates virtual field D in the new context created by the JOIN
command:

DEFINE FILE VIDEOTRK SAVE
 D/A10='TOY STORY';
 END
? DEFINE

The output of the ? DEFINE query shows that virtual fields C and D are defined:

FILE     FIELD NAME                 FORMAT  SEGMENT   VIEW         TYPE
VIDEOTRK C                          A10
VIDEOTRK D                          A10

The DEFINE FILE RETURN command clears virtual field D created in the current context (after
the JOIN):

DEFINE FILE VIDEOTRK RETURN
END
? DEFINE

The output of the ? DEFINE query shows that virtual field D was cleared, but C is still defined:

FILE     FIELD NAME                 FORMAT  SEGMENT   VIEW         TYPE
VIDEOTRK C                          A10

The following DEFINE FILE RETURN command does not clear virtual field C because field C was
not created using a DEFINE FILE SAVE command:

DEFINE FILE VIDEOTRK RETURN
END
? DEFINE

The output of the ? DEFINE query shows that virtual field C is still defined:

FILE     FIELD NAME                 FORMAT  SEGMENT   VIEW         TYPE
VIDEOTRK C                          A10

Note: DEFINE FILE RETURN is only activated when a DEFINE FILE SAVE is in effect.

1148

14. Joining Data Sources

Screening Segments With Conditional JOIN Expressions

The conditional JOIN command can reference any and all fields in the joined segment and any
and all fields in the parent segment, or higher on the parent's path.

When active, these join expressions screen the segment on which they reside (the child or
joined segment). That is, if no child segment passes the test defined by the expression, the
join follows the rules of SET ALL=OFF, or SET ALL=ON when no child segment exists. Unlike
WHERE phrases in TABLE commands, JOIN_WHERE screening does not automatically screen
the parent segment when SET ALL=ON.

Parsing WHERE Criteria in a Join

WHERE criteria take effect in a join only when a TABLE request reference is made to a cross-
referenced segment or its children. If no such reference is made, the WHERE has no effect.

The AT attribute is used to link the correct parent segment or host to the correct child or cross-
referenced segment. The field values used as the AT parameter are not used to cause the link.
They are used simply as segment references.

Note: If no WHERE criteria are in effect, you receive a Cartesian product.

Displaying Joined Structures

When you join two data sources together, they are subsequently treated as one logical
structure. This structure results from appending the structure of the cross-referenced file to the
structure of the host file. The segment in the cross-referenced file containing the shared value
field becomes the child of the segment in the host file with the shared value field.

Syntax:

How to Display a Joined Structure

To display the joined structure, issue the following command:

CHECK FILE hostfile PICTURE

where:

hostfile

Is the name of the host file.

Creating Reports With TIBCO® WebFOCUS Language

 1149

Displaying Joined Structures

Example:

Displaying a Joined Structure

Notice that the segments belonging to the host file appear as regular segments outlined by
asterisks. The segments belonging to the cross-referenced file appear as virtual segments
outlined by dots. The segments of the cross-referenced file are also labeled with the cross-
referenced file name below each segment.

JOIN PIN IN EMPDATA TO PIN IN SALHIST
CHECK FILE EMPDATA PICTURE
0 NUMBER OF ERRORS=     0
  NUMBER OF SEGMENTS=   2  ( REAL=    1  VIRTUAL=   1 )
  NUMBER OF FIELDS=    14  INDEXES=   1  FILES=     2
  NUMBER OF DEFINES=    1
  TOTAL LENGTH OF ALL FIELDS=  132
1SECTION 01.01
              STRUCTURE OF FOCUS    FILE EMPDATA  ON 03/05/01 AT 12.22.49

          EMPDATA
  01      S1
 **************
 *PIN         **I
 *LASTNAME    **
 *FIRSTNAME   **
 *MIDINITIAL  **
 *            **
 ***************
  **************
        I
        I
        I
        I SLHISTRY
  02    I KU
 ..............
 :PIN         :K
 :EFFECTDATE  :
 :OLDSALARY   :
 :            :
 :            :
 :............:
  JOINED  SALHIST

The top segment of the cross-referenced file structure is the one containing the shared-value
field. If this segment is not the root segment, the cross-referenced file structure is inverted, as
in an alternate file view.

1150

14. Joining Data Sources

The cross-referenced file segment types in the joined structure are the following:

In unique join structures, the top cross-referenced file segment has the segment type KU.
Its unique child segments have segment type KLU. Non-unique child segments have
segment type KL.

In non-unique join structures, the top cross-referenced file segment has the segment type
KM. Its unique child segments have segment type KLU. Non-unique child segments have
segment type KL.

The host file structure remains unchanged. The cross-referenced file may still be used
independently.

Syntax:

How to List Joined Structures

To display a list of joined data sources, issue the following command:

? JOIN

This displays every JOIN command currently in effect. For example:

  JOINS CURRENTLY ACTIVE

HOST                        CROSSREFERENCE
FIELD      FILE      TAG    FIELD      FILE     TAG    AS       ALL  WH
-----      ----      ---    -----      ----     ---    --       ---  --
JOBCODE    EMPLOYEE         JOBCODE    JOBFILE                   N    N

If the joined structure has no join name, the AS phrase is omitted. If two data sources are
joined by multiple JOIN commands, only the first command you issued is displayed. The N in
the WH column indicates that the join is not conditional. A Y indicates that the join is
conditional.

Clearing Joined Structures

You can clear specific join structures, or all existing structures. Clearing deactivates the
designated joins. If you clear a conditional join, all joins issued subsequently to that join using
the same host file are also cleared.

Tip: If you wish to list the current joins before clearing or see details about all active joined
structures, issue the query command ? JOIN. For details and illustrations, see How to List
Joined Structures on page 1151.

Creating Reports With TIBCO® WebFOCUS Language

 1151


Clearing Joined Structures

Syntax:

How to Clear a Join

To clear a joined structure, issue this command:

JOIN CLEAR {joinname|*}

where:

joinname

Is the AS name of the joined structure you want to clear.

*

Clears all joined structures.

Clearing a Conditional Join

You can clear a join by issuing the JOIN CLEAR command. The effect of the JOIN CLEAR
command depends on whether any conditional join exists.

If conditional joins are found and were issued after the join you wish to clear, or if the join
you wish to clear is a conditional join, then the JOIN CLEAR as_name command removes all
joins issued after the specified join.

If no conditional joins were issued after the join you wish to clear, only the join you specify
is cleared. Any virtual fields saved in the context of a join that is cleared are also cleared.
Normal joins may or may not be cleared, depending on the position of the conditional join.
The JOIN CLEAR * command clears every join issued, along with its associated virtual
fields. However, all virtual fields in the null context remain untouched.

Note: The null context is the context of the data source prior to any joins being issued.

Example:

Clearing Joins

The following request creates three joins using VIDEOTRK as the host data source. The first
two are conditional (JW1, JW2), and the third join is unconditional (J1):

JOIN FILE VIDEOTRK AT PRODCODE TO ALL
     FILE GGSALES  AT PCD AS JW1
WHERE PRODCODE NE PCD;
END
JOIN  FILE VIDEOTRK AT TRANSDATE TO ALL
      FILE MOVIES   AT RELDATE   AS JW2
WHERE (TRANSDATE - RELDATE)/365 GT 10;
END
JOIN MOVIECODE IN VIDEOTRK TO MOVIECODE IN MOVIES AS J1

1152

14. Joining Data Sources

The next request creates a conditional join (JW3) using MOVIES as the host data source:

JOIN  FILE MOVIES   AT MOVIECODE TO ONE
      FILE VIDEOTRK AT TRANSDATE AS JW3
WHERE (TRANSDATE - RELDATE)/365 LT 2;
END

The last request creates a third conditional join (JW4) that uses VIDEOTRK as the host data
source:

JOIN  FILE VIDEOTRK AT LASTNAME  TO ALL
      FILE EMPLOYEE AT LAST_NAME AS JW4
WHERE LASTNAME GE LAST_NAME;
END

Following is the output of the ? JOIN query after executing these joins:

? JOIN
 JOINS CURRENTLY ACTIVE

HOST                           CROSSREFERENCE
FIELD       FILE     TAG    FIELD       FILE      TAG   AS      ALL  WH
-----       ----     ---    -----       ----      ---   --      ---  --
PRODCODE    VIDEOTRK        PCD         GGSALES         JW1      Y    Y
TRANSDATE   VIDEOTRK        RELDATE     MOVIES          JW2      Y    Y
MOVIECODE   VIDEOTRK        MOVIECODE   MOVIES          J1       N    N
MOVIECODE   MOVIES          TRANSDATE   VIDEOTRK        JW3      N    Y
LASTNAME    VIDEOTRK        LAST_NAME   EMPLOYEE        JW4      Y    Y

Clearing JW2 clears all joins that were issued after JW2 and that use the same host data
source. JW1 remains because it was issued prior to JW2, and JW3 remains because it uses a
different host data source:

JOIN CLEAR JW2
? JOIN
 JOINS CURRENTLY ACTIVE

HOST                           CROSSREFERENCE
FIELD        FILE     TAG   FIELD        FILE     TAG      AS   ALL WH
-----        ----     ---   -----        ----     ---      --   --- --
PRODCODE     VIDEOTRK       PCD          GGSALES           JW1   Y   Y
MOVIECODE    MOVIES         TRANSDATE    VIDEOTRK          JW3   N   Y

Creating Reports With TIBCO® WebFOCUS Language

 1153



Clearing Joined Structures

1154

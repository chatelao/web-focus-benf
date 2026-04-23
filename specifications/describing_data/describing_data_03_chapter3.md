Chapter3

Describing a Group of Fields

Certain fields in a data source may have a one-to-one correspondence. The different
groups formed can be related to one another. For some types of data sources you can
define a subset, a logical view of a group. You can identify these groups and the
relationships between them by using attributes in the Master and Access File, as well as
related facilities, such as the JOIN command.

This section describes the relationships of fields and how to implement them using
Master File attributes. If your type of data source also requires an Access File, see the
appropriate data adapter documentation for supplementary information about defining
groups and group relations in the Access File.

For Maintain Data: Dynamic joins (SEGTYPE DKU), and recursive joins are not supported.
Static joins (SEGTYPE KU) are supported.

In this chapter:

Defining a Single Group of Fields

One-to-One Relationship

Identifying a Logical View: Redefining a
Segment

Relating Multiple Groups of Fields

Logical Dependence: The Parent-Child
Relationship

Logical Independence: Multiple Paths

Cardinal Relationships Between
Segments

One-to-Many Relationship

Many-to-Many Relationship

Recursive Relationships

Relating Segments From Different Types
of Data Sources

Rotating a Data Source: An Alternate
View

Defining a Prefix for Field Titles

Defining a Single Group of Fields

Certain fields in a data source may have a one-to-one correspondence. For each value of a
field, the other fields may have exactly one corresponding value. For example, consider the
EMPLOYEE data source:

Each employee has one ID number which is unique to that employee.

Describing Data With TIBCO WebFOCUS® Language

 65

Defining a Single Group of Fields

For each ID number there is one first and last name, one date hired, one department, and
one current salary.

In the data source, one field represents each of these employee characteristics. The entire
group of fields represents the employee. In Master File terms, this group is called a segment.

Understanding a Segment

A segment is a group of fields that have a one-to-one correspondence with each other and
usually describe a group of related characteristics. In a relational data source, a segment is
equivalent to a table. Segments are the building blocks of larger data structures. You can
relate different segments to each other, and describe the new structures, as discussed in
Relating Multiple Groups of Fields on page 71.

The following diagram illustrates the concept of a segment.

Understanding a Segment Instance

While a segment is an abstract description of data, the instances that correspond to it are the
actual data. Each instance is an occurrence of segment values found in the data source. For a
relational data source, an instance is equivalent to a row in a table. In a single segment data
source, a segment instance is the same as a record.

66

The relationship of a segment to its instances is illustrated in the following diagram.

3. Describing a Group of Fields

Understanding a Segment Chain

The instances of a segment that are descended from a single parent instance are collectively
known as a segment chain. In the special case of a root segment, which has no parent, all of
the root instances form a chain. The parent-child relationship is discussed in Logical
Dependence: The Parent-Child Relationship on page 74.

The following diagram illustrates the concept of a segment chain.

Describe a segment using the SEGNAME and SEGTYPE attributes in the Master File. The
SEGNAME attribute is described in Identifying a Segment: SEGNAME on page 68.

Describing Data With TIBCO WebFOCUS® Language

 67

Defining a Single Group of Fields

Identifying a Key Field

Most segments also have key fields, which are one or more fields that uniquely identify each
segment instance. In the EMPLOYEE data source, the ID number is the key because each
employee has one ID number, and no other employee has the same number. The ID number is
represented in the data source by the EMP_ID field.

If your data source uses an Access File, you may need to specify which fields serve as keys by
identifying them in the Access File. If the data source also happens to be a relational data
source, the fields constituting the primary key in the Master File should be the first fields
described for that segment, meaning that the field declarations should come before any others
in that segment.

For FOCUS data sources, identify key fields and their sorting order using the SEGTYPE attribute
in the Master File, as shown in Describing a FOCUS Data Source on page 293. Position the key
fields as the first fields in the segment.

Identifying a Segment: SEGNAME

The SEGNAME attribute identifies the segment. It is the first attribute you specify in a segment
declaration. Its alias is SEGMENT.

For a FOCUS data source, the segment name may consist of up to eight characters. Segment
names for an XFOCUS data source may have up to 64 characters. You can use segment
names of up to 64 characters for non-FOCUS data sources, if supported by the DBMS. To
make the Master File self-documenting, set SEGNAME to something meaningful to the user or
the native file manager. For example, if you are describing a DB2 table, assign the table name
(or an abbreviation) to SEGNAME.

In a Master File, each segment name must be unique. The only exception to this rule is in a
FOCUS or XFOCUS data source, where cross-referenced segments in Master File-defined joins
can have the same name as other cross-referenced segments in Master File-defined joins. If
their names are identical, you can still refer to them uniquely by using the CRSEGNAME
attribute. See Defining a Join in a Master File on page 349.

In a FOCUS or XFOCUS data source, you cannot change the value of SEGNAME after data has
been entered into the data source. For all other types of data sources, you can change
SEGNAME as long as you also change all references to it. For example, any references in the
Master and Access File.

If your data source uses an Access File as well as a Master File, you must specify the same
segment name in both.

68

3. Describing a Group of Fields

Syntax:

How to Identify a Segment

{SEGNAME|SEGMENT} = segment_name

where:

segment_name

Is the name that identifies this segment. For a FOCUS data source, it can be a maximum
of eight characters long. Segment names for an XFOCUS data source can consist of up to
64 characters. You can use segment names of up to 64 characters for non-FOCUS data
sources, if supported by the DBMS.

The first character must be a letter, and the remaining characters can be any combination
of letters, numbers, and underscores ( _ ). It is not recommended to use other characters,
because they may cause problems in some operating environments or when resolving
expressions.

Example:

Identifying a Segment

If a segment corresponds to a relational table named TICKETS, and you want to give the
segment the same name, use the SEGNAME attribute in the following way:

SEGNAME = TICKETS

Identifying a Logical View: Redefining a Segment

The segments that you define usually correspond to underlying groups in your data source. For
example, a segment could be a table in a relational data source.

However, you are not limited to using the segment as it was originally defined in the native
data source. You can define a logical view which includes only a subset of the fields in a
segment fields (similar to a relational view), or define the unwanted fields as one or more filler
fields. This technique can be helpful if, for example, you only want to make some of the fields
in the segment available to an application or its users.

Use these methods with the following types of data sources:

Relational data sources. Omit unwanted fields from the segment description in the Master
File.

Non-relational data sources. Define unwanted fields as one or more filler fields.

To restrict access explicitly at the file, segment, or field level based on user ID, field values,
and other characteristics, use the DBA facility as described in Providing Data Source Security:
DBA on page 405.

Describing Data With TIBCO WebFOCUS® Language

 69

Identifying a Logical View: Redefining a Segment

Example:

Omitting a Field: Creating a Segment Subset

Define a logical view for a relational data source by omitting the unwanted fields from the
segment description in the Master File. Consider the following Master File for an Oracle table
named EMPFACTS:

FILENAME = EMPFACTS, SUFFIX = SQLORA ,$
 SEGNAME = EMPFACTS, SEGTYPE = S0 ,$
  FIELDNAME= EMP_NUMBER, ALIAS= ENUM,  USAGE= A9,     ACTUAL= A9   ,$
  FIELDNAME= LAST_NAME,  ALIAS= LNAME, USAGE= A15,    ACTUAL= A15  ,$
  FIELDNAME= FIRST_NAME, ALIAS= FNAME, USAGE= A10,    ACTUAL= A10  ,$
  FIELDNAME= HIRE_DATE,  ALIAS= HDT,   USAGE= I6YMD,  ACTUAL= DATE ,$
  FIELDNAME= DEPARTMENT, ALIAS= DPT,   USAGE= A10,    ACTUAL= A10  ,$
  FIELDNAME= SALARY,     ALIAS= SAL,   USAGE= D12.2M, ACTUAL= D8   ,$
  FIELDNAME= JOBCODE,    ALIAS= JCD,   USAGE= A3,     ACTUAL= A3   ,$
  FIELDNAME= OFFICE_NUM, ALIAS= OFN,   USAGE= I8,     ACTUAL= I4   ,$

If you develop an application that refers to only the employee ID and name fields, and you want
this to be reflected in the application view of the segment, you can code an alternative Master
File that names only the desired fields:

FILENAME = EMPFACTS, SUFFIX = SQLORA ,$
  SEGNAME = EMPFACTS, SEGTYPE = S0 ,$
    FIELDNAME= EMP_NUMBER, ALIAS= ENUM,  USAGE= A9,  ACTUAL= A9   ,$
    FIELDNAME= LAST_NAME,  ALIAS= LNAME, USAGE= A15, ACTUAL= A15  ,$
    FIELDNAME= FIRST_NAME, ALIAS= FNAME, USAGE= A10, ACTUAL= A10  ,$

Example:

Redefining a Field: Creating a Filler Field

Define a logical view for certain data sources, such as a sequential or FOCUS data source, by
defining the fields excluded from the view as one or more filler fields. Define the field format
as alphanumeric, its length as the number of bytes making up the underlying fields, and its
name and alias as blank. Field declarations and length are discussed in detail in Describing an
Individual Field on page 103.

Consider the EMPINFO segment of the EMPLOYEE data source:

SEGNAME = EMPINFO, SEGTYPE = S1 ,$
  FIELDNAME = EMP_ID,       ALIAS = EID,  USAGE = A9     ,$
  FIELDNAME = LAST_NAME,    ALIAS = LN,   USAGE = A15    ,$
  FIELDNAME = FIRST_NAME,   ALIAS = FN,   USAGE = A10    ,$
  FIELDNAME = HIRE_DATE,    ALIAS = HDT,  USAGE = I6YMD  ,$
  FIELDNAME = DEPARTMENT,   ALIAS = DPT,  USAGE = A10    ,$
  FIELDNAME = CURR_SAL,     ALIAS = CSAL, USAGE = D12.2M ,$
  FIELDNAME = CURR_JOBCODE, ALIAS = CJC,  USAGE = A3     ,$
  FIELDNAME = ED_HRS,       ALIAS = OJT,  USAGE = F6.2   ,$

70

3. Describing a Group of Fields

If you develop an application that refers to only the employee ID and name fields, and you want
this to be reflected in the application view of the segment, you can code an alternative Master
File that explicitly names only the desired fields:

SEGNAME = EMPINFO, SEGTYPE = S1 ,$
  FIELDNAME = EMP_ID,     ALIAS = EID, USAGE = A9  ,$
  FIELDNAME = LAST_NAME,  ALIAS = LN,  USAGE = A15 ,$
  FIELDNAME = FIRST_NAME, ALIAS = FN,  USAGE = A10 ,$
  FIELDNAME =,            ALIAS =,     USAGE = A29 ,$

The filler field is defined as an alphanumeric field of 29 bytes, which is the combined internal
length of the fields it replaces: HIRE_DATE (4 bytes), DEPARTMENT (10 bytes), CURR_SAL (8
bytes), CURR_JOBCODE (3 bytes), and ED_HRS (4 bytes).

Relating Multiple Groups of Fields

After you have described a segment, you can relate segments to each other to build more
sophisticated data structures. You can:

Describe physical relationships. If groups of fields are already physically related in your
data source, you can describe the relationship.

Describe logical relationships. Describe a logical relationship between any two segments
that have at least one field in common by joining them. The underlying data structures
remain physically separate, but they are treated as if they were part of a single structure.
The new structure can include segments from the same or different types of data sources.

If you are creating a new FOCUS data source, you can implement segment relationships in
several ways, depending upon your design goals, as described in Describing a FOCUS Data
Source on page 293.

To describe a data structure containing several segments, whether it is a multisegment data
source or several data sources that have been joined together, you should be aware of the
following:

Logical dependence between related segments.

Logical independence between unrelated segments.

Facilities for Specifying a Segment Relationship

There are several facilities for specifying relationships between segments. The use of a Master
and Access File to specify a relationship is documented in this chapter. The JOIN command,
which joins segments into a structure from which you can report, is described in the Creating
Reports With WebFOCUS Language manual.

Describing Data With TIBCO WebFOCUS® Language

 71

Relating Multiple Groups of Fields

A related facility, the MATCH FILE command, enables many types of relationships by first
describing a relationship as a series of extraction and merging conditions, then merging the
related data into a new single segment data source. The result is not a joined structure, but an
entirely new data source that can be further processed. The original data sources remain
unchanged. The MATCH FILE command is documented in the Creating Reports With WebFOCUS
Language manual.

Identifying a Parent Segment: PARENT

The PARENT attribute identifies a parent segment. Specify the PARENT attribute in the
segment declaration of the Master File. Because a root segment has no parent, you do not
specify the PARENT segment when declaring a root.

A parent segment must be declared in the Master File before any of its child segments.

If the parent-child relationship is permanently implemented within the structure of the data
source, such as within a FOCUS data source, then you cannot change the PARENT attribute
without changing the underlying structure of the data source. However, if the parent-child
relationship is temporary, as it is when you join several relational tables in the Master File,
then you can change the PARENT attribute.

Syntax:

How to Identify the Parent Segment

PARENT = segment_name

where:

segment_name

If no PARENT attribute is specified in a Master File, then, by default, each segment takes
the preceding segment in the Master File as its parent. If a PARENT attribute is specified,
then all segments that follow will take that segment as their parent, unless explicitly
specified.

It is recommended that you use the PARENT attribute for unique segments with a SEGTYPE
of U.

Example:

Identifying a Parent Segment

In the EMPLOYEE data source, SALINFO is the parent of DEDUCT, so the segment declaration
for DEDUCT includes the following attribute:

PARENT = SALINFO

72

3. Describing a Group of Fields

Identifying the Type of Relationship: SEGTYPE

The SEGTYPE attribute specifies the type of relationship that a segment has to its parent.
SEGTYPE is part of the segment declaration and is used differently in various types of data
sources. For sequential, VSAM, and ISAM data sources, see Describing a Sequential, VSAM, or
ISAM Data Source on page 231. For FOCUS data sources, see Describing a FOCUS Data
Source on page 293. For other types of data sources, see the appropriate data adapter
documentation for details.

Understanding the Efficiency of the Minimum Referenced Subtree

In any database structure consisting of more than a single table or segment, WebFOCUS
handles retrieval by only accessing data from the minimum referenced subtree, which is a
subset of the full database structure. A minimum referenced subtree consists of only those
segments containing referenced fields, and any intervening segments needed to make a
complete structure.

Consider the following database structure consisting of three segments, A, B, and C, with A
being the parent of B, and B the parent of C. Segment A is also known as the root segment.
This structure may be three different joined tables, or a single, multisegment structure.

If a database request references fields contained only in segment A, then only data in segment
A is retrieved. Likewise, if fields from segments A and B are requested, only segments A and B
are retrieved. No additional retrieval costs are incurred, as would occur if all three segments
were retrieved for each request.

Describing Data With TIBCO WebFOCUS® Language

 73

Logical Dependence: The Parent-Child Relationship

For joined structures, there is an implicit reference to the root segment, which is always
retrieved in a database request. If a request involving a joined structure references fields from
segment B only, both segments A and B are retrieved since the root segment (A) is implied to
link segment B. Additionally, if fields from segment C only are referenced, all three segments
are retrieved since segments A and B are implied to link segment C. The retrieval costs are
higher when intervening segments are retrieved for a request.

For multisegment structures, which are defined in the same Master File, there is no implied
reference to the root segment. If a request involving this type of structure references fields
from one segment only, such as segment C, then one segment only, segment C, is retrieved.
However, if fields from segments A and C are referenced, then all three segments are retrieved
since segment B is an intervening segment required to make a complete structure. When all
possible database relations are described in a single Master File, you can eliminate the costs
associated with retrieving non-referenced segments.

Logical Dependence: The Parent-Child Relationship

Logical dependence between segments is expressed in terms of the parent-child relationship.
A child segment is dependent upon its parent segment. An instance of the child segment can
exist only if a related instance of the parent segment exists. The parent segment has logical
precedence in the relationship, and is retrieved first when the data source is accessed.

Note that if the parent-child relationship is logical and not physical, as in the case of a join, it
is possible to have a child instance without a related parent instance. In this case, the child
instance is not accessible through the join, although it is still accessible independently.

If a join relates the parent-child segments, the parent is known as the host segment, and the
child is known as the cross-referenced segment. The fields on which the join is based (that is,
the matching fields in the host and cross-referenced segments) are known respectively as the
host and cross-referenced fields.

A Simple Parent-Child Relationship

In the EMPLOYEE data source, the EMPINFO and SALINFO segments are related. EMPINFO
identifies an employee by ID number, while SALINFO contains the pay history of the employee.
EMPINFO is the parent segment, and SALINFO is a child segment dependent upon it. It is
possible to have in this relationship an employee identified by ID and name for whom no salary
information has been entered (that is, the parent instance without the child instance).
However, it is meaningless to have salary information for an employee if one does not know
who the employee is (that is, a child instance without the parent instance).

74

The following diagram illustrates the concept of a parent-child relationship.

3. Describing a Group of Fields

A Parent-Child Relationship With Multiple Segments

The same general parent-child relationships hold for data structures containing more than two
segments. Consider the following diagram of a portion of the EMPLOYEE data source,
containing the EMPINFO, SALINFO, and DEDUCT segments. DEDUCT contains payroll deduction
information for each paycheck.

The following diagram illustrates the concept of a parent-child relationship with multiple
segments.

Describing Data With TIBCO WebFOCUS® Language

 75

Logical Dependence: The Parent-Child Relationship

EMPINFO is related to SALINFO, and in this relationship EMPINFO is the parent segment and
SALINFO is the child segment. SALINFO is also related to DEDUCT. In this second relationship,
SALINFO is the parent segment and DEDUCT is the child segment. Just as SALINFO is
dependent upon EMPINFO, DEDUCT is dependent upon SALINFO.

Understanding a Root Segment

The segment that has logical precedence over the entire data structure, the parent of the
entire structure, is called the root segment. This is because a data structure can branch like a
tree, and the root segment, like the root of a tree, is the source of the structure.

In the following diagram, EMPINFO is the root. It has no parent, and all other segments in the
structure are its children, directly (SALINFO) or indirectly (DEDUCT).

Understanding a Descendant Segment

Direct and indirect children of a segment are collectively known as its descendant segments.
SALINFO and DEDUCT are descendants of EMPINFO. DEDUCT is also a descendant of
SALINFO. A descendant segment with no children is called a leaf segment, because the
branching of the data structure tree ends with the leaf. DEDUCT is a leaf.

76

The following diagram illustrates the concept of a descendant segment.

3. Describing a Group of Fields

Understanding an Ancestral Segment

Direct and indirect parents of a segment are its ancestral segments. In the following diagram,
SALINFO and EMPINFO are ancestors of DEDUCT.

Describing Data With TIBCO WebFOCUS® Language

 77

Logical Independence: Multiple Paths

Logical Independence: Multiple Paths

A group of segments that are related to each other as a sequence of parent-child
relationships, beginning with the root segment and continuing down to a leaf, is called a path.
Because the path is a sequence of parent-child relationships, each segment is logically
dependent upon all of the segments higher in the path.

Understanding a Single Path

In the following view of the EMPLOYEE data source, EMPINFO, SALINFO, and DEDUCT form a
path. An instance of DEDUCT (paycheck deductions) can exist only if a related instance of
SALINFO (the paycheck) exists, and the instance of SALINFO can exist only if a related instance
of EMPINFO (the employee) exists.

78

3. Describing a Group of Fields

Understanding Multiple Paths

Consider the full EMPLOYEE structure, which includes the EMPLOYEE data source and the
JOBFILE and EDUCFILE data sources that have been joined to it.

This is a multipath data structure. There are several paths, each beginning with the root
segment and ending with a leaf. Every leaf segment is the end of a separate path. The
following diagram illustrates the concept of a multipath data structure.

Describing Data With TIBCO WebFOCUS® Language

 79

Cardinal Relationships Between Segments

Understanding Logical Independence

The EMPLOYEE data structure has six paths. The paths begin with the EMPINFO segment (the
root), and end with:

The FUNDTRAN segment.

The SECSEG segment.

The SKILLSEG segment.

The ADDRESS segment.

The DEDUCT segment.

The COURSEG segment.

Each path is logically independent of the others. For example, an instance of DEDUCT is
dependent upon its ancestor segment instances SALINFO and EMPINFO, but the ADDRESS
segment lies in a different path, so DEDUCT is independent of ADDRESS.

This is because employee deductions are identified by the paycheck from which they came, so
deduction information can be entered into the data source only if the paycheck from which the
deduction was made is entered first. However, deductions are not identified by the employee
address. An employee paycheck deduction can be entered without the address being known,
and conversely, the employee address can be entered before any paychecks and deductions
have been entered into the data source.

Cardinal Relationships Between Segments

The following types of cardinal relationships between groups of data are supported:

One-to-one (1:1).

One-to-many (1:M).

Many-to-many (M:M).

You can define these relationships between:

Instances of different segments.

Instances of the same segment. That is, a recursive or bill-of-materials relationship.

Segments from the same type of data source.

80

3. Describing a Group of Fields

Segments from different types of data sources. For example, you can define the
relationship between an Oracle table and a FOCUS data source. Note that you can join
different types of data sources only by using the JOIN command, not by defining the join in
the Master File or Access File.

If you are using a network data source, you can also rotate the data source after you have
defined it, creating an alternate view that reverses some of the data relationships and
enables you to access the segments in a different order.

One-to-One Relationship

Fields in a segment have a one-to-one relationship with each other. Segments can also exhibit
a one-to-one relationship. Each instance of a parent segment can be related to one instance of
a child segment, as shown in the following diagram. Because the relationship is one-to-one,
the parent instance is never related to more than one instance of the child. However, not every
parent instance must have a matching child instance.

The child in a one-to-one relationship is referred to as a unique segment, because there can
never be more than a single child instance. The following diagram illustrates the concept of a
one-to-one relationship.

Describing Data With TIBCO WebFOCUS® Language

 81

One-to-One Relationship

Example:

Understanding a One-to-One Relationship

In the EMPLOYEE data source, each EMPINFO segment instance describes one employee ID
number, name, current salary, and other related information. Some employees have joined the
Direct Deposit program, which deposits their paycheck directly into their bank accounts each
week. For these employees, the data source also contains the name of their bank and their
account number.

Because only one set of bank information is required for each employee (since each employee
paycheck is deposited into only one account), there is a one-to-one relationship between
employee ID fields and bank information fields. Because there is limited participation in the
Direct Deposit program, only some employees have bank information. Most of the employees
do not need the bank fields.

The data source was designed with storage efficiency in mind, and so the bank fields have
been put into a separate segment called FUNDTRAN. Space is only used for the banking
information, creating an instance of FUNDTRAN, if it is needed. However, if banking fields are
used in the parent segment (EMPINFO), the EMPINFO segment for each employee reserves
space for the banking fields, even though those fields are empty in most cases. This concept
is illustrated in the following diagram.

Where to Use a One-to-One Relationship

When you retrieve data, you can specify a segment as unique in order to enforce a one-to-one
relationship.

82

3. Describing a Group of Fields

When you retrieve data from a segment described as unique, the request treats the segment
as an extension of its parent. If the unique segment has multiple instances, the request
retrieves only one. If the unique segment has no instances, the request substitutes default
values for the missing segment fields. Zero (0) is substituted for numeric fields, blank ( ) is
substituted for alphanumeric fields, and the missing value is substituted for fields that have
the MISSING attribute specified. The MISSING attribute is described in Describing an Individual
Field on page 103.

Implementing a One-to-One Relationship in a Relational Data Source

Describe this relationship by joining the tables in the Master File and specifying a SEGTYPE of
U for the child table. For more information on joining the tables in a Master File, see the
appropriate data adapter documentation. Alternatively, you can join the tables by issuing the
JOIN command without the ALL (or MULTIPLE) option (or with the UNIQUE option) and turning
off the SQL Optimization facility with the SET OPTIMIZATION command.

Implementing a One-to-One Relationship in a Sequential Data Source

Specify this relationship between two records by issuing the JOIN command without the ALL (or
MULTIPLE) option (or with the UNIQUE option).

Implementing a One-to-One Relationship in a FOCUS Data Source

Describe this relationship by specifying a SEGTYPE of U for the child segment. Alternately, you
can join segments by issuing the JOIN command without the ALL (or MULTIPLE) option (or with
the UNIQUE option), or by specifying a unique join in the Master File using a SEGTYPE of KU
(for a static join) or DKU (for a dynamic join). All of these SEGTYPE values are described in
Describing a FOCUS Data Source on page 293.

You can also describe a one-to-one segment relationship as a one-to-many relationship in the
Master File or by using the JOIN command. This technique gives you greater flexibility, but does
not enforce the one-to-one relationship when reporting or entering data and does not use
resources as efficiently.

One-to-Many Relationship

The most common relationship between two segments is the one-to-many relationship. Each
instance of a parent segment can be related to one or more instances of a child segment.
However, not every parent instance needs to have matching child instances.

Describing Data With TIBCO WebFOCUS® Language

 83

One-to-Many Relationship

The following diagram illustrates the concept of a one-to-many relationship.

Example:

Understanding a One-to-Many Relationship

In the EMPLOYEE data source, each EMPINFO segment instance describes an employee ID
number, name, current salary, and other related information. Each SALINFO segment contains
an employee gross salary for each month. Most employees work for many months, so the
relationship between EMPINFO and SALINFO is one-to-many.

84

The following diagram further illustrates the concept of a one-to-many relationship.

3. Describing a Group of Fields

Implementing a One-to-Many Relationship in a Relational Data Source

Describe this relationship by joining the tables in the Master File and specifying a SEGTYPE of
S0 for the child table. For more information on joining the tables in a Master File, see the
appropriate data adapter documentation. Alternately, you can join the tables by issuing the
JOIN command with the ALL or MULTIPLE option.

Implementing a One-to-Many Relationship in a VSAM or Sequential Data Source

You can describe a one-to-many relationship between a record and a group of multiply
occurring fields within the record.

The OCCURS attribute specifies how many times the field (or fields) occur.

The POSITION attribute specifies where in the record the field (or fields) occur if they are
not at the end of the record.

The ORDER field determines the sequence number of an occurrence of a field.

The PARENT attribute indicates the relationship between the singly and multiply occurring
fields.

The OCCURS and POSITION attributes and the ORDER field are all described in Describing a
Sequential, VSAM, or ISAM Data Source on page 231.

Describe a one-to-many relationship between different records by using a RECTYPE field to
indicate the type of each record, and the PARENT attribute to indicate the relationship between
the different records. RECTYPE fields are described in Describing a Sequential, VSAM, or ISAM
Data Source on page 231.

Describing Data With TIBCO WebFOCUS® Language

 85

Many-to-Many Relationship

You can also specify a one-to-many relationship between two records in different data sources
by issuing the JOIN command with the ALL or MULTIPLE option, or defining the join in the
Master File. See the Creating Reports With WebFOCUS Language manual for information about
the JOIN command, and see Defining a Join in a Master File on page 349, for information
about joins in a Master File.

Implementing a One-to-Many Relationship in a FOCUS Data Source

Describe this relationship by specifying a SEGTYPE of Sn or SHn for the child segment.
Alternatively, you can join the segments by issuing the JOIN command with the ALL or
MULTIPLE option or by specifying a join in the Master File with a SEGTYPE of KM (for a static
join) or DKM (for a dynamic join). All of these SEGTYPE values are described in Describing a
FOCUS Data Source on page 293.

Many-to-Many Relationship

A less commonly used relationship is a many-to-many relationship. Each instance of one
segment can be related to one or more instances of a second segment, and each instance of
the second segment can be related to one or more instances of the first segment. It is
possible to implement this relationship directly between two relational tables, and indirectly
between segments of other types of data sources.

Implementing a Many-to-Many Relationship Directly

A direct many-to-many relationship can exist between two relational tables. The STUDENT table
contains one row for each student enrolled at a college, and the CLASSES table contains one
row for each class offered at the college. Each student can take many classes, and many
students can take each class.

The many-to-many type of relationship is illustrated in the following diagram.

86

3. Describing a Group of Fields

When the M:M relationship is seen from the perspective of either of the two tables, it looks
like a 1:M relationship. One student taking many classes (1:M from the perspective of
STUDENT), or one class taken by many students (1:M from the perspective of CLASSES). This
type of relationship is illustrated in the following diagram.

When you report from or update the tables, at any one time the M:M relationship is seen from
the perspective of one of the tables (that is, it sees a 1:M relationship). You decide which
table perspective to use by making that table the parent (host) segment in the Master File or
JOIN command. Describe the join in the Master File or JOIN command as you do for a standard
one-to-many relationship.

Example:

Implementing a Many-to-Many Relationship Directly

You can use the JOIN command to describe the relationship from the perspective of the
STUDENT table as follows:

JOIN STUDENT_ID IN STUDENT TO ALL STUDENT_ID IN CLASSES

You can describe the relationship from the perspective of the CLASSES table as follows:

JOIN COURSE_CODE IN CLASSES TO ALL COURSE_CODE IN STUDENT

Describing Data With TIBCO WebFOCUS® Language

 87

Many-to-Many Relationship

Implementing a Many-to-Many Relationship Indirectly

Some non-relational data sources cannot represent a many-to-many relationship directly.
However, they can represent it indirectly, and you can describe it as such.

Consider the EMPINFO segment in the EMPLOYEE data source and the CLASSES segment in a
hypothetical SCHOOL data source. Each instance of EMPINFO describes one employee, and
each instance of CLASSES describes one course. Each employee can take many courses, and
many employees can take each course, so this is a many-to-many relationship. This type of
relationship is illustrated in the following diagram.

However, because some types of data sources cannot represent such a relationship directly,
you must introduce a mediating segment called ENROLLED. This new segment contains the
keys from both of the original segments, EMP_ID and CLASS_CODE, representing the
relationship between the two original segments. It breaks the M:M relationship into two 1:M
relationships. Each instance of EMPINFO can be related to many instances of ENROLLED
(since one employee can be enrolled in many classes), and each instance of CLASSES can be
related to many instances of ENROLLED (since one class can have many employees enrolled).

88

These relationships are illustrated in the following diagram.

3. Describing a Group of Fields

The next step is to make the mediating segment a child of one of the two original segments.
You can design the SCHOOL data source so that CLASSES is the root and ENROLLED is the
child of CLASSES. Note that when ENROLLED was an unattached segment it explicitly
contained the keys (EMP_ID and CLASS_CODE) from both original segments. Yet as part of the
SCHOOL data source, CLASS_CODE is implied by the parent-child relationship with CLASSES,
and it can be removed from ENROLLED. You can then join EMPINFO and ENROLLED together.

Describing Data With TIBCO WebFOCUS® Language

 89

Many-to-Many Relationship

This type of join is illustrated in the following diagram.

When the original M:M relationship is seen from this perspective, it looks like a 1:M:1
relationship. That is, one employee (EMPINFO) is enrolled many times (ENROLLED), and each
enrollment is for a single class (CLASSES).

When you report from or update the new structure at any one time, the relationship is seen
from the perspective of one of the original segments (in this case, from EMPINFO or CLASSES).
Determine which segment perspective is used by making that segment the parent in the join.
Describe the join using the JOIN command, or for FOCUS data sources, in the Master File. If
you make the mediating segment, in this case ENROLLED, the child (cross-referenced)
segment in the join, you implement the relationship as a standard one-to-many. If you make it
the parent (host) segment, you implement the relationship as a standard one-to-one join.

For example, you can use the JOIN command to describe the relationship from the perspective
of the CLASSES segment, making ENROLLED the join host:

JOIN EMP_ID IN ENROLLED TO EMP_ID IN EMPINFO

90

The new structure is illustrated in the following diagram.

3. Describing a Group of Fields

Another example that uses a join defined in the Master File is illustrated by the sample FOCUS
data sources EMPLOYEE and EDUCFILE. Here, ATTNDSEG is the mediating segment between
EMPINFO and COURSEG.

Recursive Relationships

Generally, you use one-to-one and one-to-many relationships to join two different segments,
usually in two different data sources. However, you can also join the same data source, or
even the same segment, to itself. This technique is called a recursive join.

See the Creating Reports With WebFOCUS Language manual for more information on recursive
joins.

Describing Data With TIBCO WebFOCUS® Language

 91

Recursive Relationships

Example:

A Recursive Join With a Single Segment

Assume that you have a single-segment data source called MANAGER, which includes the ID
number of an employee, the employee name, and the ID number of the manager of the
employee, as shown in the following image.

If you want to generate a report showing every employee ID number and name, and every
manager ID number and name, you must join the segment to itself. Issue the following
command:

JOIN MANAGER_ID IN MANAGER TO ID IN MANAGER AS BOSS

This creates the following structure:

Note: You can refer to fields uniquely in cross-referenced recursive segments by prefixing them
with the first four letters of the join name (BOSS, in this example). The only exception is the
cross-referenced field, for which the alias is prefixed instead of the field name.

92

3. Describing a Group of Fields

After you have issued the join, you can generate an answer set that looks like this:

ID      NAME               MANAGER_ID     BOSSNAME
--      ----               ----------     --------
026255  JONES              837172         CRUZ
308743  MILBERG            619426         WINOKUR
846721  YUTANG             294857         CAPRISTI
743891  LUSTIG             089413         SMITH
585693  CAPRA              842918         JOHNSON

Example:

A Recursive Join With Multiple Segments

You can join larger structures recursively as well. For example, consider a two-segment data
source called AIRCRAFT that stores a bill-of-materials for an aircraft company. The root
segment has the name and description of a part, and the child segment has the name of a
subpart. For each part, there can be many subparts. This type of joined structure is illustrated
in the following diagram.

While many of the larger parts are constructed of several levels of subparts, some of these
subparts, such as bolts, are used throughout aircraft at many different levels. It is redundant
to give each occurrence of a subpart its own segment instance. Instead, use the two-segment
design shown previously and then join the data source to itself:

JOIN SUBPART IN AIRCRAFT TO PART IN AIRCRAFT AS SUB_PART

Describing Data With TIBCO WebFOCUS® Language

 93

Recursive Relationships

This produces the following data structure.

94

3. Describing a Group of Fields

Relating Segments From Different Types of Data Sources

The JOIN command enables you to join segments from different data sources, creating
temporary data structures containing related information from otherwise incompatible sources.
For example, you can join two Oracle data sources to a FOCUS data source to a VSAM (C-ISAM
for WebFOCUS) data source, as illustrated in the following diagram.

Joins between VSAM and fixed-format data sources are also supported in a Master File, as
described in Defining a Join in a Master File on page 349.

For detailed information on using the JOIN command with different types of data sources, see
the Creating Reports With WebFOCUS Language manual.

Describing Data With TIBCO WebFOCUS® Language

 95

Rotating a Data Source: An Alternate View

Rotating a Data Source: An Alternate View

If you are using a network data source or certain hierarchical data sources, such as FOCUS,
you can rotate the data source after you have described it. This creates an alternate view that
changes some of the segment relationships and enables you to access the segments in a
different order. Customizing the access path in this way makes it easier for a given application
to access. This type of alternate view is illustrated in the following diagram.

You can join hierarchical and/or network data sources together and then create an alternate
view of the joined structure, selecting the new root segment from the host data source.

Using an alternate view can be helpful when you want to generate a report using record
selection criteria based on fields found in a lower segment (such as, segment C in the
previous diagram). You can report from an alternate view that makes this the root segment.
FOCUS then begins its record selection based on the relevant segment, and avoids reading
irrelevant ancestral segments.

When you report from a data source using an alternate view, you can access the data more
efficiently if both of the following conditions are satisfied:

The field on which the alternate view is based is indexed. For FOCUS data sources, the
alternate view field must include INDEX = I in the Master File.

96

3. Describing a Group of Fields

You use the field in a record selection test, with the WHERE or IF phrases, and make the
selection criteria an equality or range test.

You can request an alternate view on any segment in a data source, except a cross-referenced
segment. Request an alternate view with the TABLE command by naming a field from the
segment you want to view as the new root segment. The only restriction on requesting an
alternate view is that the field on which it is requested must be a real field in the data source.
It cannot be a virtual field.

This type of alternate view is illustrated in the following diagram.

The following diagram further illustrates this type of alternate view.

Describing Data With TIBCO WebFOCUS® Language

 97

Defining a Prefix for Field Titles

Syntax:

How to Specify an Alternate View

Append a field name to the file name in the reporting command, using the syntax

TABLE FILE filename.fieldname

where:

filename

Is the name of the data source on which you are defining the alternate view.

fieldname

Is a field located in the segment that you are defining as the alternate root. It must be a
real field, not a temporary field defined with the DEFINE attribute or the DEFINE or
COMPUTE commands.

If the field is declared in the Master File with the FIELDTYPE attribute set to I, and you use
the alternate view in a report, you must use the field in an equality selection test (such as
EQ) or range test.

Example:

Specifying an Alternative View

To report from the EMPLOYEE data source using an alternate view that makes the DEDUCT
segment an alternate root, issue the following TABLE FILE command:

TABLE FILE EMPLOYEE.DED_CODE

Defining a Prefix for Field Titles

If a field in a Master File has a TITLE attribute defined, this title will be used as the column
heading for the file on report output, unless the report request specifies an AS name to be
used instead.

On the segment level in a Master File, you can define a prefix for the field titles in that
segment. This is useful for distinguishing which field is being displayed on report output when
field names from different segments have the same title, as in the case when a base synonym
is used multiple times in a cluster Master File.

Reference: Define a Prefix for Field Titles

SEGMENT=segname, ... , SEG_TITLE_PREFIX='prefix', $

where:

segname

Is a valid segment name.

98

3. Describing a Group of Fields

'prefix'

Is text to be prefixed to the field title on report output, for any field in the segment that has
a TITLE attribute defined. The total length of the SEG_TITLE_PREFIX plus the TITLE string
cannot be more than 512 characters. You can split the text across as many as five
separate title lines by separating the lines with a comma (,). Include blanks at the end of a
column title by including a slash (/) in the final blank position. You must enclose the string
within single quotation marks if it includes commas or leading blanks.

If you generate a HOLD file with SET HOLDATTRS ON, the SEG_TITLE_PREFIX will be prefixed to
the original TITLE value to generate the TITLE value in the HOLD file.

Example:

Defining a Prefix for Field Titles

The following sample shows three segments from the WF_RETAIL_LITE Cluster Master File that
all reference the WF_RETAIL_TIME_LITE table. The SEG_TITLE_PREFIX in the
WF_RETAIL_TIME_SALES segment is 'Sale,'. The SEG_TITLE_PREFIX in the
WF_RETAIL_TIME_DELIVERED segment is 'Delivery,'. The SEG_TITLE_PREFIX in the
WF_RETAIL_TIME_SHIPPED segment is 'Shipped,'.

SEGMENT=WF_RETAIL_TIME_SALES, CRFILE=wfretail82/dimensions/wf_retail_time_lite,
CRSEGMENT=WF_RETAIL_TIME_LITE, CRINCLUDE=ALL,
    DESCRIPTION='Time Sales Dimension', SEG_TITLE_PREFIX='Sale,', $
   PARENT=WF_RETAIL_SALES, SEGTYPE=KU, CRJOINTYPE=LEFT_OUTER,
    JOIN_WHERE=WF_RETAIL_SALES.ID_TIME EQ WF_RETAIL_TIME_SALES.ID_TIME;, $
     ...
   SEGMENT=WF_RETAIL_TIME_DELIVERED, SEGTYPE=KU, PARENT=WF_RETAIL_SHIPMENTS,
   CRFILE=ibisamp/dimensions/wf_retail_time_lite, CRSEGMENT=WF_RETAIL_TIME_LITE,
CRINCLUDE=ALL, CRJOINTYPE=LEFT_OUTER,
    JOIN_WHERE=ID_TIME_DELIVERED EQ WF_RETAIL_TIME_DELIVERED.ID_TIME;,
    DESCRIPTION='Shipping Time Delivered Dimension', SEG_TITLE_PREFIX='Delivery,', $
     ...
  SEGMENT=WF_RETAIL_TIME_SHIPPED, SEGTYPE=KU, PARENT=WF_RETAIL_SHIPMENTS,
    CRFILE=ibisamp/dimensions/wf_retail_time_lite, CRSEGMENT=WF_RETAIL_TIME_LITE,
CRINCLUDE=ALL, CRJOINTYPE=LEFT_OUTER,
    JOIN_WHERE=ID_TIME_SHIPPED EQ WF_RETAIL_TIME_SHIPPED.ID_TIME;,
    DESCRIPTION='Shipping Time Shipped Dimension', SEG_TITLE_PREFIX='Shipped,', $

Describing Data With TIBCO WebFOCUS® Language

 99

Defining a Prefix for Field Titles

All three segments have the same fields. The SEG_TITLE_PREFIX displays on the report output
and indicates which segment the field came from. The following request sums DAYSDELAYED
by TIME_QTR:

TABLE FILE wf_retail_lite
SUM DAYSDELAYED
BY TIME_QTR
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
END

The column heading on the output shows that the TIME_QTR value is coming from the
WF_RETAIL_TIME_SALES segment, as that is the topmost segment with that field name in the
WF_RETAIL_LITE Master File.

To specify a different segment, such as WF_RETAIL_TIME_DELIVERED, use a qualified field
name in the request.

TABLE FILE wf_retail_lite
SUM DAYSDELAYED
BY WF_RETAIL_TIME_DELIVERED.TIME_QTR
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
END

100

The column heading on the output shows that the TIME_QTR value is coming from the
WF_RETAIL_TIME_DELIVERED segment.

3. Describing a Group of Fields

Example:

Generating a HOLD File When a Segment Specifies a SEG_TITLE_PREFIX

The title for the field TIME_QTR in the WF_RETAIL_TIME_LITE Master File is 'Quarter'. The
SEG_TITLE_PREFIX for the segment WF_RETAIL_TIME_DELIVERED in the WF_RETAIL_LITE
Master File is 'Delivery,'. The following request generated a HOLD file named SEGPREFIX with
the HOLDATTRS parameter set ON:

APP HOLD baseapp
TABLE FILE wf_retail_lite
SUM DAYSDELAYED
BY WF_RETAIL_TIME_DELIVERED.TIME_QTR
ON TABLE SET HOLDATTRS ON
ON TABLE HOLD AS SEGPREFIX
END

The SEGPREFIX Master File generated when you run this request has the title 'Delivery,Quarter'
for the TIME_QTR field. This title was created by concatenating the SEG_TITLE_PREFIX value
from the WF_RETAIL_LITE Master File with the TITLE value from the WF_RETAIL_TIME_LITE
Master File:

 FIELDNAME=TIME_QTR, ALIAS=E01, USAGE=I2, ACTUAL=I04,
      MISSING=ON,
      TITLE='Delivery,Quarter', DESCRIPTION='Quarter', $

Describing Data With TIBCO WebFOCUS® Language

 101

Defining a Prefix for Field Titles

102

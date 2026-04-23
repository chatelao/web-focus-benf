Chapter7

Defining a Join in a Master File

Describe a new relationship between any two segments that have at least one field in
common by joining them. The underlying data structures remain physically separate, but
are treated as if they were part of a single structure from which you can report. This
section describes how to define a join in a Master File for FOCUS, fixed-format
sequential, and VSAM data sources. For information about whether you can define a join
in a Master File to be used with other types of data sources, see the appropriate data
adapter manual.

In this chapter:

Join Types

Static Joins Defined in the Master File: SEGTYPE = KU and KM

Using Cross-Referenced Descendant Segments: SEGTYPE = KL and KLU

Dynamic Joins Defined in the Master File: SEGTYPE = DKU and DKM

Conditional Joins in the Master File

Comparing Static and Dynamic Joins

Joining to One Cross-Referenced Segment From Several Host Segments

Creating a Single-Root Cluster Master File

Creating a Multiple-Root Cluster Master File

Join Types

You can join two data sources in the following ways:

Dynamically using the JOIN command. The join lasts for the duration of the session (or
until you clear it during the session) and creates a temporary view of the data that includes
all of the segments in both data sources. You can also use the JOIN command to join two
data sources of any type, including a FOCUS data source to a non-FOCUS data source. The
JOIN command is described in detail in the Creating Reports With WebFOCUS Language
manual.

Describing Data With TIBCO WebFOCUS® Language

 349

Static Joins Defined in the Master File: SEGTYPE = KU and KM

Statically within a Master File. This method is helpful if you want to access the joined
structure frequently. The link (pointer) information needed to implement the join is
permanently stored and does not need to be retrieved for each record during each request,
saving you time. Like a dynamic Master File defined join, it is always available and retrieves
only the segments that you specify. See Static Joins Defined in the Master File: SEGTYPE =
KU and KM on page 350. This is supported for FOCUS data sources only.

Dynamically within a Master File. This method saves you the trouble of issuing the JOIN
command every time you need to join the data sources and gives you flexibility in choosing
the segments that will be available within the joined structure. See Dynamic Joins Defined
in the Master File: SEGTYPE = DKU and DKM on page 362.

Tip: Some users find it helpful to prototype a database design first using dynamic joins,
implemented by issuing the JOIN command or within the Master File. After the design is stable,
to change the frequently used joins to static joins defined in the Master File, accelerating data
source access. Static joins should be used when the target or cross-referenced data source
contents do not change. You can change dynamic joins to static joins by using the REBUILD
facility.

Note: Master File defined joins are sometimes referred to as cross-references.

Static Joins Defined in the Master File: SEGTYPE = KU and KM

Static joins allow you to relate segments in different FOCUS data sources permanently. You
specify static joins in the Master File of the host data source.

There are two types of static joins: one-to-one (SEGTYPE KU) and one-to-many (SEGTYPE KM).

You specify a one-to-one join, also known as a unique join, when you want to retrieve at
most one record instance from the cross-referenced data source for each record instance
in the host data source.

You specify a one-to-many join when you want to retrieve any number of record instances
from the cross-referenced data source.

Describing a Unique Join: SEGTYPE = KU

In the EMPLOYEE data source, there is a field named JOBCODE in the PAYINFO segment. The
JOBCODE field contains a code that specifies the employee job.

350

7. Defining a Join in a Master File

The complete description of the job and other related information is stored in a separate data
source named JOBFILE. You can retrieve the job description from JOBFILE by locating the
record whose JOBCODE corresponds to the JOBCODE value in the EMPLOYEE data source, as
shown in the following diagram:

Using a join in this situation saves you the trouble of entering and revising the job description
for every record in the EMPLOYEE data source. Instead, you can maintain a single list of valid
job descriptions in the JOBFILE data source. Changes need be made only once, in JOBFILE,
and are reflected in all of the corresponding joined EMPLOYEE data source records.

Implementing the join as a static join is most efficient because the relationship between job
codes and job descriptions is not likely to change.

Although the Employee Information and Job Description segments are stored in separate data
sources, for reporting purposes the EMPLOYEE data source is treated as though it also
contains the Job Description segment from the JOBFILE data source. The actual structure of
the JOBFILE data source is not affected.

Describing Data With TIBCO WebFOCUS® Language

 351

Static Joins Defined in the Master File: SEGTYPE = KU and KM

The EMPLOYEE data source is viewed as follows:

Syntax:

How to Specify a Static Unique Join

SEGNAME = segname, SEGTYPE = KU, PARENT = parent,
CRFILE = db_name, CRKEY = field, [CRSEGNAME = crsegname,]
[DATASET = physical_filename,] $

where:

segname

Is the name by which the cross-referenced segment will be known in the host data source.
You can assign any valid segment name, including the original name of the segment in the
cross-referenced data source.

parent

Is the name of the host segment.

db_name

Is the name of the cross-referenced data source. You can change the name without
rebuilding the data source.

field

Is the common name (field name or alias) of the host field and the cross-referenced field.
The field name or alias of the host field must be identical to the field name of the cross-
referenced field. You can change the field name without rebuilding the data source as long
as the SEGTYPE remains the same.

Both fields must have the same format type and length.

352

7. Defining a Join in a Master File

The cross-referenced field must be indexed (FIELDTYPE=I or INDEX=I).

crsegname

Is the name of the cross-referenced segment. If you do not specify this, it defaults to the
value assigned to SEGNAME. After data has been entered into the cross-referenced data
source, you cannot change the crsegname without rebuilding the data source.

physical_filename

Optionally, is the platform-dependent physical name of the data source for the CRFILE.

The SEGTYPE value KU stands for keyed unique.

Example:

Creating a Static Unique Join

SEGNAME = JOBSEG, SEGTYPE = KU, PARENT = PAYINFO,
   CRFILE = JOBFILE, CRKEY = JOBCODE, $

The relevant sections of the EMPLOYEE Master File follow (nonessential fields and segments
are not shown):

FILENAME = EMPLOYEE, SUFFIX = FOC, $
SEGNAME = EMPINFO, SEGTYPE = S1, $
   .
   .
   .
SEGNAME = PAYINFO, SEGTYPE = SH1, PARENT = EMPINFO, $
   FIELDNAME = JOBCODE,    ALIAS = JBC, FORMAT = A3, $
   .
   .
   .
SEGNAME = JOBSEG, SEGTYPE = KU, PARENT = PAYINFO,   CRFILE = JOBFILE,
   CRKEY = JOBCODE, $

Note that you only have to give the name of the cross-referenced segment. The fields in that
segment are already known from the cross-referenced data source Master File (JOBFILE in this
example). Note that the CRSEGNAME attribute is omitted, since in this example it is identical
to the name assigned to the SEGNAME attribute.

The Master File of the cross-referenced data source, as well as the data source itself, must be
accessible whenever the host data source is used. There does not need to be any data in the
cross-referenced data source.

Describing Data With TIBCO WebFOCUS® Language

 353

Static Joins Defined in the Master File: SEGTYPE = KU and KM

Using a Unique Join for Decoding

Decoding is the process of matching a code (such as the job code in our example) to the
information it represents (such as the job description). Because every code has only one set of
information associated with it, the join between the code and the information should be one-to-
one, that is, unique. You can decode using a join, as in our example, or using the DECODE
function with the DEFINE command, as described in the Creating Reports With WebFOCUS
Language manual. The join method is recommended when there are a large number of codes.

Describing a Non-Unique Join: SEGTYPE = KM

You use a one-to-many join (that is, a non-unique join) when you may have several instances of
data in the cross-referenced segment associated with a single instance in the host segment.
Using our EMPLOYEE example, suppose that you kept an educational data source named
EDUCFILE to track course work for employees. One segment in that data source, ATTNDSEG,
contains the dates on which each employee attended a given class. The segment is keyed by
attendance date. The EMP_ID field, which identifies the attendees, contains the same ID
numbers as the EMP_ID field in the EMPINFO segment of the EMPLOYEE data source.

If you want to see an employee educational record, you can join the EMP_ID field in the
EMPINFO segment to the EMP_ID field in the ATTNDSEG segment. You should make this a
one-to-many join, since you want to retrieve all instances of class attendance associated with a
given employee ID:

Syntax:

How to Specify a Static Multiple Join

The syntax for describing one-to-many joins is similar to that for one-to-one joins described in
How to Specify a Static Unique Join on page 352, except that you supply a different value, KM
(which stands for keyed multiple), for the SEGTYPE attribute, as follows:

SEGTYPE = KM

354

Example:

Specifying a Static Multiple Join

SEGNAME = ATTNDSEG, SEGTYPE = KM, PARENT = EMPINFO,
   CRFILE = EDUCFILE, CRKEY = EMP_ID, $

7. Defining a Join in a Master File

The relevant sections of the EMPLOYEE Master File follow (nonessential fields and segments
are not shown):

FILENAME = EMPLOYEE, SUFFIX = FOC, $
SEGNAME = EMPINFO,  SEGTYPE = S1, $
   FIELDNAME = EMP_ID, ALIAS = EID, FORMAT = A9, $
   .
   .
   .
SEGNAME = PAYINFO,  SEGTYPE = SH1, PARENT = EMPINFO, $
   FIELDNAME = JOBCODE, ALIAS = JBC, FORMAT = A3, $
   .
   .
   .
SEGNAME = JOBSEG,   SEGTYPE = KU,  PARENT = PAYINFO, CRFILE = JOBFILE,
   CRKEY = JOBCODE, $
   .
   .
   .
SEGNAME = ATTNDSEG, SEGTYPE = KM,  PARENT = EMPINFO, CRFILE = EDUCFILE,
   CRKEY = EMP_ID, $

Describing Data With TIBCO WebFOCUS® Language

 355

Using Cross-Referenced Descendant Segments: SEGTYPE = KL and KLU

Within a report request, both cross-referenced data sources, JOBFILE and EDUCFILE, are
treated as though they are part of the EMPLOYEE data source. The data structure resembles
the following:

Using Cross-Referenced Descendant Segments: SEGTYPE = KL and KLU

When you join two data sources, you can access any or all of the segments in the cross-
referenced data source, not just the cross-referenced segment itself. These other segments
are sometimes called linked segments. From the perspective of the host data source, all of
the linked segments are descendants of the cross-referenced segment. It is as though an
alternate view had been taken on the cross-referenced data source to make the cross-
referenced segment the root. To access a linked segment, you only need to declare it in the
Master File of the host data source.

Syntax:

How to Identify Cross-Referenced Descendant Segments

SEGNAME = segname, SEGTYPE = {KL|KLU}, PARENT = parentname,
CRFILE = db_name, [CRSEGNAME = crsegname,]
[DATASET = physical_filename,] $

356

7. Defining a Join in a Master File

where:

segname

Is the name assigned to the cross-referenced segment in the host data source.

Indicates that this segment is a descendant segment in a cross-referenced data source
(as viewed from the perspective of the host data source), and has a one-to-many
relationship to its parent. KL stands for keyed through linkage.

KL

KLU

Indicates that this segment is a descendant segment in a cross-referenced data source
(as viewed from the perspective of the host data source), and has a one-to-one
relationship to its parent. KLU stands for keyed through linkage, unique.

parentname

Is the name of the segment parent in the cross-referenced data source, as viewed from
the perspective of the host data source.

db_name

Is the name of the cross-referenced data source. You can change the name without
rebuilding the data source.

crsegname

Is the name of the cross-referenced segment. If you do not specify this, it defaults to the
value assigned to SEGNAME.

physical_filename

Optionally, is the platform-dependent physical name of the data source for the CRFILE.

Example:

Identifying a Cross-Referenced Descendant Segment

SEGNAME = SECSEG,   SEGTYPE = KLU, PARENT = JOBSEG, CRFILE = JOBFILE, $
SEGNAME = SKILLSEG, SEGTYPE = KL,  PARENT = JOBSEG, CRFILE = JOBFILE, $

Note that you do not use the CRKEY attribute in a declaration for a linked segment, since the
common join field (which is identified by CRKEY) needs to be specified only for the cross-
referenced segment.

Describing Data With TIBCO WebFOCUS® Language

 357

Using Cross-Referenced Descendant Segments: SEGTYPE = KL and KLU

Example:

Using a Cross-Referenced Descendant Segment

Consider our EMPLOYEE example. JOBFILE is a multi-segment data source:

In your EMPLOYEE data source application, you may need the security information stored in the
SECSEG segment and the job skill information stored in the SKILLSEG segment. After you have
created a join, you can access any or all of the other segments in the cross-referenced data
source using the SEGTYPE value KL for a one-to-many relationship (as seen from the host data
source), and KLU for a one-to-one relationship (as seen from the host data source). KL and
KLU are used to access descendant segments in a cross-referenced data source for both
static (KM) and dynamic (DKM) joins.

358

When the JOBSEG segment is retrieved from JOBFILE, it also retrieves all of the children for
JOBSEG that were declared with KL or KLU SEGTYPEs in the EMPLOYEE Master File:

7. Defining a Join in a Master File

Describing Data With TIBCO WebFOCUS® Language

 359

Using Cross-Referenced Descendant Segments: SEGTYPE = KL and KLU

Example:

Using a Cross-Referenced Ancestral Segment

Remember that you can retrieve all of the segments in a cross-referenced data source,
including both descendants and ancestors of the cross-referenced segment. Ancestor
segments should be declared in the host Master File with a SEGTYPE of KLU, as a segment
can have only one parent and so, from the perspective of the host data source, this is a one-
to-one relationship.

Consider the EDUCFILE data source used in our example. The COURSEG segment is the root
and describes each course. ATTNDSEG is a child and includes employee attendance
information:

When you join EMPINFO in EMPLOYEE to ATTNDSEG in EDUCFILE, you can access course
descriptions in COURSEG by declaring it as a linked segment.

360

From this perspective, COURSEG is a child of ATTNDSEG, as shown in the following diagram.

7. Defining a Join in a Master File

The sections of the EMPLOYEE Master File used in the examples follow (nonessential fields
and segments are not shown).

FILENAME = EMPLOYEE, SUFFIX = FOC, $
SEGNAME = EMPINFO, SEGTYPE = S1, $
   FIELDNAME = EMP_ID, ALIAS = EID, FORMAT = A9, $
   .
   .
   .
SEGNAME = PAYINFO, SEGTYPE = SH1, PARENT = EMPINFO, $
   FIELDNAME = JOBCODE, ALIAS = JBC, FORMAT = A3, $
   .
   .
   .
SEGNAME = JOBSEG,  SEGTYPE = KU, PARENT = PAYINFO,  CRFILE = JOBFILE,
   CRKEY = JOBCODE, $
SEGNAME = SECSEG,  SEGTYPE = KLU,PARENT = JOBSEG,   CRFILE = JOBFILE, $
SEGNAME = SKILLSEG,SEGTYPE = KL, PARENT = JOBSEG,   CRFILE = JOBFILE, $
SEGNAME = ATTNDSEG,SEGTYPE = KM, PARENT = EMPINFO,  CRFILE = EDUCFILE,
   CRKEY = EMP_ID, $
SEGNAME = COURSEG, SEGTYPE = KLU,PARENT = ATTNDSEG, CRFILE = EDUCFILE, $

Describing Data With TIBCO WebFOCUS® Language

 361

Dynamic Joins Defined in the Master File: SEGTYPE = DKU and DKM

Hierarchy of Linked Segments

A KL segment may lead to other KL segments. Graphically, this can be illustrated as:

The letters on the arrows are the SEGTYPEs.

Note that segment G may either be a unique descendant of B or the parent of B.

Dynamic Joins Defined in the Master File: SEGTYPE = DKU and DKM

You can define a dynamic join in a Master File using the SEGTYPE attribute. There are two
types of dynamic Master File defined joins: one-to-one (SEGTYPE DKU) and one-to-many
(SEGTYPE DKM).

As with a static join, specify a one-to-one join, also known as a unique join, when you want
to retrieve at most one record instance from the cross-referenced data source for each
record instance in the host data source.

You specify a one-to-many join when you want to retrieve any number of record instances
from the cross-referenced data source.

The difference between static and dynamic joins deals with storage, speed, and flexibility:

The links (pointers) for a static join are retrieved once and then permanently stored in the
host data source (and automatically updated as needed).

The links for a dynamic join are not saved and need to be retrieved for each record in each
report request.

362

7. Defining a Join in a Master File

This makes static joins much faster than dynamic ones, but harder to change. You can
redefine or remove a static join only using the REBUILD facility. You can redefine or remove a
dynamic join at any time by editing the Master File.

Syntax:

How to Specify a Dynamic Join in a Master File

You specify a dynamic Master File defined join the same way that you specify a static join (as
described in How to Specify a Static Unique Join on page 352), except that the value of the
SEGTYPE attribute for the cross-referenced segment is DKU (standing for dynamic keyed
unique) for a one-to-one join, and DKM (standing for dynamic keyed multiple) for a one-to-many
join.

For example:

SEGNAME = JOBSEG, SEGTYPE = DKU, PARENT = PAYINFO,
   CRFILE = JOBFILE, CRKEY = JOBCODE, $

You declare linked segments in a dynamic join the same way that you do in a static join. In
both cases, SEGTYPE has a value of KLU for unique linked segments, and KL for non-unique
linked segments.

Example:

Specifying a Dynamic Join in a Master File

The following Master File includes the relevant sections of EMPLOYEE and the segments joined
to it, but with the static joins replaced by dynamic joins (nonessential fields and segments are
not shown):

FILENAME = EMPLOYEE, SUFFIX = FOC, $
SEGNAME = EMPINFO, SEGTYPE = S1, $
   FIELDNAME = EMP_ID,   ALIAS = EID, FORMAT = A9, $
   .
   .
   .
SEGNAME = PAYINFO, SEGTYPE = SH1,  PARENT = EMPINFO, $
   FIELDNAME = JOBCODE,   ALIAS = JBC, FORMAT = A3, $
   .
   .
   .
SEGNAME = JOBSEG,  SEGTYPE = DKU,  PARENT = PAYINFO, CRFILE = JOBFILE,
   CRKEY = JOBCODE, $
SEGNAME = SECSEG,  SEGTYPE = KLU,  PARENT = JOBSEG,  CRFILE = JOBFILE, $
SEGNAME = SKILLSEG,SEGTYPE = KL,   PARENT = JOBSEG,  CRFILE = JOBFILE, $
SEGNAME = ATTNDSEG,SEGTYPE = DKM,  PARENT = EMPINFO, CRFILE = EDUCFILE,
   CRKEY = EMP_ID, $
SEGNAME = COURSEG, SEGTYPE = KLU,  PARENT = ATTNDSEG,CRFILE = EDUCFILE,$

Describing Data With TIBCO WebFOCUS® Language

 363

Conditional Joins in the Master File

Conditional Joins in the Master File

The conditional (or WHERE-based) join describes how to relate rows from two data sources
based on any condition. In this type of embedded join, the Master File for one data source
contains a cross-reference to the Master File for the other data source. When used to relate
non-FOCUS data sources, a conditional embedded join does not require a multi-table Access
File.

Syntax:

How to How to Define a Conditional Join in the Master File

The conditions specified in the join are considered virtual fields in the Master File. You can use
the CRJOINTYPE attribute to specify the type of join.

FILENAME=filename, SUFFIX=suffix   [,$]
 SEGNAME=file1, SEGTYPE= {S0|KL} [,CRFILE=crfile1] [,$]
  FIELD=name1,...,$
  .
  .
  .
SEGNAME=seg,  SEGTYPE=styp,  PARENT=parseg,
        CRFILE=xmfd,  [CRSEG=xseg,  ], [CRJOINTYPE = {INNER|LEFT_OUTER}]
        JOIN_WHERE=expression; [JOIN_WHERE=expression; ...] ,$

where:

filename

Is the name of the Master File.

suffix

Is the SUFFIX value.

file1

Is the SEGNAME value for the parent segment.

name

Is any field name.

seg

Is the segment name for the joined segment. Only this segment participates in the join,
even if the cross-referenced Master File describes multiple segments.

styp

Is the segment type for the joined segment. Can be DKU, DKM, KU, or KM, as with
traditional cross-references in the Master File.

364

7. Defining a Join in a Master File

Note: If you specify a unique join when the relationship between the host and cross-
referenced files is one-to-many, the results will be unpredictable.

parseg

Is the parent segment name.

xmfd

Is the cross-referenced Master File.

xseg

Is the cross-referenced segment, if seg is not the same name as the SEGNAME in the
cross-referenced Master File.

expression

Is any expression valid in a DEFINE FILE command. All of the fields referenced in all of the
expressions must lie on a single path.

Example:

Using a Conditional Join in the Master File

The following Master File named EMPDATAJ1 defines a conditional join between the EMPDATA
and JOBHIST data sources.

FILENAME=EMPDATA, SUFFIX=FOC  , DATASET=ibisamp/empdata.foc
SEGNAME=EMPDATA,  SEGTYPE=S1
 FIELDNAME=PIN,          ALIAS=ID,       FORMAT=A9,  INDEX=I,    $
 FIELDNAME=LASTNAME,     ALIAS=LN,       FORMAT=A15,             $
 FIELDNAME=FIRSTNAME,    ALIAS=FN,       FORMAT=A10,             $
 FIELDNAME=MIDINITIAL,   ALIAS=MI,       FORMAT=A1,              $
 FIELDNAME=DIV,          ALIAS=CDIV,     FORMAT=A4,              $
 FIELDNAME=DEPT,         ALIAS=CDEPT,    FORMAT=A20,             $
 FIELDNAME=JOBCLASS,     ALIAS=CJCLAS,   FORMAT=A8,              $
 FIELDNAME=TITLE,        ALIAS=CFUNC,    FORMAT=A20,             $
 FIELDNAME=SALARY,       ALIAS=CSAL,     FORMAT=D12.2M,          $
 FIELDNAME=HIREDATE,     ALIAS=HDAT,     FORMAT=YMD,             $
SEGNAME=JOBHIST, PARENT=EMPDATA,  SEGTYPE=DKM, CRFILE=ibisamp/jobhist,
CRJOINTYPE=INNER,$
   JOIN_WHERE = EMPDATA.JOBCLASS CONTAINS '257' AND JOBHIST.JOBCLASS
CONTAINS '019';$

Describing Data With TIBCO WebFOCUS® Language

 365

Conditional Joins in the Master File

The following request uses the joined Master File.

TABLE FILE EMPDATAJ1
SUM SALARY TITLE AS 'Empdata Title' FUNCTITLE AS 'Jobhist Title'
BY LASTNAME
BY FIRSTNAME
BY EMPDATA.JOBCLASS AS 'Empdata Job'
BY JOBHIST.JOBCLASS AS 'Jobhist Job'
WHERE LASTNAME LT 'D'
ON TABLE SET PAGE NOPAGE

ON TABLE SET STYLE *
GRID=OFF,$
FONT=ARIAL, SIZE=8,$
TYPE=TITLE, STYLE=BOLD,$
END

The following image shows that all of the job class values from the EMPDATA segment start
with the characters 257, and all of the job class values from the JOBHIST segment start with
the characters 019, as specified in the join condition:

366


Comparing Static and Dynamic Joins

7. Defining a Join in a Master File

To join two FOCUS data sources, you can choose between two types of joins (static and
dynamic) and two methods of defining the join (defined in the Master File and defined by
issuing the JOIN command).

For a static join, the links, which point from a host segment instance to the corresponding
cross-referenced segment instance, are created once and then permanently stored and
automatically maintained in the host data source.

For a dynamic join, the links are retrieved each time needed. This makes static joins faster
than dynamic ones, since the links only need to be established once, but less flexible, as
you can redefine or remove a static join only by using the REBUILD facility or reloading the
file with MODIFY or Maintain Data.

Among dynamic joins, the JOIN command is easier to use in that you do not need to edit the
Master File each time you want to change the join specification, and you do not need to
describe each linked segment as it appears from the perspective of the host data source. On
the other hand, Master File defined dynamic joins enable you to omit unnecessary cross-
referenced segments.

You may find it efficient to implement frequently used joins as static joins. You can change
static joins to dynamic, and dynamic to static, using the REBUILD facility.

The following chart compares implementing a static join defined in a Master File, a dynamic
join defined in a Master File, and a dynamic join defined by issuing the JOIN command.

Join Type

Advantages

Disadvantages

Static Join in
Master File

Faster after first use. Links are
created only once.

(SEGTYPE = KU or
KM)

Always in effect.

Can select some linked
segments and omit others.

Must be specified before data
source is created or reloaded
using REBUILD.

Requires REBUILD facility to
change.

Requires four bytes of file space
per instance.

User needs to know how to
specify relationships for linked
segments (KL, KLU).

Describing Data With TIBCO WebFOCUS® Language

 367

Joining to One Cross-Referenced Segment From Several Host Segments

Join Type

Advantages

Disadvantages

Dynamic Join in
Master File

(SEGTYPE =DKU or
DKM)

Dynamic Join
(using the JOIN
Command)

Can be specified at any time.

Always in effect. Does not use
any space in the data source.

Can be changed or removed as
needed, without using the
REBUILD facility.

Can select some linked
segments and omit others.

Can be specified at any time.

Does not use any space in the
data source. Can be changed
or removed as needed, without
using the REBUILD facility.

User never needs to describe
relationships of linked
segments.

Slower. Links are retrieved for
each record in each report
request.

User needs to know how to
specify relationships for linked
segments (KL, KLU).

Slower. Links are retrieved for
each record in each report
request.

JOIN command must be issued in
each session in which you want
the join to be in effect.

All segments in the target are
always included, whether or not
you need them.

Joining to One Cross-Referenced Segment From Several Host Segments

You may come upon situations where you need to join to one cross-referenced segment from
several different segments in the host data source. You may also find a need to join to one
cross-referenced segment from two different host data sources at the same time. You can
handle these data structures using Master File defined joins.

368

7. Defining a Join in a Master File

Joining From Several Segments in One Host Data Source

In an application, you may want to use the same cross-referenced segment in several places in
the same data source. Suppose, for example, that you have a data source named COMPFILE
that maintains data on companies you own:

The DIVSEG segment contains an instance for each division and includes fields for the name
of the division and its manager. Similarly, the PRODSEG segment contains an instance for
each product and the name of the product manager.

Retrieve personal information for both the product managers and the division managers from a
single personnel data source, as shown below:

Describing Data With TIBCO WebFOCUS® Language

 369

Joining to One Cross-Referenced Segment From Several Host Segments

You cannot retrieve this information with a standard Master File defined join because there are
two cross-reference keys in the host data source (PRODMGR and DIVMGR) and in your reports
you will want to distinguish addresses and dates of birth retrieved for the PRODSEG segment
from those retrieved for the DIVSEG segment.

A way is provided for you to implement a join to the same cross-referenced segment from
several segments in the one host data source. You can match the cross-referenced and host
fields from alias to field name and uniquely rename the fields.

The Master File of the PERSFILE could look like this:

FILENAME = PERSFILE, SUFFIX = FOC, $
SEGNAME = IDSEG, SEGTYPE = S1, $
   FIELD = NAME,     ALIAS = FNAME, FORMAT = A12,     INDEX=I, $
   FIELD = ADDRESS,  ALIAS = DAS,   FORMAT = A24,              $
   FIELD = DOB,      ALIAS = IDOB,  FORMAT = YMD,              $

You use the following Master File to join PERSFILE to COMPFILE. Note that there is no record
terminator ($) following the cross-referenced segment declaration (preceding the cross-
referenced field declarations).

FILENAME = COMPFILE, SUFFIX = FOC, $
 SEGNAME = COMPSEG, SEGTYPE = S1, $
   FIELD = COMPANY,   ALIAS = CPY,     FORMAT = A40,           $
 SEGNAME = DIVSEG,  PARENT = COMPSEG, SEGTYPE = S1, $
   FIELD = DIVISION,  ALIAS = DV,      FORMAT = A20,           $
   FIELD = DIVMGR,    ALIAS = NAME,    FORMAT = A12,           $
 SEGNAME = ADSEG,   PARENT = DIVSEG,  SEGTYPE = KU,
  CRSEGNAME = IDSEG, CRKEY = DIVMGR, CRFILE = PERSFILE,
   FIELD = NAME,      ALIAS = FNAME,   FORMAT = A12, INDEX = I,$
   FIELD = DADDRESS,  ALIAS = ADDRESS, FORMAT = A24,           $
   FIELD = DDOB,      ALIAS = DOB,     FORMAT = YMD,           $
 SEGNAME = PRODSEG, PARENT = COMPSEG, SEGTYPE = S1, $
   FIELD = PRODUCT,   ALIAS = PDT,     FORMAT = A8,            $
   FIELD = PRODMGR,   ALIAS = NAME,    FORMAT = A12,           $
 SEGNAME = BDSEG,   PARENT = PRODSEG, SEGTYPE = KU,
  CRSEGNAME = IDSEG, CRKEY = PRODMGR, CRFILE = PERSFILE,
   FIELD = NAME,      ALIAS = FNAME,   FORMAT = A12, INDEX = I,$
   FIELD = PADDRESS,  ALIAS = ADDRESS, FORMAT = A24,           $
   FIELD = PDOB,      ALIAS = DOB,     FORMAT = YMD,           $

DIVMGR and PRODMGR are described as CRKEYs. The common alias, NAME, is automatically
matched to the field name NAME in the PERSFILE data source. In addition, the field
declarations following the join information rename the ADDRESS and DOB fields to be referred
to separately in reports. The actual field names in PERSFILE are supplied as aliases.

370

7. Defining a Join in a Master File

Note that the NAME field cannot be renamed since it is the common join field. It must be
included in the declaration along with the fields being renamed, as it is described in the cross-
referenced data source. That it cannot be renamed is not a problem, since its ALIAS can be
renamed and the field does not need to be used in reports. Because it is the join field, it
contains exactly the same information as the DIVMGR and PRODMGR fields.

The following conventions must be observed:

The common join field FIELDNAME or ALIAS in the host data source must be identical to its
FIELDNAME in the cross-referenced data source.

The common join field should not be renamed, but the alias can be changed. The other
fields in the cross-referenced segment can be renamed.

Place field declarations for the cross-referenced segment after the cross-referencing
information in the Master File of the host data source, in the order in which they actually
occur in the cross-referenced segment. Omit the record terminator ($) at the end of the
cross-referenced segment declaration in the host Master File, as shown:

SEGNAME = BDSEG, PARENT = PRODSEG, SEGTYPE = KU,
 CRSEGNAME = IDSEG, CRKEY = PRODMGR, CRFILE = PERSFILE,
  FIELD = NAME,     ALIAS = FNAME,   FORMAT = A12 ,INDEX=I, $
  FIELD = PADDRESS, ALIAS = ADDRESS, FORMAT = A24         , $
  FIELD = PDOB,     ALIAS = DOB,     FORMAT = YMD         , $

Joining From Several Segments in Several Host Data Sources: Multiple Parents

At some point, you may need to join to a cross-referenced segment from two different host
data sources at the same time. If you were to describe a structure like this as a single data
source, you would have to have two parents for the same segment, which is invalid. You can,
however, describe the information in separate data sources, using joins to achieve a similar
effect.

Describing Data With TIBCO WebFOCUS® Language

 371

Joining to One Cross-Referenced Segment From Several Host Segments

Consider an application that keeps track of customer orders for parts, warehouse inventory of
parts, and general part information. If this were described as a single data source, it would be
structured as follows:

You can join several data sources to create this structure. For example:

The CUSTOMER and ORDER segments are in the ORDERS data source, the WAREHOUSE and
STOCK segments are in the INVENTRY data source, and the PRODINFO segment is stored in
the PRODUCTS data source. Both the INVENTRY and ORDERS data sources have one-to-one
joins to the PRODUCTS data source. In the INVENTRY data source, STOCK is the host
segment. In the ORDERS data source, ORDER is the host segment.

372

7. Defining a Join in a Master File

In addition, there is a one-to-many join from the STOCK segment in the INVENTRY data source
to the ORDER segment in the ORDERS data source, and a reciprocal one-to-many join from the
ORDER segment in the ORDERS data source to the STOCK segment in the INVENTRY data
source.

The joins among these three data sources can be viewed from the perspectives of both host
data sources, approximating the multiple-parent structure described earlier.

Recursive Reuse of a Segment

In rare cases, a data source may cross-reference itself. Consider the case of a data source of
products, each with a list of parts that compose the product, where a part may itself be a
product and have subparts. Schematically, this would appear as:

Describing Data With TIBCO WebFOCUS® Language

 373

Creating a Single-Root Cluster Master File

A description for this case, shown for two levels of subparts, is:

See the Creating Reports With WebFOCUS Language manual for more information on recursive
joins.

Creating a Single-Root Cluster Master File

A cluster Master File is a Master File in which different segments describe separate data
sources, which may be of varying types. The SEGSUF attribute specifies the suffix for a specific
segment, if it is different from the SUFFIX for the top segment.

Note: a FOCUS segment cannot be the top segment in a cluster Master File with varying
SUFFIX values.

Reading a Field Containing Delimited Values as individual Rows

A field that contains a list of delimited values (such as email addresses separated by spaces)
can be pivoted to be read as individual rows, when an additional segment is added with
SEGSUF=DFIX (Delimited Flat File).

374

Syntax:

How to Read a Field Containing Delimited Values as Individual Rows

In the Master File, add a segment definition with SEGTYPE=S0, SEGSUF=DFIX, and a POSITION
attribute that points to the field with delimited values.

7. Defining a Join in a Master File

SEGNAME=parentseg, SUFFIX=suffix, SEGTYPE=S1,$
 FIELD=FIELD1,  ...,$
 FIELD=delimitedfield, ALIAS=alias1, USAGE=fmt, ACTUAL=afmt,$
   ...
SEGNAME=dfixsegname, PARENT=parentseg, SEGSUF=DFIX,
  POSITION=delimitedfield,$
  FIELD=name, ALIAS=alias2, USAGE=fmt, ACTUAL=afmt,$
   ...

Create an Access File that specifies the row delimiter and any other DFIX attributes for the
DFIX segment.

 SEGNAME=dfixsegname, RDELIMITER='delimiter', $

where:

delimitedfield

Is the name of the delimited field.

alias1

Is the alias of the delimited field.

fmt

Is the USAGE format for the delimited field.

afmt

Is the ACTUAL format for the delimited field.

dfixsegname

Is the segment name of the added segment definition for the DFIX field.

parentseg

Is the name of the segment that actually contains the delimited field.

name

Is the name for the pieces of the delimited field.

alias2

Is the alias for the pieces of the delimited field.

Describing Data With TIBCO WebFOCUS® Language

 375

Creating a Single-Root Cluster Master File

delimiter

Is the delimiter in the DFIX field.

When you issue a request, the field will be treated as separate rows based on the delimiter.

Example:

Reading a Field Containing Delimited Values as Individual Rows

The following file named COUNTRYL.FTM contains country names and the longitude and
latitude values of their capitals, The longitude and latitude values are stored as a single field
named LNGLAT, separated by a comma:

Argentina      -64.0000000,-34.0000000
Australia      133.0000000,-27.0000000
Austria        13.3333000,47.3333000
Belgium        4.0000000,50.8333000
Brazil         -55.0000000,-10.0000000
Canada         -95.0000000,60.0000000
Chile          -71.0000000,-30.0000000
China          105.0000000,35.0000000
Colombia       -72.0000000,4.0000000
Denmark        10.0000000,56.0000000
Egypt          30.0000000,27.0000000
Finland        26.0000000,64.0000000
France         2.0000000,46.0000000
Germany        9.0000000,51.0000000
Greece         22.0000000,39.0000000
Hungary        20.0000000,47.0000000
India          77.0000000,20.0000000
Ireland        -8.0000000,53.0000000
Israel         34.7500000,31.5000000
Italy          12.8333000,42.8333000
Japan          138.0000000,36.0000000
Luxembourg     6.1667000,49.7500000
Malaysia       112.5000000,2.5000000
Mexico         -102.0000000,23.0000000
Netherlands    5.7500000,52.5000000
Norway         10.0000000,62.0000000
Philippines    122.0000000,13.0000000
Poland         20.0000000,52.0000000
Portugal       -8.0000000,39.5000000
Singapore      103.8000000,1.3667000
South Africa   24.0000000,-29.0000000
South Korea    127.5000000,37.0000000
Spain          -4.0000000,40.0000000
Sweden         15.0000000,62.0000000
Switzerland    8.0000000,47.0000000
Taiwan         121.0000000,23.5000000
Thailand       100.0000000,15.0000000
Tunisia        9.0000000,34.0000000
Turkey         35.0000000,39.0000000
United Kingdom -.1300000,51.5000000
United States  -97.0000000,38.0000000

376

7. Defining a Join in a Master File

Following is the original Master File, COMMA1.

FILENAME=COMMA1  , SUFFIX=FIX, IOTYPE=STREAM
 DATASET=appname/countryl.ftm, $
   SEGNAME=COU, SEGTYPE=S1, $
     FIELDNAME=COUNTRY, ALIAS=E01, USAGE=A15, ACTUAL=A15, $
     FIELDNAME=LNGLAT, ALIAS=LNGLAT,USAGE=A25, ACTUAL=A25, $

Following is the COMMA2 Master File, with the DFIX segment added.

FILENAME=COMMA2  , SUFFIX=FIX, IOTYPE=STREAM,
 DATASET=appname/countryl.ftm, $
   SEGNAME=COU, SEGTYPE=S1, $
     FIELDNAME=COUNTRY, ALIAS=E01, USAGE=A15, ACTUAL=A15, $
     FIELDNAME=LNGLAT, ALIAS=LNGLAT,USAGE=A25, ACTUAL=A25, $
   SEGNAME=COMMA2, SEGTYPE=S0, SEGSUF=DFIX,PARENT=COU,POSITION=LNGLAT,$
     FIELD=COORD, ALIAS = XY, USAGE=A25, ACTUAL=A25,$

Following is the COMMA2 Access File.

SEGNAME=COMMA2, RDELIMITER=',', HEADER=NO, PRESERVESPACE=NO, $

The following request uses the COMMA2 Master File to print the values.

TABLE FILE COMMA2
PRINT COORD
BY COUNTRY
END

On the output, the LNGLAT field has been treated as two separate records. The partial output
follows:

COUNTRY          COORD
-------          -----
Argentina        -64.0000000
                 -34.0000000
Australia        133.0000000
                 -27.0000000
Austria          13.3333000
                 47.3333000
Belgium          4.0000000
                 50.8333000
Brazil           -55.0000000
                 -10.0000000
Canada           -95.0000000
                 60.0000000
Chile            -71.0000000
                 -30.0000000
China            105.0000000
                 35.0000000
Colombia         -72.0000000

Describing Data With TIBCO WebFOCUS® Language

 377

Creating a Multiple-Root Cluster Master File

Creating a Multiple-Root Cluster Master File

A cluster Master File is a Master File in which each segment is added to the cluster by
reference using a CRFILE attribute that points to the base synonym. Child segments are joined
to their parents using a JOIN WHERE attribute. A cluster Master File can have multiple root
segments. In this case, the root segments are usually fact tables and the child segments are
usually dimension tables, as found in a star schema. This type of structure is called a multi-
fact cluster.

Each fact table that is a root of the cluster must have a PARENT=. attribute in the Master File
to identify it as a root segment.

A dimension table can be a child of multiple fact tables (called a shared dimension) or be a
child of a single fact table (called a non-shared dimension). Each shared dimension has
multiple PARENT attributes in the Master File.

The following image shows a simple multi-fact structure.

For information about reporting against a multi-fact Master File, see the Creating Reports With
WebFOCUS Language manual.

378

7. Defining a Join in a Master File

Syntax:

How to Define a Multi-Fact Cluster

Each root segment description must have a PARENT=. attribute in the Master File. The
following syntax describes the attributes necessary to define a root segment in a multi-fact
cluster. All other segment attributes are also supported.

SEGMENT=rsegname, PARENT=., CRFILE=[rapp/]rfilename,
         CRINCLUDE=ALL,$

where:

SEGMENT=rsegname

Is the name of the root segment.

PARENT=.

Defines this segment as a root segment in a multi-fact cluster.

CRFILE=[rapp/]rfilename

Is the optional application path and the name of the Master File where the root fact table
is described.

CRINCLUDE=ALL

Makes all fields from the fact table accessible using this cluster Master File. If you omit
this attribute, you must list the fields from the fact table that you want to be accessible
using this Master File.

The following is an example of a root segment description from the WF_RETAIL_LITE Master
File that is in the wfretail application.

SEGMENT=WF_RETAIL_SALES, PARENT=., CRFILE=wfretail/facts/wf_retail_sales,
      CRINCLUDE=ALL, DESCRIPTION='Sales Fact', $

Each shared dimension must have multiple PARENT attributes in the Master File and a JOIN
WHERE attribute for each parent. The following syntax describes the attributes necessary to
define a shared dimension in a multi-fact cluster Master File.

 SEGMENT=dsegname, CRFILE=[dapp/]dfilename,
          [CRSEGMENT=crsegname,] CRINCLUDE=ALL,$
     PARENT=parent1, SEGTYPE=KU, CRJOINTYPE=jointype1,
       JOIN_WHERE=expression1;, $
    PARENT=parent2, SEGTYPE=KU, JOIN_TYPE=jointype2,
       JOIN_WHERE=expression2;,
    . . . $

where:

SEGMENT=dsegname

Is the name of the shared dimension segment.

Describing Data With TIBCO WebFOCUS® Language

 379

Creating a Multiple-Root Cluster Master File

CRFILE=[dapp/]dfilename

Is the optional application path and the name of the Master File where the dimension table
is described.

CRSEGMENT=crsegname

Is the name of the segment to which to join in the dimension Master File. This is optional
if the dimension Master File has a single segment.

CRINCLUDE=ALL

Makes all fields from the dimension table accessible using this cluster Master File. If you
omit this attribute, you must list the fields from the fact table that you want to be
accessible using this Master File.

PARENT=parent1 PARENT=parent2 ...

Are the names of the parent segments of the shared dimension.

CRJOINTYPE=jointype1

Is a supported join type for the join between the shared dimension and the first parent
segment. Valid values are INNER, LEFT-OUTER, RIGHT-OUTER, FULL-OUTER. The type of
join specified must be supported by the relational engine in which the tables are defined.

JOIN_TYPE=jointype2

Is a supported join type a join between the shared dimension and a subsequent parent
segment. Valid values are INNER, LEFT-OUTER, RIGHT-OUTER, FULL-OUTER. The type of
join specified must be supported by the relational engine in which the tables are defined.

JOIN_WHERE=expression1; JOIN_WHERE=expression2;

Are the join expressions for the joins between each parent segment and the shared
dimension.

For a synonym that describes a star schema, each expression usually describes an
equality condition (using the EQ operator) and a 1-to-many relationship.

The following is an example of a shared dimension segment definition from the
WF_RETAIL_LITE Master File, where the synonym is defined in the wfretail application.

SEGMENT=WF_RETAIL_CUSTOMER, CRFILE=wfretail/dimensions/wf_retail_customer,
       CRINCLUDE=ALL, DESCRIPTION='Customer Dimension', $
   PARENT=WF_RETAIL_SALES, SEGTYPE=KU, CRJOINTYPE=LEFT_OUTER,
    JOIN_WHERE=WF_RETAIL_SALES.ID_CUSTOMER EQ
      WF_RETAIL_CUSTOMER.ID_CUSTOMER;, $
   PARENT=WF_RETAIL_SHIPMENTS, SEGTYPE=KU, JOIN_TYPE=LEFT_OUTER,
    JOIN_WHERE=WF_RETAIL_SHIPMENTS.ID_CUSTOMER EQ
       WF_RETAIL_CUSTOMER.ID_CUSTOMER;, $

380

7. Defining a Join in a Master File

The following is an example of a non-shared dimension segment definition from the
WF_RETAIL_LITE Master File, where the synonym is defined in in the wfretail application.

SEGMENT=WF_RETAIL_TIME_DELIVERED, SEGTYPE=KU, PARENT=WF_RETAIL_SHIPMENTS,
      CRFILE=wfretail/dimensions/wf_retail_time_lite,
      CRSEGMENT=WF_RETAIL_TIME_LITE,
      CRINCLUDE=ALL, CRJOINTYPE=LEFT_OUTER,
      JOIN_WHERE=ID_TIME_DELIVERED EQ WF_RETAIL_TIME_DELIVERED.ID_TIME;,
      DESCRIPTION='Shipping Time Delivered Dimension',
      SEG_TITLE_PREFIX='Delivery,', $

Describing Data With TIBCO WebFOCUS® Language

 381

Creating a Multiple-Root Cluster Master File

382

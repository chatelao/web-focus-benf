Chapter6

Describing a FOCUS Data Source

The following covers data description topics unique to FOCUS data sources:

Design tips. Provides suggestions for designing a new FOCUS data source or
changing the design of an existing data source.

Describing segments. Contains information about Master File segment declarations
for FOCUS data sources, including defining segment relationships, keys, and sort
order using the SEGTYPE attribute, and storing segments in different locations using
the LOCATION attribute.

Describing fields. Contains information about Master File field declarations for
FOCUS data sources, including the FIND option of the ACCEPT attribute, indexing
fields using the INDEX attribute, redefining sequences of fields using the GROUP
attribute, and the internal storage requirements of each data type defined by the
FORMAT attribute, and of null values described by the MISSING attribute.

Describing partitioned data sources. Contains information about Master File and
Access File declarations for intelligently partitioned FOCUS data sources.

In this chapter:

Types of FOCUS Data Sources

Designing a FOCUS Data Source

Describing a Single Segment

GROUP Attribute

ACCEPT Attribute

INDEX Attribute

Describing a Partitioned FOCUS Data Source

Multi-Dimensional Index (MDI)

Describing Data With TIBCO WebFOCUS® Language

 293

Types of FOCUS Data Sources

Types of FOCUS Data Sources

The type of FOCUS data source you create depends on the amount of storage you require:

FOCUS data sources with SUFFIX = FOC consist of 4K database pages.

XFOCUS data sources with SUFFIX = XFOCUS consist of 16K database pages.

The following table lists the usable bytes in a segment in FOCUS and XFOCUS data sources.

Type of Segment

FOCUS Data Source

XFOCUS Data Source

Segment in a single-
segment Master File

Root or leaf of a multi
segment Master File

3968

3964

Any other type of segment

3960

16284

16280

16276

Using a SUFFIX=FOC Data Source

The FOCUS data source size can be a maximum of two gigabytes per physical data file.
Through partitioning, one logical FOCUS data source can consist of up to 1022 physical files of
up to two gigabytes each.

Using an XFOCUS Data Source

The XFOCUS data source is a database structure that parallels the original FOCUS data
source, but extends beyond its capabilities with several significant performance and data
volume improvements:

Allows over four times the amount of data per segment instance.

Holds 16 times as much data in a single physical file - up to 32 gigabytes.

With the multi-dimensional index (MDI) paradigm, sophisticated indexed searches are
possible, with retrieval time improved by as much as 90%. (Performance without the MDI
may show only marginal improvement.)

The XFOCUS data source has 16K database pages. The SUFFIX in the Master File is XFOCUS.
FOCUS data sources (SUFFIX=FOC) have 4K database pages.

All existing commands that act on FOCUS files work on XFOCUS files. No new syntax is
required, except for MDI options.

294

6. Describing a FOCUS Data Source

You can convert to an XFOCUS data source from a FOCUS data source by changing the SUFFIX
in the Master File and applying the REBUILD utility.

Syntax:

How to Specify an XFOCUS Data Source

FILE = filename, SUFFIX = XFOCUS, $

where:

filename

Can be any valid file name.

Syntax:

How to Control the Number of Pages Used for XFOCUS Data Source Buffers

FOCUS data sources use buffer pages that are allocated by the BINS setting. Buffer pages for
XFOCUS data sources are allocated by the XFOCUSBINS setting

SET XFOCUSBINS = n

where:

n

Is the number of pages used for XFOCUS data source buffers. Valid values are 16 to
1023. 64 is the default value.

The memory is not actually allocated until an XFOCUS data source is used in the session.
Therefore, if you issue the ? SET XFOCUSBINS query command, you will see the number of
pages set for XFOCUS buffers and an indication of whether the memory has actually been
allocated (passive for no, active for yes).

Describing Data With TIBCO WebFOCUS® Language

 295

Types of FOCUS Data Sources

Procedure: How to Create an XFOCUS Data Source

There are two methods for creating an XFOCUS data source. You can either issue the CREATE
FILE command or use the HOLD FORMAT XFOCUS command.

Do the following to create an XFOCUS data source using the CREATE FILE command:

1. Create a Master File that specifies SUFFIX=XFOCUS.

2.

Issue the CREATE FILE command

CREATE FILE name

where:

name

Is the name of the Master File that specifies SUFFIX=XFOCUS.

Reference: Usage Notes for the XFOCUS Data Source

On mainframe platforms, the LRECL and BLKSIZE are both 16384 (16K).

The extension on UNIX and Windows is .foc.

Alphanumeric fields with the format A4096 are supported. They are not limited to A3968 as
in SUFFIX=FOC.

The CALCFILE utility automatically adjusts the calculation algorithm to the suffix type and
can be used to size the file.

The USE command supports 1022 files of mixed XFOCUS and FOC suffixes as long as each
type of data source has its own Master File with the correct suffix (FOC for the FOCUS data
sources, XFOCUS for the XFOCUS data sources).

Specify USE...AS for the data sources with suffix FOC and another AS for the data sources
with suffix XFOCUS in the same USE.

An attempt to access a SUFFIX=XFOCUS data source with an earlier release causes an
error because SUFFIX=XFOCUS is not recognized as a valid value.

JOIN commands among suffix FOC and suffix XFOCUS data sources are supported. Master
File cross-references are supported to other suffix XFOCUS data sources only.

The COMBINE command supports SUFFIX=XFOCUS data sources. You can COMBINE
SUFFIX FOC and XFOCUS in a single COMBINE.

296

6. Describing a FOCUS Data Source

Designing a FOCUS Data Source

The database management system enables you to create sophisticated hierarchical data
structures. The following sections provide information to help you design an effective and
efficient FOCUS data source and tell you how you can change the design after the data source
has been created.

Data Relationships

The primary consideration when designing a data source is the set of relationships among the
various fields. Before you create the Master File, draw a diagram of these relationships. Is a
field related to any other fields? If so, is it a one-to-one or a one-to-many relationship? If any of
the data already exists in another data source, can that data source be joined to this one?

In general, use the following guidelines:

All information that occurs once for a given record should be placed in the root segment or
a unique child segment.

Any information that can be retrieved from a joined data source should, in most cases, be
retrieved in this way, and not redundantly maintained in two different data sources.

Any information that has a many-to-one relationship with the information in a given segment
should be stored in a descendant of that segment.

Related data in child segments should be stored in the same path. Unrelated data should
be placed in different paths.

The following illustration summarizes the rules for data relationship considerations:

Describing Data With TIBCO WebFOCUS® Language

 297

Designing a FOCUS Data Source

Join Considerations

If you plan to join one segment to another, remember that both the host and cross-referenced
fields must have the same format, and the cross-referenced field must be indexed using the
INDEX attribute. In addition, for a cross-reference in a Master File, the host and cross-
referenced fields must share the same name. The name or alias of both fields must be
identical, or else the name of one field must be identical to the alias of the other.

General Efficiency Considerations

A FOCUS data source reads the root segment first, then traverses the hierarchy to satisfy your
query. The smaller you make the root segment, the more root segment instances can be read
at one time, and the faster records can be selected to process a query.

You can also improve record substitution efficiency by setting AUTOPATH. AUTOPATH is the
automation of TABLE FILE ddname.fieldname syntax, where the field name is not indexed, and
physical retrieval starts at the field name segment. AUTOPATH is described in the Developing
Reporting Applications manual.

As with most information processing issues, there is a trade-off when designing an efficient
FOCUS data source: you must balance the desire to speed up record retrieval, by reducing the
size of the root segment, against the need to speed up record selection, by placing fields used
in record selection tests as high in the data structure as possible. The segment location of
fields used in WHERE or IF tests is significant to the processing efficiency of a request. When
a field fails a record selection test, there is no additional processing to that segment instance
or its descendants. The higher the selection fields are in a data structure, the fewer the
number of segments that must be read to determine a record status.

After you have designed and created a data source, if you want to select records based on
fields that are low in the data structure, you can rotate the data structure to place those fields
temporarily higher by using an alternate view. Alternate views are discussed in Describing a
Group of Fields on page 65. For details on using alternate views in report requests, see the
Creating Reports With WebFOCUS Language manual.

Use the following guidelines to help you design an efficient data structure:

Limit the information in the root segment to what is necessary to identify the record and
what is used often in screening conditions.

Avoid unnecessary key fields. Segments with a SEGTYPE of S1 are processed much more
efficiently than those with, for example, a SEGTYPE of S9.

Index the first field of the segment (the key field) if the root segment of your data source is
SEGTYPE S1, for increased efficiency in MODIFY procedures that read transactions from
unsorted data sources (FIXFORM).

298

6. Describing a FOCUS Data Source

Use segments with a SEGTYPE of SH1 when adding and maintaining data in date
sequence. In this case, a SEGTYPE of SH1 logically positions the most recent dates at the
beginning of the data source, not at the end.

If a segment contains fields frequently used in record selection tests, keep the segment
small by limiting it to key fields, selection fields, and other fields frequently used in reports.

Index the fields on which you perform frequent searches of unique instances. When you
specify that a field be indexed, you construct and maintain a table of data values and their
corresponding physical locations in the data source. Thus, indexing a field speeds retrieval.

You can index any field you want, although it is advisable to limit the number of indexes in
a data source since each index requires additional storage space. You must weigh the
increase in speed against the increase in space.

Changing a FOCUS Data Source

After you have designed and created a FOCUS data source, you can change some of its
characteristics simply by editing the corresponding attribute in the Master File. The
documentation for each attribute specifies whether it can be edited after the data source has
been created.

Some characteristics whose attributes cannot be edited can be changed if you rebuild the data
source using the REBUILD facility, as described in Creating and Rebuilding a Data Source on
page 441. You can also use REBUILD to add new fields to a data source.

Describing a Single Segment

In a segment description, you can describe key fields, sort order, and segment relationships.
The number of segments cannot exceed 64 in a FOCUS data source, or 512 in an XFOCUS
data source. This count includes segments plus indexes plus the number of TEXT location files
(each TEXT location file can have multiple TEXT fields).

Structures created using JOIN commands can have up to 1024 segments. and FOCUS data
sources can participate in join structures that consist of up to 1024 segments.

Using an indexed view reduces the maximum number of segments plus indexes to 191 for the
structure being used. If AUTOINDEX is ON, you may be using an indexed view without
specifically asking for one.

You can code LOCATION segments in a Master File to expand the file size by pointing to
another physical file location.

You can also create a field to timestamp changes to a segment using AUTODATE.

Describing Data With TIBCO WebFOCUS® Language

 299

Describing a Single Segment

Three additional segment attributes that describe joins between FOCUS segments, CRFILE,
CRKEY, and CRSEGNAME, are described in Defining a Join in a Master File on page 349.

Describing Keys, Sort Order, and Segment Relationships: SEGTYPE

FOCUS data sources use the SEGTYPE attribute to describe segment key fields and sort order,
as well as the relationship of the segment to its parent.

The SEGTYPE attribute is also used with SUFFIX=FIX data sources to indicate a logical key
sequence for that data source. SEGTYPE is discribed in Describing a Group of Fields on page
65.

Syntax:

How to Describe a Segment

The syntax of the SEGTYPE attribute when used for a FOCUS data source is

SEGTYPE = segtype

Valid values are:

SH[n]

Indicates that the segment instances are sorted from highest to lowest value, based on
the value of the first n fields in the segment. n can be any number from 1 to 99. If you do
not specify it, it defaults to 1.

S[n]

Indicates that the segment instances are sorted from lowest value to highest, based on
the value of the first n fields in the segment. n can be any number from 1 to 255. If you do
not specify it, it defaults to 1.

S0

Indicates that the segment has no key field and is therefore not sorted. New instances are
added to the end of the segment chain. Any search starts at the current position.

S0 segments are often used to store text for applications where the text needs to be
retrieved in the order entered, and the application does not need to search for particular
instances.

300

6. Describing a FOCUS Data Source

(blank)

Indicates that the segment has no key field, and is therefore not sorted. New instances
are added to the end of the segment chain. Any search starts at the beginning of the
segment chain.

SEGTYPE = blank segments are often used in situations where there are very few segment
instances, and the information stored in the segment does not include a field that can
serve as a key.

Note that a root segment cannot be a SEGTYPE blank segment.

U

KM

KU

DKM

DKU

Indicates that the segment is unique, with a one-to-one relationship to its parent. Note that
a unique segment described with a SEGTYPE of U cannot have any children.

Indicates that this is a cross-referenced segment joined to the data source using a static
join defined in the Master File and has a one-to-many relationship to the host segment.
Joins defined in the Master File are described in Defining a Join in a Master File on page
349. The parent-child pointer is stored in the data source.

Indicates that this is a cross-referenced segment joined to the data source using a static
join defined in the Master File, and has a one-to-one relationship to the host segment (that
is, it is a unique segment). Joins defined in the Master File are described in Defining a Join
in a Master File on page 349. The parent-child pointer is stored in the data source.

Indicates that this is a cross-referenced segment joined to the data source using a
dynamic join defined in the Master File, and has a one-to-many relationship to the host
segment. Joins defined in the Master File are described in Defining a Join in a Master File
on page 349. The parent-child pointer is resolved at run time, and therefore new
instances can be added without rebuilding.

Indicates that this is a cross-referenced segment joined to the data source using a
dynamic join defined in the Master File, and has a one-to-one relationship to the host
segment (that is, it is a unique segment). Joins defined in the Master File are described in
Defining a Join in a Master File on page 349. The parent-child pointer is resolved at run
time, and therefore new instances can be added without rebuilding.

Describing Data With TIBCO WebFOCUS® Language

 301

Describing a Single Segment

KL

KLU

Indicates that this segment is described in a Master File defined join as descending from a
KM, KU, DKM, or DKU segment in a cross-referenced data source, and has a one-to-many
relationship to its parent.

Indicates that this segment is described in a Master File defined join as descending from a
KM, KU, DKM, or DKU segment in a cross-referenced data source, and has a one-to-one
relationship to its parent (that is, it is a unique segment).

Reference: Usage Notes for SEGTYPE

Note the following rules when using the SEGTYPE attribute with a FOCUS data source:

Alias. SEGTYPE does not have an alias.

Changes. You can change a SEGTYPE of S[n] or SH[n] to S0 or b, or increase the number
of key fields. To make any other change to SEGTYPE, you must use the REBUILD facility.

Describing a Key Field

Use the SEGTYPE attribute to describe which fields in a segment are key fields. The values of
these fields determine how the segment instances are sequenced. The keys must be the first
fields in a segment. You can specify up to 255 keys in a segment that is sorted from low to
high (SEGTYPE = Sn), and up to 99 keys in a segment sorted from high to low (SEGTYPE =
SHn). To maximize efficiency, it is recommended that you specify only as many keys as you
need to make each record unique. You can also choose not to have any keys (SEGTYPE = S0
and SEGTYPE = blank).

Note: Text fields cannot be used as key fields.

Describing Sort Order

For segments that have key fields, use the SEGTYPE attribute to describe the segment sort
order. You can sort a segment instances in two ways:

Low to high. By specifying a SEGTYPE of Sn (where n is the number of keys), the instances
are sorted using the concatenated values of the first n fields, beginning with the lowest
value and continuing to the highest.

High to low. By specifying a SEGTYPE of SHn (where n is the number of keys), the
instances are sorted using the concatenated values of the first n fields, beginning with the
highest value and continuing to the lowest.

302

6. Describing a FOCUS Data Source

Segments whose key is a date field often use a high-to-low sort order, since it ensures that
the segment instances with the most recent dates are the first ones encountered in a
segment chain.

Understanding Sort Order

Suppose the following fields in a segment represent a department code and the employee last
name:

06345

Jones

19887

Smith

19887

Frank

23455

Walsh

21334

Brown

If you set SEGTYPE to S1, the department code becomes the key. Note that two records have
duplicate key values in order to illustrate a point about S2 segments later in this example.
Duplicate key values are not recommended for S1 and SH1 segments. The segment instances
are sorted as follows:

06345

Jones

19887

Smith

19887

Frank

21334

Brown

23455

Walsh

If you change the field order to put the last name field before the department code and leave
SEGTYPE as S1, the last name becomes the key. The segment instances are sorted as
follows:

Brown

21334

Frank

19887

Jones

06345

Smith

19887

Walsh

23455

Alternately, if you leave the department code as the first field, but set SEGTYPE to S2, the
segments are sorted first by the department code and then by last name, as follows:

06345

Jones

19887

Frank

19887

Smith

21334

Brown

23455

Walsh

Describing Data With TIBCO WebFOCUS® Language

 303

Describing a Single Segment

Describing Segment Relationships

The SEGTYPE attribute describes the relationship of a segment to its parent segment:

Physical one-to-one relationships are usually specified by setting SEGTYPE to U. If a
segment is described in a Master File-defined join as descending from the cross-referenced
segment, then SEGTYPE is set to KLU in the join description.

Physical one-to-many relationships are specified by setting SEGTYPE to any valid value
beginning with S (such as S0, SHn, and Sn) to blank, or, if a segment is described in a
Master File-defined join as descending from the cross-referenced segment, to KL.

One-to-one joins defined in a Master File are specified by setting SEGTYPE to KU or DKU,
as described in Defining a Join in a Master File on page 349.

One-to-many joins defined in a Master File are specified by setting SEGTYPE to KM or DKM,
as described in Defining a Join in a Master File on page 349.

Storing a Segment in a Different Location: LOCATION

By default, all of the segments in a FOCUS data source are stored in one physical file. For
example, all of the EMPLOYEE data source segments are stored in the data source named
EMPLOYEE.

Use the LOCATION attribute to specify that one or more segments be stored in a physical file
separate from the main data source file. The LOCATION file is also known as a horizontal
partition. You can use a total of 64 LOCATION files per Master File (one LOCATION attribute per
segment, except for the root). This is helpful if you want to create a data source larger than the
FOCUS limit for a single data source file, or if you want to store parts of the data source in
separate locations for security or other reasons.

There are at least two cases in which to use the LOCATION attribute:

Each physical file is individually subject to a maximum file size. You can use the LOCATION
attribute to increase the size of your data source by splitting it into several physical files,
each one subject to the maximum size limit. (See Defining a Join in a Master File on page
349 to learn if it is more efficient to structure your data as several joined data sources.)

You can also store your data in separate physical files to take advantage of the fact that
only the segments needed for a report must be present. Unreferenced segments stored in
separate data sources can be kept on separate storage media to save space or implement
separate security mechanisms. In some situations, separating the segments into different
data sources allows you to use different disk drives.

304

6. Describing a FOCUS Data Source

Divided data sources require more careful file maintenance. Be especially careful about
procedures that are done separately to separate data sources, such as backups. For example,
if you do backups on Tuesday and Thursday for two related data sources, and you restore the
FOCUS structure using the Tuesday backup for one half and the Thursday backup for the other,
there is no way of detecting this discrepancy.

Syntax:

How to Store a Segment in a Different Location

LOCATION = filename [,DATASET = physical_filename]

where:

filename

Is the ddname of the file in which the segment is to be stored.

physical_filename

Is the physical name of the data source, dependent on the platform.

Example:

Specifying Location for a Segment

The following illustrates the use of the LOCATION attribute:

FILENAME = PEOPLE, SUFFIX = FOC, $
SEGNAME = SSNREC,  SEGTYPE = S1, $
 FIELD = SSN,     ALIAS = SOCSEG, USAGE = I9,  $
SEGNAME = NAMEREC, SEGTYPE = U, PARENT = SSNREC, $
 FIELD = LNAME,   ALIAS = LN,     USAGE = A25, $
SEGNAME = HISTREC, SEGTYPE = S1,PARENT = SSNREC, LOCATION = HISTFILE, $
FIELD = DATE,    ALIAS = DT,     USAGE = YMD, $
SEGNAME = JOBREC,  SEGTYPE = S1,PARENT = HISTREC,$
 FIELD = JOBCODE, ALIAS = JC,     USAGE = A3,  $
SEGNAME = SKREC,   SEGTYPE = S1,PARENT = SSNREC, $
 FIELD = SCODE,   ALIAS = SC,     USAGE = A3,  $

Describing Data With TIBCO WebFOCUS® Language

 305

Describing a Single Segment

This description groups the five segments into two physical files, as shown in the following
diagram:

Note that the segment named SKREC, which contains no LOCATION attribute, is stored in the
PEOPLE data source. If no LOCATION attribute is specified for a segment, it is placed by
default in the same file as its parent. In this example, you can assign the SKREC segment to a
different file by specifying the LOCATION attribute in its declaration. However, it is
recommended that you specify the LOCATION attribute, and not allow it to default.

Separating Large Text Fields

Text fields, by default, are stored in one physical file with non-text fields. However, as with
segments, a text field can be located in its own physical file, or any combination of text fields
can share one or several physical files. Specify that you want a text field stored in a separate
file by using the LOCATION attribute in the field definition.

For example, the text for DESCRIPTION is stored in a separate physical file named CRSEDESC:

FIELD = DESCRIPTION, ALIAS = CDESC, USAGE = TX50, LOCATION = CRSEDESC ,$

If you have more than one text field, each field can be stored in its own file, or several text
fields can be stored in one file.

306

6. Describing a FOCUS Data Source

In the following example, the text fields DESCRIPTION and TOPICS are stored in the LOCATION
file CRSEDESC. The text field PREREQUISITE is stored in another file, PREREQS.

FIELD = DESCRIPTION , ALIAS = CDESC, USAGE = TX50, LOCATION = CRSEDESC,$
FIELD = PREREQUISITE, ALIAS = PREEQ, USAGE = TX50, LOCATION = PREREQS ,$
FIELD = TOPICS,       ALIAS =      , USAGE = TX50, LOCATION = CRSEDESC,$

As with segments, you might want to use the LOCATION attribute on a text field if it is very
long. However, unlike LOCATION segments, LOCATION files for text fields must be present
during a request, whether or not the text field is referenced.

The LOCATION attribute can be used independently for segments and for text fields. You can
use it for a text field without using it for a segment. You can also use the LOCATION attribute
for both the segment and the text field in the same Master File.

Note: Field names for text fields in a FOCUS Master File are limited to 12 characters. Field
names for text fields in an XFOCUS Master File are not subject to this 12 character limitation.
However, for both types of data sources, alias names for these fields can be up to 66
characters.

Limits on the Number of Segments, LOCATION Files, Indexes, and Text Fields

The maximum number of segments in a Master File is 64. There is a limit on the number of
different location segments and text LOCATION files you can specify. This limit is based on the
number of entries allowed in the File Directory Table (FDT) for FOCUS and XFOCUS data
sources. The FDT contains the names of the segments in the data source, the names of
indexed fields, and the names of LOCATION files for text fields.

Reference: FDT Entries for a FOCUS or XFOCUS Data Source

The FDT can contain 189 entries, of which up to 64 can represent segments and LOCATION
files. Each unique LOCATION file counts as one entry in the FDT.

Determine the maximum number of LOCATION files for a data source using the following
formula:

Available FDT entries = 189 - (Number of Segments + Number of Indexes)
Location files = min (64, Available FDT entries)

where:

Location files

Is the maximum number of LOCATION segments and text LOCATION files (up to a
maximum of 64).

Describing Data With TIBCO WebFOCUS® Language

 307

Describing a Single Segment

Number of Segments

Is the number of segments in the Master File.

Number of Indexes

Is the number of indexed fields.

For example, a ten-segment data source with 2 indexed fields enables you to specify up to 52
LOCATION segments and/or LOCATION files for text fields (189 - (10 + 2)). Using the formula,
the result equals 177. However, the maximum number of text LOCATION files must always be
no more than 64.

Note: If you specify a text field with a LOCATION attribute, the main file is included in the text
location file count.

Specifying a Physical File Name for a Segment: DATASET

In addition to specifying a DATASET attribute at the file level in a FOCUS Master File, you can
specify the attribute on the segment level to specify the physical file name for a LOCATION
segment, or a cross-referenced segment with field redefinitions.

For information on specifying the DATASET attribute at the file level, see Identifying a Data
Source on page 31.

Note:

If you issue a USE command or explicit allocation for the file, a warning is issued that the
DATASET attribute will be ignored.

You cannot use both the ACCESSFILE attribute and the DATASET attribute in the same
Master File.

The segment with the DATASET attribute must be either a LOCATION segment or a cross-
referenced segment. For cross-referenced segments:

If field declarations are specified for the cross-referenced fields, the DATASET attribute is
the only method for specifying a physical file, because the cross-referenced Master File is
not read and therefore is not able to pick up its DATASET attribute if one is specified.

If field declarations are not specified for the cross-referenced fields, it is better to place the
DATASET attribute at the file level in the cross-referenced Master File. In this case,
specifying different DATASET values at the segment level in the host Master File and the
file level of the cross-referenced Master File causes a conflict, resulting in a (FOC1998)
message.

308

6. Describing a FOCUS Data Source

If DATASET is used in a Master File whose data source is managed by the FOCUS Database
Server, the DATASET attribute is ignored on the server side because the FOCUS Database
Server does not read Master Files for servicing table requests.

The DATASET attribute in the Master File has the lowest priority:

A user explicit allocation overrides DATASET attributes.

The USE command for FOCUS data sources overrides DATASET attributes and explicit
allocations.

Note: If a DATASET allocation is in effect, you must issue a CHECK FILE command in order to
override it by an explicit allocation command. The CHECK FILE command deallocates the
allocation created by DATASET.

Syntax:

How to Use the DATASET Attribute on the Segment Level

For a LOCATION segment:

SEGNAME=segname, SEGTYPE=segtype, PARENT=parent, LOCATION=filename,
                 DATASET='physical_filename [ON sinkname]',$

For a cross-referenced segment:

SEGNAME=segname, SEGTYPE=segtype, PARENT=parent, [CRSEGNAME=crsegname,]
[CRKEY=crkey,] CRFILE=crfile, DATASET='filename1 [ON sinkname]',
  FIELD=...

where:

filename

Is the logical name of the LOCATION file.

physical_filename

Is the platform-dependent physical name of the data source.

sinkname

Indicates that the data source is located on the FOCUS Database Server. This attribute is
valid for FOCUS data sources.

The syntax on z/OS is:

{DATASET|DATA}='qualifier.qualifier ...'

Describing Data With TIBCO WebFOCUS® Language

 309

Describing a Single Segment

or

{DATASET|DATA}='ddname ON sinkname'

On UNIX, the syntax is:

{DATASET|DATA}='path/filename'

On Windows, the syntax is:

{DATASET|DATA}='path\filename'

Example:

Allocating a Segment Using the DATASET Attribute

On z/OS:

FILE = ...
SEGNAME=BODY,SEGTYPE=S1,PARENT=CARREC,LOCATION=BODYSEG,
 DATASET='USER1.BODYSEG.FOCUS',
 FIELDNAME=BODYTYPE,TYPE,A12,$
 FIELDNAME=SEATS,SEAT,I3,$
 FIELDNAME=DEALER_COST,DCOST,D7,$
 FIELDNAME=RETAIL_COST,RCOST,D7,$
 FIELDNAME=SALES,UNITS,I6,$

On z/OS with SU:

FILE = ...
SEGNAME=BODY,SEGTYPE=S1,PARENT=CARREC,LOCATION=BODYSEG,
 DATASET='BODYSEG ON MYSU',
 FIELDNAME=BODYTYPE,TYPE,A12,$
 FIELDNAME=SEATS,SEAT,I3,$
 FIELDNAME=DEALER_COST,DCOST,D7,$
 FIELDNAME=RETAIL_COST,RCOST,D7,$
 FIELDNAME=SALES,UNITS,I6,$

On UNIX/USS:

FILE = ...
 SEGNAME=BDSEG,SEGTYPE=KU,CRSEGNAME=IDSEG,CRKEY=PRODMGR,
  CRFILE=PERSFILE,DATASET='/u2/prod/user1/idseg.foc',
   FIELD=NAME,ALIAS=FNAME,FORMAT=A12,INDEX=I, $

On Windows:

FILE = ...
 SEGNAME=BDSEG,SEGTYPE=KU,CRSEGNAME=IDSEG,CRKEY=PRODMGR,
  CRFILE=PERSFILE,DATASET='\u2\prod\user1\idseg.foc',
   FIELD=NAME,ALIAS=FNAME,FORMAT=A12,INDEX=I, $

310

Timestamping a FOCUS Segment: AUTODATE

6. Describing a FOCUS Data Source

Each segment of a FOCUS data source can have a timestamp field that records the date and
time of the last change to the segment. This field can have any name, but its USAGE format
must be AUTODATE. The field is populated each time its segment instance is updated. The
timestamp is stored as format HYYMDS, and can be manipulated for reporting purposes using
any of the date-time functions.

In each segment of a FOCUS data source, you can define a field with USAGE = AUTODATE. The
AUTODATE field cannot be part of a key field for the segment. Therefore, if the SEGTYPE is S2,
the AUTODATE field cannot be the first or second field defined in the segment.

The AUTODATE format specification is supported only for a real field in the Master File, not in a
DEFINE or COMPUTE command or a DEFINE in the Master File. However, you can use a DEFINE
or COMPUTE command to manipulate or reformat the value stored in the AUTODATE field.

After adding an AUTODATE field to a segment, you must REBUILD the data source. REBUILD
does not timestamp the field. It does not have a value until a segment instance is inserted or
updated.

If a user-written procedure updates the AUTODATE field, the user-specified value is overwritten
when the segment instance is written to the data source. No message is generated to inform
the user that the value was overwritten.

The AUTODATE field can be indexed. However, it is recommended that you make sure the index
is necessary, because of the overhead needed to keep the index up to date each time a
segment instance changes.

If you create a HOLD file that contains the AUTODATE field, it is propagated to the HOLD file as
a date-time field with the format HYYMDS.

Syntax:

How to Define an AUTODATE Field for a Segment

FIELDNAME = fieldname, ALIAS = alias, {USAGE|FORMAT} = AUTODATE ,$

where:

fieldname

Is any valid field name.

alias

Is any valid alias.

Describing Data With TIBCO WebFOCUS® Language

 311

Describing a Single Segment

Example:

Defining an AUTODATE Field

Create the EMPDATE data source by performing a REBUILD DUMP of the EMPLOYEE data
source and a REBUILD LOAD into the EMPDATE data source. The Master File for EMPDATE is
the same as the Master File for EMPLOYEE, with the FILENAME changed and the DATECHK
field added:

FILENAME=EMPDATE, SUFFIX=FOC
SEGNAME=EMPINFO,  SEGTYPE=S1
 FIELDNAME=EMP_ID,    ALIAS=EID,  FORMAT=A9,       $
 FIELDNAME=DATECHK,   ALIAS=DATE, USAGE=AUTODATE,  $
 FIELDNAME=LAST_NAME, ALIAS=LN,   FORMAT=A15,      $
   .
   .
   .

To add the timestamp information to EMPDATE, run the following procedure:

SET TESTDATE = 20010715
TABLE FILE EMPLOYEE
PRINT EMP_ID CURR_SAL
ON TABLE HOLD
END
MODIFY FILE EMPDATE
FIXFORM FROM HOLD
MATCH EMP_ID
ON MATCH COMPUTE CURR_SAL = CURR_SAL + 10;
ON MATCH UPDATE CURR_SAL
ON NOMATCH REJECT
DATA ON HOLD
END

Then reference the AUTODATE field in a DEFINE or COMPUTE command, or display it using a
display command. The following request computes the difference of the number of days
between the date 7/31/2001 and the DATECHK field:

DEFINE FILE EMPLOYEE
DATE_NOW/HYYMD = DT(20010731);
DIFF_DAYS/D12.2 =  HDIFF(DATE_NOW, DATECHK, 'DAY', 'D12.2');
END
TABLE FILE EMPDATE
PRINT DATECHK DIFF_DAYS
WHERE LAST_NAME EQ 'BANNING'
END

The output is:

DATECHK                       DIFF_DAYS
-------                       ---------
2001/07/15 15:10:37           16.00

312

Reference: Usage Notes for AUTODATE

PRINT * and PRINT.SEG.fld print the AUTODATE field.

6. Describing a FOCUS Data Source

The FOCUS Database Server updates the AUTODATE field per segment using the date and
time on the Server.

Maintain Data processes AUTODATE fields at COMMIT time.

DBA is permitted on the AUTODATE field. However, when unrestricted fields in the segment
are updated, the system updates the AUTODATE field.

The AUTODATE field does not support the following attributes: MISSING, ACCEPT, and
HELPMESSAGE.

GROUP Attribute

A group provides a convenient alternate name for one or more contiguous fields. The group
redefines a sequence of fields and does not require any storage of its own.

Group fields enable you to:

Join to multiple fields in a cross-referenced data source. Redefine the separate fields as a
group, index this group key, and join it to the group field.

Automatically use indexes in MODIFY when the root segment has multiple indexed fields
that comprise the key. In this case you define the group as the key. The SEGTYPE then
becomes S1, and MODIFY automatically uses the index.

Use an indexed view in a TABLE request when records are selected based on an equality
test on each component of the group. TABLE only uses one index for this type of retrieval,
so you can index the group and enhance retrieval efficiency.

Describing a Group Field With Formats

The component fields can contain alphanumeric or numeric data. However, the group field
should always have an alphanumeric format. The length of the group field must be the sum of
the actual lengths of the component fields. For example, integer fields always have an actual
length of four bytes, regardless of the USAGE format that determines how many characters
appear on a report.

Describing Data With TIBCO WebFOCUS® Language

 313

GROUP Attribute

Syntax:

How to Define a Group Field With Formats

GROUP=groupname, [ALIAS=groupalias,] USAGE=An, [FIELDTYPE=I,] $
 FIELDNAME=field1, ALIAS=alias1, USAGE=fmt1,$
 FIELDNAME=field2, ALIAS=alias2, USAGE=fmt2,$
 .
 .
 .
 FIELDNAME=fieldn, ALIAS=aliasn, USAGE=fmtn,$

where:

groupname

Is the name of the group.

groupalias

Is an optional alias name for the group.

An

Is the format for the group field. Its length is the sum of the internal lengths of the
component fields:

Fields of type I have an internal length of 4.

Fields of type F have an internal length of 4.

Fields of type P that have a USAGE format of P15 or P16 or smaller have an internal
length of 8, and fields of type P that have a USAGE format of P17 or greater have an
internal length of 16.

Fields of type D have an internal length of 8.

Fields of type A have an internal length equal to the number of characters (n) in their
USAGE formats.

Describing the group field with a format other than A does not generate an error message.
However, it is not recommended and may produce unpredictable results.

field1, ..., fieldn

Are the component fields in the group.

alias1, ..., aliasn

Are the alias names for the component fields in the group.

fmt1, ..., fmtn

Are the USAGE formats of the component fields in the group.

314

6. Describing a FOCUS Data Source

FIELDTYPE=I

Creates a separate index for the group.

Reference: Usage Notes for Group Fields in FOCUS Data Sources

When at least one component of the group has a numeric or date format, the group field
does not appear correctly. However, the value of the group field is correct, and the
individual fields appear correctly. Use this type of group in a TABLE request for indexed
retrieval on more than one component field or to join to more than one component field.

You can add or remove a non-key group field definition in a Master File at any time without
impact. If the group field is indexed and you MODIFY the data source without the group field
definition in the Master File, you must rebuild the index when you add the group field back
to the Master File.

The MISSING attribute is not supported on a group field.

To use a group field that contains a numeric component in screening criteria, separate the
component values with slashes. However, if the value of one the group components
contains a slash '/', the slash may not be used as a delimiter and no test can be issued
against this value.

Note that using slashes makes it easier to specify values when the component fields
contain trailing blanks, because you do not have to account for those blanks.

The only masks supported in screening criteria for group fields are those that accept any
combination of characters for all group components after the first component. For example,
if the FULL_NAME group consists of LAST_NAME and FIRST_NAME, the following mask is
supported:

WHERE FULL_NAME EQ '$R$$$$*'

To use a group field that contains only alphanumeric components in screening criteria,
separating the component values with a slash is optional.

A group format supports date display options.

In MODIFY, you can match on the group field when it is the first field in the segment (S1). A
MATCH on a component field in the group without matching on the group generates the
following:

(FOC439) WARNING. A MATCH CONDITION HAS BEEN ASSUMED FOR:

If the group has an index, and the group components are also indexes, you can MATCH on
the group level with no need to match on the group components.

Describing Data With TIBCO WebFOCUS® Language

 315

GROUP Attribute

Although MODIFY enables you to update group components even if they are key fields, this
is not recommended. Instead, use SCAN or FSCAN to update key fields.

If both a group and the field following it are part of a key, the number specified for the
SEGTYPE attribute must include the group field plus its component fields, plus the field
following the group. For example, if the group key has two components and is followed by
another field that is also part of the key, the SEGTYPE must be S4:

GROUP = ...,               ,$
  FIELDNAME = FIELDG1, ... ,$
  FIELDNAME = FIELDG2, ... ,$
  FIELDNAME = FIELD3, ...  ,$

Example:

Displaying an Alphanumeric Group Field

In the following group field definition, the group length is 25, the sum of the lengths of the
LAST_NAME and FIRST_NAME fields:

FILENAME=EMPLOYEE, SUFFIX=FOC
SEGNAME=EMPINFO,  SEGTYPE=S1
 FIELDNAME=EMP_ID,       ALIAS=EID,      FORMAT=A9,      $
 GROUP=FULL_NAME,                 ,      FORMAT=A25,     $
FIELDNAME=LAST_NAME,    ALIAS=LN,      FORMAT=A15,     $
  FIELDNAME=FIRST_NAME,   ALIAS=FN,      FORMAT=A10,     $

The WHERE test on the group field does not need slashes between the component values,
because both component fields are alphanumeric:

TABLE FILE EMPLOYEE
PRINT EMP_ID HIRE_DATE
BY FULL_NAME
WHERE FULL_NAME GT 'CROSSBARBARA'
END

The output is:

FULL_NAME                  EMP_ID     HIRE_DATE
---------                  ------     ---------
GREENSPAN      MARY        543729165   82/04/01
IRVING         JOAN        123764317   82/01/04
JONES          DIANE       117593129   82/05/01
MCCOY          JOHN        219984371   81/07/01
MCKNIGHT       ROGER       451123478   82/02/02
ROMANS         ANTHONY     126724188   82/07/01
SMITH          MARY        112847612   81/07/01
SMITH          RICHARD     119265415   82/01/04
STEVENS        ALFRED      071382660   80/06/02

316

6. Describing a FOCUS Data Source

Example:

Screening on a Group Field With an Integer Component

In the following group field definition, the group length is 29, the sum of the lengths of the
LAST_NAME, FIRST_NAME, and HIRE_DATE fields. Because HIRE_DATE is an integer field, its
internal length is 4:

FILENAME=EMPLOYEE, SUFFIX=FOC
SEGNAME=EMPINFO,  SEGTYPE=S1
 FIELDNAME=EMP_ID,       ALIAS=EID,      FORMAT=A9,    $
 GROUP=FULL_NAME,                 ,      FORMAT=A29,   $
FIELDNAME=LAST_NAME,    ALIAS=LN,      FORMAT=A15,   $
  FIELDNAME=FIRST_NAME,   ALIAS=FN,      FORMAT=A10,   $
  FIELDNAME=HIRE_DATE,    ALIAS=HDT,     FORMAT=I6YMD, $

In the following request, the component field values must be separated by slashes in the
WHERE test. The request does not display the group field, because the integer component
would not appear correctly:

TABLE FILE EMPGROUP
PRINT EMP_ID LAST_NAME FIRST_NAME HIRE_DATE
BY FULL_NAME NOPRINT
WHERE FULL_NAME GT 'CROSS/BARBARA/811102'
END

The output is:

EMP_ID     LAST_NAME        FIRST_NAME  HIRE_DATE
------     ---------        ----------  ---------
543729165  GREENSPAN        MARY         82/04/01
123764317  IRVING           JOAN         82/01/04
117593129  JONES            DIANE        82/05/01
219984371  MCCOY            JOHN         81/07/01
451123478  MCKNIGHT         ROGER        82/02/02
126724188  ROMANS           ANTHONY      82/07/01
112847612  SMITH            MARY         81/07/01
119265415  SMITH            RICHARD      82/01/04
071382660  STEVENS          ALFRED       80/06/02

Describing a Group Field as a Set of Elements

A GROUP declaration in a Master File describes several fields as a single entity. One use of a
group is to describe Group keys in a VSAM data source. Sometimes referring to several fields
by one group name facilitates ease of reporting.

Traditionally, when describing a GROUP field, you had to take account of the fact that while the
USAGE and ACTUAL format for the GROUP field are both alphanumeric, the length portion of
the USAGE format for the group had to be calculated as the sum of the component lengths,
where each integer or single precision field counted as 4 bytes, each double precision field as
8 bytes, and each packed field counted as either 8 or 16 bytes depending on its size.

Describing Data With TIBCO WebFOCUS® Language

 317

GROUP Attribute

To avoid the need to calculate these lengths, you can use the GROUP ELEMENTS option, which
describes a group as a set of elements without USAGE and ACTUAL formats.

Syntax:

How to Describe a GROUP Field as a Set of Elements

GROUP=group1, ALIAS=g1alias,ELEMENTS=n1,$
   FIELDNAME=field11, ALIAS=alias11, USAGE=ufmt11, ACTUAL=afmt11, $
   .
   .
   .
   FIELDNAME=field1h, ALIAS=alias1h, USAGE=ufmt1h, ACTUAL=afmt1h, $
GROUP=group2,ALIAS=g2alias,ELEMENTS=n2,$
   FIELDNAME=field21, ALIAS=alias21, USAGE=ufmt21, ACTUAL=afmt21, $
   .
   .
   .
   FIELDNAME=field2k, ALIAS=alias2k, USAGE=ufmt2k, ACTUAL=afmt2k, $

where:

group1, group2

Are valid names assigned to a group of fields. The rules for acceptable group names are
the same as the rules for acceptable field names.

n1, n2

Are the number of elements (fields and/or groups) that compose the group. If a group is
defined within another group, the subgroup (with all of its elements) counts as one
element of the parent group.

field11, field2k

Are valid field names.

alias11, alias2k

Are valid alias names.

ufmt11, ufmt2k

Are USAGE formats for each field.

afmt11, afmt2k

Are ACTUAL formats for each field.

318

Reference: Usage Notes for Group Elements

6. Describing a FOCUS Data Source

To use the ELEMENTS attribute, the GROUP field declaration should specify only a group
name and number of elements.

If a group declaration specifies USAGE and ACTUAL without the ELEMENTS attribute, the
USAGE and ACTUAL are accepted as specified, even if incorrect.

If a group declaration specifies USAGE and ACTUAL with the ELEMENTS attribute, the
ELEMENTS attribute takes precedence.

Each subgroup counts as one element. Its individual fields and subgroups do not count in
the number of elements of the parent group.

Example:

Declaring a GROUP With ELEMENTS

In the following Master File, GRP2 consists of two elements, fields FIELDA and FIELDB. GRP1
consists of two elements, GRP2 and field FIELDC. Field FIELDD is not part of a group:

FILENAME=XYZ     , SUFFIX=FIX     , $
  SEGMENT=XYZ, SEGTYPE=S2, $
GROUP=GRP1,ALIAS=CCR,ELEMENTS=2,$
   GROUP=GRP2,ALIAS=CC,ELEMENTS=2,$
    FIELDNAME=FIELDA, ALIAS=E01, USAGE=A10, ACTUAL=A10, $
    FIELDNAME=FIELDB, ALIAS=E02, USAGE=A16, ACTUAL=A16, $
    FIELDNAME=FIELDC, ALIAS=E03, USAGE=P27, ACTUAL=A07, $
    FIELDNAME=FIELDD, ALIAS=E04, USAGE=D7, ACTUAL=A07, $

The following chart shows the offsets and formats of these fields.

Field Number

Field Name

Offset

USAGE

ACTUAL

1

2

3

4

5

6

GRP1

GRP2

FIELDA

FIELDB

FIELDC

FIELDD

0

0

0

10

26

42

A42 - Supports 16
characters for FIELDC (P27)

A26

A10

A16

P27

D7

A33

A26

A10

A16

A7

A7

Describing Data With TIBCO WebFOCUS® Language

 319

ACCEPT Attribute

ACCEPT Attribute

ACCEPT is an optional attribute that you can use to validate data that is entered into a field
using a MODIFY procedure. For a description of its use with all types of data sources, see
Describing an Individual Field on page 103. However, ACCEPT has a special option, FIND, that
you can use only with FOCUS data sources. FIND enables you to verify incoming data against
values stored in another field.

Syntax:

How to Specify Data Validation

ACCEPT = list
ACCEPT = range
ACCEPT = FIND (sourcefield [AS targetfield] IN file)

where:

list

Is a list of acceptable values. See Describing an Individual Field on page 103.

range

Gives the range of acceptable values. See Describing an Individual Field on page 103.

FIND

Verifies the incoming data against the values in an index in a FOCUS data source.

sourcefield

Is the name of the field to which the ACCEPT attribute is being applied, or any other field in
the same segment or path to the segment. This must be the actual field name, not the
alias or a truncation of the name.

targetfield

Is the name of the field that contains the acceptable data values. This field must be
indexed.

file

Is the name of the file describing the data source that contains the indexed field of
acceptable values.

320

INDEX Attribute

6. Describing a FOCUS Data Source

Index the values of a field by including the INDEX attribute, or its alias of FIELDTYPE, in the
field declaration. An index is an internally stored and maintained table of data values and
locations that speeds retrieval. You must create an index to:

Join two segments based on equality. The cross-referenced field in a joined FOCUS data
source must be indexed, as described in Describing a Single Segment on page 299 (for
joins defined in a Master File), and the Creating Reports With WebFOCUS Language manual
(for joins defined using the JOIN command).

Create an alternate view and make it faster, as described in Describing a Group of Fields on
page 65.

Use a LOOKUP function in MODIFY.

Use a FIND function in MODIFY.

Speed segment selection and retrieval based on the values of a given field, as described
for reporting in the Creating Reports With WebFOCUS Language manual.

Syntax:

How to Specify Field Indexing

The syntax of the INDEX attribute in the Master File is:

INDEX = I or FIELDTYPE = I

Text fields cannot be indexed. The maximum field name length for indexed fields in a FOCUS
data source is 12 characters. The maximum field name length for indexed fields in an XFOCUS
data source is 66 characters.

Example:

Specifying an Index for the JOBCODE Field

FIELDNAME = JOBCODE, ALIAS = CJC, FORMAT = A3, INDEX = I, $

Describing Data With TIBCO WebFOCUS® Language

 321

INDEX Attribute

Joins and the INDEX Attribute

In order to cross reference a segment using a static cross reference, a dynamic cross
reference, or an equijoin, at least one field in the segment must be indexed. This field, called
the cross-referenced field, shares values with a field in the host data source. Only the cross-
referenced segment requires an indexed field, shown as follows:

Other data sources locate and use segments through these indexes. Any number of fields may
be indexed on a segment, although it is advisable to limit the number of fields you index in a
data source.

322

6. Describing a FOCUS Data Source

The value for the field named JOBCODE in the EMPLOYEE data source is matched to the field
named JOBCODE in the JOBFILE data source by using the index for the JOBCODE field in the
JOBFILE data source, as follows:

Indexes are stored and maintained as part of the FOCUS data source. The presence of the
index is crucial to the operation of the cross-referencing facilities. Any number of external
sources may locate and thereby share a segment because of it. New data sources which have
data items in common with indexed fields in existing data sources can be added at any time.

Reference: Usage Notes for INDEX

Note the following rules when using the INDEX attribute:

Alias. INDEX has an alias of FIELDTYPE.

Changes. If the INDEX attribute is removed from a field, or assigned the equivalent value of
blank, the index is longer maintained. If you no longer need the index, use the REORG
option of the REBUILD facility to recover space occupied by the index after you remove the
INDEX attribute. REBUILD is described in Creating and Rebuilding a Data Source on page
441.

To turn off indexing temporarily (for example, to load a large amount of data into the data
source quickly), you can remove the INDEX attribute before loading the data, restore the
attribute, and then use the REBUILD command with the INDEX option to create the index.
This is known as post-indexing the data source.

Describing Data With TIBCO WebFOCUS® Language

 323

Describing a Partitioned FOCUS Data Source

You can index the field after the data source has already been created and populated with
records, by using the REBUILD facility with the INDEX option.

Maximum number. The total of indexes, text fields, and segments cannot exceed 189 (of
which a maximum of 64 can be segments and text LOCATION files).

FORMAT and MISSING: Internal Storage Requirements

Some application developers find it useful to know how different data types and values are
represented and stored internally:

Integer fields are stored as full-word (four byte) binary integers.

Floating-point double-precision fields are stored as double-precision (eight byte) floating-
point numbers.

Floating-point single-precision fields are stored as single-precision (four byte) floating-point
numbers.

Packed-decimal fields are stored as 8 or 16 bytes and represent decimal numbers with up
to 31 digits.

Date fields are stored as full-word (four byte) binary integers representing the difference
between the specified date and the date format base date of December 31, 1900 (or JAN
1901, depending on the date format).

Date-time fields are stored in 8 or 10 bytes depending on whether the time component
specifies microseconds.

Alphanumeric fields are stored as characters in the specified number of bytes.

Variable length alphanumeric fields are stored as characters in the specified number of
bytes plus two additional bytes to specify the length of the character string stored in the
field.

Missing values are represented internally by a flag.

Describing a Partitioned FOCUS Data Source

FOCUS data sources can consist of up to 1022 physical files. The horizontal partition is a slice
of one or more segments of the entire data source structure. Note, however, that the number
of physical files associated with one FOCUS data source is the sum of its partitions and
LOCATION files. This sum must be less than or equal to 1022. FOCUS data sources can grow
in size over time, and can be repartitioned based on the requirements of the application.

324

Intelligent Partitioning

6. Describing a FOCUS Data Source

The FOCUS data source supports intelligent partitioning, which means that each vertical
partition contains the complete data source structure for specific data values or ranges of
values. Intelligent partitioning not only lets you separate the data into up to 1022 physical
files, it allows you to create an Access File in which you describe the actual data values in
each partition using WHERE criteria. When processing a report request, the selection criteria in
the request are compared to the WHERE criteria in the Access File to determine which
partitions are required for retrieval.

To select applications that can benefit most from partitioning, look for ones that employ USE
commands to concatenate data sources, or for data that lends itself to separation based on
data values or ranges of values, such as data stored by month or department. Intelligent
partitioning functions like an intelligent USE command. It looks at the Access File when
processing a report request to determine which partitions to read, whereas the USE command
reads all of the files on the list. This intelligence decreases I/O and improves performance.

To take advantage of the partitioning feature, you must:

Edit the Master File and add the ACCESSFILE attribute.

Create the Access File using a text editor.

Concatenation of multiple partitions is supported for reporting only. You must load or rebuild
each physical partition separately. You can either create a separate Master File for each
partition to reference in the load procedure, or you can use the single Master File created for
reporting against the partitioned data source, if you:

Issue an explicit allocation command to link the Master File to each partition in turn.

Run the load procedure for each partition in turn.

Note: Report requests automatically read all required partitions without user intervention.

Specifying an Access File in a FOCUS Master File

To take advantage of the partitioning feature, you must edit the Master File and add the
ACCESSFILE attribute.

The name of the Access File must be the same as the Master File name, and it must be
specified with the ACCESS = attribute in the Master File.

Describing Data With TIBCO WebFOCUS® Language

 325

Describing a Partitioned FOCUS Data Source

Syntax:

How to Specify an Access File for a FOCUS Data Source

FILENAME=filename, SUFFIX=FOC, ACCESS[FILE]=accessfile,
.
.
.

where:

filename

Is the file name of the partitioned data source.

accessfile

Is the name of the Access File. This must be the same as the Master File name.

Example: Master File for the VIDEOTR2 Partitioned Data Source

FILENAME=VIDEOTR2,  SUFFIX=FOC,
 ACCESS=VIDEOTR2,  $
  SEGNAME=CUST,       SEGTYPE=S1
   FIELDNAME=CUSTID,     ALIAS=CIN,         FORMAT=A4,          $
   FIELDNAME=LASTNAME,   ALIAS=LN,          FORMAT=A15,         $
   FIELDNAME=FIRSTNAME,  ALIAS=FN,          FORMAT=A10,         $
   FIELDNAME=EXPDATE,    ALIAS=EXDAT,       FORMAT=YMD,         $
   FIELDNAME=PHONE,      ALIAS=TEL,         FORMAT=A10,         $
   FIELDNAME=STREET,     ALIAS=STR,         FORMAT=A20,         $
   FIELDNAME=CITY,       ALIAS=CITY,        FORMAT=A20,         $
   FIELDNAME=STATE,      ALIAS=PROV,        FORMAT=A4,          $
   FIELDNAME=ZIP,        ALIAS=POSTAL_CODE, FORMAT=A9,          $
  SEGNAME=TRANSDAT, SEGTYPE=SH1,  PARENT=CUST
   FIELDNAME=TRANSDATE,  ALIAS=OUTDATE,     FORMAT=HYYMDI,      $
  SEGNAME=SALES,    SEGTYPE=S2,   PARENT=TRANSDAT
   FIELDNAME=TRANSCODE,  ALIAS=TCOD,        FORMAT=I3,          $
   FIELDNAME=QUANTITY,   ALIAS=NO,          FORMAT=I3S,         $
   FIELDNAME=TRANSTOT,   ALIAS=TTOT,        FORMAT=F7.2S,       $
  SEGNAME=RENTALS,  SEGTYPE=S2,   PARENT=TRANSDAT
   FIELDNAME=MOVIECODE,  ALIAS=MCOD,        FORMAT=A6, INDEX=I, $
   FIELDNAME=COPY,       ALIAS=COPY,        FORMAT=I2,          $
   FIELDNAME=RETURNDATE, ALIAS=INDATE,      FORMAT=YMD,         $
   FIELDNAME=FEE,        ALIAS=FEE,         FORMAT=F5.2S,       $
 DEFINE DATE/I4 = HPART(TRANSDATE, 'YEAR', 'I4');

326

Reference: Using a Partitioned Data Source

The following illustrates how to use an intelligently partitioned data source. The Access File for
the VIDEOTR2 data source describes three partitions based on DATE:

6. Describing a FOCUS Data Source

TABLE FILE VIDEOTR2
PRINT LASTNAME FIRSTNAME DATE
WHERE DATE FROM 1996 TO 1997
END

The output is:

LASTNAME         FIRSTNAME   DATE
--------         ---------   ----
HANDLER          EVAN        1996
JOSEPH           JAMES       1997
HARRIS           JESSICA     1997
HARRIS           JESSICA     1996
MCMAHON          JOHN        1996
WU               MARTHA      1997
CHANG            ROBERT      1996

There is nothing in the request or output that signifies that a partitioned data source is used.
However, only the second partition is retrieved, reducing I/O and enhancing performance.

Describing Data With TIBCO WebFOCUS® Language

 327

Describing a Partitioned FOCUS Data Source

Reference: Usage Notes for Partitioned FOCUS Data Sources

Concatenation of multiple partitions in one request is only valid for reporting. To MODIFY or
REBUILD a partitioned data source, you must explicitly allocate and MODIFY, Maintain, or
REBUILD one partition at a time.

The order of precedence for allocating data sources is:

A USE command that is in effect has the highest precedence. It overrides an Access
File or an explicit allocation for a data source.

An Access File overrides an explicit allocation for a data source.

A DATASET attribute cannot be used in the same Master File as an ACCESSFILE attribute.

Commands that alter a data source (for example, MODIFY, Maintain, and REBUILD) do not
use the Access File. If you use a Master File that contains an ACCESSFILE attribute with a
command that alters the data source, the following warning message appears:

(FOC1968)ACCESS FILE INFORMATION IN MASTER %1 WILL NOT BE CONSIDERED

This message may appear in the View Source, not on the HTML page.

The CREATE FILE command automatically issues a dynamic allocation for the data source it
creates, and this allocation takes precedence over the ACCESSFILE attribute. In order to
use the ACCESSFILE attribute after issuing a CREATE FILE command, you must first free
this automatic allocation.

When the type of command changes from reading a data source to writing to a data source,
or vice versa (for example, Maintain to TABLE), the Master File is reparsed.

When a cross-referenced Master File includes an ACCESSFILE attribute, the host Master
File cannot rename the cross-referenced fields.

FOCUS Access File Attributes

Every request supplies the name of a Master File. The Master File is read and the declarations
in it are used to access the data source. If the Master File contains an ACCESS= attribute, the
Access File is read and used to locate the correct data sources. The Access File must have the
same name as the Master File. If there is no Access File with the same name as the ACCESS=
attribute in the Master File, the request is processed with the Master File alone.

328

Reference: Access File Attributes for a FOCUS Access File

6. Describing a FOCUS Data Source

Each FOCUS Access File describes the files and MDIs for one Master File, and that Master File
must have the same file name as the Access File.

All attribute and value pairs are separated by an equal sign (=), and each pair in a declaration
is delimited with a comma (,). Each declaration is terminated with the comma dollar sign (,$).

1. Each Access File starts with a declaration that names its corresponding Master File.

2. Next comes the DATA declaration that describes the location of the physical file. If the file

is partitioned, it has multiple DATA declarations.

If the file is intelligently partitioned so that an expression describes which data values
reside in each partition, the DATA declaration has a WHERE phrase that specifies this
expression.

3. If the data source has LOCATION segments the LOCATION declaration names a location
segment. Its corresponding DATA declaration points to the physical LOCATION file.

4. If the data source has an MDI, the Access File has an MDI declaration that names the MDI
and its target segment, followed by declarations that name the dimensions of the MDI,
followed by the MDIDATA declaration that points to the physical MDI file. If the MDI is
partitioned, there are multiple MDIDATA declarations for the MDI.

Syntax:

How to Create a FOCUS Access File

Master File declaration:

MASTER=mastername,$

where:

mastername

Indicates the name of the Master File with which this Access File is associated. It is the
same value included in the Master File ACCESS=filename attribute, used to indicate both
the existence of the Access File and its name.

Describing Data With TIBCO WebFOCUS® Language

 329

Describing a Partitioned FOCUS Data Source

DATA=file_specification,
   [WHERE= expression; ,]$
[DATA=file_specification,
   [WHERE= expression; ,]$ ...]

where:

file_specification

Points to the file location. This is a complete file specification. There are can be up to
1022 DATA declarations (partitions) in a single Access File. The WHERE clause is the
basis of the Intelligent Partitioning feature. The expression is terminated with the
semi-colon and the entire declaration with the comma/dollar sign. WHERE expressions
of the following type are supported:

WHERE= field  operator value1 [ OR  value2...]; ,$

WHERE= field FROM value1 TO value2 [AND FROM value3 TO value4];,$

Expressions can be combined with the AND operator.

Location File declarations:

LOCATION=location_segment_name,
  DATA=location_segment_file_specification,$

where:

location_segment_name

Is the name of the segment stored in the location file.

location_segment_file_specification

Is the full file specification for the physical file the segment is located in.

MDI declarations:

MDI=mdiname, TARGET_OF = segname,$
   DIM = [filename.]fieldname [, MAXVALUES = n] [, WITHIN = dimname1],$
   [DIM = [filename.]fieldname [, MAXVALUES = n] [, WITHIN = dimname1] ,
$ ...]
 MDIDATA=mdi_file_specification,$
 [MDIDATA=mdi_file_specification,$ ...]

where:

mdiname

Is the name of the MDI.

330

6. Describing a FOCUS Data Source

segname

Is the name of the target segment.

filename

Is the name of the file where an MDI dimension resides.

fieldname

Is the name of a field that is a dimension of the MDI.

n

Is the number of distinct values in the dimension. When the MDI is created, the actual
dimension value will be converted to an integer of length 1, 2, or 4 bytes, and this number
will be stored in the index leaf.

mdi_file_specification

Is the fully-qualified specification of the physical MDI file. If the MDI is partitioned, it is the
specification for one partition of the MDI. An MDI can have up to 250 MDIDATA
declarations (partitions). An Access File can have an unlimited number of MDIs.

dimname

Defines a hierarchy of dimensions. This dimension is defined within the dimname
dimension. For example, CITY WITHIN STATE.

Describing Data With TIBCO WebFOCUS® Language

 331

Describing a Partitioned FOCUS Data Source

Example:

Access File for the VIDEOTR2 Data Source

VIDEOTR2 is an intelligently partitioned FOCUS data source. The Master File has an
ACCESS=VIDEOTR2 attribute:

FILENAME=VIDEOTR2,  SUFFIX=FOC,    ACCESS=VIDEOTR2
SEGNAME=CUST,       SEGTYPE=S1
 FIELDNAME=CUSTID,       ALIAS=CIN,          FORMAT=A4,       $
 FIELDNAME=LASTNAME,     ALIAS=LN,           FORMAT=A15,      $
 FIELDNAME=FIRSTNAME,    ALIAS=FN,           FORMAT=A10,      $
 FIELDNAME=EXPDATE,      ALIAS=EXDAT,        FORMAT=YMD,      $
 FIELDNAME=PHONE,        ALIAS=TEL,          FORMAT=A10,      $
 FIELDNAME=STREET,       ALIAS=STR,          FORMAT=A20,      $
 FIELDNAME=CITY,         ALIAS=CITY,         FORMAT=A20,      $
 FIELDNAME=STATE,        ALIAS=PROV,         FORMAT=A4,       $
 FIELDNAME=ZIP,          ALIAS=POSTAL_CODE,  FORMAT=A9,       $
 FIELDNAME=EMAIL,        ALIAS=EMAIL,        FORMAT=A18,      $
SEGNAME=TRANSDAT, SEGTYPE=SH1,  PARENT=CUST
 FIELDNAME=TRANSDATE,    ALIAS=OUTDATE,   FORMAT=HYYMDI,
   MISSING=ON, $
SEGNAME=SALES,    SEGTYPE=S2,   PARENT=TRANSDAT
 FIELDNAME=TRANSCODE,    ALIAS=TCOD,    FORMAT=I3,            $
 FIELDNAME=QUANTITY,     ALIAS=NO,      FORMAT=I3S,           $
 FIELDNAME=TRANSTOT,     ALIAS=TTOT,    FORMAT=F7.2S,         $
SEGNAME=RENTALS,  SEGTYPE=S2,   PARENT=TRANSDAT
 FIELDNAME=MOVIECODE,    ALIAS=MCOD,      FORMAT=A6, INDEX=I, $
 FIELDNAME=COPY,         ALIAS=COPY,      FORMAT=I2,          $
 FIELDNAME=RETURNDATE,   ALIAS=INDATE,    FORMAT=YMD,         $
 FIELDNAME=FEE,          ALIAS=FEE,       FORMAT=F5.2S,       $
 DEFINE DATE/I4 = HPART(TRANSDATE, 'YEAR', 'I4');

The following shows the Access File, named VIDEOTR2, on z/OS:

MASTER=VIDEOTR2 ,$
  DATA=USER1.VIDPART1.FOCUS,
    WHERE=DATE EQ 1991;,$

  DATA=USER1.VIDPART2.FOCUS,
    WHERE=DATE FROM 1996 TO 1998; ,$

  DATA=USER1.VIDPART3.FOCUS,
   WHERE=DATE FROM 1999 TO 2000;,$

The following shows the Access File, named VIDEOTR2, on UNIX:

MASTER=VIDEOTR2 ,$
  DATA=/user1/vidpart1.foc,
    WHERE=DATE EQ 1991;,$

  DATA=/user1/vidpart2.foc,
    WHERE=DATE FROM 1996 TO 1998; ,$

  DATA=/user1/vidpart3.foc,
   WHERE=DATE FROM 1999 TO 2000;,$

332





The following shows the Access File, named VIDEOTR2, on Windows:

6. Describing a FOCUS Data Source

MASTER=VIDEOTR2 ,$
  DATA=c:\user1\vidpart1.foc,
    WHERE=DATE EQ 1991;,$

  DATA=c:\user1\vidpart2.foc,
    WHERE=DATE FROM 1996 TO 1998; ,$

  DATA=c:\user1\vidpart3.foc,
   WHERE=DATE FROM 1999 TO 2000;,$

Multi-Dimensional Index (MDI)

A multi-dimensional index (MDI) enables you to efficiently and flexibly retrieve information you
need for business analysis. It looks at data differently from transaction processing systems in
which the goal is to retrieve records based on a key. (WebFOCUS uses a B-tree index for this
type of retrieval). The MDI is for retrieval only. It is not used for MODIFY or Maintain Data
requests.

Business analysts may be interested in specific facts (data values, also called measures)
about multiple categories of data in the data source. Categories of data, such as region or
department, are referred to as dimensions. A multi-dimensional index uses dimensions and all
of their hierarchical relationships to point to specific facts.

The MDI is a multi-field index that contains at least two dimensions. This index behaves like a
virtual cube of values that intersect at measures of interest. The more dimensions used in a
query, the better the retrieval performance.

For example, suppose that the CENTORD data source has an MDI with dimensions STATE,
REGION, and PRODCAT. The MDI is used to retrieve the facts (LINEPRICE and QUANTITY data)
that lie at the intersection of the dimension values specified in the following request:

TABLE FILE CENTORD
SUM QUANTITY LINEPRICE
WHERE REGION EQ 'EAST'
WHERE STATE EQ 'DC'
WHERE PRODCAT EQ 'Cameras'
END

The MDI also provides the following other retrieval enhancing features: MDI JOIN, Dimensional
JOIN, MDI WITHIN, MAXVALUES, MDI Encoding, and AUTOINDEX for MDI.

Specifying an MDI in the Access File

All MDI attributes are specified in the Access File for the data source. The only attribute
needed in the Master File is the ACCESSFILE attribute to point to the Access File containing
the MDI specifications.

Describing Data With TIBCO WebFOCUS® Language

 333



Multi-Dimensional Index (MDI)

An MDI can be partitioned into multiple MDI files. However, even if the data source on which
the MDI is built is partitioned, each MDI partition spans all data source partitions.

Syntax:

How to Specify an MDI in an Access File

MASTER = masterfile,$
    DATA = database_filename1,$
     .
     .
     .
    DATA = database_filenamen ,$
    MDI = mdiname,
        TARGET_OF = segname ,$
        DIM = field1 [MAXVALUES = n1] [WITHIN = dimname1],$
          .
          .
          .
        DIM = fieldn [MAXVALUES = nn] [WITHIN = dimnamen],$

        MDIDATA = mdifile1 ,$
          .
          .
          .
        MDIDATA = mdifilen,$

where:

masterfile

Is the Master File name.

database_filename1, ..., database_filenamen

Are fully qualified physical file names in the syntax native to your operating environment. If
the name contains blanks or special characters, it must be enclosed in single quotation
marks. Multiple DATA declarations describe concatenated partitions.

mdiname

Is the logical name of the MDI, up to 8 characters.

segname

Is the segment that contains the facts pointed to by the MDI. If the target data is
distributed among several segments, the target should be the top segment that contains
MDI data in order to avoid the multiplicative effect.

field1, ..., fieldn

Are the fields to use as dimensions. At least two dimensions are required for an MDI.

334


6. Describing a FOCUS Data Source

mdifile1, ..., mdifilen

Are fully qualified physical file names for the MDI in the syntax native to your operating
environment. If the name contains blanks or special characters, it must be enclosed in
single quotation marks. Multiple MDIDATA declarations describe concatenated partitions.

n1, ..., nn

Is the number of distinct values the field can have. This number must be a positive
integer.

dimname1, ..., dimnamen

Defines a hierarchy of dimensions. This dimension is defined within the dimname
dimension. For example, CITY WITHIN STATE.

Example:

Defining an MDI on UNIX

This example shows an MDI with two partitions:

MASTERNAME = CAR,$
 DATA = /user1/car.foc,$
 MDI = carmdi,
   TARGET_OF = ORIGIN,$
   DIM = CAR,$
   DIM = COUNTRY,$
   DIM = MODEL,$
   MDIDATA = /user1/car1.mdi,$
   MDIDATA = /user1/car2.mdi,$

Example:

Defining an MDI on Windows

This example shows an MDI with two partitions:

MASTERNAME = CAR,$
 DATA = c:\user1\car.foc,$
 MDI = carmdi,
   TARGET_OF = ORIGIN,$
   DIM = CAR,$
   DIM = COUNTRY,$
   DIM = MODEL,$
   MDIDATA = c:\user1\car1.mdi,$
   MDIDATA = c:\user1\car2.mdi,$

Describing Data With TIBCO WebFOCUS® Language

 335

Multi-Dimensional Index (MDI)

Example:

Defining an MDI on z/OS

This example shows an MDI with two partitions:

MASTER = CAR,$
 DATA = USER1.CAR.FOCUS,$
 MDI = CARMDI,
   TARGET_OF = ORIGIN,$
   DIM = CAR,$
   DIM = COUNTRY,$
   DIM = MODEL,$
   MDIDATA = USER1.CAR1.MDI,$
   MDIDATA = USER1.CAR2.MDI,$

Creating a Multi-Dimensional Index

Each MDI is specified in an Access File for the data source. WebFOCUS uses the Access File in
its retrieval analysis for each TABLE request.

You then use the REBUILD MDINDEX command to build the MDI. The MDI has the following
DCB attributes: RECFM=F,LRECL=4096,BLKSIZE=4096.

A multi-dimensional index gives complex queries high-speed access to combinations of
dimensions across data sources. If you know what information users want to retrieve and why,
you can make intelligent choices about index dimensions.

An Access File can define more than one MDI. If the Access File defines multiple MDIs, the
AUTOINDEX facility chooses the best index to use for each query.

The first step in designing an MDI is to find out what kind of information users need from the
data source. You can get advice about your MDIs directly from WebFOCUS.

Choosing Dimensions for Your Index

The choice of index dimensions depends on knowing the data and on analyzing what is needed
from it. Examine the record selection (IF and WHERE) tests in your queries to see how many
index dimensions each application actually uses to select records. If different applications
need different subsets of dimensions, consider separate MDIs for the separate subsets.
Although WebFOCUS can produce high-speed reporting performance with indexes of up to 30
dimensions, smaller indexes usually generate less retrieval overhead. You can create an
unlimited number of MDIs.

The following are good candidates for dimensions in an MDI:

Fields used frequently in record selection tests. Multiple fields used in selection tests
within one query belong in the same MDI.

Fields used as the basis for vertical partitioning, such as date or region.

336

6. Describing a FOCUS Data Source

Derived dimensions (DEFINE fields) that define a new category based on an existing
category. For example, if your data source contains the field STATE but you need region for
your analysis, you can use the STATE field to derive the REGION dimension.

Fields with many unique values. Fields which have few possible values are not normally
good candidates. However, you may want to index such a field if the data source contains
very few instances of one of the values, and you want to find those few instances.

Packed decimal fields may be used as MDI dimensions on all platforms.

An MDI can include a field that has a B-tree index as a dimension.

MDI dimensions support missing values.

Including a field that is updated frequently (such as an AUTODATE field) in the MDI, requires
frequent rebuilding of the MDI in order to keep it current. WebFOCUS can advise you on
selecting MDI dimensions.

DEFINE fields described in the Master File can be used as dimensions. Dynamic DEFINE fields
cannot be dimensions.

An MDI is for retrieval only. FIND and LOOKUP are not supported on an MDI.

Reference: Guidelines for a Multi-Dimensional Index

The following guidelines apply to each MDI:

The maximum size of an MDI is 200 GB.

The maximum size of each index partition is 2 GB.

Describing Data With TIBCO WebFOCUS® Language

 337

Multi-Dimensional Index (MDI)

The total size of all dimensions in an MDI cannot exceed 256 bytes. However, if you
include the MAXVALUES attribute in the Access File declaration for a dimension,
WebFOCUS uses a small number of bytes to store the values of that dimension:

MAXVALUES

1 through 253

254 through 65,533

Greater than 65,533

Number of Bytes Required

1

2

4

To allow for expansion, if the maximum number of values is close to a limit, make
MAXVALUES big enough to use a larger number of bytes. For example, if you have 250
values, specify 254 for MAXVALUES, and reserve 2 bytes for each dimension value.

Building and Maintaining a Multi-Dimensional Index

The REBUILD command is used to create or maintain a multi-dimensional index. This command
can be issued in a FOCEXEC.

The best MDI is built by specifying the dimensions in order of best cardinality (most distinct
values).

To issue the REBUILD command in a FOCEXEC, you place the REBUILD command and the user-
supplied information needed for REBUILD processing in the FOCEXEC.

If the MDI file might be larger than two gigabytes or if you plan to add more data partitions to
it, the MDI index file must be partitioned from the initial REBUILD phase. After the index has
been created, you can use it in a retrieval request. You cannot use an MDI for modifying the
data source. If you update the data source without rebuilding the MDI and then attempt to
retrieve data with it, WebFOCUS displays a message indicating that the MDI is out of date. You
must then rebuild the MDI.

338

Example:

Creating a Multi-Dimensional Index

The following FOCEXEC creates the CARMDI MDI and contains each user-supplied value
needed for REBUILD processing on a separate line of the FOCEXEC, entered in uppercase:

6. Describing a FOCUS Data Source

REBUILD
MDINDEX
NEW
CAR
CARMDI
NO

Using a Multi-Dimensional Index in a Query

WebFOCUS allows you to use an MDI in a TABLE or SQL query. The performance is best when
all of the dimensions in the MDI are used in selection criteria for the query.

There are two ways to use an MDI with a TABLE query:

Lazy OR parameters. For example:

IF (or WHERE) field EQ value_1 OR value_2 OR value_3. . .

Mask or wildcard characters. For example, the following would show all values for a field
that begin with A:

IF (or WHERE) field EQ A*

where field is a dimension in an MDI.

You can use an MDI with an SQL query by issuing an SQL SELECT statement with a WHERE
test using a field of an MDI. For example,

SELECT field_1, field_2 FROM table WHERE field_3 = value;

where field_3 is a dimension in an MDI.

Note: AUTOINDEX must be turned on for this feature to be operational.

Querying a Multi-Dimensional Index

WebFOCUS provides a query command that generates statistics and descriptions for your
MDIs. The command ? MDI allows you to display information about MDIs for a given FOCUS/
XFOCUS Master File that hosts the target of your MDI.

Describing Data With TIBCO WebFOCUS® Language

 339

Multi-Dimensional Index (MDI)

Syntax:

How to Query a Multi-Dimensional Index

? MDI mastername {mdiname|*} [HOLD [AS holdfile]]

where:

mastername

Is the logical name of the Master File. If you do not include any other parameters, a list of
all MDI names specified is displayed with the command TARGET_OF in the Access File for
this mastername. If the Access File for the mastername does not have any MDI
information, a message will display.

mdiname

Is the logical name of an MDI. Specifying this parameter displays all the dimensions that
are part of this MDI.

mdiname must be specified as TARGET_OF in the Access File for this mastername, or a
message will display. If any of the dimensions are involved in a parent-child structure, a
tree-like picture will display.

*

Displays a list of all dimensions, by MDI, whose targets are specified inside the Access
File for this mastername.

HOLD

Saves the output in a text file.

holdfile

Is the file in which the output is saved. If this is not included with the AS phrase, the file is
named HOLD.

Using AUTOINDEX to Choose an MDI

When an Access File defines multiple MDIs, retrieval efficiency for a query may become a
function of the index it uses to access the data source. The AUTOINDEX facility analyzes each
retrieval request and chooses the MDI or B-tree index that provides the best access to the
data. You can issue the AUTOINDEX command in a FOCEXEC or in a profile. The AUTOINDEX
facility can be enabled or disabled. The default is to disable AUTOINDEX on reverse byte
platforms and to enable it on forward byte platforms.

340

6. Describing a FOCUS Data Source

In its analysis, AUTOINDEX considers the following factors:

The segment most involved in the query.

The MDI with the most filtering conditions (IF/WHERE selection tests).

The percent of index dimensions involved in the request from each MDI.

How close the fields being retrieved are to the target segment.

The size of each MDI.

If the selection criteria in a request do not involve any MDI fields, WebFOCUS looks for an
appropriate B-tree index to use for retrieval. If a field is both a B-tree index and a dimension in
an MDI, the MDI is used for retrieval if two-thirds of the fields in selection tests are
dimensions in the MDI. If it is less than two-thirds, the B-tree index is used. If there are
multiple B-tree indexes, the one highest in the hierarchy is used.

If everything else is equal, WebFOCUS uses the first MDI it finds in the Access File.

Syntax:

How to Enable or Disable AUTOINDEX for Retrieval

SET AUTOINDEX = {ON|OFF}

where:

ON

Optimizes MDI retrieval. AUTOINDEX can only be set to ON when the ALL parameter is set
to OFF.

OFF

Disables the AUTOINDEX facility. No MDI will be used for retrieval.

Note: AUTOINDEX defaults to ON on reverse byte platforms and to OFF on forward byte
platforms.

Note: WebFOCUS TABLE requests can automatically turn off AUTOINDEX and select the
appropriate index for retrieval by indicating the index name in the request itself:

TABLE FILE filename.mdiname

You can also assure access with a specific MDI by creating an Access File that describes only
that index.

Describing Data With TIBCO WebFOCUS® Language

 341

Multi-Dimensional Index (MDI)

Joining to a Multi-Dimensional Index

Joining to an MDI uses the power of the MDI to produce a fast, efficient join. Instead of joining
one field in the source file to an indexed field in the target file, you can join to multiple
dimensions of the MDI.

When the join is implemented, the answer set from the source file is created, and the values
retrieved for the source fields serve as index values for the corresponding dimensions in the
target MDI.

You can join to an MDI in two ways:

Join to all dimensions of a named MDI (MDI join). In the MDI join, you pick the MDI to use
in the join.

Join certain dimensions in a dimensional join. In this type of join, the JOIN engine picks the
most efficient MDI based on the dimensions you choose. The dimensional join supports
partial joins.

The source fields must form a one-to-one correspondence with the target dimensions. The MDI
engine uses the source field values to get pointers to the target segment of the MDI,
expediting data retrieval from the target file.

You can think of the source fields as mirror dimensions. If you put tighter constraints on the
mirror dimensions, a smaller answer set is retrieved from the source file, and fewer index I/Os
are required to locate the records from the target file. The speed of the join improves
dramatically with the speed of retrieval of the source file answer set. Therefore, you can
expedite any TABLE request against the source file by incorporating selection criteria on fields
that participate in either a B-tree or MDI.

The following formula computes the time for a TABLE request that uses an MDI Join:

Total Time = Time to Retrieve the answer set from the source file (Ts)
+ Time to retrieve the MD index pointers (Tp)
+ Time to retrieve data from the target file (Tt)

Using a B-tree index or MDI in data retrieval reduces all types of retrieval time, reducing the
total retrieval time.

342

6. Describing a FOCUS Data Source

Syntax:

How to Join to All Dimensions of a Multi-Dimensional Index

JOIN field_1 [AND field_2 ...] IN sfile [TAG tag_1]
TO ALL mdiname IN tfile [TAG tag_2] [AS joinname]
[END]

where:

field_1, field_2

Are the join fields from the source file.

sfile

Is the source Master File.

tag_1, tag_2

Are one-character to eight-character names that can serve as unique qualifiers for field
names in a request.

mdiname

Is the logical name of the MDI, built on tfile, to use in the join.

tfile

Is the target Master File.

joinname

Is a one-character to eight-character join name. A unique join name prevents a subsequent
join from overwriting the existing join, allows you to selectively clear the join, and serves as
a prefix for duplicate field names in a recursive join.

END

Is required to terminate the JOIN command if it is longer than one line.

Describing Data With TIBCO WebFOCUS® Language

 343

Multi-Dimensional Index (MDI)

Syntax:

How to Create a Dimensional Join

JOIN field_1 [AND field_2 ...] IN sfile [TAG tag_1]
TO ALL dim_1 [AND dim_2 ...] IN tfile [TAG tag_2] [AS joinname]
[END]

where:

field_1, field_2

Are the join fields from the source file.

sfile

Is the source Master File.

tag_1, tag_2

Are one-character to eight-character names that can serve as unique qualifiers for field
names in a request.

dim_1, dim_2

Are dimensions in tfile.

tfile

Is the target Master File.

joinname

Is a one-character to eight-character join name. A unique join name prevents a subsequent
join from overwriting the existing join, allows you to selectively clear the join, and serves as
a prefix for duplicate field names in a recursive join.

END

Is required to terminate the JOIN command if it is longer than one line.

Reference: Guidelines for Choosing a Source Field (Dimensional Joins Only)

A maximum of four mirror and MDI dimensions can participate in a JOIN command.

The target of the MDI must be a real segment in the target file.

The order of the mirror dimensions must match the exact physical order of the MDI (target)
dimensions.

The format of each mirror dimension must be identical to that of the corresponding MDI
dimension.

The ALL attribute is required.

344

6. Describing a FOCUS Data Source

Encoding Values in a Multi-Dimensional Index

WebFOCUS encodes indexed values any time a field or dimension of an MDI has a MAXVALUES
attribute specified or is involved in a parent-child relationship. Encoded values are stored in the
MDI file at rebuild time and can be retrieved and decoded with a TABLE request that specifies
the MDIENCODING command. The MDIENCODING command allows the user to get output from
the MDI file itself without having to read the data source.

Reference: Rules for Encoding a Multi-Dimensional Index

The following two rules apply to fields in a TABLE request that uses MDIENCODING:

Only one MDI can be referred to at a time.

Only dimensions that are part of the same parent-child hierarchy can be used
simultaneously in a request. A dimension that is not part of a parent-child relationship can
be used as the field in a request if it has a MAXVALUES attribute.

Syntax:

How to Retrieve Output From a Multi-Dimensional Index

SET MDIENCODING = {ON|OFF}

where:

ON

Enables retrieval of output from the MDI file without reading the data source.

OFF

Requires access of the data source to allow retrieval of MDI values.

Syntax:

How to Encode a Multi-Dimensional Index

TABLE FILE mastername.mdiname request
ON TABLE SET MDIENCODING ON
END

where:

mastername

Is the Master File.

mdiname

Is the logical name of the MDI.

Describing Data With TIBCO WebFOCUS® Language

 345

Multi-Dimensional Index (MDI)

request

Is the TABLE request that decodes the MDI.

Example:

Encoding a Multi-Dimensional Index

The following examples show correct MDI encoding:

TABLE FILE COMPANY.I DATA1
PRINT CITY BY STATE
ON TABLE SET MDIENCODING ON
END

TABLE FILE COMPANY.I DATA1
COUNT CITY
IF STATE EQ NY
ON TABLE SET MDIENCODING ON
END

TABLE FILE COMPANY.I DATA1
PRINT CATEGORY
ON TABLE SET MDIENCODING ON
END

The following example is incorrect because CATEGORY is not part of the CITY-STATE hierarchy.

TABLE FILE COMPANY.I DATA1
PRINT CITY BY STATE
IF STATE EQ NY
IF CATEGORY EQ RESTAURANT
ON TABLE SET MDIENCODING ON
END

Example:

Using a Multi-Dimensional Index in a Request

The following TABLE request accesses the CAR data source. It will use the CARMDI index for
retrieval because CARMDI is the only MDI described in the Master File:

TABLE FILE CAR
SUM RETAIL_COST DEALER_COST
BY BODYTYPE
-* WHERE Condition utilizing MDI fields:
WHERE (COUNTRY EQ 'JAPAN' OR 'ENGLAND')
AND (CAR EQ 'TOYOTA' OR 'JENSEN' OR 'TRIUMPH')
AND (MODEL EQ 'COROLLA 4 DOOR DIX AUTO'
OR 'INTERCEPTOR III' OR 'TR7')
END

346

6. Describing a FOCUS Data Source

Partitioning a Multi-Dimensional Index

If the data source has grown due to the addition of new data partitions, and these partitions
need to be added to the MDI, you must perform the following steps:

1. Update the Access File to include the new data partitions.

2. Verify that your MDI is partitioned. Remember that the ADD function of the REBUILD utility

cannot be executed on a non-partitioned MDI.

3. Perform the REBUILD, MDINDEX, and ADD on the MDI.

Example:

Adding a Partition to a Multi-Dimensional Index

The following FOCEXEC contains commands that add a partition to a multi-dimensional index
named CARMDI defined on the CAR data source:

REBUILD
MDINDEX
ADD
CAR
CARMDI
NO

After the MDI is rebuilt to include the new data partitions, any retrieval query that uses the MDI
will use the newly added data partitions within that MDI.

Querying the Progress of a Multi-Dimensional Index

Use the SET MDIPROGRESS command to view messages about the progress of your MDI build.
The messages will show the number of data records accumulated for every n records inserted
into the MDI as it is processed.

Syntax:

How to Query the Progress of a Multi-Dimensional Index

SET MDIPROGRESS = {0|n}

where:

n

0

Is an integer greater than 1000, which displays a progress message for every n records
accumulated in the MDI build. 100,000 is the default value.

Disables progress messages.

Describing Data With TIBCO WebFOCUS® Language

 347

Multi-Dimensional Index (MDI)

Displaying a Warning Message

The SET MDICARDWARN command displays a warning message every time a dimension
cardinality exceeds a specified value, offering you the chance to study the MDI build. When the
number of equal values of a dimension data reaches a specified percent, a warning message
will be issued. In order for MDICARDWARN to be reliable, the data source should contain at
least 100,000 records.

Note: In addition to the warning message, a number displays in brackets. This number is the
least number of equal values for the dimension mentioned in the warning message text.

Syntax:

How to Display a Warning Message

SET MDICARDWARN = n

where:

n

Is a percentage value from 0 to 50.

348

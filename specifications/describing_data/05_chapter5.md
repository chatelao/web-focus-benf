Chapter5

Describing a Sequential, VSAM, or ISAM
Data Source

You can describe and report from sequential, VSAM, and ISAM data sources.

In a sequential data source, records are stored and retrieved in the same order as they
are entered.

With VSAM and ISAM data sources, a new element is introduced: the key or group key. A
group key consists of one or more fields, and can be used to identify the various record
types in the data source. In the Master File representation of a data source with different
record types, each record type is assigned its own segment.

For VSAM and ISAM data sources, you must allocate the Master File name to the
CLUSTER component of the data source.

For information about updating VSAM data sources, see the Dynamic Private User Exit
appendix in the Adapter Administration manual.

In this chapter:

Sequential Data Source Formats

Standard Master File Attributes for a Sequential Data Source

Standard Master File Attributes for a VSAM or ISAM Data Source

Describing a Multiply Occurring Field in a Free-Format Data Source

Describing a Multiply Occurring Field in a Fixed-Format, VSAM, or ISAM Data Source

Redefining a Field in a Non-FOCUS Data Source

Extra-Large Record Length Support

Describing Multiple Record Types

Combining Multiply Occurring Fields and Multiple Record Types

Establishing VSAM Data and Index Buffers

Using a VSAM Alternate Index

Describing a Token-Delimited Data Source

Describing Data With TIBCO WebFOCUS® Language

 231

Sequential Data Source Formats

Sequential Data Source Formats

Sequential data sources formatted in the following ways are recognized:

Fixed-format, in which each field occupies a predefined position in the record.

Delimited, in which fields can occupy any position in a record and are separated by a
delimiter:

Comma-delimited or tab-delimited, in which fields can occupy any position in a record
and are separated by a comma or a tab, respectively. Ending a line terminates the
record.

Free-format is a type of comma-delimited data source in which a record can span
multiple lines and is terminated by a comma-dollar sign (,$) character combination.

Token-delimited, in which the delimiter can be any combination of characters. For
information on describing token-delimited files, see Describing a Token-Delimited Data
Source on page 282.

Note: SET HOLDLIST is not supported for delimited files.

You can describe two types of sequential data sources:

Simple. This is the most basic type, consisting of only one segment. It is supported in all
formats.

Complex. This is a multi-segment data source. The descendant segments exist in the data
source as multiply occurring fields (which are supported in both fixed-format and free-
format) or multiple record types (which are supported only in fixed-format).

What Is a Fixed-Format Data Source?

Fixed-format data sources are sequential data sources in which each field occupies a
predefined position in the record. You describe the record format in the Master File.

For example, a fixed-format record might look like this:

1352334556George Eliot The Mill on the Floss H

The simplest form of a fixed-record data source can be described by providing just field
declarations. For example, suppose you have a data source for a library that consists of the
following components:

A number, like an ISBN number, that identifies the book by publisher, author, and title.

The name of the author.

232

5. Describing a Sequential, VSAM, or ISAM Data Source

The title of the book.

A single letter that indicates whether the book is hard-bound or soft-bound.

The book's price.

A serial number that actually identifies the individual copies of the book in the library (a call
number).

A synopsis of the book.

This data source might be described with the seven field declarations shown here:

FIELDNAME = PUBNO    ,ALIAS = PN  ,USAGE = A10   ,ACTUAL = A10  ,$
FIELDNAME = AUTHOR   ,ALIAS = AT  ,USAGE = A25   ,ACTUAL = A25  ,$
FIELDNAME = TITLE    ,ALIAS = TL  ,USAGE = A50   ,ACTUAL = A50  ,$
FIELDNAME = BINDING  ,ALIAS = BI  ,USAGE = A1    ,ACTUAL = A1   ,$
FIELDNAME = PRICE    ,ALIAS = PR  ,USAGE = D8.2N ,ACTUAL = D8   ,$
FIELDNAME = SERIAL   ,ALIAS = SN  ,USAGE = A15   ,ACTUAL = A15  ,$
FIELDNAME = SYNOPSIS ,ALIAS = SYN ,USAGE = A150  ,ACTUAL = A150 ,$

Note:

Each declaration begins with the word FIELDNAME, and normally contains four elements (a
FIELDNAME, an ALIAS, a USAGE attribute, and an ACTUAL attribute).

ALIAS=, USAGE=, and ACTUAL= may be omitted as identifiers, since they are positional
attributes following FIELDNAME.

If you omit the optional ALIAS, its absence must be signaled by a second comma between
FIELDNAME and USAGE (FIELDNAME=PUBNO,,A10,A10,$).

Both the USAGE and the ACTUAL attributes must be included. Failure to specify both is a
common cause of errors in describing non-FOCUS data sources (FOCUS data sources do
not have ACTUAL attributes).

Each declaration can span multiple lines and must be terminated with a comma followed by
a dollar sign (,$). Typically, the LRECL for a Master File is 80 and the RECFM is F. Support
also exists for LRECL up to 32K and RECFM V.

When using Maintain Data to read a fixed-format data source, the record length as
described in the Master File may not exceed the actual length of the data record (the
LRECL value).

Describing Data With TIBCO WebFOCUS® Language

 233

Sequential Data Source Formats

You must describe the entire record. The values for field name and alias can be omitted for
fields that do not need to be accessed. This is significant when using existing data sources,
because they frequently contain information that you do not need for your requests. You
describe only the fields to include in your reports or calculations, and use filler fields to
represent the rest of the logical record length (LRECL) of the data source.

In the above example, the book synopsis is hardly necessary for most reports. The synopsis
can therefore be replaced with a filler field, as follows:

FIELDNAME = FILLER, ALIAS = FILL1, USAGE = A150, ACTUAL = A150,$

Fillers of this form may contain up to 4095 characters. If you need to describe larger areas,
use several filler fields together:

FIELDNAME = FILLER,,A256,A256,$
FIELDNAME = FILLER,,A200,A200,$

The field name FILLER is no different than any other field name. To prevent access to the data
in the field, you can use a blank field name. For example:

FIELDNAME =,,A200,A200,$

It is recommended that you include file and segment attributes, even for simple data sources,
to complete your documentation. The example below shows the Master File for the library data
source with file and segment declarations added.

FILENAME = LIBRARY1, SUFFIX = FIX,$
 SEGNAME = BOOKS, SEGTYPE = S0,$
  FIELDNAME = PUBNO   ,ALIAS = PN    ,USAGE = A10   ,ACTUAL = A10  ,$
  FIELDNAME = AUTHOR  ,ALIAS = AT    ,USAGE = A25   ,ACTUAL = A25  ,$
  FIELDNAME = TITLE   ,ALIAS = TL    ,USAGE = A50   ,ACTUAL = A50  ,$
  FIELDNAME = BINDING ,ALIAS = BI    ,USAGE = A1    ,ACTUAL = A1   ,$
  FIELDNAME = PRICE   ,ALIAS = PR    ,USAGE = D8.2N ,ACTUAL = D8   ,$
  FIELDNAME = SERIAL  ,ALIAS = SN    ,USAGE = A15   ,ACTUAL = A15  ,$
  FIELDNAME = FILLER  ,ALIAS = FILL1 ,USAGE = A150  ,ACTUAL = A150 ,$

What Is a Comma or Tab-Delimited Data Source?

Master Files for comma-delimited and tab-delimited sequential data sources can have SUFFIX
values of COM, COMT, TAB, or TABT. Comma-delimited data sources are sequential data
sources in which field values are separated by commas. Tab-delimited data sources are
sequential data sources in which field values are separated by tabs.

Note: SET HOLDLIST is not supported for delimited files.

You can also create delimited files using any token as the delimiter. For information, see
Describing a Token-Delimited Data Source on page 282.

234

5. Describing a Sequential, VSAM, or ISAM Data Source

You can use the SET HNODATA command to specify how to propagate missing data to these
data sources when you create them using the HOLD command. For more information, see the
Developing Reporting Applications manual.

For the SUFFIX values of COM, COMT, TAB and TABT, if the data is numeric and has a zoned
format (ACTUAL=Zn), the data must be unsigned (cannot contain a positive or negative value).

Reference: Accessing SUFFIX=COM Data Sources

A Master File containing the attribute SUFFIX=COM can be used to access two styles of
comma-delimited sequential data sources:

Free-format style is described in What Is a Free-Format Data Source? on page 236.
Character values are not enclosed in double quotation marks, and the comma-dollar sign
character combination terminates the record. With this style of comma-delimited data
source, records can span multiple lines. A field that contains a comma as a character must
be enclosed within single quotation marks.

The second style is consistent with the current industry standard for comma-delimited data
sources. Character values are enclosed in double quotation marks, and the cr/lf (carriage-
return, line-feed) character combination terminates the record, although the comma-dollar
sign combination is also accepted. In addition, each input record must be completely
contained on a single input line. A double quotation mark within a field is identified by two
consecutive double quotation marks.

Note that the setting PCOMMA=ON is required in conjunction with the SUFFIX=COM Master
File when accessing this type of data source in order to interpret the double quotation
marks around character values correctly. Without this setting, the double quotation marks
are considered characters within the field, not delimiters enclosing the field values.

Reference: Accessing SUFFIX=COMT Data Sources

A Master File containing the attribute SUFFIX=COMT can be used to access comma-delimited
sequential data sources in which all of the following conditions are met:

The first record of the data source contains column titles. This record is ignored when the
data source is accessed in a request.

Character values are enclosed in double quotation marks. A double quotation mark within a
field is identified by two consecutive double quotation marks.

Each record is completely contained on one line and terminated with the cr/lf character
combination.

Describing Data With TIBCO WebFOCUS® Language

 235

Sequential Data Source Formats

Reference: Accessing SUFFIX=TAB Data Sources

A Master File containing the attribute SUFFIX=TAB can be used to access tab-delimited
sequential data sources in which all of the following conditions are met:

Character values are not enclosed in double quotation marks.

Each record is completely contained on one line and terminated with the cr/lf character
combination.

Reference: Accessing SUFFIX=TABT Data Sources

A Master File containing the attribute SUFFIX=TABT can be used to access tab-delimited
sequential data sources in which all of the following conditions are met:

The first record of the data source contains column titles. This record is ignored when the
data source is accessed in a request.

Character values are not enclosed in double quotation marks.

Each record is completely contained on one line and terminated with the cr/lf character
combination.

What Is a Free-Format Data Source?

A common type of external structure is a comma-delimited sequential data source. These data
sources are a convenient way to maintain low volumes of data, since the fields in a record are
separated from one another by commas rather than being padded with blanks or zeroes to
fixed field lengths. Comma-delimited data sources must be stored as physical sequential data
sources.

Note: SET HOLDLIST is not supported for delimited files.

The report request language processes free-format comma-delimited data sources the same
way it processes fixed-format data sources. The same procedure is used to describe these
data sources in a comma-delimited Master File. The only difference is that the file suffix is
changed to COM, as shown:

FILENAME = filename, SUFFIX = COM,$

Note: Free-format comma-delimited data sources do not have character fields enclosed in
double quotation marks, and use the comma-dollar sign character combination to terminate
the record.

236

5. Describing a Sequential, VSAM, or ISAM Data Source

You can use the system editor to change values, add new records, and delete records. Since
the number of data fields on a line varies depending on the presence or absence of fields and
the actual length of the data values, a logical record may be one or several lines. Hence, you
need to use a terminator character to signal the end of the logical record. This is a dollar sign
following the last comma (,$).

A section of comma-delimited data might look like this:

PUBNO=1352334556, AUTHOR='Eliot, George',
TITLE='The Mill on the Floss', BINDING=H,$

The order in which the data values are described in the Master File plays an important role in
comma-delimited data sources. If the data values are typed in their natural order, then only
commas between the values are necessary. If a value is out of its natural order, then it is
identified by its name or alias and an equal sign preceding it, for example, AUTHOR= 'Eliot,
George'.

Rules for Maintaining a Free-Format Data Source

If a logical record contains every data field, it contains the same number of commas used as
delimiters as there are data fields. It also has a dollar sign following the last comma, signaling
the end of the logical record. Thus, a logical record containing ten data fields contains ten
commas as delimiters, plus a dollar sign record terminator.

A logical record may occupy as many lines in the data source as is necessary to contain the
data. A record terminator (,$) must follow the last physical field.

Each record need not contain every data field, however. The identity of a data field that might
be out of sequence can be provided in one of the following ways:

You can use the field name, followed by an equal sign and the data value.

You can use the field alias, followed by an equal sign and the data value.

You can use the shortest unique truncation of the field name or alias, followed by an equal
sign and the data value.

If a field name is not mentioned, it inherits its value from the prior record.

Thus, the following statements are all equivalent:

BI=H, PRICE=17.95,$
BI=H, PR=17.95,$
BI=H, P=17.95,$

Describing Data With TIBCO WebFOCUS® Language

 237

Standard Master File Attributes for a Sequential Data Source

Standard Master File Attributes for a Sequential Data Source

Most standard Master File attributes are used with sequential data sources in the standard
way. For more information, see Identifying a Data Source on page 31, Describing a Group of
Fields on page 65, and Describing an Individual Field on page 103.

SEGTYPE. The SEGTYPE attribute is ignored with free-format data sources.

The SEGTYPE value for fixed-format data sources has a default of S0. However, if you use
keyed retrieval, the SEGTYPE value depends on the number of keys and sort sequence. See
Describing a FOCUS Data Source on page 293, for a description of the SEGTYPE attribute.
For a description of keyed retrieval from fixed-format data sources, see the Creating Reports
With WebFOCUS Language manual.

ACTUAL. The ACTUAL values for sequential data sources are described in Describing an
Individual Field on page 103.

Note that file and segment declarations are optional for simple sequential data sources that
you are not joining. However, they are recommended in order to make the data source
description self-documenting, and to give you the option of joining the data source in the
future.

Standard Master File Attributes for a VSAM or ISAM Data Source

Most standard Master File attributes are used with VSAM and ISAM data sources in the
standard way. For more information, see Identifying a Data Source on page 31, Describing a
Group of Fields on page 65, and Describing an Individual Field on page 103.

SUFFIX. The SUFFIX attribute in the file declaration for these data sources has the value
VSAM or ISAM.

SEGNAME. The SEGNAME attribute of the first or root segment in a Master File for a VSAM
or ISAM data source must be ROOT. The remaining segments can have any valid segment
name.

The only exception involves unrelated RECTYPEs, where the root SEGNAME must be
DUMMY.

All non-repeating data goes in the root segment. The remaining segments may have any
valid name from one to eight characters.

Any segment except the root is the descendant, or child, of another segment. The PARENT
attribute supplies the name of the segment that is the hierarchical parent or owner of the
current segment. If no PARENT attribute appears, the default is the immediately preceding
segment. The PARENT name may be one to eight characters.

238

5. Describing a Sequential, VSAM, or ISAM Data Source

SEGTYPE. The SEGTYPE attribute should be S0 for VSAM data sources. (For a general
description of the SEGTYPE attribute, see Describing a Group of Fields on page 65.)

GROUP. The keys of a VSAM or ISAM data source are defined in the segment declarations
as GROUPs consisting of one or more fields.

Describing a Group Field With Formats

A single-segment data source may have only one key field, but it must still be described with a
GROUP declaration. The group must have ALIAS=KEY.

Groups can also be assigned simply to provide convenient reference names for groups of
fields. Suppose that you have a series of three fields for an employee: last name, first name,
and middle initial. You use these three fields consistently to identify the employee. You can
identify the three fields in your Master File as a GROUP named EMPINFO. Then, you can refer
to these three linked fields as a single unit, called EMPINFO. When using the GROUP feature
for non-keys, the parameter ALIAS= must still be used, but should not equal KEY.

For group fields, you must supply both the USAGE and ACTUAL formats in alphanumeric
format. The length must be exactly the sum of the subordinate field lengths.

The GROUP declaration USAGE attribute specifies how many positions to use to describe the
key in a VSAM KSDS data source. If a Master File does not completely describe the full key at
least once, the following warning message appears:

(FOC1016) INVALID KEY DESCRIPTION IN MASTER FILE

The cluster key definition is compared to the Master File for length and displacement.

When you expand on the key in a RECTYPE data source, describe the key length in full on the
last non-OCCURS segment on each data path.

Do not describe a group with ALIAS=KEY for OCCURS segments.

If the fields that make up a group key are not alphanumeric fields, the format of the group key
is still alphanumeric, but its length is determined differently. The ACTUAL length is still the
sum of the subordinate field lengths. The USAGE format, however, is the sum of the internal
storage lengths of the subordinate fields because regardless of the data types, the group will
be displayed as alphanumeric. You determine these internal storage lengths as follows:

Fields of type I have a value of 4.

Fields of type F have a value of 4.

Fields of type P that are 8 bytes can have a USAGE of P15.x or P16 (sign and decimal for a
total of 15 digits). Fields that are 16 bytes have a USAGE of P16.x, P17 or larger.

Describing Data With TIBCO WebFOCUS® Language

 239

Standard Master File Attributes for a VSAM or ISAM Data Source

Fields of type D have a value of 8.

Alphanumeric fields have a value equal to the number of characters they contain as their
field length.

Note:

Since all group fields must be defined in alphanumeric format, those that include numeric
component fields should not be used as verb objects in a report request.

The MISSING attribute is not supported on the group field, but is supported on the
individual fields comprising the group.

Syntax:

How to Describe a VSAM Group Field With Formats

GROUP = keyname, ALIAS = KEY, USAGE = Ann, ACTUAL = Ann ,$

where:

keyname

Can have up to 66 characters.

Example:

Describing a VSAM Group Field With Formats

In the library data source, the first field, PUBNO, can be described as a group key. The
publisher number consists of three elements: a number that identifies the publisher, one that
identifies the author, and one that identifies the title. They can be described as a group key,
consisting of a separate field for each element if the data source is a VSAM data structure.

The Master File looks as follows:

FILE = LIBRARY5, SUFFIX = VSAM,$
 SEGMENT = ROOT, SEGTYPE = S0,$
  GROUP = BOOKKEY      ,ALIAS = KEY ,USAGE = A10   ,ACTUAL = A10  ,$
   FIELDNAME = PUBNO   ,ALIAS = PN  ,USAGE = A3    ,ACTUAL = A3   ,$
   FIELDNAME = AUTHNO  ,ALIAS = AN  ,USAGE = A3    ,ACTUAL = A3   ,$
   FIELDNAME = TITLNO  ,ALIAS = TN  ,USAGE = A4    ,ACTUAL = A4   ,$
  FIELDNAME = AUTHOR   ,ALIAS = AT  ,USAGE = A25   ,ACTUAL = A25  ,$
  FIELDNAME = TITLE    ,ALIAS = TL  ,USAGE = A50   ,ACTUAL = A50  ,$
  FIELDNAME = BINDING  ,ALIAS = BI  ,USAGE = A1    ,ACTUAL = A1   ,$
  FIELDNAME = PRICE    ,ALIAS = PR  ,USAGE = D8.2N ,ACTUAL = D8   ,$
  FIELDNAME = SERIAL   ,ALIAS = SN  ,USAGE = A15   ,ACTUAL = A15  ,$
  FIELDNAME = SYNOPSIS ,ALIAS = SY  ,USAGE = A150  ,ACTUAL = A150 ,$
  FIELDNAME = RECTYPE  ,ALIAS = B   ,USAGE = A1    ,ACTUAL = A1   ,$

240

5. Describing a Sequential, VSAM, or ISAM Data Source

Example:

Describing a VSAM Group Field With Multiple Formats

GROUP = A, ALIAS = KEY, USAGE = A14, ACTUAL = A8   ,$
 FIELDNAME = F1, ALIAS = F1, USAGE = P6, ACTUAL=P2 ,$
 FIELDNAME = F2, ALIAS = F2, USAGE = I9, ACTUAL=I4 ,$
 FIELDNAME = F3, ALIAS = F3, USAGE = A2, ACTUAL=A2 ,$

The lengths of the ACTUAL attributes for subordinate fields F1, F2, and F3 total 8, which is the
length of the ACTUAL attribute of the group key. The display lengths of the USAGE attributes
for the subordinate fields total 17. However, the length of the group key USAGE attribute is
found by adding their internal storage lengths as specified by their field types: 8 for
USAGE=P6, 4 for USAGE=I9, and 2 for USAGE=A2, for a total of 14.

Example:

Accessing a Group Field With Multiple Formats

When you use a group field with multiple formats in a query, you must account for each
position in the group, including trailing blanks or leading zeros. The following example
illustrates how to access a group field with multiple formats in a query:

GROUP = GRPB, ALIAS = KEY, USAGE = A8, ACTUAL = A8 ,$
 FIELDNAME = FIELD1, ALIAS = F1, USAGE = A2, ACTUAL = A2 ,$
 FIELDNAME = FIELD2, ALIAS = F2, USAGE = I8, ACTUAL = I4 ,$
 FIELDNAME = FIELD3, ALIAS = F3, USAGE = A2, ACTUAL = A2 ,$

The values in fields F1 and F3 may include some trailing blanks, and the values in field F2 may
include some leading zeros. When using the group in a query, you must account for each
position. Because FIELD2 is a numeric field, you cannot specify the IF criteria as follows:

IF GRPB EQ 'A 0334BB'

You can eliminate this error by using a slash (/) to separate the components of the group key:

IF GRPB EQ 'A/334/BB'

Note: Blanks and leading zeros are assumed where needed to fill out the key.

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

 241

Standard Master File Attributes for a VSAM or ISAM Data Source

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

242

Reference: Usage Notes for Group Elements

5. Describing a Sequential, VSAM, or ISAM Data Source

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

 243

Describing a Multiply Occurring Field in a Free-Format Data Source

Note that the display characteristics of the group have not changed. The mixed format group
GRP1 will still display as all alphanumeric.

Describing a Multiply Occurring Field in a Free-Format Data Source

Since any data field not explicitly referred to in a logical record continues to have the same
value as it did the last time one was assigned, up until the point a new data value is entered,
a free-format sequential data source can resemble a hierarchical structure. The parent
information needs to be entered only once, and it carries over for each descendant segment.

Example:

Describing a Multiply Occurring Field in a Free-Format Data Source

Consider the example of a library data source. The information for two copies of The Sun Also
Rises, one hardcover and one paperback, can be entered as follows:

PUBNO=1234567890, AUTHOR='Hemingway, Ernest',
TITLE='The Sun Also Rises',
 BI=H,PR=17.95, $
 BI=S,PR=5.25, $

There are two values for binding and price, which both correspond to the same publisher
number, author, and title. In the Master File, the information that occurs only once (the
publisher number, author, and title) is placed in one segment, and the information that occurs
several times in relation to this information is placed in a descendant segment.

Similarly, information that occurs several times in relation to the descendant segment, such as
an individual serial number for each copy of the book, is placed in a segment that is a
descendant of the first descendant segment, as shown in the following diagram:

244

5. Describing a Sequential, VSAM, or ISAM Data Source

Describe this data source as follows:

FILENAME = LIBRARY4, SUFFIX = COM, $
 SEGNAME = PUBINFO, SEGTYPE=S0, $
  FIELDNAME = PUBNO,   ALIAS = PN,   USAGE = A10,   ACTUAL = A10, $
  FIELDNAME = AUTHOR,  ALIAS = AT,   USAGE = A25,   ACTUAL = A25, $
  FIELDNAME = TITLE,   ALIAS = TL,   USAGE = A50,   ACTUAL = A50, $
 SEGNAME = BOOKINFO, PARENT = PUBINFO,  SEGTYPE=S0, $
  FIELDNAME = BINDING, ALIAS = BI,   USAGE = A1,    ACTUAL = A1,  $
  FIELDNAME = PRICE,   ALIAS = PR,   USAGE = D8.2N, ACTUAL = D8,  $
 SEGNAME = SERIANO,  PARENT = BOOKINFO, SEGTYPE=S0, $
  FIELDNAME = SERIAL,  ALIAS = SN,   USAGE = A15,   ACTUAL = A15, $

Note that each segment other than the first has a PARENT attribute. You use the PARENT
attribute to signal that you are describing a hierarchical structure.

Describing a Multiply Occurring Field in a Fixed-Format, VSAM, or ISAM Data Source

Fixed-format sequential, VSAM, or ISAM data sources can have repeating fields. Consider the
following data structure:

A

B

C1

C2

C1

C2

Fields C1 and C2 repeat within this data record. C1 has an initial value, as does C2. C1 then
provides a second value for that field, as does C2. Thus, there are two values for fields C1 and
C2 for every one value for fields A and B.

The number of times C1 and C2 occur does not have to be fixed. It can depend on the value of
a counter field. Suppose field B is this counter field. In the case shown above, the value of
field B is 2, since C1 and C2 occur twice. The value of field B in the next record can be 7, 1, 0,
or any other number you choose, and fields C1 and C2 occur that number of times.

The number of times fields C1 and C2 occur can also be variable. In this case, everything after
fields A and B is assumed to be a series of C1s and C2s, alternating to the end of the record.

Describe these multiply occurring fields by placing them in a separate segment. Fields A and B
are placed in the root segment. Fields C1 and C2, which occur multiply in relation to A and B,
are placed in a descendant segment. You use an additional segment attribute, the OCCURS
attribute, to specify that these segments represent multiply occurring fields. In certain cases,
you may also need a second attribute, called the POSITION attribute.

Describing Data With TIBCO WebFOCUS® Language

 245

Describing a Multiply Occurring Field in a Fixed-Format, VSAM, or ISAM Data Source

Using the OCCURS Attribute

The OCCURS attribute is an optional segment attribute used to describe records containing
repeating fields or groups of fields. Define such records by describing the singly occurring
fields in one segment, and the multiply occurring fields in a descendant segment. The OCCURS
attribute appears in the declaration for the descendant segment.

You can have several sets of repeating fields in your data structure. Describe each of these
sets of fields as a separate segment in your data source description. Sets of repeating fields
can be divided into two basic types: parallel and nested.

Syntax:

How to Specify a Repeating Field

OCCURS = occurstype

Possible values for occurstype are:

n

Is an integer value showing the number of occurrences (from 1 to 4095).

fieldname

Names a field in the parent segment or a virtual field in an ancestor segment whose
integer value contains the number of occurrences of the descendant segment. Note that if
you use a virtual field as the OCCURS value, it cannot be redefined inside or outside of the
Master File.

VARIABLE

Indicates that the number of occurrences varies from record to record. The number of
occurrences is computed from the record length (for example, if the field lengths for the
segment add up to 40, and 120 characters are read in, it means there are three
occurrences).

Place the OCCURS attribute in your segment declaration after the PARENT attribute.

When different types of records are combined in one data source, each record type can contain
only one segment defined as OCCURS=VARIABLE. It may have OCCURS descendants (if it
contains a nested group), but it may not be followed by any other segment with the same
parent. There can be no other segments to its right in the hierarchical data structure. This
restriction is necessary to ensure that data in the record is interpreted unambiguously.

246

5. Describing a Sequential, VSAM, or ISAM Data Source

Example:

Using the OCCURS Attribute

Consider the following simple data structure:

A

B

C1

C2

C1

C2

You have two occurrences of fields C1 and C2 for every one occurrence of fields A and B.
Thus, to describe this data source, you place fields A and B in the root segment, and fields C1
and C2 in a descendant segment, as shown here:

Describe this data source as follows:

FILENAME = EXAMPLE1, SUFFIX = FIX, $
 SEGNAME = ONE, SEGTYPE=S0, $
  FIELDNAME = A,  ALIAS=, USAGE = A2, ACTUAL = A2, $
  FIELDNAME = B,  ALIAS=, USAGE = A1, ACTUAL = A1, $
 SEGNAME = TWO, PARENT = ONE, OCCURS = 2, SEGTYPE=S0, $
  FIELDNAME = C1, ALIAS=, USAGE = I4, ACTUAL = I2, $
  FIELDNAME = C2, ALIAS=, USAGE = I4, ACTUAL = I2, $

Describing a Parallel Set of Repeating Fields

Parallel sets of repeating fields are those that have nothing to do with one another (that is,
they have no parent-child or logical relationship). Consider the following data structure:

A1

A2

B1

B2

B1

B2

C1

C2

C1

C2

C1

C2

Describing Data With TIBCO WebFOCUS® Language

 247

Describing a Multiply Occurring Field in a Fixed-Format, VSAM, or ISAM Data Source

In this example, fields B1 and B2 and fields C1 and C2 repeat within the record. The number
of times that fields B1 and B2 occur has nothing to do with the number of times fields C1 and
C2 occur. Fields B1 and B2 and fields C1 and C2 are parallel sets of repeating fields. They
should be described in the data source description as children of the same parent, the
segment that contains fields A1 and A2.

The following data structure reflects their relationship:

Describing a Nested Set of Repeating Fields

Nested sets of repeating fields are those whose occurrence depends on one another in some
way. Consider the following data structure:

A1

A2

B1

B2

C1

C1

B1

B2

C1

C1

C1

248

5. Describing a Sequential, VSAM, or ISAM Data Source

In this example, field C1 only occurs after fields B1 and B2 occur once. It occurs varying
numbers of times, recorded by a counter field, B2. There is not a set of occurrences of C1
which is not preceded by an occurrence of fields B1 and B2. Fields B1, B2, and C1 are a
nested set of repeating fields.

These repeating fields can be represented by the following data structure:

Since field C1 repeats with relation to fields B1 and B2, which repeat in relation to fields A1
and A2, field C1 is described as a separate, descendant segment of Segment TWO, which is in
turn a descendant of Segment ONE.

Example:

Describing Parallel and Nested Repeating Fields

The following data structure contains both nested and parallel sets of repeating fields.

A
1

A
2

B
1

B
2

C
1

C
1

C
1

B
1

B
2

C
1

C
1

C
1

C
1

D
1

D
1

E
1

E
1

E
1

E
1

Describing Data With TIBCO WebFOCUS® Language

 249
















Describing a Multiply Occurring Field in a Fixed-Format, VSAM, or ISAM Data Source

It produces the following data structure:

Describe this data source as follows. Notice that the assignment of the PARENT attributes
shows you how the occurrences are nested.

FILENAME = EXAMPLE3, SUFFIX = FIX,$
 SEGNAME = ONE,   SEGTYPE=S0,$
  FIELDNAME = A1 ,ALIAS= ,ACTUAL = A1  ,USAGE = A1  ,$
  FIELDNAME = A2 ,ALIAS= ,ACTUAL = I1  ,USAGE = I1  ,$
 SEGNAME = TWO,   SEGTYPE=S0, PARENT = ONE, OCCURS = 2  ,$
  FIELDNAME = B1 ,ALIAS= ,ACTUAL = A15 ,USAGE = A15 ,$
  FIELDNAME = B2 ,ALIAS= ,ACTUAL = I1  ,USAGE = I1  ,$
 SEGNAME = THREE, SEGTYPE=S0, PARENT = TWO, OCCURS = B2 ,$
  FIELDNAME = C1 ,ALIAS= ,ACTUAL = A25 ,USAGE = A25 ,$
 SEGNAME = FOUR,  SEGTYPE=S0, PARENT = ONE, OCCURS = A2 ,$
  FIELDNAME = D1 ,ALIAS= ,ACTUAL = A15 ,USAGE = A15 ,$
 SEGNAME = FIVE,  SEGTYPE=S0, PARENT = ONE, OCCURS = VARIABLE,$
  FIELDNAME = E1 ,ALIAS= ,ACTUAL = A5  ,USAGE = A5  ,$

250

5. Describing a Sequential, VSAM, or ISAM Data Source

Note:

Segments ONE, TWO, and THREE represent a nested group of repeating segments. Fields
B1 and B2 occur a fixed number of times, so OCCURS equals 2. Field C1 occurs a certain
number of times within each occurrence of fields B1 and B2. The number of times C1
occurs is determined by the value of field B2, which is a counter. In this case, its value is 3
for the first occurrence of Segment TWO and 4 for the second occurrence.

Segments FOUR and FIVE consist of fields that repeat independently within the parent
segment. They have no relationship to each other or to Segment TWO except their common
parent, so they represent a parallel group of repeating segments.

As in the case of Segment THREE, the number of times Segment FOUR occurs is
determined by a counter in its parent, A2. In this case, the value of A2 is two.

The number of times Segment FIVE occurs is variable. This means that all the rest of the
fields in the record (all those to the right of the first occurrence of E1) are read as
recurrences of field E1. To ensure that data in the record is interpreted unambiguously, a
segment defined as OCCURS=VARIABLE must be at the end of the record. In a data
structure diagram, it is the rightmost segment. Note that there can be only one segment
defined as OCCURS=VARIABLE for each record type.

Using the POSITION Attribute

The POSITION attribute is an optional attribute used to describe a structure in which multiply
occurring fields with an established number of occurrences are located in the middle of the
record. You describe the data source as a hierarchical structure, made up of a parent segment
and at least one child segment that contains the multiply occurring fields. The parent segment
is made up of whatever singly occurring fields are in the record, as well as one or more
alphanumeric fields that appear where the multiply occurring fields appear in the record. The
alphanumeric field may be a dummy field that is the exact length of the combined multiply
occurring fields. For example, if you have four occurrences of an eight-character field, the
length of the field in the parent segment is 32 characters.

You can also use the POSITION attribute to redescribe fields with SEGTYPE=U. For more
information, see Redefining a Field in a Non-FOCUS Data Source on page 254.

Describing Data With TIBCO WebFOCUS® Language

 251

Describing a Multiply Occurring Field in a Fixed-Format, VSAM, or ISAM Data Source

Syntax:

How to Specify the Position of a Repeating Field

The POSITION attribute is described in the child segment. It gives the name of the field in the
parent segment that specifies the starting position and overall length of the multiply occurring
fields. The syntax of the POSITION attribute is

POSITION = fieldname

where:

fieldname

Is the name of the field in the parent segment that defines the starting position of the
multiple field occurrences.

Example:

Specifying the Position of a Repeating Field

Consider the following data structure:

A1

Q1

Q1

Q1

Q1

A2

A3

A4

In this example, field Q1 repeats four times in the middle of the record. When you describe
this structure, you specify a field or fields that occupy the position of the four Q1 fields in the
record. You then assign the actual Q1 fields to a multiply occurring descendant segment. The
POSITION attribute, specified in the descendant segment, gives the name of the field in the
parent segment that identifies the starting position and overall length of the Q fields.

Use the following Master File to describe this structure:

FILENAME = EXAMPLE3, SUFFIX = FIX,$
 SEGNAME = ONE, SEGTYPE=S0,$
  FIELDNAME = A1   ,ALIAS= ,USAGE = A14 ,ACTUAL = A14 ,$
  FIELDNAME = QFIL ,ALIAS= ,USAGE = A32 ,ACTUAL = A32 ,$
  FIELDNAME = A2   ,ALIAS= ,USAGE = I2  ,ACTUAL = I2  ,$
  FIELDNAME = A3   ,ALIAS= ,USAGE = A10 ,ACTUAL = A10 ,$
  FIELDNAME = A4   ,ALIAS= ,USAGE = A15 ,ACTUAL = A15 ,$
 SEGNAME = TWO, SEGTYPE=S0, PARENT = ONE, POSITION = QFIL, OCCURS = 4 ,$
  FIELDNAME = Q1   ,ALIAS= ,USAGE = D8  ,ACTUAL = D8  ,$

252

5. Describing a Sequential, VSAM, or ISAM Data Source

This produces the following structure:

If the total length of the multiply occurring fields is longer than 4095, you can use a filler field
after the dummy field to make up the remaining length. This is required, because the format of
an alphanumeric field cannot exceed 4095 bytes.

Notice that this structure works only if you have a fixed number of occurrences of the repeating
field. This means the OCCURS attribute of the descendant segment must be of the type
OCCURS=n. OCCURS=fieldname or OCCURS=VARIABLE does not work.

Specifying the ORDER Field

In an OCCURS segment, the order of the data may be significant. For example, the values may
represent monthly or quarterly data, but the record itself may not explicitly specify the month or
quarter to which the data applies.

To associate a sequence number with each occurrence of the field, you may define an internal
counter field in any OCCURS segment. A value is automatically supplied that defines the
sequence number of each repeating group.

Describing Data With TIBCO WebFOCUS® Language

 253

Redefining a Field in a Non-FOCUS Data Source

Syntax:

How to Specify the Sequence of a Repeating Field

The syntax rules for an ORDER field are:

It must be the last field described in an OCCURS segment.

The field name is arbitrary.

The ALIAS is ORDER.

The USAGE is In, with any appropriate edit options.

The ACTUAL is I4.

Order values are 1, 2, 3, and so on, within each occurrence of the segment. The value is
assigned prior to any selection tests that might accept or reject the record, and so it can be
used in a selection test.

Example:

Using the ORDER Attribute in a Selection Test

The following declaration assigns ACT_MONTH as the ORDER field:

FIELD = ACT_MONTH, ALIAS = ORDER, USAGE = I2MT, ACTUAL = I4, $

The following WHERE test obtains data for only the month of June:

SUM AMOUNT...
WHERE ACT_MONTH IS 6

The ORDER field is a virtual field used internally. It does not alter the logical record length
(LRECL) of the data source being accessed.

Redefining a Field in a Non-FOCUS Data Source

Redefining record fields in non-FOCUS data sources is supported. This enables you to describe
a field with an alternate layout.

Within the Master File, the redefined fields must be described in a separate unique segment
(SEGTYPE=U) using the POSITION=fieldname and OCCURS=1 attributes.

The redefined fields can have any user-defined name.

254

5. Describing a Sequential, VSAM, or ISAM Data Source

Syntax:

How to Redefine a Field

SEGNAME = segname, SEGTYPE = U, PARENT = parentseg,
OCCURS = 1, POSITION = fieldname,$

where:

segname

Is the name of the segment.

parentseg

Is the name of the parent segment.

fieldname

Is the name of the first field being redefined. Using the unique segment with redefined
fields helps avoid problems with multipath reporting.

A one-to-one relationship forms between the parent record and the redefined segment.

Example:

Redefining a VSAM Structure

The following example illustrates redefinition of the VSAM structure described in the COBOL
file description, where the COBOL FD is:

01 ALLFIELDS
  02 FLD1   PIC X(4)         -  this describes alpha/numeric data
  02 FLD2   PIC X(4)         -  this describes numeric data
  02 RFLD1  PIC 9(5)V99 COMP-3 REDEFINES FLD2
  02 FLD3   PIC X(8)         -  this describes alpha/numeric data

FILE = REDEF, SUFFIX = VSAM,$
 SEGNAME = ONE, SEGTYPE = S0,$
  GROUP = RKEY, ALIAS = KEY, USAGE = A4 ,ACTUAL = A4 ,$
   FIELDNAME = FLD1,,  USAGE = A4   ,ACTUAL = A4 ,$
   FIELDNAME = FLD2,,  USAGE = A4   ,ACTUAL = A4 ,$
   FIELDNAME = FLD3,,  USAGE = A8   ,ACTUAL = A8 ,$
 SEGNAME = TWO, SEGTYPE = U, POSITION = FLD2,OCCURS = 1, PARENT = ONE ,$
   FIELDNAME = RFLD1,, USAGE = P8.2 ,ACTUAL = Z4 ,$

Describing Data With TIBCO WebFOCUS® Language

 255


Extra-Large Record Length Support

Reference: Special Considerations for Redefining a Field

Redefinition is a read-only feature and is used only for presenting an alternate view of the
data. It is not used for changing the format of the data.

For non-alphanumeric fields, you must know your data. Attempts to print numeric fields that
contain alphanumeric data produce data exceptions or errors converting values. It is
recommended that the first definition always be alphanumeric to avoid conversion errors.

More than one field can be redefined in a segment.

Redefines are supported only for IDMS, IMS, VSAM, DB2, and FIX data sources.

Extra-Large Record Length Support

MAXLRECL indicates the largest actual file record length that WebFOCUS can read. The limit
for MAXLRECL is 65536 bytes, allowing the user to read a record twice as large as the length
of the internal matrix, which is limited to 32K.

If the Master File describes a data source with OCCURS segments, and if the longest single
record in the data source is larger than 16K bytes, it is necessary to specify a larger record
size in advance.

Syntax:

How to Define the Maximum Record Length

SET MAXLRECL = nnnnn

where:

nnnnn

Is an integer value up to 65536.

For example, SET MAXLRECL=12000 allows handling of records that are 12000 bytes long.
After you have entered the SET MAXLRECL command, you can obtain the current value of the
MAXLRECL parameter by using the ? SET MAXLRECL command.

If the actual record length is longer than specified, retrieval halts and the actual record length
appears in hexadecimal notation.

256

Describing Multiple Record Types

5. Describing a Sequential, VSAM, or ISAM Data Source

Fixed-format sequential, VSAM, and ISAM data sources can contain more than one type of
record. When they do, they can be structured in one of two ways:

A positional relationship may exist between the various record types, with a record of one
type being followed by one or more records containing detailed information about the first
record.

If a positional relationship exists between the various record types, with a parent record of
one type followed by one or more child records containing detail information about the
parent, you describe the structure by defining the parent as the root, and the detail
segments as descendants.

Some VSAM and ISAM data sources are structured so that descendant records relate to
each other through concatenating key fields. That is, the key fields of a parent record serve
as the first part of the key of a child record. In such cases, the segment key fields must be
described using a GROUP declaration. Each segment GROUP key fields consist of the
renamed key fields from the parent segment plus the unique key field from the child record.

The records have no meaningful positional relationship, and records of varying types exist
independently of each other in the data source.

If the records have no meaningful positional relationship, you have to provide some means
for interpreting the type of record that has been read. Do this by creating a dummy root
segment for the records.

In order to describe sequential data sources with several types of records, regardless of
whether they are logically related, use the PARENT segment attribute and the RECTYPE field
attribute. Any complex sequential data source is described as a multi-segment structure.

Key-sequenced VSAM and complex ISAM data sources also use the RECTYPE attribute to
distinguish various record types within the data source.

A parent does not always share its RECTYPE with its descendants. It may share some other
identifying piece of information, such as the PUBNO in the example. This is the field that
should be included in the parent key, as well as the keys of all of its descendants, to relate
them.

When using the RECTYPE attribute in VSAM or ISAM data sources with group keys, the
RECTYPE field can be part of the segment group key only when it belongs to a segment that
has no descendants, or to a segment whose descendants are described with an OCCURS
attribute. In Describing VSAM Positionally Related Records on page 262, the RECTYPE field is
added to the group key in the SERIANO segment, the lowest descendant segment in the chain.

Describing Data With TIBCO WebFOCUS® Language

 257

Describing Multiple Record Types

SEGTYPE Attributes With RECTYPE Fields

It is always assumed that at least one record for each SEGTYPE will exist in positionally related
types. The SEGTYPE is usually S0.

In the case where there is a unique relationship between the parent RECTYPE and a child
RECTYPE, and only one record of the child is expected for a given parent, a SEGTYPE of U may
be used. This will have the effect of making the second segment be a logical extension of the
parent. An example is when a given bookcode has only one book name but might have multiple
editions. Then, edition information can be sorted by BOOKCODE or BOOKNAME.

Note: When specifying SEGTYPE U for this type of file, the rule is that there must be an
instance of the child for each parent instance. If the child instance is missing, the results are
unpredictable and will not be defaulted to blanks.

Describing a RECTYPE Field

When a data source contains multiple record types, there must be a field in the records
themselves that can be used to differentiate between the record types. You can find
information on this field in your existing description of the data source (for example, a COBOL
FD statement). This field must appear in the same physical location of each record. For
example, columns 79 and 80 can contain a different two-digit code for each unique record
type. Describe this identifying field with the field name RECTYPE.

Another technique for redefining the parts of records is to use the MAPFIELD and MAPVALUE
attributes described in Describing a Repeating Group Using MAPFIELD on page 275.

Syntax:

How to Specify a Record Type Field

The RECTYPE field must fall in the same physical location of each record in the data source, or
the record is ignored. The syntax to describe the RECTYPE field is

FIELDNAME = RECTYPE, ALIAS = value, USAGE = format, ACTUAL = format,
ACCEPT = {list|range} ,$

where:

value

Is the record type in alphanumeric format, if an ACCEPT list is not specified. If there is an
ACCEPT list, this can be any value.

258

5. Describing a Sequential, VSAM, or ISAM Data Source

format

Is the data type of the field. In addition to RECTYPE fields in alphanumeric format,
RECTYPE fields in packed and integer formats (formats P and I) are supported. Possible
values are:

An (where n is 1-4095) indicates character data, including letters, digits, and other
characters.

In indicates ACTUAL (internal) format binary integers:

I1 = single-byte binary integer.

I2 = half-word binary integer (2 bytes).

I4 = full-word binary integer (4 bytes).

The USAGE format can be I1 through I9, depending on the magnitude of the ACTUAL
format.

Pn (where n is 1-16) indicates packed decimal ACTUAL (internal) format. n is the number of
bytes, each of which contains two digits, except for the last byte which contains a digit and
the sign. For example, P6 means 11 digits plus a sign.

If the field contains an assumed decimal point, represent the field with a USAGE format of
Pm.n, where m is the total number of digits, and n is the number of decimal places. Thus,
P11.1 means an eleven-digit number with one decimal place.

list

Is a list of one or more lines of specific RECTYPE values for records that have the same
segment layout. The maximum number of characters allowed in the list is 255. Separate
each item in the list with either a blank or the keyword OR. If the list contains embedded
blanks or commas, it must be enclosed within single quotation marks. The list may contain
a single RECTYPE value. For example:

FIELDNAME = RECTYPE, ALIAS = TYPEABC, USAGE = A1,ACTUAL = A1,
 ACCEPT = A OR B OR C, $

range

Is a range of one or more lines of RECTYPE values for records that have the same
segment layout. The maximum number of characters allowed in the range is 255. If the
range contains embedded blanks or commas, it must be enclosed within single quotation
marks.

To specify a range of values, include the lowest value, the keyword TO, and the highest
value, in that order. For example:

Describing Data With TIBCO WebFOCUS® Language

 259

Describing Multiple Record Types

FIELDNAME = RECTYPE, ALIAS = ACCTREC, USAGE = P3,ACTUAL = P2,
 ACCEPT = 100 TO 200, $

Example:

Specifying the RECTYPE Field

The following field description is of a one-byte packed RECTYPE field containing the value 1:

FIELD = RECTYPE, ALIAS = 1, USAGE = P1, ACTUAL = P1, $

The following field description is of a three-byte alphanumeric RECTYPE field containing the
value A34:

FIELD = RECTYPE, ALIAS = A34, USAGE = A3, ACTUAL = A3,$

Describing Positionally Related Records

The following diagram shows a more complex version of the library data source:

Information that is common to all copies of a given book (the identifying number, the author
name, and its title) has the same record type. All of this information is assigned to the root
segment in the Master File. The synopsis is common to all copies of a given book, but in this
data source it is described as a series of repeating fields of ten characters each, in order to
save space.

260

5. Describing a Sequential, VSAM, or ISAM Data Source

The synopsis is assigned to its own subordinate segment with an attribute of
OCCURS=VARIABLE in the Master File. Although there are segments in the diagram to the right
of the OCCURS=VARIABLE segment, OCCURS=VARIABLE is the rightmost segment within its
own record type. Only segments with a RECTYPE that is different from the OCCURS=VARIABLE
segment can appear to its right in the structure. Note also that the OCCURS=VARIABLE
segment does not have a RECTYPE. This is because it is part of the same record as its parent
segment.

Binding and price can vary among copies of a given title. For instance, the library may have two
different versions of Pamela, one a paperback costing $7.95, the other a hardcover costing
$15.50. These two fields are of a second record type, and are assigned to a descendant
segment in the Master File.

Finally, every copy of the book in the library has its own identifying serial number, which is
described in a field of record type S. In the Master File, this information is assigned to a
segment that is a child of the segment containing the binding and price information.

Use the following Master File to describe this data source:

FILENAME = LIBRARY2, SUFFIX = FIX,$
 SEGNAME = PUBINFO, SEGTYPE = S0,$
  FIELDNAME = RECTYPE  ,ALIAS = P     ,USAGE = A1    ,ACTUAL = A1  ,$
  FIELDNAME = PUBNO    ,ALIAS = PN    ,USAGE = A10   ,ACTUAL = A10 ,$
  FIELDNAME = AUTHOR   ,ALIAS = AT    ,USAGE = A25   ,ACTUAL = A25 ,$
  FIELDNAME = TITLE    ,ALIAS = TL    ,USAGE = A50   ,ACTUAL = A50 ,$
 SEGNAME = SYNOPSIS, PARENT = PUBINFO,  OCCURS = VARIABLE, SEGTYPE = S0,$
  FIELDNAME = PLOTLINE ,ALIAS = PLOTL ,USAGE = A10   ,ACTUAL = A10 ,$
 SEGNAME = BOOKINFO, PARENT = PUBINFO,  SEGTYPE = S0,$
  FIELDNAME = RECTYPE  ,ALIAS = B     ,USAGE = A1    ,ACTUAL = A1  ,$
  FIELDNAME = BINDING  ,ALIAS = BI    ,USAGE = A1    ,ACTUAL = A1  ,$
  FIELDNAME = PRICE    ,ALIAS = PR    ,USAGE = D8.2N ,ACTUAL = D8  ,$
 SEGNAME = SERIANO,  PARENT = BOOKINFO, SEGTYPE = S0,$
  FIELDNAME = RECTYPE  ,ALIAS = S     ,USAGE = A1    ,ACTUAL = A1  ,$
  FIELDNAME = SERIAL   ,ALIAS = SN    ,USAGE = A15   ,ACTUAL = A15 ,$

Note that each segment, except OCCURS, contains a field named RECTYPE and that the ALIAS
for the field contains a unique value for each segment (P, B, and S). If there is a record in this
data source with a RECTYPE other than P, B, or S, the record is ignored. The RECTYPE field
must fall in the same physical location in each record.

Ordering of Records in the Data Source

Physical order determines parent/child relationships in sequential records. Every parent record
does not need descendants. Specify how you want data in missing segment instances handled
in your reports by using the SET command to change the ALL parameter. The SET command is
described in the Developing Reporting Applications manual.

Describing Data With TIBCO WebFOCUS® Language

 261

Describing Multiple Record Types

In the example in Describing Positionally Related Records on page 260, if the first record in the
data source is not a PUBINFO record, the record is considered to be a child without a parent.
Any information allotted to the SYNOPSIS segment appears in the PUBINFO record. The next
record may be a BOOKINFO or even another PUBINFO (in which case the first PUBINFO is
assumed to have no descendants). Any SERIANO records are assumed to be descendants of
the previous BOOKINFO record. If a SERIANO record follows a PUBINFO record with no
intervening BOOKINFO, it is treated as if it has no parent.

Example:

Describing VSAM Positionally Related Records

Consider the following VSAM data source that contains three types of records. The ROOT
records have a key that consists of the publisher number, PUBNO. The BOOKINFO segment
has a key that consists of that same publisher number, plus a hard-cover or soft-cover
indicator, BINDING. The SERIANO segment key consists of the first two elements, plus a
record type field, RECTYPE.

FILENAME = LIBRARY6, SUFFIX = VSAM,$
 SEGNAME = ROOT, SEGTYPE = S0,$
  GROUP=PUBKEY        ,ALIAS=KEY   ,USAGE=A10   ,ACTUAL=A10  ,$
   FIELDNAME=PUBNO    ,ALIAS=PN    ,USAGE=A10   ,ACTUAL=A10  ,$
  FIELDNAME=FILLER    ,ALIAS=      ,USAGE=A1    ,ACTUAL=A1   ,$
  FIELDNAME=RECTYPE   ,ALIAS=1     ,USAGE=A1    ,ACTUAL=A1   ,$
  FIELDNAME=AUTHOR    ,ALIAS=AT    ,USAGE=A25   ,ACTUAL=A25  ,$
  FIELDNAME=TITLE     ,ALIAS=TL    ,USAGE=A50   ,ACTUAL=A50  ,$
 SEGNAME=BOOKINFO,PARENT=ROOT,   SEGTYPE=S0,$
  GROUP=BOINKEY       ,ALIAS=KEY   ,USAGE=A11   ,ACTUAL=A11  ,$
   FIELDNAME=PUBNO1   ,ALIAS=P1    ,USAGE=A10   ,ACTUAL=A10  ,$
   FIELDNAME=BINDING  ,ALIAS=BI    ,USAGE=A1    ,ACTUAL=A1   ,$
  FIELDNAME=RECTYPE   ,ALIAS=2     ,USAGE=A1    ,ACTUAL=A1   ,$
  FIELDNAME=PRICE     ,ALIAS=PR    ,USAGE=D8.2N ,ACTUAL=D8   ,$
 SEGNAME=SERIANO, PARENT=BOOKINFO,SEGTYPE=S0,$
  GROUP=SERIKEY       ,ALIAS=KEY   ,USAGE=A12   ,ACTUAL=A12  ,$
   FIELDNAME=PUBNO2   ,ALIAS=P2    ,USAGE=A10   ,ACTUAL=A10  ,$
   FIELDNAME=BINDING1 ,ALIAS=B1    ,USAGE=A1    ,ACTUAL=A1   ,$
   FIELDNAME=RECTYPE  ,ALIAS=3     ,USAGE=A1    ,ACTUAL=A1   ,$
  FIELDNAME=SERIAL    ,ALIAS=SN    ,USAGE=A15   ,ACTUAL=A15  ,$
 SEGNAME=SYNOPSIS,PARENT=ROOT,    SEGTYPE=S0, OCCURS=VARIABLE,$
  FIELDNAME=PLOTLINE  ,ALIAS=PLOTL ,USAGE=A10   ,ACTUAL=A10  ,$

Notice that the length of the key fields specified in the USAGE and ACTUAL attributes of a
GROUP declaration is the length of the key fields from the parent segments, plus the length of
the added field of the child segment (RECTYPE field). In the example above, the length of the
GROUP key SERIKEY equals the length of PUBNO2 and BINDING1, the group key from the
parent segment, plus the length of RECTYPE, the field added to the group key in the child
segment. The length of the key increases as you traverse the structure.

Note: Each segment key describes as much of the true key as needed to find the next
instance of that segment.

262

5. Describing a Sequential, VSAM, or ISAM Data Source

In the sample data source, the repetition of the publisher number as PUBNO1 and PUBNO2 in
the descendant segments interrelates the three types of records.

The data source can be diagrammed as the following structure:

A typical query may request information on price and call numbers for a specific publisher
number:

PRINT PRICE AND SERIAL BY PUBNO
IF PUBNO EQ 1234567890 OR 9876054321

Since PUBNO is part of the key, retrieval can occur quickly, and the processing continues. To
further speed retrieval, add search criteria based on the BINDING field, which is also part of
the key.

Describing Data With TIBCO WebFOCUS® Language

 263

Describing Multiple Record Types

Describing Unrelated Records

Some VSAM and ISAM data sources do not have records that are related to one another. That
is, the VSAM or ISAM key of one record type is independent of the keys of other record types.
To describe data sources with unrelated records, define a dummy root segment for the record
types. The following rules apply to the dummy root segment:

The name of the root segment must be DUMMY.

It must have only one field with a blank name and alias.

The USAGE and ACTUAL attributes must both be A1.

All other non-repeating segments must point to the dummy root as their parent. Except for the
root, all non-repeating segments must have a RECTYPE and a PARENT attribute and describe
the full VSAM/ISAM key. If the data source does not have a key, the group should not be
described. RECTYPEs may be anywhere in the record.

Example:

Describing Unrelated Records Using a Dummy Root Segment

The library data source has three types of records: book information, magazine information,
and newspaper information. Since these three record types have nothing in common, they
cannot be described as parent records followed by detail records.

The data source can look like this:

A structure such as the following can also describe this data source:

264

5. Describing a Sequential, VSAM, or ISAM Data Source

The Master File for the structure in this example is:

FILENAME = LIBRARY3, SUFFIX = FIX,$
 SEGMENT = DUMMY, SEGTYPE = S0,$
  FIELDNAME=           ,ALIAS=     ,USAGE = A1    ,ACTUAL = A1   ,$
 SEGMENT = BOOK, PARENT = DUMMY, SEGTYPE = S0,$
  FIELDNAME = RECTYPE  ,ALIAS = B  ,USAGE = A1    ,ACTUAL = A1   ,$
  FIELDNAME = PUBNO    ,ALIAS = PN ,USAGE = A10   ,ACTUAL = A10  ,$
  FIELDNAME = AUTHOR   ,ALIAS = AT ,USAGE = A25   ,ACTUAL = A25  ,$
  FIELDNAME = TITLE    ,ALIAS = TL ,USAGE = A50   ,ACTUAL = A50  ,$
  FIELDNAME = BINDING  ,ALIAS = BI ,USAGE = A1    ,ACTUAL = A1   ,$
  FIELDNAME = PRICE    ,ALIAS = PR ,USAGE = D8.2N ,ACTUAL = D8   ,$
  FIELDNAME = SERIAL   ,ALIAS = SN ,USAGE = A15   ,ACTUAL = A15  ,$
  FIELDNAME = SYNOPSIS ,ALIAS = SY ,USAGE = A150  ,ACTUAL = A150 ,$
 SEGMENT = MAGAZINE, PARENT = DUMMY, SEGTYPE = S0,$
  FIELDNAME = RECTYPE  ,ALIAS = M  ,USAGE = A1    ,ACTUAL = A1   ,$
  FIELDNAME = PER_NO   ,ALIAS = PN ,USAGE = A10   ,ACTUAL = A10  ,$
  FIELDNAME = PER_NAME ,ALIAS = NA ,USAGE = A50   ,ACTUAL = A50  ,$
  FIELDNAME = VOL_NO   ,ALIAS = VN ,USAGE = I2    ,ACTUAL = I2   ,$
  FIELDNAME = ISSUE_NO ,ALIAS = IN ,USAGE = I2    ,ACTUAL = I2   ,$
  FIELDNAME = PER_DATE ,ALIAS = DT ,USAGE = I6MDY ,ACTUAL = I6   ,$
 SEGMENT = NEWSPAP, PARENT = DUMMY, SEGTYPE = S0,$
  FIELDNAME = RECTYPE  ,ALIAS = N  ,USAGE = A1    ,ACTUAL = A1   ,$
  FIELDNAME = NEW_NAME ,ALIAS = NN ,USAGE = A50   ,ACTUAL = A50  ,$
  FIELDNAME = NEW_DATE ,ALIAS = ND ,USAGE = I6MDY ,ACTUAL = I6   ,$
  FIELDNAME = NVOL_NO  ,ALIAS = NV ,USAGE = I2    ,ACTUAL = I2   ,$
  FIELDNAME = ISSUE    ,ALIAS = NI ,USAGE = I2    ,ACTUAL = I2   ,$

Example:

Describing a VSAM Data Source With Unrelated Records

Consider another VSAM data source containing information on the library. This data source has
three types of records: book information, magazine information, and newspaper information.

There are two possible structures:

The RECTYPE is the beginning of the key. The key structure is:

Book Code

Magazine Code

Newspaper Code

RECTYPE B

RECTYPE M

RECTYPE N

The sequence of records is:

Book

Book

Describing Data With TIBCO WebFOCUS® Language

 265

Describing Multiple Record Types

Magazine

Magazine

Newspaper

Newspaper

Note the difference between the use of the RECTYPE here and its use when the records are
positionally related. In this case, the codes are unrelated and the database designer has
chosen to accumulate the records by type first (all the book information together, all the
magazine information together, and all the newspaper information together), so the RECTYPE
may be the initial part of the key.

The RECTYPE is not in the beginning of the key or is outside of the key.

The key structure is:

Book Code

Magazine Code

Newspaper Code

The sequence of record types in the data source can be arbitrary.

Both types of file structure can be represented by the following:

266

Example:

Describing a Key and a Record Type for a VSAM Data Source With Unrelated Records

5. Describing a Sequential, VSAM, or ISAM Data Source

FILE=LIBRARY7, SUFFIX=VSAM,$
 SEGMENT=DUMMY,$
  FIELDNAME=         ,ALIAS=    ,USAGE=A1    ,ACTUAL=A1   ,$
 SEGMENT=BOOK,     PARENT=DUMMY,SEGTYPE=S0,$
  GROUP=BOOKKEY      ,ALIAS=KEY ,USAGE=A11   ,ACTUAL=A11  ,$
   FIELDNAME=PUBNO   ,ALIAS=PN  ,USAGE=A3    ,ACTUAL=A3   ,$
   FIELDNAME=AUTHNO  ,ALIAS=AN  ,USAGE=A3    ,ACTUAL=A3   ,$
   FIELDNAME=TITLNO  ,ALIAS=TN  ,USAGE=A4    ,ACTUAL=A4   ,$
   FIELDNAME=RECTYPE ,ALIAS=B   ,USAGE=A1    ,ACTUAL=A1   ,$
  FIELDNAME=AUTHOR   ,ALIAS=AT  ,USAGE=A25   ,ACTUAL=A25  ,$
  FIELDNAME=TITLE    ,ALIAS=TL  ,USAGE=A50   ,ACTUAL=A50  ,$
  FIELDNAME=BINDING  ,ALIAS=BI  ,USAGE=A1    ,ACTUAL=A1   ,$
  FIELDNAME=PRICE    ,ALIAS=PR  ,USAGE=D8.2N ,ACTUAL=D8   ,$
  FIELDNAME=SERIAL   ,ALIAS=SN  ,USAGE=A15   ,ACTUAL=A15  ,$
  FIELDNAME=SYNOPSIS ,ALIAS=SY  ,USAGE=A150  ,ACTUAL=A150 ,$
 SEGMENT=MAGAZINE, PARENT=DUMMY, SEGTYPE=S0,$
  GROUP=MAGKEY       ,ALIAS=KEY ,USAGE=A11   ,ACTUAL=A11  ,$
   FIELDNAME=VOLNO   ,ALIAS=VN  ,USAGE=A2    ,ACTUAL=A2   ,$
   FIELDNAME=ISSUNO  ,ALIAS=IN  ,USAGE=A2    ,ACTUAL=A2   ,$
   FIELDNAME=PERDAT  ,ALIAS=DT  ,USAGE=A6    ,ACTUAL=A6   ,$
   FIELDNAME=RECTYPE ,ALIAS=M   ,USAGE=A1    ,ACTUAL=A1   ,$
  FIELDNAME=PER_NAME ,ALIAS=PRN ,USAGE=A50   ,ACTUAL=A50  ,$
 SEGMENT=NEWSPAP,  PARENT=DUMMY, SEGTYPE=S0,$
  GROUP=NEWSKEY      ,ALIAS=KEY ,USAGE=A11   ,ACTUAL=A11  ,$
   FIELDNAME=NEWDAT  ,ALIAS=ND  ,USAGE=A6    ,ACTUAL=A6   ,$
   FIELDNAME=NVOLNO  ,ALIAS=NV  ,USAGE=A2    ,ACTUAL=A2   ,$
   FIELDNAME=NISSUE  ,ALIAS=NI  ,USAGE=A2    ,ACTUAL=A2   ,$
   FIELDNAME=RECTYPE ,ALIAS=N   ,USAGE=A1    ,ACTUAL=A1   ,$
  FIELDNAME=NEWNAME  ,ALIAS=NN  ,USAGE=A50   ,ACTUAL=A50  ,$

Using a Generalized Record Type

If your fixed-format sequential, VSAM, or ISAM data source has multiple record types that
share the same layout, you can specify a single generalized segment that describes all record
types that have the common layout. By using a generalized segment (also known as a
generalized RECTYPE) instead of one segment per record type, you reduce the number of
segments you need to describe in the Master File.

When using a generalized segment, you identify RECTYPE values using the ACCEPT attribute.
You can assign any value to the ALIAS attribute.

Describing Data With TIBCO WebFOCUS® Language

 267

Describing Multiple Record Types

Syntax:

How to Specify a Generalized Record Type

FIELDNAME = RECTYPE, ALIAS = alias, USAGE = format, ACTUAL = format,
ACCEPT = {list|range} ,$

where:

RECTYPE

Is the required field name.

Note: Since the field name, RECTYPE, may not be unique across segments, you should not
use it in this way unless you qualify it. An alias is not required. You may leave it blank.

alias

Is any valid alias specification. You can specify a unique name as the alias value for the
RECTYPE field only if you use the ACCEPT attribute. The alias can then be used in a TABLE
request as a display field, a sort field, or in selection tests using either WHERE or IF.

list

Is a list of one or more lines of specific RECTYPE values for records that have the same
segment layout. The maximum number of characters allowed in the list is 255. Each item
in the list must be separated by either a blank or the keyword OR. If the list contains
embedded blanks or commas, it must be enclosed within single quotation marks. The list
may contain a single RECTYPE value. For example:

FIELDNAME = RECTYPE, ALIAS = TYPEABC, USAGE = A1,ACTUAL = A1,
ACCEPT = A OR B OR C, $

range

Is a range of one or more lines of RECTYPE values for records that have the same
segment layout. The maximum number of characters allowed in the range is 255. If the
range contains embedded blanks or commas, it must be enclosed within single quotation
marks.

To specify a range of values, include the lowest value, the keyword TO, and the highest
value, in that order. For example:

FIELDNAME = RECTYPE, ALIAS = ACCTREC, USAGE = P3,ACTUAL = P2,
ACCEPT = 100 TO 200, $

268

Example:

Using a Generalized Record Type

5. Describing a Sequential, VSAM, or ISAM Data Source

To illustrate the use of the generalized record type in a VSAM Master File, consider the
following record layouts in the DOC data source. Record type DN is the root segment and
contains the document number and title. Record types M, I, and C contain information about
manuals, installation guides, and course guides, respectively. Notice that record types M and I
have the same layout.

Record type DN:

---KEY---
+----------------------------------------------------------------------+
DOCID   FILLER            RECTYPE     TITLE
+----------------------------------------------------------------------+

Record type M:

--------KEY--------
+----------------------------------------------------------------------+
MDOCID   MDATE            RECTYPE     MRELEASE         MPAGES     FILLER
+----------------------------------------------------------------------+

Record type I:

--------KEY--------
+----------------------------------------------------------------------+
IDOCID   IDATE            RECTYPE     IRELEASE         IPAGES     FILLER
+----------------------------------------------------------------------+

Record type C:

--------KEY--------
+----------------------------------------------------------------------+
CRSEDOC   CDATE           RECTYPE     COURSENUM  LEVEL  CPAGES    FILLER
+----------------------------------------------------------------------+

Without the ACCEPT attribute, each of the four record types must be described as separate
segments in the Master File. A unique set of field names must be provided for record type M
and record type I, although they have the same layout.

The generalized RECTYPE capability enables you to code just one set of field names that
applies to the record layout for both record type M and I. The ACCEPT attribute can be used for
any RECTYPE specification, even when there is only one acceptable value.

Describing Data With TIBCO WebFOCUS® Language

 269

Describing Multiple Record Types

FILENAME=DOC2, SUFFIX=VSAM,$
SEGNAME=ROOT, SEGTYPE=SO,$
 GROUP=DOCNUM,    ALIAS=KEY,       A5,  A5,  $
  FIELD=DOCID,    ALIAS=SEQNUM,    A5,  A5,  $
 FIELD=FILLER,    ALIAS,=          A5,  A5,  $
 FIELD=RECTYPE,   ALIAS=DOCRECORD, A3,  A3,  ACCEPT = DN,$
 FIELD=TITLE,     ALIAS=,          A18, A18, $
SEGNAME=MANUALS, PARENT=ROOT, SEGTYPE=SO,$
 GROUP=MDOCNUM,   ALIAS=KEY, A10, A10,$
  FIELD=MDOCID,   ALIAS=MSEQNUM,   A5,  A5,  $
  FIELD=MDATE,    ALIAS=MPUBDATE,  A5,  A5,  $
 FIELD=RECTYPE,   ALIAS=MANUAL,    A3,  A3,  ACCEPT = M OR I,$
 FIELD=MRELEASE,  ALIAS=,          A7,  A7,  $
 FIELD=MPAGES,    ALIAS=,          I5,  A5,  $
 FIELD=FILLER,    ALIAS=,          A6,  A6,  $
SEGNAME=COURSES, PARENT=ROOT, SEGTYPE=SO,$
 GROUP=CRSEDOC,   ALIAS=KEY, A10, A10,$
  FIELD=CDOCID,   ALIAS=CSEQNUM,   A5,  A5,  $
  FIELD=CDATE,    ALIAS=CPUBDATE,  A5,  A5,  $
 FIELD=RECTYPE,   ALIAS=COURSE,    A3,  A3,  ACCEPT = C,$
 FIELD=COURSENUM, ALIAS=CNUM,      A4,  A4,  $
 FIELD=LEVEL,     ALIAS=,          A2,  A2,  $
 FIELD=CPAGES,    ALIAS=,          I5,  A5,  $
 FIELD=FILLER,    ALIAS=,          A7,  A7,  $

Using an ALIAS in a Report Request

You can include an alias for the RECTYPE field if you use the ACCEPT attribute to specify one
or more RECTYPE values in the Master File. This enables you to use the alias in a report
request as a display field, as a sort field, or in selection tests using either WHERE or IF.

270

5. Describing a Sequential, VSAM, or ISAM Data Source

Example:

Using a RECTYPE Value in a Display Command

Display the RECTYPE values by including the alias as a display field. In this example, the alias
MANUAL displays the RECTYPE values M and I:

TABLE FILE DOC
PRINT MANUAL MRELEASE MPAGES
BY DOCID BY TITLE BY MDATE
END

The output is:

PAGE 1

DOCID    TITLE                MDATE   RECTYPE   MRELEASE   MPAGES
-----    -----                -----   -------   --------   ------
40001    FOCUS USERS MANUAL   8601    M         5.0        1800
                              8708    M         5.5        2000
40057    MVS INSTALL GUIDE    8806    I         5.5.3        66
                              8808    I         5.5.4        66
40114    zOS INSTALL GUIDE    8806    I         5.5.3        58
                              8808    I         5.5.4        58

Example:

Using a RECTYPE Value in a WHERE Test

You can use the alias in a WHERE test to display a subset of records:

TABLE FILE DOC
PRINT MANUAL MRELEASE MPAGES
BY DOCID BY TITLE BY MDATE
WHERE MANUAL EQ 'I'
END

The output is:

PAGE 1

DOCID    TITLE                MDATE   RECTYPE   MRELEASE   MPAGES
-----    -----                -----   -------   --------   ------
40057    MVS INSTALL  GUIDE   8806    I         5.5.3          66
                              8808    I         5.5.4          66
40114    zOS INSTALL GUIDE    8806    I         5.5.3          58
                              8808    I         5.5.4          58

Combining Multiply Occurring Fields and Multiple Record Types

You can have two types of descendant segments in a single fixed-format sequential, VSAM, or
ISAM data source:

Descendant segments consisting of multiply occurring fields.

Additional descendant segments consisting of multiple record types.

Describing Data With TIBCO WebFOCUS® Language

 271



Combining Multiply Occurring Fields and Multiple Record Types

Describing a Multiply Occurring Field and Multiple Record Types

In the data structure shown below, the first record (of type 01) contains several different
sequences of repeating fields, all of which must be described as descendant segments with
an OCCURS attribute. The data source also contains two separate records, of types 02 and
03, which contain information that is related to that in record type 01.

The relationship between the records of various types is expressed as parent-child
relationships. The children that contain record types 02 and 03 do not have an OCCURS
attribute. They are distinguished from their parent by the field declaration where
field=RECTYPE.

The description for this data source is:

FILENAME = EXAMPLE1, SUFFIX = FIX,$
 SEGNAME = A, SEGTYPE=S0,$
  FIELDNAME = RECTYPE   ,ALIAS = 01   ,USAGE = A2   ,ACTUAL = A2 ,$
  FIELDNAME = T1        ,ALIAS =      ,USAGE = A2   ,ACTUAL = A1 ,$
  FIELDNAME = N1        ,ALIAS =      ,USAGE = A1   ,ACTUAL = A1 ,$
 SEGNAME = B, PARENT = A, OCCURS = VARIABLE, SEGTYPE=S0,$
  FIELDNAME = B1        ,ALIAS =      ,USAGE = I2   ,ACTUAL = I2 ,$
  FIELDNAME = B2        ,ALIAS =      ,USAGE = I2   ,ACTUAL = I2 ,$
 SEGNAME = C, PARENT = B, OCCURS = B1, SEGTYPE=S0,$
  FIELDNAME = C1        ,ALIAS =      ,USAGE = A1   ,ACTUAL = A1 ,$
 SEGNAME = D, PARENT = B, OCCURS = 7,  SEGTYPE=S0,$
  FIELDNAME = D1        ,ALIAS =      ,USAGE = A1   ,ACTUAL = A1 ,$
 SEGNAME = E, PARENT = A, SEGTYPE=S0,$
  FIELDNAME = RECTYPE   ,ALIAS = 02   ,USAGE = A2   ,ACTUAL = A2 ,$
  FIELDNAME = E1        ,ALIAS =      ,USAGE = A1   ,ACTUAL = A1 ,$
 SEGNAME = F, PARENT = E, SEGTYPE=S0,$
  FIELDNAME = RECTYPE   ,ALIAS = 03   ,USAGE = A2   ,ACTUAL = A2 ,$
  FIELDNAME = F1        ,ALIAS =      ,USAGE = A1   ,ACTUAL = A1 ,$

272

5. Describing a Sequential, VSAM, or ISAM Data Source

It produces the following data structure:

Segments A, B, C, and D all belong to the same record type. Segments E and F each are
stored as separate record types.

Note:

Segments A, E, and F are different records that are related through their record types. The
record type attribute consists of certain prescribed values, and is stored in a fixed location
in the records. Records are expected to be retrieved in a given order. If the first record does
not have a RECTYPE of 01, the record is considered to be a child without a parent. The next
record can have a RECTYPE of either 01 (in which case, the first record is considered to
have no descendants except the OCCURS descendants) or 02. A record with a RECTYPE of
03 can follow only a record with a RECTYPE of 02 (its parent) or another 03.

The OCCURS descendants all belong to the record whose RECTYPE is 01. (This is not a
necessary condition. Records of any type can have OCCURS descendants.) Note that the
OCCURS=VARIABLE segment, Segment B, is the right-most segment within its own record
type. If you look at the data structure, the pattern that makes up Segment B and its
descendants (the repetition of fields B1, B2, C1, and D1) extends from the first mention of
fields B1 and B2 to the end of the record.

Describing Data With TIBCO WebFOCUS® Language

 273

Combining Multiply Occurring Fields and Multiple Record Types

Although fields C1 and D1 appear in separate segments, they are actually part of the
repeating pattern that makes up the OCCURS=VARIABLE segment. Since they occur
multiple times within Segment B, they are each assigned to their own descendant segment.
The number of times field C1 occurs depends on the value of field B2. In the example, the
first value of field B2 is 3. The second, 2. Field D1 occurs a fixed number of times, 7.

Describing a VSAM Repeating Group With RECTYPEs

Suppose you want to describe a data source that, schematically, looks like this:

A     RECTYPE  B C    RECTYPE   B C

A     RECTYPE  D      RECTYPE   D

You must describe three segments in your Master File, with A as the root segment, and
segments for B, C, and D as two descendant OCCURS segments for A.

The following diagram illustrates these segments.

Each of the two descendant OCCURS segments in this example depends on the RECTYPE
indicator that appears for each occurrence.

All the rules of syntax for using RECTYPE fields and OCCURS segments also apply to
RECTYPEs within OCCURS segments.

Since each OCCURS segment depends on the RECTYPE indicator for its evaluation, the
RECTYPE must appear at the start of the OCCURS segment. This enables you to describe
complex data sources, including those with nested and parallel repeating groups that depend
on RECTYPEs.

274

5. Describing a Sequential, VSAM, or ISAM Data Source

Example:

Describing a VSAM Repeating Group With RECTYPEs

In this example, B/C, and D represent a nested repeating group, and E represents a parallel
repeating group.

A

RECTYPE B C

RECTYPE D

RECTYPE E

RECTYPE E

FILENAME=SAMPLE,SUFFIX=VSAM,$
 SEGNAME=ROOT,SEGTYPE=S0,$
  GROUP=GRPKEY      ,ALIAS=KEY ,USAGE=A8 ,ACTUAL=A8 ,$
   FIELD=FLD000     ,E00       ,A08      ,A08       ,$
   FIELD=A_DATA     ,E01       ,A02      ,A02       ,$
 SEGNAME=SEG001,PARENT=ROOT,OCCURS=VARIABLE,SEGTYPE=S0  ,$
  FIELD=RECTYPE     ,A01       ,A01      ,ACCEPT=B OR C ,$
  FIELD=B_OR_C_DATA ,E02       ,A08      ,A08       ,$
 SEGNAME=SEG002,PARENT=SEG001,OCCURS=VARIABLE,SEGTYPE=S0,$
  FIELD=RECTYPE     ,D         ,A01      ,A01       ,$
  FIELD=D_DATA      ,E03       ,A07      ,A07       ,$
 SEGNAME=SEG003,PARENT=ROOT,OCCURS=VARIABLE,SEGTYPE=S0  ,$
  FIELD=RECTYPE     ,E         ,A01      ,A01       ,$
  FIELD=E_DATA      ,E04       ,A06      ,A06       ,$

Describing a Repeating Group Using MAPFIELD

In another combination of record indicator and OCCURS, a record contains a record indicator
that is followed by a repeating group. In this case, the record indicator is in the fixed portion of
the record, not in each occurrence. Schematically, the record appears like this:

The first record contains header information, values for A and B, followed by an OCCURS
segment of C and D that was identified by its preceding record indicator. The second record
has a different record indicator and contains a different repeating group, this time for E.

Describing Data With TIBCO WebFOCUS® Language

 275

Combining Multiply Occurring Fields and Multiple Record Types

The following diagram illustrates this relationship:

Since the OCCURS segments are identified by the record indicator rather than the parentA/B
segment, you must use the keyword MAPFIELD. MAPFIELD identifies a field in the same way as
RECTYPE, but since each OCCURS segment has its own value for MAPFIELD, the value of
MAPFIELD is associated with each OCCURS segment by means of a complementary field
named MAPVALUE.

The following diagram illustrates this relationship:

MAPFIELD is assigned as the ALIAS of the field that is the record indicator. It may have any
name.

276

5. Describing a Sequential, VSAM, or ISAM Data Source

Syntax:

How to Describe a Repeating Group With MAPFIELD

FIELD = name, ALIAS = MAPFIELD, USAGE = format, ACTUAL = format,$

where:

name

Is the name you choose to provide for this field.

ALIAS

MAPFIELD is assigned as the alias of the field that is the RECTYPE indicator.

USAGE

Follows the usual field format.

ACTUAL

Follows the usual field format.

The descendant segment values depend on the value of the MAPFIELD. They are described as
separate segments, one for each possible value of MAPFIELD, and all descending from the
segment that has the MAPFIELD. A special field, MAPVALUE, is described as the last field in
these descendant segments after the ORDER field, if one has been used. The actual
MAPFIELD value is supplied as the ALIAS of MAPVALUE.

Syntax:

How to Use MAPFIELD for a Descendant Repeating Segment in a Repeating Group

FIELD = MAPVALUE, ALIAS = alias, USAGE = format, ACTUAL = format,
ACCEPT = {list|range} ,$

where:

MAPVALUE

Indicates that the segment depends on a MAPFIELD in its parent segment.

alias

Is the primary MAPFIELD value, if an ACCEPT list is not specified. If there is an ACCEPT
list, this can be any value.

USAGE

Is the same format as the MAPFIELD format in the parent segment.

ACTUAL

Is the same format as the MAPFIELD format in the parent segment.

Describing Data With TIBCO WebFOCUS® Language

 277

Establishing VSAM Data and Index Buffers

list

Is the list of one or more lines of specified MAPFIELD values for records that have the
same segment layout. The maximum number of characters allowed in the list is 255. Each
item in the list must be separated by either a blank or the keyword OR. If the list contains
embedded blanks or commas, it must be enclosed within single quotation marks ('). The
list may contain a single MAPFIELD value.

For example:

FIELDNAME = MAPVALUE, ALIAS = A, USAGE = A1, ACTUAL = A1,
ACCEPT = A OR B OR C,$

range

Is a range of one or more lines of MAPFIELD values for records that have the same
segment layout. The maximum number of characters allowed in the range is 255. If the
range contains embedded blanks or commas, it must be enclosed in single quotation
marks (').

To specify a range of values, include the lowest value, the keyword TO, and the highest
value, in that order.

Example:

Using MAPFIELD and MAPVALUE

Using the sample data source at the beginning of this section, the Master File for this data
source looks like this:

FILENAME=EXAMPLE,SUFFIX=FIX,$
 SEGNAME=ROOT,SEGTYPE=S0,$
  FIELD =A,              ,A14   ,A14 ,$
  FIELD =B,              ,A10   ,A10 ,$
  FIELD =FLAG ,MAPFIELD  ,A01   ,A01 ,$
 SEGNAME=SEG001,PARENT=ROOT,OCCURS=VARIABLE,SEGTYPE=S0  ,$
  FIELD =C,              ,A05   ,A05 ,$
  FIELD =D,              ,A07   ,A07 ,$
  FIELD =MAPVALUE ,1     ,A01   ,A01 ,$
 SEGNAME=SEG002,PARENT=ROOT,OCCURS=VARIABLE,SEGTYPE=S0  ,$
  FIELD =E,              ,D12.2 ,D8  ,$
  FIELD =MAPVALUE ,2     ,A01   ,A01 ,$

Note: MAPFIELD can only exist on an OCCURS segment that has not been re-mapped. This
means that the segment definition cannot contain POSITION=fieldname.

MAPFIELD and MAPVALUE may be used with SUFFIX=FIX and SUFFIX=VSAM data sources.

Establishing VSAM Data and Index Buffers

Two SET commands make it possible to establish DATA and INDEX buffers for processing
VSAM data sources online.

278

5. Describing a Sequential, VSAM, or ISAM Data Source

The AMP subparameters BUFND and BUFNI enable z/OS batch users to enhance the I/O
efficiency of TABLE, TABLEF, MODIFY, and JOIN against VSAM data sources by holding
frequently used VSAM Control Intervals in memory, rather than on physical DASD. By reducing
the number of physical Input/Output operations, you may improve job throughput. In general,
BUFND (data buffers) increase the efficiency of physical sequential reads, whereas BUFNI
(index buffers) are most beneficial in JOIN or KEYED access operations.

Syntax:

How to Establish VSAM Data and Index Buffers

MVS VSAM SET BUFND {n|8}
MVS VSAM SET BUFNI {n|1}

where:

n

Is the number of data or index buffers. BUFND=8 and BUFNI=1 (eight data buffers and one
index buffer) are the default values.

Note: The AMODE setting controls whether the buffers are created above or below the line.
SET AMODE=31 places the buffers above the line. SET AMODE=24 places the buffers
below the line.

Reference: Determining How Many Buffers Are in Effect

MVS VSAM SET ?

Using a VSAM Alternate Index

VSAM key-sequenced data sources support the use of alternate key indexes (keys). A key-
sequenced VSAM data source consists of two components: an index component and a data
component. The data component contains the actual data records, while the index component
is the key used to locate the data records in the data source. Together, these components are
referred to as the base cluster.

An alternate index is a separate, additional index structure that enables you to access records
in a KSDS VSAM data source based on a key other than the data source primary key. For
instance, you may usually use a personnel data source sequenced by Social Security number,
but occasionally need to retrieve records sorted by job description. The job description field
might be described as an alternate index. An alternate index must be related to the base
cluster it describes by a path, which is stored in a separate data source.

The alternate index is a VSAM structure and is, consequently, created and maintained in the
VSAM environment. It can, however, be described in your Master File, so that you can take
advantage of the benefits of an alternate index.

Describing Data With TIBCO WebFOCUS® Language

 279

Using a VSAM Alternate Index

The primary benefit of these indexes is improved efficiency. You can use it as an alternate,
more efficient, retrieval sequence or take advantage of its potential indirectly, with screening
tests (IF...LT, IF...LE, IF...GT, IF...GE, IF...EQ, IF...FROM...TO, IF...IS), which are translated into
direct reads against the alternate index. You can also join data sources with the JOIN
command through this alternate index.

It is not necessary to identify the indexed view explicitly in order to take advantage of the
alternate index. An alternate index is automatically used when described in the Master File.

To take advantage of a specific alternate index during a TABLE request, provide a WHERE or IF
test on the alternative index field that meets the above criteria. For example:

TABLE FILE CUST
PRINT SSN
WHERE LNAME EQ 'SMITH'
END

As you see in the Master File in Describing a VSAM Alternate Index on page 281, the LNAME
field is defined as an alternate index field. The records in the data source are retrieved
according to their last names, and certain IF screens on the field LNAME result in direct reads.
Note that if the alternate index field name is omitted, the primary key (if there is any) is used
for a sequential or a direct read, and the alternate indexes are treated as regular fields.

Alternate indexes must be described in the Master File as fields with FIELDTYPE=I. The ALIAS
of the alternate index field must be the file name allocated to the corresponding path name.
Alternate indexes can be described as GROUPs if they consist of portions with dissimilar
formats. Remember that ALIAS=KEY must be used to describe the primary key.

Only one record type can be referred to in the request when using alternate indexes, but there
is no restriction on the number of OCCURS segments.

Note that the path name in the allocation is different from both the cluster name and the
alternate index name.

If you are not sure of the path names and alternate indexes associated with a given base
cluster, you can use the IDCAMS utility. (See the IBM manual entitled Using VSAM Commands
and Macros for details.)

280

5. Describing a Sequential, VSAM, or ISAM Data Source

Example:

Describing a VSAM Alternate Index

Consider the following:

FILENAME = CUST, SUFFIX = VSAM,$
 SEGNAME = ROOT, SEGTYPE = S0,$
  GROUP = G, ALIAS = KEY, A10, A10,$
   FIELD = SSN,   SSN, A10, A10,$
   FIELD = FNAME, DD1, A10, A10, FIELDTYPE=I,$
   FIELD = LNAME, DD2, A10, A10, FIELDTYPE=I,$

In this example, SSN is a primary key and FNAME and LNAME are alternate indexes. The path
data set must be allocated to the ddname specified in ALIAS= of your alternate index field. In
this Master File, ALIAS=DD1 and ALIAS=DD2 each have an allocation pointing to the path data
set. FNAME and LNAME must have INDEX=I or FIELDTYPE=I coded in the Master File. CUST
must be allocated to the base cluster.

Example:

Using IDCAMS

The following example demonstrates how to use IDCAMS to find the alternate index and path
names associated with a base cluster named CUST.DATA:

First, find the alternate index names (AIX) associated with the given cluster.

IDCAMS input:
 LISTCAT CLUSTER ENTRIES(CUST.DATA) ALL

IDCAMS output (fragments):
 CLUSTER -------- CUST.DATA
  ASSOCIATIONS
   AIX ---------- CUST.INDEX1
   AIX ---------- CUST.INDEX2

This gives you the names of the alternate indexes (AIX): CUST.INDEX1 and CUST.INDEX2.

Next, find the path names associated with the given AIX name:

IDCAMS input:
 LISTCAT AIX ENTRIES (CUST.INDEX1 CUST.INDEX2) ALL

IDCAMS output (fragments):
 AIX ---------CUST.INDEX1
  ASSOCIATIONS
   CLUSTER -- CUST.DATA
   PATH ------CUST.PATH1
 AIX ---------CUST.INDEX2
  ASSOCIATIONS
   CLUSTER -- CUST.DATA
   PATH ------CUST.PATH2

This gives you the path names: CUST.PATH1 and CUST.PATH2.

Describing Data With TIBCO WebFOCUS® Language

 281



Describing a Token-Delimited Data Source

This information, along with the TSO DDNAME command, may be used to ensure the proper
allocation of your alternate index.

Describing a Token-Delimited Data Source

You can read files in which fields are separated by any type of delimiter including commas,
tabs and other characters. Defining a Master File with the SUFFIX=DFIX attribute lets you
specify any combination of characters as the field delimiter. Delimiters may consist of printable
or non-printable characters, or any combination of printable and non-printable characters.

Two methods of describing delimited files are supported:

Placing delimiter information in the Master File.

Placing delimiter information in the Access File. This method also allows you to specify an
enclosure character for alphanumeric fields, preserve leading and trailing blank spaces in
alphanumeric data, and specify whether you want a header record in the file to contain
column titles for the fields in the file. In addition, you can create this type of delimited file
using the HOLD FORMAT DFIX command. For information on HOLD formats, see the
Creating Reports With WebFOCUS Language manual.

Note: SET HOLDLIST is not supported for delimited files.

Defining a Delimiter in the Master File

Delimiters in the Master File are defined using a special field named DELIMITER. The FILE
declaration must include the attribute SUFFIX=DFIX.

Syntax:

How to Define a File With Delimiters in the Master File

Describe the delimiter characters in a special field or group named DELIMITER. The delimiter
characters are specified in the ALIAS attribute of this special field or group.

To use a delimiter that consists of a single non-printable character or of one or more printable
characters, the delimiter is defined as a field with the following attributes:

FIELDNAME=DELIMITER, ALIAS=delimiter, USAGE=ufmt, ACTUAL=afmt ,$

To use a delimiter that consists of multiple non-printable characters or a combination of
printable and non-printable characters, the delimiter is defined as a group:

282

5. Describing a Sequential, VSAM, or ISAM Data Source

GROUP=DELIMITER,      ALIAS=          , USAGE=ufmtg, ACTUAL=afmtg ,$
 FIELDNAME=DELIMITER, ALIAS=delimiter1, USAGE=ufmt1, ACTUAL=afmt1 ,$
  .
  .
  .
 FIELDNAME=DELIMITER, ALIAS=delimitern, USAGE=ufmtn, ACTUAL=afmtn ,$

where:

DELIMITER

Indicates that the field or group is used as the delimiter in the data source.

delimiter

Identifies a delimiter, up to 30 characters long. For one or more printable characters, the
value consists of the actual characters. The delimiter must be enclosed in single quotation
marks if it includes characters used as delimiters in Master File syntax. For a non-printable
character, the value is the decimal equivalent of the EBCDIC or ASCII representation of the
character, depending on your operating environment.

ufmt, afmt

Are the USAGE and ACTUAL formats for the delimiter. Possible values are:

Type of delimiter

USAGE

ACTUAL

Printable characters

An where n is the
number of
characters

An where n is the
number of characters

Non-printable character such as Tab

I4

I1

Group (combination of printable and non-
printable characters, or multiple non-
printable characters)

Sum of the
individual USAGE
lengths

Sum of the individual
ACTUAL lengths

Reference: Usage Notes for a Token-Delimited File

If the delimiter is alphanumeric and the delimiter value contains special characters (those
used as delimiters in Master File syntax), it must be enclosed in single quotation marks.

If the data is numeric and has a zoned format (ACTUAL=Zn), the data must be unsigned
(cannot contain a positive or negative value).

Describing Data With TIBCO WebFOCUS® Language

 283

Describing a Token-Delimited Data Source

Numeric values may be used to represent any character, but are predominantly used for
non-printable characters such as Tab. The numeric values may differ between EBCDIC and
ASCII platforms.

A delimiter is needed to separate field values. A pair of delimiters denotes a missing or
default field value.

Trailing delimiters are not necessary except that all fields must be terminated with the
delimiter if the file has fixed length records in z/OS.

Only one delimiter field or group is permitted per Master File.

Token-delimited files support the RECTYPE, POSITION, and OCCURS attributes. For
information about RECTYPE, see Describing Multiple Record Types on page 257. For
information about OCCURS, see Describing a Multiply Occurring Field in a Fixed-Format,
VSAM, or ISAM Data Source on page 245.

Example:

Defining a Delimiter in the Master File

The following example shows a one-character alphanumeric delimiter:

FIELDNAME=DELIMITER, ALIAS=',' ,USAGE=A1, ACTUAL=A1  ,$

The following example shows a two-character alphanumeric delimiter:

FIELDNAME=DELIMITER, ALIAS=//  ,USAGE=A2, ACTUAL=A2  ,$

The following example shows how to use the Tab character as a delimiter:

FIELDNAME=DELIMITER, ALIAS=05  ,USAGE=I4, ACTUAL=I1  ,$

The following example shows how to use a blank character described as a numeric delimiter:

FIELDNAME=DELIMITER, ALIAS=64  ,USAGE=I4, ACTUAL=I1  ,$

The following example shows a group delimiter (Tab-slash-Tab combination):

GROUP=DELIMITER,  ALIAS=   ,USAGE=A9, ACTUAL=A3  ,$
 FIELDNAME=DEL1,  ALIAS=05 ,USAGE=I4, ACTUAL=I1  ,$
 FIELDNAME=DEL2,  ALIAS=/  ,USAGE=A1, ACTUAL=A1  ,$
 FIELDNAME=DEL3,  ALIAS=05 ,USAGE=I4, ACTUAL=I1  ,$

284

5. Describing a Sequential, VSAM, or ISAM Data Source

Example:

Separating Field Values for Missing Data

The following Master File shows the MISSING attribute specified for the CAR field:

FILE=DFIXF01  ,SUFFIX=DFIX
 SEGNAME=SEG1  ,SEGTYPE=S0
  FIELDNAME=COUNTRY   ,ALIAS=F1  ,USAGE=A10 ,ACTUAL=A10 ,$
  FIELDNAME=CAR       ,ALIAS=F2  ,USAGE=A16 ,ACTUAL=A16 ,MISSING=ON, $
  FIELDNAME=NUMBER    ,ALIAS=F3  ,USAGE=P10 ,ACTUAL=Z10 ,$
  FIELDNAME=DELIMITER ,ALIAS=',' ,USAGE=A1  ,ACTUAL=A1  ,$

In the source file, two consecutive comma delimiters indicate missing values for CAR:

GERMANY,VOLKSWAGEN,1111
GERMANY,BMW,
USA,CADILLAC,22222
USA,FORD
USA,,44444
JAPAN
ENGLAND,
FRANCE

The output is:

COUNTRY            CAR              NUMBER
-------            ---              ------
GERMANY            VOLKSWAGEN         1111
GERMANY            BMW                   0
USA                CADILLAC          22222
USA                FORD                  0
USA                .                 44444
JAPAN              .                     0
ENGLAND                                  0
FRANCE             .                     0

Defining a Delimiter in the Access File

The Master File has the standard attributes for any sequential file. The SUFFIX value is DFIX.
All of the delimiter information is in the Access File.

In addition, you can use the HOLD FORMAT DFIX command to create this type of Master and
Access File for a token-delimited file. For information on HOLD formats, see the Creating
Reports With WebFOCUS Language manual.

Reference: Access File Attributes for a Delimited Sequential File

DELIMITER = delimiter [,ENCLOSURE = enclosure]
  [,HEADER = {YES|NO}] [,SKIP_ROWS = n] [,PRESERVESPACE={YES|NO}]
  [,RDELIMITER=rdelimiter], $

Describing Data With TIBCO WebFOCUS® Language

 285

Describing a Token-Delimited Data Source

where:

delimiter

Is the delimiter sequence consisting of up to 30 printable or non-printable non-null
characters. This represents character semantics. For example, if you are using DBCS
characters, the delimiter can be up to 60 bytes. For a non-printable character, enter the
hexadecimal value that represents the character. If you use a mixture of printable and non-
printable characters, you must enter them all as hexadecimal values. For printable
characters you can either use the characters themselves or their hexadecimal equivalents
(for example, the ampersand character may be interpreted as the beginning of a variable
name rather than as part of the delimiter). To create a tab-delimited file, you can specify
the delimiter value as TAB or as its hexadecimal equivalent (0x09 on ASCII platforms or
0x05 on EBCDIC platforms). To create a file delimited by a single quotation mark, you
must specify the single quotation mark delimiter value as its hexadecimal equivalent (0x27
on ASCII platforms or 0x7D on EBCDIC platforms), otherwise the request will not be parsed
correctly and will result in an unusable HOLD file.

Note that numeric digits and symbols used in numbers, such as a period (.), plus sign (+),
or minus sign (-) cannot be used in the delimiter sequence.

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
be interpreted as the beginning of a variable name rather than as part of the enclosure).

HEADER = {YES|NO}

Specifies whether to include a header record that contains the names of the fields in the
delimited sequential file generated by the request. NO is the default value.

SKIP_ROWS = n

Specifies the number of rows above the header row that should be ignored when creating
the synonym and reading the data.

286

5. Describing a Sequential, VSAM, or ISAM Data Source

PRESERVESPACE={YES|NO}

Specifies whether to retain leading and trailing blanks in alphanumeric data. YES
preserves leading and trailing blanks. NO only preserves leading and trailing blanks that
are included within the enclosure characters. NO is the default value.

Note: PRESERVESPACE is overridden by the ENCLOSURE option. Therefore, exclude the
enclosure option in order to have the PRESERVESPACE setting respected.

rdelimiter

Is the record delimiter sequence consisting of up to 30 printable or non-printable non-null
characters. (This represents character semantics. For example, if you are using DBCS
characters, the delimiter can be up to 60 bytes.) For a non-printable character, enter the
hexadecimal value that represents the character. If you use a mixture of printable and non-
printable characters, you must enter them all as hexadecimal values. For printable
characters you can either use the characters themselves or their hexadecimal equivalents
(for example, the ampersand character may be interpreted as the beginning of a variable
name rather than as part of the delimiter.) To use a tab character as the record delimiter,
you can specify the delimiter value as TAB or as its hexadecimal equivalent (0x09 on ASCII
platforms or 0x05 on EBCDIC platforms). The comma (,) is not supported as a record
delimiter.

Note that numeric digits and symbols used in numbers, such as a period (.), plus sign (+),
or minus sign (-) cannot be used in the delimiter sequence. When RDELIMITER is included,
the RECFM is UB.

Example: Master and Access File for a Pipe Delimited File

The pipe delimited file named PIPE1 contains the following data in which each data value is
delimited by a pipe character (|). Note that you can create a delimited file as output from a
request using the HOLD FORMAT DFIX command in a request:

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

Describing Data With TIBCO WebFOCUS® Language

 287

Describing a Token-Delimited Data Source

The PIPE1 Master File is:

FILENAME=PIPE1   , SUFFIX=DFIX    , $
  SEGMENT=PIPE1, SEGTYPE=S2, $
    FIELDNAME=REGION, ALIAS=E01, USAGE=A5, ACTUAL=A05, $
    FIELDNAME=YEAR, ALIAS=E02, USAGE=YY, ACTUAL=A04, $
    FIELDNAME=QUANTITY, ALIAS=E03, USAGE=I8C, ACTUAL=A08, $
    FIELDNAME=LINEPRICE, ALIAS=E04, USAGE=D12.2MC, ACTUAL=A12, $

The PIPE1 Access File is:

SEGNAME=PIPE1, DELIMITER=|, HEADER=NO, $

In the following version of the PIPE1 delimited file, each alphanumeric value is enclosed in
double quotation marks:

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

The Master File does not change, but the Access File now specifies the enclosure character:

SEGNAME=PIPE1, DELIMITER=|, ENCLOSURE=", $

In this version of the PIPE1 delimited file, the first record in the file specifies the name of each
field, and each alphanumeric value is enclosed in double quotation marks:

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

The Master File remains the same. The Access File now specifies that there is a header record
in the data file:

SEGNAME=PIPE1, DELIMITER=|, ENCLOSURE=", HEADER=YES, $

288

5. Describing a Sequential, VSAM, or ISAM Data Source

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

Describing Data With TIBCO WebFOCUS® Language

 289

Describing a Token-Delimited Data Source

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

290

5. Describing a Sequential, VSAM, or ISAM Data Source

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

In the following request against the GGSALES data source, the field delimiter is a comma, the
enclosure character is a single quotation mark, and the record delimiter consists of both
printable and non-printable characters, so it is specified as the following hexadecimal
sequence:

0x: character sequence identifying the delimiter as consisting of hexadecimal character
codes.

2C: hexadecimal value for comma (,).

Describing Data With TIBCO WebFOCUS® Language

 291

Describing a Token-Delimited Data Source

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
return and line space. A partial listing follows:

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

292

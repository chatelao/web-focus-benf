Chapter4

Describing an Individual Field

A field is the smallest meaningful element of data in a data source, but it can exhibit a
number of complex characteristics. Master File attributes are used to describe these
characteristics.

In this chapter:

Field Characteristics

Alternative Report Column Titles: TITLE

The Field Name: FIELDNAME

Documenting the Field: DESCRIPTION

The Field Synonym: ALIAS

Multilingual Metadata

The Displayed Data Type: USAGE

Describing a Virtual Field: DEFINE

The Stored Data Type: ACTUAL

Describing a Calculated Value: COMPUTE

Adding a Geographic Role for a Field

Describing a Filter: FILTER

Null or MISSING Values: MISSING

Describing a Sort Object: SORTOBJ

Describing an FML Hierarchy

Defining a Dimension: WITHIN

Validating Data: ACCEPT

Specifying Acceptable Values for a
Dimension

Calling a DEFINE FUNCTION in a Master
File

Using Date System Amper Variables in
Master File DEFINEs

Parameterizing Master and Access File
Values Using Variables

Converting Alphanumeric Dates to
WebFOCUS Dates

Field Characteristics

The Master File describes the following field characteristics:

The name of the field, as identified in the FIELDNAME attribute.

Describing Data With TIBCO WebFOCUS® Language

 103

The Field Name: FIELDNAME

Another name for the field, either its original name, as defined to its native data
management system, or (for some types of data sources) a synonym of your own choosing,
or (in some special cases) a pre-defined value that tells how to interpret the field, that you
can use as an alternative name in requests. This alternative name is defined by the ALIAS
attribute.

How the field stores and displays data, specified by the ACTUAL, USAGE, and MISSING
attributes.

The ACTUAL attribute describes the type and length of the data as it is actually stored in
the data source. For example, a field might be alphanumeric and 15 characters in length.
Note that FOCUS data sources do not use the ACTUAL attribute, and instead use the
USAGE attribute to describe the data as it is formatted. WebFOCUS handles the storage.

The USAGE attribute, also known by its alias, FORMAT, describes how a field is formatted
when it appears in reports. You can also specify edit options, such as date formats,
floating dollar signs, and zero suppression.

The MISSING attribute enables null values to be entered into and read from a field in data
sources that support null data, such as FOCUS data sources and most relational data
sources.

The option for a field to be virtual, rather than being stored in the data source, and have its
value derived from information already in the data source. Virtual fields are specified by the
DEFINE attribute.

Optional field documentation for the developer, contained in the DESCRIPTION attribute.

Acceptable data-entry values for the field, specified by the ACCEPT attribute.

An alternative report column title for the field, described by the TITLE attribute.

A 100-year window that assigns a century value to a two-digit year stored in the field. Two
attributes define this window: DEFCENT and YRTHRESH.

The Field Name: FIELDNAME

Identify a field using FIELDNAME, the first attribute specified in a field declaration in the
Master File. You can assign any name to a field, regardless of its name in its native data
source. Likewise, for FOCUS data sources, you can assign any name to a field in a new data
source.

104

4. Describing an Individual Field

When you generate a report, each column title in the report has the name of the field displayed
in that column as its default, so assigning meaningful field names helps readers of the report.
Alternatively, you can specify a different column title within a given report by using the AS
phrase in the report request, as described in the Creating Reports With WebFOCUS Language
manual, or a different default column title for all reports by using the TITLE attribute in the
Master File, as described in Alternative Report Column Titles: TITLE on page 191.

Syntax:

How to Identify the Field Name

FIELD[NAME] = field_name

where:

field_name

Is the name you are giving this field. It can be a maximum of 512 characters, in a single-
byte character set. If you are working in a Unicode environment, this length will be affected
by the number of bytes used to represent each character, as described in the chapter
named Unicode Support in the Server Administration manual. Some restrictions apply to
names longer than 12 characters, as described in Restrictions for Field Names on page
106. The name can include any combination of letters, digits, and underscores (_), and
must contain at least one letter. Other characters are not recommended, and may cause
problems in some operating environments or when resolving expressions.

It is recommended that you not use field names of the type Cn, En, and Xn (where n is any
sequence of one or two digits) because these can be used to refer to report columns,
HOLD file fields, and other special objects.

If you must use special characters because of a field report column title, consider using
the TITLE attribute in the Master File to specify the title, as described in Alternative Report
Column Titles: TITLE on page 191.

Reference: Usage Notes for FIELDNAME

Note the following rules when using FIELDNAME:

Alias. FIELDNAME has an alias of FIELD.

Changes. In a FOCUS data source, if the INDEX attribute has been set to I (that is, if an
index has been created for the field), you cannot change the field name without rebuilding
the data source. You may change the name in all other situations.

Describing Data With TIBCO WebFOCUS® Language

 105

The Field Name: FIELDNAME

Reference: Restrictions for Field Names

The following restrictions apply to field names and aliases longer than 12 characters:

You cannot use a field name longer than 12 characters to specify a cross-referenced field
in a JOIN command when the cross-referenced file is a FOCUS data source.

Indexed fields and text fields in FOCUS data sources cannot have field names longer than
12 characters. Indexed fields and text fields in XFOCUS data sources are not subject to this
12 character limitation. Long ALIAS names are supported for both types of data sources.

A field name specified in an alternate file view cannot be qualified.

The CHECK FILE command PICTURE and HOLD options display the first 11 characters of
long names within the resulting diagram or HOLD file. A caret (>) in the 12th position
indicates that the name is longer than the displayed portion.

?FF, ? HOLD, ? DEFINE

These display up to 31 characters of the name, and display a caret (>) in the 32nd
character to indicate a longer field name.

Using a Qualified Field Name

Requests can qualify all referenced field names and aliases with file and/or segment names, a
useful technique when duplicate field names exist across segments in a Master File or in
joined data sources.

The names of text fields and indexed fields in FOCUS Master Files are limited to 12
characters. Text fields and indexed fields in XFOCUS Master Files are not subject to this 12-
character limitation. However, the aliases for text and indexed fields may be up to 512
characters. Field names up to 512 characters appear as column titles in TABLE reports if there
is no TITLE attribute or AS phrase.

The default value for the SET FIELDNAME command, SET FIELDNAME=NEW, activates long and
qualified field names. The syntax is described in the Developing Reporting Applications manual.

Syntax:

How to Specify a Qualified Field Name in a Request

[filename.][segname.]fieldname

where:

filename

Is the name of the Master File or tag name. Tag names are used with the JOIN and
COMBINE commands.

106

4. Describing an Individual Field

segname

Is the name of the segment in which the field resides.

fieldname

Is the name of the field.

Example:

Qualifying a Field Name

The fully qualified name of the field EMP_ID in the EMPINFO segment of the EMPLOYEE data
source is:

EMPLOYEE.EMPINFO.EMP_ID

Syntax:

How to Change the Qualifying Character

SET QUALCHAR = qualcharacter

The period (.) is the default qualifying character. For further information about the SET
QUALCHAR command and valid qualifying characters (. : ! % | \ ), see the Developing Reporting
Applications manual.

Describing Data With TIBCO WebFOCUS® Language

 107

The Field Name: FIELDNAME

Using a Duplicate Field Name

Field names are considered duplicates when you can reference two or more fields with the
same field name or alias. Duplication may occur:

If a name appears multiple times within a Master File.

In a JOIN between two or more Master Files, or in a recursive JOIN.

If you issue a COMBINE and do not specify a prefix.

Duplicate fields (those having the same field name and alias) are not allowed in the same
segment. The second occurrence is never accessed, and the following message is generated
when you issue CHECK and CREATE FILE:

(FOC1829) WARNING. FIELDNAME IS NOT UNIQUE WITHIN A SEGMENT: fieldname

Duplicate field names may exist across segments in a Master File. To retrieve such a field, you
must qualify its name with the segment name in a request. If a field that appears multiple
times in a Master File is not qualified in a request, the first field encountered in the Master File
is the one retrieved.

Note: If a Master File includes duplicate field names for real fields and/or virtual fields, the
following logic is used when retrieving a field:

If only virtual fields are duplicated, the last virtual field is retrieved.

If only real fields are duplicated, the first real field is retrieved.

If a Master File has both a real field and one or more virtual fields with the same name, the
last virtual field is retrieved.

If a field defined outside of a Master File has the same name as a virtual or real field in a
Master File, the last field defined outside of the Master File is retrieved.

Reports can include qualified names as column titles. The SET QUALTITLES command,
discussed in the Developing Reporting Applications manual, determines whether reports display
qualified column titles for duplicate field names. With SET QUALTITLES=ON, they display
qualified column titles for duplicate field names even when the request itself does not specify
qualified names. The default value, OFF, disables qualified column titles.

Rules for Evaluating a Qualified Field Name

The following rules are used to evaluate qualified field names:

The maximum field name qualification is filename.segname.fieldname. For example:

108

4. Describing an Individual Field

TABLE FILE EMPLOYEE
PRINT EMPLOYEE.EMPINFO.EMP_ID
END

includes EMP_ID as a fully qualified field. The file name, EMPLOYEE, and the segment
name, EMPINFO, are the field qualifiers.

Qualifier names can also be duplicated. For example:

FILENAME=CAR, SUFFIX=FOC
  SEGNAME=ORIGIN, SEGTYPE=S1
      FIELDNAME=COUNTRY, COUNTRY, A10, $
  SEGNAME=COMP, SEGTYPE=S1, PARENT=ORIGIN
      FIELDNAME=CAR, CARS, A16, $
        .
        .
        .
TABLE FILE CAR
PRINT CAR.COMP.CAR
END

This request prints the field with alias CARS. Both the file name and field name are CAR.

A field name can be qualified with a single qualifier, either its file name or its segment
name. For example:

FILENAME=CAR, SUFFIX=FOC
   SEGNAME=ORIGIN, SEGTYPE=S1
      FIELDNAME=COUNTRY, COUNTRY, A10, $
   SEGNAME=COMP, SEGTYPE=S1, PARENT=ORIGIN
      FIELDNAME=CAR, CARS, A16, $
        .
        .
        .
TABLE FILE CAR
PRINT COMP.CAR AND CAR.CAR
END

This request prints the field with alias CARS twice.

When there is a single qualifier, segment name takes precedence over file name.
Therefore, if the file name and segment name are the same, the field qualified by the
segment name is retrieved.

Describing Data With TIBCO WebFOCUS® Language

 109

The Field Name: FIELDNAME

If a field name begins with characters that are the same as the name of a prefix operator, it
may be unclear whether a request is referencing that field name or a second field name
prefixed with the operator. The value of the first field is retrieved, not the value calculated
by applying the prefix operator to the second field. In the next example, there is a field
whose unqualified field name is CNT.COUNTRY and another whose field name is COUNTRY:

FILENAME=CAR, SUFFIX=FOC
   SEGNAME=ORIGIN, SEGTYPE=S1
      FIELDNAME=CNT.COUNTRY, ACNTRY, A10, $
      FIELDNAME=COUNTRY, BCNTRY, A10, $
TABLE FILE CAR
SUM CNT.COUNTRY
END

In this request, the string CNT.COUNTRY is interpreted as a reference to the field named
CNT.COUNTRY, not as a reference to the prefix operator CNT. applied to the field named
COUNTRY. Therefore, the request sums the field whose alias is ACNTRY. Although the field
name CNT.COUNTRY contains a period as one of its characters, it is an unqualified field
name. It is not a qualified name or a prefix operator acting on a field name, neither of
which is allowed in a Master File. The request does not count instances of the field whose
alias is BCNTRY.

If a Master File has either a file name or segment name that is the same as a prefix
operator, the value of the field within the segment is retrieved in requests, not the value
calculated by applying the prefix operator to the field.

For example:

FILENAME=CAR, SUFFIX=FOC
   SEGNAME=ORIGIN, SEGTYPE=S1
      FIELDNAME=COUNTRY, COUNTRY, A10, $
   SEGNAME=PCT, SEGTYPE=S1, PARENT=ORIGIN
      FIELDNAME=CAR, CARS, I2, $
 TABLE FILE CAR
SUM PCT.CAR PCT.PCT.CAR
BY COUNTRY
END

This request sums the field with alias CARS first, and then the percent of CARS by
COUNTRY.

110

4. Describing an Individual Field

When a qualified field name can be evaluated as a choice between two levels of
qualification, the field name with the higher level of qualification takes precedence.

In the following example, the choice is between an unqualified field name (the field named
ORIGIN.COUNTRY in the ORIGIN segment) and a field name with segment name
qualification (the field named COUNTRY in the ORIGIN segment). The field with segment
name qualification is retrieved:

FILENAME=CAR, SUFFIX=FOC
   SEGNAME=ORIGIN, SEGTYPE=S1
      FIELDNAME=ORIGIN.COUNTRY, OCNTRY, A10, $
      FIELDNAME=COUNTRY, CNTRY, A10, $
TABLE FILE CAR
PRINT ORIGIN.COUNTRY
END

This request prints the field with alias CNTRY. To retrieve the field with alias OCNTRY,
qualify its field name, ORIGIN.COUNTRY, with its segment name, ORIGIN:

PRINT ORIGIN.ORIGIN.COUNTRY

When a qualified field name can be evaluated as a choice between two field names with
the same level of qualification, the field with the shortest basic field name length is
retrieved. For example:

FILENAME=CAR, SUFFIX=FOC
   SEGNAME=CAR, SEGTYPE=S1
      FIELDNAME=CAR.CAR, CAR1, A10, $
   SEGNAME=CAR.CAR, SEGTYPE=S1, PARENT=CAR
      FIELDNAME=CAR, CAR2, A10, $
TABLE FILE CAR
PRINT CAR.CAR.CAR
END

In this example, it is unclear if you intend CAR.CAR.CAR to refer to the field named
CAR.CAR in the CAR segment, or the field named CAR in the CAR.CAR segment. (In either
case, the name CAR.CAR is an unqualified name that contains a period, not a qualified
name. Qualified names are not permitted in Master Files.)

No matter what the intention, the qualified field name is exactly the same and there is no
obvious choice between levels of qualification.

Since the field with alias CAR2 has the shortest basic field name length, CAR2 is printed.
This is different from the prior example, where the choice is between two levels of
qualification. To retrieve the CAR1 field, you must specify its alias.

Describing Data With TIBCO WebFOCUS® Language

 111

The Field Synonym: ALIAS

The Field Synonym: ALIAS

You can assign every field an alternative name, or alias. A field alias may be its original name
as defined to its native data source, any name you choose, or, in special cases, a predefined
value. The way in which you assign the alias is determined by the type of data source and, in
special cases, the role the field plays in the data source. After it has been assigned, you can
use this alias in requests as a synonym for the regular field name. Assign this alternative
name using the ALIAS attribute.

Example:

Using a Field Synonym

In the EMPLOYEE data source, the name CURR_SAL is assigned to a field using the
FIELDNAME attribute, and the alternative name CSAL is assigned to the same field using the
ALIAS attribute:

FIELDNAME = CURR_SAL, ALIAS = CSAL, USAGE = D12.2M,  $

Both names are equally valid within a request. The following TABLE requests illustrate that they
are functionally identical, refer to the same field, and produce the same result:

TABLE FILE EMPLOYEE
PRINT CURR_SAL BY EMP_ID
END

TABLE FILE EMPLOYEE
PRINT CSAL BY EMP_ID
END

Note: In extract files (HOLD, PCHOLD), the field name is used to identify fields, not the ALIAS.

Implementing a Field Synonym

The value you assign to ALIAS must conform to the same naming conventions to which the
FIELDNAME attribute is subject, unless stated otherwise. Assign a value to ALIAS in the
following way for the following types of data sources:

Relational data sources. ALIAS describes the field original column name as defined in the
relational table.

Sequential data sources. ALIAS describes a synonym, or alternative name, that you can
use in a request to identify the field. You can assign any name as the alias. Many users
choose a shorter version of the primary name of the field. For example, if the field name is
LAST_NAME, the alias might be LN. The ALIAS attribute is required in the Master File, but it
can have the value blank.

112


4. Describing an Individual Field

Note that ALIAS is used in a different way for sequenced repeating fields, where its value is
ORDER, as well as for RECTYPE and MAPVALUE fields when the data source includes
multiple record types. For more information, see Describing a Sequential, VSAM, or ISAM
Data Source on page 231.

FOCUS data sources. ALIAS describes a synonym, or alternative name, that you can use in
a request to identify the field. You can assign any name as the alias. Many users choose a
shorter version of the primary name of the field. For example, if the field name is
LAST_NAME, the alias might be LN. The ALIAS attribute is required in the Master File, but it
can have the value blank. For more information, see Describing a FOCUS Data Source on
page 293. Aliases can be changed without rebuilding the data source. If an alias is
referred to in other data sources, similar changes may be needed in those Master Files.

The Displayed Data Type: USAGE

This attribute, which is also known as FORMAT, describes how to format a field when
displaying it in a report or using it in a calculation.

Specifying a Display Format

For FOCUS data sources, which do not use the ACTUAL attribute, USAGE also specifies how to
store the field. For other types of data sources, assign a USAGE value that corresponds to the
ACTUAL value, to identify the field as the same data type used to store it in the data source. If
the data is store as alphanumeric, assign the USAGE based on how the field will be displayed
in your reports. The conversion is done automatically. For instructions on which ACTUAL values
correspond to which USAGE values, see the documentation for the specific data adapter. For
sequential, VSAM, and ISAM data sources, see Describing a Sequential, VSAM, or ISAM Data
Source on page 231. For other types of data sources, see your adapter documentation.

In addition to selecting the data type and length, you can also specify display options, such as
date formatting, floating dollar signs, and zero suppression. Use these options to customize
how the field appears in reports.

Syntax:

How to Specify a Display Format

USAGE = tl[d]

where:

t

Is the data type. Valid values are A (alphanumeric), F (floating-point single-precision), D
(floating-point double-precision), X extended decimal precision floating-point), I (integer), P
(packed decimal), D, W, M, Q, or Y used in a valid combination (date), and TX (text).

Describing Data With TIBCO WebFOCUS® Language

 113

The Displayed Data Type: USAGE

l

d

Is a length specification. The specification varies according to the data type. See the
section for each data type for more information. Note that you do not specify a length for
date format fields.

Is one or more display options. Different data types offer different display options. See the
section for each data type for more information.

The complete USAGE value cannot exceed eight characters.

The values that you specify for type and field length determine the number of print positions
allocated for displaying or storing the field. Display options only affect displayed or printed
fields. They are not active for non-display retrievals, such as extract files.

Note: If a numeric field cannot display with the USAGE format given (for example, the result of
aggregation is too large), asterisks appear.

See the sections for each format type for examples and additional information.

Reference: Usage Notes for USAGE

Note the following rules when using USAGE:

Alias. USAGE has an alias of FORMAT.

Changes. For most data sources, you can change the type and length specifications of
USAGE only to other types and lengths valid for the ACTUAL attribute of that field. You can
change display options at any time.

For FOCUS data sources, you cannot change the type specification. You can change the
length specification for I, F, D, and P fields, because this affects only display, not storage.
You cannot change the decimal part of the length specification for P fields. You can change
the length specification of A (alphanumeric) fields only if you use the REBUILD facility. You
can change display options at any time.

Data Type Formats

You can specify several types of formats:

Numeric. There are six types of numeric formats: integer, floating-point single-precision,
floating-point double-precision, extended decimal precision floating-point (XMATH), decimal
precision floating-point (MATH), and packed decimal. See Numeric Display Options on page
121 for additional information.

114

4. Describing an Individual Field

Alphanumeric. You can use alphanumeric format for any value to be interpreted as a
sequence of characters and composed of any combination of digits, letters, and other
characters.

Hexadecimal. This usage format is used with an Alphanumeric actual format to display or
save the hexadecimal representation of the alphanumeric field value.

String. You can use string format for alphanumeric data from Relational data sources that
have a STRING data type.

Date. The date format enables you to define date components, such as year, quarter,
month, day, and day of week to:

Sort by date.

Do date comparisons and arithmetic with dates.

Validate dates automatically in transactions.

Note that for some applications, such as assigning a date value using the DECODE
function, you may wish instead to use alphanumeric, integer, or packed-decimal fields with
date display options, which provide partial date functionality.

Date-Time. The date-time format supports both the date and the time, similar to the
timestamp data types available in many relational data sources. Date-time fields are stored
in eight, ten, or 12 bytes: four bytes for date and either four, six, or eight bytes for time,
depending on whether the format specifies a microsecond or nanosecond. Computations
only allow direct assignment within data types. All other operations are accomplished
through a set of date-time functions.

Text. Text fields can be used to store large amounts of data and display it with line breaks.

Integer Format

You can use integer format for whole numbers. An integer is any value composed of the digits
zero to nine, without a decimal point.

You can also use integer fields with date display options to provide limited date support. This
use of integer fields is described in the Alphanumeric and Numeric Formats With Date Display
Options on page 153.

The integer USAGE type is I. See Numeric Display Options on page 121. The format of the
length specification is:

Describing Data With TIBCO WebFOCUS® Language

 115

The Displayed Data Type: USAGE

n

where:

n

Is the number of digits to display. The maximum length is 11 for 32-bit versions of
WebFOCUS and 22 for 64-bit versions, which must include the digits and a leading minus
sign if the field contains a negative value. You can also specify a number of decimal
places (up to n - 1), and the number will display with a decimal point before that number of
digits.

For example:

Format

I6

I6.2

I2

I4

Display

  4316

 43.16

22

 -617

Floating-Point Double-Precision Format

You can use floating-point double-precision format for any value composed of the digits zero to
nine and an optional decimal point.

The floating-point double-precision USAGE type is D. See Numeric Display Options on page 121
for the compatible display options. The length specification format is:

t[.s]

where:

t

Is the number of characters to display up to a maximum of 33, including the numeric
digits, an optional decimal point, and a leading minus sign if the field contains a negative
value. The number of significant digits supported varies with the operating environment.

116

4. Describing an Individual Field

s

Is the number of digits that follow the decimal point. It can be a maximum of 31 and must
be less than t.

For example:

Format

D8.2

D8

Display

3,187.54

416

In the case of D8.2, the 8 represents the maximum number of places, including the decimal
point and decimal places. The 2 represents how many of these eight places are decimal
places. The commas are automatically included in the display, and are not counted in the total.

Floating-Point Single-Precision Format

You can use floating-point single-precision format for any number, including numbers with
decimal positions. The number is composed of the digits 0 to 9, including an optional decimal
point. This format is intended for use with smaller decimal numbers. Unlike floating-point
double-precision format, its length cannot exceed nine positions.

The floating-point single-precision USAGE type is F. Compatible display options are described in
Numeric Display Options on page 121. The length specification format is:

t[.s]

where:

t

Is the number of characters to display, up to a maximum of 33, including the numeric
digits, an optional decimal point, and a leading minus sign if the field contains a negative
value. The number of significant digits supported varies with the operating environment.

s

Is the number of digits that follow the decimal point. It can be up to 31 digits and must be
less than t.

Describing Data With TIBCO WebFOCUS® Language

 117

The Displayed Data Type: USAGE

For example:

Format

F5.1

F4

Display

614.2

318

Extended Decimal Precision Floating-Point Format (XMATH)

You can use extended decimal precision floating-point format for any number, including
numbers with decimal positions. The number is composed of the digits 0 to 9, including an
optional decimal point. Its length cannot exceed 37 significant digits. An extended decimal
precision floating-point value is stored as a base 10 number, unlike double-precision and
single-precision floating-point values, which are stored as binary numbers. By default, all
numeric processing is done using double-precision floating-point. You can change this default
using the SET FLOATMAPPING command.

The extended decimal precision floating-point USAGE type is X. Compatible display options are
described in Numeric Display Options on page 121. The length specification format is:

t[.s]

where:

t

Is the number of characters to display, up to a maximum of 44, including the numeric
digits, an optional decimal point, and a leading minus sign if the field contains a negative
value. The number of significant digits supported varies with the operating environment.

s

Is the number of digits that follow the decimal point. It can be up to 37 digits and must be
less than t.

For example:

Format

X5.1

118

Display

614.2

4. Describing an Individual Field

Format

X4

Display

318

Decimal Precision Floating-Point Format (MATH)

You can use decimal precision floating-point format for any number, including numbers with
decimal positions. The number is composed of the digits 0 to 9, including an optional decimal
point. This format is intended for use with smaller decimal numbers. Unlike extended decimal
precision floating-point format, its length cannot exceed 15 significant digits. A decimal
precision floating-point value is stored as a base 10 number, unlike double-precision and
single-precision floating-point values, which are stored as binary numbers. By default, all
numeric processing is done using double-precision floating-point. You can change this default
using the SET FLOATMAPPING command.

The decimal precision floating-point USAGE type is M. Compatible display options are
described in Numeric Display Options on page 121. The length specification format is:

t[.s]

where:

t

Is the number of characters to display, up to a maximum of 34, including the numeric
digits, an optional decimal point, and a leading minus sign if the field contains a negative
value. The number of significant digits supported varies with the operating environment.

s

Is the number of digits that follow the decimal point. It can be up to 31 digits and must be
less than t.

For example:

Format

M5.1

M4

Display

614.2

318

Describing Data With TIBCO WebFOCUS® Language

 119

The Displayed Data Type: USAGE

Packed-Decimal Format

You can use packed-decimal format for any number, including decimal numbers. A decimal
number is any value composed of the digits zero to nine, including an optional decimal point.

You can also use packed-decimal fields with date display options to provide limited date
support. See Alphanumeric and Numeric Formats With Date Display Options on page 153.

The packed-decimal USAGE type is P. The compatible display options are described in Numeric
Display Options on page 121.

The length specification format is:

t[.s]

where:

t

s

Is the number of characters to display, up to 33, including a maximum of 31 digits, an
optional decimal point, and a leading minus sign if the field contains a negative value.

Is the number of digits that follow the decimal point. It can be up to 31 digits and must be
less than t.

For example:

Format

P9.3

P7

Display

4168.368

617542

P fields have two internal lengths, 8 bytes (which supports up to 15 digits) and 16 bytes (which
supports up to 33 digits). A USAGE of P1 through P15 is automatically assigned an internal
storage consisting of 8 bytes. A USAGE of P16 or greater is assigned an internal storage
consisting of 16 bytes.

If your USAGE does not account for the number of digits required to display the stored number,
asterisks display instead of a number. This does not necessarily indicate an overflow of the
field, just that you did not account for displaying the number of digits that are stored in the
field.

120

4. Describing an Individual Field

Overflow occurs if you attempt to store a number with more digits than can actually fit in the
internal storage assigned. Overflow such as this is indicated by storing a number consisting of
all 9's, in all operating environments except z/OS. On z/OS, the value 0 (zero) is used.
Therefore, if you try to store a number consisting of 16 digits in a packed field assigned 8
bytes of internal storage, the number 999999999999999 (the digit 9 repeated 15 times), or
the number zero on z/OS, will be stored in the field instead.

If you assign a USAGE of P1 through P14 to such a field, the 15 digits stored in the field will
not be able to be displayed, and you will see asterisks. However, if you assign the USAGE P15
to the field, it will be able to display the 15-digit number stored in the field, so you will see the
value 999999999999999 (zero on z/OS). If you see that number for a P15 field, it could be
the actual number that was required or it could be a replacement for a number that could not
fit.

Numeric Display Options

Display options may be used to edit numeric formats. These options only affect how the data
in the field is printed or appears on the screen, not how it is stored in your data source.

Edit Option

Meaning

Effect

-

%

p

Minus sign

Displays a minus sign to the right of
negative numeric data.

Percent sign

Percentage

Note: Not supported with format options
B, E, R, T, DMY, MDY, and YMD.

Displays a percent sign (%), along with
numeric data. Does not calculate the
percent.

Converts a number to a percentage by
multiplying it by 100, and displays it
followed by a percent sign (%). Not
supported with formats I and P.

Describing Data With TIBCO WebFOCUS® Language

 121

The Displayed Data Type: USAGE

Edit Option

Meaning

Effect

A

a

b

122

Negative
suppression

Displays the absolute value of the
number, but does not affect the stored
value.

If you propagate a field with a
negative suppression USAGE
attribute to a HOLD file, the HOLD
file contains the signed values. The
negative suppression USAGE
attribute is also propagated to the
HOLD file so that if you run a report
request against the HOLD file, the
minus signs are suppressed on the
report output.

The negative suppression option
cannot be used in with the following
display options:

B (bracket negative).

R (credit negative).

- (right side negative).

Calculates the appropriate abbreviation
(K, M, B, or T) to use for displaying the
number based on the magnitude of the
number. This option uses the
appropriate abbreviation for the specific
value on the current row and, therefore,
each row may have a different
abbreviation. For example,
1234567890 displays as 1.23B, while
1234567890000 displays as 1.23T.

Automatic
abbreviation

Billions
abbreviation

Displays numeric values in terms of
billions. For example, 1234567890
displays as 1.23B.

Edit Option

Meaning

Effect

4. Describing an Individual Field

Bracket negative

Encloses negative numbers in
parentheses.

Comma suppress

Suppresses the display of commas.

DMY

Day-Month-Year

Used with numeric format options M and
N (floating and non-floating dollar sign)
and data format D (floating-point double-
precision).

Inserts a comma after every third
significant digit, or a period instead of a
comma if continental decimal notation is
in use.

Displays alphanumeric or integer data
as a date in the form day/month/year.

Displays only significant digits.

Displays numeric values in terms of
thousands. For example, 12345
displays as 12.35K.

Comma edit

Scientific
notation

Thousands
abbreviation

Leading zeroes

Adds leading zeroes.

Millions
abbreviation

Displays numeric values in terms of
millions. For example, 1234567
displays as 1.23M.

B

c

C

E

k

L

m

Describing Data With TIBCO WebFOCUS® Language

 123

The Displayed Data Type: USAGE

Edit Option

Meaning

Effect

M

MDY

N

Floating currency
symbol ($ for US
code page)

Places a floating currency symbol to the
left of the highest significant digit. The
default currency symbol depends on the
code page. You can use the SET
CURRSYMB=symbol command to specify
up to four characters as the currency
symbol or one of the following currency
codes:

USD or '$' specifies U. S. dollars.

GBP specifies the British pound.

JPY specifies the Japanese yen or
Chinese yuan.

EUR specifies the Euro.

Month-Day-Year

Displays alphanumeric or integer data
as a date in the form month/day/year.

Fixed currency
symbol ($ for US
code page)

Places a currency symbol to the left of
the field. The symbol appears only on
the first detail line of each page. The
default currency symbol depends on the
code page. You can use the SET
CURRSYMB=symbol command to specify
up to four characters as the currency
symbol or one of the following currency
codes:

USD or '$' specifies U. S. dollars.

GBP specifies the British pound.

JPY specifies the Japanese yen or
Chinese yuan.

EUR specifies the Euro.

Places CR after negative numbers.

R

Credit (CR)
negative

124

4. Describing an Individual Field

Edit Option

Meaning

Effect

S

t

T

Zero suppress

If the data value is zero, prints a blank
in its place.

Trillions
abbreviation

Displays numeric values in terms of
trillions. For example, 1234567890000
displays as 1.23T.

Month translation

Displays the month as a three-character
abbreviation.

YMD

Year-Month-Day

Displays alphanumeric or integer data
as a date in the form year/month/day.

Note: For abbreviation options k, m, b, t, and a.

The abbreviated value displays with the number of decimal places specified in the format of
the field to which is it returned.

The format options do not change how a value is stored, just how it is displayed.

Numbers are rounded prior to display in an abbreviated format. Therefore, when a packed
or integer formatted number is displayed in abbreviated form using the EXTENDNUM ON
setting, overflow values can be mistaken for correct results.

These display options are supported with all numeric formats and are compatible with
additional display options such as -, B, R, C, c, M, and N.

Example:

Using Numeric Display Options

The following table shows examples of the display options that are available for numeric fields.

Option

Minus sign

Format

I2-
D7-
F7.2-

Data

-21
-6148
-8878

Display

21-
6148-
8878.00-

Describing Data With TIBCO WebFOCUS® Language

 125

The Displayed Data Type: USAGE

Option

Percent sign

Comma suppression

Comma inclusion

Zero suppression

Bracket negative

Credit negative

Leading zeroes

Floating dollar

Non-floating dollar

Format

I2%
D7%
F3.2%

D6c
D7Mc
D7Nc

I6C

D6S

I6B

I8R

F4L

D7M

D7N

Data

21
6148
48

41376
6148
6148

41376

0

Display

21%
6,148%
48.00%

41376
$6148
$  6148

41,376

-64187

(64187)

-3167

3167 CR

31

6148

5432

0031

$6,148

$    5,432

Scientific notation

D12.5E

1234.5

0.12345D+04

Year/month/day

Month/day/year

Day/month/year

I6YMD
I8YYMD

I6MDY
I8MDYY

I6DMY
I8DMYY

980421
19980421

042198
04211998

210498
21041998

98/04/21
1998/04/21

04/21/98
04/21/1998

21/04/98
21/04/1998

Month translation

I2MT

07

JUL

126


4. Describing an Individual Field

Several display options can be combined, as shown:

Format

I5CB

Data

-61874

Display

(61,874)

All of the options may be specified in any order. Options M and N (floating and non-floating
dollar sign) and data format D (floating-point double-precision) automatically invoke option C
(comma). Options L and S cannot be used together. Option T (Translate) can be included
anywhere in an alphanumeric or integer USAGE specification that includes the M (month)
display option. Date display options (D, M, T, and Y), which cannot be used with floating-point
fields, are described in Alphanumeric and Numeric Formats With Date Display Options on page
153.

Using International System (SI) Numeric Format Abbreviation Options

The International System standard provides numeric abbreviations for very large and very small
numbers.

WebFOCUS supports the following SI-compliant numeric abbreviations. The SI-compliant format
uses a two-character display code that consists of a lowercase n followed by the SI
abbreviation.

Prefix

WebFOCUS
Format Code

Size

Example

English Name
(American/British)

yotta

zetta

exa

peta

tera

giga

mega

kilo

milli

nY

nZ

nE

nP

nT

nG

nM

nK

nm

10**24

1000000000000000000000000

septillion/quadrillion

10**21

1000000000000000000000

sextillion/trilliard

10**18

1000000000000000000

quintillion/trillion

10**15

1000000000000000

quadrillion/billiard

10**12

1000000000000

10**9

1000000000

10**6

1000000

10**3

1000

10**(-3)

0.001

trillion/billion

billion/milliard

million

thousand

thousandth

Describing Data With TIBCO WebFOCUS® Language

 127

The Displayed Data Type: USAGE

Prefix

WebFOCUS
Format Code

Size

Example

English Name
(American/British)

micro

nano

pico

femto

atto

zepto

yocto

nu

nn

np

nf

na

nz

ny

10**(-6)

0.000001

millionth

10**(-9)

0.000000001

billionth/milliardth

10**(-12)

0.000000000001

trillionth/billionth

10**(-15)

0.000000000000001

quadrillionth/billiardth

10**(-18)

0.000000000000000001

quintillionth/trillionth

10**(-21)

0.000000000000000001

sextillionth/trilliardth

10**(-24)

0.000000000000000000000001

septillionth/quadrillionth

The following request uses the mega and giga format options. The decimal precision is
controlled by the format which, in this case, is a reformat specified in the SUM command.

DEFINE FILE GGSALES
NEWDOLL/D12.2 = DOLLARS * 100;
END
TABLE FILE GGSALES
SUM DOLLARS NEWDOLL/D12.5nM AS Millions NEWDOLL/D12.3nG AS Billions
BY CATEGORY
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

The output is shown in the following image.

128

Extended Currency Symbol Display Options

4. Describing an Individual Field

You can select a currency symbol for display in report output regardless of the default currency
symbol configured for National Language Support (NLS). Use the extended currency symbol
format in place of the floating dollar (M) or non-floating dollar (N) display option. When you use
the floating dollar (M) or non-floating dollar (N) display option, the currency symbol associated
with the default code page is displayed. For example, when you use an American English code
page, the dollar sign is displayed.

The extended currency symbol format allows you to display a symbol other than the dollar sign.
For example, you can display the symbol for a United States dollar, a British pound, a
Japanese yen or Chinese yuan, or the euro. Extended currency symbol support is available for
numeric formats (I, D, F, and P).

The extended currency symbol formats are specified as two-character combinations in the last
positions of any numeric display format. The first character in the combination can be either an
exclamation point (!) or a colon (:). The colon is the recommended character because it will
work in all ASCII and EBCDIC code pages. The exclamation point is not consistent on all
EBCDIC code pages and may produce unexpected behavior if the code page you are using
translates the exclamation point differently.

In addition, you can use the SET commands SET CURSYM_D, SET CURSYM_E, SET
CURSYM_F, SET CURSYM_G, SET CURSYM_L, and SET CURSYM_Y to redefine the default
display characters for the extended currency symbol formats. For example, you can display a
euro symbol on the right of the number and add a space between the number and the euro
symbol by issuing the SET CURSYM_F command and using the extended currency symbol
format :F in the request or Master File.

SET CURSYM_F = ' €'

For more information, see the Developing Reporting Applications manual.

Describing Data With TIBCO WebFOCUS® Language

 129

The Displayed Data Type: USAGE

The following table lists the supported extended currency display options:

Display
Option

:C or !C

Example

D12.2:C

Description

The currency symbol is determined by
the locale settings. Its display is
controlled by the following parameters:

CURRENCY_PRINT_ISO specifies
whether to display the currency
symbol or ISO code.

CURRENCY_DISPLAY controls where
the currency symbol or ISO code
displays relative to the number.

CURRENCY_ISO_CODE sets the ISO
code and, therefore, the currency
symbol to use.

:d or !d

Fixed dollar sign.

:D or !D

Floating dollar sign.

:e or !e

Fixed euro symbol.

D12.2:d

D12.2:D

F9.2:e

:E or !E

Floating euro symbol on the left side.

F9.2:E

:F or !F

Floating euro symbol on the right side.

F9.2:F

:G or !G

Floating dollar symbol on the right side.

F9.2:G

:l or !l

Fixed British pound sign.

:L or !L

Floating British pound sign.

:y or !y

:Y or !Y

Fixed Japanese yen or Chinese yuan
symbol.

Floating Japanese yen or Chinese yuan
symbol.

D12.1:l

D12.1:L

I9:y

I9:Y

130

Reference: Extended Currency Symbol Formats

The following guidelines apply:

4. Describing an Individual Field

A format specification cannot be longer than eight characters.

The extended currency option must be the last option in the format.

The extended currency symbol format cannot include the floating (M) or non-floating (N)
display option.

A non-floating currency symbol is displayed only on the first row of a report page. If you use
field-based reformatting (as in the example that follows) to display multiple currency
symbols in a report column, only the symbol associated with the first row is displayed. In
this case, do not use non-floating currency symbols.

Lowercase letters are transmitted as uppercase letters by the terminal I/O procedures.
Therefore, the fixed extended currency symbols can only be specified in a procedure.

Extended currency symbol formats can be used with fields in floating point, decimal,
packed, and integer formats. Alphanumeric and variable character formats cannot be used.

Syntax:

How to Select an Extended Currency Symbol

numeric_format {:|!}option

where:

numeric_format

Is a valid numeric format (data type I, D, F, or P).

: or !

Is required. The exclamation point is not consistent on all EBCDIC code pages and may
produce unexpected behavior if the code page you are using translates the exclamation
point differently. The colon does not vary across code pages, so it is the recommended
symbol to use.

option

Determines the currency symbol that is displayed, and whether the symbol is floating or
non-floating. Possible values are:

C. Displays the currency symbol determined by the locale settings.

d. Displays a non-floating dollar sign.

Describing Data With TIBCO WebFOCUS® Language

 131

The Displayed Data Type: USAGE

D. Displays a floating dollar sign.

e. Displays a non-floating euro symbol.

E. Displays a floating euro symbol on the left side.

F. Displays a floating euro symbol on the right side.

l. Displays a non-floating British pound sterling symbol.

L. Displays a floating British pound sterling symbol.

y. Displays a non-floating Japanese yen or Chinese yuan symbol.

Y. Displays a floating Japanese yen or Chinese yuan symbol.

The extended currency option must be in the last positions in the format.

Example:

Displaying Extended Currency Symbols

The following request displays the euro symbol.

SET PAGE-NUM = OFF
TABLE FILE CENTORD
PRINT PRODNAME QUANTITY PRICE/D10.2!E
BY ORDER_DATE
WHERE QUANTITY GT 700;
ON TABLE SET STYLE *
TYPE = REPORT, GRID = OFF,$
ENDSTYLE
END

132

The output is:

4. Describing an Individual Field

Reference: Locale Display Options for Currency Values

The CURRENCY_ISO_CODE and CURRENCY_DISPLAY parameters can be applied on the field
level as display parameters in a Master File DEFINE, a DEFINE command, or in a COMPUTE
using the :C display option.

Note: These parameters are not supported with FORMAT EXL2K report output.

The syntax is:

fld/fmt:C(CURRENCY_DISPLAY='pos',
   CURRENCY_ISO_CODE='iso')= expression;

where:

fld

Is the field to which the parameters are to be applied.

fmt

Is a numeric format that supports a currency value.

Describing Data With TIBCO WebFOCUS® Language

 133

The Displayed Data Type: USAGE

pos

Defines the position of the currency symbol relative to a number. The default value is
default, which uses the position for the format and currency symbol in effect. Valid values
are:

LEFT_FIXED. The currency symbol is left-justified preceding the number.

LEFT_FIXED_SPACE. The currency symbol is left-justified preceding the number, with at
least one space between the symbol and the number.

LEFT_FLOAT. The currency symbol precedes the number, with no space between them.

LEFT_FLOAT_SPACE. The currency symbol precedes the number, with one space
between them.

TRAILING. The currency symbol follows the number, with no space between them.

TRAILING_SPACE. The currency symbol follows the number, with one space between
them.

iso

Is a standard three-character currency code, such as USD for US dollars or JPY for
Japanese yen. The default value is default, which uses the currency code for the configured
language code.

expression

Is the expression that creates the virtual field.

Note: If currency parameters are specified at multiple levels, the order of precedence is:

1. Field level parameters.

2. Parameters set in a request (ON TABLE SET).

3. Parameters set in a FOCEXEC outside of a request.

4. Parameters set in a profile, using the precedence for profile processing.

134

Example:

Specifying Currency Parameters in a DEFINE

4. Describing an Individual Field

The following request creates a virtual field named Currency_parms that displays the currency
symbol on the right using the ISO code for Japanese yen, 'JPY'.

DEFINE FILE WF_RETAIL_LITE
Currency_parms/D20.2:C(CURRENCY_DISPLAY='TRAILING',CURRENCY_ISO_CODE='JPY')
= COGS_US;
END
TABLE FILE WF_RETAIL_LITE
SUM COGS_US Currency_parms
BY BUSINESS_REGION AS 'Region'
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
END

The output is shown in the following image.

Rounding

When a value with decimal places is assigned to a numeric field, if there are more decimal
places in the value than are specified in the field length description, the value is rounded to an
acceptable size before either storing or displaying it. The value is rounded down when the first
extra decimal digit is less than five, and rounded up when it is five or greater (although an
additional consideration is introduced for floating-point values).

For example, consider a packed-decimal field with two decimal places

FIELDNAME = PRESSURE, FORMAT = P8.2, $

to which you assign a value with four decimal places:

PRESSURE = 746.1289

The first extra digit (that is, the first one past the specified length of two decimal places), is 8.
Since 8 is greater than or equal to five, the value is rounded up, and PRESSURE becomes:

746.13

Describing Data With TIBCO WebFOCUS® Language

 135

The Displayed Data Type: USAGE

The details of rounding are handled in the following ways for the following numeric formats:

Integer format. When a value with decimal places is assigned to an integer field, the value
is rounded before it is stored. If the value is assigned using a DEFINE or COMPUTE
command, the decimal portion of the value is truncated before it is stored.

Packed-decimal format. When a value is assigned to a packed-decimal field, and the value
has more decimal places than the field format specifies, the value is rounded before it is
stored.

Floating-point single-precision and double-precision formats. When a value is assigned to
one of these fields, and the value has more decimal places than the field format specifies,
the full value is stored in the field (up to the limit of precision determined by the field
internal storage type). When this value is later displayed, however, it is rounded.

Note that if the decimal portion of a floating-point value as it is internally represented in
hexadecimal floating-point notation is repeating (that is, non-terminating), the repeating
hexadecimal number is resolved as a non-repeating slightly lower number, and this lower
number is stored as the field value. In these situations, if in the original value of the digit to
be rounded had been a five (which would be rounded up), in the stored lower value, it would
become a four (which is rounded down).

For example, consider a floating-point double-precision field with one decimal place

FIELDNAME = VELOCITY, FORMAT = D5.1, $

to which you assign a value with two decimal places:

VELOCITY = 1.15

This value is stored as a slightly smaller number due to the special circumstances of
floating-point arithmetic, as previously described:

1.149999

While the original number, 1.15, would have been rounded upward to 1.2 (since the first
extra digit was 5 or greater), the number as stored is slightly less than 1.15 (1.149999)
and, as the first extra digit is now less than 5 (4 in this case), it is rounded down to 1.1. To
summarize the process:

format:    D5.1
entered:   1.15
stored:    1.149999
rounded:   1.1
displayed: 1.1

136

Alphanumeric Format

4. Describing an Individual Field

You can use alphanumeric format for any value to be interpreted as a sequence of characters
and composed of any combination of digits, letters, and other characters.

You can also use alphanumeric fields with date display options to provide limited date support.
This use of alphanumeric fields is described in Alphanumeric and Numeric Formats With Date
Display Options on page 153.

The alphanumeric USAGE type is A. The format of the length specification is n, where n is the
maximum number of characters in the field. You can have up to 3968 bytes in an
alphanumeric field in a FOCUS file segment, and up to 4096 bytes in an XFOCUS file segment.
You can have up to 4095 bytes in a fixed-format sequential data source. You may define the
length in the Master File, a DEFINE FILE command, or a COMPUTE command.

For example:

Format

Display

A522

The minutes of today's meeting were submitted...

A2

A24

B3

127-A429-BYQ-49

Standard numeric display options are not available for the alphanumeric data format. However,
alphanumeric data can be printed under the control of a pattern that is supplied at run time.
For instance, if you are displaying a product code in parts, with each part separated by a "-",
include the following in a DEFINE command:

PRODCODE/A11 = EDIT (fieldname,'999-999-999') ;

where:

fieldname

Is the existing field name, not the newly defined field name.

If the value is 716431014, the PRODCODE appears as 716-431-014. See the Creating
Reports With WebFOCUS Language manual for more information.

Describing Data With TIBCO WebFOCUS® Language

 137

The Displayed Data Type: USAGE

Reference: Usage Notes for 4K Alphanumeric Fields

Long alphanumeric fields cannot be indexed.

For FOCUS data sources, a segment still has to fit on a 4K page. Thus, the maximum
length of an alphanumeric field depends on the length of the other fields within its
segment.

You can print or hold long alphanumeric fields, but you cannot view them online.

Long alphanumeric fields may be used as keys.

Hexadecimal Format

You can use the USAGE format Un to display the hexadecimal representation of alphanumeric
data. The corresponding ACTUAL format is A with two times the length of the USAGE format.

The following operations are supported for hexadecimal format:

Display.

Reformatting.

DEFINE.

COMPUTE.

HOLD that produces alphanumeric output.

SAVE.

Selection on the alphanumeric representation of the characters.

Assignment between hexadecimal and alphanumeric fields.

For example, the following request prints the hexadecimal representation of the alphanumeric
Category field:

TABLE FILE GGSALES
SUM CATEGORY/U10 AS Hex,Category DOLLARS UNITS
BY CATEGORY
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

138

The output is shown in the following image.

4. Describing an Individual Field

The following version of the request creates the hexadecimal field in a DEFINE command and
adds a HOLD command:

APP HOLD baseapp
DEFINE FILE GGSALES
HEXCAT/U10 = CATEGORY;
END

TABLE FILE GGSALES
SUM HEXCAT DOLLARS UNITS
BY CATEGORY
ON TABLE HOLD AS HOLDHEX FORMAT ALPHA
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

The generated Master File follows. The HEXCAT field has USAGE=U10 and ACTUAL=A20.

FILENAME=HOLDHEX , SUFFIX=FIX     , IOTYPE=STREAM, $
  SEGMENT=HOLDHEX, SEGTYPE=S1, $
    FIELDNAME=CATEGORY, ALIAS=E01, USAGE=A11, ACTUAL=A11, $
    FIELDNAME=HEXCAT, ALIAS=E02, USAGE=U10, ACTUAL=A20, $
    FIELDNAME=DOLLARS, ALIAS=E03, USAGE=I08, ACTUAL=A08, $
    FIELDNAME=UNITS, ALIAS=E04, USAGE=I08, ACTUAL=A08, $

String Format

Certain relational data sources support a data type called STRING to store alphanumeric data
that has an unlimited length. This type of data can be mapped to the TX data type. However,
text fields have limitations on their use in WebFOCUS sort and selection phrases.

The format specification for a STRING field has no length specification. The length is
determined on retrieval. For example:

FIELD1/STRING

Describing Data With TIBCO WebFOCUS® Language

 139

The Displayed Data Type: USAGE

The STRING data type has all of the functionality of alphanumeric data types in WebFOCUS.
The limit to a STRING field value length is 2 GB. It can be propagated to relational data
sources that have the STRING data type and to delimited HOLD files, where both the USAGE
and ACTUAL formats are generated as STRING.

Date Formats

Date format enables you to define a field as a date, then manipulate the field value and
display that value in ways appropriate to a date. Using date format, you can:

Define date components, such as year, quarter, month, day, and day of week, and extract
them easily from date fields.

Sort reports into date sequence, regardless of how the date appears.

Perform arithmetic with dates and compare dates without resorting to special date-handling
functions.

Refer to dates in a natural way, such as JAN 1 1995, without regard to display or editing
formats.

Automatically validate dates in transactions.

Date Display Options

The date format does not specify type or length. Instead, it specifies date component options
(D, W, M, Q, Y, and YY) and display options. These options are shown in the following chart.

Display Option

Meaning

Effect

D

M

Y

YY

T

Day

Month

Year

Prints a value from 1 to 31 for the day.

Prints a value from 1 to 12 for the month.

Prints a two-digit year.

Four-digit year

Prints a four-digit year.

Translate month or
day

Prints a three-letter abbreviation for months
in uppercase, if M is included in the USAGE
specification. Otherwise, it prints day of
week.

140

Display Option

Meaning

Effect

4. Describing an Individual Field

t

TR

tr

Q

W

w

WR

wr

Translate month or
day

Translate month or
day

Functions the same as uppercase T
(described above), except that the first letter
of the month or day is uppercase and the
following letters are lowercase.*

Functions the same as uppercase T
(described above), except that the entire
month or day name is printed instead of an
abbreviation.

Translate month or
day

Functions the same as lowercase t (described
above), except that the entire month or day
name is printed instead of an abbreviation.*

Quarter

Prints Q1 - Q4.

Day-of-Week

Day-of-Week

Day-of-Week

Day-of-Week

If it is included in a USAGE specification with
other date component options, prints a three-
letter abbreviation of the day of the week in
uppercase. If it is the only date component
option in the USAGE specification, it prints
the number of the day of the week (1-7;
Mon=1).

Functions the same as uppercase W
(described above), except that the first letter
is uppercase and the following letters are
lowercase.*

Functions the same as uppercase W
(described above), except that the entire day
name is printed instead of an abbreviation.

Functions the same as lowercase w
(described above), except that the entire day
name is printed instead of an abbreviation.*

J[UL]or JULIAN

Julian format

Prints date in Julian format.

Describing Data With TIBCO WebFOCUS® Language

 141

The Displayed Data Type: USAGE

Display Option

Meaning

Effect

YYJ[UL]

Julian format

Prints a Julian format date in the format
YYYYDDD. The 7-digit format displays the
four-digit year and the number of days
counting from January 1. For example,
January 3, 2001 in Julian format is 2001003.

Note: When using these display options, be sure they are actually stored in the Master File as
lowercase letters.

The following combinations of date components are not supported in date formats:

I2M, A2M, I2MD, A2MD

Reference: How Field Formats Y, YY, M, and W Are Stored

The Y, YY, and M formats are not smart dates. Smart date formats YMD and YYMD are stored
as an offset from the base date of 12/31/1900. Smart date formats YM, YQ, YYM, and YYQ
are stored as an offset from the base date 01/1901 on z/OS and 12/1900 on other
platforms. W formats are stored as integers with a display length of one, containing values 1-7
representing the days of the week. Y, YY, and M formats are stored as integers. Y and M have
display lengths of two. YY has a display length of four. When using Y and YY field formats,
keep in mind these two important points:

The Y formats do not sort based on DEFCENT and YRTHRESH settings. A field with a format
of Y does not equal a YY field, as this is not a displacement, but a 4-digit integer.

It is possible to use DEFCENT and YRTHRESH to convert a field from Y to YY format.

Reference: Date Literals Interpretation Table

This table illustrates the behavior of date formats. The columns indicate the number of input
digits for a date format. The rows indicate the usage or format of the field. The intersection of
row and column describes the result of input and format.

Date Format

1

2

3

4

YYMD

MDYY

     *

     *

CC00/0m/dd

CC00/mm/dd

     *

     *

     *

     *

142

4. Describing an Individual Field

Date Format

1

2

3

4

DMYY

     *

     *

     *

     *

YMD

MDY

DMY

YYM

MYY

YM

MY

M

YYQ

QYY

YQ

QY

Q

     *

     *

CC00/0m/dd

CC00/mm/dd

     *

     *

     *

     *

     *

     *

     *

     *

CC00/0m

 CC00/mm

CC0y/mm

CCyy/mm

     *

     *

     *

     *

CC00/0m

 CC00/mm

CC0y/mm

CCyy/mm

     *

     *

0m/CCyy

mm/CCyy

0m

mm

     *

CC00/q

CC0y/q

CCyy/q

     *

     *

q/CCyy

CC00/q

CC0y/q

CCyy/q

     *

     *

q/CCyy

q

     *

     *

     *

0yyy/q

     *

0yyy/q

     *

     *

0y/ddd

JUL

00/00d

00/0dd

00/ddd

YYJUL

CC00/00d

CC00/0dd

CC00/ddd

CC0y/ddd

YY

000y

00yy

0yyy

Y

D

0y

0d

yy

dd

     *

     *

yyyy

     *

     *

Describing Data With TIBCO WebFOCUS® Language

 143

The Displayed Data Type: USAGE

Date Format

W

1

w

2

3

4

      *

     *

     *

Date Format

5

6

7

8

YYMD

MDYY

DMYY

YMD

MDY

DMY

YYM

MYY

YM

MY

M

YYQ

QYY

YQ

QY

Q

CC0y/mm/dd

CCyy/mm/dd

0yyy/mm/dd

yyyy/mm/dd

0m/dd/CCyy

mm/dd/CCyy

0m/dd/yyyy

mm/dd/yyyy

0d/mm/CCyy

dd/mm/CCyy

0d/mm/yyyy

dd/mm/yyyy

CC0y/mm/dd

CCyy/mm/dd

0yyy/mm/dd

yyyy/mm/dd

0m/dd/CCyy

mm/dd/CCyy

0m/dd/yyyy

mm/dd/yyyy

0d/mm/CCyy

dd/mm/CCyy

0d/mm/yyyy

dd/mm/yyyy

0yyy/mm

yyyy/mm

      *

      *

0m/yyyy

mm/yyyy

      *

      *

0yyy/mm

yyyy/mm

      *

      *

0m/yyyy

mm/yyyy

      *

      *

      *

      *

      *

      *

yyyy/q

      *

      *

      *

q/yyyy

      *

      *

      *

yyyy/q

      *

      *

      *

q/yyyy

      *

      *

      *

      *

      *

      *

      *

JUL

yy/ddd

      *

      *

      *

144

4. Describing an Individual Field

Date Format

5

6

7

8

YYJUL

CCyy/ddd

0yyy/ddd

yyyy/ddd

      *

      *

      *

      *

      *

      *

      *

      *

      *

      *

      *

      *

      *

      *

      *

      *

      *

YY

Y

D

W

Note:

CC stands for two century digits provided by DFC/YRT settings.

* stands for message FOC177 (invalid date constant).

Date literals are read from right to left. Date literals and fields can be used in
computational expressions, as described in the Creating Reports With WebFOCUS Language
manual.

Controlling the Date Separator

You can control the date separators when the date appears. In basic date format, such as
YMD and MDYY, the date components appear separated by a slash character (/). The same is
true for the year-month format, which appears with the year and quarter separated by a blank
(for example, 94 Q3 or Q3 1994). The single component formats display just the single
number or name.

The separating character can also be a period, a dash, or a blank, or can even be eliminated
entirely. The following table shows the USAGE specifications for changing the separating
character.

Format

Display

YMD

93/12/24

Y.M.D

93.12.24

Y-M

93-12

Describing Data With TIBCO WebFOCUS® Language

 145

The Displayed Data Type: USAGE

Format

Display

YBMBD

93 12 24

(The letter B signifies blank spaces.)

Y|M|D

931224

(The concatenation symbol (|) eliminates the separation character.)

Note:

You can change the date separator in the following date formats: YYMD, MDYY, DMYY,
YMD, MDY, DMY, YYM, MYY, YM, MY, YYQ, QYY, YQ, and QY.

You cannot change the date separator in a format that includes date translation options.

You cannot change the date separator (/) in an alphanumeric or numeric format with date
display options (for example, I8YYMD).

Date Translation

Numeric months and days can be replaced by a translation, such as JAN, January, Wed, or
Wednesday. The translated month or day can be abbreviated to three characters or fully
spelled out. It can appear in either uppercase or lowercase. In addition, the day of the week
(for example, Monday) can be appended to the beginning or end of the date. All of these
options are independent of each other.

Translation

MT

Mt

MTR

Mtr

WR

wr

146

Display

JAN

Jan

JANUARY

January

MONDAY

Monday

4. Describing an Individual Field

Example:

Using a Date Format

The following chart shows sample USAGE and ACTUAL formats for data stored in a non-FOCUS
data source. The Value column shows the actual data value, and the Display column shows
how the data appears.

USAGE

ACTUAL

Value

Display

wrMtrDYY

A6YMD

990315

Monday, March 15 1999

YQ

QYY

YMD

A6YMD

A6YMD

A6

990315

99 Q1

990315

Q1 1999

990315

99/03/15

MDYY

A6YMD

990315

03/15/1999

Note that the date attributes in the ACTUAL format specify the order in which the date is stored
in the non-FOCUS data source. If the ACTUAL format does not specify the order of the month,
day, and year, it is inferred from the USAGE format.

Using a Date Field

A field formatted as a date is automatically validated when entered. It can be entered as a
natural date literal (for example, JAN 12 1999) or as a numeric date literal (for example,
011299).

Natural date literals enable you to specify a date in a natural, easily understandable way, by
including spaces between date components and using abbreviations of month names. For
example, April 25, 1999 can be specified as any of the following natural date literals:

APR 25 1999
25 APR 1999
1999 APR 25

Natural date literals can be used in all date computations, and all methods of data source
updating. The following code shows examples:

In WHERE screening                   WHERE MYDATE IS 'APR 25 1999'
In arithmetic expressions            MYDATE - '1999 APR 25'
In computational date comparisons    IF MYDATE GT '25 APR 1999'

In comma-delimited data          ...,MYDATE = APR 25 1999, ...

Describing Data With TIBCO WebFOCUS® Language

 147

The Displayed Data Type: USAGE

The following chart describes the format of natural date literals.

Literal

Format

Year-month-day

Four-digit year, uppercase three-character abbreviation, or
uppercase full name, of the month, and one-digit or two-digit day
of the month (for example, 1999 APR 25 or APRIL 25 1999).

Year-month

Year and month as described above.

Year-quarter

Month

Quarter

Day of week

Year as described above, Q plus quarter number for the quarter
(for example, 1999 Q3).

Month as described above.

Quarter as described above.

Three-character, uppercase abbreviation, or full, uppercase name,
of the day (for example, MON or MONDAY).

The date components of a natural date literal can be specified in any order, regardless of their
order in the USAGE specification of the target field. Date components are separated by one or
more blanks.

For example, if a USAGE specification for a date field is YM, a natural date literal written to
that field can include the year and month in any order. MAY 1999 and 1990 APR are both valid
literals.

Numeric Date Literals

Numeric date literals differ from natural date literals in that they are simple strings of digits.
The order of the date components in a numeric date literal must match the order of the date
components in the corresponding USAGE specification. In addition, the numeric date literal
must include all of the date components included in the USAGE specification. For example, if
the USAGE specification is DMY, then April 25 1999 must be represented as:

250499

Numeric date literals can be used in all date computations and all methods of data source
updating.

148

4. Describing an Individual Field

Date Fields in Arithmetic Expressions

The general rule for manipulating date fields in arithmetic expressions is that date fields in the
same expression must specify the same date components. The date components can be
specified in any order, and display options are ignored. Y or YY, Q, M, W, and D are valid
components.

Note that arithmetic expressions assigned to quarters, months, or days of the week are
computed modulo 4, 12, and 7, respectively, so that anomalies like fifth quarters and
thirteenth months are avoided.

For example, if NEWQUARTER and THISQUARTER both have USAGE specifications of Q, and the
value of THISQUARTER is 2, then the following statement gives NEWQUARTER a value of 1
(that is, the remainder of 5 divided by 4):

NEWQUARTER = THISQUARTER + 3

Converting a Date Field

Two types of conversion are possible: format conversion and date component conversion. In
the first case, the value of a date format field can be assigned to an alphanumeric or integer
field that uses date display options (see the following section). The reverse conversion is also
possible.

In the second case, a field whose USAGE specifies one set of date components can be
assigned to another field specifying different date components.

For example, the value of REPORTDATE (DMY) can be assigned to ORDERDATE (Y). In this
case, the year is being extracted from REPORTDATE. If REPORTDATE is Apr 27 99, ORDERDATE
is 99.

You can also assign the value of ORDERDATE to REPORTDATE. If the value of ORDERDATE is
99, the value of REPORTDATE is Jan 1 99. In this case, REPORTDATE is given values for the
missing date components.

Syntax:

How to Convert a Date Field

field1/format = field2;

where:

field1

Is a date format field, or an alphanumeric or integer format field using date display
options.

Describing Data With TIBCO WebFOCUS® Language

 149

The Displayed Data Type: USAGE

format

Is the USAGE (or FORMAT) specification of field1 (the target field).

field2

Is a date format field, or an alphanumeric or integer format field using date display
options. The format types (alphanumeric, integer, or date) and the date components (YY,
Y, Q, M, W, D) of field1 and field2 do not need to match.

How a Date Field Is Represented Internally

Date fields are represented internally as four-byte binary integers indicating the time elapsed
since the date format base date. For each field, the unit of elapsed time is that field smallest
date component.

For example, if the USAGE specification of REPORTDATE is MDY, then elapsed time is
measured in days, and internally the field contains the number of days elapsed between the
entered date and the base date. If you enter the numeric literal for February 13, 1964 (that is,
021364), and then print the field in a report, 02/13/64 appears. If you use it in the equation:

NEWDATE = 'FEB 28 1964' - REPORTDATE ;
DAYS/D = NEWDATE ;

then the value of DAYS is 15. However, the internal representation of REPORTDATE is a four
byte binary integer representing the number of days between December 31, 1900 and February
13, 1964.

Just as the unit of elapsed time is based on a field smallest date component, so too is the
base date. For example, for a YQ field, elapsed time is measured in quarters, and the base
date is the first quarter of 1901 on z/OS and the last quarter of 1900 on other platforms. For
a YM field, elapsed time is measured in months, and the base date is the first month of 1901
on z/OS and the last month of 1900 on other platforms.

To display blanks or the actual base date in a report, use the SET DATEDISPLAY command
described in the Developing Reporting Applications manual. The default value, OFF, displays
blanks when a date matches the base date. ON displays the actual base date value.

You do not need to be concerned with the date format internal representation, except to note
that all dates set to the base date appear as blanks, and all date fields that are entered blank
or as all zeroes are accepted during validation and interpreted as the base date. They appear
as blanks, but are interpreted as the base date in date computations and expressions.

150

4. Describing an Individual Field

There are several types of formats you can use to represent date components, and the
different types do not represent the same values or offsets.

Full date formats are stored as the number of days from the base date 12/31/1900.

Single component formats Y, YY, M, W, and D are stored as integers, not as offsets from a
base date.

Partial date formats YM, YQ, YYM, and YYQ are stored as an offset from the base date
01/1901 on z/OS and 12/1900 on other platforms. Both of these base dates are different
from the base date for full component dates (12/31/1900). The offset is expressed in a
number of months from the base date for YM and YYM, and as a number of quarters from
the base date for YQ and YYQ.

Full date formats with component display options, such as YYMDy, YYMDm, and YYMDq,
display the same values as the component formats such as YYQ and YM. However, they
are stored as full component dates (the number of days from the base date 12/31/1900).
Therefore, while they display the same types of dates as the component date formats YM,
YYM, YQ, and YYQ, their internal offset values are not the same. They are considered
different types of date formats and cannot be compared or subtracted.

When either a partial date or a component date is assigned to a field with a full date
format, the missing components are assigned the value 01.

Example:

Using Full Date Formats and Component Date Formats

The following request retrieves the current date as a full date field named FULLDATE. It creates
a partial date field named PARTIALDATE with format YYM, and a component date field named
FULLCOMPONENT with format YYMDm, from the full date field. It then creates two new full
dates FULLDATE2 and FULLDATE3 by assigning the partial date to one and the component
date to the other.

DEFINE FILE GGSALES
FULLDATE/YYMD = '2017/09/12';
PARTIALDATE/YYM =FULLDATE;
FULLCOMPONENT/YYMDm = FULLDATE;
FULLDATE2/YYMD = FULLCOMPONENT;
FULLDATE3/YYMD = PARTIALDATE;
END
TABLE FILE GGSALES
PRINT FULLDATE PARTIALDATE FULLCOMPONENT FULLDATE2 FULLDATE3
BY CATEGORY
WHERE RECORDLIMIT EQ 1
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

Describing Data With TIBCO WebFOCUS® Language

 151

The Displayed Data Type: USAGE

The output is shown in the following image. Note that when the partial and component dates
are assigned to FULLDATE2 and FULLDATE3, the day assigned is 01 in both cases.

Displaying a Non-Standard Date Format

By default, if a date field in a non-FOCUS data source contains an invalid date, a message
appears and the entire record fails to appear in a report. For example, if a date field contains
'980450' with an ACTUAL of A6 and a USAGE of YMD, the record containing that field does not
appear. The SET ALLOWCVTERR command enables you to display the rest of the record that
contains the incorrect date.

Note: The ALLOWCVTERR parameter is not supported for virtual fields.

Syntax:

How to Invoke ALLOWCVTERR

SET ALLOWCVTERR = {ON|OFF}

where:

ON

OFF

Enables you to display a field containing an incorrect date.

Generates a diagnostic message if incorrect data is encountered, and does not display the
record containing the bad data. OFF is the default value.

When a bad date is encountered, ALLOWCVTERR sets the value of the field to either MISSING
or to the base date, depending on whether MISSING=ON.

The following chart shows the results of interaction between DATEDISPLAY and MISSING,
assuming ALLOWCVTERR=ON and the presence of a bad date.

MISSING=OFF

MISSING=ON

DATEDISPLAY=ON

Displays Base Date
19001231 or 1901/1

DATEDISPLAY=OFF

Displays Blanks

.

.

152


4. Describing an Individual Field

DATEDISPLAY affects only how the base date appears. See the Developing Reporting
Applications manual for a description of DATEDISPLAY.

Date Format Support

Date format fields are used in special ways with the following facilities:

Dialogue Manager. Amper variables can function as date fields if they are set to natural
date literals. For example:

-SET &NOW = 'APR 25 1960' ;
-SET &LATER = '1990 25 APR' ;
-SET &DELAY = &LATER - &NOW ;

In this case, the value of &DELAY is the difference between the two dates, measured in
days: 10,957.

Extract files. Date fields in SAVB and unformatted HOLD files are stored as four-byte binary
integers representing the difference between the field face value and the standard base
date. Date fields in SAVE files and formatted HOLD files (for example, USAGE WP) are
stored without any display options.

GRAPH. Date fields are not supported as sort fields in ACROSS and BY phrases.

FML. Date fields are not supported within the RECAP statement.

Alphanumeric and Numeric Formats With Date Display Options

In addition to the standard date format, you can also represent a date by using an
alphanumeric, integer, or packed-decimal field with date display options (D, M, Y, and T). Note,
however, that this does not offer the full date support that is provided by the standard date
format.

Alphanumeric and integer fields used with date display options have some date functionality
when used with special date functions, as described in the Creating Reports With WebFOCUS
Language manual.

When representing dates as alphanumeric or integer fields with date display options, you can
specify the year, month, and day. If all three of these elements are present, then the date has
six digits (or eight if the year is presented as four digits), and the USAGE can be:

Format

I6MDY

Display

04/21/98

Describing Data With TIBCO WebFOCUS® Language

 153

The Displayed Data Type: USAGE

Format

I6YMD

P6DMY

I8DMYY

Display

98/04/21

21/04/98

21/04/1998

The number of a month (1 to 12) can be translated to the corresponding month name by
adding the letter T to the format, immediately after the M. For instance:

Format

I6MTDY

I4MTY

I2MT

Data

05/21/98

0698

07

Display

MAY 21 98

JUN 98

JUL

If the date has only the month element, a format of I2MT displays the value 4 as APR, for
example. This is particularly useful in reports where columns or rows are sorted by month.
They then appear in correct calendar order. For example, JAN, FEB, MAR, because the sorting
is based on the numeric, not alphabetical, values. (Note that without the T display option, I2M
is interpreted as an integer with a floating dollar sign.)

Date-Time Formats

The date-time data type supports both the date and time, similar to the timestamp data types
available in many relational data sources.

Date-time fields are stored in eight, ten, or 12 bytes: four bytes for date and either four, six, or
eight bytes for time, depending on whether the format specifies a microsecond or nanosecond.

Computations only allow direct assignment within data types: alpha to alpha, numeric to
numeric, date to date, and date-time to date-time. All other operations are accomplished
through a set of date-time functions. See the Using Functions manual for information on
subroutines for manipulating date-time fields.

154

4. Describing an Individual Field

Date-time formats can also produce output values and accept input values that are compatible
with the ISO 8601:2000 date-time notation standard. A SET parameter and specific formatting
options enable this notation.

Syntax:

How to Enable ISO Standard Date-Time Notation

SET DTSTANDARD = {OFF|ON|STANDARD|STANDARDU}

where:

OFF

Does not provide compatibility with the ISO 8601:2000 date-time notation standard. OFF is
the default value.

ON|STANDARD

Enables recognition and output of the ISO standard formats, including use of T as the
delimiter between date and time, use of period or comma as the delimiter of fractional
seconds, use of Z at the end of universal times, and acceptance of inputs with time zone
information. STANDARD is a synonym for ON.

STANDARDU

Enables ISO standard formats (like STANDARD) and also, where possible, converts input
strings to the equivalent universal time (formerly known as Greenwich Mean Time), thus
enabling applications to store all date-time values in a consistent way.

Example:

Using SET DTSTANDARD

The following request displays date-time values input in ISO 8601:2000 date-time standard
formats. With SET DTSTANDARD=OFF, the request terminates with a (FOC177): INVALID DATE
CONSTANT:

Describing Data With TIBCO WebFOCUS® Language

 155

The Displayed Data Type: USAGE

SET DTSTANDARD = &STAND
DEFINE FILE EMPLOYEE
-* The following input is format YYYY-MM-DDThh:mm:ss.sTZD
DT1/HYYMDs  =     DT(2004-06-01T19:20:30.45+01:00);
-* The following input has comma as the decimal separator
DT2/HYYMDs  =     DT(2004-06-01T19:20:30,45+01:00);
DT3/HYYMDs  =     DT(20040601T19:20:30,45);
DT4/HYYMDUs =     DT(2004-06-01T19:20:30,45+01:00);
END
TABLE FILE EMPLOYEE
HEADING CENTER
"DTSANDARD = &STAND "
" "
SUM CURR_SAL NOPRINT DT1 AS 'DT1: INPUT = 2004-06-01T19:20:30.45+01:00'
OVER DT2 AS 'DT2: INPUT = 2004-06-01T19:20:30,45+01:00'
OVER DT3 AS 'DT3: INPUT = 20040601T19:20:30,45'
OVER DT4 AS 'DT4: OUTPUT  FORMAT HYYMDUs'
END

With DTSTANDARD= STANDARD, the output shows that the input values were accepted, but
the time zone offsets in DT1, DT2, and DT4 (+01:00) were ignored on output. The character U
in the format for DT4 causes the T separator to be used between the date and the time:

                      DTSANDARD = STANDARD

DT1: INPUT = 2004-06-01T19:20:30.45+01:00  2004-06-01 19:20:30.450
DT2: INPUT = 2004-06-01T19:20:30,45+01:00  2004-06-01 19:20:30.450
DT3: INPUT = 20040601T19:20:30,45          2004-06-01 19:20:30.450
DT4: OUTPUT  FORMAT HYYMDUs                2004-06-01T19:20:30.450

With DTSTANDARD= STANDARDU, the output shows that the values DT1, DT2, and DT4 were
converted to universal time by subtracting the time zone offsets (+01:00):

                      DTSANDARD = STANDARDU

DT1: INPUT = 2004-06-01T19:20:30.45+01:00  2004-06-01 18:20:30.450
DT2: INPUT = 2004-06-01T19:20:30,45+01:00  2004-06-01 18:20:30.450
DT3: INPUT = 20040601T19:20:30,45          2004-06-01 19:20:30.450
DT4: OUTPUT  FORMAT HYYMDUs                2004-06-01T18:20:30.450

Describing a Date-Time Field

In a Master File, the USAGE (or FORMAT) attribute determines how date-time field values
appear in report output and forms, and how they behave in expressions and functions. For
FOCUS data sources, it also determines how they are stored.

Format type H describes date-time fields. The USAGE attribute for a date-time field contains
the H format code and can identify either the length of the field or the relevant date-time
display options.

156



4. Describing an Individual Field

The MISSING attribute for date-time fields can be ON or OFF. If it is OFF, and the date-time field
has no value, it defaults to blank.

Syntax:

How to Describe a Numeric Date-Time Value Without Display Options

This format is appropriate for alphanumeric HOLD files or transaction files.

USAGE = Hn

where:

n

Is the field length, from 1 to 23, including up to eight characters for displaying the date
and up to nine, 12, or 15 characters for the time. For lengths less than 20, the date is
truncated on the right.

An eight-character date includes four digits for the year, two for the month, and two for the
day of the month, YYYYMMDD.

A nine-character time includes two digits for the hour, two for the minute, two for the
second, and three for the millisecond, HHMMSSsss. The millisecond component
represents the decimal portion of the second to three places.

A twelve-character time includes two digits for the hour, two for the minute, two for the
second, three for the millisecond, and three for the microsecond, HHMMSSsssmmm. The
millisecond component represents the decimal portion of the second value to three
places. The microsecond component represents three additional decimal places beyond
the millisecond value.

A fifteen-character time includes two digits for the hour, two for the minute, two for the
second, three for the millisecond, three for the microsecond and three for the nanosecond,
HHMMSSsssmmmnnn. The millisecond component represents the decimal portion of the
second value to three places. The microsecond component represents three additional
decimal places beyond the millisecond value. The nanosecond component represents
three additional decimal places beyond the microsecond value.

With this format, there are no spaces between the date and time components, no decimal
points, and no spaces or separator characters within either component. The time must be
entered using the 24-hour system. For example, the value 19991231225725333444
represents 1999/12/31 10:57:25.333444PM.

Describing Data With TIBCO WebFOCUS® Language

 157

The Displayed Data Type: USAGE

Syntax:

How to Describe a Time-Only Value

USAGE = Htimefmt1

where:

timefmt1

Is the USAGE format for displaying time only. Hour, minute, and second components are
always separated by colons (:), with no intervening blanks. A time value can have a blank
immediately preceding an am/pm indicator. For information, see Display Options for a Time-
Only Value on page 158.

Reference: Display Options for a Time-Only Value

The following table lists the valid time display options for a time-only USAGE attribute. Assume
the time value is 2:05:27.123456444 a.m.

Option

Meaning

Effect

H

Hour (two digits).

Prints a two-digit hour. For example:

If the format includes the option
a, b, A, or B, the hour value is
from 01 to 12.

Otherwise, the hour value is
from 00 to 23, with 00
representing midnight.

Hour with zero suppression.

If the format includes the option
a, b, A, or B, the hour value is
from 1 to 12.

Otherwise, the hour is from 0 to
23.

USAGE = HH prints 02

Displays the hour with zero suppression. For
example:

USAGE = Hh prints 2

Minute (two digits).

Prints the two-digit minute. For example:

The minute value is from 00 to
59.

USAGE = HHI prints 02:05

h

I

158

Option

Meaning

Effect

4. Describing an Individual Field

i

S

s

m

n

x

A

Minute with zero suppression.

The minute value is from 0 to
59.

Prints the minute with zero suppression.
This cannot be used together with an hour
format (H or h). For example:

USAGE = Hi prints 5

Second (two digits).

Prints the two-digit second. For example:

S: 00 to 59

USAGE = HHIS prints 02:05:27

Millisecond (three digits, after
the decimal point in the
second).

Prints the second to three decimal places.
For example:

USAGE = HHISs prints 02:05:27.123

000 to 999

Microsecond (three additional
digits after the millisecond).

Prints the second to six decimal places. For
example:

000 through 999

USAGE = HSsm prints 27.123456

Nanosecond (three additional
digits after the microsecond).

Prints the second to nine decimal places.
For example:

000 through 999

USAGE = HSsn prints 27.123456444

USAGE = HHI1 prints 02:05:27.1

Instead of using S, s, m, or n,
you can specify up to nine
decimal places for seconds
using the x option, where x is a
number from 1 to 9.
Alternatively, you can use the s,
m, and n formats to display
three, six, or nine decimal
places.

12-hour time display with AM or
PM in uppercase.

Prints the hour from 01 to 12, followed by
AM or PM. For example:

USAGE = HHISA prints 02:05:27AM

Describing Data With TIBCO WebFOCUS® Language

 159

The Displayed Data Type: USAGE

Option

Meaning

Effect

a

B

b

Z

12-hour time display with am or
pm in lowercase.

Prints the hour from 01 to 12, followed by
am or pm. For example:

USAGE = HHISa prints 02:05:27am

12-hour time display with AM or
PM in uppercase, with a blank
space before the AM or PM.

Prints the hour from 01 to 12, followed by a
space and then AM or PM. For example:

USAGE = HHISB prints 02:05:27 AM

12-hour time display with am or
pm in lowercase, with a blank
space before the am or pm.

Prints the hour from 01 to 12, followed by a
space followed by am or pm. For example:

USAGE = HHISb prints 02:05:27 am

24-hour time display with Z to
indicate universal time. Z is
incompatible with AM/PM
output.

Prints the hour from 01 to 24, followed by Z.
For example:

USAGE = HHISZ prints 14:30[:20.99]Z

When the format includes more than one time display option:

The options must appear in the order hour, minute, second, millisecond, microsecond,
nanosecond.

The first option must be either hour, minute, or second.

No intermediate component can be skipped. If hour is specified, the next option must be
minute. It cannot be second.

Note: Unless you specify one of the AM/PM time display options, the time component appears
using the 24-hour system.

Syntax:

How to Describe a Date-Time Value

USAGE = Hdatefmt [separator] [timefmt2]

where:

datefmt

Is the USAGE format for displaying the date portion of the date-time field. For information,
see Display Options for the Date Component of a Date-Time Field on page 161.

160

4. Describing an Individual Field

separator

Is a separator between the date components. The default separator is a slash (/). Other
valid separators are: period (.), hyphen (-), blank (B), or none (N). With translated months,
these separators can only be specified when the k option is not used.

With the STANDARD and STANDARDU settings, the separator for dates is always hyphen.
The separator between date and time is blank by default. However, if you specify the
character U as the separator option, the date and time will be separated by the character
T.

timefmt2

Is the format for a time that follows a date. Time is separated from the date by a blank.
Time components are separated from each other by colons. Unlike the format for time
alone, a time format that follows a date format consists of at most two characters: a
single character to represent all of the time components that appear and, optionally, one
character for an AM/PM option. For information, see Display Options for the Time
Component of a Date-Time Field on page 164.

Reference: Display Options for the Date Component of a Date-Time Field

The date format can include the following display options, as long as they conform to the
allowed combinations. In the following table, assume the date is February 5, 1999.

Option

Meaning

Y

YY

M

MT

Mt

D

d

2-digit year

4-digit year

2-digit month (01 - 12)

Full month name

Short month name

2-digit day

Zero-suppressed day. A blank space replaces the
zero.

Example

99

1999

02

February

Feb

05

 5

Describing Data With TIBCO WebFOCUS® Language

 161

The Displayed Data Type: USAGE

Option

Meaning

Example

e

o

k

Zero-removed day. The day number is shifted to
the left, and any components to the right of this
are shifted to the left.

Requires a date separator.

Zero-removed month. Automatically implements
the e option for a zero-removed day. The month
and day numbers are shifted to the left, and any
components to the right of these are also shifted.

Required a date separator.

For formats in which month or day is followed by
year, and month is translated to a short or full
name, k separates the year from the day with a
comma and blank. Otherwise, the separator is a
blank.

5

5

USAGE = HMtDkYY

prints Feb 05, 1999

Note: Unless you specify one of the AM/PM time display options, the time component uses
the 24-hour system.

Example:

Using Zero Removal for Date-Time Month and Day Numbers

The following request creates the date-time value 01/01/2013. It then displays this value
using:

Normal month and day numbers, format HMDYY.

Month removal and day removal, format HoeYY.

Month removal without day removal (which forces day removal), format HodYY.

162

4. Describing an Individual Field

Day removal without month removal, format HMeYY. Note that month removal is not forced
by day removal.

DEFINE FILE GGSALES
DATE1A/HMDYY = DT(01/01/2013);
DATE1B/HoeYY = DATE1A;
DATE1C/HodYY = DATE1A;
DATE1D/HMeYY = DATE1A;
END
TABLE FILE GGSALES
SUM DOLLARS NOPRINT
DATE1A AS 'HMDYY'
DATE1B AS 'HoeYY'
DATE1C AS 'HodYY'
DATE1D AS 'HMeYY'
ON TABLE SET PAGE NOPAGE
END

The output is:

HMDYY       HoeYY       HodYY       HMeYY
-----       -----       -----       -----
01/01/2013  1/1/2013    1/1/2013    01/1/2013

Example:

Comparing Zero Suppression With Zero Removal

The following request creates two dates with date-time formats in which the date component
has a leading zero (01). In the first date, the day component is the first component and
displays on the left. In the second date, the day component is the second component and
displays in the middle. The request prints these dates:

With all zeros displayed, format HDMYY.

With zero suppression for the day component, format HdMYY.

Describing Data With TIBCO WebFOCUS® Language

 163

The Displayed Data Type: USAGE

With zero removal for the day component, format HeMYY.

DEFINE FILE GGSALES
DATE1A/HDMYY = DT(01/12/2012);
DATE2A/HMDYY = DT(12/01/2012);
DATE1B/HdMYY = DATE1A;
DATE2B/HMdYY = DATE2A;
DATE1C/HeMYY = DATE1A;
DATE2C/HMeYY = DATE2A;
END
TABLE FILE GGSALES
SUM DOLLARS NOPRINT
DATE1A AS 'HDMYY'
DATE2A AS ''      OVER
DATE1B AS 'HdMYY'
DATE2B AS ''      OVER
DATE1C AS 'HeMYY'
DATE2C AS ''
ON TABLE SET PAGE NOPAGE

On the output, the first row shows the date with all zeros displayed. The second row shows
zero suppression of the day number, where the zero has been replaced by a blank space so
that all the components are aligned with the components on row 1. The last row shows zero
removal, where the zero has been removed from the day number, and all of the remaining
characters have been shifted over to the left:

HDMYY  01/12/2012    12/01/2012
HdMYY   1/12/2012    12/ 1/2012
HeMYY  1/12/2012     12/1/2012

Reference: Display Options for the Time Component of a Date-Time Field

The following table lists the valid options. Assume the date is February 5, 1999 and the time
is 02:05:25.444555333 a.m.

Option

Meaning

Example

H

I

S

Prints hour.

Prints hour:minute.

Prints hour:minute:second.

USAGE = HYYMDH prints
1999/02/05 02

USAGE = HYYMDI prints
1999/02/05 02:05

USAGE = HYYMDS prints
1999/02/05 02:05:25

164

Option

Meaning

Example

4. Describing an Individual Field

s

m

n

x

A

a

B

b

Z

Prints hour:minute:second.millisecond.

Prints hour:minute:second.microsecond.

Prints hour:minute:second.nanosecond.

Instead of using S, s, m, or n, you can
specify up to nine decimal places for
seconds using the x option, where x is a
number from 1 to 9. Alternatively, you
can use the s, m, and n formats to
display three, six, or nine decimal
places.

Prints AM or PM. This uses the 12-hour
system and causes the hour to be
printed with zero suppression.

Prints am or pm. This uses the 12-hour
system and causes the hour to be
printed with zero suppression.

Prints AM or PM, preceded by a blank
space. This uses the 12-hour system and
causes the hour to be printed with zero
suppression.

Prints am or pm, preceded by a blank
space. This uses the 12-hour system and
causes the hour to be printed with zero
suppression.

Prints Z to indicate universal time. This
uses the 24-hour system. Z is
incompatible with AM/PM output.

USAGE = HYYMDs prints
1999/02/05 02:05:25.444

USAGE = HYYMDm prints
1999/02/05 02:05:25.444555

USAGE = HYYMDn prints
1999/02/05
02:05:25.444555333

USAGE = HYYMD1 prints
1999/02/05 02:05:25.4

USAGE = HYYMDSA prints
1999/02/05 2:05:25AM

USAGE = HYYMDSa prints
1999/02/05 2:05:25am

USAGE = HYYMDSB prints
1999/02/05 2:05:25 AM

USAGE = HYYMDSb prints
1999/02/05 2:05:25 am

USAGE = HHISZ prints 14:30[:
20.99]Z

Describing Data With TIBCO WebFOCUS® Language

 165

The Displayed Data Type: USAGE

The date components can be in any of the following combinations and order:

Year-first combinations: Y, YY, YM, YYM, YMD, YYMD.

Month-first combinations: M, MD, MY, MYY, MDY, MDYY.

Day-first combinations: D, DM, DMY, DMYY.

Reference: Date-Time Usage Notes

In order to have a time component, you must have a day component.

If you use the k option, you cannot change the date separator.

Character Format AnV

The character format AnV is supported in Master Files for FOCUS, XFOCUS, and relational data
sources. This format is used to represent the VARCHAR (variable length character) data types
supported by relational database management systems.

For relational data sources, AnV keeps track of the actual length of a VARCHAR column. This
information is important when the value is used to populate a VARCHAR column in a different
RDBMS. It affects whether trailing blanks are retained in string concatenation and, for Oracle,
string comparisons (the other relational engines ignore trailing blanks in string comparisons).

In a FOCUS or XFOCUS data source, AnV does not provide true variable length character
support. It is a fixed-length character field with two extra leading bytes to contain the actual
length of the data stored in the field. This length is stored as a short integer value occupying
two bytes. Trailing blanks entered as part of an AnV field count in its length.

Note: Because of the two bytes of overhead and the additional processing required to strip
them, AnV format is not recommended for use in non-relational data sources.

Syntax:

How to Specify AnV Fields in a Master File

FIELD=name, ALIAS=alias, USAGE=AnV [,ACTUAL=AnV] , $

where:

n

Is the size (maximum length) of the field. It can be from 1 to 4093. Note that because of
the additional two bytes used to store the length, an A4093V field is actually 4095 bytes
long. A size of zero (A0V) is not supported. The length of an instance of the field can be
zero.

166

4. Describing an Individual Field

Note: HOLD FORMAT ALPHA creates an ACTUAL format of AnW in the Master File. See
Propagating an AnV Field to a HOLD File on page 168.

Example:

Specifying the AnV Format in a Master File

The following represents a VARCHAR field in a Master File for a Db2 data source with size 200:

$ VARCHAR FIELD USING AnV
  FIELD=VARCHAR200, ALIAS=VC200, USAGE=A200V, ACTUAL=A200V,MISSING=ON ,$

The following represents an AnV field in a Master File for a FOCUS data source with size 200:

FIELD=ALPHAV, ALIAS=AV200, USAGE=A200V, MISSING=ON ,$

If a data source has an AnV field, specify the following in order to create a HOLD FORMAT
ALPHA file without the length designator:

FIELD=ALPHA, USAGE=A25, ACTUAL=A25V, $

or

DEFINE ...
  ALPHA/A25 = VARCHAR ;
END

or

COMPUTE ALPHA/A25 = VARCHAR ;

In order to alter or create a Master File to include AnV, the data must be converted and the
length added to the beginning of the field. For example, issue a HOLD command when the field
is described as follows:

FIELD=VARCHAR, ,USAGE=A25V, ACTUAL=A25, $

or

DEFINE ...
  VARCHAR/A25V = ALPHA ;
END

or

COMPUTE VARCHAR/A25V = ALPHA ;

Reference: Usage Notes for AnV Format

AnV can be used anywhere that An can be used, except for the restrictions listed in these
notes.

Describing Data With TIBCO WebFOCUS® Language

 167

The Displayed Data Type: USAGE

Full FOCUS and SQL operations are supported with this data type, including CREATE FILE
for relational data sources.

Joins are not supported between An and AnV fields.

DBCS characters are supported. As with the An format, the number of characters must fit
within the 4K data area.

COMPUTE and DEFINE generate the data type specified on the left-hand side.

Conversion between AnV and TX fields is not supported.

AnV fields cannot have date display options.

Reference: Propagating an AnV Field to a HOLD File

When a user propagates an AnV field to a sequential data source using the HOLD FORMAT
ALPHA command, the two-byte integer length is converted to a six-digit alphanumeric length.
The field in the HOLD file consists of this six-digit number followed by the character data. The
format attributes for this field are:

... USAGE=AnV, ACTUAL=AnW

AnW is created as a by-product of HOLD FORMAT ALPHA. However, it can be read and used for
input as necessary. The number of bytes occupied by this field in the HOLD file is 6+n.

Example:

Propagating an AnV Field to a HOLD File

The A39V field named TITLEV, is propagated to the HOLD file as:

FIELDNAME = TITLEV ,E03 ,A39V ,A39W ,$

In a binary HOLD file, the USAGE and ACTUAL formats are AnV, although the ACTUAL format
may be padded to a full 4-byte word. The number of bytes occupied by this field in the HOLD
file is 2+n.

When an AnV field is input into a data source, all bytes in the input field beyond the given
length are ignored. These bytes are set to blanks as part of the input process.

When a user creates a relational data source using the HOLD FORMAT sqlengine command,
the AnV field generates a VARCHAR column in the relational data source.

For example, the A39V field named TITLEV, is propagated to a HOLD FORMAT DB2 file as:

FIELDNAME = 'TITLEV', 'TITLEV', A39V, A39V ,$

168

4. Describing an Individual Field

Text Field Format

You can store any combination of characters as a text field.

Syntax:

How to Specify a Text Field in a Master File

FIELD = fieldname, ALIAS = aliasname, USAGE = TXn[F],$

where:

fieldname

Is the name you assign the text field.

aliasname

Is an alternate name for the field name.

n

Is the output display length in TABLE for the text field. The display length may be between
1 and 256 characters.

All letters, digits, and special characters can be stored with this format. The following are
some sample text field formats.

Format

Display

TX50

TX35

This course provides the DP professional with the skills
needed to create, maintain, and report from FOCUS data
sources.

This course provides the DP professional with the skills
needed to create, maintain, and report from FOCUS data
sources.

The standard edit options are not available for the text field format.

Reference: Usage Notes for Text Field Format

Conversion between text and alphanumeric fields is supported in DEFINE and COMPUTE
commands.

Multiple text fields are supported, and they and be anywhere in the segment.

Describing Data With TIBCO WebFOCUS® Language

 169

The Stored Data Type: ACTUAL

The Stored Data Type: ACTUAL

ACTUAL describes the type and length of data as it is actually stored in the data source. While
some data types, such as alphanumeric, are universal, others differ between different types of
data sources. Some data sources support unique data types. For this reason, the values you
can assign to the ACTUAL attribute differ for each type of data source.

ACTUAL Attribute

This attribute describes the type and length of your data as it actually exists in the data
source. The source of this information is your existing description of the data source (such as
a COBOL FD statement). The ACTUAL attribute is one of the distinguishing characteristics of a
Master File for non-FOCUS data sources. Since this attribute exists only to describe the format
of a non-FOCUS data structure, it is not used in the Master File of a FOCUS data structure.

If your data source has a date stored as an alphanumeric field and you need to convert it to a
WebFOCUS date for sorting or aggregation in a report, you can use the DATEPATTERN attribute
in the Master File. WebFOCUS then uses the pattern specified to convert the alphanumeric
date to a WebFOCUS date.

Syntax:

How to Specify the ACTUAL Attribute

ACTUAL = format

where:

format

Consists of values taken from the following table, which shows the codes for the types of
data that can be read.

ACTUAL Type

Meaning

DATE

Four-byte integer internal format, representing the difference
between the date to be entered and the date format base date.

170

4. Describing an Individual Field

ACTUAL Type

Meaning

An

D8

F4

Hn

In

M8

Pn

Where n = 1-4095 for fixed-format sequential and VSAM data
sources, and 1-256 for other non-FOCUS data sources.
Alphanumeric characters A-Z, 0-9, and the special characters in
the EBCDIC display mode.

An accepts all the date-time string formats, as well as the Hn
display formats. ACTUAL=An also accepts a date-time field as it
occurs in an alphanumeric HOLD file or SAVE file.

Alphanumeric format can also be used with the hexadecimal
USAGE format (U). The length of the ACTUAL has to be twice the
length of the USAGE.

Double-precision, floating-point numbers, stored internally in eight
bytes.

Single-precision, floating-point numbers, stored internally in four
bytes.

H8, H10, or H12 accepts a date-time field as it occurs in a binary
HOLD file or SAVB file.

Binary integers:

I1 = single-byte binary integer.

I2 = half-word binary integer (2 bytes).

I4 = full-word binary integer (4 bytes).

I8 = double-word binary integer (8 bytes).

Note: The USAGE must be P or D. Decimals are honored, with
proper conversion to the decimals of the P or D USAGE.

Decimal precision floating-point numbers (MATH), stored
internally in eight bytes.

Where n = 1-16. Packed decimal internal format. n is the number
of bytes, each of which contains two digits, except for the last
byte which contains a digit and the sign (+ or -). For example, P6
means 11 digits plus a sign.

Describing Data With TIBCO WebFOCUS® Language

 171

The Stored Data Type: ACTUAL

ACTUAL Type

Meaning

STRING

X16

Zn

For Relational data sources that have a STRING data type. There
is no length specification.

Extended decimal precision floating-point numbers (XMATH),
stored internally in 16 bytes.

Where n = 1-31. Zoned decimal internal format. n is the number
of digits, each of which takes a byte of storage. The last digit
contains a digit and the sign.

If the field contains an assumed decimal point, represent the
field with an ACTUAL format of Zn and a USAGE format of Pm.d,
where m is the total number of digits in the display plus the
assumed decimal point, d is the number of decimal places, and
m must be at least 1 greater than the value of n. For example, a
field with ACTUAL=Z5 and one decimal place needs USAGE=P6.1
(or P7.1, or greater).

Note:

Unless your data source is created by a program, all of the characters are either of type A
(alphanumeric) or type Z (zoned decimal).

ACTUAL formats supported for date-time values are An, H8, H10, and H12. An accepts all
the date-time string formats, as well as the Hn USAGE display format. ACTUAL=H8, H10, or
H12 accepts a date-time field as it occurs in a binary HOLD file or SAVB file. ACTUAL=An
accepts a date-time field as it occurs in an alphanumeric HOLD file or SAVE file.

If you create a binary HOLD file from a data source with a date-time field, the ACTUAL
format for that field is of the form Hn. If you create an alphanumeric HOLD file from a data
source with a date-time field, the ACTUAL format for that field is of the form An.

172

4. Describing an Individual Field

Reference: ACTUAL to USAGE Conversion

The following conversions from ACTUAL format to USAGE (display) format are automatically
handled and do not require invoking a function:

ACTUAL

USAGE

A

D

DATE

F

H

I

M

P

X

Z

A, D, F, I, P, date format, date-time format

D

date format

F

H

I, date format

M

P, date format

X

D, F, I, P

Reference: COBOL Picture to USAGE Format Conversion

The following table shows the USAGE and ACTUAL formats for COBOL, FORTRAN, PL1, and
Assembler field descriptions.

COBOL USAGE
FORMAT

BYTES OF COBOL
PICTURE

INTERNAL
STORAGE

ACTUAL
FORMAT

USAGE
FORMAT

DISPLAY
DISPLAY
DISPLAY
DISPLAY

X(4)
S99
9(5)V9
99

4
2
6
2

A4
Z2
Z6.1
A2

A4
P3
P8.1
A2

Describing Data With TIBCO WebFOCUS® Language

 173

The Stored Data Type: ACTUAL

COBOL USAGE
FORMAT

BYTES OF COBOL
PICTURE

INTERNAL
STORAGE

ACTUAL
FORMAT

USAGE
FORMAT

COMP
COMP
COMP*
COMP
COMP-1**

S9
S9(4)
S9(5)
S9(9)
—

COMP-2***

—

COMP-3
COMP-3
COMP-3

FIXED
BINARY(7)
(COMP-4)

9
S9V99
9(4)V9(3)

B or XL1

4
4
4
4
4

8

8
8
8

8

I2
I2
I4
I4
F4

D8

P1
P2
P4

I4

I1
I4
I5
I9
F6

D15

P1
P5.2
P8.3

I7

* Equivalent to INTEGER in FORTRAN, FIXED BINARY(31) in PL/1, and F in Assembler.

** Equivalent to REAL in FORTRAN, FLOAT(6) in PL/1, and E in Assembler.

*** Equivalent to DOUBLE PRECISION or REAL*8 in FORTRAN, FLOAT(16) in PL/1, and D in
Assembler.

Note:

1. The USAGE lengths shown are minimum values. They may be larger if desired. Additional

edit options may also be added.

2. In USAGE formats, an extra character position is required for the minus sign if negative

values are expected.

3. PICTURE clauses are not permitted for internal floating-point items.

4. USAGE length should allow for maximum possible number of digits.

5. In USAGE formats, an extra character position is required for the decimal point.

For information about using ACTUAL with sequential, VSAM, and ISAM data sources, see
Describing a Sequential, VSAM, or ISAM Data Source on page 231. For other types of data
sources, see your adapter documentation. Note that FOCUS data sources do not use the
ACTUAL attribute, and instead rely upon the USAGE attribute to specify both how a field is
stored and formatted.

174

4. Describing an Individual Field

Adding a Geographic Role for a Field

When a field represents a geographic location or coordinate, you can identify its correct
geographic role using the GEOGRAPHIC_ROLE attribute in the Master File.

GEOGRAPHIC_ROLE Attribute

This attribute specifies the type of location intelligence data represented by the field.

Syntax:

How to Specify a Geographic Role

GEOGRAPHIC_ROLE = georole

where:

georole

Is a valid geographic role. Geographic roles can be names, postal codes, ISO (International
Organization for Standardization) codes, FIPS (Federal Information Processing Standards)
codes, or NUTS (Nomenclature of Territorial Units for Statistics ) codes. The following is a
list of supported geographic roles.

ADDRESS_FULL. Full address.

ADDRESS_LINE. Number and street name.

CITY. City name.

CONTINENT. Continent name.

CONTINENT_ISO2. Continent ISO-3166 code.

COUNTRY. Country name.

COUNTRY_FIPS. Country FIPS code.

COUNTRY_ISO2. Country ISO-3166-2 code.

COUNTRY_ISO3. Country ISO-3166-3 code.

GEOMETRY_AREA. Geometry area.

GEOMETRY_LINE. Geometry line.

GEOMETRY_POINT. Geometry point.

LATITUDE. Latitude.

LONGITUDE. Longitude.

Describing Data With TIBCO WebFOCUS® Language

 175

Null or MISSING Values: MISSING

NUTS0. Country name (NUTS level 0).

NUTS0_CC. Country code (NUTS level 0).

NUTS1. Region name (NUTS level 1).

NUTS1_CC. Region code (NUTS level1).

NUTS2. Province name (NUTS level 2).

NUTS2_CC. Province code (NUTS level 2).

NUTS3. District name (NUTS level 3).

NUTS3_CC. District code (NUTS level 3).

POSTAL_CODE. Postal code.

STATE. State name.

STATE_FIPS. State FIPS code.

STATE_ISO_SUB. US State ISO subdivision code.

USSCITY. US city name.

USCITY_FIPS. US city FIPS code.

USCOUNTY. US county name.

USCOUNTY_FIPS. US county FIPS code.

USSTATE. US state name.

USSTATE_ABBR. US state abbreviation.

USSTATE_FIPS. US state FIPS code.

ZIP3. US 3-digit postal code.

ZIP5. US 5-digit postal code.

Null or MISSING Values: MISSING

If a segment instance exists but no data has been entered into one of its fields, that field has
no value. Some types of data sources represent this absence of data as a blank space ( ) or
zero (0), but others explicitly indicate an absence of data with a null indicator or as a special
null value. Null values (sometimes known as missing data) are significant in reporting
applications, especially those that perform aggregating functions, such as averaging.

176

4. Describing an Individual Field

If your type of data source supports missing data, as do FOCUS data sources and most
relational data sources, then you can use the optional MISSING attribute to enable null values
to be entered into and read from a field. MISSING plays a role when you:

Create new segment instances. If no value is supplied for a field for which MISSING has
been turned ON in the Master File or in a DEFINE or COMPUTE definition, then the field is
assigned a missing value.

Generate reports. If a field with a null value is retrieved, the field value is not used in
aggregating calculations, such as averaging and summing. If the report calls for the field
value to display, a special character appears to indicate a missing value. The default
character is a period (.), but you can change it to any character string you wish using the
SET NODATA command or the SET HNODATA command for HOLD files, as described in the
Developing Reporting Applications manual.

Syntax:

How to Specify a Missing Value

MISSING = {ON|OFF}

where:

ON

Distinguishes a missing value from an intentionally entered blank or zero when creating
new segment instances and reporting.

OFF

Does not distinguish between missing values and blank or zero values when creating new
segment instances and reporting. OFF is the default value.

Reference: Usage Notes for MISSING

Note the following rules when using MISSING:

Alias. MISSING does not have an alias.

Value. It is recommended that you set the MISSING attribute to match the field predefined
null characteristic (whether the characteristic is explicitly set when the data source is
created, or set by default). For example, if a relational table column has been created with
the ability to accept null data, describe the field with the MISSING attribute set to ON so
that its null values are correctly interpreted.

FOCUS data sources also support MISSING=ON, which assigns sets an internal flag for
missing values.

Describing Data With TIBCO WebFOCUS® Language

 177

Describing an FML Hierarchy

Changes. You can change the MISSING attribute at any time. Note that changing MISSING
does not affect the actual stored data values that were entered using the old setting.
However, it does affect how that data is interpreted. If null data is entered when MISSING
is turned ON, and then MISSING is switched to OFF, the data originally entered as null is
interpreted as blanks (for alphanumeric fields) or zeroes (for numeric fields). The only
exception is FOCUS data sources, in which the data originally entered as missing is
interpreted as the internal missing value for that data type, which is described in Describing
a FOCUS Data Source on page 293.

Using a Missing Value

Consider the field values shown in the following four records:

1

3

If you average these values without declaring the field with the MISSING attribute, a value of
zero is automatically be supplied for the two blank records. Thus, the average of these four
records is (0+0+1+3)/4, or 1. If you turn MISSING to ON, the two blank records are not used
in the calculation, so the average is (1+3)/2, or 2.

Missing values in a unique segment are also automatically supplied with a zero, a blank, or a
missing value depending on the MISSING attribute. What distinguishes missing values in
unique segments from other values is that they are not stored. You do have to supply a
MISSING attribute for fields in unique segments on which you want to perform counts or
averages.

The Creating Reports With WebFOCUS Language manual contains a more thorough discussion
of using null values (sometimes called missing data) in reports. It includes alternative ways of
distinguishing these values in reports, such as using the WHERE phrase with MISSING
selection operators, and creating virtual fields using the DEFINE FILE command with the SOME
or ALL phrase.

Describing an FML Hierarchy

The Financial Modeling Language (FML) supports dynamic reporting against hierarchical data
structures.

You can define the hierarchical relationships between fields in a Master File and automatically
display these fields using FML. You can also provide descriptive captions to appear in reports
in place of the specified hierarchy field values.

178



4. Describing an Individual Field

In the Master File, use the PROPERTY=PARENT_OF and REFERENCE=hierarchyfld attributes to
define the hierarchical relationship between two fields.

The parent and child fields must have the same FORMAT or USAGE, and their relationship
should be hierarchical. The formats of the parent and child fields must both be numeric or both
alphanumeric.

Syntax:

How to Specify a Hierarchy Between Fields in a Master File

FIELD=parentfield,...,PROPERTY=PARENT_OF, REFERENCE=[seg.]hierarchyfld,$

where:

parentfield

Is the parent field in the hierarchy.

PROPERTY=PARENT_OF

Identifies this field as the parent of the referenced field in a hierarchy.

These attributes can be specified on every field. Therefore, multiple hierarchies can be
defined in one Master File. However, an individual field can have only one parent. If
multiple fields have PARENT_OF attributes for the same hierarchy field, the first parent
found by traversing the structure in top-down, left-to-right order is used as the parent.

seg

Is the segment location of the hierarchy field. Required if more than one segment has a
field named hierarchyfield.

hierarchyfld

Is the child field in the hierarchy.

PARENT_OF is also allowed on a virtual field in the Master File:

DEFINE name/fmt=expression;,PROPERTY=PARENT_OF,REFERENCE=hierarchyfld,$

Describing Data With TIBCO WebFOCUS® Language

 179

Describing an FML Hierarchy

Syntax:

How to Assign Descriptive Captions for Hierarchy Field Values

The following attributes specify a caption for a hierarchy field in a Master File

FIELD=captionfield,..., PROPERTY=CAPTION, REFERENCE=[seg.]hierarchyfld,$

where:

captionfield

Is the name of the field that contains the descriptive text for the hierarchy field. For
example, if the employee ID is the hierarchy field, the last name may be the descriptive
text that appears on the report in place of the ID.

PROPERTY=CAPTION

Signifies that this field contains a descriptive caption that appears in place of the hierarchy
field values.

A caption can be specified for every field, but an individual field can have only one caption.
If multiple fields have CAPTION attributes for the same hierarchy field, the first parent
found by traversing the structure in top-down, left-to-right order is used as the caption.

seg

Is the segment location of the hierarchy field. Required if more than one segment has a
field named hierarchyfield.

hierarchyfld

Is the hierarchy field.

CAPTION is also allowed on a virtual field in the Master File:

DEFINE name/format=expression;,PROPERTY=CAPTION,REFERENCE=hierarchyfld,$

180

4. Describing an Individual Field

Example:

Defining a Hierarchy in a Master File

The CENTGL Master File contains a chart of accounts hierarchy. The field
GL_ACCOUNT_PARENT is the parent field in the hierarchy. The field GL_ACCOUNT is the
hierarchy field. The field GL_ACCOUNT_CAPTION can be used as the descriptive caption for the
hierarchy field:

FILE=CENTGL     ,SUFFIX=FOC
SEGNAME=ACCOUNTS,SEGTYPE=S01
FIELDNAME=GL_ACCOUNT,           ALIAS=GLACCT,  FORMAT=A7,
          TITLE='Ledger,Account', FIELDTYPE=I, $
FIELDNAME=GL_ACCOUNT_PARENT,    ALIAS=GLPAR,   FORMAT=A7,
          TITLE=Parent,
          PROPERTY=PARENT_OF, REFERENCE=GL_ACCOUNT, $
FIELDNAME=GL_ACCOUNT_TYPE,      ALIAS=GLTYPE,  FORMAT=A1,
          TITLE=Type,$
FIELDNAME=GL_ROLLUP_OP,         ALIAS=GLROLL,  FORMAT=A1,
          TITLE=Op, $
FIELDNAME=GL_ACCOUNT_LEVEL,     ALIAS=GLLEVEL, FORMAT=I3,
          TITLE=Lev, $
FIELDNAME=GL_ACCOUNT_CAPTION,   ALIAS=GLCAP,   FORMAT=A30,
          TITLE=Caption,
          PROPERTY=CAPTION,   REFERENCE=GL_ACCOUNT, $
FIELDNAME=SYS_ACCOUNT,          ALIAS=ALINE,   FORMAT=A6,
          TITLE='System,Account,Line', MISSING=ON, $

Defining a Dimension: WITHIN

The OLAP model organizes data structures by predefining dimensions in the Master File, using
the field name attribute WITHIN. A dimension is a group or list of related fields called
elements.

The WITHIN attribute enables drill up and drill down functionality on hierarchical dimensions.
You can manipulate a report by selecting an OLAP-enabled field and drilling down to view other
levels of a dimension hierarchy.

For example, a hierarchy of sales regions can be defined in the Master File as the GEOGRAPHY
dimension and can include the following fields (elements): Region, State, and City in
descending order. Region, the highest element in the hierarchy, would contain a list of all of
the Regions within the GEOGRAPHY dimension. State, the second highest element in the
hierarchy, would contain a list of all available States within Region, and so on. Dimensions can
be defined in the Master File for any supported data source.

Describing Data With TIBCO WebFOCUS® Language

 181

Defining a Dimension: WITHIN

The combination, or matrix, of two or more dimensional hierarchies in an OLAP-enabled data
source is called multi-dimensional. For example, although products are sold within states they
need not be grouped in the same dimension as states. Instead, the elements Product
Category and Product Name likely would be grouped in a dimension called PRODUCT. State
would be a member of the GEOGRAPHY dimension that also can include Region and City.
These dimensions are combined in a matrix so that the intersections of their criteria provide
specific values, for example, sales of coffee in the Northeast region.

You can specify a list of acceptable values for each dimension element (field) using the
ACCEPT attribute. This is done using either a hard coded list in the Master File or a lookup file.
For more information on the ACCEPT attribute, see Validating Data: ACCEPT on page 186.

Syntax:

How to Define a Dimension

WITHIN='*dimensionname'
WITHIN=field

where:

'*dimensionname'

Is the name of the dimension. The dimension is defined in the field declaration for the field
that is at the top of the hierarchy. The name must be preceded by an asterisk and
enclosed within single quotation marks. The name must start with a letter and can consist
of any combination of letters, digits, underscores, or periods. Avoid using special
characters and embedded blanks.

field

Is used to define the hierarchical relationship among additional elements to be included in
a given dimension. After the dimension name is defined at the top of the hierarchy, each
element (field) uses the WITHIN attribute to link to the field directly above it in the
hierarchy. The WITHIN attribute can refer to a field either by its field name or its alias. Note
that a given field may participate in only one dimension, and two fields cannot reference
the same higher level field.

182

Example:

Defining a Dimension

The following example shows how to define the PRODUCT dimension in the OSALES Master
File.

4. Describing an Individual Field

PRODUCT Dimension
           ===> Product Category
               ===> Product Name
FILENAME=OSALES,  SUFFIX=FOC
  SEGNAME=SALES01,  SEGTYPE=S1
     FIELD=PRODCAT,    ALIAS=PCAT,     FORMAT=A11,
       WITHIN='*PRODUCT',$
     FIELD=PRODNAME,   ALIAS=PNAME,    FORMAT=A16,
       WITHIN=PRODCAT,$

Example:

Defining Multiple Dimensions

The following annotated example shows how to define the dimensions, PRODUCT,
GEOGRAPHY, and TIME in the OSALES Master File.

PRODUCT Dimension
           ===> Product Category
               ===> Product Name
GEOGRAPHY Dimension
           ===> Region
               ===> State
                   ===> City
                         ===> Store Name (from the OSTORES Master File)
TIME Dimension
           ===> Year
               ===> Quarter
                   ===> Month
                       ===> Date

Describing Data With TIBCO WebFOCUS® Language

 183

Defining a Dimension: WITHIN

OSALES Master File

   FILENAME=OSALES, SUFFIX=FOC
    SEGNAME=SALES01, SEGTYPE=S1
    FIELD=SEQ_NO,    ALIAS=SEQ,   FORMAT=I5,   TITLE='Sequence#',
     DESC='Sequence number in database',$
    FIELD=PRODCAT,   ALIAS=PCAT,  FORMAT=A11,INDEX=I, TITLE='Category',
     DESC='Product category',
     ACCEPT='Coffee' OR 'Food' OR 'Gifts',
1.      WITHIN='*PRODUCT',$
    FIELD=PRODCODE, ALIAS=PCODE, FORMAT=A4, INDEX=I, TITLE='Product ID',
     DESC='Product Identification code (for sale)',$
    FIELD=PRODNAME, ALIAS=PNAME, FORMAT=A16,         TITLE='Product',
     DESC='Product name',
2.   ACCEPT='Espresso' OR 'Latte' OR 'Cappuccino' OR 'Scone' OR
            'Biscotti' OR 'Croissant' OR 'Mug' OR 'Thermos' OR
            'Coffee Grinder' OR 'Coffee Pot',
        WITHIN=PRODCAT,$
    FIELD=REGION,   ALIAS=REG,   FORMAT=A11, INDEX=I,TITLE='Region',
     DESC='Region code',
     ACCEPT='Midwest' OR 'Northeast' OR 'Southwest' OR 'West',
3.      WITHIN='*GEOGRAPHY',$
    FIELD=STATE,    ALIAS=ST,    FORMAT=A2, INDEX=I,TITLE='State',
     DESC='State',
4.   ACCEPT=(OSTATE),
        WITHIN=REGION,$
    FIELD=CITY,      ALIAS=CTY,    FORMAT=A20,        TITLE='City',
     DESC='City',
        WITHIN=STATE,$
    FIELD=STORE_CODE, ALIAS=STCD,  FORMAT=A5, INDEX=I, TITLE='Store ID',
     DESC='Store identification code (for sale)',$
    FIELD=DATE,       ALIAS=DT,    FORMAT=I8YYMD,      TITLE='Date',
     DESC='Date of sales report',
        WITHIN=MO,$
5.  FIELD=UNITS,     ALIAS=UN,    FORMAT=I8,     TITLE='Unit Sales',
     DESC='Number of units sold',$
    FIELD=DOLLARS,    ALIAS=DOL,   FORMAT=I8,     TITLE='Dollar Sales',
     DESC='Total dollar amount of reported sales',$
    FIELD=BUDUNITS,   ALIAS=BUNIITS, FORMAT=I8,   TITLE='Budget Units',
     DESC='Number of units budgeted',$
    FIELD=BUDDOLLARS, ALIAS=BDOLLARS,FORMAT=I8,   TITLE='Budget Dollars',
     DESC='Total sales quota in dollars',$

184

4. Describing an Individual Field

6. DEFINE ADATE/A8 = EDIT(DATE);$
   DEFINE YR/I4 = EDIT (EDIT(ADATE,'9999$$$$')); WITHIN='*TIME',$
   DEFINE MO/I2 = EDIT (EDIT(ADATE,'$$$$99$$')); WITHIN=QTR,$
   DEFINE QTR/I1 = IF MO GE 1 AND MO LE 3
     THEN 1 ELSE IF MO GE 4 AND MO LE 6
     THEN 2 ELSE IF MO GE 7 AND MO LE 9
     THEN 3 ELSE IF MO GE 10 AND MO LE 12
     THEN 4 ELSE 0;
     WITHIN=YR,$
7. SEGNAME = STORES01, SEGTYPE = KU, PARENT = SALES01,
     CRFILE = OSTORES, CRKEY = STORE_CODE, $

1. Declares the PRODUCT dimension. The name must be preceded by an asterisk and

enclosed within single quotation marks.

2. A list of acceptable values may be defined for each dimension element (field), if you wish.
You specify the ACCEPT attribute using either a hard coded list in the Master File or an
external flat file. The list of acceptable values is presented to you as possible selection
criteria values. In this example, the value for the product name must be Espresso, Latte,
Cappuccino, Scone, Biscotti, Croissant, Mug, Thermos, Coffee Grinder, or Coffee Pot. For
more information on the ACCEPT attribute, see Specifying Acceptable Values for a
Dimension on page 190.

3. Declares the GEOGRAPHY dimension and defines the dimension hierarchy for GEOGRAPHY:
Region within GEOGRAPHY (top of the hierarchy), State within Region, and City within State.

4. In this example, the ACCEPT attribute is using an external flat file (OSTATE) to determine all

of the possible data values for state (field ST).

5. The four fields, UNITS, DOLLARS, BUDUNITS, and BUDDOLLARS, are examples of measure
fields. A measure field is used for analysis that typically defines how much or how many.
For example, Units, Dollars, Budget Units, and Budget Dollars are measures that specify
how many units were sold, the total dollar amount of reported sales, how many units were
budgeted, and total sales quota in dollars, respectively.

Describing Data With TIBCO WebFOCUS® Language

 185

Validating Data: ACCEPT

6. Shows the following:

Virtual fields may be included at any level in a dimension. In this example, the fields YR,
MO, and QTR are defined within the TIME dimension. The WITHIN attribute for a virtual field
must be placed on the same line as the semicolon that ends the expression.

How to define the dimension hierarchy for the TIME dimension: Year within Time, Quarter
within Year, Month within Quarter, Date within Month.

Fields in a hierarchy can occur in any order in the Master File.

7. Dimensions may span a dynamic or static JOIN structure using a qualified name. In this
example, the OSALES data source is statically cross-referenced to the OSTORES data
source using the common field STORE_CODE. Through this linkage, the OLAP application
can retrieve the value for store name from the OSTORES data source. Note that
STORE_NAME in the OSTORES Master File is an element of the GEOGRAPHY dimension
that was defined in the OSALES Master File. The following is the OSTORES Master File:

FILENAME=OSTORES, SUFFIX=FOC
SEGNAME=STORES01, SEGTYPE=S1
 FIELD=STORE_CODE, ALIAS=STCD,  FORMAT=A5, INDEX=I,TITLE='Store ID',
   DESC='Franchisee ID Code',$
 FIELD=STORE_NAME, ALIAS=SNAME, FORMAT=A23,  TITLE='Store Name',
   DESC='Store Name', WITHIN=SALES01.CITY,$
 FIELD=ADDRESS1,   ALIAS=ADDR1, FORMAT=A19,  TITLE='Contact',
   DESC='Franchisee Owner',$
 FIELD=ADDRESS2,   ALIAS=ADDR2, FORMAT=A31,  TITLE='Address',
   DESC='Street Address',$
 FIELD=CITY,       ALIAS=CTY,   FORMAT=A22,  TITLE='City',
   DESC='City',$
 FIELD=STATE,      ALIAS=ST,    FORMAT=A2,   TITLE='State',
   DESC='State',$
 FIELD=ZIP,        ALIAS=ZIP,   FORMAT=A6,   TITLE='Zip Code',
   DESC='Postal Code',$

Virtual fields may be included at any level in a dimension. In this example, the fields YR,
MO, and QTR are defined within the TIME dimension. The WITHIN attribute for a virtual field
must be placed on the same line as the semicolon that ends the expression.

How to define the dimension hierarchy for the TIME dimension: Year within Time, Quarter
within Year, Month within Quarter, Date within Month.

Fields in a hierarchy can occur in any order in the Master File.

Validating Data: ACCEPT

ACCEPT is an optional attribute that you can use to validate data as it is entered into a
parameter prompt screen.

186

4. Describing an Individual Field

Note: Suffix VSAM and FIX data sources may use the ACCEPT attribute to specify multiple
RECTYPE values, which are discussed in Describing a Sequential, VSAM, or ISAM Data Source
on page 231.

The ACCEPT attribute supports the following types of operations:

ACCEPT = value1 OR value2 ...

This option is used to specify one or more acceptable values.

ACCEPT = value1 TO value2

This option is used to specify a range of acceptable values.

ACCEPT = FIND

This option is used to validate incoming transaction data against a value from a FOCUS
data source when performing maintenance operations on another data source. FIND is only
supported for FOCUS data sources and does not apply to OLAP-enabled synonyms. Note
also that, in the Maintain environment, FIND is not supported when developing a synonym.

ACCEPT = DECODE

This option is used to supply pairs of values for auto amper-prompting. Each pair consists
of one value that can be looked up in the data source and a corresponding value for
display.

ACCEPT = FOCEXEC

This option is used to retrieve lookup and display field values by running a FOCEXEC. Each
row in the output must include one value for lookup and a corresponding value for display.
These values can be anywhere in the row, in any order. The FOCEXEC can return other
columns as well.

ACCEPT = SYNONYM

This option is used to look up values in another data source and retrieve a corresponding
display value. The lookup field values must exist in both data sources, although they do not
need to have matching field names. You supply the name of the synonym, the lookup field
name, and the display field name.

Describing Data With TIBCO WebFOCUS® Language

 187

Validating Data: ACCEPT

Syntax:

How to Validate Data

ACCEPT = list

ACCEPT = value1 TO value2

ACCEPT = FIND (field [AS name] IN file)

ACCEPT=SYNONYM(lookup_field AS display_field IN lookup_synonym)

ACCEPT=FOCEXEC(lookup_field AS display_field IN lookup_focexec)

where:

list

Is a string of acceptable values. The syntax is:

value1 OR value2 OR value3...

For example, ACCEPT = RED OR WHITE OR BLUE. You can also use a blank as an item
separator. If the list of acceptable values runs longer than one line, continue it on the
next. The list is terminated by a comma.

value1 TO value2

Gives the range of acceptable values. For example, ACCEPT = 150 TO 1000.

FIND

Verifies the incoming data against the values in another indexed field. This option is
available only in MODIFY procedures for FOCUS data sources. For more information, see
Describing a FOCUS Data Source on page 293.

SYNONYM

Looks up values in another data source and retrieves a corresponding display value. The
lookup field values must exist in both data sources, although they do not need to have
matching field names. You supply the name of the synonym, the lookup field name and the
display field name.

FOCEXEC

Retrieves lookup and corresponding display values by running a FOCEXEC. Each row must
return a lookup field value and its corresponding display field value anywhere in the row, in
any order. You supply the name of the FOCEXEC, the lookup field name, and the display
field name.

188

4. Describing an Individual Field

lookup_field

Is the field in the lookup_synonym or returned by the lookup_focexec whose value will be
used in the filter (WHERE dialogue) or by the amper autoprompt facility that will be
compared with the field that has the ACCEPT attribute.

display_field

Is the field in the lookup_synonym or returned by the lookup_focexec, whose value will be
displayed for selection in the filter dialogue or amper autoprompt drop-down list.

lookup_synonym

Is the name of the synonym that describes the lookup data.

lookup_focexec

Is the name of the FOCEXEC that returns the lookup and display field values, in any order.
This FOCEXEC can return other field values as well.

Any value in the ACCEPT that contains an embedded blank (for example, Great Britain) must be
enclosed within single quotation marks.

If the ACCEPT attribute is included in a field declaration and the SET command parameter
ACCBLN has a value of OFF, blank ( ) and zero (0) values are accepted only if they are explicitly
coded into the ACCEPT. SET ACCBLN is described in the Developing Reporting Applications
manual.

Example:

Specifying a List With an Embedded Blank

ACCEPT = SPAIN OR ITALY OR FRANCE OR 'GREAT BRITAIN'

Reference: Usage Notes for ACCEPT

Note the following rules when using ACCEPT:

Alias. ACCEPT does not have an alias.

Changes. You can change the information in an ACCEPT attribute at any time.

Virtual fields. You cannot use the ACCEPT attribute to validate virtual fields created with
the DEFINE attribute.

HOLD files. If you wish to propagate the ACCEPT attribute into the Master File of a HOLD
file, use the SET HOLDATTR command. HOLD files are discussed in the Creating Reports
With WebFOCUS Language manual.

Describing Data With TIBCO WebFOCUS® Language

 189

Specifying Acceptable Values for a Dimension

ACCEPT=FIND is used only in MODIFY procedures. It is useful for providing one central
validation list to be used by several procedures. The FIND function is useful when the list of
values is large or undergoes frequent change.

Specifying Acceptable Values for a Dimension

The optional ACCEPT attribute enables you to specify a list of acceptable values for use in an
OLAP-enabled Master File.

ACCEPT is useful whenever data fields are to be addressed by several requests. One ACCEPT
attribute in the Master File eliminates the need to provide lists in each separate procedure
(FOCEXEC).

The ACCEPT attribute enables you to specify:

A list of acceptable data values.

A range of acceptable data values.

Acceptable data values that match any value contained in an external flat data source
(lookup).

The use of the lookup option is helpful when the list of values is large and undergoes frequent
change.

Syntax:

How to Specify a List of Acceptable Values for a Dimension

ACCEPT=value1 OR value2 OR value3...

where:

value1, value2, value3...

Is a list of acceptable values. Any value in the ACCEPT list which contains an embedded
blank must be enclosed within single quotation marks. For values without embedded
blanks, single quotation marks are optional.

Example:

Specifying a List of Acceptable Products for a Dimension

The following shows the ACCEPT syntax in the Master File, which specifies the list of
acceptable products: Espresso, Latte, Cappuccino, Scone, Biscotti, Croissant, Mug, Thermos,
Coffee Grinder, and Coffee Pot.

ACCEPT='Espresso' OR 'Latte' OR 'Cappuccino' OR 'Scone' OR 'Biscotti' OR
   'Croissant' OR 'Mug' OR 'Thermos' OR 'Coffee Grinder' OR 'Coffee Pot'

190

Syntax:

How to Specify a Range of Acceptable Values for a Dimension

4. Describing an Individual Field

ACCEPT=value1 TO value2

where:

value1

Is the value for the beginning of the range.

value2

Is the value for the end of the range.

Example:

Specifying a Range of Acceptable Values for a Dimension

The following shows the ACCEPT syntax in the Master File, which specifies a range of
acceptable data values between 150 and 1000.

ACCEPT=150 TO 1000

Syntax:

How to Verify Data Against Values in an External Flat Data Source

ACCEPT=(ddname)

where:

ddname

Is the ddname that points to the fully qualified name of an existing data source that
contains the list of acceptable values. The ddname can consist of a maximum of 8
characters. Note that you must FILEDEF or ALLOCATE the ddname to the external data
source. You can issue the FILEDEF or ALLOCATE statement in any valid profile.

Example:

Verifying Data Against Acceptable Values for the State Field

The OSTATE data source contains the list of all acceptable values for the state field. The
following shows the ACCEPT syntax in the Master File which verifies state values against the
external OSTATE data source:

ACCEPT=(OSTATE)

Alternative Report Column Titles: TITLE

When you generate a report, each column title in the report defaults to the name of the field
that appears in that column. However, you can change the default column title by specifying
the optional TITLE attribute for that field.

Describing Data With TIBCO WebFOCUS® Language

 191

Alternative Report Column Titles: TITLE

You can also specify a different column title within an individual report by using the AS phrase
in that report request, as described in the Creating Reports With WebFOCUS Language manual.

Note that the TITLE attribute has no effect in a report if the field is used with a prefix operator,
such as AVE. You can supply an alternative column title for fields used with prefix operators by
using the AS phrase.

Master Files support TITLE attributes for multiple languages. For information, see Multilingual
Metadata on page 194.

Syntax:

How to Specify an Alternative Title

TITLE = 'text'

where:

text

Is any string of up to 512 characters, in a single-byte character set. If you are working in a
Unicode environment, this length will be affected by the number of bytes used to represent
each character, as described in the chapter named Unicode Support in the Server
Administration manual. You can split the text across as many as five separate title lines by
separating the lines with a comma (,). Include blanks at the end of a column title by
including a slash (/) in the final blank position. You must enclose the string within single
quotation marks if it includes commas or leading blanks.

Example:

Replacing the Default Column Title

The following FIELD declaration:

FIELD = LNAME, ALIAS = LN, USAGE = A15, TITLE = 'Client,Name',$

replaces the default column heading, LNAME, with the following:

Client
Name
------

Reference: Usage Notes for TITLE

Note the following rules when using TITLE:

Alias. TITLE does not have an alias.

Changes. You can change the information in TITLE at any time. You can also override the
TITLE with an AS name in a request, or turn it off with the SET TITLES=OFF command.

192

4. Describing an Individual Field

Virtual fields. If you use the TITLE attribute for a virtual field created with the DEFINE
attribute, the semicolon (;) terminating the DEFINE expression must be on the same line as
the TITLE keyword.

HOLD files. To propagate the TITLE attribute into the Master File of a HOLD file, use the
SET HOLDATTR command. HOLD files are discussed in the Creating Reports With
WebFOCUS Language manual.

Documenting the Field: DESCRIPTION

DESCRIPTION is an optional attribute that enables you to provide comments and other
documentation for a field within the Master File. You can include any comment up to 2K
(2048) characters in length.

Note that you can also add documentation to a field declaration, or to a segment or file
declaration, by typing a comment in the columns following the terminating dollar sign. You can
even create an entire comment line by inserting a new line following a declaration and placing
a dollar sign at the beginning of the line. The syntax and rules for creating a Master File are
described in Understanding a Data Source Description on page 17.

The DESCRIPTION attribute for a FOCUS data source can be changed at any time without
rebuilding the data source.

Master Files support description attributes for multiple languages. For information, see
Multilingual Metadata on page 194.

Syntax:

How to Supply Field Documentation

DESC[RIPTION] = text

where:

DESCRIPTION

Can be shortened to DESC. Abbreviating the keyword has no effect on its function.

text

Is any string of up to 2K (2048) characters. If it contains a comma, the string must be
enclosed within single quotation marks.

Example:

Specifying a DESCRIPTION

The following FIELD declaration provides a DESCRIPTION:

FIELD=UNITS,ALIAS=QTY,USAGE=I6, DESC='QUANTITY SOLD, NOT RETURNED',$

Describing Data With TIBCO WebFOCUS® Language

 193

Multilingual Metadata

Reference: Usage Notes for DESCRIPTION

Note the following rules when using the DESCRIPTION attribute:

Alias. The DESCRIPTION attribute has an alias of DEFINITION.

Changes. You can change DESCRIPTION at any time.

Virtual fields. You can use the DESCRIPTION attribute for a virtual field created with the
DEFINE attribute.

Multilingual Metadata

Master Files support column headings and descriptions in multiple languages.

The heading or description used depends on the value of the LANG parameter and whether a
TITLE_ln or DESC_ln attribute is specified in the Master File, or a set of translation files exist
for the Master File, where ln identifies the language to which the column heading or description
applies.

In a Master File, column headings are taken from:

1. A heading specified in the report request using the AS phrase.

2. A TITLE attribute in the Master File, if no AS phrase is specified in the request and SET

TITLES=ON.

3. The field name specified in the Master File, if no AS phrase or TITLE attribute is specified,

or if SET TITLES=OFF.

Syntax:

How to Activate the Use of a Language

Issue the following command in a supported profile or in a FOCEXEC:

SET LANG = lng

or

SET LANG = ln

where:

lng

Is the three-letter abbreviation for the language.

ln

Is the two-letter ISO language code.

194

Note: If SET LANG is used in a procedure, its value will override the values set in nlscfg.err or
in any profile.

4. Describing an Individual Field

Reference: Activating a Language in the NLS Configuration File

In the nlscfg.err configuration file, issue the following command:

LANG = lng

Reference: Languages and Language Code Abbreviations

Language Name

Arabic

Baltic

Chinese - Simplified GB

Chinese - Traditional Big-5

Czech

Danish

Dutch

English - American

English - UK

Finnish

French - Canadian

French - Standard

German - Austrian

German - Standard

Greek

Hebrew

Two-Letter
Language Code

Three-Letter Language
Abbreviation

ar

lt

zh

tw

cs

da

nl

en

uk

fi

fc

fr

at

de

el

iw

ARB

BAL

PRC

ROC

CZE

DAN

DUT

AME or ENG

UKE

FIN

FRE

FRE

GER

GER

GRE

HEW

Describing Data With TIBCO WebFOCUS® Language

 195

Multilingual Metadata

Language Name

Italian

Japanese - Shift-JIS(cp942) on ascii
cp939 on EBCDIC

Japanese - EUC(cp10942) on ascii
(UNIX)

Korean

Norwegian

Polish

Portuguese - Brazilian

Portuguese - Portugal

Russian

Spanish

Swedish

Thai

Turkish

Two-Letter
Language Code

Three-Letter Language
Abbreviation

it

ja

je

ko

no

pl

br

pt

ru

es

sv

th

tr

ITA

JPN

JPE

KOR

NOR

POL

POR

POR

RUS

SPA

SWE

THA

TUR

Placing Multilingual Metadata Directly in a Master File

You can place TITLE_ln and DESCRIPTION_ln attributes directly in the Master file, where ln
specifies the language code.

Note: You can also create a set of language translation files and include the trans_file
attribute at the file level of the Master File. For information on this technique, see Storing
Localized Metadata in Language Files on page 58.

196

4. Describing an Individual Field

Syntax:

How to Specify Multilingual Metadata in a Master File

FIELDNAME = field, ...
   .
   .
   .
TITLE= default_column_heading, TITLE_ln = column_heading_for_ln,
   .
   .
   .
DESC= default_desc, DESC_ln = desc_for_ln,
   .
   .
   .

where:

field

Is a field in the Master File.

default_column_heading

Is the column heading to use when SET TITLES=ON and either the LANG parameter is set
to the default language for the server, or another language is set but the Master File has
no corresponding TITLE_ln attribute for that field. This column heading is also used if the ln
value is invalid.

default_desc

Is the description to use when either the LANG parameter is set to the default language for
the server, or another language is set but the Master File has no corresponding DESC_ln
attribute for that field. This description is also used if the ln value is invalid.

TITLE_ln = column_heading_for_ln

Specifies the language for which the column heading applies and the text of the column
heading in that language. That column heading is used when SET TITLES=ON, the LANG
parameter is set to a non-default language for the server, and the Master File has a
corresponding TITLE_ln attribute, where ln is the two-digit code for the language specified
by the LANG parameter Valid values for ln are the two-letter ISO 639 language code
abbreviations. For information, see Languages and Language Code Abbreviations on page
195.

Describing Data With TIBCO WebFOCUS® Language

 197

Multilingual Metadata

DESC_ln = desc_for_ln

Specifies the language for which the description applies and the description text in that
language. This description is used when the LANG parameter is set to a non-default
language for the server and the Master File has a corresponding DESC_ln attribute. Valid
values for ln are the two-letter ISO 639 language code abbreviations.

Reference: Usage Notes for Multilingual Metadata

To generate the correct characters, all languages used must be on the code page specified
at server startup. To change the code page, you must stop and restart the server with the
new code page.

Master Files should be stored using the code page of the server.

Multilingual descriptions are supported with all fields described in the Master File, including
DEFINE and COMPUTE fields.

If you issue a HOLD command with SET HOLDATTR=ON, only one TITLE attribute is
propagated to the HOLD Master File. Its value is the column heading that would have
appeared on the report output.

Example:

Using Multilingual Descriptions in a Master File

The following Master File for the CENTINV data source specifies French descriptions (DESC_FR)
and Spanish descriptions (DESC_ES) as well as default descriptions (DESC) for the
PROD_NUM and PRODNAME fields:

FILE=CENTINV, SUFFIX=FOC, FDFC=19, FYRT=00
 SEGNAME=INVINFO, SEGTYPE=S1, $
  FIELD=PROD_NUM, ALIAS=PNUM, FORMAT=A4, INDEX=I,
   DESCRIPTION='Product Number'
   DESC='Product Number',
   DESC_ES='Numero de Producto',
   DESC_FR='Nombre de Produit', $
  FIELD=PRODNAME, ALIAS=PNAME, FORMAT=A30,
   WITHIN=PRODCAT,
   DESCRIPTION='Product Name'
   DESC_FR='Nom de Produit',
   DESC_ES='Nombre de Producto', $
  FIELD=QTY_IN_STOCK, ALIAS=QIS, FORMAT=I7,
   DESCRIPTION='Quantity In Stock', $
  FIELD=PRICE, ALIAS=RETAIL, FORMAT=D10.2,
   TITLE='Price:',
   DESCRIPTION=Price, $

198

4. Describing an Individual Field

Example:

Using Multilingual Titles in a Request

The following Master File for the CENTINV data source specifies French titles (TITLE_FR) and
Spanish titles (TITLE_ES) as well as default titles (TITLE) for the PROD_NUM and PRODNAME
fields:

FILE=CENTINV, SUFFIX=FOC, FDFC=19, FYRT=00
 SEGNAME=INVINFO, SEGTYPE=S1, $
  FIELD=PROD_NUM, ALIAS=PNUM, FORMAT=A4, INDEX=I,
   TITLE='Product,Number:',
   TITLE_FR='Nombre,de Produit:',
   TITLE_ES='Numero,de Producto:',
   DESCRIPTION='Product Number', $
  FIELD=PRODNAME, ALIAS=PNAME, FORMAT=A30,
   WITHIN=PRODCAT,
   TITLE='Product,Name:',
   TITLE_FR='Nom,de Produit:',
   TITLE_ES='Nombre,de Producto:'
   DESCRIPTION='Product Name', $
  FIELD=QTY_IN_STOCK, ALIAS=QIS, FORMAT=I7,
   TITLE='Quantity,In Stock:',
   DESCRIPTION='Quantity In Stock', $
  FIELD=PRICE, ALIAS=RETAIL, FORMAT=D10.2,
   TITLE='Price:',
   DESCRIPTION=Price, $

The default language for the server code page is English and, by default, SET TITLES=ON.
Therefore, the following request, uses the TITLE attributes to produce column headings that
are all in English:

TABLE FILE CENTINV
PRINT PROD_NUM PRODNAME PRICE
WHERE PRICE LT 200
END

The output is:

Product  Product
Number:  Name:                                 Price:
-------  -------                               ------
1004     2 Hd VCR LCD Menu                     179.00
1008     DVD Upgrade Unit for Cent. VCR        199.00
1026     AR3 35MM Camera 10 X                  129.00
1028     AR2 35MM Camera 8 X                   109.00
1030     QX Portable CD Player                 169.00
1032     R5 Micro Digital Tape Recorder         89.00

Now, issue the following command to set the language to Spanish and run the same request:

SET LANG = SPA

Describing Data With TIBCO WebFOCUS® Language

 199

Describing a Virtual Field: DEFINE

The output now displays column headings from the TITLE_ES attributes where they exist
(Product Number and Product Name). Where no Spanish title is specified (the Price field), the
column heading in the TITLE attribute appears:

Numero        Nombre
de Producto:  de Producto:                          Price:
------------  ------------                          ------
1004          2 Hd VCR LCD Menu                     179.00
1008          DVD Upgrade Unit for Cent. VCR        199.00
1026          AR3 35MM Camera 10 X                  129.00
1028          AR2 35MM Camera 8 X                   109.00
1030          QX Portable CD Player                 169.00
1032          R5 Micro Digital Tape Recorder         89.00

Describing a Virtual Field: DEFINE

DEFINE is an optional attribute used to create a virtual field for reporting. You can derive the
virtual field value from information already in the data source (that is, from permanent fields).
Some common uses of virtual data fields include:

Computing new numeric values that are not on the data record.

Computing a new string of alphanumeric characters from other strings.

Classifying data values into ranges or groups.

Invoking subroutines in calculations.

Virtual fields are available whenever the data source is used for reporting.

Syntax:

How to Define a Virtual Field

DEFINE fieldname/format [(GEOGRAPHIC_ROLE = georole)]
  [REDEFINES field2] = expression;
  [,TITLE='title',]
  [TITLE_ln='titleln', ... ,]
  [,DESC[CRIPTION]='desc',]
  [DESC_ln='descln', ... ,]$

where:

fieldname

Is the name of the virtual field. The name is subject to the same conventions as names
assigned using the FIELDNAME attribute. FIELDNAME is described in The Field Name:
FIELDNAME on page 104.

200

4. Describing an Individual Field

format

Is the field format. It is specified in the same way as formats assigned using the USAGE
attribute, which is described in The Displayed Data Type: USAGE on page 113. If you do not
specify a format, it defaults to D12.2.

georole

Is a valid geographic role. Geographic roles can be names, postal codes, ISO (International
Organization for Standardization) codes, FIPS (Federal Information Processing Standards)
codes, or NUTS (Nomenclature of Territorial Units for Statistics ) codes. The following is a
list of supported geographic roles.

ADDRESS_FULL. Full address.

ADDRESS_LINE. Number and street name.

CITY. City name.

CONTINENT. Continent name.

CONTINENT_ISO2. Continent ISO-3166 code.

COUNTRY. Country name.

COUNTRY_FIPS. Country FIPS code.

COUNTRY_ISO2. Country ISO-3166-2 code.

COUNTRY_ISO3. Country ISO-3166-3 code.

GEOMETRY_AREA. Geometry area.

GEOMETRY_LINE. Geometry line.

GEOMETRY_POINT. Geometry point.

LATITUDE. Latitude.

LONGITUDE. Longitude.

NUTS0. Country name (NUTS level 0).

NUTS0_CC. Country code (NUTS level 0).

NUTS1. Region name (NUTS level 1).

NUTS1_CC. Region code (NUTS level1).

NUTS2. Province name (NUTS level 2).

Describing Data With TIBCO WebFOCUS® Language

 201

Describing a Virtual Field: DEFINE

NUTS2_CC. Province code (NUTS level 2).

NUTS3. District name (NUTS level 3).

NUTS3_CC. District code (NUTS level 3).

POSTAL_CODE. Postal code.

STATE. State name.

STATE_FIPS. State FIPS code.

STATE_ISO_SUB. US State ISO subdivision code.

USSCITY. US city name.

USCITY_FIPS. US city FIPS code.

USCOUNTY. US county name.

USCOUNTY_FIPS. US county FIPS code.

USSTATE. US state name.

USSTATE_ABBR. US state abbreviation.

USSTATE_FIPS. US state FIPS code.

ZIP3. US 3-digit postal code.

ZIP5. US 5-digit postal code.

field2

Enables you to redefine or recompute a field whose name exists in more than one
segment.

expression

Is a valid expression. The expression must end with a semicolon (;). Expressions are fully
described in the Creating Reports With WebFOCUS Language manual.

Note that when an IF-THEN phrase is used in the expression of a virtual field, it must
include the ELSE phrase.

TITLE='title'

Is a column title for the virtual field in the default language.

TITLE_ln='titleln'

Is a column title for the virtual field in the language specified by the language code ln.

202

4. Describing an Individual Field

DESC[CRIPTION]='desc'

Is a description for the virtual field in the default language.

DESC_ln='descln'

Is a description for the virtual field in the language specified by the language code ln.

Place each DEFINE attribute after all of the field descriptions for that segment.

Example:

Defining a Field

The following shows how to define a field called PROFIT in the segment CARS:

SEGMENT = CARS ,SEGTYPE = S1 ,PARENT = CARREC, $
   FIELDNAME = DEALER_COST ,ALIAS = DCOST ,USAGE = D7, $
   FIELDNAME = RETAIL_COST ,ALIAS = RCOST ,USAGE = D7, $
   DEFINE PROFIT/D7 = RETAIL_COST - DEALER_COST; $

Reference: Usage Notes for Virtual Fields in a Master File

Note the following rules when using DEFINE:

Alias. DEFINE does not have an alias.

Changes. You can change the virtual field declaration at any time.

A DEFINE FILE command takes precedence over a DEFINE in the Master with same name.

If the expression used to derive the virtual field invokes a function, parameter numbers and
types are not checked unless the USERFCHK parameter is set to FULL.

Using a Virtual Field

A DEFINE attribute cannot contain qualified field names on the left-hand side of the
expression. Use the WITH phrase on the left-hand side to place the defined field in the same
segment as any real field you choose. This will determine when the DEFINE expression will be
evaluated.

Expressions on the right-hand side of the DEFINE can refer to fields from any segment in the
same path. The expression on the right-hand side of a DEFINE statement in a Master File can
contain qualified field names.

A DEFINE attribute in a Master File can refer to only fields in its own path. If you want to create
a virtual field that derives its value from fields in several different paths, you have to create it
with a DEFINE FILE command using an alternate view prior to a report request, as discussed in
the Creating Reports With WebFOCUS Language manual. The DEFINE FILE command is also
helpful when you wish to create a virtual field that is only used once, and you do not want to
add a declaration for it to the Master File.

Describing Data With TIBCO WebFOCUS® Language

 203

Describing a Calculated Value: COMPUTE

Virtual fields defined in the Master File are available whenever the data source is used, and
are treated like other stored fields. Thus, a field defined in the Master File cannot be cleared in
your report request.

A virtual field cannot be used for cross-referencing in a join. It can, however, be used as a host
field in a join.

Note: Maintain Data does not support DEFINE attributes that have a constant value. Using
such a field in a Maintain Data procedure generates the following message:

(FOC03605) name is not recognized.

Describing a Calculated Value: COMPUTE

COMPUTE commands can be included in Master Files and referenced in subsequent TABLE
requests, enabling you to build expressions once and use them in multiple requests.

Syntax:

How to Include a COMPUTE Command in a Master File

COMPUTE fieldname/fmt [(GEOGRAPHIC_ROLE = georole)]
 =expression;
  [,TITLE='title',]
  [TITLE_ln='titleln', ... ,]
  [,DESC[CRIPTION]='desc',]
  [DESC_ln='descln', ... ,]$

where:

fieldname

Is name of the calculated field.

fmt

Is the format and length of the calculated field.

georole

Is a valid geographic role. Geographic roles can be names, postal codes, ISO (International
Organization for Standardization) codes, FIPS (Federal Information Processing Standards)
codes, or NUTS (Nomenclature of Territorial Units for Statistics ) codes. The following is a
list of supported geographic roles.

ADDRESS_FULL. Full address.

ADDRESS_LINE. Number and street name.

CITY. City name.

204

4. Describing an Individual Field

CONTINENT. Continent name.

CONTINENT_ISO2. Continent ISO-3166 code.

COUNTRY. Country name.

COUNTRY_FIPS. Country FIPS code.

COUNTRY_ISO2. Country ISO-3166-2 code.

COUNTRY_ISO3. Country ISO-3166-3 code.

GEOMETRY_AREA. Geometry area.

GEOMETRY_LINE. Geometry line.

GEOMETRY_POINT. Geometry point.

LATITUDE. Latitude.

LONGITUDE. Longitude.

NUTS0. Country name (NUTS level 0).

NUTS0_CC. Country code (NUTS level 0).

NUTS1. Region name (NUTS level 1).

NUTS1_CC. Region code (NUTS level1).

NUTS2. Province name (NUTS level 2).

NUTS2_CC. Province code (NUTS level 2).

NUTS3. District name (NUTS level 3).

NUTS3_CC. District code (NUTS level 3).

POSTAL_CODE. Postal code.

STATE. State name.

STATE_FIPS. State FIPS code.

STATE_ISO_SUB. US State ISO subdivision code.

USSCITY. US city name.

USCITY_FIPS. US city FIPS code.

Describing Data With TIBCO WebFOCUS® Language

 205

Describing a Calculated Value: COMPUTE

USCOUNTY. US county name.

USCOUNTY_FIPS. US county FIPS code.

USSTATE. US state name.

USSTATE_ABBR. US state abbreviation.

USSTATE_FIPS. US state FIPS code.

ZIP3. US 3-digit postal code.

ZIP5. US 5-digit postal code.

expression

Is the formula for calculating the value of the field.

TITLE='title'

Is a column title for the calculated field in the default language.

TITLE_ln='titleln'

Is a column title for the calculated field in the language specified by the language code ln.

DESC[CRIPTION]='desc'

Is a description for the calculated field in the default language.

DESC_ln='descln'

Is a description for the calculated field in the language specified by the language code ln.

Reference: Usage Notes for COMPUTE in a Master File

In all instances, COMPUTEs in the Master File have the same functionality and limitations as
temporary COMPUTEs. Specifically, fields computed in the Master File must follow these rules:

They cannot be used in JOIN, DEFINE, or ACROSS phrases, or with prefix operators.

When used as selection criteria, syntax is either IF TOTAL field or WHERE TOTAL field.

When used as sort fields, syntax is BY TOTAL COMPUTE field.

To insert a calculated value into a heading or footing, you must reference it prior to the
HEADING or FOOTING command.

Note: Maintain Data does not currently support using COMPUTEs in Master Files.

206

4. Describing an Individual Field

Example:

Coding a COMPUTE in the Master File and Accessing the Computed Value

Use standard COMPUTE syntax to add a calculated value to your Master File. You can then
access the calculated value by referencing the computed fieldname in subsequent TABLE
requests. When used as a verb object, as in the following example, the syntax is SUM (or
PRINT) COMPUTE field.

The following is the SALESTES Master File (the SALES FILE modified with an embedded
COMPUTE):

FILENAME=SALESTES, SUFFIX=FOC,
SEGNAME=STOR_SEG, SEGTYPE=S1,
   FIELDNAME=STORE_CODE,  ALIAS=SNO,  FORMAT=A3,   $
   FIELDNAME=CITY,        ALIAS=CTY,  FORMAT=A15,  $
   FIELDNAME=AREA,        ALIAS=LOC,  FORMAT=A1,   $

SEGNAME=DATE_SEG, PARENT=STOR_SEG, SEGTYPE=SH1,
   FIELDNAME=DATE,        ALIAS=DTE,  FORMAT=A4MD, $

SEGNAME=PRODUCT, PARENT=DATE_SEG, SEGTYPE=S1,
   FIELDNAME=PROD_CODE,     ALIAS=PCODE,   FORMAT=A3,    FIELDTYPE=I, $
   FIELDNAME=UNIT_SOLD,     ALIAS=SOLD,    FORMAT=I5,    $
   FIELDNAME=RETAIL_PRICE,  ALIAS=RP,      FORMAT=D5.2M, $
   FIELDNAME=DELIVER_AMT,   ALIAS=SHIP,    FORMAT=I5,    $
   FIELDNAME=OPENING_AMT,   ALIAS=INV,     FORMAT=I5,    $
   FIELDNAME=RETURNS,       ALIAS=RTN,     FORMAT=I3,    MISSING=ON, $
   FIELDNAME=DAMAGED,       ALIAS=BAD,     FORMAT=I3,    MISSING=ON, $

   COMPUTE REVENUE/D12.2M=UNIT_SOLD*RETAIL_PRICE;

The following TABLE request uses the REVENUE field:

TABLE FILE SALESTES
HEADING CENTER
"NEW YORK PROFIT REPORT"
" "
SUM UNIT_SOLD AS 'UNITS,SOLD' RETAIL_PRICE AS 'RETAIL_PRICE'
COMPUTE REVENUE;
BY PROD_CODE AS 'PROD,CODE'
WHERE CITY EQ 'NEW YORK'
END

Describing Data With TIBCO WebFOCUS® Language

 207




Describing a Filter: FILTER

The output is:

           NEW YORK PROFIT REPORT

  PROD  UNITS
  CODE  SOLD   RETAIL_PRICE          REVENUE
  ----  ----   ------------          -------
  B10      30          $.85           $25.50
  B17      20         $1.89           $37.80
  B20      15         $1.99           $29.85
  C17      12         $2.09           $25.08
  D12      20         $2.09           $41.80
  E1       30          $.89           $26.70
  E3       35         $1.09           $38.15

Describing a Filter: FILTER

Boolean virtual fields (DEFINE fields that evaluate to TRUE or FALSE) can be used as record
selection criteria. If the primary purpose of a virtual field is for use in record selection, you can
clarify this purpose and organize virtual fields in the Master File by storing the expression using
a FILTER declaration rather than a DEFINE. Filters offer the following features:

They allow you to organize and store popular selection criteria in a Master File, group them
in a Business View, and reuse them in multiple requests and tools.

The front-end tools build and use them properly based on their primary function in a
request.

For some data sources (such as VSAM and ISAM), certain filter expressions can be
inserted inline into the WHERE or IF clause, enhancing optimization compared to a Boolean
DEFINE.

Syntax:

How to Declare a Filter in a Master File

FILTER  filtername = expression; [MANDATORY={YES|NO}]
  [, DESC[RIPTION]='desc']
  [, DESC_ln='descln', ... ] ,$

where:

filtername

Is the name assigned to the filter. The filter is internally assigned a format of I1, which
cannot be changed.

208


4. Describing an Individual Field

expression

Is a logical expression that evaluates to TRUE (which assigns the value 1 to the filter field)
or FALSE (which assigns the value 0 to the filter field). For any other type of expression,
the field becomes a standard numeric virtual field in the Master File. Dialogue Manager
variables (amper variables) can be used in the filter expression in same way they are used
in standard Master File DEFINEs.

MANDATORY={YES|NO}

Specifies whether to apply the filter even if it is not referenced in a request against the
synonym. YES applies the filter to all requests against the synonym. NO applies the filter
only when it is referenced in a request. NO is the default value.

Note: Unlike a filter created using the FILTER FILE command, which can be toggled ON and
OFF, this setting can only be turned off by removing or changing the value in the Master
File.

DESC[RIPTION]='desc'

Is a description for the sort object in the default language.

DESC_ln='descln'

Is a description for the sort object in the language specified by the language code ln.

Syntax:

How to Use a Master File Filter in a Request

TABLE FILE filename
   .
   .
   .
{WHERE|IF} expression_using_filters

where:

expression_using_filters

Is a logical expression that references a filter. In a WHERE phrase, the logical expression
can reference one or more filters and/or virtual fields.

Reference: Usage Notes for Filters in a Master File

The filter field name is internally assigned a format of I1 which cannot be changed.

A filter can be used as a standard numeric virtual field anywhere in a report request, except
that they are not supported in WHERE TOTAL tests.

Describing Data With TIBCO WebFOCUS® Language

 209

Describing a Filter: FILTER

A mandatory filter can be used to force access to a segment (for example, a table in a
cluster synonym) that is not referenced in a request.

Example:

Defining and Using a Master File Filter

Consider the following filter declaration added to the MOVIES Master File:

FILTER G_RATING = RATING EQ 'G' OR 'PG'; $

The following request applies the G_RATING filter:

TABLE FILE MOVIES
HEADING CENTER
"Rating G and PG"
PRINT TITLE CATEGORY RATING
WHERE G_RATING
ON TABLE SET PAGE NOPAGE
ON TABLE SET GRID OFF

ON TABLE SET STYLE *
type=report, style=bold, color=black, backcolor=yellow, $
type=data, backcolor=aqua, $
ENDSTYLE
END

210

The output is shown in the following image:

4. Describing an Individual Field

Example:

Using a Mandatory Filter

Consider the following filter declaration added to the MOVIES Master File:

FILTER G_RATING = RATING EQ 'G' OR 'PG'; MANDATORY=YES ,$

Describing Data With TIBCO WebFOCUS® Language

 211

Describing a Filter: FILTER

The following request does not reference the G_RATING filter:

TABLE FILE MOVIES
HEADING CENTER
"Rating G and PG"
PRINT TITLE CATEGORY RATING
ON TABLE SET PAGE NOPAGE
ON TABLE SET GRID OFF

ON TABLE SET STYLE *
type=report, style=bold, color=black, backcolor=yellow, $
type=data, backcolor=aqua, $
ENDSTYLE
END

212

The output is shown in the following image. Note that the G_RATING filter is applied even
though it is not referenced in the request:

4. Describing an Individual Field

Describing a Sort Object: SORTOBJ

You can define sort phrases and attributes in a Master File and reference them by name in a
request against the Master File. The entire text of the sort object is substituted at the point in
the TABLE where the sort object is referenced. The sort phrases in the sort object are not
verified prior to this substitution. The only verification is that there is a sort object name and
an equal sign in the Master File SORTOBJ record.

Describing Data With TIBCO WebFOCUS® Language

 213

Describing a Sort Object: SORTOBJ

Reference: Usage Notes for Sort Objects in a Master File

The sort object declaration can appear anywhere after the first SEGNAME/SEGMENT
record. However, it must appear after all fields mentioned by it in the Master File, including
virtual fields.

A sort object can use both Master File and local virtual fields.

Unlimited sort object declarations may appear in a Master File, but the number referenced
by a TABLE request cannot result in more than the maximum number of sort phrases in the
request.

The sort object declaration can be followed by optional attributes.

If a sort object has the same name as a field, the sort object will be used when referenced
in a request.

Syntax:

How to Declare a Sort Object in a Master File

FILE= ...
SEG= ...
FIELD= ...
SORTOBJ sortname = {BY|ACROSS} sortfield1 [attributes]
  [{BY|ACROSS} sortfield2 ... ];
  [,DESC[CRIPTION]='desc',]
  [DESC_ln='descln', ... ,]$

where:

sortname

Is a name for the sort object.

sortfield1, sortfield2 ..

Are fields from the Master File or local DEFINE fields that will be used to sort the report
output.

attributes

Are any valid sort attributes.

;

Is required syntax for delimiting the end of the sort object expression.

DESC[CRIPTION]='desc'

Is a description for the sort object in the default language.

214

4. Describing an Individual Field

DESC_ln='descln'

Is a description for the sort object in the language specified by the language code ln.

Syntax:

How to Reference a Sort Object in a Request

TABLE FILE ...
   .
   .
   .
BY sortname   .
   .
   .
END

where:

sortname

Is the sort object to be inserted into the request.

Example:

Declaring and Referencing a Sort Object

The following sort object for the GGSALES Master File is named CRSORT. It defines two sort
phrases:

BY the REGION field, with a SKIP-LINE attribute.

ACROSS the CATEGORY field.

SORTOBJ CRSORT = ACROSS CATEGORY BY REGION SKIP-LINE ; ,$

The following request references the CRSORT sort object:

TABLE FILE GGSALES
SUM DOLLARS
BY CRSORT
ON TABLE SET PAGE NOPAGE
END

The output is:

                      Category
Region       Coffee        Food          Gifts
------------------------------------------------
Midwest      4178513       4404483       2931349
Northeast    4201057       4445197       2848289
Southeast    4435134       4308731       3037420
West         4493483       4204333       2977092

Describing Data With TIBCO WebFOCUS® Language

 215

Calling a DEFINE FUNCTION in a Master File

Calling a DEFINE FUNCTION in a Master File

You can reference a DEFINE FUNCTION in an expression in a Master File DEFINE, COMPUTE, or
FILTER field. The DEFINE FUNCTION will be loaded into memory when its associated expression
is used in a request.

Note: A DEFINE FUNCTION cannot be used in a multi-root Master File.

Syntax:

How to Call a DEFINE FUNCTION in a Master File Expression

DF.[appname/]filename.functionname(parm1, parm2, ...);
  [DESCRIPTION='description',$

where:

appname

Is an optional application name under which the DEFINE FUNCTION FOCEXEC is stored.

filename

Is the name of the FOCEXEC that contains the DEFINE FUNCTION definition. The FOCEXEC
can contain multiple DEFINE FUNCTION definitions.

functionname(parm1, parm2,...)

Is the function name with the parameters to be used in the expression.

'description'

Is an optional description enclosed in single quotation marks.

Example:

Using a DEFINE FUNCTION in a Master File

The following DEFINE FUNCTION is stored in the DMFUNCS FOCEXEC. Given a last name and
first name, it generates a full name in the format Lastname, Firstname:

DEFINE FUNCTION DMPROPER
DESCRIPTION 'Convert name to proper case and last, first format‘
(LASTNAME/A17, FIRSTNAME/A14)
DMPROPER/A34V=LCWORD(17, LASTNAME, 'A17')
             || (', ' | LCWORD(14, FIRSTNAME, 'A14'));
END

The following is the DEFINE field named WHOLENAME added to the WF_RETAIL_CUSTOMER
Master File that calls the DEFINE FUNCTION:

DEFINE WHOLENAME/A40 = DF.DMFUNCS.DMPROPER(LASTNAME, FIRSTNAME);
     DESCRIPTION = 'Calls DMPROPER to create full name',$

216

4. Describing an Individual Field

The following request uses the DEFINE field WHOLENAME:

TABLE FILE WF_RETAIL_CUSTOMER
PRINT WHOLENAME AS Whole,Name
BY ID_CUSTOMER
WHERE ID_CUSTOMER LT 600
ON TABLE SET PAGE NOPAGE
END

The output is:

             Whole
ID Customer  Name
-----------  -----
         15  Nolan, Tyler
         20  Bull, Joshua
         78  Wood, Zara
        124  Mckenzie, Callum
        125  Charlton, Bradley
        132  Griffiths, Henry
        152  Rowe, Anthony
        161  Storey, Max
        185  Thomas, Evie
        201  Birch, Brandon
        213  Parry, Maisie
        239  Barrett, Taylor
        258  Lord, Harvey
        270  Bell, Jay
        312  Dunn, Daisy
        352  Mckenzie, Callum
        379  Fisher, Leo
        454  Day, Zak
        472  Howarth, Molly
        503  Barrett, Daniel
        531  Hargreaves, Chloe
        566  Fitzgerald, Bethany

Using Date System Amper Variables in Master File DEFINEs

Master File DEFINE fields can use Dialogue Manager system date variables to capture the
system date each time the Master File is parsed for use in a request.

The format of the returned value for each date variable is the format indicated in the variable
name. For example, &DATEYYMD returns a date value with format YYMD. The exceptions are
&DATE and &TOD, which return alphanumeric values and must be assigned to a field with an
alphanumeric format. The variable names &DATE and &TOD must also be enclosed in single
quotation marks in the DEFINE expression.

The variables supported for use in Master File DEFINEs are:

&DATE

Describing Data With TIBCO WebFOCUS® Language

 217

Using Date System Amper Variables in Master File DEFINEs

&TOD

&DATEMDY

&DATEDMY

&DATEYMD

&DATEMDYY

&DATEDMYY

&DATEYYMD

&DMY

&YMD

&MDY

&YYMD

&MDYY

&DMYY

Note that all other reserved amper variables are not supported in Master Files.

Example:

Using the Date Variable &DATE in a Master File DEFINE

The following version of the EMPLOYEE Master File has the DEFINE field named TDATE added
to it. TDATE has format A12 and retrieves the value of &DATE, which returns an alphanumeric
value and must be enclosed in single quotation marks:

FILENAME=EMPLOYEE, SUFFIX=FOC
SEGNAME=EMPINFO,  SEGTYPE=S1
 FIELDNAME=EMP_ID,       ALIAS=EID,     FORMAT=A9,       $
 FIELDNAME=LAST_NAME,    ALIAS=LN,      FORMAT=A15,      $
 FIELDNAME=FIRST_NAME,   ALIAS=FN,      FORMAT=A10,      $
 FIELDNAME=HIRE_DATE,    ALIAS=HDT,     FORMAT=I6YMD,    $
 FIELDNAME=DEPARTMENT,   ALIAS=DPT,     FORMAT=A10,      $
 FIELDNAME=CURR_SAL,     ALIAS=CSAL,    FORMAT=D12.2M,   $
 FIELDNAME=CURR_JOBCODE, ALIAS=CJC,     FORMAT=A3,       $
 FIELDNAME=ED_HRS,       ALIAS=OJT,     FORMAT=F6.2,     $
DEFINE TDATE/A12   ='&DATE';, $
   .
   .
   .

218

4. Describing an Individual Field

The following request displays the value of TDATE:

TABLE FILE EMPLOYEE
PRINT LAST_NAME FIRST_NAME HIRE_DATE TDATE AS 'TODAY''S,DATE'
WHERE LAST_NAME EQ 'BANNING'
END

The output is:

Example:

Using the Date Variable &YYMD in a Master File DEFINE

The following version of the EMPLOYEE Master File has the DEFINE field named TDATE added
to it. TDATE has format YYMD and retrieves the value of &YYMD:

FILENAME=EMPLOYEE, SUFFIX=FOC
SEGNAME=EMPINFO,  SEGTYPE=S1
 FIELDNAME=EMP_ID,       ALIAS=EID,     FORMAT=A9,       $
 FIELDNAME=LAST_NAME,    ALIAS=LN,      FORMAT=A15,      $
 FIELDNAME=FIRST_NAME,   ALIAS=FN,      FORMAT=A10,      $
 FIELDNAME=HIRE_DATE,    ALIAS=HDT,     FORMAT=I6YMD,    $
 FIELDNAME=DEPARTMENT,   ALIAS=DPT,     FORMAT=A10,      $
 FIELDNAME=CURR_SAL,     ALIAS=CSAL,    FORMAT=D12.2M,   $
 FIELDNAME=CURR_JOBCODE, ALIAS=CJC,     FORMAT=A3,       $
 FIELDNAME=ED_HRS,       ALIAS=OJT,     FORMAT=F6.2,     $
DEFINE TDATE/YYMD   = &YYMD ;, $
   .
   .
   .

The following request displays the value of TDATE:

TABLE FILE EMPLOYEE
PRINT LAST_NAME FIRST_NAME HIRE_DATE TDATE AS 'TODAY''S,DATE'
WHERE LAST_NAME EQ 'BANNING'
END

The output is:

Describing Data With TIBCO WebFOCUS® Language

 219

Parameterizing Master and Access File Values Using Variables

Reference: Messages for Date System Amper Variables in Master File DEFINEs

The following message appears if an attempt is made to use an unsupported amper variable in
a Master File DEFINE:

(FOC104) DEFINE IN MASTER REFERS TO A FIELD OUTSIDE ITS SCOPE: var

Parameterizing Master and Access File Values Using Variables

You can define global variables in a Master File and use them to parameterize certain
attributes in the Master File and its corresponding Access File. For example, you can
parameterize the connection attribute in the Access File with a variable you define in the
Master File and then specify the actual connection name at run time.

Syntax:

How to Create a Master File Variable

Add variable definitions after the FILE declaration in the Master File:

VARIABLE NAME=[&&]var, USAGE=Aln, [DEFAULT=defvalue,][QUOTED={OFF|ON},]$

where:

[&&]var

Is the name you are assigning to the global variable. When you reference the variable in
the Master or Access File, you must prepend the name with two ampersands. However,
the ampersands are optional when defining the variable.

ln

Is the maximum length for the variable value.

defvalue

Is the default value for the variable. If no value is set at run time, this value is used.

QUOTED = {OFF|ON}

ON adds single quotation marks around the assigned string for the variable. A single
quotation mark within the string is converted to two single quotation marks. OFF is the
default value.

Reference: Support for Variables in Master and Access File Attributes

In the Master File, the following attributes can be parameterized with variables: POSITION,
OCCURS, REMARKS, DESCRIPTION, TITLE, HELPMESSAGE.

220

4. Describing an Individual Field

In the DBA section of a Master File, the following attributes can be parameterized: USER,
VALUE. For information about using these variables in a Master File profile to create dynamic
DBA rules, see Creating and Using a Master File Profile on page 46.

In the Access File, the following attributes can be parameterized with variables: CONNECTION,
TABLENAME, WORKSHEET (Excel via Direct Retrieval) START, CHKPT_SAVE, CHKPT_FILE,
POLLING, TIMEOUT, MAXLUWS, ACTION, MSGLIMIT, DIRECTORY, NAME, EXTENSION,
DATA_ORIGIN, MAXFILES, MAXRECS, OBJECT, PICKUP, TRIGGER, DISCARD, ARCHIVE.

Note: You can concatenate multiple variables to create an attribute value.

Example:

Parameterizing Attributes in a Master and Access File

The following request creates an Oracle table named ORAEMP from the FOCUS data source
named EMPLOYEE:

TABLE FILE EMPLOYEE
SUM LAST_NAME FIRST_NAME CURR_SAL CURR_JOBCODE DEPARTMENT
BY EMP_ID
ON TABLE HOLD AS ORAEMP FORMAT SQLORA
END

The following is the Master File created by the request:

FILENAME=ORAEMP , SUFFIX=SQLORA , $
  SEGMENT=SEG01, SEGTYPE=S0, $
    FIELDNAME=EMP_ID, ALIAS=EID, USAGE=A9, ACTUAL=A9, $
    FIELDNAME=LAST_NAME, ALIAS=LN, USAGE=A15, ACTUAL=A15, $
    FIELDNAME=FIRST_NAME, ALIAS=FN, USAGE=A10, ACTUAL=A10, $
    FIELDNAME=CURR_SAL, ALIAS=CSAL, USAGE=D12.2M, ACTUAL=D8, $
    FIELDNAME=CURR_JOBCODE, ALIAS=CJC, USAGE=A3, ACTUAL=A3, $
    FIELDNAME=DEPARTMENT, ALIAS=DPT, USAGE=A10, ACTUAL=A10, $

The following is the Access File created by the request:

SEGNAME=SEG01, TABLENAME=ORAEMP, KEYS=01, WRITE=YES, $

Add the following variable definitions to the Master File in order to parameterize the
TABLENAME attribute in the Access File and the TITLE attribute for the EMP_ID column in the
Master File:

FILENAME=ORAEMP, SUFFIX=SQLORA , $
VARIABLE NAME=table, USAGE=A8, DEFAULT=EDUCFILE, $
VARIABLE NAME=emptitle, USAGE=A30, DEFAULT=empid,$

Now, in the Master File, add the TITLE attribute to the FIELD declaration for EMP_ID:

FIELDNAME=EMP_ID, ALIAS=EID, USAGE=A9, ACTUAL=A9,
      TITLE='&&emptitle', $

Describing Data With TIBCO WebFOCUS® Language

 221

Parameterizing Master and Access File Values Using Variables

In the Access File, replace the value for the TABLENAME attribute with the variable name:

SEGNAME=SEG01, TABLENAME=&&table, KEYS=01, WRITE=YES, $

The following request sets the values of the variables and then issues a TABLE request:

-SET &&table = ORAEMP;
-SET &&emptitle = 'Id,number';
TABLE FILE ORAEMP
PRINT EMP_ID LAST_NAME FIRST_NAME DEPARTMENT
END

Note that the value for &&emptitle is enclosed in single quotation marks in the --SET command
because it contains a special character (the comma). The single quotation marks are not part
of the string and do not display on the report output. The column title would display enclosed
in single quotation marks if the variable definition contained the attribute QUOTED=ON.

On the report output, the column title for the employee ID column displays the value set for
&&emptitle, and the table accessed by the request is the ORAEMP table created as the first
step in the example:

Id
number     LAST_NAME        FIRST_NAME  DEPARTMENT
------     ---------        ----------  ----------
071382660  STEVENS          ALFRED      PRODUCTION
112847612  SMITH            MARY        MIS
117593129  JONES            DIANE       MIS
119265415  SMITH            RICHARD     PRODUCTION
119329144  BANNING          JOHN        PRODUCTION
123764317  IRVING           JOAN        PRODUCTION
126724188  ROMANS           ANTHONY     PRODUCTION
219984371  MCCOY            JOHN        MIS
326179357  BLACKWOOD        ROSEMARIE   MIS
451123478  MCKNIGHT         ROGER       PRODUCTION
543729165  GREENSPAN        MARY        MIS
818692173  CROSS            BARBARA     MIS

Example:

Concatenating Variables to Create an Attribute Value

In the following example, the TABLENAME attribute requires a multipart name consisting of a
database name, an owner ID, a table prefix, and a static table name with a variable suffix. In
this case, you can define separate variables for the different parts and concatenate them.

First, define separate variables for each part:

VARIABLE NAME=db,USAGE=A8,DEFAULT=mydb,$
VARIABLE NAME=usr,USAGE=A8,DEFAULT=myusrid,$
VARIABLE NAME=tprf,USAGE=A4,DEFAULT=test_,$
VARIABLE NAME=tsuf,USAGE=YYM,$

222

4. Describing an Individual Field

In the Access File, concatenate the variables to create the TABLENAME attribute. Note that the
separator for between each part is a period, but to concatenate a variable name and retain the
period, you must use two periods:

TABLENAME=&db..&usr..&tprf.table&tsuf,

Based on the defaults, the TABLENAME would be:

TABLENAME=mydb.myusrid.test_table

In a request, set the following values for the separate variables:

I-SET &&db=db1;
-SET &&tprf=prod_;
-SET &&tsuf=200801;

With these values, the TABLENAME used is the following:

TABLENAME=db1.myusrid.prod_table200801

Converting Alphanumeric Dates to WebFOCUS Dates

In some data sources, date values are stored in alphanumeric format without any particular
standard, with any combination of components, such as year, quarter, and month, and with
any delimiter. In a sorted report, if such data is sorted alphabetically, the sequence does not
make business sense. To ensure adequate sorting, aggregation, and reporting on date fields,
WebFOCUS can convert the alphanumeric dates into standard WebFOCUS date format using a
conversion pattern that you can specify in the Master File attribute called DATEPATTERN.

Each element in the pattern is either a constant character which must appear in the actual
input or a variable that represents a date component. You must edit the USAGE attribute in the
Master File so that it accounts for the date elements in the date pattern. The maximum length
of the DATEPATTERN string is 64.

Reference: Usage Notes for DATEPATTERN

If your original date has elements with no WebFOCUS USAGE format equivalent, the
converted date will not look like the original data. In that case, if you want to display the
original data, you may be able to use an OCCURS segment to redefine the field with the
original alphanumeric format and display that field in the request.

DATEPATTERN requires an ACTUAL format to USAGE format conversion. Therefore, it is not
supported for SUFFIX=FOC and SUFFIX=XFOC data sources.

Describing Data With TIBCO WebFOCUS® Language

 223

Converting Alphanumeric Dates to WebFOCUS Dates

Specifying Variables in a Date Pattern

The valid date components (variables) are year, quarter, month, day, and day of week. In the
date pattern, variables are enclosed in square brackets (these brackets are not part of the
input or output. Note that if the data contains brackets, you must use an escape character in
the date pattern to distinguish the brackets in the data from the brackets used for enclosing
variables).

Syntax:

How to Specify Years in a Date Pattern

[YYYY]

Specifies a four-digit year.

[YYYY]

Specifies a four-digit year.

[YY]

Specifies a two-digit year.

[yy]

Specifies a zero-suppressed two-digit year (for example, 8 for 2008).

[by]

Specifies a blank-padded two-digit year.

Syntax:

How to Specify Month Numbers in a Date Pattern

[MM]

Specifies a two-digit month number.

[mm]

Specifies a zero-suppressed month number.

[bm]

Specifies a blank-padded month number.

Syntax:

How to Specify Month Names in a Date Pattern

[MON]

Specifies a three-character month name in upper case.

[mon]

Specifies a three-character month name in lower case.

224

4. Describing an Individual Field

[Mon]

Specifies a three-character month name in mixed case.

[MONTH]

Specifies a full month name in upper case.

[month]

Specifies a full month name in lower case.

[Month]

Specifies a full month name in mixed case.

Syntax:

How to Specify Days of the Month in a Date Pattern

[DD]

Specifies a two-digit day of the month.

[dd]

Specifies a zero-suppressed day of the month.

[bd]

Specifies a blank-padded day of the month.

Syntax:

How to Specify Julian Days in a Date Pattern

[DDD]

Specifies a three-digit day of the year.

[ddd]

Specifies a zero-suppressed day of the year.

[bdd]

Specifies a blank-padded day of the year.

Syntax:

How to Specify Day of the Week in a Date Pattern

[WD]

Specifies a one-digit day of the week.

[DAY]

Specifies a three-character day name in upper case.

Describing Data With TIBCO WebFOCUS® Language

 225

Converting Alphanumeric Dates to WebFOCUS Dates

[day]

Specifies a three-character day name in lower case.

[Day]

Specifies a three-character day name in mixed case.

[WDAY]

Specifies a full day name in upper case.

[wday]

Specifies a full day name in lower case.

[Wday]

Specifies a full day name in mixed case.

For the day of the week, the WEEKFIRST setting defines which day is day 1.

Syntax:

How to Specify Quarters in a Date Pattern

[Q]

Specifies a one-digit quarter number (1, 2, 3, or 4).

For a string like Q2 or Q02, use constants before [Q], for example, Q0[Q].

Specifying Constants in a Date Pattern

Between the variables, you can insert any constant values.

If you want to insert a character that would normally be interpreted as part of a variable, use
the backslash character as an escape character. For example:

Use \[ to specify a left square bracket constant character.

Use \\ to specify a backslash constant character.

For a single quotation mark, use two consecutive single quotation marks ('').

Sample Date Patterns

If the date in the data source is of the form CY 2001 Q1, the DATEPATTERN attribute is:

DATEPATTERN = 'CY [YYYY] Q[Q]'

If the date in the data source is of the form Jan 31, 01, the DATEPATTERN attribute is:

DATEPATTERN = '[Mon] [DD], [YY]'

226

4. Describing an Individual Field

If the date in the data source is of the form APR-06, the DATEPATTERN attribute is:

DATEPATTERN = '[MON]-[YY]'

If the date in the data source is of the form APR - 06, the DATEPATTERN attribute is:

DATEPATTERN = '[MON] - [YY]'

If the date in the data source is of the form APR '06, the DATEPATTERN attribute is:

DATEPATTERN = '[MON] ''[YY]'

If the date in the data source is of the form APR [06], the DATEPATTERN attribute is:

DATEPATTERN = '[MON] \[[YY]\]' (or '[MON] \[[YY]]'

Note that the right square bracket does not have to be escaped.

Example:

Sorting By an Alphanumeric Date

In the following example, date1.ftm is a sequential file containing the following data:

June 1, '02
June 2, '02
June 3, '02
June 10, '02
June 11, '02
June 12, '02
June 20, '02
June 21, '02
June 22, '02
June 1, '03
June 2, '03
June 3, '03
June 10, '03
June 11, '03
June 12, '03
June 20, '03
June 21, '03
June 22, '03
June 1, '04
June 2, '04
June 3, '04
June 4, '04
June 10, '04
June 11, '04
June 12, '04
June 20, '04
June 21, '04
June 22, '04

Describing Data With TIBCO WebFOCUS® Language

 227

Converting Alphanumeric Dates to WebFOCUS Dates

In the DATE1 Master File, the DATE1 field has alphanumeric USAGE and ACTUAL formats, each
A18:

FILENAME=DATE1   , SUFFIX=FIX ,
  DATASET = c:\tst\date1.ftm    , $
  SEGMENT=FILE1, SEGTYPE=S0, $
    FIELDNAME=DATE1, ALIAS=E01, USAGE=A18, ACTUAL=A18, $

The following request sorts by the DATE1 FIELD:

TABLE FILE DATE1
PRINT DATE1 NOPRINT
BY DATE1
ON TABLE SET PAGE NOPAGE
END

The output shows that the alphanumeric dates are sorted alphabetically, not chronologically:

DATE1
-----
June 1, '02
June 1, '03
June 1, '04
June 10, '02
June 10, '03
June 10, '04
June 11, '02
June 11, '03
June 11, '04
June 12, '02
June 12, '03
June 12, '04
June 2, '02
June 2, '03
June 2, '04
June 20, '02
June 20, '03
June 20, '04
June 21, '02
June 21, '03
June 21, '04
June 22, '02
June 22, '03
June 22, '04
June 3, '02
June 3, '03
June 3, '04
June 4, '04

228

4. Describing an Individual Field

In order to sort the data correctly, you can add a DATEPATTERN attribute to the Master File
that enables WebFOCUS to convert the date to a WebFOCUS date field. You must also edit the
USAGE format to make it a WebFOCUS date format. To construct the appropriate pattern, you
must account for all of the components in the stored date. The alphanumeric date has the
following variables and constants:

Variable: full month name in mixed case, [Month].

Constant: blank space.

Variable: zero-suppressed day of the month number, [dd].

Constant: comma followed by a blank space followed by an apostrophe (coded as two
apostrophes in the pattern).

Variable: two-digit year, [YY].

The edited Master File follows. Note the addition of the DEFCENT attribute to convert the two-
digit year to a four-digit year:

FILENAME=DATE1   , SUFFIX=FIX ,
  DATASET = c:\tst\date1.ftm    , $
  SEGMENT=FILE1, SEGTYPE=S0, $
    FIELDNAME=DATE1, ALIAS=E01, USAGE=MtrDYY, ACTUAL=A18,
      DEFCENT=20,
      DATEPATTERN = '[Month] [dd], ''[YY]', $

Describing Data With TIBCO WebFOCUS® Language

 229

Converting Alphanumeric Dates to WebFOCUS Dates

Now, issuing the same request produces the following output. Note that DATE1 has been
converted to a WebFOCUS date in MtrDYY format (as specified in the USAGE format):

DATE1
-----
June  1, 2002
June  2, 2002
June  3, 2002
June 10, 2002
June 11, 2002
June 12, 2002
June 20, 2002
June 21, 2002
June 22, 2002
June  1, 2003
June  2, 2003
June  3, 2003
June 10, 2003
June 11, 2003
June 12, 2003
June 20, 2003
June 21, 2003
June 22, 2003
June  1, 2004
June  2, 2004
June  3, 2004
June  4, 2004
June 10, 2004
June 11, 2004
June 12, 2004
June 20, 2004
June 21, 2004
June 22, 2004

230

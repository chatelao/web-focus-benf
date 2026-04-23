Chapter9

Checking and Changing a Master File:
CHECK

Use the CHECK command to validate your Master Files. You must always do this after
writing the Master File. If you do not issue the CHECK command, your Master File may
not be reloaded into memory if a parsed copy already exists.

In this chapter:

Checking a Data Source Description

CHECK Command Display

PICTURE Option

HOLD Option

Checking a Data Source Description

The CHECK output highlights any errors in your Master File and allows you to correct each
before reading the data source. After making any necessary corrections, use CHECK again to
confirm that the Master File is valid.

Syntax:

How to Check a Data Source Description

CHECK FILE filename[.field] [PICTURE [RETRIEVE]] [DUPLICATE]
[HOLD [AS name] [ALL]]

where:

filename

Is the name under which you created the Master File.

.field

Is used for an alternate view of the Master File.

PICTURE

Is an option that displays a diagram showing the complete data source structure. The
keyword PICTURE can be abbreviated to PICT. This option is explained in PICTURE Option
on page 399.

Describing Data With TIBCO WebFOCUS® Language

 395

CHECK Command Display

RETRIEVE

Alters the picture to reflect the order in which segments are retrieved when TABLE or
TABLEF commands are issued. Note that unique segments are viewed as logical
extensions of the parent segment. The keyword RETRIEVE can be abbreviated to RETR.

DUPLICATE

Lists duplicate field names for the specified data source. The keyword DUPLICATE can be
abbreviated to DUPL.

HOLD

Generates a temporary HOLD file and HOLD Master File containing information about fields
in the data source. You can use this HOLD file to write reports. The AS option specifies a
field name for your data sources. The option is described and illustrated in HOLD Option on
page 401.

name

Is a name for the HOLD file and HOLD Master File.

ALL

Adds the values of FDEFCENT and FYRTHRESH at the file level and the values of DEFCENT
and YRTHRESH at the field level to the HOLD file.

CHECK Command Display

If your Master File contains syntactical errors, the CHECK command displays appropriate
messages.

Reference: CHECK FILE Command Output

If the data source description has no syntactical errors, the CHECK command displays the
following message

NUMBER OF ERRORS=     0
NUMBER OF SEGMENTS=   n  ( REAL=    n VIRTUAL=    n )
NUMBER OF FIELDS=     n  INDEXES=   n FILES=      n
NUMBER OF DEFINES=    n
TOTAL LENGTH OF ALL FIELDS=  n

where:

NUMBER OF ERRORS

Indicates the number of syntactical errors in the Master File.

NUMBER OF SEGMENTS

Is the number of segments in the Master File, including cross-referenced segments.

396

9. Checking and Changing a Master File: CHECK

REAL

Is the number of segments that are not cross-referenced. These segments have types Sn,
SHn, U, or blank.

VIRTUAL

Is the number of segments that are cross-referenced. These segments have types KU,
KLU, KM, KL, DKU, or DKM.

NUMBER OF FIELDS

Is the number of fields described in the Master File.

INDEXES

Is the number of indexed fields. These fields have the attribute FIELDTYPE=I or INDEX=I in
the Master File.

FILES

Is the number of data sources containing the fields.

NUMBER OF DEFINES

Is the number of virtual fields in the Master File. This message appears only if virtual fields
are defined.

TOTAL LENGTH

Is the total length of all fields as defined in the Master File by either the FORMAT attribute
(if the data source is a FOCUS data source) or the ACTUAL attribute (if the data source is a
non-FOCUS data source).

Example:

Using the CHECK File Command

Entering the following command

CHECK FILE EMPLOYEE

produces the following information:

NUMBER OF ERRORS=     0
NUMBER OF SEGMENTS=  11     ( REAL=   6 VIRTUAL=  5 )
NUMBER OF FIELDS=    34     INDEXES=  0 FILES=    3
TOTAL LENGTH OF ALL FIELDS = 365

Describing Data With TIBCO WebFOCUS® Language

 397

CHECK Command Display

Determining Common Errors

If the data source is a non-FOCUS data source, check the TOTAL LENGTH OF ALL FIELDS to
verify the accuracy of the field lengths specified. One of the most common causes of errors
in generating reports from non-FOCUS data sources is incorrectly specified field lengths.
The total length of all fields should be equal to the logical record length of the non-FOCUS
data source.

In general, if the total length of all fields is not equal to the logical record length of the non-
FOCUS data source, the length of at least one field is specified incorrectly. Your external
data may not be read correctly if you do not correct the error.

If the following warning message is generated, duplicate fields (those having the same field
names and aliases) are not allowed in the same segment. The second occurrence is never
accessed.

(FOC1829) WARNING. FIELDNAME IS NOT UNIQUE WITHIN A SEGMENT: fieldname

When the CHECK command is issued for a data source with more than one field of the
same name in the same segment, a FOC1829 message is generated along with a warning
such as the following indicating that the duplicate fields cannot be accessed:

(FOC1829) WARNING. FIELDNAME IS NOT UNIQUE WITHIN A SEGMENT: BB
WARNING: FOLLOWING FIELDS CANNOT BE ACCESSED
BB  IN SEGMENT SEGA        (VS SEGB

When the DUPLICATE option is added, the output contains a warning message that
indicates where the first duplicate field resides:

WARNING: FOLLOWING FIELDS APPEAR MORE THAN ONCE
AA IN SEGMENT SEGB        (VS SEGA)

398

9. Checking and Changing a Master File: CHECK

PICTURE Option

The PICTURE option displays a diagram of the structure defined by the Master File. Each
segment is represented by a box. There are four types of boxes, which indicate whether a
segment (including the root segment) is non-unique or unique and whether it is real or cross-
referenced. The four types of boxes are

Real segments

Non-unique segment:

Unique segment:

segname
   numsegtype
   **************
   *field1      **I
   *field2      **
   *field3      **
   *field4      **
   *            **
   ***************
    **************

Cross-referenced segments

            segname
   num      U
   **************
   *field1      *I
   *field2      *
   *field3      *
   *field4      *
   *            *
   **************

Non-unique segment:

Unique segment

segname
   num      KM (or KLM)
   ..............
   :field1      ::K
   :field2      ::
   :field3      ::
   :field4      ::
   :            ::
   :...........::
    ............:
           crfile

  segname
   num      KU (or KLU)
   ..............
   :field1      :K
   :field2      :
   :field3      :
   :field4      :
   :            :
   :............:
           crfile

Describing Data With TIBCO WebFOCUS® Language

 399



PICTURE Option

where:

num

Is the number assigned to the segment in the structure.

segname

Is the name of the segment.

segtype

Is the segment type for a real, non-unique segment: Sn, SHn, or N (for blank segtypes).

field1...

Are the names of fields in the segment. Field names greater than 12 characters are
truncated to 12 characters in CHECK FILE PICTURE operations, with the last character
appearing as a ' >', indicating that more characters exist than can be shown.

I

K

Indicates an indexed field.

Indicates the key field in the cross-referenced segment.

crfile

Is the name of the cross-referenced data source if the segment is cross-referenced.

The diagram also shows the relationship between segments (see the following example).
Parent segments are shown above children segments connected by straight lines.

400

9. Checking and Changing a Master File: CHECK

Example:

Using the CHECK FILE PICTURE Option

The following diagram shows the structure of the JOB data source joined to the SALARY data
source:

JOIN EMP_ID IN JOB TO EMP_ID IN SALARY
>
CHECK FILE JOB PICTURE
 NUMBER OF ERRORS=    0
 NUMBER OF SEGMENTS=  2  ( REAL=    1  VIRTUAL=   1 )
 NUMBER OF FIELDS=    7  INDEXES=   0  FILES=     2
 TOTAL LENGTH OF ALL FIELDS=   86
SECTION 01
             STRUCTURE OF FOCUS    FILE JOB      ON 01/31/03 AT 12.33.04

         JOBSEG
 01      S1
**************
*EMP_ID      **
*FIRST_NAME  **
*LAST_NAME   **
*JOB_TITLE   **
*            **
***************
 **************
       I
       I
       I
       I SALSEG
 02    I KU
..............
:EMP_ID      :K
:SALARY      :
:EXEMPTIONS  :
:            :
:            :
:............:
JOINED  SALARY

HOLD Option

The HOLD option generates a temporary HOLD file. HOLD files are explained in the Creating
Reports With WebFOCUS Language manual. This HOLD file contains detailed information
regarding file, segment, and field attributes, which you can display in reports using TABLE
requests.

Certain fields in this HOLD file are of special interest. Unless otherwise noted, these fields are
named the same as attributes in Master Files. Each field stores the values of the similarly
named attribute. The fields can be grouped into file attributes, segment attributes, and field
attributes.

Describing Data With TIBCO WebFOCUS® Language

 401


HOLD Option

File Attributes:

FILENAME, SUFFIX, FDEFCENT, FYRTHRESH

Note that the FDEFCENT and FYRTHRESH attributes are included in the HOLD file, if they
exist in the original Master File and you specify the ALL option.

Segment Attributes:

SEGNAME, SEGTYPE

Note that this field does not indicate the number of segment key fields. Segment types
S1, S2, and so on are shown as type S. The same is true with segment type SHn.

SKEYS

The number of segment key fields. For example, if the segment type is S2, SKEYS has the
value 2.

SEGNO

The number assigned to the segment within the structure. This appears in the picture.

LEVEL

The level of the segment within the structure. The root segment is on Level 1, its children
are on Level 2, and so on.

PARENT, CRKEY, FIELDNAME

Field Attributes:

ALIAS, FORMAT, ACTUAL

Note that if you include the FORMAT field in the TABLE request, do not use the full field
name FORMAT. Rather, you should use the alias USAGE or a unique truncation of the
FORMAT field name (the shortest unique truncation is FO).

DEFCENT, YRTHRESH

Note that these attributes are included in the HOLD file, if they exist in the original Master
File and you specify the ALL option.
Using the CHECK FILE HOLD Option

Example:

This sample procedure creates a HOLD file describing the EMPLOYEE data source. It then
writes a report that displays the names of cross-referenced segments in the EMPLOYEE data
source, the segment types, and the attributes of the fields: field names, aliases, and formats.

402

9. Checking and Changing a Master File: CHECK

CHECK FILE EMPLOYEE HOLD
TABLE FILE HOLD
HEADING
"FIELDNAMES, ALIASES, AND FORMATS"
"OF CROSS-REFERENCED FIELDS IN THE EMPLOYEE DATA SOURCE"
" "
PRINT FIELDNAME/A12 ALIAS/A12 USAGE BY SEGNAME BY SEGTYPE
WHERE SEGTYPE CONTAINS 'K'
END

The output is:

PAGE 1

FIELDNAMES, ALIASES, AND FORMATS
OF CROSS-REFERENCED FIELDS IN THE EMPLOYEE DATA SOURCE

SEGNAME    SEGTYPE            FIELDNAME      ALIAS   FORMAT
-------    -------            ---------      -----   ------
ATTNDSEG   KM                 DATE_ATTEND    DA      I6YMD
                              EMP_ID         EID     A9
COURSEG    KLU                COURSE_CODE    CC      A6
                              COURSE_NAME    CD      A30
JOBSEG     KU                 JOBCODE        JC      A3
                              JOB_DESC       JD      A25
SECSEG     KLU                SEC_CLEAR      SC      A6
SKILLSEG   KL                 SKILLS                 A4
                              SKILL_DESC     SD      A30

Example:

Using the CHECK FILE HOLD ALL Option

Assume the EMPLOYEE data source contains the following FILE declaration:

FILENAME = EMPLOYEE, SUFFIX = FOC, FDEFCENT = 19, FYRTHRESH = 50

The following request:

CHECK FILE EMPLOYEE HOLD ALL
TABLE FILE HOLD
PRINT FDEFCENT FYRTHRESH
END

produces the following output:

FDEFCENT    FYRTHRESH
--------    ---------
      19           50

Describing Data With TIBCO WebFOCUS® Language

 403



HOLD Option

Specifying an Alternate File Name With the HOLD Option

An AS name may be provided for the temporary HOLD file generated by the CHECK command.
If a name is not specified, the default name is HOLD and any existing default file will be
replaced.

Note: When the AS option is specified in combination with other CHECK options, the AS
holdname specification must appear last.

TITLE, HELPMESSAGE, and TAG Attributes

When using the HOLD option of the CHECK command, the TITLE text is placed in the TITLE
field of the FLDATTR segment, the HELPMESSAGE text in the HELPMESSAGE field of the
FLDATTR segment, and the TAG names in the TAGNAME field of the SEGATTR segment.

When no JOINs are in effect, or when a JOIN command is issued without a TAG name, the
TAGNAME field by default contains the name of the data source specified in the CHECK
command. When JOINs are issued in conjunction with the TAG name feature, the TAGNAME
field contains the TAG name for the host and cross-referenced data sources.

Virtual Fields in the Master File

With the HOLD option, virtual fields are placed in the segment in which they would be stored if
they were real fields in the data source. This is not necessarily the physical location of the field
in the Master File, but the lowest segment that must be accessed in order to evaluate the
expression defining the field. Fields whose values are not dependent on retrieval default to the
top segment. The value of FLDSEG in the FLDATTR segment is zero for these fields. The format
of FLDSEG is I2S in the Master File, which causes zero to appear as blank in reports. FLDSEG
may be dynamically reformatted in a TABLE request (FLDSEG/I2) to force the display of zero.

After data has been entered into a data source, you can no longer make arbitrary changes to
the Master File. Some changes are entirely harmless and can be made at any time. Others are
prohibited unless the data is reentered or the data source rebuilt. A few others can be made if
corresponding changes are made in several places.

You can use a text editor to make permitted changes to the Master File. The checking
procedure, CHECK, should be used after any change.

404

Chapter8

Creating a Business View of a Master File

A Business View (BV) of a Master File groups related items together to reflect an
application business logic rather than the physical position of items in the data source.
By separating the information model of the data from its physical storage mechanisms,
the Business View gives developers and users access to the information they need in
order to solve a business problem without involving them in the intricacies of the
database design.

In this chapter:

Grouping Business Logic In a Business View

Business View DV Roles

Grouping Business Logic In a Business View

A Business View is a limited set of fields accessible by users and stored as part of a real
Master File. Defining a Business View provides users with a limited view of the data, simplifies
application maintenance, and provides additional security.

A Business View is organized into virtual segments called folders, which are defined below all
of the real and cross-reference segments in the Master File. Each folder can contain a group of
fields and can contain other folders. A folder can also be empty. The fields in a folder can
come from different segments in the Master File. If the fields do not lie along a single path in
the Master File and your request includes fields from separate paths, warning messages may
be generated when you run the request.

Hierarchies of folders can be defined by specifying the PARENT attribute in the child folder
declarations.

When a Business View is used in a request, all of the actual field and security information
comes from the original segments. If the field is from a cross-referenced segment in the
Master File, all of the cross-reference segment and key information remains in the original
Master File containing that segment.

If you open a Master File that contains a Business View in a WebFOCUS tool, only the folders
in the Business View display.

A Business View can include real fields, calculated values (COMPUTEs), virtual fields
(DEFINEs), and filters from the original Master File.

Describing Data With TIBCO WebFOCUS® Language

 383

Grouping Business Logic In a Business View

Business Views are most useful as views of relational and FOCUS data sources.

The field and segment names in a Business View can be the same as the names in the
original segments, or you can assign new names in the Business View. When a new field name
is assigned in a Business View, the ALIAS value must be the original field name.

Syntax:

How to Define a Folder

FOLDER = folder_name, [PARENT=parent_folder_name
    [,DESCRIPTION="default_desc"
    [, DESC_ln="desc_for_ln" ...]] $
     [FIELD = bv_field_name, [ALIAS=real_field_name] ,
     [BELONGS_TO_SEGMENT= real_segment_name]  ,
     [, TITLE = "default_title"
     [, TITLE_ln="title_for_ln" ...]]]
     [, DESC="default_desc"
     [, DESC_ln="desc_for_ln" ...], $]]
      FIELD= bv_field_name[, ALIAS = real_field_name],
          BELONGS_TO_SEGMENT = real_segment_name
          [,TITLE = default_title]
          [,TITLE_ln = title_for_ln]
          [,DESCRIPTION = default_description ]
          [,DESCRIPTION_ln = desc_for_ln]  ,$

where:

folder_name

Is the name of a virtual segment in the view. A folder is allowed to be empty.

parent_folder_name

Is the name of the parent of the virtual segment.

bv_field_name

Is the field name you assign. It can be the same as the real field name or a different field
name. If it is different, the real field is identified by the ALIAS attribute.

real_field_name

Is the name of the field in the original Master File. This field can be a real field, a virtual
field, or a calculated value. If bv_field_name matches real_field_name, the ALIAS attribute
can be omitted. If no ALIAS is specified, the Business View field name must match the
field name in the original Master File.

384

8. Creating a Business View of a Master File

real_segment_name

Is the name of the segment in which the field resides in the original Master File. If the real
field name is unique in the original Master File, the BELONGS_TO_SEGMENT attribute can
be omitted. If BELONGS_TO_SEGMENT is missing and the field name is not unique in the
original Master File, the first field with a matching field name in the original Master File is
used.

default_title

Is the column title to use when the LANG parameter is set to the default language for the
server, or another language is set but the Master File has no corresponding TITLE_ln
attribute for that field. This title is also used if the ln value is invalid.

default_desc

Is descriptive text to use when the LANG parameter is set to the default language for the
server, or another language is set but the Master File has no corresponding DESC_ln
attribute for that field. This description is also used if the ln value is invalid. This
description displays in the front-end user interface.

ln

Specifies the language for which the title or description applies. Valid values for ln are the
two-letter ISO 639 language code abbreviations.

title_for_ln

Is the title to use when the LANG parameter is set to a non-default language for the server,
and the Master File has a corresponding TITLE_ln attribute, where ln is the two-digit code
for the language specified by the LANG parameter.

desc_for_ln

Is the description to use when the LANG parameter is set to a non-default language for the
server, and the Master File has a corresponding DESC_ln attribute, where ln is the two-digit
code for the language specified by the LANG parameter.

Reference: Languages and Language Codes

Language Name

Arabic

Baltic

Two-Letter
Language Code

Three-Letter Language
Abbreviation

ar

lt

ARB

BAL

Describing Data With TIBCO WebFOCUS® Language

 385

Grouping Business Logic In a Business View

Language Name

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

Italian

Japanese - Shift-JIS (cp942) on ASCII
cp939 on EBCDIC

Japanese - EUC (cp10942) on ASCII
(UNIX)

Korean

Norwegian

Polish

386

Two-Letter
Language Code

Three-Letter Language
Abbreviation

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

it

ja

je

ko

no

pl

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

ITA

JPN

JPE

KOR

NOR

POL

Language Name

Portuguese - Brazilian

Portuguese - Portugal

Russian

Spanish

Swedish

Thai

Turkish

8. Creating a Business View of a Master File

Two-Letter
Language Code

Three-Letter Language
Abbreviation

br

pt

ru

es

sv

th

tr

POR

POR

RUS

SPA

SWE

THA

TUR

Reference: Usage Notes for Business Views

The detailed information about fields, such as USAGE and ACTUAL formats or indexes
remain in the original segment.

To include fields from more than one Master File in the Business View, the segments must
all be included in the Master File that contains the Business View, either as a cross-
reference or a cluster join.

DBA attributes that are defined in the Master File that contains the Business View will apply
to the Business View. To apply DBA attributes from cross-reference segments, the SET
DBASOURCE=ALL command must be in effect.

Business Views do not support data source maintenance commands such as Maintain.

When a Master File contains more than one field with the same name, as can occur when
files are joined, the BELONGS_TO_SEGMENT attribute identifies which instance of the field
name is being referenced in the Business View.

Folders can be empty.

The USE command supports Business Views.

Master File profiles (MFD_PROFILE attribute) are run for each Master File accessed.

SORTOBJ and STYLEOBJ declarations are not supported in the original master

Describing Data With TIBCO WebFOCUS® Language

 387

Grouping Business Logic In a Business View

You can issue an SQL SELECT command against a Business View. However, a Direct SQL
Passthru request is not supported against a Business View.

Business Views can be encrypted and decrypted with the ENCRYPT and DECRYPT
commands.

Business Views support alternate file views and fully qualified field names.

The SEG. operator against a Business View folder displays all of the fields in that folder,
not all of the fields in the real segment.

All HOLD formats are supported against a Business View.

All adapters for non-FOCUS data sources support retrieval requests against a Business
View.

Example:

Creating a Business View

The following Business View of the EMPLOYEE data source consists of three folders:

The first folder contains the employee ID, name current salary, and current job code fields
from the EMPLOYEE Master File.

The second folder contains the salary and increase history fields from the PAYINFO
segment of the original Master File.

The third folder contains the job code and job description fields from the JOBSEG segment,
which is a cross-referenced segment.

388

8. Creating a Business View of a Master File

Note that a field named JOBCODE exists in folders 2 and 3. The BELONGS_TO_SEGMENT
attribute distinguishes between the JOBCODE field from the PAYINFO segment and the
JOBCODE field from the JOBSEG segment in the EMPLOYEE Master File. Also note that the
fields defined with different names than in the real segments have ALIAS values that specify
the field names in the real segments.

FILENAME=EMPLOYEE, SUFFIX=FOC, REMARKS='Legacy Metadata Sample: employee',$
SEGNAME=EMPINFO,  SEGTYPE=S1
 FIELDNAME=EMP_ID,       ALIAS=EID,     FORMAT=A9,       $
 FIELDNAME=LAST_NAME,    ALIAS=LN,      FORMAT=A15,      $
 FIELDNAME=FIRST_NAME,   ALIAS=FN,      FORMAT=A10,      $
 FIELDNAME=HIRE_DATE,    ALIAS=HDT,     FORMAT=I6YMD,    $
 FIELDNAME=DEPARTMENT,   ALIAS=DPT,     FORMAT=A10,      $
 FIELDNAME=CURR_SAL,     ALIAS=CSAL,    FORMAT=D12.2M,   $
 FIELDNAME=CURR_JOBCODE, ALIAS=CJC,     FORMAT=A3,       $
 FIELDNAME=ED_HRS,       ALIAS=OJT,     FORMAT=F6.2,     $
SEGNAME=FUNDTRAN, SEGTYPE=U,   PARENT=EMPINFO
 FIELDNAME=BANK_NAME,    ALIAS=BN,      FORMAT=A20,      $
 FIELDNAME=BANK_CODE,    ALIAS=BC,      FORMAT=I6S,      $
 FIELDNAME=BANK_ACCT,    ALIAS=BA,      FORMAT=I9S,      $
 FIELDNAME=EFFECT_DATE,  ALIAS=EDATE,   FORMAT=I6YMD,    $
SEGNAME=PAYINFO,  SEGTYPE=SH1, PARENT=EMPINFO
 FIELDNAME=DAT_INC,      ALIAS=DI,      FORMAT=I6YMD,    $
 FIELDNAME=PCT_INC,      ALIAS=PI,      FORMAT=F6.2,     $
 FIELDNAME=SALARY,       ALIAS=SAL,     FORMAT=D12.2M,   $
 FIELDNAME=JOBCODE,      ALIAS=JBC,     FORMAT=A3,       $
SEGNAME=ADDRESS,  SEGTYPE=S1,  PARENT=EMPINFO
 FIELDNAME=TYPE,         ALIAS=AT,      FORMAT=A4,       $
 FIELDNAME=ADDRESS_LN1,  ALIAS=LN1,     FORMAT=A20,      $
 FIELDNAME=ADDRESS_LN2,  ALIAS=LN2,     FORMAT=A20,      $
 FIELDNAME=ADDRESS_LN3,  ALIAS=LN3,     FORMAT=A20,      $
 FIELDNAME=ACCTNUMBER,   ALIAS=ANO,     FORMAT=I9L,      $
SEGNAME=SALINFO,  SEGTYPE=SH1, PARENT=EMPINFO
 FIELDNAME=PAY_DATE,     ALIAS=PD,      FORMAT=I6YMD,    $
 FIELDNAME=GROSS,        ALIAS=MO_PAY,  FORMAT=D12.2M,   $
SEGNAME=DEDUCT,   SEGTYPE=S1,  PARENT=SALINFO
 FIELDNAME=DED_CODE,     ALIAS=DC,      FORMAT=A4,       $
 FIELDNAME=DED_AMT,      ALIAS=DA,      FORMAT=D12.2M,   $
SEGNAME=JOBSEG,  SEGTYPE=KU ,PARENT=PAYINFO, CRFILE=JOBFILE, CRKEY=JOBCODE,$
SEGNAME=SECSEG,  SEGTYPE=KLU,PARENT=JOBSEG,  CRFILE=JOBFILE,$
SEGNAME=SKILLSEG,SEGTYPE=KL, PARENT=JOBSEG,  CRFILE=JOBFILE,$
SEGNAME=ATTNDSEG,SEGTYPE=KM, PARENT=EMPINFO, CRFILE=EDUCFILE,CRKEY=EMP_ID,$
SEGNAME=COURSEG, SEGTYPE=KLU,PARENT=ATTNDSEG,CRFILE=EDUCFILE,$

Describing Data With TIBCO WebFOCUS® Language

 389

Grouping Business Logic In a Business View

FOLDER=FOLDER1, $
 FIELDNAME=EMPID, ALIAS=EMP_ID,
  BELONGS_TO_SEGMENT=EMPINFO, $
FIELDNAME=LASTNAME, ALIAS=LAST_NAME,
  BELONGS_TO_SEGMENT=EMPINFO, $
FIELDNAME=FIRSTNAME,
  ALIAS=FIRST_NAME,
  BELONGS_TO_SEGMENT=EMPINFO, $
 FIELDNAME=DEPARTMENT,
  BELONGS_TO_SEGMENT=EMPINFO, $
 FIELDNAME=CURRSAL, ALIAS=CURR_SAL,
  BELONGS_TO_SEGMENT=EMPINFO, $
 FIELDNAME=CURR_JOBCODE,
  BELONGS_TO_SEGMENT=EMPINFO, $

FOLDER=FOLDER3, PARENT=FOLDER1, $
 FIELDNAME=DAT_INC,
  BELONGS_TO_SEGMENT=PAYINFO, $
 FIELDNAME=PCT_INC,
  BELONGS_TO_SEGMENT=PAYINFO, $
 FIELDNAME=SALARY,
  BELONGS_TO_SEGMENT=PAYINFO, $
 FIELDNAME=JOBCODE,
  BELONGS_TO_SEGMENT=PAYINFO, $

FOLDER=FOLDER2, PARENT=FOLDER1, $
 FIELDNAME=JOBCODE,
  BELONGS_TO_SEGMENT=JOBSEG, $
 FIELDNAME=JOB_DESC,
  BELONGS_TO_SEGMENT=JOBSEG, $

One of the folders contains the JOBCODE field from the JOBSEG segment. The JOBSEG
segment in EMPLOYEE is a cross-referenced segment that points to the JOBFILE Master File.
The JOBFILE Master File follows:

FILENAME=JOBFILE  ,SUFFIX=FOC, $
SEGNAME=JOBSEG   ,SEGTYPE=S1
 FIELD=JOBCODE     ,ALIAS=JC          ,USAGE=A3          ,INDEX=I,$
 FIELD=JOB_DESC    ,ALIAS=JD          ,USAGE=A25                 ,$
SEGNAME=SKILLSEG ,SEGTYPE=S1   ,PARENT=JOBSEG
 FIELD=SKILLS      ,ALIAS=            ,USAGE=A4                  ,$
 FIELD=SKILL_DESC  ,ALIAS=SD          ,USAGE=A30                 ,$
SEGNAME=SECSEG   ,SEGTYPE=U    ,PARENT=JOBSEG
 FIELD=SEC_CLEAR   ,ALIAS=SC          ,USAGE=A6                  ,$

The following procedure references the Business View:

TABLE FILE EMPLOYEE
PRINT FOLDER3.JOBCODE JOB_DESC
BY LASTNAME BY FIRSTNAME
BY HIGHEST 1 DAT_INC  NOPRINT
END

390

8. Creating a Business View of a Master File

The output is:

LAST_NAME        FIRST_NAME  JOBCODE  JOB_DESC
---------        ----------  -------  --------
BANNING          JOHN        A17      DEPARTMENT MANAGER
BLACKWOOD        ROSEMARIE   B04      SYSTEMS ANALYST
CROSS            BARBARA     A17      DEPARTMENT MANAGER
GREENSPAN        MARY        A07      SECRETARY
IRVING           JOAN        A15      ASSIST.MANAGER
JONES            DIANE       B03      PROGRAMMER ANALYST
MCCOY            JOHN        B02      PROGRAMMER
MCKNIGHT         ROGER       B02      PROGRAMMER
ROMANS           ANTHONY     B04      SYSTEMS ANALYST
SMITH            MARY        B14      FILE QUALITY
                 RICHARD     A01      PRODUCTION CLERK
STEVENS          ALFRED      A07      SECRETARY

Next, add a filter to the EMPLOYEE Master File, and include it in FOLDER1 of the Business
View.

In the EMPLOYEE Master File:

FILTER DFILTER  WITH EMPINFO.EMP_ID=DEPARTMENT EQ 'MIS'; $

In the Business View:

FIELDNAME=DFILTER, ALIAS=DFILTER, BELONGS_TO_SEGMENT=EMPINFO, $

The following request implements the filter:

TABLE FILE EMPLOYEE
PRINT FOLDER3.JOBCODE JOB_DESC
BY LASTNAME BY FIRSTNAME
BY HIGHEST 1 DAT_INC  NOPRINT
WHERE DFILTER
END

The output is:

LAST_NAME        FIRST_NAME  JOBCODE  JOB_DESC
---------        ----------  -------  --------
BLACKWOOD        ROSEMARIE   B04      SYSTEMS ANALYST
CROSS            BARBARA     A17      DEPARTMENT MANAGER
GREENSPAN        MARY        A07      SECRETARY
JONES            DIANE       B03      PROGRAMMER ANALYST
MCCOY            JOHN        B02      PROGRAMMER
SMITH            MARY        B14      FILE QUALITY

Describing Data With TIBCO WebFOCUS® Language

 391

Business View DV Roles

Business View DV Roles

A traditional Business View offered users a customized logical view of a data source by
grouping related items into folders that reflect business logic for an application, rather than the
physical position of items in the data source. However, the fields in these folders did not have
any indication of their roles in a request.

A traditional Dimension View, on the other hand, categorized fields on the basis of their roles
in a request. Measures were placed in measure groups, hierarchies were organized within
dimensions, levels were organized within hierarchies, and attributes were organized within
levels. Then, when a field was double-clicked in InfoAssist or dragged onto the report or chart
canvas in App Studio, it was added as a sort field or aggregation field depending on its
placement in the Dimension View structure. Dimension Views, however, offered no ability to
create a custom logical view of the data source.

DV Roles in a Business View enable you to group fields into folders and, for each field, assign
a role that indicates its role in a request. The syntax is clear and simple, and it gives you total
flexibility in creating folders anywhere in the structure, and in reusing fields in multiple folders.

For example, if you assign the role DIMENSION to a field, it will automatically be added to the
By field container for reports and the horizontal axis for charts if you double-click or drag the
field onto the report or chart canvas. If you assign the role Drill Level to successive fields in a
folder and turn AUTODRILL on, automatic drilldowns will be generated from the top level to the
bottom level on the generated output.

You can create or edit a synonym in the Reporting Server Web Console, the Data Management
Console, or the App Studio Metadata Canvas.

Assigning DV Roles

In Business Views, you define folders, which function as segments to provide a view of the
synonym and to define the accessible fields and their relationships. Folder relationships are
the same as segment relationships, with parent folders, child folders, and sibling folders.

While you have total flexibility defining a structure using any fields from your data source, when
you issue a report request against the synonym, the retrieval path for the data must conform
to any constraints imposed by your DBMS entity diagrams and by the rules of WebFOCUS
retrieval.

By default, when you open a cluster synonym in the WebFOCUS tools, the dimension nodes are
created as folders in the Business View. You can add nodes or folders, but the
recommendation is to use the DV structure if one already exists.

Only the folders will be displayed in the WebFOCUS tools, not the real segments, and only the
fields within the folder structure will be accessible for reporting.

392

8. Creating a Business View of a Master File

You can assign a DV role to a folder or field by right-clicking the folder or field and selecting a
DV role.

You can explicitly assign a DV role to a folder or field, or have it automatically inherit its role
from its parent. If you explicitly assign a DV role, that role moves with the object if you move it
to another location within the BV structure. If you do not explicitly assign a DV role, the role
changes as you move the object under a new parent, except if you move it onto a field with the
Drill Level role. If moved onto a Drill Level field, the moved field inherits the Drill Level role.

The following DV roles can be assigned.

Dimension. A dimension field, when double-clicked or dragged onto the report or chart
canvas in the WebFOCUS tools, will automatically be added to the request as a vertical (BY)
sort field.

A folder can be assigned the role Dimension.

A field can be assigned the role Dimension (Standalone) or Dimension (Drill Level). When it
is assigned the role Dimension (Drill Level), it will become part of a hierarchy where the
levels depend on the order of the fields in the folder. Then, when AUTODRILL is turned on,
automatic drilldowns will be created on the report or chart output.

For a folder assigned the DV role Dimension or a field assigned the DV role Dimension
(Standalone), the following attribute is added to the folder or field declaration in the
synonym.

DV_ROLE=DIMENSION

For a field assigned the DV role Dimension (Drill Level), the following attribute is added to
the field declaration in the synonym.

DV_ROLE=LEVEL

A folder can contain only one drill level hierarchy. However, you can use the same fields in
multiple hierarchies by placing each hierarchy in a separate folder. A folder with a drill level
hierarchy is not limited to just the hierarchy. It can contain other fields with different
DV_ROLEs.

Measure. A measure field, when double-clicked or dragged onto the report or chart canvas
in the WebFOCUS tools, will automatically be added to the request as an aggregated value
(SUM), if it is numeric. If it is alphanumeric, it will be added as a vertical (BY) sort field. A
folder or field can be assigned the role Measure.

Describing Data With TIBCO WebFOCUS® Language

 393

Business View DV Roles

For a folder or field assigned the DV role Measure, the following attribute is added to the
folder or field declaration in the synonym.

DV_ROLE=MEASURE

Attribute. An attribute field, when double-clicked or dragged onto the report or chart canvas
in the WebFOCUS tools, will automatically be added to the request as an aggregated value
(SUM), if it is numeric, or as a vertical sort field (BY), if it is alphanumeric. A folder or field
can be assigned the role Attribute.

For a folder or field assigned the DV role Attribute, the following attribute is added to the
folder or field declaration in the synonym.

DV_ROLE=ATTRIBUTE

Folder. A folder is a virtual segment in a BV. It can be assigned the roles Dimension,
Measure, or Attribute.

Note: When a folder is inserted as a child of a field, the attribute PARENT_FIELD describes
this relationship. By default, such a folder and its fields will be assumed to have the
Attribute role.

None. If no role is assigned, the field or folder will inherit its role from its parent. If a role
has been assigned, you can remove it by selecting the option to inherit its role from its
parent.

Example:

Sample Dimension Folder Declaration

The DV_ROLE for the PRODUCT folder is DIMENSION.

 FOLDER=PRODUCT, PARENT=FOLDER1,
    DV_ROLE=DIMENSION,
    DESCRIPTION='Product and Vendor', $

394

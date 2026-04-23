Appendix C

Rounding in WebFOCUS

This appendix describes how WebFOCUS numeric fields store and display data, how
rounding occurs in calculations, and what happens in conversion from one format to
another.

In this appendix:

Data Storage and Display

Rounding in Calculations and Conversions

Data Storage and Display

Values are rounded before storage or before display, depending on the format. Integer fields
(format I) and packed decimal fields (format P) are rounded or truncated before being stored.
Floating-point fields (formats F and D) and decimal floating-point fields (formats M and X) are
stored as entered and rounded for display.

In general, when a final decimal digit is less than 5, the data value rounds down. A data value
with a final digit of 5 or greater rounds up. The following rounding algorithm is used:

1. The incoming value is multiplied by 10.

2. This multiplication repeats the same number of times as the number of decimal places in
the target format. For example, if 123.78 is input to a packed decimal field with one
decimal place, it is multiplied by 10 once:

1237.8

3. Next, 0.5 is added if the incoming value is positive or subtracted if the incoming value is

negative:

1237.8 + 0.5 = 1238.3

or, if the input value was -123.78,

-1237.8 - 0.5 = -1238.3

4. The value is truncated, and the decimal is shifted to the left.

123.8

or, if the original value was negative,

Describing Data With TIBCO WebFOCUS® Language

 519

Data Storage and Display

-123.8

The following chart illustrates the rounding differences between WebFOCUS numeric field
formats. Subsequent topics discuss these differences in detail.

Format

Type

Format

Input

Stored

Display

I

F

D

M

X

P

Integer

Floating-Point
Single-Precision

Floating-Point
Double-Precision

Decimal
Precision
Floating-Point

Extended
Decimal
Precision
Floating-Point

Packed

I3

F5.1

F3

D3

D5.1

M5.1

M3

X3

X5.1

P3

P5.1

123.78

0124

124

123.78

123.7800

124

123.78

123.7800

123.8

123.78

123.78

124

123.8

123.78000
0000000

123.78000
0000000

123.78

123.7800

124

123.78

123.7800

123.8

123.78

123.78

124

123.8

123.78000
0000000

123.78000
0000000

123.78

0000124

124

123.78

00001238

123.8

Note: For floating-point fields (format D or F), the stored values of decimal numbers are in
hexadecimal and may convert to a value very slightly less than the actual decimal number.
When the final digit is 5, these numbers may round down instead of up. Using the SET
FLOATMAPPING command to treat double precision numbers as decimal precision numbers
can help alleviate this problem.

Integer Fields: Format I

An integer value entered with no decimal places is stored as entered.

520

C. Rounding in WebFOCUS

When a value with decimal places is entered into an integer field using a transaction, that
value is rounded, and the result is stored. If the fractional portion of the value is less than 0.5,
the value is rounded down; if the fractional portion of the value is greater than or equal to 0.5,
the value is rounded up.

However, if an integer field is computed, the decimal portion of the resulting value is
truncated, and the integer portion of the answer is stored (or printed). For example, if the
result of a calculation is 123.78, the value stored is 123.

Floating-Point Fields: Formats F and D

Format type F describes single-precision floating-point numbers stored internally in 4 bytes.
Format F is comparable to COBOL COMP-1. Format type D describes double-precision floating-
point numbers stored internally in 8 bytes. Format D is comparable to COBOL COMP-2.

Formats F and D store as many decimal places as are input, up to the limit of the storage
allocated to the field. Format D is more accurate than format F for larger numbers, since D
fields can store up to 15 significant digits, and format F fields are not accurate beyond a
maximum of 8 digits. Floating-point fields are stored in a logarithmic format. The first byte
stores the exponent. The remaining 3 or 7 bytes store the mantissa, or value.

When the number of decimal places input is greater than the number of decimal places
specified in the format, F and D field values are stored as they are input, up to the limit of
precision. These values are rounded for display according to the field format. For example, if
123.78 is entered in a floating-point field with one decimal place, 123.78 is stored, and 123.8
is displayed.

Decimal Floating-Point Fields: Formats M and X

Format type M describes decimal precision floating-point numbers stored internally in 8 bytes.
Format type X describes extended decimal precision floating-point numbers stored internally in
16 bytes.

Formats M and X store as many decimal places as are input, up to the limit of the precision.
Format X is more accurate than format M for larger numbers, since X fields can store up to 37
significant digits, and M fields are not accurate beyond a maximum of 15 digits. Like formats F
and D, these fields are stored in a logarithmic format. The first byte stores the exponent. The
remaining bytes store the mantissa, or value, in a binary format. The primary difference
between formats M and X and formats F and D is the base to which the exponent is applied.
Formats M and X use base 10, eliminating the rounding issues seen in formats F and D, which
use base 16.

Describing Data With TIBCO WebFOCUS® Language

 521

Data Storage and Display

When the number of decimal places input is greater than the number of decimal places stored
in the format, M and X field values are stored as they are input, up to the limit of precision.
These values are rounded for display according to the field format. For example, if 123.78 is
entered in a format M or X field with one decimal place, 123.78 is stored, and 123.8 is
displayed.

The command SET FLOATMAPPING = {D|M|X} is available to automatically determine how a
floating-point number will be used and stored in subsequent HOLD files. The default format is
D.

Packed Decimal Format: Format P

In packed-decimal format (format type P), each byte contains two digits, except the last byte,
which contains a digit and the sign (D for negative numbers, C for positive). Packed fields are
comparable to COBOL COMP-3.

Packed field values are rounded to the number of digits specified in the field format before
they are stored. When the number of decimal places input is greater than the number that can
be stored, P field values are rounded first, then stored or displayed.

Packed fields are precisely accurate when sufficient decimal places are available to store
values. Otherwise, since values are rounded before being stored, accuracy cannot be improved
by increasing the number of digits displayed. For example, if 123.78 is input to a packed field
with 1 decimal place, 123.8 is stored. If the field format is then changed to P6.2 using a
COMPUTE or DEFINE, 123.80 will be displayed. If the format is changed to P6.2 in the Master
File, 12.38 is displayed.

Note: Continuous improvement to our expression handler, providing more efficient and more
accurate results, may expose some rounding differences between releases when using packed
fields. Enhancements have improved the accuracy of the calculations when working with
packed numbers. Rounding of a packed field is done at the time of storage, changing the
actual number. This is different from precision-based fields, which round when they are
displayed, ensuring that the original number is retained.

Example:

Storing and Displaying Values

For floating-point fields (format F or D), the stored values of decimal numbers are in
hexadecimal and may convert to a value very slightly less than the actual decimal number.
When the final digit is 5, these numbers may round down instead of up.

522

C. Rounding in WebFOCUS

The following example shows an input value with two decimal places, which is stored as a
packed field with two decimal places, a packed field with one decimal place, a D field with one
decimal place, an F field with one decimal place, an M field with one decimal place, and an X
field with one decimal place:

Master File

FILE=FIVE, SUFFIX=FOC
 SEGNAME=ONLY, SEGTYPE=S1,$
  FIELD=PACK2,,P5.2,$
  FIELD=PACK1,,P5.1,$
  FIELD=DOUBLE1,,D5.1,$
  FIELD=FLOAT1,,F5.1,$
  FIELD=MATH1,,M5.1,$
  FIELD=XMATH1,,X5.1,$

Program to Load Data

This MODIFY creates a file with six fields: a P field with two decimal places, a P field with one
decimal place, a D field with one decimal place, an F field with one decimal place, an M field
with one decimal place, and an X field with one decimal place. The same data values are then
loaded into each field.

CREATE FILE FIVE
MODIFY FILE FIVE
FIXFORM  PACK2/5 PACK1/5 DOUBLE1/5 FLOAT1/5 MATH1/5 XMATH1/5
MATCH PACK2
  ON MATCH REJECT
  ON NOMATCH INCLUDE
DATA
1.05 1.05 1.05 1.05 1.05 1.05
1.15 1.15 1.15 1.15 1.15 1.15
1.25 1.25 1.25 1.25 1.25 1.25
1.35 1.35 1.35 1.35 1.35 1.35
1.45 1.45 1.45 1.45 1.45 1.45
1.55 1.55 1.55 1.55 1.55 1.55
1.65 1.65 1.65 1.65 1.65 1.65
1.75 1.75 1.75 1.75 1.75 1.75
1.85 1.85 1.85 1.85 1.85 1.85
1.95 1.95 1.95 1.95 1.95 1.95
END

TABLE Request

This TABLE request prints the values and a total for all six fields.

TABLE FILE FIVE
PRINT PACK2 PACK1 DOUBLE1 FLOAT1 MATH1 XMATH1
ON TABLE SUMMARIZE
ON TABLE SET PAGE NOLEAD
END

Describing Data With TIBCO WebFOCUS® Language

 523

Rounding in Calculations and Conversions

The following report results:

PACK2  PACK1  DOUBLE1  FLOAT1  MATH1  XMATH1
-----  -----  -------  ------  -----  ------
 1.05    1.1      1.1     1.1    1.1     1.1
 1.15    1.2      1.1     1.1    1.2     1.2
 1.25    1.3      1.3     1.3    1.3     1.3
 1.35    1.4      1.4     1.4    1.4     1.4
 1.45    1.5      1.4     1.4    1.5     1.5
 1.55    1.6      1.6     1.6    1.6     1.6
 1.65    1.7      1.6     1.6    1.7     1.7
 1.75    1.8      1.8     1.8    1.8     1.8
 1.85    1.9      1.9     1.9    1.9     1.9
 1.95    2.0      1.9     1.9    2.0     2.0

TOTAL
15.00   15.5     15.0    15.0   15.0    15.0

Note that for the PACK2 value 1.15, the single and double precision floating-point fields round
to 1.1 because the value 1.15 could not be converted exactly to binary, so they were stored as
slightly less than 1.15 (for example, 1.1499999) and rounded down instead of up. All of the
single and double precision values, except 1.25 and 1.75, are stored as repeating decimals in
hexadecimal.

The PACK2 values are not rounded. They are stored and displayed as they were entered.

Since the PACK1 values are rounded up before they are stored, the PACK1 total is 0.5 higher
than the PACK2 total.

The D field total is the same as the PACK2 total because the D field values are stored as
input, and then rounded for display.

Rounding in Calculations and Conversions

Most computations are done in floating-point arithmetic. Packed fields are converted to D
internally, then back to P. Where the operating system supports it, native arithmetic is used for
addition and subtraction for either integer or packed (8-byte) formats. Long packed (16-byte)
format is converted to extended precision numbers for computation.

When a field with decimal places is computed to an integer field, the decimal places are
truncated, and the resulting value is the integer part of the input value.

When a field with decimal places is computed from one format to another, two conversions
take place, unless native arithmetic is being used:

1. First, the field is converted internally to floating-point notation.

2. Second, the result of this conversion is converted to the specified format. At this point, the

rounding algorithm described previously is applied.

524


Example:

Redefining Field Formats

The following example illustrates some differences in the way packed fields, floating-point
fields, decimal precision fields, and integer fields are stored and displayed. It also shows
database values redefined to a format with a larger number of decimal places.

C. Rounding in WebFOCUS

Master File

FILE=EXAMPLE, SUFFIX=FOC
 SEGNAME=ONLY, SEGTYPE=S1,$
  FIELD=PACKED2,,P9.2,$
  FIELD=DOUBLE2,,D9.2,$
  FIELD=FLOAT2,, F9.2,$
  FIELD=INTEGER,,I9  ,$
  FIELD=MATH2,,  M9.2,$
  FIELD=XMATH2,, X9.2,$

Program to Load Data

This MODIFY creates a file with six fields: a P field with two decimal places, a D field with two
decimal places, an F field with two decimal places, an integer field, an M field with two decimal
places, and an X field with two decimal places. The same data values are then loaded into
each field.

CREATE FILE EXAMPLE
MODIFY FILE EXAMPLE
FIXFORM PACKED2/9 X1 DOUBLE2/9 X1 FLOAT2/9 X1 INTEGER/9 X1
FIXFORM MATH2/9 X1 XMATH2/9
MATCH PACKED2
ON MATCH REJECT
ON NOMATCH INCLUDE
DATA
1.6666666 1.6666666 1.6666666 1.6666666 1.6666666 1.6666666
125.16666 125.16666 125.16666 125.16666 125.16666 125.16666
5432.6666 5432.6666 5432.6666 5432.6666 5432.6666 5432.6666
4.1666666 4.1666666 4.1666666 4.1666666 4.1666666 4.1666666
5.5       5.5       5.5       5.5       5.5       5.5
106.66666 106.66666 106.66666 106.66666 106.66666 106.66666
7.2222222 7.2222222 7.2222222 7.2222222 7.2222222 7.2222222
END

Report Request

A DEFINE command creates temporary fields that are equal to PACKED2, DOUBLE2, FLOAT2,
MATH2, and XMATH2 with redefined formats containing four decimal places instead of two.
These DEFINE fields illustrate the differences in the way packed fields, floating-point fields,
and decimal precision fields are stored and displayed.

Describing Data With TIBCO WebFOCUS® Language

 525

Rounding in Calculations and Conversions

The request prints the values and a total for all six database fields, and for the five DEFINE
fields.

DEFINE FILE EXAMPLE
PACKED4/P9.4=PACKED2;
DOUBLE4/D9.4=DOUBLE2;
FLOAT4/D9.4=FLOAT2;
MATH4/M9.4 = MATH2;
XMATH4/X9.4=XMATH2;
END

TABLE FILE EXAMPLE
PRINT PACKED2 PACKED4 DOUBLE2 DOUBLE4 FLOAT2 FLOAT4 MATH2 MATH4 XMATH2
XMATH4 INTEGER
ON TABLE SUMMARIZE
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

The following image shows the resulting output on z/OS:

The following image shows the resulting output on Windows:

526

C. Rounding in WebFOCUS

In this example, the PACKED2 sum is an accurate sum of the displayed values, which are the
same as the stored values. The PACKED4 values and total are the same as the PACKED2
values.

The DOUBLE2 sum looks off by .01 on z/OS and by .04 on Windows. It is not the sum of the
printed values but a rounded sum of the stored values. The DOUBLE4 values show that the
DOUBLE2 values are actually rounded from the stored values. The DOUBLE4 values and sum
show more of the decimal places from which the DOUBLE2 values are rounded.

The FLOAT2 total seems off by .02 on z/OS. Like the DOUBLE2 total, the FLOAT2 total is a
rounded total of the stored FLOAT2 values. F fields are not accurate beyond eight digits, as the
FLOAT4 column shows.

The integer sum is an accurate total. Like packed fields, the storage values and displayed
values are the same.

The MATH2 and XMATH2 sums look off by .01. They are not the sum of the printed values but
a rounded sum of the stored values. The MATH4 and XMATH4 values show that the MATH2
and XMATH2 values are actually rounded from the stored values. The MATH4 and XMATH4
values and sum show more of the decimal places from which the MATH2 and XMATH2 values
are rounded.

The following request illustrates the difference between floating-point and MATH data types.

DEFINE FILE ROUND1
DOUBLE20/D32.20=DOUBLE2;
MATH20/M32.20=MATH2;
END
TABLE FILE ROUND1
PRINT DOUBLE20 MATH20
ON TABLE SUMMARIZE
END

Describing Data With TIBCO WebFOCUS® Language

 527

Rounding in Calculations and Conversions

The output shows that the double precision floating-point number is not exactly the same as
the input values in most cases. It has extra digits for those values that do not have an exact
binary equivalent. The math values represent the input values exactly.

                           DOUBLE20                               MATH20
                           --------                               ------
             1.66666660000000010911               1.66666660000000000000
           125.16666000000000025238             125.16666000000000000000
         5,432.66659999999956198735           5,432.66660000000000000000
             4.16666660000000010911               4.16666660000000000000
             5.50000000000000000000               5.50000000000000000000
           106.66666000000000025238             106.66666000000000000000
             7.22222220000000003637               7.22222220000000000000

TOTAL
         5,683.05547539999770378927           5,683.05547540000000000000

DEFINE and COMPUTE

DEFINE and COMPUTE may give different results for rounded fields. DEFINE fields are treated
like data source fields, while COMPUTE fields are calculated on the results of the display
command in the TABLE request. The following example illustrates this difference:

DEFINE FILE EXAMPLE
DEFP3/P9.3=PACKED2/4;
END

TABLE FILE EXAMPLE
PRINT PACKED2 DEFP3
COMPUTE COMPP3/P9.3=PACKED2/4;
ON TABLE SUMMARIZE
END

The following report results:

PAGE     1

 PACKED2      DEFP3     COMPP3
 -------      -----     ------
    1.67       .417       .417
  125.17     31.292     31.292
 5432.67   1358.167   1358.167
    4.17      1.042      1.042
    5.50      1.375      1.375
  106.67     26.667     26.667
    7.22      1.805      1.805

TOTAL
 5683.07   1420.765   1420.767

528






C. Rounding in WebFOCUS

The DEFP3 field is the result of a DEFINE. The values are treated like data source field values.
The printed total, 1420.765, is the sum of the printed DEFP3 values, just as the PACKED2
total is the sum of the printed PACKED2 values.

The COMPP3 field is the result of a COMPUTE. The printed total, 1420.767, is calculated from
the total sum of PACKED2 (5683.07 / 4).

Describing Data With TIBCO WebFOCUS® Language

 529

Rounding in Calculations and Conversions

530

Legal and Third-Party Notices

SOME TIBCO SOFTWARE EMBEDS OR BUNDLES OTHER TIBCO SOFTWARE. USE OF SUCH
EMBEDDED OR BUNDLED TIBCO SOFTWARE IS SOLELY TO ENABLE THE FUNCTIONALITY (OR
PROVIDE LIMITED ADD-ON FUNCTIONALITY) OF THE LICENSED TIBCO SOFTWARE. THE
EMBEDDED OR BUNDLED SOFTWARE IS NOT LICENSED TO BE USED OR ACCESSED BY ANY
OTHER TIBCO SOFTWARE OR FOR ANY OTHER PURPOSE.

USE OF TIBCO SOFTWARE AND THIS DOCUMENT IS SUBJECT TO THE TERMS AND CONDITIONS
OF A LICENSE AGREEMENT FOUND IN EITHER A SEPARATELY EXECUTED SOFTWARE LICENSE
AGREEMENT, OR, IF THERE IS NO SUCH SEPARATE AGREEMENT, THE CLICKWRAP END USER
LICENSE AGREEMENT WHICH IS DISPLAYED DURING DOWNLOAD OR INSTALLATION OF THE
SOFTWARE (AND WHICH IS DUPLICATED IN THE LICENSE FILE) OR IF THERE IS NO SUCH
SOFTWARE LICENSE AGREEMENT OR CLICKWRAP END USER LICENSE AGREEMENT, THE
LICENSE(S) LOCATED IN THE "LICENSE" FILE(S) OF THE SOFTWARE. USE OF THIS DOCUMENT
IS SUBJECT TO THOSE TERMS AND CONDITIONS, AND YOUR USE HEREOF SHALL CONSTITUTE
ACCEPTANCE OF AND AN AGREEMENT TO BE BOUND BY THE SAME.

This document is subject to U.S. and international copyright laws and treaties. No part of this
document may be reproduced in any form without the written authorization of TIBCO Software
Inc.

TIBCO, the TIBCO logo, the TIBCO O logo, FOCUS, iWay, Omni-Gen, Omni-HealthData, and
WebFOCUS are either registered trademarks or trademarks of TIBCO Software Inc. in the
United States and/or other countries.

Java and all Java based trademarks and logos are trademarks or registered trademarks of
Oracle Corporation and/or its affiliates.

All other product and company names and marks mentioned in this document are the property
of their respective owners and are mentioned for identification purposes only.

This software may be available on multiple operating systems. However, not all operating
system platforms for a specific software version are released at the same time. See the
readme file for the availability of this software version on a specific operating system platform.

THIS DOCUMENT IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS
OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR NON-INFRINGEMENT.

THIS DOCUMENT COULD INCLUDE TECHNICAL INACCURACIES OR TYPOGRAPHICAL ERRORS.
CHANGES ARE PERIODICALLY ADDED TO THE INFORMATION HEREIN; THESE CHANGES WILL
BE INCORPORATED IN NEW EDITIONS OF THIS DOCUMENT. TIBCO SOFTWARE INC. MAY MAKE
IMPROVEMENTS AND/OR CHANGES IN THE PRODUCT(S) AND/OR THE PROGRAM(S)
DESCRIBED IN THIS DOCUMENT AT ANY TIME.

 531

THE CONTENTS OF THIS DOCUMENT MAY BE MODIFIED AND/OR QUALIFIED, DIRECTLY OR
INDIRECTLY, BY OTHER DOCUMENTATION WHICH ACCOMPANIES THIS SOFTWARE, INCLUDING
BUT NOT LIMITED TO ANY RELEASE NOTES AND "READ ME" FILES.

This and other products of TIBCO Software Inc. may be covered by registered patents. Please
refer to TIBCO's Virtual Patent Marking document (https://www.tibco.com/patents) for details.

Copyright © 2021. TIBCO Software Inc. All Rights Reserved.

532

Index

? FILE command 462

&FOCDISORG variable 447

$ VIRT attribute 22, 23

$BOTTOM keyword 409

16K page 294

A

A data type 137

ACCBLN parameter 188

ACCEPT attribute 186, 188–191, 320

FOCUS data sources 320

ACCEPTBLANK parameter 188

ACCESS attribute 406, 414, 422

Access Files 18

applications and 19

creating 21

DATASET attribute and 39

identifying 325, 326

AIX (alternate index names) for VSAM data

sources 279, 281

ALIAS attribute 103, 112

aliases of fields 112

ALLBASE/SQL data sources 33

allocating data sources in Master Files 39–41

ALLOWCVTERR parameter 152

alphanumeric data type 137, 138

alphanumeric dates, converting 223

alternate column titles 191, 192

alternate file views 96, 98

CHECK FILE command and 395–397

long field names and 106

alternate index names (AIX) for VSAM data

sources 279, 281

amper variables 217

in Master File DEFINEs 217

ancestral segments 76, 77

join linkage 360

applications 18

Multi-Dimensional Index (MDI) 333, 334

data descriptions and 18, 19, 31

access to data 405, 418

commands 415

restricting 405, 406, 418, 422

ACCESSFILE attribute 39, 325, 326, 333

accounts hierarchies 181

ACTUAL attribute 103, 170, 171, 174

ADABAS data sources 33

attributes 405

database security 405

AUTODATE 311

AUTOINDEX parameter 341

AUTOPATH parameter 298

B

base dates 150

Describing Data With TIBCO WebFOCUS® Language

 533

Index

blank lines between declarations 27, 28

CHECK FILE command 395–397

blank spaces in declarations 27, 28

HELPMESSAGE attribute and 404

BUFND parameter 278, 279

BUFNI parameter 278, 279

Business Views 383

BYTEORDER attribute 37

C

C-ISAM data sources 34

allocating in Master Files 45, 46

CA-Datacom/DB data sources 33

CA-IDMS data sources 33

CA-IDMS/SQL data sources 33

calculating date fields 149

CAR data source 479, 481

case sensitive passwords 412

CENTFIN data source 501

CENTHR data source 501

CENTINV data source 501

CENTORD data source 501

CENTQA data source 501

Century Corp data sources 501

chart of accounts hierarchies 181

CHECK command 415

CHECK FILE command 395–397

DATASET attribute and 39

DBA and 416

DEFCENT attribute and 395, 401, 403

DUPLICATE option 395, 398

FDEFCENT attribute and 395, 401, 403

534

HOLD ALL option 395, 401–403

HOLD option 395, 401–403

long field names and 106

non-FOCUS data sources and 398

PICTURE option 395, 399, 401

retrieval paths and 395

TAG attribute and 404

TITLE attribute and 404

virtual fields and 404

Y2K attributes and 401, 403

YRTHRESH attribute 395, 401, 403

CHECK subcommand 460

child-parent segment relationships 72, 74–78

CLUSTER component 231

cluster Master File 374

code page 36

column title substitutions 191, 192

columns in relational tables 18

COMBINE command and data security 428–430,

433, 434

comma-delimited data sources 33, 232, 235

repeating fields 244

commands 415

user access levels 415

comments in Master Files 28, 38

COMPUTE command 528

rounding 528

COMPUTEs in Master File 204

Index

concatenated data sources 458

DATA attribute 39–41

conditional join 364

converting date values 149

COURSE data source 486, 487

data buffers for VSAM data sources 278, 279

data descriptions 17, 18

applications and 18, 19, 31

CREATE command 415, 416, 442

creating 21

CREATE FILE command 296

creating Access Files 21

creating data descriptions 21

creating Master Files 21

CRFILE 364

field declarations 20, 103

field relationships 20, 65–68

file declarations 20, 31

Master Files 19, 26

data display 519, 522

CRFILE attribute 352, 353, 357, 363

data encryption 436, 437

CRKEY attribute 352, 353, 363

performance considerations 437

cross-referenced data sources 350, 352

data paths 78–80

ancestral segments 360

data retrieval

descendant segments 356–358

minimum referenced subtree 73

cross-referenced fields 352

cross-referenced segments 352

CRSEG 364

data security 405–407

access levels 414, 418, 420

central Master File 428–430

CRSEGNAME attribute 352, 353, 357

CHECK FILE command and 416

currency display options 133

currency symbols 129

COMBINE command and 428–430, 433, 434

encrypting Master Files 436

extended currency symbols 131

encrypting segments 436, 437

D

D data type 116

rounding of values 135

data access 405, 418

levels of 414, 418, 420

restricting 406, 422

security attributes 405

filters 434

JOIN command and 428–430, 433, 434

passwords 413

restricting access 420, 422, 423

special considerations 408

data source security 405

data sources 17, 31, 471

access control 405, 418

Describing Data With TIBCO WebFOCUS® Language

 535

Index

data sources 17, 31, 471

data types 113, 114, 170, 173, 174, 324

allocating in Master Files 39–41

extended decimal precision floating-point 118

creating 442

floating-point double-precision 116

creating an external index 455, 457

floating-point single-precision 117

date stamps 464

integer 115

describing field relationships 65–68

internal representation 324

describing fields 20, 103

numeric display options 121, 125

describing files 18, 20, 31, 32

packed-decimal 120

documenting 28, 38

erasing 442

file pointers 460

indexes 453

joining 71, 95, 349

multi-dimensional 181–183

OLAP-enabling 181–183

partitioning 324, 325, 327

rebuilding (FOCUS) 444

rotating 96, 98

security 405–407

tab-delimited 232, 236

time stamps 464

types 32, 33

XFOCUS 294–296

data storage 519, 522

rounding of numeric values 135

text 169

data

retrieval 73

database administration (DBA) 405

attributes 405

CHECK FILE command and 416

displaying decision tables 422

database administration (DBA)security 405

Database Administrators (DBAs) 406

identifying 406

security privileges 409

database descriptions 17, 18

applications and 19

creating 21

field declarations 20, 103

data types 113, 114, 170, 173, 174, 324

field relationships 20, 65–68

alphanumeric 137, 138

date storage 142

date-time 154, 156

dates 140, 147, 148, 153

file declarations 20, 31

Master Files 18, 19, 26

database page 294

large 294

decimal precision floating-point 119

database rotation 96, 98

536

Index

database structure 73

Datacom/DB data sources 33

DATASET attribute 39–41

DATE NEW subcommand 465–467

date separators 145

date stamps 464

C-ISAM data sources 45, 46

REBUILD TIMESTAMP subcommand 464

FOCUS data source allocation 42

date translation 146

FOCUS data sources 39

ISAM data sources 45

sequential data sources 43, 44

date-time data types 154

HOLD files and 171, 172

SAVE files and 171, 172

VSAM data sources 45, 46

DATEDISPLAY parameter 150

DATASET behavior in FOCUS data sources 308

ALLOWCVTERR and 152

DATASET priority in the Master File 308

DATEPATTERN attribute 223

DATASET syntax for FOCUS data sources 309

dates, alphanumeric 223

date calculations 149

date conversions 149

DB2 data sources 33

DBA (database administration) 405

date data types 140, 147, 148, 153

attributes 405

calculations 149

converting values 149

Dialogue Manager and 153

display options 140

extract files and 153

graph considerations 153

internal representation 150

literals 142, 147, 148

non-standard formats 152

RECAP command and 153

separators 145

storage 142

translation 146

date display options 140

date literals 142, 147, 148

CHECK FILE command and 416

displaying decision tables 422

DBA attributes 405

DBA decision table 422

DBA passwords 409, 410, 444, 445

DBA security 409

HOLD files 409

DBACSENSITIV parameter 412

DBAFILE attribute 428–430

file naming requirements 433

DBAJOIN 428

DBAs (Database Administrators) 406

identifying 406

security privileges 409

DBATABLE 422

Describing Data With TIBCO WebFOCUS® Language

 537

Index

DBATABLE procedure 422

DBMS data sources 34

decimal data types 116–120

rounding of values 135

decimal floating-point fields

rounding 521

describing data sources 17, 18

Access Files 18

field declarations 20, 103

field relationships 20, 65–68

file declarations 20, 31

FML hierarchies 178

decimal precision floating-point data type 119

Master Files 18, 19, 26

decision tables 422

DESCRIPTION attribute 103, 193, 194

declarations in Master Files 27

designing FOCUS data sources 297, 298

documenting 28

DFIX 282, 285

improving readability 27, 28

diagrams in Master Files 399, 401

declaring data sources 31

decoding values 354

Dialogue Manager 153

variables in Master File DEFINEs 217

DECRYPT command 415, 416

Digital Standard MUMPS data sources 35

decrypting procedures 439

DEFCENT attribute 103

dimensions 181–183

display formats for fields 113, 114, 170, 173,

CHECK FILE command and 395, 401, 403

174

DEFINE attribute 103, 200, 203

DEFINE command 415, 416

rounding 528

DEFINE fields in Master Files 404

DEFINE FUNCTION

alphanumeric 137, 138

date display options 140

date storage 142

date-time 154, 156

dates 140, 147, 148, 153

calling in a Master File 216

decimal precision floating-point 119

defining dimensions 181–183

DEFINITION attribute 193, 194

delimiters 282–285

DESC attribute 193, 194

extended decimal precision floating-point 118

floating-point double-precision 116

floating-point single-precision 117

integer 115

descendant segments 76, 297

internal representation 324

FOCUS data sources 297

join linkage 356–358

numeric display options 121, 125

packed-decimal 120

538

display formats for fields 113, 114, 170, 173,

dynamic keyed multiple (DKM) segments 362,

174

363

rounding of numeric values 135

dynamic keyed unique (DKU) segments 362, 363

Index

text 169

display options 113, 114

date 140

numeric 121, 125

DKM (dynamic keyed multiple) segments 362,

363

DKU (dynamic keyed unique) segments 362, 363

DMS data sources 34

documenting data sources 28, 38

documenting fields 193, 194

double-precision fields 521

rounding 521

double-precision floating-point data type 116

rounding of values 135

DTSTANDARD parameter 155

DUMMY root segments 264, 265, 267

duplicate field names 106–108

CHECK FILE command and 395, 398

E

edit options 113, 114

date 140

numeric 121, 125

EDUCFILE data source 476, 477

EMPDATA data source 485

EMPLOYEE data source 471, 473, 474

ENCRYPT command 415, 416, 436

ENCRYPT parameter 436, 437

encrypting procedures 438

in Master Files 436

Enscribe data sources 34

entry-sequenced data sources (ESDS) 231

error files 517

error messages 398, 517

ESDS (entry-sequenced data sources) 231

extended currency symbols 129, 131

DUPLICATE option to CHECK FILE command 395,

formats 131

398

DYNAM ALLOC command 39

DYNAM ALLOCATE command 22, 24, 25

DYNAM commands 26

DYNAM FREE LONGNAME command 24

dynamic join relationships 349, 362, 363

extended decimal precision floating-point data

type 118

external index 455, 457

concatenated data sources 458

defined fields 459

REBUILD command 455

static relationships compared to 362, 367

extract files 401

CHECK FILE command and 395, 401–404

Describing Data With TIBCO WebFOCUS® Language

 539

Index

extract files 401

date data types and 153

F

F data type 117

rounding of values 135

FDEFCENT attribute 31

CHECK FILE command and 395, 401, 403

FDS (FOCUS Database Server) 39, 42

field aliases 112

FIELD attribute 104, 105

field formats 113, 114, 170, 173, 174, 524

alphanumeric 137, 138

date display options 140

date storage 142

date-time 154, 156

dates 140, 147, 148, 153

decimal precision floating-point 119

extended decimal precision floating-point 118

floating-point double-precision 116

floating-point single-precision 117

integer 115

numeric display options 121, 125

packed-decimal 120

redefining 524, 525

rounding of numeric values 135

text 169

field names 104–108

checking for duplicates with CHECK FILE

command 395, 398

540

field names 104–108

qualified 106–108

FIELD option to RESTRICT attribute 417

field values 422, 423

restricting access to 422, 423

validating 186, 188–191

FIELDNAME attribute 103–106

fields 18, 103

describing 20, 103

documenting 193, 194

naming 104–108

redefining 254–256

repeating 232, 244, 245, 271, 272

restricting access to 420, 422

FIELDTYPE attribute 321, 323

file allocations in Master Files 39–41

FILE attribute 32

file declarations 31

file descriptions 17, 18

applications and 19

creating 21

field declarations 20, 103

field relationships 20, 65–68

file declarations 20, 31

Master Files 19, 26

FILEDEF command 39

FILENAME attribute 32

FILESUFFIX attribute 32, 33

filler fields 69, 232

filter in a Master File 208

Index

filters 434

FOCUS data sources 33, 293

FINANCE data source 483, 484

allocating in Master Files 39, 41, 42

financial reports 181

FIND function 39

DATASET attribute and 39

FIND option to ACCEPT attribute 320

fixed-format data sources 33, 232

allocating in Master Files 43, 44

changing 299

data type representation 324

designing 297, 298

FIND option 320

FORMAT attribute 324

INDEX attribute 321, 323

generalized record types 267–269

internal storage lengths 324

multiple record types 257, 258, 260,

270–272, 274, 275

joining 298

key fields 302

nested repeating fields 248, 249

LOCATION attribute 304–307

order of repeating fields 253, 254

parallel repeating fields 247, 249

MISSING attribute 324

partitioning 294, 324–326

position of repeating fields 251, 252

rebuilding 328

positionally related records 260, 261

rebuilding (Maintain) 444

repeating fields 245–247, 271, 272

segment relationships 297, 304

unrelated records 264

segment sort order 302, 303

floating-point double-precision data type 116, 135

segments 299

floating-point fields 519

rounding 519, 521

SEGTYPE attribute 300, 302, 303

sorting 328

floating-point single-precision data type 117, 135

support for 294

FML hierarchies 181

FOCUS Database Server (FDS) 39, 42

describing data 178

Master Files for 181

requirements 178

FOC2GIGDB parameter 294

FOCUS data sources 33, 293

ACCEPT attribute 320

allocating 328

FORMAT attribute 113, 114

formatting currency 129

free-format data sources 33, 232, 236, 237

repeating fields 244

FYRTHRESH attribute 31

CHECK FILE command and 395, 401, 403

Describing Data With TIBCO WebFOCUS® Language

 541

Index

G

generalized record types 267–269

GEOGRAPHIC_ROLE attribute 175

GGDEMOG data source 495

GGORDER data source 495

GGPRODS data source 495

GGSALES data source 495

GGSTORES data source 495

global variables 220

Gotham Grinds data sources 495

GROUP ELEMENTS 241, 317

group fields 241, 317

group keys 231, 238–241

H

H data type 154, 156

HELPMESSAGE attribute 103

CHECK FILE command and 404

hierarchical data structures 96, 178, 297

HOLD ALL option to CHECK FILE command 395,

401–403

HOLD files 171, 172, 409

and date-time data type 172

DBA security 409

HOLD option to CHECK FILE command 395,

401–403

HOLDSTAT files 409

DBA security 409

host data sources 350

host fields 352

542

host segments 352

I

I data type 115

rounding of values 135

IDCAMS utility 279, 281

identifying data sources 31

IDMS data sources 33

IDMS/DB data sources 33

IMAGE/SQL data sources 36

IMS data sources 33

INDEX attribute 321, 323

joining data sources 322

index buffers for VSAM data sources 278, 279

INDEX subcommand 453, 454

indexes 453

concatenated data sources 458

defined fields 459

external 455

INDEX subcommand 453

multi-dimensional 470

REBUILD EXTERNAL INDEX subcommand 455

REBUILD INDEX command 453

INFOAccess data sources 34

Information/Management data sources 34

Informix data sources 35

Ingres data sources 35

integer data type 115

rounding of values 135

integer fields 520

rounding 519, 520

internal representation 324

of data types 324

of dates 150

ISAM data sources 231

allocating in Master Files 45

describing 238

Index

JOIN command 349

dimensional 344

long field names and 106

Multi-Dimensional Index (MDI) 342, 343

JOIN_WHERE 364

join

conditional 364

joining data sources 71, 95, 349

generalized record types 267–269

ancestral segments in cross-referenced files

group keys 239–241

360

multiple record types 257, 258, 260,

descendant segments in cross-referenced

270–272

files 358

nested repeating fields 248

dynamic relationships 362, 367

order of repeating fields 253, 254

FOCUS 298

parallel repeating fields 247

from many host files 368, 371

position of repeating fields 251, 252

from many segments in single host file 369

positionally related records 260, 261

INDEX attribute 322

repeating fields 245–247, 271, 272

recursive relationships 91–93, 373

unrelated records 264

static relationships 350, 362, 367

ISO standard date-time notation 155

ITEMS data source 493, 494

K

J

key fields 68, 302

FOCUS data sources 302

JOBFILE data source 474, 475

key-sequenced data sources (KSDS) 231

JOBHIST data source;sample data sources

keyed multiple (KM) segments 350, 354, 355

JOBHIST 487

keyed through linkage (KL) segments 356–358,

JOBLIST data source;sample data sources

360, 362, 363

JOBLIST 487

JOIN command 349

data security 428–430, 433, 434

keyed through linkage unique (KLU) segments

356–358, 360, 362, 363

Describing Data With TIBCO WebFOCUS® Language

 543

Index

keyed unique (KU) segments 350, 352, 353

long field names 106–108

decoding values 354

alternate file views and 106

KL (keyed through linkage) segments 356–358,

CHECK FILE command and 106

360, 362, 363

indexed fields and 106

KLU (keyed through linkage unique) segments

temporary fields 107, 200

356–358, 360, 362, 363

long names 22

KM (keyed multiple) segments 350, 354, 355

LONGNAME option 22, 24–26

KSAM data sources 35

KSDS (key-sequenced data sources) 231

Master Files 22–26

member names 22

KU (keyed unique) segments 350, 352, 353

LONGNAME option 22, 24–26

decoding values 354

L

languages 194

leaf segments 76

LEDGER data source 482, 483

legacy dates 465

converting 465, 469

M

M data type 119

many-to-many segment relationships 86, 88

MAPFIELD alias 275, 277, 278

MAPVALUE fields 275, 277, 278

Master File attributes

JOIN_WHERE 364

DATE NEW subcommand 465–467

Master File Editor 21

linked segments 362

Master File global variables 220

literals for dates 142, 147, 148

Master Files 18, 19, 26, 178, 181, 405, 416,

LNGPREP utility 58

load procedures 471

locale-based display options 133

LOCATION attribute 304–307

location files 307

471

allocating files 39–41, 43, 44

applications and 19

Business Views of 383

calling a DEFINE FUNCTION in 216

LOCATOR data source;sample data sources

common errors 398

LOCATOR 488

logical views of segments 69, 70

long alphanumeric fields 138

creating 21

data sources 32, 33

declarations 27

544

Master Files 18, 19, 26, 178, 181, 405, 416,

MDI (Multi-Dimensional Index) 333, 346

Index

471

diagrams 399, 401

dimensions 181–183

documenting 28, 38

encrypting 436

error messages 398

file statistics 396

filters 208

defining on Windows 335

defining on z/OS 336

displaying warnings 348

encoding 345, 346

guidelines 337

joining 342–344

maintaining 338

partitioning 347

GROUP declaration 241, 317

querying 339, 340, 347

hierarchies in 178

REBUILD MDINDEX subcommand 470

improving readability 27, 28

retrieving output 345

joining data sources 71, 95, 349

specifying in Access File 333, 334

long names 22–26

multilingual descriptions 194

names of data sources 32

naming 21, 22

OLAP-enabling 181–183

security attributes 405

user access to 416

validating 29, 395–397

virtual fields 404

Y2K attributes 31, 103

MATCH command 415

using AUTOINDEX 340, 341

MDICARDWARN parameter 348

MDIENCODING parameter 345, 346

MDINDEX subcommand 470

MDIPROGRESS parameter 347

member names for long names 22

metadata

multilingual 58

Micronetics Standard MUMPS data sources 35

minimum referenced subtree 73

MISSING attribute 103, 176–178

MDI (Multi-Dimensional Index) 333, 346

ALLOWCVTERR parameter and 152

building 338

choosing dimensions 336

creating 336

creating in FOCEXEC 339

defining on UNIX 335

missing values 176–178, 285

MOVIES data source 493

multi-dimensional data sources 181–183

Multi-Dimensional Index (MDI) 333, 346, 470

building 338

Describing Data With TIBCO WebFOCUS® Language

 545

Index

Multi-Dimensional Index (MDI) 333, 346, 470

multiply occurring fields 232, 244–247, 271, 272,

choosing dimensions 336

274, 275

creating 336

creating in FOCEXEC 339

defining on UNIX 335

defining on Windows 335

defining on z/OS 336

displaying warnings 348

encoding 345, 346

guidelines 337

joining 342–344

maintaining 338

partitioning 347

querying 339, 340, 347

REBUILD MDINDEX subcommand 470

retrieving output 345

specifying in Access File 333, 334

using AUTOINDEX 340, 341

multi-path data structures 79

multilingual metadata 58, 194

usage notes 194

multiple join relationships 350

dynamic 362, 363

static 354, 355

multiple record types 257, 258, 260, 270–272,

274, 275

ORDER fields 253, 254

parallel 247, 249

POSITION attribute 251, 252

record length 256

MUMPS data sources 35

N

naming conventions 21

fields 104–106

Master Files 22

segments 68, 69

naming fields 107

National Language Support (NLS) 27

Native Interface data sources 35

nested repeating fields 248, 249

NETISAM Interface data sources 35

NLS 194

NLS (National Language Support) 27

NOMAD data sources 33

non-FOCUS data sources 254

CHECK FILE command 397

redefining fields 254, 255

non-relational data sources 69, 88

NonStop SQL data sources 35

multiply occurring fields 232, 244–247, 271, 272,

NOPRINT option to RESTRICT attribute 417

274, 275

MAPFIELD and MAPVALUE 275, 277, 278

nested 248, 249

Nucleus data sources 35

null values 176–178

546

Index

numbers 519

rounding 519

numeric data types 114

OpenIngres data sources 35

Oracle data sources 33

ORDER fields 253, 254

decimal precision floating-point 119

display options 121, 125

P

extended decimal precision floating-point 118

floating-point double-precision 116, 135

floating-point single-precision 117, 135

integer 115, 135

packed-decimal 120, 135

rounding of values 135

numeric display options 121, 125

numeric fields 519

O

P data type 120

rounding of values 135

PACE data sources 35

packed-decimal data type 120

rounding of values 135

packed-decimal fields 120

rounding 519, 522

page size for XFOCUS data source 294

parallel repeating fields 247, 249

PARENT attribute 72

OCCURS attribute 246, 247, 249

parent-child segment relationships 72, 74–77

ODBC data sources 35

partitioned data sources 327, 328

OLAP-enabling data sources 181–183

partitioning data sources 324, 325

one-to-many join relationships 350

passwords 405, 409–411

dynamic 362, 363

static 354, 355

changing 409

DBA 410

one-to-many segment relationships 83–86, 297

PERMPASS 410, 411

FOCUS data sources 297, 304

setting externally 438

one-to-one join relationships 350

paths in data sources 78–80, 297

decoding values 354

dynamic 362, 363

static 350, 352, 353

FOCUS data sources 297

PERMPASS SET parameter 410, 411

PERSINFO data source;sample data sources

one-to-one segment relationships 81–83, 297

PERSINFO 489

FOCUS data sources 297, 304

PICTURE option to CHECK FILE command 395,

Open M/SQL data sources 35

399, 401

Describing Data With TIBCO WebFOCUS® Language

 547

Index

pointer chains 460, 462

POSITION attribute 251, 252

REBUILD command 415, 416, 444, 458, 465

interactive use 444

positionally related records 260–262

MDINDEX subcommand 470

primary keys 68

procedures 438

decrypting 438

encrypting 438

security 438

Progress data sources 35

Q

QUALCHAR parameter 107

qualification character 107

qualified field names 106–108

levels of qualification 111

temporary fields 203

virtual fields 203

query commands

? MDI 339, 340

R

Rdb data sources 35

read-only access 414, 422

read/write access 414

REBUILD command 415, 416, 444, 458, 465

CHECK subcommand 460

DATE NEW subcommand 465–467

DBA passwords 444, 445

EXTERNAL INDEX subcommand 455, 458

INDEX subcommand 453, 454

548

message frequency 446

prerequisites 444, 445

REBUILD subcommand 447, 448

REORG subcommand 449, 450

SET REBUILDMSG command 446

TIMESTAMP subcommand 464

user access to 416

REBUILD EXTERNAL INDEX procedure 457, 459

concatenated data sources 458

REBUILD facility 454

REBUILD subcommand 447, 448

REBUILDMSG parameter 446

record length in sequential data sources 256

record types 232

generalized 267–269

multiple 257, 258, 260, 270–272, 274, 275

RECTYPE fields 257, 258, 260, 267–272

MAPFIELD and MAPVALUE 275, 277, 278

recursive join relationships 91–93, 373

Red Brick data sources 35

redefining field formats 524, 525

redefining fields in non-FOCUS data sources

254–256

referencing COMPUTE objects 204

REGION data source 484

relating segments 71, 80, 95

many-to-many relationships 86, 88

Index

relating segments 71, 80, 95

root segments 67, 76, 297

one-to-many relationships 83, 85, 86

describing 72

one-to-one relationships 81–83, 297

FOCUS data sources 297

parent-child relationships 72, 74–78

rounding numbers 519

recursive relationships 91–93, 373

COMPUTE fields 528

relational data sources 69, 83, 85

decimal floating-point fields 521

REMARKS attribute 38

decimal precision floating-point fields 521

REORG subcommand 449, 450

DEFINE fields 528

repeating fields 232, 244–247, 271, 272, 274,

double-precision fields 521

275

floating-point fields 519, 521

MAPFIELD and MAPVALUE 275, 277, 278

in calculations 524

nested 248, 249

ORDER fields 253, 254

parallel 247, 249

POSITION attribute 251, 252

record length 256

RESTRICT attribute 406, 415, 418, 420

keywords 415, 417

options 417

SAME option 417, 418

SEGMENT option 417, 418

VALUE option 417, 418

RESTRICT command 415

restricting access 420, 422

to data 405, 406, 415, 420

to fields 420, 422

to segments 420, 422

retrieval logic 73

retrieval paths and CHECK FILE command 395

RMS data sources 35

integer fields 519, 520

packed-decimal fields 519, 522

rounding of numeric values 135

S

SALES data source 477–479

SALHIST data source;sample data sources

SALHIST 490

SAME option to RESTRICT attribute 417

sample data sources 471

CAR 479, 481

Century Corp 501

COURSE 486, 487

EDUCFILE 476, 477

EMPLOYEE 471, 473, 474

FINANCE 483, 484

Gotham Grinds 495

ITEMS 493, 494

JOBFILE 474, 475

Describing Data With TIBCO WebFOCUS® Language

 549

Index

sample data sources 471

LEDGER 482, 483

MOVIES 493

REGION 484

SALES 477–479

TRAINING 485, 486

VIDEOTR2 494, 495

VideoTrk 490–492

SAVE files 171, 172

security 405–407

ACCESS 407, 420

access levels 414, 418, 420

DBA 405

segments 20, 65, 66, 304

data retrieval 73

encrypting 436, 437

excluding fields from 69, 70

instances 66

key fields 68, 302

naming 68, 69

parent-child relationships 72, 74–76, 78

relating 71, 80–86, 88, 91–93, 95

restricting access to 420, 422

sort order 68

storing 305

timestamping 311–313, 464

decrypting procedures 439

SEGNAME attribute 67–69

encrypting data segments 436, 437

VSAM and ISAM considerations 238

encrypting Master Files 436

encrypting procedures 438

FOCUSID routine 438

for FOCUS procedures 438

identifying users 409, 410

passwords 408, 413, 438

RESTRICT 406

SEGTYPE attribute 67, 68, 73

displaying 399, 401

FOCUS data sources 300, 302, 303

sequential data source considerations 238

VSAM considerations 238

SEGTYPE U and RECTYPE fields 258

separators for dates 145

storing DBA information centrally 428–430

sequential data sources 33, 231, 232, 235, 236,

SEG_TITLE_PREFIX 98

SEGMENT attribute 67–69

segment declarations 68

SEGMENT option to RESTRICT attribute 417

segments 20, 65, 66, 304

chains 67

data paths 78–80

550

282, 283, 285

allocating in Master Files 39–41, 43, 44

describing 238

fixed-format 232

free-format 236, 237

generalized record types 267–269

Index

sequential data sources 33, 231, 232, 235, 236,

SET parameters 104, 298, 409

282, 283, 285

multiple record types 257, 258, 260,

270–272, 274, 275

PASS 409, 410, 413

PERMPASS 410, 411

QUALCHAR 107

multiply occurring fields 232, 244–247, 256,

REBUILDMSG 446

271, 272, 274, 275

nested repeating fields 248, 249

USER 409, 410, 413

XFOCUSBINS 295

order of repeating fields 253, 254

setting a permanent DBA password 410

parallel repeating fields 247, 249

setting passwords externally 438

position of repeating fields 251, 252

single-path data structures 78

positionally related records 260, 261

single-precision floating-point data type 117

record length 256

rounding of numeric values 135

repeating fields 232, 244–247, 271, 272,

smart dates 142

274, 275

specifying an Access File in a Master File 325,

unrelated records 264, 265, 267

326

SET parameters 104, 298, 409

specifying multiple languages 194

ACCBLN 188

ACCEPTBLANK 188

ALLOWCVTERR 152

AUTOINDEX 341

AUTOPATH 298

DATEDISPLAY 150

DBACSENSITIV 412

DBAJOIN 428

DTSTANDARD 155

SQL Server data sources 36

SQL StorHouse data sources 36

SQL Translator and long field names 106

SQL/DS data sources 33

static join relationships 349, 350, 354

decoding values 354

dynamic relationships compared to 362, 367

multiple 354, 355

unique 350, 352, 353

FIELDNAME 103, 104, 106

storing date type data 142

FOC2GIGDB 294

MDICARDWARN 348

MDIENCODING 345, 346

MDIPROGRESS 347

structure diagrams 471

SUFFIX attribute 32, 33

using with XFOCUS data source 295

VSAM and ISAM 238

Describing Data With TIBCO WebFOCUS® Language

 551

Index

SUFFIX DFIX 282, 285

SUFFIX values 33

SUFFIX=COM attribute 235

SUFFIX=COMT attribute 235

SUFFIX=TAB attribute 236

SUFFIX=TABT attribute 236

Sybase data sources 36

token-delimited data sources 232, 282–285

TRAINING data source 485, 486

trans_file attribute 58

translation of dates 146

TSOALLOC command 39

TurboIMAGE data sources 36

TX data type 169

T

U

tab-delimited data sources 232, 236

Unify data sources 36

TABLE command 416

TABLEF command 462

unique join relationships 350

decoding values 354

TAG attribute and CHECK FILE command 404

dynamic 362, 363

temporary fields 200

creating 200, 203

in Master Files 404

static 350, 352, 353

uniVerse data sources 36

unrelated records 264, 265, 267

long field names and 106, 200

update access 414

qualified field names 203

USAGE attribute 103, 113, 114

Teradata data sources 33

text data type 169

long field names and 106

text fields 306

USAGE format 173, 282

USE command 39

USER attribute 409–411

user exits for data access 32

LOCATION segments and files for 307

user identification 406

storing 306

time stamps 311, 313, 464

REBUILD TIMESTAMP subcommand 464

timestamp data type 154, 156

TIMESTAMP subcommand 464

TITLE attribute 103, 191, 192

CHECK FILE command and 404

552

V

validating field values 186, 188–191

validating Master Files 29, 395–397

VALUE option to RESTRICT attribute 417, 422,

423

values 135, 422

VSAM data sources 33, 231

restricting user access to 422

positionally related records 260–262

Index

rounding off 135

variables 217

in Master File DEFINEs 217

in Master Files 217

VIDEOTR2 data source 494, 495

VideoTrk data source 490–492

views 383

virtual fields 200, 217

CHECK FILE command and 404

creating 200, 203

in Master Files 404

long field names and 200

qualified field names 203

VSAM data sources 33, 231

allocating in Master Files 45, 46

alternate indexes 279, 281

data buffers 278, 279

describing 238

generalized record types 267–269

group keys 239–241

IDCAMS utility 279, 281

index buffers 278, 279

multiple record types 257, 258, 260,

270–272, 274, 275

nested repeating fields 248, 249

order of repeating fields 253, 254

parallel repeating fields 247, 249

position of repeating fields 251, 252

repeating fields 245–247, 271, 272, 274,

275

unrelated records 264, 265, 267

W

WHERE-based join

Master File syntax 364

WITHIN attribute 181–183

write-only access 414

X

X data type 118

XFOCUS data source 294

controlling buffer pages 295

creating 296

partitioning 294

specifying 295

SUFFIX 295

support for 294

usage notes 296

XFOCUSBINS parameter 295

Y

Y2K attributes in Master Files 31, 103

CHECK FILE command and 401, 403

Year 2000 attributes in Master Files 31, 103

CHECK FILE command and 401, 403

Describing Data With TIBCO WebFOCUS® Language

 553

Index

YRTHRESH attribute 31, 103

CHECK FILE command and 395, 401, 403

554


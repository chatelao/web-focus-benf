Chapter13

Handling Records With Missing Field
Values

Missing data is defined as data that is missing from a report because it is not relevant or
does not exist in the data source. Report output that involves averaging and counting
calculations or the display of parent segment instances may be affected by missing data.
Data can be missing from reports and calculations for the following reasons:

Data is not relevant to a particular row and column in a report. See Irrelevant Report
Data on page 1035.

A field in a segment instance does not have a data value. See Missing Field Values on
page 1036.

A parent segment instance does not have child instances (missing segment
instances). See Handling a Missing Segment Instance on page 1056.

Note: To run the examples in this topic, you must run the stored procedures EMPMISS
and SALEMISS to add missing data to the EMPLOYEE and SALES data sources,
respectively.

In this chapter:

Irrelevant Report Data

Missing Field Values

Handling a Missing Segment Instance

Setting the NODATA Character String

Irrelevant Report Data

Data can be missing from a report row or column because it is not relevant. The missing or
inapplicable value is indicated by the NODATA default character, a period (.).

Tip: You may specify a more meaningful NODATA value by issuing the SET NODATA command
(see Setting the NODATA Character String on page 1066).

Creating Reports With TIBCO® WebFOCUS Language

 1035

Missing Field Values

Example:

Irrelevant Report Data

The following request shows how the default NODATA character displays missing data in a
report.

TABLE FILE EMPLOYEE
PRINT CURR_SAL
BY LAST_NAME
BY FIRST_NAME
ACROSS DEPARTMENT
END

The output is:

The salary for an employee working in the production department displays in the PRODUCTION
column. The salary for an employee working in the MIS department displays in the MIS column.
The corresponding value in the PRODUCTION or MIS column, respectively, is missing because
the salary displays only under the department where the person is employed.

Missing Field Values

Missing values within segment instances occur when the instances exist, but some of the
fields lack values.

When fields in instances lack values, numeric fields are assigned the value 0, and
alphanumeric fields, the value blank. These default values appear in reports and are used in
all calculations performed by the SUM and COUNT display commands, DEFINE commands, and
prefix operators such as MAX. and AVE.

1036

13. Handling Records With Missing Field Values

To prevent the use of these default values in calculations (which might then give erroneous
results), you can add the MISSING attribute to the field declaration in the Master File, for
either a real or a virtual field. When the MISSING attribute is set to ON, the missing values are
marked with a special internal code to distinguish them from blanks or zeros, and the missing
values are ignored in calculations. In reports, the internal code is represented by the SET
NODATA value, a period (.), by default. See Setting the NODATA Character String on page
1066.

For example, missing data for a field in a segment instance may occur when the data values
are unknown, as in the following scenario. Suppose that the employees recorded in the
EMPLOYEE data source are due for a pay raise by a certain date, but the amount of the raise
has not yet been determined. The company enters the date for each employee into the data
source without the salary amounts; the salaries will be entered later. Each date is an individual
instance in the salary history segment, but the new salary for each date instance is missing.
Suppose further that a report request averages the SALARY field (SUM AVE.SALARY). The
accuracy of the resulting average depends on whether the missing values for the SALARY field
are treated as zeros (MISSING=OFF), or as internal codes (MISSING=ON).

Note: When all of the field values used in the calculation of a numeric summary value, such as
a subtotal, are missing, the summary value is assigned the missing data value, not the value
zero (0). This includes summary values produced by the operators ST. and CT. used in a
subfooting.

Example:

Counting With Missing Values

Suppose the CURR_SAL field appears in 12 segment instances. In three of those instances,
the field was given no value. Nevertheless, the display command

COUNT CURR_SAL

counts 12 occurrences of the CURR_SAL field. This occurs because the MISSING attribute is
OFF by default, so the missing values are included in the count. If you wanted to exclude the
missing data from the count, you could set MISSING ON.

Example:

Averaging With Missing Values

Suppose you have the following records of data for a field:

.
.
1
3

Creating Reports With TIBCO® WebFOCUS Language

 1037

Missing Field Values

The numeric values in the first two records are missing (indicated by the periods). The last two
records have values of 1 and 3. If you average these fields without the MISSING attribute
(MISSING OFF), the value 0 is supplied for the two records that are missing values. Thus, the
average of the records is (0+0+1+3)/4, or 1. If you use the MISSING ON attribute, the two
missing values are ignored, calculating the average as (1+3)/2, or 2.

MISSING Attribute in the Master File

In some applications, the default values (blanks and zeros) may represent valid data rather
than the absence of information. However, if this is not the case, you can include the MISSING
attribute after the field format in the Master File declaration for the field with the missing
values. The MISSING attribute can be used with an actual field in the data source, or a virtual
field that you are defining in the Master File.

For example, the following field declaration specifies the MISSING attribute for the RETURNS
field:

FIELDNAME=RETURNS, ALIAS=RTN, FORMAT=I4, MISSING=ON,$

The next declaration specifies the MISSING attribute for a virtual field called PROFIT:

DEFINE PROFIT/D7 MISSING ON NEEDS SOME DATA = RETAIL_COST - DEALER_COST;$

To ensure that missing values are handled properly for virtual fields, you can set the MISSING
attribute ON for the virtual field in the DEFINE command, and specify whether you want to apply
the calculation if some or all values are missing. For related information on the SOME and ALL
phrases, see How to Specify Missing Values in a DEFINE or COMPUTE Command on page
1040.

When the MISSING attribute is set to ON in a field declaration, the field containing no data is
marked with a special internal code, rather than with blanks or zeros. During report generation,
the SUM and COUNT commands and all prefix operators (for example, AVE., MAX., MIN.)
exclude the missing data in their computations. For related information about the MISSING
attribute and field declarations, see the Describing Data With WebFOCUS Language manual.

Note:

You may add MISSING field attributes to the Master File at any time. However, MISSING
attributes only affect data entered into the data source after the attributes were added.

Key fields are needed to identify a record. Therefore, key fields should not be identified as
missing.

1038

13. Handling Records With Missing Field Values

Example:

Handling Missing Values With the MISSING Attribute

This example illustrates the difference between a field with MISSING ON and one without. In it
a virtual field, X_RETURNS, without the MISSING attribute, is set to equal a real field,
RETURNS, with the MISSING attribute declared in the Master File. When the field with the
MISSING attribute (RETURNS) is missing a value, the corresponding value of X_RETURNS is 0,
since a data source field that is missing a value is evaluated as 0 (or blank) for the purpose of
computation (see MISSING Attribute in a DEFINE or COMPUTE Command on page 1039).

The following request defines the virtual field:

DEFINE FILE SALES
X_RETURNS/I4 = RETURNS;
END

Now issue the following report request:

TABLE FILE SALES
SUM CNT.X_RETURNS CNT.RETURNS AVE.X_RETURNS AVE.RETURNS
END

Remember that the field X_RETURNS has the same value as RETURNS except when RETURNS
is missing a value, in which case, the X_RETURNS value is 0.

The output is:

The count for the RETURNS field is lower than the count for X_RETURNS and the average for
RETURNS is higher than for X_RETURNS because the missing values in RETURNS are not part
of the calculations.

MISSING Attribute in a DEFINE or COMPUTE Command

You can set the MISSING attribute ON in a DEFINE or COMPUTE command to enable a
temporary field with missing values to be interpreted and represented correctly in reports.

An expression used to derive the values of the temporary field can contain real fields that have
missing values. However, when used to derive the value of a temporary field, a data source
field that is missing a value is evaluated as 0 or blank for computational purposes, even if the
MISSING attribute has been set to ON for that field in the Master File.

Creating Reports With TIBCO® WebFOCUS Language

 1039

Missing Field Values

To ensure that missing values are handled properly for temporary fields, you can set the
MISSING attribute ON for the virtual field in the DEFINE or COMPUTE command, and specify
whether you want to apply the calculation if some or all values are missing. See How to Specify
Missing Values in a DEFINE or COMPUTE Command on page 1040.

Syntax:

How to Specify Missing Values in a DEFINE or COMPUTE Command

field[/format] MISSING {ON|OFF} [NEEDS] {SOME|ALL} [DATA] = expression;

where:

field

Is the name of the virtual field created by the DEFINE command.

/format

Is the format of the virtual field. The default is D12.2.

MISSING

ON enables the value of the temporary field to be interpreted as missing (that is,
distinguished by the special internal code from an intentionally entered zero or blank), and
represented by the NODATA character in reports.

OFF treats missing values for numeric fields as zeros, and missing values for
alphanumeric fields as blanks. This is the default value.

NEEDS

Is optional. It helps to clarify the meaning of the command.

SOME

Indicates that if at least one field in the expression has a value, the temporary field has a
value (the missing values of the field are evaluated as 0 or blank in the calculation). If all
of the fields in the expression are missing values, the temporary field is missing its value.
SOME is the default value.

ALL

Indicates that if all the fields in the expression have values, the temporary field has a
value. If at least one field in the expression has a missing value, the temporary field also
has a missing value.

DATA

Is optional. It helps to clarify the meaning of the command.

1040

13. Handling Records With Missing Field Values

expression

Is a valid expression from which the temporary field derives its value.

Note: You can also use the SET MISS_ON command to set a default value for MISSING ON in
DEFINE and COMPUTE.

Example:

Handling Missing Values for a Virtual Field With MISSING OFF

The following request illustrates the use of two fields, RETURNS and DAMAGED, to define the
NO_SALE field. Both the RETURNS and DAMAGED fields have the MISSING attribute set to ON
in the SALES Master File, yet whenever one of these fields is missing a value, that field is
evaluated as 0.

DEFINE FILE SALES
NO_SALE/I4 = RETURNS + DAMAGED;
END
TABLE FILE SALES
PRINT RETURNS AND DAMAGED AND NO_SALE
BY CITY BY DATE BY PROD_CODE
END

The output is:

CITY             DATE   PROD_CODE  RETURNS  DAMAGED  NO_SALE
----             ----   ---------  -------  -------  -------
NEW YORK         10/17  B10              2        3        5
                        B17              2        1        3
                        B20              0        1        1
                        C13              .        6        6
                        C14              4        .        4
                        C17              0        0        0
                        D12              3        2        5
                        E1               4        7       11
                        E2               .        .        0
                        E3               4        2        6
NEWARK           10/18  B10              1        1        2
                 10/19  B12              1        0        1
STAMFORD         12/12  B10             10        6       16
                        B12              3        3        6
                        B17              2        1        3
                        C13              3        0        3
                        C7               5        4        9
                        D12              0        0        0
                        E2               9        4       13
                        E3               8        9       17
UNIONDALE        10/18  B20              1        1        2
                        C7               0        0        0

Creating Reports With TIBCO® WebFOCUS Language

 1041

Missing Field Values

Notice that the products C13, C14, and E2 in the New York section all show missing values for
either RETURNS or DAMAGED, because the MISSING ON attribute has been set in the Master
File. However, the calculation that determines the value of NO_SALE interprets these missing
values as zeros, because MISSING ON has not been set for the virtual field.

Example:

Handling Missing Values for Virtual Fields With SOME and ALL

The following request illustrates how to use the DEFINE command with the MISSING attribute
to specify that if either some or all of the field values referenced in a DEFINE command are
missing, the virtual field should also be missing its value.

The SOMEDATA field contains a value if either the RETURNS or DAMAGED field contains a
value. Otherwise, SOMEDATA is missing its value. The ALLDATA field contains a value only if
both the RETURNS and DAMAGED fields contain values. Otherwise, ALLDATA is missing its
value.

DEFINE FILE SALES
SOMEDATA/I5 MISSING ON NEEDS SOME=RETURNS + DAMAGED;
ALLDATA/I5 MISSING ON NEEDS ALL=RETURNS + DAMAGED;
END

TABLE FILE SALES
PRINT RETURNS AND DAMAGED SOMEDATA ALLDATA
BY CITY BY DATE BY PROD_CODE
END

1042

13. Handling Records With Missing Field Values

The output is:

Syntax:

How to Setting MISSING ON Behavior for DEFINE and COMPUTE

When a virtual field or calculated value can have missing values, you can specify whether all or
some of the field values used in the expression that creates the DEFINE or COMPUTE field
must be missing to make the result field missing. If you do not specify ALL or SOME for a
DEFINE or COMPUTE with MISSING ON, the default value is SOME.

The SET parameter MISS_ON enables you to specify whether SOME or ALL should be used for
MISSING ON in a DEFINE or COMPUTE that does not specify which to use.

SET MISS_ON = {SOME|ALL}

where:

SOME

Indicates that if at least one field in the expression has a value, the temporary field has a
value (the missing values of the field are evaluated as 0 or blank in the calculation). If all
of the fields in the expression are missing values, the temporary field has a missing value.
SOME is the default value.

Creating Reports With TIBCO® WebFOCUS Language

 1043

Missing Field Values

ALL

Indicates that if all the fields in the expression have values, the temporary field has a
value. If at least one field in the expression has a missing value, the temporary field has a
missing value.

Example:

Setting a Default Value for MISSING ON in DEFINE and COMPUTE

The following request creates three virtual fields that all have MISSING ON. Field AAA has all
missing values. Field BBB is missing only when the category is Gifts and has the value 100
otherwise. Field CCC is the sum of AAA and BBB.

SET MISS_ON = SOME
DEFINE FILE GGSALES
AAA/D20 MISSING ON = MISSING;
BBB/D20 MISSING ON = IF CATEGORY EQ 'Gifts' THEN MISSING ELSE 100;
CCC/D20 MISSING ON = AAA + BBB;
END
TABLE FILE GGSALES
SUM
AAA
BBB
CCC
BY CATEGORY
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
END

Running the request with SET MISS_ON=SOME (the default) shows that CCC has a value
unless both AAA and BBB are missing.

1044

13. Handling Records With Missing Field Values

Changing SET MISS_ON to ALL, produces the following output. CCC is assigned a missing
value because one of the fields used to calculate it is always missing.

Testing for Missing Values in IF-THEN-ELSE Expressions

In order to optimize the efficiency of IF-THEN-ELSE expression processing, the entire
expression may not be parsed when the result (true or false) can be determined without
parsing the entire expression. For example, consider the following IF-THEN-ELSE expression.

COMPUTE CCC/D9.1 MISSING ON = IF AAA EQ 0 OR BBB EQ 0 THEN 0 ELSE AAA / BBB
* 100;

Note:

AAA is a missable field (MISSING ON) that is set to MISSING.

BBB is a field with MISSING ON that is set to 100, so it has a value that is not MISSING.

For evaluation in expressions, a field that is MISSING is treated as zero (0).

CCC is a numeric field that has MISSING ON computed using an IF-THEN-ELSE expression. The
IF clause contains two tests connected by the OR operator. If either one of these two tests is
TRUE, the value in the THEN clause will be passed to the final MISSING check. If neither is
TRUE, the value in the ELSE clause will be passed to the MISSING check.

In this case, AAA EQ 0 is true (since MISSING is treated as 0 when used in a comparison). So
the THEN value, which is zero, is accepted. Since CCC has MISSING ON, which defaults to
NEEDS SOME values, at least one data value evaluated in the IF clause must not be missing.

Only AAA was evaluated to get the TRUE condition. BBB was not tested and, therefore, is not
included in the fields that are checked for missing values. Since AAA is MISSING, CCC (since it
NEEDS SOME and does not have any) must be set to MISSING. Note that this processing
represents a change from the processing in prior releases and, while it increases processing
efficiency, it may produce different results.

Since the test for a value and the test for existence or presence (MISSING) are not the same,
the best practice is always to use the test that is appropriate. When testing for MISSING,
using IS MISSING is preferred to using EQ 0, as it is more direct and does not result in the
same behavior change from previous releases.

Creating Reports With TIBCO® WebFOCUS Language

 1045

Missing Field Values

Consider the following request. CCC uses EQ 0 in the IF-THEN-ELSE test, and DDD uses IS
MISSING.

DEFINE FILE GGSALES
AAA/D20 MISSING ON = MISSING;
BBB/D20 MISSING ON = 100;
END
TABLE FILE GGSALES
SUM
  AAA
  BBB
  COMPUTE CCC/D9.1 MISSING ON = IF AAA EQ 0 OR BBB EQ 0 THEN 0 ELSE AAA /
BBB * 100;
  COMPUTE DDD/D9.1 MISSING ON = IF AAA IS MISSING OR BBB IS MISSING THEN 0
ELSE AAA / BBB * 100;
BY  CATEGORY
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
END

The output is shown in the following image. While CCC evaluates to a missing value, DDD
evaluates to 0 because the both AAA and BBB were evaluated to get the TRUE condition and
BBB is not missing, satisfying the NEEDS SOME VALUES definition for DDD.

Reference: Using SET MISSINGTEST With IF-THEN-ELSE Expressions

In prior releases, by default, when an IF-THEN-ELSE expression was used to calculate a result
and the IF expression evaluated to zero (for numeric expressions) or blank (for alphanumeric
expressions), the left hand side was checked to see if it had MISSING ON. If it did, and only
some values were needed (NEEDS SOME), the result of the IF expression was MISSING, not
true or false. The outcome returned was also MISSING, not the result of evaluating the THEN
or ELSE expression. The SET MISSINGTEST = NEW command eliminates the missing test for
the IF expression so that either the THEN expression or the ELSE expression will be evaluated
and returned as the result. This is the default behavior.

The syntax is:

SET MISSINGTEST = {NEW|OLD|SPECIAL}

1046

13. Handling Records With Missing Field Values

where:

NEW

Excludes the IF expression from the missing values evaluation so that the IF expression
results in either true or false, not MISSING. If it evaluates to true, the THEN expression is
used to calculate the result. If it evaluates to false, the ELSE expression is used to
calculate the result. This is the default value.

OLD

Includes the IF expression in the missing values evaluation. If the IF expression evaluates
to MISSING and the missing field only needs some missing values, the result is also
MISSING.

SPECIAL

Is required for passing parameters to RStat.

Example:

Using SET MISSINGTEST With IF-THEN-ELSE Expressions

The following request defines a field named MISS_FIELD that contains a missing value for the
country name Austria. In the TABLE request there are two calculated values, CALC1 and CALC2
that test this field in IF-THEN-ELSE expressions. Both of these fields have MISSING ON and
need only some missing values to be missing:

SET MISSINGTEST = OLD
DEFINE FILE WF_RETAIL_LITE
MISS_FIELD/A10 MISSING ON = IF COUNTRY_NAME NE 'Austria' THEN 'DATAEXISTS'
ELSE MISSING;
END

TABLE FILE WF_RETAIL_LITE
SUM COGS_US MISS_FIELD
COMPUTE CALC1/A7 MISSING ON = IF ((MISS_FIELD EQ '') OR (MISS_FIELD EQ
MISSING)) THEN 'THEN' ELSE 'ELSE';
COMPUTE CALC2/A7 MISSING ON = IF ((MISS_FIELD EQ MISSING) OR (MISS_FIELD EQ
'')) THEN 'THEN' ELSE 'ELSE';
BY COUNTRY_NAME
WHERE BUSINESS_REGION EQ 'EMEA'
WHERE COUNTRY_NAME LT 'E'
ON TABLE SET NODATA 'MISSING'
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1047


Missing Field Values

Running the request with MISSINGTEST=OLD produces the output shown in the following
image:

Note that for Austria, MISS_FIELD is MISSING.

In CALC1, the expression MISS_FIELD EQ ' ' is evaluated to true. MISS_FIELD IS MISSING
is not evaluated at all because evaluation stops when it can be determined that the result
of the expression is true. However, since the expression compared the field to blank, it is
checked to see if the result field supports missing values. Since it does, the final result is
MISSING.

In CALC2, the expression MISS_FIELD EQ MISSING is true. MISS_FIELD EQ ' ' is not
evaluated at all because evaluation stops when it can be determined that the result of the
expression is true. No missing check is needed, so the result of the IF expression is TRUE,
and the THEN expression is evaluated and returned as the result.

Changing the SET command to SET MISSINGTEST=NEW and rerunning the request produces
the output shown in the following image. The IF expressions in CALC1 and CALC2 both
evaluate to true because neither expression is checked to see if the result field supports
missing, so the THEN expression is evaluated and returned as the result in both cases.

Testing for a Segment With a Missing Field Value

You can specify WHERE criteria to identify segment instances with missing field values.

1048

13. Handling Records With Missing Field Values

You cannot use these tests to identify missing instances. See Handling a Missing Segment
Instance on page 1056.

Syntax:

How to Test for a Segment With a Missing Field Value

To test for a segment with missing field values, the syntax is:

WHERE field {IS|EQ} MISSING

To test for the presence of field values, the syntax is:

WHERE field {NE|IS-NOT} MISSING

A WHERE criterion that tests a numeric field for 0 or an alphanumeric field for blanks also
retrieves instances for which the field has a missing value.

Example:

Testing for a Missing Field Value

The following request illustrates the use of MISSING to display grocery items (by code) for
which the number of packages returned by customers is missing.

TABLE FILE SALES
PRINT RETURNS
BY CITY BY DATE BY PROD_CODE
WHERE RETURNS IS MISSING
END

The output is:

CITY             DATE   PROD_CODE  RETURNS
----             ----   ---------  -------
NEW YORK         10/17  C13              .
                        E2               .

Creating Reports With TIBCO® WebFOCUS Language

 1049

Missing Field Values

Example:

Testing for an Existing Field Value

The following request illustrates the use of MISSING to display only those grocery items for
which the number of packages returned by customers is not missing.

TABLE FILE SALES
PRINT RETURNS
BY CITY BY DATE BY PROD_CODE
WHERE RETURNS IS-NOT MISSING
END

The output is:

Example:

Testing for a Blank or Zero

The following request displays grocery items that either were never returned or for which the
number of returned packages was never recorded:

TABLE FILE SALES
PRINT RETURNS
BY CITY BY DATE BY PROD_CODE
WHERE RETURNS EQ 0
END

1050

13. Handling Records With Missing Field Values

The output is:

Example:

Excluding Missing Values From a Test

To display only those items that have not been returned by customers, you need two WHERE
criteria. The first to restrict the number of returns to 0, the other to exclude missing values, as
in the following request.

TABLE FILE SALES
PRINT RETURNS
BY CITY BY DATE BY PROD_CODE
WHERE RETURNS EQ 0
WHERE RETURNS IS-NOT MISSING
END

The output is:

Preserving Missing Data Values in an Output File

The ability to distinguish between missing data and default values (blanks and zeros) in fields
can be carried over into output files. If the retrieved and processed information displayed the
NODATA string in a report, by default the NODATA string can be stored in the output file. Using
the SET HNODATA command, you can change the NODATA value used for alphanumeric output
files. You can also use the SET HOLDMISS command to store the missing values rather than
the NODATA character in an output file. For related information, see Saving and Reusing Your
Report Output on page 471.

Creating Reports With TIBCO® WebFOCUS Language

 1051

Missing Field Values

Syntax:

How to Distinguish Missing Data in an Extract File

ON TABLE {HOLD|SAVE|SAVB} MISSING {ON|OFF}

where:

HOLD

Creates an extract file for use in subsequent reports. The default for MISSING is ON.

SAVE

Creates a text extract file for use in other programs. The default for MISSING is OFF.

SAVB

Creates a binary extract file for use in other programs. The default for MISSING is OFF.

HOLD files can be created with both the MISSING and FORMAT ALPHA options, specified in any
order. For example:

ON TABLE HOLD FORMAT ALPHA MISSING OFF
ON TABLE HOLD MISSING OFF FORMAT ALPHA

Example:

Incorporating MISSING Values in an Extract File

The following request specifies MISSING ON in the HOLD phrase:

TABLE FILE SALES
SUM RETURNS AND HOLD FORMAT ALPHA MISSING ON
BY CITY BY DATE BY PROD_CODE
END

The MISSING=ON attribute for the RETURNS field is propagated to the HOLD Master File. In
addition, the missing data symbols are propagated to the HOLD file for the missing field
values:

FILENAME=HOLD    , SUFFIX=FIX     , $
  SEGMENT=HOLD, SEGTYPE=S3, $
    FIELDNAME=CITY, ALIAS=E01, USAGE=A15, ACTUAL=A15, $
    FIELDNAME=DATE, ALIAS=E02, USAGE=A4MD, ACTUAL=A04, $
    FIELDNAME=PROD_CODE, ALIAS=E03, USAGE=A3, ACTUAL=A03, $
    FIELDNAME=RETURNS, ALIAS=E04, USAGE=I3, ACTUAL=A03,
      MISSING=ON, $

With MISSING OFF in the HOLD phrase, the MISSING=ON attribute is not propagated to the
HOLD Master File and the missing data symbols are replaced with default values.

1052

13. Handling Records With Missing Field Values

Syntax:

How to Store Missing Data in HOLD Files

SET HOLDMISS={ON|OFF}
ON TABLE SET HOLDMISS {ON|OFF}

where:

ON

Allows you to store missing data in a HOLD file. When TABLE generates a default value for
data not found, it generates missing values.

OFF

Does not allow you to store missing data in a HOLD file. OFF is the default value.

Reference: Usage Notes for Holding Missing Values

Setting HOLDMISS ON adds the MISSING=ON attribute to every field in the extract file.

Data is not found if:

ALL is set to ON.

The request is multi-path.

An ACROSS statement has been issued.

Example:

Holding Missing Values Using HOLDMISS

SET HOLDMISS=ON
TABLE FILE MOVIES
 SUM WHOLESALEPR
BY CATEGORY ACROSS RATING
 ON TABLE HOLD AS HLDM
END
TABLE FILE HLDM
 PRINT *
 END

Creating Reports With TIBCO® WebFOCUS Language

 1053

Missing Field Values

The output is:

CATEGORY  WHOLESALEPR  WHOLESALEPR  WHOLESALEPR  WHOLESALEPR  WHOLESALEPR
--------  -----------  -----------  -----------  -----------  -----------
ACTION              .            .        20.98            .        34.48
CHILDREN        54.49        51.38            .            .            .
CLASSIC         40.99       160.80            .            .            .
COMEDY              .            .        46.70        30.00        13.75
DRAMA               .            .            .            .        10.00
FOREIGN         13.25            .        62.00            .        70.99
MUSICALS        15.00            .        13.99         9.99        13.99
MYSTERY             .         9.00        18.00         9.00        80.97
SCI/FI              .            .            .        35.99        43.53
TRAIN/EX            .
60.98            .            .             .

Propagating Missing Values to Reformatted Fields in a Request

When a field is reformatted in a request (for example, SUM field/format), an internal COMPUTE
field is created to contain the reformatted field value and display on the report output. If the
original field has a missing value, that missing value can be propagated to the internal field by
setting the COMPMISS parameter ON. If the missing value is not propagated to the internal
field, it displays a zero (if it is numeric) or a blank (if it is alphanumeric). If the missing value is
propagated to the internal field, it displays the missing data symbol on the report output.

Syntax:

How to Control Missing Values in Reformatted Fields

SET COMPMISS = {ON|OFF}

where:

ON

Propagates a missing value to a reformatted field. ON is the default value.

OFF

Displays a blank or zero for a reformatted field.

Note: The COMPMISS parameter cannot be set in an ON TABLE command.

Example:

Controlling Missing Values in Reformatted Fields

The following procedure prints the RETURNS field from the SALES data source for store 14Z.
With COMPMISS OFF, the missing values display as zeros in the column for the reformatted
field value.

Note: Before trying this example, you must make sure that the SALEMISS procedure, which
adds missing values to the SALES data source, has been run.

1054

13. Handling Records With Missing Field Values

SET COMPMISS = OFF
TABLE FILE SALES
PRINT RETURNS RETURNS/D12.2 AS 'REFORMATTED,RETURNS'
BY STORE_CODE
WHERE STORE_CODE EQ '14Z'
END

The output is:

                        REFORMATTED
STORE_CODE  RETURNS     RETURNS
----------  -------     -----------
14Z               2            2.00
                  2            2.00
                  0             .00
                  .             .00
                  4            4.00
                  0             .00
                  3            3.00
                  4            4.00
                  .             .00
                  4            4.00

With COMPMISS ON, the column for the reformatted version of RETURNS displays the missing
data symbol when a value is missing:

SET COMPMISS = ON
TABLE FILE SALES
PRINT RETURNS RETURNS/D12.2 AS 'REFORMATTED,RETURNS'
BY STORE_CODE
WHERE STORE_CODE EQ '14Z'
END

The output is:

                        REFORMATTED
STORE_CODE  RETURNS     RETURNS
----------  -------     -----------
14Z               2            2.00
                  2            2.00
                  0             .00
                  .               .
                  4            4.00
                  0             .00
                  3            3.00
                  4            4.00
                  .               .
                  4            4.00

Creating Reports With TIBCO® WebFOCUS Language

 1055

Handling a Missing Segment Instance

Reference: Usage Notes for SET COMPMISS

If you create a HOLD file with COMPMISS ON, the HOLD Master File for the reformatted field
indicates MISSING = ON (as does the original field). With COMPMISS = OFF, the reformatted
field does NOT have MISSING = ON in the generated Master File.

Handling a Missing Segment Instance

In multi-segment data sources, when an instance in a parent segment does not have
descendant instances, the nonexistent descendant instances are called missing instances.

When you write a request from a data source that has missing segment instances, the missing
instances affect the report. For example, if the request names fields in a segment and its
descendants, the report omits parent segment instances that have no descendants. It makes
no difference whether fields are display fields or sort fields.

When an instance is missing descendants in a child segment, the instance, its parent, the
parent of its parent, and so on up to the root segment, is called a short path. Unique
segments are never considered to be missing.

For example, consider the following subset of the EMPLOYEE data source.

The top segment contains employee names.

The left segment contains addresses.

The right segment contains the salary history of each employee: the date the employee was
granted a new salary, and the amount of the salary.

Suppose some employees are paid by an outside agency. None of these employees have a
company salary history. Instances referring to these employees in the salary history segment
are missing.

1056

13. Handling Records With Missing Field Values

Nonexistent descendant instances affect whether parent segment instances are included in
report results. The SET ALL parameter and the ALL. prefix enable you to include parent
segment data in reports.

For illustrations of how missing segment instances impact reporting, see Reporting Against
Segments Without Descendant Instances on page 1057 and Reporting Against Segments With
Descendant Instances on page 1058.

Example:

Reporting Against Segments Without Descendant Instances

The following request displays the salary histories for each employee.

TABLE FILE EMPLOYEE
PRINT SALARY
BY LAST_NAME BY FIRST_NAME
BY DAT_INC
END

However, two employees, Davis and Gardner, are omitted from the following report because
the LAST_NAME and FIRST_NAME fields belong to the root segment, and the DAT_INC and
SALARY fields belong to the descendant salary history segment. Since Davis and Gardner have
no descendant instances in the salary history segment, they are omitted from the report.

The output is:

LAST_NAME        FIRST_NAME   DAT_INC           SALARY
---------        ----------   -------           ------
BANNING          JOHN        82/08/01       $29,700.00
BLACKWOOD        ROSEMARIE   82/04/01       $21,780.00
CROSS            BARBARA     81/11/02       $25,775.00
                             82/04/09       $27,062.00
GREENSPAN        MARY        82/04/01        $8,650.00
                             82/06/11        $9,000.00
IRVING           JOAN        82/01/04       $24,420.00
                             82/05/14       $26,862.00
JONES            DIANE       82/05/01       $17,750.00
                             82/06/01       $18,480.00
MCCOY            JOHN        82/01/01       $18,480.00
MCKNIGHT         ROGER       82/02/02       $15,000.00
                             82/05/14       $16,100.00
ROMANS           ANTHONY     82/07/01       $21,120.00
SMITH            MARY        82/01/01       $13,200.00
                 RICHARD     82/01/04        $9,050.00
                             82/05/14        $9,500.00
STEVENS          ALFRED      81/01/01       $10,000.00
                             82/01/01       $11,000.00

Creating Reports With TIBCO® WebFOCUS Language

 1057

Handling a Missing Segment Instance

Example:

Reporting Against Segments With Descendant Instances

The following request displays the course codes and expenses for employees in the EMPDATA
and TRAIN2 data sources. The report output displays all employees that have instances in the
COURSECODE or EXPENSES fields. The employees that are missing instances for either of
those fields are omitted from the report. For those employees that have instances for only one
of the fields, the designator for missing data displays in the respective column. In this
example, Henry Chisolm has taken two courses but only has expenses for one. Therefore, the
designator for missing instances displays in the EXPENSES column.

JOIN EMPDATA.PIN IN EMPDATA TO ALL TRAINING.PIN IN TRAIN2 AS JOIN1
TABLE FILE EMPDATA
PRINT LASTNAME AND FIRSTNAME AND COURSECODE AND EXPENSES
BY PIN
END

The output is:

PIN

LASTNAME

FIRSTNAME

COURSECODE

EXPENSES

000000010

VALINO

DANIEL

000000030

CASSANOVA

CASSANOVA

.
.
.

000000350

FERNSTEIN

FERNSTEIN

FERNSTEIN

000000360

CHISOLM

CHISOLM

000000370

WANG

000000380

ELLNER

ELLNER

LOIS

LOIS

ERWIN

ERWIN

ERWIN

HENRY

HENRY

JOHN

DAVID

DAVID

000000410

CONTI

MARSHALL

PDR740

NAMA730

EDP090

2,300.00

2,600.00

2,300.00

SSI220

MC90

UMI720

EDP090

EDP690

UMI710

EDP090

UNI780

EDP690

1,850.00

1,730.00

3,350.00

.00

3,000.00

2,050.00

.

3,350.00

3,100.00

Note: The report output has been truncated for demonstration purposes.

1058

13. Handling Records With Missing Field Values

Including Missing Instances in Reports With the ALL. Prefix

If a request excludes parent segment instances that lack descendants, you can include the
parent instances by attaching the ALL. prefix to one of the fields in the parent segment.

Note that if the request contains WHERE or IF criteria that screen fields in segments that have
missing instances, the report omits parent instances even when you use the ALL. prefix. To
include these instances, use the SET ALL=PASS command described in Including Missing
Segment Instances With the ALL. Prefix on page 1059.

Example:

Including Missing Segment Instances With the ALL. Prefix

The following request displays the salary history of each employee. Although employees
Elizabeth Davis and David Gardner have no salary histories, they are included in the report.

TABLE FILE EMPLOYEE
PRINT SALARY
BY ALL.LAST_NAME BY FIRST_NAME
BY DAT_INC
END

The output is:

LAST_NAME        FIRST_NAME   DAT_INC           SALARY
---------        ----------   -------           ------
BANNING          JOHN        82/08/01       $29,700.00
BLACKWOOD        ROSEMARIE   82/04/01       $21,780.00
CROSS            BARBARA     81/11/02       $25,775.00
                             82/04/09       $27,062.00
DAVIS            ELIZABETH          .                .
GARDNER          DAVID              .                .
GREENSPAN        MARY        82/04/01        $8,650.00
                             82/06/11        $9,000.00
IRVING           JOAN        82/01/04       $24,420.00
                             82/05/14       $26,862.00
JONES            DIANE       82/05/01       $17,750.00
                             82/06/01       $18,480.00
MCCOY            JOHN        82/01/01       $18,480.00
MCKNIGHT         ROGER       82/02/02       $15,000.00
                             82/05/14       $16,100.00
ROMANS           ANTHONY     82/07/01       $21,120.00
SMITH            MARY        82/01/01       $13,200.00
                 RICHARD     82/01/04        $9,050.00
                             82/05/14        $9,500.00
STEVENS          ALFRED      81/01/01       $10,000.00
                             82/01/01       $11,000.00

Including Missing Instances in Reports With the SET ALL Parameter

You can control how parent instances with missing descendants are processed by issuing the
SET ALL command before executing the request. In a join, issuing the SET ALL = ON command
controls left outer join processing.

Creating Reports With TIBCO® WebFOCUS Language

 1059

Handling a Missing Segment Instance

Note: A request with WHERE or IF criteria, which screen fields in a segment that has missing
instances, omits instances in the parent segment even if you use the SET ALL=ON command.
To include these instances, use the SET ALL=PASS command.

In WebFOCUS, the command SET ALL = ON or JOIN LEFT_OUTER specifies a left outer join.
With a left outer join, all records from the host file display on the report output. If a cross-
referenced segment instance does not exist for a host segment instance, the report output
displays missing values for the fields from the cross-referenced segment.

If there is a screening condition on the dependent segment, those dependent segment
instances that do not satisfy the screening condition are omitted from the report output, and
so are their corresponding host segment instances. With missing segment instances, tests for
missing values fail because the fields in the segment have not been assigned missing values.

When a relational engine performs a left outer join, it processes host records with missing
cross-referenced segment instances slightly differently from the way WebFOCUS processes
those records when both of the following conditions apply:

There is a screening condition on the cross-referenced segment.

A host segment instance does not have a corresponding cross-referenced segment
instance. This is called a short path.

When these two conditions are true, WebFOCUS omits the host record from the report output,
while relational engines supply null values for the fields from the dependent segment and then
apply the screening condition. If the missing values pass the screening condition, the entire
record is retained on the report output. This type of processing is useful for finding or counting
all host records that do not have matching records in the cross-referenced file or for creating a
DEFINE-based join from the cross-referenced segment with the missing instance to another
dependent segment.

If you want WebFOCUS to assign null values to the fields in a missing segment instance when
a left outer join is in effect, you can issue the command SET SHORTPATH=SQL.

Syntax:

How to Include a Parent Instance With Missing Descendants

SET ALL= {OFF|ON|PASS}

where:

OFF

Omits parent instances that are missing descendants from the report. OFF is the default
value.

1060

13. Handling Records With Missing Field Values

ON

Includes parent instances that are missing descendants in the report. However, if a test
on a missing segment fails, this causes the parent to be omitted from the output. It is
comparable to the ALL. prefix.

PASS

Includes parent instances that are missing descendants, even if WHERE or IF criteria exist
to screen fields in the descendant segments that are missing instances (that is, a test on
a missing segment passes).

Example:

Including Missing Segment Instances With SET ALL

The following request displays all employees, regardless of whether they have taken a course
or not since the ALL=PASS command is set.

If the ALL=ON command had been used, employees that had not taken courses would have
been omitted because of the WHERE criteria.

JOIN EMPDATA.PIN IN EMPDATA TO ALL TRAINING.PIN IN TRAINING AS JOIN1
SET ALL = PASS
TABLE FILE EMPDATA
PRINT LASTNAME AND FIRSTNAME AND COURSECODE AND EXPENSES
BY PIN
WHERE EXPENSES GT 3000
END

Creating Reports With TIBCO® WebFOCUS Language

 1061

Handling a Missing Segment Instance

The output is:

Syntax:

How to Control Short Path Processing In a Left Outer Join

SET SHORTPATH = {FOCUS|SQL}

where:

FOCUS

Omits a host segment from the report output when it has no corresponding cross-
referenced segment and the report has a screening condition on the cross-referenced
segment.

SQL

Supplies missing values for the fields in a missing cross-referenced segment in an outer
join. Applies screening conditions against this record and retains the record on the report
output if it passes the screening test.

Note: There must be an outer join in effect, either as a result of the SET ALL=ON
command or a JOIN LEFT_OUTER command (either inside or outside of the Master File).

1062

13. Handling Records With Missing Field Values

Reference: Usage Notes for SET SHORTPATH = SQL

A FOCUS data source is supported as the host file in a join used with SET SHORTPATH = SQL,
but not as the cross-referenced file.

Example:

Controlling Outer Join Processing

The following procedure creates two Oracle tables, ORAEMP and ORAEDUC, that will be used in
a join.

TABLE FILE EMPLOYEE
SUM LAST_NAME FIRST_NAME CURR_SAL CURR_JOBCODE DEPARTMENT
BY EMP_ID
ON TABLE HOLD AS ORAEMP FORMAT SQLORA
END
-RUN
TABLE FILE EDUCFILE
SUM COURSE_CODE COURSE_NAME
BY EMP_ID BY DATE_ATTEND
ON TABLE HOLD AS ORAEDUC FORMAT SQLORA
END

The following request joins the two Oracle tables and creates a left outer join (SET ALL = ON).

JOIN EMP_ID IN ORAEMP TO ALL EMP_ID IN ORAEDUC AS J1
SET ALL = ON
TABLE FILE ORAEMP
PRINT COURSE_CODE COURSE_NAME
BY EMP_ID
END

Since the join is an outer join, all ORAEMP rows display on the report output. ORAEMP rows
with no corresponding ORAEDUC row display the missing data symbol for the fields from the
ORAEDUC table.

Creating Reports With TIBCO® WebFOCUS Language

 1063

Handling a Missing Segment Instance

EMP_ID     COURSE_CODE     COURSE_NAME
------     -----------     -----------
071382660  101             FILE DESCRPT & MAINT
112847612  101             FILE DESCRPT & MAINT
           103             BASIC REPORT PREP FOR PROG
117593129  101             FILE DESCRPT & MAINT
           103             BASIC REPORT PREP FOR PROG
           201             ADVANCED TECHNIQUES
           203             FOCUS INTERNALS
119265415  108             BASIC RPT NON-DP MGRS
119329144  .               .
123764317  .               .
126724188  .               .
219984371  .               .
326179357  104             FILE DESC & MAINT NON-PROG
           106             TIMESHARING WORKSHOP
           102             BASIC REPORT PREP NON-PROG
           301             DECISION SUPPORT WORKSHOP
           202             WHAT'S NEW IN FOCUS
451123478  101             FILE DESCRPT & MAINT
543729165  .               .
818692173  107             BASIC REPORT PREP DP MGRS

The following request adds a screening condition on the ORAEDUC segment. To satisfy the
screening condition, the course name must either contain the characters BASIC or be missing.

JOIN CLEAR
JOIN EMP_ID IN ORAEMP TO ALL EMP_ID IN ORAEDUC AS J1
SET ALL = ON
TABLE FILE ORAEMP
PRINT COURSE_CODE COURSE_NAME
BY EMP_ID
WHERE COURSE_NAME CONTAINS 'BASIC' OR COURSE_NAME IS MISSING
END

However, with SET ALL = ON, the rows with missing values are not retained on the report
output.

EMP_ID     COURSE_CODE     COURSE_NAME
------     -----------     -----------
112847612  103             BASIC REPORT PREP FOR PROG
117593129  103             BASIC REPORT PREP FOR PROG
119265415  108             BASIC RPT NON-DP MGRS
326179357  102             BASIC REPORT PREP NON-PROG
818692173  107             BASIC REPORT PREP DP MGRS

1064

13. Handling Records With Missing Field Values

The following request adds the SET SHORTPATH = SQL command.

JOIN CLEAR
JOIN EMP_ID IN ORAEMP TO ALL EMP_ID IN ORAEDUC AS J1
SET ALL = ON
SET SHORTPATH=SQL
TABLE FILE ORAEMP
PRINT COURSE_CODE COURSE_NAME
BY EMP_ID
WHERE COURSE_NAME CONTAINS 'BASIC' OR COURSE_NAME IS MISSING
END

The report output now displays both the records containing the characters BASIC and those
with missing values.

EMP_ID     COURSE_CODE     COURSE_NAME
------     -----------     -----------
112847612  103             BASIC REPORT PREP FOR PROG
117593129  103             BASIC REPORT PREP FOR PROG
119265415  108             BASIC RPT NON-DP MGRS
119329144  .               .
123764317  .               .
126724188  .               .
219984371  .               .
326179357  102             BASIC REPORT PREP NON-PROG
543729165  .               .
818692173  107             BASIC REPORT PREP DP MGRS

Example:

Finding Host Records That Have No Matching Cross-Referenced Records

The following request counts and lists those employees who have taken no courses.

JOIN LEFT_OUTER EMP_ID IN ORAEMP TO ALL EMP_ID IN ORAEDUC AS J1
SET ALL = ON
SET SHORTPATH=SQL
TABLE FILE ORAEMP
COUNT EMP_ID
LIST EMP_ID LAST_NAME FIRST_NAME
WHERE COURSE_NAME IS MISSING
END

The output is:

EMP_ID
COUNT    LIST  EMP_ID     LAST_NAME        FIRST_NAME
------   ----  ------     ---------        ----------
     5      1  119329144  BANNING          JOHN
            2  123764317  IRVING           JOAN
            3  126724188  ROMANS           ANTHONY
            4  219984371  MCCOY            JOHN
            5  543729165  GREENSPAN        MARY

Creating Reports With TIBCO® WebFOCUS Language

 1065

Setting the NODATA Character String

Testing for Missing Instances in FOCUS Data Sources

You can use the ALL PASS parameter to produce reports that include only parent instances
with missing descendant values. To do so, write the request to screen out all existing
instances in the segment with missing instances. After you set the ALL parameter to PASS, the
report displays only the parent instances that are missing descendants.

Example:

Testing for a MISSING Instance in a FOCUS Data Source

The following request tests for missing instances in the COURSECODE field. Since no
COURSECODE can equal 'XXXX', only employees with missing instances in COURSECODE
display in the report output.

JOIN EMPDATA.PIN IN EMPDATA TO ALL TRAINING.PIN IN TRAINING AS JOIN1
SET ALL = PASS
TABLE FILE EMPDATA
PRINT LASTNAME AND FIRSTNAME AND COURSECODE AND EXPENSES
BY PIN
WHERE COURSECODE EQ 'XXXX'
END

The output is:

PIN

LASTNAME

FIRSTNAME

COURSECODE

EXPENSES

000000020

000000060

BELLA

PATEL

000000070

SANCHEZ

MICHAEL

DORINA

EVELYN

000000090

PULASKI

MARIANNE

000000130

000000170

000000220

000000230

000000300

000000390

000000400

CVEK

MORAN

LEWIS

NOZAWA

SOPENA

GRAFF

LOPEZ

MARCUS

WILLIAM

CASSANDRA

JIM

BEN

ELAINE

ANNE

.

.

.

.

.

.

.

.

.

.

.

       .

       .

       .

       .

       .

       .

       .

       .

       .

       .

       .

Setting the NODATA Character String

In a report, the NODATA character string indicates no data or inapplicable data. The default
NODATA character is a period. However, you can change this character designation.

1066

13. Handling Records With Missing Field Values

Syntax:

How to Set the NODATA String

SET NODATA = string

where:

string

Is the character string used to indicate missing data in reports. The default string is a
period (.). The string may be a maximum of 11 characters. Common choices are NONE,
N/A, and MISSING.

Example:

Setting NODATA Not to Display Characters

If you do not want any characters, issue the command:

SET NODATA = ' '

Example:

Setting the NODATA Character String

In the following request, the NODATA character string is set to MISSING. The word MISSING
displays on the report instead of the default period.

SET NODATA=MISSING

TABLE FILE EMPLOYEE
PRINT CURR_SAL BY LAST_NAME BY FIRST_NAME
ACROSS DEPARTMENT
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1067


Setting the NODATA Character String

1068

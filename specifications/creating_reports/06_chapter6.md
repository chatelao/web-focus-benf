Chapter6

Including Totals and Subtotals

To help interpret detailed information in a report, you can summarize the information
using row and column totals, grand totals, and subtotals. You can use these summary
lines in a report to clarify or highlight information.

In this chapter:

Calculating Row and Column Totals

Including Section Totals and a Grand Total

Including Subtotals

Recalculating Values for Subtotal Rows

Summarizing Alphanumeric Columns

Manipulating Summary Values With Prefix Operators

Combinations of Summary Commands

Producing Summary Columns for Horizontal Sort Fields

Performing Calculations at Sort Field Breaks

Suppressing Grand Totals

Conditionally Displaying Summary Lines and Text

Calculating Row and Column Totals

You can produce totals for rows or columns of numbers in a report. Use:

ROW-TOTAL to display a new column containing the sum of all numbers in each row.

COLUMN-TOTAL to display a final row on the report, which contains the totals for each
column of numbers.

You can use row totals and column totals in matrix reports (created by using a BY and an
ACROSS in your report request), rename row and column total titles, and include calculated
values in your row or column totals. You can also create row totals using ACROSS-TOTAL.

Creating Reports With TIBCO® WebFOCUS Language

 367

Calculating Row and Column Totals

Note that when producing totals in a report, if one field is summed, the format of the row total
is the same as the format of the field. For example, if the format of the CURR_SAL field is
D12.2M, the format of the row total for CURR_SAL is also D12.2M. When you are summing
fields with different formats, the default format of D12.2 is used for the total.

You can rename the default column titles using the AS phrase and align the labels for row and
column totals. For details, see Using Headings, Footings, Titles, and Labels on page 1517.

Syntax:

How to Calculate Row and Column Totals

display_command fieldname AND ROW-TOTAL [alignment][/format] [AS 'name']
display_command fieldname AND COLUMN-TOTAL [alignment][AS 'name']

where:

display_command

Is one of the following commands: PRINT, LIST, SUM, or COUNT.

fieldname

Is the name of the field for which to calculate row and/or column totals.

alignment

Specifies the alignment of the ROW-TOTAL or COLUMN-TOTAL label. Possible values
are:

/R right justifies the label.

/L left justifies the label.

/C centers the label.

Note that these alignment settings are ignored in HTML output. If you are working in
WebFOCUS, to take advantage of column alignment features, you can include the
command SET STYLE=OFF in the report request or generate your output in PDF, or in
another format that supports these features.

format

Reformats the ROW-TOTAL.

name

Is the label for the ROW-TOTAL or COLUMN-TOTAL.

You may also specify row or column totals with the ON TABLE command. Field names are
optional with COLUMN-TOTAL, and cannot be listed with ROW-TOTAL. Use the following syntax:

ON TABLE COLUMN-TOTAL [alignment][AS 'name'][field field field]
ON TABLE ROW-TOTAL [alignment][/format] [AS 'name']

368

6. Including Totals and Subtotals

Example:

Calculating Row and Column Totals

The following request illustrates the use of ROW-TOTAL and COLUMN-TOTAL. The column and
row total labels are "TOTAL" by default. You can change them using an AS phrase.

TABLE FILE SALES
SUM RETURNS DAMAGED AND ROW-TOTAL AND COLUMN-TOTAL
BY PROD_CODE
END

The output is:

PROD_CODE  RETURNS  DAMAGED      TOTAL
---------  -------  -------  ---------
B10             13       10         23
B12              4        3          7
B17              4        2          6
B20              1        2          3
C13              3        0          3
C17              0        0          0
C7               5        4          9
D12              3        2          5
E1               4        7         11
E2               9        4         13
E3              12       11         23

TOTAL           58       45        103

Example:

Specifying Column Totals With ON TABLE

The following request illustrates the use of COLUMN-TOTAL with the ON TABLE command.

TABLE FILE EMPLOYEE
PRINT CURR_SAL
BY LAST_NAME
ON TABLE COLUMN-TOTAL
END

Creating Reports With TIBCO® WebFOCUS Language

 369


Calculating Row and Column Totals

The output is:

LAST_NAME               CURR_SAL
---------               --------
BANNING               $29,700.00
BLACKWOOD             $21,780.00
CROSS                 $27,062.00
GREENSPAN              $9,000.00
IRVING                $26,862.00
JONES                 $18,480.00
MCCOY                 $18,480.00
MCKNIGHT              $16,100.00
ROMANS                $21,120.00
SMITH                 $13,200.00
                       $9,500.00
STEVENS               $11,000.00

TOTAL                $222,284.00

Example:

Using Row and Column Totals in a Matrix Report

The following request illustrates the use of ROW-TOTAL and COLUMN-TOTAL in a matrix report
(created by using the BY and ACROSS phrases together).

TABLE FILE EMPLOYEE
SUM CURR_SAL AND ROW-TOTAL AND COLUMN-TOTAL
BY BANK_NAME
ACROSS DEPARTMENT
END

The output is:

                           DEPARTMENT
BANK_NAME                  MIS              PRODUCTION
TOTAL
-----------------------------------------------------------------------
                           $40,680.00       $41,620.00       $82,300.00
ASSOCIATED                 $21,780.00       $42,962.00       $64,742.00
BANK ASSOCIATION           $27,062.00                .       $27,062.00
BEST BANK                           .       $29,700.00       $29,700.00
STATE                      $18,480.00                .       $18,480.00

TOTAL                     $108,002.00      $114,282.00      $222,284.00

370



Example:

Including Calculated Values in Row and Column Totals

The following request illustrates the inclusion of the calculated value, PROFIT, in row and
column totals.

6. Including Totals and Subtotals

TABLE FILE CAR
SUM DCOST RCOST
COMPUTE PROFIT/D12=RCOST-DCOST;
ROW-TOTAL/L/D12 AS 'TOTAL_COST'
BY COUNTRY
ON TABLE COLUMN-TOTAL/L AS 'FINAL_TOTAL'
END

The output is:

COUNTRY     DEALER_COST  RETAIL_COST           PROFIT
TOTAL_COST
-------     -----------  -----------           ------  ---------------
ENGLAND          37,853       45,319            7,466           90,638
FRANCE            4,631        5,610              979           11,220
ITALY            41,235       51,065            9,830          102,130
JAPAN             5,512        6,478              966           12,956
W GERMANY        54,563       64,732           10,169          129,464

FINAL_TOTAL     143,794      173,204           29,410          346,408

Reference: Using ROW-TOTAL With ACROSS and Multiple Display Commands

When a request has an ACROSS sort field, each ACROSS value displays a column for each
field displayed on the report output. For example, the following request, each state has a
column for units and a column for dollars:

TABLE FILE GGSALES
SUM UNITS AS 'U' DOLLARS AS 'D' BY CITY
ACROSS ST
IF ST EQ 'CA'
IF BUDUNITS NE MISSING
END

The output is:

                       State
                       CA
City                         U        D
-----------------------------------------
Los Angeles             298070  3772014
San Francisco           312500  3870258

Creating Reports With TIBCO® WebFOCUS Language

 371


Calculating Row and Column Totals

When you specify a row total with ACROSS, the row total is calculated separately for each
column in each ACROSS group. For example, in the following request the row total has a
column for units and a column for dollars:

TABLE FILE GGSALES
SUM UNITS AS 'U' DOLLARS AS 'D' BY CITY
ACROSS ST
IF ST EQ 'CA'
IF BUDUNITS NE MISSING
  ON TABLE ROW-TOTAL
END

The output is:

                       State
                       CA                          TOTAL
 City                         U        D         U        D
 ----------------------------------------------------------
 Los Angeles             298070  3772014    298070  3772014
 San Francisco           312500  3870258    312500  3870258

When the request also has multiple display commands, each additional command adds
additional columns to each ACROSS group on the report output.

The first column of the row total group is calculated by adding the first column from each
display command under each ACROSS value, the second column adds the second column from
each display command, and so on.

For example, the following request has a SUM command for units and dollars and another
SUM command for budgeted units and budgeted dollars. The row total has a column for the
sum of units and budgeted units and another column for the sum of dollars and budgeted
dollars:

TABLE FILE GGSALES
SUM UNITS AS 'U' DOLLARS AS 'D'         BY CITY
SUM BUDUNITS AS 'BU' BUDDOLLARS AS 'BD' BY CITY
ACROSS ST
IF ST EQ 'CA'
IF BUDUNITS NE MISSING
ON TABLE ROW-TOTAL
END

The output is:

                   State
                   CA
TOTAL
City                    U         D        BU       BD       BU       BD
------------------------------------------------------------------------
Los Angeles        298070   3772014    295637  3669484   593707  7441498
San Francisco      312500   3870258    314725  3916863   627225  7787121

372

6. Including Totals and Subtotals

If the different display commands do not all specify the same number of fields, some columns
will not be represented in the row total. For example, in the following request, the second SUM
command has a column for budgeted units but not for budgeted dollars. Therefore, the row
total group has no column for dollars:

TABLE FILE GGSALES
SUM UNITS AS 'U' DOLLARS AS 'D' BY CITY
SUM BUDUNITS AS 'BU'            BY CITY
ACROSS ST
IF ST EQ 'CA'
IF BUDUNITS NE MISSING
ON TABLE ROW-TOTAL
END

The output is:

                        State
                        CA                             TOTAL
City                         U         D        BU        BU
------------------------------------------------------------
Los Angeles             298070   3772014    295637    593707
San Francisco           312500   3870258    314725    627225

In this case, you can use column notation to calculate the row total properly. For example, the
following request calculates the row total column by adding the units, dollars, and budgeted
units columns together:

TABLE FILE GGSALES
SUM UNITS AS 'U' DOLLARS AS 'D' BY CITY
SUM BUDUNITS AS 'BU'            BY CITY
ACROSS ST
COMPUTE TOTAL/I10 = C1 + C2 +C3; AS 'ROW-TOTAL'
IF ST EQ 'CA'
IF BUDUNITS NE MISSING
END

The output is:

                        State
                        CA                            ROW-TOTAL
City                         U         D        BU
---------------------------------------------------------------
Los Angeles             298070   3772014    295637      4365721
San Francisco           312500   3870258    314725      4497483

Creating Reports With TIBCO® WebFOCUS Language

 373

Calculating Row and Column Totals

Producing Row Totals for Horizontal (ACROSS) Sort Field Values

You can produce row totals for horizontal (ACROSS) sort field values. Row totals for horizontal
sort fields, referenced by ACROSS-TOTAL, are different from standard row totals because only
horizontal sort field values, referenced by ACROSS, are included in the total. Integer, single
precision floating point, double precision floating point, packed, and long packed fields can all
be totaled.

Syntax:

How to Produce Row Totals for Horizontal (ACROSS) Sort Field Values

ACROSS sortfield ACROSS-TOTAL [AS 'name'] [COLUMNS col1 AND col2 ...]

where:

sortfield

Is the name of the field being sorted across.

name

Is the new name for the ACROSS-TOTAL column title.

col1, col2

Are the titles of the ACROSS columns you want to include in the total.

Example:

Producing Row Totals for Horizontal (ACROSS) Sort Field Values

The following illustrates how to generate a row total for horizontal (ACROSS) sort field values.
Notice that the summed values in the TOTAL TITLE COUNT column only reflect the values in the
(RATING) PG and R columns. The values in the COPIES column are not included since they are
not horizontal (ACROSS) sort field values.

TABLE FILE MOVIES
SUM COPIES BY CATEGORY
COUNT TITLE BY CATEGORY
ACROSS RATING ACROSS-TOTAL
COLUMNS PG AND R
END

The output is:

                    RATING
                    PG     R      TOTAL
  CATEGORY  COPIES
  ---------------------------------------
  ACTION        14      2      3      5
  COMEDY        16      4      1      5
  DRAMA          2      0      1      1
  FOREIGN        5      2      3      5
  MUSICALS       2      1      1      2
  MYSTERY       17      2      5      7
  SCI/FI         3      0      3      3

374

Reference: Usage Notes for ACROSS-TOTAL

Stacking headings in ACROSS-TOTAL is not supported.

6. Including Totals and Subtotals

Attempting to use ACROSS-TOTAL with other types of fields (alphanumeric, text, and dates)
produces blank columns.

In cases of multiple ACROSS columns with ACROSS-TOTAL, there are additional columns
with subtotaled values.

The results of ROW-TOTAL and ACROSS-TOTAL are the same if there is only a single display
field or single display command in the procedure.

The maximum number of ACROSS-TOTAL components is five.

ACROSS-TOTAL populates the ACROSSVALUE component in a StyleSheet. For an example
of styling an ACROSS-TOTAL component, see Identifying Row Totals (ACROSS-TOTAL) for
Horizontal Sort Data on page 1266.

Including Section Totals and a Grand Total

Frequently, reports contain detailed information that is broken down into subsections, for
which simple column and row totals may not provide adequate summaries. In these instances,
it is more useful to look at subtotals for particular sections, and a grand total.

You can add the following commands to your requests to create section subtotals and grand
totals:

SUB-TOTAL and SUBTOTAL

SUMMARIZE and RECOMPUTE (used with calculated values)

RECAP and COMPUTE

Each command produces grand totals and/or subtotals by using different information.
Subtotals produce totals every time a specified sort field value changes, and are independent
of record selection criteria. You can further control when subtotals are produced by specifying
WHEN criteria (see Conditionally Displaying Summary Lines and Text on page 427). You can
control whether subtotals display above or below the data. For information, see How to Control
Placement of Summary Lines on page 378. You can also suppress grand totals using the
NOTOTAL command. For details, see Suppressing Grand Totals on page 425.

By default, a blank line is generated before a subtotal on the report output. You can eliminate
these automatic blank lines by issuing the SET DROPBLNKLINE=ON command.

Note: When the request has a PAGE-BREAK command, the GRANDTOTAL is on a page by itself.

Creating Reports With TIBCO® WebFOCUS Language

 375

Including Section Totals and a Grand Total

You can use prefix operators with SUBTOTAL, SUB-TOTAL, SUMMARIZE, and RECOMPUTE. For
details, see Manipulating Summary Values With Prefix Operators on page 388. In addition, you
can combine different summary operations in a single request. For information, see
Combinations of Summary Commands on page 407.

Example:

Using Section Totals and Grand Totals

The following request illustrates how to create a subtotal every time the department value
changes. The grand total is automatically produced when you use the SUBTOTAL command.

TABLE FILE EMPLOYEE
SUM DED_AMT BY DED_CODE BY DEPARTMENT
BY BANK_ACCT
WHERE BANK_ACCT NE 0
WHERE DED_CODE EQ 'CITY' OR 'FED'
ON DEPARTMENT SUBTOTAL
END

The first and last portions of the output are:

DED_CODE  DEPARTMENT  BANK_ACCT          DED_AMT
--------  ----------  ---------          -------
CITY      MIS          40950036           $14.00
                      122850108           $31.75
                      163800144           $82.70

*TOTAL DEPARTMENT MIS                    $128.45

          PRODUCTION     160633            $7.42
                      136500120           $18.25
                      819000702           $60.20

*TOTAL DEPARTMENT PRODUCTION              $85.87

FED       MIS          40950036        $1,190.77
                      122850108        $2,699.80
                      163800144        $7,028.30

*TOTAL DEPARTMENT MIS                 $10,918.87

          PRODUCTION     160633          $631.12
                      136500120        $1,552.10
                      819000702        $5,120.04

*TOTAL DEPARTMENT PRODUCTION           $7,303.26

TOTAL                                 $18,436.45

376










Including Subtotals

6. Including Totals and Subtotals

You can use the SUBTOTAL and SUB-TOTAL commands to sum individual values, such as
columns of numbers, each time a named sort field changes value.

SUB-TOTAL displays a subtotal when the sort field changes value, and for any higher-level
sort fields when their values change.

SUBTOTAL displays a subtotal only when the specified sort field changes value. It does not
give subtotals for higher-level fields.

Both SUB-TOTAL and SUBTOTAL produce grand totals. You can suppress grand totals using the
NOTOTAL command. See Suppressing Grand Totals on page 425.

The subtotal is calculated every time the sort field value changes or, if WHEN criteria are
applied to the sort field, every time the WHEN conditions are met.

A BY, ACROSS, or ON phrase is required to initialize the syntax.

Syntax:

How to Create Subtotals

{BY|ON} fieldname {SUB-TOTAL|SUBTOTAL} [MULTILINES]
      [field1 [AND] field2...] [AS 'text'][WHEN expression;]

where:

fieldname

Must be the name of a field in a sort phrase. A BY phrase can include a summary
command. The number of fields to subtotal multiplied by the number of levels of
subtotals counts in the number of display fields permitted for the request. For details
on determining the maximum number of display fields that can be used in a request,
see Displaying Report Data on page 39.

SUB-TOTAL|SUBTOTAL

SUB-TOTAL displays subtotals for numeric values when the BY|ON field changes value,
and for any higher-level sort fields when their values change.

SUBTOTAL displays a subtotal only when the specified sort field changes value.

MULTILINES

Suppresses the printing of a subtotal line for every sort break that has only one detail
line, since the subtotal value is equal to this one value. Note that MULTI-LINES is a
synonym for MULTILINES. MULTILINES is not supported with horizontal (ACROSS) sort
fields.

field1, field2, ...

Denotes a list of specific fields to subtotal. This list overrides the default, which
includes all numeric display fields. The list can included numeric and alphanumeric
fields.

Creating Reports With TIBCO® WebFOCUS Language

 377

Including Subtotals

You can use the asterisk (*) wildcard character instead of a field list to indicate that all
fields, numeric and alphanumeric, should be included on the summary lines.

AS 'text'

Enables you to specify a different label. For related information, see Using Headings,
Footings, Titles, and Labels on page 1517.

WHEN expression

Specifies the conditional display of subtotals as determined by a Boolean expression.
You must end the expression with a semicolon.

Syntax:

How to Control Placement of Summary Lines

SET SUBTOTALS = {ABOVE|BELOW}

where:

ABOVE

Places summary lines above the detail lines and displays the sort field values on every
detail line of the report output.

BELOW

Places summary lines below the detail lines. BELOW is the default value.

Note: SET SUBTOTALS = ABOVE is not supported with format XLSX, EXL07, or EXL2K
FORMULA.

Example:

Placing Subtotals Above the Data

The following request against the EMPLOYEE data source sums deduction amounts and gross
salaries by department, deduction code, and last name. It then subtotals the deduction
amounts and gross salaries for each department. The following request places the subtotals
below the detail lines (the default):

TABLE FILE EMPLOYEE
SUM DED_AMT GROSS
BY DEPARTMENT
BY DED_CODE
  BY LAST_NAME
WHERE BANK_ACCT NE 0
WHERE DED_CODE EQ 'FICA' OR 'CITY'
  ON DEPARTMENT SUBTOTAL
  ON TABLE SET SUBTOTALS BELOW
  ON TABLE SET PAGE NOPAGE
END

378

6. Including Totals and Subtotals

The output is:

DEPARTMENT  DED_CODE  LAST_NAME                DED_AMT            GROSS
----------  --------  ---------                -------            -----
MIS         CITY      BLACKWOOD                 $31.76        $9,075.00
                      CROSS                     $82.69       $22,013.77
                      JONES                     $14.01        $6,099.50
            FICA      BLACKWOOD              $2,223.37        $9,075.00
                      CROSS                  $5,788.01       $22,013.77
                      JONES                    $980.64        $6,099.50

*TOTAL DEPARTMENT MIS                        $9,120.47       $74,376.54

PRODUCTION  CITY      BANNING                    $7.42        $2,475.00
                      IRVING                    $60.24       $17,094.00
                      MCKNIGHT                  $18.26        $9,129.99
            FICA      BANNING                  $519.75        $2,475.00
                      IRVING                 $4,216.53       $17,094.00
                      MCKNIGHT               $1,278.21        $9,129.99

*TOTAL DEPARTMENT PRODUCTION                 $6,100.40       $57,397.98

TOTAL                                       $15,220.88      $131,774.52

The following is the same request, but with the subtotals placed above the detail lines:

TABLE FILE EMPLOYEE
SUM DED_AMT GROSS
BY DEPARTMENT
BY DED_CODE
  BY LAST_NAME
WHERE BANK_ACCT NE 0
WHERE DED_CODE EQ 'FICA' OR 'CITY'
  ON DEPARTMENT SUBTOTAL
  ON TABLE SET SUBTOTALS ABOVE
  ON TABLE SET PAGE NOPAGE
END

Creating Reports With TIBCO® WebFOCUS Language

 379

Including Subtotals

On the output, the grand total line comes first, then the subtotal for the MIS department
followed by the detail lines for the MIS department, followed by the subtotal for the
PRODUCTION department and its detail lines. Note that all sort field values display on each
line of the report output:

DEPARTMENT  DED_CODE  LAST_NAME                DED_AMT            GROSS
----------  --------  ---------                -------            -----
TOTAL                                       $15,220.88      $131,774.52
*TOTAL DEPARTMENT MIS                        $9,120.47       $74,376.54

MIS         CITY      BLACKWOOD                 $31.76        $9,075.00
MIS         CITY      CROSS                     $82.69       $22,013.77
MIS         CITY      JONES                     $14.01        $6,099.50
MIS         FICA      BLACKWOOD              $2,223.37        $9,075.00
MIS         FICA      CROSS                  $5,788.01       $22,013.77
MIS         FICA      JONES                    $980.64        $6,099.50

*TOTAL DEPARTMENT PRODUCTION                 $6,100.40       $57,397.98

PRODUCTION  CITY      BANNING                    $7.42        $2,475.00
PRODUCTION  CITY      IRVING                    $60.24       $17,094.00
PRODUCTION  CITY      MCKNIGHT                  $18.26        $9,129.99
PRODUCTION  FICA      BANNING                  $519.75        $2,475.00
PRODUCTION  FICA      IRVING                 $4,216.53       $17,094.00
PRODUCTION  FICA      MCKNIGHT               $1,278.21        $9,129.99

Reference: Usage Notes for Subtotals

When using a SUM or COUNT command with only one sort phrase in the request, SUB-
TOTAL and SUBTOTAL produce the same result as the value of the SUM or COUNT
command. However, when using a PRINT command with one sort phrase, SUBTOTAL is
useful because there can be many values within a sort break.

All SUB-TOTALs display up to and including the point where the sort break occurs, so only
the innermost point of subtotaling should be requested. For instance, if the BY fields are

BY AREA
BY PROD_CODE
BY DATE SUB-TOTAL

then, when AREA changes, subtotals are displayed for DATE, PROD_CODE, and AREA on
three lines (one under the other).

If you use a WHERE TOTAL or IF TOTAL test, the display of the sort field value for the
subtotal line is suppressed unless PRINTPLUS is ON. For details about using PRINTPLUS in
WebFOCUS, see Using PRINTPLUS on page 1678.

Subtotals display on the next line if the subtotal text does not fit on the line prior to the
displayed field columns.

380

6. Including Totals and Subtotals

If a report request has multiple BY phrases, with SUBTOTAL/SUMMARIZE/RECOMPUTE/
SUB-TOTAL at several levels, and MULTILINES or MULTI-LINES is specified at any one of
those levels, it applies to all levels.

Note: ON BYfield SUBFOOT applies only to the level specified.

Example:

Generating Subtotals

The following request illustrates how to create a subtotal for SALES every time the country
value changes.

TABLE FILE CAR
SUM AVE.MPG AND SALES AND AVE.RETAIL_COST
BY COUNTRY SUB-TOTAL SALES
BY BODYTYPE
END

The output is:

                             AVE           AVE
COUNTRY     BODYTYPE         MPG    SALES  RETAIL_COST
-------     --------         ----   -----  -----------
ENGLAND     CONVERTIBLE        16       0        8,878
            HARDTOP            25       0        5,100
            SEDAN              10   12000       15,671

*TOTAL ENGLAND                      12000

FRANCE      SEDAN              21       0        5,610

*TOTAL FRANCE                           0

ITALY       COUPE              11   12400       19,160
            ROADSTER           21   13000        6,820
            SEDAN              21    4800        5,925
*TOTAL ITALY

JAPAN       SEDAN              14   78030        3,239

*TOTAL JAPAN                        78030

W GERMANY   SEDAN              20   88190        9,247

*TOTAL W GERMANY                    88190

TOTAL                              208420

Creating Reports With TIBCO® WebFOCUS Language

 381

Including Subtotals

Example:

Comparing SUB-TOTAL and SUBTOTAL

The following request illustrates how to create a subtotal for the numeric fields DED_AMT and
GROSS when the department value changes, and for the higher-level sort field (DED_CODE)
when its value changes.

TABLE FILE EMPLOYEE
SUM DED_AMT GROSS BY DED_CODE BY DEPARTMENT
BY BANK_ACCT
WHERE BANK_ACCT NE 0
ON DEPARTMENT SUB-TOTAL
END

If you use SUBTOTAL instead of SUB-TOTAL, the totals for DED_AMT and GROSS display only
when the DEPARTMENT value changes.

The first portion of the output is:

DED_CODE  DEPARTMENT  BANK_ACCT          DED_AMT            GROSS
--------  ----------  ---------          -------            -----
CITY      MIS          40950036           $14.00        $6,099.50
                      122850108           $31.75        $9,075.00
                      163800144           $82.70       $22,013.75

*TOTAL DEPARTMENT MIS                    $128.45       $37,188.25

          PRODUCTION     160633            $7.42        $2,475.00
                      136500120           $18.25        $9,130.00
                      819000702           $60.20       $17,094.00

*TOTAL DEPARTMENT PRODUCTION              $85.87       $28,699.00
*TOTAL DED_CODE CITY                     $214.32       $65,887.25

The last portion of the output is:

DED_CODE  DEPARTMENT  BANK_ACCT          DED_AMT            GROSS
--------  ----------  ---------          -------            -----
STAT      MIS          40950036          $196.13        $6,099.50
                      122850108          $444.65        $9,075.00
                      163800144        $1,157.60       $22,013.75

*TOTAL DEPARTMENT MIS                  $1,798.38       $37,188.25

          PRODUCTION     160633          $103.95        $2,475.00
                      136500120          $255.65        $9,130.00
                      819000702          $843.32       $17,094.00

*TOTAL DEPARTMENT PRODUCTION           $1,202.92       $28,699.00
*TOTAL DED_CODE STAT                   $3,001.30       $65,887.25

TOTAL                                 $41,521.18      $461,210.75

382

6. Including Totals and Subtotals

Recalculating Values for Subtotal Rows

You can use the SUMMARIZE and RECOMPUTE commands instead of SUB-TOTAL and
SUBTOTAL to recalculate the result of a COMPUTE command. SUMMARIZE is similar to SUB-
TOTAL in that it recomputes values at every sort break. RECOMPUTE is similar to SUBTOTAL in
that it recalculates only at the specified sort break.

SUMMARIZE recomputes grand totals for the entire report. If you wish to suppress grand
totals, you can include the NOTOTAL command in your request. See Suppressing Grand Totals
on page 425.

Syntax:

How to Subtotal Calculated Values

{BY|ON} fieldname {SUMMARIZE|RECOMPUTE} [MULTILINES]
      [field1 [AND] field2...] [AS 'text'][WHEN expression;]

where:

fieldname

Must be the name of a field in a sort phrase. A BY phrase can include a summary
command. The number of fields to summarize multiplied by the number of levels of
summary commands counts in the number of display fields for the request. For details
on determining the maximum number of display fields that can be used in a request,
see Displaying Report Data on page 39.

SUMMARIZE

Recomputes values at every sort break.

RECOMPUTE

Recalculates values only at the specified sort break.

MULTILINES

Suppresses the printing of a subtotal line for every sort break that has only one detail
line, since the subtotal value is equal to this one value. Note that MULTI-LINES is a
synonym for MULTILINES. MULTILINES is not supported with horizontal (ACROSS) sort
fields.

You can also suppress grand totals using the NOTOTAL command, as described in
Suppressing Grand Totals on page 425.

AS 'text'

Enables you to specify a different label. For related information, see Using Headings,
Footings, Titles, and Labels on page 1517.

field1, field2, ...

Denotes a list of specific fields to be subtotaled after the RECOMPUTE or
SUMMARIZE. This list overrides the default, which includes all numeric display fields.

Creating Reports With TIBCO® WebFOCUS Language

 383

Recalculating Values for Subtotal Rows

You can use the asterisk (*) wildcard character instead of a field list to indicate that all
fields, numeric and alphanumeric, should be included on the summary lines. You can
either use the asterisk to display all columns or reference the specific columns, numeric
and alphanumeric, you want to display.

WHEN expression

Specifies the conditional display of subtotals based on a Boolean expression. You
must end the expression with a semicolon.

You may also generate subtotals for the recalculated values with the ON TABLE command. Use
the following syntax:

ON TABLE SUMMARIZE

Example:

Using SUMMARIZE

The following request illustrates the use of SUMMARIZE to recalculate DG_RATIO at the
specified sort break, DEPARTMENT, and for the higher-level sort break, PAY_DATE:

TABLE FILE EMPLOYEE
SUM GROSS DED_AMT AND COMPUTE
DG_RATIO/F4.2=DED_AMT/GROSS;
BY HIGHEST PAY_DATE BY DEPARTMENT
BY BANK_ACCT
WHERE BANK_ACCT NE 0
ON DEPARTMENT SUMMARIZE
END

The first portion of the output is:

PAY_DATE  DEPARTMENT  BANK_ACCT          GROSS          DED_AMT  DG_RATIO
--------  ----------  ---------          -----          -------  --------
82/08/31  MIS          40950036      $1,540.00          $725.34       .47
                      122850108      $1,815.00        $1,261.40       .69
                      163800144      $2,255.00        $1,668.69       .74

*TOTAL DEPARTMENT MIS                $5,610.00        $3,655.43       .65

          PRODUCTION     160633      $2,475.00        $1,427.24       .58
                      136500120      $1,342.00          $522.28       .39
                      819000702      $2,238.50        $1,746.03       .78

*TOTAL DEPARTMENT PRODUCTION         $6,055.50        $3,695.55       .61
*TOTAL PAY_DATE 82/08/31            $11,665.50        $7,350.98       .63

384

6. Including Totals and Subtotals

The last portion of the output is:

PAY_DATE  DEPARTMENT  BANK_ACCT          GROSS          DED_AMT  DG_RATIO
--------  ----------  ---------          -----          -------  --------
82/01/29  PRODUCTION  819000702      $2,035.00        $1,241.33       .61

*TOTAL DEPARTMENT PRODUCTION         $2,035.00        $1,241.33       .61
*TOTAL PAY_DATE 82/01/29             $4,182.75        $2,648.12       .63

81/12/31  MIS         163800144      $2,147.75        $1,406.79       .66

*TOTAL DEPARTMENT MIS                $2,147.75        $1,406.79       .66
*TOTAL PAY_DATE 81/12/31             $2,147.75        $1,406.79       .66

81/11/30  MIS         163800144      $2,147.75        $1,406.79       .66

*TOTAL DEPARTMENT MIS                $2,147.75        $1,406.79       .66
*TOTAL PAY_DATE 81/11/30             $2,147.75        $1,406.79       .66

TOTAL                               $65,887.25       $41,521.18       .63

Tip: If you use SUB-TOTAL or SUBTOTAL rather than SUMMARIZE, the values of DG_RATIO are
added.

Example:

Using RECOMPUTE

The following request illustrates the use of RECOMPUTE to recalculate DG_RATIO only at the
specified sort break, DEPARTMENT.

TABLE FILE EMPLOYEE
SUM GROSS DED_AMT AND COMPUTE
DG_RATIO/F4.2=DED_AMT/GROSS;
BY HIGHEST PAY_DATE BY DEPARTMENT
BY BANK_ACCT
WHERE BANK_ACCT NE 0
ON DEPARTMENT RECOMPUTE
END

Creating Reports With TIBCO® WebFOCUS Language

 385

Summarizing Alphanumeric Columns

The first portion of the output is:

PAY_DATE  DEPARTMENT  BANK_ACCT          GROSS          DED_AMT  DG_RATIO
--------  ----------  ---------          -----          -------  --------
82/08/31  MIS          40950036      $1,540.00          $725.34       .47
                      122850108      $1,815.00        $1,261.40       .69
                      163800144      $2,255.00        $1,668.69       .74

*TOTAL DEPARTMENT MIS                $5,610.00        $3,655.43       .65

          PRODUCTION     160633      $2,475.00        $1,427.24       .58
                      136500120      $1,342.00          $522.28       .39
                      819000702      $2,238.50        $1,746.03       .78

*TOTAL DEPARTMENT PRODUCTION         $6,055.50        $3,695.55       .61

82/07/30  MIS          40950036      $1,540.00          $725.34       .47
                      122850108      $1,815.00        $1,261.40       .69

The last portion of the output is:

PAY_DATE  DEPARTMENT  BANK_ACCT          GROSS          DED_AMT  DG_RATIO
--------  ----------  ---------          -----          -------  --------
82/01/29  MIS         163800144      $2,147.75        $1,406.79       .66

*TOTAL DEPARTMENT MIS                $2,147.75        $1,406.79       .66

          PRODUCTION  819000702      $2,035.00        $1,241.33       .61

*TOTAL DEPARTMENT PRODUCTION         $2,035.00        $1,241.33       .61

81/12/31  MIS         163800144      $2,147.75        $1,406.79       .66

*TOTAL DEPARTMENT MIS                $2,147.75        $1,406.79       .66

81/11/30  MIS         163800144      $2,147.75        $1,406.79       .66

*TOTAL DEPARTMENT MIS                $2,147.75        $1,406.79       .66

TOTAL                               $65,887.25       $41,521.18       .63

Summarizing Alphanumeric Columns

By default, subtotals (using the SUBTOTAL and SUB-TOTAL commands) and recalculations
(using the RECOMPUTE and SUMMARIZE commands) only display values for numeric report
columns. However, you can include alphanumeric columns on these summary lines by either
specifying the columns you want to display on the summary lines or by using the asterisk
wildcard character to display all fields on the summary lines.

386

6. Including Totals and Subtotals

The alphanumeric value displayed on a SUBTOTAL or SUB-TOTAL line is either the first,
minimum, maximum, or last alphanumeric value within the sort group, depending on the value
of the SUMPREFIX parameter. On a RECOMPUTE or SUMMARIZE line, alphanumeric values are
recalculated using the summary values for that line.

Syntax:

How to Include All Columns on Summary Lines

ON sortfield summarycommand *

where:

sortfield

Is the sort field for which a change in value triggers the summary line.

summarycommand

Is SUBTOTAL, SUB-TOTAL, RECOMPUTE, or SUMMARIZE.

*

Indicates that all fields, numeric and alphanumeric, should be included on the
summary lines. You can either use the asterisk to display all columns or reference the
specific columns you want to display.

Example:

Including Alphanumeric Fields on Summary Lines

The following request against the GGSALES data source computes the alphanumeric
equivalents of the DOLLARS and UNITS fields, creates an alphanumeric version of the formula
for the ratio between DOLLARS and UNITS, and computes the numeric ratio between DOLLARS
and UNITS. The RECOMPUTE * command recomputes all values on a change of value for the
state sort field:

SET SUMPREFIX=FST
TABLE FILE GGSALES
SUM PRODUCT DOLLARS/I8M AS 'Dollars' IN 22 UNITS AS 'Units'
COMPUTE Formula/A19 = EDIT(DOLLARS)|'/'|EDIT(UNITS)|'=';
COMPUTE Ratio/F8    = DOLLARS/UNITS;
BY ST
BY CATEGORY NOPRINT
WHERE ST EQ 'CA' OR 'IL'
ON ST RECOMPUTE *
ON TABLE SET PAGE NOPAGE
END

Creating Reports With TIBCO® WebFOCUS Language

 387

Manipulating Summary Values With Prefix Operators

On the output, the alphanumeric formula is recomputed using the summed numeric fields.
However, the product value is taken from the first product within each sort value, as that field
is not recomputed and SUMPREFIX=FST:

State  Product           Dollars     Units  Formula                 Ratio
-----  -------           -------     -----  -------                 -----
CA     Capuccino      $2,957,852    237246  02957852/00237246=         12
       Biscotti       $2,770,508    222844  02770508/00222844=         12
       Coffee Grinder $1,935,863    152276  01935863/00152276=         13

*TOTAL CA
       Capuccino      $7,664,223    612366  07664223/00612366=         13

IL     Espresso       $1,398,779    109581  01398779/00109581=         13
       Biscotti       $1,561,904    120976  01561904/00120976=         13
       Coffee Grinder $1,050,243     83541  01050243/00083541=         13

*TOTAL IL
       Espresso       $4,010,926    314098  04010926/00314098=         13

TOTAL  Capuccino     $11,675,149    926464  11675149/00926464=         13

Note that if the SUBTOTAL summary command had been used, the formula would not have
been recomputed and would have displayed the values from the first line within each sort
group.

Reference: Usage Notes for Summarizing Alphanumeric Columns

Date fields and numeric and alphanumeric fields with date formatting options are not
included on summary lines.

Column total lines follow the same rules as summary lines.

Summary values for ACROSS sort fields are supported.

Manipulating Summary Values With Prefix Operators

You can use the SUBTOTAL, SUB-TOTAL, RECOMPUTE, and SUMMARIZE commands at the ON
TABLE level to specify the type of summary operation to use to produce the grand total line on
the report.

In addition, prefix operators can be used with the summary options SUBTOTAL, SUB-TOTAL,
RECOMPUTE, and SUMMARIZE at both the sort break and grand total levels. If the same field
was aggregated using multiple prefix operators in the SUM command, you can use the prefix
operator along with the field name to differentiate between the fields with multiple operators in
the summary command.

388

6. Including Totals and Subtotals

Prefix operations on summary lines are performed on the retrieved, selected, and summed
values that become the detail lines in the report. Unlike field-based prefix operations, they are
not performed on each incoming record.

Each type of summary has its own purpose, and handles the prefix operators appropriately for
the type of summary information to be displayed. For example, using AVE. at a sort field break
produces the average within the sort group.

Alphanumeric fields can also be displayed on summary lines. In order to do this, you must
either explicitly list the alphanumeric field name on the summary command, or use the
asterisk (*) wildcard to display all fields.

Different operations from two ON phrases for the same sort break display on the same
summary line, and allow a mixture of operations on summary lines. The grand total line
populates all fields populated by any summary command, even fields that are not specified in
the grand total command.

If the same field is referenced in more than one ON phrase for the same sort break, the last
function specified is applied.

The following prefix operators are supported for numeric fields:

ASQ.

AVE.

CNT.

FST.

LST.

MAX.

MIN.

SUM.

The following prefix operators are supported for alphanumeric fields:

FST.

LST.

MAX.

MIN.

Creating Reports With TIBCO® WebFOCUS Language

 389

Manipulating Summary Values With Prefix Operators

SUM. (means LST. if SUMPREFIX=LST or FST. if SUMPREFIX=FST)

Syntax:

How to Use Prefix Operators With Summary Values

{BY|ON} breakfield [AS 'text1'] sumoption [MULTILINES]
        [pref. ] [*|[field1 [[pref2. ] field2 ...]]]
        [AS 'text2'] [WHEN expression;]

To replace the default grand total, use the following syntax

ON TABLE sumoption [pref. ][field1 [[pref2. ]field2 ...]] [AS 'text2']

where:

breakfield

Is the sort field whose change in value triggers the summary operation. A BY phrase
can include a summary command. When the value of the sort field changes, it triggers
the summary operation.

sumoption

Can be one of the following: SUBTOTAL, SUB-TOTAL, RECOMPUTE, or SUMMARIZE.

'text1'

Is the column heading to use for the break field on the report output.

MULTILINES

Suppresses the printing of a summary line for every sort break that has only one detail
line. Note that MULTILINES suppresses the summary line even if a prefix operator is
used to specify a different operation for the summary line. MULTI-LINES is a synonym
for MULTILINES. MULTILINES is not supported with horizontal (ACROSS) sort fields.

pref.

Is a prefix operator. When specified without a field list, the prefix operator is applied
to every numeric column in the report output and every numeric column is populated
with values on the summary row.

*

Includes all display fields on the summary line. If a prefix operator is specified, it is
applied to all fields. If the prefix operator is not supported with alphanumeric fields,
alphanumeric fields are not included on the summary line.

[field1 [field2 ... fieldn]]

Produces the type of summary specified by sumoption for the listed fields. If no field
names are listed, the summary is produced for every numeric column in the report
output.

pref. field1 [field2 ... fieldn] [pref2. fieldm ...]

The first prefix operator is applied to field1 through fieldn. The second prefix operator
is applied to fieldm. Only the fields specified are populated with values on the

390

summary row. Each prefix operator must be separated by a blank space from the
following field name. For example:

6. Including Totals and Subtotals

'text2'

Is the text that prints on the left of the summary row.

expression

Is an expression that determines whether the summary operation is performed at
each break.

Reference: Usage Notes for Summary Prefix Operators

COLUMN-TOTAL does not support prefix operators.

Prefix operators PCT., RPCT., AND TOT. are not supported.

Double prefix operators (such as PCT.CNT.) are not supported.

When an ACROSS field is used in the request, the same field name displays over multiple
columns (ACROSS groups) in the report output. A prefix operator applied to such a field on
a summary line is applied to all of those columns.

The SUM. prefix operator produces the same summary values as a summary phrase with
no prefix operator.

SUMMARIZE and RECOMPUTE apply the calculations defined in the associated COMPUTE
command to the summary values. Therefore, in order to perform the necessary
calculations, the SUMMARIZE or RECOMPUTE command must calculate all of the fields
referenced in the COMPUTE command.

If the same field is referenced by more than one summary operation with different prefix
operators at each level, the default grand total (one produced without an ON TABLE
summaryoption command) applies the operation specified by the first operator used in the
report request (the left-most sort field in the output).

Example:

Using Prefix Operators With SUBTOTAL

The following example uses prefix operators to calculate the:

Average list price by rating.

Sum copies by category within the rating field.

Creating Reports With TIBCO® WebFOCUS Language

 391

Manipulating Summary Values With Prefix Operators

Notice that the subtotal row for each rating contains a value only in the LISTPR column, and
the subtotal row for each category contains a value only in the COPIES column. The grand total
line contains values only for the columns that were subtotaled. Note the blank space between
each prefix operator and the field name that follows it:

TABLE FILE MOVIES
PRINT COPIES LISTPR WHOLESALEPR TITLE/A23
  BY RATING
  BY CATEGORY
  WHERE CATEGORY EQ 'CHILDREN' OR 'CLASSIC'
  WHERE RATING   EQ 'G' OR 'NR'
  ON RATING    SUBTOTAL AVE. LISTPR AS '*Ave:  '
  ON CATEGORY  SUBTOTAL SUM. COPIES AS '*Sum:  '
END

The output is:

RATING  CATEGORY  COPIES  LISTPR  WHOLESALEPR  TITLE
------  --------  ------  ------  -----------  -----
G       CHILDREN       2   44.95        29.99  SHAGGY DOG, THE
                       2   29.95        12.50  ALICE IN WONDERLAND
                       3   26.99        12.00  BAMBI

*Sum:   CHILDREN       7

        CLASSIC        3   89.95        40.99  GONE WITH THE WIND

*Sum:   CLASSIC        3
*Ave:   G                  47.96

NR      CHILDREN       1   19.95        10.00  SMURFS, THE
                       1   19.95         9.75  SCOOBY-DOO-A DOG IN THE
                       1   14.95         7.65  SESAME STREET-BEDTIME S
                       1   14.98         7.99  ROMPER ROOM-ASK MISS MO
                       1   29.95        15.99  SLEEPING BEAUTY

*Sum:   CHILDREN       5

        CLASSIC        1   24.98        14.99  EAST OF EDEN
                       3   39.99        20.00  CITIZEN KANE
                       1   29.95        15.99  CYRANO DE BERGERAC
                       1   19.99        10.95  MARTY
                       2   19.99        10.95  MALTESE FALCON, THE
                       2   19.95         9.99  ON THE WATERFRONT
                       2   89.99        40.99  MUTINY ON THE BOUNTY
                       2   19.99        10.95  PHILADELPHIA STORY, THE
                       2   19.98        10.99  CAT ON A HOT TIN ROOF
                       2   29.95        15.00  CASABLANCA

*Sum:   CLASSIC       18
*Ave:   NR                 27.64

TOTAL                 33   31.91

392

6. Including Totals and Subtotals

Example:

Using SUBTOTAL at the Sort Break and Grand Total Levels

The following example adds the ON TABLE SUBTOTAL command to the request in the previous
example (Using Prefix Operators With SUBTOTAL on page 391) at the sort break level to
calculate the minimum number of copies and maximum list price on the grand total line for the
entire report:

TABLE FILE MOVIES
PRINT COPIES LISTPR WHOLESALEPR TITLE/A23
  BY RATING
  BY CATEGORY
  WHERE CATEGORY EQ 'CHILDREN' OR 'CLASSIC'
  WHERE RATING   EQ 'G' OR 'NR'
  ON RATING    SUBTOTAL AVE. LISTPR AS '*Ave:  '
  ON CATEGORY  SUBTOTAL SUM. COPIES AS '*Sum:  '
  ON TABLE SUBTOTAL MIN. COPIES MAX. LISTPR
END

Creating Reports With TIBCO® WebFOCUS Language

 393

Manipulating Summary Values With Prefix Operators

The output is exactly the same as in the previous request, except for the grand total line:

RATING  CATEGORY  COPIES  LISTPR  WHOLESALEPR  TITLE
------  --------  ------  ------  -----------  -----
G       CHILDREN       2   44.95        29.99  SHAGGY DOG, THE
                       2   29.95        12.50  ALICE IN WONDERLAND
                       3   26.99        12.00  BAMBI

*Sum:   CHILDREN       7

        CLASSIC        3   89.95        40.99  GONE WITH THE WIND

*Sum:   CLASSIC        3
*Ave:   G                  47.96

NR      CHILDREN       1   19.95        10.00  SMURFS, THE
                       1   19.95         9.75  SCOOBY-DOO-A DOG IN THE
                       1   14.95         7.65  SESAME STREET-BEDTIME S
                       1   14.98         7.99  ROMPER ROOM-ASK MISS MO
                       1   29.95        15.99  SLEEPING BEAUTY

*Sum:   CHILDREN       5

        CLASSIC        1   24.98        14.99  EAST OF EDEN
                       3   39.99        20.00  CITIZEN KANE
                       1   29.95        15.99  CYRANO DE BERGERAC
                       1   19.99        10.95  MARTY
                       2   19.99        10.95  MALTESE FALCON, THE
                       2   19.95         9.99  ON THE WATERFRONT
                       2   89.99        40.99  MUTINY ON THE BOUNTY
                       2   19.99        10.95  PHILADELPHIA STORY, THE
                       2   19.98        10.99  CAT ON A HOT TIN ROOF
                       2   29.95        15.00  CASABLANCA

*Sum:   CLASSIC       18
*Ave:   NR                 27.64

TOTAL                  1   89.99

Example:

Differentiating Between Fields With Multiple Prefix Operators

The following request uses both the MAX. and MIN. prefix operators with the UNITS field. On
the summary commands, these are differentiated by referencing them as MAX.UNITS and
MIN.UNITS.

TABLE FILE GGSALES
   SUM MAX.UNITS MIN.UNITS
     BY REGION
   BY ST
   ON REGION RECOMPUTE MAX.  MAX.UNITS MIN. MIN.UNITS
   WHERE DATE GE 19971001
   WHERE REGION EQ 'West' OR 'Northeast'
   ON TABLE RECOMPUTE MIN. MAX.UNITS MAX. MIN.UNITS
   ON TABLE SET PAGE NOPAGE
   END

394

6. Including Totals and Subtotals

On the report output, the summary for each region displays the maximum of the state
maximum values and the minimum of the state minimum values. The summary for the entire
report displays the minimum of the state maximum values and the maximum of the state
minimum values. The report output is shown in the following image:

Example:

Displaying an Alphanumeric Field on a Summary Line

The following request displays the sum of the list price field and the minimum value of the
director field by rating:

TABLE FILE MOVIES
PRINT COPIES LISTPR WHOLESALEPR DIRECTOR
BY RATING
BY CATEGORY
WHERE CATEGORY EQ 'CHILDREN' OR 'CLASSIC'
WHERE RATING   EQ 'G' OR 'NR'
WHERE DIRECTOR NE ' '
ON RATING SUBTOTAL SUM. LISTPR MIN. DIRECTOR AS '*A/N:'
END

Creating Reports With TIBCO® WebFOCUS Language

 395

Manipulating Summary Values With Prefix Operators

The output is:

RATING  CATEGORY  COPIES  LISTPR  WHOLESALEPR  DIRECTOR
------  --------  ------  ------  -----------  --------
G       CHILDREN       2   44.95        29.99  BARTON C.
                       2   29.95        12.50  GEROMINI
                       3   26.99        12.00  DISNEY W.
        CLASSIC        3   89.95        40.99  FLEMING V

*A/N: G                   191.84               BARTON C.

NR      CHILDREN       1   29.95        15.99  DISNEY W.
        CLASSIC        1   24.98        14.99  KAZAN E.
                       3   39.99        20.00  WELLES O.
                       1   29.95        15.99  GORDON M.
                       1   19.99        10.95  MANN D.
                       2   19.99        10.95  HUSTON J.
                       2   19.95         9.99  KAZAN E.
                       2   89.99        40.99  MILESTONE L.
                       2   19.99        10.95  CUKOR G.
                       2   19.98        10.99  BROOKS R.
                       2   29.95        15.00  CURTIZ M.

*A/N: NR                  344.71               BROOKS R.

TOTAL                     536.55               BARTON C.

Example:

Displaying All Fields on a Summary Line

The following request displays the sum of every display field on the subtotal line. The director
field is alphanumeric, so the last value displays:

TABLE FILE MOVIES
PRINT COPIES LISTPR WHOLESALEPR DIRECTOR
BY RATING
BY CATEGORY
WHERE CATEGORY EQ 'CHILDREN' OR 'CLASSIC'
WHERE RATING   EQ 'G' OR 'NR'
WHERE DIRECTOR NE ' '
ON RATING SUBTOTAL SUM. * AS '*All:  '
END

396

6. Including Totals and Subtotals

The output is:

RATING  CATEGORY  COPIES  LISTPR  WHOLESALEPR  DIRECTOR
------  --------  ------  ------  -----------  --------
G       CHILDREN       2   44.95        29.99  BARTON C.
                       2   29.95        12.50  GEROMINI
                       3   26.99        12.00  DISNEY W.
        CLASSIC        3   89.95        40.99  FLEMING V

*All:   G             10  191.84        95.48  FLEMING V

NR      CHILDREN       1   29.95        15.99  DISNEY W.
        CLASSIC        1   24.98        14.99  KAZAN E.
                       3   39.99        20.00  WELLES O.
                       1   29.95        15.99  GORDON M.
                       1   19.99        10.95  MANN D.
                       2   19.99        10.95  HUSTON J.
                       2   19.95         9.99  KAZAN E.
                       2   89.99        40.99  MILESTONE L.
                       2   19.99        10.95  CUKOR G.
                       2   19.98        10.99  BROOKS R.
                       2   29.95        15.00  CURTIZ M.

*All:   NR            19  344.71       176.79  CURTIZ M.

TOTAL                 29  536.55       272.27  CURTIZ M.

Controlling Summary Line Processing

When processing summary lines, you can control whether SUBTOTAL and RECOMPUTE
commands are propagated to the grand total row of a report.

If the summary line contains fields with and without prefix operators, those fields without prefix
operators are processed as though they were specified with the operator SUM.

The function of the SET SUMMARYLINES command is to make the processing of SUBTOTAL,
SUB-TOTAL, SUMMARIZE, and RECOMPUTE on the grand total line consistent with how they
work for sort field breaks. The setting that invokes this type of processing is SET
SUMMARYLINES=EXPLICIT.

When SUBTOTAL and RECOMPUTE are used at a sort break level, they do not propagate to
other sort breaks. SUB-TOTAL and SUMMARIZE propagate to all higher level sort breaks.

The grand total can be considered the highest level sort field in a request. However, by default,
all of the summary options, not just SUB-TOTAL and SUMMARIZE, propagate to the grand total
level.

The SET SUMMARYLINES=EXPLICIT command prevents the propagation of SUBTOTAL and
RECOMPUTE to the grand total. In addition, if all summary commands in the request specify
field lists, only the specified fields are aggregated and displayed on the grand total line.

Creating Reports With TIBCO® WebFOCUS Language

 397

Manipulating Summary Values With Prefix Operators

When SUBTOTAL and RECOMPUTE are the only summary commands used in the request, a
grand total line is produced only if it is explicitly specified in the request using the ON TABLE
SUBTOTAL/SUB-TOTAL/RECOMPUTE/SUMMARIZE phrase. If the ON TABLE phrase specifies a
field list, only those fields are aggregated and displayed.

Note that you can always suppress the grand total line using the ON TABLE NOTOTAL
command in the request.

Syntax:

How to Control Summary Line Processing

SET SUMMARYLINES = {NEW|OLD|EXPLICIT}

where:

NEW

Propagates all summary operations to the grand total line. Fields listed in a summary
command are populated only on summary lines created by that summary command and on
summary lines created by propagation of that summary command. NEW is the default
value.

The alphanumeric value displayed on a SUBTOTAL or SUB-TOTAL line is either the first or
last alphanumeric value within the sort group, depending on the value of the SUMPREFIX
parameter. On a RECOMPUTE or SUMMARIZE line, alphanumeric values are recalculated
using the summary values for that line.

OLD

This value is no longer supported and is processed as NEW.

EXPLICIT

Does not propagate SUBTOTAL and RECOMPUTE to the grand total line. Fields listed
in a summary command are populated only on summary lines created by that
summary command and on summary lines created by propagation of that summary
command.

Note: This command is not supported in a request using the ON TABLE SET syntax.

Reference: Usage Notes for SET SUMMARYLINES

SET SUMMARYLINES is not supported within a TABLE request (ON TABLE).

If COLUMN-TOTAL is specified in the request, all numeric fields are totaled on the grand
total line unless the COLUMN-TOTAL phrase lists specific fields. If the COLUMN-TOTAL
phrase lists specific fields, those fields and any fields propagated by SUB-TOTAL or
SUMMARIZE commands are totaled.

398

6. Including Totals and Subtotals

A summary command with a list of field names populates only those columns on the
associated summary line.

For example:

TABLE FILE MOVIES
PRINT COPIES LISTPR WHOLESALEPR
 BY RATING
 BY CATEGORY
 WHERE CATEGORY EQ 'CHILDREN'
 WHERE RATING   EQ 'G'
 ON RATING    SUBTOTAL LISTPR AS '*LIST'
 ON CATEGORY  SUBTOTAL  COPIES AS '*COPY'
END

The output has subtotals for COPIES on the CATEGORY sort break and for LISTPR on the
RATING sort break. Both columns are populated on the grand total line. WHOLESALEPR is not
referenced in either SUBTOTAL command and, therefore, is not on any summary line:

RATING  CATEGORY  COPIES  LISTPR  WHOLESALEPR
------  --------  ------  ------  -----------
G       CHILDREN       2   44.95        29.99
                       2   29.95        12.50
                       3   26.99        12.00

*COPY CHILDREN         7
*LIST G                   101.89

TOTAL                  7  101.89

Example:

Using SET SUMMARYLINES With SUBTOTAL

The following request using the MOVIES data source has a sort break for CATEGORY that
subtotals the COPIES field and a sort break for RATING that subtotals the LISTPR field:

TABLE FILE MOVIES
SUM COPIES LISTPR WHOLESALEPR
BY RATING
BY CATEGORY
WHERE CATEGORY EQ 'CHILDREN'
WHERE RATING   EQ 'G'
ON RATING SUBTOTAL COPIES
ON CATEGORY SUBTOTAL LISTPR
END

Creating Reports With TIBCO® WebFOCUS Language

 399

Manipulating Summary Values With Prefix Operators

Running the request with SUMMARYLINES=NEW subtotals COPIES only for the RATING sort
break and subtotals LISTPR only for the CATEGORY sort break but propagates both to the
grand total line:

RATING  CATEGORY  COPIES  LISTPR  WHOLESALEPR
------  --------  ------  ------  -----------
G       CHILDREN       7  101.89        54.49

*TOTAL CHILDREN           101.89
*TOTAL G               7

TOTAL                  7  101.89

Running the request with SUMMARYLINES=EXPLICIT subtotals COPIES only for the RATING sort
break and subtotals LISTPR only for the CATEGORY sort break. It does not produce a grand
total line:

RATING  CATEGORY  COPIES  LISTPR  WHOLESALEPR
------  --------  ------  ------  -----------
G       CHILDREN       7  101.89        54.49

*TOTAL CHILDREN           101.89
*TOTAL G               7

Adding the phrase ON TABLE SUBTOTAL WHOLESALEPR with SUMMARYLINES=EXPLICIT
produces a grand total line with the WHOLESALEPR field subtotaled:

RATING  CATEGORY  COPIES  LISTPR  WHOLESALEPR
------  --------  ------  ------  -----------
G       CHILDREN       7  101.89        54.49

*TOTAL CHILDREN           101.89
*TOTAL G               7

TOTAL                                   54.49

400

6. Including Totals and Subtotals

Example:

Using COLUMN-TOTAL With SET SUMMARYLINES=EXPLICIT

The following request using the MOVIES data source has a sort break for CATEGORY for which
subtotals the COPIES field and a sort break for RATING that subtotals the LISTPR field. It also
has an ON TABLE COLUMN-TOTAL phrase:

SET SUMMARYLINES=EXPLICIT
TABLE FILE MOVIES
SUM COPIES LISTPR WHOLESALEPR
BY RATING
BY CATEGORY
WHERE CATEGORY EQ 'CHILDREN'
WHERE RATING   EQ 'G'
ON RATING SUBTOTAL COPIES
ON CATEGORY SUBTOTAL LISTPR
ON TABLE COLUMN-TOTAL
END

The grand total line displays a column total for all numeric columns because of the ON TABLE
COLUMN-TOTAL phrase:

RATING  CATEGORY  COPIES  LISTPR  WHOLESALEPR
------  --------  ------  ------  -----------
G       CHILDREN       7  101.89        54.49

*TOTAL CHILDREN           101.89
*TOTAL G               7

TOTAL                  7  101.89        54.49

The following request has an ON TABLE SUBTOTAL WHOLESALEPR command. It also has an
ON TABLE COLUMN-TOTAL phrase:

SET SUMMARYLINES=EXPLICIT
TABLE FILE MOVIES
SUM COPIES LISTPR WHOLESALEPR
BY RATING
BY CATEGORY
WHERE CATEGORY EQ 'CHILDREN'
WHERE RATING   EQ 'G'
ON RATING SUBTOTAL COPIES
ON CATEGORY SUBTOTAL LISTPR
ON TABLE SUBTOTAL WHOLESALEPR
ON TABLE COLUMN-TOTAL
END

Creating Reports With TIBCO® WebFOCUS Language

 401

Manipulating Summary Values With Prefix Operators

The grand total line displays a column total only for the WHOLESALEPR column because of the
ON TABLE SUBTOTAL command:

RATING  CATEGORY  COPIES  LISTPR  WHOLESALEPR
------  --------  ------  ------  -----------
G       CHILDREN       7  101.89        54.49

*TOTAL CHILDREN           101.89
*TOTAL G               7

TOTAL                                   54.49

Using SUB-TOTAL instead of SUBTOTAL causes COPIES and LISTPR to be aggregated on the
grand total line. WHOLESALEPR is totaled because it is listed in the COLUMN-TOTAL phrase.
The subtotal for LISTPR propagates to the RATING sort break as well as to the grand total:

SET SUMMARYLINES=EXPLICIT
TABLE FILE MOVIES
SUM COPIES LISTPR WHOLESALEPR
BY RATING
BY CATEGORY
WHERE CATEGORY EQ 'CHILDREN'
WHERE RATING   EQ 'G'
ON RATING SUB-TOTAL COPIES
ON CATEGORY SUB-TOTAL LISTPR
ON TABLE COLUMN-TOTAL WHOLESALEPR
END

The output is:

RATING  CATEGORY  COPIES  LISTPR  WHOLESALEPR
------  --------  ------  ------  -----------
G       CHILDREN       7  101.89        54.49

*TOTAL CHILDREN           101.89
*TOTAL G               7  101.89

TOTAL                  7  101.89        54.49

Using Prefix Operators With Calculated Values

If a request includes the RECOMPUTE or SUMMARIZE command, the expression specified in
the associated COMPUTE command is applied using values from the summary line. The
columns used to recompute the expression can have prefix operators. The recomputed
column, regardless of the prefix operator specified for it, applies these input values to the
expression specified in the COMPUTE command. Therefore, any supported prefix operator can
be specified for the recomputed report column without affecting the calculated value.

402

6. Including Totals and Subtotals

All fields used in the COMPUTE command must be displayed by the RECOMPUTE or
SUMMARIZE command in order to be populated. If any field used in the expression is not
populated, the calculated value returned for the expression is unpredictable.

Example:

Using Prefix Operators With RECOMPUTE

The first request creates a calculated field named DIFF, which is the difference between
DOLLARS and BUDDOLLARS. This value is then recomputed for each region, without using
prefix operators.

TABLE FILE GGSALES
SUM UNITS DOLLARS BUDDOLLARS
AND COMPUTE DIFF/I10 = DOLLARS-BUDDOLLARS;
  BY REGION
  BY CATEGORY
  WHERE CATEGORY EQ 'Food' OR 'Coffee'
  WHERE REGION EQ 'West' OR 'Midwest'
  ON REGION  RECOMPUTE
END

The recomputed value is the difference between the totals for DOLLARS and BUDDOLLARS.

Region      Category    Unit Sales Dollar Sales Budget Dollars       DIFF
------      --------    ---------- ------------ --------------       ----
Midwest     Coffee          332777      4178513        4086032      92481
            Food            341414      4338271        4220721     117550

*TOTAL Midwest              674191      8516784        8306753     210031

West        Coffee          356763      4473517        4523963     -50446
            Food            340234      4202337        4183244      19093

*TOTAL West                 696997      8675854        8707207     -31353

TOTAL                      1371188     17192638       17013960     178678

Creating Reports With TIBCO® WebFOCUS Language

 403

Manipulating Summary Values With Prefix Operators

The following request uses prefix operators in the RECOMPUTE command to calculate the
maximum DOLLARS and the minimum BUDDOLLARS and then recompute DIFF. No matter
which prefix operator we specify for DIFF, it is calculated as the difference between the values
in the DOLLARS and BUDDOLLARS columns. If any of the fields used in the calculation
(DOLLARS, BUDDOLLARS, and DIFF) do not display on the summary row, the calculation cannot
be performed.

TABLE FILE GGSALES
SUM UNITS DOLLARS BUDDOLLARS
AND COMPUTE DIFF/I10 = DOLLARS-BUDDOLLARS;
  BY REGION
  BY CATEGORY
  WHERE CATEGORY EQ 'Food' OR 'Coffee'
  WHERE REGION EQ 'West' OR 'Midwest'
  ON REGION RECOMPUTE MAX. DOLLARS MIN. BUDDOLLARS AVE. DIFF
END

The output is:

Region      Category    Unit Sales Dollar Sales Budget Dollars       DIFF
------      --------    ---------- ------------ --------------       ----
Midwest     Coffee          332777      4178513        4086032      92481
            Food            341414      4338271        4220721     117550

*TOTAL Midwest                          4338271        4086032     252239

West        Coffee          356763      4473517        4523963     -50446
            Food            340234      4202337        4183244      19093

*TOTAL West                             4473517        4183244     290273

Example:

Using RECOMPUTE at the Sort Break and Grand Total Levels

The following example adds the ON TABLE RECOMPUTE command to the previous request
(Using Prefix Operators With RECOMPUTE on page 403) to calculate the average values for
each column. Notice that the value of DIFF is calculated as the difference between the values
in the Dollar Sales and the Budget Dollars columns on the grand total line:

TABLE FILE GGSALES
SUM UNITS DOLLARS BUDDOLLARS
AND COMPUTE DIFF/I10 = DOLLARS-BUDDOLLARS;
  BY REGION
  BY CATEGORY
  WHERE CATEGORY EQ 'Food' OR 'Coffee'
  WHERE REGION EQ 'West' OR 'Midwest'
  ON REGION  RECOMPUTE MAX. DOLLARS MIN. BUDDOLLARS DIFF
 ON TABLE RECOMPUTE AVE.
END

404

6. Including Totals and Subtotals

The output is:

Region      Category    Unit Sales Dollar Sales Budget Dollars       DIFF
------      --------    ---------- ------------ --------------       ----
Midwest     Coffee          332777      4178513        4086032      92481
            Food            341414      4338271        4220721     117550

*TOTAL Midwest                          4338271        4086032     252239

West        Coffee          356763      4473527        4523963     -50436
            Food            340234      4202338        4183244      19094

*TOTAL West                             4473527        4183244     290283

TOTAL                       342797      4298162        4253490      44672

Using Multiple SUB-TOTAL or SUMMARIZE Commands With Prefix Operators

SUB-TOTAL and SUMMARIZE propagate their operations to all higher-level sort fields. If a
request uses SUB-TOTAL or SUMMARIZE at multiple sort levels, more than one prefix operator
may apply to the same field.

When a SUB-TOTAL or SUMMARIZE command on a lower-level sort field propagates up to the
higher levels, it applies its prefix operators only to those fields that did not already have
different prefix operators specified at the higher level. For any field that had a prefix operator
specified at a higher level, the original prefix operator is applied at the level at which it was
first specified and to the grand total line, unless a different operator is specified for the grand
total line.

Example:

Using Multiple SUB-TOTAL Commands With Prefix Operators

The following illustrates prefix operators work in a request that has multiple SUB-TOTAL
commands, each with a different prefix operator.

DEFINE FILE GGSALES
YEAR/YY = DATE;
END

TABLE FILE GGSALES
SUM   UNITS DOLLARS/D10.2 BUDDOLLARS
  BY YEAR
  BY ST
  BY REGION
  BY CATEGORY
WHERE REGION EQ 'West' OR 'Midwest'
WHERE ST     EQ 'CA' OR 'IL'
WHERE YEAR EQ '1996' OR '1997'
  ON YEAR SUB-TOTAL CNT. UNITS AS '*CNT. UNITS:'
  ON ST SUB-TOTAL AVE. DOLLARS AS '*AVE. $:'
  ON REGION SUB-TOTAL MIN. AS '*MIN.:'
END

Creating Reports With TIBCO® WebFOCUS Language

 405


Manipulating Summary Values With Prefix Operators

In the following report output, some of the values have been manually italicized or bolded for
clarity:

Outlined rows are the rows generated by the SUB-TOTAL commands.

Subtotal values in the normal typeface are the count of unit sales generated by the
command ON YEAR SUB-TOTAL CNT. UNITS. This is the topmost summary command, and
therefore does not propagate to any other summary lines.

Subtotal values in italic are average dollar sales generated by the command ON ST SUB-
TOTAL AVE. DOLLARS. This is the second summary command, and therefore propagates to
the DOLLARS column of summary lines for the YEAR sort field.

406

6. Including Totals and Subtotals

Subtotal values in boldface are minimums within their sort groups generated by the
command ON REGION SUB-TOTAL MIN. This is the last summary command, and therefore
propagates to all other summary lines, but only calculates minimum values for those
columns not already populated with a count or an average.

Combinations of Summary Commands

You can specify a different summary operation for each sort break (BY or ACROSS field).

Creating Reports With TIBCO® WebFOCUS Language

 407

Combinations of Summary Commands

If you have multiple summary commands for the same sort field, the following message
displays and the last summary command specified in the request is used:

(FOC36359)  MORE THAN 1 SUBTOTAL/SUB-TOTAL/RECOMPUTE/SUMMARIZE

There is more than one SUBTOTAL/SUB-TOTAL/RECOMPUTE/SUMMARIZE
on the same key field which is not allowed. The last one specified will
override the rest.

SUMMARIZE and SUB-TOTAL, which propagate their summary operations to higher level sort
breaks, skip those fields at higher level sort breaks that have their own summary commands.
The propagation of summary operations depends on whether prefix operator processing is
used for summary lines. If prefix operators are:

Not used on summary lines, if any summary command specifies a field list, only the fields
specified on the summary line field lists are populated on the report.

Used on summary lines, SUB-TOTAL and SUMMARIZE propagate to:

All fields at higher level sort breaks that do not have their own summary command.

Fields not specified in the field list at higher level sort breaks that do have their own
summary commands (columns that would have been empty). Note that this is the only
technique that allows different fields at the same sort break to have different summary
options.

Prefix operators on summary lines result in the same values whether the command is
RECOMPUTE/SUMMARIZE or SUBTOTAL/SUB-TOTAL. For a computed field, the prefix operator
is not applied, and the value is recalculated using the expression in the COMPUTE command
and the values from the summary line.

When you use different summary commands for different sort fields, the default grand total row
inherits the summary command associated with the first sort field in the request. You can
change the operation performed at the grand total level by using the ON TABLE phrase to
specify a specific summary command.

Note: The grand total is considered the highest sort level. Therefore, although you can use the
SUMMARIZE or SUB-TOTAL command at the grand total level, these commands apply only to
the grand total and are not propagated to any other line on the report. On the grand total level
SUMMARIZE operates as a RECOMPUTE command, and SUB-TOTAL operates as a SUBTOTAL
command.

408

6. Including Totals and Subtotals

Example:

Using SUBTOTAL and RECOMPUTE in a Request

In the following request, the first sort field specified is COPIES, which is associated with the
RECOMPUTE command. Therefore, on the grand total line, the value of RATIO is correctly
recomputed and the values of LISTPR and WHOLESALEPR are summed (because this is the
default operation when the field is not calculated by a COMPUTE command).

TABLE FILE MOVIES
PRINT DIRECTOR LISTPR WHOLESALEPR
COMPUTE RATIO = LISTPR/WHOLESALEPR;
BY COPIES
BY RATING
WHERE COPIES LT 3
WHERE DIRECTOR EQ 'DISNEY W.' OR 'HITCHCOCK A.'
ON COPIES RECOMPUTE AS '*REC: '
ON RATING SUBTOTAL AS '*SUB:  '
END

The output is:

COPIES  RATING  DIRECTOR           LISTPR  WHOLESALEPR           RATIO
------  ------  --------           ------  -----------           -----
     1  NR      DISNEY W.           29.95        15.99            1.87

*SUB:   NR                          29.95        15.99            1.87
*REC:    1                          29.95        15.99            1.87

     2  NR      HITCHCOCK A.        19.98         9.00            2.22

*SUB:   NR                          19.98         9.00            2.22

        PG      HITCHCOCK A.        19.98         9.00            2.22
                HITCHCOCK A.        19.98         9.00            2.22

*SUB:   PG                          39.96        18.00            4.44
     2  PG13    HITCHCOCK A.        19.98         9.00            2.22

*SUB:   PG13                        19.98         9.00            2.22

        R       HITCHCOCK A.        19.98         9.00            2.22

*SUB:   R                           19.98         9.00            2.22
*REC:    2                          99.90        45.00            2.22

TOTAL                              129.85        60.99            2.13

If you reverse the BY fields, the grand total line sums the RATIO values as well as the LISTPR
and WHOLESALEPR values because the SUBTOTAL command controls the grand total line:

TOTAL                              129.85        60.99           12.97

Creating Reports With TIBCO® WebFOCUS Language

 409

Combinations of Summary Commands

You can change the operation performed at the grand total level by adding the following
command to the request:

ON TABLE RECOMPUTE

The grand total line then displays the recomputed values:

TOTAL                              129.85        60.99            2.13

Example:

Using SUB-TOTAL With Multiple Summary Commands

In the following request, the SUB-TOTAL command propagates its operation to the DIRECTOR
sort field (see the total line for HITCHCOCK, on which the RATIO values are subtotaled, not
recomputed).

SUB-TOTAL is not propagated to the RATING sort field which has its own RECOMPUTE
command, and for this sort field the RATIO value is recomputed. The grand total line is
recomputed because RECOMPUTE is performed on a higher level sort field than SUB-TOTAL.

TABLE FILE MOVIES
PRINT LISTPR WHOLESALEPR
COMPUTE RATIO = LISTPR/WHOLESALEPR;
BY DIRECTOR
BY RATING
BY COPIES
WHERE COPIES LT 3
WHERE DIRECTOR EQ 'HITCHCOCK A.'
ON COPIES SUB-TOTAL AS '*SUB: '
ON RATING RECOMPUTE AS '*REC:  '
END

410

6. Including Totals and Subtotals

The output is:

DIRECTOR           RATING  COPIES  LISTPR  WHOLESALEPR           RATIO
--------           ------  ------  ------  -----------           -----
HITCHCOCK A.       NR           2   19.98         9.00            2.22

*SUB:    2                          19.98         9.00            2.22
*REC:   NR                          19.98         9.00            2.22

                   PG           2   19.98         9.00            2.22
                                    19.98         9.00            2.22

*SUB:    2                          39.96        18.00            4.44
*REC:   PG                          39.96        18.00            2.22

                   PG13         2   19.98         9.00            2.22
*SUB:    2                          19.98         9.00            2.2
*REC:   PG13                        19.98         9.00            2.2

HITCHCOCK A.       R            2   19.98         9.00            2.2

*SUB:    2                          19.98         9.00            2.2
*REC:   R                           19.98         9.00            2.2
*TOTAL DIRECTOR HITCHCOCK A.        99.90        45.00           11.1

TOTAL                               99.90        45.00            2.2

Example:

Using Multiple Summary Commands With Prefix Operators

The following request prints the average value of LISTPR and the recomputed value of RATIO
on the lines associated with sort field RATING. The SUB-TOTAL command associated with sort
field COPIES is propagated to all fields on the DIRECTOR sort field lines and to the
WHOLESALEPR and RATIO1 columns associated with the RATING sort field. The grand total line
is suppressed for this request.

TABLE FILE MOVIES
PRINT LISTPR WHOLESALEPR
COMPUTE RATIO/D6.2 = LISTPR/WHOLESALEPR;
COMPUTE RATIO1/D6.2 = LISTPR/WHOLESALEPR;
BY DIRECTOR
BY RATING
BY COPIES
WHERE COPIES LT 3
  WHERE DIRECTOR EQ 'KAZAN E.'
  ON RATING  RECOMPUTE  AVE. LISTPR  RATIO AS '*REC:  '
  ON COPIES  SUB-TOTAL                     AS '*SUB:  '
  ON TABLE NOTOTAL
END

Creating Reports With TIBCO® WebFOCUS Language

 411

Combinations of Summary Commands

On the output:

The values of WHOLESALEPR and RATIO1 on the row labeled *REC are subtotals because
of propagation of the SUB-TOTAL command to the fields not specified in the RECOMPUTE
command.

The LISTPR value is an average and the value of RATIO (which has the same definition as
RATIO1) is recomputed because these two fields are specified in the RECOMPUTE
command.

The SUB-TOTAL command is propagated to the DIRECTOR row.

The output is:

DIRECTOR           RATING  COPIES  LISTPR  WHOLESALEPR   RATIO  RATIO1
--------           ------  ------  ------  -----------   -----  ------
KAZAN E.           NR           1   24.98        14.99    1.67    1.67

*SUB:    1                          24.98        14.99    1.67    1.67

                                2   19.95         9.99    2.00    2.00

*SUB:    2                          19.95         9.99    2.00    2.00
*REC:   NR                          22.46        24.98     .90    3.66
*TOTAL DIRECTOR KAZAN E.            44.93        24.98    3.66    3.66

Example:

Propagation of Summary Commands With Field Lists

In the following request, the RECOMPUTE command has a field list.

TABLE FILE MOVIES
PRINT LISTPR WHOLESALEPR
COMPUTE RATIO/D6.2 = LISTPR/WHOLESALEPR;
COMPUTE RATIO1/D6.2 = LISTPR/WHOLESALEPR;
BY DIRECTOR
BY RATING
BY COPIES
WHERE COPIES LT 3
  WHERE DIRECTOR EQ 'KAZAN E.'
  ON RATING RECOMPUTE LISTPR RATIO AS '*REC:  '
  ON COPIES SUB-TOTAL AS '*SUB:  '
END

412

6. Including Totals and Subtotals

SUB-TOTAL propagates to all of the columns that would otherwise be unpopulated. The grand
total line inherits the RECOMPUTE command for the fields listed in its field list, and the SUB-
TOTAL command propagates to the other columns:

DIRECTOR           RATING  COPIES  LISTPR  WHOLESALEPR   RATIO  RATIO1
--------           ------  ------  ------  -----------   -----  ------
KAZAN E.           NR           1   24.98        14.99    1.67    1.67

*SUB:     1                         24.98        14.99    1.67    1.67

                                2   19.95         9.99    2.00    2.00

*SUB:     2                         19.95         9.99    2.00    2.00
*REC:   NR                          44.93        24.98    1.80    3.66
*TOTAL DIRECTOR KAZAN E.            44.93        24.98    3.66    3.66

TOTAL                               44.93        24.98    1.80    3.66

Reference: Usage Notes for Combinations of Summary Commands

SET SUMMARYLINES=EXPLICIT affects propagation of summary commands to the grand
total line by making it consistent with the behavior for any sort break. Therefore, with this
setting in effect, SUB-TOTAL and SUMMARIZE propagate to the grand total line but
SUBTOTAL and RECOMPUTE do not.

Producing Summary Columns for Horizontal Sort Fields

The summary commands SUBTOTAL, SUB-TOTAL, SUMMARIZE, and RECOMPUTE can be used
with horizontal sort breaks.

When a request has multiple display fields and an ACROSS sort field, the report output has
multiple columns under each ACROSS value. If you want to apply a summary field to some of
the columns for each ACROSS value, but not others, you can specify the field names you want
summarized. This technique is most useful for report requests that use the OVER phrase to
place the fields on separate rows

Syntax:

How to Produce a Summary Operation on a Horizontal Sort Field

{ACROSS|ON} acrossfield [AS 'text1'] sumoption [AS 'text2']
             [COLUMNS c1 [AND c2 ...]]

or

ACROSS acrossfieldsumoption [field1field2 ... fieldn]

or

Creating Reports With TIBCO® WebFOCUS Language

 413

Producing Summary Columns for Horizontal Sort Fields

ACROSS acrossfield

ON acrossfieldsumoption [field1field2 ... fieldn]

where:

acrossfield

Is the ACROSS field whose for which you want to generate the summary option. The
end of the values for the ACROSS field triggers the summary operation.

sumoption

Can be one of the following: SUBTOTAL, SUB-TOTAL, RECOMPUTE, or SUMMARIZE.

'text1'

Is the column heading to use for the break field on the report output.

'text2'

Is the text that prints on the top of the summary column.

COLUMNSc1, c2 ...

Lists the specific ACROSS values that you want to display on the report output in the
order in which you want them. This list of values cannot be specified in an ON phrase.
If it is specified in an ACROSS phrase, it must be the last option specified in the
ACROSS phrase.

field1field2 ... fieldn

Are the fields that will have the summary command applied. If no fields are listed, all fields
will be summarized.

Reference: Usage Notes for Summaries on ACROSS Fields

SUMMARIZE and SUB-TOTAL operate on the ACROSS field for which they are specified and
for all higher level ACROSS fields. They do not operate on BY fields. SUBTOTAL and
RECOMPUTE operate only on the ACROSS field for which they are specified. However, the
summary is not produced until the higher level ACROSS field changes value.

SUMMARIZE and SUB-TOTAL commands specified for a BY field operate on that BY and all
higher level BY fields. They do not operate on ACROSS fields.

ROW-TOTAL, ACROSS-TOTAL, SUBTOTAL, and SUB-TOTAL sum the values in the columns.
Unlike SUMMARIZE and RECOMPUTE, they do not reapply calculations other than sums.

Summary commands specified in an ON TABLE phrase operate on columns, not rows.

With ACROSS, summary columns only display at the end of the ACROSS group (when the
higher-level ACROSS field changes value).

414

6. Including Totals and Subtotals

Different operations from two ON phrases for the same sort break display in the same
summary column, and allow a mixture of operations on summary columns.

If the same field is referenced in more than one ON phrase for the same sort break, the
last summary command specified is applied.

You can specify a different summary operation for each sort break.

The SUMMARYLINES parameter does not affect processing for ACROSS fields.

When used with OVERs, the rows containing fields not to be summarized will be blank.

Prefix operators are supported on summary lines:

The following prefix operators are supported for numeric fields: ASQ., AVE., CNT., FST.,
LST., MAX., MIN., SUM.

Prefix operators PCT., RPCT., AND TOT. are not supported.

Double prefix operators (such as PCT.CNT.) are not supported.

The SUM. prefix operator produces the same summary values as a summary phrase
with no prefix operator.

SUMMARIZE and RECOMPUTE apply the calculations defined in the associated
COMPUTE command to the summary values. Therefore, in order to perform the
necessary calculations, the SUMMARIZE or RECOMPUTE command must specify all of
the fields referenced in the COMPUTE command.

If the same field has summary operations with different prefix operators at each level,
the appropriate calculation is done at each level for the prefix operator specified.

SUB-TOTAL and SUMMARIZE propagate their operations to all higher-level sort fields. If
a request uses SUB-TOTAL or SUMMARIZE at multiple sort levels, more than one prefix
operator may apply to the same field. When a SUB-TOTAL or SUMMARIZE command on
a lower-level sort field propagates up to the higher levels, it applies its prefix operators
only to those fields that did not already have a prefix operator specified at the higher
level. For any field that had a prefix operator specified at a higher level, the original
prefix operator is applied at the level at which it was first specified.

Prefix operators on summary lines result in the same values whether the command is
RECOMPUTE/SUMMARIZE or SUBTOTAL/SUB-TOTAL. For a computed field, the prefix
operator is not applied, and the value is recalculated using the expression in the
COMPUTE command and the values from the summary line.

Creating Reports With TIBCO® WebFOCUS Language

 415

Producing Summary Columns for Horizontal Sort Fields

If an ACROSS field has an ACROSS-TOTAL phrase and a summary command with a
prefix operator, the prefix operator is applied, not the ACROSS-TOTAL.

Example:

Using Summary Commands With ACROSS

The following request sums units and dollars and calculates the unit cost by product and
across region and month. The ACROSS MNTH RECOMPUTE command creates totals of units
and dollars, and recomputes the calculated value for the selected months within regions. The
ACROSS REGION RECOMPUTE command does the same for the selected regions. The ON
TABLE SUMMARIZE command creates summary rows. It has no effect on columns:

DEFINE FILE GGSALES
MNTH/MTr   = DATE;
END
TABLE FILE GGSALES
SUM
 UNITS/I5 AS 'UNITS'                   OVER
 DOLLARS/I6 AS 'DOLLARS'               OVER
 COMPUTE DOLLPER/I6 = DOLLARS/UNITS; AS 'UNIT COST'
BY PRODUCT
ACROSS REGION RECOMPUTE AS 'Region Sum' COLUMNS 'Northeast' AND 'West'
ACROSS MNTH   RECOMPUTE AS 'Month Sum' COLUMNS 'November' AND 'December'
WHERE DATE FROM '19971101' TO '19971231';
WHERE PRODUCT EQ 'Capuccino' OR 'Espresso';
ON TABLE SUMMARIZE AS 'Grand Total'

END

416

The output is:

6. Including Totals and Subtotals

Example:

Subtotaling One Field Within an ACROSS Group

The following request against the GGSALES data source sums the DOLLARS and UNITS fields
by CATEGORY and across REGION, but subtotals only the UNITS field.

TABLE FILE GGSALES
SUM DOLLARS AS 'Dollars' OVER
UNITS AS 'Units'
  BY CATEGORY
  ACROSS REGION SUBTOTAL UNITS
WHERE REGION EQ 'Midwest' OR 'West'
ON TABLE SET PAGE NOPAGE
END

Creating Reports With TIBCO® WebFOCUS Language

 417

Producing Summary Columns for Horizontal Sort Fields

The output shows that only the rows with the UNITS values are subtotaled.

                      Region
                      Midwest      West         TOTAL
Category
-------------------------------------------------------------
Coffee       Dollars   4178513      4473517
             Units      332777       356763       689540
Food         Dollars   4338271      4202337
             Units      341414       340234       681648
Gifts        Dollars   2883881      2977092
             Units      230854       235042       465896

Example:

Summarizing a Calculated Value in an ACROSS Group

The following request against the GGSALES data source sums the DOLLARS and UNITS fields
and calculates DOLLARS PER UNIT across REGION. The request also has a higher-level
ACROSS field, CATEGORY, so the SUMMARIZE command propagates to both ACROSS fields.

SET BYPANEL = ON
TABLE FILE GGSALES
SUM DOLLARS AS 'Dollars' OVER
UNITS AS 'Units'         OVER
AND COMPUTE DPERU/D9.2 = DOLLARS/UNITS;
  ACROSS CATEGORY
  ACROSS REGION
  ON REGION SUMMARIZE DPERU
  WHERE REGION EQ 'Midwest' OR 'West'
  WHERE CATEGORY EQ 'Food' OR 'Gifts'
  ON TABLE PCHOLD FORMAT PDF
END

The first panel of output shows:

The values of DOLLARS, UNITS, and DPERU for the Midwest and West regions under the
Food category.

The summary column, which has a value just for the DPERU row. Note that for ACROSS, the
summary column for REGION appears only after the higher-level ACROSS field, CATEGORY,
changes value.

The values of DOLLARS, UNITS, and DPERU for the Midwest and West regions under the
Gifts category.

418

6. Including Totals and Subtotals

PAGE   1.1

         Category
         Food                                   Gifts
         Region
         Midwest      West         TOTAL        Midwest      West
-------------------------------------------------------------------------
Dollars      4338271      4202337                   2883881      2977092
Units         341414       340234                    230854       235042
DPERU          12.71        12.35        12.53        12.49        12.67

The second panel has the total column for the Gifts category and the grand total column. Each
of those only has a value in the DPERU row.

 PAGE   1.2

         Category
                       TOTAL
         Region
          TOTAL
 ----------------------------------
 Dollars
 Units
 DPERU          12.58        12.55

Example:

Using Prefix Operators in a Summary Command With ACROSS

The following request against the GGSALES data source sums the DOLLARS and UNITS fields
ACROSS CATEGORY and ACROSS REGION, with a SUMMARIZE command on the REGION field.
The request also has a higher-level ACROSS field, CATEGORY, so the SUMMARIZE command
propagates to both ACROSS fields. The SUMMARIZE command specifies the AVE. prefix
operator for the DOLLARS field.

SET BYPANEL = ON
TABLE FILE GGSALES
SUM DOLLARS AS 'Dollars' OVER
UNITS AS 'Units'
  ACROSS CATEGORY
  ACROSS REGION
  ON REGION SUMMARIZE AVE. DOLLARS
  WHERE REGION EQ 'Midwest' OR 'West'
  WHERE CATEGORY EQ 'Food' OR 'Gifts'
  ON TABLE PCHOLD FORMAT PDF
END

The first panel of output shows:

The values of DOLLARS and UNITS for the Midwest and West regions under the Food
category.

Creating Reports With TIBCO® WebFOCUS Language

 419

Producing Summary Columns for Horizontal Sort Fields

The summary column, which has a value just for the DOLLARS row. Note that for ACROSS,
the summary column for REGION appears only after the higher-level ACROSS field,
CATEGORY, changes value.

The values of DOLLARS and UNITS for the Midwest and West regions under the Gifts
category.

PAGE   1.1

         Category
         Food                                   Gifts
         Region
         Midwest      West         TOTAL        Midwest      West
-------------------------------------------------------------------------
Dollars    4338271      4202337      4270304      2883881      2977092
Units       341414       340234                    230854       235042

The second panel has the total column for the Gifts category and the grand total column. Each
of those only has a value in the DOLLARS row.

PAGE   1.2

        Category
                      TOTAL
        Region
         TOTAL
----------------------------------
Dollars    2930486      3600395
Units

Example:

Using Combinations of ACROSS Summary Commands

The following request against the GGSALES data source sums the DOLLARS and UNITS fields
ACROSS CATEGORY and ACROSS REGION, with a SUMMARIZE command on the REGION field
and a SUBTOTAL command on the CATEGORY field. The SUMMARIZE command specifies
average DOLLARS and minimum UNITS. The SUBTOTAL command specifies minimum
DOLLARS.

420

6. Including Totals and Subtotals

SET BYPANEL = ON
TABLE FILE GGSALES
SUM DOLLARS AS 'Dollars' OVER
UNITS AS 'Units'
  ACROSS CATEGORY
  ACROSS REGION
    ON CATEGORY SUBTOTAL MIN. DOLLARS
    ON REGION SUMMARIZE AVE. DOLLARS MIN. UNITS
  WHERE REGION EQ 'Midwest' OR 'West'
  WHERE CATEGORY EQ 'Food' OR 'Gifts'
  ON TABLE PCHOLD FORMAT PDF
END

On the output, all of the TOTAL columns have the minimum UNITS. The TOTAL columns
associated with the REGION sort field have the average DOLLARS, but the TOTAL column
associated with the CATEGORY sort field has the minimum DOLLARS because SUMMARIZE
does not change the prefix operator associated with a higher-level sort field.

PAGE   1.1

         Category
         Food                                   Gifts
         Region
         Midwest      West         TOTAL        Midwest      West
-------------------------------------------------------------------------
Dollars    4338271      4202337      4270304      2883881      2977092
Units       341414       340234       340234       230854       235042

PAGE   1.2

        Category
                      TOTAL
        Region
         TOTAL
----------------------------------
Dollars    2930486      2883881
Units       230854       230854

Performing Calculations at Sort Field Breaks

You can use the RECAP and COMPUTE commands to create subtotal values in a calculation.
The subtotal values are not displayed. Only the result of the calculation is shown on the report.

Creating Reports With TIBCO® WebFOCUS Language

 421

Performing Calculations at Sort Field Breaks

Syntax:

How to Use Subtotals in Calculations

Both the RECAP and COMPUTE commands have similar syntax to other total and subtotal
commands.

{BY|ON} fieldname1 {RECAP|COMPUTE} fieldname2[/format] = expression;
                                      [WHEN expression;]

where:

fieldname1

Is the field in the BY phrase. Each time the BY field changes value, a new recap value is
calculated.

fieldname2

Is the field name that contains the result of the expression.

/format

Can be any valid format. The default is D12.2.

expression

Can be any valid expression, as described in Using Expressions on page 429. You must
end the expression with a semicolon.

WHEN expression

Is for use with RECAP only. It specifies the conditional display of RECAP lines as
determined by a Boolean expression (see Conditionally Displaying Summary Lines and Text
on page 427). You must end the expression with a semicolon.

Reference: Usage Notes for RECAP and COMPUTE

RECAP uses the current value of the named sort field, the current subtotal values of any
computational fields that appear as display fields, or the last value for alphanumeric fields.

RECAP reserves space at the bottom of the page to ensure that a RECAP will not be alone
at the top of the next page while the data it is recapping is on the previous page. The same
technique is used for subtotals and grand totals, but not for subfootings or COMPUTEs.

The field names in the expression must be fields that appear on the report. That is, they
must be display fields or sort control fields.

422

6. Including Totals and Subtotals

Each RECAP value displays on a separate line. However, if the request contains a RECAP
command and SUBFOOT text, the RECAP value displays only in the SUBFOOT text and must
be specified in the text using a spot marker. (For details, see Using Headings, Footings,
Titles, and Labels on page 1517.)

The calculations in a RECAP or COMPUTE can appear anywhere under the control break,
along with any text. (For details, see Using Headings, Footings, Titles, and Labels on page
1517.)

In an ON phrase, a COMPUTE command is the same as a RECAP command.

The limit for ON sortfield RECAP phrases is 64 for each sort field.

You can specify multiple recap calculations in one RECAP phrase. Use the following syntax:

ON sortfield RECAP field1/format= ... ;field2/format= ... ;
.
.
.

Example:

Using RECAP

The following request illustrates the use of RECAP (DEPT_NET) to determine net earnings for
each department:

TABLE FILE EMPLOYEE
SUM DED_AMT AND GROSS
BY DEPARTMENT BY PAY_DATE
ON DEPARTMENT RECAP DEPT_NET/D8.2M = GROSS-DED_AMT;
WHEN PAY_DATE GT 820101
END

Creating Reports With TIBCO® WebFOCUS Language

 423

Performing Calculations at Sort Field Breaks

The output is:

DEPARTMENT  PAY_DATE          DED_AMT            GROSS
----------  --------          -------            -----
MIS         81/11/30        $1,406.79        $2,147.75
            81/12/31        $1,406.79        $2,147.75
            82/01/29        $1,740.89        $3,247.75
            82/02/26        $1,740.89        $3,247.75
            82/03/31        $1,740.89        $3,247.75
            82/04/30        $3,386.73        $5,890.84
            82/05/28        $3,954.35        $6,649.50
            82/06/30        $4,117.03        $7,460.00
            82/07/30        $4,117.03        $7,460.00
            82/08/31        $4,575.72        $9,000.00

** DEPT_NET           $22,311.98

PRODUCTION  81/11/30          $141.66          $833.33
            81/12/31          $141.66          $833.33
            82/01/29        $1,560.09        $3,705.84
            82/02/26        $2,061.69        $4,959.84
            82/03/31        $2,061.69        $4,959.84
            82/04/30        $2,061.69        $4,959.84
            82/05/28        $3,483.88        $7,048.84
            82/06/30        $3,483.88        $7,048.84
            82/07/30        $3,483.88        $7,048.84
            82/08/31        $4,911.12        $9,523.84

** DEPT_NET           $27,531.14

Example:

Using Multiple RECAP Commands

You can include multiple RECAP or COMPUTE commands in a request. This option enables you
to perform different calculations at different control breaks.

The following request illustrates the use of multiple RECAP commands.

TABLE FILE SALES
SUM UNIT_SOLD AND RETURNS
WHERE AREA EQ 'U'
BY DATE BY AREA BY PROD_CODE
ON DATE RECAP
DATE_RATIO=RETURNS/UNIT_SOLD;
ON AREA UNDER-LINE RECAP
AREA_RATIO=RETURNS/UNIT_SOLD;
END

424

6. Including Totals and Subtotals

The output is:

DATE   AREA  PROD_CODE  UNIT_SOLD  RETURNS
----   ----  ---------  ---------  -------
10/17  U     B10               30        2
             B17               20        2
             B20               15        0
             C17               12        0
             D12               20        3
             E1                30        4
             E3                35        4

** AREA_RATIO                      .09

** DATE_RATIO                      .09

------------------------------------------
10/18  U     B10               13        1

** AREA_RATIO                      .08

** DATE_RATIO                      .08

------------------------------------------
10/19  U     B12               29        1

** AREA_RATIO                      .03

** DATE_RATIO                      .03

------------------------------------------

Suppressing Grand Totals

You can use the NOTOTAL command to suppress grand totals in a report.

Suppressing the grand total is useful when there is only one value at a sort break, since the
grand total value is equal to that one value. Using the NOTOTAL command prevents the report
from displaying a grand total line for every sort break that has only one detail line. You can
also suppress subtotals using the MULTILINES command. For details, see How to Create
Subtotals on page 377.

Syntax:

How to Suppress Grand Totals

To suppress grand totals, add the following syntax to your request:

ON TABLE NOTOTAL

Creating Reports With TIBCO® WebFOCUS Language

 425

Suppressing Grand Totals

Example:

Suppressing Grand Totals

The following request includes the NOTOTAL phrase to suppress grand totals for CURR_SAL,
GROSS, and DED_AMT.

TABLE FILE EMPLOYEE
SUM CURR_SAL AND GROSS AND DED_AMT
BY EMP_ID
BY BANK_ACCT
WHERE BANK_ACCT NE 0
ON BANK_ACCT SUB-TOTAL
ON TABLE NOTOTAL
END

426

The output is:

6. Including Totals and Subtotals

Conditionally Displaying Summary Lines and Text

In addition to using summary lines to control the look and content of your report, you can
specify WHEN criteria to control the conditions under which summary lines appear for each
vertical (BY) sort field value. WHEN is supported with SUBFOOT, SUBHEAD, SUBTOTAL, SUB-
TOTAL, SUMMARIZE, RECOMPUTE, and RECAP.

Creating Reports With TIBCO® WebFOCUS Language

 427

Conditionally Displaying Summary Lines and Text

Example:

Conditionally Displaying Summary Lines and Text

In a sales report that covers four regions (Midwest, Northeast, Southeast, and West), you may
only want to display a subtotal when total dollar sales are greater than $11,500,000. The
following request accomplishes this by including criteria that trigger the display of a subtotal
when dollar sales exceed $11,500,000 and subfooting text when dollar sales are less than
$11,500,000.

TABLE FILE GGSALES
SUM UNITS DOLLARS
BY REGION
BY CATEGORY
ON REGION SUBTOTAL
WHEN DOLLARS GT 11500000
SUBFOOT
"The total for the <REGION region is less than 11500000."
WHEN DOLLARS LT 11500000
END

The output is:

Region       Category     Unit Sales  Dollar Sales
------       --------     ----------  ------------
Midwest      Coffee           332777       4178513
             Food             341414       4338271
             Gifts            230854       2883881

The total for the Midwest region is less than 11500000.
Northeast    Coffee           335778       4164017
             Food             353368       4379994
             Gifts            227529       2848289

The total for the Northeast region is less than 11500000.
Southeast    Coffee           350948       4415408
             Food             349829       4308731
             Gifts            234455       2986240

*TOTAL Southeast              935232      11710379

West         Coffee           356763       4473517
             Food             340234       4202337
             Gifts            235042       2977092

*TOTAL West                   932039      11652946

TOTAL                        3688991      46156290

428

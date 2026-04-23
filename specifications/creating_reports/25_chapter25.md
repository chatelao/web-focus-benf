Chapter25 Creating Financial Reports With Financial

Modeling Language (FML)

The Financial Modeling Language (FML) is designed for the special needs associated
with creating, calculating, and presenting financially oriented data, such as balance
sheets, consolidations, or budgets. These reports are distinguished from other reports
because calculations are inter-row, as well as inter-column, and each row or line
represents a unique entry or series of entries that can be aggregated directly from the
input data or calculated as a function of the data.

In this chapter:

Reporting With FML

Inserting Rows of Free Text

Creating Rows From Data

Adding a Column to an FML Report

Supplying Data Directly in a Request

Creating a Recursive Model

Performing Inter-Row Calculations

Reporting Dynamically From a Hierarchy

Referring to Rows in Calculations

Customizing a Row Title

Referring to Columns in Calculations

Formatting an FML Report

Referring to Rows and Columns in
Calculations

Referring to Cells in Calculations

Suppressing the Display of Rows

Saving and Retrieving Intermediate
Report Results

Using Functions in RECAP Calculations

Creating HOLD Files From FML Reports

Reporting With FML

FML is an integrated extension of the TABLE command. By adding the FOR phrase and the
RECAP command, you can handle an expanded range of applications.

Note: MORE is not supported in FML requests.

In conjunction with Dialogue Manager, FML can evaluate "what if" scenarios and develop
complete decision support systems. These systems can take advantage of business
intelligence features, such as statistical analysis and graphics, in addition to standard
financial statements.

Creating Reports With TIBCO® WebFOCUS Language

 1817

Reporting With FML

Procedures using FML are not hard-wired to the data. As in any other report request, they can
easily be changed. FML includes the following facilities:

Row and column formatting. You can specify results in a row-by-row, column-by-column
fashion. For more information, see Performing Inter-Row Calculations on page 1831.

Intermediate results. You can post FML results to an external file and pick them up at a
later time for analysis. This is useful when intermediate results are developed and a final
procedure consolidates the results later. For more information, see Saving and Retrieving
Intermediate Report Results on page 1894.

Inline data entry. FML enables you to specify constants from within the procedure, in
addition to the data values retrieved from your data source. For more information, see
Supplying Data Directly in a Request on page 1829.

Recursive reporting. You can produce reports where the results from the end of one time
period or column become the starting balance in the next. For example, you can use
recursive reports to produce a cash flow projection. For more information, see Creating a
Recursive Model on page 1852.

Dynamic reporting from a chart of accounts or a similar hierarchy of information. You can
create a report that changes as the organization of information changes, ensuring that you
automatically retrieve information that reflects the latest structure and its values. There is
no need to alter either the Master File or the report request. For more information, see
Reporting Dynamically From a Hierarchy on page 1853.

Example:

Sample FML Request

This example produces a simple asset sheet, contrasting the results of two years. It illustrates
many key features of the Financial Modeling Language (FML). Numbers to the left of the
procedure lines correspond to explanations that follow the request.

1818

25. Creating Financial Reports With Financial Modeling Language (FML)

   TABLE FILE FINANCE
   HEADING CENTER
   "COMPARATIVE ASSET SHEET </2"
   SUM AMOUNT ACROSS HIGHEST YEAR
   WHERE YEAR EQ '1983' OR '1982'
1. FOR ACCOUNT
2. 1000           AS 'UTILITY PLANT'                 LABEL   UTP     OVER
2. 1010 TO 1050   AS 'LESS ACCUMULATED DEPRECIATION' LABEL   UTPAD   OVER
3. BAR                                                               OVER
4. RECAP UTPNET = UTP-UTPAD; AS 'TOTAL PLANT-NET'                    OVER
   BAR                                                               OVER
    2000 TO 3999  AS 'INVESTMENTS'                   LABEL   INV     OVER
5. "CURRENT ASSETS"                                                  OVER
    4000          AS 'CASH'                          LABEL   CASH    OVER
    5000 TO 5999  AS 'ACCOUNTS RECEIVABLE-NET'       LABEL   ACR     OVER
    6000          AS 'INTEREST RECEIVABLE'           LABEL   ACI     OVER
    6500          AS 'FUEL INVENTORY'                LABEL   FUEL    OVER
    6600          AS 'MATERIALS AND SUPPLIES'        LABEL   MAT     OVER
    6900          AS 'OTHER'                         LABEL   MISC    OVER
    BAR                                                              OVER
   RECAP TOTCAS=CASH+ACR+ACI+FUEL+MAT+MISC;AS 'TOTAL CURRENT ASSETS' OVER
    BAR                                                              OVER
    7000          AS 'DEFERRED DEBITS'               LABEL   DEFDB   OVER

    BAR                                                              OVER
6. RECAP TOTAL = UTPNET+INV+TOTCAS+DEFDB; AS 'TOTAL ASSETS'          OVER
    BAR AS '='
    FOOTING
    "</2 *** PRELIMINARY ASSET SHEET BASED ON UNAUDITED FIGURES ***"
   END

1. FOR and OVER are FML phrases that enable you to structure the report on a row-by-row

basis.

2. LABEL assigns a variable name to a row item for use in a RECAP calculation.

1000 and 1010 TO 1050 are tags that identify the data values of the FOR field, ACCOUNT
in the FINANCE data source. A report row can be associated with a tag that represents a
single data value (like 1000), multiple data values, or a range of values (like 1010 TO
1050).

3. BAR enables you to underline a column of numbers before performing a RECAP calculation.

4. The RECAP command creates a new value based on values already identified in the report

with LABEL. In this case, the value UTPNET is derived from UTP and UTPAD and is renamed
TOTAL PLANT-NET with an AS phrase to provide it with greater meaning in the report.

5. Free text can be incorporated at any point in an FML report, similar to underlines.

6. Notice that this RECAP command derives a total (TOTAL ASSETS) from values retrieved

directly from the data source, and from values derived from previous RECAP computations
(UTPNET and TOTCAS).

Creating Reports With TIBCO® WebFOCUS Language

 1819

Creating Rows From Data

The output is shown as follows.

Creating Rows From Data

A normal TABLE request sorts rows of a report according to the BY phrase you use. The data
retrieved is sorted from either low-to-high or high-to-low, as requested. The rows may be limited
by a screening phrase to a specific subset, but:

They appear in a sort order.

Rows appear only for values that are retrieved from the file.

1820

25. Creating Financial Reports With Financial Modeling Language (FML)

You can only insert free text between rows when a sort field changes value, such as:

ON DIVISION SUBFOOT

You can only insert calculations between rows when a sort field changes value, such as:

ON DIVISION RECAP

In contrast, the FML FOR phrase creates a matrix in which you can structure your report row-by-
row. This organization gives you greater control over the data that is incorporated into a report,
and its presentation. You can:

Report on specific data values for a field in a data source and combine particular data
values under a common label, for use in calculations.

Type data directly into the request to supplement data retrieved from the data source.

Include text, underlines, and calculations at points in the report that are not related to sort
breaks.

Perform recursive processing, in which the result of an interim calculation is saved and
then used as the starting point for a subsequent calculation.

Suppress the display of rows for which no data is retrieved.

Identify rows by labels and columns by numbers, addresses, and values so that you can
point to the individual cells formed at each intersection (as on a spreadsheet).

Syntax:

How to Retrieve FOR Field Values From a Data Source

The syntax for specifying rows is:

FOR fieldname [AS 'coltitle'] value [OR value OR...] [AS 'text']
[LABEL label] OVER
.
.
.
[value [OR value ...]] [AS 'text'] [LABEL label]
END

where:

fieldname

Is the FOR field for the FML report.

coltitle

Is the column title for the FOR field on the report output.

Creating Reports With TIBCO® WebFOCUS Language

 1821

Creating Rows From Data

value

Is the value (also known as a tag value) describing the data that is retrieved for this row of
the report.

AS 'text'

Enables you to assign a name to a tag value, which replaces the tag value in the output.
Enclose the text in single quotation marks.

label

Assigns a label to the row for reference in a RECAP expression. The label can be up to 66
characters and cannot have blanks or special characters. Each explicit label you assign
must be unique.

Even if you assign an explicit label, the positional label (R1, R2, and so on) is retained
internally.

By default, a tag value for a FOR field (like 1010) may be added only once to the FML matrix.
However, if you wish to add the same value of a FOR field to the matrix more than once, you
can turn on the FORMULTIPLE parameter (the default setting is OFF). For more information, see
How to Use the Same FOR Field Value in Multiple Rows on page 1826.

For more information about the FMLFOR, FMLLIST, and FMLINFO functions that return the tag
values used in an FML request, see the Using Functions manual.

Example:

Creating Rows From Values in a Data Source

Assume you have a simple data source with financial data for each corporate account, as
follows:

CHART OF ACCOUNTS

ACCOUNT          DESCRIPTION

1010             CASH ON HAND
1020             DEMAND DEPOSITS
1030             TIME DEPOSITS
1100             ACCOUNTS RECEIVABLE
1200             INVENTORY
.                     .
.                     .
.                     .

Using the FOR phrase in FML, you can issue the following TABLE request in which each value
of ACCOUNT is represented by a tag (1010, 1020, and so on), and displays as a separate row:

1822



25. Creating Financial Reports With Financial Modeling Language (FML)

TABLE FILE LEDGER
SUM AMOUNT
FOR ACCOUNT
1010 OVER
1020 OVER
1030 OVER
1100 OVER
1200
END

The output is shown as follows.

      AMOUNT
      ------
1010   8,784
1020   4,494
1030   7,961
1100  18,829
1200  27,307

Creating Rows From Multiple Records

There are different ways to combine multiple values from your data sources into an FML report
row. You can use:

The OR phrase to sum the values of two or more tags in a single expression. For more
information, see How to Sum Values in Rows With the OR Phrase on page 1824.

The TO phrase to identify a range of tag values on which to report. For more information,
see How to Identify a Range of Values With the TO Phrase on page 1825.

A mask to specify a group of tag values without having to name each one. For more
information, see How to Use Masking Characters to Retrieve Tag Values on page 1826.

By default, a FOR field value can only be included in a single row of an FML matrix. However, by
turning on the FORMULTIPLE parameter, you can include the same data value in multiple rows
in the FML matrix. For example, the same value can exist as a solitary value in one row, be
part of a range in another row, and be used in a calculation in a third row. For more
information, see How to Use the Same FOR Field Value in Multiple Rows on page 1826.

In addition to these methods, you can extract multiple tags for a row from an external file.

Creating Reports With TIBCO® WebFOCUS Language

 1823

Creating Rows From Data

Syntax:

How to Sum Values in Rows With the OR Phrase

To sum the values of two or more tags in a single report row, use the OR phrase in the FOR
phrase. The syntax is:

FOR fieldname
value1 OR value2 [OR valuen...] [AS 'text'] [LABEL label] [OVER]
.
.
.

where:

fieldname

Is a field name in the data source.

value1, value2, valuen

Are the tag values to be retrieved and summed.

AS 'text'

Assigns a title to the combined tag values. Enclose the text in single quotation marks (').

label

Assigns a label to the row for reference in a RECAP expression. The label can be up to 66
characters and cannot have blanks or special characters. Each explicit label you assign
must be unique.

Even if you assign an explicit label, the positional label (R1, R2, and so on) is retained
internally.

Example:

Summing Values in Rows

The following model sums the values of three tags (1010, 1020, 1030) as CASH.

TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
1010 OR 1020 OR 1030  AS 'CASH'                   OVER
1100                  AS 'ACCOUNTS RECEIVABLE'    OVER
1200                  AS 'INVENTORY'
END

The output is shown as follows.

                     AMOUNT
                     ------
CASH                 21,239
ACCOUNTS RECEIVABLE  18,829
INVENTORY            27,307

1824

25. Creating Financial Reports With Financial Modeling Language (FML)

Syntax:

How to Identify a Range of Values With the TO Phrase

To sum the values of a range of tags in a single report row, use the TO phrase in the FOR
phrase. The syntax is:

FOR fieldname
value1 TO value2 [AS 'text'] [LABEL label] [OVER]

where:

fieldname

Is a field name in the data source.

value1

Is the tag value at the lower limit of the range.

TO

Is the required phrase.

value2

Is the tag value at the upper limit of the range.

AS 'text'

Assigns a title to the combined tag values. Enclose the text in single quotation marks (').

label

Assigns a label to the row for reference in a RECAP expression. The label can be up to 66
characters and cannot have blanks or special characters. Each explicit label you assign
must be unique.

Even if you assign an explicit label, the positional label (R1, R2, and so on) is retained
internally.

Example:

Identifying a Range of Values

Since CASH accounts in the LEDGER system are identified by the tags 1010, 1020, and 1030,
you can specify the range 1010 to 1030:

TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
1010 TO 1030 AS 'CASH'
END

Creating Reports With TIBCO® WebFOCUS Language

 1825

Creating Rows From Data

Syntax:

How to Use Masking Characters to Retrieve Tag Values

If the tag field has a character (alphanumeric) format, you can perform a masked match. Use
the dollar sign character ($) as the mask. For instance,

A$$D

matches any four-character value beginning with A and ending with D. The two middle places
can be any character. This is useful for specifying a whole group of tag values without having to
name each one.

Example:

Using Masking Characters to Match a Group of Tags

In this example, the amounts associated with all four-character accounts that begin with 10,
expressed with a mask as 10$$, are used to produce the CASH row of the report.

TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
10$$ AS 'CASH'                 OVER
1100 AS 'ACCOUNTS RECEIVABLE'  OVER
1200 AS 'INVENTORY'
END

The output is shown as follows.

                     AMOUNT
                     ------
CASH                 21,239
ACCOUNTS RECEIVABLE  18,829
INVENTORY            27,307

Syntax:

How to Use the Same FOR Field Value in Multiple Rows

You can use the same value of a FOR field in many separate rows (whether alone, as part of a
range, or in a calculation) by including the following syntax before or within an FML request.

SET FORMULTIPLE={ON|OFF}

or

ON TABLE SET FORMULTIPLE {ON|OFF}

where:

ON

Enables you to reference the same value of a FOR field in more than one row in an FML
request.

With FORMULTIPLE set to ON, a value retrieved from the data source is included on every
line in the report output for which it matches the tag references.

1826

25. Creating Financial Reports With Financial Modeling Language (FML)

OFF

Does not enable you to include the same value in multiple rows. OFF is the default value.

With FORMULTIPLE set to OFF, multiple tags referenced in any of these ways (OR, TO, *)
are evaluated first for an exact reference or for the end points of a range, then for a mask,
and finally within a range. For example, if a value is specified as an exact reference and
then as part of a range, the exact reference is displayed. Note that the result is
unpredictable if a value fits into more than one row whose tags have the same priority (for
example, an exact reference and the end point of a range).

For more information, see Reporting Dynamically From a Hierarchy on page 1853.

Example:

Referencing the Same Value in More Than One Row

This request retrieves the tag values for accounts 1010, 1020, and 1030, and lists
corresponding values individually. It then aggregates the same values and displays the sum as
TOTAL CASH. Similarly, the tag values for accounts 1100 and 1200 displays as detail items,
and then summarized as TOTAL NON-CASH ASSETS.

SET FORMULTIPLE=ON
TABLE FILE LEDGER
SUM AMOUNT
FOR ACCOUNT
1010 AS 'CASH ON HAND'                OVER
1020 AS 'DEMAND DEPOSITS'             OVER
1030 AS 'TIME DEPOSITS'               OVER
BAR                                   OVER
1010 OR 1020 OR 1030 AS 'TOTAL CASH'  OVER
" "                                   OVER
1100 AS 'ACCOUNTS RECEIVABLE'         OVER
1200 AS 'INVENTORY'                   OVER
BAR                                   OVER
1100 TO 1200 AS 'TOTAL NON-CASH ASSETS'
END

The output is shown as follows.

                       AMOUNT
                       ------
CASH ON HAND            8,784
DEMAND DEPOSITS         4,494
TIME DEPOSITS           7,961
                       ------
TOTAL CASH             21,239

ACCOUNTS RECEIVABLE    18,829
INVENTORY              27,307
                       ------
TOTAL NON-CASH ASSETS  46,136

Creating Reports With TIBCO® WebFOCUS Language

 1827


Creating Rows From Data

Example:

Using Tags From External Files

In this example, the values for a row of the FML report come from an external file called
CASHSTUF, which contains the following tags.

1010
1020
1030

The following TABLE request uses the tag values from the external file, summing the amounts
in accounts 1010, 1020, and 1030 into the CASH row of the FML report.

TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
(CASHSTUF)  AS 'CASH'                 OVER
1100        AS 'ACCOUNTS RECEIVABLE'
END

Notice that the file name must be enclosed in parentheses.

Using the BY Phrase in FML Requests

Only one FOR phrase is permitted in a TABLE request. It substitutes in part for a BY phrase,
which controls the sort sequence. However, the request can also include up to 32 BY phrases.
In general, BY phrases specify the major (outer) sort fields in FML reports, and the FOR phrase
specifies the minor (inner) sort field. Note that the BY ROWS OVER phrase is not supported in
a request that uses the FOR phrase.

1828

25. Creating Financial Reports With Financial Modeling Language (FML)

Combining BY and FOR Phrases in an FML Request

In this example, the report results for ACCOUNT (the inner sort field) are sorted by REGION (the
outer sort field).

DEFINE FILE REGION
CUR_YR=E_ACTUAL;
LAST_YR=.831*CUR_YR;
REGION/A4=IF E_ACTUAL NE 0 OR E_BUDGET NE 0 THEN 'EAST' ELSE 'WEST';
END

TABLE FILE REGION
HEADING CENTER
"CURRENT ASSETS FOR REGION <REGION"
" "
SUM CUR_YR LAST_YR
BY REGION NOPRINT
FOR ACCOUNT
10$$ AS 'CASH'                      OVER
1100 AS 'ACCOUNTS RECEIVABLE'       OVER
1200 AS 'INVENTORY'                 OVER
BAR                                 OVER
RECAP CUR_ASSET/I5C = R1 + R2 + R3;
END

The output is shown as follows.

          CURRENT ASSETS FOR REGION EAST

                             CUR_YR         LAST_YR
                             ------         -------
CASH                       9,511.00        7,903.64
ACCOUNTS RECEIVABLE               .               .
INVENTORY                         .               .
                     --------------  --------------
CUR_ASSET                     9,511           7,903

A sort field value can be used in a RECAP command to allow the model to take different
actions within each major sort break. For instance, the following calculation computes a non-
zero value only for the EAST region.

RECAP X=IF REGION EQ 'EAST' THEN .25*CASH ELSE 0;
AS 'AVAILABLE FOR DIVIDENDS'

For more information, see Performing Inter-Row Calculations on page 1831.

Supplying Data Directly in a Request

In certain cases, you may need to include additional constants (such as exchange rates or
inflation rates) in your model. Not all data values for the model have to be retrieved from the
data source. Using FML, you can supply data directly in the request.

Creating Reports With TIBCO® WebFOCUS Language

 1829



Supplying Data Directly in a Request

Syntax:

How to Supply Data Directly in a Request

DATA value,[..., value],$ [AS 'text'] [LABEL label] OVER

where:

value

Specifies the values that you are supplying. Values in a list must be separated by
commas. The list must end with a comma and a dollar sign (,$).

AS 'text'

Enables you to assign a title to the data row. Enclose the text in single quotation marks.

Without this entry, the row title is blank on the report.

label

Assigns a name to the data row for use in RECAP calculations. The label can be up to 66
characters and cannot have blanks or special characters. Each explicit label you assign
must be unique.

Example:

Supplying Data Directly in a Request

In this example, two values (.87 and 1.67) are provided for the exchange rates of euros and
pounds, respectively.

DEFINE FILE LEDGER
EUROS/I5C=AMOUNT;
POUNDS/I5C=3.2*AMOUNT;
END

TABLE FILE LEDGER
SUM EUROS AS 'EUROPE,DIVISION'
POUNDS AS 'ENGLISH,DIVISION'
FOR ACCOUNT
1010 AS 'CASH--LOCAL CURRENCY' LABEL CASH          OVER
DATA .87, 1.67 ,$ AS 'EXCHANGE RATE' LABEL EXCH    OVER
RECAP US_DOLLARS/I5C = CASH * EXCH;
END

The values supplied are taken one column at a time for as many columns as the report
originally specified.

1830


25. Creating Financial Reports With Financial Modeling Language (FML)

The output is shown in the following image.

Performing Inter-Row Calculations

The RECAP command enables you to perform calculations on data in the rows of the report to
produce new rows. You must supply the name and format of the value that results from the
calculation, and an expression that defines the calculation you wish to perform. Since RECAP
calculations are performed among rows, each row in the calculation must be uniquely
identified. FML supplies default row labels for this purpose (R1, R2, and so on). However, you
may assign more meaningful labels. For more information, see Referring to Rows in
Calculations on page 1832.

Syntax:

How to Define Inter-Row Calculations

RECAP calcname[/format]=expression; [AS 'text']

where:

RECAP

Is the required command name. It should begin on a line by itself.

calcname

Is the name you assign to the calculated value. The name can be up to 66 characters
long, and must start with an alphabetic character. This name also serves as an explicit
label. For more information, see Referring to Rows in Calculations on page 1832.

format

Is the USAGE format of the calculated value. It cannot exceed the column width. The
default is the format of the column in which the calculated value is displayed.

expression

Can be any calculation available with the DEFINE command (including IF ... THEN ... ELSE
syntax, functions, excluding DECODE and EDIT, and fields in date format). The expression
may extend to as many lines as it requires. A semicolon is required at the end of the
expression. For more information, see Using Functions in RECAP Calculations on page
1845 and the Using Functions manual.

Creating Reports With TIBCO® WebFOCUS Language

 1831

Referring to Rows in Calculations

The expression can include references to specific rows using the default FML positional
labels (R1, R2, and so on), or it can refer to rows, columns, and cells using a variety of
flexible notation techniques. Note that Rn references can only be used for rows previously
evaluated within the model. For more information, see Referring to Rows in Calculations on
page 1832, Referring to Columns in Calculations on page 1835, and Referring to Cells in
Calculations on page 1843.

AS 'text'

Changes the default title of the row. By default, the name of the RECAP value is displayed
as the row title in output. The AS phrase replaces the default. Enclose the text in single
quotation marks.

Reference: Usage Notes for RECAP

RECAP expressions refer to other rows in the model by their labels (either explicit or
default). Labels referred to in a RECAP expression must also be specified in the report
request.

The format specified for the RECAP result overrides the format of the column. In the
following example,

RECAP TOTVAL/D6.2S=IF R1 GT R4 THEN R4 ELSE R1;
AS 'REDUCED VALUE'

TOTVAL/D6.2S displays the result as six positions with two decimal places (and displays
blanks if the value was zero) in each column of the report, regardless of the format of the
data in the column. This feature can be used to display percentages in a column of whole
numbers.

Subtotals are not supported in FML.

In environments that support the RETYPE command, note that RETYPE does not recognize
labels in FML with field format redefinition.

Rn references (default positional row labels) can only be used for rows previously evaluated
within the model.

Referring to Rows in Calculations

FML assigns a default positional label to each TAG, DATA, RECAP, and PICKUP row. These
positional labels are automatically prefixed with the letter R, so that the first such row in the
model is R1, the second is R2, and so on. You can use these labels to refer to rows in RECAP
expressions.

1832

25. Creating Financial Reports With Financial Modeling Language (FML)

Note: Default labels are not assigned to rows that contain underlines, blank lines, or free text,
since these row types need not be referenced in expressions.

When you refer to rows in a RECAP expression, you can:

Use the positional row label assigned by FML.

Create an explicit row label of your own.

Note: You should not create an explicit label with a name of the form Rn, as that type of
name is used for default positional row labels assigned by FML and may cause problems
with subsequent RECAPs.

Mix positional and explicit row labels.

If you assign an explicit label, the positional label (R1, R2, and so on) is retained internally.

Note that an explicit label is not needed for a RECAP row, because the name of the calculated
value on the left of the equal sign can be used as a label.

In addition to their role in RECAP calculations, you can use labels to format rows in an FML
report. For more information, see Formatting an FML Report on page 1871.

Syntax:

How to Assign an Explicit Row Label

rowtype [AS 'text'] LABEL label [OVER]

where:

rowtype

Can be a TAG, DATA, or PICKUP row.

AS 'text'

Assigns a different name to the row for the report. Enclose the text in single quotation
marks (').

label

Assigns a label to a row for reference in a RECAP expression or a StyleSheet declaration.
The label can be up to 66 characters and cannot have blanks or special characters. Each
explicit label you assign must be unique.

Note: You should not create an explicit label with a name of the form Rn, as that type of
name is used for default positional row labels assigned by FML and may cause problems
with subsequent RECAPs.

Creating Reports With TIBCO® WebFOCUS Language

 1833

Referring to Rows in Calculations

Even if you assign an explicit label, the positional label (R1, R2, and so on) is retained
internally.

Example:

Referring to Default Row Labels in RECAP Expressions

In this example, FML assigns account 1010 the implicit label R1, account 1020, the implicit
label R2, and account 1030, the implicit label R3. Since no label is assigned to a BAR row, the
RECAP row is assigned the implicit label R4.

TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
1010 AS 'CASH ON HAND'      OVER
1020 AS 'DEMAND DEPOSITS'   OVER
1030 AS 'TIME DEPOSITS'     OVER
BAR                         OVER
RECAP TOTCASH = R1 + R2 + R3; AS 'TOTAL CASH'
END

The output is shown as follows.

                 AMOUNT
                 ------
CASH ON HAND      8,784
DEMAND DEPOSITS   4,494
TIME DEPOSITS     7,961
                 ------
TOTAL CASH       21,239

Referring to Explicit Row Labels in RECAP Expressions

The following request assigns the labels CA, AR, and INV to three tag rows, which are
referenced in the RECAP expression.

TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
10$$ AS 'CASH'                   LABEL CA    OVER
1100 AS 'ACCOUNTS RECEIVABLE'    LABEL AR    OVER
1200 AS 'INVENTORY'              LABEL INV   OVER
BAR                                          OVER
RECAP CURASST/I5C = CA + AR + INV;
END

The output is shown as follows.

                     AMOUNT
                     ------
CASH                 21,239
ACCOUNTS RECEIVABLE  18,829
INVENTORY            27,307
                     ------
CURASST              67,375

Note that the RECAP value could subsequently be referred to by the name CURASST, which
functions as an explicit label.

1834

25. Creating Financial Reports With Financial Modeling Language (FML)

Using Labels to Repeat Rows

In certain cases, you may wish to repeat an entire row later in your report. For example, the
CASH account can appear in the Asset statement and Cash Flow statement of a financial
analysis, as shown below.

TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
"ASSETS"                          OVER
10$$ AS 'CASH' LABEL TOTCASH      OVER
.
.
"CASH FLOW"                       OVER
RECAP SAMECASH/I5C = TOTCASH; AS 'CASH'
END

When you refer to the CASH row the second time, you can use a RECAP calculation (with a new
name) and refer to the label, either explicitly (TOTCASH) or implicitly (R1), in the row where
CASH was first used.

Tip: If you set the FORMULTIPLE parameter ON, you can repeat the row without giving it
another name. For more information, see Creating Rows From Multiple Records on page 1823.

Referring to Columns in Calculations

An FML report can refer to explicit columns, as well as explicit rows. You can refer to columns
using:

Column numbers.

Contiguous column notation in RECAP expressions. For example, (2,5) represents columns
2 through 5.

Column addressing.

A factor to represent every other column, or every third column, and so on.

Column notation to control the creation of column reference numbers.

Column values.

Example:

Applying Column Declarations in RECAP Expressions

The following request generates an FML matrix with four rows and three columns of data.

Creating Reports With TIBCO® WebFOCUS Language

 1835

Referring to Columns in Calculations

DEFINE FILE LEDGER
CUR_YR/I5C=AMOUNT;
LAST_YR/I5C=.87*CUR_YR - 142;
END

TABLE FILE LEDGER
SUM CUR_YR AS 'CURRENT,YEAR'
   LAST_YR AS 'LAST,YEAR'
COMPUTE CHANGE/I5C = CUR_YR - LAST_YR;
FOR ACCOUNT
1010 AS 'CASH ON HAND'                  OVER
1020 AS 'DEMAND DEPOSITS'               OVER
1030 AS 'TIME DEPOSITS'                 OVER
BAR                                     OVER
RECAP TOTCASH/I5C = R1 + R2 + R3; AS 'TOTAL CASH'
END

Both the columns of the report, as well as the cells of the matrix, can be referenced in another
FML report.

The output is shown in the following image.

For example, you could use the value 6,499 in another FML report by referring to column 2,
row 3. For more information, see Referring to Cells in Calculations on page 1843.

Referring to Column Numbers in Calculations

You can perform a calculation for one column or for a specific set of columns. To identify the
columns, place the column number in parentheses after the label name.

1836


25. Creating Financial Reports With Financial Modeling Language (FML)

Example:

Referring to Column Numbers in a RECAP Expression

DEFINE FILE LEDGER
CUR_YR/I5C=AMOUNT;
LAST_YR/I5C=.87*CUR_YR - 142;
END

TABLE FILE LEDGER
SUM CUR_YR AS 'CURRENT,YEAR'
LAST_YR AS 'LAST,YEAR'
FOR ACCOUNT
1010 AS 'CASH ON HAND'                             OVER
1020 AS 'DEMAND DEPOSITS'                          OVER
1030 AS 'TIME DEPOSITS'                            OVER
BAR                                                OVER
RECAP TOTCASH/I5C = R1 + R2 + R3; AS 'TOTAL CASH'  OVER
" "                                                OVER
RECAP GROCASH(2)/F5.2 = 100*TOTCASH(1)/TOTCASH(2) - 100;
AS 'CASH GROWTH(%)'
END

In the second RECAP expression, note that:

TOTCASH(1) refers to total cash in column 1.

TOTCASH(2) refers to total cash in column 2.

The resulting calculation is displayed in column 2 of the row labeled CASH GROWTH(%).

The RECAP value is only calculated for the column specified.

The output is shown in the following image.

After data retrieval is completed, a single column is calculated all at once, and multiple
columns one by one.

Referring to Contiguous Columns in Calculations

When a set of contiguous columns is needed within a RECAP, you can separate the first and
last column numbers with commas. For example, DIFFERENCE (2,5) indicates that you want to
compute the results for columns 2 through 5.

Creating Reports With TIBCO® WebFOCUS Language

 1837


Referring to Columns in Calculations

Example:

Recapping Over Contiguous Columns

In this example, the RECAP calculation for ATOT occurs only for columns 2 and 3, as specified
in the request. No calculation is performed for column 1.

DEFINE FILE LEDGER
CUR_YR/I5C=AMOUNT;
LAST_YR/I5C=.87*CUR_YR - 142;
NEXT_YR/I5C=1.13*CUR_YR + 222;
END

TABLE FILE LEDGER
SUM NEXT_YR CUR_YR LAST_YR
FOR ACCOUNT
10$$ AS 'CASH'                      OVER
1100 AS 'ACCOUNTS RECEIVABLE'       OVER
1200 AS 'INVENTORY'                 OVER
BAR                                 OVER
RECAP ATOT(2,3)/I5C = R1 + R2 + R3;
AS 'ASSETS--ACTUAL'
END

The output is shown in the following image.

Referring to Column Addresses in Calculations

When you need a calculation for every other or every third column instead of every column, you
can supply a factor, or column address, to do this. Column addressing is useful when several
data fields are displayed within each value of a column sort.

Syntax:

How to Use Column Addressing in a RECAP Expression

The left-hand side of the expression has the form:

value(s,e,i)[/format]=

where:

value

Is the name you assign to the result of the RECAP calculation.

s

Is the starting column.

1838


25. Creating Financial Reports With Financial Modeling Language (FML)

e

i

Is the ending column (it may be * to denote all columns).

Is the increment factor.

format

Is the USAGE format of the calculated value. The default value is the format of the original
column.

Example:

Applying Column Addressing in a RECAP Expression

In the following statement, there are two columns for each month:

SUM ACTUAL AND FORECAST ACROSS MONTH

If you want to perform a calculation only for the ACTUAL data, control the placement of the
results with a RECAP in the form:

RECAP calcname(1,*,2)=expression;

The asterisk means to continue the RECAP for all odd-numbered columns (beginning in column
1, with an increment of 2, for all columns).

Referring to Relative Column Addresses in Calculations

A calculation can use a specific column as a base, and refer to all other columns by their
displacement from that column. The column to the left of the base column has a displacement
of -1 relative to the base column. The column to the right has a displacement of +1. For
example,

COMP=FIX(*)-FIX(*-1);

can refer to the change in fixed assets from one period to the next. The reference to
COMP=FIX(*) is equivalent to COMP=FIX.

When referring to a prior column, the column must already have been retrieved, or its value is
zero.

Creating Reports With TIBCO® WebFOCUS Language

 1839

Referring to Columns in Calculations

Applying Relative Column Addressing in a RECAP Expression

This example computes the change in cash (CHGCASH) for columns 1 and 2.

DEFINE FILE LEDGER
CUR_YR/I5C=AMOUNT;
LAST_YR/I5C=.87*CUR_YR - 142;
NEXT_YR/I5C=1.13*CUR_YR + 222;
END

TABLE FILE LEDGER
SUM NEXT_YR CUR_YR LAST_YR
FOR ACCOUNT
10$$ AS 'TOTAL CASH' LABEL TOTCASH           OVER
" "                                          OVER
RECAP CHGCASH(1,2)/I5SC = TOTCASH(*) - TOTCASH(*+1); AS 'CHANGE IN CASH'
END

The output is shown in the following image.

Controlling the Creation of Column Reference Numbers

Column notation assigns a sequential column number to each column in the internal matrix
created for a report request. If you want to control the creation of column reference numbers
for the columns that are used in your report, use the CNOTATION column notation command.

Because column numbers refer to columns in the internal matrix, they are assigned after
retrieval and aggregation of data are completed. Columns created and displayed in a report are
stored in the internal matrix, and columns that are not displayed in a report may also be
generated and stored in the internal matrix. Columns stored in the internal matrix include
calculated values, reformatted field values, BY fields, fields with the NOPRINT option, and
certain RECAP calculations such as FORECAST and REGRESS. Every other column in the
internal matrix is assigned a column number by default, which means you have to account for
all internally generated columns, if you want to refer to the appropriate column value in your
request.

You can change the default assignment of column reference numbers by using the SET
CNOTATION=PRINTONLY command which assigns column numbers only to columns that
display in the report output. You can use column notation in COMPUTE and RECAP commands
to refer to these columns in your request.

1840


25. Creating Financial Reports With Financial Modeling Language (FML)

Syntax:

How to Control the Creation of Column Reference Numbers

SET CNOTATION={ALL|PRINTONLY|EXPLICIT}

where:

ALL

Assigns column reference numbers to every column in the internal matrix. ALL is the
default value.

PRINTONLY

Assigns column reference numbers only to columns that display in the report output.

EXPLICIT

Assigns column reference numbers to all fields referenced in the request, whether
displayed or not.

Note: CNOTATION is not supported in an ON TABLE phrase.

Referring to Column Values in Calculations

When a report is sorted using the ACROSS phrase, all of the retrieved values are aligned under
their appropriate columns. Each column has a title consisting of one value of the ACROSS
field. The entire column of data can be addressed by this value in a RECAP calculation.

Example:

Referring to a Column by Its Value in a RECAP Expression

The following request uses a factor that depends on the value of the ACROSS field (YEAR) to
calculate the inventory cost for each year. It then calculates the profit by summing the assets
and subtracting the inventory cost for each year.

TABLE FILE LEDGER
SUM AMOUNT ACROSS YEAR
FOR ACCOUNT
10$$ AS 'CASH' LABEL CASH                         OVER
1100 AS 'ACCOUNTS RECEIVABLE' LABEL RECEIVE       OVER
BAR                                               OVER
1200 AS 'INVENTORY VALUE' LABEL INVENT            OVER
RECAP INVENTORY_FACTOR/F5.2 = IF YEAR LT '1986'
   THEN 1.1 ELSE 1.25; AS 'INVENTORY COST FACTOR' OVER
RECAP INVENTORY_COST = INVENTORY_FACTOR * INVENT;
   AS 'INVENTORY COST'                            OVER
BAR                                               OVER
RECAP PROFIT = CASH + RECEIVE - INVENTORY_COST;
END

Creating Reports With TIBCO® WebFOCUS Language

 1841

Referring to Rows and Columns in Calculations

The output is shown in the following image.

Referring to Rows and Columns in Calculations

You can style multiple RECAP commands in a matrix when the RECAP statements are placed
after the last ACROSS value.

1842

25. Creating Financial Reports With Financial Modeling Language (FML)

Example:

Styling Multiple RECAP Statements in a Matrix

TABLE FILE GGSALES
SUM UNITS
BY PRODUCT
ACROSS REGION
RECAP
TTL1/I8 = C1+C2+C3+C4;
TTL2/D12.2 = TTL1*1.25;

ON TABLE SET STYLE *
TYPE=DATA, COLUMN=TTL1 (*), COLOR=BLUE, BACKCOLOR=SILVER, STYLE=BOLD, $
TYPE=DATA, COLUMN=TTL2 (*), COLOR=RED, BACKCOLOR=AQUA, STYLE=BOLD, $
ENDSTYLE
END

The output is shown in the following image.

Referring to Cells in Calculations

You can refer to columns and rows using a form of cell notation that identifies the intersection
of a row and a column as (r, c).

Creating Reports With TIBCO® WebFOCUS Language

 1843

Referring to Cells in Calculations

Syntax:

How to Use Cell Notation for Rows and Columns in a RECAP Expression

A row and column can be addressed in an expression by the notation:

E(r,c)

where:

E

r

c

Is a required constant.

Is the row number.

Is the column number. Use an asterisk (*) to indicate the current column.

Example:

Referring to Columns Using Cell Notation in a RECAP Expression

In this request, two RECAP expressions derive VARIANCEs (EVAR and WVAR) by subtracting
values in four columns (1, 2, 3, 4) in row three (PROFIT). These values are identified using cell
notation (r,c).

TABLE FILE REGION
SUM E_ACTUAL E_BUDGET W_ACTUAL W_BUDGET
FOR ACCOUNT
3000 AS 'SALES'                         OVER
3100 AS 'COST'                          OVER
BAR                                     OVER
RECAP PROFIT/I5C = R1 - R2;             OVER
" "                                     OVER
RECAP EVAR(1)/I5C = E(3,1) - E(3,2);
AS 'EAST--VARIANCE'                     OVER
RECAP WVAR(3)/I5C = E(3,3) - E(3,4);
AS 'WEST--VARIANCE'
END

The output is shown as follows.

                E_ACTUAL  E_BUDGET  W_ACTUAL  W_BUDGET
                --------  --------  --------  --------
SALES              6,000     4,934     7,222     7,056
COST               4,650     3,760     5,697     5,410
                  ------    ------    ------    ------
PROFIT             1,350     1,174     1,525     1,646

EAST--VARIANCE       176
WEST--VARIANCE                          -121

1844


25. Creating Financial Reports With Financial Modeling Language (FML)

Note: In addition to illustrating cell notation, this example demonstrates the use of column
numbering. Notice that the display of the EAST and WEST VARIANCEs in columns 1 and 3,
respectively, are controlled by the numbers in parentheses in the request: EVAR (1) and WVAR
(3).

Using Functions in RECAP Calculations

You may provide your own calculation routines in RECAP rows to perform special-purpose
calculations, a useful feature when these calculations are mathematically complex or require
extensive look-up tables.

User-written functions are coded as subroutines in any language that supports a call process,
such as FORTRAN, COBOL, PL/1, and BAL. For information about creating your own functions,
see the Using Functions manual.

Syntax:

How to Call a Function in a RECAP Command

RECAP calcname[(s,e,i)][/format]=function
(input1,...,inputn,'format2');

where:

calcname

Is the name you assign to the calculated value.

(s,e,i)

Specify a start (s), end (e), and increment (i) value for the column where you want the
value displayed. If omitted, the value appears in all columns.

format

The format for the calculation is optional. The default is the format of the column. If the
calculation consists of only the subroutine, make sure that the format of the subroutine
output value (format2) agrees with the calculation format. If the calculation format is larger
than the column width, the value displays in that column as asterisks (*).

function

Is the name of the function, up to eight characters long. It must be different from any row
label and cannot contain any of the following special characters:

= -, / ()

Creating Reports With TIBCO® WebFOCUS Language

 1845

Using Functions in RECAP Calculations

input1, inputn

Are the input arguments for the call to the function. They may include numeric constants,
alphanumeric literals, row and column references notation, E notation, or labels, or names
of other RECAP calculations.

Make sure that the values being passed to the function agree in number and type with the
arguments as coded in the function.

format2

Is the format of the return value, which must be enclosed in single quotation marks.

Example:

Calling a Function in a RECAP Command

Suppose you have a function named INVEST in your private collection of functions (INVEST is
not available in the supplied library), and it calculates an amount on the basis of cash on
hand, total assets, and the current date. In order to create a report that prints an account of
company assets and calculates how much money the company has available to invest, you
must create a report request that invokes the INVEST function.

The current date is obtained from the &YMD system variable. The NOPRINT option beside it
prevents the date from appearing in the report. The date is solely used as input for the next
RECAP statement.

1846

25. Creating Financial Reports With Financial Modeling Language (FML)

The request is:

TABLE FILE LEDGER
HEADING CENTER
"ASSETS AND MONEY AVAILABLE FOR INVESTMENT </2"
SUM AMOUNT ACROSS HIGHEST YEAR
IF YEAR EQ 1985 OR 1986
FOR ACCOUNT
1010 AS 'CASH'                                 LABEL CASH      OVER
1020 AS 'ACCOUNTS RECEIVABLE'                  LABEL ACR       OVER
1030 AS 'INTEREST RECEIVABLE'                  LABEL ACI       OVER
1100 AS 'FUEL INVENTORY'                       LABEL FUEL      OVER
1200 AS 'MATERIALS AND SUPPLIES'               LABEL MAT       OVER
BAR                                                            OVER
RECAP TOTCAS = CASH+ACR+ACI+FUEL+MAT; AS 'TOTAL ASSETS'        OVER
BAR                                                            OVER
RECAP THISDATE/A8 = &YMD; NOPRINT                              OVER
RECAP INVAIL = INVEST(CASH,TOTCAS,THISDATE,'D12.2'); AS
          'AVAIL. FOR INVESTMENT'                              OVER
BAR AS '='
END

The output is shown in the following image.

Inserting Rows of Free Text

Insert text anywhere in your FML report by typing it on a line by itself and enclosing it within
double quotation marks. You can also add blank lines, designated as text, to improve the
appearance of the report.

In addition, you can include data developed in your FML report in a row of free text by including
the label for the data variable in the text row.

Creating Reports With TIBCO® WebFOCUS Language

 1847

Inserting Rows of Free Text

Example:

Inserting Free Text

In this example, three rows of free text are inserted, one blank and two text rows.

TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
" --- CASH ACCOUNTS ---"             OVER
1010 AS 'CASH ON HAND'               OVER
1020 AS 'DEMAND DEPOSITS'            OVER
1030 AS 'TIME DEPOSITS'              OVER
" "                                  OVER
" --- OTHER CURRENT ASSETS ---"      OVER
1100 AS 'ACCOUNTS RECEIVABLE'        OVER
1200 AS 'INVENTORY'
END

The output is shown as follows.

                     AMOUNT
                     ------
 --- CASH ACCOUNTS ---
CASH ON HAND          8,784
DEMAND DEPOSITS       4,494
TIME DEPOSITS         7,961

 --- OTHER CURRENT ASSETS ---
ACCOUNTS RECEIVABLE  18,829
INVENTORY            27,307

Notice that the blank row was created by enclosing a blank within double quotation marks on a
separate line of the report request.

Syntax:

How to Insert Data Variables in Text Rows

"text <label[(c)][>]"

where:

<

Is a required left caret to bracket the label.

label

Is the explicit or implicit row label. (In a RECAP, the calculated value functions as the
label.)

Is an optional cell identifier that indicates the column number of the cell. However, this
identifier is required whenever there is more than one column in the report. If you use it,
enclose it in parentheses.

c

1848


25. Creating Financial Reports With Financial Modeling Language (FML)

>

Is an optional right caret that can be used to make the positioning clearer.

Example:

Inserting a Data Variable in a Text Row

In this example, the RECAP value CURASST is suppressed by the NOPRINT command, and
inserted instead as a data variable in the text row.

SET PAGE-NUM=OFF
TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
10$$ AS 'Cash'                   LABEL CA    OVER
1100 AS 'Accounts Receivable'    LABEL AR    OVER
1200 AS 'Inventory'              LABEL INV   OVER
RECAP CURASST/I5C = CA + AR + INV; NOPRINT   OVER
"Current Assets: <CURASST"
END

The output is shown in the following image.

                     AMOUNT
                     ------
Cash                 21,239
Accounts Receivable  18,829
Inventory            27,307
Current Assets: 67,375

Adding a Column to an FML Report

The request controls the number of columns in any report. For instance, if a request contains
the display command SUM AMOUNT AND FORECAST, the report contains two columns:
AMOUNT and FORECAST.

Add columns in an FML request, just as in a TABLE request, using the COMPUTE command to
calculate a value or simply to allocate the space, column title, and format for a column.

Example:

Adding a Column to an FML Report

This example uses a COMPUTE command to generate the calculated value CHANGE and
display it as a new column in the FML report. The following request generates an FML matrix
with four rows and three columns of data.

Creating Reports With TIBCO® WebFOCUS Language

 1849

Adding a Column to an FML Report

DEFINE FILE LEDGER
CUR_YR/I5C=AMOUNT;
LAST_YR/I5C=.87*CUR_YR - 142;
END

TABLE FILE LEDGER
SUM CUR_YR AS 'CURRENT,YEAR'
   LAST_YR AS 'LAST,YEAR'
COMPUTE CHANGE/I5C = CUR_YR - LAST_YR;
FOR ACCOUNT
1010 AS 'CASH ON HAND'                  OVER
1020 AS 'DEMAND DEPOSITS'               OVER
1030 AS 'TIME DEPOSITS'                 OVER
BAR                                     OVER
RECAP TOTCASH/I5C = R1 + R2 + R3; AS 'TOTAL CASH'
END

The output is shown in the following image.

Note: The designated calculation is performed on each tag or RECAP row of the report. The
RECAP rows, however, may change the calculation.

Adding a New Time Period as a Column

The following request adds a future time period to a report.

DEFINE FILE LEDGER
CUR_YR/P5C=AMOUNT;
LAST_YR/P5C=.87*AMOUNT - 142;
END

TABLE FILE LEDGER
SUM AMOUNT
ACROSS YEAR AND COMPUTE 1999/P5C = 2.5*AMOUNT;
FOR ACCOUNT
1010 AS 'CASH ON HAND'                   OVER
1020 AS 'DEMAND DEPOSITS'                OVER
1030 AS 'TIME DEPOSITS'                  OVER
BAR                                      OVER
RECAP TOTCASH/P5C = R1 + R2 + R3; AS 'TOTAL CASH' OVER
RECAP CHANGE(2,*) = TOTCASH(*) - TOTCASH(*-1);
END

1850



25. Creating Financial Reports With Financial Modeling Language (FML)

The output is shown as follows.

Creating Reports With TIBCO® WebFOCUS Language

 1851

Creating a Recursive Model

Creating a Recursive Model

Models involving different time periods often require using the ending value of one time period
as the starting value for the next. The calculations describing these situations have two
characteristics:

The labels on one or more RECAP rows are duplicates of other rows. They are used
repeatedly to recompute certain values.

A calculation may refer to a label not yet described, but provided later in the model. If, at
the end of the model, a label that is needed is missing, a message is displayed.

Recursive models require that the columns are produced in sequential order, one by one. In
nonrecursive models, all of the columns can be produced simultaneously. Schematically, these
patterns are shown as follows.

FML automatically switches to sequential order as soon as either of the two modeling
conditions requiring the switch is recognized (either reuse of labels by different rows, or
forward reference to a label in a calculation).

Example:

Creating a Recursive Model

The following example illustrates recursive models. Note that one year of ENDCASH becomes
the next year of STARTING CASH.

1852

25. Creating Financial Reports With Financial Modeling Language (FML)

DEFINE FILE REGION
CUR_YR=E_ACTUAL;
LAST_YR=.831*CUR_YR;
NEXT_YR=1.2297*CUR_YR;
END

TABLE FILE REGION
SUM LAST_YR CUR_YR NEXT_YR
FOR ACCOUNT
10$$ AS 'STARTING CASH' LABEL STCASH        OVER
RECAP STCASH(2,*) = ENDCASH(*-1);           OVER
" "                                         OVER
3000 AS 'SALES' LABEL SLS                   OVER
3100 AS 'COST' LABEL COST                   OVER
BAR                                         OVER
RECAP PROFIT/I5C = SLS - COST;              OVER
" "                                         OVER
RECAP ENDCASH/I5C = STCASH + PROFIT;
END

The output is shown as follows.

Reporting Dynamically From a Hierarchy

Hierarchical relationships between fields can be defined in a Master File, and automatically
displayed using the Financial Modeling Language (FML). The parent and child fields must share
data values, and their relationship should be hierarchical. The formats of the parent and child
fields must both be either numeric or alphanumeric.

For example, suppose that:

Employee and manager IDs are contained within an employee data source.

or

A general ledger data source contains both an account number field and an account parent
field.

Creating Reports With TIBCO® WebFOCUS Language

 1853


Reporting Dynamically From a Hierarchy

By examining these fields, it is possible to construct the entire organization chart or chart of
accounts structure. However, to print the chart in a traditional FML report, you need to list the
employee IDs or account numbers in the request syntax in the order in which they should
appear on the report. If an employee or account is added, removed, or transferred, you have to
change the report request to reflect this change in organizational structure. For example:

TABLE FILE EMPLOYEE
PRINT DEPARTMENT CURR_JOBCODE
FOR EMP_ID
999999999   OVER
222222222   OVER
 .
 .
 .

In contrast, with FML hierarchies you can define the hierarchical relationship between two
fields in the Master File and load this information into memory. The FML request can then
dynamically construct the rows that represent this relationship and display them in the report,
starting at any point in the hierarchy. In the example shown, EMP_ID is called the hierarchy
field.

Requirements for FML Hierarchies

1. In the Master File, use the PROPERTY=PARENT_OF and REFERENCE=hierarchyfld attributes
to define the hierarchical relationship between two fields. For more information, see the
Describing Data With WebFOCUS Language manual.

The hierarchy must be loaded into memory. This loaded hierarchy is called a chart. If the
hierarchy is defined in the Master File and referenced by the FML request, it is loaded
automatically. If you want to use a hierarchy defined in a Master File that is not either
referenced in the FML request or joined to the Master File referenced in the FML request,
issue the LOAD CHART command before issuing the FML request.

The number of charts that can be loaded is 16. Charts are automatically unloaded when
the session ends.

1854

25. Creating Financial Reports With Financial Modeling Language (FML)

2. In the FOR phrase of the FML request. Use the GET/WITH CHILDREN or ADD phrase to

retrieve the hierarchical data starting at a specific point in the hierarchy.

To use FML hierarchies, the FOR field must either be:

The hierarchy field.

or

Used as the join field to a unique segment that has the hierarchy field. In this case, the
hierarchy field must be the join field. Note that the condition that the join be unique only
applies if the hierarchy is defined in the cross-referenced segment.

In other words, the FOR field must be in a parent-child hierarchy, or linked to one. The latter
case allows transaction data that contains the hierarchy field to be joined to a separate data
source that contains the hierarchy definition.

As with any FML request, a tagged row is displayed even if no data is found in the file for the
tag values, with a period (.) representing the missing data. You can override this convention by
adding the phrase WHEN EXISTS to the definition of a tagged row. This makes displaying a row
dependent upon the existence of data for the tag.

Note: In order for the hierarchical indentations to be retained in HTML output, the setting
SHOWBLANKS=ON must be in effect.

Example:

Defining a Hierarchy in a Master File

The CENTGL Master File contains a charts of accounts hierarchy. The field
GL_ACCOUNT_PARENT is the parent field in the hierarchy. The field GL_ACCOUNT is the
hierarchy field. The field GL_ACCOUNT_CAPTION can be used as the descriptive caption for the
hierarchy field.

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
          PROPERTY=CAPTION, REFERENCE=GL_ACCOUNT, $
FIELDNAME=SYS_ACCOUNT,          ALIAS=ALINE,   FORMAT=A6,
          TITLE='System,Account,Line', MISSING=ON, $

Creating Reports With TIBCO® WebFOCUS Language

 1855

Reporting Dynamically From a Hierarchy

The CENTSYSF data source contains detail-level financial data. This is unconsolidated financial
data for a fictional corporation, CenturyCorp. It is designed to be separate from the CENTGL
database as if it came from an external accounting system. It uses a different account line
system (SYS_ACCOUNT) which can be joined to the SYS_ACCOUNT field in CENTGL. Data uses
natural signs (expenses are positive, revenue negative).

FILE=CENTSYSF     ,SUFFIX=FOC
SEGNAME=RAWDATA   ,SEGTYPE=S2
FIELDNAME=SYS_ACCOUNT   ,  ,A6       , FIELDTYPE=I,
          TITLE='System,Account,Line', $
FIELDNAME=PERIOD        ,  ,YYM      , FIELDTYPE=I, $
FIELDNAME=NAT_AMOUNT    ,  ,D10.0    , TITLE='Month,Actual', $
FIELDNAME=NAT_BUDGET    ,  ,D10.0    , TITLE='Month,Budget', $
FIELDNAME=NAT_YTDAMT    ,  ,D12.0    , TITLE='YTD,Actual', $

Displaying an FML Hierarchy

The GET CHILDREN and WITH CHILDREN commands dynamically retrieve and display
hierarchical data on the FML report. GET CHILDREN displays only the children, not the parent
value referenced in the command. WITH CHILDREN displays the parent and then the children.

Syntax:

How to Display an FML Hierarchy

TABLE FILE filename{PRINT|SUM} ...
FOR hierarchyfld
parentvalue {GET|WITH} CHILD[REN] [n|ALL]
 [AS CAPTION|'text'] [LABEL label]
.
.
.
END

where:

filename

Is the name of the file to be used in the FML request. If the hierarchy for this request
cannot be loaded automatically, it must have been loaded previously by issuing the LOAD
CHART command.

hierarchyfld

Is the hierarchy field name. If the request references a joined structure, the name must be
the field name from the host file. The alias name is not supported.

parentvalue

Is the parent value for which the children are to be retrieved.

1856

25. Creating Financial Reports With Financial Modeling Language (FML)

GET CHILDREN

Displays the hierarchy starting from the first child of the specified parentvalue. It does not
include the parent in the display. (This corresponds to the FML syntax CHILD1 OVER
CHILD2 OVER ...)

WITH CHILDREN

Displays the hierarchy starting from the specified parentvalue. It includes the parent in the
display. (This corresponds to the FML syntax parentvalue OVER CHILD1 OVER CHILD2
OVER ...).

n|ALL

Is a positive integer from 1 to 99, specifying the number of levels of the hierarchy to
display. If a number greater than 99 is specified, a warning message is displayed and n is
set to 99. The default value is 1. Therefore, if n is omitted, only direct children are
displayed. GET or WITH CHILDREN 2 displays direct children and grandchildren. GET or
WITH CHILDREN 99 displays children to 99 levels. ALL is a synonym for 99. Each child
instance is printed over the one that follows. Successive levels of the hierarchy field are
indented two spaces from the previous level.

CAPTION

Indicates that the caption values to display should be taken from the field defined as the
CAPTION in the Master File.

Note that the AS CAPTION phrase is supported for tagged rows, including those that do not
use the GET/WITH CHILDREN or ADD syntax. However, the hierarchy must be defined (by
specifying the PARENT_OF attribute) in order to load and display the caption values. If the
hierarchy is not defined, the AS CAPTION phrase is ignored.

'text'

Is a text string to use as the row title for the hierarchy field values. The CAPTION field
defined in the Master File is not used as the caption on the report output.

label

Is an explicit row label. Each generated row is labeled with the specified label text.

Note: The hierarchy is displayed sorted by the parent field and, within parent, sorted by the
hierarchy field.

For information about the FMLFOR, FMLLIST, FMLCAP, and FMLINFO functions that return the
tag values and captions used in an FML request, see the Using Functions manual.

Creating Reports With TIBCO® WebFOCUS Language

 1857

Reporting Dynamically From a Hierarchy

Example:

Displaying an FML Hierarchy

The following request displays two levels of account numbers, starting from account 3000:

SET SHOWBLANKS=ON
TABLE FILE CENTGL
PRINT GL_ACCOUNT_PARENT
FOR GL_ACCOUNT
3000 WITH CHILDREN 2
END

The output is shown as follows.

             Parent
             ------
3000         1000
  3100       3000
    3110     3100
    3120     3100
    3130     3100
    3140     3100
    3200     3000
    3300     3200
    3400     3200
    3500     3200
    3600     3200
    3700     3200
    3800     3200
    3900     3200

Note:

If the request specifies GET CHILDREN instead of WITH CHILDREN, the line for the parent
value (3000) does not display on the report output.

In order to retain the indentations in HTML output, the SET SHOWBLANKS=ON command
must be in effect.

1858

25. Creating Financial Reports With Financial Modeling Language (FML)

Displaying an FML Hierarchy With Captions

The following request displays two levels of a chart of accounts hierarchy, starting with account
1000 (the top of the hierarchy), and displays the caption field values instead of the account
numbers.

SET SHOWBLANKS=ON
TABLE FILE CENTGL
PRINT GL_ACCOUNT_PARENT
FOR GL_ACCOUNT
1000 WITH CHILDREN 2 AS CAPTION
END

The output is shown as follows.

                                    Parent
                                    ------
Profit Before Tax
  Gross Margin                      1000
    Sales Revenue                   2000
    Cost Of Goods Sold              2000
  Total Operating Expenses          1000
    Selling Expenses                3000
    General + Admin Expenses        3000
  Total R+D Costs                   1000
    Salaries                        5000
    Misc. Equipment                 5000

Note: If the request specifies GET CHILDREN instead of WITH CHILDREN, the line for the
parent value (1000, Profit Before Tax) does not display on the report output.

Consolidating an FML Hierarchy

The ADD command consolidates multiple levels of the hierarchy on one line of the FML report
output. You can use ADD alone or in conjunction with GET CHILDREN or WITH CHILDREN. Note
that ADD is designed to work with requests that use the SUM command. It is also designed to
be used with detail-level data, not data that is consolidated.

When used alone, ADD aggregates the parent and children on one line of the report output,
summing the numeric data values included on the line. This corresponds to the FML syntax
parentvalue or CHILD1 OR CHILD2 OR ...

When used in conjunction with GET CHILDREN, ADD displays one line for each child of the
specified parent value. Each line is a summation of that child and all of its children. You can
specify the number of levels of children to display (which determines the number of lines
generated on the report output) and the depth of summation under each child. By default, only
direct children have a line in the report output, and the summary for each child includes all of
its children.

Creating Reports With TIBCO® WebFOCUS Language

 1859

Reporting Dynamically From a Hierarchy

When used in conjunction with WITH CHILDREN, ADD first displays a line in the report output
that consists of the summation of the parent value and all of its children. Then it displays
additional lines identical to those displayed by GET CHILDREN ADD.

In order to use a data record in more than one line of an FML report (for example, to display
both detail and summary lines or to consolidate detail data at multiple levels), the following
setting is required:

SET FORMULTIPLE=ON

Syntax:

How to Create One Summary Row for an FML Hierarchy

TABLE FILE filenameSUM ...
FOR hierarchyfld
parentvalue ADD [n|ALL]
 [AS CAPTION|'text'] [LABEL label]
.
.
.
END

where:

filename

Is the name of the file to be used in the FML request. If the hierarchy for this request
cannot be loaded automatically, it must have been loaded previously by issuing the LOAD
CHART command.

hierarchyfld

Is the hierarchy field name. If the request references a joined structure, the name must be
the field name from the host file. The alias name is not supported.

parentvalue

Is the parent value that determines the starting point in the hierarchy for the aggregation.

ADD

Displays the parent and n levels of its children on one row, summing the numeric data
values displayed on the row. This corresponds to the FML syntax parentvalue or CHILD1
OR CHILD2 OR CHILD3 and more, if applicable.

1860

25. Creating Financial Reports With Financial Modeling Language (FML)

To display the sum of just the children, you must display the parent row, display the
summary row, and use a RECAP to subtract the parent row from the sum. For example:

FOR ...
parentvalue                 OVER
parentvalue ADD 1           OVER
RECAP CHILDSUM = R2-R1;

n|ALL

Is a positive integer from 1 to 99, specifying the number of levels of the hierarchy to
aggregate. ALL is the default value. Therefore, if n is omitted, all children are included in
the sum. If n is 1, only direct children are included. If n is 2, direct children and
grandchildren are included. ADD 99 includes up to 99 levels of children. ALL is a synonym
for 99.

CAPTION

Indicates that the caption of the parent value displays for the total row.

Note that the AS CAPTION phrase is supported for tagged rows, including those that do not
use the GET CHILDREN or ADD syntax. However, the hierarchy must be defined (by
specifying the PARENT_OF attribute) in order to load and display the caption values. If the
hierarchy is not defined, the AS CAPTION phrase is ignored.

'text'

Is a text string to use as the row title for the aggregate row. The CAPTION field defined in
the Master File is not used as the caption on the report output.

label

Is an explicit row label. Each generated row is labeled with the specified label text.

Creating Reports With TIBCO® WebFOCUS Language

 1861

Reporting Dynamically From a Hierarchy

Example:

Displaying One Summary Line for an FML Hierarchy

The CENTSYSF data source contains detail-level financial data. To use the account hierarchy in
the CENTGL data source with this financial data, the two data sources are joined. The data in
CENTSYSF is stored with natural signs, which means, in financial terms, that revenues and
liabilities are stored as negative numbers. The portion of the hierarchy used in this request
contains only positive data.

Note that the join is not required to be unique, because the hierarchy is defined in the host
segment.

First the WITH CHILDREN command displays the lines of the hierarchy starting with account
Selling Expenses (3100). Note that only accounts with no children are populated in this detail-
level data source. The ADD command then creates one line that is the sum of account 3100
and all of its children.

SET SHOWBLANKS=ON
SET FORMULTIPLE=ON
JOIN SYS_ACCOUNT IN CENTGL TO ALL SYS_ACCOUNT IN CENTSYSF
TABLE FILE CENTGL
SUM NAT_AMOUNT/D10.0 NAT_YTDAMT/D10.0
FOR GL_ACCOUNT
3100 WITH CHILDREN ALL AS CAPTION OVER
BAR                               OVER
3100 ADD AS CAPTION
IF PERIOD EQ '2002/03'
END

The output is shown as follows.

1862

25. Creating Financial Reports With Financial Modeling Language (FML)

Syntax:

How to Consolidate FML Hierarchy Data to Any Level and Depth

TABLE FILE filename
SUM ...
FOR hierarchyfld
parentvalue {GET|WITH} CHILD[REN] [n|ALL] ADD [m|ALL]
 [AS CAPTION|'text'] [LABEL label]
.
.
.
END

where:

filename

Is the name of the file used in the FML request. If the hierarchy for this request cannot
load automatically, it previously loaded by issuing the LOAD CHART command.

hierarchyfld

Is the hierarchy field name. If the request references a joined structure, the name must be
the field name from the host file. The alias name is not supported.

parentvalue

Is the parent value that determines the starting point in the hierarchy for the aggregation.

GET|WITH

GET specifies that the first line generated on the report is the consolidated line for the first
child of the parent value. WITH specifies that the first line generated on the report is the
consolidated line for the parent value, followed by the consolidated lines for each of its
children, to the level specified by n.

n|ALL

Is a positive integer from 1 to 99, specifying the number of levels of children to display.
The line of output for each child has the sum of that child and its children to the depth
specified for the ADD option. The default value is 1. Therefore, if n is omitted, each direct
child has a line on the report. If n is 2, direct children and grandchildren each have a line
on the report output. ALL is a synonym for 99.

ADD

Sums the hierarchy to the depth specified by m for each line generated by the GET or WITH
CHILDREN command.

Creating Reports With TIBCO® WebFOCUS Language

 1863

Reporting Dynamically From a Hierarchy

m|ALL

Is a positive integer from 1 to 99, specifying the number of levels of children to
consolidate on each line of the report output. If a number greater than 99 is specified, a
warning message is displayed and m is set to 99. The default value is ALL. Therefore, if m
is omitted, the consolidated line sums all children. If m is 2, only direct children and
grandchildren are consolidated for each line on the report output. ADD 99 aggregates
children to 99 levels. ALL is a synonym for 99.

CAPTION

Indicates that the caption of the parent value displays for the total row.

Note that the AS CAPTION phrase is supported for tagged rows, including those that do not
use the GET CHILDREN or ADD syntax. However, the hierarchy must be defined (by
specifying the PARENT_OF attribute) in order to load and display the caption values. If the
hierarchy is not defined, the AS CAPTION phrase is ignored.

'text'

Is a text string to use as the row title for the aggregate row. The CAPTION field defined in
the Master File is not used as the caption on the report output.

label

Is an explicit row label. Each generated row is labeled with the specified label text.

Example:

Consolidating FML Hierarchy Data

In the following request, the first WITH CHILD command displays the detail data for the
hierarchy starting with account 3100. The next WITH CHILD command creates a consolidated
line for the parent account (3100) and each direct child.

SET SHOWBLANKS=ON
SET FORMULTIPLE=ON
JOIN SYS_ACCOUNT IN CENTGL TO ALL SYS_ACCOUNT IN CENTSYSF
TABLE FILE CENTGL
SUM NAT_AMOUNT/D10.0 NAT_YTDAMT/D10.0
FOR GL_ACCOUNT
3100 WITH CHILDREN ALL AS CAPTION      OVER
" "                                    OVER
BAR AS =                               OVER
" "                                    OVER
3100 WITH CHILDREN ADD AS CAPTION
IF PERIOD EQ '2002/03'
END

Note that the join is not required to be unique, because the hierarchy is defined in the host
segment.

1864

25. Creating Financial Reports With Financial Modeling Language (FML)

In the following output, the top portion shows the detail-level data. The bottom portion shows
the consolidated data. In the consolidated portion of the report:

There is one line for the parent that is the sum of itself plus all of its children to all levels.

There is one line for each direct child of account Selling Expenses (3100): Advertising,
Promotional Expenses, Joint Marketing, and Bonuses/Commisions.

The line for Advertising is the sum of itself plus all of its children. If it has multiple levels of
children, they are all added into the sum. The other direct children of 3100 do not
themselves have children, so the sum on each of those lines consists of only the parent
value.

Creating Reports With TIBCO® WebFOCUS Language

 1865

Reporting Dynamically From a Hierarchy

Using GET CHILDREN instead of WITH CHILDREN eliminates the top line from each portion of
the output. The remaining lines are the same.

1866

25. Creating Financial Reports With Financial Modeling Language (FML)

The following request displays a consolidated line for account 2000 and each of its direct
children and grandchildren.

SET SHOWBLANKS=ON
SET FORMULTIPLE=ON
JOIN SYS_ACCOUNT IN CENTGL TO ALL SYS_ACCOUNT IN CENTSYSF
TABLE FILE CENTGL
SUM NAT_AMOUNT/D10.0 NAT_YTDAMT/D10.0
FOR GL_ACCOUNT
2000 WITH CHILDREN 2 ADD AS CAPTION
IF PERIOD EQ '2002/03'
END

The output is shown as follows.

Loading a Hierarchy Manually

In most cases, a hierarchy loads automatically as a result of the request syntax. However, if
you need to use a hierarchy defined in one Master File against a data source that is not joined
to the hierarchy file (but that contains the same hierarchy field), you can manually load the
hierarchy data using the LOAD CHART command.

The number of charts that can load is limited by available memory. Charts automatically unload
when the session ends.

The chart loads by running a TABLE request that produces a list of parent values and their
associated children.

TABLE FILE chartfile
BY parentfield BY hierarchyfield
[SUM captionfield]
END

Creating Reports With TIBCO® WebFOCUS Language

 1867

Reporting Dynamically From a Hierarchy

The resulting chart contains the following information. It may also contain the associated
captions, depending on whether the AS CAPTION phrase was used in the request.

parentfield     hierarchyfield
-----------     --------------
parentvalue1    child1
parentvalue1    child2
parentvalue2    child3
  .
  .
  .

Syntax:

How to Load a Hierarchy From One Master File for Use With a Separate Master File

You can manually load the hierarchy data, if you need to use a hierarchy defined in one Master
File, against a data source that is not joined to the hierarchy file but that contains the same
hierarchy field.

Available memory dictates the number of charts that can load. Charts automatically unload
when WebFOCUS terminates.

LOAD CHART chartfile[.sega].hierarchyfld
   [FOR requestfile[[.segb].fieldb]]

where:

chartfile

Is the name of the Master File that contains the hierarchy information.

sega

Is the name of the segment that contains the hierarchy field. The segment name is only
required if a field in another segment in the structure has the same field name as the
hierarchy field.

hierarchyfld

Is the hierarchy field. It is required because a Master File can define multiple hierarchies.

FOR

Loads a hierarchy defined in a Master File that is not used in the FML report request. For
example, if Master File B contains the hierarchy information but Master File A is used in
the request (without a join between Master Files A and B), issue the following LOAD CHART
command prior to the FML request:

LOAD CHART B.FLDB FOR A.FLDA
TABLE FILE A ...

1868

25. Creating Financial Reports With Financial Modeling Language (FML)

requestfile

Is the name of the Master File used in the FML request.

segb

Is the name of the segment that contains the hierarchy field values in the Master File used
in the FML request. It is not required if it has the same name as sega.

fieldb

Is the field in the Master File specified in the FML request that contains the values of the
hierarchy field. It is not required if it has the same name as the hierarchy field.

Note:

If you issue the LOAD CHART command multiple times for the same hierarchy, the new
hierarchy overlays the previous version in memory.

If you issue the LOAD CHART command for a data source that is dynamically joined to the
hierarchy file, you must issue the JOIN command prior to issuing the LOAD CHART
command.

Reference: Usage Notes for FML Hierarchies

PROPERTY and REFERENCE are propagated to HOLD Master Files when HOLDATTR is set to
ON.

The following setting is required in order to use a data record in more than one row of an
FML request (for example, both a detail and summary row):

SET FORMULTIPLE=ON

When reporting against a rolled-up data source such as ESSBASE, the data values stored
for the parent instance are an aggregate of all of its children. Do not use the ADD feature
on consolidated data.

When reporting against a data source with shared members (such as ESSBASE), in which
the same data can be defined multiple times with different hierarchy field values, data
shared by two different parents is counted twice in an aggregation operation. To avoid this
double aggregation, use the FST operator in the SUM command for the shared fields.

When the report output is in HTML format, the setting SHOWBLANKS=ON must be in effect
in order to retain the hierarchical indentations.

Creating Reports With TIBCO® WebFOCUS Language

 1869

Customizing a Row Title

Customizing a Row Title

You can customize a row title in an FML report for accurate data identification. Using the AS
phrase, you can provide new titles for TAG, DATA, RECAP, and PICKUP rows.

Syntax:

How to Customize a Row Title in FML

For a TAG row, use the syntax:

value AS {'title'|CAPTION}

For a DATA or PICKUP row, use the syntax:

value AS 'title'

For a RECAP row, use the syntax:

RECAP calcname[/format]=expression; AS 'title'

where:

value

Is the value on which you are reporting, whether retrieved from a data source or external
file (represented by a tag), supplied directly by a user in the request, or picked up from a
work file.

title

Is the customized row title, enclosed in single quotation marks if it contains embedded
blanks.

In a TAG, DATA, or PICKUP row, the default row title is value.

In a RECAP row, the default title is calcname.

CAPTION

In the Master File of a hierarchical data source, CAPTION identifies a TAG row using a
caption field. Note that the hierarchy in the Master File defines the PARENT-OF the FOR
field.

calcname

Is the value that is derived by the RECAP calculation.

Example:

Changing the Titles of Tag Rows

In the following example, the row titles CASH ON HAND and DEMAND DEPOSITS provide
meaningful identifications for the corresponding tags.

1870

25. Creating Financial Reports With Financial Modeling Language (FML)

TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
1010 AS 'CASH ON HAND' OVER
1020 AS 'DEMAND DEPOSITS'
END

Note that single quotation marks are necessary since the row title being assigned has
embedded blanks.

The output is shown as follows.

                 AMOUNT
                 ------
CASH ON HAND      8,784
DEMAND DEPOSITS   4,494

If no AS phrase is included, the tag values are displayed in the report.

Customizing a Row Title for a RECAP Value

This request creates the title TOTAL CASH for the RECAP value TOTCASH.

TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
1010 AS 'CASH ON HAND'      OVER
1020 AS 'DEMAND DEPOSITS'   OVER
1030 AS 'TIME DEPOSITS'     OVER
RECAP TOTCASH = R1 + R2 + R3; AS 'TOTAL CASH'
END

The output is shown as follows.

                 AMOUNT
                 ------
CASH ON HAND      8,784
DEMAND DEPOSITS   4,494
TIME DEPOSITS     7,961
TOTAL CASH       21,239

If no AS phrases are included, the name of the RECAP value (TOTCASH) displays in the report.

Formatting an FML Report

Improve the readability and presentation of your FML report by:

Underlining numeric columns. Reports with columns of numbers frequently need to display
underlines before some RECAP calculations. You can specify an underline character,
introduced by the word BAR, in place of the tag value.

Adding page breaks. You can request a new page at any point in a report by placing the
word PAGE-BREAK in place of the tag value.

Creating Reports With TIBCO® WebFOCUS Language

 1871

Formatting an FML Report

Formatting rows, columns, and cells. You can apply StyleSheet attributes, such as FONT,
SIZE, STYLE, and COLOR, to individual rows and columns, or to cells within those rows.

Adding borders around rows, columns, and cells. You can use BORDER attributes in a
StyleSheet to specify the weight, style, and color of border lines around a row or cell. You
can specify formatting variations for the top, bottom, left, and right borders.

Indenting text or numbers. You can indent a tag value, label text, or caption text a
specified number of spaces for an FML tag row, hierarchy, or RECAP row. If you apply the
indent to rows in an FML hierarchy, the parent line of the hierarchy is indented the number
of spaces specified as the indent.

Note: For an HTML, PDF, or PostScript report, you can use the BLANKINDENT setting to
specify an indentation between levels of an FML hierarchy. See Indenting Row Titles in an
FML Hierarchy on page 1889.

Syntax:

How to Add an Underline Character for Columns

BAR [AS 'character'] OVER

where:

character

Is either the hyphen character (-) or the equal character (=). Enclose the character in
single quotation marks. The default character is the hyphen (-).

Example:

Underlining Columns

This example uses the default underscore character (_).

TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
1010 AS 'CASH ON HAND'       OVER
1020 AS 'DEMAND DEPOSITS'    OVER
1030 AS 'TIME DEPOSITS'      OVER
BAR                          OVER
RECAP TOTCASH = R1 + R2 + R3;
END

The output is shown as follows.

                 AMOUNT
                 ------
CASH ON HAND      8,784
DEMAND DEPOSITS   4,494
TIME DEPOSITS     7,961
                 ------
TOTCASH          21,239

1872

25. Creating Financial Reports With Financial Modeling Language (FML)

Notice that the BAR ... OVER phrase underlines only the column containing the display field.

Syntax:

How to Specify a Page Break in an FML Report

Include the following syntax in the FML request in place of a tag value.

PAGE-BREAK OVER

Example:

Specifying a Page Break in an FML Report

In this example, a page break is inserted after the first two RECAP commands to highlight each
calculation.

TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
1010 AS 'CASH ON HAND'                                    OVER
1020 AS 'DEMAND DEPOSITS'                                 OVER
1030 AS 'TIME DEPOSITS'                                   OVER
BAR                                                       OVER
RECAP TOTCASH = R1 + R2 + R3; AS 'TOTAL CASH'             OVER
PAGE-BREAK                                                OVER
1100 AS 'ACCOUNTS RECEIVABLE' LABEL RECEIVE               OVER
1200 AS 'INVENTORY'  LABEL INVENT                         OVER
BAR                                                       OVER
RECAP TOTASSET = RECEIVE + INVENT; AS 'TOTAL ASSETS'      OVER
PAGE-BREAK                                                OVER
RECAP TOTAL = TOTCASH + TOTASSET;
END

Creating Reports With TIBCO® WebFOCUS Language

 1873

Formatting an FML Report

The output is shown as follows.

Syntax:

How to Format a Row, Column, or Cell in an FML Report

TYPE=type, [COLUMN=column] [LABEL={Rn|label}], format_def, $

where:

type

Identifies the component you wish to format. Valid values are:

REPORT denotes a row with the specified label.

DATA denotes a row with the specified label, which contains user-supplied data values.

FREETEXT denotes a free text or a blank row with the specified label.

1874

25. Creating Financial Reports With Financial Modeling Language (FML)

UNDERLINE denotes underlines generated by BAR. Formatting of an underline is supported
for PDF and PS, but not for HTML reports.

column

Identifies a specific column. You can identify the column by its name or position in a row.

LABEL

Is the controlling factor in identifying and formatting an FML row.

Note that the label is used to identify a row for calculation or formatting. The label for a
TAG or DATA row never appears in the report output. It is used only to identify rows within
the FML code. For a RECAP row, the name of the calculated value serves as a label. It
appears in the report unless an alternate title is specified.

label is an explicit row label that you can assign to identify a row more clearly.

format_def

Is the formatting definition, such as FONT, SIZE, STYLE, and COLOR. See Formatting an
FML Report on page 1871.

Note: To format a cell, identify the cell as the intersection of a column and a row using
COLUMN= ... plus LABEL= ... in the same StyleSheet declaration.

Example:

Formatting Rows in an FML Report

The following illustrates how to identify and format an entire FML row, consisting of the row
label and the row data. The LABEL attribute in the StyleSheet identifies the three TAG rows,
which are styled here as italic.

SET PAGE-NUM=OFF
TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
1010 AS 'CASH ON HAND' LABEL COH OVER
1020 AS 'DEMAND DEPOSITS' LABEL DD OVER
1030 AS 'TIME DEPOSITS' LABEL TD OVER
BAR OVER
RECAP TOTCASH = R1 + R2 + R3; AS 'TOTAL CASH'
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID = OFF, $
TYPE = REPORT, LABEL = COH, STYLE = ITALIC, $
TYPE = REPORT, LABEL = DD,  STYLE = ITALIC, $
TYPE = REPORT, LABEL = TD,  STYLE = ITALIC, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1875

Formatting an FML Report

The output is shown in the following image.

Applying Boldface to a TAG Row in an FML Report

This request applies boldface to the customized row title, CASH, and to the related data in the
AMOUNT column. The StyleSheet uses the explicit label CA to identify the component to
format.

SET PAGE-NUM=OFF
TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
10$$ AS 'CASH'                LABEL CA   OVER
1100 AS 'ACCOUNTS RECEIVABLE' LABEL AR   OVER
1200 AS 'INVENTORY'           LABEL INV  OVER
RECAP CURASST/I5C = CA + AR + INV;
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID = OFF, $
TYPE = REPORT, LABEL = CA, STYLE = BOLD, $
ENDSTYLE
END

The output is shown in the following image.

Applying Boldface to a Cell in an FML Matrix

This request generates a report in which the data value for AMOUNT is bold in the row titled
CASH. However, the row title CASH is not bold. This is accomplished by pinpointing the cell in
the StyleSheet declaration. In this case, the column (N2) within the row (CA).

1876

25. Creating Financial Reports With Financial Modeling Language (FML)

SET PAGE-NUM=OFF
TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
10$$ AS 'CASH'                LABEL CA   OVER
1100 AS 'ACCOUNTS RECEIVABLE' LABEL AR   OVER
1200 AS 'INVENTORY'           LABEL INV  OVER
RECAP CURASST/I5C = CA + AR + INV;
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID = OFF, $
TYPE = REPORT, COLUMN = N2, LABEL = CA, STYLE = BOLD, $
ENDSTYLE
END

The output is shown in the following image.

Applying Boldface to a Column in an FML Report

This request identifies the AMOUNT column by name and formats its title and data in bold. The
same result is achieved if the column is identified as N2.

SET PAGE-NUM=OFF
TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
"---CASH ACCOUNTS---"                   OVER
1010 AS 'CASH ON HAND'                  OVER
1020 AS 'DEMAND DEPOSITS'               OVER
1030 AS 'TIME DEPOSITS'                 OVER
" "                                     OVER
"---OTHER CURRENT ASSETS---"            OVER
1100 AS 'ACCOUNTS RECEIVABLE'           OVER
1200 AS 'INVENTORY'
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID = OFF, $
TYPE = REPORT, COLUMN = AMOUNT, STYLE = BOLD, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1877

Formatting an FML Report

The output is shown in the following image.

Applying Boldface to a Free Text Row

This request styles the free text as bold. Since in this example the same styling applies to
both free text rows, labels are not required to distinguish between them.

SET PAGE-NUM=OFF
TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
"---CASH ACCOUNTS---"  LABEL CA         OVER
1010 AS 'CASH ON HAND'                  OVER
1020 AS 'DEMAND DEPOSITS'               OVER
1030 AS 'TIME DEPOSITS'                 OVER
" "                                     OVER
"---OTHER CURRENT ASSETS---"  LABEL OCA OVER
1100 AS 'ACCOUNTS RECEIVABLE'           OVER
1200 AS 'INVENTORY'
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID = OFF, $
TYPE = FREETEXT, STYLE = BOLD, $
ENDSTYLE
END

1878

25. Creating Financial Reports With Financial Modeling Language (FML)

The output is shown in the following image.

Formatting Free Text Rows Separately in an FML Report

This request uses the SIZE attribute to distinguish two lines of free text: CASH ACCOUNTS and
OTHER CURRENT ASSETS. The labels CA and OCA are used to identify and format each row
separately.

SET PAGE-NUM=OFF
TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
" --- CASH ACCOUNTS ---" LABEL CA            OVER
1010 AS 'CASH ON HAND'                       OVER
1020 AS 'DEMAND DEPOSITS'                    OVER
1030 AS 'TIME DEPOSITS'                      OVER
" "                                          OVER
" --- OTHER CURRENT ASSETS ---" LABEL OCA    OVER
1100 AS 'ACCOUNTS RECEIVABLE'                OVER
1200 AS 'INVENTORY'
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID = OFF, $
TYPE = FREETEXT, LABEL = CA, STYLE = BOLD, SIZE = 12, $
TYPE = FREETEXT, LABEL = OCA, STYLE = BOLD, SIZE = 10, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1879

Formatting an FML Report

The output is shown in the following image.

Styling Text and a Variable in a Free Text Row

In this example, the text and variable components of the free text row are styled separately.
The text, Current Assets, is italic and the value derived from the RECAP calculation is bold.

SET PAGE-NUM=OFF
TABLE FILE LEDGER
SUM AMOUNT AS 'Amount' FOR ACCOUNT
10$$ AS 'Cash'                   LABEL CA    OVER
1100 AS 'Accounts Receivable'    LABEL AR    OVER
1200 AS 'Inventory'              LABEL INV   OVER
RECAP CURASST/I5C = CA + AR + INV; NOPRINT  OVER
"Current Assets: <CURASST"
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID=OFF, $
TYPE = FREETEXT, OBJECT = TEXT, ITEM = 1, SIZE = 12, STYLE = ITALIC, $
TYPE = FREETEXT, OBJECT = FIELD, ITEM = 1, STYLE = BOLD, $
ENDSTYLE
END

The output is shown in the following image.

1880

25. Creating Financial Reports With Financial Modeling Language (FML)

Applying Boldface to an FML RECAP Row

This request applies boldface to the row title and calculated value in a RECAP row. Notice that
the RECAP label in the StyleSheet is TOTCASH. In a RECAP, the name assigned to the
calculated value serves as the explicit label.

SET PAGE-NUM=OFF
TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
1010 AS 'CASH ON HAND'    LABEL CASH    OVER
1020 AS 'DEMAND DEPOSITS' LABEL DD      OVER
1030 AS 'TIME DEPOSITS'   LABEL TD      OVER
RECAP TOTCASH = R1 + R2 + R3; AS 'TOTAL CASH'
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID = OFF, $
TYPE = REPORT, LABEL = TOTCASH, STYLE = BOLD, $
TYPE = REPORT, LABEL = CASH, COLUMN = N1, STYLE = ITALIC, $
TYPE = REPORT, LABEL = DD, COLUMN = N1, STYLE = ITALIC, $
TYPE = REPORT, LABEL = TD, COLUMN = N1, STYLE = ITALIC, $
ENDSTYLE
END

The output is shown in the following image.

Syntax:

How to Add and Format Row and Cell Borders

To request a uniform border around a row or cell, use this syntax:

TYPE=REPORT, LABEL=row_label, [COLUMN=column,] BORDER=option,
[BORDER-STYLE=line_style,] [BORDER-COLOR={color|RGB® g b)},] $

To specify different characteristics for the top, bottom, left, and/or right borders, use this
syntax:

TYPE=REPORT, LABEL=row_label, [COLUMN=column,] BORDER-position=option,
[BORDER-[position-]STYLE=line_style,]
[BORDER-[position-]COLOR={color|RGB(r g b)},] $

To specify different characteristics for the top, bottom, left, and/or right borders, use this
syntax:

Creating Reports With TIBCO® WebFOCUS Language

 1881

Formatting an FML Report

TYPE=REPORT, LABEL=row_label, [COLUMN=column,] BORDER-position=option,
[BORDER-[position-]STYLE=line_style,]
[BORDER-[position-]COLOR={color|RGB(r g b)},] $

where:

row_label

Is the row to which the specified border characteristics are applied.

column

Used in conjunction with row label. Designates a cell (at the point of intersection of the
row and the column) to which the specified border characteristics are applied.

option

Can be one of the following values:

ON turns borders on for the entire heading or footing. ON generates the same line as
MEDIUM.

OFF turns borders off for the entire heading or footing. OFF is the default.

LIGHT specifies a thin line. You can specify a light line for the entire heading or footing, or
for one or more border positions.

MEDIUM identifies a medium line (ON sets the line as MEDIUM). You can specify a light line
for the entire heading or footing, or for one or more border positions. Note that the
medium line setting ensures consistency with lines created with GRID attributes.

HEAVY identifies a thick line. You can specify a heavy line for the entire heading or footing,
or for one or more border positions.

width specifies the line width in points (where 72 pts=1 inch). You can specify a line
width in points for the entire heading or footing or for one or more border positions. Line
width specified in points is displayed differently in HTML and PDF output. For uniform
appearance, regardless of display format, use LIGHT, MEDIUM, or HEAVY.

position

Specifies which border line to format. Valid values are TOP, BOTTOM, LEFT, RIGHT.

You can specify a position qualifier for any of the BORDER keywords. This enables you to
format line width, line style, and line color individually, for any side of the border.

1882

25. Creating Financial Reports With Financial Modeling Language (FML)

line_style

Sets the style of the border line. WebFOCUS StyleSheets support all of the standard
Cascading Style Sheets line styles. Several 3-dimensional styles are only available in
HTML, as noted by asterisks. Valid values are:

NONE
SOLID
DOTTED
DASHED
DOUBLE*
GROOVE*
RIDGE*
INSET*
OUTSET*

color

Is one of the preset color values. The default value is BLACK.

If the display or output device does not support colors, it substitutes shades of gray.

RGB

Specifies the font color using a mixture of red, green, and blue.

(r g b)

Is the desired intensity of red, green, and blue, respectively. The values are on a scale of 0
to 255, where 0 is the least intense and 255 is the most intense. Note that using the
three color components in equal intensities results in shades of gray.

Note: For HTML reports, the BORDERS feature requires that cascading style sheets be turned
ON. This code is not required for PDF and PS reports.

Example:

Emphasizing a Row Using Uniform Border Lines

This example places a dashed border of medium thickness around the RECAP row identified by
the label TOTCASH. For HTML reports, the BORDERS feature requires that cascading style
sheets be turned ON.

Creating Reports With TIBCO® WebFOCUS Language

 1883

Formatting an FML Report

SET PAGE-NUM=OFF
TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
1010 AS 'CASH ON HAND'    LABEL CASH    OVER
1020 AS 'DEMAND DEPOSITS' LABEL DD      OVER
1030 AS 'TIME DEPOSITS'   LABEL TD      OVER
RECAP TOTCASH = R1 + R2 + R3; AS 'TOTAL CASH'
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID = OFF, $
TYPE = REPORT, LABEL = TOTCASH, BORDER = MEDIUM,
  BORDER-STYLE = DASHED, $
ENDSTYLE
END

The output is shown in the following image.

1884

25. Creating Financial Reports With Financial Modeling Language (FML)

Example:

Emphasizing a Row Using Different Top/Bottom and Left/Right Borders

This example places a heavy black border line above and below the RECAP row identified by
the label TOTCASH, and a thin silver dotted line to the left and right of each column in the row.

For HTML reports, the BORDERS feature requires that cascading style sheets be turned ON.

SET PAGE-NUM=OFF
TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
1010 AS 'CASH ON HAND'    LABEL CASH    OVER
1020 AS 'DEMAND DEPOSITS' LABEL DD      OVER
1030 AS 'TIME DEPOSITS'   LABEL TD      OVER
RECAP TOTCASH = R1 + R2 + R3; AS 'TOTAL CASH'
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID = OFF,$
TYPE = REPORT, LABEL = TOTCASH,
     BORDER-TOP = HEAVY,
     BORDER-BOTTOM = HEAVY,
     BORDER-LEFT = LIGHT,
     BORDER-RIGHT = LIGHT,
     BORDER-TOP-STYLE = SOLID,
     BORDER-BOTTOM-STYLE = SOLID,
     BORDER-LEFT-STYLE = DOTTED,
     BORDER-RIGHT-STYLE = DOTTED,
     BORDER-LEFT-COLOR = 'SILVER',
     BORDER-RIGHT-COLOR = 'SILVER', $
ENDSTYLE
END

The output is shown in the following image.

Example:

Adding Uniform Border Lines Around a Cell

This example places a border of medium thickness around the cell in the second column of the
row identified by the label TOTCASH. The combined LABEL and COLUMN specifications are
identified in the cell. The BORDERS feature requires that cascading style sheets be turned ON.

Creating Reports With TIBCO® WebFOCUS Language

 1885

Formatting an FML Report

SET PAGE-NUM=OFF
TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
1010 AS 'CASH ON HAND'    LABEL CASH    OVER
1020 AS 'DEMAND DEPOSITS' LABEL DD      OVER
1030 AS 'TIME DEPOSITS'   LABEL TD      OVER
RECAP TOTCASH = R1 + R2 + R3; AS 'TOTAL CASH'
ON TABLE SET ONLINE-FMT HTML
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLESHEET *
TYPE = REPORT, GRID = OFF,$
TYPE = REPORT, LABEL = TOTCASH, COLUMN = N2, BORDER = MEDIUM, $
ENDSTYLE
END

The output is shown in the following image.

Syntax:

How to Specify an Indent for an FML Label, Tag, or Caption

FOR forfield [IN k]
tag [[GET CHILDREN|WITH CHILDREN] n] INDENT m [AS ['text'|CAPTION]]
[OVER]

or

RECAP fieldname[/format]=expression; INDENT m [AS 'text']

where:

forfield

Is a field in the data source whose values are included in the report.

k

Is the starting column for the FOR value in an FML report.

tag

Is a value of forfield to be displayed on a row of the FML report.

1886

25. Creating Financial Reports With Financial Modeling Language (FML)

n

m

Is the number of levels of an FML hierarchy to display on the FML report.

Is a positive integer (zero is not supported) specifying the number of spaces to indent the
tag value, label, or caption of an FML row or hierarchy. The indentation starts from column
one if there is no IN phrase specified in the FOR command. If there is an IN phrase,
indentation starts from the column specified in the IN phrase. The maximum indentation is
the same as the maximum length of an AS name.

If you indent an FML hierarchy, the parent line of the hierarchy is indented the number of
spaces specified as the indent. The hierarchy levels are indented two spaces from each
other. If the GET CHILDREN phrase is used, the first line of the hierarchy is indented an
additional two spaces because the hierarchy output begins with the first child rather than
the parent. For more information about the use of GET CHILDREN, see Displaying an FML
Hierarchy on page 1856.

'text'

Is a label to be displayed on a row of the FML report.

CAPTION

Indicates that a caption field has been defined in the Master File.

OVER

Indicates that this row is not the last row to be displayed.

fieldname

Is a name you assign to the value calculated by the RECAP command.

format

Is the USAGE format for RECAP field. It cannot exceed the column width. The default is the
format of the column in which the calculated value is displayed.

expression

Is the expression that describes how to calculate the field value for RECAP.

Creating Reports With TIBCO® WebFOCUS Language

 1887

Formatting an FML Report

Example:

Indenting a Tag Row in an FML Hierarchy

In the following request, the label of the second row for tag value 3000 is indented five
spaces. Because the GET CHILDREN phrase is used, the first line of the FML hierarchy, in the
third row for tag value 3000, is indented seven spaces (five + two).

SET FORMULTIPLE=ON
TABLE FILE CENTGL
PRINT GL_ACCOUNT_PARENT
FOR GL_ACCOUNT
3000                           AS 'Not Indented'        OVER
3000                 INDENT 5  AS 'Indented 5'          OVER
3000 GET  CHILDREN 2 INDENT 5  AS 'Hierarchy Indented 5'
END

The output is shown as follows.

                               Parent
                               ------
Not Indented                   3000
     Indented 5                3000
       Hierarchy Indented 5    3000
         Hierarchy Indented 5  3100
         Hierarchy Indented 5  3100
         Hierarchy Indented 5  3100
         Hierarchy Indented 5  3100
         Hierarchy Indented 5  3000
         Hierarchy Indented 5  3200
         Hierarchy Indented 5  3200
         Hierarchy Indented 5  3200
         Hierarchy Indented 5  3200
         Hierarchy Indented 5  3200
         Hierarchy Indented 5  3200
         Hierarchy Indented 5  3200

Indenting FML RECAP Rows

The following request sums price, cost, and quantity in stock for digital and analog product
types. The first RECAP command calculates the total for each column, and indents the label
five spaces. The second RECAP command calculates the profit, and indents the label 10
spaces.

SET FORMULTIPLE=ON
TABLE FILE CENTINV
SUM PRICE COST QTY_IN_STOCK
FOR PRODTYPE
Digital                                          OVER
Analog                                           OVER
BAR                                              OVER
RECAP TOTAL = R1 + R2; INDENT 5  AS 'Total:'     OVER
BAR                                              OVER
RECAP PROFIT(2) = TOTAL(1) - TOTAL(2); AS 'Profit:' INDENT 10
END

1888

25. Creating Financial Reports With Financial Modeling Language (FML)

The output is shown as follows.

                                        Our    Quantity
                         Price:         Cost:  In Stock:
                         ------         -----  ---------
Digital                4,080.00      3,052.00     119143
Analog                 1,883.00      1,371.00     139345
                   ------------  ------------    -------
     Total:            5,963.00      4,423.00     258488
                   ------------  ------------    -------
          Profit:                    1,540.00

Indenting Row Titles in an FML Hierarchy

To clarify relationships within an FML hierarchy, the captions (titles) of values are indented at
each level. Use the BLANKINDENT parameter in an HTML, PDF, or PostScript report to specify
the indentation between each level in the hierarchy. You can use the default indentation for
each hierarchy level or choose your own indentation value. To print indented captions in an
HTML report, you must set the BLANKINDENT parameter to ON or to a number.

SET BLANKINDENT does not redefine the width of the indented column, if it is not wide enough
to accommodate the indented fields. Columns in table-based formats will automatically size
themselves as needed, while columns in position-based formats, such as PDF, PostScript, or
PPTX, shift out of alignment. You can use StyleSheet syntax to make the column wide enough
for the indented values, and move the columns that follow it. Change the width of a column
using the StyleSheet SQUEEZE = n attribute to supply the required space.

A related feature enables you to change the number of blank spaces before the parent line of
a hierarchy or before any FML tag or RECAP row in any FML request. For more information, see
Formatting an FML Report on page 1871.

Syntax:

How to Indent FML Hierarchy Captions in an HTML Report

SET BLANKINDENT={ON|OFF|n}
ON TABLE SET BLANKINDENT {ON|OFF|n}

where:

ON

Indents FML hierarchy captions 0.125 units for each space that normally displays before
the caption. For child levels in an FML hierarchy, it indents 0.125 units for each space that
normally displays between this line and the line above it.

OFF

Turns off indentations for FML hierarchy captions in an HTML report. OFF is the default
value. For other formats, uses the default indentation of two spaces.

Creating Reports With TIBCO® WebFOCUS Language

 1889

Formatting an FML Report

n

Is an explicit measurement in the unit of measurement defined by the UNITS parameter.
This measurement is multiplied by the number of spaces that normally displays before the
caption. For child levels in an FML hierarchy, it indents n units for each space that normally
displays between this line and the line above it. The default number of spaces is two. Zero
(0) produces the same report output as OFF. Negative values for n are not supported.

Example:

Using the Default Indentation for FML Hierarchy Captions

The following request creates an HTML report with the default indentation:

SET PAGE-NUM=NOPAGE
SET BLANKINDENT=ON
SET FORMULTIPLE=ON
TABLE FILE CENTGL
PRINT GL_ACCOUNT_PARENT
FOR GL_ACCOUNT
3000                  AS CAPTION      OVER
3000 GET  CHILDREN 2  AS CAPTION

ON TABLE SET ONLINE-FMT HTML
ON TABLE SET HTMLCSS ON
ON TABLE SET STYLE *
TYPE = REPORT, GRID = OFF, $
ENDSTYLE
END

1890

25. Creating Financial Reports With Financial Modeling Language (FML)

The output is shown in the following image.

Example:

Specifying an Indentation Value for FML Hierarchy Captions

The following request specifies an indentation of .25 for each level of an FML hierarchy. This
number is expressed in the default unit of measurement, which is inches:

SET PAGE-NUM=NOPAGE
SET BLANKINDENT=.25
SET FORMULTIPLE=ON
TABLE FILE CENTGL
PRINT GL_ACCOUNT_PARENT
FOR GL_ACCOUNT
3000                 AS CAPTION          OVER
3000 GET  CHILDREN 2 AS CAPTION

ON TABLE SET STYLE *
TYPE = REPORT, GRID = OFF, $
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 1891

Suppressing the Display of Rows

The output is shown in the following image.

Suppressing the Display of Rows

You may sometimes wish to retrieve data in a TAG row solely for use in a calculation, without
displaying the row in a report. To suppress the display of a tag row, add the word NOPRINT to
the row declaration, as in a TABLE request.

You may also wish to suppress the display of a TAG row if no data is found for the values. For
more information, see Suppressing Rows With No Data on page 1893.

In addition, you can suppress the display of RECAP rows by adding the word NOPRINT to the
RECAP command, following the semicolon. This technique is useful to suppress the display of
an intermediate RECAP value, which is intended for use as input to other calculations.

Example:

Suppressing the Display of a TAG Row

This example uses the value of COST in its computation, but does not display COST as a row
in the report.

1892

25. Creating Financial Reports With Financial Modeling Language (FML)

DEFINE FILE REGION
AMOUNT/I5C=E_ACTUAL;
END

TABLE FILE REGION
SUM AMOUNT FOR ACCOUNT
3000 AS 'SALES' LABEL SLS           OVER
3100 AS 'COST' LABEL COST NOPRINT   OVER
RECAP PROFIT/I5C = SLS - COST;      OVER
" "                                 OVER
RECAP ROS/F6.2 = 100*PROFIT/SLS;
AS 'RETURN ON SALES'
END

The output is shown in the following image.

Suppressing Rows With No Data

The text for a tag row is displayed even if no data is found in the file for the tag values, with a
period (.) representing the missing data. You can override this convention by adding the phrase
WHEN EXISTS to the definition of a TAG row. This makes displaying a row dependent upon the
existence of data for the tag. This feature is useful, for example, when the same model is
applied to different divisions in a company.

Example:

Suppressing Rows With No Data

In this example, assume that the variable DIVISION contains Division 1, a real estate
syndicate, and Division 2, a bank. The following request describes their balance sheets in one
FML report. Rows that are irrelevant for each division are not displayed.

TABLE FILE LEDGER
HEADING CENTER
"BALANCE SHEET FOR DIVISION <DIVISION"
" "
SUM AMOUNT
BY DIVISION NOPRINT
ON DIVISION PAGE-BREAK
FOR ACCOUNT
2000 AS 'LAND' WHEN EXISTS LABEL LD          OVER
2100 AS 'CAR LOANS' WHEN EXISTS LABEL LOAN   OVER
   .
   .
   .

Creating Reports With TIBCO® WebFOCUS Language

 1893


Saving and Retrieving Intermediate Report Results

Saving and Retrieving Intermediate Report Results

Many reports require results developed in prior reports. This can be accomplished only if a
place is provided for storing intermediate values. An example is the need to compute net profit
in an Income Statement prior to calculating equity in a Balance Sheet. FML can save selected
rows from one or more models by posting them to a work file. The posted rows can then be
picked up from the work file and reused.

The default work file is FOCPOST. This is a comma-delimited file from which you can report
directly if a FOCPOST Master File is available. In order to use the work file in a request, you
must assign a physical name to the FOCPOST ddname before running the report that posts the
data, and again before running the report that picks up the data.

You can assign the physical name to the file by issuing a FILEDEF command on Windows and
UNIX, or a TSO ALLOCATE or DYNAM ALLOCATE command on z/OS, before the request is run.
You may create a FILEDEF command by using the Allocation Wizard.

While you cannot prepare an FML report entirely from data that you supply directly in your
request, you can prepare a report entirely from data that is stored in a comma-delimited work
file.

You can save any TAG, RECAP, or DATA row by posting the output to a file. You can use these
rows as though they were provided in a DATA row.

The row is processed in the usual manner in the report, depending on its other options, and
then posted. The label of the row is written first, followed by the numeric values of the
columns, each comma-separated, and ending with the terminator character ($). For more
information, see Posting Rows to a Work File on page 1895.

Note: Only fields that are actually displayed on the report output are posted. Fields that are not
printed (for example, fields specified with the NOPRINT option, extra fields that are created
when you reformat fields in the request, or fields implied by use in a calculation) are not
posted.

Posting Data

1894

25. Creating Financial Reports With Financial Modeling Language (FML)

Syntax:

How to Post Data to a File

The syntax for saving any TAG, RECAP, or DATA row is:

POST [TO ddname]

where:
ddname

Is the logical name you assign to the work file in which you are posting data.

Add this syntax to any row you wish to post to the work file.

Example:

Posting Rows to a Work File

The following request creates an FML report, and posts two tag rows to the LEDGEOUT work
file.

FILEDEF LEDGEOUT DISK [APP]\LEDGEOUT.DAT

DEFINE FILE LEDGER
CUR_YR/I5C=AMOUNT;
LAST_YR/I5C=.87*CUR_YR - 142;
END

TABLE FILE LEDGER
SUM CUR_YR LAST_YR
FOR ACCOUNT
1100 LABEL AR POST TO LEDGEOUT OVER
1200 LABEL INV POST TO LEDGEOUT
END

The output is shown in the following image.

Syntax:

How to Pick Up Data From a Work File

You can retrieve posted rows from any work file and use them as if they were provided in a
DATA row by adding the following phrase to an FML request.

DATA PICKUP [FROM ddname] id1 [OR id2 ...] [LABEL label] [AS 'text']

where:
ddname

Is the logical name of the work file from which you are retrieving data.

Creating Reports With TIBCO® WebFOCUS Language

 1895

Saving and Retrieving Intermediate Report Results

id

Is the label that was assigned in the work file to the posted row of data that is now being
picked up.

label

Is the label you wish to assign to the data you are picking up.

The label you assign to the picked data can, but is not required to, match the label (id) of
the posted data.

You can include LABEL and AS phrases, but WHEN EXISTS is not supported.

Note: The retrieved fields are mapped to all fields (printed or not) in the memory repository
(internal matrix) of the report. If the matrix contains columns that do not correspond to the
fields in the posted file, the retrieved values may be misaligned. For example, if you reformat a
field in the PICKUP request, that field will be represented by two columns in the internal matrix.
However, the posted file will have only one value representing that field, and the retrieved
values will not be mapped properly to the associated columns in the matrix.

Example:

Picking Up Data From a Work File

In the following example, the data in the LEDGER data source and in the LEDGEOUT work file
are used in the RECAP calculation. To see how this file was created, refer to Posting Rows to a
Work File on page 1895.

Tip: You must assign a logical name to the file by issuing a FILEDEF command on Windows
and UNIX, or a DYNAM ALLOCATE command on z/OS, before the request is run. You may
create a FILEDEF command by using the Allocation Wizard.

DEFINE FILE LEDGER
CUR_YR/I5C=AMOUNT;
LAST_YR/I5C=.87*CUR_YR - 142;
END

TABLE FILE LEDGER
SUM CUR_YR LAST_YR
FOR ACCOUNT
1010 TO 1030 AS 'CASH' LABEL CASH   OVER
DATA PICKUP FROM LEDGEOUT AR  AS 'ACCOUNTS RECEIVABLE' LABEL AR   OVER
DATA PICKUP FROM LEDGEOUT INV AS 'INVENTORY' LABEL INV            OVER
BAR                                 OVER
RECAP CUR_ASSET/I5C = CASH + AR + INV;
END

1896

25. Creating Financial Reports With Financial Modeling Language (FML)

The output is shown in the following image.

The following line can be used to pick up the sum of the two accounts from LEDGEOUT.

DATA PICKUP FROM LEDGEOUT AR OR INV
AS 'ACCTS REC AND INVENTORY'

Note: Since the rows in a PICKUP file are stored in standard comma-delimited format, they can
be provided either from a prior posting, or directly by a user.

Creating HOLD Files From FML Reports

A report created with FML can be extracted to a HOLD file in the same way as all other reports
created with the TABLE language.

In this case, you identify the set of tag values specified for each row by the description field
(the AS text supplied in the model). When no text is given for a row, the first tag value is used
automatically. Therefore, in simple models with only one tag per row and no text, the lines in
the HOLD file contain the single tag value. The rows derived from the RECAP calculation form
part of the HOLD file. Pure text rows (including BAR rows) are omitted.

For HOLD to be supported with RECAP, the format of the RECAP field must be the same as the
format of the original column.

This feature enables you to create new rows in the HOLD file that are the result of calculations.
The augmented HOLD file may then be used in a variety of TABLE requests.

Note: You cannot reformat RECAP rows when creating HOLD files.

Example:

Creating a Hold File From an FML Report

The following request creates a HOLD file that contains records for CASH, ACCOUNTS
RECEIVABLE, INVENTORY, and the RECAP row CURRENT ASSETS.

TABLE FILE LEDGER
SUM AMOUNT FOR ACCOUNT
1010 TO 1030 AS 'CASH'                            OVER
1100 AS 'ACCOUNTS RECEIVABLE'                     OVER
1200 AS 'INVENTORY'                               OVER
RECAP CA = R1 + R2 + R3; AS 'CURRENT ASSETS'
ON TABLE HOLD
END

Creating Reports With TIBCO® WebFOCUS Language

 1897

Creating HOLD Files From FML Reports

Query the HOLD file:

>
? HOLD

DEFINITION OF HOLD FILE: HOLD

FIELDNAME          ALIAS          FORMAT

                   EO1            A 19
AMOUNT             EO2            I5C

Then report from the HOLD file as:

TABLE FILE HOLD
PRINT E01 E02
END

The output is shown in the following image.

                     AMOUNT
                     ------
CASH                 21,239
ACCOUNTS RECEIVABLE  18,829
INVENTORY            27,307
CURRENT ASSETS       67,375

1898

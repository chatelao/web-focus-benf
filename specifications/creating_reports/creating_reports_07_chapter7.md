Chapter7

Using Expressions

An expression combines field names, constants, and operators in a calculation that
returns a single value. You can use an expression in a variety of commands to assign a
value to a temporary field or Dialogue Manager amper variable, or use it in screening.
You can combine simpler ones to build increasingly complex expressions.

When you write an expression, you can specify the operation yourself, or you can use one
of the many supplied functions that perform specific calculations or data manipulation.
These functions operate on one or more arguments, and return a single value as a
result. To use a function, you simply call it. For details about functions, see the Using
Functions manual.

IF-THEN-ELSE logic is supported as part of an expression, including arithmetic,
chararcter, and logical expressions. It is also supported in WHERE clauses.

In this chapter:

Using Expressions in Commands and Phrases

Types of Expressions

Creating a Numeric Expression

Creating a Date Expression

Creating a Date-Time Expression

Creating a Character Expression

Creating a Variable Length Character Expression

Creating a Logical Expression

Creating a Conditional Expression

Using Expressions in Commands and Phrases

You can use an expression in various commands and phrases. An expression may not exceed
40 lines and must end with a semicolon, except in WHERE and WHEN phrases, in which the
semicolon is optional.

Creating Reports With TIBCO® WebFOCUS Language

 429

Types of Expressions

The commands that support expressions, and their basic syntax, are summarized here. For
complete syntax with an explanation, see the applicable documentation.

You can use an expression when you:

Create a temporary field, and assign a value to that field. The field can be created in a
Master File using the DEFINE attribute, or using a DEFINE or COMPUTE command:

DEFINE command preceding a report request:

DEFINE FILE filename
 fieldname  [/format] = expression;
   .
   .
   .
END

DEFINE attribute in a Master File:

DEFINE fieldname [/format] = expression;$

COMPUTE command in a report request:

COMPUTE fieldname  [/format] = expression;

Define record selection criteria and criteria that control report formatting.

{WHERE|IF} logical_expression[;]
      WHEN logical_expression[;]

Determine branching in Dialogue Manager, or assign a value to a Dialogue Manager amper
variable.

-IF logical_expression [THEN] GOTO label1 [ELSE GOTO label2];

-SET &name = expression;

Perform a calculation with the RECAP command in the Financial Modeling Language (FML).

RECAP name [(n)] [/format] = expression;

Types of Expressions

An expression can be one of the following:

Numeric. Use numeric expressions to perform calculations that use numeric constants
(integer or decimal) and fields. For example, you can write an expression to compute the
bonus for each employee by multiplying the current salary by the desired percentage as
follows:

430

7. Using Expressions

COMPUTE BONUS/D12.2 = CURR_SAL * 0.05 ;

A numeric expression returns a numeric value. For details, see Creating a Numeric
Expression on page 432.

Date. Use date expressions to perform numeric calculations on dates. For example, you
can write an expression to determine when a customer can expect to receive an order by
adding the number of days in transit to the date on which you shipped the order as follows:

COMPUTE DELIVERY/MDY = SHIPDATE + 5 ;

There are two types of date expressions:

Date expressions, which return a date, a component of a date, or an integer that
represents the number of days, months, quarters, or years between two dates. For
details, see Creating a Date Expression on page 439.

Date-time expressions, which you can create using a variety of specialized date-time
functions, each of which returns a different kind of value. For details on these functions,
see the Using Functions manual.

Character. Use character expressions to manipulate alphanumeric constants or fields. For
example, you can write an expression to extract the first initial from an alphanumeric field
as follows:

COMPUTE FIRST_INIT/A1 = EDIT (FIRST_NAME, '9$$$$$$$$$') ;

A character expression returns an alphanumeric value. For details, see Creating a Character
Expression on page 456.

Note: Text fields can be assigned to alphanumeric fields and receive assignment from
alphanumeric fields. Text fields can also participate in expressions using the operators
CONTAINS and OMITS.

Logical. Use logical expressions to evaluate the relationship between two values. A logical
expression returns TRUE or FALSE. For details, see Creating a Logical Expression on page
465.

Conditional. Use conditional expressions to assign values based on the result of logical
expressions. A conditional expression (IF ... THEN ... ELSE) returns a numeric or
alphanumeric value. For details, see Creating a Conditional Expression on page 467.

Creating Reports With TIBCO® WebFOCUS Language

 431

Creating a Numeric Expression

Expressions and Field Formats

When you use an expression to assign a value to a field, make sure that you give the field a
format that is consistent with the value returned by the expression. For example, if you use a
character expression to concatenate a first name and last name and assign it to the field
FULL_NAME, make sure you define the field as character.

Example:

Assigning a Field Format of Sufficient Length

The following example contains a character expression that concatenates a first name and last
name to derive the full name. It assigns the field FULL_NAME an alphanumeric format of
sufficient length to accommodate the concatenated name:

DEFINE FILE EMPLOYEE
FULL_NAME/A25 = FIRST_NAME | LAST_NAME;
END
TABLE FILE EMPLOYEE
PRINT FULL_NAME
WHERE LAST_NAME IS 'BLACKWOOD'
END

The output is:

FULL_NAME
---------
ROSEMARIE BLACKWOOD

Creating a Numeric Expression

A numeric expression performs a calculation that uses numeric constants, fields, operators,
and functions to return a numeric value. When you use a numeric expression to assign a value
to a field, that field must have a numeric format. The default format is D12.2.

A numeric expression can consist of the following components, shown below in bold:

A numeric constant. For example:

COMPUTE COUNT/I2 = 1 ;

A numeric constant in scientific notation. For example:

COMPUTE COST/D12.2 = EXPN(8E+3);

For syntax usage, see How to Express a Number in Scientific Notation on page 433.

A numeric field. For example:

COMPUTE RECOUNT/I2 = COUNT ;

Two numeric constants or fields joined by an arithmetic operator. For example:

432

7. Using Expressions

COMPUTE BONUS/D12.2 = CURR_SAL * 0.05 ;

For a list of arithmetic operators, see Arithmetic Operators on page 435.

A numeric function. For example:

COMPUTE LONGEST_SIDE/D12.2 = MAX (WIDTH, HEIGHT) ;

Two or more numeric expressions joined by an arithmetic operator. For example:

COMPUTE PROFIT/D12.2 = (RETAIL_PRICE - UNIT_COST) * UNIT_SOLD ;

Note the use of parentheses to change the order of evaluation of the expression. For
information on the order in which numeric operations are performed, see Order of
Evaluation on page 435.

Before they are used in calculations, numeric values are generally converted to double-
precision floating-point format. The result is then converted to the specified field format. In
some cases the conversion may result in a difference in rounding. Note that environments that
support native-mode arithmetic handle rounding differently. For details, see Evaluating Numeric
Expressions With Native-Mode Arithmetic on page 437.

If a number is too large (greater than 1075) or too small (less than 10-75), you receive an
Overflow or Underflow warning, and asterisks display for the field value.

Note: You can change the overflow character by issuing the SET OVERFLOWCHAR command.

For detailed information on rounding behavior for numeric data formats, see the Describing
Data With WebFOCUS Language manual.

IF-THEN-ELSE logic is supported in numeric expressions.

Syntax:

How to Express a Number in Scientific Notation

In an IF clause, use the following:

IF field op n[.nn]{E|D|e|d}[+|-]p

In a WHERE clause, use the following:

WHERE field op EXPN(n[.nn{E|D|e|d}[+|-]p);

In a COMPUTE command, use the following:

COMPUTE field[/format] = EXPN(n[.nn]{{E|D|e|d}[+|-]p);

Creating Reports With TIBCO® WebFOCUS Language

 433

Creating a Numeric Expression

In a DEFINE command, use the following:

DEFINE FILE filename
field[/format] = EXPN(n[.nn]{E|D|e|d}[+|-]p);
END

In a DEFINE in the Master File, use the following:

DEFINE field[/format] = EXPN(n[.nn]{{E|D|e|d}[+|-]p);

where:

field

Is a field in a request.

/format

Is the optional format of the field. For information on formats, see the Describing Data
With WebFOCUS Language manual.

op

Is a relational operator in a request.

n.nn

Is a numeric constant that consists of a whole number component, followed by a
decimal point, followed by a fractional component.

E, D, e, d

Denotes scientific notation. E, e, d, and D are interchangeable.

+, -

Indicates if p is positive or negative. Positive is the default.

p

Is the power of 10 to which to raise the number. The range of values for p is between
 -78 and +78 on z/OS, -99 to +99 elsewhere.

Note: EXPN is useful for calculations on fields with F and D formats. It is generally not useful
for calculations on fields with P or I formats.

Example:

Evaluating a Number in Scientific Notation

You can use scientific notation in an IF or WHERE clause to express 8000 as 8E+03:

IF RCOST LT 8E+03

WHERE RCOST LT EXPN(8E+03)

434

Reference: Arithmetic Operators

The following list shows the arithmetic operators you can use in an expression:

7. Using Expressions

Addition

Subtraction

Multiplication

Division

Exponentiation

+

-

*

/

**

Note: If you attempt to divide by 0, the value of the expression is 0. Multiplication and
exponentiation are not supported for date expressions of any type. To isolate part of a date,
use a simple assignment command.

Order of Evaluation

Numeric expressions are evaluated in the following order:

1. Exponentiation.

2. Division and multiplication.

3. Addition and subtraction.

When operators are at the same level, they are evaluated from left to right. Because
expressions in parentheses are evaluated before any other expression, you can use
parentheses to change this predefined order. For example, the following expressions yield
different results because of parentheses:

COMPUTE PROFIT/D12.2  =  RETAIL_PRICE  -  UNIT_COST  *  UNIT_SOLD ;
COMPUTE PROFIT/D12.2  = (RETAIL_PRICE  -  UNIT_COST) *  UNIT_SOLD ;

In the first expression, UNIT_SOLD is first multiplied by UNIT_COST, and the result is
subtracted from RETAIL_PRICE. In the second expression, UNIT_COST is first subtracted from
RETAIL_PRICE, and that result is multiplied by UNIT_SOLD.

Note:Two operators cannot appear consecutively. The following expression is invalid:

a * -1

To make it valid, you must add parentheses:

a* (-1)

Creating Reports With TIBCO® WebFOCUS Language

 435

Creating a Numeric Expression

Example:

Controlling the Order of Evaluation

The order of evaluation can affect the result of an expression. Suppose you want to determine
the dollar loss in retail sales attributed to the return of damaged items. You could issue the
following request:

TABLE FILE SALES
PRINT RETAIL_PRICE RETURNS DAMAGED
COMPUTE RETAIL_LOSS/D12.2 = RETAIL_PRICE * RETURNS + DAMAGED;
BY PROD_CODE
WHERE PROD_CODE IS 'E1';
END

The calculation

COMPUTE RETAIL_LOSS/D12.2 = RETAIL_PRICE * RETURNS + DAMAGED;

gives an incorrect result because RETAIL_PRICE is first multiplied by RETURNS, and then the
result is added to DAMAGED. The correct result is achieved by adding RETURNS to DAMAGED,
then multiplying the result by RETAIL_PRICE.

You can change the order of evaluation by enclosing expressions in parentheses. An
expression in parentheses is evaluated before any other expression. You may also use
parentheses to improve readability.

Using parentheses, the correct syntax for the preceding calculation is:

COMPUTE RETAIL_LOSS/D12.2 = RETAIL_PRICE * (RETURNS + DAMAGED);

The output is:

PROD_CODE  RETAIL_PRICE  RETURNS  DAMAGED     RETAIL_LOSS
---------  ------------  -------  -------     -----------
E1                 $.89        4        7            9.79

Example:

Using IF-THEN-ELSE Logic in an Arithmetic Expression

The following request uses IF-THEN-ELSE logic in an arithmetic expression to determine how
much to add to LISTPR to calculate NEWPRICE.

TABLE FILE MOVIES
SUM COPIES
LISTPR
COMPUTE
NEWPRICE = LISTPR + (IF COPIES GT 10 THEN 0.00 ELSE 25.00);
BY CATEGORY
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

436

The output is shown in the following image. Where there are more than 10 copies, the
NEWPRICE equals LISTPR, otherwise NEWPRICE is $25.00 greater than LISTPR.

7. Using Expressions

Evaluating Numeric Expressions With Native-Mode Arithmetic

When native-mode arithmetic is used, a specific evaluation path is followed for each numeric
expression based on the format of the operands and the operators. If the operands all have
the same format, most operations are carried out in that format. If the operands have different
formats, the operands are converted to a common format in a specific order of format
precedence. Regardless of operand formats, some operators require conversion to specific
formats so that all operands are in the appropriate format.

Using Identical Operand Formats With Native-Mode Arithmetic

If all operands of a numeric operator are of the same format, you can use the following table to
determine whether or not the operations are performed in that native format or if the operands
are converted before and after executing the operation. In each case requiring conversion,
operands are converted to the operational format and the intermediate result is returned in the
operational format. If the format of the result differs from the format of the target variable, the
result is converted to the format of the target variable.

Operation

Addition

Subtraction

Operational Format

+

-

Native

Native

Creating Reports With TIBCO® WebFOCUS Language

 437

Creating a Numeric Expression

Operation

Multiplication

Full Division

*

/

Operational Format

Native

Accepts single or double-precision floating point,
converts all others to double-precision floating
point

Exponentiation

**

Double-precision floating point

Example:

Using Identical Operand Formats (Native-mode Arithmetic)

The following variables are defined as integers in Maintain Data:

COMPUTE OPERANDONE/I4  ;
        OPERANDTWO/I4  ;
        RESULT/I4  ;

The required multiplication is done in native-mode arithmetic (integer arithmetic):

COMPUTE RESULT/I4 = OPERANDONE * OPERANDTWO  ;

Using Different Operand Formats With Native-Mode Arithmetic

If operands of a numeric operator have different formats, you can use the following table to
determine what the common format is after they are converted. The lower operand is converted
to the format of the higher operand before performing the operation.

Order

Format

1

2

3

4

5

6

16-byte packed decimal

Double-precision floating point

8-byte packed-decimal

Single-precision floating point

Integer

Character (alphanumeric and text)

438

7. Using Expressions

For example, if a 16-byte packed-decimal operand is used in an expression, all other operands
are converted to 16-byte packed-decimal format for evaluation. On the other hand, if an
expression includes only integer and alphanumeric operands, all alphanumeric operands are
converted to integer format.

A character (that is, alphanumeric or text) value can be used in a computation if it is a numeric
string. An attempt is made to convert the character operand to the format of the other operand
in the expression. If both operands are character, an attempt is made to convert them to
double-precision. If the conversion is not possible, an error message is generated.

If you assign a decimal value to an integer, the fractional value is truncated.

Creating a Date Expression

A date expression performs a numeric calculation that involves dates.

A date expression returns a date, a date component, or an integer that represents the number
of days, months, quarters, or years between two dates. You can write a date expression
directly that consists of:

A date constant. For example:

COMPUTE END_DATE/MDYY = 'FEB 29 2000';

This requires single quotation marks around the date constant.

A date field. For example:

COMPUTE NEWDATE/YMD = START_DATE;

An alphanumeric, integer, or packed decimal format field, with date edit options. For
example, in the second COMPUTE command, OLDDATE is a date expression:

COMPUTE OLDDATE/I6YMD = 980307;
COMPUTE NEWDATE/YMD DFC 19 YRT 10 = OLDDATE;

A calculation that uses an arithmetic operator or date function to return a date. Use a
numeric operator only with date formats (formerly called Smart dates). The following
example first converts the integer date HIRE_DATE (format I6YMD) to the date format
CONVERTED_HDT (format YMD). It then adds 30 days to CONVERTED_HDT:

COMPUTE CONVERTED_HDT/YMD = HIRE_DATE;
HIRE_DATE_PLUS_THIRTY/YMD = CONVERTED_HDT + 30;

A calculation that uses a numeric operator or date function to return an integer that
represents the number of days, months, quarters, or years between two dates. The
following example uses the date function YMD to calculate the difference (number of days)
between an employee hire date and the date of his first salary increase:

Creating Reports With TIBCO® WebFOCUS Language

 439

Creating a Date Expression

COMPUTE DIFF/I4 = YMD (HIRE_DATE,FST.DAT_INC);

Formats for Date Values

You can work with dates in one of two ways:

In date format. The value is treated as an integer that represents the number of days
between the date value and a base date. There are two base dates for date formats:

YMD and YYMD formats have a base date of December 31, 1900.

YM and YYM formats have a base date of January, 1901 on z/OS and a base date of
December 31, 1900 on Windows and UNIX.

When displayed, the integer value is converted to the corresponding date in the format
specified for the field. The format can be specified in either the Master File or in the
command that uses an expression to assign a value to the field. These were previously
referred to as smart date formatted fields.

In integer, packed decimal, or alphanumeric format with date edit options. The value is
treated as an integer, a packed decimal, or an alphanumeric string. When displayed, the
value is formatted as a date. These were previously referred to as old date formatted
fields.

You can convert a date in one format to a date in another format simply by assigning one to
the other. For example, the following assignments take a date stored as an alphanumeric field,
formatted with date edit options, and convert it to a date stored as a temporary date field:

COMPUTE ALPHADATE/A6MDY = '120599' ;
        REALDATE/MDY = ALPHADATE;

Reference: Base Dates for Date Formats

The following table shows the base date for each supported date format:

Format

YMD, YYMD, MDYY, DMYY, MDY,
and DMY

Base Date

1900/12/31

YM, YYM, MYY, and MY

1901/01 on z/OS

1900/12/31 on Windows and UNIX

440

7. Using Expressions

Format

YQ, YYQ, QYY, and QY

JUL and YYJUL

Base Date

1901 Q1

1900/365

D
M
Y, YY
Q
W

There is no base date for these formats; these are
just numbers, not dates.

Note that the base date used for the functions DA and DT is December 31, 1899. For details
on date functions, see the Using Functions manual.

Reference: Impact of Date Formats on Storage and Display

The following table illustrates how the field format affects storage and display:

Date Format (For example:
MDYY)

Integer, Packed, Decimal, or
Alphanumeric Format (For
example: A8MDYY)

February 28, 1999

35853

02/28/1999

02281999

02/28/1999

March 1, 1999

35854

03/01/1999

03011999

03/01/1999

Performing Calculations on Dates

The format of a field determines how you can use it in a date expression. Calculations on
dates in date format can incorporate numeric operators as well as numeric functions.
Calculations on dates in integer, packed, decimal, or alphanumeric format require the use of
date functions. Numeric operators return an error message or an incorrect result.

A full set of functions is supplied with your software, enabling you to manipulate dates in
integer, packed decimal, and alphanumeric format. For details on date functions, see the Using
Functions manual.

Creating Reports With TIBCO® WebFOCUS Language

 441

Creating a Date Expression

Example:

Calculating Dates

Assume that your company maintains a SHIPPING database. The following example calculates
how many days it takes the shipping department to fill an order by subtracting the date on
which an item is ordered, the ORDER_DATE, from the date on which it is shipped, the
SHIPDATE:

COMPUTE TURNAROUND/I4 = SHIP_DATE - ORDER_DATE;

An item ordered on February 28, 1999, and shipped on March 1, 1999, results in a difference
of one day. However, if the SHIP_DATE and ORDER_DATE fields have an integer format, the
result of the calculation (730000) is incorrect, since you cannot use the numeric operator
minus (-) with that format.

The following table shows how the field format affects the result:

Value in Date Format

Value in Integer Format

SHIP_DATE = March 1, 1999

35854

ORDER_DATE = February 28, 1999

35853

TURNAROUND

1

03011999

02281999

730000

To obtain the correct result using fields in integer, packed, decimal, or alphanumeric format,
use the date function MDY, which returns the difference between two dates in the form month-
day-year. Using the function MDY, you can calculate TURNAROUND as follows:

COMPUTE TURNAROUND/I4 = MDY(ORDER_DATE, SHIP_DATE);

Cross-Century Dates With DEFINE and COMPUTE

You can use an expression in a DEFINE or COMPUTE command, or in a DEFINE attribute in a
Master File, that implements the sliding window technique for cross-century date processing.
The parameters DEFCENT and YRTHRESH provide a means of interpreting the century if the
first two digits of the year are not provided elsewhere. If the first two digits are provided, they
are simply accepted.

442

7. Using Expressions

Returned Field Format Selection

A date expression always returns a number. That number may represent a date, or the number
of days, months, quarters, or years between two dates. When you use a date expression to
assign a value to a field, the format selected for the field determines how the result is
returned.

Example:

Selecting the Format of a Returned Field

Consider the following commands, assuming that SHIP_DATE and ORDER_DATE are date-
formatted fields. The first command calculates how many days it takes a shipping department
to fill an order by subtracting the date on which an item is ordered, ORDER_DATE, from the
date on which it is shipped, SHIP_DATE. The second command calculates a delivery date by
adding five days to the date on which the order is shipped.

COMPUTE TURNAROUND/I4 = SHIP_DATE - ORDER_DATE;
COMPUTE DELIVERY/MDY = SHIP_DATE + 5;

In the first command, the date expression returns the number of days it takes to fill an order;
therefore, the associated field, TURNAROUND, must have an integer format. In the second
command, the date expression returns the date on which the item will be delivered; therefore,
the associated field, DELIVERY, must have a date format.

Using a Date Constant in an Expression

When you use a date constant in a calculation with a field in date format, you must enclose it
in single quotation marks; otherwise, it is interpreted as the number of days between the
constant and the base date (December 31, 1900, or January 1, 1901). For example, if
022899 were not enclosed in quotation marks, the value would be interpreted as the
22,899th day after 12/31/1900, rather than as February 28, 1999.

Example:

Initializing a Field With a Date Constant

The following command initializes START_DATE with the date constant 02/28/99:

COMPUTE START_DATE/MDY = '022899';

The following command calculates the number of days elapsed since January 1, 1999:

COMPUTE YEAR_TO_DATE/I4 = CURR_DATE - 'JAN 1 1999' ;

Creating Reports With TIBCO® WebFOCUS Language

 443

Creating a Date Expression

Extracting a Date Component

Date components include days, months, quarters, or years. You can write an expression that
extracts a component from a field in date format. However, you cannot write an expression
that extracts days, months, or quarters from a date that does not have these components. For
example, you cannot extract a month from a date in YY format, which represents only the
number of years.

Example:

Extracting the Month Component From a Date

The following example extracts the month component from SHIP_DATE, which has the format
MDYY:

COMPUTE SHIP_MONTH/M = SHIP_DATE;

If SHIP_DATE has the value March 1, 1999, the above expression returns the value 03 for
SHIP_MONTH.

A calculation on a date component automatically produces a valid value for the desired
component. For example, if the current value of SHIP_MONTH is 03, the following expression
correctly returns the value 06:

COMPUTE ADD_THREE/M = SHIPMONTH + 3;

If the addition of months results in an answer greater than 12, the months are adjusted
correctly (for example, 11 + 3 is 2, not 14).

Combining Fields With Different Formats in an Expression

When using fields in date format, you can combine fields with a different order of components
within the same expression. In addition, you can assign the result of a date expression to a
field with a different order of components from the fields in the expression.

You cannot, however, write an expression that combines dates in date format with dates in
integer, packed, decimal or character format.

Example:

Combining Fields With Format YYMD and MDY

Consider the two fields DATE_PAID and DUE_DATE. DATE_PAID has the format YYMD, and
DUE_DATE has the format MDY. You can combine these two fields in an expression to
calculate the number of days that a payment is late:

COMPUTE DAYS_LATE/I4 = DATE_PAID - DUE_DATE;

444

7. Using Expressions

Example:

Assigning a Different Order of Components to a Returned Field

Consider the field DATE_SOLD. This field contains the date on which an item is sold, in YYMD
format. The following expression adds seven days to DATE_SOLD to determine the last date on
which the item can be returned. It then assigns the result to a field with DMY format:

COMPUTE RETURN_BY/DMY = DATE_SOLD + 7;

Creating a Date-Time Expression

A date-time expression returns date and time components. You can create these expressions
using a variety of supplied date-time functions. For details about date-time functions, see the
Using Functions manual.

Reference: Automatic Conversion Between Date and Date-Time Formats

In early releases of date-time fields, you were required to use date-time functions for all
conversions between date and date-time formats. While these functions are still supported for
conversions, the requirement to use them has been eliminated in certain operations.

The following automatic direct operations are supported between date and date-time formats:

Assignment.

Assignment of a date field or a date constant to a date-time field. The time component is
set to zero (midnight). The date can be a full component date such as YYMD or a partial
component date such as YYM. It cannot be a single component date such as Q, as this
type of date, although displayed as a date in reports, is stored as an integer value and is
used as an integer value in expressions.

Assignment of a date-time field or date-time constant to a date field. The time
components are removed.

Comparison and Subtraction.

When a date-time value is compared with or subtracted from a date value, or a date value
is compared with or subtracted from a date-time value, the date is converted to date-time
with the time component set to midnight. They are then compared or subtracted as date-
time values.

Function parameters.

Simplified date functions can use either date or date-time values as their date parameters.
Legacy user functions do not support this new functionality. The date-time functions (H
functions) use date-time parameters and the new date functions use new dates, which are
stored as offsets from a base date.

Creating Reports With TIBCO® WebFOCUS Language

 445

Creating a Date-Time Expression

Recognition and use of date or date-time constants.

Constants can be expressed as strings, without the DT operator.

Constants are converted to or from date or date-time values in accordance with the field
format they are compared with, subtracted from, or assigned to.

Unless it is expressed in a non-ambiguous translated or formatted string format with proper
delimiters (not as a numeric string or number), the recognition of a constant as a date
depends on the format of its field counterpart.

In this case, the size in terms of number of digits is strictly limited to at least six for a full
component date or date-time value, (eight for a four-digit year), three for a partial
component date, and one for a single component date.

When numeric constants are used as function parameters and, therefore, do not have a
field counterpart, they are recognized according to YYMD or YMD format. The only exception
is a string with a single blank or the number zero which, in reports, will be presented as a
blank. Date offset constants are no longer allowed. Blank separators between digits in a
string are also not supported.

For additional information about date and date-time formats, see the Describing Data With
WebFOCUS Language manual.

Example:

Assigning Date and Date-Time Values

The following request generates a date-time value using the DT_CURRENT_DATETIME function.
It then assigns this value to a date field and assigns that date field to a date-time field.

TABLE FILE WF_RETAIL_LITE
PRINT QUANTITY_SOLD NOPRINT AND COMPUTE
 DATETIME1/HYYMDm =  DT_CURRENT_DATETIME(MILLISECOND);
     AS 'Date-Time 1'
COMPUTE
 DATE1/YYMD   = DATETIME1;
     AS 'Date'
COMPUTE
DATETIME2/HYYMDm = DATE1;
     AS 'Date-Time 2'
WHERE RECORDLIMIT EQ 20
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

446

The output is shown in the following image. The original date-time field has a non-zero time
component. When assigned to the date field, the time component is removed. When that date
is assigned to the second date-time field, a zero time component is added.

7. Using Expressions

Creating Reports With TIBCO® WebFOCUS Language

 447

Creating a Date-Time Expression

Example:

Comparing Date and Date-Time Values

The following request creates one date-time field and one date field. When QUANTITY_SOLD is
1, they have the same date value and the date-time field has a zero time component. When
QUANTITY_SOLD is 2, they have different date values, and the date-time field has a zero time
component. In all other cases, the date-time field has the current date with a non-zero time
component, and the date field has the current date. The EQUAL1 field compares them to see if
they compare as equal.

TABLE FILE WF_RETAIL_LITE
PRINT QUANTITY_SOLD AS Quantity AND COMPUTE
 DATETIME1/HYYMDm = IF QUANTITY_SOLD EQ 1 THEN '2017/06/05'
        ELSE IF QUANTITY_SOLD EQ 2 THEN '2016/02/29'
        ELSE DT_CURRENT_DATETIME(MILLISECOND);
        AS 'Date-Time'
COMPUTE
  DATE1/YYMD   = IF QUANTITY_SOLD EQ 1 THEN '2017/06/05'
        ELSE IF QUANTITY_SOLD EQ 2 THEN '2015/12/30'
        ELSE DT_CURRENT_DATE();
        AS 'Date'
COMPUTE
  EQUAL1/A1 = IF DATETIME1 EQ DATE1 THEN 'Y' ELSE 'N';
        AS 'Equal?'
WHERE RECORDLIMIT EQ 12
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

448

7. Using Expressions

The output is shown in the following image. When a date value is compared to a date-time
value, the date is converted to a date-time value with the time component set to zero, and
then the values are compared. Therefore, when QUANTITY_SOLD is 1, both the date
components are equal and the time component of the date-time field is set to zero, so when
the date is converted to a date-time value, they are equal. When QUANTITY_SOLD is 2, the
date components are different, so they are not equal. When QUANTITY_SOLD is 3, the date
components are the same, but the date-time field has a non-zero time component. Therefore,
when the date field is converted to a date-time value with a zero time component and they are
compared, they are not equal.

Syntax:

How to Specify the Order of Date Components in a Date-Time Field

SET DATEFORMAT = option

where:

option

Can be one of the following: MDY, DMY, YMD, or MYD. MDY is the default value for
the U.S. English format.

Creating Reports With TIBCO® WebFOCUS Language

 449

Creating a Date-Time Expression

Specifying a Date-Time Value

An external date-time value is a constant in character format from one of the following sources:

A sequential data source.

Used in an expression in a WHERE, IF, DEFINE, or a COMPUTE.

A date-time constant or a date-time value as it appears in a character file has one of the
following formats:

time_string  [date_string]
date_string  [time_string]

A date-time constant in a COMPUTE, DEFINE, or WHERE expression must have one of the
following formats:

DT(time_string  [date_string])
DT(date_string  [time_string])

A date-time constant in an IF expression has one of the following formats:

'time_string  [date_string]'
'date_string  [time_string]'

If the value contains no blanks or special characters, the single quotation marks are not
necessary. Note that the DT prefix is not supported in IF criteria.

where:

time_string

Cannot contain blanks. Time components are separated by colons, and may be followed by
AM, PM, am, or pm. For example:

14:30:20:99       (99 milliseconds)
14:30
14:30:20.99       (99/100 seconds)
14:30:20.999999   (999999 microseconds)
02:30:20:500pm

Note that the second can be expressed with a decimal point or be followed by a colon:

If there is a colon after the second, the value following it represents the millisecond.
There is no way to express the microsecond or nanosecond using this notation.

A decimal point in the second value indicates the decimal fraction of a second. A
microsecond can be represented using six decimal digits. A nanosecond can be
represented using nine decimal digits.

450

7. Using Expressions

date_string

Can have one of the following three formats:

Numeric string format. Is exactly four, six, or eight digits. Four-digit strings are
considered to be a year (century must be specified). The month and day are set to
January 1. Six and eight-digit strings contain two or four digits for the year, followed by
two for the month, and then two for the day. Because the component order is fixed with
this format, the DATEFORMAT setting described in How to Specify the Order of Date
Components in a Date-Time Field on page 449 is ignored.

If a numeric-string format longer than eight digits is encountered, it is treated as a
combined date-time string in the Hn format. The following are examples of numeric
string date constants:

99
1999
19990201

Formatted-string format. Contains a one or two-digit day, a one or two-digit month, and
a two or four-digit year separated by spaces, slashes, hyphens, or periods. All three
parts must be present and follow the DATEFORMAT setting described in How to Specify
the Order of Date Components in a Date-Time Field on page 449. If any of the three
fields is four digits, it is interpreted as the year, and the other two fields must follow
the order given by the DATEFORMAT setting. The following are examples of formatted-
string date constants:

1999/05/20
5 20 1999
99.05.20
1999-05-20

Translated-string format. Contains the full or abbreviated month name. The year must
also be present in four-digit or two-digit form. If the day is missing, day 1 of the month
is assumed; if present, it can have one or two digits. If the string contains both a two-
digit year and a two-digit day, they must be in the order given by the DATEFORMAT
setting. For example:

January 6 2000

Note:

The date and time strings must be separated by at least one blank space. Blank spaces
are also permitted at the beginning and end of the date-time string or immediately before
an am/pm indicator.

Creating Reports With TIBCO® WebFOCUS Language

 451

Creating a Date-Time Expression

In each date format, two-digit years are interpreted using the [F]DEFCENT and [F]YRTHRESH
settings.

Example:

Assigning Date-Time Literals

The DT prefix can be used, although it is no longer required, in a COMPUTE, DEFINE, or WHERE
expression to assign a date-time literal to a date-time field. For example:

DT2/HYYMDS = DT(20051226 05:45);

DT3/HYYMDS = DT(2005 DEC 26 05:45);

DT4/HYYMDS = DT(December 26 2005 05:45);

Example:

Specifying the Order of Date Components for a Date-Time Field

The following request sets DATEFORMAT to MYD:

SET DATEFORMAT = MYD
DEFINE FILE EMPLOYEE
DTFLDYYMD/HYYMDI =  DT(APR 04 05);
END

TABLE FILE EMPLOYEE
PRINT CURR_SAL DTFLDYYMD
END

The output shows that the natural date literal 'APR 04 05' is interpreted as April 5, 1904:

  CURR_SAL  DTFLDYYMD
  --------  ---------
$11,000.00  1904/04/05 00:00
$13,200.00  1904/04/05 00:00
$18,480.00  1904/04/05 00:00
 $9,500.00  1904/04/05 00:00
$29,700.00  1904/04/05 00:00
$26,862.00  1904/04/05 00:00
$21,120.00  1904/04/05 00:00
$18,480.00  1904/04/05 00:00
$21,780.00  1904/04/05 00:00
$16,100.00  1904/04/05 00:00
 $9,000.00  1904/04/05 00:00
$27,062.00  1904/04/05 00:00

Example:

Reading Date-Time Values From a Transaction File

The DTTRANS comma-delimited transaction file has an ID field and a date-time field that
contains both the date (as eight characters) and time (in the format hour:minute:second):

01, 20000101 02:57:25,$
02, 19991231 14:05:35,$

452


7. Using Expressions

Because the transaction file contains the dates in numeric string format, the DATEFORMAT
setting is not used, and the dates are entered in YMD order.

The following transaction file is also valid. It contains formatted string dates that comply with
the default DATEFORMAT setting, MDY:

01, 01/01/2000 02:57:25,$
02, 12/31/1999 14:05:35,$

The following Master File describes the FOCUS data source named DATETIME, which receives
these values:

FILE=DATETIME,    SUFFIX=FOC   ,$
SEGNAME=DATETIME, SEGTYPE=S0   ,$
FIELD=ID,  ID,    USAGE = I2   ,$
FIELD=DT1, DT1,   USAGE=HYYMDS ,$

Example:

Using a Date-Time Value in a COMPUTE Command

TABLE FILE EMPLOYEE
PRINT LAST_NAME FIRST_NAME AND COMPUTE
NEWSAL/D12.2M = CURR_SAL + (0.1 * CURR_SAL);
RAISETIME/HYYMDIA = DT(20000101 09:00AM);
WHERE CURR_JOBCODE LIKE 'B%'
END

The output is:

LAST_NAME        FIRST_NAME           NEWSAL  RAISETIME
---------        ----------           ------  ---------
SMITH            MARY             $14,520.00  2000/01/01  9:00AM
JONES            DIANE            $20,328.00  2000/01/01  9:00AM
ROMANS           ANTHONY          $23,232.00  2000/01/01  9:00AM
MCCOY            JOHN             $20,328.00  2000/01/01  9:00AM
BLACKWOOD        ROSEMARIE        $23,958.00  2000/01/01  9:00AM
MCKNIGHT         ROGER            $17,710.00  2000/01/01  9:00AM

Example:

Using a Date-Time Value in WHERE Criteria

In a WHERE clause, a date-time constant must use the DT( ) format:

TABLE FILE VIDEOTR2
PRINT CUSTID TRANSDATE
WHERE TRANSDATE GT DT(2000/01/01 02:57:25)
END

The output is:

CUSTID  TRANSDATE
------  ---------
1118    2000/06/26 05:45
1237    2000/02/05 03:30

Creating Reports With TIBCO® WebFOCUS Language

 453

Creating a Date-Time Expression

Example:

Using a Date-Time Value in IF Criteria

In an IF clause, a date-time constant must be enclosed in single quotation marks if it contains
any blanks:

TABLE FILE VIDEOTR2
PRINT CUSTID TRANSDATE
IF TRANSDATE GT '2000/01/01 02:57:25'
END

Note: The DT prefix for a date-time constant is not supported in an IF clause.

The output is:

CUSTID  TRANSDATE
------  ---------
1118    2000/06/26 05:45
1237    2000/02/05 03:30

Example:

Specifying Universal Date-Time Input Values

With DTSTANDARD settings of STANDARD and STANDARDU, the following date-time values can
be read as input:

Input Value

Description

14:30[:20,99]

Comma separates time components instead of period

14:30[:20.99]Z

Universal time

15:30[:20,99]+01
15:30[:20,99]+0100
15:30[:20,99]+01:00

Each of these is the same as above in Central European
Time

09:30[:20.99]-05

Same as above in Eastern Standard Time

Note that these values are stored identically internally with the STANDARDU setting. With the
STANDARD setting, everything following the Z, +, or - is ignored.

Manipulating Date-Time Values

Any two date-time values can be compared, even if their lengths do not match.

454

7. Using Expressions

If a date-time field supports missing values, fields that contain the missing value have a
greater value than any date-time field can have. Therefore, in order to exclude missing values
from the report output when using a GT or GE operator in a selection test, it is recommended
that you add the additional constraint field NE MISSING to the selection test:

date_time_field {GT|GE} date_time_value AND date_time_field NE MISSING

Assignments are permitted between date-time formats of equal or different lengths. Assigning
a 10-byte date-time value to an 8-byte date-time value truncates the microsecond portion (no
rounding takes place). Assigning a short value to a long one sets the low-order three digits of
the microseconds to zero.

Other operations, including concatenation, EDIT, and LIKE on date-time operands are not
supported. Prefix operators that work with alphanumeric fields are supported.

Example:

Testing for Missing Date-Time Values

Consider the DATETIM2 Master File:

FILE=DATETIM2,  SUFFIX=FOC                ,$
SEGNAME=DATETIME, SEGTYPE=S0              ,$
FIELD=ID, ID, USAGE = I2                  ,$
FIELD=DT1, DT1,   USAGE=HYYMDS, MISSING=ON,$

Field DT1 supports missing values. Consider the following request:

TABLE FILE DATETIM2
PRINT ID DT1
END

The resulting report output shows that in the instance with ID=3, the field DT1 has a missing
value:

ID  DT1
--  ---
 1  2000/01/01 02:57:25
 2  1999/12/31 00:00:00
 3  .

The following request selects values of DT1 that are greater than 2000/01/01 00:00:00 and
are not missing:

TABLE FILE DATETIM2
PRINT ID DT1
  WHERE DT1 NE MISSING AND DT1 GT DT(2000/01/01 00:00:00);
END

Creating Reports With TIBCO® WebFOCUS Language

 455

Creating a Character Expression

The missing value is not included in the report output:

ID  DT1
--  ---
 1  2000/01/01 02:57:25

Example:

Assigning a Different Usage Format to a Date-Time Column

Consider the following request using the VIDEOTR2 data source:

TABLE FILE VIDEOTR2
 PRINT CUSTID TRANSDATE AND COMPUTE
  DT2/HYYMDH = TRANSDATE;
  T1/HHIS = TRANSDATE;
 WHERE DATE EQ 2000
 END

The output is:

CUSTID  TRANSDATE         DT2            T1
------  ---------         ---            --
1118    2000/06/26 05:45  2000/06/26 05  05:45:00
1237    2000/02/05 03:30  2000/02/05 03  03:30:00

Creating a Character Expression

A character expression uses alphanumeric constants, fields, concatenation operators, IF-THEN-
ELSE logic, or functions to derive an alphanumeric value.

Both text and alphanumeric fields can be assigned values stored in text fields or alphanumeric
expressions in TABLE COMPUTE, MODIFY COMPUTE, and DEFINE commands. If an
alphanumeric field is assigned the value of a text field that is too long for the alphanumeric
field, the value is truncated before being assigned to the alphanumeric field.

A character expression can consist of:

An alphanumeric constant (character string) enclosed in single quotation marks. For
example:

COMPUTE STATE/A2 = 'NY';

A combination of alphanumeric fields and/or constants joined by the concatenation
operator. For example:

DEFINE FILE EMPLOYEE TITLE/A19 = 'DR. ' | LAST_NAME;
END

An alphanumeric function. For example:

DEFINE FILE EMPLOYEE INITIAL/A1 = EDIT(FIRST_NAME, '9$$$$$$$$$$');
END

456

7. Using Expressions

A text field.

Note:

Non-printable characters are not supported in an alphanumeric constant.

Two consecutive single quotation marks represent a null value with format A1V and an
actual length of 0 (zero), when the field has MISSING ON.

Embedding a Quotation Mark in a Quote-Delimited Literal String

Under certain conditions, you can use quote-delimited strings containing embedded quotation
marks. Within the string, you can use either one single quotation mark or two contiguous
single quotation marks to represent the single quotation mark. Both are interpreted as a single
quotation mark.

You can use quote-delimited strings in the following instances:

WHERE and IF criteria containing multiple quotes.

WHERE criteria containing: fieldname {IS, IS-NOT, IN, IN FILE, or NOT IN FILE}.

EDIT.

WHEN fieldname EQ an embedded quote in a literal.

DEFINE commands.

DEFINE attributes in Master Files.

Database Administrator (DBA) attributes in Master Files (for example, VALUE = fieldname
EQ an embedded quote in a literal).

ACCEPT=, DESCRIPTION=, TITLE= attributes in Master Files.

AS.

DECODE.

Creating Reports With TIBCO® WebFOCUS Language

 457

Creating a Character Expression

Example:

Specifying the Data Value O'BRIEN in a Quote-Delimited Literal String

The following example illustrates the use of quotation marks for the correct interpretation of
the data value O'BRIEN:

TABLE FILE VIDEOTRK
PRINT LASTNAME
WHERE LASTNAME IS 'O'BRIEN'
END

Concatenating Character Strings

You can write an expression that concatenates two or more alphanumeric constants and/or
fields into a single character string. This concatenation operator has two forms, as shown in
the following table:

Symbol

Represents

Description

|

||

Weak concatenation

Preserves trailing blanks.

Strong concatenation

Moves trailing blanks to the end of a concatenated
string.

Example:

Concatenating Character Strings

The following example uses the EDIT function to extract the first initial from a first name. It
then uses both strong and weak concatenation to produce the last name, followed by a
comma, followed by the first initial, followed by a period:

DEFINE FILE EMPLOYEE
FIRST_INIT/A1 = EDIT(FIRST_NAME, '9$$$$$$$$$');
NAME/A19 = LAST_NAME ||(', '| FIRST_INIT |'.');
END

TABLE FILE EMPLOYEE
PRINT NAME WHERE LAST_NAME IS 'BANNING'
END

The output is:

NAME
----
BANNING, J.

458

7. Using Expressions

The request evaluates the expressions as follows:

1. The EDIT function extracts the initial J from FIRST_NAME.

2. The expression in parentheses returns the value:

, J.

3. LAST_NAME is concatenated to the string derived in step 2 to produce:

Banning, J.

While LAST_NAME has the format A15 in the EMPLOYEE Master File, strong concatenation
suppresses the trailing blanks. Regardless of the suppression or inclusion of blanks, the
resulting field name, NAME, has a length of 19 characters (A19).

Example:

Using IF-THEN-ELSE Logic in a Character Expression

The following request uses IF-THEN-ELSE logic to determine what characters to concatenate to
MOVIECODE in order to compute NEWCODE.

TABLE FILE MOVIES
PRINT COPIES
MOVIECODE
COMPUTE
NEWCODE/A20 =  MOVIECODE |(IF MOVIECODE CONTAINS 'DIS' THEN  'NEY;' ELSE
';');
BY CATEGORY
WHERE CATEGORY EQ 'CHILDREN'
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 459

Creating a Variable Length Character Expression

The output is shown in the following image. If MOVIECODE contains the characters 'DIS',
NEWCODE is generated by concatenating the characters 'NEY;', otherwise NEWCODE is
generated by concatenating the character ';'.

Creating a Variable Length Character Expression

As an alphanumeric type, an AnV field can be used in arithmetic and logical expressions in the
same way that the An type is used.

An expression that contains AnV type fields can be of either the AnV or An type.

The type that results from the expression depends on the specific type of operation, as
described in subsequent sections.

Note: Because AnV fields have two bytes of overhead and there is additional processing
required to strip them, AnV format is not recommended for use in non-relational data sources.

460

Using Concatenation With AnV Fields

7. Using Expressions

If either of the operands in a concatenation between two fields is an AnV field, variable length
alphanumeric rules are used to perform the concatenation:

The size of the concatenated string is the sum of the sizes of the operands.

For weak concatenation, the actual length of the concatenated string is the sum of the two
actual lengths of the input strings.

For strong concatenation, the actual length stored in an AnV field of the concatenated
string is the sum of the actual length of the first input string minus its number of trailing
blanks plus the actual length of the second string.

For any An field in the concatenation, the size and length are equal.

Two consecutive single quotation marks represent a null value with format A1V and an
actual length of 0 (zero), when the field has MISSING ON.

Using the EDIT Function With AnV Fields

The following expression results in an AnV format only when x has AnV format.

EDIT(x,mask)

The actual length of the result is the number of characters in mask other than '$'.

Note that an actual length of zero may result.

EDIT(x) can be used to convert an AnV field to an integer value when x has AnV format.

Using CONTAINS and OMITS With AnV Fields

The only difference in evaluation of the CONTAINS and OMITS operators with AnV fields occurs
when one of the operands has an actual length of zero.

In the following examples, the field Z has an actual length of zero, but X and Y do not:

Expression

Z CONTAINS Y

X CONTAINS Z

Z CONTAINS Z

Result

FALSE

TRUE

TRUE

Creating Reports With TIBCO® WebFOCUS Language

 461

Creating a Variable Length Character Expression

Expression

Z OMITS Y

X OMITS Z

Z OMITS Z

Using LIKE With AnV Fields

Result

TRUE

FALSE

FALSE

The only difference in evaluation of the following expression occurs when x has an actual
length of zero:

x LIKE mask ...

In the following example, the field instance Z has an actual length of zero:

Z LIKE mask ...

This expression evaluates to TRUE only when the mask consists exclusively of percent ('%')
signs.

Note that no other mask can evaluate to an empty string. Even the mask in the following
expression has a length of one, and therefore the expression evaluates as FALSE:

Z LIKE ''

Using the EQ, NE, LT, GT, LE, and GE Operators With AnV Fields

As with An type fields, operations are evaluated on the assumption that the shorter operand is
padded with blanks.

Therefore, even an empty AnV field, Z, is compared as a field consisting of all blanks.

In the following examples, Z is an empty AnV field instance and X is an AnV field instance that
is not empty and contains non-blank characters:

Expression

Z EQ Z
Z GE Z
Z LE Z

462

Result

TRUE

7. Using Expressions

Expression

Z NE Z
Z LT Z
Z GT Z

Z EQ X

Z NE X

Z LT X

Z GT X

Z LE X

Z GE X

X EQ Z

X NE Z

X LT Z

X GT Z

X LE Z

X GE Z

Result

FALSE

FALSE

TRUE

TRUE

FALSE

TRUE

FALSE

FALSE

TRUE

FALSE

TRUE

FALSE

TRUE

Using the DECODE Function With AnV Fields

DECODE alphafield (value 'result'...

The use of either an An or AnV field with DECODE causes a result of type An as long as the
result part of the value-result pairs is provided as a constant. (Constants are type An.)

Creating Reports With TIBCO® WebFOCUS Language

 463

Creating a Variable Length Character Expression

Using the Assignment Operator With AnV Fields

There are three situations to consider when using the assignment operator with the AnV
format: AnV data type on the right hand side only, AnV data type on both sides, and AnV data
type on the left side only.

fld/An = AnV_type_expression;

The actual length of the evaluated expression is lost on assignment to the An field.

The size of the AnV result does not prevent assignment to a shorter An format field:

If the result of the expression has an actual length that is shorter than the length of the
field on the left side of the assignment operator, the result is padded with blanks.

If the result of the expression has an actual length that is longer than the length of the
field on the left side of the assignment operator, the result is truncated.

fld/AnV = AnV_type_expression;

The length of the result is assigned as the length of the field on the left of the assignment
operator unless it exceeds the field's declared size. In this case, the length assigned is the
declared size (n).

The size of the AnV evaluation result does not prevent assignment to a shorter AnV field:

If the length of the result of the expression is shorter than the size of the field on the
left side of the assignment operator, the result is padded with blanks.

If the result of the expression has an actual length that is longer than the size of the
field on the left side of the assignment operator, the result is truncated.

fld/AnV = An_type_expression;

The length of the field on the left side of the assignment operator is assigned equal to its
size (n).

The actual length of the result is verified against the size n declared for the AnV field. An
error is generated if the result is longer than n.

464

7. Using Expressions

Creating a Logical Expression

A logical expression determines whether a particular condition is true. There are two kinds of
logical expressions: relational and Boolean. The entities to be compared determine the kind of
expression used:

A relational expression returns TRUE or FALSE based on a comparison of two individual
values (either field values or constants).

A Boolean expression returns TRUE or FALSE based on the outcome of two or more
relational expressions.

You can use a logical expression to assign a value to a numeric field. If the expression is true,
the field receives the value 1. If the expression is false, the field receives the value 0.

Reference: Logical Operators

The following is a list of common operators used in logical expressions. For information on
relational operators and additional operators available for record selection using WHERE and
IF, see Selecting Records for Your Report on page 217.

Operator

Description

EQ

NE

GE

GT

LE

LT

Returns the value TRUE if the value on the left is equal to the value on the
right.

Returns the value TRUE if the value on the left is not equal to the value on
the right.

Returns the value TRUE if the value on the left is greater than or equal to
the value on the right.

Returns the value TRUE if the value on the left is greater than the value on
the right.

Returns the value TRUE if the value on the left is less than or equal to the
value on the right.

Returns the value TRUE if the value on the left is less than the value on
the right.

AND

Returns the value TRUE if both operands are true.

Creating Reports With TIBCO® WebFOCUS Language

 465

Creating a Logical Expression

Operator

Description

OR

NOT

Returns the value TRUE if either operand is true.

Returns the value TRUE if the operand is false.

CONTAINS

Contains the specified character strings.

OMITS

Omits the specified character strings.

IS MISSING

Returns the value TRUE if the field is missing.

IS-NOT
MISSING

Returns the value TRUE if the field is not missing.

Syntax:

How to Write a Relational Expression

Any of the following are valid for a relational expression:

value {EQ|NE} value  value {LE|LT} value value {GE|GT}
valuecharacter_value {CONTAINS|OMITS} character_value

where:

value

Is a field value or constant.

character_value

Is a character string. If it contains blanks, the string must be enclosed in single
quotation marks.

Syntax:

How to Write a Boolean Expression

Either of the following is valid for a Boolean expression:

(relational_expression) {AND|OR} (relational_expression)
NOT (logical_expression)

where:

relational_expression

Is an expression based on a comparison of two individual values (either field values or
constants).

466

7. Using Expressions

logical_expression

Is an expression that evaluates to the value TRUE or FALSE. If the expression is true,
the field receives the value 1. If the expression is false, the field receives the value 0.
The expression must be enclosed in parentheses.

Creating a Conditional Expression

A conditional expression assigns a value based on the result of a logical expression. The
assigned value can be numeric or alphanumeric.

Note: Unlike selection criteria using IF, all alphanumeric values in conditional expressions
must be enclosed in single quotation marks. For example, IF COUNTRY EQ 'ENGLAND'.

Syntax:

How to Write a Conditional Expression

IF expression1 THEN expression2 [ELSE expression3]

where:

expression1

Is the expression that is evaluated to determine whether the field is assigned the
value of expression2 or of expression3.

expression2

Is an expression that results in a format compatible with the format assigned to the
field. It may be a conditional expression, in which case you must enclose it in
parentheses.

expression3

Is an expression that results in a format compatible with the format assigned to the
field. Enclosure of the expression in parentheses is optional.

ELSE

Is optional, along with expression3. However, if you do not specify an ELSE condition and
the IF condition is not met, the value is taken from the last evaluated condition. Therefore,
the results may not be what you expect if you do not include an ELSE condition.

Note that the final sorted report may display mixed values. This depends on whether a
DEFINE or a COMPUTE is used, and if a data record is evaluated before or after
aggregation.

The expressions following THEN and ELSE must result in a format that is compatible with the
format assigned to the field. Each of these expressions may itself be a conditional expression.
However, the expression following IF may not be an IF ... THEN ... ELSE expression (for
example, IF ... IF ...).

Creating Reports With TIBCO® WebFOCUS Language

 467

Creating a Conditional Expression

Example:

Supplying a Value With a Conditional Expression

The following example uses a conditional expression to assign the value NONE to the field
BANK_NAME when it is missing a data value (that is, when the field has no data in the data
source):

DEFINE FILE EMPLOYEE
BANK_NAME/A20 = IF BANK_NAME EQ ' ' THEN 'NONE'
ELSE BANK_NAME;
END

TABLE FILE EMPLOYEE
PRINT CURR_SAL AND BANK_NAME
BY EMP_ID BY BANK_ACCT
END

The output is:

EMP_ID     BANK_ACCT         CURR_SAL  BANK_NAME
------     ---------         --------  ---------
071382660                  $11,000.00  NONE
112847612                  $13,200.00  NONE
117593129   40950036       $18,480.00  STATE
119265415                   $9,500.00  NONE
119329144     160633       $29,700.00  BEST BANK
123764317  819000702       $26,862.00  ASSOCIATED
126724188                  $21,120.00  NONE
219984371                  $18,480.00  NONE
326179357  122850108       $21,780.00  ASSOCIATED
451123478  136500120       $16,100.00  ASSOCIATED
543729165                   $9,000.00  NONE
818692173  163800144       $27,062.00  BANK ASSOCIATION

Example:

Defining a True or False Condition

You can define a true or false condition and then test it to control report output. The following
example assigns the value TRUE to the field MYTEST if either of the relational expressions in
parentheses is true. It then tests the value of MYTEST:

DEFINE FILE EMPLOYEE
MYTEST= (CURR_SAL GE 11000) OR (DEPARTMENT EQ 'MIS');
END

TABLE FILE EMPLOYEE
PRINT CURR_SAL AND DEPARTMENT
BY EMP_ID
IF MYTEST IS TRUE
END

468



7. Using Expressions

The output is:

EMP_ID            CURR_SAL  DEPARTMENT
------            --------  ----------
071382660       $11,000.00  PRODUCTION
112847612       $13,200.00  MIS
117593129       $18,480.00  MIS
119329144       $29,700.00  PRODUCTION
123764317       $26,862.00  PRODUCTION
126724188       $21,120.00  PRODUCTION
219984371       $18,480.00  MIS
326179357       $21,780.00  MIS
451123478       $16,100.00  PRODUCTION
543729165        $9,000.00  MIS
818692173       $27,062.00  MIS

Note: Testing for a TRUE or FALSE condition is valid only with the IF command. It is not valid
with WHERE.

Creating Reports With TIBCO® WebFOCUS Language

 469

Creating a Conditional Expression

470

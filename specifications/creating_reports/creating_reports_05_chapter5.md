Chapter5

Creating Temporary Fields

When you create a report, you are not restricted to the fields that exist in your data
source. If you can generate the information you want from the existing data, you can
create a temporary field to evaluate and display it. A temporary field takes up no storage
space in the data source. It is created only when needed.

In this chapter:

What Is a Temporary Field?

Defining a Virtual Field

Creating a Calculated Value

Assigning Column Reference Numbers

Using FORECAST in a COMPUTE Command

Calculating Trends and Predicting Values With FORECAST

Calculating Trends and Predicting Values With Multivariate REGRESS

Using Text Fields in DEFINE and COMPUTE

Creating Temporary Fields Independent of a Master File

What Is a Temporary Field?

A temporary field is a field whose value is not stored in the data source, but can be calculated
from the data that is there, or assigned an absolute value. A temporary field takes up no
storage space in the data source, and is created only when needed.

When you create a temporary field, you determine its value by writing an expression. You can
combine fields, constants, and operators in an expression to produce a single value. For
example, if your data contains salary and deduction amounts, you can calculate the ratio of
deductions to salaries using the following expression:

deduction / salary

Creating Reports With TIBCO® WebFOCUS Language

 277

What Is a Temporary Field?

You can specify the expression yourself, or you can use one of the many supplied functions
that perform specific calculations or manipulations. In addition, you can use expressions and
functions as building blocks for more complex expressions, as well as use one temporary field
to evaluate another.

Reference: Types of Temporary Fields

You can use two types of temporary fields (a virtual field and a calculated value), which differ in
how they are evaluated:

A virtual field (DEFINE) is evaluated as each record that meets the selection criteria is retrieved
from the data source. The result of the expression is treated as though it were a real field
stored in the data source.

A calculated value (COMPUTE) is evaluated after all the data that meets the selection criteria
is retrieved, sorted, and summed. Therefore, the calculation is performed using the aggregated
values of the fields.

278

Reference: Evaluation of Temporary Fields

The following illustration shows how a request processes, and when each type of temporary
field is evaluated:

5. Creating Temporary Fields

Example:

Distinguishing Between Virtual Fields and Calculated Values

In the following example, both the DRATIO field (virtual field) and the CRATIO (calculated value)
use the same expression DELIVER_AMT/OPENING_AMT, but do not return the same result.
The value for CRATIO is calculated after all records have been selected, sorted, and
aggregated. The virtual field DRATIO is calculated for each retrieved record.

DEFINE FILE SALES
DRATIO = DELIVER_AMT/OPENING_AMT;
END
TABLE FILE SALES
SUM DELIVER_AMT AND OPENING_AMT AND DRATIO
COMPUTE CRATIO = DELIVER_AMT/OPENING_AMT;
END

Creating Reports With TIBCO® WebFOCUS Language

 279

Defining a Virtual Field

The output is:

Reference: Selecting a Temporary Field

The following is to help you choose the kind of temporary field you need.

Choose a virtual field when you want to:

Use the temporary field to select data for your report. You cannot use a calculated value,
since it is evaluated after data selection takes place.

Use the temporary field to sort on data values. A calculated value is evaluated after the
data is sorted. With the BY TOTAL phrase, you can sort on this type of field.

Choose a calculated value when you want to:

Evaluate the temporary field using total values or prefix operators (which operate on total
values). You cannot use a virtual field, since it is evaluated before any totaling takes place.

Evaluate the temporary field using fields from different paths in the data structure. You
cannot use a virtual field, since it is evaluated before the relationship between data in the
different paths is established.

Defining a Virtual Field

A virtual field can be used in a request as though it is a real data source field. The calculation
that determines the value of a virtual field is performed on each retrieved record that passes
any screening conditions on real fields. The result of the expression is treated as though it
were a real field stored in the data source.

You can define a virtual field in the following ways:

In a Master File. These virtual fields are available whenever the data source is used for
reporting. These fields cannot be cleared by JOIN or DEFINE FILE commands.

For more information, see the Describing Data With WebFOCUS Language manual.

In a procedure. A virtual field created in a procedure lasts only for that procedure.

Tip: If your environment supports the KEEPDEFINES parameter, you can set KEEPDEFINES to
ON to protect virtual fields from being cleared by a subsequent JOIN command. For details, see
Joining Data Sources on page 1069.

280

Reference: Usage Notes for Creating Virtual Fields

5. Creating Temporary Fields

If you do not use the KEEPDEFINES parameter, when a JOIN is issued, all pre-existing
virtual fields for that data source are cleared except those defined in the Master File.

To join structures using a virtual field with the source, make sure the DEFINE follows the
JOIN command. Otherwise, the JOIN command clears the temporary field. For an
explanation of reporting on joined data sources, see Joining Data Sources on page 1069.

If no field in the expression is in the Master File or has been defined, use the WITH
command to identify the logical home of the defined calculation. See Establishing a
Segment Location for a Virtual Field on page 289.

WITH can be used to move the logical home for the virtual field to a segment lower than
that to which it would otherwise be assigned (for example, to count instances in a lower
segment).

You may define fields simultaneously (in addition to fields defined in the Master File) for as
many data sources as desired. The total length of all virtual fields and real fields cannot
exceed 32,000 characters.

When you specify virtual fields in a request, they count toward the display field limit. For
details on determining the maximum number of display fields that can be used in a
request, see Displaying Report Data on page 39.

Virtual fields are only available when the data source is used for reporting. Virtual fields
cannot be used with MODIFY.

A DEFINE command may not contain qualified field names on the left-hand side of the
expression. If the same field name exists in more than one segment, and that field must
be redefined or recomputed, use the REDEFINES command.

Using a self-referencing DEFINE such as x=x+1 disables AUTOPATH (see the Developing
Reporting Applications manual).

Field names used in the expression that defines the virtual field cannot be enclosed in
single or double quotation marks. Any character string enclosed in quotation marks is
treated as a literal string, not a field reference.

A DEFINE FILE command overwrites a DEFINE in the Master File with same name as long as
you do not redefine the format (which is not allowed).

Creating Reports With TIBCO® WebFOCUS Language

 281

Defining a Virtual Field

Syntax:

How to Create a Virtual Field

Before you begin a report request, include

DEFINE FILE filename[.view_fieldname] [CLEAR|ADD]
fieldname[/format] [(GEOGRAPHIC_ROLE = georole]
         [,TITLE = 'line1[,line2 ...']]
         [,DESCRIPTION = 'description'])] = expression;
fieldname[/format][WITH realfield] = expression;
fieldname[/format] REDEFINES qualifier.fieldname = expression;
.
.
.
END

where:

filename

Is the name of the data source for which you are defining the virtual field.

If the report request specifies an alternate view, use filename in conjunction with
view_fieldname.

All fields used to define the virtual field must lie on a single path in the data source. If they
do not, you can use an alternate view, which requires alternate view DEFINE commands.
For an alternate view, virtual fields cannot have qualified field names. For information on
alternate views, see Rotating a Data Structure for Enhanced Retrieval on page 1929.

The DEFINE FILE command line must be on a separate line from its virtual field definitions.

view_fieldname

Is the field on which an alternate view is based in the corresponding request. You may
need to use an alternate view if the fields used do not lie on a single path in the
normal view.

CLEAR

Clears previously defined virtual fields associated with the specified data source.
CLEAR is the default value.

ADD

Enables you to specify additional virtual fields for a data source without releasing any
existing virtual fields. Omitting ADD produces the same results as the CLEAR option.

fieldname

Is a name that complies with WebFOCUS field naming rules. Indexed field names in
FOCUS data sources must be less than or equal to 12 characters. It can be the name
of a new virtual field that you are defining, or an existing field declared in the Master
File, which you want to redefine.

282

5. Creating Temporary Fields

The name can include any combination of letters, digits, and underscores (_), and should
begin with a letter.

Do not use field names of the type Cn, En, or Xn (where n is any sequence of one or two
digits), because they are reserved for other uses.

format

Is the format of the field. The default value is D12.2. For information on field formats,
see the Describing Data With WebFOCUS Language manual.

georole

Is a valid geographic role. The following is a list of default geographic roles.

ADDRESS_FULL. Full address.

ADDRESS_LINE. Number and street name.

CITY. City name.

CONTINENT. Continent name.

COUNTY. County name.

COUNTRY. Country name.

GEOMETRY_AREA. Geometry area.

GEOMETRY_LINE. Geometry line.

GEOMETRY_POINT. Geometry point.

LATITUDE. Latitude.

LONGITUDE. Longitude.

POSTAL_CODE. Postal code.

STATE. State name.

WITH realfield

Associates a virtual field with a data source segment containing a real field. For more
information, see Usage Notes for Creating Virtual Fields on page 281.

line1, line2...

Are the lines of default column title to be displayed for the virtual field unless
overridden by an AS phrase.

description

Is the description to be associated with the virtual field, enclosed in single quotation
marks. The description displays in the tools that browse Master Files.

Creating Reports With TIBCO® WebFOCUS Language

 283

Defining a Virtual Field

REDEFINES qualifier.fieldname

Enables you to redefine or recompute a field whose name exists in more than one
segment. If you change the format of the field when redefining it, the length in the new
format must be the same as or shorter than the original. In addition, conversion
between alphanumeric and numeric data types is not supported.

expression

Can be an arithmetic or logical expression or function, evaluated to establish the
value of fieldname (see Using Expressions on page 429). You must end each
expression with a semicolon except for the last one, where the semicolon is optional.

Fields in the expression can be real data fields, data fields in data sources that are cross-
referenced or joined, or previously defined virtual fields. For related information, see Usage
Notes for Creating Virtual Fields on page 281.

END

Is required to end the DEFINE FILE command. END must be on its own line in the
procedure.

Note: For information about missing attributes for virtual fields, see MISSING Attribute in a
DEFINE or COMPUTE Command on page 1039.

Example:

Defining a Virtual Field

In the following request, the value of RATIO is calculated by dividing the value of DELIVER_AMT
by OPENING_AMT. The DEFINE command creates RATIO as a virtual field, which is used in the
request as though it were a real field in the data source.

DEFINE FILE SALES
RATIO = DELIVER_AMT/OPENING_AMT;
END
TABLE FILE SALES
PRINT DELIVER_AMT AND OPENING_AMT AND RATIO
WHERE DELIVER_AMT GT 50
END

The output is:

DELIVER_AMT  OPENING_AMT           RATIO
-----------  -----------           -----
         80           65            1.23
        100          100            1.00
         80           90             .89

284

Example:

Redefining a Field

The following request redefines the salary field in the EMPDATA data source to print asterisks
for job titles that contain the word EXECUTIVE:

5. Creating Temporary Fields

SET EXTENDNUM=OFF
DEFINE FILE EMPDATA
SALARY REDEFINES EMPDATA.SALARY =
 IF TITLE CONTAINS 'EXECUTIVE' THEN  ELSE
 EMPDATA.SALARY;
END
TABLE FILE EMPDATA
SUM SALARY BY TITLE
WHERE TITLE CONTAINS 'MANAGER' OR 'MARKETING' OR 'SALES'
ON TABLE SET PAGE OFF
END

The output is:

TITLE                          SALARY
-----                          ------
EXEC MANAGER               $54,100.00
EXECUTIVE MANAGER     ***************
MANAGER                   $270,500.00
MARKETING DIRECTOR        $176,800.00
MARKETING EXECUTIVE   ***************
MARKETING SUPERVISOR       $50,500.00
SALES EXECUTIVE       ***************
SALES MANAGER              $70,000.00
SALES SPECIALIST           $82,000.00
SENIOR SALES EXEC.         $43,400.00

Creating Reports With TIBCO® WebFOCUS Language

 285

Defining a Virtual Field

Example:

Redefining a Field That Has the Same Name in Multiple Segments

The following request joins the EMPDATA data source to itself. This creates a two-segment
structure in which the names are the same in both segments. The request then redefines the
salary field in the top segment (tag name ORIG) so that all names starting with the letter L are
replaced by asterisks, and redefines the salary field in the child segment (tag name NEW) so
that all names starting with the letter M are replace by asterisks:

SET EXTENDNUM=OFF
JOIN PIN IN EMPDATA TAG ORIG TO PIN IN EMPDATA TAG NEW AS AJ
DEFINE FILE EMPDATA
SALARY/D12.2M REDEFINES ORIG.SALARY = IF LASTNAME LIKE 'L%'  THEN
                                      999999999999 ELSE ORIG.SALARY;
SALARY/D12.2M REDEFINES NEW.SALARY = IF LASTNAME LIKE 'M%' THEN
                                     999999999999 ELSE NEW.SALARY * 1.2;
END
TABLE FILE EMPDATA
PRINT ORIG.SALARY AS 'ORIGINAL' NEW.SALARY AS 'NEW'
BY LASTNAME
WHERE LASTNAME FROM 'HIRSCHMAN' TO 'OLSON'
ON TABLE SET PAGE NOPAGE
END

The output is:

LASTNAME                ORIGINAL              NEW
--------                --------              ---
HIRSCHMAN             $62,500.00       $75,000.00
KASHMAN               $33,300.00       $39,960.00
LASTRA           ***************      $138,000.00
LEWIS            ***************       $60,600.00
LIEBER           ***************       $62,400.00
LOPEZ            ***************       $31,680.00
MARTIN                $49,000.00  ***************
MEDINA                $39,000.00  ***************
MORAN                 $30,800.00  ***************
NOZAWA                $80,500.00       $96,600.00
OLSON                 $30,500.00       $36,600.00

Defining Multiple Virtual Fields

You may wish to have more than one set of virtual fields for the same data source, and to use
some or all of the virtual fields in the request. The ADD option enables you to specify
additional virtual fields without clearing existing ones. If you omit the ADD option, previously
defined virtual fields in that data source are cleared.

If you want to clear a virtual field for a particular data source, use the CLEAR option.

286

5. Creating Temporary Fields

Syntax:

How to Add a Virtual Field to Existing Virtual Fields

DEFINE FILE filename ADD

where:

filename

Is the data source.

Example:

Adding Virtual Fields

The following annotated example illustrates the use of the ADD and CLEAR options for virtual
fields:

1. DEFINE FILE CAR
   ETYPE/A2=DECODE STANDARD (OHV O OHC O ELSE L);
   END
2. DEFINE FILE CAR ADD
   TAX/D8.2=IF MPG LT 15 THEN .06*RCOST
      ELSE .04*RCOST;
   FCOST = RCOST+TAX;
   END

1. The first DEFINE command creates the TYPE virtual field for the CAR data source. For

information about the DECODE function, see the Using Functions manual.

2. Two or more virtual fields, TAX and FCOST, are created for the CAR data source. The ADD

option allows you to reference ETYPE, TAX, and FCOST in future requests.

Displaying Virtual Fields

You can display all virtual fields with the ? DEFINE command.

Syntax:

How to Display Virtual Fields

? DEFINE

For more information, see the Developing Reporting Applications manual.

Procedure: How to Display Virtual Fields

Click the Defined Fields tab in the Define tool.

Creating Reports With TIBCO® WebFOCUS Language

 287

Defining a Virtual Field

Clearing a Virtual Field

The following can clear a virtual field created in a procedure:

A DEFINE FILE filename CLEAR command.

A subsequent DEFINE command (without the ADD option), against the same data source.

A join. When a join is created for a data source, all pre-existing virtual fields for that data
source are cleared except those defined in the Master File. This may affect virtual fields
used in an expression.

A change in the value of the FIELDNAME SET parameter.

Unlike fields created in a procedure, virtual fields in the Master File are not cleared in the
above ways.

To clear all virtual fields for all data sources, issue the following command:

DEFINE FILE * CLEAR
END

Example:

Clearing Virtual Fields

The following annotated example illustrates the use of the CLEAR options for virtual fields:

1. DEFINE FILE CAR
   ETYPE/A2=DECODE STANDARD (OHV O OHC O ELSE L);
   END
2. DEFINE FILE CAR CLEAR
   COST = RCOST-DCOST;
   END

1. The first DEFINE command creates the TYPE virtual field for the CAR data source. For

information about the DECODE function, see the Using Functions manual.

2. The CLEAR option clears the previously defined virtual fields, and only the COST virtual field

in the last DEFINE is available for further requests.

288

5. Creating Temporary Fields

Establishing a Segment Location for a Virtual Field

Virtual fields have a logical location in the data source structure, just like permanent data
source fields. The logical home of a virtual field is on the lowest segment that has to be
accessed in order to evaluate the expression, and determines the time of execution for that
field. Consider the following data source structure and DEFINE command:

DEFINE RATIO = DELIVER_AMT/RETAIL_PRICE ;

The expression for RATIO includes at least one real data source field. As far as report
capabilities are concerned, the field RATIO is just like a real field in the Master File, and is
located in the lowest segment.

In some applications, you can have a virtual field evaluated by an expression that contains no
real data source fields. Such an expression might refer only to temporary fields or literals. For
example,

NCOUNT/I5 = NCOUNT+1;

or

DATE/YMD = '19990101';

Since neither expression contains a data source field (NCOUNT and the literal do not exist in
the Master File), their logical positions in the data source cannot be determined. You have to
specify in which segment you want the expression to be placed. To associate a virtual field
with a specific segment, use the WITH phrase. The field name following WITH may be any real
field in the Master File.

Creating Reports With TIBCO® WebFOCUS Language

 289

Defining a Virtual Field

For FOCUS data sources, you may be able to increase the retrieval speed with an external
index on the virtual field. In this case, you can associate the index with a target segment
outside of the segment containing the virtual field. See the Developing Reporting Applications
manual for more information on external indexes.

Example:

Establishing a Segment Location

The field NCOUNT is placed in the same segment as the UNITS field. NCOUNT is calculated
each time a new segment instance is retrieved.

DEFINE FILE GGSALES
NCOUNT/I5 WITH UNITS = NCOUNT+1;
END

Defining Virtual Fields Using a Multi-Path Data Source

Calculations of a virtual field may include fields from all segments of a data source, but they
must lie in a unique top-to-bottom path. Different virtual fields may, of course, lie along
different paths. For example, consider the following data source structure:

This data source structure does not permit you to write the following expression:

NEWAMT = SALARY+GROSS;

The expression is invalid because the structure implies that there can be several SALARY
segments for a given EMPLOYEE, and it is not clear which SALARY to associate with which
GROSS.

To accomplish such an operation, you can use the alternate view option explained in Improving
Report Processing on page 1929.

Increasing the Speed of Calculations in Virtual Fields

Virtual fields are compiled into machine code in order to increase the speed of calculations.

290

Preserving Virtual Fields Using DEFINE FILE SAVE and RETURN

5. Creating Temporary Fields

Occasionally, new code needs to be added to an existing application. When adding code, there
is always the possibility of over-writing existing virtual fields by reusing their names
inadvertently.

The DEFINE FILE SAVE command forms a new context for virtual fields. Each new context
creates a new layer or command environment. When you first enter the new environment, all of
the virtual fields defined in the previous layer are available in the new layer. Overwriting or
clearing a virtual field definition affects only the current layer. You can return to the default
context with the DEFINE FILE RETURN command, and the virtual field definitions remain intact.

Therefore, all the virtual fields that are created in the new application can be removed before
returning to the calling application, without affecting existing virtual fields in that application.

For an example of DEFINE FILE SAVE and DEFINE FILE RETURN, see Joining Data Sources on
page 1069.

Note: A JOIN command can be issued after a DEFINE FILE SAVE command. However, in order
to clear the join context, you must issue a JOIN CLEAR command if the join is still in effect. If
only virtual fields and DEFINE FILE ADD were issued after a DEFINE FILE SAVE command, you
can clear them by issuing a DEFINE FILE RETURN command.

Syntax:

How to Protect Virtual Fields From Being Overwritten

DEFINE FILE filename SAVE
fld1/format1=expression1;
fld2/format2=expression2;
END
TABLE FILE filename ...
MODIFY FILE filename ...
DEFINE FILE filename RETURN
END

where:

SAVE

Creates a new context for virtual fields.

filename

Is the name of the Master File that gets a new context and has the subsequent virtual
fields applied before the DEFINE FILE RETURN command is issued.

RETURN

Clears the current context if it was created by DEFINE FILE SAVE, and restores the
previous context.

Creating Reports With TIBCO® WebFOCUS Language

 291

Defining a Virtual Field

Applying Dynamically Formatted Virtual Fields to Report Columns

Dynamic formatting enables you to apply different formats to specific data in a column by using
a temporary field that contains dynamic data settings.

Before you can format a report column using the dynamic format, you must create the report,
then apply the temporary field to a column in the report. For example, you can create a
temporary field that contains different decimal currency formats for countries like Japan (which
uses no decimal places) and England (which uses 2 decimal places). These currency formats
are considered dynamic formats. You can then apply the temporary field containing the
dynamic formatting to a Sales column. In a report, the Sales column reflects the different
currency formats for each country.

The field that contains the format specifications can be:

A real field in the data source.

A temporary field created with a DEFINE command.

A DEFINE in the Master File.

A COMPUTE command. If the field is created with a COMPUTE command, the command
must appear in the request prior to using the calculated field for reformatting.

The field that contains the formats must be alphanumeric, and at least eight characters in
length. Only the first eight characters are used for formatting.

The field-based format may specify a length longer than the length of the original field.
However, if the new length is more than one-third larger than the original length, the report
column width may not be large enough to hold the value (indicated by asterisks in the field).

You can apply a field-based format to any type of field. However, the new format must be
compatible with the original format:

A numeric field can be reformatted to any other numeric format with any edit format
options.

An alphanumeric field can be reformatted to a different length.

Any date field can be reformatted to any other date format type.

Any date-time field can be reformatted to any other date-time format.

If the field-based format is invalid or specifies an impermissible type of conversion, the field
displays with plus signs (++++) on the report output.

292

Syntax:

How to Define and Apply a Format Field

5. Creating Temporary Fields

With a DEFINE command:

DEFINE FILE filename
format_field/A8 = expression;
END

In a Master File:

DEFINE format_field/A8 = expression; $

In a request:

COMPUTE format_field/A8 = expression;

where:

format_field

Is the name of the field that contains the format for each row.

expression

Is the expression that assigns the format values to the format field.

After the format field is defined, you can apply it in a report request:

TABLE FILE filename
display fieldname/format_field[/just]
END

where:

display

Is any valid display command.

fieldname

Is a field in the request to be reformatted.

format_field

Is the name of the field that contains the formats. If the name of the format field is
the same as an explicit format, the explicit format is used. For example, a field named
I8 cannot be used for field-based reformatting, because it is interpreted as the explicit
format I8.

just

Is a justification option: L, R, or C. The justification option can be placed before or
after the format field, separated from the format by a slash.

Creating Reports With TIBCO® WebFOCUS Language

 293

Defining a Virtual Field

Reference: Usage Notes for Field-Based Reformatting

Field-based reformatting is supported for TABLE and TABLEF. It works with StyleSheets,
joins, and any type of data source.

Field-based reformatting is not supported for MODIFY, Maintain, MATCH, GRAPH, RECAP,
FOOTING, HEADING, or text fields.

Although you can use a DEFINE or COMPUTE command to create the format field, you
cannot apply a field-based format to a calculated or virtual field.

Field-based reformatting cannot be used on a BY sort field. It does work with an ACROSS
field.

If a report column is produced using field-based reformatting, the format used for a total or
subtotal of the column is taken from the previous detail line.

Explicit reformatting creates two display fields internally for each field that is reformatted.
Field-based reformatting creates three display fields.

Field-based formats are applied at the final output phase of report processing, while
specific formats are applied at the final output phase of report processing, while specific
formats are applied prior to performing calculations. Therefore, the dynamically reformatted
field will perform calculations, including summation, using the original format, while a field
reformatted using a specific format will use the new format for calculations. Thus, there
may be numeric differences in the final output because of rounding when using packed
fields that reduce the precision.

Field-based reformatting works for alphanumeric fields in a HOLD file, although three fields
are stored in the file for each field that is reformatted. To prevent the extra fields from
being propagated to the HOLD file, specify SET HOLDLIST=PRINTONLY.

If the number of decimal places varies between rows, the decimal points are not aligned in
the report output.

Example:

Creating Dynamically Formatted Fields

The following request formats the DOLLARS2 field according to the value of the CATEGORY
field and shows the numeric differences in sums using dynamic and static reformatting:

DEFINE FILE GGSALES
MYFORMAT/A8=DECODE CATEGORY ('Coffee' 'P15.3' 'Gifts' 'P15.0' ELSE
'P15.2');
DOLLARS2/P15.2 = DOLLARS + .5;
END

294

5. Creating Temporary Fields

TABLE FILE GGSALES
SUM DOLLARS2/MYFORMAT AS 'Dynamic' DOLLARS2/P10.2 AS 'Specific'
BY CATEGORY
ON TABLE SUBTOTAL
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
END

The output is shown in the following image:

Passing Function Calls Directly to a Relational Engine Using SQL.Function Syntax

The SQL adapters can pass virtual fields that call certain SQL scalar functions to the relational
engine for processing. This enables you to use SQL functions in a request even when they
have no equivalent in the WebFOCUS language. The function must be row-based and have a
parameter list that consists of a comma-delimited list of column names or constants. In order
to reference the function in an expression, prefix the function name with SQL.

If the virtual field is in the Master File, both TABLE requests and those SQL requests that
qualify for Automatic Passthru (APT) can access the field. If the virtual field is created by a
DEFINE FILE command, TABLE requests can access the field. The function name and
parameters are passed without translation to the relational engine. Therefore, the expression
that creates the DEFINE field must be optimized, or the request will fail.

Reference: Usage Notes for Direct SQL Function Calls

The expression containing the SQL.function call must be optimized or the request will fail
with the following message:

(FOC32605) NON OPTIMIZABLE EXPRESSION WITH SQL. SYNTAX

The function must be a row-based scalar function and have a parameter list that consists
of a comma-delimited list of column names or constants. If the function uses anything
other than a list of comma separated values, the SQL. syntax cannot be used to pass it.

Creating Reports With TIBCO® WebFOCUS Language

 295

Defining a Virtual Field

Constant DEFINE fields must be assigned a segment location using the WITH phrase.

Expressions should be declared as DEFINE fields, which are supported as parameters to an
SQL function.

Data types are not supported as parameters to an SQL function. Examples of data type
arguments are CHAR and INT for the CONVERT function and ISO, EUR, JIS, and USA for the
CHAR function.

Example:

Calling the SQL CONCAT Function in a Request

This example uses the WebFOCUS Retail demo sample. You can create this sample data
source for a relational adapter by right-clicking the application in which you want to place this
sample, and selecting New and then Samples from the context menu. Then, select WebFOCUS
- Retail Demo from the Sample procedures and data for drop-down list and click Create.

The following request against the WebFOCUS Retail demo data source uses the SQL CONCAT
function to concatenate the product category with the product subcategory.

SET TRACEUSER = ON
SET TRACEOFF = ALL
SET TRACEON = STMTRACE//CLIENT
SET TRACESTAMP=OFF
SET XRETRIEVAL = OFF

DEFINE FILE WF_RETAIL
CAT_SUBCAT/A50 = SQL.CONCAT(PRODUCT_CATEGORY, PRODUCT_SUBCATEG);
END

TABLE FILE WF_RETAIL
PRINT CAT_SUBCAT
BY PRODUCT_CATEGORY NOPRINT
END

The trace output shows that the SQL function call was passed to the RDBMS.

SELECT
CONCAT(T2."PRODUCT_CATEGORY",T2."PRODUCT_SUBCATEG"),
T2."PRODUCT_CATEGORY",
T2."PRODUCT_SUBCATEG"
FROM
wfr_product T2
ORDER BY
T2."PRODUCT_CATEGORY"
FOR FETCH ONLY;

296



5. Creating Temporary Fields

Creating a Calculated Value

A calculated value is a temporary field that is evaluated after all the data that meets the
selection criteria is retrieved, sorted, and summed. Calculated values are available only for the
specified report request.

You specify the COMPUTE command in the body of the report request, following the display
command and optionally introduced by AND. You can compute more than one field with a
single COMPUTE command.

Reference: Usage Notes for Calculated Field Values

The following apply to the use of calculated values:

If you specify any optional COMPUTE phrases (such as, AS, IN, or NORPINT), and you
compute additional fields following these phrases, you must repeat the commands
COMPUTE or AND COMPUTE before specifying the additional fields.

You can rename and justify column totals and row totals. For information, see the
examples in Including Totals and Subtotals on page 367.

Expressions in a COMPUTE command can include fields with prefix operators (see
Manipulating Display Fields With Prefix Operators on page 56). For more information on valid
expressions, see Using Expressions on page 429.

Fields referred to in a COMPUTE command are counted toward the display field limit, and
appear in the internal matrix. For details on determining the maximum number of display
fields that can be used in a request, see Displaying Report Data on page 39.

Field names used in the expression that defines the calculated field cannot be enclosed in
single or double quotation marks. Any character string enclosed in quotation marks is
treated as a literal string, not a field reference.

When using a COMPUTE with an ACROSS COLUMNS phrase, the COLUMNS should be
specified last:

ACROSS acrossfield [AND] COMPUTE compute_expression; COLUMNS values

Creating Reports With TIBCO® WebFOCUS Language

 297

Creating a Calculated Value

Syntax:

How to Create a Calculated Value

COMPUTE fld [/format] [(GEOGRAPHIC_ROLE = georole)] = expression;
  [AS 'title'] [NOPRINT] [IN [+n]]

where:

fld

Is the name of the calculated value.

The name can be any name that complies with WebFOCUS field naming rules.

Do not use field names of the type Cn, En, and Xn (where n is any sequence of one or two
digits), because they are reserved for other uses.

format

Is the format of the field. The default is D12.2. For information on formats, see the
Describing Data With WebFOCUS Language manual.

georole

Is a valid geographic role. The following is a list of default geographic roles.

ADDRESS_FULL. Full address.

ADDRESS_LINE. Number and street name.

CITY. City name.

CONTINENT. Continent name.

COUNTY. County name.

COUNTRY. Country name.

GEOMETRY_AREA. Geometry area.

GEOMETRY_LINE. Geometry line.

GEOMETRY_POINT. Geometry point.

LATITUDE. Latitude.

LONGITUDE. Longitude.

POSTAL_CODE. Postal code.

STATE. State name.

298

5. Creating Temporary Fields

expression

Can be an arithmetic and/or logical expression or function (see Using Expressions on
page 429). Each field used in the expression must be part of the request. Each
expression must end with a semicolon (;).

NOPRINT

Suppresses printing of the field. For more information, see Laying Out the Report Page
on page 1331.

AS 'title'

Changes the name of the calculated value. For more information, see Using Headings,
Footings, Titles, and Labels on page 1517.

IN [+n]

Specifies the location of the column. For more information, see Using Headings,
Footings, Titles, and Labels on page 1517. IN only works in an HTML report when the
STYLEMODE SET parameter is set to FIXED or OFF.

Syntax:

How to Create a Calculated Value Without a Calculation

COMPUTE fld [/format]= ;

where:

fld

Is the name of the calculated value.

The name can be any name that complies with WebFOCUS field naming rules.

Do not use field names of the type Cn, En, and Xn (where n is any sequence of one or two
digits), because they are reserved for other uses.

format

Is the format of the field. The default is D12.2. For information on formats, see the
Describing Data With WebFOCUS Language manual.

Creating Reports With TIBCO® WebFOCUS Language

 299

Creating a Calculated Value

Example:

Calculating a Field Value

In the following example, the COMPUTE command creates a temporary field REVENUE based
on the product of UNIT_SOLD and RETAIL_PRICE, and displays this information for New York
City. The format D12.2M indicates the field format for REVENUE and the AS command changes
the default column headings for UNIT_SOLD and RETAIL_PRICE. REVENUE is only available for
this report request.

TABLE FILE SALES
HEADING CENTER
"NEW YORK PROFIT REPORT"
" "
SUM UNIT_SOLD AS 'UNITS,SOLD' RETAIL_PRICE AS 'RETAIL,PRICE'
COMPUTE REVENUE/D12.2M = UNIT_SOLD * RETAIL_PRICE;
BY PROD_CODE AS 'PROD,CODE'
WHERE CITY EQ 'NEW YORK'
END

The output is:

       NEW YORK PROFIT REPORT

PROD  UNITS  RETAIL
CODE  SOLD   PRICE           REVENUE
----  -----  ------          -------
B10      30    $.85           $25.50
B17      20   $1.89           $37.80
B20      15   $1.99           $29.85
C13      15   $1.99           $29.85
C14      18   $2.05           $36.90
C17      12   $2.09           $25.08
D12      20   $2.09           $41.80
E1       30    $.89           $26.70
E2       33    $.99           $32.67
E3       35   $1.09           $38.15

Using Positional Column Referencing With Calculated Values

In a COMPUTE command, it is sometimes convenient to refer to a field by its report column
position, rather than its name. This option is especially useful when the same field is specified
for several report columns.

Column referencing becomes essential when you are using the same field name in a variety of
ways. The following image shows that columns produced by display commands (whether
displayed or not) can be referred to as C1 for the first column, C2 for the second column, and
so forth. The BY field columns are not counted.

For additional information about column reference numbers, see Assigning Column Reference
Numbers on page 302.

300


Example:

Using Positional Column Referencing

The following example demonstrates positional field references in a COMPUTE command:

5. Creating Temporary Fields

TABLE FILE CAR
SUM AVE.DEALER_COST
SUM AVE.DEALER_COST AND COMPUTE RATIO=C1/C2;
BY COUNTRY
END

The columns produced by display commands can be referred to as C1 for the first column
(AVE.DEALER_COST), C2 for the second column (AVE.DEALER_COST BY COUNTRY), and so
forth. The BY field columns are not counted.

The output is:

AVE                      AVE
DEALER_COST  COUNTRY     DEALER_COST           RATIO
-----------  -------     -----------           -----
      7,989  ENGLAND           9,463             .84
             FRANCE            4,631            1.73
             ITALY            10,309             .77
             JAPAN             2,756            2.90
             W GERMANY         7,795            1.02

Using ACROSS With Calculated Values

If the COMPUTE command is issued immediately following an ACROSS phrase, only a recap
type of the calculation is performed once for all columns. COMPUTE is used as part of a
display command, so a new column is calculated for each set of values.

Example:

Using COMPUTE as Part of a Display Command

TABLE FILE SALES
SUM UNIT_SOLD
COMPUTE NEWVAL = UNIT_SOLD * RETAIL_PRICE;
ACROSS CITY
END

The first page of output is:

CITY
NEW YORK            NEWARK              STAMFORD            UNIONDALE
UNIT_SOLD    NEWVAL UNIT_SOLD    NEWVAL UNIT_SOLD    NEWVAL UNIT_SOLD    NEWVAL
--------------------------------------------------------------------------------
      162  1,764.18        42    104.16       376  4,805.28        65    297.70

Creating Reports With TIBCO® WebFOCUS Language

 301

Assigning Column Reference Numbers

Example:

Using ACROSS With Calculated Values

In the following COMPUTE command, C1, C2, C3, C4, C5, and C6 are positional column
references, and the COMPUTE command follows the ACROSS phrase. The COMPUTE is
performed once for the report, and the results are displayed to the right of all sort groups.

TABLE FILE SALES
SUM UNIT_SOLD AND RETURNS
WHERE DATE GE '010' AND DATE LE '1031'
ACROSS DATE
COMPUTE
TOT_UNITS/D5=C1 + C3 + C5;
TOT_RETURNS = C2 + C4 + C6;
END

The output is:

DATE
10/17       10/18     10/19       TOT_UNITS   TOT_RETURNS              TOT_UNITS
TOT_RETURNS
UNIT_SOLD   RETURNS   UNIT_SOLD   RETURNS     UNIT_SOLD     RETURNS
------------------------------------------------------------------------------------
----------
162         15        78          2           29            1          269
18.00

Sorting Calculated Values

You can sort a report by a virtual field or a calculated value. To sort by a calculated value, you
must use the BY TOTAL phrase in your request. For details, see Sorting and Aggregating Report
Columns on page 173.

Screening on Calculated Values

You can screen on values produced by COMPUTE commands by using the WHERE TOTAL or
WHERE_GROUPED test, as described in Selecting Records for Your Report on page 217.

If you use a WHERE test, it will automatically be changed to WHERE_GROUPED, if the test is
eligible for WHERE_GROUPED processing, or to WHERE TOTAL, if it is not.

Assigning Column Reference Numbers

Column notation assigns a sequential column number to each column in the internal matrix
created for a report request. If you want to control the creation of column reference numbers
for the columns that are used in your report, use the CNOTATION column notation command.

302

5. Creating Temporary Fields

Because column numbers refer to columns in the internal matrix, they are assigned after
retrieval and aggregation of data are completed. Columns created and displayed in a report are
stored in the internal matrix, and columns that are not displayed in a report may also be
generated and stored in the internal matrix. Columns stored in the internal matrix include
calculated values, reformatted field values, BY fields, fields with the NOPRINT option, and
certain RECAP calculations such as FORECAST and REGRESS. Every other column in the
internal matrix is assigned a column number by default which means you have to account for
all internally generated columns if you want to refer to the appropriate column value in your
request.

You can change the default assignment of column reference numbers by using the SET
CNOTATION command which can assign column numbers only to columns that display in the
report output or to all fields referenced in the report request. You can use column notation in
COMPUTE and RECAP commands to refer to these columns in your request.

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

Using Column Notation in a Report Request

To create a column reference in a request, you can:

Preface the column number with a C in a non-FML request.

Use the column number as an index in conjunction with a row label in an FML request. With
this type of notation, you can specify a specific column, a relative column number, or a
sequence or series of columns.

Refer to a particular cell in an FML request using the notation E(r,c), where r is a row
number and c is a column number.

Creating Reports With TIBCO® WebFOCUS Language

 303

Assigning Column Reference Numbers

Example:

Using Column Notation in a Non-FML Request With CNOTATION=ALL

In the following request with CNOTATION=ALL, the product of C1 and C2 does not calculate
TRANSTOT times QUANTITY because the reformatting generates additional columns.

SET CNOTATION = ALL
TABLE FILE VIDEOTRK
SUM TRANSTOT/D12.2 QUANTITY/D12.2
AND COMPUTE
PRODUCT = C1 * C2;
BY TRANSDATE
END

The output is:

TRANSDATE        TRANSTOT        QUANTITY         PRODUCT
---------        --------        --------         -------
 91/06/17           57.03           12.00        3,252.42
 91/06/18           21.25            2.00          451.56
 91/06/19           38.17            5.00        1,456.95
 91/06/20           14.23            3.00          202.49
 91/06/21           44.72            7.00        1,999.88
 91/06/24          126.28           12.00       15,946.63
 91/06/25           47.74            8.00        2,279.11
 91/06/26           40.97            2.00        1,678.54
 91/06/27           60.24            9.00        3,628.85
 91/06/28           31.00            3.00          961.00

BY fields do not get a column reference, so the first column reference is for TRANSTOT with its
original format, then the reformatted version. Next is QUANTITY with its original format and
then the reformatted version. Last is the calculated value, PRODUCT.

Example:

Using Column Notation in a Non-FML Request With CNOTATION=PRINTONLY

Setting CNOTATION=PRINTONLY assigns column references to the output columns only. In this
case, the product of C1 and C2 does calculate TRANSTOT times QUANTITY.

SET CNOTATION = PRINTONLY

TABLE FILE VIDEOTRK
SUM TRANSTOT/D12.2 QUANTITY/D12.2
AND COMPUTE
PRODUCT = C1 * C2;
BY TRANSDATE
END

304


5. Creating Temporary Fields

The output is:

TRANSDATE        TRANSTOT        QUANTITY         PRODUCT
---------        --------        --------         -------
 91/06/17           57.03           12.00          684.36
 91/06/18           21.25            2.00           42.50
 91/06/19           38.17            5.00          190.85
 91/06/20           14.23            3.00           42.69
 91/06/21           44.72            7.00          313.04
 91/06/24          126.28           12.00        1,515.36
 91/06/25           47.74            8.00          381.92
 91/06/26           40.97            2.00           81.94
 91/06/27           60.24            9.00          542.16
 91/06/28           31.00            3.00           93.00

Example:

Using CNOTATION=PRINTONLY With Column Numbers in an FML Request

In the following request, the reformatting of fields generates additional columns in the internal
matrix. In the second RECAP expression, note that because of the CNOTATION setting:

TOTCASH(1) refers to total cash in displayed column 1.

TOTCASH(2) refers to total cash in displayed column 2.

The resulting calculation is displayed in column 2 of the row labeled CASH GROWTH(%).

The RECAP value is only calculated for the column specified.

SET CNOTATION=PRINTONLY
DEFINE FILE LEDGER
CUR_YR/I5C=AMOUNT;
LAST_YR/I5C=.87*CUR_YR - 142;
END
TABLE FILE LEDGER
SUM CUR_YR/F9.2 AS 'CURRENT,YEAR'
LAST_YR/F9.2 AS 'LAST,YEAR'

FOR ACCOUNT
1010 AS 'CASH ON HAND'                             OVER
1020 AS 'DEMAND DEPOSITS'                          OVER
1030 AS 'TIME DEPOSITS'                            OVER
BAR                                                OVER
RECAP TOTCASH/F9.2C= R1 + R2 + R3; AS 'TOTAL CASH' OVER
" "                                                OVER
RECAP GROCASH(2)/F9.2C=100*TOTCASH(1)/TOTCASH(2) - 100;
AS 'CASH GROWTH(%)'
END

The output is:

 CURRENT
    YEAR

    LAST
    YEAR

Creating Reports With TIBCO® WebFOCUS Language

 305


Assigning Column Reference Numbers

CASH ON HAND

 8784.00

 7216.00

DEMAND DEPOSITS

 4494.00

 3483.00

TIME DEPOSITS

 7961.00

 6499.00

--------

--------

TOTAL CASH

21239.00

17198.00

CASH GROWTH(%)

   23.50

Example:

Using CNOTATION=PRINTONLY to RECAP Over Contiguous Columns in an FML
Request

In this example, the RECAP calculation for ATOT occurs only for displayed columns 2 and 3, as
specified in the request. No calculation is performed for displayed column 1.

SET CNOTATION=PRINTONLY
DEFINE FILE LEDGER
CUR_YR/I5C=AMOUNT;
LAST_YR/I5C=.87*CUR_YR - 142;
NEXT_YR/I5C=1.13*CUR_YR + 222;
END
TABLE FILE LEDGER
SUM NEXT_YR/F9.2 CUR_YR/F9.2 LAST_YR/F9.2
FOR ACCOUNT
10$$ AS 'CASH'                      OVER
1100 AS 'ACCOUNTS RECEIVABLE'       OVER
1200 AS 'INVENTORY'                 OVER
BAR                                 OVER
RECAP ATOT(2,3)/I5C = R1 + R2 + R3;
AS 'ASSETS  ACTUAL'
END

The output is:

 NEXT_YR

  CUR_YR

 LAST_YR

CASH

25992.00

21239.00

17198.00

ACCOUNTS
RECEIVABLE

21941.00

18829.00

15954.00

INVENTORY

31522.00

27307.00

23329.00

306

5. Creating Temporary Fields

--------

--------

--------

ASSETS ACTUAL

  67,375

  56,478

Example:

Using CNOTATION=PRINTONLY With Relative Column Addressing in an FML Request

This example computes the change in cash (CHGCASH) for displayed columns 1 and 2.

SET CNOTATION=PRINTONLY
DEFINE FILE LEDGER
CUR_YR/I5C=AMOUNT;
LAST_YR/I5C=.87*CUR_YR - 142;
NEXT_YR/I5C=1.13*CUR_YR + 222;
END
TABLE FILE LEDGER
SUM NEXT_YR/F9.2 CUR_YR/F9.2 LAST_YR/F9.2
FOR ACCOUNT
10$$ AS 'TOTAL CASH' LABEL TOTCASH           OVER
" "                                          OVER
RECAP CHGCASH(1,2)/I5SC = TOTCASH(*) - TOTCASH(*+1); AS 'CHANGE IN CASH'
END

The output is:

  NEXT_YR

  CUR_YR

 LAST_YR

TOTAL CASH

 25992.00

21239.00

17198.00

CHANGE IN CASH

    4,752

   4,044

Creating Reports With TIBCO® WebFOCUS Language

 307

Assigning Column Reference Numbers

Example:

Using CNOTATION=PRINTONLY With Cell Notation in an FML Request

In this request, two RECAP expressions derive VARIANCEs (EVAR and WVAR) by subtracting
values in four displayed columns (1, 2, 3, 4) in row three (PROFIT); these values are identified
using cell notation (r,c).

SET CNOTATION=PRINTONLY
TABLE FILE REGION
SUM E_ACTUAL/F9.2 E_BUDGET/F9.2 W_ACTUAL/F9.2 W_BUDGET/F9.2
FOR ACCOUNT
3000 AS 'SALES'                         OVER
3100 AS 'COST'                          OVER
BAR                                     OVER
RECAP PROFIT/I5C = R1 - R2;             OVER
" "                                     OVER
RECAP EVAR(1)/I5C = E(3,1) - E(3,2);
AS 'EAST  VARIANCE'                     OVER
RECAP WVAR(3)/I5C = E(3,3) - E(3,4);
AS 'WEST  VARIANCE'
END

The output is:

308

5. Creating Temporary Fields

Example:

Using NOPRINT, Field Reformatting, and COMPUTE With Column Notation

The following request has a field that is not printed, several reformatted fields and three
calculated values. With SET CNOTATION=PRINTONLY, the column references result in correct
output.

SET CNOTATION = PRINTONLY
DEFINE FILE LEDGER
CUR_YR/I5C=AMOUNT;
LAST_YR/I5C=.87*CUR_YR - 142;
NEXT_YR/I5C=1.13*CUR_YR + 222;
END
TABLE FILE LEDGER
SUM NEXT_YR NOPRINT CUR_YR
COMPUTE AMT2/D6 = AMOUNT *2;
LAST_YR/D5   AMOUNT NEXT_YR
COMPUTE AMT3/D6  = AMOUNT*3;
COMPUTE AMT4/D6  = AMOUNT*4;
FOR ACCOUNT
10$$ AS 'CASH'                                 OVER
1100 AS 'ACCTS. REC.'                          OVER
1200 AS 'INVENTORY'                            OVER
BAR                                            OVER
RECAP ATOT/I8C = R1 + R2 + R3; AS 'TOTAL'      OVER
RECAP DIFF(2,10,2)/D8  = ATOT(*) - ATOT(*-1);
END

The output is:

Example:

Using Column Notation With NOPRINT in a non-FML Request

The following request, sums TRANSTOT, QUANTITY, and TRANSCODE by TRANSDATE.
TRANSTOT has the NOPRINT option, so it is not displayed on the report output. The request
also calculates the following fields using COMPUTE commands:

TTOT2, which has the same value as TRANSTOT and displays on the report output.

UNIT_COST1, which is calculated by dividing column1 by column2.

UNIT_COST2, which is calculated by dividing column1 by QUANTITY.

Creating Reports With TIBCO® WebFOCUS Language

 309

Assigning Column Reference Numbers

SET CNOTATION = ALL
TABLE FILE VIDEOTRK
SUM TRANSTOT/D7.2 NOPRINT QUANTITY/D7.2 TRANSCODE
  COMPUTE TTOT2/D7.2 = C1;
  COMPUTE UNIT_COST1/D7.2 = C1/C2;
  COMPUTE UNIT_COST2/D7.2 = C1/QUANTITY;
BY TRANSDATE
END

With this request, only CNOTATION=EXPLICIT produces the correct output. The following
discussion illustrates why the EXPLICIT setting is needed.

With CNOTATION=ALL, all fields in the internal matrix are assigned column numbers. In
particular, the request creates the following column references:

C1 is TRANSTOT with its original format.

C2 is TRANSTOT with format D7.2.

C3 is QUANTITY with its original format.

C4 is QUANTITY with format D7.2.

C5 is TRANSCODE.

UNIT_COST1 is C1/C2. These column numbers have both been assigned to TRANSTOT, so
UNIT_COST1 always equals 1. UNIT_COST2 is C1 (TRANSTOT) divided by QUANTITY. The
output is:

TRANSDATE  QUANTITY  TRANSCODE     TTOT2  UNIT_COST1  UNIT_COST2
---------  --------  ---------     -----  ----------  ----------
 91/06/17     12.00         10     57.03        1.00        4.75
 91/06/18      2.00          2     21.25        1.00       10.63
 91/06/19      5.00          4     38.17        1.00        7.63
 91/06/20      3.00          3     14.23        1.00        4.74
 91/06/21      7.00          6     44.72        1.00        6.39
 91/06/24     12.00          9    126.28        1.00       10.52
 91/06/25      8.00          7     47.74        1.00        5.97
 91/06/26      2.00          2     40.97        1.00       20.48
 91/06/27      9.00          7     60.24        1.00        6.69
 91/06/28      3.00          3     31.00        1.00       10.33

With CNOTATION = PRINTONLY, the field TRANSTOT, which has the NOPRINT option, is not
assigned any column numbers. QUANTITY with its original format is not assigned a column
number because it is not displayed on the report output. The reformatted QUANTITY field is
displayed and is assigned a column number. Therefore, the request creates the following
column references:

C1 is QUANTITY with format D7.2.

310

5. Creating Temporary Fields

C2 is TRANSCODE.

UNIT_COST1 is C1/C2, QUANTITY/TRANSCODE. UNIT_COST2 is C1 (QUANTITY) divided by
QUANTITY. Therefore, UNIT_COST2 always equals 1. The output is:

TRANSDATE  QUANTITY  TRANSCODE     TTOT2  UNIT_COST1  UNIT_COST2
---------  --------  ---------     -----  ----------  ----------
 91/06/17     12.00         10     12.00        1.20        1.00
 91/06/18      2.00          2      2.00        1.00        1.00
 91/06/19      5.00          4      5.00        1.25        1.00
 91/06/20      3.00          3      3.00        1.00        1.00
 91/06/21      7.00          6      7.00        1.17        1.00
 91/06/24     12.00          9     12.00        1.33        1.00
 91/06/25      8.00          7      8.00        1.14        1.00
 91/06/26      2.00          2      2.00        1.00        1.00
 91/06/27      9.00          7      9.00        1.29        1.00
 91/06/28      3.00          3      3.00        1.00        1.00

With CNOTATION = EXPLICIT, the reformatted TRANSTOT field is explicitly referenced in the
request, so it is assigned a column number even though it is not displayed. However, the
TRANSTOT field with its original format is not assigned a column number. The QUANTITY field
with its original format is not assigned a column number because it is not explicitly referenced
in the request. The reformatted QUANTITY field is assigned a column number. Therefore, the
request creates the following column references:

C1 is TRANSTOT with format D7.2.

C2 is QUANTITY with format D7.2.

C3 is TRANSCODE.

UNIT_COST1 is C1/C2, TRANSTOT/QUANTITY. UNIT_COST2 is C1 (TRANSTOT) divided by
QUANTITY. Therefore, UNIT_COST2 always equals UNIT_COST1. The output is:

TRANSDATE  QUANTITY  TRANSCODE     TTOT2  UNIT_COST1  UNIT_COST2
---------  --------  ---------     -----  ----------  ----------
 91/06/17     12.00         10     57.03        4.75        4.75
 91/06/18      2.00          2     21.25       10.63       10.63
 91/06/19      5.00          4     38.17        7.63        7.63
 91/06/20      3.00          3     14.23        4.74        4.74
 91/06/21      7.00          6     44.72        6.39        6.39
 91/06/24     12.00          9    126.28       10.52       10.52
 91/06/25      8.00          7     47.74        5.97        5.97
 91/06/26      2.00          2     40.97       20.48       20.48
 91/06/27      9.00          7     60.24        6.69        6.69
 91/06/28      3.00          3     31.00       10.33       10.33

Creating Reports With TIBCO® WebFOCUS Language

 311

Assigning Column Reference Numbers

Example:

Using Cell Notation in an FML Request

In the following request, CUR_YR has the NOPRINT option. The CHGCASH RECAP expression is
supposed to subtract CUR_YR from LAST_YR and NEXT_YR.

SET CNOTATION = ALL
DEFINE FILE LEDGER
CUR_YR/I7C = AMOUNT;
LAST_YR/I5C = .87*CUR_YR - 142;
NEXT_YR/I5C = 1.13*CUR_YR + 222;
END
TABLE FILE LEDGER
SUM CUR_YR/I5C NOPRINT LAST_YR NEXT_YR
FOR ACCOUNT
10$$ AS 'TOTAL CASH ' LABEL TOTCASH OVER
" " OVER
RECAP CHGCASH(1,3)/I5SC=(TOTCASH(*) - TOTCASH(1));
  AS 'CHANGE FROM CURRENT'
END

When CNOTATION = ALL, C1 refers to the CUR_YR field with its original format, C2 refers to
the reformatted value, C3 is LAST_YR, and C4 is NEXT_YR. Since there is an extra column and
the RECAP only refers to columns 1 and 3, the calculation for NEXT_YR - CUR_YR is not
performed. The output is:

                     LAST_YR  NEXT_YR
                     -------  -------
TOTAL CASH            17,195   25,991

CHANGE FROM CURRENT   -4,044

When CNOTATION = PRINTONLY, the CUR_YR field is not assigned any column number, so
there is no column 3. Therefore, no calculations are performed. The output is:

                     LAST_YR  NEXT_YR
                     -------  -------
TOTAL CASH            17,195   25,991

CHANGE FROM CURRENT

When CNOTATION = EXPLICIT, the reformatted version of the CUR_YR field is C1 because it is
referenced in the request even though it is not displayed. Both calculations are performed
correctly. The output is:

                     LAST_YR  NEXT_YR
                     -------  -------
TOTAL CASH            17,195   25,991

CHANGE FROM CURRENT   -4,044    4,752

Reference: Usage Notes for Column Numbers

BY fields are not assigned column numbers.

312




5. Creating Temporary Fields

ACROSS columns are assigned column numbers.

Calculated fields are assigned column numbers.

Column numbers outside the range of the columns created in the request are allowed
under the following circumstances (and are treated as containing the value zero):

When specified in a COMPUTE command issued after an ACROSS phrase.

In a cell reference in an FML RECAP command.

In those cases, it is not possible to know in advance how many columns will be generated
by the syntax. Using a column number outside of the range in any other context generates
the following message:

(FOC258) FIELDNAME OR COMPUTATIONAL ELEMENT NOT RECOGNIZED: column

Using FORECAST in a COMPUTE Command

A version of the FORECAST feature was implemented for use in a RECAP command. However,
the use of RECAP imposes limitations on placement of the FORECAST field in the output and
use of sort fields.

Using FORECAST in a COMPUTE command eliminates these limitations and enables you to
place the FORECAST calculation in a Master File. For the COMPUTE version of FORECAST, each
type of calculation has its own version of the FORECAST function.

Calculating Trends and Predicting Values With FORECAST

You can calculate trends in numeric data and predict values beyond the range of those stored
in the data source by using the FORECAST feature. FORECAST can be used in a report or graph
request.

The calculations you can make to identify trends and forecast values are:

Simple moving average (FORECAST_MOVAVE). Calculates a series of arithmetic means
using a specified number of values from a field. For details, see FORECAST_MOVAVE: Using
a Simple Moving Average on page 315.

Exponential moving average. Calculates a weighted average between the previously
calculated value of the average and the next data point. There are three methods for using
an exponential moving average:

Single exponential smoothing (FORECAST_EXPAVE). Calculates an average that allows
you to choose weights to apply to newer and older values. For details, see
FORECAST_EXPAVE: Using Single Exponential Smoothing on page 320.

Creating Reports With TIBCO® WebFOCUS Language

 313

Using FORECAST in a COMPUTE Command

Double exponential smoothing (FORECAST_DOUBLEXP). Accounts for the tendency of
data to either increase or decrease over time without repeating. For details, see
FORECAST_DOUBLEXP: Using Double Exponential Smoothing on page 324.

Triple exponential smoothing (FORECAST_SEASONAL). Accounts for the tendency of
data to repeat itself in intervals over time. For details, see FORECAST_SEASONAL: Using
Triple Exponential Smoothing on page 326.

Linear regression analysis (FORECAST_LINEAR). Derives the coefficients of a straight line
that best fits the data points and uses this linear equation to estimate values. For details,
see FORECAST_LINEAR: Using a Linear Regression Equation on page 331.

When predicting values in addition to calculating trends, FORECAST continues the same
calculations beyond the data points by using the generated trend values as new data points.
For the linear regression technique, the calculated regression equation is used to derive trend
and predicted values.

FORECAST performs the calculations based on the data provided, but decisions about their
use and reliability are the responsibility of the user. Therefore, the user is responsible for
determining the reliability of the FORECAST predictions, based on the many factors that
determine how accurate a prediction will be.

FORECAST Processing

You invoke FORECAST processing by including one of the FORECAST functions in a COMPUTE
command. FORECAST performs the specified calculation for all the existing data points and
then continues them to generate the number of predicted values that you request. The
parameters needed for FORECAST include the field to use in the calculations, the number of
predictions to generate, and whether to display the input field values or the calculated values
on the report output for the rows that represent existing data points.

FORECAST operates on the lowest sort field in the request. This is either the last ACROSS field
in the request or, if the request does not contain an ACROSS field, it is the last BY field. The
FORECAST calculations start over when the highest-level sort field changes its value. In a
request with multiple display commands, FORECAST operates on the last ACROSS field (or if
there are no ACROSS fields, the last BY field) of the last display command. When using an
ACROSS field with FORECAST, the display command must be SUM or COUNT.

Reference: Usage Notes for FORECAST

The sort field used for FORECAST must be in a numeric or date format.

When using simple moving average and exponential moving average methods, data values
should be spaced evenly in order to get meaningful results.

314

5. Creating Temporary Fields

The use of column notation is not supported in the FORECAST expression. Column notation
continues to be supported as before outside of this expression. The process of generating
the FORECAST values creates extra columns that are not printed in the report output. The
number and placement of these additional columns varies depending on the specific
request.

Missing values may lead to unexpected or unusable results and are not recommended for
use with FORECAST_LINEAR.

If you use the ESTRECORDS parameter to enable the external sort to better estimate the
amount of sort work space needed, you must take into account that FORECAST with
predictions creates additional records in the output.

In a styled report, you can assign specific attributes to values predicted by FORECAST with
the StyleSheet attribute WHEN=FORECAST. For example, to make the predicted values
display with the color red, use the following syntax in the TABLE request:

ON TABLE SET STYLE *
TYPE=DATA,COLUMN=MYFORECASTSORTFIELD,WHEN=FORECAST,COLOR=RED,$
ENDSTYLE

Reference: FORECAST Limits

The following are not supported with a COMPUTE command that uses FORECAST:

BY TOTAL command.

MORE, MATCH, FOR, and OVER phrases.

FORECAST_MOVAVE: Using a Simple Moving Average

A simple moving average is a series of arithmetic means calculated with a specified number of
values from a field. Each new mean in the series is calculated by dropping the first value used
in the prior calculation, and adding the next data value to the calculation.

Simple moving averages are sometimes used to analyze trends in stock prices over time. In
this scenario, the average is calculated using a specified number of periods of stock prices. A
disadvantage to this indicator is that because it drops the oldest values from the calculation
as it moves on, it loses its memory over time. Also, mean values are distorted by extreme
highs and lows, since this method gives equal weight to each point.

Predicted values beyond the range of the data values are calculated using a moving average
that treats the calculated trend values as new data points.

Creating Reports With TIBCO® WebFOCUS Language

 315

Using FORECAST in a COMPUTE Command

The first complete moving average occurs at the nth data point because the calculation
requires n values. This is called the lag. The moving average values for the lag rows are
calculated as follows: the first value in the moving average column is equal to the first data
value, the second value in the moving average column is the average of the first two data
values, and so on until the nth row, at which point there are enough values to calculate the
moving average with the number of values specified.

Syntax:

How to Calculate a Simple Moving Average Column

FORECAST_MOVAVE(display, infield, interval,
 npredict, npoint1)

where:

display

Keyword

Specifies which values to display for rows of output that represent existing data. Valid
values are:

INPUT_FIELD. This displays the original field values for rows that represent existing
data.

MODEL_DATA. This displays the calculated values for rows that represent existing
data.

Note: You can show both types of output for any field by creating two independent
COMPUTE commands in the same request, each with a different display option.

infield

Is any numeric field. It can be the same field as the result field, or a different field. It
cannot be a date-time field or a numeric field with date display options.

interval

Is the increment to add to each sort field value (after the last data point) to create the
next value. This must be a positive integer. To sort in descending order, use the BY
HIGHEST phrase. The result of adding this number to the sort field values is converted
to the same format as the sort field.

For date fields, the minimal component in the format determines how the number is
interpreted. For example, if the format is YMD, MDY, or DMY, an interval value of 2 is
interpreted as meaning two days. If the format is YM, the 2 is interpreted as meaning two
months.

316

5. Creating Temporary Fields

npredict

Is the number of predictions for FORECAST to calculate. It must be an integer greater
than or equal to zero. Zero indicates that you do not want predictions, and is only
supported with a non-recursive FORECAST.

npoint1

Is the number of values to average for the MOVAVE method.

Example:

Calculating a New Simple Moving Average Column

This request defines an integer value named PERIOD to use as the independent variable for
the moving average. It predicts three periods of values beyond the range of the retrieved data.
The MOVAVE column on the report output shows the calculated moving average numbers for
existing data points.

DEFINE FILE GGSALES
SDATE/YYM = DATE;
SYEAR/Y = SDATE;
SMONTH/M = SDATE;
PERIOD/I2 = SMONTH;
END
TABLE FILE GGSALES
SUM UNITS DOLLARS
COMPUTE  MOVAVE/D10.1= FORECAST_MOVAVE(MODEL_DATA, DOLLARS,1,3,3);
BY CATEGORY BY PERIOD
WHERE SYEAR EQ 97 AND CATEGORY NE 'Gifts'
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 317

Using FORECAST in a COMPUTE Command

The output is:

In the report, the number of values to use in the average is 3 and there are no UNITS or
DOLLARS values for the generated PERIOD values.

Each average (MOVAVE value) is computed using DOLLARS values where they exist. The
calculation of the moving average begins in the following way:

The first MOVAVE value (801,123.0) is equal to the first DOLLARS value.

318

5. Creating Temporary Fields

The second MOVAVE value (741,731.5) is the mean of DOLLARS values one and two:
(801,123 + 682,340) /2.

The third MOVAVE value (749,513.7) is the mean of DOLLARS values one through three:
(801,123 + 682,340 + 765,078) / 3.

The fourth MOVAVE value (712,897.3) is the mean of DOLLARS values two through four:
(682,340 + 765,078 + 691,274) /3.

For predicted values beyond the supplied values, the calculated MOVAVE values are used as
new data points to continue the moving average. The predicted MOVAVE values (starting with
694,975.6 for PERIOD 13) are calculated using the previous MOVAVE values as new data
points. For example, the first predicted value (694,975.6) is the average of the data points
from periods 11 and 12 (620,264 and 762,328) and the moving average for period 12
(702,334.7). The calculation is: 694,975 = (620,264 + 762,328 + 702,334.7)/3.

Example:

Displaying Original Field Values in a Simple Moving Average Column

This request defines an integer value named PERIOD to use as the independent variable for
the moving average. It predicts three periods of values beyond the range of the retrieved data.
It uses the keyword INPUT_FIELD as the first argument in the FORECAST parameter list. The
trend values do not display in the report. The actual data values for DOLLARS are followed by
the predicted values in the report column.

DEFINE FILE GGSALES
SDATE/YYM = DATE;
SYEAR/Y = SDATE;
SMONTH/M = SDATE;
PERIOD/I2 = SMONTH;
END
TABLE FILE GGSALES
SUM UNITS DOLLARS
COMPUTE MOVAVE/D10.1 = FORECAST_MOVAVE(INPUT_FIELD,DOLLARS,1,3,3);
BY CATEGORY BY PERIOD
WHERE SYEAR EQ 97 AND CATEGORY NE 'Gifts'
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

Creating Reports With TIBCO® WebFOCUS Language

 319

Using FORECAST in a COMPUTE Command

The output is shown in the following image:

FORECAST_EXPAVE: Using Single Exponential Smoothing

The single exponential smoothing method calculates an average that allows you to choose
weights to apply to newer and older values.

The following formula determines the weight given to the newest value.

k = 2/(1+n)

where:
k

Is the newest value.

320

5. Creating Temporary Fields

n

Is an integer greater than one. Increasing n increases the weight assigned to the earlier
observations (or data instances), as compared to the later ones.

The next calculation of the exponential moving average (EMA) value is derived by the following
formula:

EMA = (EMA * (1-k)) + (datavalue * k)

This means that the newest value from the data source is multiplied by the factor k and the
current moving average is multiplied by the factor (1-k). These quantities are then summed to
generate the new EMA.

Note: When the data values are exhausted, the last data value in the sort group is used as the
next data value.

Syntax:

How to Calculate a Single Exponential Smoothing Column

FORECAST_EXPAVE(display, infield, interval,
 npredict, npoint1)

where:

display

Keyword

Specifies which values to display for rows of output that represent existing data. Valid
values are:

INPUT_FIELD. This displays the original field values for rows that represent existing
data.

MODEL_DATA. This displays the calculated values for rows that represent existing
data.

Note: You can show both types of output for any field by creating two independent
COMPUTE commands in the same request, each with a different display option.

infield

Is any numeric field. It can be the same field as the result field, or a different field. It
cannot be a date-time field or a numeric field with date display options.

interval

Is the increment to add to each sort field value (after the last data point) to create the
next value. This must be a positive integer. To sort in descending order, use the BY
HIGHEST phrase. The result of adding this number to the sort field values is converted
to the same format as the sort field.

Creating Reports With TIBCO® WebFOCUS Language

 321

Using FORECAST in a COMPUTE Command

For date fields, the minimal component in the format determines how the number is
interpreted. For example, if the format is YMD, MDY, or DMY, an interval value of 2 is
interpreted as meaning two days. If the format is YM, the 2 is interpreted as meaning two
months.

npredict

Is the number of predictions for FORECAST to calculate. It must be an integer greater
than or equal to zero. Zero indicates that you do not want predictions, and is only
supported with a non-recursive FORECAST.

npoint1

For EXPAVE, this number is used to calculate the weights for each component in the
average. This value must be a positive whole number. The weight, k, is calculated by
the following formula:

k=2/(1+npoint1)

Example:

Calculating a Single Exponential Smoothing Column

The following defines an integer value named PERIOD to use as the independent variable for
the moving average. It predicts three periods of values beyond the range of retrieved data.

DEFINE FILE GGSALES
SDATE/YYM = DATE;
SYEAR/Y = SDATE;
SMONTH/M = SDATE;
PERIOD/I2 = SMONTH;
END
TABLE FILE GGSALES
SUM UNITS DOLLARS
COMPUTE EXPAVE/D10.1= FORECAST_EXPAVE(MODEL_DATA,DOLLARS,1,3,3);
BY CATEGORY BY PERIOD
WHERE SYEAR EQ 97 AND CATEGORY NE 'Gifts'
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

322

5. Creating Temporary Fields

The output is shown in the following image:

Category     PERIOD  Unit Sales  Dollar Sales        EXPAVE
--------     ------  ----------  ------------        ------
Coffee            1       61666        801123     801,123.0
                  2       54870        682340     741,731.5
                  3       61608        765078     753,404.8
                  4       57050        691274     722,339.4
                  5       59229        720444     721,391.7
                  6       58466        742457     731,924.3
                  7       60771        747253     739,588.7
                  8       54633        655896     697,742.3
                  9       57829        730317     714,029.7
                 10       57012        724412     719,220.8
                 11       51110        620264     669,742.4
                 12       58981        762328     716,035.2
                 13           0             0     739,181.6
                 14           0             0     750,754.8
                 15           0             0     756,541.4
Food              1       54394        672727     672,727.0
                  2       54894        699073     685,900.0
                  3       52713        642802     664,351.0
                  4       58026        718514     691,432.5
                  5       53289        660740     676,086.3
                  6       58742        734705     705,395.6
                  7       60127        760586     732,990.8
                  8       55622        695235     714,112.9
                  9       55787        683140     698,626.5
                 10       57340        713768     706,197.2
                 11       57459        710138     708,167.6
                 12       57290        705315     706,741.3
                 13           0             0     706,028.2
                 14           0             0     705,671.6
                 15           0             0     705,493.3

In the report, three predicted values of EXPAVE are calculated within each value of CATEGORY.
For values outside the range of the data, new PERIOD values are generated by adding the
interval value (1) to the prior PERIOD value.

Each average (EXPAVE value) is computed using DOLLARS values where they exist. The
calculation of the moving average begins in the following way:

The first EXPAVE value (801,123.0) is the same as the first DOLLARS value.

The second EXPAVE value (741,731.5) is calculated as follows. Note that because of
rounding and the number of decimal places used, the value derived in this sample
calculation varies slightly from the one displayed in the report output:

n=3 (number used to calculate weights)

k = 2/(1+n) = 2/4 = 0.5

EXPAVE = (EXPAVE*(1-k))+(new-DOLLARS*k) = (801123*0.5) + (682340*0.50) =
400561.5 + 341170 = 741731.5

Creating Reports With TIBCO® WebFOCUS Language

 323

Using FORECAST in a COMPUTE Command

The third EXPAVE value (753,404.8) is calculated as follows:

EXPAVE = (EXPAVE*(1-k))+(new-DOLLARS*k) = (741731.5*0.5)+(765078*0.50) =
370865.75 + 382539 = 753404.75

FORECAST_DOUBLEXP: Using Double Exponential Smoothing

Double exponential smoothing produces an exponential moving average that takes into
account the tendency of data to either increase or decrease over time without repeating. This
is accomplished by using two equations with two constants.

The first equation accounts for the current time period and is a weighted average of the
current data value and the prior average, with an added component (b) that represents the
trend for the previous period. The weight constant is k:

DOUBLEXP(t) = k * datavalue(t) + (1-k) * ((DOUBLEXP(t-1) + b(t-1))

The second equation is the calculated trend value, and is a weighted average of the
difference between the current and previous average and the trend for the previous time
period. b(t) represents the average trend. The weight constant is g:

b(t) = g * (DOUBLEXP(t)-DOUBLEXP(t-1)) + (1 - g) * (b(t-1))

These two equations are solved to derive the smoothed average. The first smoothed average is
set to the first data value. The first trend component is set to zero. For choosing the two
constants, the best results are usually obtained by minimizing the mean-squared error (MSE)
between the data values and the calculated averages. You may need to use nonlinear
optimization techniques to find the optimal constants.

The equation used for forecasting beyond the data points with double exponential smoothing is

forecast(t+m) = DOUBLEXP(t) + m * b(t)

where:

m

Is the number of time periods ahead for the forecast.

Syntax:

How to Calculate a Double Exponential Smoothing Column

FORECAST_DOUBLEXP(display, infield,
interval, npredict, npoint1, npoint2)

324

5. Creating Temporary Fields

where:

display

Keyword

Specifies which values to display for rows of output that represent existing data. Valid
values are:

INPUT_FIELD. This displays the original field values for rows that represent existing
data.

MODEL_DATA. This displays the calculated values for rows that represent existing
data.

Note: You can show both types of output for any field by creating two independent
COMPUTE commands in the same request, each with a different display option.

infield

Is any numeric field. It can be the same field as the result field, or a different field. It
cannot be a date-time field or a numeric field with date display options.

interval

Is the increment to add to each sort field value (after the last data point) to create the
next value. This must be a positive integer. To sort in descending order, use the BY
HIGHEST phrase. The result of adding this number to the sort field values is converted
to the same format as the sort field.

For date fields, the minimal component in the format determines how the number is
interpreted. For example, if the format is YMD, MDY, or DMY, an interval value of 2 is
interpreted as meaning two days. If the format is YM, the 2 is interpreted as meaning two
months.

npredict

Is the number of predictions for FORECAST to calculate. It must be an integer greater
than or equal to zero. Zero indicates that you do not want predictions, and is only
supported with a non-recursive FORECAST.

npoint1

For DOUBLEXP, this number is used to calculate the weights for each component in
the average. This value must be a positive whole number. The weight, k, is calculated
by the following formula:

k=2/(1+npoint1)

npoint2

For DOUBLEXP, this positive whole number is used to calculate the weights for each
term in the trend. The weight, g, is calculated by the following formula:

Creating Reports With TIBCO® WebFOCUS Language

 325

Using FORECAST in a COMPUTE Command

g=2/(1+npoint2)

Example:

Calculating a Double Exponential Smoothing Column

The following sums the TRANSTOT field of the VIDEOTRK data source by TRANSDATE, and
calculates a single exponential and double exponential moving average. The report columns
show the calculated values for existing data points.

TABLE FILE VIDEOTRK
SUM TRANSTOT
COMPUTE EXP/D15.1 = FORECAST_EXPAVE(MODEL_DATA,TRANSTOT,1,0,3);
DOUBLEXP/D15.1 = FORECAST_DOUBLEXP(MODEL_DATA,TRANSTOT,1,0,3,3);
BY TRANSDATE
WHERE TRANSDATE NE '19910617'
ON TABLE SET STYLE *
GRID=OFF,$
END

The output is shown in the following image:

FORECAST_SEASONAL: Using Triple Exponential Smoothing

Triple exponential smoothing produces an exponential moving average that takes into account
the tendency of data to repeat itself in intervals over time. For example, sales data that is
growing and in which 25% of sales always occur during December contains both trend and
seasonality. Triple exponential smoothing takes both the trend and seasonality into account by
using three equations with three constants.

326


5. Creating Temporary Fields

For triple exponential smoothing you, need to know the number of data points in each time
period (designated as L in the following equations). To account for the seasonality, a seasonal
index is calculated. The data is divided by the prior season index and then used in calculating
the smoothed average.

The first equation accounts for the current time period, and is a weighted average of the
current data value divided by the seasonal factor and the prior average adjusted for the
trend for the previous period. The weight constant is k:

SEASONAL(t) = k * (datavalue(t)/I(t-L)) + (1-k) * (SEASONAL(t-1) +
b(t-1))

The second equation is the calculated trend value, and is a weighted average of the
difference between the current and previous average and the trend for the previous time
period. b(t) represents the average trend. The weight constant is g:

b(t) = g * (SEASONAL(t)-SEASONAL(t-1)) + (1-g) * (b(t-1))

The third equation is the calculated seasonal index, and is a weighted average of the
current data value divided by the current average and the seasonal index for the previous
season. I(t) represents the average seasonal coefficient. The weight constant is p:

I(t) = p * (datavalue(t)/SEASONAL(t)) + (1 - p) * I(t-L)

These equations are solved to derive the triple smoothed average. The first smoothed average
is set to the first data value. Initial values for the seasonality factors are calculated based on
the maximum number of full periods of data in the data source, while the initial trend is
calculated based on two periods of data. These values are calculated with the following steps:

1. The initial trend factor is calculated by the following formula:

b(0) = (1/L) ((y(L+1)-y(1))/L + (y(L+2)-y(2))/L + ... + (y(2L) -
y(L))/L )

2. The calculation of the initial seasonality factor is based on the average of the data values

within each period, A(j) (1<=j<=N):

A(j) = ( y((j-1)L+1) + y((j-1)L+2) + ... + y(jL) ) / L

3. Then, the initial periodicity factor is given by the following formula, where N is the number
of full periods available in the data, L is the number of points per period and n is a point
within the period (1<= n <= L):

I(n) = ( y(n)/A(1) + y(L+n)/A(2) + ... + y((N-1)L+n)/A(N) ) / N

Creating Reports With TIBCO® WebFOCUS Language

 327

Using FORECAST in a COMPUTE Command

The three constants must be chosen carefully. The best results are usually obtained by
choosing the constants to minimize the mean-squared error (MSE) between the data values
and the calculated averages. Varying the values of npoint1 and npoint2 affect the results, and
some values may produce a better approximation. To search for a better approximation, you
may want to find values that minimize the MSE.

The equation used to forecast beyond the last data point with triple exponential smoothing is:

forecast(t+m) = (SEASONAL(t) + m * b(t)) / I(t-L+MOD(m/L))

where:

m

Is the number of periods ahead for the forecast.

Syntax:

How to Calculate a Triple Exponential Smoothing Column

FORECAST_SEASONAL(display, infield,
interval, npredict, nperiod, npoint1, npoint2, npoint3)

where:

display

Keyword

Specifies which values to display for rows of output that represent existing data. Valid
values are:

INPUT_FIELD. This displays the original field values for rows that represent existing
data.

MODEL_DATA. This displays the calculated values for rows that represent existing
data.

Note: You can show both types of output for any field by creating two independent
COMPUTE commands in the same request, each with a different display option.

infield

Is any numeric field. It can be the same field as the result field, or a different field. It
cannot be a date-time field or a numeric field with date display options.

interval

Is the increment to add to each sort field value (after the last data point) to create the
next value. This must be a positive integer. To sort in descending order, use the BY
HIGHEST phrase. The result of adding this number to the sort field values is converted
to the same format as the sort field.

328

5. Creating Temporary Fields

For date fields, the minimal component in the format determines how the number is
interpreted. For example, if the format is YMD, MDY, or DMY, an interval value of 2 is
interpreted as meaning two days. If the format is YM, the 2 is interpreted as meaning two
months.

npredict

Is the number of predictions for FORECAST to calculate. It must be an integer greater
than or equal to zero. Zero indicates that you do not want predictions, and is only
supported with a non-recursive FORECAST. For the SEASONAL method, npredict is the
number of periods to calculate. The number of points generated is:

nperiod * npredict

nperiod

For the SEASONAL method, is a positive whole number that specifies the number of
data points in a period.

npoint1

For SEASONAL, this number is used to calculate the weights for each component in
the average. This value must be a positive whole number. The weight, k, is calculated
by the following formula:

k=2/(1+npoint1)

npoint2

For SEASONAL, this positive whole number is used to calculate the weights for each
term in the trend. The weight, g, is calculated by the following formula:

g=2/(1+npoint2)

npoint3

For SEASONAL, this positive whole number is used to calculate the weights for each
term in the seasonal adjustment. The weight, p, is calculated by the following formula:

p=2/(1+npoint3)

Creating Reports With TIBCO® WebFOCUS Language

 329

Using FORECAST in a COMPUTE Command

Example:

Calculating a Triple Exponential Smoothing Column

In the following, the data has seasonality but no trend. Therefore, npoint2 is set high (1000) to
make the trend factor negligible in the calculation:

TABLE FILE VIDEOTRK
SUM TRANSTOT
COMPUTE SEASONAL/D10.1 = FORECAST_SEASONAL(MODEL_DATA,TRANSTOT,
1,3,3,3,1000,1);
BY TRANSDATE
WHERE TRANSDATE NE '19910617'
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

In the output, npredict is 3. Therefore, three periods (nine points, nperiod * npredict) are
generated.

330

5. Creating Temporary Fields

FORECAST_LINEAR: Using a Linear Regression Equation

The linear regression equation estimates values by assuming that the dependent variable (the
new calculated values) and the independent variable (the sort field values) are related by a
function that represents a straight line:

y = mx + b

where:

y

x

m

b

Is the dependent variable.

Is the independent variable.

Is the slope of the line.

Is the y-intercept.

FORECAST_LINEAR uses a technique called Ordinary Least Squares to calculate values for m
and b that minimize the sum of the squared differences between the data and the resulting
line.

The following formulas show how m and b are calculated.

where:

n

y

x

Is the number of data points.

Is the data values (dependent variables).

Is the sort field values (independent variables).

Trend values, as well as predicted values, are calculated using the regression line equation.

Creating Reports With TIBCO® WebFOCUS Language

 331

Using FORECAST in a COMPUTE Command

Syntax:

How to Calculate a Linear Regression Column

FORECAST_LINEAR(display, infield, interval,
 npredict)

where:

display

Keyword

Specifies which values to display for rows of output that represent existing data. Valid
values are:

INPUT_FIELD. This displays the original field values for rows that represent existing
data.

MODEL_DATA. This displays the calculated values for rows that represent existing
data.

Note: You can show both types of output for any field by creating two independent
COMPUTE commands in the same request, each with a different display option.

infield

Is any numeric field. It can be the same field as the result field, or a different field. It
cannot be a date-time field or a numeric field with date display options.

interval

Is the increment to add to each sort field value (after the last data point) to create the
next value. This must be a positive integer. To sort in descending order, use the BY
HIGHEST phrase. The result of adding this number to the sort field values is converted
to the same format as the sort field.

For date fields, the minimal component in the format determines how the number is
interpreted. For example, if the format is YMD, MDY, or DMY, an interval value of 2 is
interpreted as meaning two days. If the format is YM, the 2 is interpreted as meaning two
months.

npredict

Is the number of predictions for FORECAST to calculate. It must be an integer greater
than or equal to zero. Zero indicates that you do not want predictions, and is only
supported with a non-recursive FORECAST.

332

Example:

Calculating a New Linear Regression Field

The following request calculates a regression line using the VIDEOTRK data source of
QUANTITY by TRANSDATE. The interval is one day, and three predicted values are calculated.

5. Creating Temporary Fields

TABLE FILE VIDEOTRK
SUM QUANTITY
COMPUTE FORTOT=FORECAST_LINEAR(MODEL_DATA,QUANTITY,1,3);
BY TRANSDATE
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
ENDSTYLE
END

The output is shown in the following image:

Note:

Three predicted values of FORTOT are calculated. For values outside the range of the data,
new TRANSDATE values are generated by adding the interval value (1) to the prior
TRANSDATE value.

There are no QUANTITY values for the generated FORTOT values.

Each FORTOT value is computed using a regression line, calculated using all of the actual
data values for QUANTITY.

Creating Reports With TIBCO® WebFOCUS Language

 333

Using FORECAST in a COMPUTE Command

TRANSDATE is the independent variable (x) and QUANTITY is the dependent variable (y).
The equation is used to calculate QUANTITY FORECAST trend and predicted values.

The following version of the request charts the data values and the regression line.

GRAPH FILE VIDEOTRK
SUM QUANTITY
COMPUTE FORTOT=FORECAST_LINEAR(MODEL_DATA,QUANTITY,1,3);
BY TRANSDATE
ON GRAPH PCHOLD FORMAT JSCHART
ON GRAPH SET LOOKGRAPH VLINE
END

The output is shown in the following image.

Distinguishing Data Rows From Predicted Rows

To make the report output easier to interpret, you can create a field that indicates whether the
FORECAST value in each row is a predicted value. To do this, define a virtual field whose value
is a constant other than zero. Rows in the report output that represent actual records in the
data source will appear with a value that is not zero. Rows that represent predicted values will
display zero. You can also propagate this field to a HOLD file.

334

5. Creating Temporary Fields

Example:

Distinguishing Data Rows From Predicted Rows

In the following example, the DATA_ROW virtual field has the value 1 for each row in the data
source. It has the value zero for the predicted rows. The PREDICT field is calculated as YES for
predicted rows, and NO for rows containing data. In addition, the StyleSheet attribute
WHEN=FORECAST is used to display the predicted values for the FORTOT field in red.

DEFINE FILE VIDEOTRK
DATA_ROW/I1 = 1;
END
TABLE FILE VIDEOTRK
SUM TRANSTOT DATA_ROW
COMPUTE
PREDICT/A3 = IF DATA_ROW NE 0 THEN 'NO' ELSE 'YES' ;
FORTOT/D12.2=FORECAST_LINEAR(MODEL_DATA,TRANSTOT,1,3);
BY TRANSDATE
ON TABLE SET PAGE NOLEAD
ON TABLE SET STYLE *
GRID=OFF,$
TYPE=DATA, COLUMN=FORTOT, WHEN=FORECAST, COLOR=RED,$
ENDSTYLE
END

The output is shown in the following image:

Creating Reports With TIBCO® WebFOCUS Language

 335

Calculating Trends and Predicting Values With FORECAST

Calculating Trends and Predicting Values With FORECAST

You can calculate trends in numeric data and predict values beyond the range of those stored
in the data source by using the FORECAST feature. FORECAST can be used in a report or graph
request.

The calculations you can make to identify trends and forecast values are:

Simple moving average (MOVAVE). Calculates a series of arithmetic means using a
specified number of values from a field. For details, see Using a Simple Moving Average on
page 341.

Exponential moving average. Calculates a weighted average between the previously
calculated value of the average and the next data point. There are three methods for using
an exponential moving average:

Single exponential smoothing (EXPAVE). Calculates an average that allows you to
choose weights to apply to newer and older values. For details, see Using Single
Exponential Smoothing on page 345.

Double exponential smoothing (DOUBLEXP). Accounts for the tendency of data to
either increase or decrease over time without repeating. For details, see Using Double
Exponential Smoothing on page 347.

Triple exponential smoothing (SEASONAL). Accounts for the tendency of data to repeat
itself in intervals over time. For details, see Using Triple Exponential Smoothing on page
349.

Linear regression analysis (REGRESS). Derives the coefficients of a straight line that best
fits the data points and uses this linear equation to estimate values. For details, see Usage
Notes for Creating Virtual Fields on page 281.

When predicting values in addition to calculating trends, FORECAST continues the same
calculations beyond the data points by using the generated trend values as new data points.
For the linear regression technique, the calculated regression equation is used to derive trend
and predicted values.

FORECAST performs the calculations based on the data provided, but decisions about their
use and reliability are the responsibility of the user. Therefore, FORECAST predictions are not
always reliable, and many factors determine how accurate a prediction will be.

336

FORECAST Processing

5. Creating Temporary Fields

You invoke FORECAST processing by including FORECAST in a RECAP command. In this
command, you specify the parameters needed for generating estimated values, including the
field to use in the calculations, the type of calculation to use, and the number of predictions to
generate. The RECAP field that contains the result of FORECAST can be a new field (non-
recursive) or the same field used in the FORECAST calculations (recursive):

In a recursive FORECAST, the RECAP field that contains the results is also the field used to
generate the FORECAST calculations. In this case, the original field is not printed even if it
was referenced in the display command, and the RECAP column contains the original field
values followed by the number of predicted values specified in the FORECAST syntax. No
trend values display in the report. However, the original column is stored in an output file
unless you set HOLDLIST to PRINTONLY.

In a non-recursive FORECAST, a new field contains the results of FORECAST calculations.
The new field is displayed in the report along with the original field when it is referenced in
the display command. The new field contains trend values and forecast values when
specified.

FORECAST operates on the last ACROSS field in the request. If the request does not contain
an ACROSS field, it operates on the last BY field. The FORECAST calculations start over when
the highest-level sort field changes its value. In a request with multiple display commands,
FORECAST operates on the last ACROSS field (or if there are no ACROSS fields, the last BY
field) of the last display command. When using an ACROSS field with FORECAST, the display
command must be SUM or COUNT.

Note: Although you pass parameters to FORECAST using an argument list in parentheses,
FORECAST is not a function. It can coexist with a function of the same name, as long as the
function is not specified in a RECAP command.

Syntax:

How to Calculate Trends and Predict Values

MOVAVE calculation

ON sortfield RECAP result_field[/fmt] = FORECAST(infield, interval,
 npredict, 'MOVAVE',npoint1)sendstyle

EXPAVE calculation

ON sortfield RECAP result_field[/fmt] = FORECAST(infield, interval,
 npredict, 'EXPAVE',npoint1);

Creating Reports With TIBCO® WebFOCUS Language

 337

Calculating Trends and Predicting Values With FORECAST

DOUBLEXP calculation

ON sortfield RECAP fld1[/fmt] = FORECAST(infield,
interval, npredict, 'DOUBLEXP',npoint1, npoint2);

SEASONAL calculation

ON sortfield RECAP fld1[/fmt] = FORECAST(infield,
interval, npredict, 'SEASONAL', nperiod, npoint1, npoint2, npoint3);

REGRESS calculation

ON sortfield RECAP result_field[/fmt] = FORECAST(infield, interval,
 npredict, 'REGRESS');

where:

sortfield

Is the last ACROSS field in the request. This field must be in numeric or date format.
If the request does not contain an ACROSS field, FORECAST works on the last BY
field.

result_field

Is the field containing the result of FORECAST. It can be a new field, or the same as
infield. This must be a numeric field; either a real field, a virtual field, or a calculated
field.

Note: The word FORECAST and the opening parenthesis must be on the same line as the
syntax sortfield=.

fmt

Is the display format for result_field. The default format is D12.2. If result_field was
previously reformatted using a DEFINE or COMPUTE command, the format specified in
the RECAP command is respected.

infield

Is any numeric field. It can be the same field as result_field, or a different field. It
cannot be a date-time field or a numeric field with date display options.

interval

Is the increment to add to each sortfield value (after the last data point) to create the
next value. This must be a positive integer. To sort in descending order, use the BY
HIGHEST phrase. The result of adding this number to the sortfield values is converted
to the same format as sortfield.

For date fields, the minimal component in the format determines how the number is
interpreted. For example, if the format is YMD, MDY, or DMY, an interval value of 2 is
interpreted as meaning two days; if the format is YM, the 2 is interpreted as meaning two
months.

338

5. Creating Temporary Fields

npredict

Is the number of predictions for FORECAST to calculate. It must be an integer greater
than or equal to zero. Zero indicates that you do not want predictions, and is only
supported with a non-recursive FORECAST. For the SEASONAL method, npredict is the
number of periods to calculate. The number of points generated is:

nperiod * npredict

nperiod

For the SEASONAL method, is a positive whole number that specifies the number of
data points in a period.

npoint1

Is the number of values to average for the MOVAVE method. For EXPAVE, DOUBLEXP,
and SEASONAL, this number is used to calculate the weights for each component in
the average. This value must be a positive whole number. The weight, k, is calculated
by the following formula:

k=2/(1+npoint1)

npoint2

For DOUBLEXP and SEASONAL, this positive whole number is used to calculate the
weights for each term in the trend. The weight, g, is calculated by the following
formula:

g=2/(1+npoint2)

npoint3

For SEASONAL, this positive whole number is used to calculate the weights for each
term in the seasonal adjustment. The weight, p, is calculated by the following formula:

p=2/(1+npoint3)

Reference: Usage Notes for FORECAST

The sort field used for FORECAST must be in a numeric or date format.

When using simple moving average and exponential moving average methods, data values
should be spaced evenly in order to get meaningful results.

When using a RECAP command with FORECAST, the command can contain only the
FORECAST syntax. FORECAST does not recognize any syntax after the closing semicolon (;).
To specify options such as AS or IN:

In a non-recursive FORECAST request, use an empty COMPUTE command prior to the
RECAP.

Creating Reports With TIBCO® WebFOCUS Language

 339

Calculating Trends and Predicting Values With FORECAST

In a recursive FORECAST request, specify the options when the field is first referenced
in the report request.

The use of column notation is not supported in a request that includes FORECAST. The
process of generating the FORECAST values creates extra columns that are not printed in
the report output. The number and placement of these additional columns varies depending
on the specific request.

A request can contain up to seven non-FORECAST RECAP commands and up to seven
additional FORECAST RECAP commands.

The left side of a RECAP command used for FORECAST supports the CURR attribute for
creating a currency-denominated field.

Recursive and non-recursive REGRESS are not supported in the same request when the
display command is SUM, ADD, or WRITE.

Missing values are not supported with REGRESS.

If you use the ESTRECORDS parameter to enable the external sort to estimate better the
amount of sort work space needed, you must take into account that FORECAST with
predictions creates additional records in the output.

In a styled report, you can assign specific attributes to values predicted by FORECAST with
the StyleSheet attribute WHEN=FORECAST. For example, to make the predicted values
display with the color red, use the following syntax in the TABLE request:

ON TABLE SET STYLE
*TYPE=DATA,COLUMN=MYFORECASTSORTFIELD,WHEN=FORECAST,COLOR=RED,
$ENDSTYLE

Reference: FORECAST Limits

The following are not supported with a RECAP command that uses FORECAST:

BY TOTAL command.

MORE, MATCH, FOR, and OVER phrases.

SUMMARIZE and RECOMPUTE are not supported for the same sort field used for
FORECAST.

MISSING attribute.

340

Using a Simple Moving Average

5. Creating Temporary Fields

A simple moving average is a series of arithmetic means calculated with a specified number of
values from a field. Each new mean in the series is calculated by dropping the first value used
in the prior calculation, and adding the next data value to the calculation.

Simple moving averages are sometimes used to analyze trends in stock prices over time. In
this scenario, the average is calculated using a specified number of periods of stock prices. A
disadvantage to this indicator is that because it drops the oldest values from the calculation
as it moves on, it loses its memory over time. Also, mean values are distorted by extreme
highs and lows, since this method gives equal weight to each point.

Predicted values beyond the range of the data values are calculated using a moving average
that treats the calculated trend values as new data points.

The first complete moving average occurs at the nth data point because the calculation
requires n values. This is called the lag. The moving average values for the lag rows are
calculated as follows: the first value in the moving average column is equal to the first data
value, the second value in the moving average column is the average of the first two data
values, and so on until the nth row, at which point there are enough values to calculate the
moving average with the number of values specified.

Example:

Calculating a New Simple Moving Average Column

This request defines an integer value named PERIOD to use as the independent variable for
the moving average. It predicts three periods of values beyond the range of the retrieved data.

DEFINE FILE GGSALES
 SDATE/YYM = DATE;
 SYEAR/Y = SDATE;
 SMONTH/M = SDATE;
 PERIOD/I2 = SMONTH;
END
TABLE FILE GGSALES
  SUM UNITS DOLLARS
  BY  CATEGORY BY PERIOD
  WHERE SYEAR EQ 97 AND CATEGORY NE 'Gifts'
  ON PERIOD RECAP MOVAVE/D10.1= FORECAST(DOLLARS,1,3,'MOVAVE',3);
END

Creating Reports With TIBCO® WebFOCUS Language

 341

Calculating Trends and Predicting Values With FORECAST

The output is:

In the report, the number of values to use in the average is 3 and there are no UNITS or
DOLLARS values for the generated PERIOD values.

Each average (MOVAVE value) is computed using DOLLARS values where they exist. The
calculation of the moving average begins in the following way:

The first MOVAVE value (801,123.0) is equal to the first DOLLARS value.

342

5. Creating Temporary Fields

The second MOVAVE value (741,731.5) is the mean of DOLLARS values one and two:
(801,123 + 682,340) /2.

The third MOVAVE value (749,513.7) is the mean of DOLLARS values one through three:
(801,123 + 682,340 + 765,078) / 3.

The fourth MOVAVE value (712,897.3) is the mean of DOLLARS values two through four:
(682,340 + 765,078 + 691,274) /3.

For predicted values beyond the supplied values, the calculated MOVAVE values are used as
new data points to continue the moving average. The predicted MOVAVE values (starting with
694,975.6 for PERIOD 13) are calculated using the previous MOVAVE values as new data
points. For example, the first predicted value (694,975.6) is the average of the data points
from periods 11 and 12 (620,264 and 762,328) and the moving average for period 12
(702,334.7). The calculation is: 694,975 = (620,264 + 762,328 + 702,334.7)/3.

Example:

Using an Existing Field as a Simple Moving Average Column

This request defines an integer value named PERIOD to use as the independent variable for
the moving average. It predicts three periods of values beyond the range of the retrieved data.
It uses the same name for the RECAP field as the first argument in the FORECAST parameter
list. The trend values do not display in the report. The actual data values for DOLLARS are
followed by the predicted values in the report column.

DEFINE FILE GGSALES
 SDATE/YYM = DATE;
 SYEAR/Y = SDATE;
 SMONTH/M = SDATE;
 PERIOD/I2 = SMONTH;
END
TABLE FILE GGSALES
  SUM UNITS DOLLARS
  BY  CATEGORY BY PERIOD
  WHERE SYEAR EQ 97 AND CATEGORY NE 'Gifts'
  ON PERIOD RECAP DOLLARS/D10.1 = FORECAST(DOLLARS,1,3,'MOVAVE',3);
END

Creating Reports With TIBCO® WebFOCUS Language

 343

Calculating Trends and Predicting Values With FORECAST

The output is:

344

5. Creating Temporary Fields

Using Single Exponential Smoothing

The single exponential smoothing method calculates an average that allows you to choose
weights to apply to newer and older values.

The following formula determines the weight given to the newest value.

k = 2/(1+n)

where:

k

n

Is the newest value.

Is an integer greater than one. Increasing n increases the weight assigned to the earlier
observations (or data instances), as compared to the later ones.

The next calculation of the exponential moving average (EMA) value is derived by the following
formula:

EMA = (EMA * (1-k)) + (datavalue * k)

This means that the newest value from the data source is multiplied by the factor k and the
current moving average is multiplied by the factor (1-k). These quantities are then summed to
generate the new EMA.

Note: When the data values are exhausted, the last data value in the sort group is used as the
next data value.

Example:

Calculating a Single Exponential Smoothing Column

The following defines an integer value named PERIOD to use as the independent variable for
the moving average. It predicts three periods of values beyond the range of retrieved data.

DEFINE FILE GGSALES
 SDATE/YYM = DATE;
 SYEAR/Y = SDATE;
 SMONTH/M = SDATE;
 PERIOD/I2 = SMONTH;
END
TABLE FILE GGSALES
  SUM UNITS DOLLARS
  BY  CATEGORY BY PERIOD
  WHERE SYEAR EQ 97 AND CATEGORY NE 'Gifts'
  ON PERIOD RECAP EXPAVE/D10.1= FORECAST(DOLLARS,1,3,'EXPAVE',3);
END

Creating Reports With TIBCO® WebFOCUS Language

 345

Calculating Trends and Predicting Values With FORECAST

The output is:

In the report, three predicted values of EXPAVE are calculated within each value of CATEGORY.
For values outside the range of the data, new PERIOD values are generated by adding the
interval value (1) to the prior PERIOD value.

Each average (EXPAVE value) is computed using DOLLARS values where they exist. The
calculation of the moving average begins in the following way:

The first EXPAVE value (801,123.0) is the same as the first DOLLARS value.

346

5. Creating Temporary Fields

The second EXPAVE value (741,731.5) is calculated as follows. Note that because of
rounding and the number of decimal places used, the value derived in this sample
calculation varies slightly from the one displayed in the report output:

n=3 (number used to calculate weights)

k = 2/(1+n) = 2/4 = 0.5

EXPAVE = (EXPAVE*(1-k))+(new-DOLLARS*k) = (801123*0.5) + (682340*0.50) =
400561.5 + 341170 = 741731.5

The third EXPAVE value (753,404.8) is calculated as follows:

EXPAVE = (EXPAVE*(1-k))+(new-DOLLARS*k) = (741731.5*0.5)+(765078*0.50) =
370865.75 + 382539 = 753404.75

For predicted values beyond those supplied, the last EXPAVE value is used as the new data
point in the exponential smoothing calculation. The predicted EXPAVE values (starting with
706,741.6) are calculated using the previous average and the new data point. Because the
previous average is also used as the new data point, the predicted values are always equal to
the last trend value. For example, the previous average for period 13 is 706,741.6, and this is
also used as the next data point. Therefore, the average is calculated as follows: (706,741.6
* 0.5) + (706,741.6 * 0.5) = 706,741.6

EXPAVE = (EXPAVE * (1-k)) + (new-DOLLARS * k) = (706741.6*0.5) +
         (706741.6*0.50) =  353370.8 + 353370.8 = 706741.6

Using Double Exponential Smoothing

Double exponential smoothing produces an exponential moving average that takes into
account the tendency of data to either increase or decrease over time without repeating. This
is accomplished by using two equations with two constants.

The first equation accounts for the current time period and is a weighted average of the
current data value and the prior average, with an added component (b) that represents the
trend for the previous period. The weight constant is k:

DOUBLEXP(t) = k * datavalue(t) + (1-k) * ((DOUBLEXP(t-1) + b(t-1))

The second equation is the calculated trend value, and is a weighted average of the
difference between the current and previous average and the trend for the previous time
period. b(t) represents the average trend. The weight constant is g:

b(t) = g * (DOUBLEXP(t)-DOUBLEXP(t-1)) + (1 - g) * (b(t-1))

Creating Reports With TIBCO® WebFOCUS Language

 347

Calculating Trends and Predicting Values With FORECAST

These two equations are solved to derive the smoothed average. The first smoothed average is
set to the first data value. The first trend component is set to zero. For choosing the two
constants, the best results are usually obtained by minimizing the mean-squared error (MSE)
between the data values and the calculated averages. You may need to use nonlinear
optimization techniques to find the optimal constants.

The equation used for forecasting beyond the data points with double exponential smoothing is

forecast(t+m) = DOUBLEXP(t) + m * b(t)

where:

m

Is the number of time periods ahead for the forecast.

Example:

Calculating a Double Exponential Smoothing Column

The following defines an integer value named PERIOD to use as the independent variable for
the moving average. The double exponential smoothing method estimates the trend in the data
points better than the single smoothing method:

SET HISTOGRAM = OFF
TABLE FILE CENTSTMT
SUM ACTUAL_YTD
  BY PERIOD
  ON PERIOD RECAP EXP/D15.1 = FORECAST(ACTUAL_YTD,1,0,'EXPAVE',3);
  ON PERIOD RECAP DOUBLEXP/D15.1 = FORECAST(ACTUAL_YTD,1,0,
     'DOUBLEXP',3,3);
WHERE GL_ACCOUNT LIKE '3%%%'
END

The output is:

348


Using Triple Exponential Smoothing

5. Creating Temporary Fields

Triple exponential smoothing produces an exponential moving average that takes into account
the tendency of data to repeat itself in intervals over time. For example, sales data that is
growing and in which 25% of sales always occur during December contains both trend and
seasonality. Triple exponential smoothing takes both the trend and seasonality into account by
using three equations with three constants.

For triple exponential smoothing you, need to know the number of data points in each time
period (designated as L in the following equations). To account for the seasonality, a seasonal
index is calculated. The data is divided by the prior season index and then used in calculating
the smoothed average.

The first equation accounts for the current time period, and is a weighted average of the
current data value divided by the seasonal factor and the prior average adjusted for the
trend for the previous period. The weight constant is k:

SEASONAL(t) = k * (datavalue(t)/I(t-L)) + (1-k) * (SEASONAL(t-1) +
b(t-1))

The second equation is the calculated trend value, and is a weighted average of the
difference between the current and previous average and the trend for the previous time
period. b(t) represents the average trend. The weight constant is g:

b(t) = g * (SEASONAL(t)-SEASONAL(t-1)) + (1-g) * (b(t-1))

The third equation is the calculated seasonal index, and is a weighted average of the
current data value divided by the current average and the seasonal index for the previous
season. I(t) represents the average seasonal coefficient. The weight constant is p:

I(t) = p * (datavalue(t)/SEASONAL(t)) + (1 - p) * I(t-L)

These equations are solved to derive the triple smoothed average. The first smoothed average
is set to the first data value. Initial values for the seasonality factors are calculated based on
the maximum number of full periods of data in the data source, while the initial trend is
calculated based on two periods of data. These values are calculated with the following steps:

1. The initial trend factor is calculated by the following formula:

b(0) = (1/L) ((y(L+1)-y(1))/L + (y(L+2)-y(2))/L + ... + (y(2L) -
y(L))/L )

2. The calculation of the initial seasonality factor is based on the average of the data values

within each period, A(j) (1<=j<=N):

A(j) = ( y((j-1)L+1) + y((j-1)L+2) + ... + y(jL) ) / L

Creating Reports With TIBCO® WebFOCUS Language

 349

Calculating Trends and Predicting Values With FORECAST

3. Then, the initial periodicity factor is given by the following formula, where N is the number
of full periods available in the data, L is the number of points per period and n is a point
within the period (1<= n <= L):

I(n) = ( y(n)/A(1) + y(L+n)/A(2) + ... + y((N-1)L+n)/A(N) ) / N

The three constants must be chosen carefully. The best results are usually obtained by
choosing the constants to minimize the mean-squared error (MSE) between the data values
and the calculated averages. Varying the values of npoint1 and npoint2 affect the results, and
some values may produce a better approximation. To search for a better approximation, you
may want to find values that minimize the MSE.

The equation used to forecast beyond the last data point with triple exponential smoothing is:

forecast(t+m) = (SEASONAL(t) + m * b(t)) / I(t-L+MOD(m/L))

where:

m

Is the number of periods ahead for the forecast.

Example:

Calculating a Triple Exponential Smoothing Column

In the following, the data has seasonality but no trend. Therefore, npoint2 is set high (1000) to
make the trend factor negligible in the calculation:

SET HISTOGRAM = OFF
TABLE FILE VIDEOTRK
SUM TRANSTOT
BY  TRANSDATE
ON TRANSDATE RECAP SEASONAL/D10.1 = FORECAST(TRANSTOT,1,3,'SEASONAL',
   3,3,1000,1);
WHERE TRANSDATE NE '19910617'
END

350

In the output, npredict is 3. Therefore, three periods (nine points, nperiod * npredict) are
generated.

5. Creating Temporary Fields

Using a Linear Regression Equation

The Linear Regression Equation estimates values by assuming that the dependent variable
(the new calculated values) and the independent variable (the sort field values) are related by a
function that represents a straight line:

y = mx + b

where:

y

x

m

Is the dependent variable.

Is the independent variable.

Is the slope of the line.

Creating Reports With TIBCO® WebFOCUS Language

 351

Calculating Trends and Predicting Values With FORECAST

b

Is the y-intercept.

REGRESS uses a technique called Ordinary Least Squares to calculate values for m and b that
minimize the sum of the squared differences between the data and the resulting line.

The following formulas show how m and b are calculated.

where:

n

y

x

Is the number of data points.

Is the data values (dependent variables).

Is the sort field values (independent variables).

Trend values, as well as predicted values, are calculated using the regression line equation.

Example:

Calculating a New Linear Regression Field

TABLE FILE CAR
PRINT MPG
BY DEALER_COST
WHERE MPG NE 0.0
  ON DEALER_COST RECAP FORMPG=FORECAST(MPG,1000,3,'REGRESS');
END

352

5. Creating Temporary Fields

The output is:

DEALER_COST      MPG          FORMPG
      2,886       27           25.51
      4,292       25           23.65
      4,631       21           23.20
      4,915       21           22.82
      5,063       23           22.63
      5,660       21           21.83
                  21           21.83
      5,800       24           21.65
      6,000       24           21.38
      7,427       16           19.49
      8,300       18           18.33
      8,400       18           18.20
     10,000       18           16.08
     11,000       18           14.75
     11,194        9           14.50
     14,940       11            9.53
     15,940        0            8.21
     16,940        0            6.88
     17,940        0            5.55

Note:

Three predicted values of FORMPG are calculated. For values outside the range of the data,
new DEALER_COST values are generated by adding the interval value (1,000) to the prior
DEALER_COST value.

There are no MPG values for the generated DEALER_COST values.

Each FORMPG value is computed using a regression line, calculated using all of the actual
data values for MPG.

DEALER_COST is the independent variable (x) and MPG is the dependent variable (y). The
equation is used to calculate MPGFORECAST trend and predicted values.

In this case, the equation is approximately as follows:

FORMPG = (-0.001323 * DEALER_COST) + 29.32

The predicted values are (the values are not exactly as calculated by FORECAST because of
rounding, but they show the calculation process).

DEALER_COST

Calculation

15,940

16,940

(-0.001323 * 15,940) + 29.32

(-0.001323 * 16,940) + 29.32

FORMPG

8.23

6.91

Creating Reports With TIBCO® WebFOCUS Language

 353

Calculating Trends and Predicting Values With FORECAST

DEALER_COST

Calculation

FORMPG

17,940

(-0.001323 * 17,940) + 29.32

5.59

FORECAST Reporting Techniques

You can use FORECAST multiple times in one request. However, all FORECAST requests must
specify the same sort field, interval, and number of predictions. The only things that can
change are the RECAP field, method, field used to calculate the FORECAST values, and number
of points to average. If you change any of the other parameters, the new parameters are
ignored.

If you want to move a FORECAST column in the report output, use an empty COMPUTE
command for the FORECAST field as a placeholder. The data type (I, F, P, D) must be the same
in the COMPUTE command and the RECAP command.

To make the report output easier to interpret, you can create a field that indicates whether the
FORECAST value in each row is a predicted value. To do this, define a virtual field whose value
is a constant other than zero. Rows in the report output that represent actual records in the
data source will appear with this constant. Rows that represent predicted values will display
zero. You can also propagate this field to a HOLD file.

Example:

Generating Multiple FORECAST Columns in a Request

This example calculates moving averages and exponential averages for both the DOLLARS and
BUDDOLLARS fields in the GGSALES data source. The sort field, interval, and number of
predictions are the same for all of the calculations.

DEFINE FILE GGSALES
 SDATE/YYM = DATE;
 SYEAR/Y = SDATE;
 SMONTH/M = SDATE;
 PERIOD/I2 = SMONTH;
END
TABLE FILE GGSALES
  SUM DOLLARS AS 'DOLLARS' BUDDOLLARS AS 'BUDGET'
  BY CATEGORY NOPRINT BY PERIOD AS 'PER'
  WHERE SYEAR EQ 97 AND CATEGORY EQ 'Coffee'
  ON PERIOD RECAP DOLMOVAVE/D10.1= FORECAST(DOLLARS,1,0,'MOVAVE',3);
  ON PERIOD RECAP DOLEXPAVE/D10.1= FORECAST(DOLLARS,1,0,'EXPAVE',4);
  ON PERIOD RECAP BUDMOVAVE/D10.1 = FORECAST(BUDDOLLARS,1,0,'MOVAVE',3);
  ON PERIOD RECAP BUDEXPAVE/D10.1 = FORECAST(BUDDOLLARS,1,0,'EXPAVE',4);
END

354

The output is shown in the following image.

5. Creating Temporary Fields

Example: Moving the FORECAST Column

The following example places the DOLLARS field after the MOVAVE field by using an empty
COMPUTE command as a placeholder for the MOVAVE field. Both the COMPUTE command and
the RECAP command specify formats for MOVAVE (of the same data type), but the format of
the RECAP command takes precedence.

DEFINE FILE GGSALES
 SDATE/YYM = DATE;
 SYEAR/Y = SDATE;
 SMONTH/M = SDATE;
 PERIOD/I2 = SMONTH;
END
TABLE FILE GGSALES
SUM   UNITS
COMPUTE MOVAVE/D10.2 = ;
DOLLARS
  BY CATEGORY BY PERIOD
  WHERE SYEAR EQ 97 AND CATEGORY EQ 'Coffee'
  ON PERIOD RECAP MOVAVE/D10.1= FORECAST(DOLLARS,1,3,'MOVAVE',3);
END

Creating Reports With TIBCO® WebFOCUS Language

 355

Calculating Trends and Predicting Values With FORECAST

The output is shown in the following image.

Category     PERIOD  Unit Sales        MOVAVE  Dollar Sales
Coffee            1       61666     801,123.0        801123
                  2       54870     741,731.5        682340
                  3       61608     749,513.7        765078
                  4       57050     712,897.3        691274
                  5       59229     725,598.7        720444
                  6       58466     718,058.3        742457
                  7       60771     736,718.0        747253
                  8       54633     715,202.0        655896
                  9       57829     711,155.3        730317
                 10       57012     703,541.7        724412
                 11       51110     691,664.3        620264
                 12       58981     702,334.7        762328
                 13           0     694,975.6             0
                 14           0     719,879.4             0
                 15           0     705,729.9             0

Example:

Distinguishing Data Rows From Predicted Rows

In the following example, the DATA_ROW virtual field has the value 1 for each row in the data
source. It has the value zero for the predicted rows. The PREDICT field is calculated as YES for
predicted rows, and NO for rows containing data.

DEFINE FILE CAR
DATA_ROW/I1 = 1;
END
TABLE FILE CAR
  PRINT DATA_ROW
COMPUTE PREDICT/A3 = IF DATA_ROW EQ 1 THEN 'NO' ELSE 'YES' ;
MPG
BY DEALER_COST
WHERE MPG GE 20
  ON DEALER_COST RECAP FORMPG/D12.2=FORECAST(MPG,1000,3,'REGRESS');
  ON DEALER_COST RECAP MPG         =FORECAST(MPG,1000,3,'REGRESS');
END

The output is:

DEALER_COST  DATA_ROW  PREDICT             MPG          FORMPG
      2,886         1  NO                27.00           25.65
      4,292         1  NO                25.00           23.91
      4,631         1  NO                21.00           23.49
      4,915         1  NO                21.00           23.14
      5,063         1  NO                23.00           22.95
      5,660         1  NO                21.00           22.21
                    1  NO                21.00           22.21
      5,800         1  NO                24.20           22.04
      6,000         1  NO                24.20           21.79
      7,000         0  YES               20.56           20.56
      8,000         0  YES               19.32           19.32
      9,000         0  YES               18.08           18.08

356

Calculating Trends and Predicting Values With Multivariate REGRESS

5. Creating Temporary Fields

The REGRESS method derives a linear equation that best fits a set of numeric data points, and
uses this equation to create a new column in the report output. The equation can be based on
one to three independent variables.

This method estimates values by assuming that the dependent variable (y, the new calculated
values) and the independent variables (x1, x2, x3) are related by the following linear equation:

y = a1*x1 [+ a2*x2 [+ a3*x3]] + b

When there is one independent variable, the equation represents a straight line. This produces
the same values as FORECAST using the REGRESS method. When there are two independent
variables, the equation represents a plane, and with three independent variables, it represents
a hyperplane. You should use this technique when you have reason to believe that the
dependent variable can be approximated by a linear combination of the independent variables.

REGRESS uses a technique called Ordinary Least Squares to calculate values for the
coefficients (a1, a2, a3, and b) that minimize the sum of the squared differences between the
data and the resulting line, plane, or hyperplane.

Syntax:

How to Create a Multivariate Linear Regression Column

ON {sortfield} RECAP y[/fmt] = REGRESS(n, x1, [x2, [x3,]] z);

where:

sortfield

Is a field in the data source. It cannot be the same field as any of the parameters to
REGRESS. A new linear regression equation is derived each time the sort field value
changes.

y

Is the new numeric column calculated by applying the regression equation. You cannot
DEFINE or COMPUTE a field with this name.

fmt

Is the display format for y. If it is omitted, the default format is D12.2.

n

Is a whole number from 1 to 3 indicating the number of independent variables.

Creating Reports With TIBCO® WebFOCUS Language

 357

Calculating Trends and Predicting Values With Multivariate REGRESS

x1, x2, x3

Are the field names to be used as the independent variables. All of these variables must
be numeric and be independent of each other.

z

Is an existing numeric field that is assumed to be approximately linearly dependent on the
independent variables and is used to derive the regression equation.

Reference: Usage Notes for REGRESS

The (By) sort field used with REGRESS must be in a numeric or date format.

REGRESS cannot operate on an ACROSS field.

If any of the independent variables are also sort fields, they cannot be referenced in the
request prior to the REGRESS sort field.

FORECAST and REGRESS cannot be used in the same request, and only one REGRESS is
supported in a request. Non-REGRESS RECAP commands are supported.

The RECAP command used with REGRESS can contain only the REGRESS syntax. REGRESS
does not recognize any syntax after the closing semicolon (;).

Although you pass parameters to REGRESS using an argument list in parentheses,
REGRESS is not a function. It can coexist with a user-written subroutine of the same name,
as long as the user-written subroutine is not specified in a RECAP command.

BY TOTAL is not supported.

MORE, MATCH, FOR, and OVER are not supported.

The process of generating the REGRESS values creates extra columns that are not printed
in the report output. The number and placement of these additional columns varies
depending on the specific request. Therefore, use of column notation is not supported in a
request that includes REGRESS.

SUMMARIZE and RECOMPUTE are not supported for the same sort field used for REGRESS.

REGRESS is not supported for the FOCUS GRAPH facility.

The left side of a RECAP command used for REGRESS supports the CURR attribute for
creating a currency-denominated field.

Fields with missing values cannot be used in the regression.

358

5. Creating Temporary Fields

Larger amounts of data produce more useful results.

Example:

Creating a Multivariate Linear Regression Column

The following request uses the GGSALES data source to calculate an estimated DOLLARS
column. The BUDUNITS, UNITS, and BUDDOLLARS fields are the independent variables. The
DOLLARS field provides the actual values to be estimated:

DEFINE FILE GGSALES
 YEAR/Y = DATE;
 MONTH/M = DATE;
 PERIOD/I2 = MONTH;
END

TABLE FILE GGSALES
PRINT BUDUNITS UNITS BUDDOLLARS DOLLARS
BY PERIOD
ON PERIOD
RECAP EST_DOLLARS/F8 = REGRESS(3, BUDUNITS, UNITS, BUDDOLLARS, DOLLARS);
WHERE CATEGORY EQ 'Coffee'
WHERE REGION EQ 'West'
WHERE UNITS GT 1600 AND UNITS LT 1700
END

Creating Reports With TIBCO® WebFOCUS Language

 359

Using Text Fields in DEFINE and COMPUTE

The output is:

Using Text Fields in DEFINE and COMPUTE

Text fields can be assigned to alphanumeric fields and receive assignment from alphanumeric
fields. If an alphanumeric field is assigned the value of a text field that is too long for the
alphanumeric field, the value is truncated before being assigned to the alphanumeric field.

Note: COMPUTE commands in Maintain do not support text fields.

360

5. Creating Temporary Fields

Example:

Assigning the Result of an Alphanumeric Expression to a Text Field

This example uses the COURSES data source, which contains a text field, to create an
alphanumeric field named ADESC, which truncates the text field at 36 characters, and a new
text field named NEWDESC, which is a text version of ADESC:

DEFINE FILE COURSES
ADESC/A36   = DESCRIPTION;
NEWDESC/TX36 = ADESC;
END

TABLE FILE COURSES
PRINT ADESC NEWDESC
END

The output is:

ADESC                                 NEWDESC
-----                                 -------
This course provides the DP professi  This course provides the DP professi
Anyone responsible for designing FOC  Anyone responsible for designing FOC
This is a course in FOCUS efficienci  This is a course in FOCUS efficienci

Creating Temporary Fields Independent of a Master File

The temporary fields you create with the DEFINE and COMPUTE commands are tied to a
specific Master File, and in the case of values calculated with the COMPUTE command, to a
specific request. However, you can create temporary fields that are independent of either a
Master File or a request using the DEFINE FUNCTION command.

A DEFINE function is a named group of calculations that use any number of input values and
produce a return value. When calling a DEFINE function, you must first define the function.

A DEFINE function can be called in most of the same situations that are valid for Information
Builders-supplied functions. Data types are defined with each argument. When substituting
values for these arguments, the format must match the defined format. Alphanumeric
arguments shorter than the specified format are padded with blanks, while longer
alphanumeric arguments are truncated.

All calculations within the function are done in double precision. Format conversions occur only
across equal signs (=) in the assignments that define temporary fields.

Creating Reports With TIBCO® WebFOCUS Language

 361


Creating Temporary Fields Independent of a Master File

Syntax:

How to Define a Function

DEFINE FUNCTION name (argument1/format1,..., argumentn/formatn)
[tempvariablea/formata [TITLE 'line1[,line2 ...']
 [DESCRiption 'description'] = expressiona;]
   .
   .
   .
[tempvariablex/formatx = expressionx;]
name/format = [result_expression];
END

where:

name

Is the name of the function, up to 64 characters. This must be the last field calculated in
the function, and is used to return the value of the function to the calling procedure.

argument1...argumentn

Are the argument names. They can be any names that comply with WebFOCUS field
naming rules.

format1...formatn

Are the formats of the function arguments.

If the format of an argument is alphanumeric, the argument value must also be
alphanumeric. Shorter arguments are padded on the right with blanks, and longer
arguments are truncated.

If the format of an argument is numeric, the argument value must also be numeric. To
prevent unexpected results, you must be consistent in your use of data types.

tempvariablea...tempvariablex

Are temporary fields. Temporary fields hold intermediate values used in the function. You
can define as many temporary fields as you need.

tempformata...tempformatx

Are the formats of the temporary fields.

line1,line2 ...

Are the lines of default column title to be displayed for the virtual field unless overridden
by an AS phrase.

362

5. Creating Temporary Fields

description

Is the description to be associated with the virtual field, enclosed in single quotation
marks. The description displays in the tools that browse Master Files.

expressiona...expressionx

Are the expressions that calculate the temporary field values. The expressions can use
parameters, constants, and other temporary fields defined in the same function.

format

Is the format of the value the function returns.

result_expression

Is the expression that calculates the value returned by the function. The expression can
use parameters, constants, and temporary fields defined in the same function.

All names defined in the body of the function are local to the function. The last field defined
before the END command in the function definition must have the same name as the function,
and represents the return value for the function.

Reference: DEFINE Function Limits and Restrictions

The number of functions you can define and use in a session is virtually unlimited.

A DEFINE function is cleared with the DEFINE FUNCTION CLEAR command. It is not cleared
by issuing a join, or by any WebFOCUS command.

When an expression tries to use a cleared function, an error appears.

DEFINE functions can call other DEFINE functions, but cannot call themselves.

If you overwrite or clear a DEFINE function, a subsequent attempt to use a temporary field
that refers to the function generates the following warning:

(FOC03665) Error loading external function '%1'

Example:

Defining a Function

The following example creates and calls the SUBTRACT function. SUBTRACT performs a
calculation with the arguments VAL1 and VAL2.

DEFINE FUNCTION SUBTRACT (VAL1/D8, VAL2/D8)
 SUBTRACT/D8.2 = VAL1 - VAL2;
END

Creating Reports With TIBCO® WebFOCUS Language

 363

Creating Temporary Fields Independent of a Master File

TABLE FILE MOVIES
 PRINT TITLE LISTPR IN 35 WHOLESALEPR AND
 COMPUTE PROFIT/D8.2 = SUBTRACT(LISTPR,WHOLESALEPR);
 BY CATEGORY
   WHERE CATEGORY EQ 'MYSTERY' OR 'ACTION'
END

The output is:

CATEGORY

TITLE

LISTP
R

WHOLESALE
PR

PROFIT

ACTION

JAWS

ROBOCOP

19.95

10.99

19.98

11.50

TOTAL RECALL

19.99

11.99

TOP GUN

RAMBO III

MYSTERY

REAR WINDOW

VERTIGO

FATAL
ATTRACTION

NORTH BY
NORTHWEST

14.95

9.99

19.95

10.99

19.98

9.00

19.98

9.00

29.98

15.99

19.98

9.00

DEAD RINGERS

25.99

15.99

MORNING
AFTER, THE

19.95

9.99

  8.96

  8.48

  8.00

  4.96

  8.96

 10.98

 10.98

 13.99

 10.98

 10.00

  9.96

364























5. Creating Temporary Fields

PSYCHO

BIRDS, THE

SEA OF LOVE

19.98

9.00

19.98

9.00

59.99

30.00

 10.98

 10.98

 29.99

Procedure: How to Display DEFINE Functions

Issue the following command from the Command Console:

? FUNCTION

Example:

Displaying DEFINE Functions

Issuing the command

? FUNCTION

displays information similar to the following:

FUNCTIONS

CURRENTLY

ACTIVE

NAME

FORMAT

PARAMETER

FORMAT

----------

---------

---------

-------

SUBTRACT

D8.2

VAL1

VAL2

D8

D8

If you issue the ? FUNCTION command when no functions are defined, the following appears:

NO FUNCTIONS CURRENTLY IN EFFECT

Creating Reports With TIBCO® WebFOCUS Language

 365







Creating Temporary Fields Independent of a Master File

Syntax:

How to Clear DEFINE Functions

DEFINE FUNCTION {name|*} CLEAR

where:

name

Is the name of the function name to clear.

*

Clears all active DEFINE functions.

366

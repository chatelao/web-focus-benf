Chapter28

Improving Report Processing

The following high-performance methods optimize data retrieval and report processing:

Temporary rotation of network and hierarchical data sources to create an alternate
view of the data.

Automatic alternate file views with the AUTOPATH feature.

Automatic indexed retrieval (AUTOINDEX).

Retrieval of pre-sorted data using the TABLEF command.

Preserving the internal matrix of a report using the SAVEMATRIX parameter.

Compiling expressions into machine code to provide faster processing.

Note: These techniques may not be available for all data sources. See your data adapter
documentation to determine if a technique is valid for your data source.

In this chapter:

Rotating a Data Structure for Enhanced Retrieval

Optimizing Retrieval Speed for FOCUS Data Sources

Automatic Indexed Retrieval

Data Retrieval Using TABLEF

Compiling Expressions

Rotating a Data Structure for Enhanced Retrieval

If you are using certain network or hierarchical data sources such as IMS, CA-IDMS/DB, or
FOCUS, you can rotate the data source, creating an alternate view which changes some of the
segment relationships and enables you to access the segments in a different order. By
reporting from an alternate view, you can do the following:

Change the access path. For example, you can access data in a lower segment more
quickly by promoting that segment to a higher level.

Creating Reports With TIBCO® WebFOCUS Language

 1929

Rotating a Data Structure for Enhanced Retrieval

Change the path structure of a data source. This option is especially helpful if you wish to
create a report using several sort fields that are on different paths in the file. By changing
the view of the file hierarchy, all the desired sort fields can be on the same path.

It should be noted that retrieval is controlled by the minimum referenced subtree. For more
information, see Understanding the Efficiency of the Minimum Referenced Subtree in the
Describing a Group of Fields chapter in the Describing Data With WebFOCUS Language manual.

For example, consider the regular and alternate views below:

Since C is the root segment in the alternate view, particular instances of C can be selected
faster.

Syntax:

How to Request an Alternate View

To request an alternate view, add the name of a field found in the alternate root segment to
the file name in the TABLE command, separated by a period (.):

TABLE FILE filename.fieldname

1930

Reference: Usage Notes for Restructuring Data

28. Improving Report Processing

If you use a non-indexed field, each segment instance is retrieved until the specified record
is found. Therefore, this process is less efficient than using an indexed field.

When you use the alternate view feature on a particular child segment, the data retrieved
from that segment is retrieved in physical order, not logical order. This is because the child
becomes a root segment for the report request, and there are no logical pointers between
the child segments of different parents.

Alternate view on an indexed field is a special case that uses the index for retrieval. When
you perform an alternate view on an indexed field, you enhance the speed of retrieval.
However, you must include an equality test on the indexed field, for example WHERE
(MONTH EQ 1) OR (MONTH EQ 2), in order to benefit from the performance improvement.

A field name specified in an alternate file view may not be qualified or exceed 12
characters.

Automatic Indexed Retrieval (AUTOINDEX) is never invoked in a TABLE request against an
alternate file view.

Example:

Restructuring Data

Consider the following data structure, in which PROD_CODE is an indexed field:

Creating Reports With TIBCO® WebFOCUS Language

 1931

Optimizing Retrieval Speed for FOCUS Data Sources

You could issue the following request to promote the segment containing PROD_CODE to the
top of the hierarchy, thereby enabling quicker access to the data in that segment.

TABLE FILE SALES.PROD_CODE
"SALES OF B10 DISTRIBUTED BY AREA"
SUM UNIT_SOLD AND RETAIL_PRICE
BY AREA
WHERE PROD_CODE EQ 'B10'
ON TABLE COLUMN-TOTAL
END

Optimizing Retrieval Speed for FOCUS Data Sources

When the AUTOPATH parameter in set ON, an optimized retrieval path—that is, one in which
the lowest retrieved segment is the entry point—is selected dynamically. It is equivalent to the
alternate view syntax

TABLE FILE filename.fieldname

where:

 fieldname

Is not indexed. Retrieval starts at the segment in which fieldname resides.

The system determines whether optimized retrieval is appropriate by analyzing the fields
referenced in a request and the data source structure. For more information on the AUTOPATH
parameter, see the Developing Reporting Applications manual.

Automatic Indexed Retrieval

Automatic indexed retrieval (AUTOINDEX) optimizes the speed of data retrieval in FOCUS data
sources. To take advantage of automatic indexed retrieval, a TABLE request must contain an
equality or range test on an indexed field in the highest segment referenced in the request.

This method is not supported if a:

Range test applies to a packed data value.

Request specifies an alternate view (that is, TABLE FILE filename.fieldname).

Request contains the code BY HIGHEST or BY LOWEST.

For related information on AUTOINDEX, see the Developing Reporting Applications manual.

1932

28. Improving Report Processing

Syntax:

How to Use Indexed Retrieval

SET AUTOINDEX = {ON|OFF}

where:

ON

Uses indexed data retrieval for optimized speed when possible. The request must contain
an equality or range test on an indexed field in the highest segment referenced in the
request. ON is the default value.

OFF

Uses sequential data retrieval unless a request specifies an indexed view (TABLE FILE
filename.indexed_fieldname) and contains an equality test on indexed_fieldname. In that
case, indexed data retrieval is automatically performed.

Reference: Usage Notes for Indexed Retrieval

AUTOINDEX is never invoked when the TABLE request contains an alternate file view (that
is, TABLE FILE filename.fieldname).

Even if AUTOINDEX is ON, indexed retrieval is not performed when the TABLE request
contains BY HIGHEST or BY LOWEST phrases.

When a request specifies an indexed view (as in TABLE FILE filename.indexed_fieldname),
indexed retrieval is implemented under the following circumstances:

AUTOINDEX is OFF and the request contains an equality test on the indexed field.

AUTOINDEX is ON and the request contains either an equality or a range (FROM ... TO)
test against the indexed field.

Creating Reports With TIBCO® WebFOCUS Language

 1933

Automatic Indexed Retrieval

Example:

Using Indexed Retrieval

The following Master File is referenced in the examples that follow:

FILENAME=SALES,SUFFIX=FOC,
  SEGNAME=STOR_SEG,SEGTYPE=S1,
    FIELDNAME=AREA,ALIAS=LOC,FORMAT=A1,$
  SEGNAME=DATE_SEG,PARENT=STOR_SEG,SEGTYPE=SH1,
    FIELDNAME=DATE,ALIAS=DTE,FORMAT=A4MD, $
  SEGNAME=DEPT,PARENT=DATE_SEG,SEGTYPE=S1,
    FIELDNAME=DEPARTMENT,ALIAS=DEPT,FORMAT=A5,FIELDTYPE=I,$
    FIELDNAME=DEPT_CODE,ALIAS=DCODE,FORMAT=A3,FIELDTYPE=I,$
    FIELDNAME=PROD_TYPE,ALIAS=PTYPE,FORMAT=A10,FIELDTYPE=I,$
  SEGNAME=INVENTORY,PARENT=DEPT,SEGTYPE=S1,$
    FIELDNAME=PROD_CODE,ALIAS=PCODE,FORMAT=A3,FIELDTYPE=I,$
    FIELDNAME=UNIT_SOLD,ALIAS=SOLD,FORMAT=I5,$
    FIELDNAME=RETAIL_PRICE,ALIAS=RP,FORMAT=D5.2M,$
    FIELDNAME=DELIVER_AMT,ALIAS=SHIP,FORMAT=I5,$

The following procedure contains an equality test on DEPT_CODE and PROD_CODE.
DEPT_CODE is used for indexed retrieval since it is in the higher of the referenced segments.

SET AUTOINDEX=ON
TABLE FILE SALES
SUM UNIT_SOLD RETAIL_PRICE
IF DEPT_CODE EQ 'H01'
IF PROD_CODE EQ 'B10'
END

If your TABLE request contains an equality or range test against more than one indexed field in
the same segment, AUTOINDEX uses the first index referenced in that segment for retrieval.
The following stored procedure contains an equality test against two indexed fields. Since
DEPT_CODE appears before PROD_TYPE in the Master File, AUTOINDEX uses DEPT_CODE for
retrieval.

SET AUTOINDEX=ON
TABLE FILE SALES
SUM UNIT_SOLD AND RETAIL_PRICE
IF PROD_TYPE EQ 'STEREO'
IF DEPT_CODE EQ 'H01'
END

1934

28. Improving Report Processing

Indexed retrieval is not invoked if the equality or range test is run against an indexed field that
does not reside in the highest referenced segment. In the following example, indexed retrieval
is not performed, because the request contains a reference to AREA, a field in the STOR_SEG
segment:

SET AUTOINDEX=ON
TABLE FILE SALES
SUM UNIT_SOLD AND RETAIL_PRICE
BY AREA
IF PROD_CODE EQ 'B10'
IF PROD_TYPE EQ 'STEREO'
END

Data Retrieval Using TABLEF

TABLEF is a variation of the TABLE command that provides a fast method of retrieving data
that is already stored in the order required for printing and requires no additional sorting.

Using TABLEF, records are retrieved in the logical sequence from the data source. The
standard report request syntax applies, subject to the following rules:

Any BY phrases must be compatible with the logical sequence of the data source. BY
phrases are used only to establish control breaks, not to change the order of the records.

ACROSS phrases are not permitted.

Multiple display commands are not permitted. Only one display command may be used.

After the report is executed, RETYPE, HOLD, and SAVE are not available. However, you can
produce an extract file if you include ON TABLE HOLD or ON TABLE SAVE as part of the
request.

NOSPLIT is not compatible with the TABLEF command, and produces a FOC037 error
message.

TABLEF can be used with HOLD files and other non-FOCUS data sources when the natural
sort sequence of both the request and the data are the same.

The DST. prefix operator is not permitted.

BORDER styling is not supported with TABLEF.

TABLEF is not supported with SQUEEZE.

Creating Reports With TIBCO® WebFOCUS Language

 1935

Compiling Expressions

Example:

Printing Using Fast Table Retrieval

If you previously created a HOLD file from the EMPLOYEE data source, sorted by the
CURR_SAL, LAST_NAME, and FIRST_NAME fields, you can issue the following TABLEF request:

TABLEF FILE HOLD
PRINT CURR_SAL AND LAST_NAME AND FIRST_NAME
END

Compiling Expressions

Compiling expressions into machine code provides faster processing.

Compiling Expressions Using the DEFINES Parameter

The SET DEFINES, SET COMPUTE, and SET MODCOMPUTE commands have been deprecated.
Expressions are compiled unless environmental conditions prevent compilation.

Among the benefits of the compiling expressions are:

Compilation of only those expressions that are actually used in the TABLE request.

Much faster execution of expressions containing complex calculations on long packed
fields.

Compilation of date expressions.

Reference: Usage Notes for Compiled Expressions

Any expression that cannot be compiled runs without compilation. This does not affect
compilation of other expressions. The following elements in an expression disable
compilation:

Functions. However, expressions that use the following functions can be compiled:
YMD, DMY, INT, and DECODE.

CONTAINS, OMITS, LAST.

If compilation is not possible because of environmental conditions, the processing is handled
without compilation. No message is generated indicating that compilation did not take place.
To determine whether it did take place, issue the ? COMPILE command.

1936

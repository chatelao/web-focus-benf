Chapter10

Providing Data Source Security: DBA

As Database Administrator, you can use DBA security features to provide security for any
FOCUS data source. You can use these security features to limit the number of records
or reads a user can request in a report.

You can also use DBA security features to provide security for non-FOCUS data sources.
Note that DBA security cannot protect a data source from non-WebFOCUS access.

Note: All references to FOCUS data sources also apply to XFOCUS data sources.

In this chapter:

Introduction to Data Source Security

Implementing Data Source Security

Specifying an Access Type: The ACCESS Attribute

Limiting Data Source Access: The RESTRICT Attribute

Controlling the Source of Access Restrictions in a Multi-file Structure

Adding DBA Restrictions to the Join Condition

Placing Security Information in a Central Master File

Summary of Security Attributes

Hiding Restriction Rules: The ENCRYPT Command

FOCEXEC Security

Introduction to Data Source Security

The DBA facility provides a number of security options:

You can limit the user who have access to a given data source using the USER attribute
discussed in Identifying Users With Access Rights: The USER Attribute on page 409.

You can restrict a user access rights to read, write, or update only using the ACCESS
attribute discussed in Specifying an Access Type: The ACCESS Attribute on page 414.

You can restrict a user access to certain fields or segments using the RESTRICT attribute
discussed in Limiting Data Source Access: The RESTRICT Attribute on page 417.

Describing Data With TIBCO WebFOCUS® Language

 405

Implementing Data Source Security

You can ensure that only records that pass a validation test are retrieved using the
RESTRICT attribute discussed in Limiting Data Source Access: The RESTRICT Attribute on
page 417.

You can limit the values a user can read or write to the data source or you can limit which
values a user can alter using the RESTRICT attribute discussed in Limiting Data Source
Access: The RESTRICT Attribute on page 417.

You can control the source of access restrictions in a multi-file structure using the SET
DBASOURCE command discussed in Controlling the Source of Access Restrictions in a Multi-
file Structure on page 424.

You can point to passwords and restrictions stored in another Master File with the DBAFILE
attribute discussed in Placing Security Information in a Central Master File on page 428.

You can use the WebFOCUS DBA exit routine to allow an external security system to set the
WebFOCUS password. For more information, see the WebFOCUS Security and Administration
manual.

You can place security on FOCEXECs, as discussed in FOCEXEC Security on page 438.

Implementing Data Source Security

You provide WebFOCUS security on a file-by-file basis. Implementing DBA security features is a
straightforward process in which you specify:

The names or passwords of WebFOCUS users granted access to a data source.

The type of access the user is granted.

The segments, fields, or ranges of data values to which the user access is restricted.

The declarations (called security declarations) follow the END command in a Master File and
tell WebFOCUS that security is needed for the data source and what type of security is needed.
Each security declaration consists of one or several of the following attributes:

The DBA attribute gives the name or password of the Database Administrator for the data
source. The Database Administrator has unlimited access to the data source and its
Master File.

The USER attribute identifies a user as a legitimate user of the data source. Only users
whose name or password is specified in the Master File of a FOCUS data source with
security placed on it have access to that data source.

406

10. Providing Data Source Security: DBA

The ACCESS attribute defines the type of access a given user has. The four types of access
available are:

RW, which allows a user to both read and write to a data source.

R, which allows a user only to read data in a data source.

W, which allows a user to only write new segment instances to a data source.

U, which allows a user only to update records in a data source.

The RESTRICT attribute specifies certain segments or fields to which the user is not
granted access. It can also be used to restrict the data values a user can see or perform
transactions on.

The NAME and VALUE attributes are part of the RESTRICT declaration.

Describe your data source security by specifying values for these attributes in a comma-
delimited format, just as you specify any other attribute in the Master File.

The word END on a line by itself in the Master File terminates the segment and field attributes
and indicates that the access limits follow. If you place the word END in a Master File, it must
be followed by at least a DBA attribute.

Example:

Implementing Data Source Security in a Master File

The following is a Master File that uses security features:

FILENAME = PERS, SUFFIX = FOC,$
SEGMENT = IDSEG, SEGTYPE = S1,$
 FIELD = SSN          ,ALIAS = SSN    ,FORMAT = A9   ,$
 FIELD = FULLNAME     ,ALIAS = FNAME  ,FORMAT = A40  ,$
 FIELD = DIVISION     ,ALIAS = DIV    ,FORMAT = A8   ,$
SEGMENT=COMPSEG, PARENT=IDSEG, SEGTYPE=S1,$
 FIELD = SALARY       ,ALIAS = SAL    ,FORMAT = D8   ,$
 FIELD = DATE         ,ALIAS = DATE   ,FORMAT = YMD  ,$
 FIELD = INCREASE     ,ALIAS = INC    ,FORMAT = D6   ,$
END
DBA=JONES76,$
USER=TOM    ,ACCESS=RW, $
USER=BILL   ,ACCESS=R  ,RESTRICT=SEGMENT  ,NAME=COMPSEG    ,$
USER=JOHN   ,ACCESS=R  ,RESTRICT=FIELD    ,NAME=SALARY     ,$
                                           NAME=INCREASE   ,$
USER=LARRY  ,ACCESS=U  ,RESTRICT=FIELD    ,NAME=SALARY     ,$
USER=TONY   ,ACCESS=R  ,RESTRICT=VALUE    ,NAME=IDSEG,
   VALUE=DIVISION EQ 'WEST' ,$
USER=MARY   ,ACCESS=W  ,RESTRICT=VALUE    ,NAME=SALTEST,
   VALUE=INCREASE+SALARY GE SALARY,$
                                           NAME=HISTTEST,
   VALUE=DIV NE ' ' AND DATE GT 0,$

Describing Data With TIBCO WebFOCUS® Language

 407

Implementing Data Source Security

Reference: Special Considerations for Data Source Security

When using the JOIN command, it is possible to bypass the DBA information in a data
source. This is a security exposure created because in a JOIN structure the DBA
information is read from the host Master File. This problem is solved by using the DBAFILE
feature discussed in Placing Security Information in a Central Master File on page 428. All
data sources in the joined structure will get security information as coded in the DBAFILE.

The DBA section of a Master File cannot have comments within it.

Identifying the DBA: The DBA Attribute

The first security attribute should be a password that identifies the Database Administrator.
This password can be up to 64 characters long and is not case-sensitive. It can include special
characters. If the DBA password contains blanks, it must be enclosed in single quotation
marks. Since nothing else is needed, this line is terminated by the usual delimiter (,$).

Note:

Every data source having access limits must have a DBA.

Groups of cross-referenced data sources must have the same DBA value.

Partitioned data sources, which are read together in the USE command, must have the
same DBA value.

The Database Administrator has unlimited access to the data source and all cross-
referenced data sources. Therefore, no field, segment, or value restrictions can be
specified with the DBA attribute.

You cannot encrypt and decrypt Master Files or restrict existing data sources without the
DBA password.

You should thoroughly test every security attribute before the data source is used. It is
particularly important to test the VALUE limits to make sure they do not contain errors.
Value tests are executed as if they were extra screening conditions or VALIDATE
statements typed after each request statement. Since users are unaware of the value
limits, errors caused by the value limits may confuse them.

Example:

Identifying the DBA Using the DBA Attribute

DBA=JONES76,$

408

10. Providing Data Source Security: DBA

Procedure: How to Change a DBA Password

The DBA has the freedom to change any of the security attributes. If you change the DBA
password in the Master File for an existing FOCUS data source, you must use the RESTRICT
command to store the changed DBA password in each FOCUS data source affected by the
change. Unless this is done, WebFOCUS assumes that the new description is an attempt to
bypass the restriction rules. You use the following procedure for each data source affected:

1. Edit the Master File, changing the DBA value from old to new.

2.

Issue the command:

SET PASS=old_DBA_password

3.

Issue the command:

RESTRICT
mastername
END

4.

Issue the command:

SET PASS=new_DBA_password

Including the DBA Attribute in a HOLD File

With the SET HOLDSTAT command, you can identify a data source containing DBA information
and comments to be automatically included in HOLD and PCHOLD Master Files. For more
information about the SET HOLDSTAT command, see the Developing Reporting Applications
manual.

Identifying Users With Access Rights: The USER Attribute

The USER attribute is a password that identifies the users who have legitimate access to the
data source. A USER attribute cannot be specified alone. It must be followed by at least one
ACCESS restriction (discussed in Specifying an Access Type: The ACCESS Attribute on page
414) to specify what sort of ACCESS the user is granted.

Before using a secured data source, a user must enter the password using the SET PASS or
SET USER command. If that password is not included in the Master File, the user is denied
access to the data source. When the user does not have a password, or has one that is
inadequate for the type of access requested, the following message appears:

(FOC047) THE USER DOES NOT HAVE SUFFICIENT ACCESS RIGHTS TO THE FILE:
filename

Describing Data With TIBCO WebFOCUS® Language

 409

Implementing Data Source Security

Syntax:

How to Set the USER Attribute

Any user whose name or password is not declared in the Master File is denied access to that
data source. The syntax of the USER attribute is

USER = name

where:

name

Is a password of up to 64 characters for the user. The password can include special
characters and is not case-sensitive. If the password contains blanks, it must be enclosed
in single quotation marks.

You can specify a blank password (default value if not previously changed). Such a password
does not require the user to issue a SET PASS= command. A blank password may still have
access limits and is convenient when a number of users have the same access rights.

Example:

Setting the USER Attribute

USER=TOM,...

An example of setting a user password to blank, and access to read only follows:

USER= , ACCESS=R,$

Non-Overridable User Passwords (SET PERMPASS)

The PERMPASS parameter establishes a user password that remains in effect throughout a
session or connection. You can issue this setting in any supported profile but is most useful
when established for an individual user by setting it in a user profile. It cannot be set in an ON
TABLE phrase. It is recommended that it not be set in EDASPROF because it would then apply
to all users.

All security rules established in the DBA sections of existing Master Files are respected when
PERMPASS is in effect. The user cannot issue the SET PASS or SET USER command to change
to a user password with different security rules. Any attempt to do so generates the following
message:

(FOC32409) A permanent PASS is in effect. Your PASS will not be honored.
VALUE WAS NOT CHANGED

Note: Only one permanent password can be established in a session. Once it is set, it cannot
be changed within the session.

410

10. Providing Data Source Security: DBA

Syntax:

How to Set a Non-Overridable User Password

SET PERMPASS=userpass

where:

userpass

Is the user password used for all access to data sources with DBA security rules
established in their associated Master Files.

Example:

Setting a Non-Overridable User Password

Consider the MOVIES Master File with the following DBA rules in effect:

DBA=USER1,$
USER = USERR,  ACCESS = R ,$
USER = USERU,  ACCESS = U ,$
USER = USERW,  ACCESS = W ,$
USER = USERRW, ACCESS = RW,$

The following FOCEXEC sets a permanent password:

SET PERMPASS = USERU
TABLE FILE MOVIES
PRINT TITLE BY DIRECTOR
END

The user has ACCESS=U and, therefore, is not allowed to issue a table request against the
file:

(FOC047) THE USER DOES NOT HAVE SUFFICIENT ACCESS RIGHTS TO THE FILE:
CAR
BYPASSING TO END OF COMMAND

The permanent password cannot be changed:

SET PERMPASS = USERRW

(FOC32409) A permanent PASS is in effect. Your PASS will not be honored.
VALUE WAS NOT CHANGED

The user password cannot be changed:

SET PASS = USERRW

(FOC32409) A permanent PASS is in effect. Your PASS will not be honored.
VALUE WAS NOT CHANGED

Describing Data With TIBCO WebFOCUS® Language

 411

Implementing Data Source Security

Controlling Case Sensitivity of Passwords

When a DBA or user issues the SET USER, SET PERMPASS or SET PASS command, this user
ID is validated before they are given access to any data source whose Master File has DBA
attributes. The password is also checked when encrypting or decrypting a FOCEXEC.

The SET DBACSENSITIV command determines whether the password is converted to
uppercase prior to validation.

Syntax:

How to Control Password Case Sensitivity

SET DBACSENSITIV = {ON|OFF}

where:

ON

Does not convert passwords to uppercase. All comparisons between the password set by
the user and the password in the Master File or FOCEXEC are case-sensitive.

OFF

Converts passwords to uppercase prior to validation. All comparisons between the
password set by the user and the password in the Master File or FOCEXEC are not case-
sensitive. OFF is the default value.

Example:

Controlling Password Case Sensitivity

Consider the following DBA declaration added to the EMPLOYEE Master File:

USER = User2, ACCESS = RW,$

User2 wants to report from the EMPLOYEE data source and issues the following command:

SET USER = USER2

With DBACSENSITIV OFF, User2 can run the request even though the case of the password
entered does not match the case of the password in the Master File.

With DBACSENSITIV ON, User2 gets the following message:

(FOC047) THE USER DOES NOT HAVE SUFFICIENT ACCESS RIGHTS TO THE FILE:

With DBACSENSITIV ON, the user must issue the following command:

SET USER = User2

412

10. Providing Data Source Security: DBA

Establishing User Identity

A user must enter his or her password before using any FOCUS data source that has security
specified for it. A single user may have different passwords in different files. For example, in
file ONE, the rights of password BILL apply, but in file TWO, the rights of password LARRY
apply. Use the SET PASS command to establish the passwords.

Syntax:

How to Establish User Identity

SET {PASS|USER} = name [[IN {file|* [NOCLEAR]}], name [IN file] ...]

where:

name

Is the user name or password. If a character used in the password has a special meaning
in your operating environment (for example, as an escape character), you can issue the
SET USER command in a FOCEXEC and execute the FOCEXEC to set the password. If the
password contains a blank, you do not have to enclose it in single quotation marks when
issuing the SET USER command.

file

Is the name of the Master File to which the password applies.

*

Indicates that name replaces all passwords active in all files.

NOCLEAR

Provides a way to replace all passwords in the list of active passwords while retaining the
list.

Example:

Establishing User Identity

In the following example, the password TOM is in effect for all data sources that do not have a
specific password designated for them:

SET PASS=TOM

For the next example, in file ONE the password is BILL, and in file TWO the password is LARRY.
No other files have passwords set for them:

SET PASS=BILL IN ONE, LARRY IN TWO

Here, all files have password SALLY except files SIX and SEVEN, which have password DAVE.

SET PASS=SALLY, DAVE IN SIX
SET PASS=DAVE IN SEVEN

Describing Data With TIBCO WebFOCUS® Language

 413

Specifying an Access Type: The ACCESS Attribute

The password is MARY in file FIVE and FRANK in all other files:

SET PASS=MARY IN FIVE,FRANK

A list of the files for which a user has set specific passwords is maintained. To see the list of
files, issue:

? PASS

When the user sets a password IN * (all files), the list of active passwords collapses to one
entry with no associated file name. To retain the file name list, use the NOCLEAR option.

In the next example, the password KEN replaces all passwords active in all files, and the table
of active passwords is folded to one entry:

SET PASS=KEN IN *

In the following, MARY replaces all passwords in the existing table of active passwords (which
consists of files NINE and TEN) but FRANK is the password for all other files. The option
NOCLEAR provides a shorthand way to replace all passwords in a specific list:

SET PASS=BILL IN NINE,TOM IN TEN
SET PASS=MARY IN * NOCLEAR,FRANK

Note: The FIND function does not work with COMBINEd data sources secured with different
passwords.

Users must issue passwords using the SET PASS command during each session in which they
use a secured data source. They may issue passwords at any time before using the data
source and can issue a different password afterward to access another data source.

Specifying an Access Type: The ACCESS Attribute

The ACCESS attribute specifies what sort of access a user is granted. Every security
declaration, except the DBA declaration, must have a USER attribute and an ACCESS attribute.

The following is a complete security declaration, consisting of a USER attribute and an ACCESS
attribute.

USER=TOM, ACCESS=RW,$

This declaration gives Tom read and write (for adding new segment instances) access to the
data source.

414

10. Providing Data Source Security: DBA

You can assign the ACCESS attribute one of four values. These are:

ACCESS=R

ACCESS=W

Read-only

Write only

ACCESS=RW

Read the data source and write new segment instances

ACCESS=U

Update only

Access levels affect what kind of commands a user can issue. Before you decide what access
levels to assign to a user, consider what commands that user will need. If a user does not
have sufficient access rights to use a given command, the following message appears:

(FOC047) THE USER DOES NOT HAVE SUFFICIENT ACCESS RIGHTS TO THE FILE:
filename

ACCESS levels determine what a user can do to the data source. Use the RESTRICT attribute
(discussed in Limiting Data Source Access: The RESTRICT Attribute on page 417) to limit the
fields, values, or segments to which a user has access. Every USER attribute must be
assigned an ACCESS attribute. The RESTRICT attribute is optional. Without it, the user has
unlimited access to fields and segments within the data source.

Types of Access

The type of access granting use of various WebFOCUS commands is shown in the following
table. When more than one type of access is shown, any type of access marked will allow the
user at least some use of that command. Often, however, the user will be able to use the
command in different ways, depending on the type of access granted.

Command

CHECK

CREATE

DECRYPT

DEFINE

ENCRYPT

R

X

X

U

X

W

X

RW

X

X

X

DBA

X

X

X

X

X

Describing Data With TIBCO WebFOCUS® Language

 415














Specifying an Access Type: The ACCESS Attribute

Command

MATCH

REBUILD

RESTRICT

TABLE

R

X

X

W

RW

U

DBA

X

X

X

X

X

X

X

CHECK Command. Users without the DBA password or read/write access are allowed limited
access to the CHECK command. However, when the HOLD option is specified, the warning
ACCESS LIMITED BY PASSWORD is produced, and restricted fields are propagated to the HOLD
file depending on the DBA RESTRICT attribute. See Limiting Data Source Access: The RESTRICT
Attribute on page 417 for more information on the RESTRICT attribute.

CREATE Command. Only users with the DBA password or read/write (RW) access rights can
issue a CREATE command.

DECRYPT Command. Only users with the DBA password can issue a DECRYPT command.

DEFINE Command. As with all reporting commands, a user need only have an access of R
(read only) to use the DEFINE command. An access of R permits the user to read records from
the data source and prepare reports from them. The only users who cannot use the DEFINE
command are those whose access is W (write only) or U (update only).

ENCRYPT Command. Only users with the DBA password can use the ENCRYPT command.

REBUILD Command. Only users with the DBA password or read/write (RW) access rights can
issue the REBUILD command. This command is only for FOCUS data sources.

RESTRICT Command. Only users with the DBA password may use the RESTRICT command.

TABLE or MATCH Command. A user who has access of R or RW may use the TABLE
command. Users with access of W or U may not.

416












Reference: RESTRICT Attribute Keywords

10. Providing Data Source Security: DBA

The RESTRICT attribute keywords affect the resulting HOLD file created by the CHECK
command as follows:

FIELD

Fields named with the NAME parameter are not included in the HOLD file.

SEGMENT

The segments named with the NAME parameter are included, but fields in those segments
are not.

SAME

The behavior is the same as for the user named in the NAME parameter.

NOPRINT

Fields named in the NAME or SEGNAME parameter are included since the user can
reference these.

VALUE

Fields named in the VALUE parameter are included since the user can reference these.

If you issue the CHECK command with the PICTURE option, the RESTRICT attribute keywords
affect the resulting picture as follows:

FIELD

Fields named with the NAME parameter are not included in the picture.

SEGMENT

The boxes appear for segments named with the NAME parameter, but fields in those
segments do not.

SAME

The behavior is the same as for the user named in the NAME parameter.

NOPRINT

This option has no effect on the picture.

VALUE

This option has no effect on the picture.

Limiting Data Source Access: The RESTRICT Attribute

The ACCESS attribute determines what a user can do with a data source.

Describing Data With TIBCO WebFOCUS® Language

 417

Limiting Data Source Access: The RESTRICT Attribute

The optional RESTRICT attribute further restricts a user access to certain fields, values, or
segments.

The RESTRICT=VALUE attribute supports those criteria that are supported by the IF phrase. The
RESTRICT=VALUE_WHERE attribute supports all criteria supported in a WHERE phrase,
including comparison between fields and use of functions. The WHERE expression will be
passed to a configured adapter when possible.

Syntax:

How to Limit Data Source Access

...RESTRICT=level, NAME={name|SYSTEM} [,VALUE=test],$

or

...RESTRICT=VALUE_WHERE, NAME=name,  VALUE=expression; ,$

where:

level

Can be one of the following:

FIELD. which specifies that the user cannot access the fields named with the NAME
parameter.

SEGMENT. which specifies that the user cannot access the segments named with the
NAME parameter.

PROGRAM. which specifies that the program named with the NAME parameter will be
called whenever the user uses the data source.

SAME. which specifies that the user has the same restrictions as the user named in
the NAME parameter. No more than four nested SAME users are valid.

NOPRINT. which specifies that the field named in the NAME or SEGMENT parameter
can be mentioned in a request statement, but will not display. You can use a VALUE
test to limit the restriction to values that satisfy an expression. For example, consider
the following RESTRICT=NOPRINT declaration. User MARY can only display the IDs of
those employees whose salaries are less than 10000.

USER=MARY   ,ACCESS=R  ,RESTRICT=NOPRINT  ,NAME=EMP_ID ,
   VALUE=CURR_SAL LT 10000;,$

Note: A field with RESTRICT=NOPRINT can be referenced in a display command (verb),
but not in any type of filtering command, such as IF, WHERE, FIND, LOOKUP, or
VALIDATE.

418

10. Providing Data Source Security: DBA

name

Is the name of the field or segment to restrict. When used after NOPRINT, this can only be
a field name. NAME=SYSTEM, which can only be used with value tests, restricts every
segment in the data source, including descendant segments. Multiple fields or segments
can be specified by issuing the RESTRICT attribute several times for one user.

Note: With value restrictions, NAME=segment restricts the named segment and any
segment lower in the hierarchy, whether or not an alternate file view changes the retrieval
view. This means that if a parent segment has a value restriction, and a join or alternate
file view makes a child segment the new root, the value restriction on the original parent
will still apply to the new root.

VALUE

Specifies that the user can have access to only those values that meet the test described
in the test parameter.

test

Is the value test that the data must meet before the user can have access to it. The test
is an expression supported in an IF phrase.

VALUE_WHERE

Specifies that the user can have access to only those values that meet the test described
in the expression parameter.

expression;

Is the value test that the data must meet before the user can have access to it. The test
is an expression supported in a WHERE phrase.

Note: The semicolon (;) is required.

Example:

Restricting Access to Values Using VALUE_WHERE

Add the following DBA declarations to the end of the GGSALES Master File. These declarations
give USER1 access to the West region and to products that start with the letter C:

END
DBA = USERD,$
USER = USER1, ACCESS = R, NAME = SALES01, RESTRICT = VALUE_WHERE,
       VALUE = REGION EQ 'West' AND PRODUCT LIKE 'C%'; ,$

Describing Data With TIBCO WebFOCUS® Language

 419

Limiting Data Source Access: The RESTRICT Attribute

The following request sets the password to USER1 and sums dollar sales and units by
REGION, CATEGORY, and PRODUCT:

SET USER = USER1
TABLE FILE GGSALES
SUM DOLLARS UNITS
BY REGION
BY CATEGORY
BY PRODUCT
END

The output only displays those regions and products that satisfy the WHERE expression in the
Master File:

Region       Category     Product           Dollar Sales  Unit Sales
------       --------     -------           ------------  ----------
West         Coffee       Capuccino               915461       72831
             Food         Croissant              2425601      197022
             Gifts        Coffee Grinder          603436       48081
                          Coffee Pot              613624       47432

If the RESTRICT=VALUE_WHERE attribute is changed to a RESTRICT=VALUE attribute, the
expression is not valid, the following message is generated, and the request does not execute:

(FOC002) A WORD IS NOT RECOGNIZED:  LIKE 'C%'

Example:

Limiting Data Source Access

USER=BILL ,ACCESS=R ,RESTRICT=SEGMENT ,NAME=COMPSEG,$

Restricting Access to a Field or a Segment

The RESTRICT attribute identifies the segments or fields that the user will not be able to
access. Anything not named in the RESTRICT attribute will be accessible.

Without the RESTRICT attribute, the user has access to the entire data source. Users may be
limited to reading, writing, or updating new records, but every record in the data source is
available for the operation.

Syntax:

How to Restrict Access to a Field or a Segment

...RESTRICT=level,  NAME=name,$

where:

level

Can be one of the following:

FIELD specifies that the user cannot access the fields named with the NAME parameter.

420

10. Providing Data Source Security: DBA

SEGMENT specifies that the user cannot access the segments named with the NAME
parameter.

SAME specifies that the user has the same restrictions as the user named in the NAME
parameter.

NOPRINT specifies that the field named in the NAME or SEGMENT parameter can be
mentioned in a request statement but will not appear. When used after NOPRINT, NAME
can only be a field name. A field with RESTRICT=NOPRINT can be referenced in a display
command (verb), but not in any type of filtering command, such as IF, WHERE, FIND,
LOOKUP, or VALIDATE.

name

Is the name of the field or segment to restrict. When used after NOPRINT, this can only be
a field name.

NAME=SYSTEM, which can only be used with value tests, restricts every segment in the
data source, including descendant segments. Multiple fields or segments can be specified
by issuing the RESTRICT attribute several times for one user.

Note:

If a field or segment is mentioned in the NAME attribute, it cannot be retrieved by the user.
If such a field or segment is mentioned in a request statement, it will be rejected as
beyond the user access rights. With NOPRINT, the field or segment can be mentioned, but
the data will not appear. The data will appear as blanks for alphanumeric format or zeros
for numeric fields. A field with RESTRICT=NOPRINT can be referenced in a display command
(verb), but not in any type of filtering command, such as IF, WHERE, FIND, LOOKUP, or
VALIDATE.

You can restrict multiple fields or segments by providing multiple RESTRICT statements. For
example, to restrict Harry from using both field A and segment B, you issue the following
access limits:

USER=HARRY, ACCESS=R, RESTRICT=FIELD,   NAME=A,$
   RESTRICT=SEGMENT, NAME=B,$

You can restrict as many segments and fields as you like.

Using RESTRICT=SAME is a convenient way to reuse a common set of restrictions for more
than one password. If you specify RESTRICT=SAME and provide a user name or password
as it is specified in the USER attribute for the NAME value, the new user will be subject to
the same restrictions as the one named in the NAME attribute. You can then add additional
restrictions, as they are needed.

Describing Data With TIBCO WebFOCUS® Language

 421

Limiting Data Source Access: The RESTRICT Attribute

Example:

Restricting Access to a Segment

In the following example, Bill has read-only access to everything in the data source except the
COMPSEG segment:

USER=BILL ,ACCESS=R ,RESTRICT=SEGMENT ,NAME=COMPSEG,$

Example:

Reusing a Common Set of Access Restrictions

In the following example, both Sally and Harry have the same access privileges as BILL. In
addition, Sally is not allowed to read the SALARY field.

USER=BILL, ACCESS=R, RESTRICT=VALUE, NAME=IDSEG,
     VALUE=DIVISION EQ 'WEST',$
USER=SALLY, ACCESS=R, RESTRICT=SAME, NAME=BILL,$
                      RESTRICT=FIELD, NAME=SALARY,$
USER=HARRY, ACCESS=R, RESTRICT=SAME, NAME=BILL,$

Note: A restriction on a segment also affects access to its descendants.

Restricting Access to a Value

You can also restrict the values to which a user has access by providing a test condition in
your RESTRICT attribute. The user is restricted to using only those values that satisfy the test
condition.

You can restrict values in one of two ways: by restricting the values the user can read from the
data source, or restricting what the user can write to a data source. These restrictions are two
separate functions: one does not imply the other. You use the ACCESS attribute to specify
whether the values the user reads or the values the user writes are restricted.

You restrict the values a user can read by setting ACCESS=R and RESTRICT=VALUE. This type
of restriction prevents the user from seeing any data values other than those that meet the
test condition provided in the RESTRICT attribute. A RESTRICT attribute with ACCESS=R
functions as an involuntary IF statement in a report request. Therefore, the syntax for
ACCESS=R value restrictions must follow the rules for an IF test in a report request.

Note: RESTRICT=VALUE is not supported in Maintain Data.

422

10. Providing Data Source Security: DBA

Syntax:

How to Restrict Values a User Can Read

...ACCESS=R, RESTRICT=VALUE, NAME=name, VALUE=test,$

where:

name

Is the name of the segment which, if referenced, activates the test. To specify all
segments in the data source, specify NAME=SYSTEM.

test

Is the test being performed.

Example:

Restricting Values a User Can Read

USER=TONY, ACCESS=R, RESTRICT=VALUE, NAME=IDSEG,
     VALUE=DIVISION EQ 'WEST',$

With this restriction, Tony can only see records from the western division.

You type the test expression after VALUE=. The syntax of the test condition is the same as
that used by the TABLE command to screen records, except the word IF does not precede the
phrase. (Screening conditions in the TABLE command are discussed in the Creating Reports
With WebFOCUS Language manual.) Should several fields have tests performed on them,
separate VALUE attributes must be provided. Each test must name the segment to which it
applies. For example:

USER=DICK, ACCESS=R, RESTRICT=VALUE, NAME=IDSEG,
     VALUE=DIVISION EQ 'EAST' OR 'WEST',$
     NAME=IDSEG,
     VALUE=SALARY LE 10000,$

If a single test condition exceeds the allowed length of a line, it can be provided in sections.
Each section must start with the attribute VALUE= and end with the terminator (,$). For
example:

USER=SAM, ACCESS=R, RESTRICT=VALUE, NAME=IDSEG,
     VALUE=DIVISION EQ 'EAST' OR 'WEST',$
     VALUE=OR 'NORTH' OR 'SOUTH',$

Note: The second and subsequent lines of a value restriction must begin with the keyword OR.

Describing Data With TIBCO WebFOCUS® Language

 423

Controlling the Source of Access Restrictions in a Multi-file Structure

You can apply the test conditions to the parent segments of the data segments on which the
tests are applicable. Consider the following example:

USER=DICK, ACCESS=R, RESTRICT=VALUE, NAME=IDSEG,
     VALUE=DIVISION EQ 'EAST' OR 'WEST',$
     NAME=IDSEG,
     VALUE=SALARY LE 10000,$

The field named SALARY is actually part of a segment named COMPSEG. Since the test is
specified with NAME=IDSEG, the test is made effective for requests on its parent, IDSEG. In
this case, the request PRINT FULLNAME would only print the full names of people who meet
this test, that is, whose salary is less than or equal to $10,000, even though the test is
performed on a field that is part of a descendant segment of IDSEG. If, however, the test was
made effective on COMPSEG, that is, NAME=COMPSEG, then the full name of everyone in the
data source could be retrieved, but with the salary information of only those meeting the test
condition.

Restricting Both Read and Write Values

In many cases, it will prove useful to issue both ACCESS=W (for data maintenance) and
ACCESS=R (for TABLE) value restrictions for a user. This will both limit the values a user can
write to the data source and limit the data values that the user can actually see. You do this by
issuing a RESTRICT=VALUE attribute with ACCESS=R to prohibit the user from seeing any
values other than those specified in the test condition. You then issue a RESTRICT=VALUE
attribute with ACCESS=W that specifies the write restrictions placed on the user. You cannot
use ACCESS=RW to do this.

Note: Write restrictions apply to data maintenance facilities not discussed in this manual. For
more information, see the Maintain Data documentation.

Controlling the Source of Access Restrictions in a Multi-file Structure

The DBASOURCE parameter determines which security attributes are used to grant access to
multi-file structures. By default, access restrictions are based on the host file in a JOIN
structure or the last file in a COMBINE structure. If you set the DBASOURCE parameter to ALL,
access restrictions from all files in a JOIN or COMBINE structure will be enforced.

Note: You can also create and implement a DBAFILE to contain and enforce the access
restrictions from all files in a JOIN or COMBINE structure. For information about using a central
Master File to contain access restrictions, see Placing Security Information in a Central Master
File on page 428.

424

10. Providing Data Source Security: DBA

The SET DBASOURCE command can only be issued one time in a session or connection. Any
attempt to issue the command additional times will be ignored. If the value is set in a profile,
no user can change it at any point in the session.

When DBASOURCE=ALL:

In a TABLE request against a JOIN structure, access to a cross-reference file or segment is
allowed only if the user has at least read access to each file in the structure.

In a MODIFY COMBINE structure, the user must have a minimum of READ access to all files
in the structure. The user requires WRITE, UPDATE, or READ/WRITE access to a file in the
structure when an INCLUDE, DELETE, or UPDATE request is issued against that file.

When DBASOURCE=HOST:

In a TABLE request, the user needs read access to the host file in the JOIN structure. All
security limitations come from the host file. Note that you can create and activate a
DBAFILE in order to enforce security restrictions from all files in the structure.

In a MODIFY procedure, the user needs write access to the last file in the COMBINE
structure. All security limitations come from the restrictions in the last file in the structure.
Note that you can create and activate a DBAFILE in order to enforce security restrictions
from all files in the structure.

Syntax:

How to Control Enforcement of Access Restrictions in a JOIN or COMBINE Structure

SET DBASOURCE = {HOST|ALL}

where:

HOST

Enforces access restrictions only from the host file in a JOIN structure or the last file in a
COMBINE structure unless a DBAFILE is used to enforce access restrictions to other files
in the structure. HOST is the default value.

ALL

Requires the user to have read access to every file in a JOIN or COMBINE structure. The
user needs W, U, or RW access to a file in a COMBINE structure when an INCLUDE,
UPDATE, or DELETE command is issued against that file.

Reference: Usage Notes for SET DBASOURCE

All files in the JOIN or COMBINE structure must have the same DBA password. If the DBA
attributes are not the same, there will be no way to access the structure.

Describing Data With TIBCO WebFOCUS® Language

 425

Controlling the Source of Access Restrictions in a Multi-file Structure

If the SET DBASOURCE command is issued more than once in a session, the following
message displays and the value is not changed:

(FOC32575) DBASOURCE  CANNOT BE RESET
VALUE WAS NOT CHANGED

Example:

Controlling Access Restrictions in a JOIN

The following request joins the TRAINING data source to the EMPDATA and COURSE data
sources and then issues a request against the joined structure:

JOIN CLEAR *
JOIN COURSECODE IN TRAINING TO COURSECODE IN COURSE AS J1
JOIN PIN IN TRAINING TO PIN IN EMPDATA AS J2
TABLE FILE TRAINING
PRINT COURSECODE AS 'CODE' CTITLE
   LOCATION AS 'LOC'
BY LASTNAME
WHERE COURSECODE NE '   '
WHERE LOCATION EQ 'CA' OR LOCATION LIKE 'N%'
END

When the Master Files do not have DBA attributes, the output is:

LASTNAME         CODE     CTITLE                               LOC
--------         ----     ------                               ---
ADAMS            EDP750   STRATEGIC MARKETING PLANNING         NJ
CASTALANETTA     EDP130   STRUCTURED SYS ANALYSIS WKSHP        NY
                 AMA130   HOW TO WRITE USERS MANUAL            CA
CHISOLM          EDP690   APPLIED METHODS IN MKTG RESEARCH     NJ
FERNSTEIN        MC90     MANAGING DISTRIBUTOR SALE NETWORK    NY
GORDON           SFC280   FUND OF ACCTG FOR SECRETARIES        NY
LASTRA           MC90     MANAGING DISTRIBUTOR SALE NETWORK    NY
MARTIN           EDP130   STRUCTURED SYS ANALYSIS WKSHP        CA
MEDINA           EDP690   APPLIED METHODS IN MKTG RESEARCH     NJ
OLSON            PU168    FUNDAMNETALS OF MKTG COMMUNICATIONS  NY
RUSSO            PU168    FUNDAMNETALS OF MKTG COMMUNICATIONS  NY
SO               BIT420   EXECUTIVE COMMUNICATION              CA
WANG             PU440    GAINING COMPETITIVE ADVANTAGE        NY
WHITE            BIT420   EXECUTIVE COMMUNICATION              CA

Now, add the following DBA attributes to the bottom of the TRAINING Master File:

END
DBA = DBA1,$
USER = TUSER, ACCESS =R,$

Running the same request produces the following message:

(FOC047) THE USER DOES NOT HAVE SUFFICIENT ACCESS RIGHTS TO THE FILE:
TRAINING
BYPASSING TO END OF COMMAND

426

10. Providing Data Source Security: DBA

Now, issue the following SET PASS command:

SET PASS = TUSER

Add the following DBA attributes to the bottom of the COURSE Master File:

END
DBA = DBA1,$
USER = CUSER, ACCESS = R,$

Add the following DBA attributes to the bottom of the EMPDATA Master File:

END
DBA = DBA1,$
USER = EUSER, ACCESS = R,$

Note that the DBA attribute has the same value in all of the Master Files.

Now, run the request again. There will be no security violation, and the report output will be
generated. Since the DBASOURCE parameter is set to HOST (the default), you can run the
request using a password that is valid only in the host file.

Now, set the DBASOURCE parameter to ALL:

SET DBASOURCE = ALL
SET PASS = TUSER

Running the request produces the following message because TUSER is not a valid user for
the COURSE data source:

(FOC052) THE USER DOES NOT HAVE ACCESS TO THE FIELD: CTITLE

Now, issue the following SET PASS command that sets a valid password for each file in the
structure:

SET PASS = TUSER IN TRAINING, CUSER IN COURSE, EUSER IN EMPDATA

You can now run the request and generate the report output.

Once SET DBASOURCE command has been issued, its value cannot be changed. The following
SET command attempts to change the value to HOST, but the query command output shows
that it was not changed:

>  > set dbasource = host
(FOC32575) DBASOURCE CANNOT BE RESET
VALUE WAS NOT CHANGED

Describing Data With TIBCO WebFOCUS® Language

 427

Adding DBA Restrictions to the Join Condition

Adding DBA Restrictions to the Join Condition

When DBA restrictions are applied to a request on a multi-segment structure, by default, the
restrictions are added as WHERE conditions in the report request. When the DBAJOIN
parameter is set ON, DBA restrictions are treated as internal to the file or segment for which
they are specified, and are added to the join syntax.

This difference is important when the file or segment being restricted has a parent in the
structure and the join is an outer or unique join.

When restrictions are treated as report filters, lower-level segment instances that do not
satisfy them are omitted from the report output, along with their host segments. Since host
segments are omitted, the output does not reflect a true outer or unique join.

When the restrictions are treated as join conditions, lower-level values from segment instances
that do not satisfy them are displayed as missing values, and the report output displays all
host rows.

For more information, see the Creating Reports With WebFOCUS Language manual.

Placing Security Information in a Central Master File

The DBAFILE attribute enables you to place all passwords and restrictions for multiple Master
Files in one central file. Each individual Master File points to this central control file. Groups of
Master Files with the same DBA password may share a common DBAFILE which itself has the
same DBA password.

There are several benefits to this technique, including:

Passwords only have to be stored once when they are applicable to a group of data
sources, simplifying password administration.

Data sources with different user passwords can be JOINed or COMBINEd. In addition,
individual DBA information remains in effect for each data source in a JOIN or COMBINE.

The central DBAFILE is a standard Master File. Other Master Files can use the password and
security restrictions listed in the central file by specifying its file name with the DBAFILE
attribute.

428

10. Providing Data Source Security: DBA

Note:

All Master Files that specify the same DBAFILE have the same DBA password.

The central DBAFILE, like any Master File, must contain at least one segment declaration
and one field declaration before the END statement that signifies the presence of DBA
information. Even if a required attribute is not assigned a specific value, it must be
represented by a comma. The DBA password in the DBAFILE is the same as the password
in all the Master Files that refer to it. This prevents individuals from substituting their own
security. All Master Files should be encrypted.

The DBAFILE may contain a list of passwords and restrictions following the DBA password.
These passwords apply to all data sources that reference this DBAFILE. In the example in
Placing Security Attributes in a Central Master File on page 430, PASS=BILL, with
ACCESS=R (read only), applies to all data sources that contain the attribute
DBAFILE=FOUR.

After the common passwords, the DBAFILE may specify data source-specific passwords and
additions to general passwords. You implement this feature by including FILENAME
attributes in the DBA section of the DBAFILE (for example, FILENAME=TWO). See File
Naming Requirements for DBAFILE on page 433 for additional information about the
FILENAME attribute.

Data source-specific restrictions override general restrictions for the specified data source.
In the case of a conflict, passwords in the FILENAME section take precedence. For
example, a DBAFILE might contain ACCESS=RW in the common section, but specify
ACCESS=R for the same password by including a FILENAME section for a particular data
source.

Value restrictions accumulate. All value restrictions must be satisfied before retrieval. In
the preceding example, note the two occurrences of PASS=JOE. JOE is a common
password for all data sources, but in FILENAME=THREE it carries an extra restriction,
RESTRICT=..., which applies only to data source THREE.

Syntax:

How to Place Security Attributes in a Central Master File

END
DBA=dbaname, DBAFILE=filename ,$

where:

dbaname

Is the same as the dbaname in the central file.

Describing Data With TIBCO WebFOCUS® Language

 429

Placing Security Information in a Central Master File

filename

Is the name of the central file.

You can specify passwords and restrictions in a DBAFILE that apply to every Master File that
points to that DBAFILE. You can also include passwords and restrictions for specific Master
Files by including FILENAME attributes in the DBAFILE.

Example:

Placing Security Attributes in a Central Master File

The following example shows a group of Master Files that share a common DBAFILE named
FOUR:

ONE MASTER
FILENAME=ONE
  .
  .
END
DBA=ABC, DBAFILE=FOUR,$

TWO MASTER
FILENAME=TWO
  .
  .
END
DBA=ABC, DBAFILE=FOUR,$

THREE MASTER
FILENAME=THREE
  .
  .
END
DBA=ABC,
DBAFILE=FOUR,$

FOUR MASTER
FILENAME=FOUR,$
SEGNAME=mmmmm,$
FIELDNAME=fffff,$
END
DBA=ABC,$
   PASS=BILL,ACCESS=R,$
   PASS=JOE,ACCESS=R,$
FILENAME=TWO,$
   PASS=HARRY,ACCESS=RW,$
FILENAME=THREE,$
   PASS=JOE,ACCESS=R,RESTRICT=...,$
   PASS=TOM,ACCESS=R,$

430

10. Providing Data Source Security: DBA

Example:

Using DBAFILE With a Join Structure

The following request joins the TRAINING data source to the EMPDATA and COURSE data
sources, and then issues a request against the joined structure:

JOIN CLEAR *
JOIN COURSECODE IN TRAINING TO COURSECODE IN COURSE AS J1
JOIN PIN IN TRAINING TO PIN IN EMPDATA AS J2
TABLE FILE TRAINING
PRINT COURSECODE AS 'CODE' CTITLE
   LOCATION AS 'LOC'
BY LASTNAME
WHERE COURSECODE NE '   '
WHERE LOCATION EQ 'CA' OR LOCATION LIKE 'N%'
END

When the Master Files do not have DBA attributes, the output is:

LASTNAME         CODE     CTITLE                               LOC
--------         ----     ------                               ---
ADAMS            EDP750   STRATEGIC MARKETING PLANNING         NJ
CASTALANETTA     EDP130   STRUCTURED SYS ANALYSIS WKSHP        NY
                 AMA130   HOW TO WRITE USERS MANUAL            CA
CHISOLM          EDP690   APPLIED METHODS IN MKTG RESEARCH     NJ
FERNSTEIN        MC90     MANAGING DISTRIBUTOR SALE NETWORK    NY
GORDON           SFC280   FUND OF ACCTG FOR SECRETARIES        NY
LASTRA           MC90     MANAGING DISTRIBUTOR SALE NETWORK    NY
MARTIN           EDP130   STRUCTURED SYS ANALYSIS WKSHP        CA
MEDINA           EDP690   APPLIED METHODS IN MKTG RESEARCH     NJ
OLSON            PU168    FUNDAMNETALS OF MKTG COMMUNICATIONS  NY
RUSSO            PU168    FUNDAMNETALS OF MKTG COMMUNICATIONS  NY
SO               BIT420   EXECUTIVE COMMUNICATION              CA
WANG             PU440    GAINING COMPETITIVE ADVANTAGE        NY
WHITE            BIT420   EXECUTIVE COMMUNICATION              CA

The EMPDATA Master File will be the central DBAFILE for the request. Add the following DBA
attributes to the bottom of the EMPDATA Master File:

END
DBA=DBA1,$
USER = EUSER, ACCESS = R,$
FILENAME = COURSE
USER = CUSER2, ACCESS=RW,$

With these DBA attributes, user EUSER will have read access to all files that use EMPDATA as
their DBAFILE. User CUSER2 will have read/write access to the COURSE data source.

Describing Data With TIBCO WebFOCUS® Language

 431

Placing Security Information in a Central Master File

Add the following security attributes to the bottom of the COURSE Master File. These attributes
makes the EMPDATA Master File the central file that contains the security attributes to use for
access to the COURSE data source and it sets the DBA attribute to the same value as the DBA
attribute in the EMPDATA Master File:

END
DBA = DBA1, DBAFILE=EMPDATA,$

Add the following security attributes to the bottom of the TRAINING Master File. These
attributes makes the EMPDATA Master File the central file that contains the security attributes
to use for access to the TRAINING data source and it sets the DBA attribute to the same value
as the DBA attribute in the EMPDATA Master File:

END
DBA = DBA1, DBAFILE=EMPDATA,$

Now, in order to run a request against the JOIN structure, there must be a current user
password with read access in effect for each file in the JOIN. Issue the following SET PASS
command and run the request:

SET PASS = EUSER

or

SET PASS = EUSER IN *

The request runs and produces output because EUSER is a valid user in each of the files in
the join.

Since the EMPDATA Master File identifies CUSER2 as a valid user for the COURSE Master File,
you can also run the request with the following SET PASS command:

SET USER = EUSER IN EMPDATA, EUSER IN TRAINING, CUSER2 IN COURSE

Issuing a SET PASS command that does not specify a valid password for each file in the JOIN
structure produces one of the following messages, and the request does not run:

(FOC052) THE USER DOES NOT HAVE ACCESS TO THE FIELD: fieldname

(FOC047) THE USER DOES NOT HAVE SUFFICIENT ACCESS RIGHTS TO THE FILE:
filename

432

10. Providing Data Source Security: DBA

File Naming Requirements for DBAFILE

When a DBAFILE includes a FILENAME attribute for a specific Master File, the FILENAME
attribute in the referencing Master File must be the same as the FILENAME attribute in the
DBA section of the DBAFILE. This prevents users from renaming a Master File to a name
unknown by the DBAFILE.

Example:

DBAFILE Naming Conventions

ONE MASTER
FILENAME=XONE
  .
  .
  .
END
DBA=ABC, DBAFILE=FOUR,$

FOUR MASTER
FILENAME=XFOUR
  .
  .
  .
END
DBA=ABC,$
  .
  .
  .
FILENAME=XONE,$
  .
  .
  .

ONE MASTER is referred to in requests as TABLE FILE ONE. However, both ONE MASTER and
the DBA section of the DBAFILE, FOUR MASTER, specify FILENAME=XONE.

For security reasons, the FILENAME attribute in the Master File containing the DBAFILE
information should not be the same as the name of that Master File. Note that in Master File
FOUR, the FILENAME attribute specifies the name XFOUR.

Connection to an Existing DBA System With DBAFILE

If there is no mention of the new attribute, DBAFILE, there will be no change in the
characteristics of an existing system. In the current system, when a series of data sources is
JOINed, the first data source in the list is the controlling data source. Its passwords are the
only ones examined. For a COMBINE, only the last data source passwords take effect. All data
sources must have the same DBA password.

Describing Data With TIBCO WebFOCUS® Language

 433



Summary of Security Attributes

In the new system, the DBA sections of all data sources in a JOIN or COMBINE are examined.
If DBAFILE is included in a Master File, then its passwords and restrictions are read. To make
the DBA section of a data source active in a JOIN list or COMBINE, specify DBAFILE for that
data source.

After you start to use the new system, convert all of your Master Files. For Database
Administrators who want to convert existing systems but do not want a separate physical
DBAFILE, the DBAFILE attribute can specify the data source itself.

Example:

Connecting to an Existing DBA System With DBAFILE

FILENAME=SEVEN,
  SEGNAME=..
    FIELDNAME=...
     .
     .
     .
END
DBA=ABC,DBAFILE=SEVEN,$    (OR DBAFILE= ,$)
 PASS=...
 PASS=...

Combining Applications With DBAFILE

Since each data source now contributes its own restrictions, you can JOIN and COMBINE data
sources that come from different applications and have different user passwords. The only
requirement is a valid password for each data source. You can therefore grant access rights
for one application to an application under the control of a different DBA by assigning a
password in your system.

You can assign screening conditions to a data source that are automatically applied to any
report request that accesses the data source. See the Creating Reports With WebFOCUS
Language manual for details.

Summary of Security Attributes

The following is a list of all the security attributes used in WebFOCUS:

Attribute

Alias

Maximum
Length

Meaning

DBA

DBA

8

Value assigned is code name of the
Database Administrator (DBA) who
has unrestricted access to the data
source.

434

Attribute

Alias

USER

PASS

ACCESS

ACCESS

8

8

RESTRICT

RESTRICT

8

NAME

NAME

VALUE

VALUE

DBAFILE

DBAFILE

66

80

8

10. Providing Data Source Security: DBA

Maximum
Length

Meaning

Values are arbitrary code names,
identifying users for whom security
restrictions will be in force.

Levels of access for this user.
Values are:

R - read-only

W - write new segments only

RW - read and write

U - update values only

Types of restrictions to be imposed
for this access level. Values are:

SEGMENT
FIELD
VALUE
SAME

NOPRINT

Name of segment or field restricted
or program to be called.

Test expression which must be true
when RESTRICT=VALUE is the type
of limit.

Names the Master File containing
passwords and restrictions to use.

Describing Data With TIBCO WebFOCUS® Language

 435

Hiding Restriction Rules: The ENCRYPT Command

Hiding Restriction Rules: The ENCRYPT Command

Since the restriction information for a FOCUS data source is stored in its Master File, you can
encrypt the Master File in order to prevent users from examining the restriction rules. Only the
Database Administrator can encrypt a description. You must set PASS=DBAname before you
issue the ENCRYPT command. The syntax of the ENCRYPT command varies from operating
system to operating system.

Note: The first line of a Master File that is going to be encrypted cannot be longer than 68
characters. If it is longer than 68 characters, you must break it up onto multiple lines.

Syntax:

How to Hide Restriction Rules: ENCRYPT Command

ENCRYPT FILE filename

where:

filename

Is the name of the file to be encrypted.

Example:

Encrypting and Decrypting a Master File

The following is an example of the complete procedure:

SET PASS=JONES76
ENCRYPT FILE PERS

The process can be reversed in order to change the restrictions. The command to restore the
description to a readable form is DECRYPT.

The DBA password must be issued with the SET command before the file can be decrypted.
For example:

SET PASS=JONES76
DECRYPT FILE PERS

Encrypting Data

You may also use the ENCRYPT parameter within the Master File to encrypt some or all of its
segments. When encrypted files are stored on the external media (disk or tape) each is secure
from unauthorized examination.

Encryption takes place on the segment level. That is, the entire segment is encrypted. The
request for encryption is made in the Master File by setting the attribute ENCRYPT to ON.

436

10. Providing Data Source Security: DBA

Example:

Encrypting Data

SEGMENT=COMPSEG, PARENT=IDSEG, SEGTYPE=S1, ENCRYPT=ON,$

You must specify the ENCRYPT parameter before entering any data in the data source. The
message NEW FILE... must appear when the encryption is first requested. Encryption cannot
be requested later by a change to the Master File and cannot be removed after it has been
requested or any data has been entered in the data source.

Performance Considerations for Encrypted Data

There is a small loss in processing efficiency when data is encrypted. Minimize this loss by
grouping the sensitive data fields together on a segment and making them a separate
segment of SEGTYPE=U, unique segment, beneath the original segment. For example,
suppose the data items on a segment are:

They should be grouped as:

Describing Data With TIBCO WebFOCUS® Language

 437

FOCEXEC Security

Note: If you change the DBA password, you must issue the RESTRICT command, as described
in How to Change a DBA Password on page 409.

Setting a Password Externally

Passwords can also be set automatically by an external security system such as RACF®, CA-
ACF2®, or CA-Top Secret®. Passwords issued this way are set when WebFOCUS first enters
and may be permanent (that is, not alterable by subsequent SET USER, SET PASS, or -PASS
commands). Or they may be default passwords that can be subsequently overridden. The
passwords may be permanent for some users, defaults for other users, and not set at all for
other users.

The advantage of setting WebFOCUS passwords externally is that the password need not be
known by the user, does not require prompting, and does not have to be embedded in a
PROFILE FOCEXEC or an encrypted FOCEXEC.

Passwords set this way must match the passwords specified in the Master Files of the data
sources being accessed.

FOCEXEC Security

Most data security issues are best handled by WebFOCUS DBA exit routines. For more
information about WebFOCUS DBA exit routines see the WebFOCUS Security and Administration
manual. You can also encrypt and decrypt FOCEXECs.

Encrypting and Decrypting a FOCEXEC

Keep the actual text of a stored FOCEXEC confidential while allowing users to execute the
FOCEXEC. You do this either because there is confidential information stored in the FOCEXEC
or because you do not want the FOCEXEC changed by unauthorized users. You can protect a
stored FOCEXEC from unauthorized users with the ENCRYPT command.

Any user can execute an encrypted FOCEXEC, but you must decrypt the FOCEXEC to view it.
Only a user with the encrypting password can decrypt the FOCEXEC.

The password selected by a user to ENCRYPT or DECRYPT a FOCEXEC is not viewable by any
editor and it is unrelated to the DBA passwords of the files being used.

Syntax:

How to Encrypt and Decrypt a FOCEXEC

You use the following procedure to encrypt the FOCEXEC named SALERPT:

SET PASS = DOHIDE
ENCRYPT FILE SALERPT FOCEXEC

438

10. Providing Data Source Security: DBA

You use the following procedure to decrypt the FOCEXEC named SALERPT:

SET PASS = DOHIDE
DECRYPT FILE SALERPT FOCEXEC

Describing Data With TIBCO WebFOCUS® Language

 439

FOCEXEC Security

440

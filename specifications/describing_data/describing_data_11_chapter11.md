Chapter11

Creating and Rebuilding a Data Source

You can create a new data source, or re-initialize an existing data source, using the
CREATE command.

After a data source exists, you may find it necessary to reorganize it in order to use disk
space more effectively, to change the contents, index, or structure of the data source, or
to change legacy date fields to smart date fields. You can do all of this and more using
the REBUILD command.

You can use the CREATE and REBUILD commands with FOCUS and XFOCUS data
sources. You can also use the CREATE command to create relational tables for which
you have the appropriate data adapter.

In the remainder of this chapter, all references to FOCUS data sources apply to FOCUS
and XFOCUS data sources.

In this chapter:

Creating a New Data Source: The CREATE Command

Rebuilding a Data Source: The REBUILD Command

Optimizing File Size: The REBUILD Subcommand

Changing Data Source Structure: The REORG Subcommand

Indexing Fields: The INDEX Subcommand

Creating an External Index: The EXTERNAL INDEX Subcommand

Checking Data Source Integrity: The CHECK Subcommand

Changing the Data Source Creation Date and Time: The TIMESTAMP Subcommand

Converting Legacy Dates: The DATE NEW Subcommand

Creating a Multi-Dimensional Index: The MDINDEX Subcommand

Describing Data With TIBCO WebFOCUS® Language

 441

Creating a New Data Source: The CREATE Command

Creating a New Data Source: The CREATE Command

You can create a new, empty FOCUS data source for a Master File using the CREATE
command. You can also use the CREATE command to erase the data in an existing FOCUS
data source.

The CREATE command also works, with the appropriate data adapter installed, for a relational
table (such as a DB2 or Teradata table). For information, see the documentation for the
relevant data adapter.

If you issue the CREATE FILE command when the data source already exists, the following
message appears for a FOCUS or XFOCUS data source:

(FOC441) WARNING. THE FILE EXISTS ALREADY. CREATE WILL WRITE OVER IT.
REPLY:

The DROP option on the CREATE FILE command prevents the display of the message and
creates the data source, dropping the existing table first, if necessary, and re-parsing the
Master File if it changed.

Note that on z/OS, you must issue either an allocation or a CREATE command for a new data
source. For all other platforms, if the data source has not been initialized, a CREATE is
automatically issued on the first MODIFY or Maintain Data request made against the data
source.

Syntax:

How to Use the CREATE Command

CREATE FILE mastername [DROP]

where:

mastername

Is the name of the Master File that describes the data source.

DROP

Drops an existing file before performing the CREATE and re-parses the Master File, if
necessary. No warning messages are generated.

If you issue the CREATE FILE filename DROP command for a FOCUS or XFOCUS data
source that has an external index or MDI, you must REBUILD the index after creating the
data source.

442

11. Creating and Rebuilding a Data Source

Note the following when issuing CREATE on z/OS:

If you do not allocate the data source prior to issuing the CREATE command, the data
source is created as a temporary data set. To retain the data source, copy it to a
permanent data set with the DYNAM COPY command.

The CREATE command preformats the primary space allocation and initializes the data
source entry in the File Directory Table. A Master File must exist for the data source in a
PDS allocated to ddname MASTER.

Issuing MODIFY or Maintain commands against data sources for which no CREATE or
allocation was issued results in a read error.

After you enter the CREATE command, the following appears:

NEW FILE name ON date AT time

where:

name

Is the complete name of the new data source.

ON date AT time

Is the date and time at which the data source was created or recreated.

When you issue the CREATE command without the DROP option, if the data source already
exists, the following message appears:

(FOC441) WARNING. THE FILE EXISTS ALREADY. CREATE WILL WRITE OVER IT.
REPLY:

To erase the data source and create a new, empty data source, enter Y. To cancel the
command and leave the data source intact, enter END, QUIT, or N.

If you wish to give the data source absolute File Integrity protection, issue the following
command prior to the CREATE command:

SET SHADOW=ON

Example:

Recreating a FOCUS Data Source in Windows

To recreate the EMPLOYEE data source, issue the following command:

CREATE FILE EMPLOYEE

Describing Data With TIBCO WebFOCUS® Language

 443

Rebuilding a Data Source: The REBUILD Command

The following message appears:

(FOC441) WARNING. THE FILE EXISTS ALREADY. CREATE WILL WRITE OVER IT
REPLY:

You would reply:

YES

The following message appears:

NEW FILE C:EMPLOYEE.FOC     ON 01/03/2003 AT 15.48.57

The EMPLOYEE data source still exists on disk, but it contains no records.

Rebuilding a Data Source: The REBUILD Command

You can make a structural change to a FOCUS data source after it has been created using the
REBUILD command. Using REBUILD and one of its subcommands REBUILD, REORG, INDEX,
EXTERNAL INDEX, CHECK, TIMESTAMP, DATE NEW, and MDINDEX, you can:

Rebuild a disorganized data source (REBUILD).

Delete instances according to a set of screening conditions (REBUILD or REORG).

Redesign an existing data source. This includes adding and removing segments, adding
and removing data fields, indexing different fields, changing the size of alphanumeric data
fields and more (REORG).

Index new fields after rebuilding or creating the data source (INDEX).

Create an external index database that facilitates indexed retrieval when joining or locating
records (EXTERNAL INDEX).

Check the structural integrity of the data source (CHECK). Check when the FOCUS data
source was last changed (TIMESTAMP).

Convert legacy date formats to smart date formats (DATE NEW).

Build or modify a multi-dimensional index (MDINDEX).

You can use the REBUILD facility:

As a batch procedure, by entering the REBUILD command, the desired subcommand, and
any responses to subcommand prompts on separate lines of a procedure.

Before using the REBUILD facility, you should be aware of several required and recommended
prerequisites regarding file allocation, security authorization, and backup.

444

Reference: Before You Use REBUILD: Prerequisites

Before you use the REBUILD facility, there are several prerequisites that you must consider:

11. Creating and Rebuilding a Data Source

Allocation. Usually, you do not have to allocate workspace prior to using a REBUILD
command. It is automatically allocated. However, adequate workspace must be available.
As a rule of thumb, have space 10 to 20% larger than the size of the existing file available
for the REBUILD and REORG options.

The file name REBUILD is always assigned to the workspace. In the DUMP phase of the
REORG command, the allocation statement appears in case you want to perform the LOAD
phase at a different time.

Security authorization. If the data source you are rebuilding is protected by a database
administrator, you must be authorized for read and write access in order to perform any
REBUILD activity. For more information on data source security, see Providing Data Source
Security: DBA on page 405.

Backup. Although it is not a requirement, we recommend that you create a backup copy of
the original Master File and data source before using any of the REBUILD subcommands.

Procedure: How to Use the REBUILD Facility

The following steps describe how to use the REBUILD facility:

1.

Initiate the REBUILD facility by entering:

REBUILD

2. Select a subcommand by supplying its name or its number. The following list shows the

subcommand names and their corresponding numbers:

1. REBUILD        (Optimize the database structure)
2. REORG          (Alter the database structure)
3. INDEX          (Build/modify the database index)
4. EXTERNAL INDEX (Build/modify an external index database)
5. CHECK          (Check the database structure)
6. TIMESTAMP      (Change the database timestamp)
7. DATE NEW       (Convert old date formats to smart date formats)
8. MDINDEX        (Build/modify a multidimensional index)

Your subsequent responses depend on the subcommand you select. Generally, you will only
need to give the name of the data source and possibly one or two other items of information.

Describing Data With TIBCO WebFOCUS® Language

 445

Rebuilding a Data Source: The REBUILD Command

Controlling the Frequency of REBUILD Messages

When REBUILD processes a data source, it displays status messages periodically (for
example, REFERENCE..AT SEGMENT 1000) to inform you of the progress of the rebuild. The
default display interval is every 1000 segment instances processed during REBUILD retrieval
and load phases. The number of messages that appear is determined by the number of
segment instances in the FOCUS data source being rebuilt, divided by the display interval.

Syntax:

How to Control the Frequency of REBUILD Messages

REBUILD displays a message (REFERENCE..AT SEGMENT segnum) at periodic intervals to
inform you of its progress as it processes a data source. You can control the frequency with
which REBUILD displays this message by issuing the command

SET REBUILDMSG = {n|1000}

where:

n

Is any integer from 1,000 to 99,999,999 or 0 (to disable the messages).

A setting of less than 1000:

Generates a warning message that describes the valid values (0 or greater than 999).

Keeps the current setting. The current setting will either be the default of 1000, or the last
valid integer greater than 999 to which REBUILDMSG was set.

Example:

Controlling the Display of REBUILD Messages

The following messages are generated for a REBUILD CHECK where REBUILDMSG has been
set to 4000, and the data source contains 19,753 records.

STARTING..
REFERENCE..AT SEGMENT    4000
REFERENCE..AT SEGMENT    8000
REFERENCE..AT SEGMENT   12000
REFERENCE..AT SEGMENT   16000
NUMBER OF SEGMENTS RETRIEVED=   19753
CHECK COMPLETED...

446

Optimizing File Size: The REBUILD Subcommand

11. Creating and Rebuilding a Data Source

You use the REBUILD subcommand for one of two reasons. Primarily, you use it to improve
data access time and storage efficiency. After many deletions, the physical structure of your
data does not match the logical structure. REBUILD REBUILD dumps data into a temporary
work space and then reloads it, putting instances back in their proper logical order. A second
use of REBUILD REBUILD is to delete segment instances according to a set of screening
conditions.

Normally, you use the REBUILD subcommand as a way of maintaining a clean data source. To
check if you need to rebuild your data source, enter the ? FILE command (described in
Confirming Structural Integrity Using ? FILE and TABLEF on page 462):

? FILE filename

If your data source is disorganized, the following message appears:

FILE APPEARS TO NEED THE -REBUILD-UTILITY
REORG PERCENT IS A MEASURE OF FILE DISORGANIZATION
0 PCT IS PERFECT -- 100 PCT IS BAD
REORG PERCENT x%

This message appears whenever the REORG PERCENT measure is more than 30%. The REORG
PERCENT measure indicates the degree to which the physical placement of data in the data
source differs from its logical, or apparent, placement.

The &FOCDISORG variable can be used immediately after the ? FILE command and also shows
the percentage of disorganization in a data source. &FOCDISORG will show a data source
percentage of disorganization even if it is below 30% (see the Developing Reporting
Applications manual).

Procedure: How to Use the REBUILD Subcommand

The following steps describe how to use the REBUILD subcommand:

1.

Initiate the REBUILD facility by entering:

REBUILD

The following options are available:

1. REBUILD        (Optimize the database structure)
2. REORG          (Alter the database structure)
3. INDEX          (Build/modify the database index)
4. EXTERNAL INDEX (Build/modify an external index database)
5. CHECK          (Check the database structure)
6. TIMESTAMP      (Change the database timestamp)
7. DATE NEW       (Convert old date formats to smartdate formats)
8. MDINDEX        (Build/modify a multidimensional index)

Describing Data With TIBCO WebFOCUS® Language

 447

Optimizing File Size: The REBUILD Subcommand

2. Select the REBUILD subcommand by entering:

REBUILD or 1

3. Enter the name of the data source to be rebuilt.

On z/OS, enter the ddname.

On UNIX, Windows, and OpenVMS, enter filename. The data source to be rebuilt will be
referenced by a USE command. If no USE command is in effect, the data source will be
searched for using the EDAPATH variable.

4.

If you are simply rebuilding the data source and require no selection tests, enter:

NO

The REBUILD procedure will begin immediately.

On the other hand, if you wish to place screening conditions on the REBUILD
subcommand, enter:

YES

Then enter the necessary selection tests, ending the last line with ,$.

Test relations of EQ, NE, LE, GE, LT, GT, CO (contains), and OM (omits) are permitted.
Tests are connected with the word AND, and lists of literals may be connected with the OR
operator. A comma followed by a dollar sign (,$) is required to terminate any test.

For example, you might enter the following:

A EQ A1 OR A2 AND B LT 100 AND
C GT 400 AND D CO 'CUR',$

Statistics appear when the REBUILD REBUILD procedure is complete, including the number of
segments retrieved and the number of segments included in the rebuilt data source.

Example:

Using the REBUILD Subcommand in Windows

The following procedure:

 1. REBUILD
 2. REBUILD
 3. EMPLOYEE
 4. NO

1. Initiates the REBUILD facility.

2. Specifies the REBUILD subcommand.

3. Provides the name of the data source to rebuild.

448

11. Creating and Rebuilding a Data Source

4. Indicates that no record selection tests are required.

The data source will be rebuilt and the appropriate statistics will be generated.

Changing Data Source Structure: The REORG Subcommand

The REORG subcommand enables you to make a variety of changes to the Master File after
data has been entered in the FOCUS data source. REBUILD REORG is a two-step procedure
that first dumps the data into a temporary workspace and then reloads it under a new Master
File.

You can use REBUILD REORG to:

Add new segments as descendants of existing segments.

Remove segments.

Add new data fields as descendants to an existing segment.

Note: The fields must be added after the key fields.

Remove data fields.

Change the order of non-key data fields within a segment. Key fields may not be changed.

Promote fields from unique segments to parent segments.

Demote fields from parent segments to descendant unique segments.

Index different fields or remove indexes.

Increase or decrease the size of an alphanumeric data field.

REBUILD REORG will not enable you to:

Change field format types (alphanumeric to numeric and vice versa, changing numeric
format types).

Change the value for SEGNAME attributes.

Change the value for SEGTYPE attributes.

Change field names that are indexed.

Describing Data With TIBCO WebFOCUS® Language

 449

Changing Data Source Structure: The REORG Subcommand

Procedure: How to Use the REORG Subcommand

The following steps describe how to use the REORG subcommand:

1. Before making any changes to the original Master File, make a copy of it with another

name.

2. Using an editor, make the desired edits to the copy of the Master File.

3.

Initiate the REBUILD facility by entering:

REBUILD

The following options are available:

1. REBUILD        (Optimize the database structure)
2. REORG          (Alter the database structure)
3. INDEX          (Build/modify the database index)
4. EXTERNAL INDEX (Build/modify an external index database)
5. CHECK          (Check the database structure)
6. TIMESTAMP      (Change the database timestamp)
7. DATE NEW       (Convert old date formats to smartdate formats)
8. MDINDEX        (Build/modify a multidimensional index)

4. Select the REORG subcommand by entering:

REORG or 2

The options are:

1. DUMP           (DUMP contents of the database)
2. LOAD           (LOAD data into the database)

5.

Initiate the DUMP phase of the procedure by entering:

DUMP or 1

6. Enter the name of the data source you wish to dump from. Be sure to use the name of the

original Master File for this phase.

On z/OS, enter the ddname.

On UNIX, Windows, and OpenVMS, enter filename. The data source to be rebuilt will be
referenced by a USE command. If no USE command is in effect, the data source will be
searched for using the EDAPATH variable.

7. You can specify selection tests by entering YES. Only data that meets your specifications
will be dumped. It is more likely, however, that you will want to dump the entire data
source. To do so, enter:

NO

Statistics appear during the DUMP procedure, including the number of segments dumped
and the name and statistics for the temporary file used to hold the data.

450

8. After the DUMP phase is complete, you are ready to begin the second phase of REBUILD

11. Creating and Rebuilding a Data Source

REORG: LOAD. Enter:

REBUILD

9. Select the REORG subcommand by entering:

REORG or 2

The options are:

1. DUMP     (DUMP contents of the database)
2. LOAD     (LOAD data into the database)

10. Initiate the LOAD phase of the procedure by entering:

LOAD or 2

11. Enter the name of the data source you wish to load from the temporary file created during

the dump phase. In most cases, this will be the new data source name.

At this stage, you have loaded the specified data from the original Master File into a new data
source with the name you specified. It is important to remember that both the Master File and
data source for the original Master File remain. You have three choices:

You may want to rename the original Master File and data source to prevent possible
confusion.

You may rename the new Master File and data source to the original name. As a result, any
existing FOCEXECs referencing the original name will run against the new data source.

You may delete the original Master File and data source after you verify that the new
Master File and data source are correct and complete.

On non-z/OS platforms, if you enter the name of a data source that already exists, (the original
Master File) you are prompted that you will be appending data to a preexisting data source and
asked if you wish to continue.

In z/OS, you are not asked if you want to append to an existing data source. The data source
is created. If you want to append, when you issue the LOAD command, enter LOAD NOCREATE.

Enter N to terminate REBUILD execution. Enter Y to add the records in the temporary REBUILD
file to the original FOCUS data source.

If duplicate field names occur in a Master File, REBUILD REORG is not supported.

In z/OS, you must issue either an allocation or a CREATE for a new data source being loaded.

Describing Data With TIBCO WebFOCUS® Language

 451

Changing Data Source Structure: The REORG Subcommand

Example:

Using the REORG Subcommand in Windows

The following procedure:

1.  COPY EMPLOYEE.FOC EMPOLD.FOC
2.  REBUILD
3.  REORG
4.  DUMP
5.  EMPLOYEE
6.  NO
7.  ERASE EMPLOYEE.FOC
8.  REBUILD
9.  REORG
10. LOAD
11. EMPLOYEE

1. Makes a copy of the data source.

2. Initiates the REBUILD facility.

3. Specifies the REORG subcommand.

4. Initiates the DUMP phase.

5. Specifies the name of the data source to dump.

6. Indicates that no record selection tests are required.

The data source will be dumped and the appropriate statistics will be generated.

7. Erases the EMPLOYEE data source.

8. Initiates the REBUILD facility.

9. Specifies the REORG subcommand.

10.Initiates the LOAD phase.

11.Specifies the name of the data source to load.

The data source will be loaded and the appropriate statistics will be generated.

452

11. Creating and Rebuilding a Data Source

Indexing Fields: The INDEX Subcommand

To index a field after you have entered data into the data source, use the INDEX subcommand.
You can index fields in addition to those previously specified in the Master File or since the
last REBUILD or CREATE command. The only requirement is that each field specified must be
described with the FIELDTYPE=I (or INDEX=I) attribute in the Master File.

The INDEX option uses the operating system sort program. You must have disk space to which
you can write. To calculate the amount of space needed, add 8 to the length of the index field
in bytes and multiply the sum by twice the number of segment instances

(LENGTH + 8) * 2n

where:

n

Is the number of segment instances.

You may decide to wait until after loading data to add the FIELDTYPE=I attribute and index the
field. This is because the separate processes of loading data and indexing can be faster than
performing both processes at the same time when creating the data source. This is especially
true for large data sources.

Sort libraries and workspace must be available. The REBUILD allocates default sort work space
in z/OS, if you have not already. DDNAMEs SORTIN and SORTOUT must be allocated prior to
issuing a REBUILD INDEX.

Describing Data With TIBCO WebFOCUS® Language

 453

Indexing Fields: The INDEX Subcommand

Procedure: How to Use the INDEX Subcommand

The following steps describe how to use the INDEX subcommand:

1. Add the FIELDTYPE=I attribute to the field or fields you are indexing in the Master File.

2.

Initiate the REBUILD facility by entering:

REBUILD

The following options are available:

1. REBUILD        (Optimize the database structure)
2. REORG          (Alter the database structure)
3. INDEX          (Build/modify the database index)
4. EXTERNAL INDEX (Build/modify an external index database)
5. CHECK          (Check the database structure)
6. TIMESTAMP      (Change the database timestamp)
7. DATE NEW       (Convert old date formats to smartdate formats)
8. MDINDEX        (Build/modify a multidimensional index)

3. Select the INDEX subcommand by entering:

INDEX or 3

4. Enter the name of the Master File in which you will add the FIELDTYPE=I or INDEX=I

attribute.

5. Enter the name of the field to index. If you are indexing all the fields that have

FIELDTYPE=I, enter an asterisk (*).

Statistics appear when the REBUILD INDEX procedure is complete, including the field names
that were indexed and the number of index values included.

Example:

Using the INDEX Subcommand in Windows

The following procedure:

1. REBUILD
2. INDEX
3. EMPLOYEE
4. EMP_ID

1. Initiates the REBUILD facility.

2. Specifies the INDEX subcommand.

3. Specifies the name of the Master File.

4. Specifies the name of the field to index.

The field will be indexed and the appropriate statistics will be generated.

454

Creating an External Index: The EXTERNAL INDEX Subcommand

11. Creating and Rebuilding a Data Source

Users with READ access to a local FOCUS data source can create an index database that
facilitates indexed retrieval when joining or locating records. An external index is a FOCUS data
source that contains index, field, and segment information for one or more specified FOCUS
data sources. The external index is independent of its associated FOCUS data source. External
indexes offer equivalent performance to permanent indexes for retrieval and analysis
operations.

External indexes enable indexing on concatenated FOCUS data sources, indexing on real and
defined fields, and indexing selected records from WHERE/IF tests. External indexes are
created as temporary data sets unless preallocated to a permanent data set. They are not
updated as the indexed data changes.

You create an external index with the REBUILD command. Internally, REBUILD begins a
process which reads the databases that make up the index, gathers the index information, and
creates an index database containing all field, format, segment, and location information.

You provide information about:

Whether you want to add new records from a concatenated database to the index
database.

The name of the external index database that you want to build.

The name of the data source from which the index information is obtained.

The name of the field from which the index is to be created.

Whether you want to position the index field within a particular segment.

Any valid WHERE or IF record selection tests.

Sort libraries and work space must be available. The REBUILD allocates default sort work
space in z/OS, if you have not already. DDNAMEs SORTIN and SORTOUT must be allocated
prior to issuing a REBUILD.

Describing Data With TIBCO WebFOCUS® Language

 455

Creating an External Index: The EXTERNAL INDEX Subcommand

Procedure: How to Use the EXTERNAL INDEX Subcommand

To create an external index from a concatenated database, follow these steps:

1. Assume that you have the following USE in effect:

USE CLEAR *
USE
EMPLOYEE
EMP2 AS EMPLOYEE
JOBFILE
EDUCFILE
END

Note that EMPLOYEE and EMP2 are concatenated and can be described by the EMPLOYEE
Master File.

2.

Initiate the REBUILD facility by entering:

REBUILD

The following options are available:

1. REBUILD        (Optimize the database structure)
2. REORG          (Alter the database structure)
3. INDEX          (Build/modify the database index)
4. EXTERNAL INDEX (Build/modify an external index database)
5. CHECK          (Check the database structure)
6. TIMESTAMP      (Change the database timestamp)
7. DATE NEW       (Convert old date formats to smartdate formats)
8. MDINDEX        (Build/modify a multidimensional index)

3. Select the EXTERNAL INDEX subcommand by entering:

EXTERNAL INDEX or 4

4. Specify whether to create a new index data source or add to an existing one by entering

one of the following choices:

NEW
ADD

For this example, assume you are creating a new index database and respond by entering:

NEW

5. Specify the name of the external index database:

EMPIDX

6. Specify the name of the data source from which the index records are obtained:

EMPLOYEE

456

11. Creating and Rebuilding a Data Source

7. Specify the name of the field to index:

CURR_JOBCODE

8. Specify whether the index should be associated with a particular field by entering YES or

NO. For this example, enter:

NO

9.

Indicate whether you require any record selection tests by entering YES or NO.

For this example, enter:

NO

If you responded YES, you would next enter the record selection tests, ending them with
the END command on a separate line.

For example:

IF DEPARTMENT EQ 'MIS'
END

You will see statistics (output of the ? FDT query) about the index data source when the
REBUILD EXTERNAL INDEX procedure is complete. This query is automatically issued at the
end of the REBUILD EXTERNAL INDEX process in order to validate the contents of the index
database.

Reference: Special Considerations for REBUILD EXTERNAL INDEX

Consider the following when working with external indexes:

Up to eight indexes can be activated at one time in a USE list using the WITH statement.
More than eight indexes may be activated in a session if you issue the USE CLEAR
command and issue new USE statements.

Up to 256 concatenated files may be indexed. However, only eight indexes may be
activated at one time.

Describing Data With TIBCO WebFOCUS® Language

 457

Creating an External Index: The EXTERNAL INDEX Subcommand

Verification of the component files is now done for both the date and time stamp of file
creation. Files with the same date and time stamp that are copied display the following
message:

(FOC995) ERROR. EXTERNAL INDEX DUPLICATE COMPONENT: fn REBUILD ABORTED

MODIFY may only use the external index with the FIND or LOOKUP functions. The external
index cannot be used as an entry point, such as:

MODIFY FILE filename.indexfld

Indexes may not be created on field names longer than twelve characters.

Text fields may not be used as indexed fields.

The USE options NEW, READ, ON, LOCAL, and AS master ON userid READ are not
supported for the external index database.

The external index database need not be allocated since CREATE FILE automatically
performs a temporary allocation. If a permanent database is required, then an allocation for
the index database must be in place prior to the REBUILD EXTERNAL INDEX command.

SORTIN and SORTOUT, work files that the REBUILD EXTERNAL INDEX process creates,
must be allocated with adequate space. In order to estimate the space needed, the
following formula may be used:

bytes = (field_length + 20) * number_of_occurrences

Concatenating Index Databases

The external index feature enables indexed retrieval from concatenated FOCUS data sources. If
you wish to concatenate databases that comprise the index, you must issue the appropriate
USE command prior to the REBUILD. The USE must include all cross-referenced and LOCATION
files. REBUILD EXTERNAL INDEX contains an add function that enables you to append only new
index records from a concatenated database to the index database, eliminating the need to
recreate the index database.

The original data source from which the index was built may not be in the USE list when you
add index records. If it is, REBUILD EXTERNAL INDEX generates the following message:

(FOC999) WARNING. EXTERNAL INDEX COMPONENT REUSED: ddname

458

Positioning Indexed Fields

11. Creating and Rebuilding a Data Source

The external index feature is useful for positioning retrieval of indexed values for defined fields
within a particular segment in order to enhance retrieval performance. By entering at a lower
segment within the hierarchy, data retrieved for the indexed field is affected, as the index field
is associated with data outside its source segment. This enables the creation of a relationship
between the source and target segments. The source segment is defined as the segment that
contains the indexed field. The target segment is defined as any segment above or below the
source segment within its path.

If the target segment is not within the same path, the following message is generated:

(FOC974) EXTERNAL INDEX ERROR. INVALID TARGET SEGMENT

A defined field may not be positioned at a higher segment.

While the source segment can be a cross-referenced or LOCATION segment, the target
segment cannot be a cross-referenced segment. If an attempt is made to place the target on a
cross-referenced segment, the following message is generated:

(FOC1000) INVALID USE OF CROSS REFERENCE FIELD

If you choose not to associate your index with a particular field, the source and target
segments will be the same.

Activating an External Index

After building an external index database, you must associate it with the data sources from
which it was created. This is accomplished with the USE command. The syntax is the same as
when USE is issued prior to building the external index database, except the WITH or INDEX
option is required.

Syntax:

How to Activate an External Index

USE  [ADD|REPLACE]
database_name [AS mastername]
index_database_name  [WITH|INDEX]  mastername   .
   .
   .
END

where:

ADD

Appends one or more new databases to the present USE list. Without the ADD option, the
existing USE list is cleared and replaced by the current list of USE databases.

Describing Data With TIBCO WebFOCUS® Language

 459

Checking Data Source Integrity: The CHECK Subcommand

REPLACE

Replaces an existing database_name in the USE list.

database_name

Is the name of the data source.

On z/OS, enter the ddname.

On UNIX, Windows, and OpenVMS, enter filename. The data source to be rebuilt will be
referenced by a USE command. If no USE command is in effect, the data source will be
searched for using the EDAPATH variable.

You must include a data source name in the USE list for all cross-referenced and
LOCATION files that are specified in the Master File.

AS

Is used with a Master File name to concatenate data sources.

mastername

Specifies the Master File.

index_database_name

Is the name of the external index database.

On z/OS, enter the ddname.

On UNIX, Windows, and OpenVMS, enter [pathname]filename.foc. The data source to be
rebuilt will be referenced by a USE command. If no USE command is in effect, the data
source will be searched for using the EDAPATH variable.

WITH|INDEX

Is a keyword that creates the relationship between the component data sources and the
index database. INDEX is a synonym for WITH.

Checking Data Source Integrity: The CHECK Subcommand

It is rare for the structural integrity of a FOCUS data source to be damaged. Structural damage
will occasionally occur, however, during a drive failure or if an incorrect Master File is used. In
this situation, the REBUILD CHECK command performs two essential tasks:

It checks pointers in the data source.

Should it encounter an error, it displays a message and attempts to branch around the
offending segment or instance.

460

11. Creating and Rebuilding a Data Source

Although CHECK is able to report on a good deal of data that would otherwise be lost, it is
important to remember that frequently backing up your FOCUS data sources is the best
method of preventing data loss.

CHECK will occasionally fail to uncover structural damage. If you have reason to believe that
there is damage to your data source, though CHECK reports otherwise, there is a second
method of checking data source integrity. This method entails using the ? FILE and TABLEF
commands. Though this is not a REBUILD function, it is included at the end of this section
because of its relevancy to CHECK.

Procedure: How to Use the CHECK Subcommand

The following steps describe how to use the CHECK subcommand:

1.

Initiate the REBUILD facility by entering:

REBUILD

The following options are available:

1. REBUILD        (Optimize the database structure)
2. REORG          (Alter the database structure)
3. INDEX          (Build/modify the database index)
4. EXTERNAL INDEX (Build/modify an external index database)
5. CHECK          (Check the database structure)
6. TIMESTAMP      (Change the database timestamp)
7. DATE NEW       (Convert old date formats to smartdate formats)
8. MDINDEX        (Build/modify a multidimensional index)

2. Select the CHECK subcommand by entering:

CHECK or 5

3. Enter the name of the data source to be checked.

On z/OS, enter the ddname.

On UNIX, Windows, and OpenVMS, enter filename. The data source to be rebuilt will be
referenced by a USE command. If no USE command is in effect, the data source will be
searched for using the EDAPATH variable.

Statistics appear during the REBUILD CHECK procedure:

If no errors are found, the statistics indicate the number of segments retrieved.

If errors are found, the statistics indicate the type and location of each error:

Describing Data With TIBCO WebFOCUS® Language

 461

Checking Data Source Integrity: The CHECK Subcommand

DELETE indicates that the data has been deleted and should not have been retrieved.

OFFPAGE indicates that the address of the data is not on a page owned by this segment.

INVALID indicates that the type of linkage cannot be identified. It may be a destroyed
portion of the data source.

Example:

Using the Check Subcommand (File Undamaged) in Windows

The following procedure:

1. REBUILD
2. CHECK
3. EMPLOYEE

1. Initiates the REBUILD facility.

2. Specifies the CHECK subcommand.

3. Provides the name of the data source to check.

The data source will be checked and the appropriate statistics will be generated.

Confirming Structural Integrity Using ? FILE and TABLEF

When you believe that there is damage to your data source, though REBUILD CHECK reports
there is not, use the ? FILE and TABLEF commands to compare the number of segment
instances reported after invoking each command. A disparity indicates a structural problem.

Procedure: How to Verify REBUILD CHECK Using ? FILE and TABLEF

1.

Issue the following command:

? FILE filename

where:

filename

Is the name of the FOCUS data source you are examining.

A report displays information on the status of the data source. The number of instances
for each segment is listed in the ACTIVE COUNT column.

2. To ensure that the TABLEF command in the next step counts all segment instances,

including those in the short paths, issue the command:

SET ALL = ON

462

11. Creating and Rebuilding a Data Source

3. Enter:

TABLEF FILE filenameCOUNT field1 field2END

where:

filename

Is the name of the Master File of the FOCUS data source.

field1...

Are the names of fields in the data source. Name one field from each segment. It
does not matter which field is named in the segment.

The report produced shows the number of field occurrences for those fields named and
thus the number of segment instances for each segment. These numbers should match
their respective segment instance numbers shown in the ? FILE command (except for
unique segments which the TABLEF command shows to have as many instances in the
parent segment). If the numbers do not match, or if either the ? FILE command or TABLEF
command ends abnormally, the data source is probably damaged.

Example:

Checking the Integrity of the EMPLOYEE Data Source

User input is shown in bold. Computer responses are in uppercase:

? FILE
STATUS OF FOCUS FILE: c:employee.foc   ON 01/31/2003 AT 16.17.32
                ACTIVE  DELETED    DATE OF    TIME OF    LAST TRANS
SEGNAME         COUNT   COUNT      LAST CHG   LAST CHG   NUMBER

EMPINFO           12             05/13/1999   16.17.22      448
FUNDTRAN           6             05/13/1999   16.17.22       12
PAYINFO           19             05/13/1999   16.17.22       19
ADDRESS           21             05/13/1999   16.17.22       21
SALINFO           70             05/13/1999   16.17.22      448
DEDUCT           448             05/13/1999   16.17.22      448
TOTAL SEGS       576
TOTAL CHAR      8984
TOTAL PAGES        8
LAST CHANGE                      05/13/1999   16.17.22      448
SET ALL = ON
TABLEF FILE EMPLOYEE
COUNT EMP_ID BANK_NAME DAT_INC TYPE PAY_DATE DED_CODE
END

PAGE     1

 EMP_ID  BANK_NAME  DAT_INC  TYPE   PAY_DATE  DED_CODE
 COUNT   COUNT      COUNT    COUNT  COUNT     COUNT
 ------  ---------  -------  -----  --------  --------
     12         12       19     21        70       448
NUMBER OF RECORDS IN TABLE=      488 LINES= 1

Describing Data With TIBCO WebFOCUS® Language

 463




Changing the Data Source Creation Date and Time: The TIMESTAMP Subcommand

Note that the BANK_NAME count in the TABLEF report is different than the number of
FUNDTRAN instances reported by the ? FILE query. This is because FUNDTRAN is a unique
segment and is always considered present as an extension of its parent.

Changing the Data Source Creation Date and Time: The TIMESTAMP Subcommand

A FOCUS data source date and time stamp are updated each time the data source is changed
by CREATE, REBUILD, Maintain, or MODIFY. You can update a data source date and time
stamp without making changes to the data source by using REBUILD TIMESTAMP
subcommand.

Procedure: How to Use the TIMESTAMP Subcommand

The following steps describe how to use the TIMESTAMP subcommand:

1.

Initiate the REBUILD facility by entering:

REBUILD

The following options are available:

1. REBUILD        (Optimize the database structure)
2. REORG          (Alter the database structure)
3. INDEX          (Build/modify the database index)
4. EXTERNAL INDEX (Build/modify an external index database)
5. CHECK          (Check the database structure)
6. TIMESTAMP      (Change the database timestamp)
7. DATE NEW       (Convert old date formats to smartdate formats)
8. MDINDEX        (Build/modify a multidimensional index)

2. Select the TIMESTAMP subcommand by entering:

TIMESTAMP or 6

3. Enter the name of the data source whose date and time stamp is to be updated.

On z/OS, enter the ddname.

On UNIX, Windows, and OpenVMS, enter filename. The data source to be rebuilt will be
referenced by a USE command. If no USE command is in effect, the data source will be
searched for using the EDAPATH variable.

464

11. Creating and Rebuilding a Data Source

4. Enter one of the following options for the source of the date and time:

T (today's date). Updates the data source date and time stamp with the current date and
time.

D (search file for date). Updates the data source date and time stamp with the last date
and time at which the data source was actually changed. Each page of the data source is
scanned and the most recent date and time recorded for a page is applied to the data
source. This is the same as issuing the ? FILE query, and can be time consuming when
the data source is very large. This option is used to keep an external index database
synchronized with its component data source.

MMDDYY HHMMSS. Is a date and time that you specify, which REBUILD will use to update
the data source date and time stamp. The date and time that you enter must have the
format mmddyy hhmmss or mmddyyyy hhmmss. There must be a space between the date
and the time. If you use two digits for the year, REBUILD uses the values for DEFCENT and
YRTHRESH to determine the century.

If you supply an invalid date or time, the following message appears:

(FOC961) INVALID DATE INPUT IN REBUILD TIME:

Converting Legacy Dates: The DATE NEW Subcommand

The REBUILD subcommand DATE NEW converts legacy dates (alphanumeric, integer, and
packed-decimal fields with date display options) to smart dates (fields in date format) in your
FOCUS data sources.

The utility uses update-in-place technology. It updates your data source and creates a new
Master File, yet does not change the structure or size of the data source. You must back up
the data source before executing REBUILD with the DATE NEW subcommand. We recommend
that you run the utility against the copy and then replace the original file with the updated
backup.

How DATE NEW Converts Legacy Dates

REBUILD DATE NEW subcommand overwrites the original legacy date field (an alphanumeric,
integer, or packed-decimal field with date display options) with a smart date (a field in date
format). When the storage size of the legacy date exceeds four bytes (the storage size of a
smart date), a pad field is added to the data source following the date field:

Formats A6YMD, A6MDY, and A6DMY are changed to formats YMD, MDY, and DMY,
respectively, and have a 2-byte pad field added to the Master File.

Describing Data With TIBCO WebFOCUS® Language

 465

Converting Legacy Dates: The DATE NEW Subcommand

The storage size of integer dates (I6YMD, I6MDY, for example) is 4 bytes, so no pad field is
added.

All packed fields and A8 dates add a 4-byte pad field.

When a date is a key field (but not the last key for the segment), and it requires a pad field,
the number of keys in the SEGTYPE is increased by one for each date field that requires
padding.

DATE NEW only changes legacy dates to smart dates. The field format in the Master File must
be one of the following (month translation edit options T and TR may be included in the
format):

A8YYMD A8MDYY A8DMYY A6YMD A6MDY A6DMY A6YYM A6MYY A4YM A4MY

I8YYMD I8MDYY I8DMYY I6YMD I6MDY I6DMY I6YYM I6MYY I4YM I4MY

P8YYMD P8MDYY P8DMYY P6YMD P6MDY P6DMY P6YYM P6MYY P4YM P4MY

If you have a field that stores date values but does not have one of these formats, DATE NEW
does not change it. If you have a field with one of these formats that you do not want changed,
temporarily remove the date edit options from the format, run REBUILD DATE NEW, and then
restore the edit options to the format.

Reference: DATE NEW Usage Notes

The DBA password for the data source must be issued prior to issuing REBUILD.

The original Master File cannot be encrypted.

All files must be available locally during the REBUILD, including LOCATION files.

The Master File cannot have GROUP fields.

Some error numbers are available in &FOCERRNUM while all error numbers are available in
&&FOCREBUILD. Test both &&FOCREBUILD and &FOCERRNUM for errors when writing
procedures to rebuild your data sources.

To avoid any potential problems, clear all LETs and JOINs before issuing REBUILD.

DEFCENT/YRTHRESH are respected at the global, data source, and field level.

Correct all invalid date values in the data source before executing REBUILD/DATE NEW. The
utility converts all invalid dates to zero. Invalid dates used as keys may lead to duplicate
keys in the data source.

466

11. Creating and Rebuilding a Data Source

Adequate workspace must be available for the temporary REBUILD file. As a rule of thumb,
have space 10 to 20% larger than the size of the existing file available.

REBUILD/INDEX is performed automatically if an index exists.

REBUILD/REBUILD is performed automatically after REBUILD/DATE NEW when any key is a
date.

Sort libraries and work space must be available (as with REBUILD/INDEX). The REBUILD
allocates default sort work space in z/OS, if you have not already. DDNAMEs SORTIN and
SORTOUT must be allocated prior to issuing a REBUILD.

What DATE NEW Does Not Convert

The REBUILD DATE NEW subcommand is a remediation tool for your FOCUS data sources and
date fields only. It does not remediate:

DEFINE attributes in the Master File.

ACCEPT attributes in the Master File.

DBA restrictions (for example, VALUE restrictions) in the Master File or central security
repository (DBAFILE).

Cross-references to other date fields in this or other Master Files.

Any references to date fields in your FOCEXEC.

Example:

Using the DATE NEW Subcommand in Windows

The following procedure:

1. SET DFC = 19, YRT = 50
2. REBUILD
3. DATE NEW
4. NEWEMP.MAS
5. YES

1. Sets the DEFCENT and YRTHRESH parameters that determine which century to use for

each date.

2. Initiates the REBUILD facility.

3. Specifies the DATE NEW subcommand.

4. Provides the name of the Master File that specifies the dates to convert.

5. Indicates that the data source has been backed up.

Describing Data With TIBCO WebFOCUS® Language

 467

Converting Legacy Dates: The DATE NEW Subcommand

The dates will be converted and the appropriate statistics will be generated, including the
number of segments changed.

The new Master File is an updated copy of the original Master File except that:

The USAGE format for legacy date fields is updated to remove the format and length. The
date edit options are retained. For example, A6YMDTR becomes YMDTR.

Padding fields are added for those dates that need them:

FIELDNAME= ,ALIAS= ,FORMAT=An,$ PAD FIELD ADDED BY REBUILD

where:

n

Is the padding length (either 2 or 4). Note that the FIELDNAME and ALIAS are blank.

The SEGTYPE attribute is updated for segments that have remediated dates as keys when
the date requires padding and the date is not the last field in the key. The SEGTYPE
number will be increased by the number of pad fields added to the key.

If the SEGTYPE is missing for any segment, the following line is added immediately prior to
the $ terminator for that segment:

SEGTYPE=segtype,$ OMITTED SEGTYPE ADDED BY REBUILD

where:

segtype

Is determined by REBUILD.

If the USAGE attribute for any field (including date fields) is missing, the following line is
added, immediately prior to the $ terminator for that field:

USAGE=fmt,$ OMITTED USAGE ADDED BY REBUILD

where:

fmt

Is the format of the previous field in the Master File. REBUILD automatically assigns
the previous field format to any field coded without an explicit USAGE= statement.

468

11. Creating and Rebuilding a Data Source

Using the New Master File Created by DATE NEW

REBUILD DATE NEW subcommand creates an updated Master File that reflects the changes
made to the data source. Once the data source has been rebuilt, the original Master File can
no longer be used against the data source. You must use the new Master File created by the
DATE NEW subcommand.

Example:

Sample Master File: Before and After Conversion by DATE NEW

Before Conversion

FILE=filename

After Conversion

FILE=filename

SEGNAME=segname, SEGTYPE=S2

SEGNAME=segname, SEGTYPE=S3

FIELD=KEY1,,USAGE=A6YMD,$

FIELD=KEY1,,USAGE= YMD,$

FIELD=, ,USAGE=A2,$ PAD FIELD
ADDED BY REBUILD

FIELD=KEY2,,USAGE=I6MDY,$

FIELD=KEY2,,USAGE= MDY,$

FIELD=FIELD3,,USAGE=A8YYMD,$

FIELD=FIELD3,,USAGE= YYMD,$

FIELD=, ,USAGE=A4,$ PAD FIELD
ADDED BY REBUILD

When REBUILD DATE NEW subcommand converts this Master File:

The SEGTYPE changes from an S2 to S3 to incorporate a 2-byte pad field.

Format A6YMD changes to smart date format YMD.

A 2-byte pad field with a blank field name and alias is added to the Master File.

Format I6MDY changes to smart date format MDY (no padding needed).

Format A8YYMD changes to smart date format YYMD.

A 4-byte pad field with a blank field name and alias is added to the Master File.

Describing Data With TIBCO WebFOCUS® Language

 469

Creating a Multi-Dimensional Index: The MDINDEX Subcommand

Action Taken on a Date Field During REBUILD/DATE NEW

REBUILD/DATE NEW performs a REBUILD/REBUILD or REBUILD/INDEX automatically when a
date field is a key or a date field is indexed. The following chart shows the action taken on a
date field during the REBUILD/DATE NEW process.

Date Is a Key

Index

Result

No

No

Yes

Yes

None

Yes

None

On any
field

NUMBER OF SEGMENTS CHANGED = n

REBUILD/INDEX on date field.

REBUILD/REBUILD is performed.

REBUILD/REBUILD is performed.

REBUILD/INDEX is performed for the indexed fields.

Creating a Multi-Dimensional Index: The MDINDEX Subcommand

The MDINDEX subcommand is used to create or maintain a multi-dimensional index. For more
information, see Building and Maintaining a Multi-Dimensional Index on page 338.

470

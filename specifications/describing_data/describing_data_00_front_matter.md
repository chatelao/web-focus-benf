TIBCO WebFOCUS®

Describing Data With TIBCO WebFOCUS®
Language

Release 8207
March 2021
DN4501688.0321

Copyright© 2021.TIBCOSoftwareInc.AllRightsReserved. Contents

1. Understanding a Data Source Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

A Note About Data Source Terminology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

What Is a Data Source Description? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .18

How an Application Uses a Data Source Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .19

What Does a Master File Describe? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

Identifying a Data Source. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

Identifying and Relating a Group of Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

Describing a Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

Creating a Data Source Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

Creating a Master File and Access File Using an Editor. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

Naming a Master File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

Using Long Master File Names on z/OS. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

Member Names for Long Master File Names in z/OS. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

What Is in a Master File? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

Improving Readability. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27

Adding a Comment. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

Editing and Validating a Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

2. Identifying a Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

Identifying a Data Source Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .31

Specifying a Data Source Name: FILENAME . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

Identifying a Data Source Type: SUFFIX . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

Specifying a Code Page in a Master File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36

Specifying Byte Order . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

Specifying Data Type: IOTYPE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

Providing Descriptive Information for a Data Source: REMARKS . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38

Specifying a Physical File Name: DATASET . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39

DATASET Behavior in a FOCUS Data Source. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39

DATASET Behavior in a Fixed-Format Sequential Data Source. . . . . . . . . . . . . . . . . . . . . . . . . .43

DATASET Behavior in a VSAM Data Source. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45

Creating and Using a Master File Profile . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

Storing Localized Metadata in Language Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58

LNGPREP Utility: Preparing Metadata Language Files. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .58

Describing Data With TIBCO WebFOCUS® Language

 3

Contents

LNGPREP Modes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

3. Describing a Group of Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65

Defining a Single Group of Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65

Understanding a Segment. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .66

Understanding a Segment Instance. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .66

Understanding a Segment Chain. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67

Identifying a Key Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68

Identifying a Segment: SEGNAME. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68

Identifying a Logical View: Redefining a Segment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .69

Relating Multiple Groups of Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71

Facilities for Specifying a Segment Relationship. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71

Identifying a Parent Segment: PARENT. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72

Identifying the Type of Relationship: SEGTYPE. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73

Understanding the Efficiency of the Minimum Referenced Subtree. . . . . . . . . . . . . . . . . . . . . 73

Logical Dependence: The Parent-Child Relationship . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74

A Simple Parent-Child Relationship. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74

A Parent-Child Relationship With Multiple Segments. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75

Understanding a Root Segment. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76

Understanding a Descendant Segment. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .76

Understanding an Ancestral Segment. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77

Logical Independence: Multiple Paths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78

Understanding a Single Path. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .78

Understanding Multiple Paths. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .79

Understanding Logical Independence. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80

Cardinal Relationships Between Segments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80

One-to-One Relationship . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .81

Where to Use a One-to-One Relationship. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82

Implementing a One-to-One Relationship in a Relational Data Source. . . . . . . . . . . . . . . . . . .83

Implementing a One-to-One Relationship in a Sequential Data Source. . . . . . . . . . . . . . . . . . 83

Implementing a One-to-One Relationship in a FOCUS Data Source. . . . . . . . . . . . . . . . . . . . . 83

One-to-Many Relationship . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83

Implementing a One-to-Many Relationship in a Relational Data Source. . . . . . . . . . . . . . . . . .85

4

Contents

Implementing a One-to-Many Relationship in a VSAM or Sequential Data Source. . . . . . . . . 85

Implementing a One-to-Many Relationship in a FOCUS Data Source. . . . . . . . . . . . . . . . . . . . 86

Many-to-Many Relationship . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .86

Implementing a Many-to-Many Relationship Directly. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86

Implementing a Many-to-Many Relationship Indirectly. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .88

Recursive Relationships . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91

Relating Segments From Different Types of Data Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95

Rotating a Data Source: An Alternate View . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96

Defining a Prefix for Field Titles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98

4. Describing an Individual Field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103

Field Characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103

The Field Name: FIELDNAME . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104

Using a Qualified Field Name. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106

Using a Duplicate Field Name. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108

Rules for Evaluating a Qualified Field Name. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108

The Field Synonym: ALIAS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112

Implementing a Field Synonym. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .112

The Displayed Data Type: USAGE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113

Specifying a Display Format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113

Data Type Formats. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .114

Integer Format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115

Floating-Point Double-Precision Format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .116

Floating-Point Single-Precision Format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117

Extended Decimal Precision Floating-Point Format (XMATH). . . . . . . . . . . . . . . . . . . . . . . . . . 118

Decimal Precision Floating-Point Format (MATH). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119

Packed-Decimal Format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .120

Numeric Display Options. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .121

Using International System (SI) Numeric Format Abbreviation Options. . . . . . . . . . . . . . . . . 127

Extended Currency Symbol Display Options. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .129

Rounding. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135

Alphanumeric Format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .137

Hexadecimal Format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138

Describing Data With TIBCO WebFOCUS® Language

 5

Contents

String Format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 139

Date Formats. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140

Date Display Options. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140

Controlling the Date Separator. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .145

Date Translation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .146

Using a Date Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147

Numeric Date Literals. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148

Date Fields in Arithmetic Expressions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .149

Converting a Date Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149

How a Date Field Is Represented Internally. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .150

Displaying a Non-Standard Date Format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 152

Date Format Support. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .153

Alphanumeric and Numeric Formats With Date Display Options. . . . . . . . . . . . . . . . . . . . . . .153

Date-Time Formats. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .154

Describing a Date-Time Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156

Character Format AnV. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166

Text Field Format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169

The Stored Data Type: ACTUAL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .170

ACTUAL Attribute. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170

Adding a Geographic Role for a Field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175

GEOGRAPHIC_ROLE Attribute. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 175

Null or MISSING Values: MISSING . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176

Using a Missing Value. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178

Describing an FML Hierarchy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178

Defining a Dimension: WITHIN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .181

Validating Data: ACCEPT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 186

Specifying Acceptable Values for a Dimension . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 190

Alternative Report Column Titles: TITLE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191

Documenting the Field: DESCRIPTION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193

Multilingual Metadata . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 194

Placing Multilingual Metadata Directly in a Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 196

Describing a Virtual Field: DEFINE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .200

Using a Virtual Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 203

6

Contents

Describing a Calculated Value: COMPUTE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .204

Describing a Filter: FILTER . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208

Describing a Sort Object: SORTOBJ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213

Calling a DEFINE FUNCTION in a Master File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .216

Using Date System Amper Variables in Master File DEFINEs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .217

Parameterizing Master and Access File Values Using Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . 220

Converting Alphanumeric Dates to WebFOCUS Dates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 223

Specifying Variables in a Date Pattern. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224

Specifying Constants in a Date Pattern. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226

Sample Date Patterns. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226

5. Describing a Sequential, VSAM, or ISAM Data Source . . . . . . . . . . . . . . . . . . . . . . . . . 231

Sequential Data Source Formats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232

What Is a Fixed-Format Data Source?. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 232

What Is a Comma or Tab-Delimited Data Source?. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 234

What Is a Free-Format Data Source?. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .236

Rules for Maintaining a Free-Format Data Source. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .237

Standard Master File Attributes for a Sequential Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . .238

Standard Master File Attributes for a VSAM or ISAM Data Source . . . . . . . . . . . . . . . . . . . . . . . . . 238

Describing a Group Field With Formats. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .239

Describing a Group Field as a Set of Elements. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241

Describing a Multiply Occurring Field in a Free-Format Data Source . . . . . . . . . . . . . . . . . . . . . . . . 244

Describing a Multiply Occurring Field in a Fixed-Format, VSAM, or ISAM Data Source . . . . . . . . . 245

Using the OCCURS Attribute. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .246

Describing a Parallel Set of Repeating Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247

Describing a Nested Set of Repeating Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .248

Using the POSITION Attribute. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251

Specifying the ORDER Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253

Redefining a Field in a Non-FOCUS Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 254

Extra-Large Record Length Support . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .256

Describing Multiple Record Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .257

SEGTYPE Attributes With RECTYPE Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258

Describing a RECTYPE Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258

Describing Data With TIBCO WebFOCUS® Language

 7

Contents

Describing Positionally Related Records. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260

Ordering of Records in the Data Source. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261

Describing Unrelated Records. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 264

Using a Generalized Record Type. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267

Using an ALIAS in a Report Request. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 270

Combining Multiply Occurring Fields and Multiple Record Types . . . . . . . . . . . . . . . . . . . . . . . . . . . 271

Describing a Multiply Occurring Field and Multiple Record Types. . . . . . . . . . . . . . . . . . . . . . 272

Describing a VSAM Repeating Group With RECTYPEs. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274

Describing a Repeating Group Using MAPFIELD. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 275

Establishing VSAM Data and Index Buffers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .278

Using a VSAM Alternate Index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279

Describing a Token-Delimited Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .282

Defining a Delimiter in the Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 282

Defining a Delimiter in the Access File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .285

6. Describing a FOCUS Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 293

Types of FOCUS Data Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 294

Using a SUFFIX=FOC Data Source. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 294

Using an XFOCUS Data Source. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 294

Designing a FOCUS Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 297

Data Relationships. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .297

Join Considerations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 298

General Efficiency Considerations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 298

Changing a FOCUS Data Source. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 299

Describing a Single Segment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .299

Describing Keys, Sort Order, and Segment Relationships: SEGTYPE. . . . . . . . . . . . . . . . . . 300

Describing a Key Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 302

Describing Sort Order. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 302

Understanding Sort Order. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .303

Describing Segment Relationships. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 304

Storing a Segment in a Different Location: LOCATION. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .304

Separating Large Text Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 306

Limits on the Number of Segments, LOCATION Files, Indexes, and Text Fields. . . . . . . . . .307

8

Contents

Specifying a Physical File Name for a Segment: DATASET. . . . . . . . . . . . . . . . . . . . . . . . . . . .308

Timestamping a FOCUS Segment: AUTODATE. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .311

GROUP Attribute . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 313

Describing a Group Field With Formats. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .313

Describing a Group Field as a Set of Elements. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 317

ACCEPT Attribute . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 320

INDEX Attribute . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 321

Joins and the INDEX Attribute. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 322

FORMAT and MISSING: Internal Storage Requirements. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .324

Describing a Partitioned FOCUS Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 324

Intelligent Partitioning. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 325

Specifying an Access File in a FOCUS Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 325

FOCUS Access File Attributes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .328

Multi-Dimensional Index (MDI) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .333

Specifying an MDI in the Access File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 333

Creating a Multi-Dimensional Index. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 336

Choosing Dimensions for Your Index. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 336

Building and Maintaining a Multi-Dimensional Index. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .338

Using a Multi-Dimensional Index in a Query. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .339

Querying a Multi-Dimensional Index. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 339

Using AUTOINDEX to Choose an MDI. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 340

Joining to a Multi-Dimensional Index. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .342

Encoding Values in a Multi-Dimensional Index. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 345

Partitioning a Multi-Dimensional Index. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 347

Querying the Progress of a Multi-Dimensional Index. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .347

Displaying a Warning Message. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 348

7. Defining a Join in a Master File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 349

Join Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .349

Static Joins Defined in the Master File: SEGTYPE = KU and KM . . . . . . . . . . . . . . . . . . . . . . . . . . .350

Describing a Unique Join: SEGTYPE = KU. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 350

Using a Unique Join for Decoding. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 354

Describing a Non-Unique Join: SEGTYPE = KM. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 354

Describing Data With TIBCO WebFOCUS® Language

 9

Contents

Using Cross-Referenced Descendant Segments: SEGTYPE = KL and KLU . . . . . . . . . . . . . . . . . . .356

Hierarchy of Linked Segments. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 362

Dynamic Joins Defined in the Master File: SEGTYPE = DKU and DKM . . . . . . . . . . . . . . . . . . . . . .362

Conditional Joins in the Master File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 364

Comparing Static and Dynamic Joins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 367

Joining to One Cross-Referenced Segment From Several Host Segments . . . . . . . . . . . . . . . . . . . 368

Joining From Several Segments in One Host Data Source. . . . . . . . . . . . . . . . . . . . . . . . . . . 369

Joining From Several Segments in Several Host Data Sources: Multiple Parents. . . . . . . .371

Recursive Reuse of a Segment. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 373

Creating a Single-Root Cluster Master File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 374

Reading a Field Containing Delimited Values as individual Rows . . . . . . . . . . . . . . . . . . . . . 374

Creating a Multiple-Root Cluster Master File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .378

8. Creating a Business View of a Master File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 383

Grouping Business Logic In a Business View . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 383

Business View DV Roles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 392

Assigning DV Roles. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 392

9. Checking and Changing a Master File: CHECK . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 395

Checking a Data Source Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 395

CHECK Command Display . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 396

Determining Common Errors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 398

PICTURE Option . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .399

HOLD Option . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 401

Specifying an Alternate File Name With the HOLD Option. . . . . . . . . . . . . . . . . . . . . . . . . . . . 404

TITLE, HELPMESSAGE, and TAG Attributes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 404

Virtual Fields in the Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 404

10. Providing Data Source Security: DBA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .405

Introduction to Data Source Security . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 405

Implementing Data Source Security . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 406

Identifying the DBA: The DBA Attribute. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .408

Including the DBA Attribute in a HOLD File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .409

Identifying Users With Access Rights: The USER Attribute. . . . . . . . . . . . . . . . . . . . . . . . . . . 409

Non-Overridable User Passwords (SET PERMPASS). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 410

10

Contents

Controlling Case Sensitivity of Passwords. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 412

Establishing User Identity. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .413

Specifying an Access Type: The ACCESS Attribute . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .414

Types of Access. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 415

Limiting Data Source Access: The RESTRICT Attribute . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 417

Restricting Access to a Field or a Segment. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 420

Restricting Access to a Value. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .422

Restricting Both Read and Write Values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .424

Controlling the Source of Access Restrictions in a Multi-file Structure . . . . . . . . . . . . . . . . . . . . . . 424

Adding DBA Restrictions to the Join Condition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 428

Placing Security Information in a Central Master File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 428

File Naming Requirements for DBAFILE. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 433

Connection to an Existing DBA System With DBAFILE. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 433

Combining Applications With DBAFILE. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 434

Summary of Security Attributes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .434

Hiding Restriction Rules: The ENCRYPT Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 436

Encrypting Data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 436

Performance Considerations for Encrypted Data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .437

Setting a Password Externally. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 438

FOCEXEC Security . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 438

Encrypting and Decrypting a FOCEXEC. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 438

11. Creating and Rebuilding a Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 441

Creating a New Data Source: The CREATE Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 442

Rebuilding a Data Source: The REBUILD Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 444

Controlling the Frequency of REBUILD Messages. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 446

Optimizing File Size: The REBUILD Subcommand . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .447

Changing Data Source Structure: The REORG Subcommand . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .449

Indexing Fields: The INDEX Subcommand . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .453

Creating an External Index: The EXTERNAL INDEX Subcommand . . . . . . . . . . . . . . . . . . . . . . . . . . 455

Concatenating Index Databases. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 458

Positioning Indexed Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 459

Activating an External Index. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 459

Describing Data With TIBCO WebFOCUS® Language

 11

Contents

Checking Data Source Integrity: The CHECK Subcommand . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 460

Confirming Structural Integrity Using ? FILE and TABLEF. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 462

Changing the Data Source Creation Date and Time: The TIMESTAMP Subcommand . . . . . . . . . .464

Converting Legacy Dates: The DATE NEW Subcommand . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 465

How DATE NEW Converts Legacy Dates. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 465

What DATE NEW Does Not Convert. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 467

Using the New Master File Created by DATE NEW. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 469

Action Taken on a Date Field During REBUILD/DATE NEW. . . . . . . . . . . . . . . . . . . . . . . . . . . 470

Creating a Multi-Dimensional Index: The MDINDEX Subcommand . . . . . . . . . . . . . . . . . . . . . . . . . .470

A. Master Files and Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .471

EMPLOYEE Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 471

EMPLOYEE Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 473

EMPLOYEE Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 474

JOBFILE Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 474

JOBFILE Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 475

JOBFILE Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .475

EDUCFILE Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 476

EDUCFILE Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 476

EDUCFILE Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 477

SALES Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .477

SALES Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 478

SALES Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 479

CAR Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .479

CAR Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 481

CAR Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 482

LEDGER Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 482

LEDGER Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .483

LEDGER Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .483

FINANCE Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .483

FINANCE Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 483

FINANCE Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 484

REGION Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 484

12

Contents

REGION Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 484

REGION Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 484

EMPDATA Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 485

EMPDATA Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 485

EMPDATA Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 485

TRAINING Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 485

TRAINING Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 486

TRAINING Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 486

COURSE Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 486

COURSE Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 486

COURSE Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 487

JOBHIST Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 487

JOBHIST Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 487

JOBHIST Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 487

JOBLIST Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 487

JOBLIST Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .488

JOBLIST Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .488

LOCATOR Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 488

LOCATOR Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .488

LOCATOR Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 489

PERSINFO Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 489

PERSINFO Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 489

PERSINFO Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 489

SALHIST Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 490

SALHIST Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 490

SALHIST Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 490

VIDEOTRK, MOVIES, and ITEMS Data Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .490

VIDEOTRK Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .491

VIDEOTRK Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 492

MOVIES Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 493

MOVIES Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .493

ITEMS Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 493

ITEMS Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 494

Describing Data With TIBCO WebFOCUS® Language

 13

Contents

VIDEOTR2 Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 494

VIDEOTR2 Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 494

VIDEOTR2 Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 495

Gotham Grinds Data Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 495

GGDEMOG Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 496

GGDEMOG Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 497

GGORDER Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .497

GGORDER Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 498

GGPRODS Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .498

GGPRODS Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 499

GGSALES Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 499

GGSALES Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 500

GGSTORES Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 500

GGSTORES Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 500

Century Corp Data Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 501

CENTCOMP Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 502

CENTCOMP Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .502

CENTFIN Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 503

CENTFIN Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 503

CENTHR Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .504

CENTHR Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 506

CENTINV Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 507

CENTINV Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 507

CENTORD Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 508

CENTORD Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 509

CENTQA Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .510

CENTQA Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .511

CENTGL Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 511

CENTGL Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .512

CENTSYSF Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .512

CENTSYSF Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 512

CENTSTMT Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 513

CENTSTMT Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 514

14

Contents

CENTGLL Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 514

CENTGLL Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .515

B. Error Messages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 517

Displaying Messages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 517

C. Rounding in WebFOCUS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 519

Data Storage and Display . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 519

Integer Fields: Format I. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 520

Floating-Point Fields: Formats F and D. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 521

Decimal Floating-Point Fields: Formats M and X. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 521

Packed Decimal Format: Format P. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .522

Rounding in Calculations and Conversions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 524

DEFINE and COMPUTE. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .528

Legal and Third-Party Notices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 531

Describing Data With TIBCO WebFOCUS® Language

 15

Contents

16

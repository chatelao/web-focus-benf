Creating Reports With
TIBCO® WebFOCUS Language

Release 8207
May 2021
DN4501639.0521

TIBCO WebFOCUS®Copyright© 2021.TIBCOSoftwareInc.AllRightsReserved. Contents

1. Creating Reports Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .29

Requirements for Creating a Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

Report Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .30

Developing Your Report Request . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .32

Starting a Report Request. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .34

Completing a Report Request. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .34

Creating a Report Example. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

Customizing a Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

Selecting a Report Output Destination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38

2. Displaying Report Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39

Using Display Commands in a Request . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39

Displaying Individual Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .41

Displaying All Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42

Displaying All Fields in a Segment. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44

Displaying the Structure and Retrieval Order of a Multi-Path Data Source. . . . . . . . . . . . . . . 45

Adding Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .50

Counting Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52

Counting Segment Instances. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53

Expanding Byte Precision for COUNT and LIST . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54

Maximum Number of Display Fields Supported in a Request . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55

Manipulating Display Fields With Prefix Operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56

Prefix Operator Basics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57

Averaging Values of a Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60

Averaging the Sum of Squared Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61

Calculating Maximum and Minimum Field Values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61

Calculating Median and Mode Values for a Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .62

Calculating Column and Row Percentages. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63

Producing a Direct Percent of a Count. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .65

Aggregating and Listing Unique Values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65

Retrieving First and Last Records. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68

Summing and Counting Values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .70

Ranking Sort Field Values With RNK.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .72

Creating Reports With TIBCO® WebFOCUS Language

 3

Contents

Rolling Up Calculations on Summary Rows. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75

Calculating the Standard Deviation for a Population or a Sample. . . . . . . . . . . . . . . . . . . . . . 80

Using Report-Level Prefix Operators. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .81

Displaying Pop-up Field Descriptions for Column Titles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84

3. Sorting Tabular Reports . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .87

Sorting Tabular Reports Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87

Sorting Rows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88

Using Multiple Vertical (BY) Sort Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90

Displaying a Row for Data Excluded by a Sort Phrase. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91

Sorting Columns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .94

Controlling Display of an ACROSS Title for a Single Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .96

Positioning ACROSS Titles on Report Output. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99

Using Multiple Horizontal (ACROSS) Sort Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107

Collapsing PRINT With ACROSS. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107

Hiding Null Columns in ACROSS Groups. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110

Hiding ACROSS Groups and Columns Within BY Page Breaks. . . . . . . . . . . . . . . . . . . 111

Generating Summary Lines and Hiding Null ACROSS Columns. . . . . . . . . . . . . . . . . . 119

Using Column Styling and Hiding Null ACROSS Columns. . . . . . . . . . . . . . . . . . . . . . . 123

Hiding Null ACROSS Columns in an FML Request. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129

Controlling Display of Sort Field Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133

Reformatting Sort Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .136

Manipulating Display Field Values in a Sort Group . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .138

Creating a Matrix Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140

Controlling Collation Sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141

Specifying the Sort Order . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149

Specifying Your Own Sort Order. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151

Selecting and Assigning Column Titles to ACROSS Values. . . . . . . . . . . . . . . . . . . . . . 155

Ranking Sort Field Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 156

DENSE and SPARSE Ranking. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158

Grouping Numeric Data Into Ranges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163

Grouping Numeric Data Into Tiles. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 167

Restricting Sort Field Values by Highest/Lowest Rank . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 172

4

Contents

Sorting and Aggregating Report Columns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 173

Hiding Sort Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .177

Sort Performance Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178

Sorting With Multiple Display Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180

Controlling Formatting of Reports With Multiple Display Commands. . . . . . . . . . . . . . . . . . . 181

Improving Efficiency With External Sorts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 188

Providing an Estimate of Input Records or Report Size for Sorting. . . . . . . . . . . . . . . . . . . . .190

Sort Work Files and Return Codes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .190

Mainframe External Sort Utilities and Message Options. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 192

Diagnosing External Sort Errors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 193

Aggregation by External Sort (Mainframe Environments Only). . . . . . . . . . . . . . . . . . . . . . . . .195

Changing Retrieval Order With Aggregation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .197

Creating a HOLD File With an External Sort (Mainframe Environments Only) . . . . . . . . . . . .198

Hierarchical Reporting: BY HIERARCHY . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 199

4. Selecting Records for Your Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217

Selecting Records Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .217

Choosing a Filtering Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218

Selections Based on Individual Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 218

Controlling Record Selection in Multi-path Data Sources. . . . . . . . . . . . . . . . . . . . . . . . . . . . .221

Selection Based on Aggregate Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 226

Applying Selection Criteria to the Internal Matrix Prior to COMPUTE Processing . . . . . . . . . . . . . . 228

Using Compound Expressions for Record Selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 235

Using Operators in Record Selection Tests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .236

Types of Record Selection Tests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .243

Range Tests With FROM and TO. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 243

Range Tests With GE and LE or GT and LT. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .245

Missing Data Tests. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246

Character String Screening With CONTAINS and OMITS. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 247

Screening on Masked Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248

Using an Escape Character for LIKE. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 253

Qualifying Parent Segments Using INCLUDES and EXCLUDES. . . . . . . . . . . . . . . . . . . . . . . . 256

Selections Based on Group Key Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .257

Creating Reports With TIBCO® WebFOCUS Language

 5

Contents

Setting Limits on the Number of Records Read . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 258

Selecting Records Using IF Phrases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .259

Reading Selection Values From a File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 260

Assigning Screening Conditions to a File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .265

Preserving Filters Across Joins. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .271

VSAM Record Selection Efficiencies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .274

Reporting From Files With Alternate Indexes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274

5. Creating Temporary Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277

What Is a Temporary Field? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 277

Defining a Virtual Field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 280

Defining Multiple Virtual Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .286

Displaying Virtual Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 287

Clearing a Virtual Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .288

Establishing a Segment Location for a Virtual Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 289

Defining Virtual Fields Using a Multi-Path Data Source. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290

Increasing the Speed of Calculations in Virtual Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 290

Preserving Virtual Fields Using DEFINE FILE SAVE and RETURN. . . . . . . . . . . . . . . . . . . . . . . 291

Applying Dynamically Formatted Virtual Fields to Report Columns. . . . . . . . . . . . . . . . . . . . . 292

Passing Function Calls Directly to a Relational Engine Using SQL.Function Syntax. . . . . . .295

Creating a Calculated Value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .297

Using Positional Column Referencing With Calculated Values. . . . . . . . . . . . . . . . . . . . . . . . 300

Using ACROSS With Calculated Values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .301

Sorting Calculated Values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .302

Screening on Calculated Values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 302

Assigning Column Reference Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 302

Using Column Notation in a Report Request. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 303

Using FORECAST in a COMPUTE Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 313

Calculating Trends and Predicting Values With FORECAST. . . . . . . . . . . . . . . . . . . . . . . . . . . 313

FORECAST Processing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .314

FORECAST_MOVAVE: Using a Simple Moving Average. . . . . . . . . . . . . . . . . . . . . . . . . .315

FORECAST_EXPAVE: Using Single Exponential Smoothing. . . . . . . . . . . . . . . . . . . . . . 320

FORECAST_DOUBLEXP: Using Double Exponential Smoothing. . . . . . . . . . . . . . . . . . . 324

6

Contents

FORECAST_SEASONAL: Using Triple Exponential Smoothing. . . . . . . . . . . . . . . . . . . . 326

FORECAST_LINEAR: Using a Linear Regression Equation. . . . . . . . . . . . . . . . . . . . . . . 331

Distinguishing Data Rows From Predicted Rows. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .334

Calculating Trends and Predicting Values With FORECAST . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 336

FORECAST Processing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 337

Using a Simple Moving Average. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .341

Using Single Exponential Smoothing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .345

Using Double Exponential Smoothing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 347

Using Triple Exponential Smoothing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 349

Using a Linear Regression Equation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 351

FORECAST Reporting Techniques. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 354

Calculating Trends and Predicting Values With Multivariate REGRESS . . . . . . . . . . . . . . . . . . . . . . 357

Using Text Fields in DEFINE and COMPUTE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .360

Creating Temporary Fields Independent of a Master File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 361

6. Including Totals and Subtotals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 367

Calculating Row and Column Totals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 367

Producing Row Totals for Horizontal (ACROSS) Sort Field Values. . . . . . . . . . . . . . . . . . . . . .374

Including Section Totals and a Grand Total . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .375

Including Subtotals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 377

Recalculating Values for Subtotal Rows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 383

Summarizing Alphanumeric Columns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 386

Manipulating Summary Values With Prefix Operators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 388

Controlling Summary Line Processing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .397

Using Prefix Operators With Calculated Values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 402

Using Multiple SUB-TOTAL or SUMMARIZE Commands With Prefix Operators. . . . . . . . . . . 405

Combinations of Summary Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 407

Producing Summary Columns for Horizontal Sort Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 413

Performing Calculations at Sort Field Breaks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 421

Suppressing Grand Totals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 425

Conditionally Displaying Summary Lines and Text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 427

7. Using Expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .429

Using Expressions in Commands and Phrases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .429

Creating Reports With TIBCO® WebFOCUS Language

 7

Contents

Types of Expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 430

Expressions and Field Formats. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 432

Creating a Numeric Expression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 432

Order of Evaluation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 435

Evaluating Numeric Expressions With Native-Mode Arithmetic. . . . . . . . . . . . . . . . . . . . . . . . 437

Using Identical Operand Formats With Native-Mode Arithmetic. . . . . . . . . . . . . . . . . . . . . . . 437

Using Different Operand Formats With Native-Mode Arithmetic. . . . . . . . . . . . . . . . . . . . . . . 438

Creating a Date Expression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 439

Formats for Date Values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 440

Performing Calculations on Dates. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 441

Cross-Century Dates With DEFINE and COMPUTE. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .442

Returned Field Format Selection. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 443

Using a Date Constant in an Expression. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 443

Extracting a Date Component. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .444

Combining Fields With Different Formats in an Expression. . . . . . . . . . . . . . . . . . . . . . . . . . . 444

Creating a Date-Time Expression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 445

Specifying a Date-Time Value. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 450

Manipulating Date-Time Values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 454

Creating a Character Expression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .456

Embedding a Quotation Mark in a Quote-Delimited Literal String. . . . . . . . . . . . . . . . . . . . . .457

Concatenating Character Strings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 458

Creating a Variable Length Character Expression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .460

Using Concatenation With AnV Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 461

Using the EDIT Function With AnV Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 461

Using CONTAINS and OMITS With AnV Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 461

Using LIKE With AnV Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .462

Using the EQ, NE, LT, GT, LE, and GE Operators With AnV Fields. . . . . . . . . . . . . . . . . . . . . 462

Using the DECODE Function With AnV Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 463

Using the Assignment Operator With AnV Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 464

Creating a Logical Expression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 465

Creating a Conditional Expression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 467

8. Saving and Reusing Your Report Output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 471

8

Contents

Saving Your Report Output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .472

Naming and Storing Report Output Files. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 472

Creating a HOLD File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .473

Holding Report Output in FOCUS Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 479

Controlling Attributes in HOLD Master Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 484

Controlling Field Names in a HOLD Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .485

Controlling Fields in a HOLD Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 490

Controlling Attributes in the HOLD Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 495

Keyed Retrieval From HOLD Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 496

Saving and Retrieving HOLD Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .498

Using DBMS Temporary Tables as HOLD Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 500

Column Names in the HOLD File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 505

Primary Keys and Indexes in the HOLD File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 505

Creating SAVE and SAVB Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 506

Creating a PCHOLD File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 509

Choosing Output File Formats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 511

Merging Data Into an Existing Data Source With ON TABLE MERGE . . . . . . . . . . . . . . . . . . . . . . . . 534

Using Text Fields in Output Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .547

Creating a Delimited Sequential File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 549

Saving Report Output in INTERNAL Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 558

Creating A Subquery or Sequential File With HOLD FORMAT SQL_SCRIPT . . . . . . . . . . . . . . . . . . . 561

Creating a Structured HOLD File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 563

9. Choosing a Display Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .575

Report Display Formats . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 576

Preserving Leading and Internal Blanks in Report Output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 579

Using Web Display Format: HTML . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .581

Using Print Display Formats: PDF, PS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .584

Using PDF Display Format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .585

Displaying Watermarks in PDF Output. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 586

Features Supported. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .590

Limits. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 590

Usage Notes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 590

Creating Reports With TIBCO® WebFOCUS Language

 9

Contents

Scaling PDF Report Output to Fit the Page Width. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 590

Aligning a PDF Report Within a Page. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .597

WebFOCUS PDF Report Accessibility Support. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 600

Controlling PDF Code For Accessibility. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 601

Aligning Elements in a Page Heading With Column Data. . . . . . . . . . . . . . . . . . 605

Adding Bookmarks. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 609

Adding Descriptive Text to an Image. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 616

Describing Drill Down Information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .618

Accessibility Limitations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 620

Using PostScript (PS) Display Format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 620

WebFOCUS Font Support. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 623

How WebFOCUS Uses Type 1 Fonts. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 624

Adding PostScript Type 1 Fonts for PS and PDF Formats. . . . . . . . . . . . . . . . . . . . . . . 625

Embedding TrueType Fonts Into WebFOCUS PDF Reports Generated in Windows. . .634

Creating PDF Files on z/OS for Use With UNIX Systems. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 641

Using Word Processing Display Formats: DOC, WP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 643

Saving Report Output in Excel XLSX Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 644

Overview of EXL07/XLSX Format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 645

Building the .xlsx Workbook File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 646

Opening XLSX Report Output. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 648

Formatting Values Within Cells in XLSX Report Output. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .651

Displaying Formatted Numeric Values in XLSX Report Output. . . . . . . . . . . . . . . . . . . 652

Using Numeric Formats in Report Headings and Footings. . . . . . . . . . . . . . . . . . . . . . 654

Using Numeric Format Punctuation in Headings and Footings. . . . . . . . . . . . . . . . . . . 654

Passing Dates to XLSX Report Output. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 657

Passing Dates Without a Day Component. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 658

Passing Date Components for Use in Excel Formulas. . . . . . . . . . . . . . . . . . . . . . . . . . 659

Passing Quarter Formats. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 660

Passing Date Components Defined as Translated Text. . . . . . . . . . . . . . . . . . . . . . . . .661

Passing Date-Time to XLSX. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 662

Generating Native Excel Formulas in XLSX Report Output. . . . . . . . . . . . . . . . . . . . . . . . . . . . 663

Understanding Formula Versus Value. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .663

Using XLSX FORMULA With Prefix Operators. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 672

10

Contents

NODATA With Formulas. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .675

Controlling Column Width and Wrapping in XLSX Report Output. . . . . . . . . . . . . . . . . . . . . . .676

Synchronizing WebFOCUS Page Breaks With Excel Page Breaks. . . . . . . . . . . . . . . . . . . . . . 680

Preserving Leading and Internal Blanks in Report Output. . . . . . . . . . . . . . . . . . . . . . . . . . . . 686

Support for Drill Downs With XLSX Report Output. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .690

Redirection and Excel Drill-Down Reports. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 690

Excel Page Settings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 691

Adding an Image to a Report. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 692

Inserting Images Into Excel XLSX Reports. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 692

Inserting Text and Images Into XLSX Workbook Headers and Footers. . . . . . . . . . . . . . . . . .702

Creating Excel XLSX Worksheets Using Templates. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .708

Creating Excel Table of Contents Reports. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 710

Naming XLSX Worksheets With Case Sensitive Data. . . . . . . . . . . . . . . . . . . . . . . . . . .712

Overcoming the Excel 2007/2010 Row Limit Using Overflow Worksheets. . . . . . . . . . . . . .713

Excel Compound Reports Using XLSX. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 719

Using XLSX FORMULA With Compound Reports. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 731

WebFOCUS Pivot Support for XLSX. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 733

FORMAT XLSX Limitations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .738

Using PowerPoint PPT Display Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 739

Using PowerPoint PPT Templates. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 739

Saving Report Output in PPTX Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 740

Building the .pptx Presentation File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .742

Opening PPTX Report Output. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 744

Opening PPTX Report Output in Microsoft PowerPoint 2000/2003. . . . . . . . . . . . . . .744

Viewing PowerPoint Presentations in the Browser vs. the PowerPoint Application. . 745

Grouping Tables and Components in a PowerPoint Slide. . . . . . . . . . . . . . . . . . . . . . . . . . . . 746

Date and Page/Slide Number. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 751

Text Formatting Markup Tags for a Text Object. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 751

Display Unordered Lists With Bullets, Discs, Squares, and Circles. . . . . . . . . . . . . . .762

Inserting Images In Various Elements of PowerPoint PPTX Reports. . . . . . . . . . . . . . . . . . . .764

Displaying PPTX Charts in PNG Image Format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 772

Drill Down From Microsoft PowerPoint. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 778

PowerPoint PPTX Presentations Using Templates. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .781

Creating Reports With TIBCO® WebFOCUS Language

 11

Contents

PowerPoint PPTX Compound Syntax. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 788

Coordinated Compound Layout Reports. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 793

Templates for Compound Reports. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .798

Adding Images to a Compound Request. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .799

Template Masters and Slide Layouts. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 803

Identifying Slide Master Attributes in PowerPoint. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 803

Merging WebFOCUS Content With PowerPoint Template Content. . . . . . . . . . . . . . . . . . . . . .814

ReportCaster Distribution and ReportCaster Bursting. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 817

PPTX Limitations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .817

Related Information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 817

10. Linking a Report to Other Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 819

Linking Using StyleSheets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 819

Linking to Another Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .820

Linking to a URL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 825

Defining a Hyperlink Color. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .830

Linking to a JavaScript Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 833

Linking to a Maintain Data Procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 836

Multi-Drill Feature With Cascading Menus and User-Defined Styling . . . . . . . . . . . . . . . . . . . . . . . . 842

Accessibility Support. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 842

Creating Multiple Drill-Down Links. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 843

Global Menu Styling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 843

Menu Items Styling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .845

Drill-Down Action Options. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 846

Summary of Drill-Down Links. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 847

Sample Drill Menu Stylesheet Code. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 848

Applying Conditional Styling. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 853

Creating Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 854

Linking With Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 865

Linking From a Graphic Image . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 868

Specifying a Base URL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 872

Specifying a Target Frame . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 873

Creating a Compound Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 876

12

Contents

Creating a Compound Layout Report With Document Syntax. . . . . . . . . . . . . . . . . . . . . . . . . 877

Generating a Table of Contents With BY Field Entries for PPTX and PDF Compound

Layout Reports. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 924

Table of Contents Features. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 925

Creating a Compound PDF or PS Report. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .934

Creating a Compound Excel Report Using EXL2K. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 943

Creating a PDF Compound Report With Drill Through Links . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 954

Sample Drill Through PDF Compound Reports. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .959

11. Navigating Within an HTML Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 969

Navigating Sort Groups From a Table of Contents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 969

Adding the HTML Table of Contents Tree Control to Reports . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 971

Navigation Behavior in a Multi-Level TOC. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 977

Controlling the Display of Sorted Data With Accordion Reports . . . . . . . . . . . . . . . . . . . . . . . . . . . . 989

Requirements for Accordion Reports. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .991

Creating an Accordion By Row Report. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 992

Accordion By Row Tooltips. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1006

Accordion By Row With NOPRINT. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1011

Differences Between Reformatted and Redefined BY Fields. . . . . . . . . . . . . . . . . . . . . . . . .1014

Creating an Accordion By Column Report. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1017

Navigating a Multi-Page Report With the WebFOCUS Viewer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1019

Using the WebFOCUS Viewer Search Option. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1021

Linking Report Pages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1022

12. Bursting Reports Into Multiple HTML Files . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1029

Bursting Reports Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1029

13. Handling Records With Missing Field Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1035

Irrelevant Report Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1035

Missing Field Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1036

MISSING Attribute in the Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1038

MISSING Attribute in a DEFINE or COMPUTE Command. . . . . . . . . . . . . . . . . . . . . . . . . . . . 1039

Testing for Missing Values in IF-THEN-ELSE Expressions. . . . . . . . . . . . . . . . . . . . . . 1045

Testing for a Segment With a Missing Field Value. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1048

Preserving Missing Data Values in an Output File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1051

Creating Reports With TIBCO® WebFOCUS Language

 13

Contents

Propagating Missing Values to Reformatted Fields in a Request. . . . . . . . . . . . . . . . . . . . .1054

Handling a Missing Segment Instance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1056

Including Missing Instances in Reports With the ALL. Prefix. . . . . . . . . . . . . . . . . . . . . . . . .1059

Including Missing Instances in Reports With the SET ALL Parameter. . . . . . . . . . . . . . . . . 1059

Testing for Missing Instances in FOCUS Data Sources. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1066

Setting the NODATA Character String . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1066

14. Joining Data Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1069

Types of Joins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1069

Unique and Non-Unique Joined Structures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1072

Recursive Joined Structures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1076

How the JOIN Command Works . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1081

Creating an Equijoin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1082

Joining From a Virtual Field to a Real Field Using an Equijoin. . . . . . . . . . . . . . . . . . . . . . . .1094

Join Modes in an Equijoin. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1098

Data Formats of Shared Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1099

Joining Fields With Different Numeric Data Types. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1100

Using a Conditional Join . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1101

Full Outer Joins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1105

Reporting Against a Multi-Fact Cluster Synonym . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1113

Adding a New Fact To Multi-Fact Synonyms: JOIN AS_ROOT. . . . . . . . . . . . . . . . . . . . . . . . .1115

Generating Outer Joins of Cluster Synonym Contexts. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1120

Joining From a Multi-Fact Synonym. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1124

Navigating Joins Between Cluster Synonyms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1128

Cross Database Join Optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1131

Invoking Context Analysis for a Star Schema With a Fan Trap . . . . . . . . . . . . . . . . . . . . . . . . . . . .1139

Adding DBA Restrictions to the Join Condition: SET DBAJOIN . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1140

Preserving Virtual Fields During Join Parsing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1143

Preserving Virtual Fields Using KEEPDEFINES. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1144

Preserving Virtual Fields Using DEFINE FILE SAVE and RETURN. . . . . . . . . . . . . . . . . . . . . .1147

Screening Segments With Conditional JOIN Expressions. . . . . . . . . . . . . . . . . . . . . . . . . . . 1149

Parsing WHERE Criteria in a Join. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1149

Displaying Joined Structures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1149

14

Contents

Clearing Joined Structures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1151

Clearing a Conditional Join. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1152

15. Merging Data Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1155

Merging Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1155

Types of MATCH Processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1157

MATCH Processing With Common High-Order Sort Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1166

Fine-Tuning MATCH Processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1170

Universal Concatenation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1173

Field Name and Format Matching. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1176

Merging Concatenated Data Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1178

Using Sort Fields in MATCH Requests. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1180

Cartesian Product . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1184

16. Formatting Reports: An Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1187

What Kinds of Formatting Can I Do? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1187

How to Specify Formatting in a Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1190

How to Choose a Type of Style Sheet. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1193

Standard and Legacy Formatting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1194

Techniques for Quick and Easy Formatting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1194

Navigating From a Report to Other Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1195

17. Creating and Managing a WebFOCUS StyleSheet . . . . . . . . . . . . . . . . . . . . . . . . . . . 1197

Creating a WebFOCUS StyleSheet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1197

Creating a WebFOCUS StyleSheet Within a Report Request. . . . . . . . . . . . . . . . . . . . . . . . .1198

Creating and Applying a WebFOCUS StyleSheet File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1200

General WebFOCUS StyleSheet Syntax . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1202

Improving WebFOCUS StyleSheet Readability. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1203

Adding a Comment to a WebFOCUS StyleSheet. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1204

Reusing WebFOCUS StyleSheet Declarations With Macros . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1204

Defining a WebFOCUS StyleSheet Macro. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1204

Applying a WebFOCUS StyleSheet Macro. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1205

WebFOCUS StyleSheet Attribute Inheritance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1207

Creating Reports With the ENWarm StyleSheet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1211

Report Styling. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1212

Creating Reports With TIBCO® WebFOCUS Language

 15

Contents

Data, Report, and Title Styling. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1212

Headings and Footings Styling. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1213

Subheading and Subfooting Styling. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1214

Across Styling. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1215

Subtotal and Column Total Styling. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1216

Active Reports. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1216

Pagination, Menu, and Hover Text Styling in WebFOCUS Active Reports. . . . . . . . . 1217

Usage Notes for ENWarm.sty. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1218

18. Controlling Report Formatting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1219

Generating an Internal Cascading Style Sheet for HTML Reports . . . . . . . . . . . . . . . . . . . . . . . . . 1220

Selecting a Unit of Measurement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1221

Conditionally Formatting, Displaying, and Linking in a StyleSheet . . . . . . . . . . . . . . . . . . . . . . . . 1222

Applying Sequential Conditional Formatting. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1223

Including Summary Lines, Underlines, Skipped Lines, and Page Breaks . . . . . . . . . . . . . . . . . . .1239

Conditionally Including Summary Lines, Underlines, Skipped Lines, and Page Breaks . . . . . . . 1241

Controlling the Display of Empty Reports . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1246

Formatting a Report Using Only StyleSheet Defaults . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1248

19. Identifying a Report Component in a WebFOCUS StyleSheet . . . . . . . . . . . . . . . . 1249

Identifying an Entire Report, Column, or Row . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1249

Identifying Tags for SUBTOTAL and GRANDTOTAL Lines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1258

Identifying Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1261

Identifying Totals and Subtotals. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1267

Identifying a Heading, Footing, Title, or FML Free Text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1273

Identifying a Column or Row Title. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1273

Identifying a Heading or Footing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1277

Identifying a Page Number, Underline, or Skipped Line . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1288

20. Using an External Cascading Style Sheet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1293

What Is a Cascading Style Sheet? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1293

What Are Cascading Style Sheet Rules and Classes?. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1294

Why Use an External Cascading Style Sheet? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1295

Formatting a Report With an External Cascading Style Sheet . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1296

Working With an External Cascading Style Sheet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1302

16

Contents

Choosing an External Cascading Style Sheet. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1303

External Cascading Style Sheet Location. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1303

Using Several External Cascading Style Sheets. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1303

Editing an External Cascading Style Sheet. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1304

Choosing a Cascading Style Sheet Rule. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1304

Naming a Cascading Style Sheet Class. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1305

Applying External Cascading Style Sheet Formatting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1306

Combining an External CSS With Other Formatting Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1308

Combining an External CSS With a WebFOCUS StyleSheet. . . . . . . . . . . . . . . . . . . . . . . . . .1309

Linking to an External Cascading Style Sheet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1310

Using the CSSURL Attribute and Parameter. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1310

Inheritance and External Cascading Style Sheets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1314

Using External Cascading Style Sheets With Non-HTML Reports . . . . . . . . . . . . . . . . . . . . . . . . . 1316

Requirements for Using an External Cascading Style Sheet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1321

FAQ About Using External Cascading Style Sheets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1323

Troubleshooting External Cascading Style Sheets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1327

21. Laying Out the Report Page . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1331

Selecting Page Size, Orientation, and Color . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1331

Setting Page Margins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1337

Positioning a Report Component . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1340

Arranging Columns on a Page . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1346

Determining Column Width. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1347

Controlling Column Spacing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1352

Changing Column Order. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1353

Stacking Columns. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1355

Alignment of Fields in Reports Using OVER in PDF Report Output. . . . . . . . . . . . . . .1358

Positioning a Column. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1367

Suppressing Column Display . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1371

Inserting a Page Break . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1377

Preventing an Undesirable Split. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1383

Inserting Page Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1388

Inserting the Total Page Count. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1390

Creating Reports With TIBCO® WebFOCUS Language

 17

Contents

Displaying the Total Page Count Within a Sort Group. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1392

Assigning Any Page Number to the First Page. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1395

Controlling the Display of Page Numbers. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1397

Setting the Number of Data Rows For Each Page in an AHTML Report Request. . . . . . . . 1399

Adding Grids and Borders . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1402

Defining Borders Around Boxes With PPTX and PDF Formats . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1433

Displaying Superscripts On Data, Heading, and Footing Lines . . . . . . . . . . . . . . . . . . . . . . . . . . . 1435

Adding Underlines and Skipped Lines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1440

Removing Blank Lines From a Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1456

Adding an Image to a Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1462

Associating Bar Graphs With Report Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1499

Controlling Bar Graph Scaling in Horizontal (ACROSS) Sort Fields. . . . . . . . . . . . . . . . . . . . 1506

Applying Scaling to Data Visualization Bar Graphs. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1508

Working With Mailing Labels and Multi-Pane Pages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1510

22. Using Headings, Footings, Titles, and Labels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1517

Creating Headings and Footings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1518

Limits for Headings and Footings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1519

Extending Heading and Footing Code to Multiple Lines in a Report Request. . . . . . . . . . .1520

Creating a Custom Report or Worksheet Title. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1522

Creating a Report Heading or Footing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1525

Creating a Page Heading or Footing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1532

Freezing HTML and AHTML Headings, Footings, and Column Titles. . . . . . . . . . . . . . . . . . 1540

Creating a Sort Heading or Footing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1543

Including an Element in a Heading or Footing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1557

Including a Field Value in a Heading or Footing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1558

Including a Text Field in a Heading or Footing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1565

Including a Page Number in a Heading or Footing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1567

Including a Dialogue Manager Variable in a Heading or Footing. . . . . . . . . . . . . . . . . . . . . .1567

Including an Image in a Heading or Footing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1569

Displaying Syntax Components in Heading and Footing Objects . . . . . . . . . . . . . . . . . . . . . . . . . . 1570

Repeating Headings and Footings on Panels in PDF Report Output . . . . . . . . . . . . . . . . . . . . . . . 1572

Customizing a Column Title . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1589

18

Contents

Customizing a Column Title in a Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1594

Distinguishing Between Duplicate Field Names. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1594

Controlling Column Title Underlining Using a SET Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1595

Controlling Column Title Underlining Using a StyleSheet Attribute . . . . . . . . . . . . . . . . . . . . . . . . 1597

Creating Labels to Identify Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1600

Creating a Label for a Row or Column Total. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1600

Creating a Label for a Subtotal and a Grand Total. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1602

Creating a Label for a Row in a Financial Report. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1607

Formatting a Heading, Footing, Title, or Label . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1607

Applying Font Attributes to a Heading, Footing, Title, or Label . . . . . . . . . . . . . . . . . . . . . . . . . . . .1609

Adding Borders and Grid Lines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1613

Justifying a Heading, Footing, Title, or Label . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1616

Justifying a Heading or Footing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1617

Justifying a Column Title. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1624

Justifying a Label for a Row or Column Total. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1629

Justifying a Label for a Subtotal or Grand Total. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1631

Choosing an Alignment Method for Heading and Footing Elements . . . . . . . . . . . . . . . . . . . . . . . 1633

Aligning a Heading or Footing Element in an HTML, XLSX, EXL2K, PDF, PPTX, or DHTML

Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1635

Aligning a Heading or Footing Element Across Columns in an HTML or PDF Report . . . . . . . . . .1653

Aligning Content in a Multi-Line Heading or Footing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1659

Aligning Decimals in a Multi-Line Heading or Footing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1664

Combining Column and Line Formatting in Headings and Footings. . . . . . . . . . . . . . . . . . . 1666

Positioning Headings, Footings, or Items Within Them . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1671

Using PRINTPLUS. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1678

Using Spot Markers to Refine Positioning. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1680

Controlling the Vertical Positioning of a Heading or Footing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1685

Placing a Report Heading or Footing on Its Own Page . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1692

23. Formatting Report Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1697

Specifying Font Format in a Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1697

Specifying Fonts for Reports. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1703

Specifying Background Color in a Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1705

Creating Reports With TIBCO® WebFOCUS Language

 19

Contents

Alternating Background Color By Wrapped Line . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1709

Specifying Data Format in a Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1712

Changing the Format of Values in a Report Column. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1713

Controlling Missing Values for a Reformatted Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1715

Using Commas vs. Decimals (Continental Decimal Notation). . . . . . . . . . . . . . . . . . . . . . . .1717

Setting Characters to Represent Null and Missing Values. . . . . . . . . . . . . . . . . . . . . . . . . . 1717

Using Conditional Grid Formatting in a Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1718

Positioning Data in a Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1719

Controlling Wrapping of Report Data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1719

Justifying Report Columns. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1734

Field-Based Reformatting. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1736

Displaying Multi-Line An and AnV Fields. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1739

24. Creating a Graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1743

Content Analysis: Determining Graphing Objectives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1743

The GRAPH Command . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1744

Similarities Between GRAPH and TABLE. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1745

Differences Between GRAPH and TABLE. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1745

Creating an HTML5 Graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1747

Selecting a Graph Type . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1749

Graph Types. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1749

Selecting Scales. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1750

Determining Graph Styles With Display Commands and Sort Phrases. . . . . . . . . . . . . . . . 1751

Determining Graph Styles Using LOOKGRAPH. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1759

Selecting Values for the X and Y Axes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1769

Hiding the Display of a Y-Axis Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1771

Interpolating X and Y Axis Values Using Linear Regression. . . . . . . . . . . . . . . . . . . . . . . . . 1771

Creating Multiple Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1772

Merging Multiple Graphs. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1773

Merging Multiple OLAP Graphs. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1776

Displaying Multiple Graphs in Columns. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1778

Plotting Dates in Graphs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1779

Basic Date Support for X and Y Axes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1780

20

Contents

Formatting Dates for Y-Axis Values. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1781

Refining the Data Set For Your Graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1781

Displaying Missing Data Values in a Graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1782

Applying Conditional Styling to a Graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1787

Linking Graphs to Other Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1790

Creating Parameters. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1798

Adding Labels to a Graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1798

Adding Vertical (Y-axis) and Horizontal (X-axis) Labels to a Graph. . . . . . . . . . . . . . . . . . . . 1799

Applying Custom Styling to a Graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1799

Setting the Graph Height and Width. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1800

Customizing Graphs Using SET Parameters. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1800

Setting Fixed Scales for the X-Axis. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1805

Setting Fixed Scales for the Y-Axis. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1806

Customizing Graphs Using the Graph API and HTML5 JSON Properties. . . . . . . . . . . . . . . 1807

Saving a Graph as an Image File . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1809

Saving a Graph as an Image File Using GRAPHSERVURL. . . . . . . . . . . . . . . . . . . . . . . . . . . 1809

Printing a Graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1814

25. Creating Financial Reports With Financial Modeling Language (FML) . . . . . . . . . 1817

Reporting With FML . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1817

Creating Rows From Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1820

Creating Rows From Multiple Records. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1823

Using the BY Phrase in FML Requests. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1828

Combining BY and FOR Phrases in an FML Request. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1829

Supplying Data Directly in a Request . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1829

Performing Inter-Row Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1831

Referring to Rows in Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1832

Referring to Columns in Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1835

Referring to Column Numbers in Calculations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1836

Referring to Contiguous Columns in Calculations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1837

Referring to Column Addresses in Calculations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1838

Referring to Relative Column Addresses in Calculations. . . . . . . . . . . . . . . . . . . . . . . . . . . .1839

Applying Relative Column Addressing in a RECAP Expression. . . . . . . . . . . . . . . . . . . . . . . 1840

Creating Reports With TIBCO® WebFOCUS Language

 21

Contents

Controlling the Creation of Column Reference Numbers. . . . . . . . . . . . . . . . . . . . . . . . . . . . 1840

Referring to Column Values in Calculations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1841

Referring to Rows and Columns in Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1842

Referring to Cells in Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1843

Using Functions in RECAP Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1845

Inserting Rows of Free Text . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1847

Adding a Column to an FML Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1849

Creating a Recursive Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1852

Reporting Dynamically From a Hierarchy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1853

Requirements for FML Hierarchies. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1854

Displaying an FML Hierarchy. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1856

Consolidating an FML Hierarchy. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1859

Loading a Hierarchy Manually. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1867

Customizing a Row Title . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1870

Formatting an FML Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1871

Indenting Row Titles in an FML Hierarchy. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1889

Suppressing the Display of Rows . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1892

Suppressing Rows With No Data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1893

Saving and Retrieving Intermediate Report Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1894

Posting Data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1894

Creating HOLD Files From FML Reports . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1897

26. Creating a Free-Form Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1899

Creating a Free-Form Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1899

Designing a Free-Form Report . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1903

Incorporating Text in a Free-Form Report. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1904

Incorporating Data Fields in a Free-Form Report. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1904

Incorporating Graphic Characters in a Free-Form Report. . . . . . . . . . . . . . . . . . . . . . . . . . . . 1905

Laying Out a Free-Form Report. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1905

Sorting and Selecting Records in a Free-Form Report. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1906

27. Using SQL to Create Reports . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1907

Supported and Unsupported SQL Statements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1907

Using SQL Translator Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1910

22

Contents

The SQL SELECT Statement. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1912

Using the SQL SELECT Statement Without a FROM Clause. . . . . . . . . . . . . . . . . . . . 1913

SQL Joins. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1913

SQL CREATE TABLE and INSERT INTO Commands. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1917

SQL CREATE VIEW and DROP VIEW Commands. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1918

Cartesian Product Style Answer Sets. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1920

Continental Decimal Notation (CDN). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1920

Specifying Field Names in SQL Requests. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1920

SQL UNION, INTERSECT, and EXCEPT Operators. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1921

Numeric Constants, Literals, Expressions, and Functions. . . . . . . . . . . . . . . . . . . . . . . . . . 1921

SQL Translator Support for Date, Time, and Timestamp Fields . . . . . . . . . . . . . . . . . . . . . . . . . . .1921

Extracting Date-Time Components Using the SQL Translator. . . . . . . . . . . . . . . . . . . . . . . . 1923

Index Optimized Retrieval . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1926

Optimized Joins. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1926

TABLEF Optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1927

SQL INSERT, UPDATE, and DELETE Commands . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1927

28. Improving Report Processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1929

Rotating a Data Structure for Enhanced Retrieval . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1929

Optimizing Retrieval Speed for FOCUS Data Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1932

Automatic Indexed Retrieval . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1932

Data Retrieval Using TABLEF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1935

Compiling Expressions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1936

Compiling Expressions Using the DEFINES Parameter. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1936

A. Master Files and Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1937

EMPLOYEE Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1937

EMPLOYEE Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1939

EMPLOYEE Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1940

JOBFILE Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1940

JOBFILE Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1941

JOBFILE Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1941

EDUCFILE Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1942

EDUCFILE Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1942

Creating Reports With TIBCO® WebFOCUS Language

 23

Contents

EDUCFILE Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1943

SALES Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1943

SALES Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1944

SALES Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1945

CAR Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1945

CAR Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1947

CAR Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1948

LEDGER Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1948

LEDGER Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1949

LEDGER Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1949

FINANCE Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1949

FINANCE Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1949

FINANCE Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1950

REGION Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1950

REGION Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1950

REGION Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1950

EMPDATA Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1951

EMPDATA Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1951

EMPDATA Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1951

TRAINING Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1951

TRAINING Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1952

TRAINING Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1952

COURSE Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1952

COURSE Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1952

COURSE Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1953

JOBHIST Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1953

JOBHIST Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1953

JOBHIST Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1953

JOBLIST Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1953

JOBLIST Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1954

JOBLIST Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1954

LOCATOR Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1954

LOCATOR Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1954

24

Contents

LOCATOR Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1955

PERSINFO Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1955

PERSINFO Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1955

PERSINFO Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1955

SALHIST Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1956

SALHIST Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1956

SALHIST Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1956

VIDEOTRK, MOVIES, and ITEMS Data Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1956

VIDEOTRK Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1957

VIDEOTRK Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1958

MOVIES Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1959

MOVIES Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1959

ITEMS Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1959

ITEMS Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1960

VIDEOTR2 Data Source . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1960

VIDEOTR2 Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1960

VIDEOTR2 Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1961

Gotham Grinds Data Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1961

GGDEMOG Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1962

GGDEMOG Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1963

GGORDER Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1963

GGORDER Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1964

GGPRODS Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1964

GGPRODS Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1965

GGSALES Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1965

GGSALES Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1966

GGSTORES Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1966

GGSTORES Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1966

Century Corp Data Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1967

CENTCOMP Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1968

CENTCOMP Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1968

CENTFIN Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1969

CENTFIN Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1969

Creating Reports With TIBCO® WebFOCUS Language

 25

Contents

CENTHR Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1970

CENTHR Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1972

CENTINV Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1973

CENTINV Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1973

CENTORD Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1974

CENTORD Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1975

CENTQA Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1976

CENTQA Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1977

CENTGL Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1977

CENTGL Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1978

CENTSYSF Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1978

CENTSYSF Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1978

CENTSTMT Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1979

CENTSTMT Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1980

CENTGLL Master File. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1980

CENTGLL Structure Diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1981

B. Error Messages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1983

Displaying Messages . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1983

C. Table Syntax Summary and Limits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1985

TABLE Syntax Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1986

Hierarchical Reporting Syntax Summary. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1987

TABLEF Syntax Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1988

MATCH Syntax Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1989

FOR Syntax Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1990

TABLE Limits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1991

D. Referring to Fields in a Report Request . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1993

Referring to an Individual Field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1993

Referring to Fields Using Qualified Field Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1994

Referring to All of the Fields in a Segment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1995

Displaying a List of Field Names . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1996

Listing Field Names, Aliases, and Format Information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1996

26

Legal and Third-Party Notices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1997

Contents

Creating Reports With TIBCO® WebFOCUS Language

 27

Contents

28

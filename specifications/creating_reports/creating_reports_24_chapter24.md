Chapter24

Creating a Graph

Graphs often convey meaning more clearly than data listed in tabular format. Using the
GRAPH command, you can easily transform almost any type of data into an effective
graph that you can customize to suit your needs.

You can link your graph to other resources, or feature conditional styling to highlight
specific data in your graph. You may also select from a multitude of graph styles, which
include the standard graph formats bar, line, pie, and scatter as well as many variations
on these types.

You can also represent data graphically using data visualization. For details, see
Displaying Report Data on page 39.

In this chapter:

Content Analysis: Determining Graphing
Objectives

The GRAPH Command

Refining the Data Set For Your Graph

Displaying Missing Data Values in a
Graph

Creating an HTML5 Graph

Applying Conditional Styling to a Graph

Selecting a Graph Type

Linking Graphs to Other Resources

Selecting Values for the X and Y Axes

Adding Labels to a Graph

Creating Multiple Graphs

Applying Custom Styling to a Graph

Plotting Dates in Graphs

Saving a Graph as an Image File

Printing a Graph

Content Analysis: Determining Graphing Objectives

WebFOCUS offers a range of reporting tools that allow you to create reports that deliver critical
information to your users. By selecting a tool that is well suited to your particular needs, you
can design the information you deliver to users. One effective option with almost any type of
data is a graphic presentation.

Creating Reports With TIBCO® WebFOCUS Language

 1743

The GRAPH Command

Graphs allow you to display multivariate or complex data efficiently, precisely, and in a way that
a viewer can intuitively grasp. A graph is an effective presentation tool because it presents a
visual idea, communicating meaningful changes in data to a user in a memorable way. By
viewing your graph, a user can identify and track a change that you want them to notice.

Creating a meaningful graph is not simply a matter of applying aesthetics to your data. Instead,
graphs allow you to design your presentation to capture the essential information in your data.

The first step in creating excellent graphics is determining your graphing objectives. You can
break this process into several stages.

1. Assess your data:

Look for meaningful patterns or changes in the data. Does your data change most
dramatically over time or in relationship to some other value? Are there two sets of data
that you would like to compare to each other?

Determine what movement or changes you would like to highlight. Which of the patterns in
the data would you most want the viewer to picture?

2. Select the graph type that best suits your argument and the overall shape of your data.

Determine what will lead viewers to the cognitive task or connection that you want them to
make.

3. Begin developing your graph.

4. Refine your graph:

Are the labels meaningful or useful?

How can the data be organized in a meaningful way? Consider customizing the scales you
use with your graph.

The GRAPH Command

GRAPH request syntax is similar to TABLE request syntax. To produce a graph instead of a
tabular report, you need only substitute the command GRAPH for TABLE in the request. Thus,
you can produce graphs by simply converting TABLE requests to GRAPH requests.

However, not every TABLE facility has a GRAPH counterpart, and there are some practical
limitations on the amount of information that you can effectively display in a graph. When a
TABLE request is converted in this manner, the various phrases that make up the body of the
request take on special meanings that determine the format and layout of the graph. The type
of graph produced by a GRAPH request depends on the display command used (SUM or
PRINT), and the sort phrase(s) used (ACROSS or BY).

1744

Similarities Between GRAPH and TABLE

24. Creating a Graph

The GRAPH request elements generally follow the same rules as their TABLE counterparts:

The word FILE and the file name must immediately follow the GRAPH command, unless they
were previously specified in a SET command:

SET FILE=filename

You can specify any file available to WebFOCUS, including joined or cross-referenced
structures.

You can concatenate unlike data source files in a GRAPH request with the MORE
command. For details, see Universal Concatenation on page 1173.

The order of the phrases in the request does not affect the format of the graph. For
example, the selection phrase may follow or precede the display command and sort
phrase(s). The order of sort phrases does affect the format of a graph, just as the order of
sort phrases in TABLE requests affects the appearance of reports.

The word END must be on a line by itself to complete a request.

All dates are displayed in MDY format unless they are changed to alphanumeric fields.

Differences Between GRAPH and TABLE

There are a few notable syntactical differences between TABLE and GRAPH. Specifically, the
following restrictions apply:

A GRAPH request must contain a display command with at least one display field and at
least one sort phrase (BY or ACROSS) in order to generate a meaningful graph.

In GRAPH requests the object of the display command must always be a numeric field.

No more than five display fields are permitted in a GRAPH request. Standard graph formats
generally do not permit more variables to be displayed without rendering the graph
unreadable.

Several BY phrases can be used in a request, in which case multiple graphs are created. A
single ACROSS phrase is allowed in a GRAPH request, and requests for certain graph forms
can contain both ACROSS and BY phrases.

The number of ACROSS values cannot exceed 64.

The RUN option is not available as an alternative to END.

Creating Reports With TIBCO® WebFOCUS Language

 1745

The GRAPH Command

Example:

Converting a TABLE Request to a GRAPH Request

The following illustrates how a TABLE request can easily be converted into a GRAPH request by
changing the TABLE command to a GRAPH command.

TABLE FILE GGORDER
HEADING CENTER
"SAMPLE TABLE"
SUM QUANTITY
BY PRODUCT_DESC AS 'Coffee Types'
WHERE PRODUCT_DESC EQ 'French Roast' OR 'Hazelnut' OR 'Kona'
END

The output is:

        SAMPLE TABLE
Coffee Types      Ordered Units
------------      -------------
French Roast             285689
Hazelnut                 100427
Kona                      61498

The same request with a GRAPH command in place of the TABLE command is:

GRAPH FILE GGORDER
HEADING CENTER
"Sample Graph"
SUM QUANTITY
BY PRODUCT_DESC AS 'Coffee Types'
WHERE PRODUCT_DESC EQ 'French Roast' OR 'Hazelnut' OR 'Kona'
END

1746

The output is:

24. Creating a Graph

Creating an HTML5 Graph

WebFOCUS supports a graph output format that takes advantage of the HTML5 standard. The
charts are rendered in the browser as high quality interactive vector graphics using a built-in
JavaScript engine. Note that older browsers do not support all of the features of the HTML5
standard.

You can use the SET AUTOFIT command to make the HTML5 graph output resize to fit into the
container in which it is placed.

Syntax:

How to Create HTML5 Graph Output

In your graph request, include the following commands

ON GRAPH PCHOLD FORMAT JSCHART

If the ON GRAPH PCHOLD FORMAT JSCHART command is not issued, server-side graphics are
generated.

Example:

Creating an HTML5 Vertical Bar Graph

The following request against the GGSALES data source creates an HTML5 vertical bar graph:

Creating Reports With TIBCO® WebFOCUS Language

 1747

Creating an HTML5 Graph

GRAPH FILE GGSALES
SUM DOLLARS BUDDOLLARS
BY REGION
ON GRAPH PCHOLD FORMAT JSCHART
ON GRAPH SET LOOKGRAPH VBAR
END

The output is:

Syntax:

How to Resize HTML5 Graph Output to Fit Its Container

ON GRAPH SET AUTOFIT {OFF|ON|RESIZE}

where:

OFF

Respects the dimensions specified by the HAXIS and VAXIS parameters.

ON

Always resizes the HTML5 graph output to fit its container.

RESIZE

Respects the dimensions specified by the HAXIS and VAXIS parameters initially, but
resizes the graph output if the container is resized.

1748

24. Creating a Graph

Selecting a Graph Type

When creating a graph, it is important to select the appropriate graph type with which to
display your data. You may select from a number of basic graph types, as well as refinements
on these types. Basic graph types include line graphs (connected point plots), bar graphs, pie
graphs, and scatter graphs. Use the brief descriptions (see Graph Types on page 1749) to
select a graph type that suits the data set you are displaying and the change you want to
highlight. Keep in mind that the data are the sets of numbers that you are displaying, and the
scales are the numbers or variable measures displayed along the axes of the graph.

Note: When using a stacked chart of any type at least 2 series are required.

Graph Types

Following are descriptions of the types of graphs you can create:

Line graphs. Line graphs are useful for emphasizing the movement or trend of numerical
data over time, since they allow a viewer to trace the evolution of a particular point by
working backwards or interpolating. Highs and lows, rapid or slow movement, or a tendency
towards stability are all types of trends that are well suited to a line graph.

Line graphs can also be plotted with two or more scales to suggest a comparison of the
same value, or set of values, in different time periods. The number of scales your graph
has depends on the type of graph you select. For details, see Determining Graph Styles
Using LOOKGRAPH on page 1759.

Bar graphs. A bar graph plots numerical data by displaying rectangular blocks against a
scale. The length of a bar corresponds to a value or amount. Viewers can develop a clear
mental image of comparisons among data series by distinguishing the relative heights of
the bars. Use a bar graph to display numerical data when you want to present distributions
of data. You can create horizontal as well as vertical bar graphs.

Pie graphs. A pie graph emphasizes where your data fits in relation to a larger whole. Keep
in mind that pie graphs work best when your data consists of several large sets. Too many
variables divide the pie into small segments that are difficult to see. Use color or texture on
individual segments to create visual contrast.

Scatter graphs. Scatter graphs share many of the characteristics of basic line graphs. Data
can be plotted using variable scales on both axes. When you use a scatter graph, your data
is plotted using a basic line pattern. Use a scatter graph to visualize the density of
individual data values around particular points or to demonstrate patterns in your data. A
numeric X-axis, or sort field, will always yield a scatter graph by default.

Creating Reports With TIBCO® WebFOCUS Language

 1749

Selecting a Graph Type

It is important to note that scatter graphs and line graphs are distinguishable from one
another only by virtue of their X-axis format. Line graphs can appear without connecting
lines (making them look like scatter graphs) and scatter graphs can appear with connecting
lines (making them look like line graphs).

Area graphs. Area graphs are similar to line graphs except that the area between the data
line and the zero line (or axis) is usually colored or textured. Area graphs allow you to stack
data on top of each other. Stacking allows you to highlight the relationship between data
series, showing how some data series approach or shadow a second series.

3D graphs. 3D graphs add dimension to your graphing presentation. Dimensionality allows
your viewers to recognize trends based on two or more data sets easily. 3D graphs also
add impact to your presentation.

Bipolar graphs. A bipolar graph is split along a horizontal line. This type of graph is useful
for comparative trend analysis of widely disparate data values over time or other sort
values.

Radar graphs. This is a type of circular graph used when categories are cyclical. Radar
graphs are essentially analogous to a line chart, except that the scale wraps around. Radar
graphs work well with any data that are cyclical, such as the months of a year.

Selecting Scales

After you have chosen a graph type, you should select an appropriate scale. A scale is a
classification scheme or series of measures that you select for application to the axes of your
graph. The scale provides the framework against which your data are plotted. When you
choose an appropriate scale for your data, meaningful patterns can emerge, and when you
modify a scale, the overall shape of your graph changes.

Steps or measures in the scale are represented along the axes of your graph by marks. The
type of scale you choose determines the number of divisions along the scale. There are two
general types of scales you can apply to the y-axis of your graph:

Linear scales

Logarithmic scales

A linear scale is a scale in which the values increase arithmetically. Each measure along the
scale is one unit higher than the one that precedes it. Linear scales are useful when the data
you are plotting are relatively small in range.

1750

24. Creating a Graph

A logarithmic scale is a scale in which the values increase logarithmically. Each measure along
the scale represents an exponential increase in the data value. Logarithmic scales are useful
when you need to accommodate a large range of numbers.

Syntax:

How to Select Scales

To use logarithmic scales in your graph, add the following to your GRAPH request:

ON GRAPH SET STYLE *
*GRAPH_SCRIPT
setY1LogScale(value);
*END
ENDSTYLE
END

where:

value

Is one of the following:

true turns on logarithmic scaling.

false turns off logarithmic scaling. Linear scaling is used instead.

Determining Graph Styles With Display Commands and Sort Phrases

Each GRAPH request must include a sort phrase and at least one display field (up to five are
allowed).

The fields, which are the subjects of the graph, may be real or virtual fields, with or without
direct operation prefixes (AVE., MIN., MAX., etc.). They may also be calculated values.

Note: Display fields used only for calculations need not appear in the graph. You can use the
NOPRINT or SUP-PRINT phrases to suppress the display of such fields. For details, see Sorting
Tabular Reports on page 87.

By default, a particular combination of display commands and sort phrases determines the
graph format. The combinations are:

Graph Type

Line graph

Display Command and Sort Phrase

PRINT A {ACROSS|BY} B

(where B is alphanumeric)

Creating Reports With TIBCO® WebFOCUS Language

 1751

Selecting a Graph Type

Graph Type

Display Command and Sort Phrase

Vertical bar graph

SUM A ACROSS B

Horizontal bar graph

SUM A BY B

(where B is alphanumeric)

Pie graph

Scatter graph (without
connecting lines)

Scatter graph (with connecting
lines)

SET LOOKGRAPH=PIE
SUM A {ACROSS|BY} B

or

SET PIE=ON
SUM A {ACROSS|BY} B

PRINT A ACROSS B

(where B is numeric)

SUM A ACROSS B

(where B is numeric)

You can override the default graph format using the LOOKGRAPH parameter. For details, see
Determining Graph Styles Using LOOKGRAPH on page 1759.

Syntax:

How to Create a Line Graph

To create a line graph, issue a GRAPH request with the following display command and sort
field combination

PRINT fieldname1 [AND] fieldname2...
{ACROSS|BY} sortfield

where:

fieldname1...

Is the name of the field to be displayed on the Y-axis of the graph. There can be a
maximum of 5 display fields in a GRAPH request.

Is an optional phrase used to enhance readability. It can be used between any two field
names and does not affect the graph.

AND

1752

24. Creating a Graph

sortfield

Is the name of the field to be displayed on the X-axis of the graph. This must be an
alphanumeric field in order to generate a line graph. If the field specified is numeric, you
can still create a line graph by using the LOOKGRAPH=LINE parameter. For details, see
Determining Graph Styles Using LOOKGRAPH on page 1759.

Example:

Creating a Line Graph

The following illustrates how to create a line graph using the LOOKGRAPH command:

SET LOOKGRAPH = LINE, GRID=ON
SET HAXIS=600, VAXIS=315
GRAPH FILE GGORDER
HEADING CENTER
"Sample Line Graph"
SUM QUANTITY
ACROSS PRODUCT_DESC
WHERE PRODUCT_DESC EQ 'French Roast' OR 'Hazelnut' OR 'Kona'
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1753

Selecting a Graph Type

Syntax:

How to Create a Horizontal Bar Graph

To create a horizontal bar graph, issue a GRAPH request with the following display command
and sort field combination

SUM fieldname1 [AND] fieldname2...
BY sortfield

where:

fieldname1...

Is the name of a field to be displayed on the Y-axis of the graph. There can be a maximum
of 5 display fields in a GRAPH request.

AND

Is an optional phrase used to enhance readability. It can be used between any two field
names and does not affect the graph.

sortfield

Is the name of a field to be displayed on the X-axis of the graph. A separate group of bars
is created for each value of the BY field, and each group contains one bar for each display
command (SUM) object.

Syntax:

How to Create a Vertical Bar Graph

To create a vertical bar graph, issue a GRAPH request with the following display command and
sort field combination

SUM fieldname1 [AND] fieldname2...
ACROSS sortfield

where:

fieldname1...

Is the name of the field to be displayed on the Y-axis of the graph. There can be a
maximum of 5 display fields in a GRAPH request.

AND

Is an optional phrase used to enhance readability. It can be used between any two field
names and does not affect the graph.

sortfield

Is the name of an alphanumeric field to be displayed on the X-axis of the graph.

1754

24. Creating a Graph

Example:

Creating a Horizontal Bar Graph

The following illustrates how to create a horizontal bar graph:

GRAPH FILE GGORDER
HEADING CENTER
"Sample Horizontal Bar Graph"
SUM QUANTITY
BY PRODUCT_DESC
WHERE PRODUCT_DESC EQ 'French Roast' OR 'Hazelnut' OR 'Kona'
END

The output is:

Example:

Creating a Vertical Bar Graph

The following illustrates how to create a vertical bar graph:

GRAPH FILE GGORDER
HEADING CENTER
"SAMPLE VERTICAL BAR GRAPH"
SUM QUANTITY
ACROSS PRODUCT_DESC
WHERE PRODUCT_DESC EQ 'French Roast' OR 'Hazelnut' OR 'Kona'
END

Creating Reports With TIBCO® WebFOCUS Language

 1755

Selecting a Graph Type

The output is:

Syntax:

How to Create a Pie Graph

To create a pie graph, issue a GRAPH request with the following SET command and display and
sort field combination

SET LOOKGRAPH=PIE
SUM fieldname1 [AND] fieldname2...
{ACROSS|BY} sortfield

where:

fieldname1...

Is the name of the field to be displayed in the graph. There can be a maximum of 5 display
fields in a GRAPH request.

AND

Is an optional phrase used to enhance readability. It can be used between any two field
names and does not affect the graph.

1756

24. Creating a Graph

sortfield

Is the name of the field to be displayed in the graph. Each value in the sort field will be
represented by a section in the pie graph.

Example:

Creating a Pie Graph

The following illustrates how to create a pie graph using a BY sort phrase and the LOOKGRAPH
command:

SET LOOKGRAPH=PIE
GRAPH FILE GGORDER
HEADING CENTER
"SAMPLE PIE CHART"
SUM QUANTITY
BY PRODUCT_DESC AS COFFEES
WHERE PRODUCT_DESC EQ 'French Roast' OR 'Hazelnut' OR 'Kona'
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1757

Selecting a Graph Type

Syntax:

How to Create a Scatter Graph

To create a scatter graph, issue a GRAPH request with the following display command and sort
field combination

{PRINT|SUM} fieldname1 [AND] fieldname2...
ACROSS sortfield

where:

fieldname

Is the name of the field to be displayed in the graph. There can be a maximum of 5 display
fields in a GRAPH request. When you specify more than one display field, they are
represented by different symbols.

AND

Is an optional phrase used to enhance readability. It can be used between any two field
names and does not affect the graph.

sortfield

Is the name of the numeric field to be displayed on the X-axis of the graph.

Example:

Creating a Scatter Graph

The following illustrates how to create a scatter graph:

GRAPH FILE GGORDER
HEADING CENTER
"Sample Scatter Graph"
PRINT QUANTITY AS 'Quantity'
ACROSS PRODUCT_CODE
WHERE PRODUCT_CODE EQ 'B144'
WHERE QUANTITY LT 51
END

1758

The output is:

24. Creating a Graph

Determining Graph Styles Using LOOKGRAPH

By default, a particular combination of display commands and sort phrases determines the
graph format. You can override the default graph format by using the LOOKGRAPH parameter.

The LOOKGRAPH parameter enables you to change the format of the graph without having to
set individual control parameters or restructure the graph request. However, even if you use
LOOKGRAPH, you can choose to set individual control parameters (for example, SET
GRID=ON).

Syntax:

How to Specify a Graph Style Using LOOKGRAPH

SET LOOKGRAPH= option

where:

option

Specifies the graph style. For details on graph styles, see:

Style Options for Line Graphs on page 1760.

Style Options for Bar Graphs on page 1761.

Style Options for Pie Graphs on page 1762.

Style Options for Scatter Graphs on page 1763.

Creating Reports With TIBCO® WebFOCUS Language

 1759

Selecting a Graph Type

Style Options for Three-Dimensional Graphs on page 1763.

Style Options for Area Graphs on page 1764.

Style Options for Stock Charts on page 1765.

Style Options for Polar Charts on page 1767.

Style Options for Radar Charts on page 1767.

Style Options for Bubble Charts on page 1767.

Style Options for Spectral Charts on page 1768.

Other Graph Types on page 1768.

Options for HTML5-Only Chart Types on page 1769.

Reference: Style Options for Line Graphs

Choose one of the following LOOKGRAPH values to change the style of connected point plots:

SET LOOKGRAPH=

Description

LINE

HLINE

HLINE2

HLINE2S

HLINSTK

HLINSTK2

HLNSTK2S

HLNSTKPC

A vertical connected point plot graph.

A horizontal connected point plot graph.

A horizontal connected point plot graph with two axes.

A horizontal connected point plot graph with two separate axes.

A stacked horizontal connected point plot graph.

A stacked horizontal connected point plot graph with two axes.

A stacked horizontal connected point plot graph with two separate
axes.

A stacked horizontal connected point plot graph showing
percentages.

VLINE

A vertical connected point plot graph.

1760

24. Creating a Graph

SET LOOKGRAPH=

Description

VLINE2

VLINE2S

VLINSTK

VLINSTK2

VLNSTK2S

VLNSTKPC

A vertical connected point plot graph with two axes.

A vertical connected point plot graph with two separate axes.

A stacked vertical connected point plot graph.

A stacked vertical connected point plot graph with two axes.

A stacked vertical connected point plot graph with two separate
axes.

A stacked vertical connected point plot graph showing
percentages.

Reference: Style Options for Bar Graphs

Choose one of the following LOOKGRAPH values to change the style of bar graphs:

SET LOOKGRAPH=

Description

BAR

STACK

VBAR

VBAR2AX

VBAR2AXS

VBRSTK1

VBRSTK2

VBRSTK2S

VBRSTKPC

A bar graph with the bars displayed beside each other.

A bar graph with stacked bars.

A vertical bar graph.

A vertical bar graph with two axes.

A vertical bar graph with two separate axes.

A stacked vertical bar graph.

A stacked vertical bar graph with two axes.

A stacked vertical bar graph with two separate axes.

A stacked vertical bar graph that shows percentages.

Creating Reports With TIBCO® WebFOCUS Language

 1761

Selecting a Graph Type

SET LOOKGRAPH=

Description

HBAR

HBAR2AX

HBAR2AXS

HBRSTK1

HBRSTK2

HBRSTK2S

HBRSTKPC

A horizontal bar graph.

A horizontal bar graph with two axes.

A horizontal bar graph with two separate axes.

A stacked horizontal bar graph.

A stacked horizontal bar graph with two axes.

A stacked horizontal bar graph with two separate axes.

A stacked horizontal bar graph that shows percentages.

Reference: Style Options for Pie Graphs

Choose one of the following LOOKGRAPH values to change the style of pie graphs:

SET LOOKGRAPH=

Description

PIE

PIESINGL

PIEMULTI

PIERING

PIEMULPR

PIEMULTP

PIEMULTR

A pie graph.

A single pie graph.

Multiple pie graphs.

A ring-shaped pie graph.

Multiple, ring-shaped pie graphs of proportional size.

Multiple pie graphs of proportional size.

Multiple, ring-shaped pie graphs.

1762

Reference: Style Options for Scatter Graphs

Choose one of the following LOOKGRAPH values to change the style of scatter graphs:

24. Creating a Graph

SET LOOKGRAPH=

Description

SCATTER

SCATTERD

SCATTRLS

SCATTRLD

Produces a scatter graph.

A dual scatter graph. Values from an additional data set are
displayed on a second value (Y) axis.

A scatter graph that labels each data point with its exact numeric
value.

A dual scatter graph that labels each data point with its exact
numeric value.

Reference: Style Options for Three-Dimensional Graphs

Choose one of the following LOOKGRAPH values to change the style of three-dimensional
graphs:

SET LOOKGRAPH=

Description

3DAREAG

3DAREAS

3DBAR

3D_BAR

3DCUBE

3DGROUP

3DOCTAGN

A three-dimensional connected group area chart.

A three-dimensional connected series area chart.

A two-dimensional bar graph with three-dimensional bars.

A three-dimensional chart with bars.

A three-dimensional bar graph in which all data points are blocks
of identical size, hovering at the position that shows their data
value.

A three-dimensional chart with bars.

A three-dimensional bar graph with octagon-shaped bars that have
no roots.

Creating Reports With TIBCO® WebFOCUS Language

 1763

Selecting a Graph Type

SET LOOKGRAPH=

Description

3DPYRAMD

3DRIBBNG

3DRIBBNS

3DSPHERE

3DSTACK

3DSURFCE

3DSURFHC

3DSURFSD

A three-dimensional pyramid chart.

A three-dimensional connected group ribbon chart.

A three-dimensional connected series ribbon chart.

A three-dimensional bar graph in which all data points are spheres
of identical size, hovering at the position that shows their data
value.

A two-dimensional stack chart with three-dimensional type bars.

A three-dimensional surface chart that graphs all data points as a
three-dimensional surface, like a rolling wave.

A three-dimensional honeycomb surface chart that graphs all data
points as a three-dimensional surface using a honeycomb effect.

A three-dimensional surface chart with sides that graphs all data
points as a three-dimensional surface with solid sides.

Reference: Style Options for Area Graphs

Choose one of the following LOOKGRAPH values to change the style of area graphs:

SET LOOKGRAPH=

Description

VAREA

VAREASTK

VAREAR2

VARESTK2

VARESTKP

HAREA

A vertical area graph.

A stacked vertical area graph.

A vertical area graph with two axes.

A stacked vertical area graph with two axes.

A stacked vertical area graph that shows percentages.

A horizontal area graph.

1764

24. Creating a Graph

SET LOOKGRAPH=

Description

HAREAR2

HAREASTK

HARESTK2

HARESTKP

A horizontal area graph with two axes.

A stacked horizontal area graph.

A stacked horizontal area graph with two axes.

A stacked horizontal area graph that shows percentages.

Reference: Style Options for Stock Charts

Choose one of the following LOOKGRAPH values to change the style of stock charts:

SET LOOKGRAPH=

Description

STOCK

STOCKH

STOCKHB

STOCKHD

STOCKHCL

A stock chart.

A high-low stock chart. Bars representing higher numeric values
are placed behind bars representing lower numeric values. Only
the top of the higher bar is visible, clearly illustrating the
difference in value.

The most popular application of this type of graph is to represent
stock prices. Each bar represents the highest and lowest prices
for a given stock on a given day.

A bipolar high-low stock chart. Values from different data sets are
displayed on separate poles.

A dual high-low stock chart. Values from an additional data set
are displayed on a second value (Y) axis.

A high-low-close stock chart. The most popular application of this
type of graph is to represent stock prices. Each bar represents
the highest, lowest, and closing prices for a given stock on a
given day.

Creating Reports With TIBCO® WebFOCUS Language

 1765

Selecting a Graph Type

SET LOOKGRAPH=

Description

STOCKHCB

A bipolar high-low-close stock chart. Values from different data
sets are displayed on separate poles.

The most popular application of this type of graph is to represent
stock prices. Each bar represents the highest, lowest, and closing
prices for a given stock on a given day.

STOCKHCD

A dual high-low-close stock chart. Values from an additional data
set are displayed on a second value (Y) axis.

STOCKHOC

A high-low-open-close stock chart.

The most popular application of this type of graph is to represent
stock prices. Each bar represents the highest, lowest, opening,
and closing prices for a given stock on a given day.

A bipolar high-low-open-close stock chart. Values from different
data sets are displayed on separate poles.

A dual high-low-open-close stock chart. Values from an additional
data set are displayed on a second value (Y) axis.

A high-low-volume stock chart.

A high-low-open-close-volume stock chart.

A candle stock chart.

A high-low candle stock chart.

A volume candle stock chart.

STOCKHOB

STOCKHOD

STOCKHV

STOCKHOV

STOCKC

STOCKHC

STOCKCV

STOCKHCV

A high-low-volume candle stock chart.

1766

24. Creating a Graph

Reference: Style Options for Polar Charts

Choose one of the following LOOKGRAPH values to change the style of polar charts:

SET LOOKGRAPH=

Description

POLAR

POLAR2

A polar chart that displays data points on a circle.

A dual polar chart. Values from an additional data set are
displayed on a second value (Y) axis.

Reference: Style Options for Radar Charts

Choose one of the following LOOKGRAPH values to change the style of radar charts:

SET LOOKGRAPH=

Description

RADARA

RADARL

RADARL2

A radar area chart.

A radar line chart.

A dual radar line chart. Values from an additional data set are
displayed on a second value (Y) axis.

Reference: Style Options for Bubble Charts

Choose one of the following LOOKGRAPH values to change the style of bubble charts:

SET LOOKGRAPH=

Description

BUBBLE

BUBBLED

BUBBLEDL

BUBBLEL

A bubble chart.

A bubble chart with a dual axis.

A bubble chart with a dual axis and labels.

A bubble chart with labels.

Creating Reports With TIBCO® WebFOCUS Language

 1767

Selecting a Graph Type

Reference: Style Options for Spectral Charts

Choose one of the following LOOKGRAPH values to change the style of spectral charts:

SET LOOKGRAPH=

Description

SPECTRAL

A spectral map chart. This is a chart with a row or column matrix
of markers that is colored according to the data values.

Reference: Other Graph Types

SET LOOKGRAPH=

Description

GANTT

POSITION

VWATERFL

HWATERFL

PARETO

MULTI3Y
MULTI4Y
MULTI5Y

Provides a visual representation of project oriented time critical
events. Gantt charts require six display fields and one sort field,
in that order. Conditional styling and drill-down are not supported
for GANTT charts.

Product position charts provide a visual representation of market
share and growth versus revenue and measurement (past,
present, future). Product position charts require a set of three
display fields.

Vertical waterfall graph.

Horizontal waterfall graph.

Displays data following Pareto 80:20 rule. Pareto charts require
only one display field.

Stacks charts in order to make it easier to read, analyze and
manage them.

1768

Reference: Options for HTML5-Only Chart Types

The following LOOKGRAPH values are valid only when generating an HTML5 chart:

SET LOOKGRAPH

Description

24. Creating a Graph

BUBBLEMAP

CHOROPLETH

MEKKO

PARABOX

STREAM

TAGCLOUD

TREEMAP

A bubblemap is a chart in which proportionally sized bubbles are
displayed on relevant areas of the map.

a chloropleth is a chart in which areas on a map are shaded or
patterned in proportion to the value of the measure being
represented,

A Mekko chart is a variant of a stacked bar chart, in which the
width of the bars is adjusted relative to its value in the data set.

A Parabox (or parallel coordinates chart) is similar to a regular line
chart, except that each group in the line chart has a unique and
interactive numeric axis. Each line represents one series of data.
Each vertical bar represents a numeric axis. You can click and
drag along each of the axes to select (filter) the lines that pass
through that part of the axis

A streamgraph is a simplified version of a stacked area chart. In a
streamgraph, there are no axes or gridlines. The baseline is free,
which makes it easier to perceive the thickness of any given layer
across the data.

A tagcloud is a visual representation of frequency. It displays only
group labels. The size of each label is proportional to its data
value.

A treemap chart displays hierarchical data as a set of nested
rectangles.

Selecting Values for the X and Y Axes

The values you select for the X- and Y-axes determine what data is included in the graph you
are creating, and how it appears.

Creating Reports With TIBCO® WebFOCUS Language

 1769

Selecting Values for the X and Y Axes

The X-axis value is determined by the sort phrase (BY or ACROSS) used in your GRAPH
request. At least one sort phrase is required in every GRAPH request. When there are multiple
BY phrases or when an ACROSS and BY phrase are included in the same request, multiple
graphs are generated, one for each combination of values for the fields referenced in the
request. For details, see Creating Multiple Graphs on page 1772.

The Y-axis value is determined from the display field associated with the display command
(SUM or PRINT) issued in your GRAPH request.

You can also:

Select a second horizontal category (X axis), which will produce multiple graphs. For details,
see Creating Multiple Graphs on page 1772.

Temporarily hide the display of a Y-axis field. For details, see Hiding the Display of a Y-Axis
Field on page 1771.

Interpolate X and Y axis values using linear regression. For details, see Interpolating X and
Y Axis Values Using Linear Regression on page 1771.

Example:

Selecting Values for the X and Y Axes

The following illustrates how to set the X-axis (PRODUCT_DESC) using an ACROSS phrase and
the Y-axis (QUANTITY) with the display command SUM:

GRAPH FILE GGORDER
SUM QUANTITY AS 'Ordered Units'
ACROSS PRODUCT_DESC
END

1770

The output is:

24. Creating a Graph

Hiding the Display of a Y-Axis Field

You can hide the display of a Y-axis field in a graph. This option is useful when you want to
temporarily remove a particular Y-axis field while retaining all of the original graph properties.

To temporarily hide the display of a Y-axis field, add the NOPRINT command to the field.
Although the NOPRINT command applies to both verb objects and sort fields in a TABLE
request, it only applies to verb objects in a GRAPH request.

Interpolating X and Y Axis Values Using Linear Regression

You can interpolate X and Y axis values using basic linear regression. Basic linear regression
involves the average of the summation of X and Y axis values to determine a linear equation
that expresses the trend of the scatter diagram. Use the SET parameter GTREND to turn on
basic linear regression in your graph.

GTREND is only available for use with scatter charts.

Creating Reports With TIBCO® WebFOCUS Language

 1771

Creating Multiple Graphs

Example:

Interpolating X and Y Axis Values Using Linear Regression

The following illustrates how to turn on linear regression in a scatter chart.

SET 3D=OFF
GRAPH FILE CAR
PRINT RC
ACROSS DC
ON GRAPH SET LOOKGRAPH SCATTER
ON GRAPH SET GTREND ON
END

The output is:

Creating Multiple Graphs

You can create multiple graphs by including secondary sort dimensions (fields).

By default, the number of graphs created depends on the number of values in the fields you
designate in the sort (BY, ACROSS) phrases. You can change this default using the GRMERGE
parameter:

With GRMERGE OFF (the default), if a request contains two BY fields, there will be as many
graphs as there are values in the first BY field. The second BY field will determine the X-
axis. For example, if you have selected a BY field with two values, two graphs will be
generated. If you have selected a field with ten values, ten graphs will be generated. If
there is one BY phrase and one ACROSS phrase, as many graphs will display as there are
values in the BY field. The ACROSS field will determine the X-axis. You can select the
second horizontal category by including multiple BY phrases or an ACROSS and BY phrase
in the same request.

1772

24. Creating a Graph

With GRMERGE ON, WebFOCUS creates one merged graph.

With GRMERGE ADVANCED, WebFOCUS uses three parameters to determine:

How many graphs to generate (GRMULTIGRAPH).

How many sort fields should be placed on the graph legend (GRLEGEND).

How many sort fields should be placed on the X-axis (GRXAXIS).

Multiple graphs can be displayed in either merged format or in columns. For details, see
Merging Multiple Graphs on page 1773 and Displaying Multiple Graphs in Columns on page
1778.

Merging Multiple Graphs

By default, when you create a graph that has multiple BY fields, or a BY and ACROSS field,
multiple graphs are generated. You can merge these graphs into a single graph or into multiple
merged graphs.

To do this, use the SET command GRMERGE.

Syntax:

How to Merge Multiple Graphs

SET GRMERGE={ON|OFF|ADVANCED}

where:

ON

Turns on the merge graph option.

OFF

Turns off the merge graph option. This is the default.

ADVANCED

Turns on the advanced merge option. This option uses three parameters to determine how
to merge the graphs:

GRMULTIGRAPH, which specifies how many sort fields to use to create multiple graphs.

GRLEGEND, which specifies how many sort fields to place on the graph legend.

GRXAXIS, which specifies how many sort fields to display on the X-axis. GRXAXIS must
be at least 1 in order to plot the graph. A value greater than one creates nested X-axes.

Note: The sum of the sort fields used by GRMULTIGRAPH, GRLEGEND, and GRXAXIS must
equal the number of sort fields in the graph request.

Creating Reports With TIBCO® WebFOCUS Language

 1773

Creating Multiple Graphs

The syntax for the GRMULTIGRAPH, GRLEGEND, and GRXAXIS parameters is:

ON GRAPHSET GRMULTIGRAPH n

Specifies how many sort fields (0 through 2) to use to break the output into multiple
graphs. The outermost sort fields are used to separate the graphs. When n is greater
than zero, this is similar to GRMERGE=OFF, but allows an additional sort field.

ON GRAPH SET GRLEGEND n

Specifies how many of the remaining outermost sort fields (0 through 2), after the
ones used for GRMULTIGRAPH, to add to the graph legend. When n is greater than
zero, this is similar to GRMERGE=ON, but allows an additional sort field.

ON GRAPH SET GRXAXIS n

Specifies how many of the remaining sort fields (1 through 3) to display on the X-axis.
When n is greater than 1, this creates nested X-axes.

Example: Merging Multiple Graphs With GRMERGE ON

The following illustrates a graph with two horizontal, or X-axes, categories (PRODUCT_ID and
PACKAGE_TYPE) that have been merged.

SET GRMERGE=ON
GRAPH FILE GGORDER
SUM UNIT_PRICE ORDER_NUMBER
ACROSS PRODUCT_ID
BY PACKAGE_TYPE
END

1774

The output is:

24. Creating a Graph

Example: Merging Multiple Graphs With GRMERGE ADVANCED

The following example generates a vertical bar graph that separates the outermost sort field
(REGION) onto separate graphs, distinguishes the next two sort fields (ST and CATEGORY) by
combining them on the graph legend, and places the CATEGORY sort field on the X-axis:

GRAPH FILE GGSALES
SUM DOLLARS
BY REGION BY ST BY CATEGORY BY PRODUCT
WHERE CATEGORY EQ 'Food' OR 'Gifts'
WHERE PRODUCT EQ 'Coffee Pot' OR 'Biscotti' OR 'Mug'
ON GRAPH SET GRMERGE ADVANCED
ON GRAPH SET GRMULTIGRAPH 1
ON GRAPH SET GRLEGEND 2
ON GRAPH SET GRXAXIS 1
ON GRAPH SET LOOKGRAPH VBAR
END

Creating Reports With TIBCO® WebFOCUS Language

 1775

Creating Multiple Graphs

The first graph is for region Midwest. The legend distinguishes State-Category combinations by
color, and the PRODUCT sort field is repeated on the X-axis for each State-Category
combination:

Merging Multiple OLAP Graphs

When you create an OLAP graph that has multiple BY fields, or a BY and ACROSS field,
multiple graphs are generated. You can merge these graphs into a single graph.

To do this, use the SET command OLAPGRMERGE.

Syntax:

How to Merge Multiple OLAP Graphs

SET OLAPGRMERGE={ON|OFF}

where:

Turns on the merge graph option. With this setting AUTODRILL is disabled for the graph.

Turns off the merge graph option and creates a separate graph for every value of the outer
sort field. OFF is the default value.

ON

OFF

1776

Example: Merging OLAP-Enabled Graphs

The following OLAP request against the EMPLOYEE data source has two BY fields. To merge
the graphs, the SET OLAPGRMERGE=ON command is issued:

24. Creating a Graph

-OLAP ON
SET GRAPHEDIT=SERVER
SET OLAPGRMERGE=ON
TABLE FILE EMPLOYEE
SUM SALARY
BY DEP
BY LAST_NAME
ON TABLE SET PAGE-NUM OFF
ON TABLE NOTOTAL
ON TABLE PCHOLD FORMAT HTML
ON TABLE SET HTMLCSS ON
ON GRAPH SET HAXIS 300
ON GRAPH SET VAXIS 100
ON TABLE SET AUTODRILL ALL
ON TABLE SET OLAPPANE TABBED
ON TABLE SET STYLE *
     INCLUDE = endeflt,
$
     LEFTMARGIN=0.500000,
     RIGHTMARGIN=0.500000,
     TOPMARGIN=0.500000,
     BOTTOMMARGIN=0.500000,
$
TYPE=REPORT,
     TOPGAP=0.000000,
     BOTTOMGAP=0.013889,
$
ENDSTYLE
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1777

Creating Multiple Graphs

Displaying Multiple Graphs in Columns

When you create a graph that has multiple BY fields, or a BY and ACROSS field, multiple
graphs are generated. You can display these graphs in columns.

To do this, use the SET command GRWIDTH. GRWIDTH may be set to any value between
0-512. The default is 0.

Syntax:

How to Display Multiple Graphs in Columns

SET GRWIDTH=nn

where:

nn

Is the number of columns in which to display multiple graphs. This may be any value from
0-512. The default is 0.

All values from 1-512 will display graphs in an HTML table with the corresponding number
of columns. The default value of 0 will display the graphs one under the other in a Java
applet.

Example:

Displaying Multiple Graphs in Columns

The following illustrates how to set the number of columns in which you wish to display
multiple graphs. In this example, the graphs are set to display in two columns.

SET GRWIDTH=2
GRAPH FILE GGORDER
SUM UNIT_PRICE ORDER_NUMBER
ACROSS PRODUCT_ID
BY PACKAGE_TYPE
END

The output is:

1778

Plotting Dates in Graphs

24. Creating a Graph

Numeric fields containing dates are recognized by the field formats specified in the Master
File. Such fields can be used in ACROSS or BY phrases in GRAPH requests. To review the
various format types, refer to the Describing Data With WebFOCUS Language manual.

Plotted dates are handled in the following manner:

If the date field named has a month-first format, it is plotted in ascending time order (even
if the file is not sorted in ascending date order). Hence, month/year values of 01/76,
03/76, 09/75 will be plotted by month within year: 09/75, 01/76, 03/76.

Axis scaling is performed on the basis of days in the month and months in the year. When
the date format includes the day, the scale usually starts at the first day of the month, at
the "zero" axis point.

You can selectively combine groups of date point plots to reduce the number of separate
points on the horizontal axis. You do this with the IN-GROUPS-OF option. For example, if the
date field format is I6YMD, you can display the data by month rather than by day by grouping it
in 30-day increments:

ACROSS DATE IN-GROUPS-OF 30

This eliminates plot points for individual days. If your date format is YMD, you can redefine the
format and divide the field contents by 100 to eliminate the days:

DATE/I4YM=DATE/100

Example:

Including Date Fields in a Graph

The following example illustrates how month-first formatted date fields are displayed in a
graph.

SET GRMERGE = ON
GRAPH FILE GGORDER
SUM QUANTITY
ACROSS ORDER_DATE
BY PRODUCT_DESC
WHERE PRODUCT_DESC EQ 'French Roast' OR 'Hazelnut' OR 'Kona' AND
ORDER_DATE GE '010197'
END

Creating Reports With TIBCO® WebFOCUS Language

 1779

Plotting Dates in Graphs

The output is:

Basic Date Support for X and Y Axes

OLDDATES can be manipulated accordingly with the usage of YRTHRESH and DEFCENT SET
parameters. If you do not specify the YRTHRESH and DEFCENT commands for dates with the Y
format (for example, YMD, MDY, DMY, YM, etc.), the code will assume the format 19XX.

Reference: Date Support Limitations

The following date formats are supported:

SHORT (18) is completely numeric, such as 12/13/52 or 3:30pm.

MEDIUM (19) is longer, such as Jan 12, 1952.

LONG (20) is longer, such as January 12, 1952 or 3:30:32pm.

FULL (21) is almost completely specified, such as Tuesday, April 12, 1952 AD or
3:30:42pm PST.

The default date format for the X and Y axes is MEDIUM. You can overwrite the default by
using one of the following API calls (where xx is one of the numbers listed above):

setTextFormatPreset(getX1Label(),xx); // for X Axis

setTextFormatPreset(getY1Label(),xx); // for Y Axis

1780

24. Creating a Graph

The default date format for Data Text is LONG. This only applies to graphs with dates on
the Y axis. Currently this format is not supported on the X axis. You can overwrite the
default by using the following API call:

setDataTextFormat(xx);

For more information, see Customizing Graphs Using the Graph API and HTML5 JSON
Properties on page 1807.

In a graph with dates on the X axis and numeric fields on the Y axis, the tool tip displays
the data format of the graph by default. This means that a date value will display its raw
GMT value in milliseconds. This does not occur for dates on the Y axis and strings on the X
axis, because the data format is already in date format.

DATETIME is not fully supported.

The ability to set the start and end dates for the appropriate axis is not supported.

The ability to set the step for dates is not supported.

Formatting Dates for Y-Axis Values

You can display date-formatted numbers for Y-axis fields and on tool tips. The following date
formats are supported:

Display Format

Corresponding WebFOCUS Format

yy/mm/dd

yy/mm

mm/dd/yyyy

mm/dd/yy

mm/dd

YMD

YM

MDYY

MDY

MD

For complete details on date formats, see the Describing Data With WebFOCUS Language
manual.

Refining the Data Set For Your Graph

After selecting field values for the X and Y axes, you may wish to limit the data that displays in
your graph. You can do this by creating WHERE statements. A WHERE statement limits data by
creating parameters the data must satisfy before it is included in the data set.

Creating Reports With TIBCO® WebFOCUS Language

 1781

Displaying Missing Data Values in a Graph

For details on WHERE, WHERE TOTAL, and IF phrases, see Selecting Records for Your Report
on page 217.

Example:

Specifying WHERE Criteria in a Graph Request

The syntax for WHERE, WHERE TOTAL, and IF phrases in a GRAPH request is identical to that
used in a TABLE request.

The following graph request shows data for specific product descriptions, namely French
Roast, Hazelnut, or Kona.

GRAPH FILE GGORDER
SUM QUANTITY
BY PRODUCT_DESC
WHERE PRODUCT_DESC EQ 'French Roast' OR 'Hazelnut' OR 'Kona'
END

The output is:

Displaying Missing Data Values in a Graph

You can display missing data values (in a bar graph, line graph, area graph, or any variation of
these graph types) in one of the following formats:

Graph as zero. In bar graphs, a bar appears on the zero line. In line graphs, a solid line
connects the missing value with the succeeding value. In area graphs, the area appears on
the zero line.

Graph as gap. In all graph types (bar, line, or area), missing values appear as a gap in the
graph.

1782

24. Creating a Graph

Dotted line to zero. In line graphs, a dotted line connects the missing value with the
succeeding value. In 3D bar graphs, solid lines outline the flat bar corresponding to the
missing value. In 2D bar graphs, a gap appears in the graph. In area graphs, a transparent
area extends down to the zero line and then up to the succeeding value.

Interpolated dotted line. In a line graph, missing values appear as an interpolated dotted
line that connects the plot points immediately preceding and succeeding the missing value.
In bar and area graphs, missing values display as an interpolated (transparent) bar or area.

Note: You can specify a default value (other than the default value of zero) to represent
missing data. To do this use a DEFINE command. For details, see Handling Records With
Missing Field Values on page 1035.

Syntax:

How to Display Missing Values in a Graph

GRAPH FILE filename
.
.
.
SET VZERO={ON|OFF}
ON GRAPH SET STYLE *
*GRAPH_SCRIPT
API call
*END
ENDSTYLE
END

where:

ON

Displays missing values as zero. An API call is not necessary when VZERO is set to ON.
Alternatively, you can add ON GRAPH SET VZERO ON.

OFF

Displays missing values as a gap, a dotted line to zero, or, an interpolated dotted line,
depending on the API call that is added. Alternatively, you can add ON GRAPH SET VZERO
OFF.

API call

Determines how missing values display in the graph when VZERO is set to OFF. Possible
values are:

setFillMissingData(0); displays missing values as a gap.

setFillMissingData(1); displays missing values as a dotted line to zero.

Creating Reports With TIBCO® WebFOCUS Language

 1783

Displaying Missing Data Values in a Graph

setFillMissingData(2); displays missing values as an interpolated dotted line.

Example:

Displaying Missing Values as Zero In a Graph

The following illustrates how missing values are represented in a bar graph when designated to
appear as zero. The CURR_SAL value for Seay is missing, as well as the RAISE value for Bryant
and Huntley.

SET LOOKGRAPH=BAR
SET GRAPHEDIT=SERVER
SET GRID=ON
SET VZERO=ON
GRAPH FILE MSFATIA
SUM CUR_SAL
RAISE
ACROSS LAST_NAME
ON GRAPH SET STYLE *
*GRAPH_SCRIPT
setTextRotation(getO1Label(),0);
*END
ENDSTYLE
END

The output is:

1784

Example:

Displaying Missing Values as a Gap

The following illustrates how missing values are represented in a bar graph when designated to
appear as a gap. The CURR_SAL value for Seay is missing, as well as the RAISE value for
Bryant and Huntley.

24. Creating a Graph

SET LOOKGRAPH=BAR
SET GRAPHEDIT=SERVER
SET GRID=ON
SET VZERO=OFF
GRAPH FILE MSFATIA
SUM CUR_SAL
RAISE
ACROSS LAST_NAME
ON GRAPH SET STYLE *
*GRAPH_SCRIPT
setFillMissingData(0);
setTextRotation(getO1Label(),0);
*END
ENDSTYLE
END

The output is:

Creating Reports With TIBCO® WebFOCUS Language

 1785

Displaying Missing Data Values in a Graph

Example:

Displaying Missing Values as a Dotted Line to Zero

The following illustrates how missing values are represented in a line graph when designated
to appear as a dotted line to zero. The CURR_SAL value for Seay is missing, as well as the
RAISE value for Bryant and Huntley.

SET LOOKGRAPH=LINE
SET GRAPHEDIT=SERVER
SET GRID=ON
SET VZERO=OFF
GRAPH FILE MSFATIA
SUM CUR_SAL
RAISE
ACROSS LAST_NAME
ON GRAPH SET STYLE *
*GRAPH_SCRIPT
setFillMissingData(1);
setTextRotation(getO1Label(),0);
*END
ENDSTYLE
END

The output is:

1786

Example:

Displaying Missing Values as an Interpolated Dotted Line

The following illustrates how missing values are represented in a line graph when designated
to appear as an interpolated dotted line. The CURR_SAL value for Seay is missing, as well as
the RAISE value for Bryant and Huntley.

24. Creating a Graph

SET LOOKGRAPH=LINE
SET GRAPHEDIT=SERVER
SET GRID=ON
SET VZERO=OFF
GRAPH FILE MSFATIA
SUM CUR_SAL
RAISE
ACROSS LAST_NAME
ON GRAPH SET STYLE *
*GRAPH_SCRIPT
setFillMissingData(2);
setTextRotation(getO1Label(),0);
*END
ENDSTYLE
END

The output is:

Applying Conditional Styling to a Graph

You can add further value to your graph by using conditional styling to highlight certain defined
data with specific styles and colors.

Creating Reports With TIBCO® WebFOCUS Language

 1787

Applying Conditional Styling to a Graph

For example, you can apply the color red to all departments that did not reach their sales
quotas and apply the color black to all departments that did reach their sales quotas. In this
example, the user can view quickly which departments did or did not reach their quotas. To
examine how the results of one department may impact the results of a second department,
you may want to provide a drill-down to a report that examines this possibility.

You can apply color to the following graph types:

Bar graphs.

Three-dimensional graphs with noncontinuous plot points.

Pie graphs.

Stack charts.

You can apply conditional styling using StyleSheets.

Note: Conditional styling is only supported for Y-axis values.

Syntax:

How to Apply Conditional Styling to a Graph

TYPE=DATA,[COLUMN|ACROSSCOLUMN=Nn,]COLOR=color, [WHEN=expression,]$

where:

DATA

Identifies data as the graph component to which color is being applied. This value must
appear at the beginning of the declaration.

COLUMN|ACROSSCOLUMN

Is the graph subcomponent to which you want to apply color. Valid graph subcomponents
are COLUMN and ACROSSCOLUMN.

Nn

Identifies a column by its position in the report. To determine this value, count BY fields,
display fields, and ROW-TOTAL fields, from left to right, including NOPRINT fields. For
details, see Identifying a Report Component in a WebFOCUS StyleSheet on page 1249.

color

Identifies the color that you want to apply to the graph component or subcomponent. For a
list of valid colors, see Formatting Report Data on page 1697.

1788

24. Creating a Graph

expression

Is any Boolean expression that specifies conditions for applying the specified color to the
graph component. The expression must be valid on the right side of a COMPUTE
command. For details, see Using Expressions on page 429.

Note: IF... THEN ... ELSE logic is not necessary in a WHEN clause and is not supported.

All non-numeric literals in a WHEN expression must be specified within single quotation
marks.

Example:

Applying Conditional Styling to a Graph

The following illustrates how you can apply conditional styling to a graph.

   GRAPH FILE GGSALES
   SUM UNITS DOLLARS ACROSS PRODUCT
   ON GRAPH SET STYLE *
1. TYPE=DATA,COLOR=BLUE,$
2. TYPE=DATA,ACROSSCOLUMN=N2,COLOR=FIREBRICK,$
3. TYPE=DATA,ACROSSCOLUMN=N2,COLOR=SILVER,WHEN=N2 GT 5000000,$
4. TYPE=DATA,ACROSSCOLUMN=N1,COLOR=LIME,WHEN=N1 LT 200000,$
   ENDSTYLE
   END

1. This line specifies blue as the default data color.

2. This line specifies firebrick as the default color for the DOLLARS column.

3. This line specifies silver as the color for the DOLLARS column when the value for DOLLARS

is greater than five million.

4. This line specifies lime as the UNITS column color when the number of UNITS is less than

two hundred thousand.

Creating Reports With TIBCO® WebFOCUS Language

 1789

Linking Graphs to Other Resources

The output is:

Linking Graphs to Other Resources

To drill down to a more detailed level of information in a graph, you can link a procedure
(FOCEXEC) or a URL to one or more values in your graph. When you run your graph, the
selected values become "hot spots" that invoke the underlying procedure, JavaScript function,
or URL.

The JSURLS parameter includes JavaScript or VBScript files in an HTML graph. This allows you
to customize the display of WebFOCUS HTML graphs with any JavaScript or VBScript functions.
The JavaScript and VBScript files are the last files loaded, and are loaded in the order they are
listed, allowing complete customization of the HTML page.

This feature works with any graph format that outputs an HTML document, for example
JSCHART and PCHOLD FORMAT PNG.

In addition, when a WebFOCUS graph is run, a set of pre-defined JavaScript functions is
invoked. Using JSURLS, you can disable or modify these default functions. To view the full set
of pre-defined JavaScript functions, see /ibi/WebFOCUSxx/ibi_apps/ibi_html/javaassist/ibi/
html/js/ibigl.js.

The syntax is:

SET JSURLS='/file1 [/file2] [/file3]...'

1790

24. Creating a Graph

where:

/file1 [/file2] [/file3]...

Are the files that contain JavaScript or VBScript. If there is more than one js file, the
delimiter is a blank and the values must be enclosed in single quotes. Files must be in a
location that is accessible by the web server. The total length of the value is limited to 256
bytes.

You can reference files with a URL.

Syntax:

How to Link a Graph to Another Request

TYPE=DATA,[COLUMN|ACROSSCOLUMN=Nn,]COLOR=color,[WHEN=expression,]
FOCEXEC=fex[(parameters ...),]$

where:

DATA

Identifies Data as the graph component to which the user is applying the color. The TYPE
attribute and its value must appear at the beginning of the declaration.

COLUMN|ACROSSCOLUMN

Is the graph subcomponent to which you want to apply color. Valid graph subcomponents
are COLUMN and ACROSSCOLUMN.

color

Identifies the color that you want to apply to the graph component or subcomponent. For a
list of valid colors, see Formatting Report Data on page 1697.

Nn

Identifies a column by its position in the report. To determine this value, count BY fields,
display fields, and ROW-TOTAL fields, from left to right, including NOPRINT fields. For more
information, see Identifying a Report Component in a WebFOCUS StyleSheet on page 1249.

FOCEXEC=fex

Identifies the file name of the linked procedure to run when a user selects the report
object.

parameters

Are values to be passed to the procedure. You can pass one or more values, using any
combination of the following methods:

You can specify a constant value, enclosed in single quotation marks.

Creating Reports With TIBCO® WebFOCUS Language

 1791

Linking Graphs to Other Resources

You can specify the name or the position of a graph column.

You can specify the name of a Dialogue Manager amper variable to pass its value.

You can use amper variables only in inline StyleSheets.

Note: The usual use of an amper variable is to pass a constant value, in which case, it
would have to be embedded in single quotation marks. For example:

'&ABC'.

The method you can use to pass values can vary, depending on the method you use to
execute the hyperlink. You can pass one or more values. The entire string of values must
be enclosed in parentheses, and separated from each other by a blank space.

expression

Is any Boolean expression that specifies conditions for applying the specified color to the
graph component. The expression must be valid on the right side of a COMPUTE
command. For details, see Using Expressions on page 429.

Note: IF ... THEN ... ELSE logic is not necessary in a WHEN clause and is not supported.

All non-numeric literals in a WHEN expression must be specified within single quotation
marks.

Example:

Linking to Additional Reports or Graphs

In this example, when the value for UNITS is less than four hundred thousand, the color is lime
and you can drill-down to a detail report.

GRAPH FILE GGSALES
SUM UNITS DOLLARS ACROSS PRODUCT
ON GRAPH SET STYLE *
TYPE=DATA,COLOR=SILVER,$
TYPE=DATA,ACROSSCOLUMN=N1,COLOR=LIME,WHEN=N1 LT 400000,FOCEXEC=GRAPH2,$
ENDSTYLE
END

1792

The output is:

24. Creating a Graph

Syntax:

How to Link to a URL

You can define a link from any component to any URL including webpages, websites, Servlet
programs, or non-World Wide Web resources, such as an email application. After you have
defined a link, you can select the component to access the URL.

The links you create can be dynamic. With a dynamic link, your selection passes the value of
the selected component to the URL. The resource uses the passed value to dynamically
determine the results that are returned. You can pass one or more parameters. For details,
see Creating Parameters on page 854.

TYPE=type, [subtype], URL=url[(parameters ...)], [TARGET=frame,] [ALT =
'description',] $

where:

type

Identifies the report or graph component that you select in the web browser to execute the
link. The TYPE attribute and its value must appear at the beginning of the declaration.

subtype

Are any additional attributes, such as COLUMN, LINE, or ITEM, that are needed to identify
the report component that you are formatting. For information on identifying components,
see Identifying a Report Component in a WebFOCUS StyleSheet on page 1249.

Creating Reports With TIBCO® WebFOCUS Language

 1793

Linking Graphs to Other Resources

url

Identifies any valid URL, including a URL that specifies a WebFOCUS Servlet program, or
the name of a report column enclosed in parentheses whose value is a valid URL to which
the link will jump.

Note:

The maximum length of a URL=url argument, including any associated variable=object
parameters, is limited by the maximum number of characters allowed by the browser.
For information about this limit for your browser, search on your browser vendor's
support site. The URL argument can span more than one line, as described in Creating
and Managing a WebFOCUS StyleSheet on page 1197.

Note that the length of the URL is limited by the maximum number of characters
allowed by the browser. For information about this limit for your browser, search on your
browser vendor’s support site.

If the URL refers to a WebFOCUS Servlet program that takes parameters, the URL must
end with a question mark (?).

parameters

Values that are passed to the URL. For details, see Creating Parameters on page 854.

frame

Identifies the target frame in the webpage in which the output from the drill-down link is
displayed. For details, see Specifying a Target Frame on page 873.

description

Is a textual description of the link supported in an HTML report for compliance with Section
508 accessibility. Enclose the description in single quotation marks.

The description also displays as a pop-up description when your mouse or cursor hovers
over the link in the report output.

Syntax:

How to Link to a JavaScript Function

You can use a StyleSheet to define a link to a JavaScript function from any report or graph
component. After you have defined the link, you can select the component to execute the
JavaScript function.

Just as with drill-down links to procedures and URLs, you can specify optional parameters that
allow values of a component to be passed to the JavaScript function. The function will use the
passed value to dynamically determine the results that are returned to the browser. For
details, see Creating Parameters on page 854.

1794

24. Creating a Graph

Note:

JavaScript functions can, in turn, call other JavaScript functions.

You cannot specify a target frame if you are executing a JavaScript function. However, the
JavaScript function itself can specify a target frame for its results.

TYPE=type, [subtype], JAVASCRIPT=function[(parameters ...)], $

where:

type

Identifies the report component that you select in the web browser to execute the link. The
TYPE attribute and its value must appear at the beginning of the declaration.

subtype

Are any additional attributes, such as COLUMN, LINE, or ITEM, that are needed to identify
the report component that you are formatting. See Identifying a Report Component in a
WebFOCUS StyleSheet on page 1249 for details.

function

Identifies the JavaScript function to run when you select the report component.

The maximum length of a JAVASCRIPT=function argument, including any associated
parameters, is 2400 characters and can span more than one line. If you split a single
argument across a line, you need to use the \ character at the end of the first line, as
continuation syntax. If you split an argument at a point where a space is required as a
delimiter, the space must be before the \ character or be the first character on the next
line. The \ character does not act as the delimiter.

In this example,

JAVASCRIPT=myfunc(COUNTRY \
CAR MODEL 'ABC'),$

the argument correctly spans two lines.

Note:

You can use the SET JSURLS command or the Dialogue Manager -HTMLFORM
command to embed the chart into an HTML document in which the function is defined.

When you have an HTML document called by -HTMLFORM, ensure that the file
extension is .HTM (not .HTML).

Creating Reports With TIBCO® WebFOCUS Language

 1795

Linking Graphs to Other Resources

For more information about the -HTMLFORM command, see the Developing Reporting
Applications manual.

parameters

Values that are passed to the JavaScript function. For details, see Creating Parameters on
page 854.

Syntax:

How to Create Multiple Drill-Down Links

TYPE=type, [subtype], DRILLMENUITEM='description'|'DrillDown n',
     type_of_link

where:

type

Identifies the component that you select in the web browser to execute the link. The TYPE
attribute and its value must appear at the beginning of the declaration.

subtype

Are any additional attributes, such as COLUMN, LINE, or ITEM, that are needed to identify
the component that you are formatting. See Identifying a Report Component in a
WebFOCUS StyleSheet on page 1249 for information on identifying report components.

description

Is the text that appears on the pop-up menu of drill-down options on the output. The
default value is DrillDown n, where n is a consecutive integer, such as DrillDown 1,
DrillDown 2, and so on.

type_of_link

Is the type of link, for example, a link to a detail report or URL. For a summary of valid
values, see Summary of Drill-Down Links on page 847.

Reference: Syntax Guidelines

You can create multiple drill-down links from a component on a summary request, chosen from
any combination of supported actions. For example, you can create links to a detail report,
chart, or Maintain procedure, a JavaScript function, and a URL. When you click a component in
the summary request, a pop-up menu appears listing the drill-down options.

This feature does not apply to headings or footings,

When you create multiple drill-down links, you cannot specify a single drill-down action (for
example, FOCEXEC or URL) before the first DRILLMENUITEM.

1796

24. Creating a Graph

The menu created by the DRILLMENUITEM keyword is styled using a Cascading Stylesheet file.
The file is /ibi/WebFOCUSxx/ibi_apps/ibi_html/javaassist/ibi/html/js/multidrill.css, where xx
is the version and major release number of WebFOCUS.

Tip: You can make changes to the /ibi/WebFOCUS82/ibi_apps/ibi_html/javaassist/ibi/
html/js/multidrill.css file to affect the font, size, and color of the DRILLMENUITEM menu.

Make a backup of the /ibi/WebFOCUS82/ibi_apps/ibi_html/javaassist/ibi/html/js/
multidrill.css file.

Modify the multidrill.css file, with the desired changes.

Rename the multidrill.css.gz file. This file resides in the same location as the multidrill.css
file.

Clear cache.

Restart the Reporting Server.

Reference: Summary of Drill-Down Links

You can link to:

Another request. The StyleSheet attribute is FOCEXEC.

A URL. The StyleSheet attribute is URL. You pass a valid URL.

Note that the length of the URL is limited by the maximum number of characters allowed by
the browser. For information about this limit for your browser, search on the support site for
your browser vendor.

A URL from a field. The StyleSheet attribute is URL. You pass the name of a report column
whose value is a valid URL to which the link will jump.

A JavaScript function. The StyleSheet attribute is JAVASCRIPT.

A WebFOCUS Maintain procedure. The StyleSheet attribute is URL with the keyword
MNTCON EX. For details on the syntax, see Linking to a Maintain Data Procedure on page
836.

A WebFOCUS compiled Maintain procedure. The StyleSheet attribute is URL with the
keyword MNTCON RUN. For details on the syntax, see Linking to a Maintain Data Procedure
on page 836.

Creating Reports With TIBCO® WebFOCUS Language

 1797

Adding Labels to a Graph

Creating Parameters

Parameters allow you to specify criteria and conditions for the linked (drill down) report. By
defining parameters, you can control the amount and type of information to retrieve when you
click on a hot spot.

For complete details, see Linking a Report to Other Resources on page 819.

Adding Labels to a Graph

Adding labels to your graph helps provide important information about what the data in your
graph represents. You may choose to add headings and/or footings to your graph, as well as
horizontal (X) and vertical (Y) axis labels.

You can add a heading or footing to your graph using the HEADING or FOOTING phrase. The
syntax is the same as that used for headings and footings in TABLE requests. You can also
embed field values in graph headings and footings. This capability is particularly useful for
annotating graphs that contain multiple sort fields.

For details on headings, footings, and embedded fields, see Using Headings, Footings, Titles,
and Labels on page 1517.

Note: If your graph labels or legends are not appearing correctly when you run your graph, see
How to Change Color Settings on page 1815 for details on correcting this.

Example:

Adding a Heading and Footing to a Graph

The following illustrates how to add a heading with an embedded field value to your graph. In
this example, the heading is "Total Coffee Orders" with the embedded field TOT.QUANTITY.

GRAPH FILE GGORDER
HEADING CENTER
"Total Coffee Orders: <TOT.QUANTITY "
SUM QUANTITY
BY PRODUCT_DESC
WHERE PRODUCT_DESC EQ 'French Roast' OR 'Hazelnut' OR 'Kona'
FOOTING CENTER
"For year-end orders"
END

1798

The output is:

24. Creating a Graph

Adding Vertical (Y-axis) and Horizontal (X-axis) Labels to a Graph

Vertical (Y-axis) and horizontal (X-axis) graph labels are placed on the graph according to the
display fields and sort fields specified in the request. The titles that appear on the graph are
the titles that appear in the Master File for that particular field.

The vertical (Y-axis) title of the graph is determined by the display field. Note that when the
number of Y-axis labels is greater than one, the labels do not appear along the Y-axis. Instead,
the labels appear in a legend that provides the names of the fields being graphed.

The horizontal (X-axis) title of the graph is determined by the sort field.

You can replace a title by using an AS phrase in the GRAPH request.

Applying Custom Styling to a Graph

You can customize your graph using StyleSheets and SET commands. You can set the graph
width and height, set fixed scales for the X and Y axes, enable the Graph Editor, and use
Graph API calls to further customize your graph.

Creating Reports With TIBCO® WebFOCUS Language

 1799

Applying Custom Styling to a Graph

For details on customizing graph headings and footings, see Using Headings, Footings, Titles,
and Labels on page 1517.

Setting the Graph Height and Width

The width (or horizontal axis) of each graph, which includes any surrounding text, is
automatically set to 760 pixels. When setting the graph width, you should allow for the
inclusion of any text required for the vertical axis and its labels along the left margin.

To maximize display space, you can limit the size of your labels through the use of either AS
phrases or DECODE expressions.

The height (or vertical axis) of your graph is automatically set to 405 pixels.

The vertical axis is automatically set (VAUTO=ON) to cover the total range of plotted values.
The height of the axis is set as high as possible (taking into consideration the presence of any
headings or footings and the need to provide suitably rounded vertical class markers). The
range is divided into intervals called "classes." The scale is normalized to provide class values
rounded to the appropriate multiples and powers of 10 for the intervals plotted on the axis.

Syntax:

How to Set the Graph Width

SET HAXIS={nn|760}

where:

{nn|760}

Is a positive numeric value. The default is 760 pixels.

Note: The maximum HAXIS size for SVG graphs is 40 inches.

Syntax:

How to Set the Graph Height

SET VAXIS={nn|400}

where:

{nn|400}

Is a positive numeric value. The default is 400 pixels.

Note: The maximum VAXIS size for SVG graphs is 40 inches.

Customizing Graphs Using SET Parameters

The GRAPH environment includes a set of parameters that control the appearance of the graph
and offer some additional control when you run the request.

1800

For example, the BSTACK parameter enables you to specify that the bars on a bar graph are to
be stacked rather than placed side by side.

Syntax:

How to Use SET Parameters With GRAPH Requests

24. Creating a Graph

To set the parameters that control the GRAPH environment, use the appropriate variation of
the SET parameter.

SET parameter=value,parameter=value...

For a list of supported GRAPH parameters, see Values and Functions of SET Parameters for
Graphs on page 1801.

Note:

Repeat the command SET on each new line.

When entering more than one parameter on a line, separate them with commas.

You can use unique truncations of parameter names. You must make sure that they are
unique.

Example:

Using SET Parameters With GRAPH Requests

The following shows how to set the height (Y-axis) and width (X-axis) for a graph.

SET HAXIS=75,VAXIS=40
GRAPH FILE filename
.
.
.
END

Reference: Values and Functions of SET Parameters for Graphs

Graph SET Parameter

Values

Parameter Function

3D

ON|OFF

When ON, a three-dimensional
chart is produced. When OFF, a
two-dimensional chart is
produced. ON is the default.

Creating Reports With TIBCO® WebFOCUS Language

 1801

Applying Custom Styling to a Graph

Graph SET Parameter

Values

Parameter Function

AUTOTICK

ON|OFF

BARNUMB

ON|OFF

BSTACK

ON|OFF

GRAPHEDIT

graphedit

GRID

ON|OFF

HAUTO

ON|OFF

When ON, tick mark intervals are
automatically set. ON is the
default. (See also HTICK and
VTICK.)

When ON, places the summary
values at the ends of the bars
on bar graphs or slices on pie
graphs. OFF is the default.

When ON, specifies that the
bars on a bar graph are to be
stacked rather than placed side
by side. OFF is the default.

As of WebFOCUS 8.0, this
parameter has been deprecated.
For information about editing
charts, see the WebFOCUS
InfoAssist User’s Manual.

When ON, specifies that a grid is
to be drawn on the graph at the
horizontal and vertical class
marks (see also VGRID). OFF is
the default.

When ON, specifies automatic
scaling of the horizontal axis
unless overridden by the user. If
OFF, user must supply values for
HMAX and HMIN. ON is the
default.

1802

Graph SET Parameter

Values

Parameter Function

24. Creating a Graph

HAXIS

HCLASS

nnn

HISTOGRAM

ON|OFF

HMAX

nnn

HMIN

nnn

HSTACK

ON|OFF

HTICK

nnn

Specifies the width in characters
of the horizontal axis. This
parameter can be adjusted for
graphs generated offline. HAXIS
is ignored for online displays
since the width of the graph is
automatically adjusted to the
width of the display area.

Specifies the horizontal interval
mark when AUTOTICK=OFF (see
also HTICK).

When ON, a histogram is drawn
instead of a curve when values
on the horizontal axis are not
numeric. ON is the default.

Specifies the maximum value on
the horizontal axis when the
automatic scaling is not used
(HAUTO=OFF).

Specifies the minimum value on
the horizontal axis when the
automatic scaling is not used
(HAUTO=OFF).

When ON, specifies that the
bars on a histogram are to be
stacked rather than placed side
by side. OFF is the default.

Specifies the horizontal axis tick
mark interval when AUTOTICK is
OFF (see also HCLASS).

Creating Reports With TIBCO® WebFOCUS Language

 1803

Applying Custom Styling to a Graph

Graph SET Parameter

Values

Parameter Function

LOOKGRAPH

option

PIE

ON|OFF

VAUTO

ON|OFF

VAXIS

VCLASS

nnn

VGRID

ON|OFF

VMAX

nnn

Specifies the graph type. For
more information, see
Determining Graph Styles Using
LOOKGRAPH on page 1759.

When ON, specifies that a pie
graph is desired. OFF is the
default.

When ON, specifies automatic
scaling of the vertical axis
unless overridden by the user. If
OFF, the user must supply
values for VMAX and VMIN. ON
is the default.

Specifies page length in lines.
This parameter can be adjusted
for graphs generated offline.
VAXIS is ignored for online
displays since the height of the
graph is automatically adjusted
to the display area.

Specifies the vertical interval
mark when AUTOTICK=OFF (see
also VTICK).

When ON, specifies that a grid is
to be drawn on the graph at the
horizontal and vertical class
marks (see also GRID). OFF is
the default.

Specifies the maximum value on
the vertical axis when the
automatic scaling is not used
(VAUTO=OFF).

1804

Graph SET Parameter

Values

Parameter Function

24. Creating a Graph

VMIN

nnn

VTICK

nnn

VZERO

ON|OFF

Specifies the minimum value on
the vertical axis when the
automatic scaling is not used
(VAUTO=OFF).

Specifies the vertical axis tick
mark interval when AUTOTICK is
OFF (see also VCLASS).

Determines whether values
along the Y-axis are stored or
ignored. If ON, missing data
along the Y-axis is treated as
zero. If OFF, missing data along
the Y-axis is ignored and values
are not stored in the plot matrix.
OFF is the default.

Setting Fixed Scales for the X-Axis

The horizontal scale is automatically set to cover the total range of values to be plotted
(HAUTO=ON). The range is divided into intervals called "classes." The scale is normalized to
provide class values rounded to the appropriate multiples of 10 for the intervals plotted on the
axis.

To assign fixed upper and lower limits (useful when producing a series of graphs where
consistent scales are needed), you can turn off the automatic scaling mechanism and set new
limit values by setting HAUTO=OFF.

Syntax:

How to Set Fixed Scales for the X-Axis

SET HAUTO=OFF, HMAX=nn, HMIN=nn

where:

HAUTO

Is the automatic scaling facility. If HAUTO is ON, any values for HMAX and HMIN are
overridden.

Creating Reports With TIBCO® WebFOCUS Language

 1805

Applying Custom Styling to a Graph

HMAX=nn

Sets the upper limit on the horizontal axis. The default is 0.

HMIN=nn

Controls the lower limit on the horizontal axis when HAUTO is OFF. The default is 0.

Note:

When entering several SET parameters on one line, separate them with commas.

If you define limits that do not incorporate all of the data values, OVER or UNDER will be
displayed to indicate that some of the data extracted is not reflected on the graph.

Setting Fixed Scales for the Y-Axis

To give the vertical scale fixed upper and lower limits (useful when producing a series of
graphs where consistent scales are needed), you can turn off the automatic scaling
mechanism and set fixed limits using the SET VAUTO=OFF command.

Syntax:

How to Set Fixed Scales for the Y-Axis

SET VAUTO=OFF, VMAX=nn, VMIN=nn

where:

VAUTO

Is the automatic scaling facility. If VAUTO is ON, any values for VMAX and VMIN are
overridden.

VMAX=nn

Sets the upper limit on the vertical axis when VAUTO is OFF. The default is 0.

VMIN=nn

Controls the lower limit on the vertical axis when VAUTO is OFF. The default is 0.

Note:

When entering several SET parameters on one line, separate them with commas.

If you define limits that do not incorporate all of the data values, OVER or UNDER will be
displayed to indicate that some of the data extracted is not reflected on the graph.

1806

24. Creating a Graph

Customizing Graphs Using the Graph API and HTML5 JSON Properties

You can further enhance your graph output by manually adding API calls inside the ON GRAPH
SET STYLE * and ENDSTYLE commands in the GRAPH request. If you are creating an HTML5
graph, you can also include JavaScript Object Notation (JSON) methods and properties. When
you save changes the corresponding API calls and properties will be written to the graph
StyleSheet.

For reference information about the Graph API, see the WebFOCUS Graphics manual.

When you include both JSON and API calls in the StyleSheet section of the request, the API
calls are parsed first, then the JSON. Therefore, if the JSON sets the same property as an API
call, the JSON will take precedence. In general, the later declarations overwrite the properties
set in earlier declarations.

Syntax:

How to Customize a Graph Using the Graph API

GRAPH FILE filename
graph commands
ON GRAPH SET STYLE *
*GRAPH_SCRIPT
API calls
*END

*GRAPH_JS
JSON
*END

WEBFOCUS StyleSheet commands
ENDSTYLE
END

where:

filename

Specifies a data source for the graph.

API calls

Are API calls. They must be included in a GRAPH_SCRIPT block within *GRAPH_SCRIPT and
*END declarations. A request can contain multiple GRAPH_SCRIPT blocks anywhere within
the style section. For reference information about the Graph API, see the WebFOCUS
Graphics manual.

Creating Reports With TIBCO® WebFOCUS Language

 1807

Applying Custom Styling to a Graph

JSON

Are JSON methods and properties that apply to HTML5 graph output. They must be
included in a GRAPH_JS block within *GRAPH_JS *END declarations. A request can
contain multiple GRAPH_JS blocks anywhere within the style section. For reference
information about the JSON methods and properties, see the Creating HTML5 Charts With
WebFOCUS Language manual.

WEBFOCUS StyleSheet commands

For details on StyleSheet commands, see Creating and Managing a WebFOCUS StyleSheet
on page 1197.

Example:

Customizing Graphs Using the Graph API

The following annotated example illustrates how to customize a graph using ON GRAPH SET
STYLE *. The Graph API code is highlighted in the request.

   GRAPH FILE SALES
   SUM RETURNS
   RETAIL_PRICE
   ACROSS PROD_CODE AS 'Product Code'
   ON GRAPH SET STYLE *
   *GRAPH_SCRIPT
1. setLegendMarkerPosition(4);
2. setO1LabelRotate(0);
3. setTitleString("Sales Report");
4. setTextJustHoriz(getTitle(),1);
   *END
   DEFMACRO=COND0001, MACTYPE=RULE, WHEN=RETURNS GT 4,$
   TYPE=DATA,MACRO=COND0001,ACROSSCOLUMN=RETURNS,COLOR=RED,$
   ENDSTYLE
   END

where:

1. Displays legend text inside the legend marker.

2. Displays the X-axis labels horizontally.

3. Displays the title (Sales Report) without quotes.

4. Centers the title.

1808

The output is:

24. Creating a Graph

Saving a Graph as an Image File

You can save graph output to an image file using the GRAPHSERVURL parameter or the
JSCOM3 configuration on the WebFOCUS Reporting Server. Saving graph output as an image
file is useful when you want to create a single PDF or HTML report that contains multiple
outputs, such as output from a TABLE request and a GRAPH request. You can distribute this
type of report using ReportCaster.

For details, see Saving a Graph as an Image File Using GRAPHSERVURL on page 1809.

Saving a Graph as an Image File Using GRAPHSERVURL

The GRAPHSERVURL parameter enables users who are running against a server environment
where the WebFOCUS Reporting Server is installed on a z/OS, Windows, or UNIX machine to
save graph output as a GIF file. GIF images can be embedded in a PDF or HTML report.

The GRAPHSERVURL parameter sends an http request to the machine that has the WebFOCUS
Graph Servlet. The graph image is created by the WebFOCUS Graph Servlet, and the image is
sent back to a temporary location on the WebFOCUS Reporting Server (if an Allocation has not
been specified), or to the location specified in a FILEDEF command. You may use the
Allocation Wizard to create a FILEDEF command.

Creating Reports With TIBCO® WebFOCUS Language

 1809

Saving a Graph as an Image File

Procedure: How to Save a Graph as an Image File Using GRAPHSERVURL

1.

Install JDK as per the requirements in the WebFOCUS & ReportCaster Installation &
Configuration manual for your platform.

2. Create a procedure that produces the image, and set GRAPHSERVURL in the procedure to

the URL that invokes the WebFOCUS Graph Servlet. For example,

SET GRAPHSERVURL=http://hostname/ibi_apps/IBIGraphServlet

where:

hostname

Is the name of the machine where WebFOCUS is installed.

For more details, see How to Save a Graph as an Image File on page 1810.

3. Run the procedure directly on the WebFOCUS Reporting Server, using a browser.

Syntax:

How to Save a Graph as an Image File

[FILEDEF filename DISK drive:\...\filename.fmt]
SET GRAPHSERVURL= graph_servlet_URL
GRAPH FILE file
graph commands
ON GRAPH HOLD AS filename FORMAT fmt
END

where:

FILEDEF

Saves the image file to the location you specify.

filename

Is the name you give the image file, which must match the FILEDEF command filename. If
you want to prompt for a filename, include an amper variable such as &FILENAME in the
procedure.

fmt

Is the type of image file in which to store the graph. Acceptable values are: PNG, SVG, GIF,
or JPG.

graph_servlet_URL

Is the URL to invoke the WebFOCUS Graph Servlet. The maximum number of characters is
256.

1810

24. Creating a Graph

file

Is the name of the data source you wish to report against.

Note: To insert an image that resides in a permanent location, you must provide the fully
qualified path to the image file. For example, to insert a GIF file,

TYPE=REPORT, IMAGE=drive:\...\ filename.gif

where:

drive:\...\filename.gif

Is the path where the GIF file is located. The WebFOCUS Reporting server must be
installed on that drive.

Example:

Inserting a GIF Image Into a PDF Report

The following illustrates how you can create a GIF file from a graph request, and then embed
the GIF image into a PDF report.

1. Create the remote procedure in a location accessible to the EDA path or application path.

For example, if you are running against your local server it may look like this:

SET GRAPHSERVURL= http://localhost/ibi_apps/IBIGraphServlet
GRAPH FILE CENTORD
SUM LINEPRICE
ACROSS PLANTLNG AS 'Plant'
ON GRAPH HOLD AS PLANT FORMAT GIF
END

TABLE FILE CENTORD
SUM LINEPRICE
BY PLANTLNG AS 'Plant'
ON TABLE SET STYLE *
TYPE=REPORT, IMAGE=plant.gif, POSITION=(4 0), SIZE=(5 3), $
ENDSTYLE
ON TABLE PCHOLD FORMAT PDF
END

Note: If you are using JSCOM3, you can eliminate the SET GRAPHSERVURL parameter from
the procedure.

2. Save the procedure as HOLDGIF.

3. Create an HTML file that calls the HOLDGIF WebFOCUS procedure from a hyperlink. For

example,

Creating Reports With TIBCO® WebFOCUS Language

 1811

Saving a Graph as an Image File

<HTML>
<HEAD>
<TITLE> Inserting a GIF Image in a PDF Report </TITLE>
</HEAD>
<BODY>
<H4 ALIGN=CENTER>Report on Line Price by Plant</H4>
<HR>
<P><FONT SIZE=+2></FONT></P>
<UL TYPE=SQUARE
<LI><A HREF="http://localhost/ibi_apps/WFServlet?IBIF_ex=holdgif">
<H4 ALIGN=CENTER>Click Here to Launch a PDF Report with an Embedded
    GIF Image</H4></A>
</UL>
</BODY>
</HTML>

The resulting launch page looks like this:

You can now run the report from a browser. To distribute the report using ReportCaster, you
would schedule the actual procedure, in this case HOLDGIF, to distribute the report.

1812

4. Click the link to run the report. The report looks like this:

24. Creating a Graph

Note: To run this procedure as a Managed Reporting Standard Report, add the -MRNOEDIT
command to the beginning of the StyleSheet declaration containing the IMAGE attribute. This
prevents Managed Reporting from looking for the GIF file in the Managed Reporting Repository.
The image that is specified must reside on the WebFOCUS Reporting Server.

The -MRNOEDIT syntax is not case-sensitive and it can be used on a single line or a block of
lines. For example:

Single line

-MRNOEDIT TYPE=REPORT, IMAGE=PLANT.gif, POSITION=(4 0), SIZE=(5 3), $

or

-MRNOEDIT TYPE=REPORT, IMAGE=PLANT.gif,
-MRNOEDIT POSITION=(4 0), SIZE=(5 3), $

Multiple lines

-MRNOEDIT BEGIN
TYPE=REPORT, IMAGE=PLANT.gif, POSITION=(4 0), SIZE=(5 3), $
-MRNOEDIT END

Creating Reports With TIBCO® WebFOCUS Language

 1813

Printing a Graph

Reference: Usage Notes for Saving a Graph

If you selected the Save Report check box in the configuration pane of the WebFOCUS
Administration Console (under Redirection Settings), you will be prompted whether to save or
open the output file. If the procedure contained a PCHOLD command that specified an AS
name for the output file, the name is retained if you choose to save the file. If no AS name
was specified, a random filename is generated.

Important: You must do the following in the WebFOCUS Administration Console to utilize Save
Report functionality for WebFOCUS GRAPH requests (specified with a PNG, SVG, GIF, or JPG
format in the procedure):

Set Save Report to yes for the .htm Extension.

Running a server-side GRAPH request creates an HTM file that contains a link to the actual
graph output, which is stored as a temporary image file with a .jpg, .gif, .svg, or .png
extension.

When you execute a GRAPH request, if you select the Save option when prompted to Open
or Save the output, the output is saved to an HTM file using only a reference to the graph
image, which will eventually expire and be deleted from the server (according to the
temporary file expiration settings in the WebFOCUS Client Configuration).

To preserve the output of the GRAPH request, open the saved HTM file, right-click the graph
image, and select Save Picture As to save it to disk permanently. You can then substitute
an absolute reference to the saved image file in the returned HTM output file.

Click Save to save your changes in the Redirection Settings panel.

Printing a Graph

When you run your graph, you may print the output directly from the browser.

Note: If your graph labels or legends are not appearing correctly when you run your graph, see
How to Change Color Settings on page 1815 for details on correcting this.

Procedure: How to Print Your Graph

1. Run your graph.

2.

From the browser, select Print from the File menu.

1814

24. Creating a Graph

Syntax:

How to Send Graph Output Directly to a Printer

Add the following syntax to your GRAPH request:

ON GRAPH SET PRINT OFFLINE

Procedure: How to Change Color Settings

1.

From the Windows Control Panel, select Display.

2. Click the Settings tab.

3.

In the Color palette box, click the drop-down arrow and select True Color or High Color.

Note: If your version of Windows does not have these options, select 65536 or a higher
color count.

4. Click OK.

If you use different color settings from this recommended value, your graphs may appear in
grayscale format.

Creating Reports With TIBCO® WebFOCUS Language

 1815

Printing a Graph

1816

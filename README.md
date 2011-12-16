CSV Analyzer Documentation
==========================
Buck Heroux
12/16/11

Installation
------------
To install get the latest python egg distribution file from the downloads section of this project, or in the dist/ folder and use easy_install.

    easy_install https://github.com/downloads/buckheroux/CSV-Analyzer/csv_analyzer-0.1.2-py2.6.egg


Usage
-----
The CSV Analyzer is packaged with a CLI called csv. Use the csv tool to analyze files using an execution flag, specifying parameters, and masking results from the output.

The csv tool uses the following CLI structure

    csv [--execution flag] file.csv [excution parameters] [--masks]

Here are some quick usage examples:

    csv -f file.csv
    csv -a file.csv units by date,id --unique 

### Notes
* All input is not case sensitive
* CLI is delimited by spaces
** If special charaters are needed for input surrond field with quotes
** "my long (field name)"
** If no headers exist, use column index as field name

Execution Flags
---------------
### [Fields] -f, --fields
Print column headers (fields) to ST_OUT
#### Parameters
* None

    csv -f file.csv

### [List] -l, --list
Print the given fields to ST_OUT
#### Parameters
* List of fields selected for printing
* If none, print full record

    csv -l file.csv f1,f2,f3
    csv -l file.csv

### [Count] -c, --count
Print total row count after masks
#### Parameters
* None

    csv -c file.csv

### [Aggregate], -a, --aggregate
Print summation of given field.

Break down summation using the 'by' keyword
#### Parameters
* Field to be aggregated (must be numeric)
* List of fields to break down the aggregation with

    csv -a file.csv units
    csv -a file.csv units by date,id

### [Graph] -g, --graph
Graph a field against another field.

Outputs a link to Google chart with the data.

Two or more data points must exist.
#### Parameters
* Field to be graphed on the y-axis as dependent variable (must be numeric)
* Field to be graphed against on the x-axis as the independent variable (sorted by natural order)

    csv -g file.csv units by date


Masks
-----
### [Filter] --filter
Filter input to only account for matching records.

Filters are ANDed together
#### Parameters
* List of field=regex to be used as filter

    csv -c file.csv --filter f1=rx1,f2="^[rx]+2$"

### [Unique] --unique
Mask non-unique records.

If field has many unique values, keep in mind that they are all kept in memory
#### Parameters
* List of fields to be used for uniqueness

    csv -l file.csv id,name --unique id,external



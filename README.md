# RawDataProcessing
Code to simplify extracting and processing data for data analysis

This code project came together as I saw the need to constantly pull from various data sources and do basic
data manipulations.

Examples:  Pull a list of hall of famers from a wikipedia entry and then merge that with game logs found on the retrosheet.org

There is often subtle manipulation that needs to be done and can easily be done in excel, which is fine for 1 time reporting.  But what about when the reporting needs to be done monthly.  

You could create a script to pull down the data and get it ready for reporting, but after a while this code would become mostly redundant and inefficient.  Furthermore it would be difficult to pass on the ownership to others to support.

Each step outputs a csv file that can be reported, analyzed or used as an input to another step.  Why CSV?  Well because there are a ton of good tools that enable reading and writing csv files and loading them into dictionaries and arrays for processing in standard packages for data analysis.  And I like to view those in notepad++.

## Connectors and Processors
There are two types of python modules that run, either a connector (a piece of code that fetches data) or a processor (a piece of code that processes, configures, manipulates the data).

### built in connectors

#### Database connections
-- all connections to databases are done using the sqlalchemy package and the associated drivers for that database.  You will have to download and maintain that code seperately from this package (but you would have had to do that anyway!)

* **ConnectDB:**  Connect to a generic database
* **DB_Where:** Allow to pass in where statements from passed in data or dates from the system (i.e. Last Run Date)
* **DB_WhereOffset:**  Allow you to pull data with an offset from a specified date (i.e. Last 6 months from todays date)

### built in processors

## Configurations

### Required Options and Defaults

### Dependencies

### run_frequencies

### file_write

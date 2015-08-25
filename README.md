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

*Most of what has been built and tested so far is based on pulling data from a database.*

* **ConnectDB:**  Connect to a generic database
* **DB_Where:** Allow to pass in where statements from passed in data or dates from the system (i.e. Last Run Date)
* **DB_WhereOffset:**  Allow you to pull data with an offset from a specified date (i.e. Last 6 months from todays date)
* **FileDateStrip:**  Pull off old records from a file that is being appended.. For example you want a years worth of data, and you are adding a month of data every month... so before doing that you want to whittle it down to 11 months (UNTESTED)
* **HtmlListGrabber:** *To be built* This connector will grab a list on a website specified in the options
* **ApiWrapper:**  *To be built* This connector will create a wrapper around an API to simplify some of the common pieces of API calling

### built in processors
Processors are designed to simplify some very common things done across file manipulation.  One thing that this enables is to easily move access based data manipulation to this platform by enabling SQL actions on two csv files

* **TwoFileProcessor:**  Allows two files to be merged together on a common key, with option of keeping or removing non-matched records
* **SQLProcessor:**  Allows you to use SQL to manipulate the data in a CSV file (the idea is to minimize the amount of code needed
* **SQLMultiProcess:** This processor allows you to pull in multiple CSV files and do joins across a common key and manipulate the data based on those common keys.  Often times existing Access queries can be copied over and use with little editing.
* **FieldDescriptionProcessor:** *To Be Built* This processor will create meta data on the passed in files.  This will allow you monitor existing data to check for distributions, category break downs (with % of each category used) Think the equivalent of R's summary


## Configurations
Configuration files are the key to the framework to process the data.  They establish the name of each connector or processor and the order in which to run each.  All information needed to run a connector or processor should be passed in the configuration or pulled from defaults established in the framework.

**Example:**
```
[GetBusinessInfo]
dependencies = GetSystemInfo
username = zombie
password = QYZllck994wMDxT
server = bidb2f22
port = 50000
database = BUSINFO
dialect = ibm_db_sa
src_implementation = rawdata_emca.connections.connect_db_where.DB_Where
sql_file = C:\Users\zombie\businfo\sql\business_info.sql
where_last_name = 'SMITH'
working_directory = C:\Users\zombie\businfo\output
description = Get some business information from the database
file_write = New
last_processed = 04/06/2015 10:23:14
run_frequency = Daily
num_run = 28
last_run = success
```

### Required Options and Defaults


### Dependencies

### run_frequencies

### file_write

## Future Enhancements

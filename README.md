# RawDataProcessing EMCA
Code to simplify extracting and processing data for data analysis

* **E**xtract
* **M**anipulate
* **C**lean
* **A**nalyze

** UPDATE ** Now hosted on pypi at [raw_data_emca](https://pypi.python.org/pypi/raw_data_emca)

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
	* **Required Options:** 
	* server
	* port
	* username
	* password
	* sql_file
	* dialect: (for database connection, based on SQLAlchemy)
	
* **DB_Where:** Allow to pass in where statements from passed in data or dates from the system (i.e. Last Run Date)
	* **Required Options:** 
	* server
	* port
	* username
	* password
	* sql_file
	* dialect: (for database connection, based on SQLAlchemy)
	* where_%%: replace %% with the field the where is based on and the config is set the matching criteria
	`where_last_name = 'SMITH'` is the equivalent of `where last_name = 'SMITH'`
	
* **DB_WhereOffset:**  Allow you to pull data with an offset from a specified date (i.e. Last 6 months from todays date)
	* **Required Options:** 
	* server
	* port
	* username
	* password
	* sql_file
	* dialect: (for database connection, based on SQLAlchemy)
	* where_%%: replace %% with the field the where is based on and the config is set the matching criteria
	`where_last_processed = 'SMITH'` is the equivalent of `where last_name = 'SMITH'`
	* offset_%%: replace %% with and existing field used in a where statement the config is set to X,DatePart
		* X:  The number to offset
		* DatePart:  The data unit to offset by: Options (Day, Month, Year)
	`offset_last_processed = 6, Month` is the equivalent of `where last_processed < '01-01-2015'` if last processed date was 07/01/2015
	* **NOTE** You have the option to put key words in your SQL to be replaced by framework variables
		* last_processed:  replaces the key word %%LAST_PROCESSED%% with the date this entry was last processed (if you offset that field it will be the offset from the last_processed date
		* today_dt: replacess the key word %%TODAY_DT%% with the date the entry is running (if you offset this field it will be offset from today's date)
		
	
* **FileDateStrip:**  Pull off old records from a file that is being appended.. For example you want a years worth of data, and you are adding a month of data every month... so before doing that you want to whittle it down to 11 months (UNTESTED)
	* **Required Options:**
	* strip_file:  The file to strip rows from
	* strip_date:  *optional* the date to use for the criteria to pull off records
	* strip_criteria: specifies the offset to use to pull of rows X, DatePart *see DB_WhereOffset*
	* use_last_processed: true or false (default: false), if set to true the compare date is the last processed date, if false the compare date is the date specified in the strip_date config field
	
* **HtmlListGrabber:** *To be built* This connector will grab a list on a website specified in the options
* **ApiWrapper:**  *To be built* This connector will create a wrapper around an API to simplify some of the common pieces of API calling

### built in processors
Processors are designed to simplify some very common things done across file manipulation.  One thing that this enables is to easily move access based data manipulation to this platform by enabling SQL actions on two csv files

* **TwoFileProcessor:**  Allows two files to be merged together on a common key, with option of keeping or removing non-matched records
	* **Required Options:**
	* file1:  The first file *main processing file*
	* file2:  The second file to add to the first
	* key_file1:  field in file1 that is used to match against file2
	* key_file2:  field in file2 that is sued to match against file1
	* sort: *optional* defaults to false, if true will sort both files
	* field_prefix: *optional* a prefix to add to each field in the combined file, defaults to no prefix
	* file1_nomatch: *optional* defaults to "keep", if it is set to anything else, no matches are discarded
	* all_fields: *optional* if this field is there all fields from file2 are added to file1 see next for if it is absent
	* field_%%:  *required if 'all_fields' is not entered*. for every field from file2 that is to be copied to file1 matches you must enter the config option 
	`field_id = <renamed>`  or `field_id = file2_id`
	
* **SQLProcessor:**  Allows you to use SQL to manipulate the data in a CSV file (the idea is to minimize the amount of code needed
	* **Required Options:**
	* input_file1: the file to be used in the sql
	* sql: The sql to be used against the csv file, default = 'Select * from emca_df1'

* **SQLMultiProcess:** This processor allows you to pull in multiple CSV files and do joins across a common key and manipulate the data based on those common keys.  Often times existing Access queries can be copied over and use with little editing.
	* **Required Options:**
	* input_%%: replace %% with the dataframe name that is to be used in the SQL, the config is set to the file to be pulled in for this dataframe
	* index_%%: replace %% with the dataframe name (should have matching input_ config), this is a comma seperated list of fields used to set the index of the file
	* sql: The sql used to manipulate the two files of data to get a new dateset.  for table names in the sql, use the dataframe names specified in the input_%%

* **FieldDescriptionProcessor:** *To Be Built* This processor will create meta data on the passed in files.  This will allow you monitor existing data to check for distributions, category break downs (with % of each category used) Think the equivalent of R's summary


## Configurations
Configuration files are the key to the framework to process the data.  They establish the name of each connector or processor and the order in which to run each.  All information needed to run a connector or processor should be passed in the configuration or pulled from defaults established in the framework.

**Example: (1 per connector/processor)**
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
* **name:**  the name of the processor or connector in brackets that start the configuration item *required*
`[MyConnectorName]`

* **dependencies"** a list of processors and/or connectors that must run before this entry *optional*
`dependencies = FirstConnector, FirstProcessor`

* **src_implementation:**  The implementation of the entry, must extend either BaseConnector or BaseProcessor *required*
`src_implementation = rawdata_emca.processor.built_in.TwoFileProcessor`

* **description:**  a quick description of what this entry is trying to accomplish *required*
`description = Grabbing name and address information for customers who have an order in the last 2 weeks`

* **working_directory:**  Where input files are stored and output files are written to *required*
`working_directory = C:\My Documents\RawDataOutput`

* **file_write:** specify how to write out the data options: (Append, Overlay, New) Default = Append *optional*
`file_write = Overlay`

* **last_processed:** When was the last time this entry was run?  default is never, this field is important in determining if the entry need to be run *optional*
`last_processed = 04/06/2015 10:23:14`

* **run_frequency:** How often this entry should run options: (Daily, Weekly, Monthly, Quarterly, Annual, Every, Fifteen, Hour), Default = 'Daily' *optional*  
`run_frequency = Daily`

* **num_run:** The number of times this entry has been run so far.  This is used to create a backup of the last run when the file_write option is set to 'New'
`num_run = 28`

* **last_run:** This is either 'success' or 'failure', meaning the last time this entry ran it ended okay or in an error.  If the last run was 'failure' this entry will not be run again until it is manually set to success or this config is deleted.  Defaults to 'success' *optional*
`last_run = success`


## Future Enhancements
### Built-in connectors and processors
Always on the look out for additional connectors and processor that can be added to the frame work to help speed up data work and analysis

### Database driven configurations
Right now all configurations are based on a file based configuration set.  My initial thought is switch this to be in mongodb.  That will make the transition easier.

### UI config entry and updating
Add a UI to enable the editing of the config entries to be done on a web screen.  pre-requisite is to have the configuration entries in a database.

### Connector and Processor implementation added options
I would also add a function to the BaseEntry to get all required configuration options.  By default it will be the base config options.  But all implementations would be required to pass in additional options needed (This could be more difficult, but probably pretty dang cool!)

### UI Dependency editor
Update and control the dependencies of the entries on other entries

### UI Monitoring
Added visualization and reports on the running of entries to easily tell which entries have run and any error messages returned.
The framework has some decent logging built in currently and should easily allow for this functionality to be added
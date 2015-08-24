# RawDataProcessing
Code to simplify extracting and processing data for data analysis

This code project came together as I saw the need to constantly pull from various data sources and do basic
data manipulations.

Examples:  Pull a list of hall of famers from a wikipedia entry and then merge that with game logs found on the retrosheet.org

There is often subtle manipulation that needs to be done and can easily be done in excel, which is fine for 1 time reporting.  But what about when the reporting needs to be done monthly.  

You could create a script to pull down the data and get it ready for reporting, but after a while this code would become mostly redundant and inefficient.  Furthermore it would be difficult to pass on the ownership to others to support.

## Connectors and Processors
There are two types of python modules that run, either a connector (a piece of code that fetches data) or a processor (a piece of code that processes, configures, manipulates the data).

### built in connectors

### built in processors

## Configurations

### Required Options and Defaults

### Dependencies

### run_frequencies

### file_write

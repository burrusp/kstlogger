# KSTLogger

takes specific inputs and generates a JSON formatted log and prints the entry to the console/cloudwatch.

Pass into the log_entry command in the following order (context, "SourceProcessName","CorrelationID","LogSeverity","log_detail",Addition(OPTIONAL))

NOTE: context is a field auto-generated by Lambda when triggered. Just pass in as is.

NOTE: the Addition is an optional field that you can pass a json (or dict) type object that you want included in the log. For example:

```Python
custom = {"developer": "Burrus", "Last_updated": "now"}
logger("HiveProcess","123","info","this is a test log",custom)
```

## Log format example:
Without the additional perameter:

{"SourceProcessName": "burrus", "log_timestamp_utc": "2019-01-14 10:44:48", "log_severity": "info", "CorrelationID": "123", "log_detail": "this is a test log"} 

With additional Parameter:

{"SourceProcessName": "Burrus", "log_timestamp_utc": "2019-01-14 10:58:48", "log_severity": "info", "CorrelationID": "123", "log_detail": "this is a test log", "developer": "Burrus", "Last_updated": "now"}

## Installation
This package is installed using pip.  The following command line will install the latest version of this component:

```
pip install git+https://github.com/burrusp/kstlogger
```


## Code Usage Example:
```Python
import os
from KSTLogger import *

logger=KSTLogger.log_entry

logger("insert process name","insert correlation ID","insert log severity","insert log message")
```

import datetime
import json


class KSTLogger:

    def log_entry(SourceProcessName, CorrelationID, logSeverity, log_detail, Additional = None):
        logMessage = None
        logMessage = {
            "SourceProcessName": SourceProcessName, 
            "log_timestamp_utc": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
            "log_severity": logSeverity, 
            "CorrelationID": CorrelationID, 
            "log_detail": log_detail
        }
        if Additional != None:
            for item in Additional:
                logMessage[item]=Additional[item]
        logMessage = json.dumps(logMessage)
        print(logMessage)


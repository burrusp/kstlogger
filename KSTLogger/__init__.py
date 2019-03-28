import datetime
import json


class KSTLogger:

    def log_entry(SourceProcessName, CorrelationID, logSeverity, log_detail, Additional = None):
        logMessage = None
        if Additional != None:
            Additional = str(Additional)
            Additional = Additional.replace("{",", ")
            Additional = Additional.replace("}","")
            Additional = Additional.replace("'","\"")
            logMessage = '{"SourceProcessName": "' + SourceProcessName + '", "log_timestamp_utc": "' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '", "log_severity": "' + logSeverity + '", "CorrelationID": "' + CorrelationID + '", "log_detail": "' + log_detail + '"' + Additional + '}'
        else:
            logMessage = '{"SourceProcessName": "' + SourceProcessName + '", "log_timestamp_utc": "' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '", "log_severity": "' + logSeverity + '", "CorrelationID": "' + CorrelationID + '", "log_detail": "' + log_detail + '"}'
        json.loads(logMessage)
        print(logMessage)


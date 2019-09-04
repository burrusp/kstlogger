import datetime
import json
from kmt_logging import KMTLogger


class KSTLogger:

    def __init__(self,source_process_name=None, timestamp_format='%Y-%m-%d %H:%M:%S')
        self._source_process_name=source_process_name
        self._timestamp_format=timestamp_format

    def begin(self, lambdaname, source_system_id, trade_id, source_system):
        kmtlogger=KMTLogger(self._source_process_name)
        kmtlogger.log("INFO", "Beginning lambda " + lambdaname, source_system_id=source_system_id, source_system=source_system, trade_id=trade_id)

    def log_entry(log_severity, source_process_name, source_system_id, log_detail, Additional = None):
        logMessage = None
        logMessage = {"source_process_name": source_process_name, "log_timestamp_utc": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"), "log_severity": log_severity, "source_system_id": source_system_id, "log_detail": log_detail}
        if Additional != None:
            for item in Additional:
                logMessage[item]=Additional[item]
        logMessage = json.dumps(logMessage)
        print(logMessage)


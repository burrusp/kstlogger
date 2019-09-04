import datetime
import os
import json


class KSTLogger:

    def __init__(self,source_process_name=None, timestamp_format='%Y-%m-%d %H:%M:%S'):
        self._source_process_name=source_process_name
        self._timestamp_format=timestamp_format

    def log(self, log_severity, source_system_id, trade_id, source_system, log_detail, **kwargs):
        debug = os.environ["DEBUG"]
        log_message={
            "log_severity": log_severity,
            "source_process_name": self._source_process_name,
            "log_timestamp_utc": datetime.datetime.utcnow().strftime(self._timestamp_format),
            "log_detail": log_detail,
            "source_system_id": source_system_id,
            "source_system": source_system,
            "trade_id": trade_id
        }
        if log_severity.lower() == "debug" and debug.lower() == "true": 
            if kwargs:
                for arg in kwargs:
                    if kwargs[arg_key] is not None:
                        log_message[arg_key]=kwargs[arg]
                log_message=json.dumps(log_message)
                print(log_message)
            else:
                log_message=json.dumps(log_message)
                print(log_message)
        elif log_severity.lower() != "debug":
            if kwargs:
                for arg in kwargs:
                    if kwargs[arg_key] is not None:
                        log_message[arg_key]=kwargs[arg]
                log_message=json.dumps(log_message)
                print(log_message)
            else:
                log_message=json.dumps(log_message)
                print(log_message)


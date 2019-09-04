import datetime
import os
import json
import traceback


class KSTLogger:

    def __init__(self,source_process_name, source_system_id, trade_id, source_system, timestamp_format='%Y-%m-%d %H:%M:%S'):
        self._source_process_name=source_process_name
        self.source_system_id=source_system_id
        self.trade_id=trade_id
        self.source_system=source_system
        self._timestamp_format=timestamp_format

    def log(self, log_severity, log_detail, **kwargs):
        try:
            try:
                debug = os.environ["DEBUG"]
            except:
                debug = "false"
            log_message={
                "log_severity": log_severity,
                "source_process_name": self._source_process_name,
                "log_timestamp_utc": datetime.datetime.utcnow().strftime(self._timestamp_format),
                "log_detail": log_detail,
                "source_system_id": self.source_system_id,
                "source_system": self.source_system,
                "trade_id": self.trade_id
            }
            if log_severity.lower() == "debug" and debug.lower() == "true": 
                if kwargs:
                    for arg in kwargs:
                        if kwargs[arg] is not None:
                            log_message[arg]=kwargs[arg]
                    log_message=json.dumps(log_message)
                    print(log_message)
                else:
                    log_message=json.dumps(log_message)
                    print(log_message)
            elif log_severity.lower() != "debug":
                if kwargs:
                    for arg in kwargs:
                        if kwargs[arg] is not None:
                            log_message[arg]=kwargs[arg]
                    log_message=json.dumps(log_message)
                    print(log_message)
                else:
                    log_message=json.dumps(log_message)
                    print(log_message)
        except:
            traceback.print_exc()


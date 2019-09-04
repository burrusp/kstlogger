import datetime
import os
import json
from kmt_logging import KMTLogger


class KSTLogger:

    def __init__(self,source_process_name=None, timestamp_format='%Y-%m-%d %H:%M:%S'):
        self._source_process_name=source_process_name
        self._timestamp_format=timestamp_format
        global kmtlogger
        kmtlogger=KMTLogger(self._source_process_name)

    def log(self, log_severity, source_system_id, trade_id, source_system, log_detail, **kwargs):
        debug = os.environ["DEBUG"]
        if log_severity.lower() == "debug" and debug: 
            if kwargs:
                kmtlogger.log(log_severity, log_detail, source_system_id=source_system_id, source_system=source_system, trade_id=trade_id, **kwargs)
            else:
                kmtlogger.log(log_severity, log_detail, source_system_id=source_system_id, source_system=source_system, trade_id=trade_id)
        elif log_severity.lower() != "debug":
            if kwargs:
                kmtlogger.log(log_severity, log_detail, source_system_id=source_system_id, source_system=source_system, trade_id=trade_id, **kwargs)
            else:
                kmtlogger.log(log_severity, log_detail, source_system_id=source_system_id, source_system=source_system, trade_id=trade_id)


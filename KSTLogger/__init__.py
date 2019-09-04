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

    def begin(self, lambda_name, trigger_file, source_system_id, trade_id, source_system):
        kmtlogger.log("INFO", "invoked lambda " + lambda_name, source_system_id=source_system_id, source_system=source_system, trade_id=trade_id, trigger_file=trigger_file)

    def end(self, lambda_name, destination_file, source_system_id, trade_id, source_system):
        kmtlogger.log("INFO", "invoked lambda " + lambda_name, source_system_id=source_system_id, source_system=source_system, trade_id=trade_id, destination_file=destination_file)

    def info(self, source_system_id, trade_id, source_system, log_detail, additional = None):
        also={}
        if additional:
            for item in additional:
                also[item]=additional[item]
        kmtlogger.log("INFO", log_detail, source_system_id=source_system_id, source_system=source_system, trade_id=trade_id, additional=also)

    def debug(self, source_system_id, trade_id, source_system, log_detail, additional = None):
        #debug = os.environ["DEBUG"]
        debug = "TRUE"
        if debug.lower() = "true":
            also={}
            if additional:
                for item in additional:
                    also[item]=additional[item]
            kmtlogger.log("DEBUG", log_detail, source_system_id=source_system_id, source_system=source_system, trade_id=trade_id, additional=also)

    def buserror(self, source_system_id, trade_id, source_system, log_detail, additional = None):
        also={}
        if additional:
            for item in additional:
                also[item]=additional[item]
        kmtlogger.log("ERROR", log_detail, source_system_id=source_system_id, source_system=source_system, trade_id=trade_id, error_type="business_error", additional=also)

    def techerror(self, source_system_id, trade_id, source_system, log_detail, additional = None):
        also={}
        if additional:
            for item in additional:
                also[item]=additional[item]
        kmtlogger.log("ERROR", log_detail, source_system_id=source_system_id, source_system=source_system, trade_id=trade_id, error_type="technical_error", additional=also)

    def error(self, source_system_id, trade_id, source_system, log_detail, additional = None):
        also={}
        if additional:
            for item in additional:
                also[item]=additional[item]
        kmtlogger.log("ERROR", log_detail, source_system_id=source_system_id, source_system=source_system, trade_id=trade_id, error_type="unhandled_error", additional=also)

    def warn(self, source_system_id, trade_id, source_system, log_detail, additional = None):
        also={}
        if additional:
            for item in additional:
                also[item]=additional[item]
        kmtlogger.log("warn", log_detail, source_system_id=source_system_id, source_system=source_system, trade_id=trade_id, additional=also)


import sys

sys.path.append("..")
from common.common import *
from common.logs import Logger

if __name__ == '__main__':
    # print(now_time_strap())
    # print(format_time())
    # format_print(str(time_stamp()))
    # print(format_timestamp(str(time_stamp())))
    # format_print("ss")
    # mongodb = MongoDB(None, None, 'test')
    log = Logger("common", console_log_status=True)
    print(log.logger_name)
    print(time_stamp())


    # MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)

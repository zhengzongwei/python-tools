import sys

sys.path.append("..")

# from unittest import mock

from common.common import time_stamp
from common.logs import Logger


# # 装饰器
# def user_logging(func):
#     print("11111")
#     def wrapper(*args,**kwargs):
#         raise ValueError
#         print("2222 %s",func.__name__)
#         print(args)

#         return func(*args)
#     print(("33333"))
#     return wrapper

# @user_logging
# def foo(sd):
#     print("i am foo")
if __name__ == '__main__':
    # foo("ssd")

    print(time_stamp())
    # print(format_time())
    # format_print(str(time_stamp()))
    # print(format_timestamp(str(time_stamp())))
    # format_print("ss")
    # mongodb = MongoDB(None, None, 'test')
    # log = Logger("common", console_log_status=True)
    # print(log.logger_name)
    # print(time_stamp())

    # MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)

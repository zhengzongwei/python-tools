#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import json

"""
################################################################
# description: 公共调用函数
# author: zhengzongwei@foxmail.com
################################################################
"""


def execute_time(func):
    """
    compute function execute time
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        func_return = func(*args, **kwargs)
        end_time = time.time()
        format_str = ("[%s] execute time: %s " % (func.__name__, end_time - start_time))
        os.system("echo %s >> %s-execute-time" % (format_str, func.__name__))
        return func_return

    return wrapper


def format_time(timestamp: int = None) -> str:
    """
    The format time is standard time. If the parameter is empty, the current time will be formatted
    :param timestamp:
    :return:
    """
    if timestamp is None:
        timestamp = time.time()

    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))


def time_stamp() -> int:
    """
    Returns the timestamp of the current time
    :return:
    """
    return int(time.time())


def format_timestamp(str_time: str) -> int:
    """
    Format standard format time as a timestamp
    """
    return int(time.mktime(str_time, '%Y-%m-%d %H:%M:%S'))


def format_print(data: str) -> None:
    """

    :param data:
    :return:
    """

    print(json.dumps(data, indent=4))

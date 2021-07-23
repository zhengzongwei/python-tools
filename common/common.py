import time
import os


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


def now_time(_now_time=None) -> str:
    """
    formatting time
    """
    if _now_time is None:
        _nowtime = time.time()
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(_now_time))


def now_time_strap():
    return time.time()


def time_strap(str_time: str) -> int:
    """
    formatting time to times trap
    """
    return int(time.mktime(str_time, "%Y-%m-%d %H:%M:%S"))

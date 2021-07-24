import logging

from logging import handlers


# class Logger(object):

def init_log():
    filename = "logs.log"
    logger = logging.getLogger(filename)
    log_format = "%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s"
    format_str = logging.Formatter(log_format)
    # logger.setLevel("INFO")
    sh = logging.StreamHandler()
    sh.setFormatter(format_str)

    th = handlers.TimedRotatingFileHandler(filename=filename, when='D', backupCount=3,
                                           encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
    # 实例化TimedRotatingFileHandler
    # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
    # S 秒
    # M 分
    # H 小时、
    # D 天、
    # W 每星期（interval==0时代表星期一）
    th.setFormatter(format_str)
    logger.addHandler(sh)
    logger.addHandler(th)


def blog(level, msg, mod="DEVELOP"):
    pass


def ulog(level, msg, mod="USER"):
    pass

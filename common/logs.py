#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os.path

from logging import handlers

"""
################################################################
# description: 日志记录模块
# author: zhengzongwei@foxmail.com
################################################################
"""

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Logger(object):
    LOG_FILE = "logs/log.log"
    LOG_PATH = os.path.join(BASE_DIR,LOG_FILE)
    LOG_LEVEL = logging.INFO

    def __init__(self, logger_name="logs", console_log_status=False):
        self.logger_name = logger_name
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(self.LOG_LEVEL)

        if not os.path.exists(self.LOG_PATH):
            log_dir = os.path.dirname(self.LOG_PATH)
            if not os.path.exists(log_dir):
                    os.makedirs(log_dir)

        log_format = "%(asctime)s - %(name)s[func: %(funcName)s line:%(lineno)d] - %(levelname)s: %(message)s"
        format_str = logging.Formatter(log_format)
        if console_log_status:
            console_handle = logging.StreamHandler()
            console_handle.setFormatter(format_str)
            self.logger.addHandler(console_handle)

        file_handle = handlers.TimedRotatingFileHandler(filename=self.LOG_PATH, when='D', backupCount=3,
                                                        encoding='utf-8')
        file_handle.setFormatter(format_str)
        self.logger.addHandler(file_handle)

    def log(self, msg, level="WARNING"):
        level = level.upper()
        if level == "INFO":
            self.logger.info(msg)
        elif level == "DEBUG":
            self.logger.debug(msg)
        elif level == "WARNING":
            self.logger.warning(msg)
        elif level == "ERROR":
            self.logger.error(msg)
        elif level == "CRITICAL":
            self.logger.critical(msg)
        else:
            self.logger.warning(msg)

    def blog(self, msg, level="WARNING"):
        self.log(msg,level)

    def ulog(self, msg, level="WARNING"):
        self.log(msg,level)
        # 数据库写入

    def dlog(self, msg, level="WARNING"):
        self.log(msg,level)
        # 数据库写入


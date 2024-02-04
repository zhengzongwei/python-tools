#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/2/4 14:08
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

import logging
import os
from datetime import datetime

import toml
from logging.handlers import TimedRotatingFileHandler


class Logger(object):
    """
    基础日志类
    """
    log_level = "info"
    log_format = "%(asctime)s - %(name)s[func: %(funcName)s line:%(lineno)d] - %(levelname)s: %(message)s"
    log_console = True
    stacklevel = 2

    def __init__(self, logger_name, logger_path="logs.toml") -> None:
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(self.base_dir)
        self.log_config = dict()
        self.logger = None
        self.logger_conf = dict()

        self.logger_format = None

        self.logger_name = logger_name
        self.logger_path = logger_path

        self._get_log_conf()
        self.stacklevel = self.logger_conf['stacklevel']
        self.logger_conf_level = self.logger_conf['log_level']
        self.logger_level = self.parse_log_level(self.logger_conf_level.upper())

        self.logger_format = self.get_conf_format()
        self.init_logger()

    def _get_log_conf(self) -> None:
        try:
            log_conf = toml.load(self.logger_path)
            self.logger_conf = log_conf.get("logs", {})
        except:
            self.logger_conf = {
                'log_level': self.log_level,
                'log_format': self.log_format,
                'stacklevel': self.stacklevel,
                'log_console': self.log_console
            }

    def get_conf_format(self):
        logger_format = "%(asctime)s - %(name)s[func: %(funcName)s line:%(lineno)d] - %(levelname)s: %(message)s"
        return self.logger_conf.get("format", logger_format)

    @staticmethod
    def parse_log_level(level: str) -> int:
        levels = {
            "INFO": logging.INFO,
            "DEBUG": logging.DEBUG,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL
        }
        return levels.get(level, logging.WARNING)

    def init_logger(self) -> None:
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(self.logger_level)

        # 是否打印在console
        if not self.logger_conf.get('log_console', False):
            console_handle = logging.StreamHandler()
            console_handle.setFormatter(logging.Formatter(self.logger_format))
            self.logger.addHandler(console_handle)

        if not self.logger_conf.get('log_path'):
            log_path = os.path.join(self.base_dir, 'logs', 'log-%s.log' % datetime.now().strftime('%Y-%m-%d'))
            self.make_conf_dir(os.path.dirname((log_path)))
            file_handler = TimedRotatingFileHandler(log_path, when="midnight", interval=1, backupCount=3,
                                                    encoding='utf-8')
            file_handler.setFormatter(logging.Formatter(self.logger_format))
            self.logger.addHandler(file_handler)

    def make_conf_dir(self,path) -> None:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
    def _log(self, msg):
        getattr(self.logger, self.logger_conf_level)(msg, stacklevel=self.stacklevel)

    def debug(self, msg):
        self._log(msg)

    def info(self, msg):
        self._log(msg)

    def warning(self, msg):
        self._log(msg)

    def error(self, msg):
        self._log(msg)

    def critical(self, msg):
        self._log(msg)


if __name__ == '__main__':
    # log = Logger("test123")
    # log.error("12331234")
    print(os.path.dirname(__file__))

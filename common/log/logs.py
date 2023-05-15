#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import toml
import os

import platform

from logging import handlers


class LoggerBase(object):
    """
    日志模块
    """

    def __init__(self, logger_name, log_config_path="logs.toml") -> None:

        log_config = self.get_log_config(log_config_path)
        self.logger_name = logger_name
        self.logger = self.parse_log_level(log_config['log_level'].upper())
        self.log_console = log_config['log_console']
        self.log_format = log_config['log_format']
        self.log_path = log_config['log_path']
        self.stacklevel = log_config['stacklevel']
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config_log()

    def get_log_config(self, log_config_path) -> dict:
        """
        check the log config
        :return:
        """

        log_config = toml.load(log_config_path)
        return log_config['logs']

    def parse_log_level(self, level):
        if level == "INFO":
            self.log_level = logging.INFO
        elif level == "DEBUG":
            self.log_level = logging.DEBUG
        elif level == "WARNING":
            self.log_level = logging.WARNING
        elif level == "ERROR":
            self.log_level = logging.ERROR
        elif level == "CRITICAL":
            self.log_level = logging.CRITICAL
        else:
            self.log_level = logging.WARNING

    def config_log(self):
        if platform.system().lower() == 'windows':
            base_dir = (os.path.dirname(os.path.abspath(__file__)))
            log_path = f'{base_dir}\log.log'
        else:
            log_path = self.log_path
        self.init_log(log_path=log_path, log_format=self.log_format)

    def init_log(self, log_path=None, log_format=None):
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(self.log_level)
        self.logger.propagate = True

        if self.logger in [logging.DEBUG, logging.INFO] or self.log_console:
            self.log_console = True

        if self.log_console:
            console_handle = logging.StreamHandler()
            console_handle.setFormatter(logging.Formatter(self.log_format))
            self.logger.addHandler(console_handle)

        file_handle = handlers.TimedRotatingFileHandler(filename=log_path, when='D', backupCount=3,
                                                        encoding='utf-8')
        file_handle.setFormatter(logging.Formatter(self.log_format))
        self.logger.addHandler(file_handle)

    @staticmethod
    def check_log_dir(path) -> bool:
        """
        检查日志目录是否存在，不存在则创建
        :return:
        """
        return os.path.exists(path)

    @staticmethod
    def mkdir_log_dir(path) -> None:
        """
        创建日志目录
        :return:
        """
        if os.path.isfile(path):
            path = os.path.abspath(path)
        return os.makedirs(path)


class Logger(LoggerBase):
    def __init__(self, logger_name, log_config_path="logs.toml"):
        super().__init__(logger_name, log_config_path=log_config_path)

    def debug(self, msg):
        self.logger.debug(msg, stacklevel=self.stacklevel)

    def info(self, msg):
        self.logger.info(msg, stacklevel=self.stacklevel)

    def warning(self, msg):
        self.logger.warning(msg, stacklevel=self.stacklevel)

    def error(self, msg):
        self.logger.error(msg, stacklevel=self.stacklevel)

    def critical(self, msg):
        self.logger.critical(msg, stacklevel=self.stacklevel)

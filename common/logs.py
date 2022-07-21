#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
from logging import handlers

"""
################################################################
# description: 日志记录模块
# author: zhengzongwei@foxmail.com
################################################################
"""


class LoggerBase(object):
    """
    Log Baase class
    """
    def __init__(self) -> None:
        # 是否控制台输出
        self.console_log_status = False
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config_log()

    @staticmethod
    def check_log_dir(path) -> bool:
        """
        检查日志目录是否存在，不存在则创建
        :return:
        """
        return os.path.exists(path)

    @staticmethod
    def mkdir_log_dir(path) -> bool:
        """
        创建日志目录
        :return:
        """
        if os.path.isfile(path):
            path = os.path.abspath(path)
        return os.makedirs(path)
    
    def config_log(self):
        """
        配置日志
        :return:
        """
        # TODO 通过配置文件读取log配置，读取不到使用默认配置
        log_config_path = os.path.join(self.base_dir, "log.conf")
        if os.path.exists(log_config_path):
            logging.config.fileConfig(log_config_path)
        else:
            log_path = f'{self.base_dir}/logs.log'
            log_format = "%(asctime)s - %(name)s[func: %(funcName)s line:%(lineno)d] - %(levelname)s: %(message)s"
            self.init_log(log_path=log_path, log_format=log_format)

    def init_log(self, logger_name="logs", log_path=None, log_format=None, log_level=logging.INFO):
        """
        初始化日志
        :param
        """
        self.logger_name = logger_name
        self.logger = logging.getLogger(self.logger_name)

        if log_path is None:
            self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            log_path = os.path.join(self.base_dir, "logs")
        
        if log_level in [logging.DEBUG, logging.INFO]:
            self.console_log_status = True

        if log_format is None:
            log_format = "%(asctime)s - %(name)s[func: %(funcName)s line:%(lineno)d] - %(levelname)s: %(message)s"
        format_str = logging.Formatter(log_format)

        if self.console_log_status:
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


# class Logger(LoggerBase):
    # def __init__(self, logger_name="logs", console_log_status=False):
    #     self.logger_name = logger_name
    #     self.logger = logging.getLogger(logger_name)
    #     self.logger.setLevel(self.LOG_LEVEL)

    #     if not os.path.exists(self.LOG_PATH):
    #         log_dir = os.path.dirname(self.LOG_PATH)
    #         if not os.path.exists(log_dir):
    #             os.makedirs(log_dir)

    #     log_format = "%(asctime)s - %(name)s[func: %(funcName)s line:%(lineno)d] - %(levelname)s: %(message)s"
    #     format_str = logging.Formatter(log_format)
    #     if console_log_status:
    #         console_handle = logging.StreamHandler()
    #         console_handle.setFormatter(format_str)
    #         self.logger.addHandler(console_handle)

    #     file_handle = handlers.TimedRotatingFileHandler(filename=self.LOG_PATH, when='D', backupCount=3,
    #                                                     encoding='utf-8')
    #     file_handle.setFormatter(format_str)
    #     self.logger.addHandler(file_handle)



    # def blog(self, msg, level="WARNING"):
    #     self.log(msg, level)

    # def ulog(self, msg, level="WARNING"):
    #     self.log(msg, level)
    #     # 数据库写入

    # def dlog(self, msg, level="WARNING"):
    #     self.log(msg, level)
    #     # 数据库写入

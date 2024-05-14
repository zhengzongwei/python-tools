# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# import logging
# import os
# from logging import handlers
#
# """
# ################################################################
# # description: 日志记录模块
# # author: zhengzongwei@foxmail.com
# ################################################################
# """
#
#
# class LoggerBase(object):
#     """
#     Log Baase class
#     """
#
#     def __init__(self, logger_name='log.toml') -> None:
#         # 是否控制台输出
#         self.logger_name = logger_name
#         self.LOG_LEVEL = logging.DEBUG
#         self.console_log_status = False
#         self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#         self.config_log()
#
#     @staticmethod
#     def check_log_dir(path) -> bool:
#         """
#         检查日志目录是否存在，不存在则创建
#         :return:
#         """
#         return os.path.exists(path)
#
#     @staticmethod
#     def mkdir_log_dir(path) -> None:
#         """
#         创建日志目录
#         :return:
#         """
#         if os.path.isfile(path):
#             path = os.path.abspath(path)
#         return os.makedirs(path)
#
#     def config_log(self):
#         """
#         配置日志
#         :return:
#         """
#         # TODO 通过配置文件读取log配置，读取不到使用默认配置
#         # log_config_path = os.path.join(self.base_dir, "log.conf")
#         # if os.path.exists(log_config_path):
#         #     logging.config.fileConfig(log_config_path)
#         # else:
#         #     log_path = f'{self.base_dir}/log.toml.log'
#         #     log_format = "%(asctime)s - %(name)s[func: %(funcName)s line:%(lineno)d] - %(levelname)s: %(message)s"
#         #     self.init_log(log_path=log_path, log_format=log_format)
#
#         log_path = f'{self.base_dir}/log.log'
#         log_format = "%(asctime)s - %(name)s[func: %(funcName)s line:%(lineno)d] - %(levelname)s: %(message)s"
#         self.init_log(log_path=log_path, log_format=log_format)
#
#     def init_log(self, log_path=None, log_format=None):
#         """
#         初始化日志
#         :param
#         """
#         self.logger = logging.getLogger(self.logger_name)
#         self.logger.setLevel(self.LOG_LEVEL)
#         self.logger.propagate = True
#
#         if log_path is None:
#             log_path = os.path.join(self.base_dir, "log")
#
#         if self.LOG_LEVEL in [logging.DEBUG, logging.INFO]:
#             self.console_log_status = True
#
#         if log_format is None:
#             log_format = "%(asctime)s - %(name)s[func: %(funcName)s line:%(lineno)d] - %(levelname)s: %(message)s"
#         format_str = logging.Formatter(log_format)
#
#         if self.console_log_status:
#             console_handle = logging.StreamHandler()
#             console_handle.setFormatter(format_str)
#             self.logger.addHandler(console_handle)
#
#         file_handle = handlers.TimedRotatingFileHandler(filename=log_path, when='D', backupCount=3,
#                                                         encoding='utf-8')
#         file_handle.setFormatter(format_str)
#         self.logger.addHandler(file_handle)
#
#     def log(self, msg, level="WARNING", stacklevel=3):
#         level = level.upper()
#         if level == "INFO":
#             self.logger.info(msg, stacklevel=stacklevel)
#         elif level == "DEBUG":
#             self.logger.debug(msg, stacklevel=stacklevel)
#         elif level == "WARNING":
#             self.logger.warning(msg, stacklevel=stacklevel)
#         elif level == "ERROR":
#             self.logger.error(msg, stacklevel=stacklevel)
#         elif level == "CRITICAL":
#             self.logger.critical(msg, stacklevel=stacklevel)
#         else:
#             self.logger.warning(msg)
#
#
# # class Logger(LoggerBase):
# #
# #     def dlog(self, msg, level="DEBUG", model_name='default'):
# #         """
# #         development log
# #         """
# #         self._log(msg, level)
# #         # TODO 数据库写入
# #
# #     def blog(self, msg, level="ERROR", model_name='default'):
# #         """
# #         backend log
# #         """
# #         self._log(msg, level)
# #         # TODO 数据库写入
# #
# #     def ulog(self, msg, level="WARNING", model_name='default'):
# #         """
# #         user log
# #         """
# #         self._log(msg, level)
# #         print(self.logger_name)
# #         # TODO 数据库写入

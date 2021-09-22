#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
################################################################
# description: 自定义异常处理
# author: zhengzongwei@foxmail.com
################################################################
"""


class BaseException(Exception):
    pass

class hashError(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "类型错误，请重新选择类型！"
    

    

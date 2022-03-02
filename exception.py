#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
################################################################
# description: 自定义异常处理
# author: zhengzongwei@foxmail.com
################################################################
"""


class BaseException(Exception):

    def __init__(self, detail, code=None):
        self.detail = None
        if code and code >= 0:
            code = -1
        self.code = code or -1
        super(BaseException, self).__init__(detail)

    def __str__(self):
        return 'message: %s code: %s' % (self.detail, self.code)



class hashError(BaseException):
    def __init__(self, *args: object) -> None:
        super(hashError, self).__init__(*args)


if __name__ == '__main__':
    # raise hashError("fkds")
    a = None

    b = a or -1

    print(b)

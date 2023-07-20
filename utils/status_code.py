# class RETCODE(object):
#     OK = 0
#     ERROR = -1
#
#
# ERR_MSG = {
#     RETCODE.OK: "成功",
#
#
# }
from enum import Enum


class CodeEnum(Enum):
    OK = (0, '成功')
    ERROR = (-1, '内部错误')

    @property
    def code(self):
        """获取状态码"""
        return self.value[0]

    @property
    def msg(self):
        """获取状态码信息"""
        return self.value[1]

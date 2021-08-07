#!/usr/bin/env python
# -*- coding: utf-8 -*-

import platform
import psutil

if platform.system() == 'Windows':
    import wmi

"""
################################################################
# description:获取操作系统的基本信息
# author: zhengzongwei@foxmail.com
################################################################
"""


def osinfo():
    ret = {'ret': 0, 'err': ''}

    info = dict()
    os_info = dict()
    cpu_info = dict()
    python_info = dict()
    # 判断操作系统类型
    os_info['os_type'] = platform.system()

    # 获取操作系统位数 ('64bit', 'WindowsPE')
    os_info['os_bit'] = platform.architecture()[0]
    # 获取计算机的网络名称
    os_info['os_name'] = platform.node()

    # 操作系统的版本信息
    os_info['os_version'] = platform.version()

    # cpu 信息
    if platform.system() == 'Windows':
        w = wmi.WMI()
        for cpu in w.Win32_Processor():
            cpu_name = cpu.Name
            cpu_cores = cpu.NumberOfCores
            cpu_info['cpu_name'] = cpu_name
            cpu_info['cpu_cores'] = cpu_cores

    cpu_info['cpu_info'] = platform.processor()

    # python 版本信息
    python_info['python_version'] = platform.python_version()

    info['os_info'] = os_info
    info['cpu_info'] = cpu_info
    info['python_info'] = python_info
    ret['info'] = info
    # print(platform.version())

    return ret


if __name__ == '__main__':
    print(osinfo())

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



def get_os_info():
    os_info = dict()

    try:
        # 判断操作系统类型
        os_info['os_type'] = platform.system()

        # 获取操作系统位数 ('64bit', 'WindowsPE')
        os_info['os_bit'] = platform.architecture()[0]

        # 获取计算机的网络名称
        os_info['os_name'] = platform.node()

        # 操作系统的版本信息
        os_info['os_version'] = platform.version()
    
    except Exception as e:
        pass


    return os_info

def get_cpu_info():
    cpu_info = dict()
    try:
        # cpu 信息
        if platform.system() == 'Windows':
            w = wmi.WMI()
            for cpu in w.Win32_Processor():
                cpu_name = cpu.Name
                cpu_cores = cpu.NumberOfCores
                cpu_info['cpu_name'] = cpu_name
                cpu_info['cpu_cores'] = cpu_cores
        cpu_info['cpu_info'] = platform.processor()


    except Exception as e:
        pass
    pass

def get_net_info():
    net_info = {}

    try:
        pass
    except Exception as e:
        pass

def get_disk_info():
    disk_info_arr = []
    
    try:
        # windwos 磁盘检测
        disk_partitions = psutil.disk_partitions()
        for _disk in disk_partitions:
            disk_info = {}
            disk_info['fstype'] = _disk.fstype
            disk_info['path'] = _disk.device
            _disk_usage = (psutil.disk_usage(_disk.device))
            disk_info['total'] = _disk_usage.total
            disk_info['used'] = _disk_usage.used
            disk_info['free'] = _disk_usage.free
            disk_info['percent'] = _disk_usage.percent
            disk_info_arr.append(disk_info)
            
        # linux 磁盘检测

    except Exception as e:
        pass

    return disk_info_arr


def get_node_info():
    ret = {'ret': 0, 'err': ''}
    info = dict()
    os_info = get_os_info()
    cpu_info = get_cpu_info()
    disk_info = get_disk_info()
    
    info['os_info'] = os_info
    info['cpu_info'] = cpu_info
    info['disk_info'] = disk_info
    ret['info'] = info

    return ret



if __name__ == '__main__':
    print(get_node_info())


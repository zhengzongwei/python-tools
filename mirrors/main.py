#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/7 11:37                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

import toml
import os
import shutil

import os
import shutil
import toml


def create_directories(config):
    for os_name, versions in config.items():
        for version, info in versions.items():
            system_path = os.path.join(os_name, version)
            os.makedirs(system_path, exist_ok=True)
            if 'isos' in info:
                iso_path = os.path.join(str(system_path), 'isos')
                os.makedirs(iso_path, exist_ok=True)
                for iso_arch in info['isos']:
                    iso_dir = os.path.join(iso_path, iso_arch)
                    os.makedirs(iso_dir, exist_ok=True)
            if 'raspi_img' in info:
                raspi_dir = os.path.join(str(system_path), 'raspi_img')
                os.makedirs(raspi_dir, exist_ok=True)

            if 'os' in info or 'OS' in info:
                print(info,'321')
                print(system_path,'123')
                os_dir = os.path.join(str(system_path), 'os')
                os.makedirs(os_dir, exist_ok=True)


if __name__ == "__main__":
    # 读取配置文件
    with open('conf.toml', 'r') as f:
        config = toml.load(f)

    create_directories(config)

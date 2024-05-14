#  Copyright (c)2024. zhengzongwei
#  python-tools is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.


import sys
import logging
import psutil
import platform
import re
import subprocess as sp

logging.getLogger().setLevel(logging.DEBUG)


class CPUInfoBase(object):
    def __init__(self) -> None:
        self.cpu_cores: int = 0
        self.cpu_threads: int = 0
        self.cpu_arch: str = ''
        self.cpu_percent: list[int] = []
        self.model_name: str = ''

        self.get_cpu_info()

    def get_cpu_percent(self, interval: float = 0.5, percpu: bool = True) -> None:
        self.cpu_percent = psutil.cpu_percent(interval, percpu)

    def get_cpu_arch(self):
        self.cpu_arch = platform.processor()

    def get_cpu_count(self) -> None:
        cpu_threads = psutil.cpu_count()
        cpu_cores = psutil.cpu_count(logical=False)
        self.cpu_cores = cpu_cores
        self.cpu_threads = cpu_threads

    def get_cpu_name(self):
        sys_platform = sys.platform
        if sys_platform.startswith('linux'):
            cpu_info = LinuxCPUInfo()

        elif sys_platform.startswith('darwin'):
            cpu_info = DarwinCPUInfo()

        elif sys_platform.startswith('win32'):
            cpu_info = WinCPUInfo()
        else:
            cpu_info = CPUInfoBase()

        self.model_name = cpu_info.get_cpu_name()

    @staticmethod
    def exec(cmd: str) -> str:
        p = sp.Popen(cmd, stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.STDOUT, shell=True)
        out, err = p.communicate()
        logging.debug(f"out {out}, err {err}")
        if not p.returncode:
            return out.decode().strip()
            # print("code: {}, response:{} ".format(p.returncode, out.decode(agent)))

    def get_cpu_info(self):
        self.get_cpu_count()
        self.get_cpu_percent()
        self.get_cpu_count()
        self.get_cpu_name()
        self.get_cpu_arch()

    def __str__(self) -> dict[str, str]:
        return self.__dict__


class LinuxCPUInfo(CPUInfoBase):
    @staticmethod
    def get_cpu_detail(cpu_attr_name: str) -> str:
        with open('/proc/cpuinfo') as f:
            for line in f.readlines():
                if cpu_attr_name == "model_name":
                    _reg: str = r'model name\s+: (.*)'
                m = re.match(_reg, line)
                if m:
                    return m.group(1)

    def get_cpu_name(self) -> str:
        if self.get_cpu_detail('model_name') is not None:
            return self.get_cpu_detail('model_name')


class DarwinCPUInfo(CPUInfoBase):

    def get_cpu_name(self):
        command = 'sysctl -n machdep.cpu.brand_string'
        return self.exec(command)


class WinCPUInfo(CPUInfoBase):
    def get_cpu_name(self):
        pass


if __name__ == "__main__":
    print(CPUInfoBase().__dict__)

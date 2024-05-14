#  Copyright (c)2024. zhengzongwei
#  python-tools is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.


import logging
import psutil
from common import json_indent


class NETInfoBase(object):
    def __init__(self):
        self.nets: dict = {}
        self.get_net_info()

    def get_net_info(self):
        nets = psutil.net_if_addrs()
        for net_name in nets:
            net_info = nets[net_name]
            self.nets[net_name] = []
            for net in net_info:
                net_ip_info = {
                    'address': net.address,
                    'netmask': net.netmask,
                    'broadcast': net.broadcast,
                    'ptp': net.ptp
                }
                if hasattr(net.family, 'AF_INET'):
                    net_ip_info['net_type'] = 'IP v4'

                elif hasattr(net.family, 'AF_INET6'):
                    net_ip_info['net_type'] = 'IP v6'

                if net_ip_info not in self.nets[net_name]:
                    self.nets[net_name].append(net_ip_info)

    def __str__(self):
        return self.__dict__


if __name__ == '__main__':
    data = json_indent(NETInfoBase().__dict__)
    print(data)

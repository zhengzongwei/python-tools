#  Copyright (c)2025. zhengzongwei
#  flask-app is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.

import platform
import subprocess
import hashlib


class HardwareInfo:
    def __init__(self):
        self.os_type = platform.system()
        self.hardware_info = {}
        self.collect_info()

    def get_command_output(self, command):
        try:
            result = subprocess.check_output(command, shell=True)
            return result.decode().strip()
        except Exception as e:
            return str(e)

    def get_linux_info(self):
        self.hardware_info['system_serial_number'] = self.get_command_output("sudo dmidecode -s system-serial-number")
        self.hardware_info['board_serial'] = self.get_command_output("sudo dmidecode -s baseboard-serial-number")
        self.hardware_info['cpu_id'] = self.get_command_output(
            "sudo dmidecode -t processor | grep 'ID' | awk '{print $2}'")
        self.hardware_info['hard_disk_serial'] = self.get_command_output(
            "sudo hdparm -I /dev/sda | grep 'Serial Number' | awk '{print $3}'")
        self.hardware_info['mac_address'] = self.get_command_output(
            "cat /sys/class/net/$(ip route show default | awk '/default/ {print $5}')/address")

    def get_windows_info(self):
        self.hardware_info['system_serial_number'] = self.get_command_output("wmic bios get serialnumber").split('\n')[
            1].strip()
        self.hardware_info['board_serial'] = self.get_command_output("wmic baseboard get serialnumber").split('\n')[
            1].strip()
        self.hardware_info['cpu_id'] = self.get_command_output("wmic cpu get processorid").split('\n')[1].strip()
        self.hardware_info['hard_disk_serial'] = self.get_command_output("wmic diskdrive get serialnumber").split('\n')[
            1].strip()
        self.hardware_info['mac_address'] = self.get_command_output(
            "getmac | findstr /v 'Media disconnected' | findstr /v 'Hyper-V Virtual Ethernet Adapter'").split('\n')[
            0].split()[0]

    def get_macos_info(self):
        self.hardware_info['system_serial_number'] = self.get_command_output(
            "system_profiler SPHardwareDataType | grep 'Serial Number' | awk '{print $4}'")
        self.hardware_info['board_serial'] = self.get_command_output(
            "ioreg -l | grep IOPlatformSerialNumber | awk '{print $4}' | sed 's/\"//g'")
        self.hardware_info['cpu_id'] = self.get_command_output("sysctl -n machdep.cpu.brand_string")
        self.hardware_info['hard_disk_serial'] = self.get_command_output(
            "system_profiler SPSerialATADataType | grep 'Serial Number' | awk '{print $3}'")
        self.hardware_info['mac_address'] = self.get_command_output("ifconfig en0 | grep ether | awk '{print $2}'")

    def collect_info(self):
        if self.os_type == "Linux":
            self.get_linux_info()
        elif self.os_type == "Windows":
            self.get_windows_info()
        elif self.os_type == "Darwin":
            self.get_macos_info()
        else:
            self.hardware_info = {"error": "Unsupported OS"}

    def generate_machine_code(self):
        # 将硬件信息拼接成一个字符串
        info_str = ''.join(self.hardware_info.values())
        # 对拼接后的字符串进行哈希处理，生成唯一的机器码
        machine_code = hashlib.sha256(info_str.encode()).hexdigest()
        return machine_code

    def generate_key(self, machine_code):
        # 对机器码进行进一步处理，生成一个密钥
        key = hashlib.sha256(machine_code.encode()).hexdigest()
        return key

    def display_info(self):
        print("Hardware Information:")
        for key, value in self.hardware_info.items():
            print(f"{key}: {value}")


if __name__ == '__main__':
    hardware_info = HardwareInfo()
    hardware_info.collect_info()
    hardware_info.display_info()

    machine_code = hardware_info.generate_machine_code()
    print(f"Machine Code: {machine_code}")

    key = hardware_info.generate_key(machine_code)
    print(f"Generated Key: {key}")

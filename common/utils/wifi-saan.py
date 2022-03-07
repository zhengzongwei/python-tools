
"""
扫描当前Wi-Fi网络
"""

import pywifi
import time


def GetWifi():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.scan()
    time.sleep(5)
    wifi_list = ifaces.scan_results()
    for i in range(len(wifi_list)):
        print(wifi_list[i].ssid)

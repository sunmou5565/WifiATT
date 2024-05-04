import time


def scanwifi(pywifi,wk):
    Nc = pywifi.interfaces()[wk]
    Nc.scan()
    print("[*]正在搜索附近WIFI")
    time.sleep(2)
    SIDnum = 0
    sid_array=[]
    for wifi_info in Nc.scan_results():
        print(SIDnum, "->SSID:", wifi_info.ssid)# 将SSID存入数组
        sid_array.append(str(wifi_info.ssid))
        SIDnum += 1

    return sid_array
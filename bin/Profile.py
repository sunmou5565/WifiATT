import pywifi
from pywifi import const

def create_wifi_profile(ssid, password):
    profile = pywifi.Profile()
    profile.ssid = ssid  # 设置SSID
    profile.auth = const.AUTH_ALG_OPEN  # 设置认证算法为开放系统
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # 设置加密算法为WPA2PSK
    profile.cipher = const.CIPHER_TYPE_CCMP  # 设置加密方式为CCMP
    profile.key = password  # 设置密码

    return profile
import pywifi
from pywifi import const

def create_wifi_profile(ssid, password):
    profile = pywifi.Profile()
    profile.ssid = ssid  # 设置SSID
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password  # 设置密码
    return profile
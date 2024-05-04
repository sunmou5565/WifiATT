import pywifi
from bin import Injet, Init_Title, Scan

Init_Title.pr()
pywifi = pywifi.PyWiFi()
num = len(pywifi.interfaces())
j=0
for i in range(num):
    print(j,"->",pywifi.interfaces()[j])
    j += 1
wk=int(input("请输入网卡编号："))
sid_array = Scan.scanwifi(pywifi, wk)
Injet.connect(sid_array,wk)

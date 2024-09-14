# -*- coding: utf-8 -*-
from time import sleep
import requests

# 自动登录
def autoLogin():
    url = "http://10.255.0.19/drcom/login"
    try:
        once = requests.get(url=url,
                            params={'callback': 'dr1003', 'DDDDD': "2023307506@cmcc", 'upass': "AUST@2004",
                                    '0MKKey': 123456})
        sleep(2)
        twice = requests.get(url=url,
                             params={'callback': 'dr1003', 'DDDDD': "2023307506@cmcc", 'upass': "AUST@2004",
                                     '0MKKey': 123456})
        return "自动登陆成功"
    except:
        return "发生异常"

def get_public_ip():
    try:
        response = requests.get('http://ifconfig.me/ip')  # 发送GET请求获取IP地址
        if response.status_code == 200:
            return response.text.strip()  # 返回文本形式的IP地址
        else:
            print("Error: Unable to fetch IP address.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    autoLogin()
    while True:
        if get_public_ip() == "211.141.172.154":  #你的常用IP地址    
            autoLogin()
            public_ip = get_public_ip()
            print(f"Your public IP address is: {public_ip}")
        else :
            print(get_public_ip())
            break
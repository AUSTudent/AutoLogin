# -*- coding: utf-8 -*-
from time import sleep
import requests

# 自动登录
def autoLogin():
    url = "http://10.255.0.19/drcom/login"
    try:
        once = requests.get(url=url,
                            params={'callback': 'dr1003', 'DDDDD': "学号@运营商", 'upass': "密码",
                                    '0MKKey': 123456})
        sleep(2)
        twice = requests.get(url=url,
                             params={'callback': 'dr1003', 'DDDDD': "学号@运营商", 'upass': "密码",
                                     '0MKKey': 123456})
        return "自动登陆成功"
    except:
        return "发生异常"

def get_public_ip():
    try:
        response = requests.get('http://ifconfig.me/ip')  # 发送GET请求到ipify.org
        if response.status_code == 200:
            #return response.text.strip() # 返回文本形式的IP地址
            ip_address = response.text.strip()
            ip_parts = ip_address.split('.')  # 分割IP地址
            ip_sum = sum(int(part) for part in ip_parts)  # 将各部分转换为整数并求和
            return ip_sum
        else:
            print("Error: Unable to fetch IP address.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    autoLogin()
    #建议少用稳定突破的IP，仅推荐在下载大量内容时手动使用
    while True:
        if 000 <= get_public_ip() <=  000:  #你的常用ip范围，建议获取Get_IP值后上下浮动一下  
            autoLogin()
            sleep(1)
            public_ip_Num = get_public_ip()
            print(f"Your public IP address_NumSum is: {public_ip_Num}")
        else :
            print(get_public_ip())
            break
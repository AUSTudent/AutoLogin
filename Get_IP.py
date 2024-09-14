from time import sleep
import requests

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
    
public_ip_Num = get_public_ip()
print(f"Your public IP address_sum is: {public_ip_Num}")
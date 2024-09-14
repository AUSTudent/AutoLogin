from time import sleep
import requests

def get_public_ip():
    try:
        response = requests.get('http://ifconfig.me/ip')  # 发送GET请求到ipify.org
        if response.status_code == 200:
            return response.text.strip()  # 返回文本形式的IP地址
        else:
            print("Error: Unable to fetch IP address.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

public_ip = get_public_ip()
print(f"Your public IP address is: {public_ip}")
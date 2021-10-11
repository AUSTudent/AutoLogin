<div align="center">
<h1>自动登录安徽理工大学校园网</h1>
</div>


# 前言
+ 🌟 推荐使用[ Shell 版本](https://github.com/flipped-1121/AutoLogin/tree/shell)
+ 🙄 每天打开浏览器，点击`请选择出口`，再进行登录，不胜其烦。
+ 😎 恰好有点 Python 小基础和 CV 的能力。
+ ✨ 实际上两行代码就可以解决问题。
+ 🗿 代码较烂，望理解！
+ 🌟 解除宽带速度限制。


# 配置并运行

## 环境配置
✅ Python

## clone 并进入本项目，下载所需包
```bash
git clone https://github.com/flipped-1121/AutoLogin.git
cd AutoLogin
pip install -r requirements.txt
```

# 修改配置信息
在`config.yml`中修改相关配置
```yml
url:
  login: "http://10.255.0.19/drcom/login"
  logout: "http://10.255.0.19/drcom/logout"  # 不知道为啥要写登出

users:
  # 单个账户设置
  - user:
      userid: 201930****           # 学/工号
      password: *******            # 密码
      ISP: 电信                     # 运营商，可选：教职工、电信、联通、移动
      0MKKey: 123456               # 不知道有啥用，但是有用
  # 多账号设置，已解除账号登陆设备数量限制，应用场景较少
#   - user:
#       userid:  # 学/工号
#       password: # 密码
#       ISP:  # 运营商，可选：教职工、电信、联通、移动

# 通知相关，建议不填，默认进行 Windows 通知
msg:
  go-cqhttp:
    # url 推送到个人QQ: http://127.0.0.1:port/send_private_msg  群：http://127.0.0.1:port/send_group_msg
    # token 填写在go-cqhttp文件设置的访问密钥
    # qq 被通知的QQ
    # go-cqhttp相关API https://docs.go-cqhttp.org/api
    url: "http://127.0.0.1:port/send_private_msg"
    token: *****************************
    qq: "2517421382"
  win:
    title: "自动连接🔗"  # Windows 系统通知标题
```

## 运行和调试
🟢运行
```bash
python AutoLogin.py
```
![Success](https://cdn.jsdelivr.net/gh/flipped-1121/BlogPictures/flipped-1121-PIC/20210904155520.png)

## 开机自启
新建文件`AutoLogin.vbs`,写入以下内容：
```bash
Set oShell = WScript.CreateObject ("WSCript.shell")
oShell.run "AutoLogin.py所在目录，例如：F:\Python\code\AutoLogin\AutoLogin.py",0
Set oShell = Nothing
```
将此文件放置到`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup`目录下。
<h1>Congratulations🎉</h1>

## 解除宽带限速
经过测试（~~无意间发现~~），当进行两次登录后，即可突破就宽带速度限制。


# One More Thing
✨实际上两行代码就可以解决问题。

|登录入口|对应参数|
|-------|------|
|教职工|@jzg|
|电信|@aust|
|联通|@unicom|
|移动|@cmcc|
```python
import requests
r = requests.get("http://10.255.0.19/drcom/login?callback=dr1003&DDDDD=学号@****&upass=密码&0MKKey=123456")
```
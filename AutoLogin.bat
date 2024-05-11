@echo off
::校园网名称：学生AUST_Student 教职工AUST_Faculty
set wifiName=AUST_Student
::校园网账号
set userId=201930****
::校园网密码
set Password=*******
::校园网运营商入口
::电信aust 联通unicom 移动cmcc 教职工jzg
set operatorCode=****

ping -n 1 -w 100 10.255.0.19 | findstr /i "TTL" >nul
if %ERRORLEVEL% equ 0 goto POST
@echo on
netsh wlan connect name = %wifiName%

@echo off
:CHECK_CONNECTION
netsh wlan show interface | findstr /i /e %wifiName% >nul
if %ERRORLEVEL% neq 0 goto CHECK_CONNECTION

:POST
@echo on
curl --max-time 2 --retry 4 --retry-delay 1 -d "callback=dr1003&DDDDD=%userId%@%operatorCode%&upass=%Password%&0MKKey=123456" http://10.255.0.19/drcom/login
curl --max-time 2 --retry 4 --retry-delay 1 -d "callback=dr1003&DDDDD=%userId%@%operatorCode%&upass=%Password%&0MKKey=123456" http://10.255.0.19/drcom/login

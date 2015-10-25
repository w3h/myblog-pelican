Title: 多线程WordPress后台密码爆破
Date: 2014-7-13 13:30
Tags: wordpress,python

本软件使用python编写，可以爆破WordPress后台密码。本软件为原创作品，如果转载请注名出去。郑重声明，本软件仅供学习和交流，请务用于非法用途

##### **1、功能说明** #####

1.支持多线程破解，默认为单线程

2.支持进度条显示

3.支持连接异常时延时重试，减小了并发数过大或者网络不稳定时的异常

4.支持爆破异常时，记录异常的用户名和密码，防止漏检

5.支持执行时间显示

6.支持单用户的密码破解，也支持多用户的密码破解

##### **2、程序运行** #####

帮助信息如下：

    C:\01-Code\00-Python\wpcrack v2.0\wppassword\dist>wppassword.exe
    Usage: wppassword [-u <url>]  [-n <username or username file>] [-f <password file>] [-t <thread num>]
    
    Options:
      -h, --help       show this help message and exit
      -u URL           scan url
      -n USERNAME      username or username file
      -f PASSWORDFILE  password file
      -t THREAD        thread number (default 1)


运行结果如下：

    C:\01-Code\00-Python\wpcrack v2.0\wpuser\dist>wppassword.exe -u http://ear.xxx.com/wp-login.php -u admin -f pass.txt -t 10
    [+] http://ear.xxx.com/wp-login.php
    [+] |##############################|  100% (529 - 529)
    [+] 13.2279999256

运行后会生成一个output目录，各文件功能说明如下

1.errlog-wppassword.txt文件，记录爆破异常的用户名和密码，如果有异常记录，建议使用此文件再执行一次

2.result-wppassword.txt文件，记录爆破成功的用户名和密码

3.log-wppassword.txt文件，记录处理异常信息，可用于跟踪处理异常原因


##### **3、下载** #####

源码和exe文件 [下载路径](/static/code/wppassword.rar)

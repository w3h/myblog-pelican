Title: 目录扫描器（PathScanner）
Date: 2015-1-25 9:30
Tags: Code,Tool

近一段时间使用python写了一个目录扫描器，并参照了一些目前流行的扫描器，作了一些小的改进，功能不是很复杂，麻烦的就是写界面。由于对微软的 `MFC` 框架很熟悉，所以就选择了 `wxPython` 作为界面开发，熟悉这个库到是很快，写界面大多数时间都花在找对应的函数上啦。目前支持的功能如下:

    1、增加了对网站使用的脚本语言的自动识别

    2、扫描的数据库增加了命中率参数，每次先扫描命中率高的目录，扫描后刷新目录的命中率值

    3、同时支持命令项和界面操作

    4、可以选择本地文件进行扫描（注：选择文件扫描不支持命中率排序）



【界面】

![PathScanner](/static/images/pathscanner.gif)


【命令行】

    D:\pathscanner>pathscanner.py -t http://www.xxx.com.cn
    ......................................................................
             (__)
             (oo)
       /------\/ ------ PathScanner V1.0 by W.HHH ------
      / |    ||
     *  /\---/\
        ~~   ~~
    .... Good Luck for you today .......
    ......................................................................
     [ Target]: http://www.xxx.com.cn
     [ Server]: Microsoft-IIS/7.5
     [ Script]: ['common', 'php']
     [   data]: None
     [ Thread]: 10
     [TimeOut]: 10
     [Numbers]: 1372
     [ Output]: D:\pathscanner./output/www.xxx.com.cn.html

     [+] 200 : /robots.txt
     [+] 200 : /index.php/module/action/param1/%7B$%7Bphpinfo()%7D%7D
     [+] 200 : /index.php/Index/index/name/$%7B@phpinfo%28%29%7D
     [+] 200 : /index.php
     [+] 200 : /admin.php
     [+] 200 : /Admin.php
     [P] 1372 / 1372

【源代码下载】

[下载路径](https://github.com/webhhh/pathscanner/)


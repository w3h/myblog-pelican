Title: 渗透测试中常用的Google收集信息技巧
Date: 2014-08-01 07:22
Tags: Tool,Google


渗透测试过程中，收集信息第一步都会从Google入手，下面收录工作中一些常用的语句和技巧


##### **1、查看子系统**

    site:****.com   -www -sys


##### **2、判断使用的语言**

    site:****.com filetype:php
    site:****.com filetype:jsp
    site:****.com filetype:asp
    site:****.com filetype:aspx


##### **3、找重要信息**

    site:****.com   warning
    site:****.com   error
    site:****.com   index of


##### **4、找后台**

    site:****.com intext:管理|后台|登陆|用户名|密码|验证码|系统|帐号|manage|admin|login|system
    site:*****.com inurl:login|admin|manage|manager|admin_login|login_admin|system
    site:****.com intitle:管理|后台|登陆|
    site:****.com intext:验证码


##### **5、找编辑器**

    site:****.com   inurl:fck|fckedit|fckeditor|editor


##### **6、找上传目录**

    site:xxxx.com filetype:pdf|gif|txt inurl:upload


##### **7、找备份文件**

    site:www.****.com  filetype:bak|zip|rar|tar


##### **8、注意**

上面方法找不到，需要查看robots.txt文件，此文件一般会屏蔽一些重点目录，个人建议第一问步先查robots.txt，如下面网站通过查robots.txt文件，知道版本和后台登陆页面

    #
    # robots.txt for PHPCMS v9
    #
    User-agent: * 
    Disallow: /caches
    Disallow: /phpcms
    Disallow: /install
    Disallow: /phpsso_server
    Disallow: /api
    Disallow: /admin.php

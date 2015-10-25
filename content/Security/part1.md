Title: 移动安全小试牛刀 - 从移动应用进行渗透
Date: 2015-03-13 09:30
Tags: 移动安全

某日，攻城久攻不下，无耐之举，只能另引思路。回想，近日一直在苦研移动APK安全，熟知移动应用目前安全处于水身火热、九死一生的现状，能否通过移动应用进行突破呢？放眼望去，果然，城池大们旁就悬挂着APK的下载地址，掏出我的牛刀，以试深浅。

1、下载APK进行反编译

    > 正在反编译Apk...  - 成功！
    > 正在将dex转成jar...  - 成功！
    > .smali输出目录：D:\Users\W.HHH\ApkIDE\Work\com.xxxxxxxxx
    > .class输出目录：D:\Users\W.HHH\ApkIDE\Worksrc\com.xxxxxxxxx


2、获取所有URL

使用正则表达式搜索所有的URL信息，直接过滤WSDL接口的地址如下

    http://xxxxx.xxx.com/Service/Service.asmx
    http://xxxxx.xxx.com/CtccServiceZhejiang.asmx
    http://xxxxx.xxx.com/InvoiceService.asmx

3、WSDL扫描

直接使用WVS的接口扫描工具，扫描结果如下

![Alt text](/static/images/part1-wsdl.gif)


4、注入拿到数据库

通过注入拿到手机服务器的数据库，找到数据库中的账号和密码


5、登录主站后台

使用获取的帐户和密码尝试登陆主站的后台，提权拿到服务器


##### **6、总结**

** 千里之堤毁于蚁穴，安全是一个整体的工程，移动应用大行之道之际，安全问题也不容忽视。** 



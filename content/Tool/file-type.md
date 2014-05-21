Title: window下快速判断文件编码格式的方法
Date: 2014-05-16 10:26
Tags: 文件编码,Tool


1、常见的文件编码格定义如下:

* ANSI：无格式定义，开头就是文件内容
* Unicode：前两个字节为 FFFE
* Unicode big endian：前两字节为 FEFF
* UTF-8：前两字节为 EFBB


2、使用windows自带的notepad可以快速的判断，方法如下:

* 打开notepad
* 将文件拖入notepad
* 另存为
* 在另存为对话框的“编码”项中可以看到文件的当前编码格式

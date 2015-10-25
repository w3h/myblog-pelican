Title: Beebeeto-POC下载器
Date: 2014-11-1 18:50
Tags: Code,Tool

最近一直在关注beebeeto.com网站，这个网站的思路个人觉得很不错，利用互联网的思想来开始POC，然后将这些POC加载到各种扫描器上，就可以形成一个具有中国特色的强大的扫描器，当然前提是POC的质量要非常高，不然误报率会很高。

此网站还提供了一个开放的POC开发框架，写得的确不错。为了方便下载各种POC，本人花了点时间写了一个下载器。程序说明如下


【说明】

用于Beebeeto的POC批量下载，执行后会在程序目录创建一个poc目录，所有的poc都会下载到此文件夹中，并生成一个readme.html文件用于检索

【命令行】

update.py cookie

【实例】

D:\04-Code\00-Python\Beebee>update.py "csrftoken=R6x8TFLHcVPc9RQYj1Kqj3rIaxeRMaH 7; sessionid=pa1kll51m9cldfux2ml68k6oooz8le0f; CNZZDATA1253290531=1433061732-141 4286034-%7C1414837434"

[*] Get Poc -> poc-2014-0135

[*] Get Poc -> poc-2014-0134

[*] Get Poc -> poc-2014-0133

[*] Get Poc -> poc-2014-0132

[*] Get Poc -> poc-2014-0131

[*] Get Poc -> poc-2014-0130

[*] Get Poc -> poc-2014-0129

[*] Get Poc -> poc-2014-0128

[*] Get Poc -> poc-2014-0127

[*] Get Poc -> poc-2014-0126

[*] Get Poc -> poc-2014-0125



代码下载链接：

[代码下载](https://github.com/webhhh/Beebeeto-POC-Downloader/)


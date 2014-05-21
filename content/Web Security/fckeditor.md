Title: fckeditor各版本漏洞研究
Date: 2014-05-12 10:22
Tags: fckeditor

#### **1、判断fckeditor版本方法**

使用如下文件可以判断fckeditor版本，一般用户都会删除_whatnew.html，但三个js文件并不会改变，在下面文件中搜索`2.`就可查询到具体的版本

    \fckeditor\fckeditor.js
    \fckeditor\_whatsnew.html
    \fckeditor\editor\dialog\fck_about.html
    \fckeditor\editor\js\fckeditorcode_gecko.js
    \fckeditor\editor\js\fckeditorcode_ie.js

#### **2、扩展名%00截断漏洞**

【影响版本】：所有的ASP版本

【漏洞来源】：http://www.exploit-db.com/exploits/23005/ 

【分析时间】：2014年5月21日

【代码分析】：

程序中使用用户输入的扩展名，且扩展名没有过滤，调用低层`ADODB.Stream`组件写文件时，%00认为字符串的结束符，导致字符截断，上传文件的扩展名被改变

<code>

			' Get the uploaded file name.
			sFileName	= oUploader.File( "NewFile" ).Name
			sExtension	= oUploader.File( "NewFile" ).Ext  '获取方法是截取从尾部到第一个.的位置字符
			sFileName = SanitizeFileName( sFileName )      '文件名有过滤
			sOriginalFileName = sFileName

			Dim iCounter
			iCounter = 0

			Do While ( True )
				Dim sFilePath
				sFilePath = CombineLocalPaths(sServerDir, sFileName)

				If ( oFSO.FileExists( sFilePath ) ) Then
					iCounter = iCounter + 1
                    '----------------------------------------------------------------------------------
                    ' 上传重复文件名即可进入这个分支
                    ' sExtension变量没有过滤导致存在%00截断，调用SaveAs时%00后面的内容就会被忽略
                    ' 如果sExtension为asp%00jpg，SaveAs写文件时，文件的后缀就会变成asp
                    ' 原因是c语言遇见%00就认为是字符串的结束符
                    '----------------------------------------------------------------------------------
					sFileName = RemoveExtension( sOriginalFileName ) & "(" & iCounter & ")." & sExtension
					sErrorNumber = "201"
				Else
					oUploader.SaveAs "NewFile", sFilePath
					If oUploader.ErrNum > 0 Then sErrorNumber = "202"
					Exit Do
				End If
			Loop

</code>

【漏洞利用】：

1、上传文件名'xxx.aps;gif'的文件，使用burp截断消息，发送到Repeater模块，将`;`修改为`%00`的url编码格式，重复发送两次即可


【漏洞修复】：

1、获取文件扩展名调用`SanitizeFileName`函数过滤一下

2、文件名写一个时间的随机函数，不使用用户输入的文件信息，更加安全一些

3、上传成功后sendUploadResults函数不要返回具体的文件上传信息




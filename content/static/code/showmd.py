#coding=utf-8
import sys
import os
import markdown
import win32api


# 需要设置opentool为本机的目录 
info = ''
mdhtml = 'mdtmp.html'
opentool = "C:/Program Files/Internet Explorer/iexplore.exe"

# 读取md文件内容
tmppath = os.path.dirname(os.path.abspath(sys.argv[0]))
with open(sys.argv[1], 'r') as fp: info = fp.read()

# 编译md文件生成一个临时html文件
mdfile = markdown.markdown(info)
tmpfilename = tmppath + '/' + mdhtml
with open(tmpfilename, 'w') as fp: fp.write(mdfile)

# 使用浏览器打开生成的html文件
win32api.ShellExecute(0, 'open', opentool, tmpfilename, '', 1)



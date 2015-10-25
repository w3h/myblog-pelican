Title: 搭建markdown环境(vim+markdown+ie)
Date: 2014-05-16 11:52
Tags: 文件编码,Tool


#### 1、markdown环境的安装

* 安装python环境，目前我安装的版本是python 2.7
* 安装markdown的python库，[安装文件][1]，相关markdown语法可以参考[链接][4]
* 安装vim环境，到处都是，而且Linux默认安装的神器
* 安装vim支持md文件高亮显示插件，此处推建下载GitHub上的最新版本，[安装文件][2]


#### 2、解决markdown文件浏览问题

markdown在window下默认不支持的markdown编辑工具，其它一些工具我也简单的试用了一下，习惯不了，而且现在都习惯了vim编辑器，所以想到了下面方法解决vim对md文件的浏览问题

* 将文件[showmd.py][3]下载到本机，代码如下，修改文件内的浏览器地址 `opentool = "C:/Program Files/Internet Explorer/iexplore.exe" ` 为本机IE地址即可

    import sys      
    import os      
    import markdown      
    import win32api      

    info = ''      
    mdhtml = 'mdtmp.html'      
    opentool = "C:/Program Files/Internet Explorer/iexplore.exe"      

    tmppath = os.path.dirname(os.path.abspath(sys.argv[0]))      
    with open(sys.argv[1], 'r') as fp: info = fp.read()      

    mdfile = markdown.markdown(info)      
    tmpfilename = tmppath + '/' + mdhtml      
    with open(tmpfilename, 'w') as fp: fp.write(mdfile)      
 
    win32api.ShellExecute(0, 'open', opentool, tmpfilename, '', 1)  

* 将上面文件设置vim的快捷键 `nmap <F12> :!python D:/Vim/vimfiles/showmd.py %<CR> `，以后打开md文件，直接按快捷件即可在ie中浏览



[1]: https://pypi.python.org/packages/any/M/Markdown/
[2]: https://github.com/plasticboy/vim-markdown
[3]: ./../static/code/showmd.py
[4]: https://github.com/riku/Markdown-Syntax-CN/blob/master/syntax.md

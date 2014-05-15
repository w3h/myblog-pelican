Title: xpath快速应用平台搭建
Date: 2014-5-10 12:14
Tags: xpath, FirePath, Scrapy

xpath的语法虽然不算复杂，但在要庞大的网页中准确的写出对应的xpath表达式，还是一个不容易的事。使用下面二个工具使用，会起到立竿见影的效果，再也不用盯着网页数节点

##### **1、FirePath** #####

一个FireFox扩展插件，可以准确的提取网页中的每一个元素的xpath匹配信息，安装FireFox插件需要先安装Firebug插件，这个我相信大家并不陌生，比如要抓取搜狐网导航上的“搜狗”两字，使用此插件抓取xpath信息如下


    .//*[@id='navList']/div[1]/ul/li[1]


##### **2、Scrapy shell** #####

Scrapy是一个使用python写的爬虫框架，使用此框架，开发者能够快速的开发一个网络爬虫，Scrapy shell是Scrapy提供的一个调试工具，可以抓取网页内容，里面集成了一个xpath的调试函数，借助此函数可以验证FirePath抓取的xpath匹配信息是否正确，使用如下命令启动shell调试

    scrapy shell "http://www.sohu.com"

显示如下

    [s] Available Scrapy objects:
    [s]   crawler    <scrapy.crawler.Cr.//*[@id='navList']/div[1]/ul/li[1]awler object at 0x011FA310>
    [s]   item       {}
    [s]   request    <GET http://sohu.com>
    [s]   response   <200 http://www.sohu.com/>
    [s]   sel        <Selector xpath=None data=u'<html><head><script type="text/javascrip'>
    [s]   settings   <CrawlerSettings module=None>
    [s]   spider     <Spider 'default' at 0x1bd5d10>
    [s] Useful shortcuts:
    [s]   shelp()           Shell help (print this help)
    [s]   fetch(req_or_url) Fetch request (or URL) and update local objects
    [s]   view(response)    View response in a browser

使用FirePath的xpath抓取结果

    >>> sel.xpath(".//*[@id='navList']/div[1]/ul/li[1]")
    [<Selector xpath=".//*[@id='navList']/div[1]/ul/li[1]" data=u'<li class="red"><a href="http://www.sogo'>]


##### **3、问题** #####

两个工具配合，基本不用深入理解xpath语法，也能快速的使用xpath语法抓取，但偶尔会出现两个工具之间不一致的情况，适当排查修改一下即可。



##### **4、阅读资料** #####

*  [w3school XPath 教程](http://www.w3school.com.cn/xpath/)
*  [Scrapy shell使用](http://blog.csdn.net/php_fly/article/details/19555969)



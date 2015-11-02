Title: scrapy中文下载地址解决方法
Date: 2015-11-01 14:45
Tags: scrapy

最近在写爬虫相关的代码时，发现一个scrapy中文下载地址问题。使用scrapy抓取的页面中文都使用了unicode格式，抓起下载地址使用unicode格式，文件无法下载。经过自己实际研究和读scrapy源码，总结了如下三种解决方法。当然也可能存在其它的方法，欢迎大家相互交流。

##方法一：

使用BeautifulSoup解析，并使用正则获取下载地址，然后直接使用`urllib.quote`转换成url编码

    <code>
            soup = BeautifulSoup(response.body)
            tb = soup.findAll('table')
            result = re.findall('<a href="(.*?)"', tb[0].renderContents())
            result = urllib.quote(result[0])
    </code>

###方法二：

后来发现一种更简单的方法，直接使用`urllib.quote`就可以搞定，此函数可以直接转换，写法如下

    <code>
            link = response.xpath('//table/tr[5]/td[2]/a/@href').extract()[0]
            link = urllib.quote(str(link)).decode("utf-8")
    </code>

###方法三：

当然还有一种方法可以先将`response.body`直接从unicode编码转换成utf-8，然后使用`response`的`replace`函数覆盖body，此方法未验证，理论可行，伪代码如下:

    <code>
            body = response.body转换为utf-8
            response = response.replace(body=body)
    </code>



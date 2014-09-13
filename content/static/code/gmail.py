#!/usr/bin/python
#coding=utf8
import sys

def banner():
    pass

def usage():
  if len(sys.argv) < 2:
    print ''
    print 'Usage:' 
    print '  python gmail.py [mail]'
    sys.exit(1)

def main():
    banner()    
    usage()

    print "[Result]"
    flag = False
    try:
        for line in open("Gmail.txt", 'rb'):
            if sys.argv[1] in line[:line.find(':')]:
                flag = True
                print line,
    except:
        return

    if not flag:
        print "Sorry, No Find!"
#end

if __name__ == "__main__":
    main()



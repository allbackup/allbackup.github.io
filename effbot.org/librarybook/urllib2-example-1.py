# File: urllib2-example-1.py

import urllib2

f = urllib2.urlopen("http://www.python.org")

for k, v in f.headers.items():
    print k, "=", v

print "read", len(f.read()), "bytes from", f.geturl()


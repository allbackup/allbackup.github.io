# File: urllib2-example-1.py

import urllib2

f = urllib2.urlopen("http://www.python.org")

for k, v in f.headers.items():
    print k, "=", v

print "read", len(f.read()), "bytes from", f.geturl()

## content-length = 11445
## accept-ranges = bytes
## server = Apache/2.0.54 (Debian GNU/Linux) DAV/2 SVN/1.1.4 mod_python/3.1.3
## Python/2.3.5 mod_ssl/2.0.54 OpenSSL/0.9.7e
## last-modified = Fri, 18 May 2005 18:26:14 GMT
## connection = close
## etag = "601f6-2cb5-128c3d80"
## date = Sat, 1 Jun 2005 12:00:00 GMT
## content-type = text/html
## read 11445 bytes from http://www.python.org

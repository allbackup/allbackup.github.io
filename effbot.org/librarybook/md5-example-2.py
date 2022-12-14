# File: md5-example-2.py

import md5
import string
import base64

hash = md5.new()
hash.update("spam, spam, and eggs")

value = hash.digest()

print hash.hexdigest()

# in Python 1.5.2 and earlier, use this instead:
# print string.join(map(lambda v: "%02x" % ord(v), value), "")

print base64.encodestring(value)


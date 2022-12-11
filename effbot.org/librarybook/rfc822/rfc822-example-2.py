# File: rfc822-example-2.py

import rfc822

file = open("samples/sample.eml")

message = rfc822.Message(file)

print message.getdate("date")
print message.getaddr("from")
print message.getaddrlist("to")

## $ python rfc822-example-2.py
## (2000, 11, 14, 14, 55, 7, 0, 0, 0)
## ('Frank', 'your@editor')
## [('Fredrik Lundh', 'fredrik@effbot.org')]

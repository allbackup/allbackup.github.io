# File: poplib-example-1.py

import poplib
import string, random
import StringIO, rfc822

SERVER = "pop.spam.egg"

USER  = "mulder"
PASSWORD = "trustno1"

# connect to server
server = poplib.POP3(SERVER)

# login
server.user(USER)
server.pass_(PASSWORD)

# list items on server
resp, items, octets = server.list()

# download a random message
id, size = string.split(random.choice(items))
resp, text, octets = server.retr(id)

text = string.join(text, "\n")
file = StringIO.StringIO(text)

message = rfc822.Message(file)

for k, v in message.items():
    print k, "=", v

print message.fp.read()

## $ python poplib-example-1.py
## subject = ANN: (the eff-bot guide to) The Standard Python Library
## message-id = <199910120808.KAA09206@spam.egg>
## received = (from fredrik@spam.egg)
##  by spam.egg (8.8.7/8.8.5) id KAA09206
##  for mulder; Tue, 12 Oct 1999 10:08:47 +0200
## from = Fredrik Lundh <fredrik@spam.egg>
## date = Tue, 12 Oct 1999 10:08:47 +0200
## to = mulder@spam.egg
## 
## ...

# File: telnetlib-example-1.py

import telnetlib
import sys

HOST = "spam.egg"

USER = "mulder"
PASSWORD = "trustno1"

telnet = telnetlib.Telnet(HOST)

telnet.read_until("login: ")
telnet.write(USER + "\n")

telnet.read_until("Password: ")
telnet.write(PASSWORD + "\n")

telnet.write("ls librarybook\n")
telnet.write("exit\n")

print telnet.read_all()

## [spam.egg mulder]$ ls
## README                                 os-path-isabs-example-1.py
## SimpleAsyncHTTP.py                     os-path-isdir-example-1.py
## aifc-example-1.py                      os-path-isfile-example-1.py
## anydbm-example-1.py                    os-path-islink-example-1.py
## array-example-1.py                     os-path-ismount-example-1.py
## ...

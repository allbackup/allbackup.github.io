# File: pyclbr-example-3.py

import pyclbr

# available in Python 2.0 and later
mod = pyclbr.readmodule_ex("cgi")

for k, v in mod.items():
    print k, v


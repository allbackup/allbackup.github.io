# File: sys-exit-example-2.py

import sys

print "hello"

try:
    sys.exit(1)
except SystemExit:
    pass

print "there"

## hello
## there

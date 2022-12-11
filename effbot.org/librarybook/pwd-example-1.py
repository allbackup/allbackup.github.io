# File: pwd-example-1.py

import pwd
import os

print pwd.getpwuid(os.getuid())
print pwd.getpwnam("root")


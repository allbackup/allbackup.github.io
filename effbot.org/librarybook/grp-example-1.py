# File: grp-example-1.py

import grp
import os

print grp.getgrgid(os.getgid())
print grp.getgrnam("wheel")


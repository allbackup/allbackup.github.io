# File: grp-example-1.py

import grp
import os

print grp.getgrgid(os.getgid())
print grp.getgrnam("wheel")

## $ python grp-example-1.py
## ('effbot', '', 4711, ['effbot'])
## ('wheel', '', 10, ['root', 'effbot', 'gorbot', 'timbot'])

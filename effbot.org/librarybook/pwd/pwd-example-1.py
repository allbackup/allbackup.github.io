# File: pwd-example-1.py

import pwd
import os

print pwd.getpwuid(os.getuid())
print pwd.getpwnam("root")

## ('effbot', 'dsWjk8', 4711, 4711, 'eff-bot', '/home/effbot', '/bin/bosh')
## ('root', 'hs2giiw', 0, 0, 'root', '/root', '/bin/bash')

# File: sys-stdout-example-1.py

import sys
import string

class Redirect:

    def __init__(self, stdout):
        self.stdout = stdout

    def write(self, s):
        self.stdout.write(string.lower(s))

# redirect standard output (including the print statement)
old_stdout = sys.stdout
sys.stdout = Redirect(sys.stdout)

print "HEJA SVERIGE",
print "FRISKT HUMÖR"

# restore standard output
sys.stdout = old_stdout

print "MÅÅÅÅL!"

## heja sverige friskt humör
## MÅÅÅÅL!

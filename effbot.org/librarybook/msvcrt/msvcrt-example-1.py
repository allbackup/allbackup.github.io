# File: msvcrt-example-1.py

import msvcrt

print "press 'escape' to quit..."

while 1:
    char = msvcrt.getch()
    if char == chr(27):
        break
    print char,
    if char == chr(13):
        print

## $ python msvcrt-example-1.py
## press 'escape' to quit...
## h e l l o

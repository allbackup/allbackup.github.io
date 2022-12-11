# File: posix-example-1.py

import posix

for file in posix.listdir("."):
    print file, posix.stat(file)[6]


# File: mmap-example-1.py

import mmap
import os

filename = "samples/sample.txt"

file = open(filename, "r+")
size = os.path.getsize(filename)

data = mmap.mmap(file.fileno(), size)

# basics
print data
print len(data), size

# use slicing to read from the file
print repr(data[:10]), repr(data[:10])

# or use the standard file interface
print repr(data.read(10)), repr(data.read(10))


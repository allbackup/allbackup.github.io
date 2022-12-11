# File: tempfile-example-2.py

import tempfile

file = tempfile.TemporaryFile()

for i in range(100):
    file.write("*" * 100)

file.close() # removes the file!

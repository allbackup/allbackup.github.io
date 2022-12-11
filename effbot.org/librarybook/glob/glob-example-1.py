# File: glob-example-1.py

import glob

for file in glob.glob("samples/*.jpg"):
    print file

## samples/sample.jpg

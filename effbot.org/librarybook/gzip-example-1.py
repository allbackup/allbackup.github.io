# File: gzip-example-1.py

import gzip

file = gzip.GzipFile("samples/sample.gz")

print file.read()


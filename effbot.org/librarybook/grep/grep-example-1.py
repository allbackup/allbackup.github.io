# File: grep-example-1.py

import grep
import glob

grep.grep("\<rather\>", glob.glob("samples/*.txt"))
$ python grep-example-1.py
4: indentation, rather than delimiters, might become

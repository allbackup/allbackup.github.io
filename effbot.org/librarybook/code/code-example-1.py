# File: code-example-1.py

import code
import string

# 
SCRIPT = [
    "a = (",
    "  1,",
    "  2,",
    "  3 ",
    ")",
    "print a"
]

script = ""

for line in SCRIPT:
    script = script + line + "\n"
    co = code.compile_command(script, "<stdin>", "exec")
    if co:
        # got a complete statement.  execute it!
        print "-"*40
        print script,
        print "-"*40
        exec co
        script = ""

## $ python code-example-1.py
## ----------------------------------------
## a = (
##   1,
##   2,
##   3 
## )
## ----------------------------------------
## ----------------------------------------
## print a
## ----------------------------------------
## (1, 2, 3)

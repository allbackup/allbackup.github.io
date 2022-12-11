# File: rexec-example-1.py

import rexec

r = rexec.RExec()
print r.r_eval("1+2+3")
print r.r_eval("__import__('os').remove('file')")


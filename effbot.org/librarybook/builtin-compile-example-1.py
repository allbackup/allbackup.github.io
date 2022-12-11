# File: builtin-compile-example-1.py

NAME = "script.py"

BODY = """
prnt 'owl-stretching time'
"""

try:
    compile(BODY, NAME, "exec")
except SyntaxError, v:
    print "syntax error:", v, "in", NAME


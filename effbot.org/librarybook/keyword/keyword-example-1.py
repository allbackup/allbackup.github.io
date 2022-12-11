# File: keyword-example-1.py

import keyword

name = raw_input("Enter module name: ")

if keyword.iskeyword(name):
    print name, "is a reserved word."
    print "here's a complete list of reserved words:"
    print keyword.kwlist
else:
    print name, "is a valid module name."

## $ python keyword-example-1.py
## Enter module name: assert
## assert is a reserved word.
## here's a complete list of reserved words:
## ['and', 'assert', 'break', 'class', 'continue', 'def', 'del',
## 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from',
## 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or',
## 'pass', 'print', 'raise', 'return', 'try', 'while']

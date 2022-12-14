# File: tokenize-example-1.py

import tokenize

file = open("tokenize-example-1.py")

def handle_token(type, token, (srow, scol), (erow, ecol), line):
    print "%d,%d-%d,%d:\t%s\t%s" % \
        (srow, scol, erow, ecol, tokenize.tok_name[type], repr(token))

tokenize.tokenize(
    file.readline,
    handle_token
    )

## 1,0-1,6:     NAME    'import'
## 1,7-1,15:    NAME    'tokenize'
## 1,15-1,16:   NEWLINE '\012'
## 2,0-2,1:     NL      '\012'
## 3,0-3,4:     NAME    'file'
## 3,5-3,6:     OP      '='
## 3,7-3,11:    NAME    'open'
## 3,11-3,12:   OP      '('
## 3,12-3,35:   STRING  '"tokenize-example-1.py"'
## 3,35-3,36:   OP      ')'
## 3,36-3,37:   NEWLINE '\012'
## ...

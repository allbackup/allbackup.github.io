# File: builtin-vars-example-1.py

book = "library2"
pages = 250
scripts = 350

print "the %(book)s book contains more than %(scripts)s scripts" % vars()

## the library book contains more than 350 scripts

# File: dospath-example-1.py

import dospath

file = "/my/little/pony"

print "isabs", "=>", dospath.isabs(file)
print "dirname", "=>", dospath.dirname(file)
print "basename", "=>", dospath.basename(file)
print "normpath", "=>", dospath.normpath(file)
print "split", "=>", dospath.split(file)
print "join", "=>", dospath.join(file, "zorba")

## $ python dospath-example-1.py
## isabs => 1
## dirname => /my/little
## basename => pony
## normpath => \my\little\pony
## split => ('/my/little', 'pony')
## join => /my/little/pony\zorba

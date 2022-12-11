# File: atexit-example-1.py

import atexit

def exit(*args):
    print "exit", args

# register three exit handlers
atexit.register(exit)
atexit.register(exit, 1)
atexit.register(exit, "hello", "world")

## $ python atexit-example-1.py
## exit ('hello', 'world')
## exit (1,)
## exit ()

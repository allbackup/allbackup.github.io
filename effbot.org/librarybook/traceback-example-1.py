# File: traceback-example-1.py

# note! in old Python versions, importing the traceback
# messes up the exception state.  to be on the safe side,
# let's import it here.
import traceback

try:
    raise SyntaxError, "example"
except:
    traceback.print_exc()


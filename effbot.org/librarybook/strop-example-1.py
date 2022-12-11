# File: strop-example-1.py

import strop # built-in module
import sys # built-in module

# assuming we have an executable named ".../executable", add a
# directory named ".../executable-extra" to the path

if strop.lower(sys.executable)[-4:] == ".exe":
    extra = sys.executable[:-4] # windows
else:
    extra = sys.executable

sys.path.insert(0, extra + "-extra")

import mymodule

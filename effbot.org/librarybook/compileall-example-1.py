# File: compileall-example-1.py

import compileall

print "This may take a while!"

compileall.compile_dir(".", force=1)


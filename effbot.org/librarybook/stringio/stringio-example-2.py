# File: stringio-example-2.py

import StringIO

file = StringIO.StringIO()
file.write("This man is no ordinary man. ")
file.write("This is Mr. F. G. Superman.")

print file.getvalue()

## $ python stringio-example-2.py
## This man is no ordinary man. This is Mr. F. G. Superman.

# File: cstringio-example-1.py

import cStringIO

MESSAGE = "That man is depriving a village somewhere of a computer scientist."

file = cStringIO.StringIO(MESSAGE)

print file.read()

## $ python cstringio-example-1.py
## That man is depriving a village somewhere of a computer scientist.

# File: sunaudio-example-1.py

import sunaudio

file = "samples/sample.au"

print sunaudio.gethdr(open(file, "rb"))


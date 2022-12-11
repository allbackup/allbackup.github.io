# File: os-example-8.py

import os

if os.name == "nt":
    command = "dir"
else:
    command = "ls -l"

os.system(command)


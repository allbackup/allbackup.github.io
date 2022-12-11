# File: pipes-example-1.py

import pipes

t = pipes.Template()

# create a pipeline
t.append("sort", "--")
t.append("uniq", "--")

# filter some text
t.copy("samples/sample.txt", "")


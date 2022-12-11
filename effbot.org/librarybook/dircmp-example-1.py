# File: dircmp-example-1.py

import dircmp

d = dircmp.dircmp()
d.new("samples", "oldsamples")
d.run()
d.report()


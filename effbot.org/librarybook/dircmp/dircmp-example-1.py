# File: dircmp-example-1.py

import dircmp

d = dircmp.dircmp()
d.new("samples", "oldsamples")
d.run()
d.report()

## $ python dircmp-example-1.py
## diff samples oldsamples
## Only in samples : ['sample.aiff', 'sample.au', 'sample.wav']
## Identical files : ['sample.gif', 'sample.gz', 'sample.jpg', ...]

# File: macurl2path-example-1.py

import macurl2path

file = ":my:little:pony"

print macurl2path.pathname2url(file)
print macurl2path.url2pathname(macurl2path.pathname2url(file))

## my/little/pony
## :my:little:pony

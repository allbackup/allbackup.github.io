# File: reconvert-example-1.py

import reconvert

for pattern in ("abcd", "a\(b*c\)d", "\<\w+\>"):
    print pattern, "=>", reconvert.convert(pattern)


# File: re-example-2.py

import re

text ="10/15/99"

m = re.match("(\d{2})/(\d{2})/(\d{2,4})", text)
if m:
    print m.group(1, 2, 3)

## ('10', '15', '99')

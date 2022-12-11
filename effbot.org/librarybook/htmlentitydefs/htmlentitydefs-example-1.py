# File: htmlentitydefs-example-1.py

import htmlentitydefs

entities = htmlentitydefs.entitydefs

for entity in "amp", "quot", "copy", "yen":
    print entity, "=", entities[entity]

## $ python htmlentitydefs-example-1.py
## amp = &
## quot = "
## copy = ©
## yen = ¥

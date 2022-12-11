# File: nis-example-1.py

import nis
import string

print nis.cat("ypservers")
print string.split(nis.match("bacon", "hosts.byname"))

## $ python nis-example-1.py
## {'bacon.spam.egg': 'bacon.spam.egg'}
## ['194.18.155.250', 'bacon.spam.egg', 'bacon', 'spam-010']

# File: rlcompleter-example-1.py

import rlcompleter
import sys

completer = rlcompleter.Completer()

for phrase in "co", "sys.p", "is":
    print phrase, "=>",
    # emulate readline completion handler
    try:
        for index in xrange(sys.maxint):
            term = completer.complete(phrase, index)
            if term is None:
                break
            print term,
    except:
        pass
    print

## co => continue compile complex coerce completer
## sys.p => sys.path sys.platform sys.prefix
## is => is isinstance issubclass

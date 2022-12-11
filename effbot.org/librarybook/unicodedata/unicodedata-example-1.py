# File: unicodedata-example-1.py

import unicodedata

for char in [u"A", u"-", u"1", u"\N{LATIN CAPITAL LETTER O WITH DIAERESIS}"]:
    print repr(char),
    print unicodedata.category(char),
    print repr(unicodedata.decomposition(char)),
    print unicodedata.decimal(char, None),
    print unicodedata.numeric(char, None)

## $ python unicodedata-example-1.py
## u'A' Lu '' None None
## u'-' Pd '' None None
## u'1' Nd '' 1 1.0
## u'Ö' Lu '004F 0308' None None

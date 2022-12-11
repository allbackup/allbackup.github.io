# File: crypt-example-1.py

import crypt

import random, string

def getsalt(chars = string.letters + string.digits):
    # generate a random 2-character 'salt'
    return random.choice(chars) + random.choice(chars)

print crypt.crypt("bananas", getsalt())

## $ python crypt-example-1.py
## 'py8UGrijma1j6'

# File: whrandom-example-1.py

import whrandom

# same as random
print whrandom.random()
print whrandom.choice([1, 2, 3, 5, 9])
print whrandom.uniform(10, 20)
print whrandom.randint(100, 1000)

## $ python whrandom-example-1.py
## 0.113412062346
## 1
## 16.8778954689
## 799

# File: dumbdbm-example-1.py

import dumbdbm

db = dumbdbm.open("dumbdbm", "c")
db["first"] = "fear"
db["second"] = "surprise"
db["third"] = "ruthless efficiency"
db["fourth"] = "an almost fanatical devotion to the Pope"
db["fifth"] = "nice red uniforms"
db.close()

db = dumbdbm.open("dumbdbm", "r")
for key in db.keys():
    print repr(key), repr(db[key])

## $ python dumbdbm-example-1.py
## 'first' 'fear'
## 'third' 'ruthless efficiency'
## 'fifth' 'nice red uniforms'
## 'second' 'surprise'
## 'fourth' 'an almost fanatical devotion to the Pope'

# File: aifc-example-1.py

import aifc

a = aifc.open("samples/sample.aiff", "r")

if a.getnchannels() == 1:
    print "mono,",
else:
    print "stereo,",

print a.getsampwidth()*8, "bits,",
print a.getframerate(), "Hz sampling rate"

data = a.readframes(a.getnframes())

print len(data), "bytes read"

## $ python aifc-example-1.py
## mono, 16 bits, 8012 Hz sampling rate
## 13522 bytes read

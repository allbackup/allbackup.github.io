# File: cpickle-example-1.py

try:
    import cPickle as pickle
except ImportError:
    import pickle # fall back on Python version

class Sample:
    def __init__(self, value):
        self.value = value

sample = Sample(1)

data = pickle.dumps(sample)

print pickle
print repr(data)


# File: profile-example-1.py

import profile

def func1():
    for i in range(1000):
        pass

def func2():
    for i in range(1000):
        func1()

profile.run("func2()")


# File: cstringio-example-2.py

try:
    import cStringIO
    StringIO = cStringIO
except ImportError:
    import StringIO

print StringIO

## $ python cstringio-example-2.py
## <module 'cStringIO' (built-in)>

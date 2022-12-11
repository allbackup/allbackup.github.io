# File: builtin-open-example-1.py

def open(filename, mode="rb"):
    import __builtin__
    file = __builtin__.open(filename, mode)
    if file.read(5) not in("GIF87", "GIF89"):
        raise IOError, "not a GIF file"
    file.seek(0)
    return file

fp = open("samples/sample.gif")
print len(fp.read()), "bytes"

fp = open("samples/sample.jpg")
print len(fp.read()), "bytes"


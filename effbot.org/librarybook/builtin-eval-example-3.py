# File: builtin-eval-example-3.py

print eval("__import__('os').getcwd()", {})
print eval("__import__('os').remove('file')", {"__builtins__": {}})


from __future__ import print_function # noslide
## <h1>what they do</h1>

def boldify(fn):  # noslide
    def wrapper(*args, **kw):  # noslide
        r = fn(*args, **kw)  # noslide
        return "<b>{}</b>".format(r)  # noslide
    return wrapper  # noslide

def foo(a, b):
    return a + b
#!
print(foo(1, 2))  # "3"
#!
foo = boldify(foo)
#!
print(foo(1, 2))  # "<b>3</b>"
## show-output

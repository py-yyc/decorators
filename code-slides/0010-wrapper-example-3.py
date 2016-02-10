from __future__ import print_function # noslide
## <h1>what they do</h1>

def boldify(fn):
    def wrapper(*args):
        r = fn(*args)
        return "<b>{}</b>".format(r)
    return wrapper
#!
@boldify
def foo(a, b):
    return a + b
#!
print(foo(1, 2))
## show-output

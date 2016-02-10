from __future__ import print_function # noslide
## <h1>what they do</h1>
## <ul><li>"wrapper"-style decorators</li></ul>

def boldify(fn):
#!
    def wrapper(*args):
#!
        r = fn(*args)
#!
        return "<b>{}</b>".format(r)
#!
    return wrapper

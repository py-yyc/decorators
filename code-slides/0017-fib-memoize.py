from __future__ import print_function # noslide
## <h1>how decorators work</h1>

def memoize(fn):
#!
    cache = dict()
#!
    def wrapper(*args):
#!
        try:
            return cache[args]
#!
        except KeyError:
            r = fn(*args)
#!
            cache[args] = r
            return r
#!
    return wrapper

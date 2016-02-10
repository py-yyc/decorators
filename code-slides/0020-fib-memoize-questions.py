from __future__ import print_function # noslide
## <h1>memoize: questions?</h1>

def memoize(fn):
    cache = {}
    def wrapper(*args):
        try:
            return cache[args]
        except KeyError:
            r = fn(*args)
            cache[args] = r
            return r
    return wrapper
@memoize
def fib(x):
    if x in [1, 2]:
        return 1
    return fib(x - 1) + fib(x - 2)

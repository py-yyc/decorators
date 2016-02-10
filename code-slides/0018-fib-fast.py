from __future__ import print_function # noslide
## <h1>how decorators work</h1>

from time import time  # noslide
from contextlib import contextmanager  # noslide
@contextmanager  # noslide
def timer():  # noslide
    s = time()  # noslide
    yield  # noslide
    print("took {:.6f}s".format(time() - s))  # noslide

def memoize(fn):  # noslide
    cache = dict()  # noslide
    def wrapper(*args):  # noslide
        try:  # noslide
            return cache[args]  # noslide
        except KeyError:  # noslide
            r = fn(*args)  # noslide
            cache[args] = r  # noslide
            return r  # noslide
    return wrapper  # noslide
@memoize
def fib(x):
#!
    if x in [1, 2]:
        return 1
    return fib(x - 1) + fib(x - 2)
#!
with timer():
    print("fib(35) =", fib(35))
## show-output
# remember: ~1.6 seconds previously

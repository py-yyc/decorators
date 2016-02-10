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
    cache = {}  # noslide
    def wrapper(*args):  # noslide
        try:  # noslide
            return cache[args]  # noslide
        except KeyError:  # noslide
            r = fn(*args)  # noslide
            cache[args] = r  # noslide
            return r  # noslide
    return wrapper  # noslide
@memoize  # noslide
def fib(x):  # noslide
    if x in [1, 2]:  # noslide
        return 1  # noslide
    return fib(x - 1) + fib(x - 2)  # noslide
with timer():
    print("fib(100) =", fib(100))
with timer():
    print("fib(200) =", fib(200))
## show-output

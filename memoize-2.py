from __future__ import print_function # noslide
## <h1>motivational examples</h1>
import time
from contextlib import contextmanager

@contextmanager
def timer():
    s = time.time()
    yield
    diff = time.time() - s
    print("took: {}s".format(diff))

def memoize(fn):
    cache = {}
    def wrapper(*args):
        try:
            return cache[(fn, args)]
        except KeyError:
            r = fn(*args)
            cache[(fn, args)] = r
            return r
    print("created wrapper, with cache {}".format(id(cache)))
    return wrapper

@memoize
def foo(x):
    return x + 5

@memoize
def fibonnacci(x):
    if x == 1 or x == 2:
        return 1
    return fibonnacci(x - 2) + fibonnacci(x - 1)
#!
with timer():
    print(fibonnacci(35))
print(foo(1))
print(foo(2))
## show-output

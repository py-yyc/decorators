from __future__ import print_function # noslide
## <h1>@contextmanager</h1>

class Helper(object):  # noslide
    def __init__(self, gen):  # noslide
        self._gen = gen  # noslide
    def __enter__(self):  # noslide
        return next(self._gen)  # noslide
    def __exit__(self, t, v, tb):  # noslide
        if t is None:  # noslide
            try:  # noslide
                next(self._gen)  # noslide
            except StopIteration:  # noslide
                return  # noslide
        else:  # noslide
            self._gen.throw(t, v, tb)  # noslide
def contextmanager(fn):
#!
    def wrapper(*args, **kw):
#!
        return Helper(fn(*args, **kw))
    return wrapper
#!
@contextmanager
def foo():
    print("hi")
    yield "a thing"
    print("bye")
#!
with foo() as x:
    print("inside:", x)
## show-output

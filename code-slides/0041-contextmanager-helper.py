from __future__ import print_function # noslide
## <h1>@contextmanager</h1>

class Helper(object):
    def __init__(self, gen):
        self._gen = gen
#!
    def __enter__(self):
        return next(self._gen)
#!
    def __exit__(self, type, value, traceback):
#!
        if type is None:
            try:
                next(self._gen)
#!
            except StopIteration:
                return
#!
        else:
            self._gen.throw(type, value, traceback)

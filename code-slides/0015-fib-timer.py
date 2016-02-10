from __future__ import print_function # noslide
## <h1>how decorators work</h1>

from time import time
from contextlib import contextmanager

@contextmanager
def timer():
#!
    s = time()
#!
    yield
#!
    print("took {:.6f}s".format(time() - s))
#!
with timer():
    pass
## show-output

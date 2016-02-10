from __future__ import print_function # noslide
## <h1>@contextmanager</h1>
from contextlib import contextmanager # noslide

@contextmanager
def a_thing():
#!
    print("enter")
#!
    yield "a thing"
#!
    print("exit")
#!
with a_thing() as foo:
   print("inside: {}".format(foo))
#!
## show-output

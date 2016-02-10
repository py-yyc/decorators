# bwhahahah1!! yes

from contextlib import contextmanager

@contextmanager
def test_fixture():
    print "set-up"
    yield
    print "tear-down"

with test_fixture():
    print "inner loop"

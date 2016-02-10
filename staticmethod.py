from __future__ import print_function
from functools import partial


class StaticMethod(object):
    "Emulate PyStaticMethod_Type() in Objects/funcobject.c"

    def __init__(self, f):
        self.f = f
    def __get__(self, obj, objtype=None):
        return self.f

class ClassMethod(object):
    def __init__(self, f):
        self.f = f
    def __get__(self, obj, objtype=None):
        return partial(self.f, objtype)

class Thing(object):
    def __get__(self, obj, objtype):
        print("THING!!!", obj, objtype)
        return "ohai"

def smethod(fn):
    return StaticMethod(fn)

class Foo(object):
    def blammo(cls=None):
        print("blammo", cls)
    foo = StaticMethod(blammo)

    bar = ClassMethod(blammo)

#    bar = Thing()

#Foo().blammo()
#Foo.foo()

print("Foo.foo() =", Foo.foo())
print("Foo.bar() =", Foo.bar())
#Foo.bar = 'sexy time'



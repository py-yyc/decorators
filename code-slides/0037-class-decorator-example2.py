from __future__ import print_function # noslide
## <h1>class decorators</h1>

def implements(iface): # noslide
    def decorate(cls): # noslide
        try: # noslide
            cls._interfaces.append(iface) # noslide
        except AttributeError: # noslide
            cls._interfaces = [iface] # noslide
        return cls # noslide
    return decorate # noslide

@implements("fake interface")
@implements("another interface")
class Foo(object):
    pass
#!
f = Foo()
print("f has interfaces: {}".format(f._interfaces))
## show-output

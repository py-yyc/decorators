from __future__ import print_function # noslide
## <h1>class decorators</h1>

def implements(iface):
#!
    def decorate(cls):
#!
        try:
            cls._interfaces.append(iface)
        except AttributeError:
            cls._interfaces = [iface]
#!
        return cls
#!
    return decorate

def tag(the_tag):
    def _mark(cls):
        cls._special = the_tag
        return cls
    return _mark

@tag('foo')
class FunTimes(object):
    pass

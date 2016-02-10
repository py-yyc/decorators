from __future__ import print_function # noslide
## <h1>decorators with args: Flask</h1>

class Flask(object):
    def __init__(self):
        self.url_map = dict()
#!
    def route(self, url):
#!
        def decorator(fn):
#!
            self.url_map[url] = fn
            return fn
#!
        return decorator
#!
app = Flask()  # yuck! globals!
#!
@app.route("/foo")
def foo(request):
    return "Gorgeous HTMLs"
#!
print(app.url_map['/foo']("fake request object"))
## show-output



class App(object):
    "singletons are the satan"
    def __init__(self):
        self.url_map = {}

    def route(self, url):
        def wrapture(fn):
            self.url_map[url] = fn
            return fn
        return wrapture

    def render(self, url):
        return self.url_map[url]("the request object")

app = App()

@app.route("/foo")
def root(req):
    print("root", req)

# do some request processing
app.render('/foo')

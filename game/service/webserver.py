from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.static import File
import game.scriptsystem

class Default(Resource):
    def render_GET(self, request):
        return 'No page'

default = Default()

class Page(Resource):
    @gen.coroutine
    def getChild(self, path, request):
        req = yield game.scriptsystem.get("webPage").run(path, request=request)
        if req:
            returnValue(req)

class Web(Resource):
    def __init__(self):
        Resource.__init__(self)
        self.putChild("static", File("data/web_static"))

    @gen.coroutine
    def getChild(self, path, request):
        req = yield game.scriptsystem.get("webPage").run(path, request=request)
        if req:
            returnValue(req)
        else:
            returnValue(default)

class WebFactory(Site):
    pass
from request import Request
from response import Response
import socketserver
from controllers.pages import PagesController
from router import Router
from task2.static_responder import StaticResponder

router = Router()
router.get('/', PagesController, 'home')
router.get('/click', PagesController, 'click')


class Handler(socketserver.StreamRequestHandler):

    def handle(self):
        request = Request(self.rfile)
        response = Response(self.wfile)
        response.add_header('Connection', 'close')
        static_responder = StaticResponder(request, response)

        router.run(request, response)

        response.send()
        

ADDRESS = ('localhost', 1027)
socketserver.ThreadingTCPServer.allow_reuse_address = True

with socketserver.ThreadingTCPServer(ADDRESS, Handler) as server:
    server.serve_forever()

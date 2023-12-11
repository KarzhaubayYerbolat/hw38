from request import Request
from response import Response
import errors
from static_responder import StaticResponder

import socketserver

from controllers.pages import PagesController
from controllers.posts import PostsController
from errors import not_found


from errors import not_found
from router import Router


router = Router()
router.get('/', PagesController, 'home')
router.get('/one', PagesController, 'one')
router.get('/two', PagesController, 'two')
router.get('/three', PagesController, 'three')

print(router.routes)


class Handler(socketserver.StreamRequestHandler):

    def handle(self):
        request = Request(self.rfile)
        response = Response(self.wfile)
        response.add_header('Connection', 'close')
        # static_responder = StaticResponder(request, response)

        router.run(request, response)

        response.send()
        

ADDRESS = ('localhost', 1027)
socketserver.ThreadingTCPServer.allow_reuse_address = True

with socketserver.ThreadingTCPServer(ADDRESS, Handler) as server:
    server.serve_forever()

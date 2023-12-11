from .base import BaseController


class PagesController(BaseController):
    def home(self):
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(
                               '<a href="one">First page</a>'
                               '<br>'
                               '<a href="two">Second page</a>'
                               '<br>'
                               '<a href="three">Third page</a>'
        )

    def one(self):
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body('<a href="/one">First page</a>')

    def two(self):
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body('<a href="/two">First page</a>')

    def three(self):
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body('<a href="/three">First page</a>')

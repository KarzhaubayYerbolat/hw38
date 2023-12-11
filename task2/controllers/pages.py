from .base import BaseController


class PagesController(BaseController):
    CLICK_COUNT = 0

    def home(self):
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(
            f'<h2>{self.CLICK_COUNT}</h2>'
            '<a href="/click">Click</a>'
        )

    def click(self):
        self.response.add_header('Content-Type', 'text/html')
        PagesController.CLICK_COUNT += 1
        self.response.set_body(
            f'<h2>{self.CLICK_COUNT}</h2>'
            '<a href="/click">Click</a>'
        )

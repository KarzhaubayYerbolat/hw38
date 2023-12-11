from .base import BaseController


class PostsController(BaseController):
    def get_list(self):
        posts_bd = [
            {'id': 1, 'title': 'This is 1st post'},
            {'id': 2, 'title': 'This is 2st post'},
            {'id': 3, 'title': 'This is 3st post'},
        ]

        body = '<h1>This is our posts</h1>'
        for post in posts_bd:
            body += f'<h3>{post["id"]} - {post["title"]}'

        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)


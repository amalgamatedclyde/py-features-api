import tornado.ioloop
import tornado.web
from api import ClassesHandler


class MainHandler(tornado.web.RequestHandler):
    pass


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/classes", ClassesHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

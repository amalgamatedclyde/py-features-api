import tornado.ioloop
import tornado.web
from tornado import httpserver
from api import ClassesHandler
import os
# import bugsnag
#
# bugsnag.configure(
#   api_key = "4645fab58b53cfe39793d3daf9c7e509",
#   project_root = os.getcwd()
# )

class MainHandler(tornado.web.RequestHandler):
    """mainhandler"""
    def get(self):
        self.write('Welcome!')


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/classes", ClassesHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888, xheaders=True)
    tornado.ioloop.IOLoop.current().start()
    # app = make_app()
    # server = httpserver.HTTPServer(app, xheaders=True)
    # server.bind(8888)
    # server.start(1)  # forks one process per cpu
    # tornado.ioloop.IOLoop.current().start()

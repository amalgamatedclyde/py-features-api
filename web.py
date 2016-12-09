import tornado.ioloop
import tornado.web
from tornado import httpserver
from api import ClassesHandler
from tornado.options import define, options

define("port", default=8888)
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
    options.parse_command_line()
    app = make_app()
    port = options.port
    server = httpserver.HTTPServer(app, xheaders=True)
    server.listen(port)
    print 'Listening on port {}'.format(port)
    tornado.ioloop.IOLoop.current().start()
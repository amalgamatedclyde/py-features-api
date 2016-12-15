import tornado.ioloop
import tornado.web
from tornado import httpserver
from api import ClassesHandler, UnhandledExceptionHandler, HandledException
from tornado.options import define, options

define("port", default=8888)
import os
import bugsnag
from bugsnag.tornado import BugsnagRequestHandler
bugsnag.configure(
    api_key="16a92cf41c182a50aee6ca80fae9d65d",
    project_root="/home/markable/py-features-api",
)


# class MainHandler(tornado.web.RequestHandler):
#     """mainhandler"""
#     def get(self):
#         self.write('Welcome!')


class MainHandler(BugsnagRequestHandler):
    """mainhandler"""

    def get(self):
        self.write('Welcome!')


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/classes", ClassesHandler),
        (r"/bad_error", UnhandledExceptionHandler),
        (r"/handled", HandledException)
    ])

if __name__ == "__main__":
    options.parse_command_line()
    app = make_app()
    port = options.port
    server = httpserver.HTTPServer(app, xheaders=True)
    server.listen(port)
    print 'Listening on port {}'.format(port)
    tornado.ioloop.IOLoop.current().start()
    bugsnag.notify()
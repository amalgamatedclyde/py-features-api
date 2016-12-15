import json
import tornado.web
import nets
from bugsnag.tornado import BugsnagRequestHandler


class FriendlyError(Exception):
    """my hovercraft is full of eels"""



class ClassesHandler(BugsnagRequestHandler):

    def prepare(self):
        try:
            if self.request.headers["Content-Type"].startswith("application/json"):
                self.json_args = json.loads(self.request.body)
            else:
                self.json_args = None
        except:
            self.json_args = None

    def post(self):
        # Get a convenient handle on the given base64 string
        req_data = self.json_args.get('data')
        try:
            # pass the base64 enc string to classifier

            classes = nets.classify(image_file=req_data['image_file'])
        except KeyError:

            try:
                classes = nets.classify(url=req_data['image_uri'])
            except KeyError:
                pass
        # Send the extracted features back in the response
        try:
            self.write(dict(data=classes))
        except TypeError as e:
            self.write(str(e))



class UnhandledExceptionHandler(BugsnagRequestHandler):

    def get(self):
        r = 1/0
        self.write(r)


class HandledException(BugsnagRequestHandler):

    def get(self):
        try:
            1+'1'
        except TypeError:
            self.write('this is a handled exception ')









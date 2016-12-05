import json
import tornado.web
import nets
from tornado import gen

class ClassesHandler(tornado.web.RequestHandler):

    def prepare(self):
        if self.request.headers["Content-Type"].startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None

    def post(self):
        # Get a convenient handle on the given base64 string
        req_data = self.json_args['data']
        try:
            # pass the base64 enc string to classifier
            classes = nets.classify(image_file=req_data['image_file'])
        except KeyError:

            try:
                classes = nets.classify(url=req_data['image_uri'])
            except KeyError:
                pass
        # Send the extracted features back in the response
        self.write(dict(data=classes))


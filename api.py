import json
import tornado.web
import nets


class ClassesHandler(tornado.web.RequestHandler):
    def prepare(self):
        if self.request.headers["Content-Type"].startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None


    def post(self):

        # Get a convenient handle on the given URI
        req_data = self.json_args['data']

        # Assume the given URI is an HTTPS URL
        classes = nets.classify(url=req_data['image_uri'])

        # Send the extracted features back in the response
        self.write(dict(data=classes))

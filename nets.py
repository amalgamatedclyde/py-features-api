import caffe
import urllib
import StringIO
import  base64

# Taken from the official Caffe repo
from app import ImagenetClassifier, ClassificationError

_classifier = ImagenetClassifier()
_classifier.net.forward()


def classify(image_file=None, url=None):
    if url:
        string_buffer = StringIO.StringIO(urllib.urlopen(url).read())
        image = caffe.io.load_image(string_buffer)
    elif image_file:
        decoded = base64.standard_b64decode(image_file)
        image = caffe.io.load_image(StringIO.StringIO(decoded))

    return _classifier.classify_image(image)

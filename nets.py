import caffe
import urllib
import StringIO
import  base64

# Taken from the official Caffe repo
from app import ImagenetClassifier, ClassificationError

# Configure Caffe and load the model
# caffe.set_device(0) forces GPU mode
caffe.set_mode_cpu()

# Initialize classifier + warm start by forward for allocation
# _classifier_args = {
#     'model_def_file': (
#         'models/deploy.prototxt'),
#     'pretrained_model_file': (
#         'models/bvlc_reference_caffenet.caffemodel'),
#     'mean_file': (
#         'data/ilsvrc_2012_mean.npy'),
#     'class_labels_file': (
#         'data/ilsvrc12/synset_words.txt'),
#     'bet_file': (
#         'data/ilsvrc12/imagenet.bet.pickle'),
#     'image_dim': 256,
#     'raw_scale': 255.0,
#     'gpu_mode': False,
# }
_classifier = ImagenetClassifier()
_classifier_args = _classifier.default_args
_classifier.net.forward()


def classify(image_file=None, url=None):
    """
    Given something to classify, load the image and then pass it through the
    network to see what classes we get.

    :param str url: 
        The URL to a resource for which features should be extracted
        base64 image_file
    :returns list: The list of classification results

    """
    # print('image: {}'.format(image_file))

    # Load the image data from a string buffer

    if url:
        string_buffer = StringIO.StringIO(urllib.urlopen(url).read())
        image = caffe.io.load_image(string_buffer)
    elif image_file:
        decoded = base64.standard_b64decode(image_file)
        image = caffe.io.load_image(StringIO.StringIO(decoded))

    return _classifier.classify_image(image)

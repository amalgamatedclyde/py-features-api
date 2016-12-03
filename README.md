# py-features-api
Sample Python API created for use in staging an infrastructure 
improvement project

## Caffe setup

This project requires [Caffe RC3][1], and specifically the model files used
in the [official Caffe web demo][2].

First, build Caffe. Use CPU mode if the runtime environment does not have a
CUDA-compatible GPU from NVIDIA.

Then, run the scripts in the Caffe project directory to download the
necessary files for this API project.

```bash
# Run these commands in the Caffe RC3 project directory
./scripts/download_model_binary.py models/bvlc_reference_caffenet
./data/ilsvrc12/get_ilsvrc_aux.sh
```

Once the downloads are complete, move the files into position as follows.

```bash
# Assume CAFFE_DIR is the path to the Caffe project directory,
# and PROJECT_DIR is the path to this project directory.
mv $CAFFE_DIR/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel \
    $PROJECT_DIR/models
mv $CAFFE_DIR/data/ilsvrc12 $PROJECT_DIR/data
mv $CAFFE_DIR/python/caffe/imagenet/ilsvrc_2012_mean.npy $PROJECT_DIR/data
```

[1]: https://github.com/BVLC/caffe/releases/tag/rc3
[2]: http://caffe.berkeleyvision.org/gathered/examples/web_demo.html

## Start the web server

```bash
python web.py
```

## Test out the API

```bash
./scripts/post-classes.sh
```

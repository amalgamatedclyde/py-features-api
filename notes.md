##Notes

- i built Caffe on my local machine and an EC2 m4.large instance
- Caffe build had more issues on ubuntu 16.04. I had to remove opencv from the environment.
- also i had to symlink libhd5:
```bash
sudo ln -s libhdf5_serial_hl.so.10.0.2 libhdf5_hl.so
```
- Also, I needed to install libgcc and protobuf, which i don't think is documented.
- the path variable is incorrect for:

```bash
mv $CAFFE_DIR/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel \
    $PROJECT_DIR\models\.
mv $CAFFE_DIR/data/ilsvrc12 $PROJECT_DIR/data/.
mv $CAFFE_DIR/python/caffe/imagenet/ilsvrc_2012_mean.npy $PROJECT_DIR/data/.
```

when the app runs, it looks in

```bash
/home/user/
```

-the code was sprinkled with gpu calls across a few files, which i changed to cpu.

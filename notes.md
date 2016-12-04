##Notes

- i built Caffe on my local machine and an EC2 m4.large instance
- Caffe build had more issues on ubuntu 16.04. I had to remove opencv from the environment.
- i had to symlink libhd5:
```bash
sudo ln -s libhdf5_serial_hl.so.10.0.2 libhdf5_hl.so
```
- Also, I needed to install libgcc and protobuf, which i don't think is documented.
- the code was sprinkled with gpu calls across a few files, which i changed to cpu.
- i cut out all of the unused code to make it obvious what is going on
- i changed and subclassed some exceptions

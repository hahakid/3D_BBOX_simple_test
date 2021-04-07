# 3D_BBOX_simple_test
for Dr. jie

## envs (tested on ubuntu18 with anaconda)

conda install cudatoolkit=9.0

conda install cudnn=7.0

conda install tensorflow-gpu==1.11.0

pip install -r requirements.txt

a result from tracking seq00(https://github.com/hahakid/3D_BBOX_simple_test/blob/main/util/saveVideo.mp4)

## train:
  modified the path in train.py (use KITTI orginal labels)

  image_dir = '/home/kid/workspace/3D_detection/dataset/image_2/'
  
  label_dir = '/home/kid/workspace/3D_detection/dataset/label_2/'
 
change batch_size = 40 (line 38), epochs = 100 (line 49) and other params for local dataset.


## test:
  modified the path in detection.py (use KITTI orginal labels)
  
  image_dir = '/home/kid/workspace/3D_detection/dataset/test/image/'
  
  calib_file = '/home/kid/workspace/3D_detection/dataset/test/calib.txt'
  
  box2d_dir = '/home/kid/workspace/3D_detection/dataset/test/label/'


> use util/tracking2object.py to generate labels from tracking dataset.

> merge sequence images (./output) to mp4 with util/im2video.py

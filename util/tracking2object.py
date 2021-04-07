import os


tracking_label='/home/kid/workspace/qd-3dt/data/KITTI/tracking/training/label_02/0000.txt'
object_label='/home/kid/workspace/3D_detection/dataset/test/label/'

f=open(tracking_label,'r')
lines=f.readlines()
f.close()

for l in lines:
    if not 'DontCare' in l:
        l=l.split(" ", 2)
        frame = l[0].zfill(6)+'.txt'
        info=l[-1]
        print(frame,info)
        path=os.path.join(object_label,frame)
        with open(path, "a") as file:  # ”w"代表着每次运行都覆盖内容
            file.write(info)

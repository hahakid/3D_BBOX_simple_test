import os
import numpy as np
import cv2

imgl=os.listdir("../output")
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
videoWriter = cv2.VideoWriter('saveVideo.mp4', fourcc, 10, (1242,375))
imgl.sort()
for l in imgl:
    print(l)
    im=cv2.imread(os.path.join("../output",l))
    videoWriter.write(im)
videoWriter.release()


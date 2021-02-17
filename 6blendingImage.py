
#lab 6 blending of an image

import cv2
import numpy as np

img1 = cv2.imread('m1.png')
img2 = cv2.imread('opencv_logo.jpg')
print(img1.shape)
print(img2.shape)
img1 = cv2.resize(img1, (256,256))
img2 = cv2.resize(img2, (256,256))

#dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
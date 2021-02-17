
#opening an image, printing its shape, and converting into grayscale
import numpy as  np
import  cv2

#Load an color image in grayscale

img = cv2.imread('cartoon.png')
cv2.imshow('image',img)
img1 = cv2.imread('cartoon.png',0)
cv2.imshow('grayscale',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)
print(img1.shape)
print(img[:,:,0])
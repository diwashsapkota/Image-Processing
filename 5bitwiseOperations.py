
#lab 5 bitwise operations

import cv2

import numpy as np

image1 = cv2.imread('imag1.jpg')
image2 = cv2.imread('imag2.jpg')

img1 = cv2.resize(image1, (256,256))
img2 = cv2.resize(image2, (256,256))

dest_and = cv2.bitwise_and(img2, img1, mask = None)
dest_or = cv2.bitwise_or(img2, img1, mask = None)
dest_xor = cv2.bitwise_xor(img2, img1, mask = None)
dest_not = cv2.bitwise_not(img1, mask = None)

cv2.imshow('Bitwise and', dest_and)
cv2.imshow('Bitwise or', dest_or)
cv2.imshow('Bitwise xor', dest_xor)
cv2.imshow('Bitwise not', dest_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
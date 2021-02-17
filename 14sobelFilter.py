#Lab 14 sobel filter


import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("Bikesgray.jpg", cv2.COLOR_BGR2GRAY)
cv2.imshow("Input", image)

image1 = cv2.Sobel(image, cv2.CV_64F,1 , 0 , ksize=1)
image2 = cv2.Sobel(image, cv2.CV_64F,0 ,1 , ksize=1)

cv2.imshow("Output: Sobel X axis", image1)
cv2.imshow("Output: Sobel Yaxis", image2)

cv2.waitKey(0)
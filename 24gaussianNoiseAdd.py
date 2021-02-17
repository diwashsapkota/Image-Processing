
#lab 24 gaussian noise addition
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('camera.png',0)
row, col = img.shape
print(img.shape)
gauss = np.random.normal(10,10,(row,col))
noisy = img + gauss

plt.subplot(221),plt.imshow(img,cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(noisy,cmap='gray')
plt.title('Gaussian Noise Image'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.hist(noisy.ravel(),256,[0,256])#;plt.show()
plt.title('Noisy Image Histogram'), plt.xticks([])
plt.show()
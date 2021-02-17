#lab 15 Erosion and Dilation

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('ok.jpg',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img, kernel, iterations = 1)
dilation =cv2.dilate(img, kernel, iterations =1)
plt.subplot(131),plt.imshow(img, 'gray'),plt.title('ORIGINAL')
plt.subplot(132),plt.imshow(erosion, 'gray'),plt.title('EROSION')
plt.subplot(133),plt.imshow(dilation, 'gray'),plt.title('DILATION')
plt.show()
#lab25

#canny edge detection

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('camera.png',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('original image'),plt.xticks([]),plt.yticks([])

plt.subplot(122),plt.imshow(edges,cmap='gray')
plt.title('edges image'),plt.xticks([]),plt.yticks([])


plt.show()
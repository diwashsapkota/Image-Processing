
#lab23 denoise a noisy image
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('beenoise.jpg')

dst = cv2.fastNlMeansDenoisingColored(img,None,15,15,7,21)

plt.subplot(121),plt.imshow(img)
plt.subplot(122),plt.imshow(dst)
plt.show()

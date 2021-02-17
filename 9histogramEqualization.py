
#lab 9 histogram equalization
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('wiki.jpg',0)
img_1 = cv2.resize(img, (256,256))
equ = cv2.equalizeHist(img_1)
res = np.hstack((img_1,equ)) #stacking images side-by-side
cv2.imshow('res.png',res)

histr1 = cv2.calcHist([img_1],[0],None,[256],[0,256])
histr2 = cv2.calcHist([equ],[0],None,[256],[0,256])

titles = ['original',' equalization']
images = [histr1,histr2]

for i in range(2):
    plt.subplot(1,2,i+1),plt.plot(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

#lab 8 border for images

#importing required libraries of opencv

import cv2
#importing library for plotting

from matplotlib import pyplot as plt

#reads an input image

img1 = cv2.imread('cartoon.png',0)
img2 = cv2.imread('camera.png',0)
img3 = cv2.imread('bnw.jpg',0)
img4 = cv2.imread('img.png',0)
#find frequency of pixels in range 0-255

histr1 = cv2.calcHist([img1],[0],None,[256],[0,256])
histr2 = cv2.calcHist([img2],[0],None,[256],[0,256])
histr3 = cv2.calcHist([img3],[0],None,[256],[0,256])
histr4 = cv2.calcHist([img4],[0],None,[256],[0,256])

#show the plotting graph of images
titles = ['Cartoon','Camera','bnw','img']
images = [histr1, histr2, histr3,histr4]
for i in range(4):
    plt.subplot(4,1,i+1),plt.plot(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
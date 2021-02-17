
#lab 28 Canny Edge with contouring

import cv2
import numpy as np

image = cv2.imread('m1.png')
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray,90,210)
cv2.waitKey(0)

#Finding Contours
#Use of a copy of a image e.g. edged.copy()
#since findcontours alters the image
contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('Cannny edges after Contouring', edged)
cv2.waitKey(0)

print("Number of Contours found=" + str(len(contours)))

#Draw all contours
#-1 signifies drawing all countours
cv2.drawContours(image, counters, -1, (0,255,0),3)

cv2.imshow('Contours',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
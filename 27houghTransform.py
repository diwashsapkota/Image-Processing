
#lab 27 Hough Transform
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku.jpg')
# Convert the image to gray scale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Apply edge detection method on tthe image
edges = cv2.Canny(gray, 50, 150, apertureSize = 3)
# This returns an array of r and theta values
lines = cv2.HoughLines(edges, 1, np.pi/180, 100)
# For loop runs till r and theta values
# Are in the range pf 2D array
for line in lines:
    r,theta = line[0]
    # Stores the value of cos(theta) in a
    a = np.cos(theta)

    # Stores the value od sin(theta) in b
    b = np.sin(theta)

    # x0 stores the values rcos(theta)
    x0 = a*r

    # y0 stores the value rsin(theta)
    y0 = b*r

    # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
    x1 = int(x0 + 1000*(-b))

    # y1 stores rounded off value of (rsin(theta)+1000cos(theta))
    y1 = int(y0 + 1000*(a))

    # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
    x2 = int(x0 - 1000 * (-b))

    # y2 stores rounded off value of (rsin(theta)-1000cos(theta))
    y2 = int(y0 - 1000 * (a))

    # cv2.line draws a line in img from the point(x1,y1) to(x2,y2)
    # (0,0,255) denotes the color of the line to be
    # In this case it is red

    img2 = cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

# All the changes made in the input image are finally written on a new image houghlines.png

cv2.imshow('Hough Transform', img)
cv2.imshow('Canny Edge Deetection', edges)
cv2.waitKey(10000000)
cv2.destroyAllWindows()




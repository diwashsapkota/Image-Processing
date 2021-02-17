
#lab 17 fourier spectrum of an image

import numpy as np
import cv2

from matplotlib import pyplot as plt

img = cv2.imread('bnw.jpg',0)


img_float32 = np.float32(img)
#computed the 2-d discrete fourier transform

dft = cv2.dft(img_float32,flags = cv2.DFT_COMPLEX_OUTPUT)

#shift the zero-frequency component to the center of the spectrum
dft_shift = np.fft.fftshift(dft)

#save image in the fourier domain
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'),plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'),plt.xticks([]),plt.yticks([])
plt.show()
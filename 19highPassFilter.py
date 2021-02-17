#lab19 high pass filter in frequency domain

import numpy as np

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('bnw.jpg',0)
dft = cv2.dft(np.float32(img), flags = cv2.DFT_COMPLEX_OUTPUT)
#fourier transform
f = np.fft.fft2(img)
#move the DC component of fft output to the center of the spectrum
fshift = np.fft.fftshift(f)

magnitude_spectrum = 20*np.log(np.abs(fshift))

rows, cols = img.shape
crow,ccol = int(rows/2),int(cols/2)

#use mask to remove low frequency components
fshift[int(crow-30):int(crow+30),int(ccol-30):int(ccol+30)] = 0
#logarithm transformation
magnitude_spectrum1 = 20*np.log(np.abs(fshift))
f_ishift = np.fft.ifftshift(fshift)

#inverse fourier transform
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'),plt.axis('off')
plt.subplot(222),plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'),plt.axis('off')
plt.subplot(223),plt.imshow(magnitude_spectrum1, cmap='gray')
plt.title('After High Pass Filtering'),plt.axis('off')
plt.subplot(224),plt.imshow(img_back, cmap='gray')
plt.title('Image after HPF'),plt.axis('off')
plt.show()

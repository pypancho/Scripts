# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 22:51:52 2018

@author: Yan
"""

#import numpy as np
import matplotlib.pyplot as plt
import cv2
import numpy as np

#flags = cv2.IMREAD_GRAYSCALE
flags = cv2.IMREAD_COLOR
im = cv2.imread('elephant.jpg', flags)

plt.figure()
plt.title('The image:')
plt.imshow(im)
plt.show()

#im_tiny = c3.show_tiny_bgr_channel(im)

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
filter = cv2.Canny(gray, 100, 200)
plt.figure()
plt.title('The image with canny edge detection:')
plt.imshow(filter)
plt.show()

_,thresh_img = cv2.threshold(im,127,255,cv2.THRESH_BINARY)
plt.figure()
plt.title('The image with binary:')
plt.imshow(thresh_img)
plt.show()

plt.figure()
plt.title('The image with gray:')
plt.imshow(gray)
plt.show()

cv2.imwrite('gray.jpg', gray)
cv2.imwrite('binary.jpg', thresh_img)
cv2.imwrite('canny.jpg', filter)
# https://docs.opencv.org/master/d3/df2/tutorial_py_basic_ops.html
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('lab.jpg')

border = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=[0, 150, 150])
replicate = cv.copyMakeBorder(img, 100, 100, 100, 100, cv.BORDER_REFLECT101)

plt.subplot(121)
plt.imshow(border, 'gray')
plt.title("Constant border")
plt.subplot(122)
plt.imshow(replicate, 'gray')
plt.title("Replicate 101")

plt.show()
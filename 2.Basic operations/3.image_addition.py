# https://docs.opencv.org/master/d0/d86/tutorial_py_image_arithmetics.html

import cv2 as cv

a1 = cv.imread('a1.jpg')
a2 = cv.imread('a2.jpg')

a1 = cv.resize(a1, (200, 500), interpolation=cv.INTER_AREA)
a2 = cv.resize(a2, (200, 500), interpolation=cv.INTER_AREA)

# Blending images
a3 = cv.addWeighted(a1, 0.7, a2, 0.3, 0)
cv.imshow("Added", a3)
cv.waitKey(0)

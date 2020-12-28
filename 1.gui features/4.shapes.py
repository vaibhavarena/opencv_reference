# Refer article for all shapes
# https://docs.opencv.org/master/dc/da5/tutorial_py_drawing_functions.html

import cv2 as cv
import numpy as np

img = np.zeros((512,512,3), np.uint8)

cv.line(img,(0,0),(511,511),(0,150,0),5)
cv.line(img,(0,511),(511,0),(0,150,0),5)
cv.rectangle(img, (100, 100), (400, 400), (100, 100, 100), 5)

cv.imshow("Press any key to Quit", img)
key = cv.waitKey(0)

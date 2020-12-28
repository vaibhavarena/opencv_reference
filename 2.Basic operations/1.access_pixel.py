import numpy as np
import cv2 as cv
import sys

img = cv.imread('lab.jpg')

px = img[100, 100]
print(px)

# Accessing only the blue value - 2
print(img.item(10, 10, 2))

# Accessing only the red value - 0
print(img.item(10, 10, 0))

print(img.shape)
print(img.size)
print(img.dtype)
import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("../lab.jpg"), 0)  # IMREAD_COLOR IMREAD_UNCHANGED IMREAD_GRAYSCALE 

if img is None:
    sys.exit("Could not read the file")

cv.imshow("Starry night", img)
k = cv.waitKey(0)   # To wait for user input in ms, 0 means to wait forever, k will record pressed key

if k == ord('s'):
    cv.imwrite("starry_night.png", img)
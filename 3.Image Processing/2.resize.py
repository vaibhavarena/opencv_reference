import cv2 as cv

img = cv.imread('lab.jpg')

res = cv.resize(img, None, fx = 0.5, fy = 0.5, interpolation=cv.INTER_CUBIC)    # dsize set to None to give default calculations
cv.imshow("Press any key to exit", res)

cv.waitKey(0)
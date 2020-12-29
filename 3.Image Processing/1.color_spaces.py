# https://docs.opencv.org/4.5.1/df/d9d/tutorial_py_colorspaces.html

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

yellow = np.uint8([[[0, 255, 255]]])
hsv_yellow = cv.cvtColor(yellow, cv.COLOR_BGR2HSV)
print(hsv_yellow)
Y1 = hsv_yellow[0][0][1]
Y2 = hsv_yellow[0][0][2]
lower_yellow = np.array([0, 100, 100])
upper_yellow = np.array([30, 255, 255])

while(True):
    _, frame = cap.read()

    if not _:
        print("Camera not found")
        break

    img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.inRange(img, lower_yellow, upper_yellow)

    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("WebCam", res)

    key = cv.waitKey(5) & 0xff

    if key == 27 or key == ord('q'):
        break

cv.destroyAllWindows()
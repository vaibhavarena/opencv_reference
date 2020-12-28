import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Camera could not be opened, Exiting...")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Exiting...")
        break

    coloring = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow("frame", coloring)
    q = cv.waitKey(1)

    if q == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

import cv2
import numpy as np

path = 'assets/lamborghini.jpg'
img = cv2.imread(path)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Original", img)
cv2.imshow("HSV Image", imgHSV)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
import cv2
import numpy as np

print("Package imported")

img = cv2.imread("assets/lenna.png")
kernel = np.ones((5,5), np.uint8)

cv2.imshow("Output", img)

imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow("Gray Image", imgGray)

imgBlur = cv2.GaussianBlur(imgGray, [7,7], 0)
cv2.imshow("Blur Image", imgBlur)

imgCanny = cv2.Canny(img, 150, 200)
cv2.imshow("Canny Image", imgCanny)

imgDialation = cv2.dilate(imgCanny,kernel, iterations=1)
cv2.imshow("Image Dialation", imgDialation)

imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
cv2.imshow("Image Eroded", imgEroded)

cv2.waitKey(0)
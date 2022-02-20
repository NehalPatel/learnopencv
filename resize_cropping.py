import cv2
import numpy as np

img = cv2.imread("assets/lenna.png")
# print(img.shape)
cv2.imshow("Image", img)

imgResize = cv2.resize(img, (2000,500))
# cv2.imshow("Resize Image", imgResize)

imgCropped = img[100:200, 200:500]
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
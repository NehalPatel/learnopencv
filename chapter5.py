import cv2
import numpy as np

img = cv2.imread("assets/cards.jpg")

width, height = 250,350
pts1 = np.float32([[423, 42], [760, 134], [300, 507], [634, 600]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
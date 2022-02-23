import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img)
# img[:] = 255, 0, 0
# img[100:300, 50:100] = 255, 0, 0
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (200, 200), (0, 0, 255), cv2.FILLED)
cv2.circle(img, (200, 400), 20, (255, 255, 0), 5)
cv2.putText(img, "Open CV", (100, 300), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 150, 0), 2)
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
import cv2
import numpy as np

good_contour = []

img1 = cv2.imread('countour-letter/A.png')
gray_image = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
print(img1.shape)
ret, thresh = cv2.threshold(gray_image, 127, 255,0)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# Filtering countour
for contour in contours:
    if cv2.contourArea(contour) > 10000:
        good_contour.append(contour)
cv2.drawContours(img1, good_contour, -1, (0, 255, 0), 10)

print(len(good_contour))
cv2.imshow("B", img1)
cv2.waitKey(0)
cv2.destroyAllWindows
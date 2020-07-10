import cv2

good_contour_trainee = []
threshold_area = 5000

img = cv2.imread('training/Arr.png')
gray_trainee_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thres = cv2.threshold(gray_trainee_image, 20, 255, 0)
cv2.imshow("Thresholding", thres)
contours_trainee, heir1 = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour_trainee in contours_trainee:
    if cv2.contourArea(contour_trainee) > threshold_area:
        good_contour_trainee.append(contour_trainee)

cv2.drawContours(img, good_contour_trainee, -1, (0,255,0), 3)
cv2.imshow("Input", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

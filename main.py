import cv2
import os
import contour_list
import math
from statistics import mean

path_training = "training"
good_contour_trainee = []
threshold_area = 5000

# Pre-Processing of the input image
# Import the image for training
trainee = cv2.imread(f'{path_training}/B.png')
gray_trainee_image = cv2.cvtColor(trainee, cv2.COLOR_BGR2GRAY)
ret, thres = cv2.threshold(gray_trainee_image, 20, 255, 0)
contours_trainee, heir1 = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour_trainee in contours_trainee:
    if cv2.contourArea(contour_trainee) > threshold_area:
        good_contour_trainee.append(contour_trainee)

cv2.drawContours(trainee, good_contour_trainee, -1, (0,255,0), 3)
cv2.imshow("Input", trainee)

num_of_contour = len(good_contour_trainee)
print(f'num_of_contour : {num_of_contour}')
# Function call to get the nearest contours list
contour_letters = contour_list.contour_list_train(num_of_contour)

match_contour = []
# Comparison of the contours based on area
if num_of_contour == 1:
    for x in range(len(contour_letters)):
        match_value = cv2.matchShapes(contour_letters[x][1][0], good_contour_trainee[0],1,0.0)
        match_contour.append(match_value)
# if the contours > 1
else:
    good_contour_trainee = sorted(good_contour_trainee, key = lambda x: cv2.contourArea(x), reverse=True)
    for x in range(len(contour_letters)):
        match_value_single = []
        for y in range(num_of_contour):
            match_value = cv2.matchShapes(contour_letters[x][1][y], good_contour_trainee[0],1,0.0)
            match_value_single.append(match_value)
        match_contour.append(mean(match_value_single))

index = match_contour.index(min(match_contour))
print(index)
print(f"Letter matched with {contour_letters[index][0]}")
letter = str(contour_letters[index][0])
print(f"Letter Input : {letter[0:1]}")
cv2.waitKey(0)
cv2.destroyAllWindows()
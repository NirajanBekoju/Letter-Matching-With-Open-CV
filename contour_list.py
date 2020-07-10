import cv2
import os

def contour_list_train(num_contour):
    path_countour_images = "countour-letter"
    images_list = os.listdir(path_countour_images)
    threshold_area = 10000

    # Contour image list according to the contouer number
    contour_one = []
    contour_two = []
    contour_three = []

    for image in images_list:
        # Basic Operation on the images
        img = cv2.imread(f'{path_countour_images}/{image}')
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray_img, 127, 255, 0) # 0 => THRESH_BINARY
        contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #  Filtering the contour
        good_contour = []
        for contour in contours:
            if cv2.contourArea(contour) > threshold_area:
                good_contour.append(contour)
        
        good_contour  = sorted(good_contour, key = lambda x:cv2.contourArea(x), reverse = True)
        num_good_contour = len(good_contour)

        # Seeking the right contour list
        if num_good_contour == 1:
            contour_one.append([image, good_contour])
        elif num_good_contour == 2:
            contour_two.append([image, good_contour])
        elif num_good_contour == 3:
            contour_three.append([image, good_contour])
        else:
            print("No Contour Matches")
    # Checking for the return values
    if num_contour == 1:
        return contour_one
    elif num_contour == 2:
        return contour_two
    elif num_contour == 3:
        return contour_three
    else:
        return False


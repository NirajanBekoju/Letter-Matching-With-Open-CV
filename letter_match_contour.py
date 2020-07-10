import cv2
import os

path = "letters"
dest_countour = "countour-letter"
letters = os.listdir(path)
counter = 0
for letter in letters:
    counter += 1
    img = cv2.imread(f'{path}/{letter}')
    _, inverted = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    cv2.imwrite(f'{dest_countour}/{letter}', inverted)
    if counter < 3:
        cv2.imshow(f'Orinal{counter}', img)
        cv2.imshow(f'{counter}', inverted) 

cv2.waitKey(0)
cv2.destroyAllWindows()
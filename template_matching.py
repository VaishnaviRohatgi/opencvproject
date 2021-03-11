import numpy as np
import cv2

img = cv2.imread('simpsons.jpg')
cv2.imshow('original', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('barts_face.jpg', 0)
cv2.imshow('template', template)
w, h = template.shape[::-1]

result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
loc = np.where(result >= 0.8)

for point in zip(*loc[::-1]):
    cv2.rectangle(img, point, (point[0]+w, point[1]+h), (0, 255, 0), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
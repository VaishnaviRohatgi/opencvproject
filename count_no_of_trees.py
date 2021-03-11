import cv2
import numpy as np

img = cv2.imread('preview.jpeg')
#img = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))
cv2.imshow('Trees', img)


# image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray image', gray)
cv2.waitKey(0)

blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)


_, threshold_one = cv2.threshold(blur, 0, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)


# thresholded image
cv2.imshow('threshold image', threshold_one)
cv2.waitKey(0)


kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(threshold_one, cv2.MORPH_OPEN, kernel, iterations=3)

cv2.imshow('opening', opening)

# contours
contours, h = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print('Number of trees found:', len(contours))

# Iterate all found contours
for cnt in contours:

    cv2.drawContours(img, [cnt], 0, (0, 0, 255), 1)


# final image
cv2.imshow('result image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



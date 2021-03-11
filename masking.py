import cv2 as cv
import numpy as np

img = cv.imread('cats.jpg')
cv.imshow('Cats', img) 

# shape and size of mask should be same as that of actual image
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1 )
# cv.imshow('Mask', mask)

rectangle = cv.rectangle(blank.copy(),  (30,30), (370,370), 255, -1 )

weirdShape = cv.bitwise_and(circle,rectangle)
cv.imshow('Weird Shape', weirdShape)

masked = cv.bitwise_and(img, img, mask=weirdShape)
cv.imshow('Masked', masked)

cv.waitKey(0)
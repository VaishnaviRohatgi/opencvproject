import cv2 as cv
import numpy as np

img = cv.imread('colors.jpg')
cv.imshow('colors', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# BGR image can be split into its 3 colour channels.

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merge these channels

merged = cv.merge([b, g, r])
cv.imshow("merged", merged)


cv.waitKey(0)
import cv2 as cv
# import numpy as np

img = cv.imread('cats.jpg')
cv.imshow("image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow("Simple threshold", thresh)

threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple threshold inverse", thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 5)
cv.imshow('Adaptive thresholding', adaptive_thresh)



cv.waitKey(0)
cv.destroyAllWindows()

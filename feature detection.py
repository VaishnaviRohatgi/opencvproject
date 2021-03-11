import cv2
import numpy as np

img1 = cv2.imread('simpsons.jpg')
img2 = cv2.imread('bart 3.jpg')

img1 = cv2.resize(img1, (img1.shape[0]//2, img1.shape[1]//2))

cv2.imshow('simpson', img1)
cv2.imshow('face', img2)
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()

kp1, des1 = sift.detectAndCompute(gray, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

#brute force matching
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance )

matching_result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:30], None)
cv2.imshow('matching result', matching_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
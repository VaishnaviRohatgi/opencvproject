import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('cats.jpg')
cv.imshow('Cats', img)

#plt.imshow(img)
#plt.show()


# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#hsv to BGR
bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('BGR', bgr)



plt.imshow(rgb)
plt.show()

cv.waitKey(0)
import cv2
import numpy as np

img = cv2.imread('lena.jpg')
cv2.imshow('Lena', img)

#translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)

# -x = left
# x = right
# y = down
# -y = up

translated = translate(img, -90, 20)
cv2.imshow('Translation', translated)


# rotation
def rotate(img, angle, rotpoint=None):
    (height,width) = img.shape[:2]
    if rotpoint is None:
        rotpoint = (width/2, height/2)

    rotMat = cv2.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(img, rotMat, dimensions)
rotated = rotate(img, 45)
cv2.imshow('Rotated', rotated)


# resizing
resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)
cv2.imshow('resized', resized)

# Flipping
flip = cv2.flip(img, -1)
cv2.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv2.imshow('Cropped', cropped)


cv2.waitKey(0)
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("cats.jpg")
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("cats",img)


kernel = np.ones((5, 5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
gblur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)
bilateralfilter = cv2.bilateralFilter(img, 9, 75, 75)


titles = ['image', '2D convolution', 'blur', ' Gblur', 'median', 'bilateralfilter']
images = [img, dst, blur, gblur, median, bilateralfilter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

#plt.show()

# Averaging
average = cv2.blur(img,(3,3))
cv2.imshow('Average', average)

# Gaussian Blur
gblur = cv2.GaussianBlur(img, (3,3), 0)
cv2.imshow('Gaussian', gblur)

# Median Blur
mblur = cv2.medianBlur(img,3)
cv2.imshow('Median', mblur)

# Bilateral Blur
bblur = cv2.bilateralFilter(img, 5, 5, 5)
cv2.imshow('bilateral', blur)


cv2.waitKey(0)
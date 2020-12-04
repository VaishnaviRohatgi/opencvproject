import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("messi5.jpg", cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, c2.CV_64F)
lap = np.uint8(np.absolute(lap))

titles = ['image', 'laplacian']
images = [img, dst, blur, gblur, median, bilateralfilter, lap]

for i in range(6):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
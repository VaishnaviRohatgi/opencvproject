import cv2 as cv
import numpy as np

img = cv.imread('gradient.png', 0)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

cv.imshow("image", img)
cv.imshow("th1", th1 )


cv.waitKey(0)
cv.destroyAllWindows()
import numpy as np
import cv2
import os

def loadImages(path="."):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(".jpg")]

def convolve2d(img, kernel):
    output = cv2.filter2D(img, -1, kernel)
    return output

filenames = loadImages()

images = []

for file in filenames:
    images.append(cv2.imread(file, cv2.IMREAD_GRAYSCALE))
sharpen = 0
edge = 0
bblur = 0
gblur = 0

for image in images:
    # sharpened image
    k = np.array([[0,-1,0], [-1, 5, -1], [0,-1,0]])
    sharpened = convolve2d(image, k)
    cv2.imwrite(str(sharpen)+"sharpen.jpg", sharpened)
    sharpen+=1

    # edge detection
    ke = np.array([[-1, 0, 1], [0, 0, 0], [1, 0, -1]])
    image_edge = convolve2d(image, ke)
    cv2.imwrite(str(edge)+"edge.jpg", image_edge)
    edge+=1

    # box blur
    kbb = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    box_blurred = convolve2d(image, kbb/9)
    cv2.imwrite(str(bblur)+"box_blurred.jpg", box_blurred)
    bblur += 1

    # gaussian blur
    kgb = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
    gaussianblurred = convolve2d(image, kgb/16)
    cv2.imwrite(str(gblur)+'gaussian_blur.jpg', gaussianblurred)
    gblur += 1


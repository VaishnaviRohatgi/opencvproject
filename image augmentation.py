import random
import cv2
import glob

image_list = []
s_amd_p_images = []
hor_flip_images = []
ver_flip_images =[]


def add_noise(img):
    # Getting the dimensions of the image
    row, col = img.shape

    # Randomly pick some pixels in the
    # image for coloring them white
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # Color that pixel to white
        img[y_coord][x_coord] = 255

    # Randomly pick some pixels in
    # the image for coloring them black
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # Color that pixel to black
        img[y_coord][x_coord] = 0

    return img


for filename in glob.glob(r"C:\Users\Dell\Desktop\datasets\dataset\dataset\Pikachu\*.jpg"):
    img_read = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    image_list.append(img_read)

for image in image_list:
    resized_image = cv2.resize(image, (image.shape[1]//2,image.shape[0]//2), cv2.INTER_AREA)
    image_blur = cv2.GaussianBlur(resized_image, (5,5), 0)
    img = add_noise(image_blur)
    s_amd_p_images.append(img)
    hor_flip = cv2.flip(image, 1)
    hor_flip_images.append(hor_flip)
    ver_flip = cv2.flip(image, 0)
    ver_flip_images.append(ver_flip)


for (i, new) in enumerate(s_amd_p_images):
    cv2.imwrite(r"C:\Users\Dell\Desktop\datasets\salt&pepper\frame%d.jpg" % i, new)

for (i, new) in enumerate(hor_flip_images):
    cv2.imwrite(r"C:\Users\Dell\Desktop\datasets\horizontal flip\frame%d.jpg" % i, new)

for (i, new) in enumerate(ver_flip_images):
    cv2.imwrite(r"C:\Users\Dell\Desktop\datasets\vertical flip\frame%d.jpg" % i, new)



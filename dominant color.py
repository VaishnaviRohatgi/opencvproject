import cv2
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image
import matplotlib.pyplot as plt

class DominantColors:
    CLUSTERS = None
    IMAGE = None
    COLORS = None
    LABELS = None

    def __init__(self, image, clusters=3):
        self.CLUSTERS = clusters
        self.IMAGE = image

    def dominantColors(self):
        # read image
        img = cv2.imread(self.IMAGE)

        # convert to rgb from bgr
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # reshaping to a list of pixels
        img = img.reshape((img.shape[0] * img.shape[1], 3))

        # save image after operations
        self.IMAGE = img

        # using k-means to cluster pixels
        kmeans = KMeans(n_clusters=self.CLUSTERS)
        kmeans.fit(img)

        # the cluster centers are our dominant colors.
        self.COLORS = kmeans.cluster_centers_

        # save labels
        self.LABELS = kmeans.labels_

        # returning after converting to integer from float
        return self.COLORS


img = 'colors.jpg'
clusters = 5
dc = DominantColors(img, clusters)
colors = dc.dominantColors()
print(colors)



colors = (np.array(colors)).astype(np.uint8)

title = "p"
#creating bar image
cols = len(colors)
rows = max([1, int(cols/2.5)])

# Create color Array
barFullData = np.tile(colors, (rows,1)).reshape(rows, cols, 3)

# Create Image from Array
barImg = Image.fromarray(barFullData, 'RGB')

#saving image
barImg.save("{}_{}.png".format(title,"method"))
barImg.show()
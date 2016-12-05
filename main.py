from PIL import Image
import numpy as np

import matplotlib.pyplot as plt

from image_segmenter import ImageSegmenter

import os
image_path = "./images/imagenet_32/001_ori.png"
img = Image.open(image_path)
pixels = np.array(img)

image_segmenter = ImageSegmenter(pixels)
segmented_image = image_segmenter.segment()

print segmented_image

heatmap = plt.pcolor(segmented_image,cmap=plt.cm.Greys)

plt.show()
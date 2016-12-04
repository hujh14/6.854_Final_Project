from PIL import Image
import numpy as np

from image_segmenter import Image_Segmenter

import os
image_path = "./images/imagenet_128/001_ori.png"
img = Image.open(image_path)
pixels = np.array(img)

image_segmenter = Image_Segmenter(pixels)
segmented_image = image_segmenter.segment()

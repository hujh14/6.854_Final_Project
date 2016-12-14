from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from image_segmenter import ImageSegmenter
import os


image_path = "./images/imagenet_32/014_ori.png"
img = Image.open(image_path)
pixels = np.array(img)

algorithm = 'dfs'
verbose = True

afn_func = 'average_distance' # or squared_distance
# afn_func = 'squared_distance'

image_segmenter = ImageSegmenter(pixels, afn_func)
segmented_image = image_segmenter.segment(algorithm, verbose)

if verbose: 
    print segmented_image

heatmap = plt.imshow(segmented_image,cmap='gray_r', interpolation='none')

plt.show()
from PIL import Image
import numpy as np

from graph import *

import os
image_path = "./images/imagenet_128/001_ori.png"
img = Image.open(image_path)
pixels = np.array(img)

graph = Graph(pixels)

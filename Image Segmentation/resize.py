from PIL import Image

import os

def resize_images(dir_path, output_dir_path):
    for filename in os.listdir(dir_path):
        if os.path.splitext(filename)[1] == ".png":
            image_path = os.path.join(dir_path, filename)
            resize_image(image_path, output_dir_path)

def resize_image(image_path, output_dir_path, height=32, width=32):
    image_number = os.path.basename(image_path).split("_")[0]
    output_image_name = "{}_ori.png".format(image_number)
    output_path = os.path.join(output_dir_path, output_image_name)

    img = Image.open(image_path)
    img = img.resize((height, width), Image.ANTIALIAS)
    img.save(output_path, optimize=True)


dir_path = "./images/imagenet"
output_path = "./images/imagenet_32"

resize_images(dir_path, output_path)

from PIL import Image
import csv
import os
from os import listdir


def resize_image(image, size):
    # Load image and resize using pillow - currently not maintaining aspect ratio
    img = Image.open(image)
    fname = image.replace("images/", "").replace(".jpg", "").replace(".png", "")
    newsize = (size[0],size[1])
    img_new = img.resize(newsize)
    size_string = f"{size[0]}x{size[1]}"
    
    # Uses image dpi however if info not available will return false
    if 'dpi' in img.info.keys() :
        dpi = img_new.info['dpi'][0] * img_new.info['dpi'][1]
        if dpi >= 300:
            img_new.save(f"./resized_images/{fname}-{size_string}.jpg","JPEG")
            return size_string
        else:
            return False
    else:
        img_new.save(f"./resized_images/{fname}-{size_string}.jpg","JPEG")
        return size_string


def resize_and_write():
    # takes images in image_folder
    image_folder = os.listdir("images")

    # Add desired sizes here in nested list format
    sizes = [[10,20],[30,50]]

    # Will take each file in image_folder and run the resize saving only if dpi matches specification and adding to csv file 
    for f in image_folder:
        file_path = f"images/{f}"
        with open('info.csv','a') as fd:
            applied_sizes =[]
            fieldnames = ["filename", "sizes"]
            writer = csv.DictWriter(fd, fieldnames=fieldnames)
            for size in sizes:
                img_resize_function = resize_image(file_path, size)
                if img_resize_function:
                    applied_sizes.append(img_resize_function)
            writer.writeheader()       
            writer.writerow({"filename": f, "sizes": applied_sizes})

resize_and_write()
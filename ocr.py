from PIL import Image
import os

im_file = r"data\page_01.jpg"

try:
    im = Image.open(im_file)
    print(im.size)
    im.rotate(60).show()
    im.save('temp/page_01.jpg')
except FileNotFoundError as e:
    print(f"Error: {e}")

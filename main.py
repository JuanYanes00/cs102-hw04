import sys
from PIL import Image

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size

# Create a new, all-white image that's the same size as the original
new_img = Image.new("RGB", (width, height), "white")

# TODO: Replace this with your own filter!
# Median pixel filter, taken from https://note.nkmk.me/en/python-opencv-pillow-image-size

for i in range(1, width - 1):
    for j in range(1, height -1):
        r, g, b = img.getpixel((i,j))
        if (g+50>255 or b-50<0):
            r=int(g)
            g=int(b)
            b=int(r/5)
        else:
            r = int(g + 50)
            g = int(b - 50)
            b = int(r / 5)

        new_img.putpixel((i, j), (r,g,b))

new_img.save(output_path, "JPEG")
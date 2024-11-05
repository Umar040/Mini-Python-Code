from PIL import Image
import numpy as np

img = Image.open("./Images/Right Arrow.png").convert('RGBA')
imgData = img.getdata()

newImg = []
for x in imgData:
    if x[0] == 255 and x[1] == 255 and x[2] == 255:
        newImg.append((255,255,255,0))
    else:
        newImg.append((36,252,3,255))
img.putdata(newImg)
img.show()
img.save("Green Right Arrow.png", "PNG")




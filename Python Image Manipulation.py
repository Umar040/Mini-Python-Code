from PIL import Image
import numpy as np

img = Image.open("./Images/Right Arrow.png").convert('RGBA') #Image path then convert to RGBA if it is not already
imgData = img.getdata()

newImg = []
for x in imgData:
     #0 is red, 1 is green, 2 is blue and 3 is alpha (Transparency)
    if x[0] == 255 and x[1] == 255 and x[2] == 255: #If the background is white which is 255 in RGB make it transparent so it removes the background
        newImg.append((255,255,255,0)) 
    else: #Otherwise add the RGB value below (Current is light green)
        newImg.append((36,252,3,255))
img.putdata(newImg) #Create the new image
img.show() #Display it
img.save("Green Right Arrow.png", "PNG") #Save the image as PNG to the current folder




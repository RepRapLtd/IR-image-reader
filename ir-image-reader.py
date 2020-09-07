"""
Short program to read an image from an IR camera with a temperature scale
then allow you to get temperatures from it by clicking with the mouse.

NB assumes the temperature scale is oriented in the Y direction.
Also the PIL Image y direction is from top to bottom... (Descartes, 
did you die in vain?)

    $ python3 ir-image-reader.py

Adrian Bowyer
RepRap Ltd
7 September 2020

https://reprapltd.com

Licence: GPL

"""



import sys
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np

clickCount = 0
minT = 0
maxT = 0
xMin = 0
yMin = 0
xMax = 0
yMax = 0

def GetTemperature(x, y):
 global clickCount
 global minT
 global maxT
 global xMin
 global yMin
 global xMax
 global yMax
 cordinate = x, y
 yClose = yMin
 pixel = irImage.getpixel(cordinate)
 x = (xMin + xMax)/2
 d = sys.float_info.max
 for y in range(int(yMax), int(yMin)): # Y axis backwards...
  cordinate = x, y
  scalePixel = irImage.getpixel(cordinate)
  r = (pixel[0]-scalePixel[0])**2 + (pixel[1]-scalePixel[1])**2 + (pixel[2]-scalePixel[2])**2
  if r < d:
   d = r
   yClose = y
 return minT + (maxT - minT)*(yClose - yMin)/(yMax - yMin)
 

def onclick(event):
 global clickCount
 global minT
 global maxT
 global xMin
 global yMin
 global xMax
 global yMax
 global irImage
 x = event.xdata
 y = event.ydata
 clickCount += 1
 if clickCount is 1:
  xMin = x
  yMin = y
 elif clickCount is 2:
  xMax = x
  yMax = y
 else:
  t = GetTemperature(x, y)
  print(f"T = {t:.1f}")
  

irFile = input("Image file: ") 
irImage = Image.open(irFile)
pic = np.array(irImage)
fig = plt.imshow(pic)
canvas = fig.figure.canvas
cid = canvas.mpl_connect('button_press_event', onclick)
minT = float(input("Minimum temperature: "))
maxT = float(input("Maximum temperature: "))
print("Click on the min then max ends of the temperature bar.")
plt.show()


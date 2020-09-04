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

def GetTemperatureScale():
 x = (xMin + xMax)/2
 

def onclick(event):
 print('you pressed', event.key, event.xdata, event.ydata)
 x = event.xdata
 y = event.ydata
 clickCount += 1
 if clickCount is 1:
  xMin = x
  yMin = y
 elif clickCount is 2:
  xMax = x
  yMax = y
  GetTemperatureScale()
 else
  



irFile = input("Image file: ") 
irImage = Image.open(irFile)
pic = np.array(irImage)
#irImage.show()
mutable_object = {} 
fig = plt.imshow(pic)
canvas = fig.figure.canvas
cid = canvas.mpl_connect('button_press_event', onclick)
#lines, = plt.plot([1,2,3])
minT = float(input("Minimum temperature: "))
maxT = float(input("Maximum temperature: "))
print("Click on the min then max ends of the temperature bar.")
plt.show()
X_coordinate = mutable_object['click']
print(X_coordinate)

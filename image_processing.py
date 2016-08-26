import cv2
import numpy as np
#Read Image
img = cv2.imread('hand.jpg')

test = img[0,0]
print test



#Display Image
#cv2.imshow('image',img)
# Scaling factor
img2 = cv2.resize(img,None,fx=0.10, fy=0.10, interpolation = cv2.INTER_CUBIC)
for x in range(0, 299):
  for y in range (0,299):
   img2 [x,y] =[255,255,255]

#Applying Grayscale filter to image
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#Saving filtered image to new file
cv2.imwrite('graytest.jpg',gray)

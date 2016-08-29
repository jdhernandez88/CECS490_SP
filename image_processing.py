import cv2
import numpy as np
#Read Image
img = cv2.imread('hand.jpg')

test = img[0,0]
#median = cv2.medianBlur(img,5)

#Resize Image
img2 = cv2.resize(img,None,fx=0.10, fy=0.10, interpolation = cv2.INTER_CUBIC)

#Applying Grayscale filter to image
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imwrite('graytest.jpg',gray)

#Apply BilateralFilter
blur = cv2.bilateralFilter(gray,10,100,100)
cv2.imwrite('blurtest.jpg',blur)

#Apply Edge Detetion
edges = cv2.Canny(gray,100,255)
cv2.imwrite('edgetest.jpg',edges)
#print test
#print test
"""
# testing some file reading 
#kernal = open('test.txt', 'r')
#print kernal.read()
kernal = [1, 0, 1,
          0, 1, 0,
          1, 0, 1]

#multiply each pixial with kernal
for p in range(0,299)
for u in range(0,299)
for l in range(0,4)
 for o in range(0,9)

    kernal[o]*img[p,u,l]
q=kernal[0]*image[0,0,0]
kernal[1]*image[0,1,0]
kernal[2]*image[0,2,0]
kernal[3]*image[1,0,0]
kernal[4]*image[1,1,0]
kernal[5]*image[1,2,0]
kernal[6]*image[2,0,0]
kernal[7]*image[2,1,0]
kernal[8]*image[2,2,0]


#print array1[1]
s=0
for z in range(0,3):
 s = s + kernal[z]
 print s

#Display Image
#cv2.imshow('image',img)
# Scaling factor (fx= , fy= )

print img2[0,0,1]
print img2 [0,0]
#255 = black, 0=white
for x in range(0, 299):
  for y in range (0,299):
   img2 [x,y] =[0,255,255]
"""

#Applying Grayscale filter to image
#gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)


#Saving filtered image to new file
#cv2.imwrite('graytest.jpg',img3)

#Convolution is simple an element-wise multiplacation of two matrices followed by a sum
# two matrices, both with the same dimensions
# multiple them, element by element (not dot product just simple multiplacation)
# sum the elements together


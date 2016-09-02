import cv2
import numpy as np
import pprint


global y
global img_convo

y = 0

#Read Image
original = cv2.imread('hand.jpg')
img_resize = cv2.resize(original,None,fx=0.10, fy=0.10, interpolation = cv2.INTER_CUBIC)


#print (img[0,0,0]+img[0,0,1]+img[0,0,2])//3


#Luminance mask algorithm
for i in range(0,531):
 for j in range(0,299):
  R = img_resize[i,j,0]*0.299
  G = img_resize[i,j,1]*0.587
  B = img_resize[i,j,2]*0.114
  gray = R+G+B
  img_resize[i,j] = gray
 
img_gray = img_resize


cv2.imwrite('graytest.jpg',img_gray)


img_temp = img_gray
img_convo = img_temp

#Convolution
kernal = [0, 1, 10,
          -10, -4, 10,
         0, 1, 10]
#print img_convo[1,1,0]


for i in range(1,530):
 for j in range(1,298): 
  for k in range(0,2):
   for l in range(0,2):
    x = img_temp[(i+k),(j+k)]*kernal[k+l]
    y = y + x
 img_convo[(i+1),(j+1)] = y  

cv2.imwrite('convotest.jpg',img_gray)

#pprint.pprint(temp)






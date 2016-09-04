import cv2
import numpy as np
import pprint


global y
global img_convo

#Convolution
kernal = [[0, 1, 10],
          [-10, -4, 10],
           [0, 1, 10]]

#Read Image
original = cv2.imread('hand.jpg')
image = cv2.resize(original,None,fx=0.10, fy=0.10, interpolation = cv2.INTER_CUBIC)

#Luminance mask algorithm
def grayscale(image):
    for i in range(0,531):
     for j in range(0,299):
      R = image[i,j,0]*0.299
      G = image[i,j,1]*0.587
      B = image[i,j,2]*0.114
      gray = R+G+B
      image[i,j] = gray
    cv2.imwrite('graytest.jpg',image)
    print "Print sent"
    return image 

def convolution(image):
    y=0;
    for i in range(1,530):
     for j in range(1,298): 
      for k in range(0,2):
       for l in range(0,2):
        x = image[i+k][j+k]*kernal[k][l]
        y = y + x
     image[(i+1)][(j+1)] = y  #needs to be fixed
    cv2.imwrite('convotest.jpg',image)

img_gray = grayscale(image)
convolution(img_gray)








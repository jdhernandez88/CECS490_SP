#import cv2
#import pprint
#flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

#pprint.pprint(flags) # will print all in a row

import cv2
import numpy as np
import sys

cap = cv2.VideoCapture(0)
#img = cv2.imread(cap)
#print cap[0,0]

#s, img = cap.read()
#cv2.imshow("Test Picture", img)
#print img[0,0]

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([0,48,80])
    upper_blue = np.array([20,255,255])
    #lower_blue = np.array([100,170,170])
    #upper_blue = np.array([150,225,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

import cv2
import numpy as np
import pprint
import time



#global y
global img_convo

#Convolution
kernal1 = [[-0.5, -0.5, -0.5],
          [-0.5, 5, -0.5],
           [-0.5, -0.5, -0.5]]
kernal = [[-1, -1, -1],
          [-1, 8, -1],
           [-1, -1, -1]]

#Read Image
original = cv2.imread('hand_resize.jpg')
#image = cv2.resize(original,None,fx=0.05, fy=0.05, interpolation = cv2.INTER_CUBIC)
#cv2.imwrite('hand_resize.jpg',image)
#Luminance mask algorithm
def grayscale(image):
    for i in range(0,image.shape[0]):#531 #480 #120
     for j in range(0,image.shape[1]):#531 #640 #160
      R = image[i,j,0]*0.299
      G = image[i,j,1]*0.587
      B = image[i,j,2]*0.114
      gray = R+G+B
      image[i,j] = gray
    cv2.imwrite('graytest.jpg',image)
  #  print "Printed Grayscales"
    return image 


def convolution(image):
    
    img= image
   # print "x = ",img.shape[0]
   # print "y = ",img.shape[1]
    for y in range(1,image.shape[0]-1): #530
      for x in range(1,image.shape[1]-1): #298
        sum_all=0
        for j in range(0,2):
          for i in range(0,2):
            convo_sum = img[y+j-1][x+i-1]*kernal1[j][i]
            sum_all = sum_all + convo_sum
        img[y][x] = sum_all  #needs to be fixed
    cv2.imwrite('convotest.jpg',img)
    print "Printed Convolution"
    return img

x = grayscale(original)
convolution(x)

print "Image Dimentions: ", original.shape
#cv2.imwrite('convotest.jpg',y)
#img_gray = grayscale(image)
#convolution(img_gray)
print kernal [1][1]











"""

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
   # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    r= cv2.resize(frame,None,fx=0.2, fy=0.2, interpolation = cv2.INTER_CUBIC)
    gray =grayscale(r)
    convo = convolution(gray)

    # Display the resulting frame #Video is 480x640
    cv2.imshow('frame',convo)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #print time.time()

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
"""






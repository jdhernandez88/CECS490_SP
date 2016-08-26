import os.path
# import cv2

print os.path.exists("/Volumes/JAKE_USB/SeniorProject/hand.jpg")

# Returns the size in bytes
print os.path.getsize("/Volumes/JAKE_USB/SeniorProject/hand.jpg")

"""
image = cv2.imread("/Volumes/JAKE_USB/SeniorProject/hand.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.png',gray_image)
cv2.imshow('color_image',image)
cv2.imshow('gray_image',gray_image)
"""
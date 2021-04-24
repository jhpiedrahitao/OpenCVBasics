#Resizing and cropping
import cv2
import numpy as np



img=cv2.imread('resources/MIBS.PNG')
print(img.shape)
imgResize=cv2.resize(img,(300,310))
print(imgResize.shape)
imgCrop=img[0:200,200:500]
cv2.imshow("Output1",img)
cv2.imshow("Output2",imgResize)
cv2.imshow("Output3",imgCrop)

cv2.waitKey(0) 

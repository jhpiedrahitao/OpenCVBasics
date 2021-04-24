#Basic Functions
import cv2
import numpy as np

kernel=np.ones((5,5),np.uint8)

img=cv2.imread('resources/MIBS.PNG')
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,110,180)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded=cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("Output1",imgGray)
cv2.imshow("Output2",imgBlur)
cv2.imshow("Output3",imgCanny)
cv2.imshow("Output4",imgDialation)
cv2.imshow("Output5",imgEroded)
cv2.waitKey(0) 

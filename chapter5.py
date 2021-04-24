#Warp images
import cv2
import numpy as np

width,height = 720,1240
img=cv2.imread("resources/MIBS.PNG")
pts1=np.float32([[288,200],[257,573],[532,207],[514,590]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOut=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow('image',imgOut)
cv2.waitKey(0) 

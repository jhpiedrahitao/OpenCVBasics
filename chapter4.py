#shapes and text
import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
#print(img.shape)
#img[200:300,100:300]=255,0,0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,255),5)
cv2.rectangle(img,(0,0),(250,350),(145,213,45),2)
cv2.circle(img,(int(img.shape[1]/2),int(img.shape[0]/2)),30,(52,34,129),3)
cv2.putText(img,"Hello CV2",(210,300),cv2.FONT_HERSHEY_COMPLEX,1,(10,240,34),3)
cv2.imshow('image',img)
cv2.waitKey(0) 

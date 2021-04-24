import cv2 
import numpy as np

widthImg=480
heightImg=640
numberPlatesCascade=cv2.CascadeClassifier("resources/haarcascades/haarcascade_russian_plate_number.xml")
minimumArea=500
color=(255,0,255)
count=0

cap=cv2.VideoCapture(0)
cap.set(3,widthImg) #size
cap.set(4,heightImg) #size
cap.set(10,100) #brighthness
print(cap.isOpened())
while(True):
    success, img = cap.read()        
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberPlates=numberPlatesCascade.detectMultiScale(imgGray,1.1,10)
    for (x,y,w,h) in numberPlates:
        area=w*h
        if area > minimumArea:
            cv2.rectangle(img,(x,y),(x+w,y+w),color,2)
            cv2.putText(img, "NumberPlate", (x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,color,2)
            imgRoi=img[y:y+h,x:x+w]
            cv2.imshow("Plate",imgRoi)
    cv2.imshow("Video",img)
    if (cv2.waitKey(1)  & 0xFF == ord('s')):
        cv2.imwrite("resources/scanned/NoPlate_"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),color,cv2.FILLED)
        cv2.putText(img,"Scann Saved", (80,265),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),2)
        cv2.imshow("Video",img)
        cv2.waitKey(500)
        count+=1

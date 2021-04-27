# Object tracking
import cv2
import numpy as np
import time

pTime=0
cap = cv2.VideoCapture(0)
print(cap.isOpened())

tracker=cv2.TrackerMOSSE_create()

while(True):
    success, img = cap.read()

    cTime = time.time()
    fps = int(1/(cTime-pTime))
    pTime = cTime
    cv2.putText(img, "fps: "+str(fps), (50, 50),cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    
    cv2.imshow("Video", img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

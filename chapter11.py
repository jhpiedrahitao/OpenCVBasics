# Object tracking
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
print(cap.isOpened())

#tracker = cv2.TrackerMOSSE_create()
tracker = cv2.TrackerCSRT_create()
success, frame = cap.read()
bbox=cv2.selectROI("Tracking",frame,False)
tracker.init(frame,bbox)

def drawBox(img,bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),3)
    cv2.putText(img, "Tracking", (50, 100),
                cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)

while(True):
    timer = cv2.getTickCount()
    success, img = cap.read()
    success, bbox = tracker.update(img)

    if success:
        drawBox(img,bbox)
    else:
        cv2.putText(img, "Lost", (50, 100),
                    cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

    fps = int(cv2.getTickFrequency() / (cv2.getTickCount() - timer))
    cv2.putText(img, "fps: "+str(fps), (50, 50),cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    
    cv2.imshow("Video", img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break


#tracker = cv2.TrackerBoosting_create()
#tracker = cv2.TrackerMIL_create()
#tracker = cv2.TrackerKCF_create()
#tracker = cv2.TrackerTLD_create()
#tracker = cv2.TrackerMedianFlow_create()
#tracker = cv2.TrackerCSRT_create()
#tracker = cv2.TrackerMOSSE_create()


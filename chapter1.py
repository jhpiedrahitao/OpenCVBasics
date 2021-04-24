#reading images, videos and webcams
import cv2
print("Packege imported")
''' importing images
img=cv2.imread("resources/MIBS.PNG")
print(img)
cv2.imshow("Output",img)
cv2.waitKey(0) 
'''
''' importing a video
cap=cv2.VideoCapture("resources/Storyboard2.wmv")
print(cap)
while(True):
    success, img = cap.read() 
    cv2.imshow("Video",img)
    if (cv2.waitKey(1)  & 0xFF == ord('q')):
        break
'''
#capture web camm
cap=cv2.VideoCapture(1)
cap.set(3,640) #size
cap.set(4,480) #size
cap.set(10,100) #brighthness
print(cap.isOpened())
while(True):
    success, img = cap.read() 
    cv2.imshow("Video",img)
    if (cv2.waitKey(1)  & 0xFF == ord('q')):
        break
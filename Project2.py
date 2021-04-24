#Document Scanner
import cv2
import numpy as np

widthImg=480
heightImg=640
 
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img):
    biggest=np.array([])
    maxArea=0
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>=5000:
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            if area > maxArea and len(approx)==4:
                biggest=approx
                maxArea=area
    cv2.drawContours(imgCount,biggest,-1,(255,0,0),20)
    return biggest

def reorder(myPoints):
    myPoints=myPoints.reshape((4,2))
    newPoints=np.zeros((4,1,2),np.int32)
    add=myPoints.sum(1)
    diff=np.diff(myPoints,axis=1)
    newPoints[0]=myPoints[np.argmin(add)]
    newPoints[3]=myPoints[np.argmax(add)]
    newPoints[1]=myPoints[np.argmin(diff)]
    newPoints[2]=myPoints[np.argmax(diff)]
    return newPoints

def getWarp(img, biggest):
    biggest=reorder(biggest)
    imgOut=np.array([])
    pts1=np.float32(biggest)
    pts2=np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
    matrix=cv2.getPerspectiveTransform(pts1,pts2)
    imgOut=cv2.warpPerspective(img,matrix,(widthImg,heightImg))
    imgCropped=imgOut[30:imgOut.shape[0]-20,20:imgOut.shape[1]-20]
    imgCropped=cv2.resize(imgCropped,(widthImg,heightImg))
    return imgCropped

def preProcesing(img):
    imgGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgblur=cv2.GaussianBlur(imgGray,(5,5),1)
    imgCanny=cv2.Canny(imgblur,100,200)
    kernel=np.ones((5,5))
    imgDial=cv2.dilate(imgCanny,kernel,iterations=2)
    imgThres=cv2.erode(imgDial,kernel,iterations=1)
    return imgThres

cap=cv2.VideoCapture(0)
cap.set(3,widthImg) #size
cap.set(4,heightImg) #size
cap.set(10,150) #brighthness
print(cap.isOpened())

final=np.ones((widthImg,heightImg))
while(True):
    success, img = cap.read()
    cv2.resize(img,(widthImg,heightImg))
    imgCount = img.copy()
    
    imgThres=preProcesing(img)
    biggest = getContours(imgThres)
    if biggest.size!=0:
        imgWarped = getWarp(img,biggest)
        imgWarpedGray=cv2.cvtColor(imgWarped,cv2.COLOR_BGR2GRAY)
        final=cv2.adaptiveThreshold(imgWarpedGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,3)
        imgArray=([img,imgThres,imgCount],
               [imgWarped,imgWarpedGray,final])
    else:
        imgArray=([img,imgThres,img],
                  [img,img,img])
    stackedImages=stackImages(0.6,imgArray)

    cv2.imshow("Video",stackedImages)
    cv2.imshow("Result",final)
    if (cv2.waitKey(1)  & 0xFF == ord('q')):
        break
#detcting clicks and warping images 

import cv2
import numpy as np



width,height = 720,1240
circles=np.zeros((4,2),np.int)
counter=0

def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        circles[counter] = x, y
        counter += 1

img=cv2.imread("resources/MIBS.PNG")

while True:
    if counter==4:
        pts1 = np.float32([circles[0], circles[1],circles[2],circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOut = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("owarped Image", imgOut)

    for x in range (0,4):
        cv2.circle(img,(circles[x][0],circles[x][1]),5,(255,0,220),cv2.FILLED)

    cv2.imshow("original Image", img)
    cv2.setMouseCallback("original Image",mousePoints)

    cv2.waitKey(1)





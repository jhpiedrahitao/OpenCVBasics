import cv2
import numpy as np
from PIL import Image
import pytesseract
from datetime import datetime, date
import requests
import json

sensor_db_url = None

def post_to_sensor_db(data):
    date = datetime.now().strftime('%d_%m_%Y')
    time = datetime.now().strftime('%H:%M:%S')
    post1 = json.dumps({'date': date, 'time': time,
                       'type': 'temperature', 'id': '003', 'data': data[0]})
    post2 = json.dumps({'date': date, 'time': time,
                       'type': 'humidity', 'id': '003', 'data': data[0]})
    post3 = json.dumps({'date': date, 'time': time,
                       'type': 'temperature', 'id': '004', 'data': data[0]})
    posts = [post1, post2, post3]
    for post in posts:
        try:
            response = requests.post(sensor_db_url, post)
            print('sensor db response: ' + str(response))
        except:
            print('conection no established')


def preprocess(img, block_size, gamma):
    img = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, gamma)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    return img


def getContours(frame):
    biggest = np.array([])
    maxArea = 0
    frameCanny = cv2.Canny(frame, 45, 55)
    frameCanny = cv2.dilate(frameCanny, kernel, iterations=3)
    frameCanny = cv2.erode(frameCanny, kernel, iterations=2)
    contours, hierarchy = cv2.findContours(
        frameCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area >= 7000 and area < 80000:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.05*peri, True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    return biggest


def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    newPoints = np.zeros((4, 1, 2), np.int32)
    add = myPoints.sum(1)
    diff = np.diff(myPoints, axis=1)
    newPoints[0] = myPoints[np.argmin(add)]
    newPoints[3] = myPoints[np.argmax(add)]
    newPoints[1] = myPoints[np.argmin(diff)]
    newPoints[2] = myPoints[np.argmax(diff)]
    return newPoints


def getWarp(img, ptsSqu):
    ptsSqu = reorder(ptsSqu)
    imgOut = np.array([])
    pts1 = np.float32(ptsSqu)
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOut = cv2.warpPerspective(img, matrix, (300, 300))
    return imgOut


#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
kernel = np.ones((3, 3))

cap = cv2.VideoCapture('/dev/webcam_port')
digitsPos = [[[0, 64], [0, 92]], [[64, 128], [0, 92]], [[128, 192], [0, 92]], [
    [0, 64], [92, 184]], [[64, 128], [92, 184]], [[128, 192], [92, 184]], [[], []], [[], []]]

while True:
    displayDetected = False
    while not displayDetected:
        ret, frame = cap.read()
        frame = cv2.GaussianBlur(frame, (3, 3), 3)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(6, 6))
        #frame = clahe.apply(frame)
        ptsSqr = getContours(frame)
        if ptsSqr.size != 0:
            displayDetected = True
            frame = getWarp(frame, ptsSqr)[5:-5, 80:-25]
    frame = preprocess(frame, 43, 7)
    digits = []
    for pos in digitsPos:
        digits.append(frame[pos[1][0]:pos[1][1], pos[0][0]:pos[0][1]])

    #data = pytesseract.image_to_string(frame, config="--psm 6 digits")
    #print(f'Data: {data}')

    data = [10, 10, 10]
    #post_to_sensor_db(data)

    #imgStack = np.vstack((imgTIn, imgTOut, imgHIn))
    #cv2.imshow("outImage", imgStack)
    cv2.imshow('frame', frame)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()

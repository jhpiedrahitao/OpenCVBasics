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


    # CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
    # CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
    # CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file: 0 – start of the film, 1 – end of the film.
    # CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
    # CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
    # CV_CAP_PROP_FPS Frame rate.
    # CV_CAP_PROP_FOURCC 4-character code of codec.
    # CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
    # CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
    # CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
    # CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
    # CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
    # CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
    # CV_CAP_PROP_HUE Hue of the image (only for cameras).
    # CV_CAP_PROP_GAIN Gain of the image (only for cameras).
    # CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
    # CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
    # CV_CAP_PROP_WHITE_BALANCE_U The U value of the whitebalance setting
    # CV_CAP_PROP_WHITE_BALANCE_V The V value of the whitebalance setting
    # CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras
    # CV_CAP_PROP_ISO_SPEED The ISO speed of the camera
    # CV_CAP_PROP_BUFFERSIZE Amount of frames stored in internal buffer memory

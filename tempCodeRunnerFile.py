import cv2
from cvzone.HandTrackingModule import HandDetector

#cam
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

#hand detector
detector=HandDetector(detectionCon=0.8,maxHands=1)

while True:
    #get the frame from the web cam
    success,img=cap.read()
    #hands
    hands,img=detector.findHands(img)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
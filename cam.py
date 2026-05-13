import cv2
from cvzone.HandTrackingModule import HandDetector
import socket
#param
width=1280
height=720
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serv=("192.168.0.136",4679)
#cam
cap=cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

#hand detector
detector=HandDetector(detectionCon=0.8,maxHands=1)

while True:
    #get the frame from the web cam
    success,img=cap.read()
    #hands
    hands,img=detector.findHands(img)
    
    if hands:
        hand=hands[0]
        lmList=hand['lmList']
        data=[]
        #print(lmList)

        for lm in lmList:
            data.extend([lm[0],height-lm[1],lm[2]])
        
        sock.sendto(str.encode(str(data)),serv)

    img=cv2.resize(img,(0,0),None,0.5,0.5)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
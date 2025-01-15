import cv2
import mediapipe as mp 
import time 


cap = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()


while True:
    sucess,img = cap.read()



    cv2.imshow('image',img)
    cv2.waitKey(1)
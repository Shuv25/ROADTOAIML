import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_col=np.array([170, 120, 70])#can google this color as hsv lower limit of choiced lower
    upper_col=np.array([180, 255, 255])

    mask=cv2.inRange(hsv,lower_col,upper_col)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    kernal=np.ones((15,15),np.float32)/225
    smothed=cv2.filter2D(res,-1,kernal)
    blur=cv2.GaussianBlur(res,(15,15),0)
    median=cv2.medianBlur(res,15)
    bilateral=cv2.bilateralFilter(res,15,75,75)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    #cv2.imshow('smothed',smothed)
    #cv2.imshow('blur',blur)
    cv2.imshow('median',median)
    cv2.imshow('bilateral',bilateral)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    

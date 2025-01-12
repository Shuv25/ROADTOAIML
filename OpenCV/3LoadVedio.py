import numpy as np
import cv2
import matplotlib.pyplot as plt

cap=cv2.VideoCapture(0)#to start apturing vedio

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#to know your resolution
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc=cv2.VideoWriter_fourcc(*'XVID')#here XVID is codec, we can also use MP4V also
out=cv2.VideoWriter('Output.avi',fourcc,20.0,(width,height))#here 20.0 is frame per sc

while True:#an infinite loop untill i press q button
    ret,frame=cap.read()#original color capturing
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#second capturing in black and white
    out.write(frame)#writeing the frame input
    
    cv2.imshow('frame',frame)#to display the video for orginal
    cv2.imshow('gray',gray)#to display the video of gray
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()#to turn off the camera
out.release()
cv2.destroyAllWindows()

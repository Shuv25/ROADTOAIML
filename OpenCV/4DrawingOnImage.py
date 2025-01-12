import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('C:\\Users\\hp\\Documents\\GitHub\\ROADTOAIML\\OpenCV\\gojo.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(0,0,0),15)
cv2.rectangle(img,(15,25),(200,300),(255,0,0),5)
cv2.circle(img,(400,300),100,(0,0,255),5)
cv2.circle(img,(400,300),100,(0,0,255),-1)#here -1 will fill the circle

arr=np.array([[10,5],[200,300],[400,200],[300,100],[250,150]],np.int32)
cv2.polylines(img,[arr],True,(0,255,255),5)#True is use to wa want the last two points to connect 

font=cv2.FONT_HERSHEY_SIMPLEX
                                #pos       #size 1        #thickness 2  #style of the text
cv2.putText(img,'OpenCV Font',(0,130),font,1,(0,0,255),2,cv2.LINE_AA)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

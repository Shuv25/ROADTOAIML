import numpy as np
import cv2

img=cv2.imread('bookpage.jpg')
ret,threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)
grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret2,threshold2=cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)
gaus=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow('img',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('gaus',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()

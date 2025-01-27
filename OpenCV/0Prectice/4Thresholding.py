import cv2
import numpy as np

img=cv2.imread('gojo.jpg')
ret,threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,gray_threshold=cv2.threshold(img_gray,12,255,cv2.THRESH_BINARY)
gaus_threshold=cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
ret, otsu_threshold = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

edges=cv2.Canny(img_gray,100,100)

cv2.imshow('img',img)
cv2.imshow('threshold',threshold)
cv2.imshow('gray_threshold',gray_threshold)
cv2.imshow('gaus_threshold',gaus_threshold)
#cv2.imwrite('gojo-gaus.jpg',gaus_threshold)
cv2.imshow('otsu_threshold',otsu_threshold)
cv2.imshow('edges',edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

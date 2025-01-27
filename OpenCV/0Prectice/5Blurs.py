import cv2
import numpy as np

img=cv2.imread('gojo.jpg')
gausianBlur=cv2.GaussianBlur(img,(15,15),0)
medianBlur=cv2.medianBlur(img,9)
bilateralBlur=cv2.bilateralFilter(img,15,75,75)

#cv2.imshow('img',img)
cv2.imshow('gausianBlur',gausianBlur)
#cv2.imwrite('gojo_blur.jpg',gausianBlur)
#cv2.imshow('medianBlur',medianBlur)
#cv2.imshow('bilateralBlur',bilateralBlur)

sharping_kernal=np.array([[0,-1,0],
                          [-1,5,-1],
                          [0,-1,0]])

sharped_img=cv2.filter2D(gausianBlur,-1,sharping_kernal)
cv2.imshow('sharped_img',sharped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

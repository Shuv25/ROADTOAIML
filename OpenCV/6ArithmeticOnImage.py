import numpy
import cv2

img1=cv2.imread('3D-Matplotlib.png')
img2=cv2.imread('mainsvmimage.png')

#add = img1+img2# Simply adds the pixel values of img1 and img2. May result in overflow if pixel values exceed 255.
#add=cv2.add(img1,img2)# Adds two images but handles pixel overflow properly by capping values at 255.
#weighted=cv2.addWeighted(img1,0.6,img2,0.4,0)#here im adding the custom weight of image like for img1 its 0.6,for img2 its 0.4 and last 0 is gamma value its for brightness adj

img3=cv2.imread('mainlogo.png')

row,cols,chnnels=img3.shape
roi=img1[0:row,0:cols]

img2gray=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)#if the pixel value>220 the it will be white or f pixel value<220 then it will be black then inverse their values

mask_inv=cv2.bitwise_not(mask)#Inverts the binary mask. Now the logo area is black, and the background is white.

img1bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img3fg=cv2.bitwise_and(img3,img3,mask=mask)

dest=cv2.add(img1bg,img3fg)
img1[0:row,0:cols]=dest

cv2.imshow('img1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

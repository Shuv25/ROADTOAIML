import cv2

img=cv2.imread('gojo.jpg')
cv2.rectangle(img,(50,50),(400,300),(255,0,0),2)
cv2.circle(img,(500,200),200,(0,0,255),-1)
cv2.line(img,(9,9),(400,200),(0,255,0),3)
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy
import cv2

img=cv2.imread('gojo.jpg',cv2.IMREAD_COLOR)

print(img[55,55])#printing the color of the imgage at the specific cordinate
img[55,55]=[255,255,255]#changing the color of imge to white
px=img[55,55]
print(px)

img[100:200,100:250]=[0,0,255]#here i am changing imgage color to red of a particular region

copied_area=img[400:500,480:550]#here i am copying a particular region of image
img[0:100,0:70]=copied_area#here i am pasting the copied region on diff region

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


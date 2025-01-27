import cv2

img=cv2.imread('gojo.jpg')
#cv2.imshow('img',img)

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('img_gray',img_gray)
#cv2.imwrite('gray_gojo.jpg',img_gray)

flip_image_xaxis=cv2.flip(img,0)
#cv2.imshow('flip_image_xaxis',flip_image_xaxis)

flip_image_yaxis=cv2.flip(img,1)
#cv2.imshow('flip_image_yaxis',flip_image_yaxis)

flip_image_baxis=cv2.flip(img,-1)
#cv2.imshow('flip_image_baxis',flip_image_baxis)


rotate_img_90=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('rotate_img_90',rotate_img_90)

rotate_img_180=cv2.rotate(img,cv2.ROTATE_180)
cv2.imshow('rotate_img_180',rotate_img_180)

rotate_img_270=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('rotate_img_270',rotate_img_270)

cv2.waitKey(0)
cv2.destroyAllWindows()

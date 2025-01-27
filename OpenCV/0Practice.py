import cv2
import numpy as np

img = cv2.imread('template.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('matching.jpg', 0)
templatetwo = cv2.imread('newmatching.jpg', 0)


w, h = template.shape[::-1]
w2, h2 = templatetwo.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
res2 = cv2.matchTemplate(img_gray, templatetwo, cv2.TM_CCOEFF_NORMED)

threshold = 0.7


def draw_matches(image, result, threshold, color, w, h):
    loc = np.where(result >= threshold)
    for pt in zip(*loc[::-1]): 
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), color, 3)


draw_matches(img, res, threshold, (0, 255, 255), w, h)  
draw_matches(img, res2, threshold, (255, 0, 0), w2, h2) 

cv2.imshow('Matched Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

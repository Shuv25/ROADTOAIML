import cv2
import numpy as np


height, width = 500, 500  
canvas = np.zeros((height, width, 3), dtype=np.uint8)

line_color = (255, 255, 255)  
line_thickness = 1 
cell_size = 50  


for y in range(0, height, cell_size):
    cv2.line(canvas, (0, y), (width, y), line_color, line_thickness)

for x in range(0, width, cell_size):
    cv2.line(canvas, (x, 0), (x, height), line_color, line_thickness)

cv2.imshow('Grid Pattern', canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()

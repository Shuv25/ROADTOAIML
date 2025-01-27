import numpy as np
import cv2

# Load the input image in color (BGR format)
img_bgr = cv2.imread('template.jpg')

# Convert the input image to grayscale for template matching
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# Load the template image in grayscale
template = cv2.imread('matching.jpg', 0)

# Get the width (w) and height (h) of the template
# `shape[::-1]` reverses the dimensions from (height, width) to (width, height)
w, h = template.shape[::-1]

# Perform template matching using the normalized cross-correlation method
# `cv2.matchTemplate` outputs a result matrix with matching confidence values
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

# Set the threshold for determining a "good match" (confidence >= 0.8)
threshold = 0.8

# Find the locations in the result matrix where confidence values meet or exceed the threshold
# `np.where` returns the indices of these locations in the form (y-coordinates, x-coordinates)
loc = np.where(res >= threshold)

# Loop through all matching locations
# `loc[::-1]` reverses the order of coordinates to (x, y) format for OpenCV functions
for pt in zip(*loc[::-1]):  
    # Draw a rectangle on the original color image at each matching location
    # `pt` is the top-left corner of the match, and `(pt[0]+w, pt[1]+h)` is the bottom-right corner
    # The rectangle is drawn in yellow (BGR: (0, 255, 255)) with thickness 2
    cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

# Display the original image with rectangles drawn around the detected template matches
cv2.imshow('detected', img_bgr)

# Wait indefinitely until any key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()

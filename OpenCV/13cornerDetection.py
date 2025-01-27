import cv2
import numpy as np

# Read the input image
img = cv2.imread('opencv-corner-detection-sample.jpg')

# Convert the image to grayscale
# This step is necessary because corner detection is typically applied to grayscale images
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert the grayscale image to float32 type (required by the corner detection algorithm)
gray = np.float32(img_gray)

# Detect corners using the Shi-Tomasi corner detection algorithm
# Parameters:
# - gray: the input image (grayscale, float32)
# - 100: the maximum number of corners to return
# - 0.01: the quality level (minimum accepted quality of corners, between 0 and 1)
# - 10: the minimum possible Euclidean distance between returned corners
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

# Convert the corner coordinates to integer values (necessary for drawing them)
corners = np.intp(corners)

# Iterate through all detected corners and draw them on the image
for corner in corners:
    x, y = corner.ravel()  # Flatten the (x, y) coordinates from the array
    cv2.circle(img, (x, y), 3, 255, -1)  # Draw a small circle at the corner location

# Display the image with the detected corners
cv2.imshow('img', img)

# Wait for a key press to close the window
cv2.waitKey(0)

# Destroy all OpenCV windows
cv2.destroyAllWindows()

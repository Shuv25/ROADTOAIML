import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the input images in grayscale mode
# img1: Template image (the object you want to find)
# img2: Target image (the scene where you want to search for the object)
img1 = cv2.imread('opencv-feature-matching-template.jpg', 0)
img2 = cv2.imread('opencv-feature-matching-image.jpg', 0)

# Initialize the ORB (Oriented FAST and Rotated BRIEF) detector
# ORB is a feature detection and description algorithm
orb = cv2.ORB_create()

# Detect keypoints and compute descriptors for both images
# Keypoints (kp1, kp2): Distinctive points in the images
# Descriptors (des1, des2): Feature vectors representing the regions around keypoints
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Create a brute-force matcher
# NORM_HAMMING: Hamming distance is used as a similarity metric for binary descriptors (like ORB)
# crossCheck=True: Ensures that matches are consistent in both directions (i.e., A->B and B->A)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match the descriptors from both images
# Matches are pairs of descriptors from the two images that are similar based on Hamming distance
matches = bf.match(des1, des2)

# Sort the matches based on their distance
# Lower distance means a better match
matches = sorted(matches, key=lambda x: x.distance)

# Draw the first 10 matches between the images
# img3: The output image showing matched keypoints connected with lines
# flags=2: Draw only the matched keypoints
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

# Display the resulting image with the matched keypoints
plt.imshow(img3)
plt.show()

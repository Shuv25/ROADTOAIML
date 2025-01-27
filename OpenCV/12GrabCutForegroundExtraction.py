import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load the input image
# This is the image on which foreground extraction will be performed
img = cv2.imread('opencv-python-foreground-extraction-tutorial.jpg')

# Create an initial mask for the image (same size as the image's height and width)
# Initialize all pixels as background (0)
mask = np.zeros(img.shape[:2], np.uint8)

# Create arrays for the background and foreground models
# These models are required by the GrabCut algorithm and will be updated during processing
# `bgdModel` and `fgdModel` are temporary arrays for internal calculations
bgdModel = np.zeros((1, 65), np.float64)  # Background model
fgdModel = np.zeros((1, 65), np.float64)  # Foreground model

# Define a rectangle that roughly contains the foreground object
# Format: (x, y, width, height) -> Top-left corner (x, y), and width and height of the rectangle
rect = (161, 79, 150, 150)

# Apply the GrabCut algorithm to segment the foreground from the background
# Parameters:
# - img: The input image
# - mask: The initial mask (updated by GrabCut during processing)
# - rect: The rectangle defining the region of interest for foreground
# - bgdModel: The array for the background model (updated internally)
# - fgdModel: The array for the foreground model (updated internally)
# - 5: Number of iterations the algorithm will run
# - cv2.GC_INIT_WITH_RECT: Specifies that the algorithm should use the rectangle for initialization
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# Update the mask to create a binary mask where:
# - Pixels marked as "sure background" (0) or "probably background" (2) are set to 0
# - Pixels marked as "sure foreground" (1) or "probably foreground" (3) are set to 1
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# Multiply the input image with the binary mask to isolate the foreground
# This sets the background pixels to 0 (black) while keeping the foreground as it is
img = img * mask2[:, :, np.newaxis]

# Display the resulting image using Matplotlib
plt.imshow(img)  # Show the image with the extracted foreground
plt.colorbar()   # Display a color bar (useful for understanding intensity levels)
plt.show()       # Render the plot

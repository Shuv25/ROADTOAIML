import numpy as np
import cv2

# Open a connection to the webcam (0 is the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    # Apply the Laplacian filter to detect edges
    # Laplacian calculates the second derivative to detect regions of rapid intensity change
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)

    # Apply the Sobel filter in the X direction to detect vertical edges
    # cv2.Sobel parameters: (input image, data type, dx, dy, kernel size)
    soblex = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)

    # Apply the Sobel filter in the Y direction to detect horizontal edges
    sobley = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    # Apply the Canny edge detection algorithm
    # Canny uses gradients and thresholds to detect edges
    # Parameters: (input image, lower threshold, upper threshold)
    edges = cv2.Canny(frame, 100, 100)

    # Display the original frame
    cv2.imshow('frame', frame)

    # Display the Laplacian filter result (second-order derivative edges)
    cv2.imshow('lappacian', laplacian)

    # Display the Sobel filter result for vertical edges (X direction)
    cv2.imshow('soblex', soblex)

    # Display the Sobel filter result for horizontal edges (Y direction)
    cv2.imshow('sobley', sobley)

    # Display the result of the Canny edge detection algorithm
    cv2.imshow('edges', edges)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

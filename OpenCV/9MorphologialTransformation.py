import numpy as np
import cv2

# Open a connection to the webcam (0 is the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the color range (red in this case)
    lower = np.array([170, 120, 70])  # Lower HSV bounds for red
    higher = np.array([180, 255, 255])  # Upper HSV bounds for red

    # Create a mask to detect pixels within the specified color range
    mask = cv2.inRange(hsv, lower, higher)

    # Apply the mask to the original frame to extract the detected color region
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Define a kernel (a matrix used for morphological operations)
    kernel = np.ones((5, 5), np.uint8)

    # Perform erosion to remove noise (shrinks the white regions in the mask)
    erosion = cv2.erode(mask, kernel, iterations=1)

    # Perform dilation to fill gaps (expands the white regions in the mask)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    # Perform morphological opening (erosion followed by dilation)
    # Useful for removing small noise from the foreground
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Perform morphological closing (dilation followed by erosion)
    # Useful for closing small holes in the foreground
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Display the original frame
    cv2.imshow('frame', frame)

    # Display the result of applying the mask (detected color regions)
    cv2.imshow('res', res)

    # Display the result of morphological opening
    cv2.imshow('opening', opening)

    # Display the result of morphological closing
    cv2.imshow('closing', closing)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

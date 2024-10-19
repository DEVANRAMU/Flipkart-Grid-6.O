import cv2
import numpy as np

# Open the default camera (index 0)
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error capturing frame. Exiting.")
        break

    # Save the captured frame to a file
    cv2.imwrite('image.jpg', frame)

    # Display the captured frame (optional)
    cv2.imshow('Frame', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
cap.release()
cv2.destroyAllWindows()

# Now, process the saved image
# Read the captured image
image = cv2.imread('image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to segment out the text
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Optional: Display the thresholded image
cv2.imshow('Thresholded Image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
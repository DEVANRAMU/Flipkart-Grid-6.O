import cv2
import numpy as np
import easyocr
import sys
sys.stdout.encoding = 'utf-8'





# Initialize the camera
cap = cv2.VideoCapture(0)

# Create an EasyOCR reader
reader = easyocr.Reader(['en'])  # Specify the language as English

while True:
    # Capture a frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error capturing frame. Exiting.")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to segment out the text
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Use EasyOCR to extract text from the thresholded image
    result = reader.readtext(thresh)

    # Extract the text from the result
    text = ''
    for (bbox, text, prob) in result:
        text += text + ' '

    # Display the extracted text on the original frame
    cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the output
    cv2.imshow('Frame', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
cap.release()
cv2.destroyAllWindows()
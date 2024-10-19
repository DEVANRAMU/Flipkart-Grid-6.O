import cv2

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
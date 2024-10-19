import pytesseract
import cv2

# Explicitly set the path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Devan\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Load the image using OpenCV
filename = r"R:\Images for flipkart\Clincitop Gel Exp Date.jpg"
image = cv2.imread(filename)

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Denoise the image
    denoised = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply adaptive thresholding
    adaptive_thresh = cv2.adaptiveThreshold(denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                            cv2.THRESH_BINARY, 11, 2)

    # Use morphological operations to enhance text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    morph = cv2.morphologyEx(adaptive_thresh, cv2.MORPH_CLOSE, kernel)

    # Directly pass the adaptively processed image to Tesseract
    custom_config = r'--oem 3 --psm 6'  # Page Segmentation Mode suited for this type of image
    text = pytesseract.image_to_string(morph, config=custom_config)

    print("Extracted Text: ", text)

import cv2
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Devan\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Load image from file
image = cv2.imread(r"R:\Images for flipkart\Clincitop Gel Exp Date.jpg")

# Preprocess image (convert to grayscale, thresholding, etc.)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Apply thresholding
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Use pytesseract to do OCR on the processed image
custom_config = r'--oem 3 --psm 6'
details = pytesseract.image_to_string(thresh, config=custom_config)

# Print extracted text
print(details)

# For structured output
details_dict = pytesseract.image_to_data(thresh, output_type=Output.DICT)
for i in range(len(details_dict['text'])):
    if int(details_dict['conf'][i]) > 60:  # Confidence level threshold
        print(f"Text: {details_dict['text'][i]} - Conf: {details_dict['conf'][i]}")

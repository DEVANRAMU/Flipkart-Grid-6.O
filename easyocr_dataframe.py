import easyocr
import cv2
import pandas as pd
import glob

# Initialize EasyOCR reader for Hindi and English
reader = easyocr.Reader(['hi', 'en'], gpu=False)  # Hindi and English

# Read and process a single image
def process_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not open or find the image at {image_path}.")
        return
    
    results = reader.readtext(img, detail=1, paragraph=False)

    for (bbox, text, prob) in results:
        (tl, tr, br, bl) = bbox
        tl = (int(tl[0]), int(tl[1]))
        br = (int(br[0]), int(br[1]))

        # Clean the text
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()

        # Draw bounding box and text
        cv2.rectangle(img, tl, br, (0, 255, 0), 2)
        cv2.putText(img, text, (tl[0], tl[1] - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Show the output image
    cv2.imshow("Processed Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Process a specific image
process_image('images/SBI.jpg')

# Read multiple images from a directory and capture results in a DataFrame
path = "images/english/*.*"
df = pd.DataFrame()

for file in glob.glob(path):
    print(f"Processing file: {file}")
    img = cv2.imread(file)
    if img is None:
        print(f"Error: Could not open or find the image at {file}.")
        continue

    results = reader.readtext(img, detail=0, paragraph=True)
    if results:
        df = df.append({'image': file, 'detected_text': results[0]}, ignore_index=True)

# Print the DataFrame to verify results
print(df)

Using the OV7670 camera module connected to an Arduino Uno board, the system captures product images and applies machine learning algorithms to detect the brand and type of the product.

The image detection process is enhanced with Optical Character Recognition (OCR) tools like EasyOCR, PaddleOCR, and Pytesseract for text extraction from product labels.

OCR and ML Integration: 
Text detection is carried out using OCR techniques through Pytesseract. The machine learning model, trained on a dataset created with Roboflow and Google Teachable Machine, is used to classify the products based on the extracted text and image features.

Roboflow Integration:
Roboflow is utilized to label and annotate product images, creating a robust dataset for training. This dataset is then used to fine-tune machine learning models for better accuracy in detecting product types and brands.

Google Teachable Machine:
Google Teachable Machine is employed to create, train, and test the ML model. The user uploads labeled images to the platform, and it automatically trains the model for classification tasks.

Please note that each program requires a certain package to be installed prior to the execution.

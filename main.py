import pytesseract
import pandas
from PIL import Image

IMAGE_FOLDER = "images"

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def image_to_text(IMG_PATH) :
    img = Image.open(IMG_PATH)
    text = pytesseract.image_to_string(img)
    print(text)

print(image_to_text('images/tester/Screenshot 2024-03-08 143455.png'))
# print(image_to_text('images/tester/Screenshot 2024-03-08 143513.png'))
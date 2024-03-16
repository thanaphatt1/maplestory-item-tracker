import pytesseract
import pandas
from PIL import Image
import re

IMAGE_FOLDER = "images"

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

item_attributes = {
    "name": "",
    "description": "",
    "type": "",
    "rarity": "",
    "level": 0,
    "value": 0
}

def image_to_text(IMG_PATH) :
    img = Image.open(IMG_PATH)
    text = pytesseract.image_to_string(img)
    return text

def check_type(text) :
    type_pattern = r"Type:\s*(\w+)"

    # Search for the "Type" attribute in the extracted text
    match = re.search(type_pattern, text)

    # Check if the "Type" attribute is found
    if match:
        item_type = match.group(1)
        print("Item Type:", item_type)
        return item_type
    else:
        print("Item Type not found.")

# def extract_potential(text) :

#     return None

extracted_text = image_to_text('images\character1\Screenshot 2024-03-08 143622.png')
print(extracted_text)
print(type(extracted_text))
print(check_type(extracted_text))                     

# print(image_to_text('images\character1\Screenshot 2024-03-08 143622.png'))
# print(image_to_text('images/tester/Screenshot 2024-03-08 143513.png'))
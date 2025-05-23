import pytesseract
import requests
from PIL import Image
from io import BytesIO

def extract_text_from_image(image_url):
    try:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        return pytesseract.image_to_string(img)
    except:
        return "Failed to extract text from image."

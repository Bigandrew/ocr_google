import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

image = Image.open('C:/Users/yinghe/pyworkspace/ocr/0912/2sjs.jpg')
code = pytesseract.image_to_string(image)
print(code)
#coding:utf-8
import random
import os
from PIL import Image
import re
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

def get_name_image():
    """
    获取图片和图片名字
    :return:
    """
    all_image = os.listdir('C:/Users/yinghe/pyworkspace/ocr/0912/')
    random_f = random.randint(0, 649)
    base = os.path.basename('C:/Users/yinghe/pyworkspace/ocr/0912/' + all_image[random_f])
    name = os.path.splitext(base)[0]
    image = Image.open('C:/Users/yinghe/pyworkspace/ocr/0912/' + all_image[random_f])
    return name, image


def image_data_to_tiff(image):

    img = image.convert('RGBA')
    img = binarize_image(img)
    img = img.convert('L')
    return img

def binarize_image(img):
    pixdata = img.load()
    # print(img.size[1])
    # print(img.size[0])
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x,y][0] < 132 or pixdata[x,y][1] < 40 or  pixdata[x,y][2] < 100:
                pixdata[x,y] = (0,0,0,255)
            else:
                pixdata[x,y] = (255,255,255,255)
    return img

def image_to_text(img):
    return tesseract(img)

def tesseract(img):
    text = pytesseract.image_to_string(img)
    text = re.sub('[\W]', '', text)
    print text
    return text

def crack_captcha():
    n = 1
    while n<=100:
        name, image = get_name_image()
        image = image_data_to_tiff(image)
        text1 = image_to_text(image)
        print("right: {} pred: {}".format(name, text1))
        n += 1
crack_captcha()

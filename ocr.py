import numpy as np
from matplotlib import pyplot as plt
import cv2
import imutils
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from pytesseract import Output

def build_tesseract_options(psm=7):
    # tell Tesseract to only OCR alphanumeric characters
    alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.!0123456789"
    options = "-c tessedit_char_whitelist={}".format(alphanumeric)
    # set the PSM mode
    #options += " --psm {}".format(psm)
    # return the built options string
    return options

def get_text(img):

    height, width = img.shape[:2]
    img = cv2.resize(img, (width*3, height*3))

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #cv2.imshow("rgb", rgb)
    #cv2.waitKey(0)

    kernel_sharpening = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])

    sharpened = cv2.filter2D(rgb, -1, kernel_sharpening)

    results = pytesseract.image_to_data(sharpened, output_type=Output.DICT, config='--psm 11')
    texts= ""
    for i in range(0, len(results["text"])):

              if results["text"][i]!="":
                  print(results["text"][i])
                  texts= texts+results["text"][i]
    if texts == "":
        return "Not able to detect Number..."

    return texts

#image = cv2.imread("pic12.JPG")
#text= get_text(image)
#print(text,'text')

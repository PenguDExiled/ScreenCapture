import numpy as nm
import pytesseract
from PIL import ImageGrab
import cv2
import time

"""
Text recognition in a certain area to read the augments
"""

def imageToString():
    print('reading augments...')
    counter = 0
    compare1 = []
    compare2 = []
    compare3 = []
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    while True:
        time.sleep(0.1)

        box1 = ImageGrab.grab(bbox=(426,573,665,610),
                             all_screens=True)

        box2 = ImageGrab.grab(bbox=(826,573,1065,610),
                             all_screens=True)

        box3 = ImageGrab.grab(bbox=(1226, 573, 1465, 610),
                              all_screens=True)
        # 400 532 1st 665 631
        # 800 532 1st 1092 631
        # 1200 532 1st 1510 631

        augment1 = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(box1), cv2.COLOR_BGR2GRAY),
            lang='eng')
        augstr1 = str(augment1).strip()
        compare1.append(augstr1)


        augment2 = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(box2), cv2.COLOR_BGR2GRAY),
            lang='eng')
        augstr2 = str(augment2).strip()
        compare2.append(augstr2)

        augment3 = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(box3), cv2.COLOR_BGR2GRAY),
            lang='eng')
        augstr3 = str(augment3).strip()
        compare3.append(augstr3)

        counter = counter + 1
        if counter >= 20:
            break
    return max(set(compare1), key=compare1.count), max(set(compare2), key=compare2.count), max(set(compare3), key=compare3.count)

print(imageToString())
import asyncio
import PIL.ImageChops
from PIL import ImageChops
import numpy as np
import PIL.Image
import PIL.ImageEnhance
import PIL.ImageFilter
import PIL.ImageGrab
from PIL import Image, ImageEnhance, ImageFilter, ImageGrab
import ScreenPosition
import cv2
from pynput.mouse import Button, Controller
import time

# define box for screenshot
def getImage(posx1, posy1, posx2, posy2):
    x = 0
    y = 0
    w = 0
    h = 0
    streamhost = ' '
    mouse = Controller()
    position_append = asyncio.run(ScreenPosition.getPosition(2, posx1, posy1, posx2, posy2))
    time.sleep(0.5)
    # screen grab
    screen = ImageGrab.grab(bbox=(position_append[0],position_append[1],position_append[2],position_append[3]), all_screens=True)


    # save picture

    screen.save('grabbed.png')

    img = cv2.imread("grabbed.png")

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_range_streamtape = np.array([122, 100, 100])  # lower and upper range for streamtape icon
    upper_range_streamtape = np.array([133, 255, 255])

    mask = cv2.inRange(hsv, lower_range_streamtape, upper_range_streamtape)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 18: #check if contours
        for contour in contours:
            if cv2.contourArea(contour) > 2:  #check if many contours
                streamhost = 'streamtape'
                x, y, w, h = cv2.boundingRect(contour) #create rectangle
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 3)
    else:
        lower_range_dood = np.array([15, 100, 100])  # lower and upper range for Doodstream icon
        upper_range_dood = np.array([35, 255, 255])
        mask = cv2.inRange(hsv, lower_range_dood, upper_range_dood)
        streamhost = 'doodstream'
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 100:  # check if many contours
                    x, y, w, h = cv2.boundingRect(contour)  # create rectangle
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

    #cv2.imshow("mask", mask)
    #cv2.imshow("source", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows

    return(x+position_append[0],y+position_append[1], streamhost)
#getImage(-1421,984,-535,1024)

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller
import ScreenPosition
import pywintypes
import win32clipboard
import time
import getClipboard
import colorDetection
import setScreenPosition
import makeMousemovement
from PIL import Image, ImageEnhance, ImageFilter, ImageGrab
import PIL.ImageChops
import numpy as np
import cv2
import tkinter as tk
from tkinter import  filedialog, Text
import os
import asyncio

def main():
    root = tk.Tk()
    apps = []

    if os.path.isfile('save.txt'):
        with open('save.txt', 'r') as f:
            tempPos = f.read()
            tempPos = tempPos.split(',')
            apps = [x for x in tempPos if x.strip()]

    def b_urlLeiste():
        for widget in frame.winfo_children():
            widget.destroy()
        url_location = setScreenPosition.set_position()
        tmp1 = url_location[0]
        tmp2 = url_location[1]
        apps.append(tmp1)
        apps.append(tmp2)
        print(url_location)
        for app in apps:
            label = tk.Label(frame, text=app, bg='gray')
            label.pack()

    def b_run():
        openStream(apps[0], apps[1],apps[2],apps[3],apps[4],apps[5])

    def b_hosts():
        for widget in frame.winfo_children():
            widget.destroy()
        for x in range(0,2):
            time.sleep(0.1)
            url_location = setScreenPosition.set_position()
            tmp1 = url_location[0]
            tmp2 = url_location[1]
            apps.append(tmp1)
            apps.append(tmp2)
            print(url_location)
        for app in apps:
            label = tk.Label(frame, text=app, bg='gray')
            label.pack()

    def b_closestream():
        closeStream()


    canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
    canvas.pack()

    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    openFile = tk.Button(root, text="Url Leiste markieren", padx=10,
                         pady=5, fg="white", bg="#263D42", command=b_urlLeiste)
    openFile.pack()

    hosts = tk.Button(root, text="Hosts markieren", padx=10,
                         pady=5, fg="white", bg="#263D42", command=b_hosts)
    hosts.pack()

    run = tk.Button(root, text="Open Stream", padx=10, pady=5, fg="white", bg="#263D42", command=b_run)

    run.pack()

    close = tk.Button(root, text="Close Stream", padx=10, pady=5, fg="white", bg="#263D42", command=b_closestream)

    close.pack()

    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()

    root.mainloop()



    with open('save.txt', 'w') as f:
        for app in apps:
            f.write(str(app) + ',')


def openStream(url_posx, url_posy, posx1, posy1, posx2, posy2):
    mouse = Controller()
    keyboard = KeyboardController()

    mouse.position = (url_posx, url_posy)
    time.sleep(0.1)
    for x in range(0,3):
        mouse.press(Button.left)
        mouse.release(Button.left)
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)
    time.sleep(0.1)
    clip = str(getClipboard.clipboard())
    indexmin = clip.find("/",32)
    indexmax = clip.find("-", indexmin)
    url_substring = clip[indexmin+1:indexmax]
    url_intstring = int(url_substring) + 1
    url_final = clip.replace(url_substring, str(url_intstring))
    keyboard.type(url_final)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    result = (colorDetection.getImage(posx1, posy1, posx2, posy2))
    mouse.position = result[0], result[1]
    streamhost = result[2]
    print(streamhost)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.5)
    mouse.scroll(0, -1)
    time.sleep(0.1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(5)
    if (streamhost == 'streamtape'):
        mouse.click(Button.left, 3)
        time.sleep(1)
        #mouse.click(Button.left,2)
    elif (streamhost == 'doodstream'):
        mouse.move(0,-500)
        time.sleep(0.2)
        mouse.press(Button.left)
        mouse.release(Button.left)

        time.sleep(0.5)
        mouse.click(Button.left, 2)

def closeStream():
    time.sleep(1)
    keyboard = KeyboardController()
    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)
if __name__ == '__main__':
    main()
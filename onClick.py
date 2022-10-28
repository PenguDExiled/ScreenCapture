from pynput import mouse
from pynput.mouse import Button, Controller
import time


def getPosition(y):
    mouse = Controller()
    time.sleep(1)
    mouse_position = []
    for x in range(0, y):
        print("Position:", x + 1)
        time.sleep(1)
        mouse_position.append(mouse.position)
    for x in mouse_position:
        print(x[0:2])


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False


def getPosition2(y):
    mou = Controller()
    time.sleep(1)
    mouse_position = []
    for x in range(0, y):
        print("Position:", x + 1)
        time.sleep(2)
        listener = mouse.Listener(
            on_click=on_click)
        listener.start()



getPosition2(2)



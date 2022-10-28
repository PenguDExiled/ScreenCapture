from pynput import mouse
import time


def set_position():
    with mouse.Events() as events:
        for event in events:
            if type(event) == mouse.Events.Move or type(event) == mouse.Events.Scroll:
                continue
            if event.button == mouse.Button.left:
                print(str(event.x) + ' ' + str(event.y))
                break
        return event.x, event.y
from pynput.mouse import Button, Controller
import time
import asyncio
async def mouse_movement(posx1, posy1, posx2, posy2):
    mouse = Controller()

    mouse.position = (posx1, posy1)
    await asyncio.sleep(1.5)
    mouse.position = (posx2, posy2)
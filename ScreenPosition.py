from pynput.mouse import Button, Controller
import time
import asyncio
import makeMousemovement

async def getPosition(y, posx1, posy1, posx2, posy2):
    task = asyncio.create_task(makeMousemovement.mouse_movement(posx1, posy1, posx2, posy2))
    mouse = Controller()
    position_append = ()
    for x in range(0, y):
        print("Position:", x+1)
        await asyncio.sleep(1)
        position_append = position_append + mouse.position
        await task
    for x in range(len(position_append)):
        print(position_append[x])
    return position_append

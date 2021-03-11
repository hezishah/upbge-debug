import bge
from bge import logic as GameLogic
import time
import timeit

# active scene cube
scene = bge.logic.getCurrentScene()
# the object "Cube"
cube = scene.objects["Cube"]
keyboard = bge.logic.keyboard

LOOP = True
FPS = 60  # Frames per Second
last_time = timeit.default_timer()

bge.logic.setExitKey(bge.events.LEFTARROWKEY)
first = True
while LOOP:
    if first:
        breakpoint()
        first = False
    # mainloop
    # wait until next frame
    current_time = timeit.default_timer()
    # sleep time until next frame
    sleep_time = 1 / FPS - (current_time - last_time)
    if sleep_time > 0:
        time.sleep(sleep_time)
    last_time = current_time

    # change scene
    # read keyboard input
    k_events = bge.logic.KX_INPUT_ACTIVE
    # uparrow key pressed
    if keyboard.events[bge.events.UPARROWKEY] == k_events:
        cube.applyMovement([0.,0.,.5])
        #cube.playAction("ActionRotation", 1, 30)
        #cube.playAction("ActionScale", 1, 30)
    # downarrow key pressed
    if keyboard.events[bge.events.DOWNARROWKEY] == k_events:
        cube.applyMovement([0.,0.,-.5])
        #cube.playAction("ActionScale", 30, 1)
        #cube.playAction("ActionRotation", 30, 1)
    # escape key pressed
    if keyboard.events[bge.events.ESCKEY] == k_events:
        # Stop mainloop -> exit program
        LOOP = False
    # render next frame
    bge.logic.NextFrame()
    print('f')
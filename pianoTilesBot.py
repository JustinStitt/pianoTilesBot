#use pynput for mouse + keyboard
#use pyautogui + numpy for pixel color detection
#http://tanksw.com/piano-tiles/
from pynput.keyboard import Key, Controller as kController, Listener
from pynput.mouse import Button, Controller as mController
import pyautogui
import numpy as np
import time, sys
run = True
#piano tiles start x,y = (785,396) end x,y = (1155,879) size = 400x600
window_size = (395,595)
start_pos = (754,280)
bbox = (start_pos[0],start_pos[1],window_size[0],window_size[1])
mouse = mController()
black = (17,17,17)
sample_points = []
to_click = []

def check_boxes():
    global bottom_boxes, grab
    for x in range(len(sample_points) - 1,-1,-1):
        if(pyautogui.pixelMatchesColor(sample_points[x][0], sample_points[x][1], black, tolerance=5)):
            to_click.append(x)
            return
def activate_clicks():
    if(len(to_click) < 1):
        return
    index = to_click[0]
    pyautogui.click((sample_points[index][0],sample_points[index][1]))
    to_click.pop(0)
def populate_sample_points():
    global sample_points
    for r in range(4):
        for c in range(4):
            coords = (50 +(c * 100), 1 + (r * 150))
            sample_points.append(coords)
    for x in range(len(sample_points)):
        sample_points[x] = (sample_points[x][0] + start_pos[0], sample_points[x][1] + start_pos[1])
def update():
    global grab, run
    mpos = pyautogui.position()
    if(mpos == (0,0)):
        run = False
    if(bbox == None):
        print("assign bbox (x1,y1,w,h)")
        return

populate_sample_points()
time.sleep(2)

while run == True:
    update()
    check_boxes()
    activate_clicks()

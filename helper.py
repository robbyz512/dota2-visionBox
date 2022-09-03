import os
from tkinter import *
from tkinter import messagebox
import traceback

posX = None
posY = None
width = None
height = None
notVisibleColor = None
visibleColor = None
address = None
offsets = []
speed = None
threshold = None

if not os.path.exists('settings.txt'):
    root = Tk()
    root.withdraw()
    messagebox.showinfo("visionBox", "settings.txt not found, extract it to where visionBox.exe is")

with open('settings.txt') as file:
    
    lines = file.readlines()

    for line in lines:
        if line.startswith('#') or line.isspace():
            continue
        else:
            try:
                line = line.strip().split('=')
                if line[0] == 'posX': posX = line[1]
                if line[0] == 'posY': posY = line[1]
                if line[0] == 'width': width = int(line[1])
                if line[0] == 'height': height = int(line[1])
                if line[0] == 'notVisibleColor': notVisibleColor = line[1]
                if line[0] == 'visibleColor': visibleColor = line[1]
                if line[0] == 'address': address = int(line[1], 16)
                if line[0] == 'offsets':
                    offs = line[1].split(" ")
                    for i in offs:
                        i = int(i, 16)
                        offsets.append(i)
                if line[0] == 'speed': 
                    f_val = float(line[1])
                    if f_val < 0.01:
                        f_val = 0.01
                    speed = f_val
                if line[0] == 'threshold': threshold = int(line[1])
            except Exception:
                with open('log.txt', 'w+') as file:
                    file.write(traceback.format_exc())
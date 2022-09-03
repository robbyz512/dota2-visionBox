import time
import threading
import traceback
import pymeow as pym
import tkinter as tk
from itertools import groupby

import helper

process = None
base_address = None

def read_offsets(process, base_address, offsets):
    base_pointer = pym.read_int64(process, base_address)
    current_pointer = base_pointer

    for offset in offsets[:-1]:
        current_pointer = pym.read_int64(process, current_pointer + offset)
    return current_pointer + offsets[-1]

def get_static_address(process, base_address, offsets):
    static_address = read_offsets(process, base_address, offsets)
    static_address = pym.read_int(process, static_address)
    return static_address

class App():
    # ------------------------------------ gui ----------------------------------- #
    def __init__(self):
        self.root = tk.Tk()
        self.root.protocol('WM_DELETE_WINDOW', self.exit)
        self.root.overrideredirect(True)
        self.root.attributes('-topmost', True)
        self.root.bind('<Button-1>', self.SaveLastClickPos)
        self.root.bind('<B1-Motion>', self.Dragging)
        self.root.bind('<ButtonRelease-1>', self.Release)
        self.root.bind('<Double-Button-1>', self.RightClick)
        self.setupGUI()

        threading.Thread(target=self.manageProcess, daemon=True).start()
        threading.Thread(target=self.Visualizer, daemon=True).start()

        self.root.mainloop()

    def exit(self):
        self.root.destroy()

    def setupGUI(self):
        self.root.resizable(False, False)
        self.root.app_width = helper.width
        self.root.app_height = helper.height
        self.root.x = helper.posX
        self.root.y = helper.posY   
        self.root.geometry(f'{self.root.app_width}x{self.root.app_height}+{int(self.root.x)}+{int(self.root.y)}')
        self.label = tk.Label(self.root)
        self.root.configure(bg="orange")
    # ---------------------------------- events ---------------------------------- #
    def SaveLastClickPos(self, event):
        global lastClickX, lastClickY
        lastClickX = event.x
        lastClickY = event.y

    def Dragging(self, event):
        x, y = event.x - lastClickX + self.root.winfo_x(), event.y - lastClickY + self.root.winfo_y()
        self.root.geometry("+%s+%s" % (x , y))
        self.label.configure(text="posX: {} posY: {}".format(self.root.winfo_x(),self. root.winfo_y()))
        self.label.pack(anchor='center', expand=True)

    def Release(self, event):
        self.label.pack_forget()

    def RightClick(self, event):
        self.root.destroy()

    # ------------------------------------ app ----------------------------------- #
    def all_equal(self, iterable):
        g = groupby(iterable)
        return next(g, True) and not next(g, False)

    def manageProcess(self):
        global process, base_address

        while True:
            try:
                process = pym.process_by_name("dota2.exe")

                if process != None:
                    base_address = process["modules"]["engine2.dll"]["baseaddr"] + helper.address

            except Exception:
                base_address = None
                self.root.configure(bg="orange")

            time.sleep(1.5)

    def Visualizer(self):
        count = 0
        duplicates = []
        while True:
            try:
                addr = get_static_address(process, base_address, helper.offsets)
                duplicates.append(addr)

                if addr == 0:   
                    count += 1
                    if count >= 10:
                        count = 0
                        duplicates = []
                        self.root.configure(background=helper.visibleColor)
                elif addr != 0 and self.all_equal(duplicates[-5:]):
                    count = 0
                    self.root.configure(background=helper.visibleColor)
                else:
                    count = 0
                    self.root.configure(background=helper.notVisibleColor)
            except Exception:
                pass

            time.sleep(helper.speed)

if __name__ == '__main__':
    try:
        app = App()
    except Exception:
        with open('log.txt', 'w+') as file:
            file.write(traceback.format_exc())
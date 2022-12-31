import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#yoffset = 31 # titlebar
yoffset = 0 # titlebar
xoffset = 1

i_buttonx = 0
i_buttonwidth = 33
i_buttonheight = 50

btnLights = [None]*6

window = tk.Tk()


class btnProperties:
    def __init__(self, x=0, y=0 ):
        self._x = x
        self._y = y

    # getter method
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y

    # setter method
    def set_x(self, x):
        self._x = x
    
    def set_y(self, x):
        self._y = x


btnLocations = []
for i in range(0,6):
    btnLocations.append(btnProperties())
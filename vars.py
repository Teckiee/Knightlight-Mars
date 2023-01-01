#import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#yoffset = 31 # titlebar
yoffset = 0 # titlebar
xoffset = 1

#i_buttonx = 0
i_parcanwidth = 33
i_parcanheight = 50

i_fresnelwidth = 50
i_fresnelheight = 50

btnLights = []

bgcolor = "#434343"

window = Tk()


image = Image.open('parcan.png')
img=image.resize((i_parcanwidth, i_parcanheight))
img_parcan = ImageTk.PhotoImage(img)

image2 = Image.open('fresnel.png')
img2=image2.resize((i_fresnelwidth, i_fresnelheight))
img_fresnel = ImageTk.PhotoImage(img2)

class btnProperties:
    btnTheLight = Button
    def __init__(self, x=0, y=0, z='', *args, **kwargs ):
        #__init__(self, *args, **kwargs)
        self._x = x
        self._y = y
        self._lighttype = z

    # getter method
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y

    def get_type(self):
        return self._lighttype

    def get_btn(self):
        return self.Button

    # setter method
    def set_x(self, x):
        self._x = x
    
    def set_y(self, x):
        self._y = x

    def set_btn(self, x):
        self.Button = x
    
    def set_type(self, x):
        self._lighttype = x


#btnLocations = []
#for i in range(0,6):
#    btnLocations.append(btnProperties())
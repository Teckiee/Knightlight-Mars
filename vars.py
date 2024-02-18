#import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import platform
from tkinter import font as tkFont  # for convenience
import serial

#yoffset = 31 # titlebar
yoffset = 0 # titlebar
xoffset = 1


# print(platform.system())

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

w0, h0 = 1024, 600
w1, h1 = 1024, 600
w2, h2 = 900, 1600

win2 = Tk()
win0 = Tk()
#win1 = Tk()

#i_buttonx = 0
i_parcanwidth = 33
i_parcanheight = 50

i_fresnelwidth = 50
i_fresnelheight = 50

i_wedgewidth = 50
i_wedgeheight = 32

i_washmovingheadwidth = 39
i_washmovingheadheight = 50

i_mirrorballwidth = 50
i_mirrorballheight = 50

i_ledsinglefloorwidth = 50
i_ledsinglefloorheight = 50

i_ledparcanwidth = 50
i_ledparcanheight = 50

i_profilewidth = 50
i_profileheight = 50

i_intimidatorwidth = 50
i_intimidatorheight = 50

i_ledpanelwidth = 50
i_ledpanelheight = 50

i_floorplanwidth = 900
i_floorplanheight = 1438

#parcan
#fresnel
#wedge
#washmovinghead
#mirrorball
#ledsinglefloor
#ledparcan
#profile

received_data = None

btnLights = []
cMusicPlayers = []

bgcolor = "#434343"

buttonlocationslocked = 1



i_btnlocationoffsetx = 0
i_btnlocationoffsety = 160


i_addbuttonoffsetx = 0

btnfont = tkFont.Font (family='Segoe UI', size=9)

if platform.system() == 'Linux':
    i_addbuttonoffsetx = 2
    i_btnlocationoffsetx = 10
    btnfont = tkFont.Font(family='Segoe UI', size=8)


imageparcan = Image.open('parcan.png')
imgparcan=imageparcan.resize((i_parcanwidth, i_parcanheight))
img_parcan = ImageTk.PhotoImage(imgparcan)

imagefresnel = Image.open('fresnel.png')
imgresnel=imagefresnel.resize((i_fresnelwidth, i_fresnelheight))
img_fresnel = ImageTk.PhotoImage(imgresnel)

imageledparcan = Image.open('ledparcan.png')
imgledparcan=imageledparcan.resize((i_ledparcanwidth, i_ledparcanheight))
img_ledparcan = ImageTk.PhotoImage(imgledparcan)

imageledsinglefloor = Image.open('ledsinglefloor.png')
imgledsinglefloor=imageledsinglefloor.resize((i_ledsinglefloorwidth, i_ledsinglefloorheight))
img_ledsinglefloor = ImageTk.PhotoImage(imgledsinglefloor)

imagemirrorball = Image.open('mirrorball.png')
imgmirrorball=imagemirrorball.resize((i_mirrorballwidth, i_mirrorballheight))
img_mirrorball = ImageTk.PhotoImage(imgmirrorball)

imageprofile = Image.open('profile.png')
imgprofile=imageprofile.resize((i_profilewidth, i_profileheight))
img_profile = ImageTk.PhotoImage(imgprofile)

imageintimidator = Image.open('intimidator.png')
imgintimidator=imageintimidator.resize((i_intimidatorwidth, i_intimidatorheight))
img_intimidator = ImageTk.PhotoImage(imgintimidator)

imagewashmovinghead = Image.open('washmovinghead.png')
imgwashmovinghead=imagewashmovinghead.resize((i_washmovingheadwidth, i_washmovingheadheight))
img_washmovinghead = ImageTk.PhotoImage(imgwashmovinghead)

imagewedge = Image.open('wedge.png')
imgwedge=imagewedge.resize((i_wedgewidth, i_wedgeheight))
img_wedge = ImageTk.PhotoImage(imgwedge)

imageledpanel = Image.open('ledpanel.png')
imgledpanel=imageledpanel.resize((i_ledpanelwidth, i_ledpanelheight))
img_ledpanel = ImageTk.PhotoImage(imgledpanel)

imagefloorplan = Image.open('PAT.png')
imgfloorplan=imagefloorplan.resize((i_floorplanwidth, i_floorplanheight))
img_floorplan = ImageTk.PhotoImage(imgfloorplan)


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

class cMusicPlayer:
    btnCue = Button
    btnPlayPause = Button
    btnStop = Button
    lblSongName = Label
    def __init__(self, x=0, y=0, z=-1, *args, **kwargs ):
        #__init__(self, *args, **kwargs)
        self._x = x
        self._y = y
        self._MusicCueIndex = z

    # getter method
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y

    def get_musiccueindex(self):
        return self._MusicCueIndex

    # setter method
    def set_x(self, x):
        self._x = x
    
    def set_y(self, x):
        self._y = x
    
    def set_musiccueindex(self, x):
        self._MusicCueIndex = x

#btnLocations = []
#for i in range(0,6):
#    btnLocations.append(btnProperties())
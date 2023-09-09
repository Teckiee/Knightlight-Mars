#import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import keyboard
from btnevents import *
from vars import *

##########################################################
#
#					Win2/Main = RIGHT 12"
#
##########################################################

wx = w2
wy = h2

frame1 = tk.Frame(master=window, width=wx, height=wy, bg=bgcolor)

frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

#win0.geometry(f"{w0}x{h0}+0+0")
#win1.geometry(f"{w1}x{h1}+0+{h0}")
window.geometry(f"{w2}x{h2}+{w0}+0")

# Remove the Title bar of the window
#w0.overrideredirect(True)
#w1.overrideredirect(True)
window.overrideredirect(True)

label = tk.Label(
image = img_floorplan,
master=frame1,
width=i_floorplanwidth,
height=i_floorplanheight,
)
label.place(relx = 0,
rely = 0,
anchor = 'nw')

#img_label = Label(image=img_parcan)

loadlocations()

#loadlocationsloadtest()


btnexit = tk.Button(
master=frame1,
text='Quit',
bg=bgcolor,
fg="black",
width=10-i_addbuttonoffsetx,
height=4,
font=btnfont
)
btnexit.bind("<Button-1>", quitme)
btnexit.place(x=810-i_btnlocationoffsetx, y=8)

btnsave = tk.Button(
master=frame1,
text='Save',
bg=bgcolor,
fg="black",
width=10-i_addbuttonoffsetx,
height=4,
font=btnfont
)
btnsave.bind("<Button-1>", savelocations)
btnsave.place(x=810-i_btnlocationoffsetx, y=wy-i_btnlocationoffsety)

btnaddparcan = tk.Button(
master=frame1,
text='Add Parcan',
bg='black',
fg="white",
width=10-i_addbuttonoffsetx,
height=4,
font=btnfont
)
btnaddparcan.bind("<Button-1>", clickbtnaddparcan)
btnaddparcan.place(x=20, y=wy-i_btnlocationoffsety)

btnaddfresnel = tk.Button(
master=frame1,
text='Add Fresnel',
bg='black',
fg="white",
width=10-i_addbuttonoffsetx,
height=4,
font=btnfont
)
btnaddfresnel.bind("<Button-1>", clickbtnaddfresnel)
btnaddfresnel.place(x=100, y=wy-i_btnlocationoffsety)

btnaddwedge = tk.Button(
master=frame1,
text='Add wedge',
bg='black',
fg="white",
width=10-i_addbuttonoffsetx,
height=4,
font=btnfont
)
btnaddwedge.bind("<Button-1>", clickbtnaddwedge)
btnaddwedge.place(x=180, y=wy-i_btnlocationoffsety)

btnaddwashmovinghead = tk.Button(
master=frame1,
text='Add wash moving head',
wraplength=80,
bg='black',
fg="white",
width=10-i_addbuttonoffsetx,
height=4,
font=btnfont
)
btnaddwashmovinghead.bind("<Button-1>", clickbtnaddwashmovinghead)
btnaddwashmovinghead.place(x=260, y=wy-i_btnlocationoffsety)

btnaddmirrorball = tk.Button(
master=frame1,
text='Add mirrorball',
wraplength=80,
bg='black',
fg="white",
width=10-i_addbuttonoffsetx,
height=4,
font=btnfont
)
btnaddmirrorball.bind("<Button-1>", clickbtnaddmirrorball)
btnaddmirrorball.place(x=340, y=wy-i_btnlocationoffsety)

btnaddledsinglefloor = tk.Button(
master=frame1,
text='Add led single floor',
wraplength=80,
bg='black',
fg="white",
width=10-i_addbuttonoffsetx,
height=4,
font=btnfont
)
btnaddledsinglefloor.bind("<Button-1>", clickbtnaddledsinglefloor)
btnaddledsinglefloor.place(x=420, y=wy-i_btnlocationoffsety)

btnaddledparcan = tk.Button(
master=frame1,
text='Add led parcan',
wraplength=80,
bg='black',
fg="white",
width=10-i_addbuttonoffsetx,
height=4,
font=btnfont
)
btnaddledparcan.bind("<Button-1>", clickbtnaddledparcan)
btnaddledparcan.place(x=500, y=wy-i_btnlocationoffsety)

btnaddprofile = tk.Button(
master=frame1,
text='Add profile',
wraplength=80,
bg='black',
fg="white",
width=10-i_addbuttonoffsetx,
height=4,
font=btnfont
)
btnaddprofile.bind("<Button-1>", clickbtnaddprofile)
btnaddprofile.place(x=580, y=wy-i_btnlocationoffsety)

btnaddintimidator = tk.Button(
master=frame1,
text='Add Intimidator',
wraplength=72,
bg='black',
fg="white",
width=10-i_addbuttonoffsetx,
height=4,
font=btnfont
)
btnaddintimidator.bind("<Button-1>", clickbtnaddintimidator)
btnaddintimidator.place(x=660, y=wy-i_btnlocationoffsety)

btnaddledpanel = tk.Button(
master=frame1,
text='Add LEDPanel',
wraplength=80,
bg='black',
fg="white",
width=10-i_addbuttonoffsetx,
height=4,
font=btnfont
)
btnaddledpanel.bind("<Button-1>", clickbtnaddledpanel)
btnaddledpanel.place(x=20, y=wy+65-i_btnlocationoffsety)

window.mainloop()


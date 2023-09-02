#import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import keyboard
import threading
from threading import Event

# My libraries and classes
from btnevents import *
from vars import *
from pyreceive import *

# bg = PhotoImage(file = 'PAT.png')

frame1 = tk.Frame(master=window, width=screena_width, height=screena_height, bg=bgcolor)

frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

# Remove the Title bar of the window
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
btnsave.place(x=810-i_btnlocationoffsetx, y=i_floorplanheight + i_btnlocationoffsety)

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
btnaddparcan.place(x=20, y=i_floorplanheight + i_btnlocationoffsety)

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
btnaddfresnel.place(x=100, y=i_floorplanheight + i_btnlocationoffsety)

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
btnaddwedge.place(x=180, y=i_floorplanheight + i_btnlocationoffsety)

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
btnaddwashmovinghead.place(x=260, y=i_floorplanheight + i_btnlocationoffsety)

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
btnaddmirrorball.place(x=340, y=i_floorplanheight + i_btnlocationoffsety)

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
btnaddledsinglefloor.place(x=420, y=i_floorplanheight + i_btnlocationoffsety)

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
btnaddledparcan.place(x=500, y=i_floorplanheight + i_btnlocationoffsety)

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
btnaddprofile.place(x=580, y=i_floorplanheight + i_btnlocationoffsety)

# Create a thread for the serial communication loop
serial_thread = threading.Thread(target=startserial)

# Start the thread
serial_thread.start()



window.mainloop()


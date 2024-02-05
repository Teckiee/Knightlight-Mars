#import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import keyboard
from btnevents import *
from vars import *
import socket
import _thread

##########################################################
#
#					Win2/Main = RIGHT 12"
#
##########################################################

wx = w2
wy = h2


frame0 = tk.Frame(master=win0, width=w0, height=h0, bg=bgcolor)
frame1 = tk.Frame(master=win1, width=w1, height=h1, bg=bgcolor)
frame2 = tk.Frame(master=win2, width=w2, height=w2, bg=bgcolor)

frame0.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

# Proper non-test geometry
#win0.geometry(f"{w0}x{h0}+0+0")
#win1.geometry(f"{w1}x{h1}+0+{h0}")
#win2.geometry(f"{w2}x{h2}+{w0}+0")

# Test only geometry
win0.geometry(f"{w0}x{h0}+0+-1080")
win1.geometry(f"{w1}x{h1}+0+-480")
win2.geometry(f"{w2}x{h2}+{w0}+-1080")

# Remove the Title bar of the window
win0.overrideredirect(True)
win1.overrideredirect(True)
win2.overrideredirect(True)

label = tk.Label(
image = img_floorplan,
master=frame2,
width=i_floorplanwidth,
height=i_floorplanheight,
)
label.place(relx = 0,
rely = 0,
anchor = 'nw')

#img_label = Label(image=img_parcan)

try:
    # https://realpython.com/python-sockets/
   _thread.start_new_thread( start_server )
except:
   print ("Error: unable to start TCP thread")

loadlocations()

addlightbuttons(frame2)

btnexit = tk.Button(
master=frame2,
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
master=frame2,
text='Save',
bg=bgcolor,
fg="black",
width=10-i_addbuttonoffsetx,
height=4,
font=btnfont
)
btnsave.bind("<Button-1>", savelocations)
btnsave.place(x=810-i_btnlocationoffsetx, y=wy-i_btnlocationoffsety)



btnexit2 = tk.Button(
master=frame0,
text='Quit',
bg=bgcolor,
fg="black",
width=10-i_addbuttonoffsetx,
height=4,
font=btnfont
)
btnexit2.bind("<Button-1>", quitme)
btnexit2.place(x=w0-100-i_btnlocationoffsetx, y=8)

btnexit3 = tk.Button(
master=frame1,
text='Quit',
bg=bgcolor,
fg="black",
width=10-i_addbuttonoffsetx,
height=4,
font=btnfont
)
btnexit3.bind("<Button-1>", quitme)
btnexit3.place(x=w1-100-i_btnlocationoffsetx, y=8)

win2.mainloop()

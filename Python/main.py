#import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
#import keyboard
#from vars import *
import vars
from btnevents import *
import socket
import _thread
import serial
import asyncio


##########################################################
#
#					Win2/Main = RIGHT 12"
#
##########################################################

wx = vars.w2
wy = vars.h2


frame0 = tk.Frame(master=vars.win0, width=vars.w0, height=vars.h0, bg=vars.bgcolor)
#frame1 = tk.Frame(master=vars.win1, width=vars.w1, height=vars.h1, bg=vars.bgcolor)
frame2 = tk.Frame(master=vars.win2, width=vars.w2, height=vars.w2, bg=vars.bgcolor)

frame0.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)
#frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

# Proper non-test geometry
vars.win0.geometry(f"{vars.w0}x{vars.h0}+0+0")
#vars.win1.geometry(f"{vars.w1}x{vars.h1}+0+{vars.h0}")
vars.win2.geometry(f"{vars.w2}x{vars.h2}+{vars.w0}+0")

# Test only geometry
#win0.geometry(f"{w0}x{h0}+0+-1080")
#win1.geometry(f"{w1}x{h1}+0+-480")
#win2.geometry(f"{w2}x{h2}+{w0}+-1080")

# Remove the Title bar of the window
vars.win0.overrideredirect(True)
#vars.win1.overrideredirect(True)
vars.win2.overrideredirect(True)

label = tk.Label(
image = vars.img_floorplan,
master=frame2,
width=vars.i_floorplanwidth,
height=vars.i_floorplanheight,
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


start_serial()

#def start_serial_thread():
#    try:
#        start_serial()
#    except Exception as e:
#        print("Error starting serial:", str(e))

#try:
#    _thread.start_new_thread(start_serial_thread, ())
#except Exception as e:
#    print("Error starting threads:", str(e))

vars.win2.bind('<<SerialReceived>>', handle_serial_received)

loadlocations()

addlightbuttons(frame2)

setupmusicplayer(frame0)

#btnexit = tk.Button(
#master=frame2,
#text='Quit',
#bg=vars.bgcolor,
#fg="black",
#width=10-vars.i_addbuttonoffsetx,
#height=4,
#font=vars.btnfont
#)
#btnexit.bind("<Button-1>", quitme)
#btnexit.place(x=810-vars.i_btnlocationoffsetx, y=8)


btnsave = tk.Button(
master=frame2,
text='Save',
bg=vars.bgcolor,
fg="black",
font=vars.btnfont
)
btnsave.bind("<Button-1>", savelocations)
btnsave.place(x=810-vars.i_btnlocationoffsetx, y=wy-vars.i_btnlocationoffsety,width=70-vars.i_addbuttonoffsetx,height=70)


btnlock = tk.Button(
master=frame2,
text='Lock',
bg=vars.bgcolor,
fg="black",
font=vars.btnfont
)
#btnlock.bind("<Button-1>", lockbuttons)
btnlock.bind("<Button-1>", lambda event: lockbuttons(btnlock))
btnlock.place(x=810-vars.i_btnlocationoffsetx, y=wy+65-vars.i_btnlocationoffsety,width=70-vars.i_addbuttonoffsetx,height=70)


btnexit2 = tk.Button(
master=frame0,
text='Quit',
bg=vars.bgcolor,
fg="black",
font=vars.btnfont
)
btnexit2.bind("<Button-1>", quitme)
btnexit2.place(x=vars.w0-100-vars.i_btnlocationoffsetx, y=8,width=108-vars.i_addbuttonoffsetx,height=80)

#btnexit3 = tk.Button(
#master=frame1,
#text='Quit',
#bg=vars.bgcolor,
#fg="black",
#font=vars.btnfont
#)
#btnexit3.bind("<Button-1>", quitme)
#btnexit3.place(x=vars.w1-100-vars.i_btnlocationoffsetx, y=8,width=108-vars.i_addbuttonoffsetx,height=80)

vars.win2.mainloop()

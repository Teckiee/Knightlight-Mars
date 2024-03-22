#import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import keyboard
from btnevents import *
from vars import *

##########################################################
#
#					Win1 = BOTTOM LEFT 7"
#
##########################################################

wx = w1
wy = h1

frame1 = tk.Frame(master=window, width=wx, height=wy, bg=bgcolor)

frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

#win0.geometry(f"{w0}x{h0}+0+0")
window.geometry(f"{w1}x{h1}+0+{h0}")
#win2.geometry(f"{w2}x{h2}+{w0}+0")

# Remove the Title bar of the window
#w0.overrideredirect(True)
#w1.overrideredirect(True)
window.overrideredirect(True)


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
btnexit.place(x=wx-100-i_btnlocationoffsetx, y=8)

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
btnsave.place(x=wx-100-i_btnlocationoffsetx, y=wy-100)



window.mainloop()


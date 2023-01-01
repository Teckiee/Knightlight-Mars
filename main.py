#import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import keyboard
from btnevents import *
from vars import *

#bg = PhotoImage(file = 'C:\Google Drive\mark@wattsofsound\My Drive\GitHub\Knightlight-Mars\theatre.png')

frame1 = tk.Frame(master=window, width=900, height=1600, bg=bgcolor)

frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

# Remove the Title bar of the window
window.overrideredirect(True)


#img_label = Label(image=img_parcan)

loadlocations()





btnexit = tk.Button(
master=frame1,
text='quit',
bg=bgcolor,
fg="black",
font=btnfont
)
btnexit.bind("<Button-1>", quitme)
btnexit.place(x=860-i_addbuttonoffsetx, y=8)

btnsave = tk.Button(
master=frame1,
text='save',
bg=bgcolor,
fg="black",
font=btnfont
)
btnsave.bind("<Button-1>", savelocations)
btnsave.place(x=860-i_addbuttonoffsetx, y=60)

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
btnaddparcan.place(x=20, y=1400)

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
btnaddfresnel.place(x=100, y=1400)

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
btnaddwedge.place(x=180, y=1400)

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
btnaddwashmovinghead.place(x=260, y=1400)

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
btnaddmirrorball.place(x=340, y=1400)

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
btnaddledsinglefloor.place(x=420, y=1400)

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
btnaddledparcan.place(x=500, y=1400)

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
btnaddprofile.place(x=580, y=1400)





window.mainloop()


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


#i = 0
#while i < len(btnLights):
#    addlight(i)
#    i += 1


btnexit = tk.Button(
master=frame1,
text='quit',
bg=bgcolor,
fg="black",
)
btnexit.bind("<Button-1>", quitme)
btnexit.place(x=860, y=8)

btnsave = tk.Button(
master=frame1,
text='save',
bg=bgcolor,
fg="black",
)
btnsave.bind("<Button-1>", savelocations)
btnsave.place(x=860, y=60)

btnaddparcan = tk.Button(
master=frame1,
text='Add Light',
bg=bgcolor,
fg="black",
)
btnaddparcan.bind("<Button-1>", clickbtnaddparcan)
btnaddparcan.place(x=800, y=1400)

btnaddfresnel = tk.Button(
master=frame1,
text='Add Light',
bg=bgcolor,
fg="black",
)
btnaddfresnel.bind("<Button-1>", clickbtnaddfresnel)
btnaddfresnel.place(x=600, y=1400)



window.mainloop()


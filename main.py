import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import keyboard
from btnevents import *
from vars import *

#bg = PhotoImage(file = 'C:\Google Drive\mark@wattsofsound\My Drive\GitHub\Knightlight-Mars\theatre.png')


frame1 = tk.Frame(master=window, width=900, height=1600, bg="silver")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

# Remove the Title bar of the window
window.overrideredirect(True)

#label1 = tk.Label(master=frame1, text="I'm at (0, 0)", bg="red")

#label1.place(x=0, y=0)


#label2 = tk.Label(master=frame1, text="I'm at (75, 75)", bg="yellow")

#label2.place(x=75, y=75)



image = Image.open('C:\Google Drive\mark@wattsofsound\My Drive\GitHub\Knightlight-Mars\parcan.png')
img=image.resize((i_buttonwidth, i_buttonheight))

click_btn = ImageTk.PhotoImage(img)

img_label = Label(image=click_btn)

loadlocations()

i = 0
while i < len(btnLights):
    btnLights[i] = tk.Button(
    master=frame1,
    image=click_btn,
    text='btn' + str(i),
    width=i_buttonwidth,
    height=i_buttonheight,
    bg="silver",
    fg="yellow",
    )
    btnLights[i].bind("<B1-Motion>", drag)
    btnLights[i].bind("<Button-1>", clicked)
    i += 1


btnexit = tk.Button(
master=frame1,
text='quit',
bg="silver",
fg="yellow",
)
btnexit.bind("<Button-1>", quitme)

btnsave = tk.Button(
master=frame1,
text='save',
bg="silver",
fg="yellow",
)
btnsave.bind("<Button-1>", savelocations)


btnexit.place(x=860, y=0)
btnsave.place(x=860, y=60)

#btnLights[0].place(x=300-i_buttonwidth, y=900)
#btnLights[1].place(x=300, y=900)

#btnLights[2].place(x=450-i_buttonwidth, y=900)
#btnLights[3].place(x=450, y=900)

#btnLights[4].place(x=600-i_buttonwidth, y=900)
#btnLights[5].place(x=600, y=900)

btnLights[0].place(x=btnLocations[0].get_x(), y=btnLocations[0].get_y())
btnLights[1].place(x=btnLocations[1].get_x(), y=btnLocations[1].get_y())

btnLights[2].place(x=btnLocations[2].get_x(), y=btnLocations[2].get_y())
btnLights[3].place(x=btnLocations[3].get_x(), y=btnLocations[3].get_y())

btnLights[4].place(x=btnLocations[4].get_x(), y=btnLocations[4].get_y())
btnLights[5].place(x=btnLocations[5].get_x(), y=btnLocations[5].get_y())

#btnLights[0].place(x=btnLocations[0], y=btnLocations[1])
#btnLights[1].place(x=btnLocations[2], y=btnLocations[3])

#btnLights[2].place(x=btnLocations[4], y=btnLocations[5])
#btnLights[3].place(x=btnLocations[6], y=btnLocations[7])

#btnLights[4].place(x=btnLocations[8], y=btnLocations[9])
#btnLights[5].place(x=btnLocations[10], y=btnLocations[11])



window.mainloop()


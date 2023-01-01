from vars import *
import tkinter as tk
from tkinter import *
import keyboard
from PIL import Image, ImageTk

def drag(event):
    if keyboard.is_pressed("shift"):
        print("You pressed shift.")
    else:
        #event.widget.place(x=event.widget.winfo_rootx(), y=event.widget.winfo_rooty(),anchor=CENTER)
        event.widget.place(x=event.x_root-window.winfo_x()-xoffset, y=event.y_root-window.winfo_y()-yoffset,anchor=CENTER)

def clicked(event, button_press):
    #print(event.widget.get()) # Where widget is the Entry Object from click event
    #x, y = button[0].winfo_rootx(), button[0].winfo_rooty()
    x, y = event.widget.winfo_rootx(), event.widget.winfo_rooty()
    print (button_press, x, y)
    #x, y = event.x_root, event.y_root
    #print (x, y)
    #print(window.winfo_x(), window.winfo_y())
        
    #command = clicked

def quitme(event):
    exit()


def clickbtnaddparcan(event):
    btnLights.append(btnProperties())
    i = len(btnLights)-1
    btnLights[i].set_x(0)
    btnLights[i].set_y(0)
    addlight(i,img_parcan)

def clickbtnaddfresnel(event):
    btnLights.append(btnProperties())
    i = len(btnLights)-1
    btnLights[i].set_x(0)
    btnLights[i].set_y(0)
    addlight(i,img_fresnel)

def savelocations(event):
    i = 0
    f = open("demofile2.txt", "w")
    while i < len(btnLights):
        #do something to all children
        print(i , btnLights[i].btnTheLight.winfo_rootx(),btnLights[i].btnTheLight.winfo_rooty())
        f.write(str(i) + ',' + str(btnLights[i].btnTheLight.winfo_rootx())+ ',' + str(btnLights[i].btnTheLight.winfo_rooty()) + "\n")
        i += 1
    f.close()

def loadlocations():
    
    f = open("demofile2.txt", "r")
    #Lines = f.readlines()
    count = 0
    while True:
        line = f.readline()
        if not line:
            break
        linesplit = line.strip().split(",")
        print(linesplit)
        #btnLocations.append()
        btnLights.append(btnProperties())
        btnLights[int(linesplit[0])].set_x(int(linesplit[1]))
        btnLights[int(linesplit[0])].set_y(int(linesplit[2]))
        addlight(count,img_parcan)
        count += 1
    f.close()

def addlight(i,img1):

    btnLights[i].btnTheLight = tk.Button(
    #master=frame1,
    image=img1,
    text='btn' + str(i),
    width=i_buttonwidth,
    height=i_buttonheight,
    bg = bgcolor,
    fg = "yellow",
    
    ) #command=lambda m=i: which_button(m)
    btnLights[i].btnTheLight.bind("<B1-Motion>", drag)
    #btnLights[i].bind("<Button-1>", clicked)
    btnLights[i].btnTheLight.bind("<Button-1>", lambda event, m=i: clicked(event,m))
    btnLights[i].btnTheLight.place(x=btnLights[i].get_x(), y=btnLights[i].get_y())
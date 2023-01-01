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
    btnLights[i].set_type('parcan')
    addlight(i)

def clickbtnaddfresnel(event):
    btnLights.append(btnProperties())
    i = len(btnLights)-1
    btnLights[i].set_x(0)
    btnLights[i].set_y(0)
    btnLights[i].set_type('fresnel')
    addlight(i)

def clickbtnaddwedge(event):
    btnLights.append(btnProperties())
    i = len(btnLights)-1
    btnLights[i].set_x(0)
    btnLights[i].set_y(0)
    btnLights[i].set_type('wedge')
    addlight(i)

def clickbtnaddwashmovinghead(event):
    btnLights.append(btnProperties())
    i = len(btnLights)-1
    btnLights[i].set_x(0)
    btnLights[i].set_y(0)
    btnLights[i].set_type('washmovinghead')
    addlight(i)

def clickbtnaddledparcan(event):
    btnLights.append(btnProperties())
    i = len(btnLights)-1
    btnLights[i].set_x(0)
    btnLights[i].set_y(0)
    btnLights[i].set_type('ledparcan')
    addlight(i)

def clickbtnaddmirrorball(event):
    btnLights.append(btnProperties())
    i = len(btnLights)-1
    btnLights[i].set_x(0)
    btnLights[i].set_y(0)
    btnLights[i].set_type('mirrorball')
    addlight(i)

def clickbtnaddledsinglefloor(event):
    btnLights.append(btnProperties())
    i = len(btnLights)-1
    btnLights[i].set_x(0)
    btnLights[i].set_y(0)
    btnLights[i].set_type('ledsinglefloor')
    addlight(i)

def clickbtnaddprofile(event):
    btnLights.append(btnProperties())
    i = len(btnLights)-1
    btnLights[i].set_x(0)
    btnLights[i].set_y(0)
    btnLights[i].set_type('profile')
    addlight(i)



def savelocations(event):
    i = 0
    f = open("Settings.txt", "w")
    while i < len(btnLights):
        #do something to all children
        print(i , btnLights[i].btnTheLight.winfo_rootx(),btnLights[i].btnTheLight.winfo_rooty())
        f.write(str(i) + ',' + \
        str(btnLights[i].btnTheLight.winfo_rootx())+ ',' + \
        str(btnLights[i].btnTheLight.winfo_rooty())+ ',' + \
        str(btnLights[i].get_type()) + "\n")
        i += 1
    f.close()

def loadlocations():
    
    f = open("Settings.txt", "r")
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
        btnLights[int(linesplit[0])].set_type(linesplit[3])
        addlight(count)
        count += 1
    f.close()

def loadlocationsloadtest():
    count = 0
    while count < 2000:
        btnLights.append(btnProperties())
        i = len(btnLights)-1
        btnLights[i].set_x(0)
        btnLights[i].set_y(0)
        btnLights[i].set_type('profile')
        addlight(i)
        count += 1

def addlight(i):
    if btnLights[i].get_type() == 'parcan':
        img1 = img_parcan
        x = i_parcanwidth
        y = i_parcanheight
    elif btnLights[i].get_type() == 'fresnel':
        img1 = img_fresnel
        x = i_fresnelwidth
        y = i_fresnelheight
    elif btnLights[i].get_type() == 'wedge':
        img1 = img_wedge
        x = i_wedgewidth
        y = i_wedgeheight
    elif btnLights[i].get_type() == 'washmovinghead':
        img1 = img_washmovinghead
        x = i_washmovingheadwidth
        y = i_washmovingheadheight
    elif btnLights[i].get_type() == 'mirrorball':
        img1 = img_mirrorball
        x = i_mirrorballwidth
        y = i_mirrorballheight
    elif btnLights[i].get_type() == 'ledsinglefloor':
        img1 = img_ledsinglefloor
        x = i_ledsinglefloorwidth
        y = i_ledsinglefloorheight
    elif btnLights[i].get_type() == 'ledparcan':
        img1 = img_ledparcan
        x = i_ledparcanwidth
        y = i_ledparcanheight
    elif btnLights[i].get_type() == 'profile':
        img1 = img_profile
        x = i_profilewidth
        y = i_profileheight

  

    btnLights[i].btnTheLight = tk.Button(
    #master=frame1,
    image=img1,
    text='btn' + str(i),
    width=x,
    height=y,
    bg = bgcolor,
    fg = "yellow",
    
    ) #command=lambda m=i: which_button(m)
    btnLights[i].btnTheLight.bind("<B1-Motion>", drag)
    #btnLights[i].bind("<Button-1>", clicked)
    btnLights[i].btnTheLight.bind("<Button-1>", lambda event, m=i: clicked(event,m))
    btnLights[i].btnTheLight.place(x=btnLights[i].get_x(), y=btnLights[i].get_y())
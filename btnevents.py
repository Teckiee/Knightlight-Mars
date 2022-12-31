from vars import *
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def drag(event):
    #event.widget.place(x=event.widget.winfo_rootx(), y=event.widget.winfo_rooty(),anchor=CENTER)
    event.widget.place(x=event.x_root-window.winfo_x()-xoffset, y=event.y_root-window.winfo_y()-yoffset,anchor=CENTER)

def clicked(event):
    #print(event.widget.get()) # Where widget is the Entry Object from click event
    #x, y = button[0].winfo_rootx(), button[0].winfo_rooty()
    x, y = event.widget.winfo_rootx(), event.widget.winfo_rooty()
    print (x, y)
    #x, y = event.x_root, event.y_root
    #print (x, y)
    #print(window.winfo_x(), window.winfo_y())
        
    #command = clicked
def quitme(event):
    exit()

def savelocations(event):
    i = 0
    f = open("demofile2.txt", "w")
    while i < len(btnLights):
        #do something to all children
        print(i , btnLights[i].winfo_rootx(),btnLights[i].winfo_rooty())
        f.write(str(i) + ',' + str(btnLights[i].winfo_rootx()) + "\n")
        i += 1
        f.write(str(i) + ',' + str(btnLights[i].winfo_rooty()) + "\n")
        i += 1
    f.close()

def loadlocations():
    i = 0
    f = open("demofile2.txt", "r")
    #Lines = f.readlines()
    count = 0
    while True:
        line = f.readline()
        if not line:
            break
        linesplit = line.strip().split(",")
        print(linesplit)
        btnLocations[int(linesplit[0])].set_x(int(linesplit[1]))
        btnLocations[int(linesplit[0])].set_y(int(linesplit[2]))
        print(btnLocations[int(linesplit[0])].get_x,btnLocations[int(linesplit[0])].get_y)
        count += 1
    f.close()
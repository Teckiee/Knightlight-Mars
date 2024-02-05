from vars import *
import tkinter as tk
from tkinter import *
import keyboard
from PIL import Image, ImageTk
import socket

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

def clickbtnaddintimidator(event):
    btnLights.append(btnProperties())
    i = len(btnLights)-1
    btnLights[i].set_x(0)
    btnLights[i].set_y(0)
    btnLights[i].set_type('intimidator')
    addlight(i)
	
def clickbtnaddledpanel(event):
    btnLights.append(btnProperties())
    i = len(btnLights)-1
    btnLights[i].set_x(0)
    btnLights[i].set_y(0)
    btnLights[i].set_type('ledpanel')
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
        btnLights[int(linesplit[0])].set_x(int(linesplit[1])-w0)
        btnLights[int(linesplit[0])].set_y(int(linesplit[2]))
        btnLights[int(linesplit[0])].set_type(linesplit[3])
        addlight(count)
        count += 1
    f.close()

def start_server():
    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                datatext = data.decode('utf-8')
                print(f"Received data: {datatext}")
                if not data:
                    break
                conn.sendall(data)

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
    elif btnLights[i].get_type() == 'intimidator':
        img1 = img_intimidator
        x = i_intimidatorwidth
        y = i_intimidatorheight
    elif btnLights[i].get_type() == 'ledpanel':
        img1 = img_ledpanel
        x = i_ledpanelwidth
        y = i_ledpanelheight

        
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

def addlightbuttons(oframe):
    btnaddparcan = tk.Button(
    master=oframe,
    text='Add Parcan',
    bg='black',
    fg="white",
    width=10-i_addbuttonoffsetx,
    height=4,
    font=btnfont
    )
    btnaddparcan.bind("<Button-1>", clickbtnaddparcan)
    btnaddparcan.place(x=20, y=h2-i_btnlocationoffsety)

    btnaddfresnel = tk.Button(
    master=oframe,
    text='Add Fresnel',
    bg='black',
    fg="white",
    width=10-i_addbuttonoffsetx,
    height=4,
    font=btnfont
    )
    btnaddfresnel.bind("<Button-1>", clickbtnaddfresnel)
    btnaddfresnel.place(x=100, y=h2-i_btnlocationoffsety)

    btnaddwedge = tk.Button(
    master=oframe,
    text='Add wedge',
    bg='black',
    fg="white",
    width=10-i_addbuttonoffsetx,
    height=4,
    font=btnfont
    )
    btnaddwedge.bind("<Button-1>", clickbtnaddwedge)
    btnaddwedge.place(x=180, y=h2-i_btnlocationoffsety)

    btnaddwashmovinghead = tk.Button(
    master=oframe,
    text='Add wash moving head',
    wraplength=80,
    bg='black',
    fg="white",
    width=10-i_addbuttonoffsetx,
    height=4,
    font=btnfont
    )
    btnaddwashmovinghead.bind("<Button-1>", clickbtnaddwashmovinghead)
    btnaddwashmovinghead.place(x=260, y=h2-i_btnlocationoffsety)

    btnaddmirrorball = tk.Button(
    master=oframe,
    text='Add mirrorball',
    wraplength=80,
    bg='black',
    fg="white",
    width=10-i_addbuttonoffsetx,
    height=4,
    font=btnfont
    )
    btnaddmirrorball.bind("<Button-1>", clickbtnaddmirrorball)
    btnaddmirrorball.place(x=340, y=h2-i_btnlocationoffsety)

    btnaddledsinglefloor = tk.Button(
    master=oframe,
    text='Add led single floor',
    wraplength=80,
    bg='black',
    fg="white",
    width=10-i_addbuttonoffsetx,
    height=4,
    font=btnfont
    )
    btnaddledsinglefloor.bind("<Button-1>", clickbtnaddledsinglefloor)
    btnaddledsinglefloor.place(x=420, y=h2-i_btnlocationoffsety)

    btnaddledparcan = tk.Button(
    master=oframe,
    text='Add led parcan',
    wraplength=80,
    bg='black',
    fg="white",
    width=10-i_addbuttonoffsetx,
    height=4,
    font=btnfont
    )
    btnaddledparcan.bind("<Button-1>", clickbtnaddledparcan)
    btnaddledparcan.place(x=500, y=h2-i_btnlocationoffsety)

    btnaddprofile = tk.Button(
    master=oframe,
    text='Add profile',
    wraplength=80,
    bg='black',
    fg="white",
    width=10-i_addbuttonoffsetx,
    height=4,
    font=btnfont
    )
    btnaddprofile.bind("<Button-1>", clickbtnaddprofile)
    btnaddprofile.place(x=580, y=h2-i_btnlocationoffsety)

    btnaddintimidator = tk.Button(
    master=oframe,
    text='Add Intimidator',
    wraplength=72,
    bg='black',
    fg="white",
    width=10-i_addbuttonoffsetx,
    height=4,
    font=btnfont
    )
    btnaddintimidator.bind("<Button-1>", clickbtnaddintimidator)
    btnaddintimidator.place(x=660, y=h2-i_btnlocationoffsety)

    btnaddledpanel = tk.Button(
    master=oframe,
    text='Add LEDPanel',
    wraplength=80,
    bg='black',
    fg="white",
    width=10-i_addbuttonoffsetx,
    height=4,
    font=btnfont
    )
    btnaddledpanel.bind("<Button-1>", clickbtnaddledpanel)
    btnaddledpanel.place(x=20, y=h2+65-i_btnlocationoffsety)



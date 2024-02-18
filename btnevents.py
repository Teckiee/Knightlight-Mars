#from vars import *
import vars
import tkinter as tk
from tkinter import *
#import keyboard
from PIL import Image, ImageTk
import socket
import serial
import threading

def drag(event):
    #if keyboard.is_pressed("shift"):
    #    print("You pressed shift.")
    #else:
        #event.widget.place(x=event.widget.winfo_rootx(), y=event.widget.winfo_rooty(),anchor=CENTER)
    if vars.buttonlocationslocked == 0:
        event.widget.place(x=event.x_root-vars.win2.winfo_x()-vars.xoffset, y=event.y_root-vars.win2.winfo_y()-vars.yoffset,anchor=CENTER)

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

def m_Play(event, index):
    vars.ser.write(f"Play,{index}\n".encode('utf-8'))
    
def m_Stop(event, index):
    vars.ser.write(f"Stop,{index}\n".encode('utf-8'))
    
def m_Cue(event, index):
    vars.ser.write(f"Cue,{index}\n".encode('utf-8'))
    

def clickbtnaddparcan(event):
    vars.btnLights.append(vars.btnProperties())
    i = len(vars.btnLights)-1
    vars.btnLights[i].set_x(0)
    vars.btnLights[i].set_y(0)
    vars.btnLights[i].set_type('parcan')
    addlight(i)

def clickbtnaddfresnel(event):
    vars.btnLights.append(vars.btnProperties())
    i = len(vars.btnLights)-1
    vars.btnLights[i].set_x(0)
    vars.btnLights[i].set_y(0)
    vars.btnLights[i].set_type('fresnel')
    addlight(i)

def clickbtnaddwedge(event):
    vars.btnLights.append(vars.btnProperties())
    i = len(vars.btnLights)-1
    vars.btnLights[i].set_x(0)
    vars.btnLights[i].set_y(0)
    vars.btnLights[i].set_type('wedge')
    addlight(i)

def clickbtnaddwashmovinghead(event):
    vars.btnLights.append(vars.btnProperties())
    i = len(vars.btnLights)-1
    vars.btnLights[i].set_x(0)
    vars.btnLights[i].set_y(0)
    vars.btnLights[i].set_type('washmovinghead')
    addlight(i)

def clickbtnaddledparcan(event):
    vars.btnLights.append(vars.btnProperties())
    i = len(vars.btnLights)-1
    vars.btnLights[i].set_x(0)
    vars.btnLights[i].set_y(0)
    vars.btnLights[i].set_type('ledparcan')
    addlight(i)

def clickbtnaddmirrorball(event):
    vars.btnLights.append(vars.btnProperties())
    i = len(vars.btnLights)-1
    vars.btnLights[i].set_x(0)
    vars.btnLights[i].set_y(0)
    vars.btnLights[i].set_type('mirrorball')
    addlight(i)

def clickbtnaddledsinglefloor(event):
    vars.btnLights.append(vars.btnProperties())
    i = len(vars.btnLights)-1
    vars.btnLights[i].set_x(0)
    vars.btnLights[i].set_y(0)
    vars.btnLights[i].set_type('ledsinglefloor')
    addlight(i)

def clickbtnaddprofile(event):
    vars.btnLights.append(vars.btnProperties())
    i = len(vars.btnLights)-1
    vars.btnLights[i].set_x(0)
    vars.btnLights[i].set_y(0)
    vars.btnLights[i].set_type('profile')
    addlight(i)

def clickbtnaddintimidator(event):
    vars.btnLights.append(vars.btnProperties())
    i = len(vars.btnLights)-1
    vars.btnLights[i].set_x(0)
    vars.btnLights[i].set_y(0)
    vars.btnLights[i].set_type('intimidator')
    addlight(i)
	
def clickbtnaddledpanel(event):
    vars.btnLights.append(vars.btnProperties())
    i = len(vars.btnLights)-1
    vars.btnLights[i].set_x(0)
    vars.btnLights[i].set_y(0)
    vars.btnLights[i].set_type('ledpanel')
    addlight(i)


def savelocations(event):
    i = 0
    f = open("Settings.txt", "w")
    while i < len(vars.btnLights):
        #do something to all children
        print(i , vars.btnLights[i].btnTheLight.winfo_rootx(),vars.btnLights[i].btnTheLight.winfo_rooty())
        f.write(str(i) + ',' + \
        str(vars.btnLights[i].btnTheLight.winfo_rootx())+ ',' + \
        str(vars.btnLights[i].btnTheLight.winfo_rooty())+ ',' + \
        str(vars.btnLights[i].get_type()) + "\n")
        i += 1
    f.close()

def lockbuttons(button):
    if vars.buttonlocationslocked == 1:
        vars.buttonlocationslocked = 0
        button.config(bg="red")
    else:
        vars.buttonlocationslocked = 1
        button.config(bg=vars.bgcolor)

def loadlocations():
    
    f = open("Settings.txt", "r")
    #Lines = f.readlines()
    count = 0
    while True:
        line = f.readline()
        if not line:
            break
        linesplit = line.strip().split(",")
        #print(linesplit)
        #btnLocations.append()
        vars.btnLights.append(vars.btnProperties())
        vars.btnLights[int(linesplit[0])].set_x(int(linesplit[1])-vars.w0)
        vars.btnLights[int(linesplit[0])].set_y(int(linesplit[2]))
        vars.btnLights[int(linesplit[0])].set_type(linesplit[3])
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

def handle_serial_received(evt):
    # Update the GUI based on the received serial message
    data1 = vars.received_data
    inccmd = data1.split(",")
    
    if inccmd[0] == "HELLO":
        print("Valid handshake request: HELLO")
        # Send a response back to the VB.NET application
        vars.ser.write("ONLINE\n".encode('utf-8'))
    elif inccmd[0] == "Song":
        indx=int(inccmd[1])
        vars.cMusicPlayers[indx].lblSongName.config(text=inccmd[2])
        
    else:
        print("Unexpected handshake request:", data1)
    
    #vars.cMusicPlayers[indx].lblSongName.config(text=inccmd[2])

def start_serial():
    
    try:
        # Configure the serial port settings (replace '/dev/ttyUSB0' with the correct device path)
        
        # Main loop to continuously monitor the serial port
        while True:
            # Read data from the serial port
            data1 = vars.ser.readline().strip().decode('utf-8')

            # Process the received data
            if data1:
                print("Received data:", data1)
                vars.received_data = data1
                vars.win2.event_generate('<<SerialReceived>>', when='tail', data=data1)
                
                # Add your logic to handle the received data here
                # For example, update GUI elements based on the received data

    except Exception as e:
        print("Error:", str(e))

    finally:
        # Close the serial port before exiting
        if vars.ser is not None and vars.ser.is_open:
            vars.ser.close()
		
def loadlocationsloadtest():
    count = 0
    while count < 2000:
        vars.btnLights.append(vars.btnProperties())
        i = len(vars.btnLights)-1
        vars.btnLights[i].set_x(0)
        vars.btnLights[i].set_y(0)
        vars.btnLights[i].set_type('profile')
        addlight(i)
        count += 1

def addlight(i):
    if vars.btnLights[i].get_type() == 'parcan':
        img1 = vars.img_parcan
        x = vars.i_parcanwidth
        y = vars.i_parcanheight
    elif vars.btnLights[i].get_type() == 'fresnel':
        img1 = vars.img_fresnel
        x = vars.i_fresnelwidth
        y = vars.i_fresnelheight
    elif vars.btnLights[i].get_type() == 'wedge':
        img1 = vars.img_wedge
        x = vars.i_wedgewidth
        y = vars.i_wedgeheight
    elif vars.btnLights[i].get_type() == 'washmovinghead':
        img1 = vars.img_washmovinghead
        x = vars.i_washmovingheadwidth
        y = vars.i_washmovingheadheight
    elif vars.btnLights[i].get_type() == 'mirrorball':
        img1 = vars.img_mirrorball
        x = vars.i_mirrorballwidth
        y = vars.i_mirrorballheight
    elif vars.btnLights[i].get_type() == 'ledsinglefloor':
        img1 = vars.img_ledsinglefloor
        x = vars.i_ledsinglefloorwidth
        y = vars.i_ledsinglefloorheight
    elif vars.btnLights[i].get_type() == 'ledparcan':
        img1 = vars.img_ledparcan
        x = vars.i_ledparcanwidth
        y = vars.i_ledparcanheight
    elif vars.btnLights[i].get_type() == 'profile':
        img1 = vars.img_profile
        x = vars.i_profilewidth
        y = vars.i_profileheight
    elif vars.btnLights[i].get_type() == 'intimidator':
        img1 = vars.img_intimidator
        x = vars.i_intimidatorwidth
        y = vars.i_intimidatorheight
    elif vars.btnLights[i].get_type() == 'ledpanel':
        img1 = vars.img_ledpanel
        x = vars.i_ledpanelwidth
        y = vars.i_ledpanelheight

        
    vars.btnLights[i].btnTheLight = tk.Button(
    #master=frame1,
    image=img1,
    text='btn' + str(i),
    width=x,
    height=y,
    bg = vars.bgcolor,
    fg = "yellow",

    ) #command=lambda m=i: which_button(m)
    vars.btnLights[i].btnTheLight.bind("<B1-Motion>", drag)
    #vars.btnLights[i].bind("<Button-1>", clicked)
    vars.btnLights[i].btnTheLight.bind("<Button-1>", lambda event, m=i: clicked(event,m))
    vars.btnLights[i].btnTheLight.place(x=vars.btnLights[i].get_x(), y=vars.btnLights[i].get_y())

def setupmusicplayer(oframe):
    i = 0
    
    #i = len(vars.cMusicPlayers)-1
    perrow = 0
    while i < 8:
        vars.cMusicPlayers.append(vars.cMusicPlayer())
        vars.cMusicPlayers[i].set_x(8)
        vars.cMusicPlayers[i].set_y(4+perrow)

        vars.cMusicPlayers[i].btnCue = tk.Button(
        master=oframe,
        font=vars.btnfont,
        bg = vars.bgcolor,
        fg = "yellow",
        text='Cue'
        )
        vars.cMusicPlayers[i].btnCue.bind("<Button-1>", lambda event, index=i: m_Cue(event, index))
        vars.cMusicPlayers[i].btnCue.place(x=8, y=vars.cMusicPlayers[i].get_y(),width=70,height=70)
        
        vars.cMusicPlayers[i].btnPlayPause = tk.Button(
        master=oframe,
        font=vars.btnfont,
        bg = vars.bgcolor,
        fg = "yellow",
        text='Play'
        )
        vars.cMusicPlayers[i].btnPlayPause.bind("<Button-1>", lambda event, index=i: m_Play(event, index))
        vars.cMusicPlayers[i].btnPlayPause.place(x=vars.cMusicPlayers[i].get_x()+474, y=vars.cMusicPlayers[i].get_y(),width=70,height=70)
        
        vars.cMusicPlayers[i].btnStop = tk.Button(
        master=oframe,
        font=vars.btnfont,
        bg = vars.bgcolor,
        fg = "yellow",
        text='Stop'
        )
        vars.cMusicPlayers[i].btnStop.bind("<Button-1>", lambda event, index=i: m_Stop(event, index))
        vars.cMusicPlayers[i].btnStop.place(x=vars.cMusicPlayers[i].get_x()+544+60, y=vars.cMusicPlayers[i].get_y(),width=70,height=70)
        
        vars.cMusicPlayers[i].lblSongName = tk.Label(
        master=oframe,
        font=vars.btnfont,
        bg = vars.bgcolor,
        fg = "yellow",
        text='Song Name'
        )
        vars.cMusicPlayers[i].lblSongName.place(x=vars.cMusicPlayers[i].get_x()+74, y=vars.cMusicPlayers[i].get_y(),width=400,height=70)
        perrow += 74
        i+=1

def addlightbuttons(oframe):
    btnaddparcan = tk.Button(
    master=oframe,
    text='Add Parcan',
    bg='black',
    fg="white",
    width=10-vars.i_addbuttonoffsetx,
    height=4,
    font=vars.btnfont
    )
    btnaddparcan.bind("<Button-1>", clickbtnaddparcan)
    btnaddparcan.place(x=20, y=vars.h2-vars.i_btnlocationoffsety)

    btnaddfresnel = tk.Button(
    master=oframe,
    text='Add Fresnel',
    bg='black',
    fg="white",
    width=10-vars.i_addbuttonoffsetx,
    height=4,
    font=vars.btnfont
    )
    btnaddfresnel.bind("<Button-1>", clickbtnaddfresnel)
    btnaddfresnel.place(x=100, y=vars.h2-vars.i_btnlocationoffsety)

    btnaddwedge = tk.Button(
    master=oframe,
    text='Add wedge',
    bg='black',
    fg="white",
    width=10-vars.i_addbuttonoffsetx,
    height=4,
    font=vars.btnfont
    )
    btnaddwedge.bind("<Button-1>", clickbtnaddwedge)
    btnaddwedge.place(x=180, y=vars.h2-vars.i_btnlocationoffsety)

    btnaddwashmovinghead = tk.Button(
    master=oframe,
    text='Add wash moving head',
    wraplength=80,
    bg='black',
    fg="white",
    width=10-vars.i_addbuttonoffsetx,
    height=4,
    font=vars.btnfont
    )
    btnaddwashmovinghead.bind("<Button-1>", clickbtnaddwashmovinghead)
    btnaddwashmovinghead.place(x=260, y=vars.h2-vars.i_btnlocationoffsety)

    btnaddmirrorball = tk.Button(
    master=oframe,
    text='Add mirrorball',
    wraplength=80,
    bg='black',
    fg="white",
    width=10-vars.i_addbuttonoffsetx,
    height=4,
    font=vars.btnfont
    )
    btnaddmirrorball.bind("<Button-1>", clickbtnaddmirrorball)
    btnaddmirrorball.place(x=340, y=vars.h2-vars.i_btnlocationoffsety)

    btnaddledsinglefloor = tk.Button(
    master=oframe,
    text='Add led single floor',
    wraplength=80,
    bg='black',
    fg="white",
    width=10-vars.i_addbuttonoffsetx,
    height=4,
    font=vars.btnfont
    )
    btnaddledsinglefloor.bind("<Button-1>", clickbtnaddledsinglefloor)
    btnaddledsinglefloor.place(x=420, y=vars.h2-vars.i_btnlocationoffsety)

    btnaddledparcan = tk.Button(
    master=oframe,
    text='Add led parcan',
    wraplength=80,
    bg='black',
    fg="white",
    width=10-vars.i_addbuttonoffsetx,
    height=4,
    font=vars.btnfont
    )
    btnaddledparcan.bind("<Button-1>", clickbtnaddledparcan)
    btnaddledparcan.place(x=500, y=vars.h2-vars.i_btnlocationoffsety)

    btnaddprofile = tk.Button(
    master=oframe,
    text='Add profile',
    wraplength=80,
    bg='black',
    fg="white",
    width=10-vars.i_addbuttonoffsetx,
    height=4,
    font=vars.btnfont
    )
    btnaddprofile.bind("<Button-1>", clickbtnaddprofile)
    btnaddprofile.place(x=580, y=vars.h2-vars.i_btnlocationoffsety)

    btnaddintimidator = tk.Button(
    master=oframe,
    text='Add Intimidator',
    wraplength=72,
    bg='black',
    fg="white",
    width=10-vars.i_addbuttonoffsetx,
    height=4,
    font=vars.btnfont
    )
    btnaddintimidator.bind("<Button-1>", clickbtnaddintimidator)
    btnaddintimidator.place(x=660, y=vars.h2-vars.i_btnlocationoffsety)

    btnaddledpanel = tk.Button(
    master=oframe,
    text='Add LEDPanel',
    wraplength=80,
    bg='black',
    fg="white",
    width=10-vars.i_addbuttonoffsetx,
    height=4,
    font=vars.btnfont
    )
    btnaddledpanel.bind("<Button-1>", clickbtnaddledpanel)
    btnaddledpanel.place(x=20, y=vars.h2+65-vars.i_btnlocationoffsety)



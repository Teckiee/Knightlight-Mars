# https://stackoverflow.com/questions/44902846/bind-drag-function-to-object-in-tkinter-ui

from tkinter import *
import tkinter as tk
window = Tk()
window.geometry('900x1500')
#window.configure(bg = 'green4')
#window.state('zoomed')

def drag(event):
    event.widget.place(x=event.x_root, y=event.y_root,anchor=CENTER)

card = Canvas(window, width=74, height=97, bg='blue')
card.place(x=300, y=600,anchor=CENTER)
card.bind("<B1-Motion>", drag)

another_card = Canvas(window, width=74, height=97, bg='red')
another_card.place(x=600, y=600,anchor=CENTER)
another_card.bind("<B1-Motion>", drag)

window.mainloop()
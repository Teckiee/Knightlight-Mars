from tkinter import *
from tkinter import font
root=Tk()
l1=Label(root,text="Hello")
l1.pack()
Button(root,text='get label font',command=lambda: print(font.nametofont(l1['font']).configure()["family"])).pack()
root.mainloop()
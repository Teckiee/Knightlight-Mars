from tkinter import *


class MyButton(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = 'red'



root = Tk()
root.geometry('200x200')

my_button = MyButton(root, text='red button')
my_button.pack()

root.mainloop()
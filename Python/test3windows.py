import tkinter as tk

def create_window(title):
    window = tk.Toplevel(root)
    window.title(title)
    tk.Label(window, text=f"This is the {title} window").pack()

root = tk.Tk()
root.title("Main Window")

# Create three windows
create_window("Window 1")
create_window("Window 2")
create_window("Window 3")

root.mainloop()

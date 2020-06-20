from tkinter import *

x = 1370
y = 800


def windows():
    global x, y
    window = Tk()
    x = window.winfo_screenwidth()
    y = window.winfo_screenheight() + 50
    window.destroy()
    return x, y


windows()

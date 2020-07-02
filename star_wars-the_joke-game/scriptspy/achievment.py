import pygame
import os
from scriptspy import loading, shoots, system_size, functions
from PIL import ImageTk
from tkinter import *

pygame.init()

gameovers = 0


def deathes():
    with open('scriptspy\papers\deathes.txt', 'a') as file:
        file.write('1 ')


def success():
    global gameovers
    for_file = []
    with open('scriptspy\papers\deathes.txt', 'r') as file:
        lines = file.readlines()
        if lines:
            list = lines[0].split(' ')
            for i in list:
                if i != '':
                    for_file.append(int(i))
    if lines:
        gameovers = sum(for_file)
    else:
        gameovers = 0


def achievements():
    root = Tk()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth()+10, root.winfo_screenheight()+10))

    def break_root():
        root.destroy()

    img_achievement2 = ImageTk.PhotoImage(loading.img_achievement)
    img_skull2 = ImageTk.PhotoImage(loading.img_skull)
    img_gunner_tk = ImageTk.PhotoImage(loading.img_gunner_tk)

    canvas = Canvas(root, width=system_size.x+10, height=system_size.y+10, bg='black')
    canvas.pack()

    img_ram2 = ImageTk.PhotoImage(loading.img_ram, master=root)

    canvas.create_image(system_size.x//2, system_size.y//2-25, image=img_ram2)

    canvas.create_image(17, 20, image=img_achievement2)
    if gameovers >= 50:
        text = canvas.create_text(130, 20, font=("Comic Sans MS", 15), text="Умрите 50 раз", fill="#dceca4")
        text = canvas.create_text(130, 50, font=("Comic Sans MS", 20), text="Получено", fill="#dceca4")
    else:
        text = canvas.create_text(130, 20, font=("Comic Sans MS", 15), text="Умрите " + (str(50 - gameovers)) + ' раз',
                                  fill="#dceca4")
        text = canvas.create_text(130, 50, font=("Comic Sans MS", 15), text="Награда: скин ", fill="#dceca4")
        canvas.create_image(230, 50, image=img_skull2)

    canvas.create_image(17, 100, image=img_achievement2)
    if functions.newgunner == 2:
        text = canvas.create_text(183, 100, font=("Comic Sans MS", 15), text="Спасти союзный корабль", fill="#dceca4")
        text = canvas.create_text(130, 130, font=("Comic Sans MS", 20), text="Получено", fill="#dceca4")
    else:
        text = canvas.create_text(183, 100, font=("Comic Sans MS", 15), text="Спасти союзный корабль", fill="#dceca4")
        text = canvas.create_text(183, 130, font=("Comic Sans MS", 15), text="Награда: новый персонаж ", fill="#dceca4")
        canvas.create_image(350, 130, image=img_gunner_tk)

    d = Button(text="OK", command=break_root, font=("Comic Sans MS", 30))
    d.place(x=50, y=system_size.y-200)
    d['bg'] = '#dceca4'
    d['activebackground'] = 'black'
    d['fg'] = 'black'
    d['activeforeground'] = '#dceca4'

    root.bind('<Return>', break_root)

    root.overrideredirect(1)
    root.attributes("-topmost", True)
    root.update()
    root.deiconify()
    root.mainloop()
    return

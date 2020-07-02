from tkinter import *
from PIL import ImageTk
from tkinter.ttk import Radiobutton
from scriptspy import loading, system_size, achievment


def settings(speed2, skins2, reset2, sprite2, sprites2, keyboard2, mouse2, moving2):
    global scale1
    global button_sprites
    global var

    root = Tk()
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth()+10, root.winfo_screenheight()+10))

    def destroy():
        speed2()
        skins2()
        reset2()
        root.destroy()

    img_ram2 = ImageTk.PhotoImage(loading.img_ram, master=root)
    img_skull2 = ImageTk.PhotoImage(loading.img_skull2)
    img_keyb = ImageTk.PhotoImage(loading.img_key)
    img_keym = ImageTk.PhotoImage(loading.img_mouse)
    img_option2 = ImageTk.PhotoImage(loading.img_option)
    img_vader4 = ImageTk.PhotoImage(loading.img1)
    img_putin = ImageTk.PhotoImage(loading.putin1)
    img_virus = ImageTk.PhotoImage(loading.virus1)
    img_vaders = ImageTk.PhotoImage(loading.img_vader_tk)

    canvas = Canvas(root, width=system_size.x+10, height=system_size.y+10, bg='black')
    canvas.pack()

    canvas.create_image(system_size.x//2, system_size.y//2-25, image=img_ram2)

    text = canvas.create_text(270, 20, font=("Comic Sans MS", 15), text="Минимальная скорость врагов(по умолчанию 4)", fill="#dceca4")
    scale1 = Scale(canvas, orient=HORIZONTAL, length=700, from_=1, to=25, tickinterval=1, resolution=1, bg='black', fg='#dceca4')
    scale1.place(x=0, y=35)
    canvas.create_image(17, 20, image=img_option2)

    text = canvas.create_text(190, 140, font=("Comic Sans MS", 15), text="Включать прорисовку спрайтов", fill="#dceca4")
    if sprites2:
        button_sprites = Button(text="Да", command=sprite2)
        button_sprites.place(x=350, y=130)
        button_sprites['bg'] = '#dceca4'
        button_sprites['activebackground'] = 'black'
        button_sprites['fg'] = 'black'
        button_sprites['activeforeground'] = '#dceca4'
    else:
        button_sprites = Button(root, text='Нет', command=sprite2)
        button_sprites.place(x=350, y=130)
        button_sprites['bg'] = '#dceca4'
        button_sprites['activebackground'] = 'black'
        button_sprites['fg'] = 'black'
        button_sprites['activeforeground'] = '#dceca4'
    canvas.create_image(17, 140, image=img_option2)

    text = canvas.create_text(160, 220, font=("Comic Sans MS", 15), text="Изображения для врагов", fill="#dceca4")
    canvas.create_image(17, 220, image=img_option2)
    canvas.create_image(60, 280, image=img_vader4)
    canvas.create_image(148, 280, image=img_putin)
    canvas.create_image(238, 280, image=img_virus)
    canvas.create_image(326, 280, image=img_vaders)
    if achievment.gameovers >= 50:
        canvas.create_image(420, 280, image=img_skull2)
    var = IntVar()
    var.set(3)
    radio = Radiobutton(root, variable=var, value=0)
    radio.place(x=45, y=325)
    radio = Radiobutton(root, variable=var, value=1)
    radio.place(x=135, y=325)
    radio = Radiobutton(root, variable=var, value=2)
    radio.place(x=225, y=325)
    radio = Radiobutton(root, variable=var, value=3)
    radio.place(x=315, y=325)
    if achievment.gameovers >= 50:
        radio = Radiobutton(root, variable=var, value=4)
        radio.place(x=404, y=325)

    text = canvas.create_text(135, 410, font=("Comic Sans MS", 15), text="Способ управления", fill="#dceca4")
    canvas.create_image(17, 410, image=img_option2)
    buttonkey = Button(command=keyboard2, image=img_keyb)
    buttonkey.place(x=30, y=460)
    buttonmouse = Button(command=mouse2, image=img_keym)
    buttonmouse.place(x=140, y=460)

    text = canvas.create_text(270, 610, font=("Comic Sans MS", 15), text="Здесь можно посмотреть текущее управление", fill="#dceca4")
    canvas.create_image(17, 610, image=img_option2)
    button = Button(text="Здесь", command=moving2, font=("Comic Sans MS", 10))
    button.place(x=55, y=630)
    button['bg'] = '#dceca4'
    button['activebackground'] = 'black'
    button['fg'] = 'black'
    button['activeforeground'] = '#dceca4'

    d = Button(text="Подтведить эти изменения", command=destroy, font=("Comic Sans MS", 14))
    d.place(x=20, y=system_size.y-100)
    d['bg'] = '#dceca4'
    d['activebackground'] = 'black'
    d['fg'] = 'black'
    d['activeforeground'] = '#dceca4'

    root.overrideredirect(1)
    root.attributes("-topmost", True)
    root.update()
    root.deiconify()
    root.mainloop()
    return

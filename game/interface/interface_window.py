import tkinter as tk

from game.texts.interface.main_menu import (BUTTON_1, BUTTON_2, BUTTON_3,
                                            BUTTON_4, BUTTON_5, HELLO)


def window_interface():
    window = tk.Tk()
    window.title("Битва шести королевств")
    window.geometry('800x600')
    window.resizable(height=False, width=False)
    window['bg'] = 'black'
    menu_image = tk.PhotoImage(file='interface/image/image.png')
    img = tk.Label(window, image=menu_image)
    img.place(x=250, y=120)
    menu = tk.Label(window, text=HELLO, font=('Arial', 15),
                    bg='black', fg='white')
    menu.place(x=300, y=310)
    btn_1 = tk.Button(window, text=BUTTON_1)
    btn_1.place(x=340, y=370)
    btn_2 = tk.Button(window, text=BUTTON_2)
    btn_2.place(x=340, y=400)
    btn_3 = tk.Button(window, text=BUTTON_3)
    btn_3.place(x=340, y=430)
    btn_4 = tk.Button(window, text=BUTTON_4)
    btn_4.place(x=340, y=460)
    btn_5 = tk.Button(window, text=BUTTON_5)
    btn_5.place(x=340, y=490)
    window.mainloop()

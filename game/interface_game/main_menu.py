import tkinter as tk

from interface.frame import MainPage
from interface_game.heroes.training_heroes import traning_hero
from interface_game.texts.menu_messages import (BUTTON_1, BUTTON_2, BUTTON_3,
                                                BUTTON_4, BUTTON_5, HELLO)
from interface_game.texts.training_messages import (BACK, NEW_TRAINING,
                                                    NEW_TRAINING_BT_1,
                                                    NEW_TRAINING_BT_2,
                                                    NEW_TRAINING_BT_3,
                                                    NEW_TRAINING_BT_4)
from interface_game.trainings.chose_enemy import TrainingEnemyMenu
from interface_game.weapons.training_weapons import (training_bow,
                                                     training_stave,
                                                     traning_sword)
from PIL import Image, ImageTk


class MainMenuPage(MainPage):
    '''Главное меню.'''
    def __init__(self, parent, controller):
        super().__init__(parent)
        load = Image.open('interface/image/main_menu_image.png')
        menu_image = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=menu_image)
        img.image = menu_image
        img.place(relx=.5, y=210, anchor='center')
        menu = tk.Label(
            self, text=HELLO, font=('Arial', 15),
            bg='black', fg='white'
            )
        menu.place(relx=.5, y=320, anchor='center')
        btn_1 = tk.Button(
            self, text=BUTTON_1,
            command=lambda: controller.show_frame(TrainingMenuPage)
            )
        btn_1.place(relx=.5, y=370, anchor='center')
        btn_2 = tk.Button(
            self, text=BUTTON_2
            )
        btn_2.place(relx=.5, y=400, anchor='center')
        btn_3 = tk.Button(
            self, text=BUTTON_3
            )
        btn_3.place(relx=.5, y=430, anchor='center')
        btn_4 = tk.Button(
            self, text=BUTTON_4
            )
        btn_4.place(relx=.5, y=460, anchor='center')
        btn_5 = tk.Button(
            self, text=BUTTON_5,
            command=controller.close_window
            )
        btn_5.place(relx=.5, y=490, anchor='center')


class TrainingMenuPage(MainPage):
    '''Меню тренировки.'''
    def __init__(self, parent, controller):
        super().__init__(parent)
        Label = tk.Label(
            self, text=NEW_TRAINING,
            font=('Arial Bold', 15),
            bg='black', fg='white'
        )
        Label.place(relx=.5, y=320, anchor='center')

        btn_1 = tk.Button(
            self, text=NEW_TRAINING_BT_1,
            command=lambda: controller.show_frame(TrainingEnemyMenu)
        )
        btn_1.place(relx=.5, y=370, anchor='center')
        btn_2 = tk.Button(
            self, text=NEW_TRAINING_BT_2,
            command=lambda: controller.show_frame(InfoHeroPage)
            )
        btn_2.place(relx=.5, y=400, anchor='center')
        btn_3 = tk.Button(
            self, text=NEW_TRAINING_BT_3,
            command=lambda: controller.show_frame(InfoWeaponsHeroPage)
            )
        btn_3.place(relx=.5, y=430, anchor='center')
        btn_4 = tk.Button(
            self, text=NEW_TRAINING_BT_4,
            command=lambda: controller.show_frame(MainMenuPage)
            )
        btn_4.place(relx=.5, y=460, anchor='center')


class InfoHeroPage(MainPage):
    '''Информация о герое.'''
    def __init__(self, parent, controller):
        super().__init__(parent)
        Label = tk.Label(
            self, text=f'{traning_hero}',
            font=('Arial Bold', 15),
            bg='black', fg='white'
        )
        Label.place(relx=.5, y=320, anchor='center')

        btn = tk.Button(
            self, text=BACK,
            command=lambda: controller.show_frame(TrainingMenuPage)
        )
        btn.place(relx=.5, y=500, anchor='center')


class InfoWeaponsHeroPage(MainPage):
    '''Инвентарь.'''
    def __init__(self, parent, controller):
        super().__init__(parent)
        Label = tk.Label(
            self, text=(f'''
{traning_sword}
{training_bow}
{training_stave}'''),
            font=('Arial Bold', 15),
            bg='black', fg='white'
        )
        Label.place(relx=.5, y=220, anchor='center')

        btn = tk.Button(
            self, text=BACK,
            command=lambda: controller.show_frame(TrainingMenuPage)
        )
        btn.place(relx=.5, y=500, anchor='center')

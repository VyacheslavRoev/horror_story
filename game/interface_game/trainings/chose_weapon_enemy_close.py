import tkinter as tk

from interface.frame import MainPage
from interface_game.texts.training_messages import (GET_TRAINING_WEAPON,
                                                    GET_TRAINING_WEAPON_BT_1,
                                                    GET_TRAINING_WEAPON_BT_2,
                                                    GET_TRAINING_WEAPON_BT_3,
                                                    NEW_WEAPON, NEXT)
from interface_game.weapons.training_weapons import list_training_weapons


class WeaponHeroPageEnemyClose(MainPage):
    '''Выбор тренировочного оружия героя
    (противник ближнего боя).'''
    def __init__(self, parent, controller):
        super().__init__(parent)
        Label = tk.Label(
            self, text=GET_TRAINING_WEAPON,
            font=('Arial Bold', 15),
            bg='black', fg='white'
        )
        Label.place(relx=.5, y=50, anchor='center')
        btn_1 = tk.Button(
            self, text=GET_TRAINING_WEAPON_BT_1,
            command=lambda: controller.show_frame(
                TrainingWeaponCloseEnemyClose
            )
        )
        btn_1.place(relx=.2, y=500, anchor='center')
        btn_2 = tk.Button(
            self, text=GET_TRAINING_WEAPON_BT_2,
            command=lambda: controller.show_frame(
                TrainingWeaponRangedEnemyClose
            )
        )
        btn_2.place(relx=.5, y=500, anchor='center')
        btn_3 = tk.Button(
            self, text=GET_TRAINING_WEAPON_BT_3,
            command=lambda: controller.show_frame(
                TrainingWeaponMagicEnemyClose
            )
        )
        btn_3.place(relx=.8, y=500, anchor='center')


class TrainingWeaponCloseEnemyClose(MainPage):
    '''Оружие ближнего боя
    (противник ближнего боя).'''
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.hero_weapon = list_training_weapons[0]
        Label = tk.Label(
            self, text=(f'''
Вы выбрали:
{self.hero_weapon}
'''),
            font=('Arial Bold', 15),
            bg='black', fg='white'
        )
        Label.place(relx=.5, y=300, anchor='center')
        btn_1 = tk.Button(
            self, text=NEXT
            )
        btn_1.place(relx=.75, y=500, anchor='center')
        btn_2 = tk.Button(
            self, text=NEW_WEAPON,
            command=lambda: controller.show_frame(WeaponHeroPageEnemyClose)
            )
        btn_2.place(relx=.25, y=500, anchor='center')


class TrainingWeaponRangedEnemyClose(MainPage):
    '''Оружие дальнего боя
    (противник ближнего боя).'''
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.hero_weapon = list_training_weapons[1]
        Label = tk.Label(
            self, text=(f'''
Вы выбрали:
{self.hero_weapon}
'''),
            font=('Arial Bold', 15),
            bg='black', fg='white'
        )
        Label.place(relx=.5, y=300, anchor='center')
        btn_1 = tk.Button(
            self, text=NEXT
            )
        btn_1.place(relx=.75, y=500, anchor='center')
        btn_2 = tk.Button(
            self, text=NEW_WEAPON,
            command=lambda: controller.show_frame(WeaponHeroPageEnemyClose)
            )
        btn_2.place(relx=.25, y=500, anchor='center')


class TrainingWeaponMagicEnemyClose(MainPage):
    '''Магическое оружие
    (противник ближнего боя).'''
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.hero_weapon = list_training_weapons[2]
        Label = tk.Label(
            self, text=(f'''
Вы выбрали:
{self.hero_weapon}
'''),
            font=('Arial Bold', 15),
            bg='black', fg='white'
        )
        Label.place(relx=.5, y=300, anchor='center')
        btn_1 = tk.Button(
            self, text=NEXT
            )
        btn_1.place(relx=.75, y=500, anchor='center')
        btn_2 = tk.Button(
            self, text=NEW_WEAPON,
            command=lambda: controller.show_frame(WeaponHeroPageEnemyClose)
            )
        btn_2.place(relx=.25, y=500, anchor='center')

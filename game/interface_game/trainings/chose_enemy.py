import tkinter as tk

from interface.frame import MainPage
from interface_game.battles.close_combat.preparing_for_battle import \
    get_close_weapon
from interface_game.battles.magic_combat.preparing_for_battle import \
    get_magic_weapon
from interface_game.battles.ranged_combat.preparing_for_battle import \
    get_ranged_weapon
from interface_game.enemies.training_enemy import list_training_enemy
from interface_game.heroes.training_heroes import traning_hero
from interface_game.random_number_func import random_phrase
from interface_game.texts.actions import COMMAND, ERROR_LIST, FAIL, FINISH
from interface_game.texts.attack_messages import WEAPON_FAIL
from interface_game.texts.training_messages import (GET_ENEMY, GET_ENEMY_BT_1,
                                                    GET_ENEMY_BT_2,
                                                    GET_ENEMY_BT_3,
                                                    GET_TRAINING_WEAPON,
                                                    GET_TRAINING_WEAPON_BT_1,
                                                    GET_TRAINING_WEAPON_BT_2,
                                                    GET_TRAINING_WEAPON_BT_3)
from interface_game.weapons.training_weapons import list_enemy_training_weapons

from .chose_weapon_enemy_close import (TrainingWeaponCloseEnemyClose,
                                       TrainingWeaponMagicEnemyClose,
                                       TrainingWeaponRangedEnemyClose)
from .chose_weapon_enemy_magic import (TrainingWeaponCloseEnemyMagic,
                                       TrainingWeaponMagicEnemyMagic,
                                       TrainingWeaponRangedEnemyMagic)
from .chose_weapon_enemy_ranged import (TrainingWeaponCloseEnemyRanged,
                                        TrainingWeaponMagicEnemyRanged,
                                        TrainingWeaponRangedEnemyRanged)


def get_training_enemy_and_weapon_close():
    """Выбор противника."""
    enemy = list_training_enemy[0]
    weapon = list_enemy_training_weapons[0]
    return enemy, weapon


def get_training_enemy_and_weapon_ranged():
    """Выбор противника."""
    enemy = list_training_enemy[1]
    weapon = list_enemy_training_weapons[1]
    return enemy, weapon


def get_training_enemy_and_weapon_magic():
    """Выбор противника."""
    enemy = list_training_enemy[2]
    weapon = list_enemy_training_weapons[2]
    return enemy, weapon


def repeat_traning(enemy, weapon):
    """Повтор тренировки."""
    traning_hero.health = 300
    enemy.health = 250
    weapon.durability = 500
    weapon.ammunition = 10


def training(enemy, weapon, max_health_enemy):
    """Тренировка."""
    new_traning = ''
    while new_traning != '0':
        if weapon.durability <= 0:
            print(WEAPON_FAIL, END_TRAINING)
            return repeat_traning(enemy, weapon)
        if weapon.ammunition <= 0:
            print(training_bow.not_ammunition())
            return repeat_traning(enemy, weapon)
        print(MESSAGE_NEW_TRAINING)
        print(GET_TRAINING_WEAPON)
        new_traning = input(COMMAND)
        if new_traning == '1':
            fin = get_close_weapon(
                new_traning, traning_hero,
                enemy, weapon, max_health_enemy, traning_inventary)
            if fin == FINISH or fin == FAIL:
                return repeat_traning(enemy, weapon)
        if new_traning == '2':
            fin = get_ranged_weapon(
                new_traning, traning_hero,
                enemy, weapon, max_health_enemy, traning_inventary)
            if fin == FINISH or fin == FAIL:
                return repeat_traning(enemy, weapon)
        if new_traning == '3':
            fin = get_magic_weapon(
                new_traning, traning_hero,
                enemy, weapon, max_health_enemy, traning_inventary
            )
            if fin == FINISH or fin == FAIL:
                return repeat_traning(enemy, weapon)
        if new_traning == '0':
            print(END_TRAINING)
        else:
            print(random_phrase(ERROR_LIST))


class TrainingEnemyMenu(MainPage):
    '''Выбор противника для тренировки.'''
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        Label = tk.Label(
            self, text=GET_ENEMY,
            font=('Arial Bold', 15),
            bg='black', fg='white'
        )
        Label.place(relx=.5, y=50, anchor='center')
        btn_1 = tk.Button(
            self, text=GET_ENEMY_BT_1,
            command=lambda: controller.show_frame(TrainingEnemyClose)
        )
        btn_1.place(relx=.2, y=500, anchor='center')
        btn_2 = tk.Button(
            self, text=GET_ENEMY_BT_2,
            command=lambda: controller.show_frame(TrainingEnemyRanged)
            )
        btn_2.place(relx=.5, y=500, anchor='center')
        btn_3 = tk.Button(
            self, text=GET_ENEMY_BT_3,
            command=lambda: controller.show_frame(TrainingEnemyMagic)
            )
        btn_3.place(relx=.8, y=500, anchor='center')


class TrainingEnemyClose(MainPage):
    '''Противник с оружием ближнего боя.'''
    def __init__(self, parent, controller):
        super().__init__(parent)
        enemy, weapon = get_training_enemy_and_weapon_close()
        self.enemy = enemy
        self.weapon = weapon
        Label = tk.Label(
            self, text=(f'''
Ваш противник - {enemy}
Его оружие: {weapon.get_weapon_enemy()}
Расстояние до противнике - {enemy.lenght}
'''),
            font=('Arial Bold', 15),
            bg='black', fg='white'
        )
        Label.place(relx=.5, y=100, anchor='center')
        Label = tk.Label(
            self, text=GET_TRAINING_WEAPON,
            font=('Arial Bold', 15),
            bg='black', fg='white'
        )
        Label.place(relx=.5, y=200, anchor='center')
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


class TrainingEnemyRanged(MainPage):
    '''Противник с оружием дальнего боя.'''
    def __init__(self, parent, controller):
        super().__init__(parent)
        enemy, weapon = get_training_enemy_and_weapon_ranged()
        self.enemy = enemy
        self.weapon = weapon
        Label = tk.Label(
            self, text=(f'''
Ваш противник - {enemy}
Его оружие: {weapon.get_weapon_enemy()}
Расстояние до противнике - {enemy.lenght}
'''),
            font=('Arial Bold', 15),
            bg='black', fg='white'
        )
        Label.place(relx=.5, y=100, anchor='center')
        Label = tk.Label(
            self, text=GET_TRAINING_WEAPON,
            font=('Arial Bold', 15),
            bg='black', fg='white'
        )
        Label.place(relx=.5, y=200, anchor='center')
        btn_1 = tk.Button(
            self, text=GET_TRAINING_WEAPON_BT_1,
            command=lambda: controller.show_frame(
                TrainingWeaponCloseEnemyRanged
            )
        )
        btn_1.place(relx=.2, y=500, anchor='center')
        btn_2 = tk.Button(
            self, text=GET_TRAINING_WEAPON_BT_2,
            command=lambda: controller.show_frame(
                TrainingWeaponRangedEnemyRanged
            )
        )
        btn_2.place(relx=.5, y=500, anchor='center')
        btn_3 = tk.Button(
            self, text=GET_TRAINING_WEAPON_BT_3,
            command=lambda: controller.show_frame(
                TrainingWeaponMagicEnemyRanged
            )
        )
        btn_3.place(relx=.8, y=500, anchor='center')


class TrainingEnemyMagic(MainPage):
    '''Противник с магическим оружием.'''
    def __init__(self, parent, controller):
        super().__init__(parent)
        enemy, weapon = get_training_enemy_and_weapon_magic()
        self.enemy = enemy
        self.weapon = weapon
        Label = tk.Label(
            self, text=(f'''
Ваш противник - {enemy}
Его оружие: {weapon.get_weapon_enemy()}
Расстояние до противнике - {enemy.lenght}
'''),
            font=('Arial Bold', 15),
            bg='black', fg='white'
        )
        Label.place(relx=.5, y=100, anchor='center')
        Label = tk.Label(
            self, text=GET_TRAINING_WEAPON,
            font=('Arial Bold', 15),
            bg='black', fg='white'
        )
        Label.place(relx=.5, y=200, anchor='center')
        btn_1 = tk.Button(
            self, text=GET_TRAINING_WEAPON_BT_1,
            command=lambda: controller.show_frame(
                TrainingWeaponCloseEnemyMagic
            )
        )
        btn_1.place(relx=.2, y=500, anchor='center')
        btn_2 = tk.Button(
            self, text=GET_TRAINING_WEAPON_BT_2,
            command=lambda: controller.show_frame(
                TrainingWeaponRangedEnemyMagic
            )
        )
        btn_2.place(relx=.5, y=500, anchor='center')
        btn_3 = tk.Button(
            self, text=GET_TRAINING_WEAPON_BT_3,
            command=lambda: controller.show_frame(
                TrainingWeaponMagicEnemyMagic
            )
        )
        btn_3.place(relx=.8, y=500, anchor='center')

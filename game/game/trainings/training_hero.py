from game.battles.close_combat.preparing_for_battle import get_close_weapon
from game.battles.magic_combat.preparing_for_battle import get_magic_weapon
from game.battles.ranged_combat.preparing_for_battle import get_ranged_weapon
from game.enemies.training_enemy import get_training_enemy
from game.heroes.inventary_hero import list_inventary
from game.heroes.training_heroes import traning_hero
from game.random_number_func import random_phrase
from game.texts.actions import COMMAND, ERROR_LIST, FINISH, FAIL
from game.texts.attack_messages import WEAPON_FAIL
from game.texts.training_messages import (END_TRAINING, GET_ENEMY,
                                          GET_TRAINING_WEAPON,
                                          MESSAGE_NEW_TRAINING, NEW_TRAINING)
from game.weapons.training_weapons import (get_enemy_training_weapons,
                                           training_bow, training_stave,
                                           traning_sword)

traning_inventary = [traning_sword, training_bow, training_stave]


def get_training_enemy_and_weapon():
    """Выбор противника."""
    print(GET_ENEMY)
    index = input(COMMAND)
    while index not in ['1', '2', '3']:
        print(random_phrase(ERROR_LIST))
        print(GET_ENEMY)
        index = input(COMMAND)
    enemy = get_training_enemy(int(index))
    weapon = get_enemy_training_weapons(int(index))
    return enemy, weapon


def repeat_traning(enemy, weapon):
    """Повтор тренировки."""
    traning_hero.health = 300
    traning_sword.durability = 500
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


def traning_menu():
    """Меню тренировки."""
    command_traning = ''
    while command_traning != '0':
        print(NEW_TRAINING)
        command_traning = input(COMMAND)
        if command_traning == '1':
            enemy, weapon = get_training_enemy_and_weapon()
            max_health_enemy = enemy.max_health()
            print(
                f'''
Ваш противник - {enemy}
Его оружие - {weapon.get_weapon_enemy()}
Расстояние до противнике - {enemy.lenght}
''')
            training(enemy, weapon, max_health_enemy)
        elif command_traning == '2':
            print(f'{traning_hero}')
        elif command_traning == '3':
            list_inventary(traning_inventary)
        elif command_traning == '0':
            print(END_TRAINING)
        else:
            print(random_phrase(ERROR_LIST))

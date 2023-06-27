from battles.close_combat.preparing_for_battle import get_close_weapon
from battles.magic_combat.preparing_for_battle import get_magic_weapon
from battles.ranged_combat.preparing_for_battle import get_ranged_weapon
from enemies.training_enemy import get_training_enemy
from heroes.inventary_hero import list_inventary
from heroes.training_heroes import traning_hero
from texts.actions import COMMAND, ERROR, FINISH
from texts.attack_messages import WEAPON_FAIL
from texts.training_messages import (END_TRAINING, GET_ENEMY,
                                     GET_TRAINING_WEAPON, MESSAGE_NEW_TRAINING,
                                     NEW_TRAINING)
from weapons.training_weapons import (get_enemy_training_weapons, training_bow,
                                      traning_sword)


def get_training_enemy_and_weapon(index):
    """Выбор противника."""
    if index == 1 or index == 2 or index == 3:
        enemy = get_training_enemy(index)
        weapon = get_enemy_training_weapons(index)
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
    while new_traning != 0:
        if weapon.durability <= 0:
            print(WEAPON_FAIL, END_TRAINING)
            return repeat_traning(enemy, weapon)
        if weapon.ammunition <= 0:
            print(training_bow.not_ammunition())
            return repeat_traning(enemy, weapon)
        print(MESSAGE_NEW_TRAINING)
        print(GET_TRAINING_WEAPON)
        new_traning = int(input(COMMAND))
        if new_traning == 1:
            fin = get_close_weapon(
                new_traning, traning_hero,
                enemy, weapon, max_health_enemy)
            if fin == FINISH:
                return repeat_traning(enemy, weapon)
        if new_traning == 2:
            fin = get_ranged_weapon(
                new_traning, traning_hero,
                enemy, weapon, max_health_enemy)
            if fin == FINISH:
                return repeat_traning(enemy, weapon)
        if new_traning == 3:
            fin = get_magic_weapon(
                new_traning, traning_hero,
                enemy, weapon, max_health_enemy
            )
            if fin == FINISH:
                return repeat_traning(enemy, weapon)
        if new_traning == 0:
            print(END_TRAINING)
        else:
            print(ERROR)


def traning_menu():
    """Меню тренировки."""
    command_traning = ''
    while command_traning != 0:
        print(NEW_TRAINING)
        command_traning = int(input(COMMAND))
        if command_traning == 1:
            print(GET_ENEMY)
            new_enemy = int(input(COMMAND))
            enemy, weapon = get_training_enemy_and_weapon(new_enemy)
            max_health_enemy = enemy.max_health()
            print(
                f'''
Ваш противник - {enemy}
Его оружие - {weapon.get_weapon_enemy()}
Расстояние до противнике - {enemy.lenght}
''')
            training(enemy, weapon, max_health_enemy)
        elif command_traning == 2:
            print(f'{traning_hero}')
        elif command_traning == 3:
            list_inventary()
        elif command_traning == 0:
            print(END_TRAINING)
        else:
            print(ERROR)

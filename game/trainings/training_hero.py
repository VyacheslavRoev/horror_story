from battles.close_combat.attack import get_close_weapon
from battles.ranged_combat.attack import get_ranged_weapon
from battles.magic_combat.attack import get_magic_weapon
from enemies.training_enemy import get_training_enemy
from weapons.training_weapons import get_enemy_training_weapons
from heroes.inventary_hero import list_inventary
from heroes.training_heroes import traning_hero
from texts.actions import HERO, INVENTARY
from texts.attack_messages import WEAPON_FAIL
from texts.training_messages import (COMMAND, END_TRAINING,
                                     MESSAGE_NEW_TRAINING,
                                     MESSAGE_REPEAT_TRAINING, NEW_TRAINING, NO,
                                     YES, GET_ENEMY, GET_TRAINING_WEAPON)
from weapons.training_weapons import training_bow, traning_sword


def get_training_enemy_and_weapon(index):
    if index == 1 or index == 2 or index == 3:
        enemy = get_training_enemy(index)
        weapon = get_enemy_training_weapons(index)
        return enemy, weapon


def repeat_traning(enemy, weapon):
    """Повтор тренировки."""
    print(MESSAGE_REPEAT_TRAINING)
    new_traning = input()
    if new_traning == YES:
        traning_hero.health = 300
        traning_sword.durability = 500
        enemy.health = 250
        weapon.durability = 500
        return traning()
    if new_traning == NO:
        return


def traning():
    """Функция тренировки."""
    print(NEW_TRAINING)
    new_traning = input()
    if new_traning == YES:
        print(GET_ENEMY)
        new_enemy = int(input())
        enemy, weapon = get_training_enemy_and_weapon(new_enemy)
        print(f'Ваш противник - {enemy}')
        print(f'Его оружие - {weapon}')
        print(MESSAGE_NEW_TRAINING)
        while new_traning != NO:
            if enemy.health <= 0:
                return repeat_traning(enemy, weapon)
            if traning_hero.health <= 0:
                return repeat_traning(enemy, weapon)
            if weapon.durability <= 0:
                print(WEAPON_FAIL, END_TRAINING)
                return repeat_traning(enemy, weapon)
            if weapon.ammunition <= 0:
                print(training_bow.not_ammunition())
                return repeat_traning()
            print(GET_TRAINING_WEAPON)
            new_traning = input(COMMAND)
            if new_traning == '1':
                get_close_weapon(
                    new_traning, traning_hero,
                    enemy, weapon)
            elif new_traning == '2':
                get_ranged_weapon(
                    new_traning, traning_hero,
                    enemy, weapon)
            elif new_traning == '3':
                get_magic_weapon(
                    new_traning, traning_hero,
                    enemy, weapon
                )
            elif new_traning == HERO:
                print(f'{traning_hero}')
            elif new_traning == INVENTARY:
                list_inventary()
    return print(END_TRAINING)

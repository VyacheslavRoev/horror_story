from battles.close_combat.attack import get_close_weapon
from battles.ranged_combat.attack import get_ranged_weapon
from battles.magic_combat.attack import get_magic_weapon
from enemies.list_enemies_lev_1 import training_enemy
from heroes.inventary_hero import list_inventary
from heroes.list_heroes import traning_hero
from texts.actions import ENDURANCE, HERO, INVENTARY
from texts.attack_messages import WEAPON_FAIL
from texts.training_messages import (COMMAND, END_TRAINING,
                                     MESSAGE_NEW_TRAINING,
                                     MESSAGE_REPEAT_TRAINING, NEW_TRAINING, NO,
                                     YES)
from weapons.list_weapons_lev_1 import (training_bow, traning_sword,
                                        traning_sword_2)


def repeat_traning():
    """Повтор тренировки."""
    print(MESSAGE_REPEAT_TRAINING)
    new_traning = input()
    if new_traning == YES:
        training_enemy.health = 300
        traning_hero.health = 300
        traning_sword.durability = 500
        traning_sword_2.durability = 500
        return traning()
    if new_traning == NO:
        return


def traning():
    """Функция тренировки."""
    print(NEW_TRAINING)
    new_traning = input()
    if new_traning == YES:
        print(MESSAGE_NEW_TRAINING)
        while new_traning != NO:
            if training_enemy.health < 0:
                return repeat_traning()
            if traning_hero.health < 0:
                return repeat_traning()
            if traning_sword.durability <= 0:
                print(WEAPON_FAIL, END_TRAINING)
                return repeat_traning()
            if training_bow.ammunition <= 0:
                print(training_bow.not_ammunition())
                return repeat_traning()
            new_traning = input(COMMAND)
            if new_traning == '1':
                get_close_weapon(
                    new_traning, traning_hero,
                    training_enemy, traning_sword_2)
            elif new_traning == '2':
                get_ranged_weapon(
                    new_traning, traning_hero,
                    training_enemy, traning_sword_2)
            elif new_traning == '3':
                get_magic_weapon(
                    new_traning, traning_hero,
                    training_enemy, traning_sword_2
                )
            elif new_traning == ENDURANCE:
                print(traning_sword.durability)
            elif new_traning == HERO:
                print(f'{traning_hero}')
            elif new_traning == INVENTARY:
                list_inventary()
    return print(END_TRAINING)

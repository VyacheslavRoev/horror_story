from random import randint

from game.random_number_func import random_phrase
from game.texts.create_heroes.name_weapons import WEAPON_NAME, WEAPON_PRENAME
from game.weapons.close_combat.swords import (create_sword_1, create_sword_2,
                                              create_sword_3, create_sword_4)
from game.weapons.magic_combat.staves import (create_stave_1, create_stave_2,
                                              create_stave_3, create_stave_4)
from game.weapons.ranged_combat.bows import (create_bow_1, create_bow_2,
                                             create_bow_3, create_bow_4)


def create_name_weapon():
    prename_weapon = random_phrase(WEAPON_PRENAME)
    name_weapon = random_phrase(WEAPON_NAME)
    weapon_full_name = prename_weapon + ' ' + name_weapon
    return weapon_full_name


def create_weapon_lev_1(weapon_full_name):
    check_weapon = randint(1, 3)
    if check_weapon == 1:
        weapon = create_sword_1(weapon_full_name)
    elif check_weapon == 2:
        weapon = create_bow_1(weapon_full_name)
    else:
        weapon = create_stave_1(weapon_full_name)
    return weapon


def create_weapon_lev_2(weapon_full_name):
    check_weapon = randint(1, 3)
    if check_weapon == 1:
        weapon = create_sword_2(weapon_full_name)
    elif check_weapon == 2:
        weapon = create_bow_2(weapon_full_name)
    else:
        weapon = create_stave_2(weapon_full_name)
    return weapon


def create_weapon_lev_3(weapon_full_name):
    check_weapon = randint(1, 3)
    if check_weapon == 1:
        weapon = create_sword_3(weapon_full_name)
    elif check_weapon == 2:
        weapon = create_bow_3(weapon_full_name)
    else:
        weapon = create_stave_3(weapon_full_name)
    return weapon


def create_weapon_lev_4(weapon_full_name):
    check_weapon = randint(1, 3)
    if check_weapon == 1:
        weapon = create_sword_4(weapon_full_name)
    elif check_weapon == 2:
        weapon = create_bow_4(weapon_full_name)
    else:
        weapon = create_stave_4(weapon_full_name)
    return weapon

from game.weapons.close_combat.swords import create_sword_1, create_sword_2
from game.weapons.magic_combat.staves import create_stave_1, create_stave_2
from game.weapons.ranged_combat.bows import create_bow_1, create_bow_2
from game.texts.create_enemy.enemy_rus import RUS_NAME, RUS_PRENAME
from game.texts.create_heroes.name_weapons import WEAPON_NAME, WEAPON_PRENAME
from random import randint

from game.enemies.create_enemies import create_enemy_lev_1, create_enemy_lev_2
from game.random_number_func import random_phrase


def preparation_enemy_1():
    """Подготовка противника 1 уровня."""
    prename_enemy = random_phrase(RUS_PRENAME)
    name_enemy = random_phrase(RUS_NAME)
    full_name = prename_enemy + ' ' + name_enemy
    enemy = create_enemy_lev_1(full_name)
    prename_weapon = random_phrase(WEAPON_PRENAME)
    name_weapon = random_phrase(WEAPON_NAME)
    weapon_full_name = prename_weapon + ' ' + name_weapon
    check_weapon = randint(1, 3)
    if check_weapon == 1:
        weapon = create_sword_1(weapon_full_name)
    elif check_weapon == 2:
        weapon = create_bow_1(weapon_full_name)
    else:
        weapon = create_stave_1(weapon_full_name)
    return enemy, weapon


def preparation_enemy_2():
    """Подготовка противника 2 уровня."""
    prename_enemy = random_phrase(RUS_PRENAME)
    name_enemy = random_phrase(RUS_NAME)
    full_name = prename_enemy + ' ' + name_enemy
    enemy = create_enemy_lev_2(full_name)
    prename_weapon = random_phrase(WEAPON_PRENAME)
    name_weapon = random_phrase(WEAPON_NAME)
    weapon_full_name = prename_weapon + ' ' + name_weapon
    check_weapon = randint(1, 3)
    if check_weapon == 1:
        weapon = create_sword_2(weapon_full_name)
    elif check_weapon == 2:
        weapon = create_bow_2(weapon_full_name)
    else:
        weapon = create_stave_2(weapon_full_name)
    return enemy, weapon

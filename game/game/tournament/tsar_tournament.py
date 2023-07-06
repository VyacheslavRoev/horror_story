from random import randint

from game.enemies.create_enemies import create_enemy_lev_1
from game.random_number_func import random_phrase
from game.texts.actions import FINISH
from game.texts.create_enemy.enemy_rus import RUS_NAME, RUS_PRENAME
from game.texts.create_heroes.name_weapons import WEAPON_NAME, WEAPON_PRENAME
from game.texts.tournament_messages import FAIL_DAY_1, WIN_DAY_1
from game.texts.tsar_tournament_message import BEGIN_TOURNAMENT
from game.weapons.close_combat.swords import create_sword_1
from game.weapons.magic_combat.staves import create_stave_1
from game.weapons.ranged_combat.bows import create_bow_1
from .course_of_tournament import battle, break_battle


def preparation_enemy():
    """Подготовка противника."""
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


def tsar_tournament_day_1(hero, hero_weapon):
    """Царский турнир, день 1"""
    enemy, enemy_weapon = preparation_enemy()
    max_health_enemy = enemy.max_health()
    print(
        f'''
{BEGIN_TOURNAMENT}
Ваш противник - {enemy}
Его оружие - {enemy_weapon.get_weapon_enemy()}
Расстояние до противнике - {enemy.lenght}
''')
    fin = battle(
        hero, hero_weapon, enemy, enemy_weapon,
        max_health_enemy
        )
    return fin


def tsar_tournament_day_2(hero, hero_weapon, max_health_hero):
    print('ДЕНЬ 2', max_health_hero)
    print(hero)
    print(hero_weapon[0])
    print(hero_weapon[1])
    print(hero_weapon)


def tsar_tournament_begin(hero, hero_weapon):
    max_health_hero = hero.max_health()
    day_1 = tsar_tournament_day_1(hero, hero_weapon)
    if day_1 == FINISH:
        print(WIN_DAY_1)
    else:
        print(FAIL_DAY_1)
        return
    break_battle(hero, hero_weapon, max_health_hero)
    day_2 = tsar_tournament_day_2(hero, hero_weapon, max_health_hero)

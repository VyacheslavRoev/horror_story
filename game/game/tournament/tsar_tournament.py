from random import randint

from game.texts.actions import FINISH
from game.texts.tournament_messages import (DAY_2, FAIL_DAY_1, FAIL_DAY_2,
                                            WIN_DAY_1, WIN_DAY_2)
from game.texts.tsar_tournament_message import BEGIN_TOURNAMENT

from .course_of_tournament import battle, break_battle
from .enemies_rus import preparation_enemy_1, preparation_enemy_2


def tsar_tournament_day_1(hero, hero_weapon):
    """Царский турнир, день 1"""
    enemy, enemy_weapon = preparation_enemy_1()
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


def tsar_tournament_day_2(hero, hero_weapon):
    """Царский турнир, день 2"""
    random_enemy = randint(1, 2)
    if random_enemy == 1:
        enemy, enemy_weapon = preparation_enemy_1()
    else:
        enemy, enemy_weapon = preparation_enemy_2()
    max_health_enemy = enemy.max_health()
    print(
        f'''
{DAY_2}
Ваш противник - {enemy}
Его оружие - {enemy_weapon.get_weapon_enemy()}
Расстояние до противнике - {enemy.lenght}
''')
    fin = battle(
        hero, hero_weapon, enemy, enemy_weapon,
        max_health_enemy
        )
    return fin


def tsar_tournament_begin(hero, hero_weapon):
    """Начало царского турнира."""
    max_health_hero = hero.max_health()
    day_1 = tsar_tournament_day_1(hero, hero_weapon)
    if day_1 == FINISH:
        print(WIN_DAY_1)
    else:
        print(FAIL_DAY_1)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)
    day_2 = tsar_tournament_day_2(hero, hero_weapon)
    if day_2 == FINISH:
        print(WIN_DAY_2)
    else:
        print(FAIL_DAY_2)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)

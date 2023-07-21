from game.enemies.base_enemy import BaseEnemy
from game.random_number_func import random_phrase
from game.texts.actions import COMMAND, ERROR_LIST, FINISH, ONE
from game.texts.koschei_tournament_messages import (BEGIN_TOURNAMENT,
                                                    FINAL_TOURNAMENT)
from game.texts.tournament_messages import (DAY_2, DAY_3, DAY_4, DAY_5, DAY_6,
                                            DAY_7, FAIL_DAY_1, FAIL_DAY_2,
                                            FAIL_DAY_3, FAIL_DAY_4, FAIL_DAY_5,
                                            FAIL_DAY_6, FAIL_DAY_7, WIN_DAY_1,
                                            WIN_DAY_2, WIN_DAY_3, WIN_DAY_4,
                                            WIN_DAY_5, WIN_DAY_6, WIN_DAY_7)
from game.weapons.close_combat.swords import SimpleSword
from game.weapons.magic_combat.staves import SimpleStave
from game.weapons.ranged_combat.bows import SimpleBow

from .course_of_tournament import (battle, break_battle,
                                   new_tournament_break_battle)
from .gifts.koschei_gift import koschei_tournament_gift


def koschei_tournament_day_1(hero, hero_weapon):
    """Финальный турнир, день 1"""
    enemy = BaseEnemy('Царский Воевода', 1200, 50, 50, 50, 15, 0, 1, 250, 8)
    enemy_weapon = SimpleSword('Ясный Сокол',
                               'воронёная сталь', 40, 15)
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


def koschei_tournament_day_2(hero, hero_weapon):
    """Финальный турнир, день 2"""
    enemy = BaseEnemy('Маршал Тевтонского ордена', 1200, 50, 50,
                      50, 10, 0, 1, 250, 8)
    enemy_weapon = SimpleSword('Огненный глаз',
                               'закалённая сталь', 40, 15)
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


def koschei_tournament_day_3(hero, hero_weapon):
    """Финальный турнир, день 3"""
    enemy = BaseEnemy('Половецкий наместник', 1200, 50, 50,
                      50, 10, 0, 15, 250, 8)
    enemy_weapon = SimpleBow('Бегущий жеребец',
                             'кость', 30, 20, 15)
    max_health_enemy = enemy.max_health()
    print(
        f'''
{DAY_3}
Ваш противник - {enemy}
Его оружие - {enemy_weapon.get_weapon_enemy()}
Расстояние до противнике - {enemy.lenght}
''')
    fin = battle(
        hero, hero_weapon, enemy, enemy_weapon,
        max_health_enemy
        )
    return fin


def koschei_tournament_day_4(hero, hero_weapon):
    """Финальный турнир, день 4"""
    enemy = BaseEnemy('Легионер ветеран', 1200, 60, 60,
                      60, 20, 0, 1, 250, 8)
    enemy_weapon = SimpleSword('Гроза варваров',
                               'чёрная сталь', 50, 15)
    max_health_enemy = enemy.max_health()
    print(
        f'''
{DAY_4}
Ваш противник - {enemy}
Его оружие - {enemy_weapon.get_weapon_enemy()}
Расстояние до противнике - {enemy.lenght}
''')
    fin = battle(
        hero, hero_weapon, enemy, enemy_weapon,
        max_health_enemy
        )
    return fin


def koschei_tournament_day_5(hero, hero_weapon):
    """Финальный турнир, день 5"""
    enemy = BaseEnemy('Персидский верховный маг', 1200, 50, 50,
                      50, 50, 50, 15, 250, 8)
    enemy_weapon = SimpleStave(
        'Пляшущий чёрт',
        'кость с навершием из козлиного черепа',
        30, 15)
    max_health_enemy = enemy.max_health()
    print(
        f'''
{DAY_5}
Ваш противник - {enemy}
Его оружие - {enemy_weapon.get_weapon_enemy()}
Расстояние до противнике - {enemy.lenght}
''')
    fin = battle(
        hero, hero_weapon, enemy, enemy_weapon,
        max_health_enemy
        )
    return fin


def koschei_tournament_day_6(hero, hero_weapon):
    """Финальный турнир, день 6"""
    enemy = BaseEnemy('Буян Непобедимый', 1300, 70, 70,
                      70, 70, 70, 15, 250, 8)
    enemy_weapon = SimpleSword('Гроза имперцев',
                               'чёрная сталь', 40, 15)
    max_health_enemy = enemy.max_health()
    print(
        f'''
{DAY_6}
Ваш противник - {enemy}
Его оружие - {enemy_weapon.get_weapon_enemy()}
Расстояние до противнике - {enemy.lenght}
''')
    fin = battle(
        hero, hero_weapon, enemy, enemy_weapon,
        max_health_enemy
        )
    return fin


def koschei_tournament_day_7(hero, hero_weapon):
    """Финальный турнир, день 7"""
    enemy = BaseEnemy('Одноглазый лич', 1200, 50, 50,
                      50, 50, 50, 15, 250, 8)
    enemy_weapon = SimpleStave(
        'Чёрная смерть',
        'человеческая кость с навершием из черепа',
        40, 15)
    max_health_enemy = enemy.max_health()
    print(
        f'''
{DAY_7}
Ваш противник - {enemy}
Его оружие - {enemy_weapon.get_weapon_enemy()}
Расстояние до противнике - {enemy.lenght}
''')
    fin = battle(
        hero, hero_weapon, enemy, enemy_weapon,
        max_health_enemy
        )
    return fin


def koschei_tournament_final(hero, max_health_hero):
    """Финал турнира."""
    hero.health = max_health_hero
    command = ''
    print(FINAL_TOURNAMENT)
    print('1 - Продолжить')
    command = input()
    while command != '1':
        print(random_phrase(ERROR_LIST))
        print(ONE)
        command = input(COMMAND)
    koschei_tournament_gift(hero, max_health_hero)


def koschei_tournament_begin(hero, hero_weapon):
    """Ход Финального турнира."""
    hero, hero_weapon = new_tournament_break_battle(hero,
                                                    hero_weapon)
    max_health_hero = hero.max_health()
    day_1 = koschei_tournament_day_1(hero, hero_weapon)
    if day_1 == FINISH:
        print(WIN_DAY_1)
    else:
        print(FAIL_DAY_1)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)

    day_2 = koschei_tournament_day_2(hero, hero_weapon)
    if day_2 == FINISH:
        print(WIN_DAY_2)
    else:
        print(FAIL_DAY_2)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)

    day_3 = koschei_tournament_day_3(hero, hero_weapon)
    if day_3 == FINISH:
        print(WIN_DAY_3)
    else:
        print(FAIL_DAY_3)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)

    day_4 = koschei_tournament_day_4(hero, hero_weapon)
    if day_4 == FINISH:
        print(WIN_DAY_4)
    else:
        print(FAIL_DAY_4)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)

    day_5 = koschei_tournament_day_5(hero, hero_weapon)
    if day_5 == FINISH:
        print(WIN_DAY_5)
    else:
        print(FAIL_DAY_5)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)

    day_6 = koschei_tournament_day_6(hero, hero_weapon)
    if day_6 == FINISH:
        print(WIN_DAY_6)
    else:
        print(FAIL_DAY_6)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)

    day_7 = koschei_tournament_day_7(hero, hero_weapon)
    if day_7 == FINISH:
        print(WIN_DAY_7)
    else:
        print(FAIL_DAY_7)
        return

    koschei_tournament_final(hero, max_health_hero)

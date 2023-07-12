from random import randint

from game.enemies.base_enemy import BaseEnemy
from game.texts.actions import COMMAND, FINISH
from game.texts.tournament_messages import (DAY_2, DAY_3, DAY_4, DAY_5, DAY_6,
                                            DAY_7, FAIL_DAY_1, FAIL_DAY_2,
                                            FAIL_DAY_3, FAIL_DAY_4, FAIL_DAY_5,
                                            FAIL_DAY_6, FAIL_DAY_7,
                                            GIFT_NOBILITY, GIFT_NOT_NOBILITY,
                                            NO_GIFT_NOT_NOBILITY, WIN_DAY_1,
                                            WIN_DAY_2, WIN_DAY_3, WIN_DAY_4,
                                            WIN_DAY_5, WIN_DAY_6, WIN_DAY_7)
from game.texts.tsar_tournament_message import (BEGIN_TOURNAMENT, FAIL_TOURN,
                                                FAIL_TOURN_2, FIN_TOURN,
                                                FINAL_TOURNAMENT)
from game.weapons.close_combat.swords import SimpleSword

from ..enemies.tournament_enemies import (preparation_enemy_1,
                                          preparation_enemy_2)
from .course_of_tournament import battle, break_battle
from .tsar_gift import tournament_tsar_gift


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
    random_enemy = randint(1, 10)
    if random_enemy <= 7:
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


def tsar_tournament_day_3(hero, hero_weapon):
    """Царский турнир, день 3"""
    random_enemy = randint(1, 10)
    if random_enemy <= 6:
        enemy, enemy_weapon = preparation_enemy_1()
    else:
        enemy, enemy_weapon = preparation_enemy_2()
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


def tsar_tournament_day_4(hero, hero_weapon):
    """Царский турнир, день 4"""
    random_enemy = randint(1, 10)
    if random_enemy <= 5:
        enemy, enemy_weapon = preparation_enemy_1()
    else:
        enemy, enemy_weapon = preparation_enemy_2()
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


def tsar_tournament_day_5(hero, hero_weapon):
    """Царский турнир, день 5"""
    random_enemy = randint(1, 10)
    if random_enemy <= 4:
        enemy, enemy_weapon = preparation_enemy_1()
    else:
        enemy, enemy_weapon = preparation_enemy_2()
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


def tsar_tournament_day_6(hero, hero_weapon):
    """Царский турнир, день 6"""
    random_enemy = randint(1, 10)
    if random_enemy <= 3:
        enemy, enemy_weapon = preparation_enemy_1()
    else:
        enemy, enemy_weapon = preparation_enemy_2()
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


def tsar_tournament_day_7(hero, hero_weapon):
    """Царский турнир, день 7"""
    random_enemy = randint(1, 10)
    if random_enemy <= 2:
        enemy, enemy_weapon = preparation_enemy_1()
    else:
        enemy, enemy_weapon = preparation_enemy_2()
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


def tsar_tournament_final(hero, hero_weapon, max_health_hero):
    """Финал царского турнира."""
    hero.health = max_health_hero
    print(FINAL_TOURNAMENT)
    if hero.nobility == 1:
        print(GIFT_NOBILITY)
        tournament_tsar_gift(hero, hero_weapon)
    else:
        random_phrase = randint(1, 10)
        if random_phrase <= 5:
            print(GIFT_NOT_NOBILITY)
            tournament_tsar_gift(hero, hero_weapon)
        else:
            print(NO_GIFT_NOT_NOBILITY)
            command = input(COMMAND)
            if command == '1':
                print(FAIL_TOURN)
            elif command == '2':
                enemy = BaseEnemy('Воевода', 300, 15, 15, 10, 5, 0, 1, 150, 5)
                enemy_weapon = SimpleSword('Ясный Сокол',
                                           'воронёная сталь', 15, 15)
                max_health_enemy = enemy.max_health()
                print(
                    f'''
Ваш противник - {enemy}
Его оружие - {enemy_weapon.get_weapon_enemy()}
Расстояние до противнике - {enemy.lenght}
''')
                fin = battle(
                    hero, hero_weapon, enemy, enemy_weapon,
                    max_health_enemy
                    )
                if fin == FINISH:
                    print(FIN_TOURN)
                    tournament_tsar_gift(hero, hero_weapon)
                    return
                else:
                    print(FAIL_TOURN_2)
                    return


def tsar_tournament_begin(hero, hero_weapon):
    """Ход царского турнира."""
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

    day_3 = tsar_tournament_day_3(hero, hero_weapon)
    if day_3 == FINISH:
        print(WIN_DAY_3)
    else:
        print(FAIL_DAY_3)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)

    day_4 = tsar_tournament_day_4(hero, hero_weapon)
    if day_4 == FINISH:
        print(WIN_DAY_4)
    else:
        print(FAIL_DAY_4)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)

    day_5 = tsar_tournament_day_5(hero, hero_weapon)
    if day_5 == FINISH:
        print(WIN_DAY_5)
    else:
        print(FAIL_DAY_5)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)

    day_6 = tsar_tournament_day_6(hero, hero_weapon)
    if day_6 == FINISH:
        print(WIN_DAY_6)
    else:
        print(FAIL_DAY_6)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)

    day_7 = tsar_tournament_day_7(hero, hero_weapon)
    if day_7 == FINISH:
        print(WIN_DAY_7)
    else:
        print(FAIL_DAY_7)
        return

    tsar_tournament_final(hero, hero_weapon, max_health_hero)

from random import randint

from game.enemies.base_enemy import BaseEnemy
from game.texts.actions import COMMAND, FINISH
from game.texts.rome_tournament_messages import (BEGIN_TOURNAMENT,
                                                 FAIL_TOURN, FAIL_TOURN_2,
                                                 FIN_TOURN,
                                                 FINAL_TOURNAMENT)
from game.texts.tournament_messages import (DAY_2, DAY_3, DAY_4, DAY_5, DAY_6,
                                            DAY_7, FAIL_DAY_1, FAIL_DAY_2,
                                            FAIL_DAY_3, FAIL_DAY_4, FAIL_DAY_5,
                                            FAIL_DAY_6, FAIL_DAY_7,
                                            GIFT_NOBILITY, GIFT_NOT_NOBILITY,
                                            NO_GIFT_NOT_NOBILITY, WIN_DAY_1,
                                            WIN_DAY_2, WIN_DAY_3, WIN_DAY_4,
                                            WIN_DAY_5, WIN_DAY_6, WIN_DAY_7)
from game.weapons.close_combat.swords import SimpleSword

from ..enemies.tournament_enemies import (preparation_enemy_3,
                                          preparation_enemy_4,
                                          preparation_enemy_5)
from .course_of_tournament import (battle, break_battle,
                                   new_tournament_break_battle)
from .gifts.rome_gift import rome_tournament_gift


def rome_tournament_day_1(hero, hero_weapon):
    """Римский турнир, день 1"""
    random_enemy = randint(1, 10)
    if random_enemy <= 3:
        enemy, enemy_weapon = preparation_enemy_3()
    else:
        enemy, enemy_weapon = preparation_enemy_4()
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


def rome_tournament_day_2(hero, hero_weapon):
    """Римский турнир, день 2"""
    random_enemy = randint(1, 10)
    if random_enemy == 1:
        enemy, enemy_weapon = preparation_enemy_3()
    elif 2 <= random_enemy <= 7:
        enemy, enemy_weapon = preparation_enemy_4()
    else:
        enemy, enemy_weapon = preparation_enemy_5()
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


def rome_tournament_day_3(hero, hero_weapon):
    """Римский турнир, день 3"""
    random_enemy = randint(1, 10)
    if random_enemy == 1:
        enemy, enemy_weapon = preparation_enemy_3()
    elif 2 <= random_enemy <= 6:
        enemy, enemy_weapon = preparation_enemy_4()
    else:
        enemy, enemy_weapon = preparation_enemy_5()
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


def rome_tournament_day_4(hero, hero_weapon):
    """Римский турнир, день 4"""
    random_enemy = randint(1, 10)
    if random_enemy == 1:
        enemy, enemy_weapon = preparation_enemy_3()
    elif 2 <= random_enemy <= 5:
        enemy, enemy_weapon = preparation_enemy_4()
    else:
        enemy, enemy_weapon = preparation_enemy_5()
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


def rome_tournament_day_5(hero, hero_weapon):
    """Римский турнир, день 5"""
    random_enemy = randint(1, 10)
    if random_enemy == 1:
        enemy, enemy_weapon = preparation_enemy_3()
    elif 2 <= random_enemy <= 4:
        enemy, enemy_weapon = preparation_enemy_4()
    else:
        enemy, enemy_weapon = preparation_enemy_5()
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


def rome_tournament_day_6(hero, hero_weapon):
    """Римский турнир, день 6"""
    random_enemy = randint(1, 10)
    if random_enemy == 1:
        enemy, enemy_weapon = preparation_enemy_3()
    elif 2 <= random_enemy <= 3:
        enemy, enemy_weapon = preparation_enemy_4()
    else:
        enemy, enemy_weapon = preparation_enemy_5()
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


def rome_tournament_day_7(hero, hero_weapon):
    """Римский турнир, день 7"""
    random_enemy = randint(1, 10)
    if random_enemy == 1:
        enemy, enemy_weapon = preparation_enemy_3()
    elif random_enemy == 2:
        enemy, enemy_weapon = preparation_enemy_4()
    else:
        enemy, enemy_weapon = preparation_enemy_5()
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


def rome_tournament_final(hero, hero_weapon, max_health_hero):
    """Финал Римского турнира."""
    hero.health = max_health_hero
    print(FINAL_TOURNAMENT)
    if hero.nobility == 1:
        print(GIFT_NOBILITY)
        rome_tournament_gift(hero, hero_weapon, max_health_hero)
    else:
        random_phrase = randint(1, 10)
        if random_phrase <= 5:
            print(GIFT_NOT_NOBILITY)
            rome_tournament_gift(hero, hero_weapon, max_health_hero)
        else:
            print(NO_GIFT_NOT_NOBILITY)
            command = input(COMMAND)
            if command == '1':
                print(FAIL_TOURN)
            elif command == '2':
                enemy = BaseEnemy('Легионер ветеран', 1000, 60, 60,
                                  60, 20, 0, 1, 150, 5)
                enemy_weapon = SimpleSword('Гроза варваров',
                                           'чёрная сталь', 35, 15)
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
                    rome_tournament_gift(hero, hero_weapon,
                                         max_health_hero)
                    return
                else:
                    print(FAIL_TOURN_2)
                    return


def rome_tournament_begin(hero, hero_weapon):
    """Ход Римского турнира."""
    hero, hero_weapon = new_tournament_break_battle(hero,
                                                    hero_weapon)
    max_health_hero = hero.max_health()
    day_1 = rome_tournament_day_1(hero, hero_weapon)
    if day_1 == FINISH:
        print(WIN_DAY_1)
    else:
        print(FAIL_DAY_1)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)

    day_2 = rome_tournament_day_2(hero, hero_weapon)
    if day_2 == FINISH:
        print(WIN_DAY_2)
    else:
        print(FAIL_DAY_2)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)

    day_3 = rome_tournament_day_3(hero, hero_weapon)
    if day_3 == FINISH:
        print(WIN_DAY_3)
    else:
        print(FAIL_DAY_3)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)

    day_4 = rome_tournament_day_4(hero, hero_weapon)
    if day_4 == FINISH:
        print(WIN_DAY_4)
    else:
        print(FAIL_DAY_4)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)

    day_5 = rome_tournament_day_5(hero, hero_weapon)
    if day_5 == FINISH:
        print(WIN_DAY_5)
    else:
        print(FAIL_DAY_5)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)

    day_6 = rome_tournament_day_6(hero, hero_weapon)
    if day_6 == FINISH:
        print(WIN_DAY_6)
    else:
        print(FAIL_DAY_6)
        return
    hero, hero_weapon = break_battle(hero, hero_weapon, max_health_hero)

    day_7 = rome_tournament_day_7(hero, hero_weapon)
    if day_7 == FINISH:
        print(WIN_DAY_7)
    else:
        print(FAIL_DAY_7)
        return

    rome_tournament_final(hero, hero_weapon, max_health_hero)

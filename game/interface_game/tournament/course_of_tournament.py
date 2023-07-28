from game.battles.close_combat.preparing_for_battle import get_close_weapon
from game.battles.magic_combat.preparing_for_battle import get_magic_weapon
from game.battles.ranged_combat.preparing_for_battle import get_ranged_weapon
from game.heroes.create_heroes.finish_create import changing_number
from game.random_number_func import random_phrase
from game.texts.actions import COMMAND, ERROR_LIST, FAIL, FINISH
from game.texts.attack_messages import WEAPON_FAIL
from game.texts.tournament_messages import (BREAK_BATTLE, FINICH_PROPERTY,
                                            GOOD_REST, NEW_TOURNAMENT,
                                            NOT_CLOSE_COMBAT,
                                            NOT_RANGED_COMBAT, SHORT_REST,
                                            SLEEP, TOURNAMENT_WEAPON)


def battle(hero, hero_weapon, enemy, enemy_weapon,
           max_health_enemy):
    """Битва."""
    new_battle = ''
    while new_battle != '0':
        if enemy_weapon.durability <= 0:
            print(WEAPON_FAIL)
            return FAIL
        if enemy_weapon.ammunition <= 0:
            print(enemy_weapon.not_ammunition())
            return FAIL
        print(f"""{TOURNAMENT_WEAPON}
        1 - {hero_weapon[0]}
        2 - {hero_weapon[1]}
        3 - {hero_weapon[2]}

        0 - Выход""")
        new_battle = input(COMMAND)
        fin = ''
        if new_battle == '1':
            fin = get_close_weapon(
                new_battle, hero,
                enemy, enemy_weapon, max_health_enemy, hero_weapon)
            if fin == FINISH:
                return fin
            if fin == FAIL:
                return fin
        if new_battle == '2':
            fin = get_ranged_weapon(
                new_battle, hero,
                enemy, enemy_weapon, max_health_enemy, hero_weapon)
            if fin == FINISH:
                return fin
            if fin == FAIL:
                return fin
        if new_battle == '3':
            fin = get_magic_weapon(
                new_battle, hero,
                enemy, enemy_weapon, max_health_enemy, hero_weapon
            )
            if fin == FINISH:
                return fin
            if fin == FAIL:
                return fin
        if new_battle == '0':
            print('BYE!!!')
        else:
            if fin is not None:
                print(random_phrase(ERROR_LIST))


def sharpen_weapon(hero, hero_weapon, max_health_hero):
    """Заточка меча."""
    if hero_weapon[0] is not None:
        hero_weapon[0].sharpen()
        print(SHORT_REST)
        hero.health += 50
        if hero.health > max_health_hero:
            hero.health = max_health_hero
    else:
        print(NOT_CLOSE_COMBAT)
        hero.health = max_health_hero


def make_arrows(hero, hero_weapon, max_health_hero):
    """Изготовление стрел."""
    if hero_weapon[1] is not None:
        hero_weapon[1].ammunition += 5
        print(SHORT_REST)
        hero.health += 50
        if hero.health > max_health_hero:
            hero.health = max_health_hero
    else:
        print(NOT_RANGED_COMBAT)
        hero.health = max_health_hero


def sleep(hero, hero_weapon, max_health_hero):
    """Меню отдыха"""
    print(SLEEP)
    command = ''
    while command not in ['1', '2', '3']:
        command = input(COMMAND)
        if command == '1':
            hero.health = max_health_hero
            print(GOOD_REST)
        elif command == '2':
            sharpen_weapon(hero, hero_weapon, max_health_hero)
        elif command == '3':
            make_arrows(hero, hero_weapon, max_health_hero)
        else:
            print(random_phrase(ERROR_LIST))


def break_battle(hero, hero_weapon, max_health_hero):
    """Перерыв между боями.
    Выбор параметров для изменения."""
    command = ''
    while command != '7':
        print(f'{hero}')
        print(f'Опыта осталось - {hero.experience}')
        print(BREAK_BATTLE)
        command = input(COMMAND)
        if command in ['2', '3', '4', '5', '6']:
            changing_number(command, hero)
        elif command == '7':
            print(FINICH_PROPERTY)
            sleep(hero, hero_weapon, max_health_hero)
        else:
            print(random_phrase(ERROR_LIST))
    return hero, hero_weapon


def new_tournament_break_battle(hero, hero_weapon):
    """Начало турнира.
    Выбор параметров для изменения."""
    command = ''
    while command != '7':
        print(f'{hero}')
        print(f'Опыта осталось - {hero.experience}')
        print(NEW_TOURNAMENT)
        command = input(COMMAND)
        if command in ['1', '2', '3', '4', '5', '6']:
            changing_number(command, hero)
        elif command == '7':
            print(FINICH_PROPERTY)
        else:
            print(random_phrase(ERROR_LIST))
    return hero, hero_weapon

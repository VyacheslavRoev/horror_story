from database.db import return_hero_for_name, return_weapons_hero

from game.heroes.base_hero import BaseHero
from game.random_number_func import random_phrase
from game.texts.actions import COMMAND, ERROR_LIST
from game.texts.menu_messages import END
from game.texts.tournament_messages import (COMPLETED, NOT_AVAILABLE,
                                            TOURNAMENT_MENU)
from game.weapons.close_combat.swords import SimpleSword
from game.weapons.magic_combat.staves import SimpleStave
from game.weapons.ranged_combat.bows import SimpleBow

from .teutonic_tournament import teutonic_tournament_begin
from .tsar_tournament import tsar_tournament_begin
from .polovtsian_tournament import polovistan_tournament_begin
from .rome_tournament import rome_tournament_begin

inventary_hero = [None, None, None]


def preparation_hero(hero):
    """Подготовка героя."""
    you_hero = BaseHero(hero[1], hero[2], hero[3], hero[4],
                        hero[5], hero[6])
    you_hero.protection = hero[7]
    you_hero.experience = hero[8]
    you_hero.nobility = hero[9]
    you_hero.tsar = hero[10]
    you_hero.teutonic = hero[11]
    you_hero.polovistan = hero[12]
    you_hero.rome = hero[13]
    you_hero.persia = hero[14]
    you_hero.barbarians = hero[15]
    you_hero.koschei = hero[16]
    weapons_list = return_weapons_hero(hero[0])
    for weapon in weapons_list:
        if weapon[7] == 'Ближний бой':
            sword_hero = SimpleSword(weapon[1], weapon[2],
                                     weapon[3], weapon[4])
            del inventary_hero[0]
            inventary_hero.insert(0, sword_hero)
        if weapon[7] == 'Магическое оружие':
            stave_hero = SimpleStave(weapon[1], weapon[2],
                                     weapon[6], weapon[9])
            del inventary_hero[2]
            inventary_hero.insert(2, stave_hero)
        if weapon[7] == 'Дальний бой':
            bow_hero = SimpleBow(weapon[1], weapon[2],
                                 weapon[5], weapon[8], weapon[9])
            del inventary_hero[1]
            inventary_hero.insert(1, bow_hero)
    return you_hero, inventary_hero


def tournament_menu(hero_name):
    """Меню турниров."""
    command = ''
    while command != 0:
        base_hero = return_hero_for_name(hero_name)
        hero, hero_weapons = preparation_hero(
                base_hero
                )
        print(TOURNAMENT_MENU)
        command = input(COMMAND)
        if command == '1':
            if hero.tsar == 0:
                tsar_tournament_begin(
                    hero, hero_weapons
                )
            else:
                print(COMPLETED)
        elif command == '2':
            if hero.teutonic == 0:
                if hero.tsar == 1:
                    teutonic_tournament_begin(
                        hero, hero_weapons
                    )
                else:
                    print(NOT_AVAILABLE)
            else:
                print(COMPLETED)
        elif command == '3':
            if hero.polovistan == 0:
                if hero.tsar == 1 and hero.teutonic == 1:
                    polovistan_tournament_begin(
                        hero, hero_weapons
                    )
                else:
                    print(NOT_AVAILABLE)
            else:
                print(COMPLETED)
        elif command == '4':
            if hero.rome == 0:
                if (hero.tsar == 1 and hero.teutonic == 1
                   and hero.polovistan == 1):
                    rome_tournament_begin(
                        hero, hero_weapons
                    )
                else:
                    print(NOT_AVAILABLE)
            else:
                print(COMPLETED)
        elif command in ['5', '6', '7']:
            print('В разработке!')
        elif command == '0':
            print(END)
            return
        else:
            print(random_phrase(ERROR_LIST))

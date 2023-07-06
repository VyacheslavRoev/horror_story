from database.db import return_weapons_hero

from game.heroes.base_hero import BaseHero
from game.random_number_func import random_phrase
from game.texts.actions import COMMAND, ERROR_LIST
from game.texts.menu_messages import END
from game.texts.tournament_messages import TOURNAMENT_MENU
from game.weapons.close_combat.swords import SimpleSword
from game.weapons.magic_combat.staves import SimpleStave
from game.weapons.ranged_combat.bows import SimpleBow

from .tsar_tournament import tsar_tournament_begin

inventary_hero = [None, None, None]


def preparation_hero(hero):
    """Подготовка героя."""
    you_hero = BaseHero(hero[1], hero[2], hero[3], hero[4],
                        hero[5], hero[6])
    you_hero.protection = hero[7]
    you_hero.experience = hero[8]
    you_hero.nobility = hero[9]
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


def tournament_menu(base_hero):
    """Меню турниров."""
    command = ''
    while command != 0:
        print(TOURNAMENT_MENU)
        command = input(COMMAND)
        if command == '1':
            hero, hero_weapons = preparation_hero(
                base_hero
                )
            tsar_tournament_begin(
                hero, hero_weapons
            )
        elif command in ['2', '3', '4', '5', '6', '7']:
            print('В разработке!')
        elif command == '0':
            print(END)
            return
        else:
            print(random_phrase(ERROR_LIST))


from texts.create_heroes.base import EXPERIENCE, CHANGE, FINISH_HERO
from texts.actions import COMMAND, ERROR_LIST, FINISH
from random_number_func import random_phrase


def changing_number(command):
    """Изменение параметров."""
    pass


def changing_properties(hero):
    """Выбор параметров для изменения."""
    command = ''
    while command != '7':
        print(CHANGE)
        command = input(COMMAND)
        if command in ['1', '2', '3', '4', '5', '6']:
            changing_number(command)
        else:
            print(random_phrase(ERROR_LIST))


def changing_properties_menu(hero):
    """Первое подведение итогов создания героя.
    Возможность завершить процесс."""
    if hero.health < 0:
        hero.health = 0
    if hero.force < 0:
        hero.force = 0
    if hero.dexterity < 0:
        hero.dexterity = 0
    if hero.magic < 0:
        hero.magic = 0
    if hero.speed < 0:
        hero.speed = 0
    if hero.protection < 0:
        hero.protection = 0
    print(hero)
    command = ''
    while command != '2':
        print(EXPERIENCE)
        command = input(COMMAND)
        if command == '1':
            changing_properties(hero)
        if command == '2':
            print(FINISH_HERO)
            fin = FINISH
        else:
            print(random_phrase(ERROR_LIST))
    return fin

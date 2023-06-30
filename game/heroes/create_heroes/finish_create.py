from heroes.create_heroes.changing_hero_properties import (change_health,
                                                           change_parametr)
from random_number_func import random_phrase
from texts.actions import COMMAND, ERROR_LIST, FINISH, FAIL, ONE
from texts.create_heroes.base import (CHANGE, EXPERIENCE, EXPERIENCE_MENU,
                                      FINISH_HERO, YOU_WEAPONS)
import re


pattern = r'^[0-9]+$'


def check_value(hero, value):
    """Проверка значения для изменения параметров."""
    check = re.fullmatch(pattern, value)
    if not check:
        print(random_phrase(ERROR_LIST))
        return FAIL
    if int(value) > hero.experience:
        print('Слишком большое значение!')
        return FAIL
    if int(value) % 10 != 0:
        print('Значение должно быть кратным 10!')
        return FAIL
    return value


def changing_number(command, hero):
    """Изменение параметров."""
    if command == '1':
        print(EXPERIENCE)
        value = input(COMMAND)
        check = check_value(hero, value)
        if check == FAIL:
            return
        hero.experience, hero.health = change_health(
            value, hero.experience, hero.health
            )
        print(hero)
    elif command == '2':
        print(EXPERIENCE)
        value = input(COMMAND)
        check = check_value(hero, value)
        if check == FAIL:
            return
        hero.experience, hero.force = change_parametr(
            value, hero.experience, hero.force
            )
        print(hero)
    elif command == '3':
        print(EXPERIENCE)
        value = input(COMMAND)
        check = check_value(hero, value)
        if check == FAIL:
            return
        hero.experience, hero.dexterity = change_parametr(
            value, hero.experience, hero.dexterity
            )
        print(hero)
    elif command == '4':
        print(EXPERIENCE)
        value = input(COMMAND)
        check = check_value(hero, value)
        if check == FAIL:
            return
        hero.experience, hero.magic = change_parametr(
            value, hero.experience, hero.magic
            )
        print(hero)
    elif command == '5':
        print(EXPERIENCE)
        value = input(COMMAND)
        check = check_value(hero, value)
        if check == FAIL:
            return
        hero.experience, hero.speed = change_parametr(
            value, hero.experience, hero.speed
            )
        print(hero)
    elif command == '6':
        print(EXPERIENCE)
        value = input(COMMAND)
        check = check_value(hero, value)
        if check == FAIL:
            return
        hero.experience, hero.protection = change_parametr(
            value, hero.experience, hero.protection
            )
        print(hero)


def changing_properties(hero):
    """Выбор параметров для изменения."""
    command = ''
    while command != '7':
        print(f'Опыта осталось - {hero.experience}')
        print(CHANGE)
        command = input(COMMAND)
        if command in ['1', '2', '3', '4', '5', '6']:
            changing_number(command, hero)
        elif command == '7':
            print(FINISH_HERO)
            fin = FINISH
        else:
            print(random_phrase(ERROR_LIST))
    return fin


def changing_properties_menu(hero):
    """Первое подведение итогов создания героя.
    Возможность завершить процесс."""
    if hero.health < 100:
        hero.health = 100
    if hero.force < 0:
        hero.force = 0
    if hero.dexterity < 0:
        hero.dexterity = 0
    if hero.magic < 0:
        hero.magic = 0
    if hero.speed < 1:
        hero.speed = 1
    if hero.protection < 0:
        hero.protection = 0
    print(hero)
    command = ''
    while command != '2':
        print(EXPERIENCE_MENU)
        command = input(COMMAND)
        if command == '1':
            fin = changing_properties(hero)
            return fin
        if command == '2':
            print(FINISH_HERO)
            fin = FINISH
        else:
            print(random_phrase(ERROR_LIST))
    return fin


def you_weapons(weapons, hero):
    print(YOU_WEAPONS)
    for i in weapons:
        print(i)
    print(ONE)
    command = input(COMMAND)
    while command != '1':
        print(random_phrase(ERROR_LIST))
        print(ONE)
        command = input(COMMAND)
    fin = changing_properties_menu(hero)
    return fin

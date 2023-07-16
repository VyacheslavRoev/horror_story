import re

from game.heroes.create_heroes.changing_hero_properties import (
    change_health, change_parametr)
from database.db import insert_hero, insert_weapon, return_hero_id
from game.random_number_func import random_phrase
from game.texts.actions import COMMAND, ERROR_LIST, FAIL, FINISH, ONE
from game.texts.create_heroes.base import (CHANGE, EXPERIENCE, EXPERIENCE_MENU,
                                           FINISH_HERO, YOU_WEAPONS)

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


def changing_properties(hero, weapons, history):
    """Выбор параметров для изменения."""
    command = ''
    while command != '7':
        print(f'Опыта осталось - {hero.experience}')
        print(CHANGE)
        command = input(COMMAND)
        if command in ['1', '2', '3', '4', '5', '6']:
            changing_number(command, hero)
        elif command == '7':
            values_hero = (hero.name, hero.health, hero.force, hero.dexterity,
                           hero.magic, hero.speed, hero.protection,
                           hero.experience, hero.nobility, hero.tsar,
                           hero.teutonic, hero.polovistan, hero.rome,
                           hero.persia, hero.barbarians, hero.koschei, history)
            insert_hero(values_hero)
            hero_id = return_hero_id(hero.name)
            for weapon in weapons:
                values_weapon = (
                    weapon.name, weapon.material, weapon.impact_force,
                    weapon.injection, weapon.shot_power,
                    weapon.magic_power, weapon.class_weapon,
                    weapon.ammunition, weapon.long_shot, weapon.durability,
                    hero_id
                )
                insert_weapon(values_weapon)
            print(FINISH_HERO)
            fin = FINISH
        else:
            print(random_phrase(ERROR_LIST))
    return fin


def changing_properties_menu(weapons, hero, history):
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
            fin = changing_properties(hero, weapons, history)
            return fin
        if command == '2':
            values_hero = (hero.name, hero.health, hero.force, hero.dexterity,
                           hero.magic, hero.speed, hero.protection,
                           hero.experience, hero.nobility, hero.tsar,
                           hero.teutonic, hero.polovistan, hero.rome,
                           hero.persia, hero.barbarians, hero.koschei, history)
            insert_hero(values_hero)
            hero_id = return_hero_id(hero.name)
            for weapon in weapons:
                values_weapon = (
                    weapon.name, weapon.material, weapon.impact_force,
                    weapon.injection, weapon.shot_power,
                    weapon.magic_power, weapon.class_weapon,
                    weapon.ammunition, weapon.long_shot, weapon.durability,
                    hero_id
                )
                insert_weapon(values_weapon)
            print(FINISH_HERO)
            fin = FINISH
        else:
            print(random_phrase(ERROR_LIST))
    return fin


def you_weapons(weapons, hero, history):
    print(YOU_WEAPONS)
    for i in weapons:
        print(i)
    print(ONE)
    command = input(COMMAND)
    while command != '1':
        print(random_phrase(ERROR_LIST))
        print(ONE)
        command = input(COMMAND)
    fin = changing_properties_menu(weapons, hero, history)
    return fin

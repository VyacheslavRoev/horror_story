from random import randint

from game.heroes.create_heroes.changing_hero_properties import (
    army_hero, bad_character_hero, bad_habits_hero, disease_hero,
    education_hero, good_character_hero, no_bad_habits_hero, no_disease_hero,
    no_education_hero, no_scool_hero, no_university_hero, scool_hero,
    sport_hero, university_hero)
from game.heroes.create_heroes.finish_create import you_weapons
from game.random_number_func import random_phrase
from game.texts.actions import COMMAND, ERROR_LIST, ONE
from game.texts.create_heroes.city_resident import (
    ARMY_CITY_RESIDENT_FAMILY, ARMY_CITY_RESIDENT_NO_FAMILY,
    BAD_CHARACTER_CITY_RESIDENT_FAMILY, BAD_CHARACTER_CITY_RESIDENT_NO_FAMILY,
    BAD_HABITS_CITY_RESIDENT_FAMILY, BAD_HABITS_CITY_RESIDENT_NO_FAMILY,
    BIRTHDAY_CITY_RESIDENT_FAMILY, BIRTHDAY_CITY_RESIDENT_NO_FAMILY,
    DISEASE_CITY_RESIDENT_FAMILY, DISEASE_CITY_RESIDENT_NO_FAMILY,
    EDUCATION_CITY_RESIDENT_FAMILY, EDUCATION_CITY_RESIDENT_NO_FAMILY,
    GOOD_CHARACTER_CITY_RESIDENT_FAMILY,
    GOOD_CHARACTER_CITY_RESIDENT_NO_FAMILY, NO_ARMY_CITY_RESIDENT_FAMILY,
    NO_ARMY_CITY_RESIDENT_NO_FAMILY, NO_BAD_HABITS_CITY_RESIDENT_FAMILY,
    NO_BAD_HABITS_CITY_RESIDENT_NO_FAMILY, NO_DISEASE_CITY_RESIDENT_FAMILY,
    NO_DISEASE_CITY_RESIDENT_NO_FAMILY, NO_EDUCATION_CITY_RESIDENT_FAMILY,
    NO_EDUCATION_CITY_RESIDENT_NO_FAMILY, NO_SCOOL_CITY_RESIDENT_FAMILY,
    NO_SCOOL_CITY_RESIDENT_NO_FAMILY, NO_SPORT_CITY_RESIDENT_FAMILY,
    NO_SPORT_CITY_RESIDENT_NO_FAMILY, NO_UNIVERSITY_CITY_RESIDENT_FAMILY,
    NO_UNIVERSITY_CITY_RESIDENT_NO_FAMILY, SCOOL_CITY_RESIDENT_FAMILY,
    SCOOL_CITY_RESIDENT_NO_FAMILY, SPORT_CITY_RESIDENT_FAMILY,
    SPORT_CITY_RESIDENT_NO_FAMILY, UNIVERSITY_CITY_RESIDENT_FAMILY,
    UNIVERSITY_CITY_RESIDENT_NO_FAMILY)
from game.weapons.create_weapon import create_name_weapon
from game.weapons.close_combat.swords import create_sword_1
from game.weapons.ranged_combat.bows import create_bow_1


def early_years_family(hero):
    """Молодость в семье"""
    history_early_years = ''
    bad_habits = randint(1, 10)
    if bad_habits <= 4:
        bad_habits_hero(hero)
        history_early_years += BAD_HABITS_CITY_RESIDENT_FAMILY
    else:
        no_bad_habits_hero(hero)
        history_early_years += NO_BAD_HABITS_CITY_RESIDENT_FAMILY
    university = randint(1, 10)
    if university <= 6:
        university_hero(hero)
        history_early_years += UNIVERSITY_CITY_RESIDENT_FAMILY
    else:
        no_university_hero(hero)
        history_early_years += NO_UNIVERSITY_CITY_RESIDENT_FAMILY
    sport = randint(1, 10)
    if sport <= 5:
        sport_hero(hero)
        history_early_years += SPORT_CITY_RESIDENT_FAMILY
    else:
        history_early_years += NO_SPORT_CITY_RESIDENT_FAMILY
    army = randint(1, 10)
    if army <= 5:
        army_hero(hero)
        history_early_years += ARMY_CITY_RESIDENT_FAMILY
    else:
        history_early_years += NO_ARMY_CITY_RESIDENT_FAMILY
    return history_early_years


def early_years_no_family(hero):
    """Молодость без семьи."""
    history_early_years = ''
    bad_habits = randint(1, 10)
    if bad_habits <= 6:
        bad_habits_hero(hero)
        history_early_years += BAD_HABITS_CITY_RESIDENT_NO_FAMILY
    else:
        no_bad_habits_hero(hero)
        history_early_years += NO_BAD_HABITS_CITY_RESIDENT_NO_FAMILY
    university = randint(1, 10)
    if university <= 3:
        university_hero(hero)
        history_early_years += UNIVERSITY_CITY_RESIDENT_NO_FAMILY
    else:
        no_university_hero(hero)
        history_early_years += NO_UNIVERSITY_CITY_RESIDENT_NO_FAMILY
    sport = randint(1, 10)
    if sport <= 5:
        sport_hero(hero)
        history_early_years += SPORT_CITY_RESIDENT_NO_FAMILY
    else:
        history_early_years += NO_SPORT_CITY_RESIDENT_NO_FAMILY
    army = randint(1, 10)
    if army <= 5:
        army_hero(hero)
        history_early_years += ARMY_CITY_RESIDENT_NO_FAMILY
    else:
        history_early_years += NO_ARMY_CITY_RESIDENT_NO_FAMILY
    return history_early_years


def teen_years_family(hero):
    """Подростковый возраст в семье."""
    history_teen_years = ''
    scool = randint(1, 10)
    if scool <= 7:
        scool_hero(hero)
        history_teen_years += SCOOL_CITY_RESIDENT_FAMILY
    else:
        no_scool_hero(hero)
        history_teen_years += NO_SCOOL_CITY_RESIDENT_FAMILY
    education = randint(1, 10)
    if education <= 7:
        education_hero(hero)
        history_teen_years += EDUCATION_CITY_RESIDENT_FAMILY
    else:
        no_education_hero(hero)
        history_teen_years += NO_EDUCATION_CITY_RESIDENT_FAMILY
    return history_teen_years


def teen_years_no_family(hero):
    """Подростковый возраст без семьи."""
    history_teen_years = ''
    scool = randint(1, 10)
    if scool <= 3:
        scool_hero(hero)
        history_teen_years += SCOOL_CITY_RESIDENT_NO_FAMILY
    else:
        no_scool_hero(hero)
        history_teen_years += NO_SCOOL_CITY_RESIDENT_NO_FAMILY
    education = randint(1, 10)
    if education <= 3:
        education_hero(hero)
        history_teen_years += EDUCATION_CITY_RESIDENT_NO_FAMILY
    else:
        no_education_hero(hero)
        history_teen_years += NO_EDUCATION_CITY_RESIDENT_NO_FAMILY
    return history_teen_years


def childhood_family(hero):
    """Детство в семье."""
    history_childhood = ''
    disease = randint(1, 10)
    if disease <= 5:
        disease_hero(hero)
        history_childhood += DISEASE_CITY_RESIDENT_FAMILY
    else:
        no_disease_hero(hero)
        history_childhood += NO_DISEASE_CITY_RESIDENT_FAMILY
    character = randint(1, 10)
    if character <= 6:
        good_character_hero(hero)
        history_childhood += GOOD_CHARACTER_CITY_RESIDENT_FAMILY
    else:
        bad_character_hero(hero)
        history_childhood += BAD_CHARACTER_CITY_RESIDENT_FAMILY
    return history_childhood


def childhood_no_family(hero):
    """Детство без семьи."""
    history_childhood = ''
    disease = randint(1, 10)
    if disease <= 7:
        disease_hero(hero)
        history_childhood += DISEASE_CITY_RESIDENT_NO_FAMILY
    else:
        no_disease_hero(hero)
        history_childhood += NO_DISEASE_CITY_RESIDENT_NO_FAMILY
    character = randint(1, 10)
    if character <= 4:
        good_character_hero(hero)
        history_childhood += GOOD_CHARACTER_CITY_RESIDENT_NO_FAMILY
    else:
        bad_character_hero(hero)
        history_childhood += BAD_CHARACTER_CITY_RESIDENT_NO_FAMILY
    return history_childhood


def create_weapons_city_resident():
    """Создание случайного оружия горожанина."""
    weapons = []
    sword_full_name = create_name_weapon()
    sword = create_sword_1(sword_full_name)
    weapons.append(sword)
    bow_full_name = create_name_weapon()
    bow = create_bow_1(bow_full_name)
    weapons.append(bow)
    return weapons


def history_city_resident(hero):
    """История горожанина."""
    history = ''
    family = randint(1, 10)
    if family <= 5:
        history += BIRTHDAY_CITY_RESIDENT_FAMILY
        childhood = childhood_family(hero)
        history += childhood
        teen_years = teen_years_family(hero)
        history += teen_years
        early_years = early_years_family(hero)
        history += early_years
    else:
        history += BIRTHDAY_CITY_RESIDENT_NO_FAMILY
        childhood = childhood_no_family(hero)
        history += childhood
        teen_years = teen_years_no_family(hero)
        history += teen_years
        early_years = early_years_no_family(hero)
        history += early_years
    weapons = create_weapons_city_resident()
    print(history)
    print(ONE)
    command = input(COMMAND)
    while command != '1':
        print(random_phrase(ERROR_LIST))
        print(ONE)
        command = input(COMMAND)
    fin = you_weapons(weapons, hero, history)
    return fin

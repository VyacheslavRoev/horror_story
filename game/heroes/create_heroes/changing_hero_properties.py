def disease_hero(hero):
    hero.health -= 10
    hero.force -= 1
    hero.dexterity -= 1
    hero.speed -= 1
    hero.protection -= 1
    hero.experience += 10


def no_disease_hero(hero):
    hero.health += 10
    hero.force += 1
    hero.dexterity += 1
    hero.speed += 1
    hero.protection += 1


def good_character_hero(hero):
    hero.magic += 2
    hero.experience += 10


def bad_character_hero(hero):
    hero.dexterity += 1
    hero.speed += 1
    hero.magic -= 1
    hero.experience += 20


def scool_hero(hero):
    hero.magic += 2
    hero.experience += 20


def no_scool_hero(hero):
    hero.health += 10
    hero.force += 1
    hero.dexterity += 1
    hero.speed += 1
    hero.protection += 1
    hero.magic -= 2
    hero.experience += 20


def education_hero(hero):
    hero.health += 10
    hero.force += 1
    hero.dexterity += 1
    hero.speed += 1
    hero.protection += 1
    hero.magic += 1


def no_education_hero(hero):
    hero.experience += 50


def bad_habits_hero(hero):
    hero.health -= 30
    hero.force -= 3
    hero.dexterity -= 3
    hero.magic -= 3
    hero.speed -= 3
    hero.protection -= 1


def no_bad_habits_hero(hero):
    hero.health += 30
    hero.force += 3
    hero.dexterity += 3
    hero.magic += 3
    hero.speed += 3
    hero.protection += 1


def university_hero(hero):
    hero.magic += 2
    hero.experience += 20


def no_university_hero(hero):
    hero.health += 10
    hero.force += 1
    hero.dexterity += 1
    hero.speed += 1
    hero.protection += 1
    hero.magic -= 2
    hero.experience += 20


def sport_hero(hero):
    hero.health += 20
    hero.force += 2
    hero.dexterity += 2
    hero.speed += 2
    hero.protection += 2
    hero.magic += 2
    hero.experience += 20


def army_hero(hero):
    hero.health -= 30
    hero.force += 2
    hero.dexterity += 2
    hero.speed += 2
    hero.protection += 2
    hero.magic += 2
    hero.experience += 30

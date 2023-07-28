def disease_hero(hero):
    """Болезни."""
    hero.health -= 20
    hero.force -= 2
    hero.dexterity -= 2
    hero.speed -= 2
    hero.protection -= 2
    hero.experience += 20


def no_disease_hero(hero):
    """Отсутствие болезней."""
    hero.health += 10
    hero.force += 1
    hero.dexterity += 1
    hero.speed += 1
    hero.protection += 1
    hero.experience += 10


def good_character_hero(hero):
    """Хороший характер."""
    hero.health += 20
    hero.magic += 2
    hero.experience += 20


def bad_character_hero(hero):
    """Плохой характер."""
    hero.dexterity += 1
    hero.speed += 1
    hero.magic -= 1
    hero.experience += 20


def scool_hero(hero):
    """Школа."""
    hero.health += 20
    hero.force += 1
    hero.dexterity += 1
    hero.speed += 1
    hero.protection += 1
    hero.magic += 2
    hero.experience += 10


def no_scool_hero(hero):
    """Отсутствие школы."""
    hero.health += 10
    hero.force += 1
    hero.dexterity += 1
    hero.speed += 1
    hero.protection += 1
    hero.magic -= 2
    hero.experience += 20


def education_hero(hero):
    """Воспитание."""
    hero.health += 10
    hero.force += 1
    hero.dexterity += 1
    hero.speed += 1
    hero.protection += 1
    hero.magic += 1
    hero.experience += 20


def no_education_hero(hero):
    """Отсутствие воспитания."""
    hero.experience += 50


def bad_habits_hero(hero):
    """Плохие привычки."""
    hero.health -= 30
    hero.force -= 3
    hero.dexterity -= 3
    hero.magic -= 3
    hero.speed -= 3
    hero.protection -= 1


def no_bad_habits_hero(hero):
    """Отсутствие плохих привычек."""
    hero.health += 30
    hero.force += 3
    hero.dexterity += 3
    hero.magic += 3
    hero.speed += 3
    hero.protection += 1


def university_hero(hero):
    """Университет."""
    hero.health += 20
    hero.force += 1
    hero.dexterity += 1
    hero.speed += 1
    hero.protection += 1
    hero.magic += 2
    hero.experience += 10


def no_university_hero(hero):
    """Отсутствие университета."""
    hero.health += 10
    hero.force += 1
    hero.dexterity += 1
    hero.speed += 1
    hero.protection += 1
    hero.magic -= 2
    hero.experience += 30


def sport_hero(hero):
    """Тренировки."""
    hero.health += 20
    hero.force += 3
    hero.dexterity += 3
    hero.speed += 3
    hero.protection += 3
    hero.magic += 3
    hero.experience += 20


def army_hero(hero):
    """Служба в армии."""
    hero.health -= 30
    hero.force += 2
    hero.dexterity += 2
    hero.speed += 2
    hero.protection += 2
    hero.magic += 2
    hero.experience += 30


def change_health(value, experience, health):
    """Изменение здоровья героя за счет опыта."""
    experience -= int(value)
    health += int(value)
    return experience, health


def change_parametr(value, experience, parametr):
    """Изменение параметра героя за счет опыта."""
    experience -= int(value)
    parametr += int((int(value) / 10))
    return experience, parametr

from random import randint

from database.validators import check_name_hero

from game.heroes.base_hero import BaseHero
from game.random_number_func import random_phrase
from game.texts.actions import COMMAND, ERROR_LIST, FAIL, FINISH
from game.texts.create_heroes.base import HELLO_CREATE, HISTORY, YOU_NAME

from .create_beggar import history_beggar
from .create_poor_peasant import history_poor_peasant
from .create_prosperous_peasant import history_prosperous_peasant
from .create_city_resident import history_city_resident
from .create_merchant import history_merchant
from .create_ruined_nobles import history_ruined_nobles
from .create_warrior import history_warrior
from .create_mayor import history_mayor
from .create_boyar import history_boyars
from .create_voevode import history_voevode
from .create_tsar import history_tsar


def random_birth(new_hero):
    """Случайный выбор развития истории героя."""
    random_birth_number = randint(98, 100)
    if random_birth_number <= 15:
        fin = history_beggar(new_hero)
    elif 15 < random_birth_number <= 30:
        fin = history_poor_peasant(new_hero)
    elif 30 < random_birth_number <= 40:
        fin = history_prosperous_peasant(new_hero)
    elif 40 < random_birth_number <= 55:
        fin = history_city_resident(new_hero)
    elif 55 < random_birth_number <= 65:
        fin = history_merchant(new_hero)
    elif 65 < random_birth_number <= 75:
        new_hero.nobility = 1
        fin = history_ruined_nobles(new_hero)
    elif 75 < random_birth_number <= 85:
        new_hero.nobility = 1
        fin = history_warrior(new_hero)
    elif 85 < random_birth_number <= 89:
        new_hero.nobility = 1
        fin = history_mayor(new_hero)
    elif 89 < random_birth_number <= 93:
        new_hero.nobility = 1
        fin = history_boyars(new_hero)
    elif 93 < random_birth_number <= 97:
        new_hero.nobility = 1
        fin = history_voevode(new_hero)
    elif 97 < random_birth_number:
        new_hero.nobility = 1
        fin = history_tsar(new_hero)
    return fin


def create_new_hero():
    """Создание экземпляра класса BaseHero со случайными параметрами."""
    new_hero = BaseHero('No name', 1, 2, 3, 4, 5)
    new_hero.health = randint(150, 250)
    new_hero.force = randint(0, 10)
    new_hero.force = randint(0, 10)
    new_hero.dexterity = randint(0, 10)
    new_hero.magic = randint(0, 10)
    new_hero.speed = randint(1, 10)
    return new_hero


def history_hero():
    """История героя."""
    new_hero = create_new_hero()
    print(YOU_NAME)
    you_name = input()
    name = check_name_hero(you_name)
    if name == FAIL:
        return
    new_hero.name = you_name
    print(f'А теперь, {you_name}, {HISTORY}')
    fin = random_birth(new_hero)
    return fin


def begin_create_hero():
    """Начало создания героя."""
    command = ''
    while command != '2':
        print(HELLO_CREATE)
        command = input(COMMAND)
        if command == '1':
            fin = history_hero()
            if fin == FINISH:
                return
        elif command == '2':
            print('Прощай!')
        else:
            print(random_phrase(ERROR_LIST))

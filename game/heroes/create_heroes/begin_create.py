from random import randint

from heroes.base_hero import BaseHero
from heroes.create_heroes.create_beggar import history_beggar
from random_number_func import random_phrase
from texts.actions import COMMAND, ERROR_LIST, FINISH
from texts.create_heroes.base import HELLO_CREATE, HISTORY, YOU_NAME


def random_birth(new_hero):
    """Случайный выбор развития истории героя."""
    random_birth_number = randint(1, 100)
    if random_birth_number <= 15:
        fin = history_beggar(new_hero)
    elif 15 < random_birth_number <= 30:
        fin = history_beggar(new_hero)
    elif 30 < random_birth_number <= 40:
        fin = history_beggar(new_hero)
    elif 40 < random_birth_number <= 55:
        fin = history_beggar(new_hero)
    elif 55 < random_birth_number <= 65:
        fin = history_beggar(new_hero)
    elif 65 < random_birth_number <= 75:
        fin = history_beggar(new_hero)
    elif 75 < random_birth_number <= 85:
        fin = history_beggar(new_hero)
    elif 85 < random_birth_number <= 89:
        fin = history_beggar(new_hero)
    elif 89 < random_birth_number <= 93:
        fin = history_beggar(new_hero)
    elif 93 < random_birth_number <= 97:
        fin = history_beggar(new_hero)
    elif 97 < random_birth_number:
        fin = history_beggar(new_hero)
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

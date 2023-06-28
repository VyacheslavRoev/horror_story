from texts.create_heroes.base import HELLO_CREATE
from texts.actions import COMMAND, ERROR_LIST
from random_number_func import random_phrase


def history_hero():
    pass


def begin_create_hero():
    print(HELLO_CREATE)
    command = ''
    while command != '2':
        command = input(COMMAND)
        if command == '1':
            history_hero()
        else:
            print(random_phrase(ERROR_LIST))

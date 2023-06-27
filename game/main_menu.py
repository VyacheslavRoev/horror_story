from trainings.training_hero import traning_menu
from texts.menu_messages import HELLO, END, MAIN_MENU
from texts.actions import COMMAND, ERROR_LIST
from random_number_func import random_phrase


def menu():
    print(HELLO)
    menu_command = ''
    while menu_command != '5':
        print(MAIN_MENU)
        menu_command = input(COMMAND)
        if menu_command == '1':
            traning_menu()
        elif menu_command in ['2', '3', '4']:
            print('В разработке!')
        elif menu_command == '5':
            print(END)
        else:
            print(random_phrase(ERROR_LIST))

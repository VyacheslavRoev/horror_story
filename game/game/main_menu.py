from game.heroes.create_heroes.begin_create import begin_create_hero
from game.random_number_func import random_phrase
from game.texts.actions import COMMAND, ERROR_LIST, FAIL
from game.texts.menu_messages import END, HELLO, MAIN_MENU
from game.trainings.training_hero import traning_menu
from database.validators import check_name_hero_tournament
from game.tournament.menu import tournament_menu


def menu():
    print(HELLO)
    menu_command = ''
    while menu_command != '5':
        print(MAIN_MENU)
        menu_command = input(COMMAND)
        if menu_command == '1':
            traning_menu()
        elif menu_command == '2':
            begin_create_hero()
        elif menu_command == '3':
            hero_name = input('Введите имя героя: ')
            hero = check_name_hero_tournament(hero_name)
            if hero == FAIL:
                print('Персонаж не найден!')
            else:
                tournament_menu(hero)
        elif menu_command == '4':
            print('В разработке!')
        elif menu_command == '5':
            print(END)
        else:
            print(random_phrase(ERROR_LIST))

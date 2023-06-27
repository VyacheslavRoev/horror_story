from trainings.training_hero import traning_menu
from texts.menu_messages import HELLO, END, MAIN_MENU
from texts.actions import COMMAND


def menu():
    print(HELLO)
    menu_command = ''
    while menu_command != 5:
        print(MAIN_MENU)
        menu_command = int(input(COMMAND))
        if menu_command == 1:
            traning_menu()
        elif menu_command == 2 or menu_command == 3 or menu_command == 4:
            print('В разработке!')
    return print(END)

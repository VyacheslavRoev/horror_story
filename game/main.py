from game.main_menu import menu
from database.db import create_tables


def main():
    create_tables()
    menu()


if __name__ == '__main__':
    main()

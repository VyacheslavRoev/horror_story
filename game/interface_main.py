from database.db import create_tables
from interface.interface_window import window_interface


def main():
    create_tables()
    window_interface()


if __name__ == '__main__':
    main()
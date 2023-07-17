import sqlite3 as sl
from game.texts.actions import FAIL, FINISH
from game.texts.db_messages import NAME_ERROR


def check_name_hero(name):
    """Проверка, что не дублируется имя."""
    with sl.connect('./horror_story.sqlite') as con:
        cur = con.cursor()

        cur.execute('''
        SELECT name
        FROM heroes
        ''')

        for result in cur:
            if result[0] == name:
                print(NAME_ERROR)
                return FAIL


def check_name_hero_tournament(name):
    """Проверка на наличие героя в БД."""
    with sl.connect('./horror_story.sqlite') as con:
        cur = con.cursor()

        cur.execute('''
        SELECT *
        FROM heroes
        ''')

        for result in cur:
            if result[1] == name:
                return FINISH
        return FAIL

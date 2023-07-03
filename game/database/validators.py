import sqlite3 as sl
from game.texts.actions import FAIL


def check_name_hero(name):
    with sl.connect('./horror_story.sqlite') as con:
        cur = con.cursor()

        cur.execute('''
        SELECT name
        FROM heroes
        ''')

        for result in cur:
            if result[0] == name:
                print('Такое имя уже есть!')
                return FAIL

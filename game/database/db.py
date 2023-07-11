import sqlite3 as sl


def create_tables():
    """Создание таблиц БД."""
    with sl.connect('./horror_story.sqlite') as con:
        cur = con.cursor()

        cur.executescript("""
        CREATE TABLE IF NOT EXISTS heroes(
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        health INTEGER,
        force INTEGER,
        dexterity INTEGER,
        magic INTEGER,
        speed INTEGER,
        protection INTEGER,
        experience INTEGER,
        nobility INTEGER,
        adventure INTEGER
        );

        CREATE TABLE IF NOT EXISTS weapons(
        id INTEGER PRIMARY KEY,
        name TEXT,
        material TEXT,
        impact_force INTEGER,
        injection INTEGER,
        shot_power INTEGER,
        magic_power INTEGER,
        class_weapon TEXT,
        ammunition INTEGER,
        long_shot INTEGER,
        durability INTEGER,
        hero_id INTEGER,
        FOREIGN KEY(hero_id) REFERENCES heroes(id)
        )
        """)

        con.commit()


def insert_hero(values):
    """Добавление героя."""
    with sl.connect('./horror_story.sqlite') as con:
        cur = con.cursor()

        cur.execute('''INSERT INTO heroes(name, health, force,
        dexterity, magic, speed, protection, experience,
        nobility, adventure) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', values)
        con.commit()


def insert_weapon(values):
    """Добавление оружия героя"""
    with sl.connect('./horror_story.sqlite') as con:
        cur = con.cursor()

        cur.execute('''INSERT INTO weapons(name, material, impact_force,
        injection, shot_power, magic_power, class_weapon,
        ammunition, long_shot, durability, hero_id)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', values)
        con.commit()


def return_hero_id(name):
    """Поиск ID героя по имени."""
    with sl.connect('./horror_story.sqlite') as con:
        cur = con.cursor()

        cur.execute('''
        SELECT id, name
        FROM heroes
        ''')

        for result in cur:
            if result[1] == name:
                return result[0]


def return_weapons_hero(hero_id):
    """Поиск оружия героя по его ID"""
    with sl.connect('./horror_story.sqlite') as con:
        cur = con.cursor()

        cur.execute('''
        SELECT *
        FROM weapons
        ''')

        weapons_list = []
        for result in cur:
            if result[11] == hero_id:
                weapons_list.append(result)
        return weapons_list


def return_id_weapon(name, hero_id):
    with sl.connect('./horror_story.sqlite') as con:
        cur = con.cursor()

        cur.execute('''
        SELECT id, name, hero_id
        FROM weapons
        ''')

        for result in cur:
            if result[1] == name and result[2] == hero_id:
                return result[0]


def delete_weapon_hero(weapon_id):
    with sl.connect('./horror_story.sqlite') as con:
        cur = con.cursor()

        cur.execute('''
        DELETE
        FROM weapons
        WHERE id=?''', (weapon_id,))
        con.commit()


def update_hero(values):
    with sl.connect('./horror_story.sqlite') as con:
        cur = con.cursor()

        cur.execute('''
        UPDATE heroes
        SET
        health = ?, force = ?,
        dexterity = ?, magic = ?, speed = ?
        WHERE id = ?
        ''', (values))

        con.commit()


def update_protection_hero(values):
    with sl.connect('./horror_story.sqlite') as con:
        cur = con.cursor()

        cur.execute('''
        UPDATE heroes
        SET
        protection = ?
        WHERE id = ?
        ''', (values))

        con.commit()

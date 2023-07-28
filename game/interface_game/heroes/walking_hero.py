import re

from game.enemies.random_actions import enemy_random_action
from game.texts.actions import FAIL, SHAME, STEPS


pattern = r'^[0-9]+$'


def walking_hero_enemy(enemy, max_health_enemy,
                       enemy_weapon, hero):
    """Двигаться к противнику."""
    if enemy.lenght == 1:
        print(STEPS)
        return
    if enemy.lenght > hero.speed:
        walking_hero = hero.speed
    else:
        walking_hero = enemy.lenght
    steps = input(f'''
Какое количество шагов вы хотите сделать.
Введите цифру от 0 до {walking_hero} ''')
    check = re.fullmatch(pattern, steps)
    if not check:
        fin = ''
        return fin
    if int(steps) > walking_hero or int(steps) < 0:
        fin = ''
        return fin
    distance = enemy.distance(int(steps))
    print(f'''
У вас получилось пройти {steps} шагов
Противник в {distance} шагах от вас.''')
    fin = enemy_random_action(enemy, enemy_weapon, hero,
                              enemy.lenght, max_health_enemy)
    return fin


def run_hero():
    """Убежать с поля боя."""
    print(SHAME)
    return FAIL

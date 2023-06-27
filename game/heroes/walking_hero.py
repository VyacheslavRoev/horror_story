from enemies.random_actions import enemy_random_action
from texts.actions import SHAME, STEPS, FINISH


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
    steps = int(input(f'''
Какое количество шагов вы хотите сделать.
Введите цифру от 0 до {walking_hero} '''))
    distance = enemy.distance(steps)
    print(f'''
У вас получилось пройти {steps} шагов
Противник в {distance} шагах от вас.''')
    fin = enemy_random_action(enemy, enemy_weapon, hero,
                              enemy.lenght, max_health_enemy)
    return fin


def run_hero():
    """Убежать с поля боя."""
    print(SHAME)
    return FINISH

from random import randint


def walking_enemy_hero(enemy):
    """Движение противника к герою."""
    if enemy.lenght > enemy.speed:
        walking_enemy = enemy.speed
    else:
        walking_enemy = enemy.lenght
    steps = randint(0, walking_enemy)
    distance = enemy.distance(steps)
    print(f'Противник делает {steps} шагов в вашу сторону.')
    print(f'Противник в {distance} шагах от вас.')

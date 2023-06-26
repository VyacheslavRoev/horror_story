from enemies.random_actions import enemy_random_action
from texts.actions import SHAME


def walking_hero_enemy(enemy, max_health_enemy,
                       enemy_weapon, hero):
    """Двигаться к противнику."""
    if enemy.lenght == 1:
        print('Противник в 1 шаге от вас. Вы не сможете подойти ближе!')
        return
    if enemy.lenght > hero.speed:
        walking_hero = hero.speed
    else:
        walking_hero = enemy.lenght
    steps = int(input(f'Какое количество шагов вы хотите сделать. '
                      f'Введите цифру от 0 до {walking_hero} '))
    distance = enemy.distance(steps)
    print(f'Противник в {distance} шагах от вас.')
    action = enemy_random_action(enemy, enemy_weapon, hero,
                                 enemy.lenght, max_health_enemy)
    return action


def run_hero():
    """Убежать с поля боя."""
    print(SHAME)
    return 2

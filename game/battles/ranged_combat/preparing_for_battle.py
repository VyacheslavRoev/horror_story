from heroes.inventary_hero import get_weapon
from heroes.walking_hero import run_hero, walking_hero_enemy
from texts.actions import INVENTARY_WEAPON_MESSAGE, COMMAND, FINISH, ERROR_LIST
from texts.attack_messages import RANGED_ATTACK
from random_number_func import random_phrase

from .hero_attack import attack_ranged_combat


def get_ranged_weapon(index, hero, enemy, enemy_weapon, max_health_enemy):
    """Подготовка к бою."""
    weapon = get_weapon(index)
    print(f'''
Вы выбрали {weapon}
{INVENTARY_WEAPON_MESSAGE}''')
    new_command = input()
    if new_command == '1':
        while new_command != '2':
            if enemy.health <= 0:
                return
            if hero.health <= 0:
                return
            if weapon.ammunition <= 0:
                return
            fin = ''
            attack_command = input(f'''
    {RANGED_ATTACK}
{COMMAND}''')
            if attack_command == '1':
                fin = attack_ranged_combat(weapon,
                                           hero, enemy,
                                           enemy_weapon, max_health_enemy)
                if fin == FINISH:
                    return fin
            if attack_command == '2':
                fin = walking_hero_enemy(enemy, max_health_enemy,
                                         enemy_weapon, hero)
                if fin == FINISH:
                    return fin
            if attack_command == '3':
                fin = run_hero()
                if fin == FINISH:
                    return fin
            if attack_command == '0':
                return
            else:
                if fin is not None or attack_command not in ['0', '1', '2',
                                                             '3']:
                    print(random_phrase(ERROR_LIST))

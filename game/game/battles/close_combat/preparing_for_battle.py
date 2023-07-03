from game.heroes.inventary_hero import get_weapon
from game.heroes.walking_hero import run_hero, walking_hero_enemy
from game.random_number_func import random_phrase
from game.texts.actions import (COMMAND, ERROR_LIST, FINISH,
                                INVENTARY_WEAPON_MESSAGE)
from game.texts.attack_messages import CLOSE_ATTACK

from .hero_attack import attack_close_combat


def get_close_weapon(index, hero, enemy, enemy_weapon, max_health_enemy):
    """Подготовка к бою."""
    weapon = get_weapon(index)
    print(f'''
Вы выбрали {weapon}
{INVENTARY_WEAPON_MESSAGE}''')
    new_command = input(COMMAND)
    if new_command == '1':
        while new_command != '2':
            if enemy.health <= 0:
                return
            if hero.health <= 0:
                return
            if weapon.durability <= 0:
                return
            fin = ''
            attack_command = input(f'''
    {CLOSE_ATTACK}
{COMMAND}''')
            if attack_command in ['1', '2']:
                fin = attack_close_combat(attack_command, weapon,
                                          hero, enemy,
                                          enemy_weapon, max_health_enemy)
                if fin == FINISH:
                    return fin
            if attack_command == '3':
                fin = walking_hero_enemy(enemy, max_health_enemy,
                                         enemy_weapon, hero)
                if fin == FINISH:
                    return fin
            if attack_command == '4':
                fin = run_hero()
                if fin == FINISH:
                    return fin
            if attack_command == '0':
                return
            else:
                if fin is not None or attack_command not in ['0', '1', '2',
                                                             '3', '4']:
                    print(random_phrase(ERROR_LIST))

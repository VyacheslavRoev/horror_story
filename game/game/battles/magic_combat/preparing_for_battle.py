from game.battles.magic_combat.hero_attack import attack_magic_combat
from game.heroes.inventary_hero import get_weapon
from game.heroes.walking_hero import run_hero, walking_hero_enemy
from game.random_number_func import random_phrase
from game.texts.actions import (COMMAND, ERROR_LIST, FINISH, FAIL,
                                INVENTARY_WEAPON_MESSAGE, MAGIC_HEALTH)
from game.texts.attack_messages import MAGIC_ATTACK


def get_magic_weapon(index, hero, enemy, enemy_weapon,
                     max_health_enemy, inventary):
    """Подготовка к бою."""
    weapon = get_weapon(index, inventary)
    if weapon is None:
        print('У вас нет этого оружия!')
        return
    print(f'''
Вы выбрали {weapon}
{INVENTARY_WEAPON_MESSAGE}''')
    new_command = input()
    if new_command == '1':
        while new_command != '2':
            fin = ''
            attack_command = input(f'''
    {MAGIC_ATTACK}
{COMMAND}''')
            if attack_command == '1':
                magic_health = input(MAGIC_HEALTH)
                fin = attack_magic_combat(weapon,
                                          hero, enemy,
                                          enemy_weapon,
                                          magic_health,
                                          max_health_enemy)
                if fin == FINISH:
                    return fin
            if attack_command == '2':
                fin = walking_hero_enemy(enemy, max_health_enemy,
                                         enemy_weapon, hero)
                if fin == FINISH:
                    return fin
                if fin == FAIL:
                    return fin
            if attack_command == '3':
                fin = run_hero()
                if fin == FAIL:
                    return fin
            if attack_command == '0':
                return
            else:
                if fin is not None or attack_command not in ['0', '1', '2',
                                                             '3']:
                    print(random_phrase(ERROR_LIST))

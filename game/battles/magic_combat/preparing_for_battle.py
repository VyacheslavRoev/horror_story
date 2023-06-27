from battles.magic_combat.hero_attack import attack_magic_combat
from heroes.inventary_hero import get_weapon
from heroes.walking_hero import run_hero, walking_hero_enemy
from texts.actions import (COMMAND, FINISH, INVENTARY_WEAPON_MESSAGE,
                           MAGIC_HEALTH)
from texts.attack_messages import MAGIC_ATTACK


def get_magic_weapon(index, hero, enemy, enemy_weapon, max_health_enemy):
    """Подготовка к бою."""
    weapon = get_weapon(index)
    print(f'''
Вы выбрали {weapon}
{INVENTARY_WEAPON_MESSAGE}''')
    new_command = int(input())
    if new_command == 1:
        while new_command != 2:
            if enemy.health <= 0:
                return
            if hero.health <= 0:
                return
            attack_command = int(input(f'''
    {MAGIC_ATTACK}
    {COMMAND}'''))
            if attack_command == 1:
                magic_health = int(input(MAGIC_HEALTH))
                fin = attack_magic_combat(weapon,
                                          hero, enemy,
                                          enemy_weapon,
                                          magic_health,
                                          max_health_enemy)
            elif attack_command == 2:
                fin = walking_hero_enemy(enemy, max_health_enemy,
                                         enemy_weapon, hero)
            elif attack_command == 3:
                fin = run_hero()
            elif attack_command == 0:
                return
            if fin == FINISH:
                return fin

from heroes.inventary_hero import get_weapon
from heroes.walking_hero import run_hero, walking_hero_enemy
from .hero_attack import attack_close_combat
from texts.actions import INVENTARY_WEAPON_MESSAGE, COMMAND, FINISH
from texts.attack_messages import CLOSE_ATTACK


def get_close_weapon(index, hero, enemy, enemy_weapon, max_health_enemy):
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
            if weapon.durability <= 0:
                return
            attack_command = int(input(f'''
    {CLOSE_ATTACK}
    {COMMAND}'''))
            if attack_command == 1 or attack_command == 2:
                fin = attack_close_combat(attack_command, weapon,
                                          hero, enemy,
                                          enemy_weapon, max_health_enemy)
            elif attack_command == 3:
                fin = walking_hero_enemy(enemy, max_health_enemy,
                                         enemy_weapon, hero)
            elif attack_command == 4:
                fin = run_hero()
            elif attack_command == 0:
                return
            if fin == FINISH:
                return fin

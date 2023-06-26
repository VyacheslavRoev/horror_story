from heroes.inventary_hero import get_weapon
from heroes.walking_hero import run_hero, walking_hero_enemy
from texts.actions import INVENTARY_WEAPON_MESSAGE
from texts.attack_messages import RANGED_ATTACK

from .hero_attack import attack_ranged_combat


def get_ranged_weapon(index, hero, enemy, enemy_weapon, max_health_enemy):
    """Подготовка к бою."""
    weapon = get_weapon(index)
    print(f'Вы выбрали {weapon}')
    print(INVENTARY_WEAPON_MESSAGE)
    new_command = int(input())
    if new_command == 1:
        while new_command != 2:
            if enemy.health <= 0:
                return
            if hero.health <= 0:
                return
            if weapon.ammunition <= 0:
                return
            attack_command = int(input(RANGED_ATTACK))
            if attack_command == 1:
                attack = attack_ranged_combat(weapon,
                                              hero, enemy,
                                              enemy_weapon, max_health_enemy)
            elif attack_command == 2:
                attack = walking_hero_enemy(enemy, max_health_enemy,
                                            enemy_weapon, hero)
            elif attack_command == 3:
                attack = run_hero()
            elif attack_command == 0:
                return
            if attack == 2:
                return attack

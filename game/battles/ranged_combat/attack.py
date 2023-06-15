from heroes.inventary_hero import get_weapon
from texts.actions import INVENTARY_WEAPON_MESSAGE
from texts.attack_messages import (DAMAGE, ENEMY_FAIL, ENEMY_MAX_DAMAGE,
                                   YOU_FAIL, YOU_MAX_DAMAGE, RANGED_ATTACK)
from battles.close_combat.attack import enemy_attack_close_combat
from heroes.walking_hero import walking_hero_enemy, run_hero


def enemy_attack_ranged_combat(enemy, weapon, hero):
    """Атака противником оружием дальнего боя."""
    effect = enemy.ranged_dealing_damage(weapon.shot_power,
                                         weapon.long_shot, enemy.lenght)
    print(f'{enemy.name} пытается выстрелить.')
    if effect == 0:
        print(weapon.shot())
        print(f'{enemy.name} {ENEMY_FAIL}')
    elif effect == ((enemy.force + enemy.dexterity +
                     weapon.shot_power - enemy.lenght) * 10):
        print(weapon.shot())
        print(ENEMY_MAX_DAMAGE)
        print(hero.taking_damage(effect))
        if hero.health <= 0:
            return
        enemy_attack_ranged_combat(enemy, weapon, hero)
    else:
        print(weapon.shot())
        print(DAMAGE)
        print(hero.taking_damage(effect))


def attack_ranged_combat(weapon, hero, enemy, weapon_enemy):
    """Атака оружием дальнего боя."""
    effect = hero.ranged_dealing_damage(weapon.shot_power,
                                        weapon.long_shot, enemy.lenght)
    if effect == 0:
        print(weapon.shot())
        print(YOU_FAIL)
        if weapon_enemy.class_weapon == 'Ближний бой':
            enemy_attack_close_combat(enemy, weapon_enemy, hero)
        elif weapon_enemy.class_weapon == 'Дальний бой':
            enemy_attack_ranged_combat(enemy, weapon_enemy, hero)
    elif effect == ((hero.force + hero.dexterity +
                     weapon.shot_power - enemy.lenght) * 10):
        print(weapon.shot())
        print(YOU_MAX_DAMAGE)
        print(enemy.taking_damage(effect))
    else:
        print(weapon.shot())
        print(DAMAGE)
        print(enemy.taking_damage(effect))
        if enemy.health <= 0:
            return
        if weapon_enemy.class_weapon == 'Ближний бой':
            enemy_attack_close_combat(enemy, weapon_enemy, hero)
        elif weapon_enemy.class_weapon == 'Дальний бой':
            enemy_attack_ranged_combat(enemy, weapon_enemy, hero)


def get_ranged_weapon(index, hero, enemy, enemy_weapon):
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
                attack_ranged_combat(weapon,
                                     hero, enemy,
                                     enemy_weapon)
            elif attack_command == 2:
                walking_hero_enemy()
            elif attack_command == 3:
                run_hero()
            elif attack_command == 0:
                return

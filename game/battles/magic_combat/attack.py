from random import randint
from heroes.inventary_hero import get_weapon
from battles.close_combat.attack import enemy_attack_close_combat
from battles.ranged_combat.attack import enemy_attack_ranged_combat
from texts.actions import (INVENTARY_WEAPON_MESSAGE, MAGIC, WEAPON, WHAT_DOING,
                           YES, MAGIC_HEALTH)
from texts.attack_messages import (DAMAGE, ENEMY_FAIL, ENEMY_MAX_DAMAGE,
                                   YOU_FAIL, YOU_MAX_DAMAGE)


def enemy_attack_magic_combat(enemy, weapon, hero):
    """Атака противником магическим оружием."""
    magic_health = randint(0, enemy.health - 1)
    effect = enemy.magic_dealing_damage(weapon.magic_power,
                                        weapon.long_shot,
                                        enemy.lenght,
                                        magic_health)
    print(f'{enemy.name} пытается колдовать.')
    if effect == 0:
        print(weapon.mythical_strike())
        print(f'{enemy.name} {ENEMY_FAIL}')
    elif effect == (magic_health * 2) + hero.magic + weapon.magic_power:
        print(weapon.mythical_strike())
        print(ENEMY_MAX_DAMAGE)
        print(hero.magic_taking_damage(effect))
        if hero.health < 0:
            return
        enemy_attack_magic_combat(enemy, weapon, hero)
    else:
        print(weapon.mythical_strike())
        print(DAMAGE)
        print(hero.magic_taking_damage(effect))


def attack_magic_combat(weapon, hero, enemy, weapon_enemy, magic_health):
    """Атака магическим оружием."""
    if magic_health >= hero.health:
        print('Вы умрёте, если сделаете это!')
        return
    effect = hero.magic_dealing_damage(weapon.magic_power,
                                       weapon.long_shot,
                                       enemy.lenght,
                                       magic_health)
    if effect == 0:
        print(weapon.mythical_strike())
        print(YOU_FAIL)
        if weapon_enemy.class_weapon == 'Ближний бой':
            enemy_attack_close_combat(enemy, weapon_enemy, hero)
        elif weapon_enemy.class_weapon == 'Дальний бой':
            enemy_attack_ranged_combat(enemy, weapon_enemy, hero)
        elif weapon_enemy.class_weapon == 'Магическое оружие':
            enemy_attack_magic_combat(enemy, weapon_enemy, hero)
    elif effect == (magic_health * 3) + hero.magic + weapon.magic_power:
        print(weapon.mythical_strike())
        print(YOU_MAX_DAMAGE)
        print(enemy.magic_taking_damage(effect))
    else:
        print(weapon.mythical_strike())
        print(DAMAGE)
        print(enemy.magic_taking_damage(effect))
        if enemy.health <= 0:
            return
        if weapon_enemy.class_weapon == 'Ближний бой':
            enemy_attack_close_combat(enemy, weapon_enemy, hero)
        elif weapon_enemy.class_weapon == 'Дальний бой':
            enemy_attack_ranged_combat(enemy, weapon_enemy, hero)
        elif weapon_enemy.class_weapon == 'Магическое оружие':
            enemy_attack_magic_combat(enemy, weapon_enemy, hero)


def get_magic_weapon(index, hero, enemy, enemy_weapon):
    """Подготовка к бою."""
    weapon = get_weapon(index)
    print(f'Вы выбрали {weapon}')
    print(INVENTARY_WEAPON_MESSAGE)
    new_command = input()
    if new_command == YES:
        while new_command != WEAPON:
            if enemy.health <= 0:
                return
            if hero.health <= 0:
                return
            new_command = input(WHAT_DOING)
            if new_command == MAGIC:
                magic_health = int(input(MAGIC_HEALTH))
                attack_magic_combat(weapon,
                                    hero, enemy,
                                    enemy_weapon, magic_health)

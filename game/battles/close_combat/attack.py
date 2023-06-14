from texts.actions import HACK, INVENTARY_WEAPON_MESSAGE, PRICK, WEAPON, YES
from texts.attack_messages import (DAMAGE, ENEMY_FAIL, ENEMY_MAX_DAMAGE,
                                   HACK_OR_PRICK, YOU_FAIL, YOU_MAX_DAMAGE)
from heroes.inventary_hero import get_weapon


def enemy_attack_close_combat(enemy, weapon, hero):
    """Атака противником оружием ближнего боя."""
    effect = enemy.close_dealing_damage(weapon.impact_force)
    print(f'{enemy.name} пытается нанести удар.')
    if effect == 0:
        print(f'{enemy.name} {ENEMY_FAIL}')
    elif effect == (enemy.force + weapon.impact_force) * 10:
        print(weapon.slashing_blow())
        print(ENEMY_MAX_DAMAGE)
        print(hero.taking_damage(effect))
        if hero.health <= 0:
            return
        enemy_attack_close_combat(enemy, weapon, hero)
    else:
        print(weapon.slashing_blow())
        print(DAMAGE)
        print(hero.taking_damage(effect))


def attack_close_combat(attack, weapon, hero, enemy, weapon_enemy):
    """Атака оружием ближнего боя."""
    if attack == HACK:
        effect = hero.close_dealing_damage(weapon.impact_force)
        if effect == 0:
            print(YOU_FAIL)
            enemy_attack_close_combat(enemy, weapon_enemy, hero)
        elif effect == (hero.force + weapon.impact_force) * 10:
            print(weapon.slashing_blow())
            print(YOU_MAX_DAMAGE)
            print(enemy.taking_damage(effect))
        else:
            print(weapon.slashing_blow())
            print(DAMAGE)
            print(enemy.taking_damage(effect))
            if enemy.health <= 0:
                return
            enemy_attack_close_combat(enemy, weapon_enemy, hero)
    elif attack == PRICK:
        effect = hero.close_dealing_damage(weapon.injection)
        if effect == 0:
            print(YOU_FAIL)
            enemy_attack_close_combat(enemy, weapon_enemy, hero)
        elif effect == (hero.force + weapon.injection) * 10:
            print(weapon.stabbing_blow())
            print(YOU_MAX_DAMAGE)
            print(enemy.taking_damage(effect))
        else:
            print(weapon.stabbing_blow())
            print(DAMAGE)
            print(enemy.taking_damage(effect))
            if enemy.health <= 0:
                return
            enemy_attack_close_combat(enemy, weapon_enemy, hero)


def get_close_weapon(index, hero, enemy, enemy_weapon):
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
            if weapon.durability <= 0:
                return
            new_command = input(HACK_OR_PRICK)
            if new_command == HACK or new_command == PRICK:
                attack_close_combat(new_command, weapon,
                                    hero, enemy,
                                    enemy_weapon)

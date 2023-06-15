from texts.actions import INVENTARY_WEAPON_MESSAGE
from texts.attack_messages import (DAMAGE, ENEMY_FAIL, ENEMY_MAX_DAMAGE,
                                   CLOSE_ATTACK, YOU_FAIL, YOU_MAX_DAMAGE)
from heroes.inventary_hero import get_weapon
from heroes.walking_hero import walking_hero_enemy, run_hero


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
    if weapon.long_shot < enemy.lenght:
        print('Противник слишком далеко!')
        return
    if attack == 1:
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
    elif attack == 2:
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
    new_command = int(input())
    if new_command == 1:
        while new_command != 2:
            if enemy.health <= 0:
                return
            if hero.health <= 0:
                return
            if weapon.durability <= 0:
                return
            attack_command = int(input(CLOSE_ATTACK))
            if attack_command == 1 or attack_command == 2:
                attack_close_combat(attack_command, weapon,
                                    hero, enemy,
                                    enemy_weapon)
            elif attack_command == 3:
                walking_hero_enemy()
            elif attack_command == 4:
                run_hero()
            elif attack_command == 0:
                return

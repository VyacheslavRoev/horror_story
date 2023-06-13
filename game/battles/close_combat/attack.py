from texts.actions import HACK, PRICK
from texts.attack_messages import (DAMAGE, ENEMY_FAIL, ENEMY_MAX_DAMAGE,
                                   YOU_FAIL, YOU_MAX_DAMAGE)


def enemy_attack_close_combat(enemy, weapon, hero):
    """Атака противником оружием ближнего боя."""
    effect = enemy.dealing_damage(weapon.impact_force)
    print(f'{enemy.name} пытается нанести удар.')
    if effect == 0:
        print(f'{enemy.name} {ENEMY_FAIL}')
    elif effect == (enemy.force + weapon.impact_force) * 10:
        print(weapon.slashing_blow())
        print(ENEMY_MAX_DAMAGE)
        print(hero.taking_damage(effect))
        if hero.health < 0:
            return
        enemy_attack_close_combat(enemy, weapon, hero)
    else:
        print(weapon.slashing_blow())
        print(DAMAGE)
        print(hero.taking_damage(effect))


def attack_close_combat(attack, weapon, hero, enemy, weapon_enemy):
    """Атака оружием ближнего боя."""
    if attack == HACK:
        effect = hero.dealing_damage(weapon.impact_force)
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
            if enemy.health < 0:
                return
            enemy_attack_close_combat(enemy, weapon_enemy, hero)
    elif attack == PRICK:
        effect = hero.dealing_damage(weapon.injection)
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
            if enemy.health < 0:
                return
            enemy_attack_close_combat(enemy, weapon_enemy, hero)

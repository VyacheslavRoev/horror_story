from enemies.random_actions import enemy_random_action
from texts.attack_messages import (DAMAGE, YOU_FAIL,
                                   YOU_MAX_DAMAGE)


def attack_close_combat(attack, weapon, hero, enemy,
                        weapon_enemy, max_health_enemy):
    """Атака оружием ближнего боя."""
    if weapon.long_shot < enemy.lenght:
        print('Противник слишком далеко!')
        return
    if attack == 1:
        effect = hero.close_dealing_damage(weapon.impact_force)
        if effect == 0:
            print(YOU_FAIL)
            action = enemy_random_action(enemy, weapon_enemy, hero,
                                         enemy.lenght, max_health_enemy)
            return action
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
            action = enemy_random_action(enemy, weapon_enemy, hero,
                                         enemy.lenght, max_health_enemy)
            return action
        
    elif attack == 2:
        effect = hero.close_dealing_damage(weapon.injection)
        if effect == 0:
            print(YOU_FAIL)
            action = enemy_random_action(enemy, weapon_enemy, hero,
                                         enemy.lenght, max_health_enemy)
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
            action = enemy_random_action(enemy, weapon_enemy, hero,
                                         enemy.lenght, max_health_enemy)
        return action

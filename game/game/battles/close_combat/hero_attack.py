from game.enemies.random_actions import enemy_random_action
from game.texts.actions import FAR_AWAY, FINISH
from game.texts.attack_messages import DAMAGE, YOU_FAIL, YOU_MAX_DAMAGE


def attack_close_combat(attack, weapon, hero, enemy,
                        weapon_enemy, max_health_enemy):
    """Атака оружием ближнего боя."""
    if weapon.long_shot < enemy.lenght:
        print(FAR_AWAY)
        return
    if attack == '1':
        effect = hero.close_dealing_damage(weapon.impact_force)
        if effect == 0:
            print(YOU_FAIL)
            fin = enemy_random_action(enemy, weapon_enemy, hero,
                                      enemy.lenght, max_health_enemy)
            return fin
        elif effect == (hero.force + weapon.impact_force) * 10:
            print(weapon.slashing_blow())
            print(YOU_MAX_DAMAGE)
            print(enemy.taking_damage(effect))
            if enemy.health <= 0:
                print(hero.gaining_experience(enemy.experience))
                fin = FINISH
                return fin
        else:
            print(weapon.slashing_blow())
            print(DAMAGE)
            print(enemy.taking_damage(effect))
            if enemy.health <= 0:
                print(hero.gaining_experience(enemy.experience))
                fin = FINISH
                return fin
            fin = enemy_random_action(enemy, weapon_enemy, hero,
                                      enemy.lenght, max_health_enemy)
            return fin

    elif attack == '2':
        effect = hero.close_dealing_damage(weapon.injection)
        if effect == 0:
            print(YOU_FAIL)
            fin = enemy_random_action(enemy, weapon_enemy, hero,
                                      enemy.lenght, max_health_enemy)
            return fin
        elif effect == (hero.force + weapon.injection) * 10:
            print(weapon.stabbing_blow())
            print(YOU_MAX_DAMAGE)
            print(enemy.taking_damage(effect))
            if enemy.health <= 0:
                print(hero.gaining_experience(enemy.experience))
                fin = FINISH
                return fin
        else:
            print(weapon.stabbing_blow())
            print(DAMAGE)
            print(enemy.taking_damage(effect))
            if enemy.health <= 0:
                print(hero.gaining_experience(enemy.experience))
                fin = FINISH
                return fin
            fin = enemy_random_action(enemy, weapon_enemy, hero,
                                      enemy.lenght, max_health_enemy)
            return fin

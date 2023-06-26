from enemies.random_actions import enemy_random_action
from texts.attack_messages import DAMAGE, YOU_FAIL, YOU_MAX_DAMAGE


def attack_ranged_combat(weapon, hero, enemy, weapon_enemy, max_health_enemy):
    """Атака оружием дальнего боя."""
    if weapon.long_shot < enemy.lenght:
        print('Противник слишком далеко!')
        return
    effect = hero.ranged_dealing_damage(weapon.shot_power,
                                        weapon.long_shot, enemy.lenght)
    if effect == 0:
        print(weapon.shot())
        print(YOU_FAIL)
        action = enemy_random_action(enemy, weapon_enemy, hero,
                                     enemy.lenght, max_health_enemy)
        return action
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
        action = enemy_random_action(enemy, weapon_enemy, hero,
                                     enemy.lenght, max_health_enemy)
        return action

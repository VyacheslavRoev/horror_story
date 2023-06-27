from enemies.random_actions import enemy_random_action
from texts.attack_messages import DAMAGE, YOU_FAIL, YOU_MAX_DAMAGE
from texts.actions import FAR_AWAY, FINISH, DEAD


def attack_magic_combat(weapon, hero, enemy, weapon_enemy,
                        magic_health, max_health_enemy):
    """Атака магическим оружием."""
    if magic_health >= hero.health:
        print(DEAD)
        return
    if weapon.long_shot < enemy.lenght:
        print(FAR_AWAY)
        return
    effect = hero.magic_dealing_damage(weapon.magic_power,
                                       weapon.long_shot,
                                       enemy.lenght,
                                       magic_health)
    if effect == 0:
        print(weapon.mythical_strike())
        print(YOU_FAIL)
        fin = enemy_random_action(enemy, weapon_enemy, hero,
                                  enemy.lenght, max_health_enemy)
        return fin
    elif effect == (magic_health * 3) + hero.magic + weapon.magic_power:
        print(weapon.mythical_strike())
        print(YOU_MAX_DAMAGE)
        print(enemy.magic_taking_damage(effect))
        if enemy.health <= 0:
            fin = FINISH
            return fin
    else:
        print(weapon.mythical_strike())
        print(DAMAGE)
        print(enemy.magic_taking_damage(effect))
        if enemy.health <= 0:
            return
        if enemy.health <= 0:
            fin = FINISH
            return fin
        fin = enemy_random_action(enemy, weapon_enemy, hero,
                                  enemy.lenght, max_health_enemy)
        return fin

import re

from game.enemies.random_actions import enemy_random_action
from game.texts.actions import DEAD, FAR_AWAY, FINISH
from game.texts.attack_messages import DAMAGE, YOU_FAIL, YOU_MAX_DAMAGE

pattern = r'^[0-9]+$'


def attack_magic_combat(weapon, hero, enemy, weapon_enemy,
                        magic_health, max_health_enemy):
    """Атака магическим оружием."""
    check = re.fullmatch(pattern, magic_health)
    if not check:
        fin = ''
        return fin
    if int(magic_health) < 0:
        fin = ''
        return fin
    if int(magic_health) >= hero.health:
        print(DEAD)
        return
    if weapon.long_shot < enemy.lenght:
        print(FAR_AWAY)
        return
    effect = hero.magic_dealing_damage(weapon.magic_power,
                                       weapon.long_shot,
                                       enemy.lenght,
                                       int(magic_health))
    if effect == 0:
        print(weapon.mythical_strike())
        print(YOU_FAIL)
        fin = enemy_random_action(enemy, weapon_enemy, hero,
                                  enemy.lenght, max_health_enemy)
        return fin
    elif effect == (int(magic_health) * 3) + hero.magic + weapon.magic_power:
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

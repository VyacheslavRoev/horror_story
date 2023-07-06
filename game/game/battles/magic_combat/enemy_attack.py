from random import randint
from game.texts.actions import FAIL
from game.texts.attack_messages import DAMAGE, ENEMY_FAIL, ENEMY_MAX_DAMAGE


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
            fin = FAIL
            return fin
        fin = enemy_attack_magic_combat(enemy, weapon, hero)
        if fin == FAIL:
            return fin
    else:
        print(weapon.mythical_strike())
        print(DAMAGE)
        print(hero.magic_taking_damage(effect))
        if hero.health <= 0:
            fin = FAIL
            return fin
